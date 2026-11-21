import { remark } from "../../schema/builders";

export default remark({
  label: "rem:figure-8-archimedean-illustration",
  title:
    "Figure-8 knot $4_1$ as illustration of the algebraic / archimedean dichotomy",
  interprets: "prop:archimedean-functor-uniqueness",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "figure-8-knot",
    "amphichiral",
    "hyperbolic-volume",
    "archimedean",
    "motivic",
    "hecke-normal-form",
    "bloch-wigner",
    "clausen",
    "illustration",
  ],
  uses: ["prop:archimedean-functor-uniqueness"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Cross-reference: $\\alpha_{EM}$.** The same dichotomy underlies\nthe additive Bring zero-mode candidate\n[additive Bring zero-mode form of $1/\\alpha_{EM}$](#prop:em-coupling-bring-zero-mode):\nthe $\\pi$ in $4_1$'s archimedean image\n$2\\,\\mathrm{Cl}_2(\\pi/3)$ and the $\\pi$ in $1/\\alpha_{EM}$'s\ncorrection $2/(3\\pi) = 2g/(4\\pi(g-1))$ at $g=4$ share a single\nprovenance — the unique archimedean shadow of pentagon-coherent\nsubstrate data on Bring's surface, factored through the\nBloch-Wigner dilogarithm." },
  ],
  cites: [
    "thurston1978",
    "suslin1991",
    "kashaev1997",
    "murakami-murakami2001",
  ],
});
