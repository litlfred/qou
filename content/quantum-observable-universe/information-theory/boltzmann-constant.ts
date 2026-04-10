import { definition } from "../../schema/builders";

export default definition({
  label: "def:boltzmann-constant",
  title: "Boltzmann constant and gas constant from $q$",
  tags: [
    "boltzmann-constant",
    "gas-constant",
    "statistical-mechanics",
    "planck-constant",
    "avogadro",
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
