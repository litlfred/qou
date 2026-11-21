import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:leray-profile",
  label: "rem:leray-profile-exclusions",
  title: "Exclusions for discretely self-similar Leray profiles",
  uses: ["def:leray-profile", "def:substrate-parameter", "thm:ns-singularity-descartes"],
  cites: [
    "necas-ruzicka-sverak1996",
    "tsai1998",
    "seregin2012",
    "chae2013adss",
    "chae-wolf2016dss",
    "bradshaw-tsai2018survey",
  ],
  tags: ["leray", "discretely-self-similar", "blowup-profile", "literature"],
});
