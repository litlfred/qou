import { proposition } from "../../schema/builders";

/**
 * The Borromean baryon λ_scale has an empirical near-form
 *
 *   λ_scale ≈ 5/2 − h² · G + O(h^4)    [acknowledged-CAL-4 as of 2026-05-23]
 *
 * where h = q − q^{-1} is the Hecke deformation and G = Catalan's
 * constant. The form matches CODATA m_p / m_e to 5.6 ppm at q_0 but
 * is NOT a structural identity — see the .md for the full eight-search
 * exhaustion record (Tier 5, PR #923, #928, #941, #943, #951, #957,
 * #969).
 *
 * Decisive refutations (2026-05-23):
 *   - PR #951 q-locality: residual across q ∈ [q_0 ± 0.05] has slope
 *     ~−1.7×10⁷ ppm/q. The match at q_0 is a residual zero-crossing,
 *     not a smooth identity. Per the standing "q_0 not special"
 *     discipline, this disqualifies the form as structural.
 *   - PR #957 reframing: λ_p(q) = (m_p/m_e) · ℏ_q² / (8G) is exactly
 *     a constant times ℏ_q² (where ℏ_q := (q-1)/q, NOT h_q = q-1/q).
 *     The h²·G form uses the wrong q-parametrization by construction.
 *     Structural search target is the constant C ≈ 250.576, not F(q).
 *   - PR #969 Strategy J: tr_M(β_p)/tr_M(β_n) ratios do not predict
 *     m_n/m_p either (0.45% best pure-substrate).
 *
 * The block is RETAINED under its original label for graph stability
 * and historical reference. Readers should interpret λ_scale as
 * "the proton scale empirically pinned by CAL-4, not derived from
 * substrate" — formally an acknowledged-CAL-4 falsifiable prediction
 * per `conj:lambda-scale-bring-bloch-identity`.
 *
 * History:
 *   - 2026-05-18: emerged from a systematic search following PR #683
 *     "investigate close the ~1700× scale gap" direction. Originally
 *     framed as proposing an explicit substrate form with one
 *     structural correction term.
 *   - 2026-05-21 (PR #888): truth-in-naming demoted the literal twin
 *     to LAMBDA_PROTON_FITTED_FROM_CODATA.
 *   - 2026-05-22 (PR #904): block kind demoted from `proposition` to
 *     `conjecture` per §3b conjectural-propagation discipline.
 *   - 2026-05-23 (PR #951/#957/#969): empirical exhaustion + q-locality
 *     refutation + reframing → formal acknowledged-CAL-4 status.
 *
 * NOT used as input to any production compute. The 3-calibration chain
 * (m_e, m_μ/m_e, $\\mathfrak{Q}$_β) is the authoritative path; this block is a
 * historical record of the empirical 5.6 ppm near-form.
 */
