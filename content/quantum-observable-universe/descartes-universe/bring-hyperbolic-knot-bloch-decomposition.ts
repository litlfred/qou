import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-hyperbolic-knot-bloch-decomposition",
  title:
    "Bloch-group decomposition of $2/(3\\pi)$ from $S_5$-equivariantly embeddable hyperbolic knots in Bring's surface",
  uses: [
    "prop:archimedean-functor-uniqueness",
    "prop:em-coupling-bring-zero-mode",
    "rem:figure-8-archimedean-illustration",
    "def:archimedean-realization-functor",
    "conj:kashaev-volume-conjecture",
  ],
  cites: [
    "suslin1991",
    "bloch2000",
    "thurston1978",
    "borel1974",
    "zagier1986",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  tags: [
    "bloch-group",
    "borel-regulator",
    "k-theory",
    "brings-surface",
    "hyperbolic-knot",
    "bloch-wigner",
    "alpha-em",
    "fine-structure-constant",
    "cyclotomic-field",
    "structural-sub-conjecture",
  ],
  lean: {
    ref: "qou:QOU.Descartes.bring_hyperbolic_decomposition",
    validation: "not_checked",
  },
});
