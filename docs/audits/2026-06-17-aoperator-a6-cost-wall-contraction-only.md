# A-operator combiner: the contraction-only streaming form + the irreducible A=6 cost wall (2026-06-17)

**Branch:** `claude/aoperator-contraction-only-rust-2026-06-17`
**Picks up:** the owner directive *"continue with rust and contraction-only"*
after #2449 (diagonal-only `ρ_ξ`, the memory enabler). Applies **formalize-first**
(bound the expensive build before launching it).
**Discipline:** derive-or-refute; exact (verified at A=4 to 50 dps); no fit,
nothing rewired.

## Contraction-only streaming form (the deliverable)

Since `A^λ_{ξν}` is block-diagonal in `V_ξ` (#2449), the combiner contraction is

```
Σ_{ξ,ν} Tr[A^{ξν}·(ρ_ξ(W)⊗ρ_ν)] = Σ_ξ Σ_a v_a · diag(ρ_ξ(W))[a],
    v_a = Σ_ν Σ_{b,b'} A^{ξν}_{a,b,b'} · ρ_ν[b',b]   (a scalar per inner index a).
```

[`rho_xi_diagonal.combiner_value_streaming`](../../computations/a_operator/rho_xi_diagonal.py)
precomputes `v_a`, then streams each `diag(ρ_ξ(W))[a] = (ρ_ξ(W)·e_a)[a]` one
column at a time and consumes it immediately — `ρ_ξ` is **never materialised**
(`O(d_ξ)` memory, the only form that fits the largest A=6 blocks). **Verified
exact** against `chi_young` at A=4 (`max|chi_young − streaming| = 8.1e-49`,
[`aoperator_a6_cost_and_contraction.py`](../../computations/probes/aoperator_a6_cost_and_contraction.py)).

## The cost wall (formalize-first — decisive, no Rust build needed)

The diagonal/contraction cost is `Σ_{ξ⊢n_inner} d_ξ²·|W|`. Since
`Σ_{ξ⊢n} d_ξ² = n!`, this is `n_inner!·|W|`, **dominated by the single largest
block** `d_max²·|W|`. The diagonal/streaming reorganisation removes the `O(d²)`
*memory* wall but **not** the `O(d²)` *time*: a generic seminormal word-rep has
no low-rank diagonal, and the *weighted* trace `Tr[D_v·ρ_ξ(W)]` breaks the
class-function structure, so **Murnaghan–Nakayama gives no shortcut** (the plain
character `χ^ξ(W) = Tr ρ_ξ(W)` is cheap; the `v_a`-weighted diagonal is not).

| A | `n_inner` | `#ξ` | `d_max` | `Σd²=n!` | `|W|` | ops | mpmath 50dps | rust (~7×) | float64 (coarse) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 4 | 9 | 30 | 216 | 3.6e5 | 47 | 3.4e7 | 17 s | 2.4 s | 0.2 s |
| 5 | 12 | 77 | 7 700 | 4.8e8 | 59 | 5.7e10 | 7.9 h | **66 min** | **4.7 min** |
| 6 | 15 | 176 | 292 864 | 1.3e12 | 71 | 1.9e14 | 1075 d | **150 d** | **10.7 d** |
| 7 | 18 | 385 | 1.6e7 | 6.4e15 | 83 | 1.1e18 | — | — | — |

## Rust verdict — evaluated, not built

`cargo`/`rustc` 1.94.1 are present; `maturin` is absent (pip-installable). Building
the `pyhecke_native` wheel buys the **~7× constant factor** in the table. That is
genuinely useful for **A=5** — it turns the exact (50-dps) A=5 cross-check from
7.9 h (mpmath) into ~66 min — but it **cannot reach A=6** (150 days for the
largest block). Per formalize-first (the bound is decisive), the wheel is **not
built here**: it does not change the A=6 verdict, and A=5 is already float64-
reachable in ~5 min. Building it is recorded as an optional follow-up for an
*exact* A=5 cross-check.

## Honest scope — what is and isn't reachable

- **A=4** — done, exact, 50 dps (#2449 + streaming here).
- **A=5** — **done** (#2459, 2026-06-18); see the RESULT section below. *Cost
  correction:* the "float64 ~5 min" is the ρ_ξ **diagonal** builds only; the naive
  combiner (rebuilding the mpmath `interface_blocks` per λ⊢15) ran **> 2.75 h** — an
  exact regrouping cuts it to **11 s**, so the whole A=5 cross-check is ≈ 2 min,
  float64. (Exact 50 dps still ~66 min Rust / ~8 h pure mpmath, unbuilt.)
- **A=6** — **out of reach for the independent cross-check by any rep-based
  backend** (float64 10.7 d, Rust 150 d). The only A=6 path is a genuinely
  rep-free weighted-trace method (none known — MN does not apply) or the
  fine-Bratteli transfer itself, which is the *production* path and so not an
  *independent* check.

## A=5 cross-check — RESULT (2026-06-18, #2459)

The operator-valued combiner **reproduces the production fine-Bratteli transfer at
A=5 (⁵He)** — `tr_M = Σ_λ y_λ χ^λ` over all 176 λ⊢15, with the contraction-only
`diag(ρ_ξ)` (ξ⊢12, `d_ξ ≤ 7700`):

| check | result | tol | status |
|---|---|---|---|
| A4-a: float64 regrouped combiner vs exact `chi_young` (λ⊢12) | `1.42e-14` | `1e-6` | ✓ |
| A4-b: float64 regrouped combiner vs original mpmath combiner (λ⊢12) | `1.78e-15` | `1e-6` | ✓ |
| A5: per-λ max\|χ_comb − χ_transfer\| (all 176 λ⊢15) | `1.89e-12` (rel `9.86e-15`) | rel `1e-8` | ✓ |
| A5: `tr_M` combiner vs transfer | rel `1.29e-15` | `1e-5` | ✓ |

`tr_M_combiner = tr_M_transfer = 0.01483482681` (`|Δtr_M| = 1.91e-17`). Float64,
but the agreement sits at the double-precision floor — the long word product does
not lose the feared ~1e-8. Witness:
[`aoperator_a5_crosscheck.witness.json`](../../computations/probes/aoperator_a5_crosscheck.witness.json)
(`allPassed=true`).

### The combiner cost — corrected (the regrouping)

The cost table above bounds the ρ_ξ **diagonal** builds (`Σ_ξ d_ξ²·|W| = n!·|W|`,
104 s float64 at A=5). It does **not** bound the **combiner contraction**: the
naive form rebuilds the production `interface_blocks` (mpmath `A^λ_{ξν}`, an
`O(d_ξ)` mpmath loop) **once per λ — all 176 λ⊢15** — and ran **> 2.75 h** without
finishing. The fix is an exact regrouping of the partial trace (identical
arithmetic, `A` never materialised):

    χ^λ = Σ_{(ξ,ν)} Σ_a dg[a]·( Σ_w bridge(cfirst[w] − c_a[a])·G[w] + d_coef·ΣG ),
    G[w] = Σ_{b,b'} rb[b',b] Σ_kk Cinv[j1,w]·C[w,j2]   (a-independent).

`G[w]` comes from the tiny `nW×nW` block-to-standard alignment; the only `O(d_ξ)`
work is then a float64 sum with `bridge(δ)` cached by integer δ. Combiner over all
176 λ⊢15: **11 s** (≈ 900× the naive mpmath form). So A=5 is float64-reachable in
≈ 2 min total, not the diagonals-only "~5 min" the table implied. The same
regrouping does **not** rescue A=6 (the `Σ_ξ d_ξ²` diagonal wall is untouched —
the cost table stands for A≥6).

## Honest framing
Per `χ_eff(k)=p(3k)` and #2441's dense-SDP closure, the route this feeds is
structurally gated. The contraction-only streaming form is the correct
`O(d)`-memory object and is exact; the A≥5 cross-check it enables is
validation/optimization infra, not a production-value change. No fit, nothing
rewired.

## Cross-links
- [`rho_xi_diagonal.py`](../../computations/a_operator/rho_xi_diagonal.py) — `combiner_value_streaming` (+ #2449's diagonal-only builders).
- [`aoperator_a6_cost_and_contraction.py`](../../computations/probes/aoperator_a6_cost_and_contraction.py) — the cost table + A=4 streaming verification.
- [`aoperator_a5_crosscheck.py`](../../computations/probes/aoperator_a5_crosscheck.py) (#2459) — the A=5 ⁵He cross-check + the regrouped float64 combiner (`combiner_chi_fast`); witness `aoperator_a5_crosscheck.witness.json`.
- [`2026-06-17-rho-xi-diagonal-aoperator-optimization.md`](../workplans/2026-06-17-rho-xi-diagonal-aoperator-optimization.md) (#2449) — the diagonal-only memory enabler this builds on.
