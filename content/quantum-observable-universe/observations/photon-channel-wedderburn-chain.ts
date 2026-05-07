import { remark } from "../../schema/builders";

export default remark({
  label: "rem:photon-channel-wedderburn-chain",
  title: "From 4 photon channels to 3 Wedderburn invariants",
  interprets: "thm:wedderburn-mass-formula",
  uses: ["thm:wedderburn-mass-formula"],
  computation: {
    engine: "python+numpy+cvxpy",
    script: "folio-assistant/computations/sdp_gamma_gamma_to_qqbar.py",
    witness: [
      "folio-assistant/computations/probe-gamma-gamma-h3-psd-scan.witness.json",
      "folio-assistant/computations/probe-gamma-gamma-lr-embed-h6.witness.json",
      "folio-assistant/computations/sdp-gamma-gamma-to-qqbar.witness.json",
    ],
    status: "experimental",
  },
});
