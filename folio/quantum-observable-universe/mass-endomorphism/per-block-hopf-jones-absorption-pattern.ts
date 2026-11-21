import { remark } from "../../schema/builders";

export default remark({
  label: "rem:per-block-hopf-jones-absorption-pattern",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): The global precision-ladder coefficient $c_3 = J_{\\text{Hopf}}(q{=}1) = -2$ emerges via the two-strand sub-braid argument ([categorical derivation of $c_3 = -2$](#prop:q-beta-c3-hopf-three-fold-markov)). The per-block decomposition shows that this Hopf-Jones value arises structurally per Wedderburn block." },
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.dimension_scaled_absorption_pattern",
    validation: "not_checked",
  },
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "Leading-order $\\varepsilon^1$ pattern in the per-Wedderburn-block character differences: $V_{(3)}, V_{(1,1,1)}$ absorb the **full** Hopf-Jones value $-2$; $V_{(2,1)}$ absorbs **half** ($-1$). Dimension-scaled Hopf absorption.",
  uses: ["rem:chi-per-irrep-cyclotomic-closed-forms"],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "per-wedderburn-block",
    "hopf-jones",
    "leading-order",
    "kashiwara-jones-alternation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/qbeta/qbeta_per_block_paper_closed_forms.py",
    witness: [
      "computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json",
    ],
    status: "experimental",
  },
});
