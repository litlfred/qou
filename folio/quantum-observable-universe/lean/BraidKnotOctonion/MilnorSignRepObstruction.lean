/-
  Milnor μ̄(123) sign-representation obstruction — finding D2 of
  docs/audits/2026-07-13-mirror-split-s3-em-functional-attempt.md.

  Model (finite explicit computation; the Magnus expansion / Milnor invariant
  itself is NOT re-derived here):

    * S₃ acts on the three link components as `Equiv.Perm (Fin 3)`.
    * The Milnor invariant μ̄(123) transforms in the SIGN representation:
      μ̄(g(1)g(2)g(3)) = sgn(g)·μ̄(123).  This transformation law was verified
      EXACTLY (integer Magnus, all 6 permutations) by the probe
      computations/deltalambda/mirror_split_s3_em_functional_probe.py —
      witness computations/deltalambda/mirror-split-s3-em-functional.witness.json
      (5/5 assertions pass).  Here it is taken as the defining model of the
      antisymmetric invariant (`muBarFamily`).
    * The charge-bilinear channel space is functions on the unordered pairs
      {i,j} ⊂ Fin 3.  For three components, unordered pairs biject
      S₃-equivariantly with their complementary singleton (the omitted index),
      so pair-functions are modelled as `Fin 3 → R` with the permutation
      action `pairAct g w = w ∘ g⁻¹` — the trivial ⊕ standard decomposition of
      the audit's D2.  The bijection's equivariance is PROVED, not assumed:
      `chargeBilinear_equivariant` shows the charge bilinear
      q_iq_j = ∏_{i ∈ {k}ᶜ} q_i intertwines the two actions.

  Main theorem (`equivariant_linearMap_eq_zero`): any S₃-equivariant R-linear
  map from the sign representation to the pair-function representation is
  ZERO.  This is the concrete Schur-lemma content of D2 — the sign rep does
  not occur in trivial ⊕ standard — proved by direct computation over
  transpositions: each channel index k is fixed by the transposition of the
  other two indices, which has sign −1, forcing v k = −v k, hence v k = 0
  given that R has no 2-torsion.

  Hypothesis honesty: the cancellation "v + v = 0 → v = 0" is FALSE in
  characteristic 2, so the core statements carry the weakest sufficient
  hypothesis explicitly (`h2 : ∀ x : R, x + x = 0 → x = 0`); a convenience
  version discharges it from `[NoZeroDivisors R]` + `[NeZero (2 : R)]`.

  Corollary (`coupling_vanishes_on_charge_bilinears`): an equivariant coupling
  functional LINEAR in μ̄ vanishes on every charge bilinear — the D2
  obstruction.  The quadratic invariant survives
  (`muBarFamily_sq_invariant`): the coupling can enter only through |μ̄|
  (equivalently μ̄²), and in particular is mirror-insensitive
  (`muBarFamily_swap_eq_neg` + `muBarFamily_sq_invariant`).

  Generic commutative ring throughout (AGENTS.md §7c): no ℝ, no ordering, no
  archimedean construct — `decide` is used only on decidable `Fin 3` / finite
  `Finset` data, never on ring elements.

  -- Ref: [leitner2026] docs/audits/2026-07-13-mirror-split-s3-em-functional-attempt.md §D2
  -- Ref: [milnor1954] https://doi.org/10.2307/1969685
-/

import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic

namespace QOU.Mass.MilnorSignRepObstruction

open Equiv Finset

variable {R : Type*} [CommRing R]

/-! ### The sign representation of S₃ on R -/

/-- The sign of a permutation of the three link components, cast into the
    base ring `R`.  `g ↦ signR g * μ̄` is the sign representation of S₃ on the
    one-dimensional space spanned by the antisymmetric invariant μ̄(123). -/
def signR (g : Equiv.Perm (Fin 3)) : R := ((Equiv.Perm.sign g : ℤ) : R)

/-- `signR` is multiplicative — `g ↦ signR g * ·` really is a representation. -/
theorem signR_mul (g h : Equiv.Perm (Fin 3)) :
    (signR (g * h) : R) = signR g * signR h := by
  unfold signR
  rw [map_mul, Units.val_mul, Int.cast_mul]

/-- Signs square to 1 in `R` (they are ±1). -/
theorem signR_mul_self (g : Equiv.Perm (Fin 3)) :
    (signR g : R) * signR g = 1 := by
  unfold signR
  rw [← Int.cast_mul, ← Units.val_mul, Int.units_mul_self, Units.val_one,
    Int.cast_one]

/-- A transposition has sign −1 in `R`. -/
theorem signR_swap {a b : Fin 3} (hab : a ≠ b) :
    (signR (Equiv.swap a b) : R) = -1 := by
  unfold signR
  rw [Equiv.Perm.sign_swap hab]
  simp

/-! ### The Milnor invariant as a sign-rep vector -/

