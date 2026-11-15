import { remark } from "../../schema/builders";

export default remark({
  label: "rem:information-paradox-incompleteness",
  title:
    "The information paradox as a theorem of arithmetic",
  interprets: "rem:hawking-radiation",
  tags: [
    "information-paradox",
    "incompleteness",
    "black-hole",
    "hawking-radiation",
    "goedel",
    "degree-0-opacity",
    "aeon-boundary",
  ],
  uses: ["rem:incompleteness-horizon"],
  cites: ["arxiv-1301.4504v4", "arxiv-hep-th-9506138v1", "hawking1975", "bekenstein1973", "goedel1931"],
});
