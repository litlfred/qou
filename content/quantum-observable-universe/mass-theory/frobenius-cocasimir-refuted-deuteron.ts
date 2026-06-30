import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:frobenius-cocasimir-refuted-deuteron",
  title:
    "Frobenius co-Casimir $\\Delta_\\lambda$ ansatz refuted at the deuteron",
  uses: ["conj:rho-prefactor-structural"],
  lean: {
    ref: "qou:QOU.BraidKnot.coCasimir_refuted_deuteron",
  },
  computation: {
    engine: "mpmath",
    script: "computations/rho_k_h3a_co_casimir.py",
    witness: "computations/rho-k-h3a-co-casimir.witness.json",
    status: "verified",
  },
  tags: [
    "delta-lambda",
    "refutation",
    "co-casimir",
    "gap-a",
    "deuteron",
    "formalize-the-refutation",
  ],
});
