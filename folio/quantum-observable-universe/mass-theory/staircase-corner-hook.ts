import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Lean scope (disclosure, not a change of claim).** The `lean.ref` theorem proves (k − 1) + (k − 1) + 1 = 2k − 1 for k ≥ 1, where `hCorner k` is defined as that arithmetic expression. No partition, Young diagram or hook is formalised. The narrative proves the claim for ρ_k = (k, k − 1, …, 1), a convention the statement does not state. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B10; bean qou-pwo1).",
    },
  ],
  label: "lem:staircase-corner-hook",
  title: "Staircase corner hook $h_{\\mathrm{corner}}(\\rho_k) = 2k - 1$",
  lean: {
    ref: "qou:QOU.StaircaseCornerHook.staircase_corner_hook_eq_two_k_sub_one",
    validation: "not_checked",
  },
  uses: ["def:staircase-partition"],
  cites: ["stanley1999"],
  tags: [
    "staircase-partition",
    "hook-length",
    "corner-cell",
    "combinatorial-lemma",
    "ew-residual",
  ],
});
