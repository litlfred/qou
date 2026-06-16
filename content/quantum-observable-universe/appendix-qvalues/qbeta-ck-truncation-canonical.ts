import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qbeta-ck-truncation-canonical",
  title:
    "Canonical closed form for the $\\mathfrak{Q}_\\beta$ truncation coefficients $c_k$ ($k\\geq 3$): only $c_2=-1$ is proved; $c_3=-2=J_{\\mathrm{Hopf}}(q{=}1)$ is a near-match; $c_{k\\geq 3}$ are cal-anchored (open)",
  lean: {
    ref: "qou:QOU.BraidKnot.QbetaCkTruncationCanonicalClass",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-categorical-precision-ladder",
  ],
  cites: [
    "jones1985",
    "habiro2002",
  ],
  tags: [
    "tier:E",
    "q-beta",
    "precision-ladder",
    "truncation-order",
    "c_k",
    "near-match",
    "cal-anchored",
    "open-problem",
    "conjecture",
    "habiro-element",
    "1ppb-roadmap",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-31",
      body:
        "**Open / cal-anchored.** Tier status (do NOT re-litigate the wire/un-wire flip-flop): " +
        "`c_2 = -1` is PROVED Taylor-exact (`qou:QOU.BraidKnot.q_beta_categorical_precision_ladder`, " +
        "Kashiwara N2 factor, q₀-stable at 10⁻⁵⁰). `c_3 = -2 = J_Hopf(q=1)` is a NEAR-MATCH " +
        "— it swings 0.49% (muon-pin q₀) → 3.47% (m_p-pin q₀), cross-anchor 2.98%, so it is NOT a " +
        "Taylor coefficient. `c_{k≥3}` are CAL-ANCHORED: extracted from CODATA 𝔔_β (circular, q₀-dependent), " +
        "cached for downstream reuse but NOT credited as predictions. This is the single shared root cause of the " +
        "L2 100× misses on 𝔔_β (164×), m_n (185×), and Δ_pn (163×) — only c_2 is derived.",
      see:
        "docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md",
    },
    {
      kind: "caveat",
      date: "2026-05-31",
      body:
        "This block makes the open status **first-class and auditable from the manifest**; it does NOT close the " +
        "conjecture, wire any `c_{k≥3}` rung to production, or add a fit. The permanent resolution is identifying " +
        "the 𝔔_β **Habiro element** whose Taylor coefficients ARE the `c_k` (parallel to the α_EM " +
        "`[2]_q·(1−h²α)` Habiro element, PR #1511); only then do `c_{k≥3}` upgrade from near-match " +
        "to proved.",
      see:
        "computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script:
      "computations/qbeta/qbeta_ck_truncation_order_analysis.py",
    witness: [
      "computations/qbeta/qbeta-ck-truncation-order-analysis.witness.json",
    ],
    status: "experimental",
  },
});
