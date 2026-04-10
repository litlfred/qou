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
  uses: [
    "rem:hawking-radiation",
    "def:jet-horizon",
    "def:computational-horizon",
    "rem:incompleteness-horizon",
    "def:aeon",
    "def:big-bang-state",
    "rem:skein-turing-machine",
    "conj:aeon-boundary-generates-chart",
  ],
  cites: ["hawking1975", "bekenstein1973", "goedel1931"],
});
