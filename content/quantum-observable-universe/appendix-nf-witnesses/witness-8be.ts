import { definition } from "../../schema/builders";

export default definition({
  label: "def:witness-8be",
  title: "Pauli witness for ${}^8\\mathrm{Be}$ (exact in $q$)",
  tags: ["pauli-witness", "beryllium-8", "exact-polynomial"],
  lean: {
    decl: "QOU.Descartes.PauliWitness.witness_8Be",
    file: "witness-8be.lean",
  },
  uses: ["def:hecke-normal-form", "prop:shell-closure-normal-form"],
});
