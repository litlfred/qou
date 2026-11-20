import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
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
  ],
});
