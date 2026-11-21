import QOU.Knot.WhiteheadBraidVolumeConjecture
import Mathlib.Algebra.Polynomial.Laurent

/-!
# The normalised Whitehead coloured Jones is an integer Laurent polynomial

`WhiteheadBraidVolumeConjecture` defines the value of `[N]⁻¹ J_N(β)` at the Kashaev point as a
punctured limit, because `[N] = 0` there. This file removes that caveat: there is an integer
Laurent polynomial `P_N ∈ ℤ[s, s⁻¹]` (`s = q`) such that

* at every `σ` where the braid-closure construction is defined, `[N]⁻¹ J_N(p)(σ) = P_N(σ²)` for
  every braid `p` Markov-equivalent to the Whitehead braid (`braidJonesRT_eq_laurent`);
* `P_N(e^{πi/N}) = whiteheadLinkKashaev N` (`laurent_at_kashaev_point`).

So the value at the Kashaev point is the evaluation of a Laurent polynomial, as in the standard
definition of the Kashaev invariant, and the volume limit is a statement about that evaluation
(`whiteheadLaurent_volume_conjecture`).

The only non-polynomial piece of van der Veen's formula is the clasp ratio
`∏_{j<n} (1 − t^{k+j+1}) / (1 − t^{j+1})`, which is the Gaussian binomial `[n+k choose n]_t`.
`gaussG` is that binomial, built from the q-Pascal recurrence, and `prod_mul_gaussG` proves
`∏_{j<n}(1 − x^{j+1}) · G_{n,k}(x) = ∏_{j<n}(1 − x^{k+j+1})` over any commutative ring.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. IV.2 (Gaussian binomials)
-/

namespace QOU.Knot.FigureEightVolume

open Polynomial Finset
open QOU.Mass.QuantumSl2
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.IwahoriHecke.BraidGroup (BraidGroupN)
open QOU.Torsion.MassTraceMarkovClass (artinTower)
open QOU.MathlibExt.MarkovMoves

/-! ### The Gaussian binomial -/

/-- The Gaussian binomial `G_{n,k} = [n+k choose n]_x ∈ ℤ[x]`, by the q-Pascal recurrence
`G_{n+1,k+1} = G_{n,k+1} + x^{n+1} G_{n+1,k}`. -/
noncomputable def gaussG : ℕ → ℕ → ℤ[X]
  | 0, _ => 1
  | _ + 1, 0 => 1
  | n + 1, k + 1 => gaussG n (k + 1) + X ^ (n + 1) * gaussG (n + 1) k

