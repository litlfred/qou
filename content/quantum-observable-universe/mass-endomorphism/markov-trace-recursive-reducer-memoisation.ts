import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:markov-trace-recursive-reducer",
  label: "rem:markov-trace-recursive-reducer-memoisation",
  title: "Memoisation optimisation of the recursive Markov-trace reducer",
  uses: [
    "prop:markov-trace-recursive-reducer",
    "prop:markov-trace-axiomatic-closed-form",
  ],
  tags: [
    "markov-trace",
    "recursive-algorithm",
    "memoisation",
    "optimisation",
  ],
});
