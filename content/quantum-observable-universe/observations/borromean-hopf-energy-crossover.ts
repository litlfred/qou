import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-hopf-energy-crossover",
  proofs: ["prf:borromean-hopf-energy-crossover"],
  title:
    "Energy crossover between Borromean and Hopf-diquark phases",
  tags: [
    "borromean",
    "hopf",
    "diquark",
    "energy-crossover",
    "critical-density",
    "phase-transition",
    "color-superconductivity",
  ],
  lean: { ref: "qou:QOU.Archimedean.borromean_hopf_energy_crossover",
    validation: "not_checked",
  },
  uses: ["def:hopf-diquark"],
});
