import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-15", body: "The statement used to put tr_M(T_w) itself in the Habiro ring. That is false: tr_M(σ₁) = z = q³/(q²+1) and 1+q² vanishes at q = i. The Habiro expansion is of the cleared numerator (q²+1)^{n−1}·tr_M(T_w), which lies in ℤ[q^{±1}]. No number moves." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:full-pole-structure-mass-trace",
  title:
    "Cyclotomic expansion of the cleared mass trace",
  lean: {
    ref: "qou:QOU.BraidKnot.HabiroCompletion",
    validation: "not_checked",
  },
  cites: ["habiro2004", "jones1987"],
  tags: [
    "habiro-ring",
    "cyclotomic-completion",
    "markov-trace",
    "root-of-unity",
    "mass",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/markov/markov_substrate_realizer.py",
    witness: [
      "computations/habiro/habiro-interpolate-cross-validation.witness.json",
      "computations/markov/markov-substrate-realization.witness.json",
      "computations/d-from-scratch.witness.json",
      "computations/proton-mass-codata-50dps.witness.json",
    ],
    status: "experimental",
  },
});
