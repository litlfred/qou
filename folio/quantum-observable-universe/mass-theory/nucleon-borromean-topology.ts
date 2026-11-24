import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation guard (`qou-x60n`, `qou-z9ws`): imports `QOU.HadronicMass`, where `skein_pnd_identity_false` is guarded by `2026-08-30-skein-mass-relation-is-false.lean`.",
      see: "docs/audits/2026-08-30-skein-mass-relation-is-false.lean",
    },
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
