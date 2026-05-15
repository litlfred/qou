import { proof } from "../../schema/builders";

export default proof({
  label: "prf:algebraic-causal-action-structure",
  title:
    "Proof of the algebraic causal-action structure on $H_n(R, q)$",
  uses: [
    "prop:algebraic-causal-action-structure",
    "thm:jones-markov-trace",
    "prop:wedderburn-weight-canonical",
    "prop:plancherel-term-7-formulation",
    "prop:operator-selection-lp",
  ],
});
