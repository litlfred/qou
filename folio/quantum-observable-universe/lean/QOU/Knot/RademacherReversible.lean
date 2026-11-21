/-
  Why the Rademacher function vanishes on the canonical 3-braid closures
  (bean `qou-aspz`) — a Dedekind-sum-free structural proof.

  CONTEXT (PR #4513).  The scope-(a) refutation of the Rademacher route to ϑ_K
  rests on `Φ((RL)ⁿ) = 0` for the canonical closures `(σ₁σ₂⁻¹)ⁿ`, whose
  SL(2,ℤ) image is `(RL)ⁿ`.  That was established by COMPUTE only — three
  agreeing methods (Dedekind-sum formula in exact `Fraction` arithmetic, the
  RL word count, and homogeneity).  The refutation is load-bearing, so it
  deserved a proof rather than an agreement of three calculations.

  THE INTENDED LEVER IS NOT AVAILABLE.  Bean `qou-aspz` proposed proving the
  Dedekind-sum formula agrees with the word count, guessing that Dedekind sums
  live in Mathlib and that reciprocity would be the lever.  They do not:
  Mathlib has `NumberTheory.ModularForms.DedekindEta` (the eta function —
  product definition, non-vanishing, differentiability) and nothing else
  relevant.  There is no Dedekind sum, no eta transformation law, no multiplier
  system, and no Rademacher function.  That route would mean building the
  theory from scratch.

  THE ROUTE TAKEN INSTEAD needs none of it.  `RL` is REVERSIBLE — conjugate to
  its own inverse — and *any* function that is conjugation-invariant and
  inverts-to-negate must vanish on such an element.  Concretely
  `S · RL · S⁻¹ = (RL)⁻¹` with `S = !![0, 1; -1, 0]`, and conjugation is a
  homomorphism, so the same `S` works for every power `(RL)ⁿ` at once.

  WHAT THIS BUYS OVER THE COMPUTE.  It is not merely a re-derivation:

  * **It explains the observation.**  The probe found `Φ = 0` at BOTH anchors
    and concluded `Φ` "cannot even distinguish them".  That is not a numerical
    accident — both anchors are `(RL)ⁿ` closures, hence both reversible, hence
    both forced to `0` by `rademacher_eq_zero_of_reversible`.
  * **It is uniform in `n`.**  The compute checked finitely many `n`.
  * **It is stronger than the target.**  Vanishing holds for EVERY homogeneous
    quasimorphism on EVERY reversible element, not just for Rademacher's `Φ` on
    `(RL)ⁿ` — so no other quasimorphism-flavoured invariant can rescue the
    route either.

  HONESTY BOUNDARY.  The two properties of `Φ` — conjugation-invariance and
  `Φ(g⁻¹) = -Φ(g)` — are carried as EXPLICIT HYPOTHESES, not proved here; they
  are standard for homogeneous quasimorphisms and `homogeneous_inv` derives the
  second from homogeneity.  What is proved sorry-free is the reversibility of
  `RL` (an explicit matrix computation) and the vanishing consequence.  This is
  §3b-cond shaped: the hypotheses are genuine INPUTS, and the conclusion is
  DERIVED from them — the class does not carry the conclusion.

  Scope (a): nothing here refutes the Rademacher function; it shows the
  Rademacher route cannot distinguish the two anchors, for a structural reason.

  -- Ref: [leitner2026] bean qou-aspz; computations/probes/qbeta_rdmr_rademacher_winding_probe.py
  -- Ref: [ghys2007] Knots and dynamics (ICM 2006) — Rademacher function as a
  --      homogeneous quasimorphism; the RL word count on hyperbolic classes
-/

import Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup
import Mathlib.Tactic

namespace QOU.Knot.RademacherReversible

open Matrix

/-- The modular group `SL(2, ℤ)`. Named explicitly rather than via the scoped
`SL(2, ℤ)` notation, which this import set does not bring into scope. -/
abbrev SL2Z := Matrix.SpecialLinearGroup (Fin 2) ℤ

/-! ## 1. Reversible elements: the group-theoretic core -/

variable {G : Type*} [Group G]

/-- An element is **reversible** when it is conjugate to its own inverse. -/
def Reversible (g : G) : Prop := ∃ x : G, x * g * x⁻¹ = g⁻¹

/-- **Reversibility passes to powers.**  Conjugation by a fixed `x` is a group
homomorphism, so a single witness `x` reverses every power of `g` at once.
This is what makes the result uniform in `n`, where the compute could only
check finitely many. -/
theorem Reversible.pow {g : G} (h : Reversible g) (n : ℕ) : Reversible (g ^ n) := by
  obtain ⟨x, hx⟩ := h
  refine ⟨x, ?_⟩
  have hconj : ∀ m : ℕ, x * g ^ m * x⁻¹ = (x * g * x⁻¹) ^ m := by
    intro m
    induction m with
    | zero => simp
    | succ k ih =>
        rw [pow_succ, pow_succ, ← ih]
        group
  rw [hconj n, hx, ← inv_pow]

/-- **The vanishing lemma.**  Any conjugation-invariant, inversion-antisymmetric
real-valued function vanishes on a reversible element.  Two lines: invariance
moves `Φ g` to `Φ g⁻¹`, antisymmetry turns that into `-Φ g`. -/
theorem eq_zero_of_reversible (Φ : G → ℝ)
    (hconj : ∀ g x : G, Φ (x * g * x⁻¹) = Φ g)
    (hinv : ∀ g : G, Φ g⁻¹ = -Φ g)
    {g : G} (hg : Reversible g) :
    Φ g = 0 := by
  obtain ⟨x, hx⟩ := hg
  have h1 : Φ g = Φ g⁻¹ := by rw [← hx, hconj]
  rw [hinv] at h1
  linarith

/-- **Antisymmetry comes free from homogeneity.**  A homogeneous quasimorphism
satisfies `Φ(gⁿ) = n·Φ(g)` for all integers `n`; at `n = -1` that is exactly
`Φ(g⁻¹) = -Φ(g)`.  So a caller who has homogeneity need not assume `hinv`
separately. -/
theorem homogeneous_inv (Φ : G → ℝ)
    (hhom : ∀ (g : G) (n : ℤ), Φ (g ^ n) = (n : ℝ) * Φ g) (g : G) :
    Φ g⁻¹ = -Φ g := by
  have := hhom g (-1)
  simpa using this

/-! ## 2. `RL` is reversible in `SL2Z` -/

/-- `R = !![1,1;0,1]`, the parabolic generator. -/
def Rm : SL2Z := ⟨!![1, 1; 0, 1], by simp [Matrix.det_fin_two_of]⟩

/-- `L = !![1,0;1,1]`, the other parabolic generator. -/
def Lm : SL2Z := ⟨!![1, 0; 1, 1], by simp [Matrix.det_fin_two_of]⟩

/-- `RL = !![2,1;1,1]` — the `SL(2,ℤ)` image of the canonical 3-braid
`σ₁σ₂⁻¹`, and the element whose powers are the two anchors. -/
def RL : SL2Z := ⟨!![2, 1; 1, 1], by simp [Matrix.det_fin_two_of]⟩

/-- `S = !![0,1;-1,0]`, the order-4 elliptic generator. This is the conjugator. -/
def Sm : SL2Z := ⟨!![0, 1; -1, 0], by simp [Matrix.det_fin_two_of]⟩

/-- `S⁻¹ = !![0,-1;1,0]`, named so the identities below stay inverse-free. -/
def SmInv : SL2Z := ⟨!![0, -1; 1, 0], by simp [Matrix.det_fin_two_of]⟩

/-- `(RL)⁻¹ = !![1,-1;-1,2]`. -/
def RLInv : SL2Z := ⟨!![1, -1; -1, 2], by simp [Matrix.det_fin_two_of]⟩

/-- `R⁻¹ = !![1,-1;0,1]`. -/
def RmInv : SL2Z := ⟨!![1, -1; 0, 1], by simp [Matrix.det_fin_two_of]⟩

@[simp] theorem Sm_mul_SmInv : Sm * SmInv = 1 := by
  apply Matrix.SpecialLinearGroup.ext; decide

@[simp] theorem RL_mul_RLInv : RL * RLInv = 1 := by
  apply Matrix.SpecialLinearGroup.ext; decide

@[simp] theorem Rm_mul_RmInv : Rm * RmInv = 1 := by
  apply Matrix.SpecialLinearGroup.ext; decide

theorem SmInv_eq : SmInv = Sm⁻¹ := (inv_eq_of_mul_eq_one_right Sm_mul_SmInv).symm

theorem RLInv_eq : RLInv = RL⁻¹ := (inv_eq_of_mul_eq_one_right RL_mul_RLInv).symm

theorem RmInv_eq : RmInv = Rm⁻¹ := (inv_eq_of_mul_eq_one_right Rm_mul_RmInv).symm

/-- `RL` really is `R * L` — so the object below is the braid image, not an
unrelated matrix that happens to have trace 3. -/
theorem RL_eq_Rm_mul_Lm : RL = Rm * Lm := by
  apply Matrix.SpecialLinearGroup.ext
  decide

/-- **The reversing conjugation, explicitly.**  `S · RL · S⁻¹ = (RL)⁻¹`.

Proved without inverting anything: `S · RL · S' = RL'` for the explicit
`S' = !![0,-1;1,0]` and `RL' = !![1,-1;-1,2]`, together with `S · S' = 1` and
`RL · RL' = 1`, which identify `S'` and `RL'` as the inverses. -/
theorem Sm_conj_RL_inv_free : Sm * RL * SmInv = RLInv := by
  apply Matrix.SpecialLinearGroup.ext; decide

theorem Sm_conj_RL : Sm * RL * Sm⁻¹ = RL⁻¹ := by
  rw [← SmInv_eq, ← RLInv_eq]; exact Sm_conj_RL_inv_free

/-- **Control: the same conjugation FAILS for the parabolic `R`.**
`S · R · S⁻¹ ≠ R⁻¹`, decided.

This is what makes `Sm_conj_RL` a fact about `RL` rather than a formality that
any matrix would satisfy — the identity is special to the hyperbolic `RL`, and
the vanishing it forces is correspondingly special.

Note the honest limit of this statement: it says THIS conjugator fails for `R`,
not that `R` is non-reversible. The latter is true in `SL(2, ℤ)` (the parabolic
classes `!![1,n;0,1]` for `n > 0` and `n < 0` are distinct, though they fuse in
`GL(2, ℤ)`), but proving it needs an argument over ALL conjugators and is not
attempted here. -/
theorem Sm_not_conj_Rm : Sm * Rm * Sm⁻¹ ≠ Rm⁻¹ := by
  rw [← SmInv_eq, ← RmInv_eq]
  intro hcon
  have h := congrArg (fun M : SL2Z => (M : Matrix (Fin 2) (Fin 2) ℤ) 0 1) hcon
  revert h
  decide

/-- `RL` is reversible. -/
theorem reversible_RL : Reversible RL := ⟨Sm, Sm_conj_RL⟩

/-- **Every power of `RL` is reversible**, by the same conjugator `S`. -/
theorem reversible_RL_pow (n : ℕ) : Reversible (RL ^ n) := reversible_RL.pow n

/-! ## 3. The conclusion `qou-aspz` asked for -/

/-- **`Φ((RL)ⁿ) = 0`, for every `n`, from structure rather than computation.**

`Φ` is any conjugation-invariant, inversion-antisymmetric real function on
`SL(2,ℤ)` — Rademacher's function is one, as is every homogeneous
quasimorphism.  No Dedekind sum, no word count, no reciprocity law.

This is the Lean form of the scope-(a) refutation in
`qbeta_rdmr_rademacher_winding_probe.py`: the Rademacher route cannot supply
`ϑ_K`, because it is pinned to `0` on the canonical closures. -/
theorem rademacher_eq_zero_of_reversible (Φ : SL2Z → ℝ)
    (hconj : ∀ g x : SL2Z, Φ (x * g * x⁻¹) = Φ g)
    (hinv : ∀ g : SL2Z, Φ g⁻¹ = -Φ g) (n : ℕ) :
    Φ (RL ^ n) = 0 :=
  eq_zero_of_reversible Φ hconj hinv (reversible_RL_pow n)

/-- The same conclusion for a caller who has homogeneity rather than
antisymmetry — the usual packaging of the Rademacher function. -/
theorem rademacher_eq_zero_of_homogeneous (Φ : SL2Z → ℝ)
    (hconj : ∀ g x : SL2Z, Φ (x * g * x⁻¹) = Φ g)
    (hhom : ∀ (g : SL2Z) (m : ℤ), Φ (g ^ m) = (m : ℝ) * Φ g) (n : ℕ) :
    Φ (RL ^ n) = 0 :=
  eq_zero_of_reversible Φ hconj (homogeneous_inv Φ hhom) (reversible_RL_pow n)

/-- **Both anchors are forced to the same value, so `Φ` cannot separate them.**
The probe reported that `Φ` vanishes for both and "cannot even distinguish
them"; this is why.  Any two powers of `RL` — the muon and proton closures
included — carry equal `Φ`, whatever `Φ` is. -/
theorem rademacher_cannot_distinguish (Φ : SL2Z → ℝ)
    (hconj : ∀ g x : SL2Z, Φ (x * g * x⁻¹) = Φ g)
    (hinv : ∀ g : SL2Z, Φ g⁻¹ = -Φ g) (m n : ℕ) :
    Φ (RL ^ m) = Φ (RL ^ n) := by
  rw [rademacher_eq_zero_of_reversible Φ hconj hinv m,
      rademacher_eq_zero_of_reversible Φ hconj hinv n]

end QOU.Knot.RademacherReversible
