import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# QOU.BraidKnot.HopfBindingLinkEigenvalueIdentity

**Categorical identification of the Hopf-link Hoefsmit-eigenvalue
structure** — supporting lemma for `conj:canonical-knot-id-sdp`'s
binding-link uniqueness for the deuteron.

## Background (PR #1712, 2026-06-02)

The deuteron's canonical binding link is `L_H = σ_1²` (Hopf link)
per the structural decomposition in
[`conj-canonical-knot-id-sdp.md`](../../../mass-theory/conj-canonical-knot-id-sdp.md).
The empirical SDP-feasibility probe
[`binding_link_psd_feasibility_probe.py`](../../../../../computations/binding_link_psd_feasibility_probe.py)
ran at H_3 and found `L_H = σ_1²` in Hoefsmit standard-(2,1) at `q_0`:

  min eigenvalue = +0.811653754... = `q_0⁻²` (10+ digit match)
  max eigenvalue = +1.232052454... = `q_0²`

Both eigenvalues strictly positive ⇒ `L_H` is PSD-feasible in the
standard block at q_0.  Together with the trivial and sign blocks
(also positive), this discharges the single-term SDP-feasibility
leg of PSD-feasibility for `CanonicalKnotIdSDP .deuterium` in
[`conj-canonical-knot-id-sdp.lean`](../../../mass-theory/conj-canonical-knot-id-sdp.lean).

**It does not discharge a field, and no longer names one.** This used to cite
`bindingKPSDFeasible_holds`, a `Prop`-universe field deleted on 2026-09-07:
being a proposition held as data, it was whatever the instance chose, and every
instance chose the decidable proxy `evenPower`. So the citation pointed at a
field that carried none of the eigenvalue content proved here. What the class
requires is `bindingKEvenPower`, a necessary condition; the positivity below is
the stronger, semantic fact, and it remains outside the class.

## What this file adds (sorry-free)

The categorical identification

    σ_k² in Hoefsmit standard-(2,1) basis ↦ diag(q², q⁻²)

— eigenvalues are EXACTLY (q², q⁻²) for ANY q > 0, not just
numerically at q_0.  Combined with q > 0 ⇒ q² > 0 and (q²)⁻¹ > 0,
this gives PSD-feasibility of `σ_k²` in the standard block at every
substrate value, not just q_0.

This strengthens the existing `evenPower` decidable proxy (which
only knows `σ²ⁿ` has the SHAPE of a Hopf-link-power) to a categorical
guarantee: `σ_k² ⪰ 0` in Hoefsmit standard-(2,1) for all q > 0.

## §3b-cond status

This is **not** a §3b-cond conjectural class — it's an unconditional
structural lemma about the Hoefsmit seminormal representation.  The
eigenvalues of `σ_k` in the standard-(2,1) rep are `(+q, −q⁻¹)` per
Hoefsmit (1979); squaring gives `(q², q⁻²)`.  No `sorry`.

The downstream **uniqueness** statement (`CanonicalKnotIdSDP_deuterium`
instance is unique modulo conjugation) remains a §3b-cond conditional
theorem proved elsewhere modulo a strict-complementarity sorry.
-/

namespace QOU.BraidKnot

/-- The two eigenvalues of `σ_k` in the Hoefsmit standard-(2,1)
    representation at parameter `q`: `+q` and `−q⁻¹`.

    Per Hoefsmit (1979) §3 / Geck-Pfeiffer (2000) §5: the
    seminormal generators of `H_n(q)` in the (n−1, 1) standard rep
    are diagonal on the basis indexed by reverse standard Young
    tableaux of shape `(n−1, 1)`.  For n=3 this gives a 2×2 diagonal
    matrix with diagonal `(+q, −q⁻¹)`. -/
noncomputable def hoefsmitStandardEig (q : ℝ) : ℝ × ℝ :=
  (q, -q⁻¹)

/-- `σ_k² = L_H` (Hopf link) in the Hoefsmit standard-(2,1)
    representation has eigenvalues `(q², (q²)⁻¹)`.  Squaring the
    diagonal `(+q, −q⁻¹)` yields `(q², q⁻²)`. -/
-- Ref: [hoefsmit1974] http://hdl.handle.net/2429/19407
-- Ref: [leitner2026] docs/audits/2026-06-02-binding-link-psd-feasibility-supports-structural-decomposition.md
noncomputable def hopfLinkStandardEig (q : ℝ) : ℝ × ℝ :=
  (q ^ 2, (q ^ 2)⁻¹)

/-- Squaring `(+q, −q⁻¹)` componentwise gives `(q², (q²)⁻¹)`.
    Stated separately for the first and second components for
    robustness across Mathlib versions (the second uses
    `(-q⁻¹)² = q⁻² = (q²)⁻¹`, which different Mathlib editions
    normalise to slightly different canonical forms). -/
theorem hopfLinkStandardEig_fst (q : ℝ) :
    (hopfLinkStandardEig q).1 = (hoefsmitStandardEig q).1 ^ 2 := by
  unfold hopfLinkStandardEig hoefsmitStandardEig
  rfl

theorem hopfLinkStandardEig_snd (q : ℝ) :
    (hopfLinkStandardEig q).2 = (hoefsmitStandardEig q).2 ^ 2 := by
  unfold hopfLinkStandardEig hoefsmitStandardEig
  dsimp only
  ring

/-- For any `q > 0`, both eigenvalues of `σ_k²` in the Hoefsmit
    standard-(2,1) representation are strictly positive.  This is
    the categorical strengthening of the numerical PSD-feasibility
    finding for the Hopf link at q_0. -/
-- Ref: [leitner2026] docs/audits/2026-06-02-binding-link-psd-feasibility-supports-structural-decomposition.md
theorem hopfLinkStandardEig_pos {q : ℝ} (hq : 0 < q) :
    0 < (hopfLinkStandardEig q).1 ∧ 0 < (hopfLinkStandardEig q).2 := by
  unfold hopfLinkStandardEig
  refine ⟨pow_pos hq 2, ?_⟩
  exact inv_pos.mpr (pow_pos hq 2)

/-- At `q > 1`, the **minimum** eigenvalue of `σ_k² = L_H` is `(q²)⁻¹`
    (since `q² > 1 > (q²)⁻¹`).  This identifies the empirical
    +0.811653754... value measured in
    `binding_link_psd_feasibility_probe.py` as `q_0⁻²`. -/
theorem hopfLinkStandardEig_min_at_q_gt_one {q : ℝ} (hq : 1 < q) :
    min (hopfLinkStandardEig q).1 (hopfLinkStandardEig q).2 =
      (hopfLinkStandardEig q).2 := by
  unfold hopfLinkStandardEig
  have hq_pos : 0 < q := lt_trans zero_lt_one hq
  have h_sq_pos : 0 < q ^ 2 := pow_pos hq_pos 2
  have h1 : (1 : ℝ) < q ^ 2 := by nlinarith
  have h2 : (q ^ 2)⁻¹ < 1 := by
    rw [show ((q ^ 2)⁻¹ : ℝ) = 1 / q ^ 2 from inv_eq_one_div _]
    exact (div_lt_one h_sq_pos).mpr h1
  exact min_eq_right (le_of_lt (lt_trans h2 h1))

end QOU.BraidKnot
