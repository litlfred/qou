import QOU.BraidsAndKnots.MarkovTraceIsMarkov
import HeckeTemperleyLieb.MarkovTraceSymmetries

/-!
# QOU.BraidsAndKnots.MarkovMirrorRefutation — P and CPT fail on a Markov trace that exists

`QOU.IwahoriHecke.MarkovTraceSymmetries.mirror_not_trace_preserving` and
`cpt_not_trace_preserving` say that *every* Markov trace with `a ≠ 0` fails the mirror (`P`,
`q` held fixed) and the composite `C·P·T` at the one-letter braid `σ₀`. A universal
negative is only informative if such a trace exists. This file applies the two theorems
to the corpus's `HeckeAlgebra` / `MarkovTrace` classes under the cross-level Markov property
(M3), and then to the concrete trace `markovTraceH2`, which satisfies (M3) for every `z`
(`isMarkov_H2`). So the refutation of `conj:p-from-braid-mirror` (trace-preservation part)
and of `conj:cpt-d6-d7-d8-closure` has a concrete witness: `H₂(q)` over any field with
`q − q⁻¹ ≠ 0`, every `z`, braid `σ₀`, values `z` and `z − (q − q⁻¹)`.

The point `q = 2` in `ℚ` below is only a certificate that the hypothesis `q − q⁻¹ ≠ 0` is
satisfiable; it is not a physical value and nothing depends on it.

-- Ref: [leitner2026] conj:p-from-braid-mirror, conj:cpt-d6-d7-d8-closure
-/

namespace QOU.BraidsAndKnots.MarkovMirrorRefutation

open QOU.Hecke QOU.IwahoriHecke.MarkovTraceSymmetries

universe u

section General

variable {K : Type u} [Field K] (q : K) {n : ℕ} {A : Type u} [Ring A] [Algebra K A]
  [HA : HeckeAlgebra K n q A]

/-- **P fails on every (M3) Markov trace** on a Hecke algebra with at least one generator,
whenever `q − q⁻¹ ≠ 0`. -/
theorem mirror_fails_of_isMarkov (MT : MarkovTrace n q A) (h : MT.IsMarkov) (hn : 0 < n - 1)
    (hq : q - q⁻¹ ≠ 0) :
    ¬ ∀ w : List (Fin (n - 1) × Bool),
        MT.trace (evalWord (stdα (q - q⁻¹)) stdβ (genSeq HA) (mirror w))
          = MT.trace (evalWord (stdα (q - q⁻¹)) stdβ (genSeq HA) w) :=
  mirror_not_trace_preserving MT.z_param MT.trace MT.normalised hn h.genSeq hq

/-- **CPT fails on every (M3) Markov trace**, same hypotheses. -/
theorem cpt_fails_of_isMarkov (MT : MarkovTrace n q A) (h : MT.IsMarkov) (hn : 0 < n - 1)
    (hq : q - q⁻¹ ≠ 0) :
    ¬ ∀ w : List (Fin (n - 1) × Bool),
        MT.trace (evalWord (stdα (q - q⁻¹)) stdβ (genSeq HA) (cpt w))
          = MT.trace (evalWord (stdα (q - q⁻¹)) stdβ (genSeq HA) w) :=
  cpt_not_trace_preserving MT.z_param MT.trace MT.normalised hn h.genSeq hq

/-- **T holds on every (M3) Markov trace**, every `n`. -/
theorem reverse_of_isMarkov (MT : MarkovTrace n q A) (h : MT.IsMarkov)
    (w : List (Fin (n - 1) × Bool)) :
    MT.trace (evalWord (stdα (q - q⁻¹)) stdβ (genSeq HA) w.reverse)
      = MT.trace (evalWord (stdα (q - q⁻¹)) stdβ (genSeq HA) w) :=
  markov_reverse genSeq_heckeFamily MT.z_param MT.trace MT.normalised MT.cyclic h.genSeq _ _ w

end General

section Concrete

/-- **The concrete witness.** On `H₂(q)` with its Markov trace, for every `z`, the mirror is
not trace-preserving whenever `q − q⁻¹ ≠ 0`. -/
theorem mirror_fails_H2 {K : Type u} [Field K] (q : K) (z : K) (hq : q - q⁻¹ ≠ 0) :
    ¬ ∀ w : List (Fin (2 - 1) × Bool),
        (MarkovTraceH2.markovTraceH2 K q z).trace
            (evalWord (stdα (q - q⁻¹)) stdβ (genSeq (inferInstance : HeckeAlgebra K 2 q _))
              (mirror w))
          = (MarkovTraceH2.markovTraceH2 K q z).trace
            (evalWord (stdα (q - q⁻¹)) stdβ (genSeq (inferInstance : HeckeAlgebra K 2 q _)) w) :=
  mirror_fails_of_isMarkov q _ (MarkovTraceIsMarkov.isMarkov_H2 K q z) (by norm_num) hq

/-- The hypothesis is satisfiable: `q = 2` in `ℚ` gives `q − q⁻¹ = 3/2`. -/
theorem two_sub_inv_ne_zero : (2 : ℚ) - 2⁻¹ ≠ 0 := by norm_num

end Concrete

end QOU.BraidsAndKnots.MarkovMirrorRefutation
