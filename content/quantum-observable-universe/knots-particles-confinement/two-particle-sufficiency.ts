import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:pairwise-interaction-decomposition",
  label: "rem:two-particle-sufficiency",
  title: "Why two-particle interactions suffice",
  tags: [
    "braiding",
    "yang-baxter",
    "reidemeister",
    "s-matrix",
    "vortex-reconnection",
    "two-body",
  ],
  uses: ["prop:pairwise-interaction-decomposition"],
  cites: ["kauffman1991", "kleckner2013"],
});
