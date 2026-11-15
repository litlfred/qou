import QOU.SchurWeyl.WenzlMarkovTraceInstance
import QOU.SchurWeyl.OcneanuWeightWenzl
import QOU.SchurWeyl.BranchingGenericity
import QOU.SchurWeyl.SymmetrisingTraceZeroParam

/-!
# QOU.SchurWeyl.MolienSymmetrisingTrace — the Molien weight is the symmetrising trace

The **Molien weight** of a Young diagram `μ`, with `Q = q²`, is

```
M_μ(Q) = Q^{n(μ)} · ∏_{x ∈ μ} (1 − Q) / (1 − Q^{h(x)}),
```

`n(μ) = Σ_{(i,j) ∈ μ} i` and `h(x)` the hook length.  In the balanced variable it is
`q^{−κ(μ)} / ∏_x [h(x)]_q` (`κ` = content sum) — proved in `MolienBalancedForm.molienWeight_eq_balanced`, and `f^μ · d_q(μ) · M_μ`-type products of it are
the Féray–Méliot q-Plancherel measure.  This file proves, in Lean and without citing the
literature, that

**the seminormal trace weighted by `M` is a Markov trace with parameter `z = 0`, and hence is the
symmetrising trace `τ(T_w) = δ_{w,1}`.**

## Main results

* `ocneanuWeight_zero_eq_molienWeight` — `M` is the Ocneanu weight at `z = 0`
  (generic field).
* `sum_dim_molienWeight_eq_one`, `sum_addable_molienWeight` — normalisation and branching
  (generic field, `Q` not a root of unity).
* `SeminormalRep.markov_molienWeight` — the Markov corner identity at `z = 0`.
* `SeminormalRep.molienMarkovTrace : MarkovTraceFamily K q q⁻¹ 0`, over any field `K`.
* `SeminormalRep.molienMarkovTrace_symmetrising` — on the coset basis it is `1` at the identity
  and `0` elsewhere; `SeminormalRep.eq_molien_of_zero` — every `z = 0` Markov trace equals it.

## Method: interpolation from the Wenzl levels

Put `W_μ(a) = Q^{n(μ)} ∏_x (1 − Q)(1 − a·Q^{c(x)}) / (1 − Q^{h(x)})`, a polynomial in `a`
(`wenzlPoly`).  Then

* `W_μ(Q^r) = (1 − Q^r)^{|μ|} · wenzlWeight r Q μ` — the level-`r` Wenzl weight, rescaled;
* `W_μ(0) = M_μ`.

Each of the three weight identities the level-`r` chain proves (`sum_dim_wenzlWeight_eq_one`,
`sum_addable_wenzlWeight_all`, `markov_wenzlWeight`) becomes, after clearing the `(1 − Q^r)`
powers, an identity between two polynomials in `a` that holds at every `a = Q^r`, `r ≥ 1`.
Those are infinitely many distinct points when `Q` is not a root of unity, so the polynomials are
equal, and evaluating at `a = 0` gives the identity for `M`.  The Markov parameter
`z_r = Q^r(1 − Q)/(q(1 − Q^r))` becomes the polynomial `a(1 − Q)/q` and vanishes at `a = 0`.

This is the `r → "∞ with a = Q^r → 0"` degeneration of Wenzl's family, made exact.  It avoids
the general-`z` Ocneanu corner identity, which is not proved in the corpus.

## Base ring (§7c)

Generic `[Field F]` throughout; the seminormal representations, and hence the trace, are built
over any field with `q ≠ 0` not a root of unity.  No ordering, no `ℝ`.

LaTeX label: `thm:molien-symmetrising-trace`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset Polynomial QOU.QBeta.WenzlWeight QOU.Mathlib

section Generic

variable {F : Type*} [Field F]

/-- The **Molien weight** `M_μ(Q) = Q^{n(μ)} ∏_x (1 − Q)/(1 − Q^{h(x)})`. -/
noncomputable def molienWeight (Q : F) (μ : YoungDiagram) : F :=
  Q ^ nPart μ * ∏ x ∈ μ.cells, (1 - Q) / (1 - Q ^ hook μ x)

