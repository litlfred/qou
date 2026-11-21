import Mathlib.Tactic
import QOU.BraidKnot.KeystoneC8SuperExpBound

/-!
# QOU.Brings.classical_jet_period_zero — the classical-jet prolongation is exact

For the classical (total `d/dz`) jet rule, the prolonged Seiberg–Witten
differential is an exact form for every `n ≥ 1`:

  λ_SW^{(n)} = X^{(n)}(z) dz = d(X^{(n−1)}),

so every local residue and every closed-cycle period vanishes identically —
Stokes/exactness, a proved invariant. Consequently the residue-sum period of
`prop:sw-period-residue-sum` is zero at every vertical degree `n ≥ 1` under the
classical-jet rule, and cannot equal the positive binding period
`a_D^{(m)} = lw(m−1) = I(m)/m > 0`. This is a scope-(b) exclusion of the
classical-jet reading, independent of (and consistent with) the q-freeness
exclusion of PR #2768; the q-difference prolongation is untouched.

LaTeX label: `prop:sw-classical-jet-exactness`.

## Lean structure — derived, not projected

The load-bearing invariant is fully proved on the formal-residue model: a local
Laurent expansion is its coefficient function `f : ℤ → R`, the residue is the
coefficient of `t⁻¹`, and the termwise derivative shifts every exponent down by
one — so the `t⁻¹` coefficient of a derivative is `0·f(0) = 0`
(`fresidue_fderiv`, generic `CommRing R`, §7c wall-safe). The period corollary
composes this with the residue-sum shape of `prop:sw-period-residue-sum`
(period = `2πi · Σ residues`), taken as an explicit hypothesis exactly as in the
sibling `sw_period_eq_residue_sum`; nothing concludes from a conclusion-typed
field. Numerical companion (exact sympy verification at `z = ∞`, sheets
`c ∈ {−1, ±i}`): `computations/lever1_saddle_action_jet_residue_probe.py`.

## References

- [leitner2026] §5-brings-surface/sw-classical-jet-exactness
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: generic `CommRing R` for the formal-residue core (§7c); `ℂ`
only in the period corollary (archimedean realisation, matching
`sw-period-residue-sum.lean`). See `GroundRingAnnotations.lean`.
-/

namespace QOU.Brings

open scoped BigOperators

section FormalResidue

variable {R : Type*} [CommRing R]

/-- Formal residue of a local Laurent expansion, presented as its coefficient
function `f : ℤ → R`: the coefficient of `t⁻¹`. -/
def fresidue (f : ℤ → R) : R := f (-1)

/-- Termwise derivative of a formal Laurent expansion:
`(Σ c_e tᵉ)' = Σ (e+1)·c_{e+1} tᵉ`. -/
def fderiv (f : ℤ → R) : ℤ → R := fun e => (e + 1) • f (e + 1)

/-- **The residue of an exact form vanishes**: the `t⁻¹` coefficient of a
termwise derivative is `((−1)+1)·f(0) = 0`. This is the invariant behind the
(b)-exclusion: `d(anything)` has no residue, anywhere, ever. -/
theorem fresidue_fderiv (f : ℤ → R) : fresidue (fderiv f) = 0 := by
  show ((-1 : ℤ) + 1) • f (-1 + 1) = 0
  norm_num

/-- The `n`-th classical jet of a local expansion: `n`-fold termwise derivative
(the coefficient-level face of `X^{(n)} = dⁿX/dzⁿ` on the curve). -/
def jet (X : ℤ → R) : ℕ → ℤ → R
  | 0 => X
  | n + 1 => fderiv (jet X n)

/-- Every positive-order classical jet is exact — `jet X (n+1) = fderiv (jet X n)`
is a derivative — so its residue vanishes at every point. -/
theorem fresidue_jet_succ (X : ℤ → R) (n : ℕ) : fresidue (jet X (n + 1)) = 0 :=
  fresidue_fderiv _

end FormalResidue

/-- **Exactness kills the classical-jet period.** If the period is `2πi` times
the residue sum (`prop:sw-period-residue-sum`, hypothesis `hperiod`) and every
local residue is that of a positive-order classical jet (`hres` — the local
face of `λ_SW^{(n+1)} = d(X^{(n)})`), the period vanishes. -/
theorem classical_jet_period_zero {k n : ℕ}
    (residues : Fin k → ℂ) (period twoPiI : ℂ)
    (hperiod : period = twoPiI * ∑ p, residues p)
    (Xs : Fin k → ℤ → ℂ)
    (hres : ∀ p, residues p = fresidue (jet (Xs p) (n + 1))) :
    period = 0 := by
  have hz : ∀ p, residues p = 0 := fun p => by
    rw [hres p]; exact fresidue_jet_succ _ _
  simp [hperiod, hz]

/-- `I(m) ≠ 0` for the involution numbers (ℕ-valued form of the library lemma
`QOU.BraidKnot.YoungTableauStandard.involutionNumber_pos`; restated here so the
content-block sibling does not pull that module's dependency cone). -/
theorem involutionNumber_ne_zero :
    ∀ m, QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber m ≠ 0 := by
  intro m
  induction m using Nat.twoStepInduction with
  | zero => decide
  | one => decide
  | more m ih1 ih2 =>
    have hstep : QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber (m + 2)
        = QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber (m + 1)
          + (m + 1) * QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber m := rfl
    omega

/-- **The classical-jet period cannot be the binding period.** The classical
binding period `a_D^{(m)} = lw(m−1) = I(m)/m` is nonzero for `m ≥ 1`, while the
classical-jet period is identically zero — so the classical-jet reading of the
identification `a_D^{(n)} = ∮ λ_SW^{(n)}` fails on every cycle. -/
theorem classical_jet_period_ne_lw {k n : ℕ}
    (residues : Fin k → ℂ) (period twoPiI : ℂ)
    (hperiod : period = twoPiI * ∑ p, residues p)
    (Xs : Fin k → ℤ → ℂ)
    (hres : ∀ p, residues p = fresidue (jet (Xs p) (n + 1)))
    (m : ℕ) (hm : 0 < m) :
    period ≠ (QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber m : ℂ) / m := by
  rw [classical_jet_period_zero residues period twoPiI hperiod Xs hres]
  have hI : (QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber m : ℂ) ≠ 0 := by
    exact_mod_cast involutionNumber_ne_zero m
  have hmc : (m : ℂ) ≠ 0 := by exact_mod_cast hm.ne'
  intro h
  field_simp at h
  rw [zero_mul] at h
  exact hI h.symm

end QOU.Brings
