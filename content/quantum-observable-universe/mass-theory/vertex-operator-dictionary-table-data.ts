import { table } from "../../schema/builders";

export default table({
  label: "tbl:vertex-operator-dictionary-table-data",
  title: "Vertex operator algebra (VOA) to QOU dictionary",
  caption:
    "Per-concept translation between the standard vertex-operator-algebra " +
    "formalism (Frenkel et al.) and QOU structures (brane tower, " +
    "exceptional divisor, Reeb bundle, Hecke eigenvalues). Covers 13 " +
    "concepts including graded state space, conformal weight, formal " +
    "variable, vertex operator, modes, $L_0$/$L_{-1}$, OPE singularity, " +
    "central charge, and the KZ equation.",
  uses: ["rem:vertex-operator-dictionary"],
  tags: ["vertex-operator", "VOA", "dictionary", "summary-table"],
});
