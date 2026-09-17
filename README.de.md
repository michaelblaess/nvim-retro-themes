# nvim-retro-themes

<p align="center">
  <img src="docs/flags/gb.svg" height="13" alt=""> <a href="README.md">English</a> ·
  <img src="docs/flags/de.svg" height="13" alt=""> <b>Deutsch</b>
</p>

---

36 dunkle Farbschemata für Neovim, gebaut aus den Retro-Paletten von
[textual-themes](https://github.com/michaelblaess/textual-themes) und auf das Lesen von Quelltext
abgestimmt.

Die Farben sind nicht 1:1 übernommen. Eine Palette für eine TUI hat kleine Textfelder, ein Editor
ist eine einzige große Textfläche. Deshalb wird hier jede Farbe geprüft und angehoben, bis sie
lesbar ist, und Syntaxfarben, die sich zu ähnlich sähen, werden auseinandergezogen.

## Einbinden

Mit `vim.pack` unter Neovim 0.12:

```lua
vim.pack.add({ "https://github.com/michaelblaess/nvim-retro-themes" })
vim.cmd.colorscheme("retro-synthwave")
```

Zum Ausprobieren ohne Installation:

```
nvim --cmd "set rtp+=/pfad/zu/nvim-retro-themes" datei.cs
:colorscheme retro-boing
```

## Was die Schemata abdecken

Editorfläche, Fenster, Popup-Menü, Statuszeile, Auswahl, Suche, Faltungen und Diffs. Die
klassischen Syntaxgruppen und die Treesitter-Captures. Diagnosen. Dazu die Plugins aus meiner
Konfiguration: render-markdown.nvim, mini.icons, mini.files, mini.pick und mini.clue. Und die
Terminal-Farben 0 bis 15.

## Die Regeln hinter den Farben

- **Lesbarkeit zuerst.** Text und Syntax erreichen auf jeder Fläche, auf der sie vorkommen,
  mindestens 4,5:1, Zeilennummern und Rahmen mindestens 3:1. Farbton und Sättigung bleiben, das
  Theme behält seinen Charakter.
- **Ein zu heller Hintergrund wird abgedunkelt.** Manche Paletten sind für einen ganzen Bildschirm
  Text zu hell. Der Hintergrund wird abgedunkelt, bis der Fließtext 8:1 erreicht. Darüber ist dann
  Platz für sechs Syntaxfarben.
- **Syntaxfarben bleiben unterscheidbar.** Wo eine Palette eine Farbe doppelt verwendet, greift
  der nächste Kandidat, dann eine Verschiebung der Helligkeit, dann eine des Farbtons. Zwei
  Syntaxfarben liegen immer mindestens 22 in CIE76 auseinander.

Jede Regel deckt ein Test über alle 36 Themes ab.

## Erzeugen

```
uv run python -m nvim_retro_themes            # schreibt colors/
uv run python -m nvim_retro_themes --report   # nur die Kontrasttabelle
```

Die Paletten in `src/nvim_retro_themes/data/` sind ein Snapshot aus textual-themes 0.14.0.
`tools/snapshot_from_textual.py` holt ihn neu und überschreibt dabei Handänderungen.

Ein Theme fällt aus der Reihe: `christophorus` hat keine eigenen elf Grundfarben. Seine Rollen aus
web-themes sind von Hand darauf abgebildet, die Zuordnung steht in seiner Datendatei. Der Snapshot
schreibt nur die Themes, die er in textual-themes findet, diese Datei bleibt also stehen.

## Lizenz

Apache-2.0.
