> **⚠ SUPERSEDED 2026-05-30** by [docs/audits/2026-05-30-qbeta-ck-mp-dk-deep-audit.md](2026-05-30-qbeta-ck-mp-dk-deep-audit.md).
>
> This audit was at the WRONG c_3 form. Canonical c_3 = J_Hopf(q=1) − ℏ_q²
> (the q-deformed Hopf invariant from 2026-05-26 b2f9087315), NOT plain
> c_3 = −2. With canonical c_3, the Taylor match is **0.0038%**, not 0.49%.
> Discipline analysis in this audit is correct for what it tested; it tested
> the wrong target.

# Q_β c_k — what's proved vs. empirical (2026-05-30 consolidation)

## TL;DR

| rung | Lean status | empirical Taylor coefficient | Lean-structural value | match | wired to production? |
|------|-------------|------------------------------|------------------------|-------|----------------------|
| **c_2** | **PROVED** (Taylor-exact via Kashiwara N2_factor) | −1.0000004203 | −1 | **4×10⁻⁷** ✓ | **YES** (in Q_N2) |
| c_3 | Lean theorem as knot invariant, NOT as Taylor coefficient | −2.0097 | −2 = J_Hopf(q=1) | 0.49% | **NO** (reverts #1452) |
| c_4 | Lean class field, "0.91% empirical residual" acknowledged | ~−1.144 | −2·b⁴ ≈ −1.13 | 0.91% | NO |
| c_5 | Lean class field, "Kashiwara b² + Hopf-half offset" | ~−1.25 | −(b²+½) | structural-form | NO |
| c_6 | **Lean: "EMPIRICAL FIT — not derived"** | extracted from CODATA | 4·b² | fit | NO |
| c_7 | **Lean: "chosen for pattern aesthetics, not derivation"** | extracted from CODATA | −8 | fit | NO |

**Net production wiring after this consolidation:** Q_β at Q_N2 (k=2, 1247 ppb miss). Honest 4/7 on the dashboard.

## The four interpretations of c_k — definitively resolved

| interpretation | description | status |
|---|---|---|
| **(a) Habiro/Taylor** | c_k ≡ Taylor coefficients of exact Habiro Q_β at q₀, expanded in u = b·ℏ_q² | **the DEFINITION** |
| (b) Lean knot-invariant forms | c_3 = J_Hopf(q=1), c_4 = J·b⁴, etc. — closed forms from substrate knot data | **structural conjectures** about (a) |
| (c) Wedderburn structural | c_2 = −1 (Kashiwara f̃₁²); per-block matrix elements | **structural conjectures** about (a), agreeing with (b) where overlapping |
| (d) "CODATA fits" | c_k chosen to make Q_β(q₀) hit CODATA | **same numbers as (a)** by construction (since exact Habiro Q_β IS Q_β); the discipline question is whether you have an independent structural form (b/c) |

## What Lean actually proves

### `jonesAtOne_hopf_eq_neg_two` (braid-link-types.lean:144)

```lean
theorem jonesAtOne_hopf_eq_neg_two : jonesAtOne Link.hopfLink = -2 := rfl
```

**Proves:** The Hopf-link Jones polynomial evaluated at q=1 equals −2.
**Does NOT prove:** This value equals the c_3 Taylor coefficient of Q_β at q₀.
**Triviality:** `by rfl` — definition unfolds.

### `q_beta_categorical_precision_ladder` (q-beta-categorical-precision-ladder.lean:160)

```lean
theorem q_beta_categorical_precision_ladder (q m_e : ℝ) (hq : 0 < q) :
    Q_beta_categorical q m_e = Q_beta_form_A q m_e * N1_factor * N2_factor * N3_factor * N4_factor * N5_factor
```

**Proves:** A naming convention — `Q_beta_categorical` unfolds to the product of `N_k_factor` definitions. Closed by `ring`.
**Does NOT prove:** That the resulting product equals the exact Habiro Q_β at q₀ beyond k=2.

### `habiro-precision-ladder-equivalence.lean` (lines 22-27, the decisive statement)

```
NOTE: the historical "precision-ladder c_k" are NOT in general the
Taylor coefficients of this exact sum — the genuinely-derived
expansion is low-order only, and the higher c_k used for ppb-level
fits were tuned against experiment.
Only the a_m integrality is claimed here.
```

This is the Lean file *itself rejecting* interpretation (a) ≡ (b) beyond
low orders. The "low orders" verified empirically by this consolidation
are **k=2 only** — c_3 (0.49%) is already outside Taylor precision.

## What's proved at Taylor-coefficient precision

**Just c_2.** The cumulative wiring is:

```
Q_N2 = Q_A · cos(α − bℏ_q²/2) · (1 − b²·ℏ_q⁴)
```

with:

- `Q_A = m_e · |q² − 2q − 1| · (q+1) / (2q³)` — Form A (prop:neutron-qvalue-symbolic)
- `α = (z−1)h/2` — Kashiwara eigenphase (Lean alpha)
- `c_2 = −1` — Kashiwara f̃₁² (Lean N2_factor, empirical match 4×10⁻⁷)

Numerical: Q_N2 = 0.78233438 vs CODATA 0.78233341 → **1247 ppb miss** at the substrate's μ-p tension floor.

## Why c_3 = J_Hopf(q=1) gets retracted from production

**The Lean theorem** `jonesAtOne_hopf_eq_neg_two` is proved. **But its identification with the c_3 Taylor coefficient at q₀ is empirically falsified** (0.49% off). The identification is a *structural conjecture* — exactly the kind the framework rejects when it appears as "c=4.03≠J²=4" in #1367 (0.8% off, retracted), or "(α/π)·m_π²·(1+ℏ_q)" in #1442 (0.46% off, flagged as selection-bias).

Wiring c_3 to production while not wiring c_4 (0.91%, same kind of structural approximation) was an incoherent bar. The strict-discipline coherent choice is to wire neither — only Taylor-exact rungs go to production.

## Dashboard impact

Pre-revert (post-#1452): Q_β at 11 ppb production (Q_N3 with c_3 = −2). 4/7 beat 100×.
Post-revert (this PR): Q_β at 1247 ppb production (Q_N2 only). **4/7 beat 100×** (m_p closed Q_β/m_n/Δ_pn-dependent rows independently via #1422 q₀ re-pin; Q_β/m_n/Δ_pn no longer in the 100× count but all beat 1×).

The honest discipline-consistent dashboard is **4/7**.

## What would close Q_β honestly

1. **Prove c_3 IS the Taylor coefficient.** Currently empirical Taylor c_3 = −2.0097; Lean structural c_3 = −2. The 0.49% gap needs a Lean theorem connecting them (presumably involving the bar involution / Habiro evaluation at q₀, not the q=1 limit). Without that proof, c_3 = J_Hopf is a structural approximation, not a derivation.
2. **Same for c_4, c_5.**
3. **OR derive Q_β all-orders.** The exact Habiro sum terminates at finite M for any braid word (Habiro 2000 Thm 1.1, cited in Lean). For the proton/neutron braids the witnessed bound is M=8. If we can compute the all-orders Habiro Q_β at q₀ symbolically (not Taylor-truncated), the c_k extraction itself becomes lossless.

The author's earlier guidance was right: **c_k are Habiro/Taylor coefficients**. The Lean knot-invariant forms are a separate conjectural identification — empirically true at c_2, false at c_3+. So either Lean proves the identification at c_3 (and we wire it) or it doesn't (and we don't).

## Related audits / PRs

- `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md` — the original "drop integer towers" call (overshot by lumping c_3 with c_4..c_7).
- `docs/audits/2026-05-30-qbeta-ck-interpretation-resolution.md` (PR #1475) — empirical c_2, c_3 extraction that motivates this consolidation.
- PR #1452 (merged) — wired c_3, retracted here.
- This PR — reverts #1452, restores Q_β at Q_N2 with discipline-consistent rationale.

## Maintenance note

If a future agent proves `c_3 = jonesHopfClassicalLimit at q₀ Taylor-coefficient precision` (i.e. closes the 0.49% gap via a Lean theorem, not a numerical near-match), wire Q_N3 back into production at that time and cite the proof. Same for c_4 (0.91%) and c_5. Don't wire structural approximations as derivations.
