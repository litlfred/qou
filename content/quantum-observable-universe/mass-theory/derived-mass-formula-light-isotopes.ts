import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:derived-mass-formula-light-isotopes",
  title: "Derived-only mass formula reproduces light atomic masses to sub-percent",
  lean: {
    ref: "qou:QOU.WedderburnMass.derivedLightIsotopeFormula",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-s-classification",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `mass-theory/derived-mass-formula-light-isotopes.lean` " +
        "carries the physical masses `m_e`, `m_p`, `m_n` and the coupling `α` as measured (CODATA-tier) quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
