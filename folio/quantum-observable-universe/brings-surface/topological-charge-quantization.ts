import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-charge-quantization",
  title: "Quantization of topological charge",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.topological_charge_quantization",
    validation: "stub",
  },
  uses: [
    "def:unit-particle-state",
    "def:rigid-dualizing-complex",
  ],
  tags: [
    "topological-charge",
    "residue",
    "quantization",
    "algebraic-residue",
  ],
  cites: ["yekutieli2015"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Demoted `theorem` -> `conjecture` (bean `qou-8b0q`).** The Lean sibling is a single `def topological_charge_quantization` that NAMES the claim; it derives nothing, and the manifest's own `validation: \"stub\"` said so. A provable kind whose Lean only names its statement is the `proof-statement-integrity` gap AGENTS.md §3b-cond item 5 defines, so `conjecture` is the honest kind until the residue computation is formalised. Nothing about the mathematics changed. Blast radius measured before the relabel: **0 `uses[]` edges**, and **2** prose anchors — the auto-generated `definition-index.md` (regenerated here) and one live reference in `prop:phase-transition-boundary`'s author note, retargeted in the same commit. The bean recorded only the generated index, so that second anchor would have broken silently: `run-validate` does **not** check `](#anchor)` targets.",
    },
  ],
});
