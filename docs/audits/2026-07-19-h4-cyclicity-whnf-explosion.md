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

## Both forward paths assessed (2026-07-19 follow-up — owner asked to try "both")

After the whnf-explosion finding, both candidate paths were investigated against
the sibling algebra framework that landed on `origin/main`
(`HeckeH2/H3AlgebraInstance`, `HeckeH3AlgebraLaws`, `HeckeH4StabilizationRung`,
`HeckeBraidedCategoryScaffold`). Neither closes `trM_cyclic` in this sandbox;
the investigation *sharpened* why.

### The wall is Fin-24 depth-6 grinding, not cyclicity

`HeckeH3AlgebraLaws.mulNF_assoc` (Fin 6) is proved `funext i; fin_cases i <;>
simp [...] <;> ring` — it works because each of the 6 *output entries* is
computed independently and the H₃ words are depth ≤ 3. Cyclicity is a **scalar**
(the `trM` sum collapses the vector — no `funext` to split), and at Fin 24 the
words are **depth 6**. Associativity at Fin 24 would explode by the *same*
mechanism; the main-branch H₄ rung only proves *local* depth-1/2 facts
(`mulσ_hecke`, `braid`, `far_commute`, `stabilizes`, `markov_σ₂`). So the
blocker is intrinsic to Fin-24 depth-6 concrete evaluation — no per-tactic
cleverness escapes it.

### Approach 1 — Matrix.Reflection re-encode: BLOCKED + dubious

`Mathlib.Data.Matrix.Reflection` (List-fold evaluation, the one route that could
beat `Fin.sum_univ_succ`) imports `Mathlib.Data.Matrix.Notation`, whose olean is
**absent** from the restored `lake-cache` and whose source **404s at the pinned
rev `f897ebc`** (the module was reorganized upstream). Obtaining it needs a full
`lake build` (which wipes the restored oleans — the AGENTS.md hazard) or a
network cache fetch (was 403). Beyond availability: reflection is engineered for
*small* matrices (2–4×4); a depth-6 product of **24×24** matrices is ~83k kernel
multiplications, so feasibility is doubtful even with a full build. Not pursued
— high cost, dubious payoff.

### Approach 2 — abstract regular-representation trace: reduces to the OPEN general-n class

`origin/main` now makes the NF module a genuine `Ring`/`Algebra` (`H3A`, mul =
`mulNF`, `mulNF_assoc`/unit/bilinearity all sorry-free) and defines the
`MarkovStabilization` class. On such an algebra, the **regular-representation
trace** `a ↦ trace(leftMul a)` is cyclic for free (`Matrix.trace_mul_comm`).
**But `trM4` is not that trace** — it is the Ocneanu/Markov functional with the
specific weights `TRM4`, which are *not* the regular-rep weights. Identifying
`trM4` with a cyclic-by-construction trace therefore still requires either (a)
the blocked Fin-24 computation, or (b) the standard **Ocneanu induction**
(`tr(ab)=tr(ba)` by induction on word length via `tr(x·σ_top·y)=z·tr(xy)`) —
which is exactly the general-n `MarkovStabilization` instance that main leaves
**OPEN** (its binders quantify the H_∞ generator family). So the abstract route
does not shortcut the open item; it *is* the open item.

### Convergence / coordination

This confirms the main-branch direction — build the abstract algebra +
`MarkovStabilization` framework and prove cyclicity by Ocneanu induction — is
the correct and only path; brute Fin-24 computation is a dead end. This module's
`MarkovTraceH4.lean` supplies the concrete **n=4 `mulNF`** (which main's H₄ rung
does *not* — main did n=3 algebra + n=4 mulσ/trace only), so it is complementary
scaffolding, not a duplicate; `trM_cyclic` should ultimately be discharged as an
instance of the abstract cyclic-trace lemma once that lemma is proved on the
`MarkovStabilization` class, rather than re-attempted by computation here.

## Disposition

- `trM_cyclic` stays an honest cited `sorry`; its docstring points at the
  abstract-route reduction (not a computation retry).
- No wiring, no axiom, no vacuous body. The other H₄ results (`trM_add`,
  `trM_smul`, `trM_markov_σ2`) remain sorry-free.
- Bean `qou-g6vb` records the full assessment. Next actionable step is upstream:
  an abstract cyclic-trace lemma on `MarkovStabilization` (Ocneanu induction),
  which discharges `trM_cyclic` for every n at once — not an H₄-specific retry.
