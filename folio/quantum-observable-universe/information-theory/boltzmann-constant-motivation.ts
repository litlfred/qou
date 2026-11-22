import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:boltzmann-constant",
  label: "rem:boltzmann-constant-motivation",
  title: "Why the Boltzmann constant is set to unity",
  tags: ["boltzmann-constant", "statistical-mechanics", "interpretation"],
  uses: ["def:boltzmann-constant", "def:quantum-temperature"],
});
