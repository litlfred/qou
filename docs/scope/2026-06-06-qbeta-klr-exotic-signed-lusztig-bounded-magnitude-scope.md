# KLR cont. 9 Option C-exotic (signed Lusztig) — bounded-magnitude structural scope

**Status**: scope doc only (no compute, no probe; the question's specification is itself research-grade). User direction (2026-06-06): the last residual cont. 9 menu option flagged "UNTESTED" by [PR #1924's results doc](2026-06-06-qbeta-klr-composite3-and-lusztig-preflights-results.md) — namely, **exotic signed Demazure-Lusztig variants** of Composite 1 (Whittaker / Lusztig-Yun-Zhu / twisted T_i with sign-changing coefficients). This doc records the structural constraints that already NARROW the escape route, without claiming a full convention-independent refutation.

**Why this is scope rather than RUN**: a preflight RUN requires choosing a specific convention (Whittaker basis? Lusztig-Yun-Zhu? twisted T_i with which T_i normalisation?). No such convention is implemented in this corpus; specifying one is itself a research task. This scope identifies what such a RUN would test.

---

## The residual question

For Composite 1's ansatz `F(u) = Σ_w D_w(λ) · (q;q)_{ℓ(w)} · u^{ℓ(w)}` with some signed Demazure-Lusztig variant `D_w^{exotic}`, can the u² rung produce the proved `c_2 = -1` at both anchors simultaneously?

At u²: `(q;q)_2 · Σ_{ℓ(w)=2} D_w^{exotic}(λ; q₀) = -1`. At q₀ ≈ 1.1097, `(q;q)_2 ≈ +0.0254`. So:

> `Σ_{ℓ(w)=2} D_w^{exotic}(λ; q₀) = -1 / 0.0254 ≈ -39.4`

The exotic variant must produce a **negative sum of magnitude ~39.4 at q₀**, simultaneously matching the slightly different `-1 / (q;q)_2(q₀_muon) ≈ -39.4 + tiny`.

## Three structural narrowings (no compute needed)

### N1. Bounded magnitude at small λ (sl_n with n ≤ 3, ω_1)

For sl_3 / ω_1 / ℓ=2 there are only **2** Demazure characters (`w = s_1 s_2` and `s_2 s_1`). In ANY natural q-monomial convention each `|D_w(q₀)| ≤ 1 + q₀ + q₀² ≈ 3.34`. So even with the worst-case sign-flipping exotic:

> `|Σ_{w} D_w^{exotic}| ≤ 6.7  <<  39.4`

**Refuted at sl_3 / ω_1 / ℓ=2 by magnitude bound** — regardless of sign convention. To survive, exotic variants must use either larger n, higher ω_j, or non-fundamental λ.

### N2. cont. 11's 1281-sweep covers natural larger-λ Demazure atoms

[`qbeta_composite_crossanchor_2factor_sweep.py`](../../computations/qbeta/qbeta_composite_crossanchor_2factor_sweep.py)'s `build_atoms()` includes `Demazure(2,1) = 2·[3]_q` (the S_3 (2,1) partition character) and SYT-major-index `q + q²`. Combined under `{×, ÷, +, −}` over the full atom set (~20 atoms) it generated 1281 2-factor candidates including `D_w_atoms × (q;q)_k`. **All 1281 failed cross-anchor at 1 ppm.**

So any exotic-signed-Lusztig variant that reduces to a signed linear combination of cont. 11's natural atoms × `(q;q)_k` is in the already-exhausted space.

### N3. Cross-anchor rigidity forces the convention to be intrinsic

Even an exotic variant must satisfy both:
- `Σ D_w^{exotic}(λ; q₀_proton) ≈ -39.4` (proton anchor target)
- `Σ D_w^{exotic}(λ; q₀_muon) ≈ -39.4 + Δ_xanc` (muon target, cross-anchor swing)

The fractional cross-anchor swing of `c_2 = -1` is 0 (q-INDEPENDENT proved relation), but `(q;q)_2(q₀_p) ≠ (q;q)_2(q₀_m)` — so the required Σ D_w fractional swing is `-Δ((q;q)_2) / ((q;q)_2)²`. Forcing this swing matches at the parts-per-million level constrains the convention's q-functional form, which is exactly what cont. 11 tested across 1281 atoms.

## Residual genuine-escape (research-grade scope item, not a build tranche)

The only theoretical escape from the combined N1+N2+N3 narrowings is an exotic convention whose Demazure-Lusztig characters are:
- **Signed** (so Σ can be negative);
- **Large-magnitude** at sl_n with n ≥ 4 and ω_j with j ≥ 2 (so |Σ| ≥ 40 achievable);
- **Not** a linear combination of cont. 11's natural categorical atoms (so not in the 1281-saturated space);
- **Cross-anchor-rigid by construction** (so the swing matches without tuning).

Specifying such a convention IS a research project — Lusztig's positivity theorem (1990) and the standard Kazhdan-Lusztig framework do not naturally produce sign-changing canonical bases for type A; Whittaker / Yun-Zhu signed variants exist (Whittaker modules, Iwahori-Whittaker pairings) but are not categorical "Demazure characters" in the Composite-1 sense.

**Recommendation**: cont. 9 Option C-exotic remains formally OPEN as a theoretical-research direction but is **not a 5-7 session build-cost-saving tranche**. The combined N1+N2+N3 narrowings + Lusztig 1990 positivity make it very unlikely a natural categorical convention escapes; if one is later identified, the same preflight pattern (`[u²]F` sign + magnitude check, then cross-anchor rigidity) applies and either refutes it cheaply or authorises a build.

## Updated cont. 9 menu state

| status | option | reinforced by |
|---|---|---|
| ✅ refuted | B / C / C′ / D | 4 preflights (PRs #1914 + #1924) |
| ⚠️ NARROWED (this scope) | C″ exotic signed Lusztig | bounded magnitude (N1) + cont. 11 saturation (N2) + cross-anchor rigidity (N3) |
| 🛑 viable (strongly reinforced) | **A** (CAL-3-anchored permanently) | **3 corpus + 4 preflight + 3 structural narrowings** |

## Cross-refs

- Today's preflight closures: [`2026-06-06-qbeta-klr-composite4-preflight-run-results.md`](2026-06-06-qbeta-klr-composite4-preflight-run-results.md), [`2026-06-06-qbeta-klr-composite1-preflight-run-results.md`](2026-06-06-qbeta-klr-composite1-preflight-run-results.md), [`2026-06-06-qbeta-klr-composite3-and-lusztig-preflights-results.md`](2026-06-06-qbeta-klr-composite3-and-lusztig-preflights-results.md).
- cont. 11 2-factor saturation: [`qbeta_composite_crossanchor_2factor_sweep.py`](../../computations/qbeta/qbeta_composite_crossanchor_2factor_sweep.py).
- Lusztig 1990 (positivity theorem): *Canonical bases arising from quantized enveloping algebras*, JAMS 3.
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) (cont. 18 follow-up).
