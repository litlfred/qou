import { table } from "../../schema/builders";

export default table({
  label: "tbl:bw-mass-decomposition-dictionary-table-data",
  title: "BW empirical terms as Schur-Weyl strata",
  caption:
    "Seven-term dictionary: each empirical Bethe-Weizs\\\"acker term (volume, " +
    "surface, Coulomb, asymmetry, pairing, Wigner, shell) mapped to its " +
    "Schur-Weyl partition stratum $\\lambda$ and algebraic origin in the " +
    "categorical $q$-hook product.",
  uses: ["rem:bw-mass-decomposition-dictionary"],
  tags: ["bethe-weizsacker", "schur-weyl", "dictionary", "summary-table"],
});
