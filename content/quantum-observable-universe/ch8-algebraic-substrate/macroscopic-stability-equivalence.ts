import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:macroscopic-stability-equivalence",
  title:
    "Macroscopic stability is equivalent to the Riemann hypothesis",
  lean: {
    decl: "QOU.AlgebraicSubstrate.macroscopic_stability_equivalence",
    validation: "not_checked",
  },
  uses: [
    "conj:classical-riemann-hypothesis",
    "cor:spectral-half-line",
    "thm:quantum-gap-collapse",
  ],
  tags: [
    "stability",
    "equivalence",
    "riemann-hypothesis",
    "macroscopic",
    "continuum",
  ],
  cites: ["weil1948"],
});
