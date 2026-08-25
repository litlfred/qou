import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-transient",
  lean: { ref: "qou:QOU.TopologicalMass.cat_transient_localises_blowup",
    validation: "not_checked",
  },
  title: "Transient terms localise to blow-up centres (categorical)",
  tags: ["transient", "blow-up", "brane-boundary", "mass-defect"],
  uses: [
    "def:brane-boundary",
    "lem:topological-mass-cat-eigenspace",
  ],
  proofs: ["prf:topological-mass-cat-transient"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/TopologicalMass/cat_transient_localises_blowup.lean` " +
        "carries the Frobenius trace `trFrob : ℝ →+ ℝ` of the mass endomorphism. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
