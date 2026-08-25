---
# qou-s6ap
title: 'GAP: frobenius-codim-universal.lean still has 8 errors after the 100->8 repair'
status: completed
type: task
priority: normal
created_at: 2026-08-23T12:55:42Z
updated_at: 2026-08-23T13:20:25Z
---

## State

`content/quantum-observable-universe/mass-theory/frobenius-codim-universal.lean`
(928 lines) went **100 errors → 8** in PR #5533. It does **not** compile. The
four defects fixed there were structural (see the commit); the eight left are
genuine formalization work.

```
 83:17  typeclass instance problem is stuck (metavariables)
 93:35  rewrite failed: pattern not found
222:44  unsolved goals
468:83  unsolved goals
603:46  unsolved goals
784:2   simp failed with a nested error
802:23  typeclass instance stuck
854:23  typeclass instance stuck
```

Reproduce with `lean`-direct against a built import cone (see
`local/lean-environment-setup` §"VERIFY a single file with lean-direct").

## Why it matters more than one broken file

Three Lean files cite `QOU.BraidKnot.frobenius_codim_universal` in their
docstrings as a result they rely on:

- `quantum-observable-universes/quantum-observable-universe.lean:231`
- `quantum-universes/quantum-universe.lean:257`
- `lean/QOU/QuantumObservableUniverse/CategoricalFoundations.lean:259`

each saying the trace identity follows "by linearity of the trace". **That
theorem has never compiled.** The citations are prose, not imports, so nothing
detected it.

There is no library twin — this sibling is the sole home, and the block's
`lean.ref` (`qou:QOU.BraidKnot.frobenius_codim_universal`) resolves here. So
this is not the shadowing class; it needs repairing where it is.

## Likely shape of the remaining work

The three `typeclass instance problem is stuck` are probably one cause: the
`∑ μ, …` notation over `[SemisimpleFrobeniusAlgebra Λ]` cannot infer the
instance from an implicit `Λ`, so the sums need the instance or the index type
made explicit. `93:35` is a `rw` whose pattern moved. The unsolved goals and
the nested simp failure need reading per-site.

## Do not

Do not "fix" this by weakening a statement, adding `sorry`, or concluding
`True`. The `codim_block_contribution` / `frobenius_codim_universal` /
`frobenius_codim_tau_invariant` chain is a real linear-algebra identity and
should be provable as stated.


## CLOSED 2026-08-23 — the file compiles

`LEAN_EXIT=0`, **0 errors, 0 sorries**, 943 lines. Confirmed twice, both reads
taken after `while pgrep -x lean; do sleep; done`.

All eight listed above are gone:

| listed error | cause | fix |
|---|---|---|
| 83, 802, 854 stuck typeclass | `∑ μ,` / `∀ μ,` left `Λ` a metavariable, so `[SemisimpleFrobeniusAlgebra Λ]` could not resolve | annotate `: Λ` |
| (revealed) `Finset.erase` | `[DecidableEq Λ]` never bound | add to both `gb_filtration_*` |
| (revealed) 4× type mismatch | `Finset.sum_erase_add` gives `∑ erase + f a`; every `show` wrote `f a + ∑ erase` | `Finset.add_sum_erase` |
| 93 rewrite failed | `mul_div_assoc` reached with the goal at `b / (a * b)` — product in the DENOMINATOR, nothing to fire on | `field_simp`; `_ha` renamed `ha`, it was never really unused |
| 222 unsolved | `simp` stopped at `1/1 + 1/1` | `norm_num [heckeH2DimQ]` |
| 468, 603, 784 unsolved | **not** what I first said — see below | `simp [div_eq_mul_inv]` |

## Retracting my own diagnosis of 468/603/784

I recorded that these needed `field_simp` with nonvanishing side conditions the
statements lack, and that their unconditional truth was an open mathematical
question. **Both claims were false**, and they were false because I reasoned
about the goal rather than printing it.

Printed, the two sides differ only in notation: `simp` normalises the left to
`a⁻¹ * b⁻¹` while the right still reads `2 / (a * b)`. `div_eq_mul_inv`
reconciles them, `ring` closes it. Unconditional. One lemma, all three cases.

`mul_inv` alongside it was reported unused at both sites and dropped.

## The n=8 heartbeat

`simp` over 22 branches of degree-7 Laurent expressions exceeds the default
budget — deterministic timeout, not a proof gap. `set_option maxHeartbeats
1000000 in`, placed **before** the docstring; after it, the docstring is
orphaned and the file will not parse. I made that exact mistake twice in this
one file.

## Method note worth keeping

Two error counts I reported on this branch came from grepping a `lean` log
while the process was still writing to it. A truncated log contains no error
text and is indistinguishable from a clean build by grep alone. Guard every
read with `while pgrep -x lean; do sleep; done`.
