import { remark } from "../../schema/builders";

export default remark({
  label: "rem:planck-length-share-vs-total",
  title:
    "$\\ell_P$ carries two meanings: the Reeb share $\\hbar_q$ and the normalised total $\\ell_P(q) \\equiv 1$",
  interprets: "prop:reeb-coefficient-is-hbar-q",
  uses: ["prop:reeb-coefficient-is-hbar-q"],
  tags: ["planck-length", "notation-collision", "hbar-q", "reeb-flow"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-09",
      body:
        "Resolves the FIRST of the two defects recorded in bean qou-adwi — the apparent " +
        "factor-t_P (about 10.1) contradiction between planck-info-unit.md ('ell_P ~ hbar_q', " +
        "local, proportionality) and discrete-planck-step.md ('ell_P(q) = hbar_q t_P = 1', " +
        "global, normalised). Read as share versus total the two are consistent, so the defect " +
        "is one symbol wearing two meanings and not a numerical disagreement. " +
        "OPEN — the SECOND defect in qou-adwi is untouched by this block: " +
        "lean/QOU/InformationTheory.lean:32-34 hardens the prose proportionality into " +
        "`localPlanckLength := quantumPlanckConstant`, a definitional equality where the " +
        "narrative asserts only a scaling. Repairing that is a Lean edit, not an exposition " +
        "edit, and no bean state was changed here — the bean may be owned by another session.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "No lean.ref by design. The two declarations that would back this block, " +
        "GramSignature.reeb_coefficient_eq_hbar_q and GramSignature.dirac_coefficients_convex, " +
        "are already owned by prop:reeb-coefficient-is-hbar-q and " +
        "rem:connes-distance-not-reeb-step-count respectively, and this remark adds no formal " +
        "content of its own — it disambiguates a symbol.",
    },
    {
      kind: "caveat",
      date: "2026-08-09",
      body:
        "uses[] deliberately omits rem:discrete-planck-step and sec:planck-info-unit, the two " +
        "sites whose symbol collision this block resolves. Both are narrative cross-references " +
        "in the .md, not prerequisites: the block restates each of the two formulas in full, so " +
        "a reader can follow it without having read either site. Listing them would also put a " +
        "forward edge in the graph — rem:discrete-planck-step sits in sec:golden-julia-dynamics, " +
        "downstream of this block's home in sec:info-time-computation, which decision 7 fixes. " +
        "Re-homing the block beside rem:discrete-planck-step instead is the alternative and is " +
        "an owner call.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): After one Planck step, [the discrete Planck step](#rem:discrete-planck-step)\nrecords the displacement as" },
  ],
});
