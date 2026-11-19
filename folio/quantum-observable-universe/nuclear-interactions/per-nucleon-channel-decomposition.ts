import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:per-nucleon-channel-decomposition",
  defines: ["per-nucleon-channel-decomposition"],
  title:
    "Per-nucleon channel decomposition via $S_3^A$ branching",
  tags: [
    "branching",
    "channel-decomposition",
    "garside",
    "hecke-algebra",
    "per-nucleon",
    "torus-knot",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.PerNucleonChannelDecomposition",
    validation: "not_checked",
  },
  uses: ["def:typed-crossing-operator"],
  computation: {
    engine: "numpy",
    script: "computations/tr_m_q_hecke_seminormal.py",
    witness: [
      "computations/tr-m-q-hecke-seminormal.witness.json",
      "computations/confinement-operator-selection.witness.json",
      "computations/sigma-f-electron-shell-chain.witness.json",
    ],
    status: "verified",
  },
});
