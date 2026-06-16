# Option E Phase 1 — Hoefsmit-seminormal Gram matrix generalisation to H_6 (deuteron)

**Branch**: `claude/option-e-phase1-gram-h6-2026-06-02`
**Goal**: close the Δ_λ Gap 5 (Gram-matrix generalisation) for the deuteron.
**Track**: Track A blocker per CLAUDE.md (Precision goals §L2); Δ_λ gating context per
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md).

## Δ_λ derivation chain — gap location

The chain runs

```
substrate q_0 → 𝐂 categorical action → Yekutieli non-abelian Stokes → 𝐇_n(q) Hecke
             → Wedderburn decomposition (partitions λ ⊢ n)
             → Frobenius pairing tr_M = Σ_λ y_λ χ_λ
             → confinement SDP → canonical T_w
             → Archimedean functor at q_0 → per-block M_λ(K) → Δ_λ(K)
             → MeV observables
```

Of the six identified structural gaps in the per-block Δ_λ extraction, this branch
attacks Gap 5 (the Frobenius pairing infrastructure) at the deuteron level.

## What's already on main (no work needed)

- **Partition-basis Gram matrix** (diagonal in Wedderburn blocks):
  `computations/pyhecke_n_generic.py::gram_matrix_n(n, q)` — landed
  2026-05-25 (PR #1251); replaces the H_3-hardcoded `pyhecke_native.gram_matrix(q)`.
  Size: $p(n) \times p(n)$ (11 × 11 for n=6, 30 × 30 for n=9, 77 × 77 for n=12).
- **Per-block Hoefsmit seminormal matrices** (the σ_k actions per partition):
  `computations/hoefsmit_symbolic.py::build_seminormal_matrices_symbolic(shape)`
  via `hecke_character_symbolic.hoefsmit_matrices_symbolic` — the per-block σ_k
  representation already generalises to any n.

## What this branch adds

The **within-block Gram matrix** for each Wedderburn block at general n. The
partition-basis Gram captures Markov pairings *between* blocks (zero off-diagonal);
the within-block Gram captures the dim_λ × dim_λ Markov pairing structure *inside*
each block — needed by Option E Phase 2 (canonical-basis trace ρ_w(K) at crystal
vertices).

### Concretely

For each $\lambda \vdash n$ with $\dim_\lambda$ standard Young tableaux, build
the $\dim_\lambda \times \dim_\lambda$ matrix

$$
  G^{(\lambda)}_{T, T'}
  \;=\;
  \mathrm{tr}_M\!\bigl(\rho_\lambda(\sigma_T) \cdot \rho_\lambda(\sigma_{T'})\bigr)
$$

where $T, T'$ range over the standard Young tableaux of shape $\lambda$,
$\sigma_T$ is the Hoefsmit-seminormal basis element indexed by $T$, and
$\rho_\lambda$ is the per-block representation from
`hoefsmit_matrices_symbolic(λ)`.

### Sizes at H_6 (deuteron, $n_{\mathrm{total}} = 6$)

| λ | dim_λ | block matrix |
|---|------:|-------------:|
| (6) | 1 | 1×1 |
| (5,1) | 5 | 5×5 |
| (4,2) | 9 | 9×9 |
| (4,1,1) | 10 | 10×10 |
| (3,3) | 5 | 5×5 |
| (3,2,1) | 16 | 16×16 |
| (3,1,1,1) | 10 | 10×10 |
| (2,2,2) | 5 | 5×5 |
| (2,2,1,1) | 9 | 9×9 |
| (2,1,1,1,1) | 5 | 5×5 |
| (1,1,1,1,1,1) | 1 | 1×1 |

Total $\sum_\lambda \dim_\lambda^2 = 720 = 6!$ (matches the discarded NF basis,
re-organised by Wedderburn block — same data, exponentially smaller per-block view).

## Scope of this PR

| Item | Status |
|------|--------|
| `gram_matrix_seminormal_block(n, λ, q)` Python implementation | this PR |
| Cross-check against `gram-matrix-dual.py` (H_3, 6×6 reassembled from blocks) | this PR |
| H_6 witness JSON: 11 per-partition blocks at q_0 | this PR |
| H_9, H_12 generalisation | follow-up (different PR) |
| Lean formalisation `QOU.BraidKnot.GramSeminormalBlock` | follow-up (different PR) |
| ρ_w(K) crystal-vertex trace using these matrices | Option E Phase 2 (sibling PR #1516) |
| Per-atom Δ_λ extraction using these matrices | Option E Phase 3 |

## Why not all of Option E at once?

Per CLAUDE.md "combine related work into one branch": this Phase 1 piece is
genuinely independent of Phase 2 (which needs the crystal-vertex enumeration,
a separate concern). Sibling PR #1516 has been scoping Phase 2 in parallel;
this PR provides Phase 2's missing infra (within-block Gram) without forcing
that branch to absorb it. Cross-reference will be added once both land.

## Acceptance criteria

1. `gram_matrix_seminormal_block(3, λ, q_0)` reassembled across all $λ ⊢ 3$
   matches `gram-matrix-dual.py`'s 6×6 Gram (modulo basis ordering) to
   1 ppQ (10⁻¹⁵).
2. `gram_matrix_seminormal_block(6, λ, q_0)` produces 11 invertible symmetric
   matrices.
3. Witness JSON includes per-block determinant, condition number, and a
   classical-limit check ($q \to 1$: the Gram reduces to the Plancherel
   pairing $y_\lambda \cdot \mathrm{Id}_{\dim_\lambda}$ modulo within-block
   cyclic structure).

## Out of scope

- Higher-n generalisation (H_9, H_12).
- Lean formalisation (declaration stub only; full proof of the Hoefsmit
  matrix construction is a separate Mathlib-bridging task).
- Per-block Δ_λ extraction (this is Phase 3 — needs the crystal-vertex
  trace from Phase 2 first).
