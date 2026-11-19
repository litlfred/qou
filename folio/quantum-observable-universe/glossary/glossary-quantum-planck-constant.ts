import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-quantum-planck-constant",
  title: "Quantum Planck constant $\\hbar_q$",
  tags: ["glossary", "foundations", "planck-constant", "q-deformation"],
  uses: ["def:quantum-planck-constant", "prop:reeb-coefficient-is-hbar-q"],
});
