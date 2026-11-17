import Mathlib.Tactic

/-!
# Collective Regime Positivity and Reeb Override Constant Offset (`qou-ls86`, `qou-xzda`)

This module formalizes two nuclear-binding structural results under `qou-v2om`:

1. **Collective many-body residual positivity and boundedness (`qou-ls86`)**:
   The per-nucleon collective residual `R(A)/A = (B_AME - B_sym)/A = B_AME/A - B_sym/A`
   is strictly positive and two-sidedly bounded on any well-bound regime where
   `B_AME/A ∈ [b_lo, b_hi]`, `B_sym/A ∈ [c_lo, c_hi]`, and `c_hi < b_lo`, whereas on the
   weakly bound / drip-line regime where the positive-floor chain over-binds
   (`B_AME/A < B_sym/A`), `R(A)/A < 0`.

2. **Constant `A`-independent offset from the `L_pn` Reeb override (`qou-xzda`)**:
   In the chain binding closed form `B_sym = α · ((Z - 1) L_pp + L_pn + (N - 1) L_nn)`,
   the `p-n` interface enters with multiplicity `1` for every `(Z, N)`. Consequently,
   replacing the trace-derived `L_pn_trace` by the Reeb-flow bound `L_pn_reeb` shifts
   `B_sym` by the exact `A`-independent constant `α · (L_pn_trace - L_pn_reeb)` across
   every isotope (`2H`, `3H`, `3He`, `4He`, ...).
-/

namespace QOU.MassTheory

/-- Per-nucleon collective many-body residual `(B_AME - B_sym) / A`. -/
def collectivePerNucleon (B_AME B_sym A : ℚ) : ℚ :=
  (B_AME - B_sym) / A

/-- Exact decomposition of the per-nucleon collective residual as the difference of
per-nucleon binding energies (`qou-ls86`). -/
theorem collectivePerNucleon_eq_sub_perNucleon (B_AME B_sym A : ℚ) :
    collectivePerNucleon B_AME B_sym A = B_AME / A - B_sym / A := by
  unfold collectivePerNucleon
  exact sub_div B_AME B_sym A

/-- On the well-bound regime (`c_hi < b_lo`, `B_AME/A ∈ [b_lo, b_hi]`, and
`B_sym/A ∈ [c_lo, c_hi]`), the per-nucleon collective residual is strictly positive
and bounded in `[b_lo - c_hi, b_hi - c_lo]`, while on the over-bound drip-line regime
(`B_AME_drip/A < B_sym_drip/A`) it is strictly negative (`qou-ls86`). -/
theorem wellBound_regime_collective_pos_and_bounded
    (B_AME B_sym B_AME_drip B_sym_drip A b_lo b_hi c_lo c_hi : ℚ)
    (h_b_lo : b_lo ≤ B_AME / A) (h_b_hi : B_AME / A ≤ b_hi)
    (h_c_lo : c_lo ≤ B_sym / A) (h_c_hi : B_sym / A ≤ c_hi)
    (h_sep : c_hi < b_lo)
    (h_drip : B_AME_drip / A < B_sym_drip / A) :
    0 < collectivePerNucleon B_AME B_sym A ∧
    b_lo - c_hi ≤ collectivePerNucleon B_AME B_sym A ∧
    collectivePerNucleon B_AME B_sym A ≤ b_hi - c_lo ∧
    collectivePerNucleon B_AME_drip B_sym_drip A < 0 := by
  rw [collectivePerNucleon_eq_sub_perNucleon, collectivePerNucleon_eq_sub_perNucleon]
  refine ⟨by linarith, by linarith, by linarith, by linarith⟩

/-- Chain binding energy closed form `α · ((Z - 1) L_pp + L_pn + (N - 1) L_nn)`
with a single `p-n` interface slot (`qou-xzda`). -/
def chainBinding (alpha L_pp L_pn L_nn Z N : ℚ) : ℚ :=
  alpha * ((Z - 1) * L_pp + L_pn + (N - 1) * L_nn)

/-- Replacing `L_pn_trace` by `L_pn_reeb` shifts `chainBinding` by the exact
`(Z, N)`-independent constant `α · (L_pn_trace - L_pn_reeb)` (`qou-xzda`). -/
theorem reebOverride_shift_is_constant
    (alpha L_pp L_pn_trace L_pn_reeb L_nn Z₁ N₁ Z₂ N₂ : ℚ) :
    chainBinding alpha L_pp L_pn_trace L_nn Z₁ N₁ -
      chainBinding alpha L_pp L_pn_reeb L_nn Z₁ N₁ =
      alpha * (L_pn_trace - L_pn_reeb) ∧
    chainBinding alpha L_pp L_pn_trace L_nn Z₁ N₁ -
      chainBinding alpha L_pp L_pn_reeb L_nn Z₁ N₁ =
      chainBinding alpha L_pp L_pn_trace L_nn Z₂ N₂ -
      chainBinding alpha L_pp L_pn_reeb L_nn Z₂ N₂ := by
  unfold chainBinding
  constructor <;> ring

/-- Whenever `α ≠ 0` and `L_pn_trace ≠ L_pn_reeb`, the Reeb-overridden chain closed form
differs strictly from the trace-derived chain at every `(Z, N)` (`qou-xzda`). -/
theorem reebOverride_nonzero_of_distinct
    (alpha L_pp L_pn_trace L_pn_reeb L_nn Z N : ℚ)
    (h_alpha : alpha ≠ 0) (h_diff : L_pn_trace ≠ L_pn_reeb) :
    chainBinding alpha L_pp L_pn_trace L_nn Z N ≠
      chainBinding alpha L_pp L_pn_reeb L_nn Z N := by
  intro h_eq
  have h_sub :
      chainBinding alpha L_pp L_pn_trace L_nn Z N -
        chainBinding alpha L_pp L_pn_reeb L_nn Z N = 0 := sub_eq_zero.mpr h_eq
  have h_id := (reebOverride_shift_is_constant alpha L_pp L_pn_trace L_pn_reeb L_nn Z N Z N).1
  rw [h_sub] at h_id
  rcases mul_eq_zero.mp h_id.symm with ha | hL
  · exact h_alpha ha
  · exact h_diff (sub_eq_zero.mp hL)

end QOU.MassTheory
