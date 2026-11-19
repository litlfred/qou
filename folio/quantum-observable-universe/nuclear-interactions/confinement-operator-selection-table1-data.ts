import { table } from "../../schema/builders";
export default table({
  label: "tbl:confinement-operator-selection-table1-data",
  title: "Three-strand candidate confinement operators evaluated on net proton normal form and Markov trace",
  uses: ["prop:confinement-operator-selection"],
  tags: ["extracted-table"],
  computation: {
    engine: "python",
    script: "computations/confinement_operator_selection.py",
    witness: "computations/confinement-operator-selection.witness.json",
    status: "experimental",
  },
});
