---
# qou-fyqh
title: "W2: rationality — the division rings \U0001D507 i collapse to R (absolute irreducibility of Specht modules over char-0; Mathlib gives this only over alg-closed base)"
status: completed
type: task
priority: normal
created_at: 2026-08-15T14:41:43Z
updated_at: 2026-08-15T20:58:47Z
---


## CLOSED sorry-free — PR #5139

`QOU/BraidKnot/SpechtAbsolutelyIrreducible.lean`, `#print axioms` clean on all
five declarations.

**The rationality descent was not needed.** Both halves of the argument were
already in the corpus:

- `SpechtIrreducible.kapL_mem_line` — `κ_t` maps all of `M^μ` into the line
  `k·e_t` (James §4.6, the submodule-theorem core);
- `SpechtCrossKappa.kapL_polytabloid` — `κ_t e_t = |C_t|·e_t`.

Equivariance moves `θ` past `κ_t`, char-0 divides by `|C_t|`, and the single
`S_n`-orbit of polytabloids spreads the scalar over a spanning set. No character
theory, no descent from ℚ.

**Upgraded past Specht modules.** `simple_end_scalar` transports the result
along `SpechtClassification.specht_exhausts_irreducibles` (closed by a sibling
inside the last nine days) to give: *no simple `k[S_n]`-module admits a
non-scalar equivariant endomorphism*. That is item (a) of the
`SnWedderburnPartitionBridge` residual in module-theoretic form — a block's
`𝔇 i` is the commutant of the corresponding simple.

**Not claimed:** block-level `𝔇 i ≃ R` *inside a named `∏ Matrix` split*. That
needs the index↔partition labelling, which is W1.
