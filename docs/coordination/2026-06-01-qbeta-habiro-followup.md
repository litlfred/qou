# Q_β Habiro follow-up — coordination ledger

**Branch:** `claude/qbeta-habiro-followup-2026-06-01`
**PR:** [#1618](https://github.com/litlfred/qou/pull/1618)
**Goal:** Three follow-up tracks on the Q_β Habiro keystone, after PR #1579 merged the structural findings (cyclotomic strand-doubling Lean lemma, Δa_m factorization with `−u^15·(u−1)(u+1)·P_8`, a_8 partition-function match, Φ_8² categorical interpretation).

## Tracks

1. **Convention-resolution gate** (highest-impact) — Phase 5q re-factorization on (D−n); does Φ_8² survive in the canonical convention?
2. **Lean-formalize a_8 partition identity** (concrete) — `a_8 = Σ p(n)·u^(5−n)` via Mathlib's `Nat.partition`.
3. **Generate canonical Phase 5q ³He/⁴He Habiro coefficients** — unlocks strand-doubling Φ_16/Φ_32 falsifiable predictions test.

## Context from PR #1579

Recent merge (commit `57b5fa2d3a`) consolidated 22 commits with the structural picture:

- Single-nucleon: Φ_4(u) = u²+1 (in p, n denominators)
- Isospin doublet (n−p): Φ_1·Φ_2 = u²−1 (classical-limit kill)
- A=1→A=2 atomic step (D−n): Φ_8² = (u^4+1)² (in Habiro-witness convention — strand-doubling Φ_8(u) = Φ_4(u²))
- Top-shared shell (a_8): partition function p(1..5) = (1, 2, 3, 5, 7)
- a_7 Padé denominator: irreducible cubic, no clean categorical match
- u^15 depth: braid-pair first-disagreement fingerprint

## Convention caveat

The Φ_8² finding lives in the Habiro-witness convention (`include_inter=True`, tr_M(D) = 0.3883 at q₀). Phase 5q canonical gives tr_M(D) = 0.7281. Whether the cyclotomic prefactor pattern survives the convention switch is the gating test for Track 1.

## Master ledger cross-link

- 1ppQ Q_β master: [`docs/coordination/1ppq-qbeta.md`](1ppq-qbeta.md)
- PR #1579 (merged 2026-06-01): commit [`57b5fa2d3a`](https://github.com/litlfred/qou/commit/57b5fa2d3a) HEAD

## Tracks 1 + 3 follow-up: Φ_8² mechanism investigation (2026-06-01)

After Tracks 1 + 3 jointly established that Φ_8² is convention-invariant and
universal across atomic-step pairs (NOT strand-doubling), a follow-up probe
tested the conjecture that Φ_8² arises from the `z(q)²` interface factor.

**Probe:** [`computations/probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py`](../../computations/probes/qbeta_habiro_phi8_squared_from_z_squared_probe.py)
**Audit:** [`docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md`](../audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md)

**Verdict: FROM-POCHHAMMER-BOUNDARY (not z(q)²).**

- `z(q)^k` alone Habiro-expands to a pure monomial `u^k` (NO cyclotomic
  factor). The Φ_4(u)^k denominator is cleared by `to_u_polynomial` into
  the normalisation prefactor.
- The Pochhammer boundaries are `(u;u)_8` (first Φ_8) and `(u;u)_16`
  (first Φ_8²).
- The ACTUAL Δa_m prefix sums acquire Φ_8 at M=7 (before the m=8 Pochhammer
  enters) and Φ_8² at M=12 (D−n) or M=15 (helium pairs). The pre-m=8 Φ_8
  appearance is a **structural Δa_m interference signature**, not mechanical
  boundary behaviour.
- The proposed "z(q)² → Φ_8²" mechanism in the FALSIFIED audit §Possible
  re-interpretations option (2) is **WRONG** (there is no u → u² substitution
  in the pipeline; z(q) = u/(u²+1) directly in u). The audit needs revision
  to reflect this finding.

The categorical content of the universal Φ_8² Δa_m signature remains
**open** — neither z(q)^k nor the m=8 Pochhammer boundary alone explains
its appearance at M=7. Probable next directions: study the Δa_m algebraic
configuration directly for a categorical witness of `ζ_8 = e^{iπ/4}`.
