# The binding weight is the Markov y_λ — the Plancherel W_λ is doubly excluded

**Date:** 2026-08-01 · **Branch:** `claude/binding-weight-markov-pinning-2026-08-01` · **PR:** #4543
(stacks on #4491) · **Axis:** Δ_λ / binding weight · **Tier:** DERIVED pinning (Markov axiom) +
scope-(b) exclusion of W_λ (conjugation symmetry); **no fit**; nothing wired.

## 0. The prerequisite

PR #4491 showed the deuteron deficit `C_knot` is weighting-convention-dependent. The prerequisite to
*any* Δ_λ magnitude derivation is: **which weight is derived?** The binding trace is the Markov trace
`J_L = tr_M(ρ(β_L))` (§7a), and the Markov trace on the Hecke tower is **unique up to normalization**
(Jones/Wenzl) — so its Wedderburn weight is *determined*, not chosen.

## 1. The weight is pinned to y_λ (Markov axiom)

The canonical module `wedderburn_jones_markov.py` — the one the binding formula imports — solves the
weight from the Markov axiom (`markov_weights_symbolic.solve_y_lambda`, `markov_trace_recursive`) →
**`y_λ`** (Wenzl Schur principal specialization), and states plainly that the `schur_weyl_weight =
d_q(λ)²/[n]_q!` form is **"NOT the Markov-trace weight."** So the derived binding weight is `y_λ`.

## 2. W_λ is doubly excluded

| λ (n=3) | y_λ (Markov) | W_λ = d_q²/[n]! |
|---|---|---|
| (3) | 0.4154 | 0.1418 |
| (2,1) | 0.2809 | 0.6313 |
| (1,1,1) | 0.0227 | 0.1418 |

1. **Wrong trace.** `y_λ ≠ W_λ` (ratios 0.16–2.9) and `W_λ` is explicitly not the Markov weight.
2. **Conjugation symmetry (structural, scope-b).** `W_λ = W_{λ'}` — because the hook-length **multiset
   is transpose-invariant** (`hooks(λ) = hooks(λ')`, verified for all `λ ⊢ n ≤ 7`), so
   `d_q(λ) = d_q(λ')` and `W_λ = d_q(λ)²/[n]! = W_{λ'}`. But `y_λ` is **asymmetric**
   (`y_(3) = 0.4154 ≠ 0.0227 = y_(1,1,1)`) — it carries the chirality / bar-parity split. **Binding
   requires that asymmetry** (GAP-1: a conjugation-symmetric `Δ_λ` gives `g₂ = 0` for even `A`), which
   `W_λ` washes out. So a symmetric weight *cannot* be the (asymmetric) Markov weight — an exclusion
   independent of the Markov axiom.

## 3. Consequences

- **Three-walls Route 1's 33× W_λ overshoot is explained** — it re-weighted `y_λ → W_λ`, i.e. used the
  wrong trace; the overshoot is a category error, not a magnitude near-miss.
- **Corpus mislabel flagged.** `alpha_em_b2_scalar_c_probe.py:116` calls `d_q²/[n]!` the
  "Markov/Wedderburn weight" — contradicting the canonical module. (Flagged for coordination, not
  rewritten here.)
- **Honest refinement of #4491's `c-knot-not-universal`.** The 41× "convention spread" (`C_knot` 5.85
  vs 240) was **right-weight** (`y_λ`, Markov) vs **wrong-weight** (signed dim_q, not Markov) — **not a
  genuine ambiguity.** With the weight pinned to the derived `y_λ`, `C_knot = 5.85` is well-posed. (The
  #4491 §0b framing over-stated the ambiguity; this refines it.)
- **Relocates the open Δ_λ target.** The `C_knot = 5.85` deficit is **not** a weight issue — the weight
  is settled. It lives in `f^λ` / `sgn` / the `E₀` scale / the word-level. That is the sharpened target
  for the Δ_λ derivation (open, bean `qou-3q7t`).

## 4. Lean (sorry-free, lean-direct exit 0)

[`BindingWeightMarkovPinning.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BindingWeightMarkovPinning.lean):

| lemma | content |
|---|---|
| `Wq` | Plancherel weight as a function of the hook product `P` and `F = [n]!` |
| `Wq_symmetric_of_prod_eq` | `P₁ = P₂ → W_λ = W_{λ'}` (W depends only on the hook product) |
| `asymmetric_weight_ne_symmetric` | a symmetric weight cannot equal an asymmetric one — the exclusion |
| `markov_y_asymmetric_n3` | `y_(3) ≠ y_(1,1,1)` (the chirality) |
| `plancherel_W_excluded` | capstone — `W_λ` excluded, weight pinned to `y_λ` |

## 5. Anti-fit / honesty ledger

- `y_λ` read from the canonical Markov-axiom module; `W_λ` computed independently (hook lengths). No
  parameter fitted; nothing wired.
- **DERIVED** pinning (`y_λ`, Markov axiom) + **scope-(b)** exclusion of `W_λ` (conjugation symmetry, a
  proved invariant). This is **not** a Δ_λ magnitude derivation — that stays open (`qou-3q7t`); it makes
  the target *well-posed*.

| statement | status |
|---|---|
| binding weight = `y_λ` (Markov axiom, canonical module) | **DERIVED** |
| `W_λ = W_{λ'}` (hook-transpose invariance) | **verified ≤ n=7 + Lean** |
| `y_λ` asymmetric ⇒ `W_λ` excluded (chirality) | **scope-(b) + Lean** |
| the `C_knot = 5.85` magnitude / Δ_λ | **OPEN** (`qou-3q7t`) — not a weight issue |

Refs: probe
[`binding_weight_markov_pinning_probe.py`](../../computations/deltalambda/binding_weight_markov_pinning_probe.py);
`wedderburn_jones_markov.py` (canonical); PR #4491 (`C_knot`, three-walls Route 1); GAP-1 (chirality).
