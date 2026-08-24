---
# qou-ko4g
title: 'Provable today: the SU(2) to SU(3) obstruction set, no new Mathlib needed'
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T14:13:36Z
updated_at: 2026-08-24T14:13:36Z
---

Five statements behind `qou-8p1g` ("tetraplectic reaches SU(2), not SU(3)")
that need **no** Mathlib infrastructure. Each turns a prose judgement into a
checkable invariant.

- [ ] **Reality obstruction.** A real matrix commutes with entrywise
  conjugation, so the rep it generates is self-conjugate. Under the *principal*
  embedding `SU(2) ↪ SU(3)` the **3** restricts to the adjoint of `su(2)`,
  which is real — hence `3 ≅ 3̄`. Colour needs `3 ≇ 3̄`. This is the decisive
  one: `qou-8p1g` argues "three Reeb fields is the *adjoint*, colour needs the
  *fundamental*" as a judgement; reality makes it mechanical.
- [ ] **SU(2) is not normal in SU(3)**, by concrete witness:
  `h = diag(i, −i, 1)` in the top-left block, `g` the 3-cycle permutation
  matrix (det +1, orthogonal); `(g h g⁻¹)₂₂ = −i ≠ 1`, so it leaves the block.
  Consequence: there is **no** short exact sequence `1 → SU(2) → SU(3) → Q → 1`,
  so "lift SU(2) to SU(3)" cannot be posed as an extension problem at all.
- [ ] **The order-120 trap.** `|Aut(Bring)| = |S₅| = 120 = |2I|` (binary
  icosahedral), but `Z(2I) = ℤ₂` and `Z(S₅) = 1`, so `2I ≇ S₅`. Any argument
  sliding from "Bring has order-120 symmetry" to "so `2I ⊂ SU(2)`" is invalid;
  the valid route is `A₅ ⊂ S₅`, which lifts to `2I`. Lean: the centre criterion
  plus `Z(S₅) = ⊥`; `2I` is not in Mathlib so its centre is narrative input,
  matching the `OctonionInvariantObstruction` house pattern.
- [ ] **G₂ dimension arithmetic.** `dim SU(3) + dim SO(4) = 8 + 6 = 14 = dim G₂`.
  Trivial to prove, worth pinning: it is the statement that G₂'s two homogeneous
  spaces `G₂/SU(3) = S⁶` and `G₂/SO(4)` (quaternionic Wolf space, dim 8) are
  complementary. **The corpus has `S⁶ = G₂/SU(3)` but no mention of
  `G₂/SO(4)` anywhere** — so the tetraplectic SU(2) and colour SU(3) have never
  been put in the same frame, and G₂ is that frame.
- [ ] **Abstract exact-triangle vanishing lemma.** If the correction term in a
  three-term exact sequence vanishes, the connecting map is an isomorphism.
  Pure homological algebra (`ShortComplex.Exact`); this is Seidel's bookkeeping
  **without** the Floer theory, and it is where filtration / jet-order / Gröbner
  degree bookkeeping would hang.

Sibling beans: `qou-fngs` (fix vacuous), `qou-8p1g` (the verdict these support).
