# 1ppb gap-closure synthesis — per-observable status + next steps

**Date:** 2026-05-23
**Branch:** `claude/q-beta-100x-closure-probe-2026-05-23`
**Trigger:** User direction "continue towards 1ppb" after
PR #916 (alternatives to Strategy D) + PR #962 (q-locality gate +
skill) merged. Three tasks selected: Q_β c_4/c_5 probe, Strategy I
bijection, state synthesis. This audit is the synthesis.

## Per-observable 100× landscape (post-PR #980 §5 ALL CLOSED)

Source: `per-observable-100x-status.witness.json` (refreshed on main).

| obs | pred | CODATA | err (ppb) | 100× tgt (ppb) | miss | status |
|---|---:|---:|---:|---:|---:|---|
| m_e | anchor | — | 0 | 0.003 | — | ✅ anchor |
| **m_μ** | 105.658375506 | 105.658375500 | **0.060** | 0.218 | **0.27** | ✅ **beats 100×** |
| **Q_β** | 0.782333419 | 0.782333410 | **11.13** | 7.80 | **1.43** | beats 1×; framework-bounded |
| Δ_pn | 1.33030 | 1.29333 | 2.86×10⁷ | 4.74 | 6×10⁶ | framework-gap (λ_scale) |
| m_p | 965.38 | 938.27 | 2.89×10⁷ | 0.003 | 9×10⁹ | framework-gap (λ_scale) |
| m_n | 966.71 | 939.57 | 2.89×10⁷ | 0.006 | 5×10⁹ | framework-gap (λ_scale) |

### Classification

