import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-transient-localisation",
  lean: { ref: "qou:QOU.LiftingDescent.tm_transient_localisation",
    validation: "not_checked",
  },
  title: "Transient terms localise to exceptional divisors",
  tags: ["transient", "exceptional-divisor", "blow-up", "central-extension"],
  uses: [
    "def:brane-boundary",
    "lem:topological-mass-eigenspace-decomp",
  ],
  proofs: ["prf:topological-mass-transient-localisation"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/LiftingDescent/tm_transient_localisation.lean` " +
        "carries the transient mass-index components `transientMI*` as physical quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
