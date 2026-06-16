# Topic 2 — m_avg +2.89% via Subgoal-1 operator-valued Wenzl branching

**Date:** 2026-06-02
**Branch:** `claude/m-avg-subgoal-1-operator-combiner-2026-06-02`
**Topic:** Owner-active path for closing m_avg +2.89% (the genuine
post-Bring-color-tube residual; see PR #1664).

## Pre-merge note for sibling agents

Topic 1 (PR #1664, merged `c4c5bcd3b038`) confirmed that:
- Bring color-tube extension at H₄ shifts m_avg by ~840 ppb — 34290× too small to close 2.89%
- 8 prior structural searches refuted (per `lambda-scale-absorbed-into-vol-density.md`)
- Subgoal-1 = **per-isotope Borromean-tower extension + operator-valued branching combiner** is the canonical closure mechanism per [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](../audits/2026-05-30-l2-100x-status-3-failing-shared-root.md)

This branch picks up Subgoal-1 from where the 2026-05-31 binding-magic-A-wireup PR left it.

## State of the infrastructure (as of 2026-06-02)

### Python compute (extant)

| Script | Role |
|---|---|
| `folio-assistant/computations/canonical_tr_m_via_branching.py` | Operator-valued Wenzl branching for tr_M via per-arc A operators |
| `folio-assistant/computations/A_operator_extract_at_level.py` | Extract A^λ_ξν(I) operators from the substrate Hecke at each level |
| `folio-assistant/computations/lr_coefficients.py` | Littlewood-Richardson coefficients for the branching combiner |

### Lean

`crystal-r-matrix-sub-lemma.lean` was strengthened 2026-05-31 from a `True := trivial` stub to a §3b-cond `class WenzlAOperator` + `theorem CrystalRMatrixSubLemma` consuming `LRCoefficientHecke` and `WenzlAOperator` as instance hypotheses.

**Remaining Lean gap** (per `2026-05-31-binding-magic-A-wireup.md`):

- `prop:operator-valued-combiner-convergence` — for an A-nucleon atom, the iterated application of sub-lemma 2.1 at each peeling level `n_k = 3(A-k+1)` assembles into a convergent representation of `χ^λ(β_atom)`. Tractable as a `theorem` with `Nat.rec` on A.

### Empirical state of m_avg

| Source | λ at q₀ | m_avg pred (MeV) | err vs CODATA (938.92 MeV) |
|---|---|---|---|
| Family A (H₄ Wedderburn average, in production) | 2.532780 | 966.05 | +2.890 % |
| CODATA-implied (round-trips m_p) | 2.461648 | 938.92 | 0 % |
| **Gap** | — | — | **+28900 ppm = 29 kppm** |

## Workplan

### Phase A — Run + characterize existing branching infrastructure

1. Run `canonical_tr_m_via_branching.py` on the trio of failing observables (m_n, Q_β, Δ_pn) at A=2,3,4 → confirm what the existing operator-valued combiner produces vs CODATA
2. Build a per-isotope tower probe that iterates the branching combiner from A=2 (deuteron) up through A=4 (⁴He), recording the m_avg correction at each step
3. Verify the L1-precision discipline holds (compute exit-criteria ≤ 1 ppQ)

### Phase B — Identify the gap-closing operator

4. Compare the operator-valued m_avg prediction vs the H₄-scalar (Family A) m_avg prediction at A=2-4
5. If the operator-valued combiner already closes the +2.89% gap (or moves it significantly toward closure), document the closure mechanism + wire into production
6. If the gap persists, identify which operator structure (Z↔N asymmetry per [2026-05-17 audit](../audits/2026-05-17-structural-diagnosis-operator-valued.md)) is responsible

### Phase C — Lean theorem (deferred if Phase A/B don't close gap)

7. Prove `prop:operator-valued-combiner-convergence` via `Nat.rec` on A in Lean — modulo class hypotheses already in `crystal-r-matrix-sub-lemma.lean`

## What this branch does NOT attempt

- New ansatz fits (forbidden per CLAUDE.md §"Δ_λ gate")
- Switching from H₄ to H₃ as the linking-weight basis (REGRESSES m_p by −57% per `linking_weight_canonical_object_lwfix.py`)
- Re-introducing `λ_scale` as a separate object (purged 2026-05-23, see `lambda-scale-absorbed-into-vol-density.md`)
- Subgoal-2 (research-grade < CAL-2 floor) — explicitly out of scope per the L2-100× audit

## Coordination

Owner is documented as "active" on this path per [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](../audits/2026-05-30-l2-100x-status-3-failing-shared-root.md). This branch:
- Builds on the **already-shipped** infrastructure (canonical_tr_m_via_branching + LRCoefficientHecke + WenzlAOperator class)
- Does NOT duplicate the operator-valued probe at A≤4 (extant in PR #1289 + follow-ups)
- Focus is on the **m_avg base-scale closure** specifically (the gap PR #1664 confirmed is +28900 ppm structural)
- Will coordinate via sibling PR comments if any overlap surfaces

## Cross-references

- Canonical reference for refuted routes: [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- L2-100× shared-root audit: [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](../audits/2026-05-30-l2-100x-status-3-failing-shared-root.md)
- Operator-valued diagnosis: [`docs/audits/2026-05-17-structural-diagnosis-operator-valued.md`](../audits/2026-05-17-structural-diagnosis-operator-valued.md)
- Binding-magic-A wireup: [`docs/audits/2026-05-31-binding-magic-A-wireup.md`](../audits/2026-05-31-binding-magic-A-wireup.md)
- PR #1664 Bring extension audit: [`docs/audits/2026-06-01-bring-color-weighted-implementation-and-compute-audit.md`](../audits/2026-06-01-bring-color-weighted-implementation-and-compute-audit.md)

## Update 2026-06-16 — closure path (b) operator construction implemented + verified (PR #2353)

The operator-valued combiner's **interface operator `A^λ_{ξν}(I)` is now
constructed analytically and verified exact**, on branch
`claude/analytic-interface-operator-closure-b-2026-06-16` (PR #2353). This
delivers the compute that the sibling workplan
[`docs/workplans/2026-06-16-wenzl-branching-a3-unlock.md`](../workplans/2026-06-16-wenzl-branching-a3-unlock.md)
(merged via `a9f5a79622`) scoped but explicitly deferred ("No compute landed —
this container has no numpy/mpmath/pyhecke_native").

**Consistent framing (no §6 conflict).** Both artifacts independently reach the
same structural conclusion as closure path (b): `A^λ_{ξν}(I)` is **universal**
(depends only on `(I, λ, ξ, ν)` via the seminormal/LR data, not on the inner
braid word), so it must be built from representation theory, not least-squares
fitted (the fit is rank-deficient at H₉⁺ → the 21–42 % A=3 error).

**What #2353 proves (exact, 50 dps):**
- `A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}` — the (ξ,ν)-isotypic block of the
  seminormal interface-generator matrix; isotypic projectors from central `H_3`
  class-sums (exact Lagrange spectral projectors).
- Decomposition `χ^λ(W·I·β) = Σ_{ξν} Tr[ρ_λ(W)·(Π_{ξν} ρ_λ(I) Π_{ξν})·ρ_λ(β)]`
  verified at the deuteron (H₆), pn interface: **891/891, residual ~1.5e-49**.
- New exact-MPFR seminormal-matrix binding `pyhecke_native.seminormal_matrices_mpfr`
  (validated: trace vs native χ ~1e-51, Hecke relation ~1e-50).

**Remaining (PR #2353 follow-up):** the `ρ_ξ⊗ρ_ν` gauge alignment (a basis-change
to feed the combiner) and H₉ universality — at which point
`compute_chi_lambda_via_branching` (`canonical_tr_m_via_branching.py:263`, currently
`return None` for A ≥ 3) closes, giving the polynomial-in-A speedup the workplan
targets for the ¹⁶O feasibility wall. **Speedup to an already-validated value — not
a production-value change, not wired, not a fit.**
