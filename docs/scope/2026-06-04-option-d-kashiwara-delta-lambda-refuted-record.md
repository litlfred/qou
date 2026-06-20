# Option D — Kashiwara crystal Δ_λ closure for per-isotope binding (refutation record)

**Date:** 2026-06-04
**Branch:** [`claude/qbeta-stageB-cosh-relabel-2026-06-04`](https://github.com/litlfred/qou/tree/claude/qbeta-stageB-cosh-relabel-2026-06-04) — PR [#1866](https://github.com/litlfred/qou/pull/1866)
**Status:** REFUTED in PR #1860 (merged); this scope record consolidates that result and redirects to the remaining productive direction.

## What this option was

The per-isotope binding-energy formula under canonical Path D:

    B(K) = m_e · Σ_{λ⊢3A} y_λ(q_0) · χ^λ(β_K) · Δ_λ(K)

requires per-partition `Δ_λ(K)` values. For the deuteron alone this
is 1 equation in 11 unknowns. The roadmap-level question was:

> **Can a Kashiwara-crystal ansatz (Macdonald n(λ), conjugate n(λ'),
> dim ratio at q_0, …) fix the underdetermined Δ_λ?**

The audit `0e30e23e` (`docs/audits/2026-06-04-three-paths-refuted-roadmap-update.md`) consolidates the result.

## Refutation

PR [#1860](https://github.com/litlfred/qou/pull/1860) tested **five
no-fit candidates** E1–E5:

- Macdonald `n(λ)` (Major-index sum on standard tableaux)
- Conjugate `n(λ')` (reflected partition)
- dim ratio at `q_0` (q-dim quotient)
- Constant-zero control
- Ordinary `dim f^λ` (classical Frobenius dimension)

**All 5 REFUTED.** Combined with the 4 prior Δ_λ failures (Frobenius
co-Casimir #602, Demazure-fibre, LP-Plancherel/LP-Frobenius #603,
Wenzl-bridge augmented Markov), the no-fit closure-of-Δ_λ family for
binding-energy is now **9-of-9 negative**.

## Consequence for this PR's scope

The original AskUserQuestion offering for this tranche was:

> "Pivot to the per-isotope binding-energy axis (still named
> 'productive' in the a817f7d4 audit). Different observable from
> c_k (binding deltas, not Q_β coefficients). Cost: high (≥
> several sessions, requires Mathlib KLR/crystal infra that
> doesn't exist yet). Best left for a dedicated session, not
> piggybacked."

PR #1860 landed **after** that offering was drafted. The "still
named 'productive'" framing was overtaken by the refutation; the
follow-on audit `0e30e23e` explicitly closes Option D and
redirects to **GAP-A-3 / GAP-A-4**:

- **GAP-A-3** — categorical brane-tower level selection: Δ_λ as
  a property of the brane-tower truncation order `ℓ(K, q_0)`,
  not of any per-partition functional.
- **GAP-A-4** — ρ general rule: the per-atom λ(K) substrate-
  derivation (Path B's gate), which would close the H₃→H₄ jump
  structurally by making the Wedderburn-count interpretation
  moot.

Both are **research-grade categorical work**, above the Δ_λ-gate
cap. AGENTS.md explicitly forbids a seventh fit ansatz; per the
audit, no further single-formula Δ_λ candidates should be tested.

## What this PR's record contributes

- **Closes the Option D action item** on this PR's workplan.
- **Cross-links** the refutation chain (PR #1860 → audit
  `0e30e23e` → this scope record) so a future session triaging
  the c_k frontier sees "Option D refuted, do not re-test" without
  needing to chase the merged PR history.
- **Names GAP-A-3 / GAP-A-4 as the open research-grade direction**,
  consistent with the audit, so subsequent agents are not tempted
  to propose a new closed-form Δ_λ ansatz.

## References

- Refutation PR: [#1860](https://github.com/litlfred/qou/pull/1860)
- Roadmap consolidation: [`docs/audits/2026-06-04-three-paths-refuted-roadmap-update.md`](../audits/2026-06-04-three-paths-refuted-roadmap-update.md)
- Δ_λ gate canonical reference: [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../audits/2026-05-18-delta-lambda-gating-context.md)
- GAP-A-3 / GAP-A-4 framing: [`docs/audits/2026-05-19-delta-lambda-phase4-z4N-closure.md`](../audits/2026-05-19-delta-lambda-phase4-z4N-closure.md)
- Q_β coordination: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
