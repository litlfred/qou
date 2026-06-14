import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:weinberg-angle-categorical",
  title:
    "Weinberg angle $\\theta_W$ as Hecke-eigenvalue ratio on the EW Hoefsmit projectors",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.WeinbergAngleCategorical",
    validation: "not_checked",
  },
  tags: [
    "tier:E",
    "weinberg-angle",
    "electroweak-mixing",
    "hoefsmit-projector",
    "hecke-eigenvalue",
    "frobenius-trace",
    "categorical-physics",
    "open-problem",
    "tier-a",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** The statement is currently a structural proposal;\nthe simple-multiplicity reading numerically fails. To promote\nto a `proposition`, the authoring sequence is:\n\n1. Discharge [`conj:categorical-linking-operation`](#conj:categorical-linking-operation)\n   first — needed to formalise the $W^3$–$B$ interaction.\n2. Discharge [`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)\n   structural assignment (which slot is $W^3$ vs $B$).\n3. Compute $\\cos\\theta_W, \\sin\\theta_W$ from the corrected\n   Hoefsmit-projector traces (using non-uniform multiplicities\n   + linking operation).\n4. Verify against CODATA $\\sin^2\\theta_W$ at the appropriate\n   precision (CODATA-$\\theta_W$ has relative uncertainty\n   $\\sim 10^{-3}$, much weaker than CODATA-$G_F$).",
    },
  ],
});
