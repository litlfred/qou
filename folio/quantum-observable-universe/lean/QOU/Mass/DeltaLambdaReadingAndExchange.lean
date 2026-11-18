import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic

/-!
# The `Δ_λ`-weighted binding functional: reading, complement identity, and exchange

Owner pick (2026-10-11, "2"): investigate the `Δ_λ` binding law — its reading and the
`pn ≠ np` asymmetry. Companion probe:
`computations/probes/delta_lambda_binding_reading_probe.py` (and its witness).

The functional is `Φ(X) = Σ_λ y_λ χ^λ(X) Δ_λ` with `Δ_λ = (−1)^{n(λ)} dim V_λ` (value
proved, `dtEuler_eq_deltaLambda_unconditional`; the binding LAW is posited —
`computations/delta-lambda-witness.json`: "NOT a binding energy"). Nothing here asserts a
value of any trace, and nothing selects a reading.

## What is proved (all over a generic ring, except §4)

1. `weighted_traces_cyclic` — any weighted sum `Σ c_λ χ^λ` of traces is cyclic, and
   `cyclic_conj_invariant` — a cyclic functional is invariant under conjugation by an
   invertible element. So `Φ(ab) = Φ(ba)` and `Φ(g x g⁻¹) = Φ(x)` hold for `Φ` exactly as for
   `tr_M`: the `Δ_λ` weights cannot break cyclicity. The `pn ≠ np` asymmetry is therefore NOT
   a failure of cyclicity.
2. `complement_identity` / `complement_identity_finset` — if `Σ_j P_j = 1` then
   `Φ(w) − Φ(w P_i) = Σ_{j ≠ i} Φ(w P_j)` for every additive `Φ` and every `w`. At the
   two-channel interface (`P₊ + P₋ = 1`) this is `Φ(w) − Φ(w P₊) = Φ(w P₋)`, for EVERY word
   `w`, not only at `n = 2`.
3. `diff_eq_neg_dir_complement` — consequently the difference reading of channel `T` equals
   the negated corpus-direct reading of the COMPLEMENTARY channel, and
   `diff_sub_dir_eq_free` — the difference reading and the corpus-direct reading differ by
   exactly `m_e Φ(free)`, so they coincide iff the free baseline vanishes.
4. `dir_diff_same_sign` (ordered ring) — the corpus-direct (`B = −m_e Φ(atom)`, the sign fixed
   by `Binding(K)` being ADDED to the constituent mass) and difference readings give the same
   sign on both channels whenever `Φ(w P₊) > 0 > Φ(w P₋)`.
5. `markov_factorising_order_blind` — a functional with the Markov factorisation
   `τ(x b) = z τ(x)` on a subalgebra, invariant under an exchange `θ` of that subalgebra, gives
   `τ(θ x · b) = τ(x · b)`: it cannot see the block order. This is why `tr_M` has `pn = np` at
   the interface letter; `Φ` has no such factorisation (measured, not proved here), so the
   exchange that fixes the interface letter — the half twist — relates `pn` to the
   in-block-MIRRORED `np`, not to `np` itself.
-/

namespace QOU.Mass.DeltaLambdaReadingAndExchange

open scoped BigOperators

section Cyclic

variable {ι R A : Type*} [CommRing R] [Ring A]

/-- A weighted sum of cyclic functionals is cyclic. -/
theorem weighted_traces_cyclic (s : Finset ι) (c : ι → R) (χ : ι → A → R)
    (hχ : ∀ i a b, χ i (a * b) = χ i (b * a)) (a b : A) :
    ∑ i ∈ s, c i * χ i (a * b) = ∑ i ∈ s, c i * χ i (b * a) :=
  Finset.sum_congr rfl fun i _ => by rw [hχ i a b]

omit [CommRing R] in
/-- A cyclic functional is invariant under conjugation `x ↦ u x v` with `v u = 1`. -/
theorem cyclic_conj_invariant (τ : A → R) (hτ : ∀ a b, τ (a * b) = τ (b * a))
    (u v x : A) (hvu : v * u = 1) : τ (u * x * v) = τ x := by
  rw [hτ (u * x) v, ← mul_assoc, hvu, one_mul]

end Cyclic

section Complement

variable {ι R A : Type*} [CommRing R] [Ring A]

