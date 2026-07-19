# Parabolic coset infra — the Bourbaki lifting lemma, conditional on exchange (2026-07-19)

**Bean:** `qou-bkcs`. **Lean:** [`QOU/Machinery/CoxeterParabolicCoset.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/CoxeterParabolicCoset.lean)
— sorry-free, `lean`-direct exit 0, first verify.

## The commissioned infra

The merged braid (#4059) and far-commutation (#4081) reductions rest on
per-pair coset data; the audited upstream gap is Mathlib's missing exchange
condition. This module isolates that gap as ONE precisely-stated hypothesis
and machine-checks the Bourbaki coset theory from it:

- **`RightExchangeProp`** — BB Thm 1.4.3 in reduced-word form (a right
  descent is realized by deleting one letter). Explicit hypothesis
  parameter — never an axiom, never a sorry.
- **Unconditional tier**: `parabolic` (W_J), the coset relation with its
  equivalence lemmas, `wordProd_mem_parabolic`, `exists_minRep`
  (well-ordering), `minRep_not_isRightDescent` (toggle + closure),
  `isReduced_of_isReduced_concat`.
- **`length_minRep_mul_wordProd`** — **the lifting lemma** (Bourbaki Lie
  IV §1 / BB Prop 2.4.4 core): for `u` minimal in its coset and `p` a
  reduced `J`-word, `ℓ(u·π p) = ℓ(u) + |p|`, conditional on
  `RightExchangeProp` alone. Classical two-case deletion argument:
  u-part deletion contradicts minimality; p-part deletion contradicts
  reducedness.

## What this changes

The `len_add` fields of the merged coset structures now reduce to
`RightExchangeProp` + reducedness of the finitely many alternating cell
words — the opaque per-pair hypotheses collapse toward one standard
textbook theorem. Follow-up tiers: the cell-equivalence assembly
(constructing `DihedralCosetStructure`/`CommutingCosetStructure` from this
lemma) and the exchange proof itself (reflection-cocycle route — the
genuine Mathlib-contribution project).

Honesty: nothing proves exchange here; every conditional theorem carries
it explicitly. Nothing wired; `1/(8π)` stays phase-4.
