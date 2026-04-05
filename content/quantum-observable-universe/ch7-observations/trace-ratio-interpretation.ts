import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:trace-ratio-observable",
  label: "rem:trace-ratio-interpretation",
  title: "Trace ratio computational results and the half-life formula",
  tags: [
    "markov-trace",
    "half-life",
    "matrix-element",
    "interpretation",
  ],
  uses: [
    "prop:trace-ratio-observable",
    "thm:markov-trace-factorization",
    "prop:skein-coulomb-enhancement",
    "prop:hadron-half-life",
  ],
});
