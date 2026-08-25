import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-descended",
  lean: { ref: "qou:QOU.TopologicalMass.cat_descended_is_base_mass",
    validation: "not_checked",
  },
  title: "Descended term equals the base-level mass",
  tags: ["descent", "categorical-trace", "ascent-embedding", "mass"],
  uses: ["lem:topological-mass-cat-eigenspace"],
  proofs: ["prf:topological-mass-cat-descended"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/TopologicalMass/cat_descended_is_base_mass.lean` " +
        "carries `baseMass` and `baseTrace` as physical quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
