import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:boltzmann-constant",
  proofs: ["prf:boltzmann-constant"],
  title: "Boltzmann constant is unity in QOU natural units",
  tags: [
    "boltzmann-constant",
    "statistical-mechanics",
    "planck-constant",
  ],
  lean: { ref: "qou:QOU.Information.thermalEnergy",
    validation: "not_checked",
  },
  uses: ["def:quantum-temperature"],
});
