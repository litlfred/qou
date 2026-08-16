---
# wpdb
title: 'The curvature-rank chain assumes a word-depth -> partition-depth bridge that is stated nowhere'
status: todo
type: task
priority: normal
created_at: 2026-08-16T02:30:00Z
updated_at: 2026-08-16T02:30:00Z
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
