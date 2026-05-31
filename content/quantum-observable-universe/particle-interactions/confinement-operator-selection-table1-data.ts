import { table } from "../../schema/builders";
export default table({
  label: "tbl:confinement-operator-selection-table1-data",
  title: "Table 1 from prop:confinement-operator-selection",
  uses: ["prop:confinement-operator-selection"],
  tags: ["extracted-table"],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/confinement_operator_selection.py",
    witness: "folio-assistant/computations/confinement-operator-selection.witness.json",
    status: "experimental",
  },
});
