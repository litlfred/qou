import QOU.Core.CategoricalHamiltonianLegendre
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The per-down-strand self term of the categorical Lagrangian

The categorical Lagrangian is `ℒ = 𝒟² + ψ*·𝒟ψ`, `𝒟 = q⁻¹∇ + (1 − q⁻¹)·Reeb`
(`QOU.CategoricalLagrangianTwoTermBridge`). Its energy is taken by the Legendre transform of
`QOU.Core.CategoricalHamiltonianLegendre`. This file asks where a **self** term of one strand
(not a crossing term between two strands) sits in that chain, and whether it can depend on
the strand's flavour.

## Model

The nucleon state is a product of strand weight vectors on `V^{⊗n}`. A one-strand operator
contributes a value `ε f` on a strand of flavour `f`, and a degree-1 operator (the Reeb vector
field) acts by the Leibniz rule, so its self part on the product state is the sum
`selfSum ε f = Σ_s ε (f s)` over **all** `n` strands. This holds for every `n` (the full tower);
the sum has no crossing terms, because a derivation has none in degree 1.

## Results

1. `selfSum_eq_counts`, `selfSum_flip_down`: the self sum is linear in the number of down
   strands, and turning one up strand into a down strand changes it by `ε down − ε up`,
   whatever the other strands are.
2. `selfSum_flavour_blind_of_weyl_even` (scope (b), invariant: the Weyl reflection `u ↔ d`):
   a Weyl-even one-strand operator (`ε up = ε down`; e.g. any function of `w²`, so the
   degree-2 `R_s²` self part and a flavour-equivariant degree-0 `∇`) gives the same self sum
   for every flavour assignment with the same `n`. Only the Weyl-odd part can split the nucleons,
   and on one strand it is `c · w` with `w = ±1`.
3. `trace_hamiltonianVel_eq_of_shared` (scope (b), invariant: the degree-1 cancellation
   `categoricalHamiltonianVel_eq`): in the velocity Legendre transform the Reeb-matter term,
   which is the only place the Weyl-odd self term enters, cancels. With a shared Dirac operator
   and a shared horizontal matter trace, the two nucleons have the same velocity energy.
4. `canonical_unit_clock_weight_state`: in the canonical (momentum) Legendre transform at unit
   clock, on a weight state (`a₂ = a₁²`), the energy is the perfect square `(a₁ − 1/2)²` (stated as `4H = (2a₁ − 1)²`).
   With the Cartan reading `a₁ = ±h`, `h = 1 − q⁻¹`, the neutron–proton difference is `2h`
   (`canonical_diff_cartan`). With the charge reading the neutron has `a₁ = 0 = a₂`, where
   the canonical Hamiltonian is singular (`canonicalHamiltonian_zero`); the continuous
   extension gives `h − h²` (`canonical_diff_charge_extension`).
5. `self_cartan_lt_gibbs_cell`: `2(1 − q⁻¹) < 2 log q` for `1 < q`. The Weyl-odd self term is
   strictly smaller than the existing Gibbs cell `2 E₀ log q`; `1 − q⁻¹` is the first term of
   `log q = Σ_k (1 − q⁻¹)^k / k`.

No empirical value enters this file.
-/

namespace QOU.Nuclear.NucleonDownStrandSelfEnergy

open scoped BigOperators
open CategoryTheory QOU.Core.CategoricalHamiltonianLegendre

/-- Quark flavour of a strand. -/
inductive Flavour
  | up
  | down
  deriving DecidableEq

/-! ## 1. Self sums over all strands -/

section SelfSum

variable {R : Type*} [CommRing R] {n : ℕ}

/-- The self part of a Leibniz (degree-1) operator, or of any one-strand operator, on a
product weight state with flavour assignment `f`. -/
def selfSum (ε : Flavour → R) (f : Fin n → Flavour) : R := ∑ s, ε (f s)

/-- Number of down strands. -/
def downCount (f : Fin n → Flavour) : ℕ := (Finset.univ.filter (fun s => f s = .down)).card

/-- Number of up strands. -/
def upCount (f : Fin n → Flavour) : ℕ := (Finset.univ.filter (fun s => ¬ f s = .down)).card

theorem upCount_add_downCount (f : Fin n → Flavour) : upCount f + downCount f = n := by
  unfold upCount downCount
  rw [add_comm, Finset.filter_card_add_filter_neg_card_eq_card, Finset.card_univ,
    Fintype.card_fin]

