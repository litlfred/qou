import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:topological-mass-formula",
  label: "rem:mass-comparison-table",
  title: "Mass predictions from knot formulas vs. CODATA/PDG values",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json", "computations/codata-masses.witness.json"],
    status: "verified",
  },
  tags: [
    "mass",
    "prediction",
    "CODATA",
    "PDG",
    "comparison",
    "knot",
    "experimental",
  ],
  uses: ["rem:mass-from-generators"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Proton/neutron LO rows (witness: [`atomic-mass-via-rho-k.witness.json`](../../../computations/atomic-mass-via-rho-k.witness.json)). Retired Form A: Witness: [`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json). LO footnote: Witness: [`atomic-mass-via-rho-k.witness.json`](../../../computations/atomic-mass-via-rho-k.witness.json). See `certificate-to-mass.witness.json` for validation." },
    {
      kind: "status",
      date: "2026-11-20",
      body:
        "Owner ruling 2026-11-20 (D1 = A, PR #8586): the SCORED $\\mathfrak{Q}_\\beta$ on the L2 scorecard is now the $T^3$ weight split of the $z_D$ trace on the gamma-gamma + reading-3 base $V^3 = (\\sigma_0\\sigma_1^{-1})^3$, " +
        "$|\\varepsilon_{\\mathrm{flavour}}(V^3)|\\,E_0 = 0.325433929$ MeV ($-58.402\\%$; tower $E_0$, proton $q_0$; Lean `QOU.QBeta.FlavourWeightSplit`). " +
        "The $\\Delta_S$ value 0.4491 MeV in this block is kept as a labelled UNSCORED history cell, as is the nuc11_interleaved cell (0.6519 MeV) the scorecard carried until this date. " +
        "D2 (same day): that number is $\\mathfrak{Q}_\\beta$, not $m_n - m_p$; under it $m_n - m_p = 0.8364$ MeV ($-35.3\\%$). The sign of the mass ordering stays open (bean qou-99qc).",
    },
  ],
});
