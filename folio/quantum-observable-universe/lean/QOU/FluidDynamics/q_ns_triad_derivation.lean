import QOU.FluidDynamics.q_ns_triad_core
import Mathlib.RingTheory.Derivation.Basic

/-!
# QOU.FluidDynamics.q_ns_triad_derivation

Bean `qou-q3dc`, owner route "q-Clebsch–Gordan coefficients" (2026-11-27).

`q_ns_modal_triad.lean` **assumed** the triad-wise energy conservation of the
couplings (field `TriadCoeff.conserve`). This file **derives** it from the
structure of the corpus nonlinearity `μ ∘ (v ⊗ ∇_q v)` (`def:q-navier-stokes`).

## The chain

1. **Transport skewness (`transport_skew`).** For any derivation `X` of a
   commutative algebra with a trace `τ` that kills `X` (incompressibility,
   `τ ∘ X = 0`), `τ(u · X u) = 0`. The proof is the Leibniz rule:
   `X(u²) = 2u·Xu`.
2. **The q-connection is a derivation (`qField`).** The corpus field
   `∇_q = q⁻¹∇ + (1 − q⁻¹)(ι_ξ∇)Θ` (`def:categorical-q-connection`) is a
   linear combination, with algebra coefficients, of derivations, so it is one
   by construction. Its incompressibility is the hypothesis `δ_q v = 0` of
   `def:q-navier-stokes`, and is carried as such.
3. **Modal couplings (`modalD`).** For a mode family `e`, set
   `Dₙₚᵣ = τ(eₙ · Xₚ eᵣ) / τ(eₙ²)`. Skewness gives
   `wₙ Dₙₚᵣ + wᵣ Dᵣₚₙ = 0` (`modalD_skew`).
4. **Kraichnan conservation (`ofTransportSkew`).** Symmetrising in the pair
   turns pairwise skewness into the cyclic identity
   `wₙ Cₙₚᵣ + wₚ Cₚᵣₙ + wᵣ Cᵣₙₚ = 0`. So the `conserve` field of `TriadCoeff`
   is now a theorem about the corpus nonlinearity, not an assumption.
5. **The transfer is the advection (`transfer_eq_advection`).** With
   `τ`-orthogonal modes, the `n`-th modal coordinate of `X_v u`, where
   `X_v = ∑ₚ aₚ Xₚ` and `u = ∑ᵣ aᵣ eᵣ`, equals the Galerkin transfer `Tₙ(a)`.
   The energy is the Parseval sum `τ(u²) = ∑ wₙ aₙ²` (`parseval`).

## What stays a hypothesis

* **Selection rule (`hsel`).** `τ(eₙ · Xₚ eᵣ) = 0` unless
  `V_n ⊂ V_p ⊗ V_r`. This is the Clebsch–Gordan rule for `SU_q(2)` at generic
  `q`. It is not derived here, and it is named wherever it is used.
* **Incompressibility (`hdiv`)** of each transport mode, as in the corpus.
* **The numerical values of the couplings.** These need the
  `q`-Clebsch–Gordan / `6j` coefficients and are not computed here.

* **Commutativity and a trace.** `A` is commutative, and only the identity
  `τ(X(u²)) = 0` is used. This covers the archimedean realisation, where `∇_q`
  acts on the commutative function algebra of the state bundle. It does **not**
  cover the noncommutative coordinate algebra `O_q(SU(2))`. There the Haar
  state is not a trace: it satisfies `h(ab) = h(b σ(a))` with a nontrivial
  modular automorphism `σ`. So `τ(X(u²)) = 2τ(u X u)` can fail, and triad
  conservation would need a twisted Leibniz rule. Whether the energy is
  conserved in the noncommutative picture is open (bean `qou-q3dc`).

The model is scalar: one amplitude per mode. The three-component velocity is
the same argument summed over components.

No empirical value enters any proof.

## References

- [leitner2026] fluid-dynamics/q-navier-stokes.md (`def:q-navier-stokes`)
- [leitner2026] quantum-observable-universes/categorical-q-connection.md
  (`def:categorical-q-connection`)
-/

namespace QOU.FluidDynamics.ModalTriad

open Finset

variable {K : Type*} [Field K]

/-! ### Pairwise skewness implies Kraichnan conservation -/

/-- Couplings that are pairwise skew in the (output, advected) slots give a
    triad system once symmetrised in the pair. -/
