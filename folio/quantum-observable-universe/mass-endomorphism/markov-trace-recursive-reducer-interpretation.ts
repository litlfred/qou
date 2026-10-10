import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:markov-trace-recursive-reducer",
  label: "rem:markov-trace-recursive-reducer-interpretation",
  title: "Memoisation optimisation and the categorical-mass reading of the reducer",
  tags: [
    "markov-trace",
    "recursive-algorithm",
    "memoisation",
    "categorical-mass",
  ],
  uses: [
    "prop:markov-trace-recursive-reducer",
    "prop:markov-trace-axiomatic-closed-form",
  ],
});
