import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-coupling-chern-simons",
  interprets: "prop:em-coupling-projection",
  title:
    "Conjectured Chern-Simons correction form $1/\\alpha = q[9]_q[10]_q\\cdot\\bigl(1+\\delta_{CS}/(1-\\delta_{CS}\\kappa)\\bigr)$ (Gram-determinant $\\kappa$ unproved)",
  lean: {
    ref: "qou:QOU.ArchimedeanUniverse.ChernSimonsCorrectionConjecture",
    validation: "not_checked",
  },
  uses: [
    "prop:em-coupling-projection",
    "prop:quantum-observable-universe-exists",
  ],
  tags: [
    "fine-structure",
    "chern-simons",
    "brings-surface",
    "genus-4",
    "torus-knot",
    "gram-matrix",
    "conjecture",
    "kappa-unproved",
  ],
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/alpha/alpha_em_seifert_kappa_pairing_probe.py",
    witness: [
      "computations/alpha/alpha-em-seifert-kappa-pairing.witness.json",
    ],
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "80-dps homological Seifert pairing probe wired: [`alpha_em_seifert_kappa_pairing_probe.py`](../../../computations/alpha/alpha_em_seifert_kappa_pairing_probe.py) (`alpha-em-seifert-kappa-pairing.witness.json`) constructs the $8\\times 8$ Milnor/Seifert matrices $V_{2,9} = V_2 \\otimes V_9$ and $V_{3,5} = V_3 \\otimes V_5$ on $H_1(\\Sigma_4; \\mathbb{Z}) \\cong \\mathbb{Z}^8$, verifies symbolically $\\kappa_{\\mathrm{Seifert}}(q) = q^{b_1(\\Sigma_4)} / (\\Delta_{T_{2,9}}(q)\\,\\Delta_{T_{3,5}}(q))$, and evaluates $\\kappa_{\\mathrm{Seifert}}(q_p) = 1.9051553282\\ldots$ ($-24.53\\;\\mathrm{ppb}$ resummed vs CODATA-2022) and $\\kappa_{\\mathrm{Seifert}}(q_\\mu) = 1.9051554269\\ldots$ ($+55.16\\;\\mathrm{ppb}$).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Reproduce with [`alpha_em_kappa_qdeformation_family_probe.py`](../../../computations/alpha/alpha_em_kappa_qdeformation_family_probe.py)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (`QOU.Archimedean.gramDetRatio_congr_invariant`; confirmed numerically to $60$ digits under unimodular, index-$2$ and irrational $B$)" },
    {
      kind: "note",
      body: "Superseded figures, recorded so the change is legible: this paragraph read $137.035944$ / $399$ ppb against CODATA-2018, which is the order-$\\delta_{CS}^2$ truncation at the muon pin. Resummation accounts for $11.06$ ppb of the difference and the pin change for $79.17$ ppb; each is invariant across the other. Reproduce with [`alpha_em_form_comparison_probe.py`](computations/alpha/alpha_em_form_comparison_probe.py).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): See [open problems](#rem:alpha-em-derivation-open-problems)." },
  ],
});
