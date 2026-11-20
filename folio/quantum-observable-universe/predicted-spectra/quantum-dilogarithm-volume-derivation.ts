import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-dilogarithm-volume",
  title: "Derivation of the quantum dilogarithm volume from the topological mass formula",
  uses: ["prop:quantum-dilogarithm-volume", "conj:topological-mass-formula"],
});
