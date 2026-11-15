/-
  # Leading-order N_v from Bring action + tower depth

  Combines the two upstream conjectures:
    conj:n-v-bring-action      (S_5 acts on H_n at EW slice)
    conj:n-v-tower-depth-ninety (depth from m_e to v = 90)

  to derive the leading-order closure
    N_v = |S_5| · q_0^90 = 120 · q_0^90

  This is a CONDITIONAL theorem: derived from the two upstream
  axioms, modulo the sub-leading correction (currently a separate
  conjecture for the residual 0.58%).

  Ref: [leitner2026] `conj:n-v-leading-order-derivation`,
       [leitner2026] `conj:n-v-bring-action`,
       [leitner2026] `conj:n-v-tower-depth-ninety`.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

namespace QOU.Observations

/-- The substrate parameter q_0 ≈ 1.10998 (witness-pinned). -/
def q_0_real : ℝ := 1.10998

/-- The electron rest mass m_e (CODATA 2022, in MeV). -/
def m_e_real : ℝ := 0.51099895069

/-- The electroweak scale v ≈ 246 GeV (= 246220 MeV).  PDG vacuum
    expectation value `v ≈ 246.220 GeV`. -/
def v_ew_real : ℝ := 246220

/-- Definition of N_v from `ex:hadron-half-life-verification`:
    N_v := 3 v / m_e. -/
noncomputable def N_v : ℝ := 3 * v_ew_real / m_e_real

/-- **Bridge axiom (depth + Bring rescaling → ratio).**

    The Coxeter-length tower depth equation
    `tower_depth level_m_e level_v = 90` (Lemma 2) and the
    Markov-trace-residual `|S_5| = 120` rescaling at the EW slice
    (Lemma 1) combine into the real-valued mass-ratio identity

      `v / m_e = (|S_5| / 3) · q_0^90 = 40 · q_0^90`

    modulo a small sub-leading correction (`|ε₁| ≤ 0.006` ⇔ ≤ 0.6%
    deviation from `v / m_e = 40 · q_0^90`).

    The factor of `40 = |S_5| / 3` is the categorical contribution
    of the Bring-fibre-functor: the `|S_5| = 120` Markov-trace
    rescaling at the EW slice (`NVBringAction`) factors
    through the `3`-fold splitting `N_v := 3 · v / m_e`, leaving
    `|S_5| / 3 = 40` as the residual prefactor on the
    `v / m_e ↔ q_0^{depth}` bridge.

    Mathematical content: each Hecke generation rescales the mass
    scale by `q_0` (per `def:hecke-mass-element` and the
    brane-tower construction), giving `v / m_e ∝ q_0^{depth}`.
    The proportionality constant is the `|S_5| / 3 = 40` Bring
    factor, so the full bridge is `v / m_e = 40 · q_0^90 (1 + ε)`.

    Numeric check at `q_0 = 1.10998`, recomputed 2026-09-03 in
    exact rational arithmetic and cross-checked at 50 dps:

      `v / m_e   = 481 840.5197…`
      `q_0^90    =  11 977.4350…`
      `ratio     =      40.2290…`
      `ε         =       0.0057255983…`

    so `|ε| ≤ 0.006` holds with a headroom factor of **1.048** — the
    bound is satisfied by 4.8 %, not comfortably.

    🛑 The three figures this docstring carried until 2026-09-03 were
    all wrong: `q_0^90 ≈ 12 012` (0.29 % high), `ratio ≈ 40.11`, and
    `ε ≈ 0.003`.  The last understates the residual by 1.9× and made
    the bound look roughly twice as slack as it is.

    Status: **this statement is a THEOREM, not an axiom** — see below.
    What remains open is not it.

    Ref: [leitner2026] `def:hecke-mass-element`,
         `conj:mass-endomorphism`,
         `conj:n-v-bring-action`,
         `conj:n-v-tower-depth-ninety`.

    ## This was an `axiom` until 2026-09-03, and should never have been one

    `q_0_real`, `m_e_real` and `v_ew_real` are concrete decimal literals, so
    the statement below is a *finite arithmetic fact* about rationals, not an
    open claim: take `ε₁` to be the exact residual and discharge the bound by
    `norm_num`.  Assuming a decidable numeric statement as an axiom is the
    shape AGENTS.md §"Axiomatization is NOT a Proof" warns about, and it cost
    something real — every downstream result named `v_over_m_e_bridge` in
    `#print axioms`, so nothing in this file was axiom-clean.

    🛑 **What this proof does NOT establish, stated because the temptation to
    read it as more is exactly why the axiom was there.** Proving the number
    does not derive the *structure*: that the prefactor is `|S_5| / 3 = 40`
    for a categorical reason, and that the Coxeter tower depth from `m_e` to
    `v` is `90`.  Fix those two integers and the rest is arithmetic — which is
    precisely why the axiom carried **no conjectural content whatsoever**.  It
    asserted the arithmetic and left the categorical claim unstated.

    The genuinely open work is unchanged and is what the docstring above used
    to list: (i) `BraneTowerLevel` as a GB filtration grade, (ii) the
    `q_0`-rescaling-per-generation lemma, (iii) the categorical derivation of
    the `|S_5| / 3` Bring fibre-functor contribution.  None exist in Lean, and
    no object in this file expresses them — deliberately not invented here,
    since a carrier that merely re-pins `120` and `90` would be provable and
    so would assert nothing.  Tracked as a bean. -/
