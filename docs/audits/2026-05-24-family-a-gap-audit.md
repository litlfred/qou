# Family A gap audit — the +2.89-3.86% systematic offset

**Date:** 2026-05-24
**Trigger:** `2026-05-24-65-isotope-mass-table-audit.md` reports +2.89-3.86% systematic offset across all 65 isotopes. m_p / m_n / Δ_pn miss the 1ppb-100×-experimental target by 6-9 orders of magnitude SOLELY because of this gap. This audit diagnoses the cause and identifies the canonical closure path.

**TL;DR:** The gap is the algebra-vs-geometry skip in the production mass formula. Family A's algebraic `λ_scale = 5/2 + (3/4)·h²` has NOT been mapped through the Geom functor. The canonical-conditional closure is `λ_scale = 5/2 - G·h²` (Geom-mapped), which the empirical probe `lambda-scale-rd1-geometric` confirms closes m_p to **~14 ppm residual** — a 2000× improvement over the current +2.89% gap. **Wiring is gated on whether `prop:geom-universality`'s conditional conjectures are accepted as canonical-derivation discipline allows.**

## §1. Empirical diagnosis (from the existing probe)

`lambda-scale-rd1-geometric.witness.json`:

| Quantity | Value | Meaning |
|----------|------:|---------|
| `pi_alg_at_q0` | 2.5328 | Family A's `λ_A(q₀) = 5/2 + (3/4)·h²(q₀)` |
| `lambda_p_target` | 2.4600 | What λ needs to be for m_p closure |
| Gap (algebraic − target) | 0.0728 | Maps to **+2.89%** when propagated via `m_p = m_e · Vol(𝓑₃)/ℏ_q² · λ_scale` |
| `Sigma_geom_implied_h2_coeff` | 1.6663 | The h² coefficient subtraction that closes the gap |
| `Sigma_geom_minus_3_4_minus_G` | **3.16 × 10⁻⁴** | Residual after subtracting `3/4 + G` → near-zero |

The implied closure formula:

$$
\lambda_{\text{scale}}^{\text{geom}} = \tfrac{5}{2} + \bigl(\tfrac{3}{4} - \tfrac{3}{4} - G\bigr)\cdot h^2 = \tfrac{5}{2} - G\cdot h^2
$$

where $G = \mathrm{Catalan}(0.9160)$.

Numerical check at $q_0 \approx 1.1098$, $h \approx 0.2087$, $h^2 \approx 0.0436$:

$$
\lambda_{\text{scale}}^{\text{geom}}(q_0) = 2.5 - 0.9160 \times 0.0436 = 2.4600
$$

— matches `lambda_p_target` to ~10⁻⁴ relative. Propagating to $m_p$: **~5-14 ppm residual** vs. the current **+2.89% gap (28,900 ppm)** — a 2000× improvement.

## §2. Structural diagnosis (from the existing coordination doc)

