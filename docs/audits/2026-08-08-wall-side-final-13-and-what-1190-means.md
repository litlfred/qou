# The last 13 wall-side blocks, and what 1190/1190 does not mean

**Date:** 2026-08-08
**Scope:** the residual `wall-side-correct` FAIL set after the MED-59 drain (#4758, #4759).
**Beans:** `qou-med65` (closes), `qou-mtc9` (grows), `tmvac` (cited).

The MED drain took the sweep to 1177/1190 and left 13. This records reading all
13, and one finding about the metric itself that matters more than the 13.

## 1. The metric is weaker than it looks

`WALL_ACK_RE` in `qa-checkers-voice.ts` is:

```js
/archimedean|over\s+\$?\\?mathbb\{R\}|over\s+ℝ|specialise|specialize|
 numerical evaluation|codata|experimental|§7c|base.?ring/i
```

A **keyword match**. Any `authorNote` containing the string `§7c` or `base ring`
flips a block from FAIL to PASS, regardless of what the note says. The checker
cannot distinguish

- *"ℝ is load-bearing here, because the theorem is positive-definiteness"* from
- *"ℝ is gratuitous and I am not fixing it"*.

This is demonstrated in-tree by `qou-infra-discharges-goncharov-zeta5`, which now
**passes** while its own acknowledgement states plainly that its `ℝ` is *not*
load-bearing. That is deliberate: the note is honest, and the block passes anyway.

**So `1190/1190` means "every block carries a note", not "every base ring is
correct".** Any future reader quoting the number should quote this sentence with
it. Chasing the number is not the same as doing the work, and the number cannot
tell the difference.

## 2. Four genuine violations — ported

| block | why `ℝ` was wrong |
|---|---|
| `collatz-contact-boundary` | The carrier arithmetic is `[2]_q = q + 1` and the hypothesis `[2]_q = 0`. The file's own prose names the ambient object as the Skein module `ℤ[q^{±1}]` — a Laurent ring. The `ℝ` contradicted the manuscript the file encodes. |
| `nucleon-ordering-factorization` | `trM_N`, three Wedderburn channel weights, and the `q`-scalars — all algebraic in the coefficient ring. |
| `lr-tensor-character-bridge` | The Littlewood–Richardson bridge: a character equals a sum of ℕ-multiples of character products. Natural home is ℤ or ℚ(q). |
| `habiro-ring` | Two independent reasons; see below. |

### The Habiro case is the interesting one

`habiro-ring.lean` opens *"The Habiro ring is the inverse limit of `ℤ[q] / ((q;q)_n)`"*
and then models that ring by functions `ℝ → ℝ`. Beyond contradicting its own first
line, this violates the framework's own doctrine: per AGENTS.md
§"Im(q) at fibre vs observable level", a Habiro element is a **fibre-level**
object where `q` is a formal variable and may be complex, while `Im(q₀) = 0` is an
*archimedean* constraint applying only after the `τ` functor. Typing the Habiro
ring over `ℝ` imposes an observable-level constraint on a fibre-level object —
the exact conflation that section was written to prevent.

**Noted, not fixed:** `z-habiro-ring.lean:58` carries the identical defect —
`embedQ (f : ℝ → ℝ)` for what its own docstring calls *"the constant inclusion
`ℤ[q^{±1}] ↪ ZHabiroElement`"*. It is **not** in the wall-side FAIL set, so it is
either acknowledged or passing. Per §1 that tells us nothing about whether its
base ring is right.

## 3. A third self-assuming projection, found by accident

`nucleon_ordering_factorization` had a docstring reading *"Honest `sorry`: this is
the Wedderburn block decomposition … not yet in Lean"* above a body of
`exact ctx.factorization_ident` — and that class field stated the theorem's
conclusion verbatim.

This is the third instance of the §3b-cond item-5 shape in one session:

| declaration | found |
|---|---|
| `confinement_categorical` | bean `qou-mtc9`, fixed |
| `nucleon_ordering_factorization` | here, fixed |
| `lr_tensor_character_bridge` (`bridge` field) | here, **not** fixed |
| `e_infinity_identifications` (six conjuncts) | here, **not** fixed |

Two of the four also carried a docstring *claiming a `sorry` that was not there*.
That is the diagnostic worth generalising: **when a docstring says "sorry" and
`#print axioms` says otherwise, the class is positing the conclusion.** A cheap
detector could compare the two directly, and would have caught all four.

The two unfixed ones are recorded on `qou-mtc9` rather than fixed here — a
base-ring pass is the wrong vehicle for a proof-integrity decision, which is the
same reason `qou-mtcx` declined to fix `confinement_categorical`.

## 4. Eight acknowledged, each on its own evidence

No boilerplate; each note cites that file's own construct. The one worth
recording is `gram-matrix-h3-symbolic`, because the **data** is misleading: the
Gram entries are rational functions of `u` and the determinant factors are
polynomials, so an entry-level read says "algebraic, port it". The *theorem* is
positive-definiteness for `u > 1`, proved through a chain of `linarith` /
`positivity` lemmas. Over `ℂ` the denominator `u² + 1` vanishes outright.

Read the statements, not the field types.

## Remaining

| queue | remaining |
|---|---|
| wall-side | **0** — but see §1 for what that is worth |
| `lean.ref` — ref names a decl absent from its own sibling | 22 |
| `lean.ref` — no formalisation at all | 10 |
| wall-side WEAK (bare `ℝ`, no archimedean construct) | 32 — untouched, and correctly so; these were never a FAIL set, they are where a gratuitous `ℝ` is most likely to hide |
| §3b-cond self-assuming projections | 2 known-unfixed (above), plus whatever a docstring-vs-axioms detector would surface |
