# sinh/cosh Lean integration audit + canonical-pin fix

**Date:** 2026-05-24
**Branch:** `claude/sinh-cosh-lean-integration-audit-2026-05-24`
**Status:** AUDIT (documents the Lean infrastructure landed on `main` from sibling commit `d4d640ce7`; one small canonical-pin fix applied).

## Headline

Sibling commit `d4d640ce7` ("lean+audit: items 1-4 — Pythagorean/tanh ladder Lean + Higgs residual audit") added a new Lean file [`QOU.BraidKnot.BarSymmetricBarAntiSymmetricIdentities`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BarSymmetricBarAntiSymmetricIdentities.lean) that formalizes the bar-symmetric / bar-anti-symmetric structure from this session's three merged PRs (`#1153`, `#1165`, `#1152`). This audit:

1. Documents what landed and its provenance trail.
2. Identifies the remaining gaps the sibling explicitly deferred.
3. Applies one trivial fix: switch the `η_substrate` from the rounded q_0 = 1.10970 to the canonical 50-digit pin from `qou_substrate.constants.Q_50_DIGIT_STR`, consistent with PR #1153's discipline.

## Lean infrastructure landed (commit `d4d640ce7`)

| Lean declaration | what it formalizes | provenance |
|---|---|---|
| `P_m (m : ℕ) (η : ℝ) := Real.cosh ((2m+1) η) / (2 Real.cosh η)` | bar-symmetric trace polynomial | PR #1129 + PR #1165 (Archimedean realization) |
| `Q_m (m : ℕ) (η : ℝ) := Real.sinh ((2m+1) η) / (2 Real.cosh η)` | bar-anti-symmetric trace polynomial | **PR #1153** (Q_m definition) |
| `bracket_2_q (η : ℝ) := 2 Real.cosh η` | `[2]_q = q + q^{-1}` at substrate | standard |
| `pythagorean_identity` | `P_m² − Q_m² = 1/(2 cosh η)²` | sibling main commit `596b500f5` (Pythagorean derivation) |
| `Q_over_P_eq_tanh` | `Q_m / P_m = tanh((2m+1) η)` | PR #1153 (per-knot EM/strong ratio) |
| `P_plus_Q` | `P_m + Q_m = exp((2m+1) η) / (2 cosh η)` | sibling commit `596b500f5` |
| `P_minus_Q` | `P_m − Q_m = exp(-(2m+1) η) / (2 cosh η)` | sibling commit `596b500f5` |
| `EM_channel_ratio (m : ℕ) := tanh((2m+1) · η_substrate)` | per-particle EM/strong fraction | PR #1153 (cited explicitly in docstring) |
| `EM_channel_ratio_pos` | `EM_channel_ratio m > 0` for `η_substrate > 0` | sibling derivation |
| `EM_channel_ratio_monotone` | `m < m' ⇒ EM_channel_ratio m < EM_channel_ratio m'` | sibling derivation (via `Real.tanh_lt_tanh + nlinarith`) |
| `Q_borromean_eq_zero : True := trivial` | placeholder for `Q_𝓑₃ = 0` | placeholder; full statement deferred |

