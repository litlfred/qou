import QOU.Hecke.H2AlgebraDimension
import QOU.Hecke.H2GramArithmetic
import QOU.MathlibExt.RegTraceGram
import QOU.MathlibExt.HeckeGramFactorial
import Mathlib.RingTheory.Trace.Basic

/-!
# QOU.Hecke.H2TraceForm — the first fully axiom-free `WenzlCriterion` discharge

Bricks `qou-lrz1` + `qou-twwf` at `n = 2`, composed.  On the genuine
`2`-dimensional algebra `H_2(q) = AdjoinRoot(X²-(q-1)X-q)`
(`H2AlgebraDimension`) we compute the **regular trace form Gram matrix in
the power basis `{1, σ}`** from Mathlib's `Algebra.trace`, prove it equals
`h2GramMatrix` (whose entries `H2GramArithmetic` had asserted), and hence

  `det(Gram) = [2]_q²  ≠ 0  ⟺  q` Wenzl-generic  ⟹  `H_2(q)` semisimple.

The three trace values are computed, not assumed:

* `tr(1) = 2`   (`Algebra.trace_algebraMap`, `dim = 2`);
* `tr(σ) = q-1` (`PowerBasis.trace_gen_eq_nextCoeff_minpoly`, `nextCoeff`);
* `tr(σ²) = q²+1` (the root relation `σ² = (q-1)σ + q` + `K`-linearity).

The capstone `h2_isSemisimpleRing_of_generic` is the **first rank at which
`WenzlCriterion` is discharged with no cited class and no `sorry`** — the
whole `det(Gram) = [n]_q!` ⇒ semisimplicity chain realised concretely at
`n = 2`.
-/

namespace QOU.Hecke

open Polynomial Algebra QOU.MathlibExt

variable {K : Type*} [Field K]

/-- `regTraceForm = Algebra.trace (x*y)` on a commutative algebra
    (sorry-free): both are `LinearMap.trace (lmul (x*y))`. -/
theorem regTraceForm_eq_trace {A : Type*} [CommRing A] [Algebra K A]
    [FiniteDimensional K A] (x y : A) :
    regTraceForm K A x y = Algebra.trace K A (x * y) := rfl

/-- The Hecke generator `σ = root(h2Poly q)` inside `H_2(q)`. -/
noncomputable def h2sigma (q : K) : AdjoinRoot (h2Poly q) := AdjoinRoot.root (h2Poly q)

/-- **`tr(1) = 2` (sorry-free).**  Via `trace(algebraMap 1) = dim • 1` and
    `dim H_2(q) = 2`. -/
theorem h2_trace_one (q : K) :
    Algebra.trace K (AdjoinRoot (h2Poly q)) 1 = 2 := by
  rw [show (1 : AdjoinRoot (h2Poly q)) = algebraMap K _ 1 by rw [map_one],
    Algebra.trace_algebraMap, h2_finrank]
  norm_num

/-- **`nextCoeff (X²-(q-1)X-q) = -(q-1)` (sorry-free).** -/
theorem h2Poly_nextCoeff (q : K) : (h2Poly q).nextCoeff = -(q - 1) := by
  rw [Polynomial.nextCoeff, if_neg (by rw [h2Poly_natDegree]; norm_num), h2Poly_natDegree]
  simp [h2Poly, coeff_X_pow]

/-- **`tr(σ) = q-1` (sorry-free).**  The power-basis generator's trace is
    minus the `nextCoeff` of its minimal polynomial `h2Poly`. -/
