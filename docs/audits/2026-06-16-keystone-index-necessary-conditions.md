# Keystone — necessary conditions any Sasakian index must satisfy to give `W_λ` (2026-06-16)

**Branch:** `claude/keystone-plancherel-target-clarification-2026-06-16` (PR #2399)
**Purpose (formalize-first pruning).** The s5-so3 keystone's one open object is a
Wu-manifold SU(3)/SO(3) Sasakian S¹-equivariant index reproducing the q-Plancherel
weights `W_λ = d_q(λ)²/[n]_q!`. Before anyone *builds* such an index, state the
**necessary conditions** it must satisfy — so candidate constructions can be pruned
(and refuted ones explained) without a full differential-geometry build. Companion to
the [target clarification](2026-06-16-keystone-plancherel-target-clarification.md)
(`W_λ` is Plancherel, not the production trace weight).

## The constraints (a valid index must satisfy ALL)

| # | Constraint | Status at q₀ | Prunes |
|---|---|---|---|
| **C1** | **Normalization** — total index `Σ_λ W_λ` | **≈ 0.982 (n=5), 0.987 (n=3) — NOT 1** | any construction asserting a unit/probability total (see below) |
| **C2** | **Conjugation symmetry** `W_λ = W_{λ'}` | **EXACT** (max diff 0.0) | any index lacking a transpose/chirality (Z/2) involution |
| **C3** | **Positivity** `W_λ > 0` ∀λ | holds (min 7.6e-3 at n=5) | any *signed/virtual* index (must be a genuine dimension/L²-index) |
| **C4** | **d_q² block signature** `W_λ = d_q(λ)²/[n]_q!` = (q-dim End V_λ)/(q-dim H_n) | by definition | any index reproducing only *eigenvalues/labels*, not block *dimensions* |
| **C5** | **Classical limit** `W_λ →_{q→1} d_λ²/n!` (classical S_n Plancherel) | Σ→1 at q=1 | any q-deformation degenerating to the wrong measure |
| **C6** | **Full support** — all `p(n)` partitions, no selection rule | verified (bond-dim audit) | any index with vanishing sectors |
| **C7** | **Boothby–Wang** — dim SU(3)/SO(3)=5 odd; χ(Wu)=0 | met (ledger) | non-regular-Sasakian-compatible structures |

## What the constraints buy

- **C2 (exact conjugation symmetry)** is the strongest pruning lever. `W_λ = W_{λ'}`
  holds *exactly* at q₀, so the geometric construction **must** carry an involution
  inducing transpose λ↔λ′ — which on the QOU side is precisely the **chirality flip
  T₁↔T₂** the keystone already identifies. So the chirality involution is not
  optional decoration; it is *forced* by the Plancherel symmetry. A construction
  without it is dead on arrival.
- **C3 (positivity)** kills any *signed* equivariant index: the answer is a genuine
  dimension. The `d_q²` form (C4) says it is specifically the **dimension of the
  Wedderburn block `End(V_λ)`** — i.e. the index must compute *block dimensions*
  (the q-regular trace of the central idempotent `e_λ`), not eigenvalues. **This
  explains the refuted Reeb-eigenvalue resonance** (ledger refutation 3): it matched
  *eigenvalues* `c(λ)=ℓ(ℓ−1)`, but C4 demands *block dimensions* `d_q²` — the wrong
  invariant, so it could never have worked. Formalize-first would have pruned it.
- **C1 (normalization ≠ 1) is a genuine open catch.** `Σ_λ d_q(λ)²/[n]_q! ≈ 0.982`
  at q₀, not 1 — so `[n]_q! ≠ Σ_λ d_q(λ)²` at q₀ (they coincide only at q=1, where
  both = n!). Either (i) the geometric index legitimately totals ≈ 0.982 and the
  missing ~1.8 % has a meaning (a defect/eta term, or a non-compact correction), or
  (ii) the **correct denominator is `Σ_λ d_q(λ)²`** (making it a true probability
  measure, total 1) and `[n]_q!` in the stated `W_λ` is a q=1 artifact. **This must
  be resolved before the geometric construction** — an S¹-equivariant index on a
  compact manifold has a clean total (often integer/normalized), so reproducing a
  non-normalized 0.982 is a specific, falsifiable demand. Recommend the keystone
  author confirm the intended normalization.

## Net

The geometric index is now **boxed in by 7 necessary conditions**, two of them
exact-verified (C2 conjugation, C3 positivity) and one a live normalization catch
(C1). The most actionable consequences: the chirality involution is *forced* (C2);
the index must compute *block dimensions* not eigenvalues (C4, retro-explaining the
Reeb-resonance refutation); and the `[n]_q!` vs `Σd_q²` normalization needs owner
clarification (C1). This prunes the candidate space without a diff-geo build — the
build itself remains owner-gated. Constraints reproducible via the q0 check in this
PR's commit.
