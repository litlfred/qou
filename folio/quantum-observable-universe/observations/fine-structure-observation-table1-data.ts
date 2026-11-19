import { table } from "../../schema/builders";
export default table({
  label: "tbl:fine-structure-observation-table1-data",
  title: "Table 1 from rem:fine-structure-observation",
  uses: ["rem:fine-structure-observation"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "Cell values computed via computations/alpha/alpha_em_form_comparison_probe.py and Lean declaration alpha_em_inv_derived; the Chern-Simons Gram constant kappa remains a sorry.",
    },
  ],
});
