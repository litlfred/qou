import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-residue-resolvent",
  title: "Bring residue → canonical resolvent form 1/(1 − h_q · q^{α_shift})",
  chapter: "mass-theory",
  cites: ["suslin1991", "thurston1978"],
  uses: [],
  defines: [],
  tags: ["normalization", "no-fitting", "uniqueness", "bring", "residue"],
  lean: { ref: "qou:QOU.BraidKnot.bring_residue_equation" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-05-30",
      body: "The residue/resolvent step was shared across PRs #1444 (α_EM), #1445 (p-n averaging), and #1455 (meson m_K/m_π); the α_shift universal derivation chain audit doc is dated 2026-05-30.",
    },
  ],
});
