import { proof } from "../../schema/builders";

export default proof({
  label: "prf:algebraic-gns-embedding",
  title: "Proof of the Markov-trace GNS embedding",
  uses: [
    "prop:algebraic-gns-embedding",
    "thm:jones-markov-trace",
  ],
});
