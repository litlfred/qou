import { definition } from "../../schema/builders";

export default definition({
  label: "def:van-der-waals-hopf-channel",
  title: "The van der Waals channel — the Hopf symmetric block",
  lean: {
    ref: "qou:QOU.VanDerWaals.vdwSymmetricBlock",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/hbond_vdw_sdp.py",
    witness: ["computations/hbond-vdw-sdp.witness.json"],
  },
  uses: [
    "def:hopf-diquark",
    "prop:trm-hopf-sigma1-sq-closed-form",
  ],
  tags: [
    "van-der-waals",
    "dispersion",
    "hopf-link",
    "wedderburn-block",
    "idempotent",
    "intermolecular",
    "vol-zero",
  ],
});