/-- The μ̄ family: the value of the antisymmetric invariant on the
    `g`-relabeled component ordering, `μ̄(g(1)g(2)g(3)) = sgn(g)·μ̄(123)`.
    This transformation law is the probe-verified D2 input (integer Magnus,
    6/6 permutations exact; witness
    `computations/deltalambda/mirror-split-s3-em-functional.witness.json`) —
    it is the MODEL here, not a re-derivation of the Milnor invariant. -/
def muBarFamily (μbar : R) (g : Equiv.Perm (Fin 3)) : R := signR g * μbar

/-- On an odd permutation (e.g. a mirror-inducing component transposition)
    the invariant flips sign: the mirror link carries `μ̄ = −μ̄(123)`. -/
theorem muBarFamily_swap_eq_neg (μbar : R) {a b : Fin 3} (hab : a ≠ b) :
    muBarFamily μbar (Equiv.swap a b) = -μbar := by
  unfold muBarFamily
  rw [signR_swap hab]
  ring

/-- The quadratic invariant μ̄² is S₃-invariant: the sign-rep obstruction
    kills only the channel LINEAR in μ̄; a coupling through |μ̄|
    (equivalently μ̄²) survives, and is in particular mirror-insensitive —
    consequence (i) of finding D2. -/
theorem muBarFamily_sq_invariant (μbar : R) (g : Equiv.Perm (Fin 3)) :
    muBarFamily μbar g ^ 2 = μbar ^ 2 := by
  unfold muBarFamily
  rw [mul_pow, pow_two, signR_mul_self, one_mul]

/-! ### The pair-channel (charge-bilinear) representation -/

/-- The S₃ action on pair-channel functions.  Channels (unordered pairs
    `{i,j} ⊂ Fin 3`) are indexed by the omitted component `k`; the action of a
    relabeling `g` sends the function `w` to `w ∘ g⁻¹`.  As a representation
    this is the permutation module on 3 points = trivial ⊕ standard. -/
def pairAct (g : Equiv.Perm (Fin 3)) (w : Fin 3 → R) : Fin 3 → R :=
  fun k => w (g⁻¹ k)

omit [CommRing R] in
@[simp] theorem pairAct_one (w : Fin 3 → R) : pairAct 1 w = w := rfl

omit [CommRing R] in
/-- `pairAct` is a left action. -/
theorem pairAct_mul (g h : Equiv.Perm (Fin 3)) (w : Fin 3 → R) :
    pairAct (g * h) w = pairAct g (pairAct h w) := by
  funext k
  simp [pairAct, Equiv.Perm.mul_apply]

/-- The charge bilinear of the pair channel `k`: the product `q_i q_j` over
    the two components `{i,j} = {k}ᶜ` other than `k`.  For ³He-type charges
    `q = (1,1,0)` exactly one channel is EM-active; for ³H-type `q = (1,0,0)`
    every channel vanishes (D1 of the audit). -/
def chargeBilinear (q : Fin 3 → R) (k : Fin 3) : R :=
  ∏ i ∈ ({k}ᶜ : Finset (Fin 3)), q i

theorem chargeBilinear_zero (q : Fin 3 → R) :
    chargeBilinear q 0 = q 1 * q 2 := by
  have h : ({(0 : Fin 3)}ᶜ : Finset (Fin 3)) = {1, 2} := by decide
  rw [chargeBilinear, h, Finset.prod_insert (by decide), Finset.prod_singleton]

theorem chargeBilinear_one (q : Fin 3 → R) :
    chargeBilinear q 1 = q 0 * q 2 := by
  have h : ({(1 : Fin 3)}ᶜ : Finset (Fin 3)) = {0, 2} := by decide
  rw [chargeBilinear, h, Finset.prod_insert (by decide), Finset.prod_singleton]

theorem chargeBilinear_two (q : Fin 3 → R) :
    chargeBilinear q 2 = q 0 * q 1 := by
  have h : ({(2 : Fin 3)}ᶜ : Finset (Fin 3)) = {0, 1} := by decide
  rw [chargeBilinear, h, Finset.prod_insert (by decide), Finset.prod_singleton]

/-- Reindexing a complement-product along a permutation. -/
theorem prod_compl_map (σ : Equiv.Perm (Fin 3)) (q : Fin 3 → R) (k : Fin 3) :
    ∏ i ∈ ({k}ᶜ : Finset (Fin 3)), q (σ i)
      = ∏ j ∈ ({σ k}ᶜ : Finset (Fin 3)), q j := by
  have h1 : ({k}ᶜ : Finset (Fin 3)).map σ.toEmbedding
      = ({σ k}ᶜ : Finset (Fin 3)) := by
    ext j
    simp [Finset.mem_map_equiv, Equiv.symm_apply_eq]
  rw [← h1, Finset.prod_map]
  rfl

/-- The pair-index bijection (pair ↔ omitted component) is S₃-EQUIVARIANT:
    the charge bilinear intertwines the component action `q ↦ q ∘ g⁻¹` with
    the pair-channel action `pairAct`.  This is the proved bridge between the
    physical charge-bilinear space and the `Fin 3 → R` model. -/
