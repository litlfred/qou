import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-laplacian-spectral-tower",
  title:
    "The $q$-Laplacian spectral tower $[k]_q^2$ and its " +
    "root-of-unity (Verlinde/ADE) truncation",
  uses: ["def:q-harmonic-form"],
  cites: ["verlinde1988", "reshetikhin1991", "kassel1995"],
  computation: {
    engine: "sympy",
    script:
      "computations/q_spectral_truncation_tower.py",
    witness:
      "computations/q-spectral-truncation-tower.witness.json",
    status: "verified",
  },
  lean: {
    ref:
      "qou:QOU.QuantumObservableUniverses.qIntegerNumerator_vanishes_at_truncRoot",
  },
  tags: [
    "q-laplacian",
    "q-integer",
    "spectral-tower",
    "root-of-unity",
    "verlinde",
    "ade-quantum-dimension",
    "fibre-level",
    "unifying",
  ],
});
