import QOU.SchurWeyl.WenzlMarkovTraceInstance
import QOU.SchurWeyl.HeckeColimitFamilyTrace

/-!
# QOU.SchurWeyl.OcneanuMarkovTraceEveryZ — the Ocneanu trace exists at every `z`, on every `H_n(q)`

The corpus had the Markov trace on the whole Hecke tower at two kinds of parameter:

* convention D, `z_D = q³/(q²+1)` (`MarkovTraceInstance.ocneanuMarkovTrace`), and
* every integer Wenzl level `r ≥ 1`, `z_r = Q^r/(q·[r]_Q)` with `Q = q²`
  (`WenzlMarkovTraceInstance.wenzlMarkovTrace`).

Off that lattice it was open: the standing note on beans `qou-uer7` / `qou-j7ln` records that the
Wenzl route has "no `r`, no `schurPrincipal`, no Pieri, no telescoping" at a general `z`. This file
closes it without a new hook identity, by **polynomial interpolation in `z`**.

## The argument

1. **The weight is a polynomial in `z`.** `ocneanuWeight q z μ` is a product of per-cell factors
   affine in `z`, over a denominator `∏ (q^{2h} − 1)` that does not involve `z`. So
   `ocneanuWeight q z μ = (wPoly q μ).eval z` with `wPoly q μ ∈ K[X]` (`wPoly_eval`). This holds
   with no hypothesis: in a field `a / 0 = a · 0⁻¹`.
2. **On the Wenzl lattice it is the Wenzl weight.** `ocneanuWeight q z_r μ = wenzlWeight r (q²) μ`
   for every Young diagram and every `r ≥ 1` (`ocneanuWeight_wenzlZ`). Per cell this is
   `(Q−1)·[r]_Q = Q^r − 1`; the case `r = 2` is the corpus's
   `wenzlWeight_two_eq_ocneanuWeight`.
3. **The lattice is infinite.** `r ↦ z_r` is injective for `q²` not a root of unity
   (`level_unique_of_wenzlMarkovParam_eq`), so a polynomial vanishing at every `z_r` is zero
   (`eq_zero_of_eval_wenzlZ`).
4. Each of the three properties `markovTraceOfWeight` needs (normalisation, branching, the
   representation-level Markov condition) is **linear in the weight** with coefficients that do
   not depend on `z`, so it is the vanishing of one polynomial in `z`. That polynomial vanishes on
   the lattice by the proved level-`r` theorems, hence identically.

The result is `ocneanuMarkovTraceEveryZ q z : MarkovTraceFamily K q q⁻¹ z` for **every** `z : K`,
and through `HeckeColimitFamilyTrace.ocneanuMarkovTraceAt` an `OcneanuTrace.MarkovTrace` on the
colimit `H_∞(q)` with parameter `z` (`ocneanuMarkovTraceColimit`).

## What is and is not new

* New: existence at every `z`. Uniqueness at a given `z` was already level-free
  (`HeckeCoset.markovTrace_unique`), so it now applies at every `z` (`eq_ocneanuWtrace_of_markov`).
* Conservativity: at `z = z_r` this trace is the level-`r` trace, and at `z_D` it is `wtrace`
  (both by uniqueness; `ocneanuMarkovTraceEveryZ_tr_wenzl`).
* Not claimed: anything at a root of unity (`hgen`, `hq2` are genericity hypotheses under which the
  seminormal form exists; they are about `q`, never about `z`). Not claimed: faithfulness; at
  `z_D` the trace is known not to be faithful (`OcneanuTraceNotFaithful`).

## Base ring (§7c)

Generic `[Field K]`. No ordering, nothing archimedean. The field is automatically infinite under
`hgen` (the powers of `q²` are distinct), which is all the interpolation uses.

-- Ref: [jones1987] V. F. R. Jones, *Hecke algebra representations of braid groups and link
--   polynomials*, Ann. of Math. 126 (1987), §5 (existence of the Ocneanu trace at every z).
-- Ref: [wenzl1988] H. Wenzl, *Hecke algebras of type A_n and subfactors*, Invent. Math. 92 (1988).

LaTeX label: `thm:ocneanu-trace-every-z`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.QBeta.WenzlWeight QOU.Mathlib
open Polynomial (C X eval eval_mul eval_C)

