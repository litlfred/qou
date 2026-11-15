import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:geometry-of-incompleteness",
  title:
    "The geometry of incompleteness: a Turing-complete QOU has a nonempty horizon",
  lean: {
    ref: "qou:QOU.Information.geometry_of_incompleteness",
    validation: "not_checked",
  },
  tags: [
    "incompleteness",
    "physical-intractability",
    "jet-horizon",
    "godel",
    "turing-complete",
    "degree-zero",
    "information-theory",
  ],
  uses: ["def:computational-boundary", "prop:p-bandwidth-bound"],
  authorNotes: [
    {
      kind: "note",
      body:
        "Scope: an **existence** statement about substrate structure (a nonempty jet horizon), NOT a claim of $\\mathrm{P} \\neq \\mathrm{NP}$ (which needs the separate, open counting$\\to$decision transfer). The physical-intractability witness is *derived* (`qou_physical_intractability_unconditional`, from the $3^{3n}$ resolution tree + the Bekenstein bandwidth bound); the formal witness is Gödel incompleteness, taken as the hypothesis $\\neg\\,\\text{formallyProvable}$.",
    },
  ],
});
