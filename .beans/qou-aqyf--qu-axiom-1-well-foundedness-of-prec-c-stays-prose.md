---
# qou-aqyf
title: 'QU axiom 1: well-foundedness of prec_c stays prose-only (encoding would be vacuous)'
status: todo
type: task
created_at: 2026-08-14T19:52:57Z
updated_at: 2026-08-14T19:52:57Z
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