/-- The self sum depends only on the strand counts. -/
theorem selfSum_eq_counts (ε : Flavour → R) (f : Fin n → Flavour) :
    selfSum ε f = (upCount f : R) * ε .up + (downCount f : R) * ε .down := by
  unfold selfSum upCount downCount
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (fun s => f s = .down)]
  have hd : ∑ s ∈ Finset.univ.filter (fun s => f s = .down), ε (f s)
      = ∑ _s ∈ Finset.univ.filter (fun s => f s = .down), ε .down :=
    Finset.sum_congr rfl (fun s hs => by rw [(Finset.mem_filter.mp hs).2])
  have hu : ∑ s ∈ Finset.univ.filter (fun s => ¬ f s = .down), ε (f s)
      = ∑ _s ∈ Finset.univ.filter (fun s => ¬ f s = .down), ε .up := by
    refine Finset.sum_congr rfl (fun s hs => ?_)
    have h := (Finset.mem_filter.mp hs).2
    cases hf : f s with
    | up => rfl
    | down => exact absurd hf h
  rw [hd, hu, Finset.sum_const, Finset.sum_const, nsmul_eq_mul, nsmul_eq_mul]
  ring

/-- **Per-down-strand self term.** Turning strand `s` from up to down, all other strands
fixed, changes the self sum by `ε down − ε up`, for every `n` and every other assignment. -/
theorem selfSum_flip_down (ε : Flavour → R) (f g : Fin n → Flavour) (s : Fin n)
    (hfs : f s = .up) (hgs : g s = .down) (hrest : ∀ t, t ≠ s → g t = f t) :
    selfSum ε g - selfSum ε f = ε .down - ε .up := by
  unfold selfSum
  rw [← Finset.add_sum_erase Finset.univ (fun t => ε (g t)) (Finset.mem_univ s),
    ← Finset.add_sum_erase Finset.univ (fun t => ε (f t)) (Finset.mem_univ s),
    Finset.sum_congr rfl (fun t ht => by rw [hrest t (Finset.ne_of_mem_erase ht)]), hfs, hgs]
  ring

/-- **Weyl-even self terms are flavour-blind** (scope (b)). If the one-strand value is the
same on `u` and `d`, the self sum is `n · ε up` for every flavour assignment. -/
theorem selfSum_flavour_blind_of_weyl_even (ε : Flavour → R) (hW : ε .up = ε .down)
    (f : Fin n → Flavour) : selfSum ε f = (n : R) * ε .up := by
  rw [selfSum_eq_counts, ← hW, ← add_mul, ← Nat.cast_add, upCount_add_downCount]

/-- Cartan weight of a strand: `u ↦ 1`, `d ↦ −1`. -/
def weight : Flavour → R
  | .up => 1
  | .down => -1

/-- **A one-strand value splits into a Weyl-even and a Weyl-odd part**, and only the odd part
`c · w` moves with flavour: `ε = b + c · weight` with `b = (ε u + ε d)/2`, `c = (ε u − ε d)/2`
(stated without division as `2ε = (ε u + ε d) + (ε u − ε d)·w`). -/
theorem two_mul_eq_even_add_odd (ε : Flavour → R) (f : Flavour) :
    2 * ε f = (ε .up + ε .down) + (ε .up - ε .down) * weight f := by
  cases f <;> simp [weight] <;> ring

/-- The Weyl-odd self sum is `c` times the total weight `n_u − n_d`. -/
theorem selfSum_odd (c : R) (f : Fin n → Flavour) :
    selfSum (fun x => c * weight x) f = c * ((upCount f : R) - (downCount f : R)) := by
  rw [selfSum_eq_counts]; simp [weight]; ring

end SelfSum

/-! ## 2. The self term through the Legendre transform -/

section Legendre

universe u v

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
  [Preadditive C] [Linear R C] {fh : FrobeniusHopfData C}

