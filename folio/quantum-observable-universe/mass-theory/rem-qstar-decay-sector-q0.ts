import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:im-q-physical-role",
  label: "rem:qstar-decay-sector-q0",
  title:
    "The $S = 0$ point $q^{*}$ is conditional on $c_3^{\\mathrm{even}} = -\\mathrm{Vol}(4_1)$, not an independent determination of $q_0$",
  uses: ["conj:im-q-physical-role", "rem:c3-s-imq-decay-projection"],
  tags: [
    "im-q",
    "decay-width",
    "q-beta",
    "c3-bar-odd",
    "substrate-anchor",
    "mu-p-tension",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/qbeta/qbeta_c3_imq_qstar_ladder_amplification_probe.py (witness qbeta-c3-imq-qstar-ladder-amplification.witness.json).",
    },
    {
      kind: "refined-framing",
      body: "An earlier version of this remark claimed q* was an independent third determination of q₀.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/qbeta/qbeta_c3_imq_qstar_ladder_amplification_probe.py",
    witness: [
      "computations/qbeta/qbeta-c3-imq-qstar-ladder-amplification.witness.json",
      "computations/q-pinning-50-digit.witness.json",
      "computations/per-observable-100x-status.witness.json",
      "computations/qbeta/qbeta-ladder-alpha-provenance.witness.json",
    ],
    status: "verified",
  },
});
