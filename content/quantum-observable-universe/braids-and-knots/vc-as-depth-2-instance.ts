import { remark } from "../../schema/builders";

export default remark({
  label: "rem:vc-as-depth-2-instance",
  title:
    "Volume Conjecture as the depth-2 instance of GS $\\leftrightarrow$ period correspondence",
  interprets: "conj:kashaev-volume-conjecture",
  uses: [
    "conj:gb-depth-period-correspondence",
    "conj:kashaev-volume-conjecture",
    "prop:q-dilogarithm-exists",
    "prop:categorical-laplace-unique",
    "rem:algebraic-core-survives",
    "rem:figure-8-archimedean-illustration",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "bloch2000",
    "zagier1986",
  ],
  tags: [
    "volume-conjecture",
    "depth-2",
    "bloch-wigner",
    "regulator",
    "graded-mikusinski",
    "interpretation",
  ],
});
