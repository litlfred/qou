import QOU.Braiding.WeakVertexCouplingNormalisation
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Pow

/-!
# Archimedean half of the coupling-normalisation result

The generic-field identities live in `WeakVertexCouplingNormalisation`; this
file is their `K := ℝ` specialisation, kept separate per AGENTS.md §7c because
everything here needs the archimedean structure of `ℝ` — `HasDerivAt` for the
vanishing orders, and decidable rational arithmetic for the exclusion.

Two results:

* **Vanishing orders.** `s²` vanishes to *second* order at `q = 1`
  (`hasDerivAt_sSq_one`: `s²′(1) = 0`, with `sSq_one` giving `s²(1) = 0`), while
  `W` has `W′(1) = 5 ≠ 0` (`hasDerivAt_weakVertexTrace_one`), so `W − W(1)`
  vanishes only to *first* order. A single bridge factor vanishing like `q − 1`
  repairs that, so the order alone does not decide the question.

* **The exclusion.** `no_constant_rescaling`: there is no constant `c` with
  `c · (W(q) − 1/4) · ℏ_q = s²(q)` for all `q > 1`. It is decided at two
  rational points — `candidateRatio_two` gives `695.91` at `q = 2` and
  `candidateRatio_three_halves` gives `≈ 65.27` at `q = 3/2` — so the ratio is a
  function of `q`, and no normalisation *constant* absorbs it.

Scope: this excludes the family `c · (W − W(1)) · X`; it says nothing against `W`
itself. Bean `qou-pfh7`.

Verified `lean`-direct, sorry-free.
-/

namespace QOU.Braiding.WeakVertexT35

/-- `s²` vanishes to second order: its derivative at `q = 1` is `0`. -/
theorem hasDerivAt_sSq_one : HasDerivAt (fun x : ℝ => sSq x) 0 1 := by
  have h : HasDerivAt (fun x : ℝ => (x - 1) ^ 2 / x) 0 1 := by
    have hx : HasDerivAt (fun x : ℝ => (x - 1) ^ 2) 0 1 := by
      have : HasDerivAt (fun x : ℝ => x - 1) 1 1 :=
        (hasDerivAt_id (1 : ℝ)).sub_const 1
      simpa using this.pow 2
    have hinv : HasDerivAt (fun x : ℝ => x⁻¹) (-1) 1 := by
      simpa using hasDerivAt_inv (one_ne_zero : (1 : ℝ) ≠ 0)
    have := hx.mul hinv
    simpa [div_eq_mul_inv] using this
  simpa [sSq, div_eq_mul_inv] using h

/-- `W` vanishes to first order about its classical value: `W′(1) = 5 ≠ 0`,
so `W − W(1)` is `5(q − 1) + O((q−1)²)`. -/
theorem hasDerivAt_weakVertexTrace_one :
    HasDerivAt (fun x : ℝ => weakVertexTrace x) 5 1 := by
  have hnum : HasDerivAt (fun x : ℝ => x ^ 14 + x ^ 10 - x ^ 2) 22 1 := by
    have h14 : HasDerivAt (fun x : ℝ => x ^ 14) 14 1 := by
      simpa using (hasDerivAt_id (1 : ℝ)).pow 14
    have h10 : HasDerivAt (fun x : ℝ => x ^ 10) 10 1 := by
      simpa using (hasDerivAt_id (1 : ℝ)).pow 10
    have h2 : HasDerivAt (fun x : ℝ => x ^ 2) 2 1 := by
      simpa using (hasDerivAt_id (1 : ℝ)).pow 2
    convert (h14.add h10).sub h2 using 1
    norm_num
  have hden : HasDerivAt (fun x : ℝ => ((x ^ 2 + 1) ^ 2)⁻¹) (-1 / 2) 1 := by
    have hd : HasDerivAt (fun x : ℝ => (x ^ 2 + 1) ^ 2) 8 1 := by
      have h2 : HasDerivAt (fun x : ℝ => x ^ 2 + 1) 2 1 := by
        simpa using ((hasDerivAt_id (1 : ℝ)).pow 2).add_const 1
      convert h2.pow 2 using 1
      norm_num
    have hne : ((1 : ℝ) ^ 2 + 1) ^ 2 ≠ 0 := by norm_num
    have := hd.inv hne
    convert this using 1
    norm_num
  have hW : (fun x : ℝ => weakVertexTrace x)
      = fun x : ℝ => (x ^ 14 + x ^ 10 - x ^ 2) * ((x ^ 2 + 1) ^ 2)⁻¹ := by
    funext x
    unfold weakVertexTrace
    rw [div_eq_mul_inv]
    ring_nf
  rw [hW]
  have := hnum.mul hden
  convert this using 1
  norm_num

/-- **The family is excluded.** No constant rescales the order-matched
candidate onto the coupling the decay rate uses: `c` would have to be
`100/69591` at `q = 2` and `86528/5647625` at `q = 3/2`. -/
theorem no_constant_rescaling :
    ¬ ∃ c : ℝ, ∀ q : ℝ, 1 < q → c * candidateCoupling q = sSq q := by
  rintro ⟨c, hc⟩
  have h2 := hc 2 (by norm_num)
  have h3 := hc (3 / 2) (by norm_num)
  unfold candidateCoupling hbarQ weakVertexTrace sSq at h2 h3
  norm_num at h2 h3
  have hcv : c = 100 / 69591 := by linarith
  rw [hcv] at h3
  norm_num at h3

/-- At `q = 2` the ratio is `69591/100 = 695.91`. -/
theorem candidateRatio_two : candidateRatio (2 : ℝ) = 69591 / 100 := by
  unfold candidateRatio candidateCoupling hbarQ weakVertexTrace sSq
  norm_num

/-- At `q = 3/2` it is `5647625/86528 ≈ 65.27` — a different number, so the
ratio is a function of `q` and not a normalisation constant. -/
theorem candidateRatio_three_halves :
    candidateRatio (3 / 2 : ℝ) = 5647625 / 86528 := by
  unfold candidateRatio candidateCoupling hbarQ weakVertexTrace sSq
  norm_num

end QOU.Braiding.WeakVertexT35
