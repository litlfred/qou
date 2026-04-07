import { definition } from "../../schema/builders";

export default definition({
  label: "def:witness-4he",
  title: "Pauli witness for ${}^4\\mathrm{He}$ (exact in $q$)",
  tags: ["pauli-witness", "helium-4", "doubly-magic", "exact-polynomial"],
  lean: {
    decl: "QOU.Descartes.PauliWitness.witness_4He",
    file: "witness-4he.lean",
  },
  uses: ["def:hecke-normal-form", "prop:shell-closure-normal-form"],
});
