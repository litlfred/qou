# GAP-A-3 transpose-invariant P_λ candidates — elementary family excluded (2026-06-20)

**Status:** audit — formalize-first *exclusion* result. Direct continuation of
the bar-even admissibility narrowing
([`2026-06-20-gap-a3-plambda-bar-even-admissibility.md`](2026-06-20-gap-a3-plambda-bar-even-admissibility.md),
merged PR #2522). EXPLORATORY — no fit, no production rewire, no 7th Δ_λ ansatz.

## Setup

PR #2522 narrowed GAP-A-3 `P_λ` to **transpose-invariant functionals**
(`P_λ = P_{λᵀ}`), ruling out the row-count content channels structurally. This
probe tests whether any *elementary* transpose-invariant functional reproduces
the deuteron `P_λ` target.

The candidates are admissible by construction, via two facts:

- The **hook-length multiset is transpose-invariant** (λ ↦ λᵀ permutes cells but
  preserves the multiset of hook lengths). Hence every symmetric function of it
  is transpose-invariant — the Specht dimension `f^λ = n!/∏h` (so `f^λ = f^{λᵀ}`,
  classical), `∑h`, `∑h²`, and the q-hook product `∏[h]_q`.
- `n(λ) + n(λᵀ)` is transpose-symmetric by construction.

So the prior content channels C1/C2 (which used `f^λ`) failed *only* from the
`rows(λ) ≤ k` cutoff — not from `f^λ`. These candidates drop the cutoff. The
probe asserts `P_λ = P_{λᵀ}` for each candidate before scoring it (all pass).

## Findings

[`computations/probes/gap_a3_transpose_invariant_plambda_probe.py`](../../computations/probes/gap_a3_transpose_invariant_plambda_probe.py)
· witness `computations/probes/gap-a3-transpose-invariant-plambda-probe.witness.json`.
Deuteron target `−B(D)/(m_e·A(D)) ≈ −0.18947`; `tr_M(β_D) ≈ +0.38829`.

| candidate | P_λ | admissible | S | verdict |
|---|---|:--:|--:|---|
| T0 constant | `1` | ✓ | +0.38829 | control: flat scale `c* = −0.48797` |
| T1 Specht dim | `f^λ` | ✓ | +1.66199 | REFUTED |
| T2 row/col moment | `n(λ)+n(λᵀ)` | ✓ | +4.44263 | REFUTED |
| T3 hook sum | `∑h` | ✓ | +6.77234 | REFUTED |
| T4 hook-square sum | `∑h²` | ✓ | +26.12897 | REFUTED |
| T5 q-hook product | `∏[h]_q` | ✓ | +121.59750 | REFUTED |

Two observations:

1. **All elementary transpose-invariant functionals are excluded.** Every
   admissible single functional overshoots and (being positive-valued against a
   positive-skewed `χ^λ` weighting) lands on the wrong side of zero — the target
   is *negative* (`−0.189`) while every `S` is positive. A flat deviation would
   need `c* = −0.488` (T0), i.e. a sign-flipped sub-unity suppression, which no
   elementary positive functional supplies.

2. **The admissible family is real but non-elementary.** Bar-even admissibility
   (PR #2522) is necessary; this probe shows it is far from sufficient among
   elementary symmetric functionals. If a categorical `P_λ` exists it is a
   **non-elementary transpose-invariant object** — plausibly knot-dependent /
   operator-valued, consistent with the s5-so3 keystone framing
   (`conj:s5-so3-fiber-action`), where the per-atom channel selection is itself
   operator-valued rather than a closed scalar functional of λ.

## What this buys

- **Exclusion (the deliverable).** The elementary symmetric (hook-multiset and
  row/column-moment) family is now excluded as the GAP-A-3 `P_λ`. Combined with
  PR #2522's exclusion of the row-count family, the search is pinned: any
  surviving `P_λ` is a non-elementary transpose-invariant functional, and the
  productive direction is the operator-valued s5-so3 keystone, not a scalar
  ansatz.
- **No fit.** No free parameter was tuned; T0's `c*` is *reported*, not used to
  wire anything. This is a refutation that narrows, not a new fitted P_λ.

## References

- [`2026-06-20-gap-a3-plambda-bar-even-admissibility.md`](2026-06-20-gap-a3-plambda-bar-even-admissibility.md) — the prior narrowing (PR #2522).
- `computations/probes/gap_a3_transpose_invariant_plambda_probe.py` — this probe.
- `conj:s5-so3-fiber-action` — the operator-valued keystone the residual points to.