theorem v_over_m_e_bridge :
    ∃ ε₁ : ℝ, abs ε₁ ≤ 0.006 ∧
      v_ew_real / m_e_real = 40 * q_0_real^(90 : ℕ) * (1 + ε₁) := by
  have hq : (0:ℝ) < q_0_real := by norm_num [q_0_real]
  have hp : (0:ℝ) < q_0_real ^ (90:ℕ) := by positivity
  have hm : (0:ℝ) < m_e_real := by norm_num [m_e_real]
  refine ⟨v_ew_real / (m_e_real * (40 * q_0_real ^ (90:ℕ))) - 1, ?_, ?_⟩
  · rw [abs_le]
    constructor <;> rw [q_0_real, m_e_real, v_ew_real] <;> norm_num
  · field_simp
    ring

/-- **Theorem (Leading-order N_v).**

    Conditional on
    [`NVBringAction`](./n-v-bring-action.lean) and
    [`tower_depth_m_e_to_v_is_ninety`](./n-v-tower-depth-ninety.lean)
    for its *meaning* — but, as of 2026-09-03, on no axiom for its
    *proof*: `v_over_m_e_bridge` above is now a theorem, so this
    result is axiom-clean.  The
    electroweak topological invariant `N_v` admits the
    leading-order closure

      `N_v = 120 · q_0^90`    (residual `≤ 0.6%`)

    where `120 = 3 · 40 = 3 · (|S_5| / 3) = |S_5|` recovers the
    full Bring-automorphism-group order from the explicit `3` in
    `N_v := 3 v / m_e` and the `|S_5| / 3` Bring contribution
    folded into the bridge axiom. -/
theorem n_v_leading_order :
    ∃ ε : ℝ, abs ε ≤ 0.006 ∧
      N_v = 120 * q_0_real^(90 : ℕ) * (1 + ε) := by
  -- Extract v/m_e = 40 · q_0^90 · (1 + ε₁) from the bridge.
  obtain ⟨ε₁, h_eps, h_ratio⟩ := v_over_m_e_bridge
  refine ⟨ε₁, h_eps, ?_⟩
  -- N_v := 3 · v/m_e = 3 · (40 · q_0^90 · (1+ε₁)) = 120 · q_0^90 · (1+ε₁)
  unfold N_v
  have hsplit : (3 * v_ew_real / m_e_real : ℝ)
      = 3 * (v_ew_real / m_e_real) := by ring
  rw [hsplit, h_ratio]
  ring

end QOU.Observations
