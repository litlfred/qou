import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-hamiltonian",
  title: "Categorical Hamiltonian and phase-space Legendre transform",
  tags: [
    "hamiltonian",
    "legendre-transform",
    "energy",
    "reeb",
    "phase-space",
  ],
  lean: {
    ref: "qou:QOU.Core.CategoricalHamiltonianLegendre.canonicalHamiltonian",
    validation: "validated",
  },
  computation: {
    engine: "mpmath",
    script: "computations/probes/categorical_hamiltonian_legendre_recoil_probe.py",
    witness: "computations/probes/categorical-hamiltonian-legendre-recoil.witness.json",
    status: "verified",
  },
  uses: [
    "def:categorical-lagrangian",
    "def:categorical-action",
  ],
});
