import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:archimedean-functor-uniqueness",
  title:
    "Uniqueness of the archimedean realization functor (Bloch-Suslin pentagon)",
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
  ],
  uses: [
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
    "def:motivic-mass-measure",
    "def:motivic-substrate",
    "prop:quantum-dilogarithm-volume",
    "conj:dilogarithm-archimedean-limit",
    "conj:mass-endomorphism",
    "conj:kashaev-volume-conjecture",
    "prop:cosimplicial-crossed-groupoid",
  ],
  cites: [
    "suslin1991",
    "bloch2000",
    "zagier1986",
    "kashaev1997",
    "murakami-murakami2001",
    "faddeev1994",
  ],
  lean: {
    ref: "qou:QOU.Descartes.archimedean_functor_uniqueness",
    validation: "not_checked",
  },
});