theorem chargeBilinear_equivariant (g : Equiv.Perm (Fin 3)) (q : Fin 3 → R) :
    chargeBilinear (fun i => q (g⁻¹ i)) = pairAct g (chargeBilinear q) := by
  funext k
  simpa [chargeBilinear, pairAct] using prod_compl_map g⁻¹ q k

/-! ### The Schur obstruction (finding D2) -/

/-- Core computation: a pair-channel vector `v` that transforms in the SIGN
    representation — `sgn(g)·v k = v (g⁻¹ k)` for all `g` — vanishes,
    provided `R` has no 2-torsion.  Proof: each channel `k` is fixed by the
    transposition of the two other indices, which has sign −1, so
    `−v k = v k`.  This is the "sign rep does not occur in trivial ⊕
    standard" Schur statement, by direct computation. -/
theorem sign_equivariant_pairVector_eq_zero
    (h2 : ∀ x : R, x + x = 0 → x = 0) (v : Fin 3 → R)
    (hequiv : ∀ (g : Equiv.Perm (Fin 3)) (k : Fin 3),
      signR g * v k = v (g⁻¹ k)) :
    v = 0 := by
  have key : ∀ a b k : Fin 3, a ≠ b → k ≠ a → k ≠ b → v k = 0 := by
    intro a b k hab hka hkb
    have h := hequiv (Equiv.swap a b) k
    rw [Equiv.swap_inv, Equiv.swap_apply_of_ne_of_ne hka hkb,
      signR_swap hab] at h
    exact h2 (v k) (by linear_combination -h)
  funext k
  show v k = 0
  fin_cases k
  · exact key 1 2 0 (by decide) (by decide) (by decide)
  · exact key 0 2 1 (by decide) (by decide) (by decide)
  · exact key 0 1 2 (by decide) (by decide) (by decide)

/-- **Finding D2 (main theorem).** Any S₃-equivariant `R`-linear map from the
    sign representation (the line spanned by μ̄(123)) to the pair-channel
    representation (charge bilinears; trivial ⊕ standard) is ZERO — the
    concrete Schur-lemma obstruction, over any commutative ring without
    2-torsion (weakest hypothesis stated explicitly). -/
theorem equivariant_linearMap_eq_zero
    (h2 : ∀ x : R, x + x = 0 → x = 0)
    (T : R →ₗ[R] (Fin 3 → R))
    (hT : ∀ (g : Equiv.Perm (Fin 3)) (x : R),
      T (signR g * x) = pairAct g (T x)) :
    T = 0 := by
  have hv : T 1 = 0 := by
    apply sign_equivariant_pairVector_eq_zero h2
    intro g k
    have h := congrFun (hT g 1) k
    rw [mul_one] at h
    have hs : T (signR g) = signR (R := R) g • T 1 := by
      have hsm := T.map_smul (signR g) 1
      simpa [smul_eq_mul] using hsm
    rw [hs] at h
    simpa [pairAct, Pi.smul_apply, smul_eq_mul] using h
  refine LinearMap.ext fun x => ?_
  have hx : T x = x • T 1 := by
    have hsm := T.map_smul x 1
    simpa [smul_eq_mul] using hsm
  rw [LinearMap.zero_apply, hx, hv, smul_zero]

/-- Convenience version: the 2-torsion-freeness hypothesis discharged from
    `[NoZeroDivisors R]` + `[NeZero (2 : R)]` (e.g. `R = ℤ`, `ℚ`, or any
    integral domain of characteristic ≠ 2). -/
theorem equivariant_linearMap_eq_zero_of_neZero_two
    [NoZeroDivisors R] [NeZero (2 : R)]
    (T : R →ₗ[R] (Fin 3 → R))
    (hT : ∀ (g : Equiv.Perm (Fin 3)) (x : R),
      T (signR g * x) = pairAct g (T x)) :
    T = 0 := by
  refine equivariant_linearMap_eq_zero ?_ T hT
  intro x hx
  have h2x : (2 : R) * x = 0 := by rw [two_mul]; exact hx
  rcases mul_eq_zero.mp h2x with h | h
  · exact absurd h (NeZero.ne (2 : R))
  · exact h

/-- **The D2 obstruction, audit-shaped corollary.** An S₃-equivariant coupling
    functional LINEAR in the antisymmetric invariant μ̄(123) vanishes on every
    charge bilinear: `∑ₖ T(μ̄)ₖ · qᵢqⱼ = 0` for all charges.  The EM coupling
    functional of the audit therefore cannot couple through μ̄ linearly — only
    through |μ̄| (see `muBarFamily_sq_invariant`). -/
theorem coupling_vanishes_on_charge_bilinears
    (h2 : ∀ x : R, x + x = 0 → x = 0)
    (T : R →ₗ[R] (Fin 3 → R))
    (hT : ∀ (g : Equiv.Perm (Fin 3)) (x : R),
      T (signR g * x) = pairAct g (T x))
    (μbar : R) (q : Fin 3 → R) :
    ∑ k : Fin 3, T μbar k * chargeBilinear q k = 0 := by
  have hT0 := equivariant_linearMap_eq_zero h2 T hT
  simp [hT0]

end QOU.Mass.MilnorSignRepObstruction
