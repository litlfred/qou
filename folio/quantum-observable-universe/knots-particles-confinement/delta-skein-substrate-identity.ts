import { remark } from "../../schema/builders";

export default remark({
  label: "rem:delta-skein-substrate-identity",
  title:
    "Aether identity for the proton–neutron Skein difference $\\Delta S(n-p)$",
  interprets: "conj:borromean-baryon-mass-formula",
  computation: {
    engine: "mpmath",
    script:
      "computations/derive_m_baryon_volume_form.py",
    witness: [
      "computations/m-baryon-volume-form.witness.json",
      "computations/codata-masses.witness.json",
      "computations/qbeta/qbeta-cos-resummation-d.witness.json",
    ],
    status: "verified",
  },
  uses: [
    "conj:borromean-baryon-mass-formula",
    "prop:q-beta-spectral-bridge",
  ],
  cites: ["codata2022"],
  tags: [
    "borromean",
    "skein",
    "delta-s",
    "neutron-proton",
    "q-beta",
    "substrate-only",
    "no-fitting",
    "three-calibration",
    "common-scale",
  ],
});
