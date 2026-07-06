import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:toroidal-harmonics-delta-lambda",
  title: "Toroidal Harmonics and the Δ_λ Mass Gap",
  is_mathematics: true,
  computation: {
    engine: "sympy",
    script: "computations/qbeta/toroidal_harmonics.py",
    status: "verified"
  },
  uses: [
    "prop:he4-two-row-dominance",
    "lem:interface-knot-markov-z"
  ]
});
