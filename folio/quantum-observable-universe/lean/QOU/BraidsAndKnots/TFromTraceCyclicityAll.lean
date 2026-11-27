import QOU.BraidsAndKnots.TFromTraceCyclicity
import HeckeTemperleyLieb.HeckeTraceReversal

/-!
# QOU.BraidsAndKnots.TFromTraceCyclicityAll — `conj:t-from-trace-cyclicity` for every `n`

The instance `TFromTraceCyclicity n d` for every number of strands `n` and every dimension
`d`: every character of every Hecke representation `ρ : HeckeRep n d` takes the same value
on a signed braid word and on its reversal. So the conjecture is a theorem.

The work is `QOU.IwahoriHecke.HeckeTraceReversal.cyclic_reverse` (every cyclic functional on
an algebra with a type-`A` Hecke family is reversal invariant). Here the generators of `ρ`
are packaged as such a family and the matrix trace is the functional.

-- Ref: [leitner2026] conj:t-from-trace-cyclicity
-/

namespace QOU.BraidsAndKnots.TFromTraceCyclicityAll

open QOU.IwahoriHecke.JonesNormalForm QOU.IwahoriHecke.MarkovTraceSymmetries
open QOU.IwahoriHecke.HeckeTraceReversal QOU.Archimedean Matrix

variable {n d : ℕ}

/-- The generators of `ρ` as an `ℕ`-indexed family (`0` past the top). -/
noncomputable def genFamily (ρ : HeckeRep n d) : ℕ → Matrix (Fin d) (Fin d) R_t :=
  fun i => if h : i < n - 1 then ρ.gen ⟨i, h⟩ else 0

theorem genFamily_of_lt (ρ : HeckeRep n d) {i : ℕ} (h : i < n - 1) :
    genFamily ρ i = ρ.gen ⟨i, h⟩ := dif_pos h

theorem genFamily_hecke (ρ : HeckeRep n d) :
    HeckeFamily (n - 1) HA_t (1 : R_t) (genFamily ρ) where
  quad i hi := by rw [genFamily_of_lt ρ hi, ρ.hecke_rel, one_smul]
  braid i hi := by
    rw [genFamily_of_lt ρ (by omega), genFamily_of_lt ρ hi]
    exact ρ.braid_adj i (by omega) hi
  comm i j hij hj := by
    rw [genFamily_of_lt ρ (by omega), genFamily_of_lt ρ hj]
    exact ρ.braid_far ⟨i, by omega⟩ ⟨j, hj⟩ (by simpa using hij)

/-- `HeckeRep.eval` is `evalWord` in the standard convention. -/
theorem eval_eq_evalWord (ρ : HeckeRep n d) (w : Archimedean.BraidWord n) :
    ρ.eval w = evalWord (stdα HA_t) stdβ (genFamily ρ) (N := n - 1) w := by
  induction w with
  | nil => rfl
  | cons p w ih =>
    obtain ⟨i, e⟩ := p
    have hi : (i : ℕ) < n - 1 := i.isLt
    cases e
    · show ρ.genInv i * ρ.eval w = _
      rw [evalWord_cons, ← ih]
      congr 1
      simp only [letter, stdα, stdβ, HeckeRep.genInv, genFamily_of_lt ρ hi]
      simp [neg_smul, sub_eq_add_neg, add_comm]
    · show ρ.gen i * ρ.eval w = _
      rw [evalWord_cons, ← ih]
      congr 1
      simp [letter, stdα, stdβ, genFamily_of_lt ρ hi]

/-- **`conj:t-from-trace-cyclicity`, unconditionally, for every `n` and `d`.** -/
theorem markovTrace_timeReversal (ρ : HeckeRep n d) (w : Archimedean.BraidWord n) :
    MathlibExt.MarkovTrace.markovTrace ρ (timeReversal w)
      = MathlibExt.MarkovTrace.markovTrace ρ w := by
  simp only [MathlibExt.MarkovTrace.markovTrace, HeckeRep.character, timeReversal,
    eval_eq_evalWord]
  exact cyclic_reverse (genFamily_hecke ρ) (Matrix.traceLinearMap (Fin d) R_t R_t)
    (fun x y => Matrix.trace_mul_comm x y) _ _ w

/-- The instance: the T conjecture holds for every `n` and `d`. -/
instance tFromTraceCyclicity : TFromTraceCyclicity n d where
  trace_reversal_invariant := markovTrace_timeReversal

end QOU.BraidsAndKnots.TFromTraceCyclicityAll
