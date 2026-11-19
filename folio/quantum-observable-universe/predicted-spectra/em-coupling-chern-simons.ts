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
  authorNotes: [
    {
      kind: "note",
      body: "Superseded figures, recorded so the change is legible: this paragraph read $137.035944$ / $399$ ppb against CODATA-2018, which is the order-$\\delta_{CS}^2$ truncation at the muon pin. Resummation accounts for $11.06$ ppb of the difference and the pin change for $79.17$ ppb; each is invariant across the other. Reproduce with [`alpha_em_form_comparison_probe.py`](computations/alpha/alpha_em_form_comparison_probe.py).",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization provenance moved from prose: `em-coupling-chern-simons.lean` carried the sketched Gram-determinant value $\\kappa \\approx 1.722$ as `sorry`; congruence invariance of the determinant ratio under invertible basis change $B$ is formalized in `QOU.Archimedean.gramDetRatio_congr_invariant`.",
    },
  ],
});
