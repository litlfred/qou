import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.MathlibExt.QIntegerCanonical


/-!
# QOU.BraidKnot.MagicShellCouplingKappa
  — Magic-shell coupling slope κ closed-form

The per-(n_pp − n_nn) excess slope of the magic-shell coupling
correction is **conjectured** to admit the closed categorical form

  κ = −E₀ · log(1/h) / ([2]_q · [3]_q)

where E₀ = m_e/(q(q-1)), h = q − q⁻¹, and [n]_q is the q-bracket.

Both factors of the right-hand side — the `E₀·log(1/h)` magic-shell quantum and
the `[2]_q·[3]_q` normalisation — were identified against the (2,2) doubly-magic
anchor, so the shape is an anchor-identified form rather than a derived one.
The three-calibration discipline admits no CAL-4 slot to declare such a form
into, which is why the content block carries the kind `conjecture`.

The file proves the properties of the *expression* outright: the bracket's tie
to the canonical `qIntBal` (`qBracket_eq_canonical`), positivity of `E₀` and `h`,
and the forced sign (`kappaClosed_neg`).  What is conjectural is only that this
expression is the observed slope — `MagicShellSlopeIsCategorical`, stated
against an `opaque` measured datum and left without an instance.

At q₀ the closed form agrees with the observed slope to a relative residual of
≈ 3.4·10⁻⁴ at the single-magic anchors, which were not used to fix the shape.
That residual is carried explicitly in the conjecture's `tol` parameter rather
than rounded away.  No production compute reads this value: the verifier
`computations/probe_kappa_categorical_h7a_closed.py` is not in the tree and its
witnesses are under `computations/_deprecated/`.

LaTeX: `\label{conj:magic-shell-coupling-kappa}`

Ref: [manuscript] conj:magic-shell-coupling-kappa
Ref: [manuscript] prop:compound-beta-shell-calibration (parent)
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

/-- The Hecke deformation parameter `h = q − q⁻¹`. -/
noncomputable def hParam (q : ℝ) : ℝ := q - q⁻¹

/-- The Hecke energy scale `E₀ = m_e / (q(q−1))`. -/
noncomputable def E0 (q m_e : ℝ) : ℝ := m_e / (q * (q - 1))

/-- The categorical magic-shell coupling slope.

    `κ_closed q m_e := −E₀(q, m_e) · log(1/h(q)) / ([2]_q · [3]_q)`

    At the substrate parameter `q₀ ≈ 1.10998`, evaluates to
    `−1.0704239 MeV` — agrees with empirical PR #656 v6 fit
    `κ_emp ≈ −1.0707908 MeV` within 0.035 %. -/
noncomputable def kappaClosed (q m_e : ℝ) : ℝ :=
  -E0 q m_e * Real.log (1 / hParam q) /
    (qBracket q 2 * qBracket q 3)

/-- The **observed** per-excess magic-shell coupling slope, as a function of the
substrate parameter and the electron mass.

`opaque` by design.  This is a measured datum, so nothing in this file may
compute it and no instance may choose it.  That is the whole repair over the
superseded `HasMagicShellCouplingKappaClosedForm`, which carried the observed
slope as a *field* `kappa_empirical` alongside the equation asserting the closed
form equalled it — so `⟨q, m_e, kappaClosed q m_e, rfl⟩` discharged the class
outright.  The class asserted nothing, and the theorem projecting it asserted
nothing either: the §3b-cond rule-5 self-assuming projection, where the carrier
holds the conclusion instead of the hypotheses. -/
opaque observedMagicShellSlope : ℝ → ℝ → ℝ

/-- **Primary conjecture (`conj:magic-shell-coupling-kappa`) — the magic-shell
slope has a categorical closed form.**

An instance asserts that `kappaClosed` reproduces the observed slope to within a
relative `tol`, at every admissible substrate point rather than at one.

*Not* proved, and no instance is supplied: the shape of `kappaClosed` was read
off the (2,2) doubly-magic anchor, so it is an anchor-identified form.  The
three-calibration discipline has no CAL-4 slot to declare it into, which is why
the content block is a `conjecture` rather than a `proposition` carrying a
fitted-result banner.

The `tol` parameter is what keeps the statement honest in both directions.  At
`q₀` the measured relative residual is `≈ 3.4·10⁻⁴`, so this class is expected
to hold for `tol ≥ 3.4·10⁻⁴` and is **known to fail** below it — an exact-equality
formulation would have been contradicted by the very data offered in its support.
A derivation discharging this conjecture must therefore also account for the
residual, or replace the form with one that has none.

Content-bearing per §3b-tax: the field is parameter-quantified in the shape of
the claim, the right-hand side is opaque, and no instance exists. -/
class MagicShellSlopeIsCategorical (tol : ℝ) : Prop where
  /-- The closed form agrees with the observed slope to relative `tol`. -/
  leading_order : ∀ q m_e : ℝ, 1 < q → 0 < m_e →
    |kappaClosed q m_e - observedMagicShellSlope q m_e| ≤
      tol * |observedMagicShellSlope q m_e|

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
    negative sign therefore forces `κ < 0`, matching the empirical
    PR #656 v6 fit `κ_emp ≈ −1.07 MeV`.

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

/-- **The observed slope inherits the forced sign** — a genuine consequence of
the conjecture, not a projection of it.

`MagicShellSlopeIsCategorical` supplies only a *bound* on the discrepancy; the
negativity of the observed slope is derived here from that bound together with
`kappaClosed_neg`, which is proved outright.  This is what §3b-cond rule 5 asks
of a conditional result: the class carries hypotheses and the theorem does work
with them, rather than storing the conclusion and reading it back.

The hypothesis `tol ≤ 1` is doing real work and is not boilerplate — a bound
allowed to exceed the magnitude of the observed slope permits the two to differ
in sign, and the conclusion genuinely fails.  At the physically relevant
`tol ≈ 3.4·10⁻⁴` it is satisfied with enormous margin. -/
theorem observedMagicShellSlope_neg {q m_e tol : ℝ}
    [c : MagicShellSlopeIsCategorical tol] (htol : tol ≤ 1)
    (hq : 1 < q) (hm : 0 < m_e)
    (hhParam_lt_one : hParam q < 1)
    (h_brackets_pos : 0 < qBracket q 2 * qBracket q 3) :
    observedMagicShellSlope q m_e < 0 := by
  have hc : kappaClosed q m_e < 0 :=
    kappaClosed_neg hq hm hhParam_lt_one h_brackets_pos
  have hbound := c.leading_order q m_e hq hm
  by_contra hcon
  push_neg at hcon
  rw [abs_of_nonneg hcon] at hbound
  have hdiff : |kappaClosed q m_e - observedMagicShellSlope q m_e|
      = observedMagicShellSlope q m_e - kappaClosed q m_e := by
    rw [abs_sub_comm]
    exact abs_of_nonneg (by linarith)
  rw [hdiff] at hbound
  nlinarith

end QOU.BraidKnot