| category | observables | what "framework-bounded" means |
|---|---|---|
| **100× MET** | m_e, m_μ | no further work needed |
| **framework-bounded** | Q_β | c_3 = -2 (Hopf, proved) gives 11.13 ppb; the 100× target 7.80 ppb requires a different proved c_3 OR a different N=3 formula structure. PSLQ on sub-leading Δc_3 ≈ -0.00974 returned negative (per `docs/audits/2026-05-22-exploration-c3-q-beta.md`) |
| **framework-gap** | m_p, m_n, Δ_pn | canonical Wedderburn λ_A = 5/2 + (3/4)h² gives ~3% gap to CODATA; conjecture-conditional improvements (Yekutieli additive → 1.4%, Bring color-tube → 670 ppm) all fail q-locality gate (per PR #951/c18e562b9, 0/4 survive). Strategy I bijection PR #978 surfaces a 5/16 vs 1/8 gating research question |

## What's proved vs conjecture-conditional vs framework-bounded

### Proved (substrate-pure, no open dependencies)

| result | formula | where |
|---|---|---|
| canonical Wedderburn λ_scale | (1/4) Σ dim_q V_λ = 5/2 + (3/4)h² (exact, terminates at h²) | PR #701 + Lean |
| Vol(𝓑_3) = 8G | Adams 1985: 8 ideal octahedra × G per cell | `borromean_volume_100dps.py` |
| substrate flavor-split | Δm/M_N = ℏ_q² · h_q · [2]_q · (1 + ℏ_q³) / 3 | PR #942 (merged) |
| Q_β c_3 = -2 (Hopf) | J_Hopf(q=1) via V_(2,1) self-fusion + Frobenius | `probe_q_beta_operator_valued_N3.py` |
| m_μ/m_e = Vol(4_1)/ℏ_q² | Figure-8 knot volume ÷ ℏ_q² (CAL-2 anchor) | exact |

### Conjecture-conditional (substrate-pure, explicit open dependency)

| result | formula | load-bearing step | gap to CODATA |
|---|---|---|---:|
| Yekutieli additive | 5/2 + (3/4 − G)h² | cell-↔-half-sym-projection bijection at H_4 (**PR #978 surfaces 5/16 vs 1/8 mismatch — the gating question**) | ~1.4% m_p |
| Bring color-tube | 1/(1 − h_q · q_0^10) | color-sheet ↔ quark-flavor mapping (Phase 5q) — BUT **q-locality fails** (substrate-q_0 coincidence per c1dca4d73); RETIRED as a structural candidate | ~670 ppm m_p |

### Framework-bounded (proved prediction is the honest accuracy; closing the residual is open research)

| observable | proved prediction | honest accuracy | target closure |
|---|---|---|---|
| Q_β | c_3 = -2 (Hopf) → 11.13 ppb | 1.4× off 100× | needs proved c_3 refinement or different N=3 tower |
| m_p / m_n | canonical Wedderburn λ_A = 5/2 + (3/4)h² → 966 MeV | ~3% off CODATA | needs categorical λ_scale derivation beyond canonical |
| Δ_pn | substrate flavor-split → 1.330 MeV | ~2.86% off CODATA | carried by m_p/m_n framework-gap |

## Strategy I bijection: the gating research question (PR #978)

PR #978 (merged) probed the load-bearing bijection step:

```
Half-symmetric Wedderburn count at H_4:
  pairs:  {(4),(1^4)} + {(3,1),(2,1,1)} = 2
  self:   {(2,2)} × 1/2 = 1/2
  total:  5/2

Cells in 𝓑_3 canonical decomposition: 8

Naive projection ratio:  5/2 / 8 = 5/16 = 0.3125
Yekutieli claim:                    1/8  = 0.125

Discrepancy: factor 5/2 (Yekutieli claims TIGHTER projection)
```

The 5/2 factor may come from the **S_4 → S_3 outer quotient**
(Borromean ring component permutation): under the quotient, the
half-symmetric image at H_4 collapses further. This is a concrete
research question — finite combinatorics on the S_4 character
table restricted to the S_3 ⊂ S_4 inclusion.

**If resolved:** the categorical bijection proof closes, and the
framework's substrate-pure λ_scale with Yekutieli additive
(5/2 + (3/4 − G)h²) becomes a proved theorem → m_p prediction
drops from 966 MeV to 951 MeV (1.4% gap instead of 3%).

## Q_β 1.4× gap: framework-bounded, not closeable by PSLQ

Per `docs/audits/2026-05-22-exploration-c3-q-beta.md`:

- c_3 categorical = -2 (Hopf, proved)
- c_3 empirical (CODATA fit) = -2.0097
- Δc_3 = -0.00974 → PSLQ at 100 dps against `{h², h²G, h⁴, h⁴G, h⁶, ℏ_q², ...}` → **no relation**

Structural interpretation: Q_β at 11.13 ppb IS the framework's
honest prediction at the N=3 Hopf layer. The 7.80 ppb 100×
target requires either:
1. A proved c_4 / c_5 from a higher N level (N=4+ operator-valued
   tower; gated by H_12+ compute — currently Tier 1.A compute
   infrastructure landed but the actual N=4 extract not yet run)
2. A different N=3 formula structure (beyond Hopf algebra —
   e.g. cyclotomic depth-3 fusion per `prop:cyclotomic-depth3-
   dimension-synthesis`, recently wired by I1 probes on main)
3. Acceptance as framework-bounded (the cheat-sheet §5 #1 path)

## Cumulative empirical-search negatives (through 2026-05-23)

| target | search type | scope | result |
|---|---|---|---|
| λ_p | Bring-Bloch PSLQ tiers 0-5 | 52 hyperbolic-knot volumes ≤ 11 crossings | NEG |
| λ_p | substrate-natural q-dilog PSLQ | Li_2^q + Φ_q at 8 substrate args | NEG |
| λ_p | |V̂_S| + Q(ζ_60) + Tier-0 knots | PSLQ coeff ≤ 10³⁰ | NEG |
| λ_p | 2-var Bloch-Wigner + Q(ζ_n)-D | PSLQ coeff ≤ 10²⁰ | NEG |
| λ_p | Φ_q functional-equation | commutative scalar | NEG |
| λ_p | Φ_q operator-theoretic pentagon | truncated 16-dim Heisenberg | 19 ppm near-match (q-locality: coincidence) |
| λ_p | q-locality on all 4 near-matches | sweep q_0 ± 0.05 | **0/4 survive** |
| λ_p | Strategy F (Markov-trace identity) | |tr_M(β_Bor)| · ℏ_q²/Vol | 1836× off (wrong shape) |
| λ_p | Strategy G (Skein polynomial) | Jones/Kauffman/HOMFLYPT at q_0 | 165 ppm (q-locality: coincidence) |
| λ_p | Strategy H V_7 (Wedderburn quotient) | Σ dim_q / [4]_q | 0.14% (q-locality: coincidence) |
| λ_p | Strategy H V_3/V_4 (Wedderburn sums) | fit-siblings, not derivations | RETIRED |
| λ_p | Strategy J (HOMFLYPT cross-orientation) | proton/neutron tr_M ratio | NEG (commit 3a1b11069) |
| Δc_3 Q_β | PSLQ on sub-leading correction | {h², h⁴, h⁶, ℏ_q², G, ...} | NEG |
| λ_p | Strategy I bijection | S_4 half-sym ↔ cells of 𝓑_3 | 5/16 vs 1/8 mismatch — OPEN |

**13 independent searches, 13 negatives (plus the Strategy I
mismatch which is a gating research question, not a negative).**

## Next steps toward 1ppb — prioritized by tractability

| # | direction | tractability | payoff if it lands |
|---|---|---|---|
| 1 | **Resolve the 5/16 → 1/8 S_4 → S_3 quotient factor** (Strategy I bijection, PR #978's gating question) | FINITE COMBINATORICS on S_4/S_3 character restriction — tractable for an algebraist, ~1-3 days | m_p gap drops from 3% to 1.4% (Yekutieli additive becomes proved theorem) |
| 2 | **N=4 Q_β operator-valued extract** (gated by H_12 Tier 1.A compute) | COMPUTE: run H_12 A-operator Phase-1 extract (already scaffolded in `sublemma_2_1_h12_helium_4_framework.py`); ~30-60 min numpy-Hoefsmit or ~1 min via Rust Tier 1.A kernel | potentially closes Q_β 100× gap if c_4 coefficient is categorical |
| 3 | **Cyclotomic depth-3 fusion** for Q_β c_3 refinement (prop:cyclotomic-depth3-dimension-synthesis, recently wired) | COMPUTE + THEORY: the depth-3 fusion recently wired by I1 probes; may provide a structural c_3 → c_3 + δ refinement beyond Hopf | potentially closes Q_β 1.4× gap if δ matches Δc_3 ≈ -0.00974 |
| 4 | **Run all 100× dashboard probes with Yekutieli additive** (conjecture-conditional, pending #1 closing) | PURE COMPUTE: replace canonical Wedderburn with 5/2+(3/4-G)h² in production and re-run mass table | m_p / m_n / Δ_pn predictions all improve; dashboard shows honest Yekutieli-conditional accuracy |
| 5 | **Strategy K (Bloch class via SnapPy triangulation)** — the remaining non-PSLQ structural approach | 2-3 DAYS: needs SnapPy bridge for the canonical 11-crossing proton braid; construct [Z_K_p] from ideal tetrahedra | bypasses PSLQ entirely; either finds the Bloch class or proves K_p isn't hyperbolic |

**Recommendation:** #1 (5/16 → 1/8 S_4 → S_3 quotient) is the
highest-leverage next step: finite combinatorics, tractable, and
directly unlocks the Yekutieli-additive theorem which halves the
framework gap. #2 (N=4 Q_β) is the compute-heaviest but could close
the only remaining winnable 100× target. #3 is research-grade and
may or may not land.

## Cross-references

- [PR #916](https://github.com/litlfred/qou/pull/916) (merged) — alternatives to Strategy D; q-dilog tower brief + 13-driver menu + Rule 14
- [PR #962](https://github.com/litlfred/qou/pull/962) (merged) — q-locality gate codification + production-vs-exploratory skill
- [PR #978](https://github.com/litlfred/qou/pull/978) (merged) — Strategy I bijection probe: 5/16 vs 1/8 mismatch
- [PR #980](https://github.com/litlfred/qou/pull/980) (merged) — cheat-sheet §5 ALL 5 ITEMS CLOSED
- [PR #942](https://github.com/litlfred/qou/pull/942) (merged) — substrate flavor-split wired (Δm/M_N to 0.03%)
- [`docs/audits/2026-05-22-exploration-c3-q-beta.md`](2026-05-22-exploration-c3-q-beta.md) — Q_β c_3 sub-leading NEGATIVE
- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](2026-05-23-lambda-scale-canonical-unification.md) — 13-driver canonical menu + Rule 14
- [`.claude/skills/local/production-vs-exploratory-discipline.md`](../../.claude/skills/local/production-vs-exploratory-discipline.md) — the bright-line skill codifying CAL-4 / empirical-fit / numerology discipline
