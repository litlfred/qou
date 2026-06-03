import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-over-e0-classical-vanishing",
  title:
    "$S(q) = Q_\\beta(q)/E_0(q)$ vanishes at the classical point $q = 1$ — the SDP-constraint scalar is not the $c_k$ ladder normalization",
  lean: {
    ref: "qou:QOU.QBeta.OverE0ClassicalVanishing.qbeta_over_e0_numerator_at_one_eq_zero",
    validation: "not_checked",
  },
  uses: [
    "prop:neutron-qvalue-symbolic",
    "rem:beta-decay-energy-scale",
    "prop:t-beta-markov-frobenius-collapse",
  ],
  cites: ["jones1987", "wenzl1988"],
  computation: {
    engine: "sympy",
    script:
      "folio-assistant/computations/qbeta/qbeta_habiro_f_from_shape_collapse.py",
    witness:
      "folio-assistant/computations/qbeta/qbeta-habiro-f-from-shape-collapse.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "markov-trace",
    "frobenius",
    "diagnostic",
    "ladder-normalization",
    "classical-limit",
  ],
});
