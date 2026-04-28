import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:landauer-cauchy-schwarz-insufficient",
  title:
    "The L${}^2$-Cauchy--Schwarz lower bound on $\\tau(f^\\dagger f)$ is strictly weaker than the conjectured Landauer bound $\\tau(C_{\\dim_q})$ on a balanced Frobenius family",
  lean: {
    ref:
      "qou:QOU.BraidKnot.landauer_cauchy_schwarz_insufficient",
    validation: "not_checked",
  },
  proofs: ["prf:landauer-cauchy-schwarz-insufficient"],
  uses: [
    "conj:tau-codim-landauer",
    "thm:frobenius-codim-universal",
  ],
  cites: ["kassel1995"],
  tags: [
    "landauer",
    "cauchy-schwarz",
    "no-go",
    "frobenius",
    "conjecture-refinement",
  ],
});