theorem h2_trace_gen (q : K) :
    Algebra.trace K (AdjoinRoot (h2Poly q)) (h2sigma q) = q - 1 := by
  haveI : Nontrivial (AdjoinRoot (h2Poly q)) :=
    Module.nontrivial_of_finrank_pos (R := K) (by rw [h2_finrank]; norm_num)
  have hg : (h2PowerBasis q).gen = h2sigma q := by
    rw [h2PowerBasis, AdjoinRoot.powerBasis'_gen, h2sigma]
  have hmin : minpoly K (h2sigma q) = h2Poly q := by
    rw [h2sigma, AdjoinRoot.minpoly_root (h2Poly_ne_zero q),
      (h2Poly_monic q).leadingCoeff, inv_one, map_one, mul_one]
  have h := PowerBasis.trace_gen_eq_nextCoeff_minpoly (h2PowerBasis q)
  rw [hg, hmin, h2Poly_nextCoeff] at h
  rw [h]; ring

/-- **The root relation `σ² = (q-1)·σ + q` (sorry-free).** -/
theorem h2sigma_sq (q : K) :
    (h2sigma q) ^ 2
      = algebraMap K (AdjoinRoot (h2Poly q)) (q - 1) * h2sigma q
        + algebraMap K (AdjoinRoot (h2Poly q)) q := by
  have h0 : (h2Poly q).eval₂ (algebraMap K (AdjoinRoot (h2Poly q))) (h2sigma q) = 0 := by
    rw [h2sigma, AdjoinRoot.algebraMap_eq]; exact AdjoinRoot.eval₂_root (h2Poly q)
  simp only [h2Poly, eval₂_sub, eval₂_mul, eval₂_pow, eval₂_X, eval₂_C] at h0
  -- `h0` now has `AdjoinRoot (X²-…)`-typed `algebraMap`s; retype to the folded
  -- form by defeq, then close by ring.
  have h0' : h2sigma q ^ 2 - algebraMap K (AdjoinRoot (h2Poly q)) (q - 1) * h2sigma q
      - algebraMap K (AdjoinRoot (h2Poly q)) q = 0 := h0
  linear_combination h0'

/-- **`tr(σ²) = q²+1` (sorry-free).**  From the root relation and the
    `K`-linearity of `Algebra.trace`: `tr(σ²) = (q-1)tr(σ) + q·tr(1)
    = (q-1)² + 2q = q²+1`. -/
theorem h2_trace_gen_sq (q : K) :
    Algebra.trace K (AdjoinRoot (h2Poly q)) (h2sigma q ^ 2) = q ^ 2 + 1 := by
  rw [h2sigma_sq, map_add, ← Algebra.smul_def, Algebra.algebraMap_eq_smul_one,
    map_smul, map_smul, h2_trace_gen, h2_trace_one, smul_eq_mul, smul_eq_mul]
  ring

/-- The power basis `{1, σ}` **reindexed to `Fin 2`** (via `dim = 2`), so
    the Gram matrix is an honest `Matrix (Fin 2) (Fin 2) K`. -/
noncomputable def h2Basis (q : K) : Module.Basis (Fin 2) K (AdjoinRoot (h2Poly q)) :=
  (h2PowerBasis q).basis.reindex (finCongr (h2PowerBasis_dim q))

/-- **`h2Basis i = σⁱ` (sorry-free).** -/
theorem h2Basis_apply (q : K) (i : Fin 2) : h2Basis q i = h2sigma q ^ (i : ℕ) := by
  have hg : (h2PowerBasis q).gen = h2sigma q := by
    rw [h2PowerBasis, AdjoinRoot.powerBasis'_gen, h2sigma]
  rw [h2Basis, Module.Basis.reindex_apply, PowerBasis.basis_eq_pow, hg]
  congr 1

/-- **The regular-trace Gram matrix of `H_2(q)` in the basis `{1, σ}`
    equals `h2GramMatrix` (sorry-free).**  Each entry `tr(σⁱ·σʲ)` reduces to
    the asserted literal via the three computed traces. -/
theorem h2_regTraceGram_eq (q : K) :
    BilinForm.toMatrix (h2Basis q)
        (regTraceBilin K (AdjoinRoot (h2Poly q)))
      = h2GramMatrix q := by
  ext i j
  rw [regTraceGram_toMatrix_apply, regTraceForm_eq_trace, h2Basis_apply, h2Basis_apply]
  fin_cases i <;> fin_cases j <;>
    simp only [h2GramMatrix, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.of_apply, Fin.isValue, Fin.zero_eta, Fin.mk_one,
      pow_zero, pow_one, one_mul, mul_one, Matrix.cons_val_fin_one]
  · exact h2_trace_one q
  · exact h2_trace_gen q
  · exact h2_trace_gen q
  · rw [← pow_two]; exact h2_trace_gen_sq q

/-- **`det(Gram) = [2]_q²` for the actual `H_2(q)` regular trace form
    (sorry-free).** -/
theorem h2_regTraceGram_det (q : K) :
    (BilinForm.toMatrix (h2Basis q)
        (regTraceBilin K (AdjoinRoot (h2Poly q)))).det = qInt q 2 ^ 2 := by
  rw [h2_regTraceGram_eq, h2GramMatrix_det]

/-- **First fully axiom-free `WenzlCriterion` discharge (sorry-free).**  For
    Wenzl-generic `q` (here: `q ≠ 1` and `q² ≠ 1`, i.e. `QGeneric q 2`),
    the Iwahori–Hecke algebra `H_2(q) = AdjoinRoot(X²-(q-1)X-q)` is
    semisimple — proved with **no cited class and no `sorry`**, by
    computing its regular-trace Gram determinant `[2]_q² = (1+q)·[2]_q!`
    and feeding it through `isSemisimpleRing_of_gram_det_eq_qFactorial`. -/
theorem h2_isSemisimpleRing_of_generic {q : K} (hq : q ≠ 1)
    (hgen : QGeneric q 2) : IsSemisimpleRing (AdjoinRoot (h2Poly q)) := by
  have hc : (1 + q) ≠ 0 := by
    intro h
    have hqm1 : q = -1 := by linear_combination h
    exact hgen 2 (le_refl 2) (le_refl 2) (by rw [hqm1]; ring)
  refine isSemisimpleRing_of_gram_det_eq_qFactorial (h2Basis q) hq hc hgen ?_
  rw [h2_regTraceGram_det, qFactorial_two, qInt_two]; ring

/-- **The substrate discharges `H_2` semisimplicity (sorry-free).**  For any
    real `q > 1` — in particular the physical substrate `q₀ ≈ 1.10998` —
    the Iwahori–Hecke algebra `H_2(q)` is semisimple: `q > 1` is
    Wenzl-generic at every rank (`qGeneric_of_one_lt`), and the axiom-free
    n=2 discharge applies.  This is the shape in which the substrate
    parameter discharges the semisimplicity leg of the `P ≠ NP`-in-QOU
    counting argument at `n = 2`, with no cited class and no `sorry`. -/
theorem h2_isSemisimpleRing_of_one_lt {q : ℝ} (hq : 1 < q) :
    IsSemisimpleRing (AdjoinRoot (h2Poly q)) :=
  h2_isSemisimpleRing_of_generic hq.ne' (qGeneric_of_one_lt hq 2)

end QOU.Hecke
