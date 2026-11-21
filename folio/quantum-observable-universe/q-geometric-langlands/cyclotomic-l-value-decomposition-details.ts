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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): [`cl_n_l_value_decomposition.py`](https://github.com/litlfred/qou/blob/main/computations/cl_n_l_value_decomposition.py), [witness](https://github.com/litlfred/qou/blob/main/computations/cl-n-l-value-decomposition.witness.json)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): - Bloch–Suslin (depth-2 theorem):\n  [Depth-2 identification of $G^{(2)}(\\mathcal{H}_q)$ with $K_3^{\\mathrm{ind}}(F) \\otimes \\mathbb{Q}$](#prop:depth-2-identification-bloch-suslin)\n- Borel partial discharge: [Borel's theorem partially discharges the depth correspondence's sharpness target — explicit dimensions](#prop:borel-partial-resolution)\n- K-theory $\\leftrightarrow$ depth filtration: [K-theory $\\leftrightarrow$ depth filtration Rosetta](#rem:k-theory-period-rosetta)\n- Period ledger: [Transcendental-accounting ledger: every period in the paper, indexed by Goncharov depth](#rem:transcendental-accounting)" },
  ],
});
