import QOU.QBeta.LocalUniformLimitEntire
import QOU.QBeta.PhiBProdMeromorphic
import Mathlib.Analysis.NormedSpace.MultipliableUniformlyOn

/-!
# The `phiBProd` partial products converge locally uniformly (input-1 closure)

This is the **last** infrastructure brick of input 1 of the Faddeev–Volkov uniqueness
keystone (`qou-7xvy`). `LocalUniformLimitEntire` (merged) reduces analyticity of the
infinite products `∏' k, numFactor b · k`, `∏' k, denFactor b · k` to a single
**local-uniform convergence** fact about their `Finset.range` partial products. This file
supplies that fact from Mathlib's uniform-product API and thereby closes input 1
**unconditionally on the product-supported branch `Im b² > 0`** — in particular at the
physical substrate b-map.

## The estimate

Each factor is `1 + exp(E(z) + k·c)` with `E` an affine (hence entire, continuous) function
of `z` and `c = 2πi b²` (numerator) / `−2πi/b²` (denominator). On the branch `Im b² > 0`,
`Re c < 0`, so on any **compact** `K ⊆ ℂ` the factor norms are dominated by the summable
geometric `u_K(k) = e^{M_K}·(e^{Re c})^k`, where `M_K = sup_{z∈K} Re(E z)` (finite by
compactness). Mathlib's `Summable.hasProdUniformlyOn_one_add` then gives uniform convergence
on each compact `K`, and `hasProdLocallyUniformlyOn_of_forall_compact` assembles these into
`HasProdLocallyUniformlyOn` on `ℂ`; its `tendstoLocallyUniformlyOn_finsetRange` accessor is
exactly the hypothesis `LocalUniformLimitEntire` needs.

The bound is **local** (per-compact), not global: `Re(E z)` is unbounded on `ℂ`, so no single
`u` dominates on all of `ℂ` — which is precisely why the local-uniform (not uniform) API is
the right tool.

Composing with `PhiBProdMeromorphic.phiBProd_meromorphicOn_of_analytic`, this discharges
`MeromorphicOn (phiBProd b)` with **no remaining analytic hypothesis** on the branch:
`phiBProd_meromorphicOn` / `phiBProd_meromorphicOn_substrate`.

Verified `lean`-direct against the pinned Mathlib `MultipliableUniformlyOn` +
`LocallyUniformLimit` cones (built from source) + `PhiBProd`. Sorry-free.

-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
--        https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

open Set Filter Topology Complex
open QOU.MathlibExt.PhiBProd

namespace QOU.QBeta.PhiBProdProductConvergence

