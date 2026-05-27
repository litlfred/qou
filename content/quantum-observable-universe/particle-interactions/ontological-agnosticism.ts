import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:crystal-graph-realization",
  label: "rem:ontological-agnosticism",
  title:
    "Crystal-limit observables transport flatly to the generic fibre",
  uses: [
    "prop:crystal-graph-realization",
    "prop:confinement-grading-correspondence",
    "prop:gb-spectral-sequence",
    "def:cemetery-group",
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
