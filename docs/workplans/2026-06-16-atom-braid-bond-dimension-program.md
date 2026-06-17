# Atom-braid trace beyond ¹²C — bond dimension, nucleon symmetry, sparsity, R-matrix MPS (2026-06-16)

**Branch:** `claude/atom-braid-bond-dimension-program-2026-06-16`
**Context:** the operator-form branching recursion (#2358/#2365/#2371) is **dominated
by the fine-Bratteli transfer** already in production (⁴He 0.09 s, ¹²C ~5.5 min;
branching needs 9 MB/block at ⁴He, 12 GB at ⁵Li). Neither reaches ¹⁶O. This program
asks whether **unused structure** can push exact `tr_M` past the transfer's ¹²C wall.

## 0. What is actually blowing up

Exact `tr_M(β_atom) = Σ_{λ⊢n} y_λ χ^λ(β)`, `n = 3A`, has two intrinsic costs:

1. **Partition count** `p(n)` — the number of Wedderburn sectors. `p(36)=17 977`
   (¹²C), `p(48)=147 273` (¹⁶O).
2. **Irrep dimension** `d_λ` — each `χ^λ = Tr ρ_λ(β)` is a trace over `V_λ`,
   `Σ_λ d_λ² = n!`.

The fine-Bratteli transfer is a **1-D transfer-matrix (MPS) contraction in the
partition-label basis**: the atom is a chain of nucleon blocks, the "bond" at the
strand-cut after nucleon `k` is the irrep label `λ⊢3k`, and the transfer steps
block→block. Its cost is set by the **bond dimension ≈ p(3k)** — which is exactly
why it tracks `p(3A)` and walls at ¹⁶O. Dense branching is worse (it materialises
`A^λ_{ξν}` at `(d_ξ d_ν)²`, `d_ξ` = irrep dim of `S_{3(A−1)}`, which explodes).

**The question for every direction below:** can we get the *effective* bond
dimension below `p(3k)` — exactly, no truncation (the active-set 10⁻³ truncation is
rejected at the 1-ppQ floor) — by exploiting structure the transfer ignores?

## 1. Bond-dimension measurement — the decisive gate (DO FIRST)

**Claim to test:** the atom braid is *highly non-generic* (A repeated nucleon
blocks + a few interfaces), so it may populate only a **small subset** of the
`p(3k)` intermediate partitions at each cut. If the *empirical* support
`χ_eff(k) = #{λ⊢3k : amplitude ≠ 0}` grows much slower than `p(3k)`, an
MPS contraction restricted to the populated subspace breaks the wall.

**Experiment (cheap, decisive, computable now):**
- Build the atom braid in the Bratteli-path / partition-label transfer
  (`tr_m_atom_via_transfer` / `chi_monotone_transfer` already do this).
- At each strand-cut `k = 3, 6, …, 3A`, record `χ_eff(k)` = number of partitions
  carrying nonzero weight (and the numerical rank of the cut state).
- Plot `χ_eff(k)` vs `p(3k)` for A = 2…6 (feasible) and extrapolate.

**Decision rule (formalize-first):**
- `χ_eff(k) ≪ p(3k)` (e.g. polynomial) → build the restricted-support MPS
  contractor; ¹⁶O+ becomes feasible. **Big prize.**
- `χ_eff(k) ≈ p(3k)` → the partition basis is intrinsically full; exact ¹⁶O stays
  out of reach and heavy nuclei rely on the A→∞ colour-weighted q-CLT
  extrapolation (#2349's honest fallback). **Stop chasing exact ¹⁶O.**

This single measurement gates the entire program — run it before building anything.

## 2. S_Z × S_N nucleon-permutation symmetry

The closed atom braid is invariant under permuting the `Z` identical proton blocks
and the `N` identical neutron blocks (`|S_Z × S_N| = Z!·N!`). Two payoffs:

- **State-space reduction:** in the transfer, identical adjacent blocks make the
  per-block transfer matrix *repeat* — the contraction is a product of powers of a
  few fixed matrices, and the populated cut states fall into `S_Z×S_N`-orbits, so
  the *distinct* states (the real bond dimension) may be far fewer than `χ_eff(k)`.
- **iMPS fixed point:** a long run of identical blocks → a translation-invariant
  transfer whose action is governed by its dominant eigenvector; heavy nuclei could
  be evaluated by a fixed-point rather than `A` explicit steps.

**Preflight (STRICT, CLAUDE.md §3.2):** mixed-species (p–n) interfaces are **not**
pure conjugations, so the symmetry is broken at each p–n boundary. Verify on ⁴He
(2p2n, orbit size 4) at 50 dps that the symmetrised trace equals the direct trace
*before* using it. Within-species (p–p, n–n) symmetry is exact; cross-species is
the boundary bookkeeping.

## 3. Interface / generator sparsity (fix the dense waste)

In Young's seminormal/orthogonal form, `σ_i` is **block-diagonal with only 1×1 (±1)
and 2×2 blocks** indexed by SYT pairs `(T, s_iT)` — `O(d_λ)` nonzeros, not `d_λ²`.
The interface `I = c·σ + d·1` inherits this; the dense extract `A = Π ρ(I) Π`
throws it away. **Fix:** carry `ρ_λ(I)` and the transfer steps as sparse
(per-SYT-pair) operators. This does not change the `p(3k)` bond dimension but cuts
the per-step cost from `O(χ²)`-dense to `O(χ·sparsity)` — a large constant-factor
win that compounds with #1/#2. Low-risk, independently useful for the transfer.

## 4. Schur–Weyl / R-matrix MPS (explore)

Alternative basis: the **physical tensor space** `V^{⊗n}` (`V` = 2-dim SU_q(2)
fundamental, or 3-dim colour), where the braid is a product of **local R-matrices =
an MPO acting on an MPS**. The atom braid is highly repetitive → the MPS bond
dimension may **saturate** (iMPS / transfer-fixed-point territory).

**Honest caveat:** in the 2-dim (TL) basis the cut bond dimension is the number of
non-crossing link states `~ Catalan(m) ~ 4^m` — *exponential*, generically **worse**
than the partition basis's sub-exponential `p(3k)`. So the colour MPS only wins if
the atom's structure + symmetry collapses the bond far below the Catalan bound. This
is the most speculative direction — explore *after* #1 tells us whether any basis
has a chance. Measure the colour-MPS bond growth the same way (#1) before committing.

## Sequencing

1. **#1 bond-dimension measurement** — decisive, cheap, gates all. ← start here
2. **#3 sparsity** — low-risk constant-factor win, do alongside #1 (same infra).
3. **#2 nucleon symmetry** — after the ⁴He preflight; the real scaling lever if #1
   is favourable.
4. **#4 R-matrix MPS** — explore only if #1/#2 show bounded bond dimension.

## Discipline

No truncation at production precision (the active-set 10⁻³ is rejected — owner
directive "don't do pruning in production"). Every reduction must be **exact**
(symmetry orbits, sparsity, populated-support) — provably lossless, verified at the
50-dps floor against the transfer. No production value changes; this is a
*compute-scaling* program, not a physics change.