/-- **The velocity energy does not see the Reeb-matter term** (scope (b)). With a shared Dirac
operator and the same horizontal matter trace, the two nucleons have the same traced velocity
Hamiltonian, whatever their Reeb-matter traces (the only place the Weyl-odd self term enters). -/
theorem trace_hamiltonianVel_eq_of_shared (τ : (fh.obj ⟶ fh.obj) →ₗ[R] R)
    (L_n L_p : CategoricalLagrangian R C fh) (hDirac : L_n.dirac = L_p.dirac)
    (hHoriz : τ (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) =
      τ (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo)) :
    τ (CategoricalHamiltonianVel L_n) = τ (CategoricalHamiltonianVel L_p) := by
  rw [trace_categoricalHamiltonianVel_eq, trace_categoricalHamiltonianVel_eq]
  have hsq : reebSqTerm L_n = reebSqTerm L_p := by unfold reebSqTerm; rw [hDirac]
  have hz : τ (spatialZeroTerm L_n) = τ (spatialZeroTerm L_p) := by
    unfold spatialZeroTerm
    rw [map_add, map_add, LinearMap.map_smul, LinearMap.map_smul, LinearMap.map_smul,
      LinearMap.map_smul, hHoriz, hDirac]
  rw [hsq, hz]

end Legendre

section Canonical

variable {K : Type*} [Field K]

/-- **Canonical unit-clock energy on a weight state is a perfect square.** On a product weight
vector `⟨R²⟩ = ⟨R⟩²`, so `a₂ = a₁²`, and `H = a₂ − a₁ + a₁²/(4a₂) = (a₁ − 1/2)²`, stated
without division as `4H = (2a₁ − 1)²`. -/
theorem canonical_unit_clock_weight_state (a₁ : K) (h2 : (2 : K) ≠ 0) (ha : a₁ ≠ 0) :
    4 * canonicalHamiltonian (a₁ ^ 2) a₁ 0 (2 * a₁ ^ 2) = (2 * a₁ - 1) ^ 2 := by
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by norm_num
    rw [e]; exact mul_ne_zero h2 h2
  rw [canonicalHamiltonian_unit_clock _ _ _ h2 (pow_ne_zero 2 ha)]
  field_simp [h4, ha]
  ring

/-- **Cartan reading**: `a₁ = h` (proton, weight `+1`), `a₁ = −h` (neutron, weight `−1`).
The neutron–proton difference of the canonical energy is `2h`, exactly (stated as `4·Δ = 8h`). -/
theorem canonical_diff_cartan (h : K) (h2 : (2 : K) ≠ 0) (hh : h ≠ 0) :
    4 * (canonicalHamiltonian ((-h) ^ 2) (-h) 0 (2 * (-h) ^ 2) -
      canonicalHamiltonian (h ^ 2) h 0 (2 * h ^ 2)) = 8 * h := by
  rw [mul_sub, canonical_unit_clock_weight_state _ h2 (neg_ne_zero.mpr hh),
    canonical_unit_clock_weight_state _ h2 hh]
  ring

/-- **The charge reading is singular for the neutron.** Its total charge is `0`, so `a₁ = a₂ = 0`
and the canonical Hamiltonian (with Lean's `x / 0 = 0`) is `0`, not the value `1/4` that the
perfect square `(a₁ − 1/2)²` tends to. The Legendre transform is undefined there. -/
theorem canonicalHamiltonian_zero : canonicalHamiltonian (0 : K) 0 0 (2 * 0) = 0 := by
  simp [canonicalHamiltonian]

/-- Continuous extension of the charge reading: `(2·0 − 1)² − (2h − 1)² = 4(h − h²)`. -/
theorem canonical_diff_charge_extension (h : K) :
    (2 * 0 - 1 : K) ^ 2 - (2 * h - 1) ^ 2 = 4 * (h - h ^ 2) := by ring

end Canonical

/-! ## 3. Comparison with the Gibbs cell (archimedean) -/

/-- **The Weyl-odd self term is strictly below the Gibbs cell**: `2(1 − q⁻¹) < 2 log q` for
`1 < q`. -/
theorem self_cartan_lt_gibbs_cell (q : ℝ) (hq : 1 < q) : 2 * (1 - q⁻¹) < 2 * Real.log q := by
  have hq0 : 0 < q := by linarith
  have hi0 : 0 < q⁻¹ := inv_pos.mpr hq0
  have hi1 : q⁻¹ ≠ 1 := by
    intro h
    have : q = 1 := by rw [← inv_inv q, h, inv_one]
    linarith
  have hlt := Real.log_lt_sub_one_of_pos hi0 hi1
  rw [Real.log_inv] at hlt
  linarith

/-- The charge reading is below the Cartan reading: `h − h² < 2h` for `0 < h`. -/
theorem charge_lt_cartan (h : ℝ) (hh : 0 < h) : h - h ^ 2 < 2 * h := by nlinarith

end QOU.Nuclear.NucleonDownStrandSelfEnergy
