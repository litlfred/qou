import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-hyperbolic-knot-bloch-decomposition",
  title:
    "Bloch-group decomposition of $2/(3\\pi)$ from $S_5$-equivariantly embeddable hyperbolic knots in Bring's surface",
  uses: [
    "prop:em-coupling-bring-zero-mode",
    "rem:figure-8-archimedean-illustration",
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
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "tier:E",
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
    ref: "qou:QOU.Archimedean.bring_hyperbolic_decomposition",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      body:
        "**Open structural sub-conjecture.** This is the K-theoretic identification required to inhabit the typeclass [`QOU.Archimedean.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean) from [prop:em-coupling-bring-zero-mode](#prop:em-coupling-bring-zero-mode). The statement is a concrete, falsifiable prediction once the '$S_5$-equivariantly embeddable' condition is made precise. The proof attempt below establishes (i) the relevant field structure unconditionally, (ii) the figure-8 contribution as a worked classical sub-piece, and (iii) the irreducible open problem.",
    },
  ],
});
