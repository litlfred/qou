import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  interprets: "prop:torus-knot-generators",
  label: "rem:building-block-knots",
  title:
    "Building block knots: classification, polynomials, and volumes",
  tags: [
    "knot",
    "torus-knot",
    "jones-polynomial",
    "hyperbolic-volume",
    "particle",
    "classification",
    "building-block",
    "amphichiral",
    "mirror",
    "appendix",
  ],
  uses: ["def:antineutrino-knot"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
