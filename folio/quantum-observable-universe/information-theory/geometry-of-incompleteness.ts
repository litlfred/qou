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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (the physical-intractability theorem `QOU.Information.qou_physical_intractability_unconditional`)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nThe end of the chain is `QOU.Information.geometry_of_incompleteness`: from a Gödel datum with $\\neg\\,\\text{formallyProvable}$ and a boundary datum whose bandwidth-$B$ extractor reads the full $3^{3n}$ tree, both are `Inaccessible`, and `horizon_nonempty` derives $\\exists\\, d,\\ \\text{Inaccessible}\\ d$. The physical leg is discharged by `qou_physical_intractability_unconditional`; the exponential-domination fact it rests on is proved (`superPoly_two_pow`)." },
    {
      kind: "note",
      body:
        "Scope: an **existence** statement about substrate structure (a nonempty jet horizon), NOT a claim of $\\mathrm{P} \\neq \\mathrm{NP}$ (which needs the separate, open counting$\\to$decision transfer). The physical-intractability witness is *derived* (`qou_physical_intractability_unconditional`, from the $3^{3n}$ resolution tree + the Bekenstein bandwidth bound); the formal witness is Gödel incompleteness, taken as the hypothesis $\\neg\\,\\text{formallyProvable}$.",
    },
  ],
});
