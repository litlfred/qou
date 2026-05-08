import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:crystal-graph-realization",
  label: "rem:ontological-agnosticism",
  title:
    "Crystal-limit observables transport flatly to the generic fibre",
  uses: [
    "conj:crystal-graph-realization",
    "conj:confinement-grading-correspondence",
    "prop:gb-spectral-sequence",
    "def:cemetery-group",
    "def:exceptional-divisor",
  ],
  cites: [
    "kashiwara1991",
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "crystal-limit",
    "klr",
    "generic-fibre",
    "transport",
    "computational-shortcut",
  ],
});
