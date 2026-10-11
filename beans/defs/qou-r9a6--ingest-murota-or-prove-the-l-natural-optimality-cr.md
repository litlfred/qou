---
# qou-r9a6
title: 'Ingest Murota (or prove the L-natural optimality criterion): the Xbot arc''s one load-bearing citation resolves to nothing in the corpus'
status: todo
type: task
priority: normal
created_at: 2026-10-11T08:35:32Z
updated_at: 2026-10-11T08:35:32Z
parent: qou-3e6w
---

The `Xbot` L♮ route — which certified `e_inf` without G1 and closed `qou-as81` — rests on
**Murota, *Discrete Convex Analysis* (SIAM 2003), Ch. 7: the L♮ optimality criterion**, that for
an L♮-concave `g : ℤ^n → ℝ ∪ {−∞}` a domain point is a *global* maximiser iff no `±χ_S` move
improves it.

That theorem is what turns `rev_e_infinity_xbot_lnatural_probe.py`'s M5 steepest-ascent fixed
point into **the** integer maximum. Without it M5 certifies a local optimum and nothing more. It
is therefore load-bearing for:

- the G1-free cut of **25** (M6),
- `e_inf` certified without G1 (the join probe, 4/4),
- the close of bean `qou-as81`.

## The corpus cannot check it

Measured on `main` after the 335 commits that landed on 2026-10-10/11: **0 hits** for *Murota* /
*discrete convex analysis* in `library/INDEX.md`, across **60,059** library files. A six-path
corpus-grep the day before — `library/INDEX.md`, `library/*/sections/`, **`library/*/ocr/`** (the
fourth tier the documented path misses), `beans/`, `content/`, `folio/`, `computations/`,
`docs/` — returned one unrelated hit (`s00453-026-01372-w`, Algorithmica 2026, concentration of
submodular functions). So the citation resolves to nothing a reader or a later agent can open.

**This is not a defect in the probe.** Citing a standard published theorem is legitimate. What
is recorded here is that the corpus holds no copy, so nothing in the repository can verify the
step, and a referee asking "where is the criterion?" has no in-repo answer.

## The companion result is already closed, which is why this one stands out

Murota §7.1 — the *sufficient condition*, that separable concave plus concave functions of
pairwise differences is L♮-concave — was the probe's other citation and **no longer needs one**:
`QOU/BraidKnot/LNaturalConcaveForm.lean` proves it (8 theorems, sorry-free), via
`concave_exchange_inward` for the separable part and `parity_spread` for the differences. So the
arc is one theorem away from citation-independence, and it is a specific, named one.

## Two ways to close it, with costs

1. **Ingest Murota** (`uploads/` → `library/<doc-id>/`). Cheapest by far, makes the citation
   resolvable, and pays off beyond this arc — discrete convex analysis is the right frame for
   any integer-programming structure in the corpus. Does **not** make the step machine-checked.
2. **Prove the criterion.** For the `±χ_S` direction the standard route is: L♮-concavity gives
   that the "steepest" move is an s-t min cut because the `χ_S` gain is a supermodular set
   function (the probe's M4 already verifies the min-cut move against brute force over all `2^n`
   subsets, both signs — so the *implementation* is checked, just not the criterion). Expensive,
   and the right scope is a Lean file beside `LNaturalConcaveForm.lean`.

**Recommendation (judgement, not a finding): do (1) now and treat (2) as optional.** The
mathematics is not in doubt; what is missing is that the repository cannot show its own work on
a load-bearing step of a closed arc.

## Default if nothing is done

`qou-as81` stays correctly closed, the cut of 25 stays correct, and the arc keeps one unresolvable
citation. Nothing breaks — this is about auditability, not correctness.
