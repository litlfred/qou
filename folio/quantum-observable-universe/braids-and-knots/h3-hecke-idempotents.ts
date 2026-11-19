import { remark } from "../../schema/builders";

export default remark({
  label: "rem:h3-hecke-idempotents",
  interprets: "rem:ck-extraction-from-algebraic-rules",
  title:
    "$H_3(q)$ Hecke idempotents — explicit $q$-dimensions and per-block $\\sigma_i$ eigenvalues for the three Wedderburn blocks $V_{(3)}, V_{(2,1)}, V_{(1^3)}$",
  uses: ["rem:ck-extraction-from-algebraic-rules"],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "q-young-symmetrizer",
    "hecke-idempotent",
    "h3-wedderburn",
    "q-dimension",
    "eigenvalue-table",
    "poincare-normalizer",
  ],
});
