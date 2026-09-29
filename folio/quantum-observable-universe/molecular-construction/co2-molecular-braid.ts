import { definition } from "../../schema/builders";

/**
 * CO₂ molecular braid: linear triatomic with two double bonds.
 */
export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:co2-molecular-braid",
  title: "Carbon dioxide $CO_2$ as a molecular braid",
  lean: { ref: "qou:QOU.Molecular.CO2Braid",
    validation: "not_checked",
  },
  uses: ["def:co-molecular-braid"],
  tags: [
    "carbon-dioxide",
    "CO2",
    "double-bond",
    "linear",
    "triatomic",
    "molecular-braid",
  ],
  computation: {
    engine: "python",
    script: "computations/molecular_experimental_refs.py",
    witness: [
      "computations/molecular-experimental-refs.witness.json"
    ],
    status: "experimental",
  },
});