/-- **The Gaussian binomial clears the clasp denominators**, over any commutative ring:
`∏_{j<n}(1 − x^{j+1}) · G_{n,k}(x) = ∏_{j<n}(1 − x^{k+j+1})`. -/
theorem prod_mul_gaussG {R : Type*} [CommRing R] (x : R) :
    ∀ n k : ℕ, (∏ j ∈ range n, (1 - x ^ (j + 1))) * (gaussG n k).eval₂ (Int.castRingHom R) x
      = ∏ j ∈ range n, (1 - x ^ (k + j + 1))
  | 0, k => by simp [gaussG]
  | n + 1, 0 => by simp [gaussG]
  | n + 1, k + 1 => by
    have h1 := prod_mul_gaussG x n (k + 1)
    have h2 := prod_mul_gaussG x (n + 1) k
    have hP : ∏ j ∈ range (n + 1), (1 - x ^ (j + 1))
        = (∏ j ∈ range n, (1 - x ^ (j + 1))) * (1 - x ^ (n + 1)) := prod_range_succ _ _
    have hB : ∏ j ∈ range (n + 1), (1 - x ^ (k + j + 1))
        = (∏ j ∈ range n, (1 - x ^ (k + 1 + j + 1))) * (1 - x ^ (k + 1)) := by
      rw [prod_range_succ']
      congr 1
      exact prod_congr rfl fun j _ => by rw [show k + (j + 1) + 1 = k + 1 + j + 1 by omega]
    have hT : ∏ j ∈ range (n + 1), (1 - x ^ (k + 1 + j + 1))
        = (∏ j ∈ range n, (1 - x ^ (k + 1 + j + 1))) * (1 - x ^ (k + 1 + n + 1)) :=
      prod_range_succ _ _
    rw [hP, hB] at h2
    simp only [gaussG, eval₂_add, eval₂_mul, eval₂_X_pow]
    rw [hP, hT]
    linear_combination (1 - x ^ (n + 1)) * h1 + x ^ (n + 1) * h2

/-! ### The clasp product as a Laurent polynomial -/

/-- The clasp product of van der Veen's formula is a Laurent monomial product times the
Gaussian binomial at `t = s²`, wherever its denominators are nonzero. -/
theorem clasp_prod_eq {s : ℂ} {N n k : ℕ}
    (hden : ∀ j ∈ range n, 1 - s ^ (2 * ((j : ℤ) + 1)) ≠ 0) :
    ∏ j ∈ range n,
        (1 - s ^ (2 * ((N : ℤ) - ((j : ℤ) + 1) - k))) * (1 - s ^ (2 * ((j : ℤ) + 1 + k)))
          / (1 - s ^ (2 * ((j : ℤ) + 1)))
      = (∏ j ∈ range n, (1 - s ^ (2 * ((N : ℤ) - ((j : ℤ) + 1) - k))))
          * (gaussG n k).eval₂ (Int.castRingHom ℂ) (s ^ 2) := by
  have hpow : ∀ a : ℕ, s ^ (2 * (a : ℤ)) = (s ^ 2) ^ a := fun a => by
    rw [← zpow_natCast, ← zpow_natCast, ← zpow_mul]; push_cast; ring_nf
  have hD : ∏ j ∈ range n, (1 - (s ^ 2) ^ (j + 1)) ≠ 0 := by
    rw [prod_ne_zero_iff]
    intro j hj
    have := hden j hj
    rwa [show (2 * ((j : ℤ) + 1)) = 2 * ((j + 1 : ℕ) : ℤ) by push_cast; ring, hpow] at this
  rw [prod_div_distrib, prod_mul_distrib, mul_div_assoc]
  congr 1
  rw [div_eq_iff (by
    convert hD using 2 with j hj
    rw [show (2 * ((j : ℤ) + 1)) = 2 * ((j + 1 : ℕ) : ℤ) by push_cast; ring, hpow])]
  have key := prod_mul_gaussG (s ^ 2) n k
  have lhs : ∏ j ∈ range n, (1 - s ^ (2 * ((j : ℤ) + 1 + k)))
      = ∏ j ∈ range n, (1 - (s ^ 2) ^ (k + j + 1)) := by
    refine prod_congr rfl fun j _ => ?_
    rw [show (2 * ((j : ℤ) + 1 + k)) = 2 * ((k + j + 1 : ℕ) : ℤ) by push_cast; ring, hpow]
  have rhs : ∏ j ∈ range n, (1 - s ^ (2 * ((j : ℤ) + 1)))
      = ∏ j ∈ range n, (1 - (s ^ 2) ^ (j + 1)) := by
    refine prod_congr rfl fun j _ => ?_
    rw [show (2 * ((j : ℤ) + 1)) = 2 * ((j + 1 : ℕ) : ℤ) by push_cast; ring, hpow]
  rw [lhs, rhs, ← key, mul_comm]

/-! ### The Laurent polynomial -/

open LaurentPolynomial in
/-- van der Veen's formula as an integer Laurent polynomial in `s` (`s = q`, `t = s²`). -/
noncomputable def whiteheadLaurent (N : ℕ) : LaurentPolynomial ℤ :=
  ∑ n ∈ range N,
    (∑ j ∈ range (2 * n + 1), T ((N : ℤ) * (2 * (n : ℤ) - 2 * (j : ℤ)))) *
      (T (((N : ℤ) ^ 2 - 1) + (N : ℤ) * ((N : ℤ) - 1)) *
        ∑ k ∈ range (N - n), T (-(2 * (N : ℤ) * ((n : ℤ) + k))) *
          ((∏ j ∈ range n, (1 - T (2 * ((N : ℤ) - ((j : ℤ) + 1) - k)))) *
            Polynomial.toLaurent ((gaussG n k).comp (X ^ 2))))

/-- Evaluation of a Laurent polynomial at a nonzero complex number. -/
noncomputable def evalL (s : ℂ) (hs : s ≠ 0) : LaurentPolynomial ℤ →+* ℂ :=
  LaurentPolynomial.eval₂ (Int.castRingHom ℂ) (Units.mk0 s hs)

theorem evalL_T (s : ℂ) (hs : s ≠ 0) (m : ℤ) : evalL s hs (LaurentPolynomial.T m) = s ^ m := by
  rw [evalL, LaurentPolynomial.eval₂_T, Units.val_zpow_eq_zpow_val, Units.val_mk0]

/-- **van der Veen's formula is the evaluation of `whiteheadLaurent N`** at every `s ≠ 0` with
`s^{2i} ≠ 1` for `1 ≤ i < N`. -/
theorem vdvWhiteheadLinkJones_eq_laurent {s : ℂ} (hs : s ≠ 0) {N : ℕ}
    (hroot : ∀ i : ℕ, 1 ≤ i → i < N → 1 - s ^ (2 * (i : ℤ)) ≠ 0) :
    vdvWhiteheadLinkJones s N = evalL s hs (whiteheadLaurent N) := by
  unfold vdvWhiteheadLinkJones whiteheadLaurent
  rw [map_sum]
  refine sum_congr rfl fun n hn => ?_
  have hn := mem_range.mp hn
  unfold vdvBeltFused vdvClasp
  simp only [map_mul, map_sum, map_prod, map_sub, map_one, evalL_T]
  congr 2
  refine sum_congr rfl fun k _ => ?_
  congr 1
  rw [clasp_prod_eq fun j hj => by
    have := hroot (j + 1) (by omega) (by have := mem_range.mp hj; omega)
    push_cast at this
    exact this]
  congr 1
  rw [evalL, LaurentPolynomial.eval₂_toLaurent, Polynomial.eval₂_comp]
  simp [Units.val_mk0]

/-! ### The braid invariant and the Kashaev point -/

/-- At a generic `σ`, `s = σ²` avoids the clasp denominators. -/
theorem braidGeneric_root {m : ℕ} {σ : ℂ} (h : BraidGeneric m σ) :
    ∀ i : ℕ, 1 ≤ i → i < m + 1 → 1 - (σ ^ 2) ^ (2 * (i : ℤ)) ≠ 0 := by
  intro i hi1 hi2 h0
  have hq := h.2.2 i (by omega) (by omega)
  have hq0 : σ ^ 2 ≠ 0 := pow_ne_zero 2 h.1
  apply hq
  have h1 : (σ ^ 2) ^ (2 * i) = 1 := by
    have := (sub_eq_zero.mp h0).symm
    rwa [show (2 * (i : ℤ)) = ((2 * i : ℕ) : ℤ) by push_cast; ring, zpow_natCast] at this
  have hi0 : (σ ^ 2) ^ i ≠ 0 := pow_ne_zero i hq0
  rw [qint, div_eq_zero_iff]
  left
  rw [sub_eq_zero, inv_pow]
  have : (σ ^ 2) ^ i * (σ ^ 2) ^ i = 1 := by rw [← pow_add, ← two_mul, h1]
  exact (eq_inv_of_mul_eq_one_left this)

/-- **The normalised coloured Jones of the Whitehead braid is a Laurent polynomial in `q`.** For
every braid `p` Markov-equivalent to the Whitehead braid and every `σ` where the construction is
defined, `[N]⁻¹ J_N(p)(σ) = P_N(σ²)` with `P_N = whiteheadLaurent N ∈ ℤ[q, q⁻¹]`. -/
theorem braidJonesRT_eq_laurent {m : ℕ} {p : Tot BraidGroupN}
    (hp : QOU.MathlibExt.MarkovMoves.MarkovEquiv
      QOU.Torsion.MassTraceMarkovClass.artinTower ⟨2, whiteheadWord⟩ p)
    {σ : ℂ} (h : BraidGeneric m σ) :
    braidJonesRT m p σ = evalL (σ ^ 2) (pow_ne_zero 2 h.1) (whiteheadLaurent (m + 1)) := by
  rw [braidJonesRT_eq_vdv hp h, vdvWhiteheadLinkJones_eq_laurent _ (braidGeneric_root h)]

/-- **At the Kashaev point the Laurent polynomial takes the Kashaev value.** -/
theorem laurent_at_kashaev_point {N : ℕ} (hN : 1 ≤ N) :
    evalL (Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)) (Complex.exp_ne_zero _)
        (whiteheadLaurent N) = whiteheadLinkKashaev N := by
  rw [← vdvWhiteheadLinkJones_eq_laurent _ fun i h1 h2 => kashaev_pow_ne_one h1 h2,
    vdvWhiteheadLinkJones_at_kashaev_point hN]

/-- **The volume conjecture for the Whitehead braid, with the Kashaev value as an evaluation.**
`(2π/N) log ‖P_N(e^{πi/N})‖ → Vol(W) = Vol(Borromean)/2`, where `P_N ∈ ℤ[q, q⁻¹]` is the
Laurent polynomial that equals `[N]⁻¹ J_N` of the Whitehead braid at every generic `q`. -/
theorem whiteheadLaurent_volume_conjecture :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖evalL
        (Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)) (Complex.exp_ne_zero _)
        (whiteheadLaurent N)‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  refine whiteheadLink_volume_conjecture.congr' ?_
  filter_upwards [Filter.eventually_ge_atTop 1] with N hN
  rw [laurent_at_kashaev_point hN]

end QOU.Knot.FigureEightVolume
