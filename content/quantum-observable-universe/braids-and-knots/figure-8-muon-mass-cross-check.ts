import { remark } from "../../schema/builders";

export default remark({
  label: "rem:figure-8-muon-mass-cross-check",
  title:
    "Numerical cross-check of CAL-2: $\\mathrm{Vol}(4_1)/\\hbar_q^2 = m_\\mu/m_e$ at 50 dps",
  interprets: "prop:three-calibration-inputs",
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/derive_m_baryon_volume_form.py",
    witness:
      "folio-assistant/computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
  uses: [
    "prop:three-calibration-inputs",
    "def:quantum-planck-constant",
    "rem:figure-8-archimedean-illustration",
    "conj:borromean-baryon-mass-formula",
  ],
  cites: ["codata2022", "thurston1978"],
  tags: [
    "figure-8-knot",
    "muon",
    "cal-2",
    "q-pinning",
    "substrate-cross-check",
    "50-dps",
    "topological-mass",
  ],
});
