import { table } from "../../schema/builders";
export default table({ label: "tbl:fine-structure-observation-table1-data", title: "Table 1 from rem:fine-structure-observation", uses: ["rem:fine-structure-observation"], tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Every cell is computed from [`alpha_em_form_comparison_probe.py`](../../../computations/alpha/alpha_em_form_comparison_probe.py) and `alpha_em_inv_derived`, satisfying … Chern-Simons correction is a conjecture whose Gram constant $\\kappa$ is carried as an unproved Lean `sorry`; exact" },
  ],
});
