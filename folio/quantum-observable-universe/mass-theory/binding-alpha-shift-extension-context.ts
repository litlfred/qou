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
      body: "Computational witness: binding-rotation-phase-lead.witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/binding_rotation_phase_lead.py",
    witness: "computations/binding-rotation-phase-lead.witness.json",
    status: "verified",
  },
});
