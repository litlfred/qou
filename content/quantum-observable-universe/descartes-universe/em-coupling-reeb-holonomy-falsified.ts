import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-coupling-reeb-holonomy-falsified",
  title:
    "Option C falsified: Reeb-bundle U(1) holonomy interpretation of $2/(3\\pi)$ is vacuous",
  interprets: "rem:alpha-em-derivation-exploration-options",
  uses: [
    "rem:alpha-em-derivation-exploration-options",
    "conj:em-coupling-bring-zero-mode",
    "def:reeb-bundle",
  ],
  tags: [
    "alpha-em",
    "fine-structure",
    "falsification",
    "negative-result",
    "reeb-bundle",
    "holonomy",
  ],
});
