import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-alpha-k-h3",
  proofs: ["prf:explicit-alpha-k-h3"],
  title: "Explicit α_k at H_3(R, q): structural prefactors closed form",
  lean: { ref: "qou:QOU.BraidsAndKnots.explicit_alpha_k_h3",
    validation: "not_checked",
  },
  uses: ["prop:spectral-sequence-h3-explicit"],
  tags: [
    "spectral-sequence",
    "alpha-k",
    "hecke-algebra",
    "markov-trace",
    "jones-markov",
    "h3",
    "structural-derivation",
    "q-algebraic",
  ],
});
