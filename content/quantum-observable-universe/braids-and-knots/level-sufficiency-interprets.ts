import { remark } from "../../schema/builders";

export default remark({
  label: "rem:level-sufficiency-interprets",
  title:
    "Physical interpretation of level sufficiency: default coarse, unfold on witness",
  tags: [
    "confinement",
    "nucleon",
    "atom",
    "compound-atom",
    "computational-strategy",
    "magic-numbers",
    "sdp",
  ],
  uses: [
    "prop:level-sufficiency",
    "def:confinement-level",
    "prop:confinement-lp",
    "prop:confinement-topological",
  ],
  interprets: "prop:level-sufficiency",
});
