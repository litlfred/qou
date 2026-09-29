import { remark } from "../../schema/builders";

export default remark({
  label: "rem:euler-characteristic-of-the-regular-representation",
  title: "The quantum dimension of the regular representation is regularisation-dependent",
  interprets: "lem:brings-euler-characteristic",
  uses: ["lem:brings-euler-characteristic", "rem:three-euler-characteristics"],
  tags: ["quantum-dimension", "regularisation", "peter-weyl", "frobenius-hopf-object", "scope-a"],
  computation: {
    engine: "python",
    script: "computations/audits/dimq_regularisation_schemes_probe.py",
    witness: "computations/audits/dimq-regularisation-schemes.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Records a scope-(a) negative: neither of the two standard regularisations of the divergent Peter–Weyl sum gives `-6` at the substrate parameter, so under the 2026-09-15 ruling `tr(id_X) = dim_q(X)` the number `-6` cannot be the trace of the identity of the Frobenius–Hopf object. No regularisation is selected. The two rational identities behind the schemes are proved for every field in `QOU/Information/DimqRegularisationIdentities.lean` (`zeta_geometric_pair_eq_neg_one`, `hadamard_eq_neg_six_iff`, `qint_two`); the analytic-continuation convention itself is cited, not proved.",
    },
  ],
});
