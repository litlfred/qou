import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  interprets: "def:knot-particle-generation",
  label: "rem:mass-from-generators",
  title: "Mass spectrum from $T_{m,n}$ generators and linking operations",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json", "computations/codata-masses.witness.json"],
    status: "verified",
  },
  tags: [
    "mass",
    "generator",
    "torus-knot",
    "hopf-link",
    "color-tube",
    "skein",
    "CODATA",
    "atomic-chart",
  ],
  uses: ["prop:torus-knot-generators"],
});
