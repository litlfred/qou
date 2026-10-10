import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-holonomy",
  lean: { ref: "qou:QOU.LiftingDescent.tm_descended_is_holonomy",
    validation: "not_checked",
  },
  title: "Descended term is the unknot-core holonomy",
  tags: ["holonomy", "ascent-embedding", "blow-up", "nonabelian-stokes"],
  uses: ["lem:topological-mass-eigenspace-decomp"],
  proofs: ["prf:topological-mass-holonomy"],
  cites: ["yekutieli2015"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/LiftingDescent/tm_descended_is_holonomy.lean` " +
        "carries `unknotHolonomy : ℝ` — a holonomy, real by construction. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
