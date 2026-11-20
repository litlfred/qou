import { remark } from "../../schema/builders";

export default remark({
  label: "rem:binding-alpha-shift-extension-context",
  title:
    "Setting, candidate table, Lean structure, and open math for the A≥3 binding extension",
  interprets: "prop:binding-alpha-shift-extension",
  tags: ["binding", "alpha-shift", "torus-knot", "reeb-phase", "open-math"],
  uses: ["prop:binding-alpha-shift-extension"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): hypothesis 1 is `class BindingPerRepReebPhase B m_e ρ_0` (fields `αShiftAt : ℕ → ℕ`, `factors`); hypothesis 2 is `class BindingForceCarrierKnot αShiftAt p k`; the consequence is `binding_unique_via_alpha_shift`, with `binding_subsingleton`.",
    },
  ],
});