variable {K : Type*} [Field K]

/-! ## The weight as a polynomial in `z` -/

/-- The Ocneanu weight as a polynomial in the Markov parameter. -/
noncomputable def wPoly (q : K) (mu : YoungDiagram) : Polynomial K :=
  C (∏ c ∈ mu.cells, (q ^ (2 * hookLength mu c) - 1))⁻¹ * ocneanuNumPoly q mu

@[simp] theorem wPoly_eval (q z : K) (mu : YoungDiagram) :
    (wPoly q mu).eval z = ocneanuWeight q z mu := by
  rw [wPoly, eval_mul, eval_C, ocneanuNumPoly_eval, ocneanuWeight, div_eq_mul_inv, mul_comm]

/-! ## The Wenzl lattice -/

/-- The level-`r` Markov parameter `z_r = Q^r / (q · [r]_Q)`, `Q = q²`. -/
noncomputable def wenzlZ (q : K) (r : ℕ) : K := (q ^ 2) ^ r / (q * levelBracket r (q ^ 2))

/-- One cell of the bridge: at `z = z_r` the Ocneanu cell factor over its hook factor is the
hook-content cell factor of `s_μ(1, Q, …, Q^{r−1})`, divided by `[r]_Q`. -/
theorem ocneanuCell_wenzlZ (q : K) (hq : q ≠ 0) {r : ℕ} (hB : levelBracket r (q ^ 2) ≠ 0)
    (i j h : ℕ) :
    (q ^ (2 * i) * (q ^ 2 - 1 - q * wenzlZ q r) + q ^ (2 * j + 1) * wenzlZ q r)
        / (q ^ (2 * h) - 1)
      = (q ^ 2) ^ i * (1 - (q ^ 2) ^ ((r : ℤ) + content (i, j))) / (1 - (q ^ 2) ^ h)
        / levelBracket r (q ^ 2) := by
  have hq2 : (q ^ 2 : K) ≠ 0 := pow_ne_zero _ hq
  have hc : (r : ℤ) + content (i, j) = ((r + j : ℕ) : ℤ) - ((i : ℕ) : ℤ) := by
    unfold content; push_cast; ring
  have hlev := one_sub_pow_eq_mul_levelBracket r (q ^ 2)
  rw [hc, zpow_sub₀ hq2, zpow_natCast, zpow_natCast]
  have hQh : ((q ^ 2 : K)) ^ h = q ^ (2 * h) := by rw [← pow_mul]
  rw [hQh]
  rcases eq_or_ne (q ^ (2 * h) - 1) 0 with hz | hz
  · have hz' : (1 : K) - q ^ (2 * h) = 0 := by linear_combination -hz
    rw [hz, hz', div_zero, div_zero, zero_div]
  · have hz' : (1 : K) - q ^ (2 * h) ≠ 0 := fun e => hz (by linear_combination -e)
    unfold wenzlZ
    field_simp
    linear_combination q ^ (2 * i) * q * (1 - q ^ (2 * h)) * hlev

/-- **The bridge, off convention D.** At `z = z_r` the Ocneanu weight is the level-`r` Wenzl
weight, for every Young diagram. The case `r = 2` is `wenzlWeight_two_eq_ocneanuWeight`. -/
theorem ocneanuWeight_wenzlZ (q : K) (hq : q ≠ 0) {r : ℕ} (hB : levelBracket r (q ^ 2) ≠ 0)
    (mu : YoungDiagram) :
    ocneanuWeight q (wenzlZ q r) mu = wenzlWeight r (q ^ 2) mu := by
  rw [ocneanuWeight, ← Finset.prod_div_distrib, wenzlWeight, schurPrincipal, nPart,
    ← Finset.prod_pow_eq_pow_sum, ← Finset.prod_mul_distrib, ← Finset.prod_const,
    ← Finset.prod_div_distrib]
  refine Finset.prod_congr rfl ?_
  rintro ⟨i, j⟩ hx
  rw [hookLength_eq_hook hx, ocneanuCell_wenzlZ q hq hB i j, mul_div_assoc]

/-- **Interpolation on the Wenzl lattice.** A polynomial in `z` that vanishes at every `z_r`,
`r ≥ 1`, is zero: the `z_r` are pairwise distinct when `q²` is not a root of unity. -/
theorem eq_zero_of_eval_wenzlZ {q : K} (hq0 : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (P : Polynomial K)
    (h : ∀ r : ℕ, r ≠ 0 → P.eval (wenzlZ q r) = 0) : P = 0 := by
  have hinj : Function.Injective (fun r : ℕ => wenzlZ q (r + 1)) := fun a b hab => by
    have := level_unique_of_wenzlMarkovParam_eq hq0 hgen (Nat.succ_ne_zero a)
      (Nat.succ_ne_zero b) hab
    omega
  exact Polynomial.eq_zero_of_infinite_isRoot P
    (Set.infinite_of_injective_forall_mem hinj (fun r => h (r + 1) (Nat.succ_ne_zero r)))

/-! ## The three weight properties, at every `z` -/

/-- **Normalisation at every `z`**: `Σ_{|ν| = n} f^ν · w_ν(z) = 1`. -/
theorem sum_dim_ocneanuWeight_eq_one {q : K} (hq0 : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) (n : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
      (QOU.Mathlib.numStandardYoungTableaux ν.1 : K) * ocneanuWeight q z ν.1) = 1 := by
  set P : Polynomial K := (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
      C (QOU.Mathlib.numStandardYoungTableaux ν.1 : K) * wPoly q ν.1) - 1 with hPdef
  have hP : P = 0 := eq_zero_of_eval_wenzlZ hq0 hgen P fun r hr => by
    have hB := levelBracket_ne_zero_of_gen hgen hr
    simp only [hPdef, Polynomial.eval_sub, Polynomial.eval_finset_sum, eval_mul, eval_C,
      wPoly_eval, Polynomial.eval_one, ocneanuWeight_wenzlZ q hq0 hB]
    rw [sum_dim_wenzlWeight_eq_one (q ^ 2) (pow_ne_zero 2 hq0) hgen hB (ne_one_of_gen hgen) n,
      sub_self]
  have h := congrArg (Polynomial.eval z) hP
  simp only [hPdef, Polynomial.eval_sub, Polynomial.eval_finset_sum, eval_mul, eval_C,
    wPoly_eval, Polynomial.eval_one, Polynomial.eval_zero] at h
  exact sub_eq_zero.mp h

/-- **Branching at every `z`**: `Σ_{s addable} w_{ν+s}(z) = w_ν(z)`. -/
theorem sum_addable_ocneanuWeight {q : K} (hq0 : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) (ν : YoungDiagram) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, ocneanuWeight q z (addCellOrSelf ν s.1))
      = ocneanuWeight q z ν := by
  set P : Polynomial K := (∑ s : {s : ℕ × ℕ // IsAddableCell ν s},
      wPoly q (addCellOrSelf ν s.1)) - wPoly q ν with hPdef
  have hP : P = 0 := eq_zero_of_eval_wenzlZ hq0 hgen P fun r hr => by
    have hB := levelBracket_ne_zero_of_gen hgen hr
    simp only [hPdef, Polynomial.eval_sub, Polynomial.eval_finset_sum, wPoly_eval,
      ocneanuWeight_wenzlZ q hq0 hB]
    rw [sum_addable_wenzlWeight_all (q ^ 2) (pow_ne_zero 2 hq0) hgen hB (ne_one_of_gen hgen) ν,
      sub_self]
  have h := congrArg (Polynomial.eval z) hP
  simp only [hPdef, Polynomial.eval_sub, Polynomial.eval_finset_sum, wPoly_eval,
    Polynomial.eval_zero] at h
  exact sub_eq_zero.mp h

namespace SeminormalRep

open QOU.Mathlib QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

/-- **The representation-level Markov condition at every `z`.** For each `y` both sides are
linear in the weight with `z`-free coefficients (the block traces), so their difference is one
polynomial in `z`; `markov_wenzlWeight` makes it vanish on the lattice. -/
theorem markov_ocneanuWeight (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) {m : ℕ} (y : Hecke K q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        ocneanuWeight q z L.1
          * ((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl K q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace
      = z * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          ocneanuWeight q z ν.1 * (seminormalRep q hq0 hq2 m ν.2 y).trace := by
  set P : Polynomial K := (∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        wPoly q L.1 * C (((seminormalRep q hq0 hq2 (m + 1) L.2 (heckeIncl K q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace))
      - X * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          wPoly q ν.1 * C ((seminormalRep q hq0 hq2 m ν.2 y).trace) with hPdef
  have hP : P = 0 := eq_zero_of_eval_wenzlZ hq0 hgen P fun r hr => by
    have hB := levelBracket_ne_zero_of_gen hgen hr
    simp only [hPdef, Polynomial.eval_sub, Polynomial.eval_finset_sum, eval_mul, eval_C,
      Polynomial.eval_X, wPoly_eval, ocneanuWeight_wenzlZ q hq0 hB]
    rw [markov_wenzlWeight q hq0 hq2 hgen hr y, wenzlZ, sub_self]
  have h := congrArg (Polynomial.eval z) hP
  simp only [hPdef, Polynomial.eval_sub, Polynomial.eval_finset_sum, eval_mul, eval_C,
    Polynomial.eval_X, wPoly_eval, Polynomial.eval_zero] at h
  exact sub_eq_zero.mp h

/-- **The Ocneanu Markov trace on the Hecke tower, at every `z`.** -/
noncomputable def ocneanuMarkovTraceEveryZ (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) :
    HeckeCoset.MarkovTraceFamily K q q⁻¹ z :=
  markovTraceOfWeight q hq0 hq2 (ocneanuWeight q z) z
    (sum_dim_ocneanuWeight_eq_one hq0 hgen z)
    (sum_addable_ocneanuWeight hq0 hgen z)
    (fun _ y => markov_ocneanuWeight q hq0 hq2 hgen z y)

theorem ocneanuMarkovTraceEveryZ_tr (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) :
    (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z).tr = wtraceW q hq0 hq2 (ocneanuWeight q z) := rfl

/-- **Uniqueness at every `z`**: every Markov trace on the tower with parameter `z` is the
`ocneanuWeight q z`-weighted seminormal trace. -/
theorem eq_ocneanuWtrace_of_markov (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ z) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    T.tr n x = wtraceW q hq0 hq2 (ocneanuWeight q z) n x :=
  HeckeCoset.markovTrace_unique T (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z) n x

/-- **Conservativity on the lattice**: at `z = z_r` the every-`z` trace is the level-`r` trace. -/
theorem ocneanuMarkovTraceEveryZ_tr_wenzl (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) {r : ℕ} (hr : r ≠ 0) (n : ℕ)
    (x : Hecke K q q⁻¹ n) :
    (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen (wenzlZ q r)).tr n x
      = wtraceW q hq0 hq2 (wenzlWeight r (q ^ 2)) n x :=
  eq_wenzlWtrace_of_markov q hq0 hq2 hgen hr _ n x

/-- **Distinct parameters give distinct traces**: the family is genuinely one-parameter, not a
relabelling. The parameter is read off the trace as `z = tr₁(σ₀)` (`MarkovTraceFamily.param_eq`). -/
theorem ocneanuMarkovTraceEveryZ_param_injective (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) {z₁ z₂ : K}
    (h : (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z₁).tr 1 (Hecke.σ K q q⁻¹ 1 (Fin.last 0))
      = (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z₂).tr 1 (Hecke.σ K q q⁻¹ 1 (Fin.last 0))) :
    z₁ = z₂ := by
  rwa [HeckeCoset.MarkovTraceFamily.param_eq, HeckeCoset.MarkovTraceFamily.param_eq] at h

/-- **The Ocneanu trace on the colimit `H_∞(q)`, at every `z`**, as an
`OcneanuTrace.MarkovTrace` — the interface the `MathlibExt` tower results are stated against. -/
noncomputable def ocneanuMarkovTraceColimit (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) :
    QOU.MathlibExt.OcneanuTrace.MarkovTrace K (HeckeColimit.HeckeLim K q q⁻¹) :=
  HeckeColimitFamilyTrace.ocneanuMarkovTraceAt (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z)
    (mul_inv_cancel₀ hq0)

/-- Its Markov parameter is the `z` it was built at; nothing is chosen. -/
@[simp] theorem ocneanuMarkovTraceColimit_z (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) :
    (ocneanuMarkovTraceColimit q hq0 hq2 hgen z).z = z := rfl

end SeminormalRep

end QOU.SchurWeyl
