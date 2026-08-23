import { theorem } from "../../schema/builders";

// Block-kind rename 2026-05-02: was `lemma`, demoted to
// `conjecture` per the cones-doc audit finding
// (docs/audits/conjecture-cones.md "Methodology" footnote).
// The Lean file's `sorry` was always the conjectural content;
// the `lem:` label was block-kind drift. The conjecture's
// downstream cone is then handled correctly under AGENTS.md §3b
// propagation.
export default theorem({
  label: "thm:motivic-perpetual-obstruction",
  title:
    "Motivic perpetual obstruction: $\\chi^{\\mathrm{mot}}_A$ is non-trivial at almost every finite place when $\\chi(A) \\neq 0$",
  tags: [
    "tier:S",
    "motivic-galois",
    "perpetuity",
    "yekutieli",
    "kummer-tower",
    "frobenius",
  ],
  uses: [
    "def:motivic-galois-character",
    "rem:kummer-tower",
  ],
  cites: ["yekutieli2010"],
  lean: {
    ref: "qou:QOU.LiftingDescent.motivic_perpetual_obstruction_frobenius",
    validation: "not_checked",
  },
});
