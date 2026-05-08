/-!
# PL/JSJ mass-integration equivalence (synthesis conjecture class)

The conjecture: the categorical Markov trace equals the SW thimble
integral over thimbles bounded by JSJ cusps, with thimble base points
at the τ_arch-images of the q-Pochhammer denominator zeros.

This is the synthesis statement of the PL/SW/JSJ subsection.
Per CLAUDE.md §3b, downstream-of-conjectures statements are
themselves conjectures.

-- Ref: [manuscript] conj:pl-jsj-mass-integration-equivalence
-- Ref: [witten2011] https://doi.org/10.1090/amsip/050/19
-- Ref: [yekutieli2015] https://doi.org/10.1093/imrn/rnu123
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.PicardLefschetz

/-- Placeholder for the prolonged Seiberg-Witten differential.
    Concrete model: returns 0 + 0i. -/
-- Ref: [manuscript] prop:sw-period-thimble-equivalence
def lambdaSW (_k : ℕ) (_z : ℂ) : ℂ := 0

/-- Placeholder thimble integral.  Concrete model: returns 0. -/
-- Ref: [manuscript] def:picard-lefschetz-thimble
def thimbleIntegral (_k : ℕ) (_z_c : ℂ) : ℂ := 0

/-- Placeholder JSJ piecewise hyperbolic-volume sum.  Concrete
    model: returns 0. -/
-- Ref: [manuscript] conj:phi-q-tower-jsj-bridge
def descendedJSJVolume (_T_w : ℕ) : ℂ := 0

/-- Placeholder algebraic Markov trace.  Concrete model: returns 0. -/
-- Ref: [manuscript] prop:categorical-mass-markov
def algebraicMarkovTrace (_k : ℕ) (_T_w : ℕ) : ℂ := 0

/-- The synthesis conjecture, packaged as a typeclass over a vertical
    degree `k`, a transient state index `T_w`, and the depth `n` of
    its q-Pochhammer partial product.  An instance carries thimble
    base points `z_c_σ : Fin n → ℂ` (data) plus the equality of the
    algebraic Markov trace and the descended JSJ volume + transient
    SW thimble integral.

    Note: `class … : Type` (not `Prop`) because the thimble base
    points and intersection numbers are data, not propositions. -/
-- Ref: [manuscript] conj:pl-jsj-mass-integration-equivalence
class PLJSJMassIntegration
    (k : ℕ) (T_w : ℕ) (n : ℕ) : Type where
  /-- Thimble base points (`τ_arch`-images of the algebraic
      denominator zeros) and Lefschetz intersection numbers. -/
  -- Ref: [manuscript] conj:denominator-zeros-as-sw-critical-points
  thimble_base_points :
    Fin n → ℂ
  intersection_numbers :
    Fin n → ℤ
  /-- The two-piece mass equality: descended JSJ volume + transient
      SW thimble sum equals the τ-image of the categorical Markov
      trace. -/
  -- Ref: [manuscript] conj:pl-jsj-mass-integration-equivalence
  mass_equality :
    algebraicMarkovTrace k T_w
      = descendedJSJVolume T_w
      + (Finset.univ.sum (fun σ : Fin n =>
          (intersection_numbers σ : ℂ) *
            thimbleIntegral k (thimble_base_points σ)))

/-- Stated form of the conjecture (inhabited via a class instance). -/
-- Ref: [manuscript] conj:pl-jsj-mass-integration-equivalence
theorem pl_jsj_mass_integration
    (k : ℕ) (T_w : ℕ) (n : ℕ)
    [h : PLJSJMassIntegration k T_w n] :
    algebraicMarkovTrace k T_w
      = descendedJSJVolume T_w
      + (Finset.univ.sum (fun σ : Fin n =>
          (h.intersection_numbers σ : ℂ) *
            thimbleIntegral k (h.thimble_base_points σ))) :=
  h.mass_equality

/-- **Skeleton instance.**  All concrete defs of `lambdaSW`,
    `thimbleIntegral`, `descendedJSJVolume`, `algebraicMarkovTrace`
    return zero, so the mass-equality field reduces to `0 = 0 + Σ·0 = 0`
    and closes by `simp`. -/
-- Ref: [manuscript] conj:pl-jsj-mass-integration-equivalence §"Skeleton"
instance skeleton (k : ℕ) (T_w : ℕ) (n : ℕ) :
    PLJSJMassIntegration k T_w n where
  thimble_base_points := fun _ => 0
  intersection_numbers := fun _ => 0
  mass_equality := by
    show (0 : ℂ) = 0 + Finset.univ.sum
      (fun σ : Fin n => ((0 : ℤ) : ℂ) * 0)
    simp

end QOU.PicardLefschetz