noncomputable def ofTransportSkew (w : ℕ → K) (D : ℕ → ℕ → ℕ → K)
    (hsel : ∀ n p r, ¬ FusionTriad n p r → D n p r = 0)
    (hskew : ∀ n p r, w n * D n p r + w r * D r p n = 0) : TriadCoeff K where
  w := w
  C n p r := (D n p r + D n r p) / 2
  supp n p r h := by
    have h' : ¬ FusionTriad n r p := fun h' => h h'.swap
    rw [hsel n p r h, hsel n r p h']; ring
  symm n p r := by ring
  conserve n p r := by
    linear_combination (hskew n p r + hskew n r p + hskew p n r) / 2

/-- A bilinear form vanishing on the diagonal of a finite mode set is skew. -/
theorem skew_of_diag (w : ℕ → K) (D : ℕ → ℕ → ℕ → K)
    (h : ∀ (S : Finset ℕ) (a : ℕ → K) (p : ℕ),
      ∑ n ∈ S, ∑ r ∈ S, w n * D n p r * a n * a r = 0)
    (n p r : ℕ) : w n * D n p r + w r * D r p n = 0 := by
  have hn := h {n} (fun _ => 1) p
  have hr := h {r} (fun _ => 1) p
  simp only [sum_singleton, mul_one] at hn hr
  by_cases hnr : n = r
  · subst hnr; rw [hn]; ring
  · have hp := h {n, r} (fun _ => 1) p
    simp only [sum_pair hnr, mul_one] at hp
    linear_combination hp - hn - hr

/-! ### Transport skewness from the Leibniz rule -/

section Derivation

variable {A : Type*} [CommRing A] [Algebra K A]

/-- **Transport skewness.** A divergence-free derivation does no work:
    `τ(u · X u) = 0`. -/
theorem transport_skew (X : Derivation K A A) (τ : A →ₗ[K] K)
    (hdiv : ∀ f, τ (X f) = 0) (h2 : (2 : K) ≠ 0) (u : A) :
    τ (u * X u) = 0 := by
  have hL : X (u * u) = u * X u + u * X u := by
    rw [X.leibniz]; simp only [smul_eq_mul]
  have h0 := hdiv (u * u)
  rw [hL, map_add] at h0
  have : (2 : K) * τ (u * X u) = 0 := by rw [two_mul]; exact h0
  exact (mul_eq_zero.mp this).resolve_left h2

/-- **Polarised transport skewness**: `τ(f · X g) + τ(g · X f) = 0`. -/
theorem transport_skew_pair (X : Derivation K A A) (τ : A →ₗ[K] K)
    (hdiv : ∀ f, τ (X f) = 0) (h2 : (2 : K) ≠ 0) (f g : A) :
    τ (f * X g) + τ (g * X f) = 0 := by
  have hfg := transport_skew X τ hdiv h2 (f + g)
  have hf := transport_skew X τ hdiv h2 f
  have hg := transport_skew X τ hdiv h2 g
  simp only [map_add, add_mul, mul_add] at hfg
  linear_combination hfg - hf - hg

/-- **The corpus q-connection field is a derivation**:
    `q⁻¹ X + (1 − q⁻¹) θ ξ`, with `X` the connection field, `ξ` the Reeb
    derivation and `θ = Θ(X)` the contact component. A derivation by
    construction. -/
def qField (q : K) (X ξ : Derivation K A A) (θ : A) : Derivation K A A :=
  q⁻¹ • X + (1 - q⁻¹) • (θ • ξ)

theorem qField_apply (q : K) (X ξ : Derivation K A A) (θ f : A) :
    qField q X ξ θ f = q⁻¹ • X f + (1 - q⁻¹) • (θ * ξ f) := by
  simp [qField, smul_eq_mul]

/-- `qField` is divergence-free when both of its parts are. -/
theorem qField_div_free (q : K) (X ξ : Derivation K A A) (θ : A) (τ : A →ₗ[K] K)
    (hX : ∀ f, τ (X f) = 0) (hξ : ∀ f, τ (θ * ξ f) = 0) (f : A) :
    τ (qField q X ξ θ f) = 0 := by
  rw [qField_apply, map_add, map_smul, map_smul, hX, hξ]; simp

/-! ### Modal couplings of an advection -/

/-- Modal couplings `Dₙₚᵣ = τ(eₙ · Xₚ eᵣ) / τ(eₙ²)`. -/
noncomputable def modalD (τ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → Derivation K A A)
    (n p r : ℕ) : K :=
  τ (e n * X p (e r)) / τ (e n * e n)

/-- Parseval weights `wₙ = τ(eₙ²)`. -/
def modalW (τ : A →ₗ[K] K) (e : ℕ → A) (n : ℕ) : K := τ (e n * e n)

theorem modalD_skew (τ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → Derivation K A A)
    (hdiv : ∀ p f, τ (X p f) = 0) (h2 : (2 : K) ≠ 0)
    (hw : ∀ n, modalW τ e n ≠ 0) (n p r : ℕ) :
    modalW τ e n * modalD τ e X n p r + modalW τ e r * modalD τ e X r p n = 0 := by
  unfold modalD modalW at *
  rw [mul_div_cancel₀ _ (hw n), mul_div_cancel₀ _ (hw r)]
  exact transport_skew_pair (X p) τ (hdiv p) h2 (e n) (e r)

/-- **The triad system of a divergence-free advection.** The conservation field
    is proved from the Leibniz rule; only the selection rule is assumed. -/
noncomputable def advectionTriad (τ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → Derivation K A A)
    (hdiv : ∀ p f, τ (X p f) = 0) (h2 : (2 : K) ≠ 0)
    (hw : ∀ n, modalW τ e n ≠ 0)
    (hsel : ∀ n p r, ¬ FusionTriad n p r → τ (e n * X p (e r)) = 0) : TriadCoeff K :=
  ofTransportSkew (modalW τ e) (modalD τ e X)
    (fun n p r h => by simp [modalD, hsel n p r h])
    (modalD_skew τ e X hdiv h2 hw)

/-- **Parseval** for `τ`-orthogonal modes: `τ(u²) = ∑ wₙ aₙ²`. -/
theorem parseval (τ : A →ₗ[K] K) (e : ℕ → A)
    (horth : ∀ m n, m ≠ n → τ (e m * e n) = 0) (S : Finset ℕ) (a : ℕ → K) :
    τ ((∑ n ∈ S, a n • e n) * (∑ n ∈ S, a n • e n)) =
      ∑ n ∈ S, modalW τ e n * a n ^ 2 := by
  simp only [sum_mul, mul_sum, smul_mul_smul_comm, map_sum, map_smul, smul_eq_mul]
  refine sum_congr rfl fun m _ => ?_
  rw [sum_eq_single m]
  · unfold modalW; ring
  · intro n _ hnm; rw [horth n m hnm]; ring
  · intro hm; exact absurd ‹m ∈ S› hm

/-- **The Galerkin transfer is the advection.** For `τ`-orthogonal modes, the
    `n`-th modal coordinate of `X_v u`, with `X_v = ∑ₚ aₚ Xₚ` and
    `u = ∑ᵣ aᵣ eᵣ`, is the transfer of `advectionTriad`. -/
theorem transfer_eq_advection (τ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → Derivation K A A)
    (hdiv : ∀ p f, τ (X p f) = 0) (h2 : (2 : K) ≠ 0)
    (hw : ∀ n, modalW τ e n ≠ 0)
    (hsel : ∀ n p r, ¬ FusionTriad n p r → τ (e n * X p (e r)) = 0)
    (S : Finset ℕ) (a : ℕ → K) (n : ℕ) :
    τ (e n * (∑ p ∈ S, a p • X p) (∑ r ∈ S, a r • e r)) / modalW τ e n =
      transfer (advectionTriad τ e X hdiv h2 hw hsel) S a n := by
  have hX : ∀ g : A, (∑ p ∈ S, a p • X p) g = ∑ p ∈ S, a p • X p g := by
    intro g
    induction S using Finset.induction_on with
    | empty => simp
    | insert x s hx ih =>
      rw [sum_insert hx, sum_insert hx, Derivation.add_apply, Derivation.smul_apply, ih]
  have hlhs : τ (e n * (∑ p ∈ S, a p • X p) (∑ r ∈ S, a r • e r)) =
      ∑ p ∈ S, ∑ r ∈ S, a p * a r * τ (e n * X p (e r)) := by
    rw [hX]
    simp only [map_sum, map_smul, mul_sum, mul_smul_comm, smul_eq_mul]
    refine sum_congr rfl fun p _ => sum_congr rfl fun r _ => ?_
    rw [(X p).map_smul, mul_smul_comm, map_smul, smul_eq_mul]
    ring
  -- the symmetrised sum equals the unsymmetrised one
  have hsym : (∑ p ∈ S, ∑ r ∈ S, modalD τ e X n r p * a p * a r) =
      ∑ p ∈ S, ∑ r ∈ S, modalD τ e X n p r * a p * a r := by
    rw [Finset.sum_comm]
    refine sum_congr rfl fun p _ => sum_congr rfl fun r _ => ?_
    ring
  have hsplit : (∑ p ∈ S, ∑ r ∈ S,
      (modalD τ e X n p r + modalD τ e X n r p) / 2 * a p * a r) =
      ((∑ p ∈ S, ∑ r ∈ S, modalD τ e X n p r * a p * a r) +
        ∑ p ∈ S, ∑ r ∈ S, modalD τ e X n r p * a p * a r) / 2 := by
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun p _ => ?_
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun r _ => ?_
    ring
  simp only [transfer, advectionTriad, ofTransportSkew]
  rw [hlhs, hsplit, hsym, ← two_mul, mul_div_cancel_left₀ _ h2, sum_div]
  refine sum_congr rfl fun p _ => ?_
  rw [sum_div]
  refine sum_congr rfl fun r _ => ?_
  simp only [modalD, modalW]
  ring

end Derivation

end QOU.FluidDynamics.ModalTriad
