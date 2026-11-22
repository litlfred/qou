import { remark } from "../../schema/builders";

export default remark({
  label: "rem:borromean-word-selection",
  title: "What fixes the Borromean word",
  interprets: "thm:borromean-character-fibre",
  uses: [
    "thm:borromean-word-minimal",
    "def:crossing-energy",
    "def:f-bor-borromean-observable",
  ],
  tags: ["borromean", "selection-rule", "crossing-energy"],
});
