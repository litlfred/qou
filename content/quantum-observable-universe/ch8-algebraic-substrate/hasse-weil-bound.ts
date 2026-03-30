import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hasse-weil-bound",
  title: "Hasse--Weil bound for the fundamental eigenvalues",
  lean: {
    decl: "QOU.AlgebraicSubstrate.hasse_weil_bound",
    validation: "not_checked",
  },
  uses: ["def:local-q-zeta-function", "def:brings-coordinate-ring"],
  tags: [
    "hasse-weil",
    "eigenvalue-bound",
    "frobenius",
    "castelnuovo-severi",
    "riemann-hypothesis-finite-field",
  ],
  cites: ["weil1948"],
});
