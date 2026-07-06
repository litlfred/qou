import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:averaging-resonance-rule",
  lean: {
    ref: "qou:QOU.BraidKnot.AveragingResonanceRule",
    validation: "not_checked",
  },
  title:
    "Averaging-resonance rule for $c_k$ sectors: precision-ladder rung $k$ lies in the bar-invariant fixed-point sector (= picks up the $1/2$ fingerprint at silver ratio) iff the silver-ratio Pell-Lucas test on $c_k$ fails; empirically $k = 5$ is the only such outlier in the proton typed-$\\mathbf{B}_3$ ladder at $k \\in \\{3, \\ldots, 10\\}$",
  uses: [
    "prop:neutron-qvalue-symbolic",
    "prop:silver-ratio-beta-decay-null",
    "prop:c5-involution-leibniz-decomposition",
  ],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
    "geckpfeiffer2000",
  ],
  tags: [
    "lean-infrastructure",
    "averaging-resonance",
    "bar-invariance",
    "categorical-action",
    "combinatorial-rule",
    "open-rd",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta_half_fill_probe.py",
    witness: [
      "computations/qbeta-half-fill-probe.witness.json",
      "computations/qbeta-decay-sdp-extended-ck.witness.json",
      "computations/qbeta-silver-ratio-pell-lucas-ck.witness.json",
    ],
    status: "experimental",
  },
});
