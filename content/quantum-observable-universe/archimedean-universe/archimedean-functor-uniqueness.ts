import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:archimedean-functor-uniqueness",
  title:
    "Uniqueness of the archimedean realization functor (Bloch-Suslin pentagon, conditional)",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/q_pinning_50_digit.py",
    witness: "folio-assistant/computations/q-pinning-50-digit.witness.json",
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
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
    "def:motivic-mass-measure",
    "def:motivic-substrate",
    "prop:quantum-dilogarithm-volume",
    "conj:dilogarithm-archimedean-limit",
    "conj:kashaev-volume-conjecture",
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
    ref: "qou:QOU.Descartes.archimedean_functor_uniqueness",
    validation: "not_checked",
  },
});
