import QOU.FluidDynamics.q_ns_block_haar_ibp
import CompactQuantumMetrics.OqSU2CartanPairingNondegenerate

/-!
# QOU.FluidDynamics.q_ns_block_pairing_nondegenerate — the block pairings are nondegenerate

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27); bean `qou-q3dc`
(q-NS Part A). `q_ns_block_haar_ibp` pairs the weight block `B_s = (αγ)^s K[ζ]` with
`K[ζ] (βδ)^s` through the Haar state, `(a, b) ↦ h(a b)`, and integrates by parts there. Its
"Not established" list asked whether that pairing is nondegenerate. It is.

## Results (over a field `K`, `q : Kˣ`, `q²` not a root of unity)

* `ev_mul_alphaGamma_ne_zero`: `P ≠ 0 → P(ζ) αγ ≠ 0`. Multiply by `βδ` on the right and
  use `αγ βδ = q²ζ + q³ζ²` and injectivity of `P ↦ P(ζ)` (`ev_injective`).
* `betaDelta_pow_mul_alphaGamma_pow_ne`: `(βδ)^s (αγ)^s = W_s(ζ)` with `W_s ≠ 0`.
* `block_pairing_eq`: `h(P(ζ)(βδ)^s · (αγ)^s Q(ζ)) = h((P W_s Q)(ζ))`.
* `block_pairing_nondegenerate_left` and `_right`: the pairing
  `K[ζ](βδ)^s × (αγ)^s K[ζ] → K` is nondegenerate on both sides, for every `s`.

So each weight block pairing reduces to the Cartan form (`cartan_pairing_nondegenerate`)
with weight `W_s`. Since `K[X]` is a domain, multiplying by `W_s ≠ 0` loses nothing.

## Not established

* That `L` is self-adjoint for the block pairing in the sense needed for a per-block
  little q-Jacobi basis (the parameter `α = s` family). The integration by parts of #9714
  moves `X₊` and `X₋` across the pairing, not `L` itself.
* That this budget is the q-NS transport budget (bean `qou-pa7n`).

Everything is algebraic. No empirical value enters any proof. Sorry-free.
-/

namespace QOU.FluidDynamics.BlockLadder

open Polynomial QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-- `αγ βδ = (q² X + q³ X²)(ζ)`. -/
theorem alphaGamma_betaDelta_ev :
    (α q * γ q) * (β q * δ q) =
      ev q (((q : K) * q) • X + ((q : K) * q * q) • X ^ 2) := by
  rw [alphaGamma_betaDelta, map_add, map_smul, map_smul, map_pow, ev, aeval_X, pow_two]

theorem ne_zero_qX (a b : K) (ha : a ≠ 0) : (a • X + b • X ^ 2 : K[X]) ≠ 0 := by
  intro h
  have := congrArg (fun P => P.coeff 1) h
  simp [coeff_X_pow] at this
  exact ha this

/-- `P ≠ 0 → P(ζ) αγ ≠ 0`. -/
theorem ev_mul_alphaGamma_ne_zero (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    {P : K[X]} (hP : P ≠ 0) : ev q P * (α q * γ q) ≠ 0 := by
  intro h0
  have h1 : ev q P * ((α q * γ q) * (β q * δ q)) = 0 := by rw [← mul_assoc, h0, zero_mul]
  rw [alphaGamma_betaDelta_ev, ← map_mul] at h1
  have h2 := ev_injective q hp (h1.trans (map_zero _).symm)
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  exact mul_ne_zero hP (ne_zero_qX _ _ (mul_ne_zero hq0 hq0)) h2

/-- `(βδ)^s (αγ)^s = W_s(ζ)` with `W_s ≠ 0`. -/
theorem betaDelta_pow_mul_alphaGamma_pow_ne (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    (n : ℕ) : ∃ W : K[X], W ≠ 0 ∧ (β q * δ q) ^ n * (α q * γ q) ^ n = ev q W := by
  induction n with
  | zero => exact ⟨1, one_ne_zero, by rw [pow_zero, pow_zero, mul_one, map_one]⟩
  | succ n ih =>
    obtain ⟨P, hP0, hP⟩ := ih
    obtain ⟨P', hP'⟩ := ev_mul_alphaGamma q P
    have hP'0 : P' ≠ 0 := by
      rintro rfl
      exact ev_mul_alphaGamma_ne_zero q hp hP0 (by rw [hP', map_zero, mul_zero])
    refine ⟨(X + C qi * X ^ 2) * P', mul_ne_zero ?_ hP'0, ?_⟩
    · intro h
      have := congrArg (fun P => P.coeff 1) h
      simp [coeff_X, coeff_X_pow, coeff_C_mul] at this
    · calc (β q * δ q) ^ (n + 1) * (α q * γ q) ^ (n + 1)
          = (β q * δ q) * ((β q * δ q) ^ n * (α q * γ q) ^ n) * (α q * γ q) := by
            rw [pow_succ', pow_succ]; simp only [mul_assoc]
        _ = (β q * δ q) * (α q * γ q) * ev q P' := by
            rw [hP, mul_assoc, hP', ← mul_assoc]
        _ = _ := by rw [betaDelta_alphaGamma_ev, map_mul]

/-- The block pairing is the Cartan form with weight `W_s`. -/
theorem block_pairing_eq (s : ℕ) (W : K[X]) (hW : (β q * δ q) ^ s * (α q * γ q) ^ s = ev q W)
    (P Q : K[X]) :
    ev q P * (β q * δ q) ^ s * ((α q * γ q) ^ s * ev q Q) = ev q (P * W) * ev q Q := by
  rw [map_mul, ← hW]; simp only [mul_assoc]

/-- **Nondegenerate on the left.** -/
theorem block_pairing_nondegenerate_left (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    (s : ℕ) (P : K[X])
    (h : ∀ Q : K[X], haarState q (ev q P * (β q * δ q) ^ s * ((α q * γ q) ^ s * ev q Q)) = 0) :
    P = 0 := by
  obtain ⟨W, hW0, hW⟩ := betaDelta_pow_mul_alphaGamma_pow_ne q hp s
  have h' : ∀ Q : K[X], haarState q (ev q (P * W) * ev q Q) = 0 := fun Q => by
    rw [← block_pairing_eq q s W hW]; exact h Q
  have := cartan_pairing_nondegenerate' q hp _ h'
  exact (mul_eq_zero.mp this).resolve_right hW0

/-- **Nondegenerate on the right.** -/
theorem block_pairing_nondegenerate_right (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    (s : ℕ) (Q : K[X])
    (h : ∀ P : K[X], haarState q (ev q P * (β q * δ q) ^ s * ((α q * γ q) ^ s * ev q Q)) = 0) :
    Q = 0 := by
  obtain ⟨W, hW0, hW⟩ := betaDelta_pow_mul_alphaGamma_pow_ne q hp s
  have h' : ∀ P : K[X], haarState q (ev q (Q * W) * ev q P) = 0 := fun P => by
    have := h P
    rw [block_pairing_eq q s W hW, ← map_mul] at this
    rw [← map_mul, show Q * W * P = P * W * Q by ring]
    exact this
  have := cartan_pairing_nondegenerate' q hp _ h'
  exact (mul_eq_zero.mp this).resolve_right hW0

end QOU.FluidDynamics.BlockLadder
