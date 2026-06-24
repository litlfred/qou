import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:alpha-k-derivation-procedure",
  proofs: ["prf:alpha-k-derivation-procedure"],
  title:
    "Linear-system procedure for Jones--Markov weights $y_\\lambda$ and stratum prefactors $\\alpha_k$ at $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.alpha_k_derivation_procedure",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-tower-coefficient-stratification",
    "prop:spectral-sequence-h3-explicit",
  ],
  tags: [
    "alpha-k",
    "jones-markov",
    "mass-tower",
    "linear-system",
    "wedderburn",
    "procedure",
    "parameterised",
  ],
});
