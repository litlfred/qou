import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:h3-markov-wenzl-weights",
  title:
    "Closed-form Wenzl/Markov weights on $H_3(q)$: $y_{(3)} = [4]_q/[2]_q^3$, $y_{(2,1)} = 1/[2]_q^2$, $y_{(1^3)} = 0$",
  lean: { ref: "qou:QOU.BraidsAndKnots.h3_markov_wenzl_weights" },
  uses: [
    "prop:borromean-markov-trace-closed-form",
  ],
  cites: [
    "jones1987",
  ],
  tags: [
    "wenzl-weights",
    "markov-trace",
    "temperley-lieb",
    "q-deformation",
    "categorical-derivation",
    "closed-form",
  ],
});
