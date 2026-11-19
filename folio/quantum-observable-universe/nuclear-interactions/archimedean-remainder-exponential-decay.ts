import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:archimedean-remainder-exponential-decay",
  title:
    "Exponential decay of the archimedean brane-tower and geometrically majorized truncation remainders",
  lean: {
    ref: "qou:QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure.braneTower_exists_exp_decay_bound",
    validation: "validated",
  },
  uses: [
    "prop:neutron-qvalue-symbolic",
  ],
  cites: [
    "jones1985",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/c_k_beta_decay_witness.py",
    witness: [
      "computations/c-k-beta-decay-bound.witness.json",
      "computations/qbeta/qbeta-convention-d-all-order-ck-generating.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Proved unconditionally in `folio/quantum-observable-universe/lean/QOU/Nuclear/BraneTowerExponentialDecayAndCPTClosure.lean` (`geometric_limit_sub_partialSum`, `hbarQ_mem_unit_interval`, `hbarQSq_mem_unit_interval`, `braneTowerExactLimit_sub_partialSum`, `braneTower_geometric_ceiling_eq_exp_decay`, `braneTower_remainder_abs_eq_exp_decay`, `braneTower_exists_exp_decay_bound`, `abs_seriesTailRemainder_le_geometric`, `abs_seriesTailRemainder_le_exp_decay`, `exists_exp_decay_of_geom_majorant`).",
    },
  ],
  tags: [
    "q-beta",
    "brane-tower",
    "truncation-remainder",
    "exponential-decay",
    "archimedean",
    "beta-decay",
  ],
});
