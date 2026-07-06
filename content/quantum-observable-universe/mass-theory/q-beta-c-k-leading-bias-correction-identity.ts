import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-beta-c-k-leading-bias-correction-identity",
  title:
    "Leading-bias correction identity for joint-fit extraction of the $c_k$ ladder — $\\hat c_k - \\hat c_{k+1} \\cdot u_0 = c_k^{\\mathrm{alg}}$ when the extraction bias is $\\hat c_k = c_k^{\\mathrm{alg}} + c_{k+1}^{\\mathrm{alg}} \\cdot u_0$ (one-line ring)",
  lean: {
    ref: "qou:QOU.QBeta.CkLeadingBiasCorrection.bias_correction_recovers_alg",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-c-2-eq-neg-one-structural",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["jones1987"],
  computation: {
    engine: "python+mpmath",
    script:
      "computations/qbeta/qbeta_ck_truncation_bias_correction_probe.py",
    witness:
      "computations/qbeta/qbeta-ck-truncation-bias-correction-probe.witness.json",
    status: "verified",
  },
  tags: [
    "q-beta",
    "precision-ladder",
    "structural",
    "c-k",
    "generating-function",
    "bias-correction",
    "categorical-derivation",
  ],
});
