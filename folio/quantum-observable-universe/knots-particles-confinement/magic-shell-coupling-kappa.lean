import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.MathlibExt.QIntegerCanonical


/-!
# QOU.BraidKnot.MagicShellCouplingKappa
  — the expression κ_closed and its proved properties

**The physical identification this file once carried has been withdrawn.**  What
remains is an expression and four facts about it, all of which are true
independently of any claim about nature.

  κ_closed(q, m_e) = −E₀ · log(1/h) / ([2]_q · [3]_q)

with E₀ = m_e/(q(q-1)), h = q − q⁻¹, and [n]_q the balanced q-bracket.

## Why the identification was withdrawn

`κ_closed` was proposed as the per-(n_pp − n_nn) excess slope of a magic-shell
coupling.  The value it was matched against, `≈ −1.0708 MeV`, turned out to be
**the Coulomb energy of ³He's pp pair**, attributed to the proton–neutron
interface asymmetry.

The original fit ran at two anchors and disagreed with itself — ³He gave
−1.0708 MeV, ³H gave **+0.2023 MeV**, opposite signs — and its own witness
recorded `hypothesis_supported: false`.  Those two nuclides differ in exactly one
respect besides the sign of the excess: ³He has a pp pair.  Restoring that
electrostatic energy makes both residuals negative under every radius model,
agreeing to 0.021 MeV — essentially the ⁴He residual of 0.022 MeV, measured where
the excess vanishes identically.  A term proportional to the excess must change
sign between anchors of excess +1 and −1; this one does not.  **The excess
coefficient is zero.**

  `computations/probe_kappa_provenance.py`
  `computations/probe_kappa_coulomb_reconciliation.py`
  `computations/probe_kappa_mirror_split_shell_test.py`

## What survives, and why it is worth keeping

Everything below concerns the *expression*, not the physics, so none of it is
touched by the withdrawal:

* `qBracket_eq_canonical` — the bracket is the canonical `qIntBal`, so this file
  introduces no competing q-integer convention.
* `qBracket_normaliser_eq_qFactorial` — `[2]_q·[3]_q = [3]_q!`, hence
  `q³/y_{(3)}(q)`, the inverse Markov weight of the trivial partition `(3) ⊢ 3`.
  This is the reusable observation: the denominator is a q-factorial, and the 3
  is the Borromean strand count of a single nucleon.
* `hParam_pos`, `E0_pos`, `kappaClosed_neg` — positivity of the Hecke deformation
  and energy scale, and the forced sign of the expression.

Nothing here is wired to production, and nothing reads the withdrawn value.

LaTeX: `\label{def:magic-shell-coupling-kappa}`

Ref: [leitner2026] def:magic-shell-coupling-kappa
Ref: [leitner2026] prop:compound-beta-shell-calibration (formerly parent)
-/

namespace QOU.BraidKnot

universe u

/-- The q-bracket `[n]_q = (q^n − q^{-n}) / (q − q⁻¹)` for `n : ℕ`,
    extended via `Real.rpow` for symbolic substrate evaluation. -/
noncomputable def qBracket (q : ℝ) (n : ℕ) : ℝ :=
  if n = 0 then 0
  else (q ^ n - q ^ (-(n : ℤ))) / (q - q⁻¹)

/-- **Bridge to the canonical balanced bracket** — and the `n = 0` guard is
redundant, which is the fact worth recording.  `qIntBal q 0 = (1 − 1)/(q − q⁻¹)`
is already `0`, so this site agrees with the canonical bracket *everywhere*,
including on the degenerate locus `q − q⁻¹ = 0` where both sides are `0` by
Lean's `x / 0 = 0`.  No hypothesis is needed. -/
theorem qBracket_eq_canonical (q : ℝ) (n : ℕ) :
    qBracket q n = QOU.QInteger.qIntBal q n := by
  unfold qBracket
  split_ifs with h
  · subst h
    simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal]
  · simp [QOU.QInteger.qIntBal, QOU.Mass.QHookDimensionBalanced.qIntBal, zpow_neg,
      zpow_natCast, inv_pow]

/-- **The normaliser is a q-factorial, not a two-channel fusion.**

`[2]_q · [3]_q = [3]_q!`.  The recovered producer described this denominator as
*"the quantum dimension of `V_2 ⊗ V_3`, the LR fusion of the two relevant
magic-shell channels for A = 3 anchors"*, which reads as a rule about **two**
channel indices.  It is a **one**-index object, and one already load-bearing
elsewhere in the corpus: `F_Bor = |tr_M(β_Bor)| · [3]_q! / q³`, and the q-Schur
Markov weight of the trivial partition, `y_{(3)}(q) = q³ / [3]_q!`.  So the
normaliser is `q³ / y_{(3)}(q)` — the inverse Markov weight of `(3) ⊢ 3`.

Why this matters rather than being a notational nicety: a
two-index rule admits several continuations off `A = 3` that all coincide there
(`(A_magic, A)`, a fixed `(2,3)`, `(A_magic, A_magic+1)`, …), and those spread by
32× at the 8 shell.  A q-factorial has one index, so the continuation question
narrows to which `n` the factorial is taken at — a strictly smaller search, and
one with a categorical handle via the Markov weight.

The hypothesis is the singular locus, inherited from `[1]_q = 1`. -/
theorem qBracket_normaliser_eq_qFactorial {q : ℝ} (h : q - q⁻¹ ≠ 0) :
    qBracket q 2 * qBracket q 3 = QOU.QInteger.qFactBal q 3 := by
  rw [qBracket_eq_canonical, qBracket_eq_canonical,
    QOU.QInteger.qFactBal_three h]

