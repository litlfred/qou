import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:toroidal-harmonics-delta-lambda",
  title: "A toroidal-harmonic change of variables for the $z$-recursion",
  is_mathematics: true,
  lean: { ref: "qou:QOU.QBeta.toroidal_ode_to_markov_w" },
  computation: {
    engine: "sympy",
    script: "computations/qbeta/toroidal_harmonics.py",
    status: "verified"
  },
  uses: [
    "prop:interface-knot-markov-z"
  ]
});
