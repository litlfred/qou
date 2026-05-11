import { remark } from "../../schema/builders";

export default remark({
  label: "rem:delta-skein-substrate-identity",
  title:
    "Substrate identity for the proton–neutron Skein difference $\\Delta S(n-p)$",
  interprets: "conj:borromean-baryon-mass-formula",
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/derive_m_baryon_volume_form.py",
    witness:
      "folio-assistant/computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
  uses: [
    "conj:borromean-baryon-mass-formula",
    "prop:three-calibration-inputs",
    "rem:beta-decay-energy-scale",
    "def:borromean-baryon",
    "def:quantum-planck-constant",
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
