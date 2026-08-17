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
        "`c_2 = -1` is STRUCTURAL — the exact u² coefficient of the explicit-factor product " +
        "`∏_{k≥2}(1 + c_k u^k)`, read off the Kashiwara N2 factor's form " +
        "(`qou:QOU.BraidKnot.q_beta_categorical_precision_ladder`); being a constant it is q₀-independent. " +
        "It is NOT 'proved' (the N2 factor is a definition, not a derived object) and 'Taylor-exact' is " +
        "a claim about THAT series — the normalised series has c̃₂ = c₂ − 1/8 = −9/8 (registry §9i). " +
        "`c_3 = -2 = J_Hopf(q=1)` is a NEAR-MATCH " +
        "— it swings 0.49% (muon-pin q₀) → 3.47% (m_p-pin q₀), cross-anchor 2.98%, so it is NOT a " +
        "Taylor coefficient. `c_{k≥3}` are CAL-ANCHORED: extracted from CODATA $\\mathfrak{Q}$_β (circular, q₀-dependent), " +
        "cached for downstream reuse but NOT credited as predictions. This is the single shared root cause of the " +
        "L2 100× misses on $\\mathfrak{Q}$_β (164×), m_n (185×), and Δ_pn (163×) — only c_2 is derived.",
      see:
        "docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md",
    },
    {
      kind: "note",
      date: "2026-08-16",
      body:
        "**Two numbers above need a normalisation label, and one disagrees with the registry — flagged, not \"fixed\".** " +
        "(a) The `3.47%` is `|−2 − c_3| / 2`; the ladder witness's own `err_pct` field reports `3.3509%` for the SAME gap, " +
        "normalised by the extracted `c_3 = −2.06934258` instead. Both are live and correct; neither should be rewritten " +
        "into the other. (b) The `cross-anchor 2.98%` does NOT reproduce: from the registry §9g anchor pair " +
        "(`−2.06934258` proton / `−2.02020024` muon) the swing is `0.0491423`, i.e. **2.3748%** proton-normalised or " +
        "**2.4326%** muon-normalised. This note predates the figures now in §9g, so the discrepancy is most likely a " +
        "pre-re-pin value — but that is NOT verified here, and an earlier guess that a neighbouring percentage was " +
        "\"stale\" turned out to be a normalisation difference instead. Resolve by re-deriving 2.98% from a named " +
        "anchor pair and normalisation before editing it.",
      see: "docs/coordination/ck-dk-canonical-registry.md",
    },
    {
      kind: "caveat",
      date: "2026-05-31",
      body:
        "This block makes the open status **first-class and auditable from the manifest**; it does NOT close the " +
        "conjecture, wire any `c_{k≥3}` rung to production, or add a fit. The permanent resolution is identifying " +
        "the $\\mathfrak{Q}$_β **Habiro element** whose Taylor coefficients ARE the `c_k` (parallel to the α_EM " +
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
