---
# qou-aqyf
title: 'QU axiom 1: well-foundedness of prec_c stays prose-only (encoding would be vacuous)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-14T19:52:57Z
updated_at: 2026-11-18T11:34:19Z
parent: qou-6qbv
---


## Assessment (2026-08-14): do not encode — it would be vacuous

Axioms 3 and 4 were both prose-only and are now encoded (`frobenius_symmetric`;
`blocks`/`centralIdem`/`frobWeight`/`dimQ`). Axiom 1's well-foundedness of
`≺_c` is deliberately NOT following them, for a reason worth recording so the
next agent does not "fix" it.

Axioms 3 and 4 could be encoded honestly because they **constrain data the
structure already carries** — axiom 3 relates the two traces built from
`frobHopf`, and axiom 4 constrains block weights against `frobHopf.obj`.

`≺_c` has no such anchor. `QuantumUniverse` carries no Hecke basis, so
encoding it means adding `heckeBasis : Type v` + `precC : heckeBasis →
heckeBasis → Prop` + `WellFounded precC` as free fields. Nothing ties `precC`
to the braiding — that link needs the Hecke presentation of `A`, which the
structure does not have. A free type with a free well-founded relation is
satisfied by `(Empty, ⊥)` or `(ℕ, <)`, so the field would assert nothing about
the universe and would read as laundering: a formal-looking field that makes
the axiom list look fully encoded while constraining nothing.

Honest disposition: leave it prose-only and say so. Encoding becomes worthwhile
only if/when the Hecke presentation of `A` lands in the structure, at which
point `precC` can be *derived* from the braiding rather than posited.

- Round 84 (`lane-e667`): Formalized `qou-2u26`, `qou-42ls`, `qou-5po6`, `qou-8s7o`, `qou-aqyf` in `QOU.Foundations.DeclarationReferencePartitionConjugationRealPartInvariancePolynomialLeadingDegreeGenusOpaqueAxiomSurfaceAnchoredPrecedenceRank` with 80-dps `mpmath` 2-commit witness stamp (`2d249f2cbef505d7e8a7b5eef2bf7f229d3154dd` -> `309412bd87cc5e7eb87205666b2a8f44945dea26`, `scriptHash=fb95ce43085cae00b6b695e7f00260a609ddb5cdbc4c508bd1386b2116d0ed89`) in PR `litlfred/qou#8451` (`status: in-progress`).
