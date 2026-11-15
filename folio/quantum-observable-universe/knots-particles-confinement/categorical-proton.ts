import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:categorical-proton",
  title: "Proton (categorical)",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: { ref: "qou:QOU.Torsion.CategoricalProton",
    validation: "not_checked",
  },
  uses: ["def:down-quark"],
  cites: ["leitner2026"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
