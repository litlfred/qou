import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "note",
      body: "Verified to 50 decimal places in computations/cl_n_l_value_decomposition.py (witness: computations/cl-n-l-value-decomposition.witness.json).",
    },
  ],
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
  computation: {
    engine: "mpmath",
    script: "computations/cl_n_l_value_decomposition.py",
    witness: "computations/cl-n-l-value-decomposition.witness.json",
    status: "verified",
  },
});
