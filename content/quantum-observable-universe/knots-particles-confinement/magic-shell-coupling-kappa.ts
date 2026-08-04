import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-shell-coupling-kappa",
  title:
    "Magic-shell coupling slope $\\kappa = -E_0 \\cdot \\log(1/h) / ([2]_q [3]_q)$ — categorical closed form",
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
    "acknowledged-cal4",
  ],
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-06-30",
      body:
        "Acknowledged CAL-4: the closed-form *shape* (E₀·log(1/h) magic-shell quantum, [2]_q·[3]_q normalization) was identified against the (2,2) doubly-magic anchor, so the single-magic 0.034% agreement is a near-match cross-check, not a zero-parameter prediction. The producer `computations/probe_kappa_categorical_h7a_closed.py` was removed and its witness `kappa-categorical-h7a-closed.witness.json` is now under `computations/_deprecated/`; a fresh witness is pending. Numerical values are recorded in the committed table `tbl:magic-shell-coupling-kappa-table-data`.",
    },
  ],
});
