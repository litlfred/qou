import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-mass-positivity",
  title:
    "Structural positivity of categorical mass and action",
  uses: [
    "def:mass-identity",
    "def:cemetery-group",
    "conj:crystal-graph-realization",
  ],
  cites: [
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "positivity",
    "categorical-mass",
    "klr",
    "computational-shortcut",
  ],
  interprets: "def:mass-identity",
});