This is the **Archimedean image** of the algebraic-side identities (which live in `ℚ(q)` per PR #1165 §"Algebraic-side identities"). The Lean formalization implicitly works at the Archimedean realization `q = e^η`; a future pre-Archimedean (over `[CommRing R]` per AGENTS.md §7c) version would carry the `<n>_q` and `[n]_q` q-brackets as Lean functions returning values in a generic ring.

## What this PR fixes

**Canonical `η_substrate` pin.** The sibling's file defined

```lean
noncomputable def η_substrate : ℝ := Real.log 1.10970000000
```

using the rounded q_0 = `1.10970000000` (10 digits). PR #1153 established that the canonical pin is `qou_substrate.constants.Q_50_DIGIT_STR = 1.10997859555418057528159407960950937799328227995870` (50 digits, derived from CODATA m_μ/m_e + SnapPy Vol(4_1)). This audit applies the same canonical-pin discipline to the Lean file:

```lean
noncomputable def η_substrate : ℝ := Real.log 1.10997859555418057528159407960950937799328227995870
```

The numerical impact is in the 5th decimal (1.10970 vs 1.10998). The `EM_channel_ratio` empirical-value docstring also updates accordingly:

| particle | m | docstring (before) | docstring (after, canonical pin) |
|---|---:|---:|---:|
| W (m=2) | 2 | 0.4780 | 0.4790 |
| Z (m=3) | 3 | 0.6222 | 0.6233 |
| H (m=4) | 4 | 0.7337 | 0.7348 |

All proofs in the file are unaffected: every theorem in `BarSymmetricBarAntiSymmetricIdentities` is stated in terms of the **abstract** `η : ℝ` parameter or uses `η_substrate` only via positivity (`Real.log 1.10998... > 0`, still true), so swapping the literal value preserves the proof skeleton.

## What this PR does NOT fix (deferred items the sibling acknowledges)

The sibling commit's own "What's still open" section enumerates:

| item | status | path forward |
|---|---|---|
| `Q_borromean_eq_zero : True := trivial` | placeholder | full statement requires `import BorromeanMarkovTrace` + showing the closed form's odd-h coefficient vanishes. Sympy verification exists (PR #1081); Lean-side proof needs the Borromean closed form to be in the same module / library. ~1-2 hour task once import chain set up. |
| PR #1165 docstring update in `HiggsCategoricalMassFormula.lean` | deferred small-docstring | landed in `e46289356` (sibling follow-up). Closed. |
| Higgs residual ~0.5% | research-grade open | 4 paths identified in [`2026-05-24-higgs-residual-research-path.md`](2026-05-24-higgs-residual-research-path.md) — out of scope for any single PR. |
| Per-particle EM-channel physical-meaning audit | "PR #1153 claim needs physical-meaning audit" | the PR #1153 framing was refined in commit `f54bbf80d` (now main) to acknowledge `Q_Borromean = 0` falsifies the bare-Q hypothesis on 𝓑₃ — the carrier for `Δm_{n-p}` is the operator-valued ⋈_K extension, not the bare 𝓑₃ trace. The Lean docstring's empirical-claim language ("These are claimed to be EM-channel/total ratios per particle") should reflect this refinement; not changed in this PR. |

The `Q_borromean_eq_zero` proper proof is the biggest open item; this audit explicitly identifies it as the next concrete Lean-formalization task.

## Status integration map

```
                ┌─────────────────────────────────────────────────────────┐
                │  PR #1125 (unified binomial pattern, sympy 54 cells)    │
                │  ↓ merged 2026-05-24, commit 2f61e83da                   │
                └─────────────────────────────────────────────────────────┘
                            │
   PR #1129 cheat-sheet integration  →  merged 0bd409539
   PR #1165 algebraic proof          →  merged 7aa49c67e (this session)
   PR #1153 sinh partner Q_m         →  merged 26e57945e (this session)
   PR #1152 EW hypothesis fold-in    →  merged 531896e6b (this session)
                            │
   Sibling commit 596b500f5 (Pythagorean) builds on PR #1153  ────────────┐
   Sibling commit 07ccc8e94 (Chebyshev T) parallel to PR #1165 ──────────┤
   Sibling commit d4d640ce7 (Lean encoding) formalizes all of above  ────┤
   Sibling commit e46289356 (PR #1165 docstring + Borromean (2,1) probe) ┘
                            │
                            ▼
   This PR: audit + canonical-pin fix for the Lean encoding
```

## Files

- [`docs/audits/2026-05-24-sinh-cosh-lean-integration-audit.md`](2026-05-24-sinh-cosh-lean-integration-audit.md) — this audit
- [`content/quantum-observable-universe/lean/QOU/BraidKnot/BarSymmetricBarAntiSymmetricIdentities.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/BarSymmetricBarAntiSymmetricIdentities.lean) — canonical-pin fix (η_substrate uses Q_50_DIGIT_STR)

## Test plan

- [x] No proof signature changes; all proofs in `BarSymmetricBarAntiSymmetricIdentities.lean` use only abstract `η : ℝ` or `η_substrate > 0` (Lean LSP not available locally to verify, but the change is a pure numeric-literal swap inside `Real.log`).
- [x] Docstring empirical values updated to match the canonical-pin substrate (W=0.4790, Z=0.6233, H=0.7348 vs the previous rounded-pin W=0.4780, Z=0.6222, H=0.7337).
- [x] Audit doc cross-references all 4 merged PRs from this session + all 4 sibling main commits + the 1 deferred Borromean proof gap.