/-- **The Molien weight is the Ocneanu weight at Markov parameter `z = 0`.** -/
theorem ocneanuWeight_zero_eq_molienWeight (q : F) (μ : YoungDiagram) :
    ocneanuWeight q 0 μ = molienWeight (q ^ 2) μ := by
  unfold ocneanuWeight molienWeight nPart
  simp only [mul_zero, sub_zero, add_zero]
  rw [← Finset.prod_pow_eq_pow_sum, ← Finset.prod_mul_distrib, ← Finset.prod_div_distrib]
  refine Finset.prod_congr rfl fun x hx => ?_
  rw [hookLength_eq_hook hx, ← pow_mul, ← pow_mul, ← neg_sub (1 : F) (q ^ 2),
    ← neg_sub (1 : F) (q ^ (2 * hook μ x)), mul_div_assoc, neg_div_neg_eq]

/-- The **interpolating polynomial** `W_μ(a)`: level `r` at `a = Q^r`, Molien at `a = 0`. -/
noncomputable def wenzlPoly (Q : F) (μ : YoungDiagram) : F[X] :=
  C (Q ^ nPart μ) * ∏ x ∈ μ.cells, (C ((1 - Q) / (1 - Q ^ hook μ x)) * (1 - C (Q ^ content x) * X))

theorem eval_wenzlPoly (Q a : F) (μ : YoungDiagram) :
    (wenzlPoly Q μ).eval a
      = Q ^ nPart μ * ∏ x ∈ μ.cells, ((1 - Q) / (1 - Q ^ hook μ x) * (1 - Q ^ content x * a)) := by
  simp [wenzlPoly, eval_prod]

theorem eval_zero_wenzlPoly (Q : F) (μ : YoungDiagram) :
    (wenzlPoly Q μ).eval 0 = molienWeight Q μ := by
  rw [eval_wenzlPoly]
  simp [molienWeight]

theorem eval_pow_wenzlPoly (Q : F) (hQ0 : Q ≠ 0) {r : ℕ} (hbr : levelBracket r Q ≠ 0)
    (μ : YoungDiagram) :
    (wenzlPoly Q μ).eval (Q ^ r) = (1 - Q ^ r) ^ μ.cells.card * wenzlWeight r Q μ := by
  rw [eval_wenzlPoly, wenzlWeight, schurPrincipal, one_sub_pow_eq_mul_levelBracket r Q, mul_pow]
  have key : ∀ x ∈ μ.cells, (1 - Q) / (1 - Q ^ hook μ x) * (1 - Q ^ content x * Q ^ r)
      = (1 - Q) * ((1 - Q ^ ((r : ℤ) + content x)) / (1 - Q ^ hook μ x)) := by
    intro x _
    rw [← zpow_natCast Q r, ← zpow_add₀ hQ0, add_comm]
    ring
  rw [Finset.prod_congr rfl key, Finset.prod_mul_distrib, Finset.prod_const]
  have hpow : levelBracket r Q ^ μ.cells.card ≠ 0 := pow_ne_zero _ hbr
  field_simp

/-- Powers `Q^{r+1}` of a non-root-of-unity are pairwise distinct. -/
theorem pow_succ_injective (Q : F) (hQ0 : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) :
    Function.Injective (fun r : ℕ => Q ^ (r + 1)) := by
  intro a b h
  simp only at h
  have hab : Q ^ a = Q ^ b := by
    rw [pow_succ, pow_succ] at h
    exact mul_right_cancel₀ hQ0 h
  by_contra hne
  apply hgen ((a : ℤ) - b) (by omega)
  rw [zpow_sub₀ hQ0, zpow_natCast, zpow_natCast, hab, div_self (pow_ne_zero _ hQ0)]

