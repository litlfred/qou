/-
# The C and D Markov parameters coincide at `q = 1` — and only there

Bean `qou-cds1` (re-derive the Q_β `c_k` ladder under convention D).

The 2026-08-15 owner ruling makes convention **D** (`z_D = q³/(q²+1)`)
canonical and excises **C** (`z_C = √q/(q+1)`).  The corpus already proves the
two are *different* on the substrate branch:
`QOU.QBeta.decayLadder_zC_not_jones` shows `z·[2]_q = q²` — which characterises
`z_D` — fails for `z_C` when `s > 1`, the denominator-cleared obstruction being
`s⁷ + s⁵ ≠ s⁴ + 1`.

What was **not** recorded is the complementary half: `s = 1` *is* a root of that
locus, so the two conventions define the **same** Markov parameter at `q = 1`.
That is the point at which the ladder's N=3 rung is evaluated
(`c₃ = J_Hopf(q = 1) = −2`, `QOU.BraidKnot.jonesHopfClassicalLimit`), so the
ruling leaves that proposed coefficient untouched while moving everything
evaluated at the substrate `q₀ ≈ 1.11`.

**Scope.** This is a statement about *which rungs the C→D ruling can move*, and
it is a pruning result, not a positive one.  `c₃ = −2` surviving the frame
change is not evidence for it: its only empirical support was the 3.47 %
near-match to the C-frame extraction, and that support does not transfer.  See
`computations/qbeta/qbeta_zcd_classical_coincidence_probe.py` (7/7, exact ℚ).

Working in the substrate variable `s` with `q = s²`, so that `z_C = s/(s²+1)`
and `z_D = s⁶/(s⁴+1)` are both rational and no `Real.sqrt` is needed.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

namespace QOU.QBeta

/-! ## The coincidence locus, as a ring identity -/

/-- The denominator-cleared coincidence locus of `z_C` and `z_D`, factored.

This is the identity behind `decayLadder_zC_not_jones`'s `s⁷ + s⁵ = s⁴ + 1`:
the polynomial has `s = 1` as a root, and the cofactor has all-positive
coefficients.  Pure `CommRing` content — no ordering, no archimedean structure
(AGENTS.md §7c). -/
theorem coincidenceLocus_factor {R : Type*} [CommRing R] (s : R) :
    s ^ 7 + s ^ 5 - s ^ 4 - 1
      = (s - 1) * (s ^ 6 + s ^ 5 + 2 * s ^ 4 + s ^ 3 + s ^ 2 + s + 1) := by
  ring

/-! ## The two parameters, in the substrate variable `q = s²` -/

/-- Convention **C** Markov parameter in the substrate variable: `z_C = s/(s²+1)`
(i.e. `√q/(q+1)` at `q = s²`).  Excised as canonical by the 2026-08-15 ruling;
retained here only to state the comparison. -/
noncomputable def zCsub (s : ℝ) : ℝ := s / (s ^ 2 + 1)

/-- Convention **D** Markov parameter (canonical) in the substrate variable:
`z_D = s⁶/(s⁴+1)` (i.e. `q³/(q²+1)` at `q = s²`). -/
noncomputable def zDsub (s : ℝ) : ℝ := s ^ 6 / (s ^ 4 + 1)

/-- At the classical point `q = 1` (`s = 1`) convention C gives `1/2`. -/
theorem zCsub_one : zCsub 1 = 1 / 2 := by
  unfold zCsub; norm_num

/-- At the classical point `q = 1` (`s = 1`) convention D gives `1/2`. -/
theorem zDsub_one : zDsub 1 = 1 / 2 := by
  unfold zDsub; norm_num

/-- **The classical-limit coincidence.**  The two conventions define the *same*
Markov parameter at `q = 1`.  This is why a ladder coefficient obtained as a
`q = 1` evaluation of a Markov-trace invariant — `c₃ = J_Hopf(1) = −2` — is
unmoved by the C→D ruling. -/
theorem zCsub_eq_zDsub_one : zCsub 1 = zDsub 1 := by
  rw [zCsub_one, zDsub_one]

/-! ## …and only there, on the substrate branch -/

/-- The cofactor of the coincidence locus is strictly positive for `s > 0`
(all coefficients positive). -/
theorem coincidenceLocus_cofactor_pos {s : ℝ} (hs : 0 < s) :
    0 < s ^ 6 + s ^ 5 + 2 * s ^ 4 + s ^ 3 + s ^ 2 + s + 1 := by
  positivity

/-- **The coincidence is isolated.**  For `s > 0`, the two Markov parameters
agree exactly at `s = 1` (`q = 1`) and nowhere else.

The forward direction is the sharp form of `decayLadder_zC_not_jones`: that
theorem rules out `s > 1`, while this rules out every positive `s ≠ 1`,
including the interval `0 < s < 1`. -/
theorem zCsub_eq_zDsub_iff {s : ℝ} (hs : 0 < s) : zCsub s = zDsub s ↔ s = 1 := by
  have h2 : (0 : ℝ) < s ^ 2 + 1 := by positivity
  have h4 : (0 : ℝ) < s ^ 4 + 1 := by positivity
  constructor
  · intro h
    -- Clear denominators: `s·(s⁴+1) = s⁶·(s²+1)`, i.e. `s·(locus) = 0`.
    have hcl : s * (s ^ 4 + 1) = s ^ 6 * (s ^ 2 + 1) := by
      unfold zCsub zDsub at h
      exact (div_eq_div_iff (ne_of_gt h2) (ne_of_gt h4)).mp h
    have hlocus : s * (s ^ 7 + s ^ 5 - s ^ 4 - 1) = 0 := by
      have hrw : s * (s ^ 7 + s ^ 5 - s ^ 4 - 1)
          = s ^ 6 * (s ^ 2 + 1) - s * (s ^ 4 + 1) := by ring
      rw [hrw, hcl]; ring
    have hfac : s * ((s - 1)
        * (s ^ 6 + s ^ 5 + 2 * s ^ 4 + s ^ 3 + s ^ 2 + s + 1)) = 0 := by
      rw [← coincidenceLocus_factor s]; exact hlocus
    have hco := coincidenceLocus_cofactor_pos hs
    have hs' : s ≠ 0 := ne_of_gt hs
    have : s - 1 = 0 := by
      rcases mul_eq_zero.mp hfac with h0 | h1
      · exact absurd h0 hs'
      · rcases mul_eq_zero.mp h1 with h2' | h3'
        · exact h2'
        · exact absurd h3' (ne_of_gt hco)
    linarith
  · rintro rfl
    exact zCsub_eq_zDsub_one

end QOU.QBeta
