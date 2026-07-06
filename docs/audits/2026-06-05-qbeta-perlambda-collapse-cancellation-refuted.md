# Q_β residue-A — the per-λ collapse-cancellation hypothesis is REFUTED (heavy probe verdict)

**Date:** 2026-06-05 · **Probe:** [`qbeta_perlambda_collapse_cancellation_probe.py`](../../computations/qbeta/qbeta_perlambda_collapse_cancellation_probe.py) · **Witness:** `qbeta-perlambda-collapse-cancellation.witness.json` · **Follows:** PR #1895 (S2+S3 exploration, merged).

## What was tested

PR #1895 (owner-confirmed) posed the **falsifiable** S2 hypothesis: does the
coherent scalar collapse `tr_M = Σ_λ y_λ χ^λ` **cancel** the per-block n↔p content
that the per-block (incoherent) sum retains — so that "observe last" recovers the
`c_3` order with no fitted amplifier? #1895 pre-committed to both branches:

- positive (`u³` cancels in `Σ_λ`) → the collapse is the artifact;
- **negative (no cancellation) → S2 refuted as the order-gap source.**

The heavy per-λ probe runs the production machinery
(`mass_at_3A_proper.markov_trace_3A`, canonical `χ^λ` via `chi_lambda_of_word`)
for the proton `(Z,N)=(1,0)` and neutron `(0,1)` H₃ braids at the substrate `q₀`,
and measures `cancellation_ratio = |Σ_λ Δcontrib_λ| / Σ_λ |Δcontrib_λ|`, where
`Δcontrib_λ = contrib_λ(n) − contrib_λ(p)`.

## Result — the NEGATIVE branch (rigorous, both weightings)

| λ ⊢ 3 | dim | χ^λ(p) | χ^λ(n) | Δχ^λ | y_λ (Wenzl) |
|---|---|---|---|---|---|
| (3) | 1 | +1.3825 | +1.1221 | **−0.260** | +0.4154 (+) |
| (2,1) | 2 | +1.8077 | +1.7009 | **−0.107** | +0.2809 (+) |
| (1,1,1) | 1 | −0.7392 | −0.9108 | **−0.172** | +0.0227 (+) |

**Every per-λ n−p contribution has the SAME sign** (every `Δχ^λ < 0`; every
`y_λ > 0`). Therefore:

$$\text{cancellation ratio} = 1.0000\quad(\text{Plancherel})\ =\ 1.0000\quad(\text{canonical Wenzl } y_\lambda).$$

`coherent = incoherent` exactly — **there is nothing for the collapse to cancel,
and observe-last recovers nothing.** The neutron's character is uniformly smaller
than the proton's across all Wedderburn blocks; the difference is **coherent**,
not interferential.

## Implication

- **The `c_3` order gap is NOT a collapse-cancellation artifact.** The `√u → u³`
  amplification (#1593) must come from the **genuine f-map / anchor-dependent
  brane-tower level** `ℓ(K, q₀)` — exactly #1887's surviving possibility after it
  refuted the fixed-ℓ closed-form f-map. The residue-A search narrows to that
  branch (GAP-A-3), and to #1900's q-difference recursion kernel.
- **The owner-confirmed S2 hypothesis (PR #1895) lands on the NEGATIVE branch it
  explicitly anticipated.** This is a *valid, valuable* outcome of the falsifiable
  test — not a reversal of framing. The broader "preserve information / observe
  last" principle (cheat sheet §9.2) and its **binding A≥3 `θ_λ` application** are
  **untouched** — they concern a different object (the per-λ Reeb phase, not the
  n-p character difference, which here simply does not cancel).
- **Bar-parity results stand.** `c_3 = odd-sinh`, `h = 2 sinh η` bar-odd, and the
  **Φ₂ = bar-odd reconciliation** (Φ₂ swing = c_3 swing; `a₁ = √2·Φ₂ = −c₃`) are
  independent of this refutation — #1900's `a₁ bar-odd` constraint is unaffected.

## Caveat (scope of the refutation)

The probe tests the **full** per-λ n−p difference at `q₀`, not the `u³`-order
slice in isolation (which needs the `u`-parametrization / f-map — the open part).
But the gross structure — all blocks same sign, ratio exactly 1.0 — leaves no
sign room for an order-specific cancellation either. A u-resolved follow-up would
need the f-map, i.e. the GAP-A-3 branch above.

## Discipline

No fit; `c_3` stays cal-anchored / NEAR-MATCH; nothing wired to production. This
is a derive-or-refute structural result (refute), the intended output of the
#1895 falsifiable design.
