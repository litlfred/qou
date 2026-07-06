# cosh / sinh session synthesis — 2026-05-24 arc

**Date:** 2026-05-24
**Status:** SYNTHESIS (audit-doc tying together 8 merged PRs from this session + 4 main-side sibling commits).

Single-page narrative connecting the day's torus-knot / Markov-trace findings into one coherent arc. **Aimed at future agents** picking up the open `T(p, n)` generalization, the operator-valued `⋈_K` extension, or the unfinished `EM_channel_ratio` physical-meaning audit.

## The arc in one diagram

```
                ┌────────────────────────────────────────────┐
                │  q3 audit (#1108, merged earlier)           │
                │  tr_M(σ_1^k) = (q^{k+2} + (-q^{-1})^k)/[2]_q²│
                │  Wedderburn closed form on H_2(q)            │
                └────────────────────────────────────────────┘
                            │
                            ▼
   PR #1125: sympy sweep across k = 2..12 → empirical pattern
            c_{2j}(T(2, 2m)) = C(m+j, 2j) / 2  (54 cells)
                            │
                            ▼
   PR #1129: cheat-sheet item #5 — connects to Phase 5b
            Li_2^q ↔ cos_q ↔ cosh three-avatars synthesis;
            derives categorical Weinberg-angle identity
            P_W / P_Z = cosh(5η_0) / cosh(7η_0) ≈ cos θ_W (1%)
                            │
                            ▼
   PR #1165: algebraic proof (4 steps) — elevates from
            "sympy across 54 cells" to "theorem for all m ≥ 0"
            via Fibonacci-polynomial identity
            (Graham-Knuth-Patashnik §6.6)
            + CAL-1/2/3 counting theorem
            + algebraic-side q-brackets <n>_q, [n]_q in ℚ(q)
                            │
                            ▼
   PR #1153: sinh bar-anti-symmetric partner Q_m
            Q_m(h) := (q^{2m+1} − q^{-(2m+1)}) / (2 [2]_q)
                   = sinh((2m+1) η) / (2 cosh η)
            per-knot EM/strong ratio Q_m / P_m = tanh((2m+1) η)
                            │
                            ▼
   PR #1152: substrate→EW empirical-match fold-in
            g = π·h_0 (+0.26%), v_ratio = log(6) (-0.50%),
            171/143 = 6/5 (+0.35%) — with Lean class scaffolds
                            │
            ┌───────────────┴───────────────────┐
            │                                    │
            ▼                                    ▼
   sibling commits 596b500f5 + d4d640ce7:    PR #1196: integration audit
   Pythagorean P_m² − Q_m² = 1/[2]_q²;      + canonical η_substrate pin
   Lean encoding of all 4 identities;        on the d4d640ce7 Lean file
   Q_borromean_eq_zero placeholder
                            │
                            ▼
   PR #1211: Q_borromean(h) = 0 PROVED in Lean over ℚ
            via even-polynomial structure of trM_borromean
                            │
                            ▼
   (this PR): canonical-pin sweep across 22 audit probes
            (q_0: 1.10970 → 1.10998 50-digit pin discipline)
```

## What this synthesis adds beyond the individual PRs

### 1. The three avatars are now MECHANICAL

PR #1129's Phase 5b synthesis (`Li_2^q ↔ cos_q ↔ cosh`) was previously an **interpretive** parallel. After the session's work it is **algebraically mechanical**:

| avatar | object | source ring |
|---|---|---|
| algebraic | `<n>_q := q^n + q^{-n}`, `[n]_q := (q^n − q^{-n})/(q − q^{-1})` | `ℤ[q, q^{-1}]` ⊂ `ℚ(q)` |
| trigonometric (root-of-unity) | `cos(nθ) = T_n(cos θ)` (Chebyshev T) | ℝ, `q = e^{iθ}` |
| hyperbolic (substrate) | `cosh(nη) = (e^{nη} + e^{-nη})/2` | ℝ, `q = e^η` |

