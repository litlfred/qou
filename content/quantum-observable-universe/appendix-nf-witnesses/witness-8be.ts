import { definition } from "../../schema/builders";

export default definition({
  label: "def:witness-8be",
  title: "Pauli witness for ${}^8\\mathrm{Be}$ (exact in $q$)",
  tags: ["pauli-witness", "beryllium-8", "exact-polynomial"],
  lean: { ref: "qou:QOU.Descartes.PauliWitness.witness_8Be",
  },
  uses: ["def:hecke-normal-form", "prop:shell-closure-normal-form"],
});
