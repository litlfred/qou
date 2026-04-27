import { remark } from "../../schema/builders";

export default remark({
  label: "rem:incompleteness-horizon",
  title:
    "Incompleteness as degree-$0$ opacity: the Turing--G\u00f6del--horizon triangle",
  interprets: "prop:incompleteness-implies-horizon",
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
    "prop:incompleteness-implies-horizon",
    "rem:substrate-computation",
    "rem:p-vs-np-event-horizon",
  ],
  cites: ["goedel1931", "turing1936"],
});
