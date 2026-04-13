import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:boltzmann-constant",
  title: "Boltzmann constant is unity in QOU natural units",
  tags: [
    "boltzmann-constant",
    "statistical-mechanics",
    "planck-constant",
  ],
  lean: {
    decl: "QOU.Information.thermalEnergy",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-temperature",
    "def:quantum-planck-constant",
  ],
});
