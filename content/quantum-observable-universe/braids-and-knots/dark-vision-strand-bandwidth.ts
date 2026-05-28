import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dark-vision-strand-bandwidth",
  title:
    "Dark-vision impossibility from strand-bandwidth of the observation channel",
  uses: [
    "def:observation",
    "def:hecke-normal-form",
    "conj:crystal-graph-realization",
    "conj:confinement-grading-correspondence",
  ],
  cites: [
    "kashiwara1991",
  ],
  tags: [
    "interpretation",
    "observation-frame",
    "vision",
    "strand-count",
    "information",
  ],
  interprets: "def:observation",
});
