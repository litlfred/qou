import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-alpha-k-h4",
  title:
    "Explicit $\\alpha_3$ at $H_4(R, q)$ via Wedderburn-orthogonal class-function $r_3$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.explicit_alpha_k_h4",
    validation: "not_checked",
  },
  uses: [
    "prop:wedderburn-bratteli-recursion",
    "rem:y-lambda-sign-pattern",
  ],
  tags: [
    "alpha-k",
    "h4",
    "wedderburn-orthogonal",
    "class-function-basis",
    "hoefsmit",
    "structural-derivation",
    "depth-3-stratum",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
