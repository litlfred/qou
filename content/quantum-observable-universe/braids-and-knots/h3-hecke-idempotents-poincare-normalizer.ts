import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:ck-extraction-from-algebraic-rules",
  label: "rem:h3-hecke-idempotents-poincare-normalizer",
  title:
    "Explicit $H_3(q)$ projector normalization via the $S_3$ Poincaré polynomial $P(q) = q^{\\ell(w_0)}\\,[3]_q!$",
  uses: ["rem:ck-extraction-from-algebraic-rules"],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "hecke-idempotent",
    "poincare-normalizer",
    "q-factorial",
    "projector",
  ],
});
