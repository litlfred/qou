import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-satisfies-blitvic-hypothesis",
  title:
    "Hecke transfer matrices satisfy Blitvić's pair-partition combinatorial hypothesis for the non-commutative CLT",
  lean: { ref: "qou:QOU.Observations.hecke_satisfies_blitvic_hypothesis", validation: "not_checked" },
  uses: [
    "rem:non-commutative-probability-dictionary",
    "thm:jones-markov-trace",
  ],
  cites: ["blitvic2012", "wenzl1988"],
  tags: [
    "q-clt",
    "blitvic",
    "pair-partition",
    "hecke-quadratic-relation",
    "established",
  ],
  proofs: ["prf:hecke-satisfies-blitvic-hypothesis"],
});
