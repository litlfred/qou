import { remark } from "../../schema/builders";

export default remark({
  label: "rem:level-zero-discards-braid-noncommutativity",
  title:
    "Level-0 discards braid non-commutativity at every $n \\geq 3$, not only " +
    "the non-extremal blocks at $n \\geq 4$",
  interprets: "thm:wedderburn-mass-formula",
  tags: ["level-zero", "transfer-matrix", "scope", "deuterium"],
  uses: ["thm:wedderburn-mass-formula", "prf:wedderburn-mass-formula"],
});
