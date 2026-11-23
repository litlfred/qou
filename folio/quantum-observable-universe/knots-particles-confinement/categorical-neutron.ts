import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([Borromean quark](#conj:borromean-quark))" },
  ],
  label: "def:categorical-neutron",
  title: "Neutron (categorical)",
  tags: ["neutron", "hadron", "baryon", "color-tube", "knot", "categorical"],
  lean: { ref: "qou:QOU.Torsion.CategoricalNeutron",
    validation: "not_checked",
  },
  uses: ["def:categorical-proton"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
