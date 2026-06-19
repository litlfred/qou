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
| **C1** | **Normalization** — total `Σ_λ W_λ` | **≈ 0.982 (n=5) — `W_λ` is *not* a probability measure (expected; `d_q` has no sum rule)** | fixes the index total; not a defect — see below |
| **C2** | **Conjugation symmetry** `W_λ = W_{λ'}` | **EXACT** (max diff 0.0); **facets formalized (#2500):** `KeystoneChiralityInvolution.lean` — content negates under transpose (chirality atom), electron `(3,1,1)` self-conjugate (chirality fixed point), `[2]↔[1,1]` flip | any index lacking a transpose/chirality (Z/2) involution |
| **C3** | **Positivity** `W_λ > 0` ∀λ | holds (min 7.6e-3 at n=5) | any *signed/virtual* index (must be a genuine dimension/L²-index) |
| **C4** | **d_q² block signature** `W_λ = d_q(λ)²/[n]_q!` = (q-dim End V_λ)/(q-dim H_n) | by definition | any index reproducing only *eigenvalues/labels*, not block *dimensions* |
| **C5** | **Classical limit** `W_λ →_{q→1} d_λ²/n!` (classical S_n Plancherel) | Σ→1 at q=1 | any q-deformation degenerating to the wrong measure |
| **C6** | **Full support** — all `p(n)` partitions, no selection rule | verified (bond-dim audit); **quantitative teeth (#2500):** the colour-`ℂ^N`-missed block count is unbounded + monotone in `A` (`ColourArenaBlockCount.lean`, sorry-free) ⇒ **no finite-`N` arena**, so the index must carry **all `p(3A)`** blocks; combiner non-degeneracy (`CombinerBranchingCompleteness.lean`) confirms every block is reached | any index with vanishing sectors, **and any finite-dimensional (finite-`N` colour) Sasakian** |
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
- **C1 (normalization) — grounded: `W_λ` is simply not a probability measure, and
  that is expected.** `Σ_λ d_q(λ)²/[n]_q! ≈ 0.982` (n=5), 0.987 (n=3), 0.991 (n=6) —
  non-monotonic, no clean value. This is **not** a convention bug (verified:
  `atom.q_dimension` / `atom.q_factorial` are the consistent *balanced* q-hook pair,
  and a from-scratch balanced calc reproduces 0.982) and **not** a defect. It is just
  that the **quantum dimension `d_q(λ)` has no sum rule**. The classical
  `Σ_λ d_λ² = n!` holds for the **ordinary** dimension `d_λ = #SYT = dim V_λ = dim
  End V_λ`, because `H_n(q) ≅ ⊕_λ End(V_λ)` has dimension `n!` (same as `ℂ[S_n]`).
  The **quantum** dimension `d_q(λ)` (the q-hook / Markov loop value) is a different
  quantity and satisfies **no** analogous `Σ d_q² = [n]_q!` identity at `q ≠ 1` (only
  at `q=1`, where `d_q → d_λ`, `[n]_q! → n!`).

  **Three distinct weights — do not conflate (the actual context):**
  | weight | formula | `Σ_λ` | role |
  |---|---|---|---|
  | ordinary-dim Plancherel | `d_λ²/n!` | **1** (probability) | classical S_n RSK measure |
  | quantum-dim `W_λ` (keystone) | `d_q(λ)²/[n]_q!` | **≈0.982** (not normalized) | the geometric-index target |
  | production `y_λ` | principal specialization | (Markov-normalized) | nuclear mass trace (≠ either above) |

  So calling `W_λ` "Plancherel" is loose — the *true* (Σ=1) Plancherel is the
  ordinary-dim `d_λ²/n!`. The only **genuine** (non-rabbit-hole) question for the
  geometry: is the index target the unnormalized `W_λ = d_q²/[n]_q!` (total ≈0.982),
  or its normalized form `d_q²/Σd_q²` (total 1)? A one-line owner answer; not a
  defect/eta term. (Earlier framing of this as a deep "open catch" was over-reach.)

## Net

The geometric index is **boxed in by 7 necessary conditions**, two exact-verified at
q₀. The two solid, actionable consequences:

1. **C2 — the chirality involution `T₁↔T₂` is forced** (conjugation symmetry
   `W_λ=W_{λ'}` is exact); a construction without it is dead on arrival.
2. **C4 — the index must compute block *dimensions* `d_q²`, not eigenvalues** — which
   retro-explains the refuted Reeb-eigenvalue resonance (it matched the wrong
   invariant).

C1 is **not** a catch: `W_λ` simply isn't a probability measure (quantum dims have no
sum rule); the only open item there is a one-line normalization-convention choice
(`d_q²/[n]_q!` vs `d_q²/Σd_q²`). The diff-geo build itself remains owner-gated.
Constraints reproducible via `keystone_index_necessary_conditions.py`.
