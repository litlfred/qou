import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-residue-resolvent",
  title: "Bring residue → canonical resolvent form 1/(1 − h_q · q^{α_shift})",
  chapter: "mass-theory",
  cites: ["suslin1991", "thurston1978"],
  uses: [],
  defines: [],
  tags: ["normalization", "no-fitting", "uniqueness", "bring", "residue"],
  lean: { ref: "qou:QOU.BraidKnot.bring_residue_gives_resolvent" },
});