export default proposition({
  label: "prop:lambda-scale-substrate-form",
  lean: { ref: "qou:QOU.BraidKnot.lambdaA_qForm_eq_hForm" },
  title:
    "Borromean baryon $\\lambda_{\\text{scale}}$ empirical form $5/2 - h^2 \\cdot G$",
  uses: [
    // conj:borromean-baryon-mass-formula removed (qou-tm3c): the claim is the identity sum of dim_q V_lambda over lambda of 4 = 10 + 3h^2; no mass formula is used.
    "prop:plancherel-weight-boundedness",
  ],
  cites: [
    "adams1985hyperbolic",
    "milnor1982",
  ],
  tags: [
    "mass-formula",
    "borromean",
    "lambda-scale",
    "catalan-constant",
    "h-squared-expansion",
    "conjecture",
    "5.6ppm",
    "acknowledged-cal-4",
    "non-smooth-in-q",
  ],
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "status", date: "2026-05-23", body: "**Status — what is canonical here.** This block records the **proved Family A closed form** for the half-symmetric Wedderburn sum at $H_4(q)$, which is the current production value of `linking_weight(𝓑_3, q)` inside `VolDensity(𝓑_3, q)`. The earlier $\\lambda_{\\mathrm{scale}}$ conjecture ($5/2 - h^2 G$) was **structurally falsified** and the CAL-4 framing **purged**; $\\lambda_{\\mathrm{scale}}$ is no longer a separate object — it was **absorbed into `VolDensity`**. The full falsification history (eight independent structural searches, the Yekutieli/Bring–Bloch dead-ends) is kept in the audit trail, **not in the paper**: `docs/audits/2026-05-18-lambda-scale-derivation-search.md` and the deprecation note on this block. **Do not revive** the $5/2 - h^2 G$ form, the Yekutieli per-cell ADD form, or the Bring–Bloch identity." },
    { kind: "deprecated", date: "2026-05-27", body: "**Status — $\lambda_{\mathrm{scale}}$ ABSORBED INTO `VolDensity`.**  Per [`docs/lambda-scale-absorbed-into-vol-density.md`](../../../docs/lambda-scale-absorbed-into-vol-density.md) (canonical framing, see PR #1080), **`λ_scale` is no longer a separate object** in the framework. The canonical mass formula is  $$m(K) = m_e \cdot \mathrm{VolDensity}(K, q_0)$$  — a single Geom-functor evaluation per knot. What older docs called `λ_scale(K, q)` is the **ratio** $\mathrm{VolDensity}(K, q) / \mathrm{Geom_{leading}}(K, q)$, i.e., what Geom assigns to multi-component links above their bare hyperbolic volume. There is nothing to \"derive from substrate\" — the value is *output* of Geom, not input.  **What remains canonical in this block:** - The Family A theorem $\lambda_A(q) = (1/4) \sum_{\lambda \vdash 4} \dim_q V_\lambda = 5/2 + (3/4) h^2$ IS the current production value of `linking_weight(𝓑_3, q)` inside `VolDensity(𝓑_3, q)`. It is PROVED (Wenzl bridge, PR #895/#942).  **What is OBSOLETE in this block:** - The original substrate-form claim $\lambda_{\mathrm{scale}}^{(u, d)} = 5/2 - h^2 \cdot G + O(h^4)$ was **structurally falsified** 2026-05-18 (PSLQ coincidence; no Wedderburn derivation gives $-G \cdot h^2$). See [`docs/audits/2026-05-18-conjecture-falsification.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-18-conjecture-falsification.md). - The CAL-4 framing ($\lambda_{\mathrm{scale}}$ as a \"4th calibration anchor\") is **purged 2026-05-24** (commit `71d674da1`). The production literal `LAMBDA_PROTON_FITTED_FROM_CODATA` was removed from `m_p_borromean_verification_50dps.py`; production now uses Family A directly. - The \"Bring-Bloch identity\" research direction was closed at PSLQ tier 5 (see [`bring_bloch_tier5_search_m_p.py`](https://github.com/litlfred/qou/blob/main/computations/bring_bloch_tier5_search_m_p.py)). - The Yekutieli per-cell ADD form $5/2 + (3/4 - G) h^2$ was also purged 2026-05-24 as non-canonical (PR #985 bijection NEGATIVE).  **Current research direction**: refine `VolDensity(𝓑_3)`'s categorical exactness at higher $h^2$ orders, NOT derive $\lambda_{\mathrm{scale}}$ from substrate. The +2.89 % gap is a `VolDensity` refinement question; the structural Markov-trace finding (`tr_M(\beta_{\mathrm{Bor}}) = 1 + 0 \cdot h^2 - (3/4)h^4 + \cdots`) brings it to +1.948 % with zero free parameters (see [`computations/probes/vol_density_borromean_h4_probe.py`](https://github.com/litlfred/qou/blob/main/computations/probes/vol_density_borromean_h4_probe.py)).  **Block-conservation rationale**: the label `conj:lambda-scale-substrate-form` is retained for graph-stability across already-cited references; the §Family A theorem section below is canonical-preserving content. Sections covering the falsified / purged forms are kept as **historical record** so future agents see what was tried, why it was rejected, and where to find the post-purge canonical framing. Do not propose reviving the falsified $5/2 - h^2 \cdot G$ form, the Yekutieli ADD form, or the Bring-Bloch identity as production candidates." },
  ],
});
