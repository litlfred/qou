# Cosh_q / sinh_q correction hypothesis — 16-candidate scan (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (extends claude/hoefsmit-chi-lambda-q-evaluator-2026-06-01, PR #1630)
**Status:** ALL 16 CANDIDATES REFUTED at q_proton (none within 0.7% of empirical).

## TL;DR

User-raised question (2026-06-01): "is the swing/oscillation due to
missing cosh_q / sinh_q?"

Scanned 16 specific q-hyperbolic candidate corrections to the nominal
c_3 = -2 (J_Hopf(q=1)) against empirical c_3 = -2.0693 at q_proton.

**Result: ALL 16 REFUTED.** Closest matches are at ~0.7-0.9% off
empirical (shaving the residual by ~70% but not closing). No clean
candidate at compute precision.

## Candidate scan

| Candidate | Value at q_proton | err vs empirical |
|---|---|---|
| `-[2]_q` | -2.011 | +2.82% |
| `-[2]_q · (1 + ℏ_q²)` | -2.031 | +1.87% |
| `-2 · cosh(h)` | -2.044 | +1.23% |
| `-2 · cosh(h/2)` | -2.011 | +2.82% |
| `-2 · cosh(ℏ_q)` | -2.010 | +2.87% |
| `-2 - sinh(h)` | -2.211 | -6.83% |
| `-2 - sinh(h)·h` | -2.044 | +1.22% |
| `-2 - h · ℏ_q` | -2.021 | +2.35% |
| `-2 - h̃²` | -2.011 | +2.82% |
| `-2 - h²` | -2.044 | +1.24% |
| **`-2 - 2h²`** | **-2.087** | **-0.88%** ← closest |
| **`-2 - h² · [2]_q`** | **-2.088** | **-0.90%** |
| **`-2 · (1 + h²/2 · [2]_q)`** | **-2.088** | **-0.90%** (same form) |
| `-[2]_q - sinh(h)/h` | -3.018 | -45.86% |
| **`-2 · cosh(h)·cosh(ℏ_q)`** | **-2.054** | **+0.74%** ← closest |
| `-[2]_q² / 2` | -2.022 | +2.29% |

## What this tells us

Three closest matches (within 1%):

- `-2 · cosh(h) · cosh(ℏ_q)` at +0.74% — product of two q-deformed cosh's
- `-2 - 2·h²` at -0.88% — simple polynomial correction
- `-2 - h²·[2]_q` at -0.90% — equivalent to `-2·(1 + h²·[2]_q/2)`

**Even the closest match misses by 7000 ppm.** Compute precision is
10⁻⁵⁰; the candidates would need to match to that level to be
Taylor-exact, not at ~7000 ppm. The empirical c_3 deviation of -0.0693
does NOT cleanly factor through any simple cosh_q / sinh_q structure.

## Why this matters

The user's intuition is structurally sensible: the Hecke algebra has
natural cosh_q-like ([2]_q = q + q⁻¹) and sinh_q-like (h = q - q⁻¹)
quantities. If c_3's near-match deviation were a missing q-hyperbolic
correction, ONE of the 16 candidates above should match cleanly. None do.

This is consistent with PR #1626's finding: the empirical c_3 swing
across anchors is NOT structural q-dependence, and the c_3 NEAR-MATCH
itself isn't a simple q-correction either.

## Anti-pattern guard

Per AGENTS.md no-7th-ansatz discipline (carrying over):

- ❌ DO NOT wire any of these candidates because their err is in the
  "interesting" 1% zone. None close at compute precision.
- ❌ DO NOT search for a 5-parameter combination of cosh_q + sinh_q
  + [n]_q + ℏ_q^k that happens to match — that's the 8th-ansatz trap.
- ❌ DO NOT use these as a starting point for "fine-tuned" corrections.

## What this PR does NOT do

- ❌ Does not propose any new c_k candidate (16 refuted with explicit numerical residuals)
- ❌ Does not resolve the c_3 saga
- ❌ Does not modify production wiring

## What it DOES add

A documented exhaustive scan of natural q-hyperbolic candidates with
explicit numerical refutations. Future agents asking "did anyone try
cosh_q / sinh_q?" can cite this audit instead of re-running the scan.

## Files

- `computations/qbeta/qbeta_cosh_q_sinh_q_candidate_scan.py`
- `computations/qbeta/qbeta-cosh-q-sinh-q-candidate-scan.witness.json`

## Cross-refs

- PR #1609 — Li_2^q × spectral candidate (mech #7 refuted)
- PR #1626 — complex c_3 diagnostic (cross-anchor under-diagnostic finding)
- PR #1630 (this PR's first commit) — Li_2^q × spectral cross-anchor completion
- `docs/audits/2026-05-31-qbeta-bridge-narrowing.md` — 7 mechanisms ruled out