/-- **Interpolation.**  Two polynomials agreeing at every `Q^r`, `r ≥ 1`, agree at `0`. -/
theorem eval_zero_eq_of_eval_pow (Q : F) (hQ0 : Q ≠ 0) (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (p₁ p₂ : F[X]) (h : ∀ r : ℕ, r ≠ 0 → p₁.eval (Q ^ r) = p₂.eval (Q ^ r)) :
    p₁.eval 0 = p₂.eval 0 := by
  have hp : p₁ - p₂ = 0 := by
    apply Polynomial.eq_zero_of_infinite_isRoot
    refine Set.Infinite.mono ?_
      (Set.infinite_range_of_injective (pow_succ_injective Q hQ0 hgen))
    rintro _ ⟨r, rfl⟩
    show IsRoot (p₁ - p₂) (Q ^ (r + 1))
    rw [IsRoot.def, eval_sub, h (r + 1) (Nat.succ_ne_zero r), sub_self]
  have h0 := congrArg (eval 0) hp
  rwa [eval_sub, eval_zero, sub_eq_zero] at h0

/-- **Normalisation**: `Σ_{|ν| = n} f^ν M_ν = 1`. -/
theorem sum_dim_molienWeight_eq_one (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (n : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (numStandardYoungTableaux ν.1 : F) * molienWeight Q ν.1) = 1 := by
  have h := eval_zero_eq_of_eval_pow Q hQ0 hgen
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
      C (numStandardYoungTableaux ν.1 : F) * wenzlPoly Q ν.1) ((1 - X) ^ n) (fun r hr => by
        have hbr := levelBracket_ne_zero_of_gen hgen hr
        simp only [eval_finset_sum, eval_mul, eval_C, eval_pow, eval_sub, eval_one, eval_X,
          eval_pow_wenzlPoly Q hQ0 hbr]
        have hs := sum_dim_wenzlWeight_eq_one Q hQ0 hgen hbr (ne_one_of_gen hgen) n
        have e : ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
            (numStandardYoungTableaux ν.1 : F) * ((1 - Q ^ r) ^ ν.1.cells.card * wenzlWeight r Q ν.1)
              = (1 - Q ^ r) ^ n * ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
                  (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1 := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun ν _ => ?_
          rw [ν.2]
          ring
        rw [e, hs, mul_one])
  simpa [eval_finset_sum, eval_zero_wenzlPoly] using h

/-- **Branching**: `Σ_{s addable} M_{ν+s} = M_ν`. -/
theorem sum_addable_molienWeight (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (ν : YoungDiagram) :
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, molienWeight Q (addCellOrSelf ν s.1))
      = molienWeight Q ν := by
  have h := eval_zero_eq_of_eval_pow Q hQ0 hgen
    (∑ s : {s : ℕ × ℕ // IsAddableCell ν s}, wenzlPoly Q (addCellOrSelf ν s.1))
    ((1 - X) * wenzlPoly Q ν) (fun r hr => by
      have hbr := levelBracket_ne_zero_of_gen hgen hr
      simp only [eval_finset_sum, eval_mul, eval_sub, eval_one, eval_X,
        eval_pow_wenzlPoly Q hQ0 hbr]
      rw [← sum_addable_wenzlWeight_all Q hQ0 hgen hbr (ne_one_of_gen hgen) ν, Finset.mul_sum,
        Finset.mul_sum]
      refine Finset.sum_congr rfl fun s _ => ?_
      rw [addCellOrSelf_of s.2, card_addCell s.2]
      ring)
  simpa [eval_finset_sum, eval_zero_wenzlPoly] using h

/-- **The Markov corner at `z = 0`, abstractly.**  If, at every level `r ≥ 1`, a pair of
`F`-valued data `t, t'` satisfies the level-`r` Markov identity with parameter
`Q^r/(q·[r]_Q)`, then the Molien-weighted sum of `t` vanishes. -/
theorem sum_molienWeight_mul_eq_zero (Q q : F) (hQ0 : Q ≠ 0) (hq : q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {m : ℕ}
    (t : {ρ : YoungDiagram // ρ.cells.card = m + 2} → F)
    (t' : {ν : YoungDiagram // ν.cells.card = m + 1} → F)
    (hw : ∀ r : ℕ, r ≠ 0 →
      ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, wenzlWeight r Q L.1 * t L
        = Q ^ r / (q * levelBracket r Q)
          * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1}, wenzlWeight r Q ν.1 * t' ν) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, molienWeight Q L.1 * t L = 0 := by
  have h := eval_zero_eq_of_eval_pow Q hQ0 hgen
    (∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, C (t L) * wenzlPoly Q L.1)
    (X * C ((1 - Q) / q) * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
      C (t' ν) * wenzlPoly Q ν.1) (fun r hr => by
      have hbr := levelBracket_ne_zero_of_gen hgen hr
      simp only [eval_finset_sum, eval_mul, eval_C, eval_X, eval_pow_wenzlPoly Q hQ0 hbr]
      have e1 : ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
          t L * ((1 - Q ^ r) ^ L.1.cells.card * wenzlWeight r Q L.1)
            = (1 - Q ^ r) ^ (m + 2) * ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
                wenzlWeight r Q L.1 * t L := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun L _ => ?_
        rw [L.2]; ring
      have e2 : ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          t' ν * ((1 - Q ^ r) ^ ν.1.cells.card * wenzlWeight r Q ν.1)
            = (1 - Q ^ r) ^ (m + 1) * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
                wenzlWeight r Q ν.1 * t' ν := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun ν _ => ?_
        rw [ν.2]; ring
      rw [e1, e2, hw r hr, one_sub_pow_eq_mul_levelBracket r Q]
      field_simp
      ring)
  simp only [eval_finset_sum, eval_mul, eval_C, eval_X, eval_zero_wenzlPoly, zero_mul] at h
  calc ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, molienWeight Q L.1 * t L
      = ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2}, t L * molienWeight Q L.1 :=
        Finset.sum_congr rfl fun L _ => mul_comm _ _
    _ = 0 := h

end Generic

namespace SeminormalRep

variable {K : Type*} [Field K]

open QOU.SchurWeyl.TableauCells QOU.SchurWeyl.Seminormal QOU.SchurWeyl.HeckeInclusion

/-- **The Markov corner identity for the Molien weight, at `z = 0`.** -/
theorem markov_molienWeight (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    {m : ℕ} (y : Hecke K q q⁻¹ m) :
    ∑ L : {ρ : YoungDiagram // ρ.cells.card = m + 2},
        molienWeight (q ^ 2) L.1
          * ((seminormalRep q hq hq2 (m + 1) L.2 (heckeIncl K q q⁻¹ m y))
              * genMat q (m + 1) (by omega) L.2.ge).trace
      = 0 * ∑ ν : {ν : YoungDiagram // ν.cells.card = m + 1},
          molienWeight (q ^ 2) ν.1 * (seminormalRep q hq hq2 m ν.2 y).trace := by
  rw [zero_mul]
  exact sum_molienWeight_mul_eq_zero (q ^ 2) q (pow_ne_zero 2 hq) hq
    (gen_of_notRootOfUnity hq2)
    (fun L => ((seminormalRep q hq hq2 (m + 1) L.2 (heckeIncl K q q⁻¹ m y))
      * genMat q (m + 1) (by omega) L.2.ge).trace)
    (fun ν => (seminormalRep q hq hq2 m ν.2 y).trace)
    (fun r hr => markov_wenzlWeight q hq hq2 (gen_of_notRootOfUnity hq2) hr y)

/-- **The Molien Markov trace**: the seminormal trace weighted by `M_μ(q²)`, a Markov trace with
parameter `z = 0`. -/
noncomputable def molienMarkovTrace (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) : HeckeCoset.MarkovTraceFamily K q q⁻¹ 0 :=
  markovTraceOfWeight q hq0 hq2 (molienWeight (q ^ 2)) 0
    (fun n => sum_dim_molienWeight_eq_one (q ^ 2) (pow_ne_zero 2 hq0)
      (gen_of_notRootOfUnity hq2) n)
    (fun ν => sum_addable_molienWeight (q ^ 2) (pow_ne_zero 2 hq0)
      (gen_of_notRootOfUnity hq2) ν)
    (fun _ y => markov_molienWeight q hq0 hq2 y)

theorem molienMarkovTrace_tr (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) :
    (molienMarkovTrace q hq0 hq2).tr = wtraceW q hq0 hq2 (molienWeight (q ^ 2)) := rfl

/-- **Molien equals the symmetrising trace.**  On the coset basis of every `H_n(q)`, the
Molien-weighted seminormal trace is `1` at the identity and `0` at every other element. -/
theorem molienMarkovTrace_symmetrising (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (p : HeckeCoset.cosetIndex m) :
    (p = HeckeCoset.cosetOne m →
        wtraceW q hq0 hq2 (molienWeight (q ^ 2)) m (HeckeCoset.cosetFam m p) = 1) ∧
      (p ≠ HeckeCoset.cosetOne m →
        wtraceW q hq0 hq2 (molienWeight (q ^ 2)) m (HeckeCoset.cosetFam m p) = 0) :=
  (molienMarkovTrace q hq0 hq2).tr_cosetFam_eq_delta m p

/-- **Every `z = 0` Markov trace is the Molien-weighted seminormal trace.** -/
theorem eq_molien_of_zero (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    T.tr n x = wtraceW q hq0 hq2 (molienWeight (q ^ 2)) n x :=
  HeckeCoset.markovTrace_unique T (molienMarkovTrace q hq0 hq2) n x

/-- **Molien is the `z = 0` Ocneanu trace** — the same statement read through
`ocneanuWeight_zero_eq_molienWeight`. -/
theorem wtraceW_ocneanu_zero_eq_molien (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) :
    wtraceW q hq0 hq2 (ocneanuWeight q 0) = wtraceW q hq0 hq2 (molienWeight (q ^ 2)) := by
  congr 1
  funext μ
  exact ocneanuWeight_zero_eq_molienWeight q μ

end SeminormalRep
end QOU.SchurWeyl
