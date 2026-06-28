import { proof } from "../../schema/builders";

export default proof({
  label: "prf:markov-trace-product",
  title: "Proof of markov trace product",
  uses: ["thm:markov-trace-product"],
});
