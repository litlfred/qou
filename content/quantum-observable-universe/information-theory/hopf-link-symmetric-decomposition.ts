import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hopf-link-symmetric-decomposition",
  title: "Hopf-link symmetric decomposition: $\\sigma_1^2 = q^2 e_+ + q^{-2} e_-$",
  lean: {
    ref: "qou:QOU.HopfSymmetric.hopf_symmetric_decomposition",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/hbond_vdw_sdp.py",
    witness: ["computations/hbond-vdw-sdp.witness.json"],
  },
  uses: [
    "def:van-der-waals-hopf-channel",
    "prop:trm-hopf-sigma1-sq-closed-form",
  ],
  tags: [
    "van-der-waals",
    "hopf-link",
    "wedderburn-decomposition",
    "symmetric-block",
    "hecke",
  ],
});
