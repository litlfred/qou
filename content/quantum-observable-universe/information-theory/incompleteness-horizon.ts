import { remark } from "../../schema/builders";

export default remark({
  label: "rem:incompleteness-horizon",
  title:
    "Incompleteness as degree-$0$ opacity: the Turing--G\u00f6del--horizon triangle",
  interprets: "def:computational-horizon",
  tags: [
    "incompleteness",
    "goedel",
    "turing-completeness",
    "computational-horizon",
    "jet-horizon",
    "black-hole",
    "information-paradox",
    "degree-0-opacity",
  ],
  uses: [
    "def:computational-horizon",
    "conj:p-vs-np-boundary",
    "rem:skein-turing-machine",
    "def:jet-horizon",
    "rem:hawking-radiation",
    "def:observable-subcategory",
    "def:big-bang-state",
  ],
  cites: ["goedel1931", "turing1936"],
});
