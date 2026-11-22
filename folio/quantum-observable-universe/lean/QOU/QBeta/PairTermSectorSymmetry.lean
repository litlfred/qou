import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Equiv
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Group
import Mathlib.Tactic.NoncommRing

/-!
# The reachable pair terms are closed under `Q_A ↦ 1 − Q_B`, `Q_B ↦ 1 − Q_A`

Two nucleon blocks on six strands carry the core `C = V_A³ V_B³`, `V = σ_lo σ_{lo+1}⁻¹`. For an
insertion `X` from the Hecke image `H`, the sector response is
`T_X(s) = tr(Π_s · C · X)` and the pair shift is `ΔE_X(s) = T_X(s) / T_1(s)`. The `K^{⊗6}`
weight is a scalar on each sector and cancels in `ΔE`, so it is left out here.

**The symmetry.** Flipping every strand (`u ↔ d`) and reversing the strand order is conjugation
`θ` by a permutation matrix. It sends `σ_i` to `σ_{4−i}`, so it sends the core to its inverse
`C⁻¹ = V_B⁻³ V_A⁻³`, and the sector `(a, b)` to `(3 − b, 3 − a)`. The inverse core is conjugate
to the core inside the blocks: with the half twist `Δ = σ_lo σ_{lo+1} σ_lo`, the braid relation
gives `Δ V Δ⁻¹ = V⁻¹` (`halfTwist_conj_core`). `Δ` acts inside each block, so it commutes with
the sector projectors. Hence `θ(C) = D C D⁻¹` with `D = Δ_A Δ_B` in `H`, and
`T_X(s) = T_{X'}(σ s)` with `X' = D⁻¹ θ(X) D` again in `H` (`readout_sectorSymm`). The set of
reachable pair shifts is closed under precomposition with the sector involution.

In charges `Q = a − 1` the sector involution is `(Q_A, Q_B) ↦ (1 − Q_B, 1 − Q_A)`. It sends the
pair term `c + κ (Q_A − β)(Q_B − α)` to `c + κ (Q_A − (1 − α))(Q_B − (1 − β))`
(`pairTerm_comp_swap`). So if the reachable pair terms with `κ ≠ 0` all share one pair
`(α, β)`, then `α + β = 1` (`alpha_add_beta_eq_one_of_unique_ray`), and the Coulomb form
`α = β = 0` is not reachable (`not_coulomb_of_unique_ray`).

An insertion fixed by `X ↦ D⁻¹ θ(X) D` has equal responses on the proton pair `(1, 1)` and the
neutron pair `(0, 0)` (`readout_eq_of_fixed`). That is the structural reason the `R`-compatible
`U_q` pair Casimir and the KZ monodromy give `pp = nn`.

**Scope.** The abstract readout symmetry is proved here for any ring with a trace, an
automorphism preserving it, and the stated relations; the 64 × 64 Jimbo instances of those
relations (`J Ř_i J = Ř_{4−i}`, `J C J = C⁻¹`, `D C D⁻¹ = C⁻¹`) are verified exactly over
`ℚ(q)` by `np_pair_term_sector_symmetry_check.py`, not in Lean. The uniqueness of the reachable
ray (rank 2 of the affine-bilinear system) is the computer-algebra result of
`np_all_q_symbolic_probe.py` over `ℚ(q)` at `n = 6`; here it is a hypothesis, named in the
theorem names (`_of_unique_ray`). What this file adds is that `α + β = 1` is forced by a symmetry
of the readout rather than being a coincidence of the elimination.
-/

namespace QOU.QBeta.PairTermSectorSymmetry

/-! ### The half twist conjugates the core to its inverse -/

section Braid

variable {G : Type*} [Group G]

/-- With the braid relation `a b a = b a b`, the half twist `Δ = a b a` swaps `a` and `b`. -/
theorem halfTwist_conj_left (a b : G) (h : a * b * a = b * a * b) :
    (a * b * a) * a * (a * b * a)⁻¹ = b := by
  rw [mul_inv_eq_iff_eq_mul, show b * (a * b * a) = (b * a * b) * a by group, ← h]

theorem halfTwist_conj_right (a b : G) (h : a * b * a = b * a * b) :
    (a * b * a) * b * (a * b * a)⁻¹ = a := by
  rw [mul_inv_eq_iff_eq_mul, show a * b * a * b = a * (b * a * b) by group, ← h]

