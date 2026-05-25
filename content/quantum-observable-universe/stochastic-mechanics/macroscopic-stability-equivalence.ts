import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:macroscopic-stability-equivalence",
  title:
    "Macroscopic stability is equivalent to the Riemann hypothesis",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.macroscopic_stability_equivalence",
    validation: "not_checked",
  },
  uses: [
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
  cites: ["vonkoch1901", "weil1948"],
});
