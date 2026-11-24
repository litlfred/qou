import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-15", body: "The statement used to put tr_M(T_w) itself in the Habiro ring. That is false: tr_M(σ₁) = z = q³/(q²+1) and 1+q² vanishes at q = i. The Habiro expansion is of the cleared numerator (q²+1)^{n−1}·tr_M(T_w), which lies in ℤ[q^{±1}]. No number moves." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-24", body: "Bean qou-f13w: re-pointed the Habiro-ring definition citation to `habiro2004cyclotomic` (Publ. RIMS 40(4), 1127-1146, 2004) alongside `habiro2008` (Invent. Math. 171, 1-81, 2008) and anchored `jones1987` in prose; `habiro2004` remains registered as a legacy alias for Lean `-- Ref:` sites." },
  ],
  label: "prop:full-pole-structure-mass-trace",
  title:
    "Cyclotomic expansion of the cleared mass trace",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.BraidKnot.HabiroCompletion",
    validation: "not_checked",
  },
  cites: ["habiro2004cyclotomic", "habiro2008", "jones1987"],
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
