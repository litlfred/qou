# Combiner branching completeness — `interface_blocks` non-degeneracy (2026-06-19)

**Branch:** `claude/serene-cerf-j4d339` (PR #2500). Owner-directed item 2 of "1 2 3".
**Discipline:** formalize-first (§3.3), corpus-grep (don't re-derive), tiered status.

## The claim

The operator-valued combiner (`a_operator_recursive.py :: interface_blocks`;
narrative [`hecke-branching-trace-decomposition.md`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md))
decomposes a per-block character along `H_{n_inner}(q) ⊗ H_{n_block}(q) ↪ H_n(q)`:

> `χ^λ(β₁·I·β₂) = Σ_{ξ⊢n_inner, ν⊢n_block} c^λ_{ξν}·Tr(A^λ_{ξν}(I)·(ρ_ξ(β₁)⊗ρ_ν(β₂)))`.

"We get all terms" = the combiner reaches **every** Wedderburn block `λ⊢n`, so the
production trace `tr_M = Σ_λ y_λ χ^λ` drops none.

## Corpus-grep: the per-λ half is ALREADY established (do not re-derive)

Per the corpus-grep discipline, the **per-λ** completeness — that the `(ξ,ν)` sum
captures *all* of `Res(V_λ)` — is already proved:

- `hecke-branching-trace-decomposition.md` ∎: the trace is the sum over the
  orthogonal `(ξ,ν)`-isotypic components of `V_λ` (no remainder).
- Wenzl 1988 semisimplicity `H_n(q) ≅ ⊕_{λ⊢n} End(V_λ)` — every `λ⊢n` is a block
  ([`QOU/Hecke/Wedderburn.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/Wedderburn.lean),
  `three_parameters_wedderburn.lean`).

So this item does **not** re-derive completeness. It formalizes the remaining,
**dual** guarantee.

## New formal content: non-degeneracy (every λ is reached)

By Frobenius reciprocity `V_λ ⊆ Ind(V_ξ ⊠ V_ν) ⟺ c^λ_{ξν} > 0`, and any skew
shape of size `n_block` admits at least one LR filling, so the existence of a
child reduces to a purely combinatorial fact:

> **every `λ ⊢ n` with `n ≥ k` has a sub-partition `ξ ⊆ λ` of size `n − k`.**

`interface_blocks` is therefore **non-degenerate** — it returns ≥ 1 child for
every `λ`, so the combiner never silently drops a block.

- **Lean (sorry-free, lean-direct exit 0):**
  [`QOU/BraidsAndKnots/CombinerBranchingCompleteness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/CombinerBranchingCompleteness.lean)
  — `exists_subpartition_of_size` (induction removing one Young box at a time:
  `dropLastBox`, `dropLastBox_sub`, `dropLastBox_pos`, `dropLastBox_sum`), with
  pointwise containment `IsSubPartition` (reflexive + transitive).
- **Verifier (exit 0):**
  [`docs/audits/scripts/combiner_branching_completeness.py`](scripts/combiner_branching_completeness.py)
  — for every canonical combiner split `(n_inner,n_block) ∈ {(3,3)→6, (6,3),(3,6)→9,
  (9,3),(6,6),(3,9)→12}`, confirms `{λ : ∃(ξ,ν), c^λ_{ξν}>0} = partitions_of(n)`
  (shape-level), and cross-checks with the canonical LR enumerator `lr_coef` that
  every block has an LR child.

| split `(n_inner,n_block)` | `n` | `#parts(n)` | reached | non-degenerate |
|---|---|---|---|---|
| (3,3) | 6 | 11 | 11 | ✓ |
| (6,3),(3,6) | 9 | 30 | 30 | ✓ |
| (9,3),(6,6),(3,9) | 12 | 77 | 77 | ✓ |

## Net

The combiner is **complete and non-degenerate**: per-λ completeness is the corpus
narrative (Wedderburn + orthogonal-isotypic sum); the dual non-degeneracy ("every
λ reached") is now machine-checked via `exists_subpartition_of_size` and verified
empirically over the actual combiner sizes. This is a *correctness guarantee* for
the operator route, not a new derivation — no fit, no new physics claim.
