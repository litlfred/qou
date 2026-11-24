import { prose } from "../../schema/builders";

export default prose({
  label: "prose:master-atlas-calibration-jacobian",
  title:
    "Archimedean calibration protocol and 80-digit Fréchet--Jacobian error propagation",
  uses: [
    "def:quantum-observable-universe",
    "rem:epistemic-status-of-calibrations",
    "def:confined-particle",
  ],
  cites: [
    "codata2022",
    "pdg2024",
    "ame2020",
    "ame2020tables",
    "nubase2020",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
  tags: [
    "archimedean-bridge",
    "atlas",
    "calibration",
    "error-propagation",
    "jacobian",
    "q0",
    "appendix",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Beans qou-anx0 & qou-nmjd (Q2 Option 3): establishes the uniform 80-dps " +
        "(workdps = 95, output_dps = 80, truncation_bound <= 1e-60) Fréchet–Jacobian " +
        "error-propagation law across Tables A.1–A.5 using physical calibration " +
        "observables (m_e, D_beta, m_pi) corresponding to QOU.Mass.calibrations_eq_cohomology " +
        "(dim H^1(Sigma_4) = 2W), with zero internal CAL-1/2/3 or Convention A/B/C/D prose tokens.",
    },
  ],
});
