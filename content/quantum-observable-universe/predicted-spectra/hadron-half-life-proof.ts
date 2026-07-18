import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hadron-half-life",
  title: "Decay rate from $q$ and $\\mu_0$",
  uses: ["prop:hadron-half-life", "prop:trace-ratio-observable", "thm:markov-trace-factorization"],
});
