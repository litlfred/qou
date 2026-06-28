import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dressed-quark-distance-from-bound",
  title: "Dressed-quark split at $33\\%$ of the substrate mass-splitting bound",
  tags: ["flavor", "quark-mass", "mass-splitting", "slack-ratio", "q0"],
  interprets: "prop:flavor-dressed-mass-from-substrate-split",
  uses: ["thm:flavor-mass-splitting-bound"],
});
