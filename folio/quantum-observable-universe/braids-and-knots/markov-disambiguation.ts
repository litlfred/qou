import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-disambiguation",
  title: "Three uses of \\emph{Markov} in this work",
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
