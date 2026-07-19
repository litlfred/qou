# H₄ Markov-trace cyclicity — the blocker is a `whnf` explosion, not `ring` size

**Date:** 2026-07-19
**Branch:** `claude/tau-f3-h4-markov-2026-07-19`
**PR:** #4046
**Bean:** `qou-g6vb` (F4 research core)
**Target:** `QOU.Machinery.H4.trM_cyclic` in
[`MarkovTraceH4.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceH4.lean)
— the one remaining cited `sorry` in the H₄ module.

## TL;DR

`trM_cyclic : trM (mulNF u v) = trM (mulNF v u)` is machine-validated in the
Python infra (`hecke_regular_nf_table.py::self_validate`, cyclicity on sampled
pairs) and held as an honest cited `sorry`. A tactic study this session
established that the Lean obstruction is a **kernel/elaborator `whnf`
explosion** intrinsic to the concrete `![…]` cons-vector encoding, **not** a
`ring`-normalization size issue. The bilinearity reduction — the plan recorded
in the prior sorry comment — was implemented and shown **not** to rescue it:
even a *single* depth-6 word `W_j u` blows up. The proof stays open; the
tractable path is a representation change (Matrix.Reflection) or an abstract
regular-representation trace argument. No laundering — the `sorry` is real,
cited, and now precisely documented.

## The object

The algebra product on the Fin-24 GB normal-form module is bilinear:

```
mulNF h u v = ∑_j v_j • (W_j u),   W_j u := u · b_j
```

where `W_j` is the fixed composition of the generator right-actions
`mulσ0/1/2` (each a concrete `![…] : Fin 24 → R` vector) along the reduced word
of the basis element `b_j = T_{S[j]}`. Hence

```
trM(u·v) = ∑_j v_j · trM(W_j u),   trM(W_j u) = ∑_i u_i · A_{j,i},
A_{j,i} := trM(b_i · b_j)   (the Gram matrix of the trace form)
```

and **cyclicity ⟺ `A` is symmetric** (`tr(b_i b_j) = tr(b_j b_i)`), i.e. the 276
off-diagonal Gram identities. That reduction is mathematically correct; the
issue is purely getting Lean to *evaluate* `trM(W_j u)`.

## What was tried (all infeasible)

The linearity half is cheap and works (`trM_add`/`trM_smul` already sorry-free;
pulling the `v_j` scalars out of the sum is fast). The blocker is evaluating one
`W_j u` — a depth-≤6 nested composition of the `mulσ` `![…]` vectors — into any
explicit or summed form. Six strategies, each hitting
`(deterministic) timeout at whnf`:

| # | strategy | result |
|---|----------|--------|
| 1 | brute `simp [mulNF, mulσ*, trM, TRM, Fin.sum_univ_succ]; ring` | whnf timeout @ **4M** heartbeats (~3.5 min) |
| 2 | per-word `simp` on one depth-6 word `trM(W₂₃ u)` | whnf timeout @ 200k |
| 3 | per-word `rfl`: `W₂₃ u = ![flat] := rfl` | whnf timeout @ 200k |
| 4 | incremental `have`-chain, each layer `:= by rw [prev]` (auto-`rfl`) | whnf timeout @ 200k on **layer 2** |
| 5 | incremental `have`-chain, each layer `rw [prev]; funext i; fin_cases i <;> rfl` | whnf timeout @ 200k on layer 2 |
| 6 | (control) single layer `mulσ0 h u = ![flat] := rfl` | **succeeds** (inner arg is the opaque `u`) |

**Root cause.** Extracting entry `i` of `mulσ_g h (W' u)` references specific
indices of the inner word `W' u` (e.g. `(W' u) 3`, `(W' u) 6 + h·(W' u) 3`).
Top-down `Matrix.cons` indexing re-derives those inner entries *per outer
index*, with no memoization, so the cost is exponential in the composition
depth. Strategy 6 works only because the inner argument is the free variable
`u` (indexing `u 3` is inert). Once one `mulσ` layer sits inside another
(depth ≥ 2), the explosion fires — which is why the bilinearity reduction,
though it isolates the words, does not make any individual word tractable.

## The tractable path (future work)

1. **Matrix.Reflection re-encoding (preferred).** Define the three generator
   right-actions as concrete `Matrix (Fin 24) (Fin 24) R` (Python already has
   the `gen[i]` matrices) and evaluate `trM(W_j u) = TRM ⬝ᵥ (M_{g₁}⋯M_{g_k}).mulVec u`
   via `Mathlib.Data.Matrix.Reflection` (`mulᵣ`/`dotProductᵣ`, List-fold
   normalisation instead of `Fin.sum_univ_succ`). The Gram matrix `A = TRMᵀ · M`
   can even be precomputed by Python so Lean only checks a concrete 24×24
   symmetric-matrix equality. **Blocked in this sandbox:** the `!![…]` notation
   and reflection lemmas live in `Mathlib.Data.Matrix.Notation`, whose olean is
   absent from the restored `lake-cache` (Mathlib source is not present either,
   so it cannot be compiled here). Needs a full-build session.
2. **Abstract regular-representation trace.** Define `H₄` as an algebra, `trM`
   as the trace of the left-multiplication operator, and derive cyclicity from
   `tr(AB) = tr(BA)` (`Matrix.trace_mul_comm`). Heavier setup, but no
   per-element computation.

## Disposition

- `trM_cyclic` stays an honest cited `sorry`; its docstring is updated with the
  precise `whnf`-explosion finding and the two forward paths.
- No wiring, no axiom, no vacuous body. The other H₄ results (`trM_add`,
  `trM_smul`, `trM_markov_σ2`) remain sorry-free.
- Bean `qou-g6vb` records the finding; the re-encode is the next actionable step
  once a full Mathlib build is available.