/-- **Local-uniform convergence of `∏(1 + exp(affine + k·c))` for `Re c < 0`.** The generic
engine: for any continuous `E : ℂ → ℂ` and constant `c` with `Re c < 0`, the `Finset.range`
partial products of `1 + exp(E z + k c)` converge locally uniformly on `ℂ` to the `tprod`.
On each compact `K` the factor norms are dominated by the summable geometric
`e^{M_K}·(e^{Re c})^k`; `hasProdLocallyUniformlyOn_of_forall_compact` glues the compacts. -/
theorem tendstoLocallyUniformlyOn_prod_one_add_exp
    {E : ℂ → ℂ} (hE : Continuous E) {c : ℂ} (hc : c.re < 0) :
    TendstoLocallyUniformlyOn
      (fun (n : ℕ) (z : ℂ) => ∏ k ∈ Finset.range n, (1 + Complex.exp (E z + (k : ℂ) * c)))
      (fun z : ℂ => ∏' k : ℕ, (1 + Complex.exp (E z + (k : ℂ) * c))) atTop univ := by
  have hHP : HasProdLocallyUniformlyOn
      (fun (k : ℕ) (z : ℂ) => 1 + Complex.exp (E z + (k : ℂ) * c))
      (fun z : ℂ => ∏' k : ℕ, (1 + Complex.exp (E z + (k : ℂ) * c))) (univ : Set ℂ) := by
    apply hasProdLocallyUniformlyOn_of_forall_compact isOpen_univ
    intro K _hKsub hK
    -- `M` bounds `Re (E z)` on the compact `K`.
    obtain ⟨M, hM⟩ := hK.bddAbove_image
      (f := fun z => (E z).re) (Complex.continuous_re.comp hE).continuousOn
    -- The dominating summable geometric.
    have hu : Summable (fun k : ℕ => Real.exp M * Real.exp c.re ^ k) :=
      (summable_geometric_of_lt_one (Real.exp_pos _).le
        (Real.exp_lt_one_iff.mpr hc)).mul_left _
    -- Continuity of each factor on `K`.
    have hcts : ∀ k : ℕ, ContinuousOn (fun z => Complex.exp (E z + (k : ℂ) * c)) K :=
      fun k => (Complex.continuous_exp.comp (hE.add continuous_const)).continuousOn
    -- The norm bound is the remaining `?_`; `ι = ℕ` is inherited from the goal.
    refine Summable.hasProdUniformlyOn_one_add hK hu ?_ hcts
    refine Filter.Eventually.of_forall (fun k z hz => ?_)
    rw [Complex.norm_exp]
    have hre : (E z + (k : ℂ) * c).re = (E z).re + (k : ℝ) * c.re := by
      simp [Complex.add_re, Complex.mul_re, Complex.natCast_re, Complex.natCast_im]
    rw [hre, Real.exp_add, Real.exp_nat_mul]
    exact mul_le_mul_of_nonneg_right
      (Real.exp_le_exp.mpr (hM (Set.mem_image_of_mem _ hz)))
      (pow_nonneg (Real.exp_pos _).le k)
  exact hHP.tendstoLocallyUniformlyOn_finsetRange

/-! ## Instantiation at the numerator / denominator factors -/

/-- **Numerator partial products converge locally uniformly** (branch `Im b² > 0`). -/
theorem tendstoLocallyUniformlyOn_numFactor (b : ℂ) (hβ : 0 < (b ^ 2).im) :
    TendstoLocallyUniformlyOn
      (fun n z => ∏ k ∈ Finset.range n, numFactor b z k)
      (fun z => ∏' k, numFactor b z k) atTop univ := by
  have hE : Continuous fun z : ℂ =>
      (Real.pi : ℂ) * I * b ^ 2 + (2 * (Real.pi : ℂ) * b) * z :=
    continuous_const.add (continuous_const.mul continuous_id)
  have hc : (2 * (Real.pi : ℂ) * I * b ^ 2).re < 0 := by
    have h : (2 * (Real.pi : ℂ) * I * b ^ 2).re = -(2 * Real.pi * (b ^ 2).im) := by
      simp [Complex.mul_re, Complex.mul_im]
    rw [h]; have : (0 : ℝ) < 2 * Real.pi * (b ^ 2).im := by positivity
    linarith
  have key := tendstoLocallyUniformlyOn_prod_one_add_exp hE hc
  have hfeq : ∀ (z : ℂ) (k : ℕ),
      1 + Complex.exp (((Real.pi : ℂ) * I * b ^ 2 + (2 * (Real.pi : ℂ) * b) * z)
        + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2)) = numFactor b z k := by
    intro z k
    unfold numFactor
    rw [show ((Real.pi : ℂ) * I * b ^ 2 + (2 * (Real.pi : ℂ) * b) * z)
          + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2)
        = (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * b * z from by
      ring]
  have hseq : (fun (n : ℕ) (z : ℂ) => ∏ k ∈ Finset.range n,
        (1 + Complex.exp (((Real.pi : ℂ) * I * b ^ 2 + (2 * (Real.pi : ℂ) * b) * z)
          + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2))))
      = fun n z => ∏ k ∈ Finset.range n, numFactor b z k := by
    funext n z; exact Finset.prod_congr rfl (fun k _ => hfeq z k)
  have hlim : (fun z : ℂ => ∏' k : ℕ,
        (1 + Complex.exp (((Real.pi : ℂ) * I * b ^ 2 + (2 * (Real.pi : ℂ) * b) * z)
          + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2))))
      = fun z => ∏' k, numFactor b z k := by
    funext z; exact tprod_congr (fun k => hfeq z k)
  rw [hseq, hlim] at key
  exact key

