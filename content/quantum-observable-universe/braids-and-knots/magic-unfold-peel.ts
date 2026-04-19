import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:magic-unfold-peel",
  title:
    "Markov peel of atom Markov trace at magic shell closures",
  lean: {
    decl: "QOU.MassEndomorphism.magic_unfold_peel",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "prop:mass-endomorphism-tower",
    "prop:atomic-braid-mass",
    "thm:markov-trace-factorization",
  ],
  cites: ["leitner2026", "jones1985", "wenzl1988"],
});
