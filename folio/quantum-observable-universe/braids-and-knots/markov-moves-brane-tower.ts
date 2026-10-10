import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:jones-markov-trace",
  label: "rem:markov-moves-brane-tower",
  title: "Markov moves as horizontal and vertical components",
  tags: ["markov-trace", "brane-tower", "cosimplicial", "weight-decomposition"],
  uses: [
    "thm:jones-markov-trace",
    "thm:weight-decomposition-exists",
    "prop:cosimplicial-crossed-groupoid",
    "def:direct-limit-algebra",
  ],
});
