# nvim-retro-themes

<p align="center">
  <img src="docs/flags/gb.svg" height="13" alt=""> <a href="README.md">English</a> ·
  <img src="docs/flags/de.svg" height="13" alt=""> <b>Deutsch</b>
</p>

---

<p align="center">
  <img src="docs/banner.jpg" alt="nvim-retro-themes - fünf Editorfenster im Terminal, jedes in einem anderen Retro-Farbschema" width="100%">
</p>

41 Farbschemata für Neovim, 36 dunkle und 5 helle, gebaut aus den Retro-Paletten von
[textual-themes](https://github.com/michaelblaess/textual-themes) und auf das Lesen von Quelltext
abgestimmt.

Die Farben sind nicht 1:1 übernommen. Eine Palette für eine TUI hat kleine Textfelder, ein Editor
ist eine einzige große Textfläche. Deshalb wird hier jede Farbe geprüft und angehoben, bis sie
lesbar ist, und Syntaxfarben, die sich zu ähnlich sähen, werden auseinandergezogen.

![retro-synthwave](docs/vorschau/retro-synthwave.png)

Oben Synthwave, darunter Classic Terminal und Clipper. **[Alle 41 Farbschemata ansehen](docs/vorschau.de.md)**

![retro-classic-terminal](docs/vorschau/retro-classic-terminal.png)

![retro-clipper](docs/vorschau/retro-clipper.png)

## Einbinden

Mit `vim.pack` unter Neovim 0.12:

```lua
vim.pack.add({ "https://github.com/michaelblaess/nvim-retro-themes" })
vim.cmd.colorscheme("retro-synthwave")
```

Zum Ausprobieren ohne Installation:

```
nvim --cmd "set rtp+=<pfad>/nvim-retro-themes" datei.cs
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
- **Die Fläche rückt vom Text ab.** Manche Paletten liegen für einen ganzen Bildschirm Text zu
  nah an ihrer eigenen Schrift. Ein dunkles Theme wird dann dunkler, ein helles heller, bis der
  Fließtext 8:1 erreicht. Darüber ist Platz für sechs Syntaxfarben. Nach oben ist bei 13:1
  Schluss, sonst landet die ausweichende Farbe fast bei Schwarz oder fast bei Weiß.
- **Syntaxfarben bleiben unterscheidbar.** Wo eine Palette eine Farbe doppelt verwendet, greift
  der nächste Kandidat, dann eine Verschiebung der Helligkeit, dann eine des Farbtons. Zwei
  Syntaxfarben liegen immer mindestens 22 in CIE76 auseinander.

Jede Regel deckt ein Test über alle 41 Themes ab.

## Erzeugen

```
uv run python -m nvim_retro_themes            # schreibt colors/
uv run python -m nvim_retro_themes --report   # nur die Kontrasttabelle
```

Die Paletten in `src/nvim_retro_themes/data/` sind ein Snapshot aus textual-themes 0.14.0.
`tools/snapshot_from_textual.py` holt ihn neu und überschreibt dabei Handänderungen.

Ein Theme ist von Hand gemacht: `christophorus` hat keine eigenen elf Grundfarben. Seine Rollen aus
web-themes sind von Hand darauf abgebildet, die Zuordnung steht in seiner Datendatei. Der Snapshot
schreibt nur die Themes, die er in textual-themes findet, diese Datei bleibt also stehen.

## Haftung

Die Farbschemata sind Freizeitarbeit und werden ohne Gewähr bereitgestellt, so wie es die
Apache-2.0-Lizenz beschreibt. Sie ändern die Darstellung im Editor, sonst nichts. Wer sie
einsetzt, tut das auf eigenes Risiko.

## Marken und Namen

Die Namen der Themes stammen aus [textual-themes](https://github.com/michaelblaess/textual-themes)
und sind Anspielungen auf Rechner, Oberflächen und Filme, die mir etwas bedeuten. Sie bezeichnen
Farbpaletten, nicht die Erzeugnisse anderer, und es besteht keine Verbindung zu deren Inhabern.
Genannte Marken gehören ihren jeweiligen Inhabern.

## Lizenz

Apache-2.0.
