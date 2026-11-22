# QOU formalization blueprint

`src/content.tex` maps each theorem-like object in the manuscript to its Lean 4
declaration via `\lean{}`, records dependency edges via `\uses{}`, and marks
sorry-free objects with `\leanok`. `web.tex` is the plasTeX/HTML entry point,
`print.tex` the print one, and both `\input{preamble}` and `\input{content}`.

## Where this came from

It was in `litlfred/folio-assistant` at `cat-harness/blueprint/`, put there by
the 2026-09-20 repo partition, which moved a set of folio artefacts into the
platform repo's stub. That repository's `AGENTS.md` says the platform holds no
folio content, so the directory is being removed there
([folio-assistant#1223](https://github.com/litlfred/folio-assistant/issues/1223)).
It had no copy here on `main` or on `gh-pages`, so it is imported rather than
deleted. Issue #7452.

**Its relative paths resolve here and did not there.** `web.tex` and `print.tex`
both `\bibliography{../../references}`, which from `blueprint/src/` is the
repository root — this repository has `references.bib` there and
folio-assistant has none. The files were written for this checkout.

## How current it is, measured 2026-09-24 at import

`content.tex` carries 128 distinct `\lean{QOU.*}` references. Matched against
this repository's 3,971 `.lean` files by declaration name — `theorem|lemma|def|
abbrev|structure|inductive|instance|class` followed by the bare name, because
Lean writes `namespace QOU` and then the unqualified declaration:

```
resolve to a live declaration:   111 / 128   (87%)
do not resolve:                   17
```

**Read 111 as an upper bound, not as a verification.** It is a name match: two
declarations sharing a name in different namespaces both count. An earlier pass
searched for the fully-qualified string `QOU.Boson` and reported 33/128, which
was wrong for the reason above — the qualified form never appears in Lean
source. Neither number is a proof that a reference binds to the object the
blueprint means; that would need the elaborator.

The 17 that do not resolve by name:

```
QOU.Brings.coral_elliptic                 QOU.KnotTheory.PlanarDiagram
QOU.BringsSurface.mi_sw_abelianisation    QOU.MassDerivation.topological_mass_formula
QOU.Calculations.muon_is_figure_eight     QOU.PAdicQuantumGroups.FiniteFieldRealisation
QOU.DescartesUniverse.DescartesCondition  QOU.PAdicQuantumGroups.PAdicRealisation
QOU.DescartesUniverse.descartes_theorem   QOU.PathIntegrals.SU2Generators
QOU.InstantonConnection.IsIrreducible     QOU.QuantumUniverse.gaugeGroup
QOU.KnotRegistry.KnotEntry.volumeValue    QOU.Torsion.euler_char_stability
                                          QOU.Torsion.jet_prolongation
```

## Not decided at import

Whether `blueprint/` is the right path here, whether the 17 should be fixed or
dropped, and whether CI should build this. The import is only about not losing
the file; nothing here is wired to a build.
