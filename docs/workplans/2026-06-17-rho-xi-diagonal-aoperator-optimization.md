# ρ_ξ optimization: only diag(ρ_ξ) is needed (A^λ_{ξν} is block-diagonal in V_ξ) — the A-operator A≥4 speedup/feasibility enabler (2026-06-17)

**Branch:** `claude/recursive-rho-xi-aoperator-2026-06-17`
**Picks up:** the A-operator-program follow-on the Δ_λ/A-operator triage flagged —
*"a production wiring would compute `ρ_ξ` recursively"* (the ⁴He cross-check
[`a_operator_recursive_he4_crosscheck.py`](../../computations/a_operator/a_operator_recursive_he4_crosscheck.py)
builds `ρ_ξ` directly, `~24 min` at `d_ξ≤216`). Coordinated on the active (now
stalled) wiring sibling #2371.
**Discipline:** formalize-first; derive-or-refute; exact (verify against the
direct build to 50 dps); no fit, no production-value change.

## The finding — the full `ρ_ξ(W_inner)` is computed but only its *diagonal* is used

`interface_blocks` ([`a_operator_recursive.py`](../../computations/a_operator/a_operator_recursive.py))
builds `A^λ_{ξν}(I)` **block-diagonal in `V_ξ`** — it only ever sets entries
`A[a·d_ν+b, a·d_ν+b']` with **matching inner index `a`** (line 303; the proven
structural result, docstring §"A^λ_{ξν} is block-diagonal in the V_ξ index"). In
the contraction

```
Tr[A·(ρ_ξ⊗ρ_ν)] = Σ_{a,a',b,b'} A[a·d_ν+b, a'·d_ν+b'] · ρ_ξ[a',a] · ρ_ν[b',b]
```

every `a' ≠ a` term multiplies `A[...] = 0`. So **only `ρ_ξ[a,a]` — the diagonal
of `ρ_ξ(W_inner)` — contributes.** Yet the cross-check builds the full dense
`d_ξ×d_ξ` matrix via `prod(exact_seminormal_matrices(ξ), W_inner)` (`O(d_ξ³·|W|)`
time, `O(d_ξ²)` memory) and then uses only its diagonal.

## The optimization

1. **Sparse generators.** The Young seminormal `σ_g` are block `1×1`/`2×2` on the
   SYT(ξ) basis (≤ 2 nonzeros/row). Right-multiplying by `c·σ_g + d·I` is `O(d²)`,
   not `O(d³)` — a `~d_ξ`-fold constant speedup (≈216× at the largest ξ⊢9).
2. **Diagonal-only, column-by-column.** Since only `diag(ρ_ξ)` is needed,
   compute `diag(ρ_ξ(W))[a] = (ρ_ξ(W)·e_a)[a]` one column at a time via sparse
   mat-vec chains: `O(d²·|W|)` time but **`O(d)` memory** — removes the `d×d`
   storage wall that blocks the largest A=6 blocks (`d_ξ≤2.9·10⁵` at ξ⊢15).

Both are exact (same arithmetic, reorganised) and verifiable against the direct
build + the `chi_young` combiner identity to 50 dps.

## Results (verified, A=4, ξ⊢9, d_ξ≤216 — `rho_xi_diagonal_verify.py`)

- [x] `rho_xi_diagonal.py` — sparse generators built directly (`O(d)` per gen,
      no `d×d` materialization); `rho_word_full_sparse` (A≤5) +
      `rho_word_diag` (`O(d)` memory). **Rust-free** (pure-Python
      `young_seminormal` rule — no `pyhecke_native` wheel).
- [x] **Exact:** `max|full_sparse − dense| = 1.6e-61`,
      `max|diag − dense.diagonal| = 2.3e-61` (to the 60-dps floor).
- [x] **Combiner identity (diag-only) vs `chi_young`:** `8.1e-49 < 1e-25` ✓ —
      the whole A=4 combiner reproduces the independent character using only
      `diag(ρ_ξ)`.
- [x] **Block-diagonal-in-`V_ξ` confirmed numerically:** diag-only `trace_A_kron`
      == full `trace_A_kron` to `6.2e-61` — the off-diagonal inner index truly
      never contributes, so only `diag(ρ_ξ)` is needed.
- [x] **Speedup** (all ξ⊢9, 5-crossing inner word): dense `prod` `138.2 s` →
      sparse full `8.0 s` (**17×**) → diagonal `1.67 s` (**83×**).

| ρ_ξ build | time | vs dense | memory |
|---|--:|--:|--|
| dense `prod` (current cross-check) | 138.2 s | 1× | `O(d²)` |
| `rho_word_full_sparse` | 8.0 s | 17× | `O(d²)` |
| `rho_word_diag` (diagonal-only) | 1.67 s | **83×** | **`O(d)`** |

## A=6 scoping (honest)

The diagonal-only builder is `O(d²·|W|)` time, `O(d)` memory. The memory win
removes the `d×d` storage wall, so the bulk of ξ⊢15 (the smaller-dim blocks) and
all of A=5 become feasible. The **largest** ξ⊢15 block (`d_ξ ≤ 2.9·10⁵`) stays
**time**-bound — `O(d²·|W|) ≈ 10¹¹` mpf-ops at 50 dps is still infeasible in pure
mpmath. Fully closing the biggest A=6 block needs either the Rust seminormal
kernel (`pyhecke_native`, which the original used) or a contraction-only scheme
that never iterates all `d` columns — the genuine research-scale piece (and the
wall the wiring sibling #2371 is stalled on). This PR removes the memory wall and
gives a constant + memory speedup; it does not by itself make the largest A=6
block tractable.

## Honest framing
Per the main-merged bond-dimension verdict `χ_eff(k)=p(3k)` and the #2441 closure
of the dense-SDP lever (the operator-cumulant route this feeds is structurally
gated), this is **validation/optimization infra** — it makes the *independent*
A≥4 cross-check feasible and removes a memory wall; it does **not** change any
production number or unlock new physics. No fit, nothing rewired.

## Wiring status — NOT wired (gated on a Lean proof of block-diagonality)

The diagonal-only contraction is correct **iff** `A^λ_{ξν}` is block-diagonal in
`V_ξ`. That structural claim is currently a rigorous argument
([`a_operator_recursive.py`](../../computations/a_operator/a_operator_recursive.py)
docstring) **numerically confirmed to `6.2e-61`** (this probe) — but it is **not
Lean-proved**: the A-operator's only Lean is the `WenzlAOperator` §3b-cond
*conjecture* class (instance-less), modelling the *scalar* `combinerValue`
recursion only, not the matrix `A^λ_{ξν}` or its block structure. Per the owner's
gate (*wire only if 100 % Lean-proved*), the diagonal-only builder is therefore
**kept as a verified standalone module, NOT swapped into the production /
cross-check hot path.** Wiring is unblocked once block-diagonality is formalised —
itself research-grade (the reason the A-operator is a conjecture class). The
module + this verification stand as the exact, ready optimisation.

## Cross-links
- [`a_operator_recursive.py`](../../computations/a_operator/a_operator_recursive.py) — `interface_blocks` (A block-diagonal in V_ξ).
- [`a_operator_recursive_he4_crosscheck.py`](../../computations/a_operator/a_operator_recursive_he4_crosscheck.py) — the direct-`ρ_ξ` consumer this optimizes.
