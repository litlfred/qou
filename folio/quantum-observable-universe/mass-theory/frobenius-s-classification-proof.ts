import { proof } from "../../schema/builders";

export default proof({
  label: "prf:frobenius-s-classification",
  title: "Proof of frobenius s classification",
  uses: ["prop:frobenius-s-classification"],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/h2_gg_electron/h2_gg_electron_probe.py",
    witness: ["computations/probes/h2_gg_electron/h2-gg-electron.witness.json"],
    status: "verified",
  },
});