/-- **Denominator partial products converge locally uniformly** (branch `Im b² > 0`). -/
theorem tendstoLocallyUniformlyOn_denFactor (b : ℂ) (hβ : 0 < (b ^ 2).im) :
    TendstoLocallyUniformlyOn
      (fun n z => ∏ k ∈ Finset.range n, denFactor b z k)
      (fun z => ∏' k, denFactor b z k) atTop univ := by
  have hE : Continuous fun z : ℂ =>
      -((Real.pi : ℂ) * I) / b ^ 2 + (2 * (Real.pi : ℂ) / b) * z :=
    continuous_const.add (continuous_const.mul continuous_id)
  have hc : (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re < 0 := by
    have h1 : (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re
        = -(2 * Real.pi * (b ^ 2).im) / Complex.normSq (b ^ 2) := by
      simp [Complex.div_re, Complex.mul_re, Complex.mul_im, neg_div]
    have hns : 0 < Complex.normSq (b ^ 2) :=
      Complex.normSq_pos.mpr (fun h => by simp [h] at hβ)
    rw [h1]; have : (0 : ℝ) < 2 * Real.pi * (b ^ 2).im := by positivity
    exact div_neg_of_neg_of_pos (by linarith) hns
  have key := tendstoLocallyUniformlyOn_prod_one_add_exp hE hc
  have hfeq : ∀ (z : ℂ) (k : ℕ),
      1 + Complex.exp ((-((Real.pi : ℂ) * I) / b ^ 2 + (2 * (Real.pi : ℂ) / b) * z)
        + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2)) = denFactor b z k := by
    intro z k
    unfold denFactor
    rw [show (-((Real.pi : ℂ) * I) / b ^ 2 + (2 * (Real.pi : ℂ) / b) * z)
          + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2)
        = -((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1) + 2 * (Real.pi : ℂ) * z / b from by
      ring]
  have hseq : (fun (n : ℕ) (z : ℂ) => ∏ k ∈ Finset.range n,
        (1 + Complex.exp ((-((Real.pi : ℂ) * I) / b ^ 2 + (2 * (Real.pi : ℂ) / b) * z)
          + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2))))
      = fun n z => ∏ k ∈ Finset.range n, denFactor b z k := by
    funext n z; exact Finset.prod_congr rfl (fun k _ => hfeq z k)
  have hlim : (fun z : ℂ => ∏' k : ℕ,
        (1 + Complex.exp ((-((Real.pi : ℂ) * I) / b ^ 2 + (2 * (Real.pi : ℂ) / b) * z)
          + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2))))
      = fun z => ∏' k, denFactor b z k := by
    funext z; exact tprod_congr (fun k => hfeq z k)
  rw [hseq, hlim] at key
  exact key

/-! ## Input 1 closed on the branch: the two products are entire, and `phiBProd` is meromorphic -/

/-- **The numerator infinite product is entire** on the branch `Im b² > 0`. -/
theorem analyticOnNhd_num_tprod (b : ℂ) (hβ : 0 < (b ^ 2).im) :
    AnalyticOnNhd ℂ (fun z => ∏' k, numFactor b z k) univ :=
  LocalUniformLimitEntire.phiBProd_num_analytic_of_tendsto b
    (tendstoLocallyUniformlyOn_numFactor b hβ)

/-- **The denominator infinite product is entire** on the branch `Im b² > 0`. -/
theorem analyticOnNhd_den_tprod (b : ℂ) (hβ : 0 < (b ^ 2).im) :
    AnalyticOnNhd ℂ (fun z => ∏' k, denFactor b z k) univ :=
  LocalUniformLimitEntire.phiBProd_den_analytic_of_tendsto b
    (tendstoLocallyUniformlyOn_denFactor b hβ)

/-- **`phiBProd b` is meromorphic on `ℂ` — unconditionally, on the branch `Im b² > 0`.**
Input 1 of the Faddeev keystone is now closed with no remaining analytic hypothesis: the two
products are entire (local-uniform limits of entire partial products) and their quotient is
meromorphic. -/
theorem phiBProd_meromorphicOn (b : ℂ) (hβ : 0 < (b ^ 2).im) :
    MeromorphicOn (phiBProd b) univ :=
  PhiBProdMeromorphic.phiBProd_meromorphicOn_of_analytic b
    (analyticOnNhd_num_tprod b hβ) (analyticOnNhd_den_tprod b hβ)

/-- **`phiBProd` is meromorphic at the physical substrate b-map** (`t = ln q₀ > 0`), with no
analytic hypothesis remaining — the substrate branch satisfies `Im b² > 0`. -/
theorem phiBProd_meromorphicOn_substrate {t : ℝ} (ht : 0 < t) :
    MeromorphicOn (phiBProd (substrateB t)) univ :=
  phiBProd_meromorphicOn _ (substrateB_sq_im_pos ht)

end QOU.QBeta.PhiBProdProductConvergence
