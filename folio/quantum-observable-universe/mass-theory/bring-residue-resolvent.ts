import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-residue-resolvent",
  title: "Bring residue → canonical resolvent form 1/(1 − h_q · q^{α_shift})",
  cites: ["suslin1991", "thurston1978"],
  uses: [],
  defines: [],
  tags: ["normalization", "no-fitting", "uniqueness", "bring", "residue"],
  lean: { ref: "qou:QOU.BraidKnot.bring_residue_equation" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The scaffolded open math, the Lean structure, the class-instance\nclosure, and the downstream consequence" },
    {
      kind: "note",
      date: "2026-05-30",
      body: "The residue/resolvent step was shared across PRs #1444 (α_EM), #1445 (p-n averaging), and #1455 (meson m_K/m_π); the α_shift universal derivation chain audit doc is dated 2026-05-30.",
    },
  ],
});
