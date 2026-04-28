import { proof } from "../../schema/builders";

export default proof({
  label: "prf:feynman-markov-identification",
  title: "Proof that the eigenbasis amplitude equals the Markov trace",
  uses: ["lem:feynman-markov-identification"],
});
