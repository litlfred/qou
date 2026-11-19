import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-beta-c-k-leading-bias-correction-identity",
  title: "Proof of q beta c k leading bias correction identity",
  uses: ["prop:q-beta-c-k-leading-bias-correction-identity"],
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_ck_truncation_bias_correction_probe.py",
    witness: [
      "computations/qbeta/qbeta-ck-truncation-bias-correction-probe.witness.json",
      "computations/qbeta/qbeta-radius-of-convergence-gate-probe.witness.json",
    ],
    status: "verified",
  },
});
