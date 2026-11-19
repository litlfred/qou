import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qbeta-ck-truncation-canonical",
  title:
    "Canonical closed form for the $\\mathfrak{Q}_\\beta$ truncation coefficients $c_k$ ($k\\geq 3$): only $c_2=-1$ is structural; $c_3=-2=J_{\\mathrm{Hopf}}(q{=}1)$ is a near-match; $c_{k\\geq 3}$ are cal-anchored (open)",
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
        "**RESOLVED — the `2.98%` above is stale, and the `3.47%` is not.** " +
        "(a) `cross-anchor 2.98%` was computed against a SUPERSEDED muon `c_3 = −2.0097` " +
        "(pre-#1422). Today's muon extraction is `−2.02020024`, giving a cross-anchor swing of " +
        "**2.3748%** proton-normalised (2.4571% normalised by the candidate −2). The corpus's " +
        "`2.88%` is the SAME stale gap under the other normalisation — one gap, not two " +
        "measurements. (b) The `3.47%` is correct and must NOT be changed: it is `|−2 − c_3|/2`, " +
        "and the ladder witness's `err_pct` reports `3.3509%` for the same gap normalised by the " +
        "extracted `c_3`. (c) The `0.49%` muon figure is likewise against the superseded value; " +
        "the current muon gap is `1.0100%`. " +
        "**The NEAR-MATCH verdict is unchanged** — 2.3748% is smaller than 2.98% but still vast " +
        "beside the 10⁻⁵⁰ compute precision. Scope-(a) correction to the evidence, no tier moves. " +
        "Measured in `computations/qbeta/qbeta_c3_crossanchor_swing_provenance_probe.py` (3/3).",
      see: "computations/qbeta/qbeta-c3-crossanchor-swing-provenance.witness.json",
    },
    {
      kind: "note",
      date: "2026-08-31",
      body:
        "**The 2026-08-16 note above is itself now on a superseded anchor, and every " +
        "percentage in this block is anchor-dependent.** `fca08de7d2` (2026-08-22, owner " +
        "ruling) moved the muon pin to CODATA 2022. There is no single muon `c_3`: the " +
        "extractor returns `−2.02018813` at the frozen pin, `−2.02020024` at CODATA-2018 " +
        "and `−2.01986031` at CODATA-2022 — a *fourth*-significant-figure spread, because " +
        "the extraction divides by `u³ ≈ 6.2e-7` and so amplifies a relative move in `q` by " +
        "≈2.1e6. Restated at the live pin: cross-anchor swing **2.3912%** proton-normalised " +
        "(**2.4741%** normalised by −2), muon gap **0.9930%**, proton gap 3.4671% (unchanged " +
        "— `m_p/m_e` moved 2e-12 relative between editions against the muon ratio's 1.5e-9, " +
        "which is why only the muon arm ever broke). " +
        "**And the honest error bar, which nothing here had:** propagated through the CAL " +
        "inputs at their CODATA-2022 published uncertainties, `c_3(muon) = −2.0199 ± 1.26`, " +
        "dominated by `Q_β` alone (0.78 ppm × 1/u³). Nine significant figures are quoted for " +
        "a quantity the calibration inputs support to **0.2** of one. What IS experimentally " +
        "resolved is the cross-anchor *swing*: `Q_β` and `m_e` are common mode and cancel in " +
        "the difference, leaving −0.0494823 ± 0.0052, **9.5σ** — the same 9.5σ as the μ–p " +
        "tension, because it is the same statement. **The NEAR-MATCH verdict is unchanged and " +
        "now rests on the quantity that carries the significance**; the absolute `c_3` " +
        "digits do not. Scope-(a); no tier moves, no `c_k` wired.",
      see:
        "computations/qbeta/qbeta-c3-muon-anchor-codata-edition-attribution.witness.json",
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
    {
      kind: "note",
      date: "2026-09-14",
      body:
        "Provenance for the **Convention frame** section added to the `.md`. The " +
        "excision of Markov convention C in favour of D (z = q³/(q²+1)) is the owner " +
        "ruling of 2026-08-15. The C→D re-extraction figures quoted there " +
        "(implied c₂ −1.0176 → −9.2989; c₃ −2.0693 → −974.43; distance to −Vol(4₁) " +
        "972.402; swing ratio 1.00522) are measured at 60 dps on the proton pin and " +
        "come from `qbeta-c3-ladder-trace-convention-sensitivity.witness.json` " +
        "(10/10 PASS). The one-rung localisation of the convention (the N=1 " +
        "eigenphase α = (z−1)h/2) is recorded in " +
        "`docs/audits/2026-09-13-d2-convention-enters-at-one-rung.md`; " +
        "`QOU.QBeta.decayLadder_zC_threeRow_ne_zero` establishes that naive substitution of " +
        "`z_D` into the C-frame expressions fails; the " +
        "re-derivation is bean `qou-cds1`, blocked on `qou-pdix`.",
      see:
        "computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json",
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
