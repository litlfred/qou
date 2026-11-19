import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-parameter",
  cites: ["lusztig1993"],
  title: "Aether parameter",
  tags: ["substrate", "deformation", "fibre-coordinate"],
  lean: { ref: "qou:QOU.SubstrateParameter",
    validation: "leanok",
  },
  uses: ["def:categorical-reeb"],
  examples: ["ex:substrate-parameter-su2"],
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean sibling is the AGENTS.md §7c exemplar: the categorical indeterminate lives in `R_q` (generic base ring), and the **archimedean** predicates (`0 < q`, `q ≥ 1`, \"not a root of unity\") live on a separate `ArchimedeanSubstrateField M` with `field : M → ℝ`, reached through the specialisation `ι : R_q → ℝ, q ↦ q₀`. The `Mathlib.Data.Real.Basic` import and `ℝ` usage are confined to that archimedean field on the far side of the substrate→archimedean wall — not a gratuitous specialisation of the categorical content.",
    },
  ],
});
