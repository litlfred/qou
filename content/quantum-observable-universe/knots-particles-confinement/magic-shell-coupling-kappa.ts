import { conjecture } from "../../schema/builders";

/**
 * Magic-shell coupling slope κ — conjectured categorical closed form.
 *
 * Demoted from `proposition` to `conjecture` (2026-08-09). The closed-form
 * *shape* was read off the (2,2) doubly-magic anchor, which makes it an
 * anchor-identified form — a fit — and the three-calibration discipline
 * admits no CAL-4. A banner acknowledging the fit would have left a fitted
 * result carrying a provable block kind; demotion is the honest disposition.
 *
 * Nothing is unwired by this change: the producer
 * `probe_kappa_categorical_h7a_closed.py` was already removed and all three
 * κ witnesses sit under `computations/_deprecated/`, so no production compute
 * reads this value. The `KAPPA` in `pyhecke/constants.py` is a different
 * object (the binding scale `m_e`), not this slope.
 *
 * Lean: the superseded `HasMagicShellCouplingKappaClosedForm` carried the
 * conclusion as a *field* (`kappa_empirical`), so `⟨q, m_e, kappaClosed q m_e,
 * rfl⟩` discharged it and the theorem projecting it asserted nothing — the
 * §3b-cond rule-5 self-assuming projection. The replacement is a
 * content-bearing primary conjecture class over an `opaque` observed slope,
 * with no instance.
 */
export default conjecture({
  label: "conj:magic-shell-coupling-kappa",
  title:
    "Magic-shell coupling slope $\\kappa = -E_0 \\cdot \\log(1/h) / ([2]_q [3]_q)$ — conjectured categorical closed form",
  lean: {
    ref: "qou:QOU.BraidKnot.MagicShellCouplingKappa",
    validation: "not_checked",
  },
  uses: [
    "prop:compound-beta-shell-calibration",
  ],
  cites: [],
  tags: [
    "magic-shell",
    "coupling-slope",
    "categorical-closed-form",
    "kappa",
    "h7a",
    "q-bracket",
    "anchor-identified-form",
  ],
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      date: "2026-08-09",
      body:
        "**Demoted `proposition` → `conjecture`.** The $E_0 \\cdot \\log(1/h)$ magic-shell quantum and the $[2]_q [3]_q$ normalization were identified against the $(2,2)$ doubly-magic anchor, so the form is fitted, not derived. Under the three-calibration discipline there is no CAL-4 to acknowledge, which leaves demotion rather than a banner. The $0.034\\%$ agreement at the single-magic $(2,1)$ / $(1,2)$ anchors is retained as the supporting evidence, and the residual is now stated as an open quantity rather than absorbed as agreement.",
    },
    {
      kind: "caveat",
      date: "2026-06-30",
      body:
        "The producer `computations/probe_kappa_categorical_h7a_closed.py` was removed and its witness `kappa-categorical-h7a-closed.witness.json` is now under `computations/_deprecated/`. Numerical values are recorded in the committed table `tbl:magic-shell-coupling-kappa-table-data`. A fresh witness is only worth building against a derivation, not against the anchor-identified form.",
    },
  ],
});
