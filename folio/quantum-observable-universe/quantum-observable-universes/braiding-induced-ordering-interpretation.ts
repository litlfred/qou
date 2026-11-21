import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:braiding-induced-ordering",
  label: "rem:braiding-induced-ordering-interpretation",
  title: "Crossing direction, Reeb flow and time reversal",
  uses: [
    "prop:braiding-induced-ordering",
    "def:categorical-reeb-derivation",
    "prop:antiparticle-crossing-reversal",
  ],
  tags: ["braiding", "arrow-of-time", "temporal", "reeb", "cpt"],
});
