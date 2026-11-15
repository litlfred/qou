import { table } from "../../schema/builders";
export default table({ label: "tbl:recomputed-low-isotope-mass-table-table1-data", title: "Table 1 from rem:recomputed-low-isotope-mass-table", uses: ["rem:recomputed-low-isotope-mass-table"], tags: ["extracted-table"],
  computation: { engine: "mpmath", script: "computations/tr_m_q_hecke_seminormal.py", witness: "computations/tr-m-q-hecke-seminormal.witness.json", status: "verified" } });
