import QOU.SchurWeyl.OcneanuMarkovTraceEveryZ
import QOU.SchurWeyl.HeckeWedderburnAnyChar

/-!
# QOU.SchurWeyl.OcneanuTraceFaithful — when the Ocneanu trace is faithful

`OcneanuMarkovTraceEveryZ` built the Ocneanu Markov trace on every `H_n(q)` at every `z`.
`OcneanuTraceNotFaithful` showed that at convention D it is **not** faithful on `H_3(q)`, because
the three-row weight vanishes. This file gives the general answer.

## Results

* `wtraceW_faithful_iff` — for **any** weight `w`, the weighted seminormal trace on
  `H_{n+1}(q)` (the corpus's `Hecke K q q⁻¹ n`) is faithful, i.e. its trace form
  `⟨x, b⟩ = tr(x b)` has zero radical, **iff** `w ν ≠ 0` for every diagram `ν` with `n + 1` cells.
  Both directions go through the Wedderburn isomorphism `heckeProductF` (any characteristic):
  a block unit `E_{ji}` in block `ν` reads off the `(i, j)` entry of `x` with factor `w ν`.
* `ocneanuWeight_ne_zero_iff_num` — under `hgen` the Ocneanu weight vanishes only through its
  numerator (hook factors `q^{2h} − 1` are nonzero).
* `ocneanuTrace_faithful_off_finite` — **Jones' genericity statement**: for each `n` there is a
  finite set `S ⊆ K` such that for every `z ∉ S` the Ocneanu trace on `H_{n+1}(q)` is faithful.
  `S` is the root set of `∏_{|ν| = n+1} N_ν(z)`, a nonzero polynomial because every per-cell
  factor has constant term `q^{2i}(q² − 1) ≠ 0`.

So faithfulness fails only on finitely many `z` per level. Convention D is one of them from
`n + 1 = 3` on, which is `OcneanuTraceNotFaithful` again, now as a special case of the `iff`.

## Base ring (§7c)

Generic `[Field K]`, any characteristic; `q ≠ 0`, `q` and `q²` not roots of unity. No ordering.

-- Ref: [jones1987] V. F. R. Jones, Ann. of Math. 126 (1987), §5 — the trace is nondegenerate
--   for generic parameter.

LaTeX label: `thm:ocneanu-trace-faithful`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib
open Polynomial (C X eval)

variable {K : Type*} [Field K]

namespace SeminormalRep

open TableauCells Hecke

/-- **Faithfulness from nonvanishing weights.** If every weight on diagrams of size `n + 1` is
nonzero, an element orthogonal to everything under `⟨x, b⟩ = tr_w(x b)` is zero. -/
theorem wtraceW_eq_zero_of_orthogonal (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (w : YoungDiagram → K) {n : ℕ}
    (hw : ∀ ν : YoungDiagram, ν.cells.card = n + 1 → w ν ≠ 0) (x : Hecke K q q⁻¹ n)
    (hx : ∀ b : Hecke K q q⁻¹ n, wtraceW q hq0 hq2 w n (x * b) = 0) : x = 0 := by
  classical
  apply AnyChar.heckeProductF_injective q hq0 hq2 n
  rw [map_zero]
  funext lam
  ext i j
  obtain ⟨b, hb⟩ := AnyChar.heckeProductF_surjective q hq0 hq2 n
    (Pi.single lam (Matrix.single j i (1 : K)))
  have h := hx b
  rw [wtraceW_apply, Finset.sum_eq_single ⟨partitionShape lam, partitionShape_card_succ lam⟩]
    at h
  · have hbl : seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) b
        = Matrix.single j i (1 : K) := by
      have := congrFun hb lam
      rw [Pi.single_eq_same] at this
      exact this
    rw [map_mul, hbl, Matrix.trace_mul_single] at h
    simp only [MulOpposite.op_one, one_smul] at h
    have hwl := hw (partitionShape lam) (partitionShape_card_succ lam)
    have hx0 := (mul_eq_zero.mp h).resolve_left hwl
    simpa using hx0
  · rintro ⟨d, hd⟩ - hne
    obtain ⟨lam', rfl⟩ := exists_partitionShape_eq (n := n + 1) d hd
    have hl : lam' ≠ lam := by
      rintro rfl; exact hne rfl
    have hbz : seminormalRep q hq0 hq2 n hd b = 0 := by
      have := congrFun hb lam'
      rw [Pi.single_eq_of_ne hl] at this
      exact this.trans rfl
    rw [map_mul, hbz, mul_zero, Matrix.trace_zero, mul_zero]
  · intro hnot; exact absurd (Finset.mem_univ _) hnot

/-- **A zero weight makes the trace unfaithful.** If some diagram `ν₀` of size `n + 1` has
`w ν₀ = 0`, the Wedderburn preimage of the identity on block `ν₀` is nonzero and orthogonal to
everything. Generalises `OcneanuTraceNotFaithful.exists_nonzero_wtrace_orthogonal`. -/
theorem exists_orthogonal_of_weight_eq_zero (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (w : YoungDiagram → K) {n : ℕ}
    (ν₀ : YoungDiagram) (hν₀ : ν₀.cells.card = n + 1) (hw : w ν₀ = 0) :
    ∃ x : Hecke K q q⁻¹ n, x ≠ 0 ∧ ∀ b, wtraceW q hq0 hq2 w n (x * b) = 0 := by
  classical
  obtain ⟨lam₀, hlam₀⟩ := exists_partitionShape_eq (n := n + 1) ν₀ hν₀
  obtain ⟨x, hx⟩ := AnyChar.heckeProductF_surjective q hq0 hq2 n
    (Pi.single lam₀ (1 : Matrix (StandardYoungTableau (partitionShape lam₀))
      (StandardYoungTableau (partitionShape lam₀)) K))
  refine ⟨x, ?_, ?_⟩
  · intro h0
    rw [h0, map_zero] at hx
    have hlam := congrFun hx lam₀
    rw [Pi.single_eq_same] at hlam
    obtain ⟨T⟩ : Nonempty (StandardYoungTableau (partitionShape lam₀)) := inferInstance
    have hentry : (0 : Matrix (StandardYoungTableau (partitionShape lam₀))
        (StandardYoungTableau (partitionShape lam₀)) K) T T
        = (1 : Matrix (StandardYoungTableau (partitionShape lam₀))
        (StandardYoungTableau (partitionShape lam₀)) K) T T := by
      rw [← hlam]; rfl
    rw [Matrix.zero_apply, Matrix.one_apply_eq] at hentry
    exact zero_ne_one hentry
  · intro b
    rw [wtraceW_apply]
    refine Finset.sum_eq_zero ?_
    rintro ⟨d, hd⟩ -
    obtain ⟨lam, rfl⟩ := exists_partitionShape_eq (n := n + 1) d hd
    by_cases hl : lam = lam₀
    · subst hl
      have hw' : w (partitionShape lam) = 0 := hlam₀ ▸ hw
      show w (partitionShape lam) * _ = 0
      rw [hw', zero_mul]
    · have hxz : seminormalRep q hq0 hq2 n hd x = 0 := by
        have h := congrFun hx lam
        rw [Pi.single_eq_of_ne hl] at h
        exact h.trans rfl
      rw [map_mul, hxz, zero_mul, Matrix.trace_zero, mul_zero]

/-- **Faithfulness criterion, any weight.** The weighted seminormal trace on `H_{n+1}(q)` has
zero radical iff no weight on a diagram of size `n + 1` vanishes. -/
theorem wtraceW_faithful_iff (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (w : YoungDiagram → K) (n : ℕ) :
    (∀ x : Hecke K q q⁻¹ n, (∀ b, wtraceW q hq0 hq2 w n (x * b) = 0) → x = 0)
      ↔ ∀ ν : YoungDiagram, ν.cells.card = n + 1 → w ν ≠ 0 := by
  constructor
  · intro hf ν hν hw
    obtain ⟨x, hx0, hx⟩ := exists_orthogonal_of_weight_eq_zero q hq0 hq2 w ν hν hw
    exact hx0 (hf x hx)
  · intro hw x hx
    exact wtraceW_eq_zero_of_orthogonal q hq0 hq2 w hw x hx

end SeminormalRep

/-! ## The Ocneanu weight: where it can vanish -/

/-- Under `hgen` the hook denominator of the Ocneanu weight is nonzero. -/
theorem ocneanuDen_ne_zero {q : K} (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1)
    (ν : YoungDiagram) : (∏ c ∈ ν.cells, (q ^ (2 * hookLength ν c) - 1)) ≠ 0 := by
  rw [Finset.prod_ne_zero_iff]
  intro c hc
  have h1 : 1 ≤ QOU.QBeta.WenzlWeight.hook ν c := QOU.QBeta.WenzlWeight.one_le_hook hc
  rw [hookLength_eq_hook hc, sub_ne_zero, pow_mul]
  have := hgen (QOU.QBeta.WenzlWeight.hook ν c : ℤ) (by exact_mod_cast (by omega : QOU.QBeta.WenzlWeight.hook ν c ≠ 0))
  rwa [zpow_natCast] at this

/-- Every per-cell factor of the Ocneanu numerator is a nonzero polynomial in `z`, so the
numerator polynomial is nonzero: its constant term is `∏ q^{2i}(q² − 1)`. -/
theorem ocneanuNumPoly_ne_zero {q : K} (hq0 : q ≠ 0) (hq21 : q ^ 2 ≠ 1) (ν : YoungDiagram) :
    ocneanuNumPoly q ν ≠ 0 := by
  rw [ocneanuNumPoly, Finset.prod_ne_zero_iff]
  intro c _ hc
  have h := congrArg (Polynomial.eval 0) hc
  simp only [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_X,
    mul_zero, add_zero, Polynomial.eval_zero] at h
  exact mul_ne_zero (pow_ne_zero _ hq0) (sub_ne_zero.mpr hq21) h

/-- **The Ocneanu weight vanishes only through its numerator.** -/
theorem ocneanuWeight_ne_zero_iff {q : K} (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1)
    (z : K) (ν : YoungDiagram) :
    ocneanuWeight q z ν ≠ 0 ↔ (ocneanuNumPoly q ν).eval z ≠ 0 := by
  rw [ocneanuNumPoly_eval, ocneanuWeight, div_ne_zero_iff]
  exact ⟨fun h => h.1, fun h => ⟨h, ocneanuDen_ne_zero hgen ν⟩⟩

namespace SeminormalRep

/-- **Jones' genericity statement.** For each level there is a finite set `S` of Markov
parameters off which the Ocneanu trace on `H_{n+1}(q)` is faithful: its trace form has zero
radical. `S` is the root set of `∏_{|ν| = n+1} N_ν`, nonzero by `ocneanuNumPoly_ne_zero`. -/
theorem ocneanuTrace_faithful_off_finite (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (n : ℕ) :
    ∃ S : Finset K, ∀ z ∉ S, ∀ x : Hecke K q q⁻¹ n,
      (∀ b, (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z).tr n (x * b) = 0) → x = 0 := by
  classical
  set P : Polynomial K := ∏ ν : {ν : YoungDiagram // ν.cells.card = n + 1},
    ocneanuNumPoly q ν.1 with hPdef
  have hq21 : (q : K) ^ 2 ≠ 1 := ne_one_of_gen hgen
  have hP : P ≠ 0 := by
    rw [hPdef, Finset.prod_ne_zero_iff]
    exact fun ν _ => ocneanuNumPoly_ne_zero hq0 hq21 ν.1
  refine ⟨P.roots.toFinset, fun z hz x hx => ?_⟩
  have hPz : P.eval z ≠ 0 := by
    intro h0
    exact hz (Multiset.mem_toFinset.mpr ((Polynomial.mem_roots hP).mpr h0))
  refine wtraceW_eq_zero_of_orthogonal q hq0 hq2 (ocneanuWeight q z) (fun ν hν => ?_) x hx
  rw [ocneanuWeight_ne_zero_iff hgen]
  rw [hPdef, Polynomial.eval_prod, Finset.prod_ne_zero_iff] at hPz
  exact hPz ⟨ν, hν⟩ (Finset.mem_univ _)

/-- **Faithfulness of the every-`z` trace, exactly.** At parameter `z` the Ocneanu trace on
`H_{n+1}(q)` is faithful iff `ocneanuWeight q z ν ≠ 0` for every `ν` with `n + 1` cells. -/
theorem ocneanuTrace_faithful_iff (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q)
    (hgen : ∀ k : ℤ, k ≠ 0 → ((q ^ 2 : K)) ^ k ≠ 1) (z : K) (n : ℕ) :
    (∀ x : Hecke K q q⁻¹ n,
        (∀ b, (ocneanuMarkovTraceEveryZ q hq0 hq2 hgen z).tr n (x * b) = 0) → x = 0)
      ↔ ∀ ν : YoungDiagram, ν.cells.card = n + 1 → ocneanuWeight q z ν ≠ 0 :=
  wtraceW_faithful_iff q hq0 hq2 (ocneanuWeight q z) n

end SeminormalRep

end QOU.SchurWeyl
