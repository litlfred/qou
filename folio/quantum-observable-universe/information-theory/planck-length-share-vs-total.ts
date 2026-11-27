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
        "Resolves both parts of bean qou-adwi: (1) separates the per-step Reeb share " +
        "`\\hbar_q = 1 - q^{-1}` (`sec:planck-info-unit`) from the unit-normalised full Reeb " +
        "circuit `\\ell_P(q) = \\hbar_q t_P = 1` (`rem:discrete-planck-step`), retiring the " +
        "colliding auxiliary glyphs `\\ell_P^{\\mathrm{step}}` and `\\ell_q`; and (2) refactors " +
        "`lean/QOU/InformationTheory.lean` so `reebStepShare := quantumPlanckConstant` and " +
        "`normalisedReebCircuit := 1` (`reebStepShare_mul_planckCircuitTime`) name the share and " +
        "circuit explicitly rather than equating `localPlanckLength` to `quantumPlanckConstant`.",
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
