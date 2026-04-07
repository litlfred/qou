import { definition } from "../../schema/builders";

export default definition({
  label: "def:witness-12c",
  title: "Pauli witness for ${}^{12}\\mathrm{C}$ (exact in $q$)",
  tags: ["pauli-witness", "carbon-12", "doubly-magic", "exact-polynomial"],
  lean: {
    decl: "QOU.Descartes.PauliWitness.witness_12C",
    file: "witness-12c.lean",
  },
  uses: ["def:hecke-normal-form", "prop:shell-closure-normal-form"],
});
