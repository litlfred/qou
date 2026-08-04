import { table } from "../../schema/builders";
export default table({
  label: "tbl:confinement-operator-selection-table1-data",
  title: "Table 1 from prop:confinement-operator-selection",
  uses: ["prop:confinement-operator-selection"],
  tags: ["extracted-table"],
  computation: {
    engine: "python",
    script: "computations/confinement_operator_selection.py",
    witness: "computations/confinement-operator-selection.witness.json",
    status: "experimental",
  },
});
