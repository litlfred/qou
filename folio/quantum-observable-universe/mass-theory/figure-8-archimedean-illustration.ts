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
  cites: [
    "thurston1978",
    "suslin1991",
    "kashaev1997",
    "murakami-murakami2001",
  ],
});
