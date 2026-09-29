import { proof } from "../../schema/builders";

export default proof({
  label: "prf:corrected-markov-trace",
  title: "Proof of corrected markov trace",
  uses: ["prop:corrected-markov-trace"],
});
