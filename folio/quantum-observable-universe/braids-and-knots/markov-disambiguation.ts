import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-disambiguation",
  title: "Three uses of Markov in this paper",
  interprets: "thm:jones-markov-trace",
  uses: [
    "thm:jones-markov-trace",
  ],
  tags: [
    "notation",
    "markov",
    "disambiguation",
  ],
});
