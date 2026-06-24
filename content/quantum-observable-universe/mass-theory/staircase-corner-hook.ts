import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:staircase-corner-hook",
  proofs: ["prf:staircase-corner-hook"],
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