/-- The Hecke deformation parameter `h = q − q⁻¹`. -/
noncomputable def hParam (q : ℝ) : ℝ := q - q⁻¹

/-- The Hecke energy scale `E₀ = m_e / (q(q−1))`. -/
noncomputable def E0 (q m_e : ℝ) : ℝ := m_e / (q * (q - 1))

/-- The expression `κ_closed q m_e := −E₀(q, m_e) · log(1/h(q)) / ([2]_q · [3]_q)`.

    At the substrate parameter `q₀ ≈ 1.10998` it evaluates to `−1.0704239`.

    **No physical quantity is claimed for this value.**  It was proposed as a
    magic-shell coupling slope and matched to `−1.0707908`, a number since
    identified as the Coulomb energy of ³He's pp pair; see the module header.
    The name is retained because the corpus refers to it, not because the
    identification stands. -/
noncomputable def kappaClosed (q m_e : ℝ) : ℝ :=
  -E0 q m_e * Real.log (1 / hParam q) /
    (qBracket q 2 * qBracket q 3)

-- ────────────────────────────────────────────────────────────────
-- Structural lemmas about the closed-form components
-- (proven, no `sorry`, no class hypothesis)
-- ────────────────────────────────────────────────────────────────

/-- `[0]_q = 0` by definition. -/
theorem qBracket_zero (q : ℝ) : qBracket q 0 = 0 := by
  unfold qBracket
  simp

/-- The Hecke deformation `h(q) = q − q⁻¹` is positive for `q > 1`.

    Uses the same `inv_mul_cancel₀ + mul_lt_mul'` contradiction
    pattern as `QOU.MathlibExt.QPartitionCombinatorics.q_sub_q_inv_pos_at_q_gt_one`. -/
theorem hParam_pos {q : ℝ} (hq : 1 < q) : 0 < hParam q := by
  unfold hParam
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have hq_inv_pos : 0 < q⁻¹ := inv_pos.mpr hq_pos
  have hq_ne : q ≠ 0 := ne_of_gt hq_pos
  have h_inv_mul : q⁻¹ * q = 1 := inv_mul_cancel₀ hq_ne
  have hq_inv_lt_one : q⁻¹ < 1 := by
    by_contra h
    push_neg at h
    have : (1 : ℝ) * 1 < q⁻¹ * q := mul_lt_mul' h hq zero_le_one hq_inv_pos
    rw [one_mul, h_inv_mul] at this
    exact lt_irrefl 1 this
  linarith

/-- The Hecke energy scale `E₀(q, m_e) > 0` when `m_e > 0` and `q > 1`. -/
theorem E0_pos {q m_e : ℝ} (hq : 1 < q) (hm : 0 < m_e) :
    0 < E0 q m_e := by
  unfold E0
  have h1 : 0 < q := lt_trans zero_lt_one hq
  have h2 : 0 < q - 1 := by linarith
  have h3 : 0 < q * (q - 1) := mul_pos h1 h2
  exact div_pos hm h3

/-- **κ is negative** under the substrate conditions `q > 1, m_e > 0`,
    `0 < hParam q < 1`, and `0 < qBracket q 2 · qBracket q 3`.

    The sign follows structurally: `E₀ > 0` (Hecke energy positive),
    `log(1/h) > 0` since `0 < h < 1` for `q` slightly above `1`, and
    the q-brackets `[2]_q, [3]_q > 0` for `q > 1`.  The leading
    negative sign therefore forces `κ_closed < 0` — a property of the
    expression, asserted of nothing else.

    The `hhParam_lt_one` hypothesis holds for `q ∈ (1, φ)` where
    `φ = (1 + √5)/2` is the golden ratio (the unique positive root
    of `q − q⁻¹ = 1`).  Verified at `q₀ ≈ 1.10998`:
    `h(q₀) ≈ 0.209 < 1`. -/
theorem kappaClosed_neg {q m_e : ℝ}
    (hq : 1 < q) (hm : 0 < m_e)
    (hhParam_lt_one : hParam q < 1)
    (h_brackets_pos : 0 < qBracket q 2 * qBracket q 3) :
    kappaClosed q m_e < 0 := by
  unfold kappaClosed
  have hE0 : 0 < E0 q m_e := E0_pos hq hm
  have hh_pos : 0 < hParam q := hParam_pos hq
  have h_inv_h_gt_one : 1 < 1 / hParam q := by
    rw [lt_div_iff₀ hh_pos]
    linarith
  have h_log_pos : 0 < Real.log (1 / hParam q) :=
    Real.log_pos h_inv_h_gt_one
  have h_num_pos : 0 < E0 q m_e * Real.log (1 / hParam q) :=
    mul_pos hE0 h_log_pos
  have h_div_pos : 0 <
      E0 q m_e * Real.log (1 / hParam q) /
        (qBracket q 2 * qBracket q 3) :=
    div_pos h_num_pos h_brackets_pos
  have h_eq : -E0 q m_e * Real.log (1 / hParam q) /
        (qBracket q 2 * qBracket q 3) =
      -(E0 q m_e * Real.log (1 / hParam q) /
        (qBracket q 2 * qBracket q 3)) := by ring
  rw [h_eq]
  linarith

end QOU.BraidKnot