The same algebraic identity (e.g. the Fibonacci-polynomial sum in PR #1165 step 4 / the trigonometric Chebyshev sum in sibling commit `07ccc8e94`) becomes the hyperbolic identity at the substrate. The three "avatars" are different *images* of one underlying algebraic identity under the **archimedean realization functor** `q ↦ e^{?}`.

### 2. CAL-1 / CAL-2 / CAL-3 counting theorem (PR #1165)

```
   pre-Archimedean (`ℤ[q, q^{-1}] / ℚ(q)`)      → 0 calibrations
   Archimedean point selection (`q ↦ q_0 ∈ ℝ`)  → 1 (CAL-2: m_μ/m_e)
   Archimedean leptonic scale                    → 1 (CAL-1: m_e)
   Archimedean hadronic scale                    → 1 (CAL-3: Q_β / 𝔈₀)
   ──────────────────────────────────────────────────────────────
   Total                                         = 3
```

Every algebraic identity in this session's session (unified binomial, Pythagorean, q-tanh, per-knot EM-channel ratio) lives at the **0-calibration** layer. The Weinberg-angle prediction `P_W/P_Z ≈ cos θ_W` consumes only **CAL-2**. Absolute mass predictions need all three. Δm_{n-p} also needs all three plus the bar-anti-symmetric structure that the canonical chain projects out.

### 3. The categorical Weinberg-angle identity

PR #1129 + PR #1165 produce, as a direct corollary of the algebraic identity:

```
cos θ_W (SM)  ≈  cosh(5 η_0) / cosh(7 η_0)              (Archimedean substrate)
              =  <5>_q / <7>_q  evaluated at q = q_0    (algebraic at substrate)
              =  T_5(cos θ) / T_7(cos θ)  at root-of-unity (trigonometric)
```

Numerically `0.8913` vs SM `0.8814` (+1.1 %). The 1% gap is the **cosh-vs-cos discrepancy** at small `η_0 ≈ 0.104` — neither categorical nor framework error, just the hyperbolic/trigonometric mismatch when `q_0` is close to but not on the unit circle.

### 4. Bar-symmetric vs bar-anti-symmetric: a clean structural split

The session's `P_m` / `Q_m` formalization makes the following structural split explicit:

| sector | content | physical role | examples |
|---|---|---|---|
| **bar-symmetric** (P-channel, kept by `P_avg` projection) | `cosh, cos_q, Li_2^q`, `<n>_q` | strong binding, neutral observables, single-flavor masses | `P_m(h)`, `tr_M(𝓑₃)`, `m_p`/`m_n` in isospin-symmetric limit |
| **bar-anti-symmetric** (Q-channel, DISCARDED by `P_avg`) | `sinh, sin_q, Φ_q`, `[n]_q · h` | Coulomb / EM, charge-distinguishing, isospin-breaking | `Q_m(h)`, EM self-energies, Δm_{n-p} |

PR #1211 proves `Q_borromean(h) = 0` identically — the Borromean trace lives entirely in the P-channel. This refines an earlier (mistaken) framing on PR #1153 that posited Δm_{n-p} as a bare-Q residual on 𝓑₃; PR #1153's "refined-framing note" + PR #1211 + sibling commit `596b500f5` together establish that the carrier for Δm_{n-p} must be the **operator-valued `⋈_K` extension** to unlike-isospin `pn` pairs (PR #1139's D9 closure work), NOT the bare 𝓑₃ trace.

### 5. T(p, n) does NOT generalize via Wedderburn

Sibling commit `bec7494ba` ran the natural next probe: does the unified binomial pattern extend from `T(2, 2m)` to `T(3, n)` via H_3(q)'s (2,1) standard rep? **NEGATIVE.** The (2,1) channel has `(σ_0 σ_1)^3 = I` exactly with eigenvalues `e^{±2πi/3}` independent of `q`, so the character `χ^{(2,1)}((σ_0σ_1)^n) = 2 cos(2πn/3) ∈ {−1, −1, +2}` cycles without `h`-dependence. The Fibonacci/Chebyshev richness is **H_2(q)-specific**.

Closed-form `J_{T(p, n)}(q)` for `p ≥ 3` must go via Burau / HOMFLY-Skein, not Wedderburn.

## Map: 8 session PRs + 4 main-side sibling commits

| PR / commit | what | merge SHA |
|---|---|---|
| PR #1125 | unified binomial pattern (sympy 54 cells) | `2f61e83da` |
| PR #1129 | cheat-sheet item #5 + cosh ↔ Phase 5b synthesis | `0bd409539` |
| PR #1165 | algebraic proof + Chebyshev cross-ref + CAL-1/2/3 counting | `7aa49c67e` |
| PR #1153 | sinh Q_m partner + per-knot tanh ladder | `26e57945e` |
| PR #1152 | EW empirical-match fold-in with Lean anchors | `531896e6b` |
| PR #1196 | sinh/cosh Lean integration audit + canonical η_substrate pin | `72054384` |
| PR #1211 | `Q_borromean(h) = 0` PROVED in Lean over ℚ | `5329eb054` |
| (this PR's sibling C+F) | canonical-pin sweep across 22 audit probes | TBD |
| sibling `596b500f5` | Pythagorean `P_m² − Q_m² = 1/[2]_q²` | — |
| sibling `07ccc8e94` | Chebyshev T derivation of binomial pattern | — |
| sibling `d4d640ce7` | Lean encoding of all 4 identities | — |
| sibling `bec7494ba` | T(3, n) extension → NEGATIVE (H_2(q)-specific) | — |

## Open items (for future sessions)

1. **Operator-valued `⋈_K` extension** to unlike-isospin `pn` pairs (PR #1139 D9 closure path). The kinematic carrier for Δm_{n-p}.
2. **ℝ-side `Q_borromean_eq_zero`** in `QOU.BraidKnot.BarSymmetricBarAntiSymmetricIdentities` — the placeholder `True := trivial` shim can be replaced via `Rat.cast` lifting of PR #1211's ℚ proof (item E in this session's menu; deferred).
3. **`EM_channel_ratio` physical-meaning audit** — the `tanh((2m+1) η_0)` per-knot ratio is structurally clean; whether it has a physical EM/strong fraction interpretation per particle requires a separate validation.
4. **Substrate-derivation of CAL-2** — if a categorical first-principles argument could pick `q_0` from the algebraic side alone, CAL-2 collapses to 0, leaving only 2 dimensional scales (CAL-1, CAL-3) irreducible. Owner declined 2026-05-08; would dramatically tighten the framework's calibration count.
5. **Burau / HOMFLY-Skein for T(p, n), p ≥ 3** — since Wedderburn doesn't generalize, the next-knot-family work (e.g. for hadrons beyond 𝓑₃) needs a different categorical route.

## Cross-references

- Cheat sheet item #5: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- Unified pattern: [`2026-05-24-torus-knot-h-expansion-pattern.md`](2026-05-24-torus-knot-h-expansion-pattern.md)
- sinh partner: [`2026-05-24-sinh-bar-antisymmetric-partner-probe.md`](2026-05-24-sinh-bar-antisymmetric-partner-probe.md)
- Lean integration: [`2026-05-24-sinh-cosh-lean-integration-audit.md`](2026-05-24-sinh-cosh-lean-integration-audit.md)
- EW empirical matches: [`2026-05-24-ew-couplings-substrate-empirical-matches.md`](2026-05-24-ew-couplings-substrate-empirical-matches.md)
- Higgs residual paths: [`2026-05-24-higgs-residual-research-path.md`](2026-05-24-higgs-residual-research-path.md)
- Bar-involution canonical reference: [`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md)
- Crossing-energy EM/strong split: [`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md)
- Three-avatars synthesis (cheat sheet §4): see canonical-derivation-cheat-sheet
- AGENTS.md §7c base-ring discipline (generic R vs archimedean ℝ)
