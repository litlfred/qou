/-
Copyright (c) 2026 litlfred. All rights reserved.

# Berezinian cross-term parity — the adjoint-scaled obstruction and its complement

Formalize-first structural brick for the super-DM / Berezinian `c₃`-mixing wall
(`qCubicGradedSplit`, bean `qou-jqof`/`qou-bgjc`, PR #4140, off-`main`). This
extends `BerezinianSelfAdjointCrossTerm` (#4421), which proved the *graded-
self-adjoint* cross-term `t = B·D⁻¹·C` with `C = −σB` is bar-EVEN, so a bar-ODD
`c₃` needs **non-self-adjoint** (independent) off-blocks.

Three sharper facts, all sorry-free over a generic `CommRing` with an abstract bar
involution `σ`:

1. **The obstruction is not special to the sign `−1`.** `crossTerm_bar_even_of_
   adjoint_scaled`: if `C = k·σB` for **any bar-even** scalar `k` (`σk = k`) and
   `Dinv` bar-even, then `t = B·Dinv·C` is bar-EVEN. #4421's `C = −σB` is the
   `k = −1` instance (`theorem selfadjoint_is_adjoint_scaled`). So the whole
   *adjoint-scaled* family — not just the self-adjoint sign — is barred from
   carrying a bar-odd `c₃`.

2. **The complementary non-self-adjoint route is realizable, and its structure is
   exactly the `OddDecayWeightParity` `g·γ` model.** `crossTerm_bar_odd_of_barEven_
   barOdd_blocks`: a **bar-even** `B` (`σB = B`) times a **bar-odd** `C`
   (`σC = −C`), dressed by bar-even `Dinv`, gives a genuinely bar-ODD cross-term
   `σt = −t`. Here `g = B·Dinv` is the bar-even dressing and `γ = C` the bar-odd
   weight — the `OddDecayWeightParity` factorization, now *derived* as the generic
   non-self-adjoint carrier rather than assumed.

3. **The two routes are genuinely disjoint (off 2-torsion).** `barOdd_blocks_
   not_adjoint_scaled`: the bar-even/bar-odd block pair of fact 2 **cannot** also be
   adjoint-scaled (`C = k·σB`, `σk = k`) unless `2·C = 0`. So the realizable bar-odd
   carrier evades the fact-1 obstruction precisely off 2-torsion — the two families
   meet only in the degenerate 2-torsion locus.

**Scope (constraint, not closure).** This narrows the search for a `q_cubic = C1`
derivation — it does **not** derive `c₃`. It (a) widens the self-adjoint
obstruction to every bar-even adjoint scaling, (b) proves the non-self-adjoint
alternative is non-vacuous with the exact `g·γ` shape, (c) pins where the two
disjoin. No `c_k` value; nothing wired; no dependency on PR #4140's unmerged
`SuperDMBerezinian.lean` (uses only on-`main` `BerezinianSelfAdjointCrossTerm`).
§7c: generic `{R : Type*} [CommRing R]`, abstract `σ : R →+* R`, no `ℝ`. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-31-berezinian-selfadjoint-crossterm-bar-even.md
-/
import QOU.QBeta.BerezinianSelfAdjointCrossTerm

namespace QOU.QBeta.BerezinianCrossTermParity

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- **The adjoint-scaled cross-term is bar-EVEN, for any bar-even scaling.** If the
odd off-diagonal blocks are adjoint-scaled `C = k·σB` with `k` bar-even (`σk = k`)
and the even inverse-block `Dinv` bar-even (`σ Dinv = Dinv`), then the cross-term
`t = B·Dinv·C` satisfies `σ t = t` — bar-EVEN — for any ring involution `σ`. The
graded-self-adjoint case `C = −σB` of #4421 is the `k = −1` instance; this shows the
obstruction is not special to that sign but holds across the whole bar-even-scaled
family. -/
theorem crossTerm_bar_even_of_adjoint_scaled
    (B Dinv k : R) (hinv : ∀ x : R, σ (σ x) = x)
    (hk : σ k = k) (hDinv : σ Dinv = Dinv) :
    σ (B * Dinv * (k * σ B)) = B * Dinv * (k * σ B) := by
  simp only [map_mul, hDinv, hk, hinv]
  ring

/-- #4421's self-adjoint result is the `k = −1` instance of the scaled obstruction:
`C = −σB = (−1)·σB`, and `−1` is bar-even. -/
theorem selfadjoint_is_adjoint_scaled
    (B Dinv : R) (hinv : ∀ x : R, σ (σ x) = x) (hDinv : σ Dinv = Dinv) :
    σ (B * Dinv * (-σ B)) = B * Dinv * (-σ B) := by
  have h := crossTerm_bar_even_of_adjoint_scaled σ B Dinv (-1)
    hinv (by simp) hDinv
  simpa using h

/-- **The non-self-adjoint route is realizable — and it is the `g·γ` model.** A
bar-even block `B` (`σB = B`) times a bar-odd block `C` (`σC = −C`), dressed by a
bar-even `Dinv`, gives a genuinely bar-ODD cross-term: `σ t = −t`. The dressing
`g = B·Dinv` is bar-even and the weight `γ = C` bar-odd — exactly the
`OddDecayWeightParity` factorization, here *derived* as the generic bar-odd carrier
from independent (non-adjoint) blocks. -/
theorem crossTerm_bar_odd_of_barEven_barOdd_blocks
    (B C Dinv : R) (hB : σ B = B) (hC : σ C = -C) (hDinv : σ Dinv = Dinv) :
    σ (B * Dinv * C) = -(B * Dinv * C) := by
  simp only [map_mul, hB, hDinv, hC]
  ring

/-- **The bar-odd carrier's blocks are genuinely non-adjoint (off 2-torsion).** If
`B` is bar-even, `C` bar-odd, and yet `C = k·σB` were adjoint-scaled with `k`
bar-even, then `2·C = 0`. So the realizable bar-odd carrier of
`crossTerm_bar_odd_of_barEven_barOdd_blocks` evades the adjoint-scaled obstruction
`crossTerm_bar_even_of_adjoint_scaled` exactly off 2-torsion — the two families are
disjoint outside the degenerate 2-torsion locus. -/
theorem barOdd_blocks_not_adjoint_scaled
    (B C k : R) (hinv : ∀ x : R, σ (σ x) = x)
    (hB : σ B = B) (hC : σ C = -C) (hk : σ k = k) (hlink : C = k * σ B) :
    2 * C = 0 := by
  have h1 : σ C = C := by rw [hlink, map_mul, hk, hinv, hB]
  rw [h1] at hC
  linear_combination hC

end QOU.QBeta.BerezinianCrossTermParity
