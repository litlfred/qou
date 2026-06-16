import { remark } from "../../schema/builders";

export default remark({
  label: "rem:calibration-inputs",
  title: "Calibration inputs and predictive content",
  interprets: "def:mass-identity",
  // Earlier versions listed `conj:mass-endomorphism` in `uses[]`,
  // which transitively typed every block citing this remark as
  // downstream of an open conjecture (see
  // `docs/audits/conjecture-cones.md` "Methodology" footnote — case
  // (2) cleanup). The three-calibration discipline does **not**
  // depend on the closed-form mass endomorphism: it only needs the
  // categorical mass framework (`def:mass-identity`,
  // `prop:categorical-mass-markov`), both already provable. The
  // conjectural reference moves to prose only.
  uses: [
    "prop:categorical-mass-markov",
    "def:categorical-action",
  ],
  tags: [
    "calibration",
    "mass",
    "prediction",
    "endomorphism",
    "substrate-parameter",
    "falsifiability",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-05-25",
      body: "**Self-referential pattern in CAL-2.** The line *\"Muon mass: $m_\\mu = m_e \\times \\mathrm{Vol}(4_1)/\\hbar_q^2$ (first prediction, by construction matches calibration input)\"* is structurally tautological: CAL-2 **defines** $q_0$ as the unique real solution of $m_\\mu/m_e = \\mathrm{Vol}(4_1)/\\hbar_q^2$, so the formula matches CODATA by construction (cf. `figure-8-muon-mass-cross-check.lean:42` *\"equality by construction\"*). $\\mathrm{Vol}(4_1) = 2\\Lambda(\\pi/3)$ is genuine cohomology and $m_e(\\text{natural}) = \\mathrm{Li}_2(q^{-2})/\\hbar_q^2$ is a motivic dilog period in $q$, but the substrate $q_0$ itself remains un-derived (declined 2026-05-08; **reopened 2026-05-25**). Full analysis: [`2026-05-25-cal-2-cohomological-vs-calibration-critique.md`](../../../docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md).",
      see: "https://github.com/litlfred/qou/pull/1246",
    },
    {
      kind: "caveat",
      date: "2026-05-25",
      body: "**CAL-3 parallel finding.** Sibling PR #1127 found $\\mathfrak{Q}_\\beta = |\\Delta(\\mathrm{net})| \\cdot \\mathfrak{E}_0$ is **postulated**, not derived from the canonical per-braid mass formula. The pattern of *\"calibration that's actually an open derivation\"* is not unique to CAL-2. Higher-order $\\mathfrak{Q}_\\beta$ rungs are being recast cohomologically as Khovanov-Rozansky strata in [`2026-05-18-qbeta-n5-cohomological-breakdown.md`](../../../docs/audits/2026-05-18-qbeta-n5-cohomological-breakdown.md). See also [`rem:epistemic-status-of-calibrations`](../observations/epistemic-status-of-calibrations.md) for the unified accounting.",
      see: "https://github.com/litlfred/qou/pull/1127",
    },
  ],
});
