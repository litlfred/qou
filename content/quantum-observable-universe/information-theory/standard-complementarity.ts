import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:algebraic-gns-embedding",
  label: "rem:standard-complementarity",
  title: "Standard complementarity: one Hilbert space, per-observer operator frames",
  tags: [
    "black-hole-complementarity",
    "gns-embedding",
    "markov-trace",
    "observable-subcategory",
    "information-causality",
  ],
  uses: [
    "prop:algebraic-gns-embedding",
    "def:observable-subcategory",
    "rem:observable-beable-correspondence",
    "rem:information-paradox-incompleteness",
  ],
  cites: ["marolf2017", "susskind1993", "thooft2016"],
});
