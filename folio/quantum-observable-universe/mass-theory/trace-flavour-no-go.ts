import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trace-flavour-no-go",
  title: "A cyclic trace on $H_3(q)$ cannot separate a nucleon word from its flip–reversal",
  lean: {
    ref: "qou:QOU.Mass.PhotonTraceLemmas.trace_flip_reverse",
  },
  uses: ["def:photon", "prop:borromean-two-photon-factorisation", "def:typed-crossing-operator"],
  cites: ["iwahori1964", "kassel2008"],
  tags: ["borromean", "hecke-algebra", "nucleon-element", "markov-trace", "flavour"],
});
