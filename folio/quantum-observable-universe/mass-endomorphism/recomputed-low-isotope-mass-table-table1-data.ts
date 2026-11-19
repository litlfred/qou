import { table } from "../../schema/builders";
export default table({ label: "tbl:recomputed-low-isotope-mass-table-table1-data", title: "Cross-check of canonical Markov trace $|\\mathrm{tr}_M(\\mathcal{B}_K)|$ against the $q$-Hecke seminormal partition sum ($A \\le 3$)", uses: ["rem:recomputed-low-isotope-mass-table"], tags: ["extracted-table"],
  computation: { engine: "mpmath", script: "computations/tr_m_q_hecke_seminormal.py", witness: "computations/tr-m-q-hecke-seminormal.witness.json", status: "verified" } });
