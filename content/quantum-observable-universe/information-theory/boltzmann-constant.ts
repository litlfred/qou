import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:boltzmann-constant",
  title: "Boltzmann constant as quantum Planck constant",
  tags: [
    "boltzmann-constant",
    "statistical-mechanics",
    "planck-constant",
  ],
  lean: {
    decl: "QOU.Information.boltzmannConstant",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-temperature",
    "def:quantum-planck-constant",
    "prop:quantum-ideal-gas-law",
  ],
});
