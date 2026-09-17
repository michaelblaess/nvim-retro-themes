"""Erzeugt die Farbschemata und zeigt ihre Kontrastwerte.

Verwendung:
    uv run python -m nvim_retro_themes                 alle dunklen Themes nach colors/
    uv run python -m nvim_retro_themes boing synthwave nur diese Themes
    uv run python -m nvim_retro_themes --report        nur die Kontrasttabelle, nichts schreiben
"""

from __future__ import annotations

import sys
from pathlib import Path

from .color import contrast, delta_e
from .derive import Scheme, derive
from .palettes import Base, load_all
from .render import write

COLORS_DIR = Path(__file__).resolve().parents[2] / "colors"


def _report_line(scheme: Scheme) -> str:
    syntax = (scheme.keyword, scheme.function, scheme.string, scheme.number, scheme.type_, scheme.special)
    min_contrast = min(contrast(color, scheme.bg) for color in (*syntax, scheme.comment, scheme.fg))
    min_distance = min(delta_e(a, b) for i, a in enumerate(syntax) for b in syntax[i + 1 :])
    return (
        f"{scheme.name:<18} Kommentar {contrast(scheme.comment, scheme.bg):5.2f}  "
        f"Zeilennr {contrast(scheme.fg_faint, scheme.bg):5.2f}  "
        f"Auswahl {contrast(scheme.fg, scheme.bg_visual):5.2f}  "
        f"Syntax min {min_contrast:5.2f}  Abstand min {min_distance:5.1f}"
    )


def main(argv: list[str]) -> int:
    only = [arg for arg in argv if not arg.startswith("-")]
    report_only = "--report" in argv
    themes: list[Base] = [theme for theme in load_all() if not only or theme.name in only]
    unknown = set(only) - {theme.name for theme in themes}
    if unknown:
        print(f"Unbekannte Themes: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 1

    for base in themes:
        scheme = derive(base)
        print(_report_line(scheme))
        if not report_only:
            write(scheme, COLORS_DIR)
    if not report_only:
        print(f"{len(themes)} Farbschemata in {COLORS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
