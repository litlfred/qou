import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "lem:nucleon-borromean-topology",
  lean: { ref: "qou:QOU.HadronicMass.nucleon_borromean_topology",
    validation: "not_checked",
  },
  title: "Nucleon Borromean topology and Hopf-link binding",
  tags: ["nucleon", "borromean", "hopf-link", "color-exchange"],
  uses: [],
  proofs: ["prf:nucleon-borromean-topology"],
});
