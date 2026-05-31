import { remark } from "../../schema/builders";

export default remark({
  label: "rem:isospin-mirror-v9-empirical-near-match",
  title:
    "Empirical near-match for the ³H/³He binding-energy mirror difference — exploratory, fitted correction factor",
  interprets: "rem:option-e-isospin-test",
  uses: [
    "rem:option-e-isospin-test",
    "lem:deuteron-binding-energy",
  ],
  tags: [
    "option-e",
    "isospin",
    "mirror",
    "binding-energy",
    "exploratory",
    "near-match",
    "negative-result",
    "overfitting",
    "audit",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-05-31",
      body: "**Exploratory empirical near-match — the $(1+q)/2$ factor is FITTED, not derived.** The cross-isotope bar-symmetric character sum $m_\\pi\\,\\hbar_q\\sum_\\lambda y_\\lambda\\,(\\chi^\\lambda(\\mathcal{B}_T)+\\chi^{\\lambda^\\mathsf{T}}(\\mathcal{B}_{^3\\mathrm{He}}))/2$ reaches the ³H/³He mirror difference to $6.15\\%$; the additional $(1+q)/2$ multiplier that takes it to $0.11\\%$ was obtained as the exact ratio needed to hit the target (`correction_target = diff_target / base_v8`) and then name-matched to a 9-candidate substrate menu. It is **not** traceable to any of the 13 canonical drivers and **does not generalize**: applying the same factor to the absolute binding energies $B(\\mathrm{D},\\mathrm{T},{}^3\\mathrm{He})$ gives $154\\%$ error (worse than $141\\%$ without it). Per the Δ_λ gate (CLAUDE.md) this is recorded as a near-match, NOT promoted to a proposition or a closure claim. Full tiered (proved / near-match / fitted) assessment: `docs/audits/2026-05-31-isospin-mirror-v9-discipline-assessment.md`. Falsification probe: `probe-isospin-mirror-v9-generalization.witness.json`.",
      see: "https://github.com/litlfred/qou/pull/1578",
    },
  ],
});
