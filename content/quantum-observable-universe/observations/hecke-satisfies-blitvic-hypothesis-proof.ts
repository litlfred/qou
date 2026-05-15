import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-satisfies-blitvic-hypothesis",
  title: "Proof: Hecke generators satisfy Blitvić's pair-partition hypothesis",
  uses: [
    "prop:hecke-satisfies-blitvic-hypothesis",
    "thm:jones-markov-trace",
    "prop:trace-locality-meets-gs-non-locality",
  ],
});
