import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:skein-mass-from-linking",
  lean: { ref: "qou:QOU.BraidsKnots.skein_mass_from_linking",
    validation: "not_checked",
  },
  title: "Mass functional on a Skein resolution: linking-energy plus constituent volume",
  tags: ["skein-resolution", "binding-energy", "torus-knot", "hopf-link"],
  uses: ["def:hadron"],
  proofs: ["prf:skein-mass-from-linking"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/BraidsKnots/skein_mass_from_linking.lean` " +
        "carries `Vol_K : ℕ → ℝ` (hyperbolic volume, transcendental) alongside `mass_Hopf` and `hbar_q`. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