Per [`docs/coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](../coordination/2026-05-23-algebraic-geometric-observable-consistency.md), the production compute pipeline currently does:

```
ALGEBRAIC:  dim_q V_λ at H_4 → (1/4) Σ dim_q V_λ = 5/2 + (3/4)·h²
                                                        ↑
                                              (algebraic +3/4)
            ──────── SKIPS Geom(K) ────────
OBSERVABLE: m_p = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_canonical_algebraic
                  ↑          ↑                    ↑
                 CAL-1   Geom @ leading      algebraic λ
                         (correct)            (NOT Geom-mapped @ h² order)
```

The Vol(𝓑₃)/ℏ_q² factor IS Geom(𝓑₃) at leading order — correctly applied. But the +3/4 algebraic h²-coefficient inside λ_scale has NOT been passed through Geom. The Yekutieli additive treatment `5/2 + (3/4 - G)·h²` would DOUBLE-COUNT (keeping algebraic +3/4 AND adding geometric -G as if independent). The correct identification per the audit:

$$
\underbrace{+\tfrac{3}{4}}_{\text{algebraic, pre-Geom}} \;\xrightarrow{\;\mathrm{Geom}(K)\;}\; \underbrace{-G}_{\text{geometric, post-Geom}}
$$

— the algebraic +3/4 is **not an independent contribution**; it's the Layer-1 view of what Layer-2 expresses as -G. The closure formula uses only the geometric expression.

## §3. Canonical-derivation status (the gate)

Per user directive (2026-05-24): "WE NEED CANONICALLY DERIVED ONLY... probe is ok, but nothing gets wired into pipeline that isnt".

| Component | Status | Notes |
|-----------|--------|-------|
| Family A algebraic `λ_A = 5/2 + (3/4)·h²` | **PROVED** | `lambda_scale_all_c_i_family_a.py` + Lean (PR #895 / #942); h-series terminates at h² exactly |
| Vol(𝓑₃) = 8·G | **PROVED** | PR #843 fix; Adams 1985 + Λ(π/4) = G/2 |
| `prop:geom-universality` (Geom(K) is the unique Frobenius-Hopf-compatible functional) | **CONDITIONAL** (§3b-cond) | Lean: 0 sorries; proved from class hypotheses. Conditional on `conj:hyperbolic-volume-transcendence` + `rem:baryon-period-ratio` |
| `+3/4 ↦ -G` under Geom (the load-bearing step) | **NOT YET FORMALIZED** | The structural audit identifies the identification, but no Lean theorem yet expresses it. Empirically verified (§1) to 10⁻⁴ residual |
| `prop:geom-yekutieli-alignment` | exists; status TBD | Uses Yekutieli non-abelian Stokes for per-cell curvature integration |

**Wiring readiness assessment:**

The Geom-mapped formula `λ_scale = 5/2 - G·h²` is **conditionally canonical** — proved from the Geom-universality axioms (which are themselves conditional on two conjectures). Per CLAUDE.md §3b-cond, conditional-class theorems CAN be wired into production with explicit conditional banners + Lean class hypotheses + `uses[]` declaring the conjectures.

**The blocker:** the specific identification `+3/4 ↦ -G` (the load-bearing arithmetic step) has not been formalized as a stand-alone theorem. The structural audit doc names it; the empirical probe verifies it; but neither constitutes a proof. **Three options:**

1. **Formalize the identification as `prop:geom-h2-coefficient-identification`** — a new content block + Lean proof showing the Yekutieli per-cell volume integration on 𝓑₃'s 8 ideal octahedra yields exactly `-G` at h² order. Then the Geom-mapped formula is canonical-conditional and wirable.
2. **Treat as a high-confidence conjecture** — open `conj:family-a-geom-mapping`, add a forward-reference banner ("conjectural closure path"), wire as an opt-in `method="canonical_geom"` flag with explicit "conditional" tag in the witness. Production default stays on the algebraic path until #1 lands.
3. **Defer wiring entirely** — keep the algebraic path as production, treat the empirical probe as documenting an open frontier, and route per-isotope predictions through the existing residual reporting (already +3% gap is documented in the 65-isotope audit).

## §4. Recommendation

**Option 2** (conjecture + opt-in flag) is the minimum-discipline path that respects "canonical only in production": no production-path change without the canonical proof landing, but a clear empirical roadmap for the closure becomes a flag-gated path that can validate the formula numerically.

**Option 1** is the principled long-term solution — formalize `prop:geom-h2-coefficient-identification` in a separate research-grade PR (1-3 weeks). When that lands with a §3b-cond conditional-class Lean proof, flip the production default.

**Option 3** is the strictest reading of the directive — the +2.89% gap stays in production until the formalization lands, and the audit documents the open frontier.

**Per the strict reading of "canonically derived only":** Option 3 is the default. Option 2 is acceptable IF the conditional-class tagging is explicit. Option 1 is the only path to closing the gap in production without conditional caveats.

## §5. Action items (queued, not started)

| # | Item | Effort | Gates |
|---|------|--------|-------|
| 5.1 | Add this audit doc to the repo (THIS PR) | done | — |
| 5.2 | Re-run `lambda-scale-rd1-geometric` and `m-p-borromean-verification` with the Geom-mapped formula as a **probe-only** witness (audit-only, no production wiring) | 1 day | none |
| 5.3 | Open `conj:family-a-geom-mapping` content block: states the identification `+3/4 ↦ -G` as a conjecture, cites the empirical probe + structural coordination doc | 2 hr | none — research-grade conjecture |
| 5.4 | Formalize `prop:geom-h2-coefficient-identification` (Yekutieli per-cell integration on 𝓑₃ → -G at h² order) — content + Lean | **1-3 weeks** | needs the categorical-geometry chain worked out; biggest deliverable |
| 5.5 | When 5.4 lands: flip `m-p-borromean-verification-50dps.py` production path to Geom-mapped formula. Regen all 65-isotope witnesses. Verify 1ppb dashboard recovers m_p / m_n / Δ_pn closure | 1 day | gated on 5.4 |
| 5.6 | Regen stale `canonical-mass-table-extended.witness.json` (3 commits behind script: v0.6.0 + Copilot + v0.7.0) — this is independent of 5.5 | 30 min | none |

## §6. Pointers

- [`docs/coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](../coordination/2026-05-23-algebraic-geometric-observable-consistency.md) — the structural audit that diagnosed the gap (this audit's parent)
- [`docs/audits/2026-05-24-65-isotope-mass-table-audit.md`](2026-05-24-65-isotope-mass-table-audit.md) — the empirical observation across 65 isotopes
- [`content/quantum-observable-universe/braids-and-knots/geom-universality.md`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md) — `prop:geom-universality` (conditional, §3b-cond)
- [`folio-assistant/computations/lambda_scale_all_c_i_family_a.py`](../../folio-assistant/computations/lambda_scale_all_c_i_family_a.py) — the canonical Family A proof (the +3/4 source-of-truth)
- [`folio-assistant/computations/lambda-scale-rd1-geometric.witness.json`](../../folio-assistant/computations/lambda-scale-rd1-geometric.witness.json) — the empirical probe (the -G evidence)
- [`folio-assistant/computations/m_p_borromean_verification_50dps.py`](../../folio-assistant/computations/m_p_borromean_verification_50dps.py) — the production m_p formula (currently algebraic Family A; +2.89% gap)
- [`CLAUDE.md §3b-cond`](../../CLAUDE.md) — conditional-class theorem conventions

## §7. Sibling: canonical-discipline paper sweep findings (parallel run)

A parallel canonical-discipline sweep audited all of
`content/quantum-observable-universe/**/*.md` for empirical /
fitting / probing / numerology floating in paper content.

**Verdict: paper is in good shape — 4 actionable items, 0 critical.**

| # | File | Severity | Action |
|---|------|----------|--------|
| 7.1 | `chirality-writhe-ribbon-derivation.md` | MAJOR | Move failed-experiment narrative (H_6 satellite D negative result) OUT of paper into an audit doc. Currently risks misleading readers about derivation status of $a_K$. |
| 7.2 | `lambda-scale-substrate-form.md` | MEDIUM | Refactor: move original "Conjecture (now empirical)" block to a historical footnote; lead with reframed structural constant-C problem. |
| 7.3 | `dressed-quark-numerology-at-q0.md` (filename) | LOW (cosmetic) | Rename → `dressed-quark-mass-at-q0.md`. Content is structurally sound (Skein-corrected + 1/3 flavor-split). |
| 7.4 | `unified-curvature-rank-mass-formula.md` | INFO | "empirically it accounts for ~3% of the binding energy" — add nucleus / term context for clarity. |

Audit docs and coordination docs were skipped per directive (their
experimental content is appropriate to their role).

Class-A opt-out labels, CAL-4 banners, and conditional caveats are
applied consistently throughout the paper. The three-calibration
discipline is broadly enforced.

**Sibling cleanup actions queued for separate small PRs** — not in
scope for this audit's scope (the Family A gap).
