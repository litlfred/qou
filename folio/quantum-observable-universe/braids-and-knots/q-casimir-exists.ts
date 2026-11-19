import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body:
        "Proved over any CommRing R with q : Rˣ and Invertible (q - q⁻¹): `QOU.UqRing.qCasimirNormRing` commutes with K, K', E, F " +
        "and acts as `[j]_q [j + 1]_q • v` across every highest-weight spin-j module V_j (`qCasimirNormRing_acts_as_eigenvalue_on_Vj`); " +
        "`QOU.UqSl2.Uq.casimirNorm_central` and `fund_casimirNorm` prove centrality and spin-1/2 action on presented U_q(sl₂), " +
        "alongside `QCasimir.not_exists_unconstrained` showing q ≠ 0 is necessary.",
    },
  ],
  label: "prop:q-casimir-exists",
  title: "Existence of the $q$-Casimir element",
  lean: { ref: "qou:QOU.UqRing.qCasimirNormRing_acts_as_eigenvalue_on_Vj",
    validation: "not_checked",
  },
  uses: ["def:q-casimir"],
  proofs: ["prf:q-casimir-exists"],
  tags: ["existence", "casimir", "quantum-group", "central-element"],
});
