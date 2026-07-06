import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:archimedean-functor-uniqueness",
  title:
    "Uniqueness of the archimedean realization functor (Bloch-Suslin pentagon, conditional)",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "archimedean",
    "realization-functor",
    "uniqueness",
    "bloch-wigner",
    "pentagon-identity",
    "dilogarithm",
    "motivic",
    "kashaev",
    "alpha-em",
    "fine-structure-constant",
    "pre-archimedean",
    "conditional-class",
  ],
  uses: [
    "prop:quantum-dilogarithm-volume",
    "conj:dilogarithm-archimedean-limit",
    "conj:mass-endomorphism",
    "prop:cosimplicial-crossed-groupoid",
  ],
  cites: [
    "suslin1991",
    "bloch2000",
    "zagier1986",
    "kashaev1997",
    "murakami-murakami2001",
    "faddeev1994",
    "thurston1978",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.archimedean_functor_uniqueness",
    validation: "not_checked",
  },
});
