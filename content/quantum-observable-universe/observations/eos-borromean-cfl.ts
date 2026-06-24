import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:eos-borromean-cfl",
  proofs: ["prf:eos-borromean-cfl"],
  title:
    "Equation of state: Borromean hadronic matter vs CFL quark matter",
  tags: [
    "equation-of-state",
    "pressure",
    "energy-density",
    "speed-of-sound",
    "conformal-limit",
    "neutron-star",
    "borromean",
    "CFL",
    "fermi-gas",
  ],
  lean: { ref: "qou:QOU.Archimedean.eos_borromean_cfl",
    validation: "not_checked",
  },
  uses: ["prop:borromean-hopf-energy-crossover"],
});