/-- The half twist conjugates `V = a b⁻¹` to `V⁻¹ = b a⁻¹`. -/
theorem halfTwist_conj_core (a b : G) (h : a * b * a = b * a * b) :
    (a * b * a) * (a * b⁻¹) * (a * b * a)⁻¹ = (a * b⁻¹)⁻¹ := by
  have hl := halfTwist_conj_left a b h
  have hr := halfTwist_conj_right a b h
  set Δ := a * b * a
  have hr' : Δ * b⁻¹ * Δ⁻¹ = a⁻¹ := by
    rw [← hr]; group
  calc Δ * (a * b⁻¹) * Δ⁻¹ = (Δ * a * Δ⁻¹) * (Δ * b⁻¹ * Δ⁻¹) := by group
    _ = b * a⁻¹ := by rw [hl, hr']
    _ = (a * b⁻¹)⁻¹ := by group

/-- Hence it conjugates every power of the core to the same power of its inverse. -/
theorem halfTwist_conj_core_pow (a b : G) (h : a * b * a = b * a * b) (n : ℕ) :
    (a * b * a) * (a * b⁻¹) ^ n * (a * b * a)⁻¹ = ((a * b⁻¹)⁻¹) ^ n := by
  rw [← halfTwist_conj_core a b h]
  induction n with
  | zero => group
  | succ n ih => rw [pow_succ, pow_succ, ← ih]; group

end Braid

/-! ### The readout is symmetric under the sector involution -/

section Readout

variable {A K ι : Type*} [Ring A]

/-- The sector response `T_X(s) = tr(P_s · C · X)`. -/
def readout (tr : A → K) (P : ι → A) (C X : A) (s : ι) : K := tr (P s * C * X)

/-- If an automorphism `θ` preserves the trace, sends the projectors to the projectors of the
involuted sectors, and sends the core to `D C D⁻¹` with `D` a unit commuting with the
projectors, then the response of `X` at `s` is the response of `D⁻¹ θ(X) D` at `σ s`. -/
theorem readout_sectorSymm (tr : A → K) (htr : ∀ x y, tr (x * y) = tr (y * x))
    (θ : A ≃+* A) (hθ : ∀ x, tr (θ x) = tr x) (P : ι → A) (σ : ι → ι)
    (hP : ∀ s, θ (P s) = P (σ s)) (C : A) (D : Aˣ)
    (hC : θ C = D * C * ↑D⁻¹) (hD : ∀ s, (D : A) * P s = P s * D) (X : A) (s : ι) :
    readout tr P C X s = readout tr P C (↑D⁻¹ * θ X * D) (σ s) := by
  unfold readout
  rw [← hθ (P s * C * X), map_mul, map_mul, hP, hC]
  -- tr(P' D C D⁻¹ θX) = tr(P' C D⁻¹ θX D)
  calc tr (P (σ s) * (↑D * C * ↑D⁻¹) * θ X)
      = tr (↑D * (P (σ s) * C * (↑D⁻¹ * θ X))) := by
          rw [← mul_assoc, ← mul_assoc, ← hD]; noncomm_ring
    _ = tr (P (σ s) * C * (↑D⁻¹ * θ X) * ↑D) := by
          rw [htr]
    _ = tr (P (σ s) * C * (↑D⁻¹ * θ X * ↑D)) := by noncomm_ring

/-- The insertion `1` maps to `1`, so the normalising response is symmetric on its own. -/
theorem readout_one_sectorSymm (tr : A → K) (htr : ∀ x y, tr (x * y) = tr (y * x))
    (θ : A ≃+* A) (hθ : ∀ x, tr (θ x) = tr x) (P : ι → A) (σ : ι → ι)
    (hP : ∀ s, θ (P s) = P (σ s)) (C : A) (D : Aˣ)
    (hC : θ C = D * C * ↑D⁻¹) (hD : ∀ s, (D : A) * P s = P s * D) (s : ι) :
    readout tr P C 1 s = readout tr P C 1 (σ s) := by
  rw [readout_sectorSymm tr htr θ hθ P σ hP C D hC hD 1 s]
  simp

/-- An insertion fixed by `X ↦ D⁻¹ θ(X) D` has the same response at `s` and at `σ s`. For the
two-block sector involution this puts the proton pair and the neutron pair in one orbit, so such
an insertion gives `pp = nn`. The `R`-compatible `U_q` pair Casimir and the KZ monodromy
`β_AB²` are fixed (`np_pair_term_sector_symmetry_check.py`, check 6); the opposite-coproduct
Casimir is not. -/
theorem readout_eq_of_fixed (tr : A → K) (htr : ∀ x y, tr (x * y) = tr (y * x))
    (θ : A ≃+* A) (hθ : ∀ x, tr (θ x) = tr x) (P : ι → A) (σ : ι → ι)
    (hP : ∀ s, θ (P s) = P (σ s)) (C : A) (D : Aˣ)
    (hC : θ C = D * C * ↑D⁻¹) (hD : ∀ s, (D : A) * P s = P s * D) (X : A)
    (hX : ↑D⁻¹ * θ X * ↑D = X) (s : ι) :
    readout tr P C X s = readout tr P C X (σ s) := by
  rw [readout_sectorSymm tr htr θ hθ P σ hP C D hC hD X s, hX]

end Readout

/-! ### Pair terms under `(Q_A, Q_B) ↦ (1 − Q_B, 1 − Q_A)` -/

section PairTerm

variable {K : Type*} [Field K]

/-- The affine-bilinear pair term `c + κ (Q_A − β)(Q_B − α)`. -/
def pairTerm (c κ α β : K) (x y : K) : K := c + κ * (x - β) * (y - α)

theorem pairTerm_comp_swap (c κ α β x y : K) :
    pairTerm c κ α β (1 - y) (1 - x) = pairTerm c κ (1 - β) (1 - α) x y := by
  unfold pairTerm; ring

/-- A pair term is determined by its values on the four charge pairs in `{0, 1}²`. -/
theorem pairTerm_params_eq (c κ α β c' κ' α' β' : K) (hκ : κ ≠ 0)
    (h : ∀ x ∈ ({0, 1} : Set K), ∀ y ∈ ({0, 1} : Set K),
      pairTerm c κ α β x y = pairTerm c' κ' α' β' x y) :
    κ = κ' ∧ α = α' ∧ β = β' := by
  have h00 := h 0 (by simp) 0 (by simp)
  have h01 := h 0 (by simp) 1 (by simp)
  have h10 := h 1 (by simp) 0 (by simp)
  have h11 := h 1 (by simp) 1 (by simp)
  unfold pairTerm at h00 h01 h10 h11
  have hk : κ = κ' := by linear_combination h11 - h10 - h01 + h00
  subst hk
  refine ⟨rfl, ?_, ?_⟩
  · have : κ * (α - α') = 0 := by linear_combination h00 - h10
    exact sub_eq_zero.mp ((mul_eq_zero.mp this).resolve_left hκ)
  · have : κ * (β - β') = 0 := by linear_combination h00 - h01
    exact sub_eq_zero.mp ((mul_eq_zero.mp this).resolve_left hκ)

/-- **`α + β = 1`.** Let `Reach` be a set of functions of the charge pair, closed under the
sector involution, and suppose every pair term in it with `κ ≠ 0` has the same `(α₀, β₀)`
(the unique-ray hypothesis). If some pair term with `κ ≠ 0` is reachable, then
`α₀ + β₀ = 1`. -/
theorem alpha_add_beta_eq_one_of_unique_ray (Reach : Set (K → K → K))
    (hswap : ∀ f ∈ Reach, (fun x y => f (1 - y) (1 - x)) ∈ Reach)
    (α₀ β₀ : K)
    (hray : ∀ c κ α β, κ ≠ 0 → pairTerm c κ α β ∈ Reach → α = α₀ ∧ β = β₀)
    (c κ α β : K) (hκ : κ ≠ 0) (hf : pairTerm c κ α β ∈ Reach) :
    α₀ + β₀ = 1 := by
  obtain ⟨hα, hβ⟩ := hray c κ α β hκ hf
  have hg : pairTerm c κ (1 - β) (1 - α) ∈ Reach := by
    have := hswap _ hf
    simpa [pairTerm_comp_swap] using this
  obtain ⟨hα', -⟩ := hray c κ (1 - β) (1 - α) hκ hg
  rw [← hα, ← hβ] at *
  linear_combination -hα'

/-- **No Coulomb pair term.** Under the same hypotheses the Coulomb form
`c + κ Q_A Q_B` (`α = β = 0`) with `κ ≠ 0` is not reachable. -/
theorem not_coulomb_of_unique_ray (Reach : Set (K → K → K))
    (hswap : ∀ f ∈ Reach, (fun x y => f (1 - y) (1 - x)) ∈ Reach)
    (α₀ β₀ : K)
    (hray : ∀ c κ α β, κ ≠ 0 → pairTerm c κ α β ∈ Reach → α = α₀ ∧ β = β₀)
    (c κ : K) (hκ : κ ≠ 0) : pairTerm c κ 0 0 ∉ Reach := by
  intro hf
  have hsum := alpha_add_beta_eq_one_of_unique_ray Reach hswap α₀ β₀ hray c κ 0 0 hκ hf
  obtain ⟨h0, h0'⟩ := hray c κ 0 0 hκ hf
  rw [← h0, ← h0'] at hsum
  norm_num at hsum

end PairTerm

end QOU.QBeta.PairTermSectorSymmetry
