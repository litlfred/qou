---
# wpdb
title: 'The curvature-rank chain assumes a word-depth -> partition-depth bridge that is stated nowhere'
status: todo
type: task
priority: normal
created_at: 2026-08-16T02:30:00Z
updated_at: 2026-08-16T03:30:00Z
---
Surfaced in #5183 as an open question, investigated and confirmed. Full
evidence:
[`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md`](../docs/audits/2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md).

**The gap.** Five sites assume

    Z^(k)(A) = span{ e_lambda : depth_GB(lambda) = k }

and all five cite `prop:curvature-rank-gb-stratification` for it. That
proposition states `J^r/J^{r+1} = {T_w : r(T_w) = r}` — a statement about
**words**. Its Lean context class carries `rank_T_w : A -> N` and
`quotient_set : N -> Set A`; **no partition type appears in it at all**.

The partition side, `gbDepth lambda = max hook`, is a plain Lean `def`. Nothing
relates the two — verified by an exhaustive pass over `QOU/**/*.lean` for a
declaration mentioning both.

**Sites:** `prf:phi-q-categorical-truncation` Step 3;
`prf:quantum-dilogarithm-stratified` Step 3(b) (corrected in #5183);
`prf:unified-curvature-rank-mass-formula`; `conj:two-filtration-bridge` (which
*presupposes* the grading rather than supplying it); and
`computations/gb_depth_period_bring_fig8.py`, which flags the two filtrations as
"SEPARATE" with an open relationship *and* attributes the partition one to the
word proposition in the same sentence.

**Scope-(a).** Unstated, not false. It may be true and provable. Two reasons to
expect it is not trivial: the word filtration counts rewrites to normal form
while the partition depth is a hook statistic; and the `(2,2)` self-conjugate
cell of `H_4(q)` (max-hook 3) is exactly where the neighbouring
iterated-integral comparison found the two filtrations disagreeing.

**Why it matters.** It is load-bearing for the whole curvature-rank mass-formula
chain — the `m^(k)` functionals, the Terms 1-7 mapping, the Phi_q truncation
depth. All of it is conditional on a step nobody has written down.

**Next step.** Give the identification its own block, so downstream blocks cite
a statement that says what they use. If it is conjectural, the three `prf:`
blocks become downstream of a conjecture and §3b applies — which is precisely
why it should be named rather than left inside a citation.

## Attempted the proof — NOT closed, but the partition side is now measured (2026-08-16)

Tried to prove the bridge. Did not close it. What the attempt did establish,
sorry-free, is a sharp fact about the partition side that bears directly on the
downstream use — `QOU/BraidKnot/TwoFiltrationBridge.lean`:

| theorem | content |
|---|---|
| `gbDepth_eq_corner` | `gbDepth μ = rowLen 0 + colLen 0 - 1` — the max hook is always the **corner** hook |
| `gbDepth_eq_of_border_eq` | two diagrams sharing a first row and column have the same depth, however different their interiors |
| `four_le_card_of_mem_one_one` | a non-hook needs ≥ 4 cells, so every partition of `n ≤ 3` is a hook |
| `gbDepth_const_on_H3` | all three `H₃` blocks have depth `3` |

**The last one is the point.** `prop:phi-q-categorical-truncation` sets
`k⋆(T_w) := max{gbDepth λ : λ ∈ supp(T_w)}` and states the truncation depth is
*"structurally locked to the NF support of `T_w`"*. At `n = 3` that maximum is
`3` for **every** `T_w` with nonempty support — constant, so it locks onto
nothing. And `n = 3` is the single-nucleon case (`schur-weyl-mass-decomposition`:
the symmetric / standard / antisymmetric blocks), not a toy.

Scope-(a): the grading is degenerate at `n ≤ 3`, not the truncation false. It
becomes non-trivial from `n = 4`, where `(2,2)` has depth `3` against `4` for
the four hooks.

**Why the bridge itself did not yield.** Two obstructions, neither dissolved:

1. **Well-definedness.** `r(T_w)` is "the number of `R_H`/`R_YB` rewrites needed
   to reach normal form" — a property of a **word**, not of its image in
   `H_n(R,q)`. Different words for the same algebra element need different
   counts. The proof's own Step 2 says `J^ℓ` is *"the image of `I^ℓ` under the
   quotient map"*, and `H_n = ℂ⟨σ⟩/I`, so that image is **zero** for `ℓ ≥ 1`.
   As written the filtration is either trivial or not a function on the
   quotient. This needs resolving before there is a statement to prove.
2. **Coarseness mismatch.** `gbDepth` is determined by `(λ₁, λ'₁ )` alone
   (`gbDepth_eq_of_border_eq`), taking values in `[2√n − 1, n]`. Any candidate
   word-side rank would have to be equally blind to the interior of `λ`, which
   is a strong constraint on what `r(T_w)` could be.

**Next honest step:** fix the definition of the word filtration so it is
well-defined on `H_n(R,q)` — as a filtration by *ideals* of the algebra, not by
rewrite counts on representatives. Until then the bridge has no well-formed
statement, which is a sharper diagnosis than "unproved".
