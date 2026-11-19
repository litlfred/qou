import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:mass-element-nf",
  lean: { ref: "qou:QOU.BraidKnot.HeckeMassNF" },
  title: "Normal form of the Hecke mass element",
  uses: ["conj:mass-endomorphism", "def:hecke-mass-element"],
  tags: [
    "mass",
    "hecke-algebra",
    "normal-form",
    "degree-filtration",
    "brane-tower",
    "photon-massless",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
