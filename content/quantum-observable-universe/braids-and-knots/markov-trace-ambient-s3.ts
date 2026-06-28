import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-trace-ambient-s3",
  title:
    "The ambient three-sphere $S^3$ is the target of the Alexander--Markov correspondence: $\\mathrm{tr}_M$ is by construction a link invariant in $S^3$",
  interprets: "thm:jones-markov-trace",
  uses: ["thm:jones-markov-trace"],
  cites: ["alexander1923", "markov1936", "jones1987"],
  tags: [
    "markov-trace",
    "ambient-manifold",
    "three-sphere",
    "alexander-markov",
    "knot-complement",
    "categorical-topology",
  ],
});
