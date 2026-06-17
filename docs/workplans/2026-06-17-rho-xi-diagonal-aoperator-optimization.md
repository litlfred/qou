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

## Plan / status
- [ ] `rho_xi_diagonal.py` — sparse full-matrix builder (A≤5) + diagonal-only
      builder (A=6, O(d) memory).
- [ ] Verify at A=4 (λ⊢12, the `_self_test` combiner identity) — diag-only +
      sparse reproduces `chi_young` to `<1e-25`; sparse == dense `prod`.
- [ ] Confirm diag-only `trace_A_kron` == full `trace_A_kron` (validates the
      block-diagonal-in-`V_ξ` structure numerically).
- [ ] Measure speedup; honestly scope the A=6 large-ξ time wall (the genuine
      Rust-engine / research-scale piece).

## Honest framing
Per the main-merged bond-dimension verdict `χ_eff(k)=p(3k)` and the #2441 closure
of the dense-SDP lever (the operator-cumulant route this feeds is structurally
gated), this is **validation/optimization infra** — it makes the *independent*
A≥4 cross-check feasible and removes a memory wall; it does **not** change any
production number or unlock new physics. No fit, nothing rewired.

## Cross-links
- [`a_operator_recursive.py`](../../computations/a_operator/a_operator_recursive.py) — `interface_blocks` (A block-diagonal in V_ξ).
- [`a_operator_recursive_he4_crosscheck.py`](../../computations/a_operator/a_operator_recursive_he4_crosscheck.py) — the direct-`ρ_ξ` consumer this optimizes.
