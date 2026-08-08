import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-cat-eigenspace",
  lean: { ref: "qou:QOU.TopologicalMass.cat_eigenspace_decomposition",
    validation: "not_checked",
  },
  title: "Eigenspace decomposition of the categorical mass integrand",
  tags: ["descent-involution", "frobenius-norm", "categorical-trace", "mass"],
  uses: [
    "def:mass-identity",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:topological-mass-cat-eigenspace"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean` " +
        "carries a norm `nrm : ℝ → ℝ` and the mass `m_rho`; a norm is archimedean by definition. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