/-- Two-channel complement identity: `P + Q = 1 ⟹ Φ w − Φ (w P) = Φ (w Q)`. -/
theorem complement_identity (Φ : A →+ R) (P Q w : A) (hPQ : P + Q = 1) :
    Φ w - Φ (w * P) = Φ (w * Q) := by
  have hQ : Q = 1 - P := by rw [← hPQ]; abel
  rw [hQ, mul_sub, mul_one, map_sub]

/-- Finite-family complement identity: `Σ_j P_j = 1 ⟹ Φ w − Φ (w P_i) = Σ_{j ≠ i} Φ (w P_j)`. -/
theorem complement_identity_finset [DecidableEq ι] (Φ : A →+ R) (s : Finset ι) (P : ι → A) (w : A)
    (hsum : ∑ j ∈ s, P j = 1) {i : ι} (hi : i ∈ s) :
    Φ w - Φ (w * P i) = ∑ j ∈ s.erase i, Φ (w * P j) := by
  have h1 : Φ w = ∑ j ∈ s, Φ (w * P j) := by
    rw [← map_sum, ← Finset.mul_sum, hsum, mul_one]
  rw [h1, ← Finset.add_sum_erase s _ hi]
  ring

/-- The difference reading of a channel is the negated corpus-direct reading of the
complementary channel. -/
theorem diff_eq_neg_dir_complement (Φ : A →+ R) (me : R) (P Q w : A) (hPQ : P + Q = 1) :
    me * (Φ w - Φ (w * P)) = -(-me * Φ (w * Q)) := by
  rw [complement_identity Φ P Q w hPQ]; ring

/-- Difference reading minus corpus-direct reading is exactly the free baseline. -/
theorem diff_sub_dir_eq_free (me Φfree Φatom : R) :
    me * (Φfree - Φatom) - (-me * Φatom) = me * Φfree := by ring

/-- The two readings coincide iff the free baseline vanishes. -/
theorem diff_eq_dir_iff (me Φfree Φatom : R) :
    me * (Φfree - Φatom) = -me * Φatom ↔ me * Φfree = 0 := by
  constructor
  · intro h; linear_combination h
  · intro h; linear_combination h

end Complement

section Sign

variable {R A : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [Ring A]

/-- If the two channel pieces have opposite signs, `Φ(wP₊) > 0 > Φ(wP₋)`, the corpus-direct
and difference readings agree in sign on both channels: `P₊` unbound, `P₋` bound. -/
theorem dir_diff_same_sign (Φ : A →+ R) (me : R) (hme : 0 < me) (Pp Pm w : A)
    (hPQ : Pp + Pm = 1) (hp : 0 < Φ (w * Pp)) (hm : Φ (w * Pm) < 0) :
    (-me * Φ (w * Pp) < 0 ∧ me * (Φ w - Φ (w * Pp)) < 0) ∧
    (0 < -me * Φ (w * Pm) ∧ 0 < me * (Φ w - Φ (w * Pm))) := by
  have hc1 := complement_identity Φ Pp Pm w hPQ
  have hc2 := complement_identity Φ Pm Pp w (by rw [add_comm]; exact hPQ)
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · nlinarith
  · rw [hc1]; nlinarith
  · nlinarith
  · rw [hc2]; nlinarith

end Sign

section Markov

variable {R A : Type*} [CommRing R] [Ring A]

/-- A Markov-factorising functional is blind to an exchange of the subalgebra it factorises
over: `τ(θ x · b) = τ(x · b)`. -/
theorem markov_factorising_order_blind (τ : A → R) (S : Set A) (b : A) (z : R)
    (hM : ∀ x ∈ S, τ (x * b) = z * τ x) (θ : A → A) (hθS : ∀ x ∈ S, θ x ∈ S)
    (hτθ : ∀ x ∈ S, τ (θ x) = τ x) {x : A} (hx : x ∈ S) :
    τ (θ x * b) = τ (x * b) := by
  rw [hM _ (hθS x hx), hM x hx, hτθ x hx]

end Markov


section ZeroFree

variable {R : Type*} [CommRing R]

/-- **Zero-baseline specialization of `diff_sub_dir_eq_free` (`qou-03fc`).**
When the free baseline `Φfree = 0`, the difference reading minus the direct reading vanishes. -/
theorem diff_sub_dir_zero_free (me Φatom : R) :
    me * ((0 : R) - Φatom) - (-me * Φatom) = 0 := by
  rw [diff_sub_dir_eq_free me 0 Φatom, mul_zero]

end ZeroFree

end QOU.Mass.DeltaLambdaReadingAndExchange
