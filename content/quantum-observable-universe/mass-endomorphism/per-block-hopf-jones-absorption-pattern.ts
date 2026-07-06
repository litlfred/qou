import { remark } from "../../schema/builders";

export default remark({
  label: "rem:per-block-hopf-jones-absorption-pattern",
  lean: {
    ref: "qou:QOU.BraidKnot.per_block_hopf_jones_absorption",
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
