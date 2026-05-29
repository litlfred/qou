import { remark } from "../../schema/builders";

export default remark({
  label: "rem:delta-skein-substrate-identity",
  title:
    "Substrate identity for the proton–neutron Skein difference $\\Delta S(n-p)$",
  interprets: "prop:borromean-baryon-mass-formula",
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/derive_m_baryon_volume_form.py",
    witness: [
      "folio-assistant/computations/m-baryon-volume-form.witness.json",
      "folio-assistant/computations/codata-masses.witness.json",
    ],
    status: "verified",
  },
  uses: [
    "prop:borromean-baryon-mass-formula",
    "prop:three-calibration-inputs",
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
