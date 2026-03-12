# Quantum Observable Universe

A LaTeX mathematics paper exploring the Quantum Observable Universe (QOU),
quantum torsion, and related topics.

## Structure

| File | Description |
|------|-------------|
| `main.tex` | Top-level document — includes all chapters |
| `chapters/quantum-observable-universe.tex` | Chapter 1: Quantum Observable Universe |
| `chapters/lifting-of-quantum-torsion.tex` | Chapter 2: Lifting of Quantum Torsion |
| `chapters/interpretations.tex` | Chapter 3: Interpretations |
| `chapters/experimental-evidence.tex` | Chapter 4: Experimental Evidence |
| `chapters/speculations.tex` | Chapter 5: Speculations |
| `references.bib` | BibTeX bibliography |

## Building

Compile with `pdflatex` (run twice to resolve cross-references):

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or use `latexmk`:

```bash
latexmk -pdf main.tex
```

## License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided
appropriate credit is given, a link to the license is provided, and any
changes made are indicated.
