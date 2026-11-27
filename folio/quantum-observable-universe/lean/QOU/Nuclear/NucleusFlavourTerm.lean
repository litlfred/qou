import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic

/-!
# The flavour term of an `A`-nucleon nucleus (gap G4 of the term-completeness ledger)

Beans `qou-tcl4` (gap G4), `qou-myts` (accuracy epic). The ledger
`docs/audits/2026-11-27-term-completeness-ledger.md` (#9658) lists the entry
`(flavour, T, r = 1)` at level `3A`, `A ≥ 2`, as missing: no formula on record lifts the
one-body nucleon flavour cell `δ = 2E₀·log q` (`K`-weight cell, ruling A, framing-corrected
trace) to a nucleus block. This file derives that lift.

## Setting

A nucleus of `A` nucleons is a word on `3A` strands. Its nucleon blocks are `A` copies of the
three-strand space, indexed by `Fin A → ι` (`ι` = the basis of one block). On a product of
disjoint blocks the element is the `A`-fold Kronecker product `kronPi X` of block elements
`X i`, and the weight of a tagging `c : Fin A → Fin 2` (`0` = proton, `1` = neutron) is the
Kronecker product of the per-block weighted projectors `W 0` (`K`-weight on the proton weight
space) and `W 1` (`K`-weight on the neutron weight space). The `K`-weight is grouplike,
`Δ(K) = K ⊗ K`, which is exactly why the weight of the tagging is a Kronecker product.

## What is proved (commutative ring / integral domain, no numerical value)

* `kronPi_mul`, `trace_kronPi`: the `A`-fold Kronecker product is multiplicative and its trace
  is the product of the block traces. So the weighted trace of a tagged nucleus is the product of
  the tagged block traces (`tauNuc_eq_prod`): **blocks multiply**, at every `A`.
* `tauNuc_eq_pow`: if every block satisfies the nucleon cell `τ_p = q²·τ_n` (the input, see
  below), then `τ(c) = q^{2Z}·∏ᵢ τ_n(Xᵢ)`, where `Z` is the number of protons of the tagging.
* `flavourMass_eq`: for any logarithm-like map `ℓ` (`ℓ(xy) = ℓx + ℓy` on nonzero elements) and
  the mass reading `M = −E₀·ℓ(τ)`, `M(c) = M₀ − Z·δ` with `δ = 2·E₀·ℓ(q)`, the nucleon cell,
  and `M₀` the reading of the all-neutron tagging (every isoscalar piece, braid included). The
  whole `Z`-dependence is the flavour rank-1 term.
* `flavourMass_two_mul`: in isospin form, `2·M(c) = (2M₀ − A·δ) − (Z − N)·δ`, i.e.
  `M = (isoscalar) − δ·T_z` with `2T_z = Z − N`. This is the ledger's entry
  `(flavour, T, r = 1)` at level `3A`, with reduced coefficient `δ`.
* `flavourMass_isobar`: two taggings with the same `Z` have the same flavour mass: the term does
  not depend on which blocks are protons, only on `T_z`.
* `flavourMass_beta_step`: turning one neutron block into a proton lowers the flavour mass by
  exactly `δ`, at every `A` and from every tagging. This is the flavour piece of
  `Q_β⁻ = M(Z, N) − M(Z+1, N−1) − m_e` along an isobar: `δ`, the same value as the free
  neutron.
* `flavourMass_second_difference`: along an isobar the flavour term has zero second difference.
  It is rank 1 only: it supplies no isobaric parabola (`T_z²`), which must come from the
  `em` rank-2 entry (G3) and the block-dependent braid coefficient (G2).

So the flavour column of the ledger at level `3A` is closed with **no new coefficient**: the
reduced matrix element is the nucleon cell `δ` on every block. Nothing here is fitted.

## The input, and what is NOT claimed

* The per-block hypothesis `τ_p = q²·τ_n` is the nucleon cell. On main it is proved for the
  `K`-weight forced by the Markov condition (`NucleonSplitFullTower.markov_forces_K`, exponent
  exactly 2) and checked on the tower; #9663 (`NucleonFlavourTypedLetters.typed_V_pow_tau_ratio`)
  proves it for every flavour-typed γγ word `Vᵏ`, raw or framing-corrected. Here it is a
  hypothesis on each block, so the result holds for any block element that satisfies it.
* Disjoint blocks only (`kronPi`). Interface letters between nucleon blocks make the block sum
  element-dependent (`docs/audits/2026-11-27-nucleon-split-full-tower.md` §3) and the nuclear
  interface word is not ruled (#7876). That is the word axis (G5), outside the ledger.
* The `Real.log` instance (`ℓ = Real.log`, `δ = 2E₀·log q`) lives behind the transcendental
  boundary in `QOU/Transcendental/Nuclear/NucleusFlavourTermLog.lean`.
-/

namespace QOU.Nuclear.NucleusFlavourTerm

open Matrix Finset

section Kron

variable {R : Type*} [CommRing R] {A : ℕ} {ι : Type*} [Fintype ι]

/-- The `A`-fold Kronecker product of block matrices, on the product basis `Fin A → ι`. -/
def kronPi (X : Fin A → Matrix ι ι R) : Matrix (Fin A → ι) (Fin A → ι) R :=
  fun s t => ∏ i, X i (s i) (t i)

/-- **The `A`-fold Kronecker product is multiplicative.** -/
theorem kronPi_mul (X Y : Fin A → Matrix ι ι R) :
    kronPi X * kronPi Y = kronPi (fun i => X i * Y i) := by
  ext s t
  simp only [kronPi, mul_apply]
  rw [Finset.prod_univ_sum, Fintype.piFinset_univ]
  refine Finset.sum_congr rfl fun u _ => ?_
  rw [Finset.prod_mul_distrib]

/-- **The trace of an `A`-fold Kronecker product is the product of the block traces.** -/
theorem trace_kronPi (X : Fin A → Matrix ι ι R) :
    (kronPi X).trace = ∏ i, (X i).trace := by
  simp only [Matrix.trace, Matrix.diag, kronPi]
  rw [Finset.prod_univ_sum, Fintype.piFinset_univ]

/-- The weighted trace of a nucleus of `A` disjoint blocks `X`, tagged by `c`
(`c i = 0`: proton, `c i = 1`: neutron), with per-type block weights `W`. -/
def tauNuc (W : Fin 2 → Matrix ι ι R) (c : Fin A → Fin 2) (X : Fin A → Matrix ι ι R) : R :=
  (kronPi (fun i => W (c i)) * kronPi X).trace

/-- **Blocks multiply.** -/
theorem tauNuc_eq_prod (W : Fin 2 → Matrix ι ι R) (c : Fin A → Fin 2)
    (X : Fin A → Matrix ι ι R) :
    tauNuc W c X = ∏ i, (W (c i) * X i).trace := by
  rw [tauNuc, kronPi_mul, trace_kronPi]

/-- The number of proton blocks of a tagging. -/
def protons (c : Fin A → Fin 2) : ℕ := (univ.filter fun i => c i = 0).card

/-- The number of neutron blocks of a tagging. -/
def neutrons (c : Fin A → Fin 2) : ℕ := (univ.filter fun i => c i ≠ 0).card

theorem protons_add_neutrons (c : Fin A → Fin 2) : protons c + neutrons c = A := by
  rw [protons, neutrons, Finset.filter_card_add_filter_neg_card_eq_card, card_univ,
    Fintype.card_fin]

/-- **The nucleus trace is `q^{2Z}` times the all-neutron trace**, given the nucleon cell
`τ_p = q²·τ_n` on every block. -/
theorem tauNuc_eq_pow (q : R) (W : Fin 2 → Matrix ι ι R) (c : Fin A → Fin 2)
    (X : Fin A → Matrix ι ι R) (hcell : ∀ i, (W 0 * X i).trace = q ^ 2 * (W 1 * X i).trace) :
    tauNuc W c X = q ^ (2 * protons c) * ∏ i, (W 1 * X i).trace := by
  have hblock : ∀ i, (W (c i) * X i).trace
      = (if c i = 0 then q ^ 2 else 1) * (W 1 * X i).trace := by
    intro i
    by_cases h : c i = 0
    · simp [h, hcell i]
    · have h1 : c i = 1 := by omega
      simp [h1]
  rw [tauNuc_eq_prod, Finset.prod_congr rfl fun i _ => hblock i, Finset.prod_mul_distrib,
    Finset.prod_ite, Finset.prod_const, Finset.prod_const_one, mul_one, ← pow_mul]
  rfl

end Kron

section Mass

variable {R F : Type*} [CommRing R] [IsDomain R] [CommRing F] {A : ℕ} {ι : Type*} [Fintype ι]

/-- A logarithm-like map: additive on products of nonzero elements. (`Real.log` is one; the
instance lives behind the transcendental boundary.) -/
def LogLike (ℓ : R → F) : Prop := ∀ x y : R, x ≠ 0 → y ≠ 0 → ℓ (x * y) = ℓ x + ℓ y

theorem LogLike.pow_pos {ℓ : R → F} (hℓ : LogLike ℓ) {q : R} (hq : q ≠ 0) (n : ℕ) (P : R)
    (hP : P ≠ 0) : ℓ (q ^ n * P) = n * ℓ q + ℓ P := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, mul_assoc, mul_comm q P, ← mul_assoc,
      hℓ _ _ (mul_ne_zero (pow_ne_zero _ hq) hP) hq, ih]
    push_cast; ring

/-- The flavour mass reading of a weighted trace: `M = −E₀·ℓ(τ)` (as in
`NucleonSplitFullTower.gibbs_split_full_tower`, where `m_n − m_p = E·ℓ(τ_p/τ_n)`). -/
def flavourMass (E₀ : F) (ℓ : R → F) (τ : R) : F := -(E₀ * ℓ τ)

/-- The nucleon cell `δ = 2·E₀·ℓ(q)`. -/
def cell (E₀ : F) (ℓ : R → F) (q : R) : F := 2 * E₀ * ℓ q

variable (E₀ : F) {ℓ : R → F} (hℓ : LogLike ℓ) {q : R} (hq : q ≠ 0)
  (W : Fin 2 → Matrix ι ι R) (X : Fin A → Matrix ι ι R)
  (hcell : ∀ i, (W 0 * X i).trace = q ^ 2 * (W 1 * X i).trace)
  (hn : ∀ i, (W 1 * X i).trace ≠ 0)

include hℓ hq hcell hn

/-- **The `A`-nucleon flavour term.** `M(c) = M₀ − Z·δ`, with `M₀` the all-neutron flavour mass
and `δ = 2E₀·ℓ(q)` the nucleon cell. -/
theorem flavourMass_eq (c : Fin A → Fin 2) :
    flavourMass E₀ ℓ (tauNuc W c X)
      = flavourMass E₀ ℓ (∏ i, (W 1 * X i).trace) - protons c * cell E₀ ℓ q := by
  rw [tauNuc_eq_pow q W c X hcell]
  simp only [flavourMass, cell]
  rw [hℓ.pow_pos hq _ _ (Finset.prod_ne_zero_iff.mpr fun i _ => hn i)]
  push_cast; ring

/-- **Isospin form.** `2·M(c) = (2M₀ − A·δ) − (Z − N)·δ`: an isoscalar plus `−δ·T_z`
(`2T_z = Z − N`). The rank-1 coefficient is the nucleon cell, on every block. -/
theorem flavourMass_two_mul (c : Fin A → Fin 2) :
    2 * flavourMass E₀ ℓ (tauNuc W c X)
      = (2 * flavourMass E₀ ℓ (∏ i, (W 1 * X i).trace) - A * cell E₀ ℓ q)
        - ((protons c : F) - neutrons c) * cell E₀ ℓ q := by
  rw [flavourMass_eq E₀ hℓ hq W X hcell hn c]
  have h : (A : F) = protons c + neutrons c := by
    rw [← Nat.cast_add, protons_add_neutrons c]
  rw [h]; ring

/-- **Only `Z` counts.** Two taggings with the same number of protons have the same flavour mass,
whichever blocks are protons. -/
theorem flavourMass_isobar (c c' : Fin A → Fin 2) (h : protons c = protons c') :
    flavourMass E₀ ℓ (tauNuc W c X) = flavourMass E₀ ℓ (tauNuc W c' X) := by
  rw [flavourMass_eq E₀ hℓ hq W X hcell hn c, flavourMass_eq E₀ hℓ hq W X hcell hn c', h]

/-- **One β step costs exactly the nucleon cell.** If `c'` has one more proton than `c`, the
flavour mass drops by `δ = 2E₀·ℓ(q)`: the flavour piece of `Q_β⁻` along an isobar, at every `A`,
equals the free-neutron value. -/
theorem flavourMass_beta_step (c c' : Fin A → Fin 2) (h : protons c' = protons c + 1) :
    flavourMass E₀ ℓ (tauNuc W c X) - flavourMass E₀ ℓ (tauNuc W c' X) = cell E₀ ℓ q := by
  rw [flavourMass_eq E₀ hℓ hq W X hcell hn c, flavourMass_eq E₀ hℓ hq W X hcell hn c', h]
  push_cast; ring

/-- **No isobaric curvature from flavour.** Along an isobar the flavour term has zero second
difference: it is rank 1 only, so the parabola in `T_z` must come from G2/G3. -/
theorem flavourMass_second_difference (c c' c'' : Fin A → Fin 2)
    (h1 : protons c' = protons c + 1) (h2 : protons c'' = protons c + 2) :
    flavourMass E₀ ℓ (tauNuc W c X) - 2 * flavourMass E₀ ℓ (tauNuc W c' X)
      + flavourMass E₀ ℓ (tauNuc W c'' X) = 0 := by
  rw [flavourMass_eq E₀ hℓ hq W X hcell hn c, flavourMass_eq E₀ hℓ hq W X hcell hn c',
    flavourMass_eq E₀ hℓ hq W X hcell hn c'', h1, h2]
  push_cast; ring

end Mass

/-- A one-neutron-to-proton flip raises the proton count by one. -/
theorem protons_update {A : ℕ} (c : Fin A → Fin 2) (j : Fin A) (hj : c j = 1) :
    protons (Function.update c j 0) = protons c + 1 := by
  classical
  unfold protons
  have : (univ.filter fun i => Function.update c j 0 i = 0)
      = insert j (univ.filter fun i => c i = 0) := by
    ext i
    by_cases hij : i = j
    · subst hij; simp
    · simp [hij]
  rw [this, Finset.card_insert_of_notMem (by simp [hj])]

end QOU.Nuclear.NucleusFlavourTerm

