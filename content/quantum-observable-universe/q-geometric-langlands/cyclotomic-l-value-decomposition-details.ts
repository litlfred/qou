import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cyclotomic-l-value-decomposition-details",
  title:
    "Cyclotomic $L$-value decomposition — verification, $N=5$ instance, and analytic-number-theory bridge",
  interprets: "prop:cyclotomic-l-value-decomposition",
  uses: [
    "prop:cyclotomic-l-value-decomposition",
    "prop:jonquiere-cyclotomic-tate-rationality",
    "prop:cyclotomic-dimension-synthesis-all-depths",
  ],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "dirichlet-l-value",
    "catalan-beta",
    "cyclotomic",
    "analytic-number-theory-bridge",
    "numerical-verification",
  ],
});
