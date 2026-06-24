import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-pair-z2",
  proofs: ["prf:markov-pair-z2"],
  title:
    "All-pairs Markov-trace identity $\\mathrm{tr}_M(\\sigma_i\\sigma_j) = z^2$",
  tags: [
    "markov-trace",
    "hecke-algebra",
    "pair-factorization",
    "jet-tower",
  ],
  lean: {
    ref: "qou:QOU.Hecke.markov_pair_z2",
    validation: "not_checked",
  },
  uses: ["rem:mass-endomorphism-jet-tower"],
  cites: ["kassel1995", "jones1987"],
});
