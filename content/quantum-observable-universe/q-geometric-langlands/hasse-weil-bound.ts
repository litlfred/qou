import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hasse-weil-bound",
  proofs: ["prf:hasse-weil-bound"],
  title: "Hasse--Weil bound for the fundamental eigenvalues",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.hasse_weil_bound",
    validation: "not_checked",
  },
  uses: ["def:local-q-zeta-function"],
  tags: [
    "hasse-weil",
    "eigenvalue-bound",
    "frobenius",
    "castelnuovo-severi",
    "riemann-hypothesis-finite-field",
  ],
  cites: ["weil1948", "rosen2002", "milne2013"],
});
