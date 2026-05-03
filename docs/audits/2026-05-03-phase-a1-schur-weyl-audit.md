# Phase A.1 audit: where does single-K averaging live?

**Date:** 2026-05-03
**Branch:** `claude/phase-a1-schur-weyl-audit`
**Goal:** identify exactly where the binding-canonical pipeline currently
"loses ~10⁶ ppb to single-K averaging" per the 22 ppb workplan
(issue #522 phase A.1).

## Verdict: **the canonical pipeline does NOT use single-K averaging.**

The pipeline already uses the axiomatic Markov trace
(`markov_trace_canonical.tr_M_element`), which satisfies (M1) cyclicity,
(M2) Markov property, (M3) normalization — no partition sum, no `k_cap`,
no Plancherel truncation. The 10⁶ ppb gap claimed in the workplan
attributable to "single-K averaging" must come from somewhere else.

The misattribution is confirmed by reading the docstring of the legacy
function:

> `folio-assistant/computations/hecke_core.py:2614` — `atom_markov_trace`:
>
> > `[DEPRECATED — Plancherel-weighted] "Markov" trace of atom braid.
> > Computes Σ_λ (Plancherel-weight) · χ_λ(W)/d_λ. At q ≠ 1 this is NOT
> > the canonical Jones–Markov trace specified in
> > prop:categorical-mass-markov (which gives tr_M(σ_0) = z ≈ 0.499). The
> > Plancherel form gives ≈ 0.104 at q_0 — see the validity audit
> > (rem:mass-endomorphism-tower-adjacency-audit). Use
> > markov_trace_canonical.tr_M_element for the canonical axiomatic
> > Markov trace that matches the prop's explicit table. Legacy form
> > retained for existing callers; new code should route through
> > binding_canonical.binding_canonical.`

## Where partition truncation DOES live (legacy / deprecated paths)

The `k_cap` partition-jet-depth truncation lives in the legacy
Plancherel-weighted code path:

- `folio-assistant/computations/hecke_core.py:452` —
  `K_PARTITION_MAX = 11` (the cap on partition jet depth `k(λ)`).
- `folio-assistant/computations/hecke_core.py:2614–2673` —
  `atom_markov_trace(Z, N, k_cap=None, include_inter=True)`. Iterates
  over partitions filtered by `k_cap`. **DEPRECATED.**
- `folio-assistant/computations/hecke_core.py:2453–2602` —
  `binding_3A` / similar functions also gated by `k_cap`.

Truncation by jet depth (not by partition count) is a research-grade
choice — partitions are streamed up to a fixed `k(λ) ≤ 11` ceiling.
This is NOT what the workplan calls "single-K averaging"; it's a
multi-K (multi-jet-depth) sum capped at depth 11.

## Where the canonical pipeline gets its trace

- `folio-assistant/computations/binding_canonical.py:37` imports
  `tr_M_element` from `markov_trace_canonical`.
- `binding_canonical.py:146` calls `tr_M_element(atom_elem, n_strands)`
  — no partition argument, no Wedderburn block sum.
- `markov_trace_canonical.py:1–35` (top docstring) confirms the trace
  is computed by axiomatic recursion (Markov axioms M1, M2, M3 at the
  H_n level), not by any sum over partitions.

## Where the 10⁶ ppb gap likely lives instead

Three candidates from the workplan:

1. **q-Hecke Φ_q normalisation** (workplan A.2). The single binding-
   energy contribution `Φ_q(|tr_M(ξ)|)` may be approximated rather
   than computed exactly at q = q_0.
2. **Higher tower levels** (workplan A.3 — separate audit). The mass
   tower truncates at some level `N`; level-`(N+1)` is currently
   unsummed.
3. **q-Plancherel weights vs classical weights** in any contributing
   downstream sum (e.g. NV-1 / Plancherel-character probes).

The first two are the most likely candidates for the actual ~10⁶ ppb
loss. None of them is "single-K averaging" of the Markov trace.

## Recommendation

**Reword issue #522's Phase A.1.** The original phrasing —

> "A.1: Full Schur–Weyl decomposition over `p(3A)` for A ∈ {1..6}.
> Currently single-K averaging loses ~10⁶ ppb (0.1%)."

— is misleading. The canonical pipeline already uses the axiomatic
Markov trace (no partition sum at all). What may be desired:

- **A.1' — Tighten the q-Plancherel approximation in Φ_q** (closer to
  workplan A.2; the binding contribution
  `Φ_q(|tr_M|) = Σ_n (something)` may need exact rather than
  truncated evaluation).
- **A.1'' — Audit the deprecated `atom_markov_trace` callers**:
  identify any caller in the 22 ppb workplan that still routes through
  the deprecated Plancherel form rather than `tr_M_element`. Such
  callers are easy 10⁶-ppb closures (the docstring explicitly says
  the Plancherel form gives ≈ 0.104 vs canonical ≈ 0.499 for σ_0 —
  ~5× error per term).

Both A.1' and A.1'' are tractable in 1–2 days each. Phase A.3
(mass-tower truncation, separate audit) likely closes more.

## Files

- Witness: [`folio-assistant/computations/phase-a1-schur-weyl-audit.witness.json`](../../folio-assistant/computations/phase-a1-schur-weyl-audit.witness.json)
- This memo
- No code changes — audit-only.

## Status

**Audit-only finding.** Phase A.1 as originally framed is a misnomer;
the underlying gap should be re-attributed to either Φ_q exactness
(workplan A.2) or higher tower levels (workplan A.3) before further
implementation work.
