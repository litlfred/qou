---
# qou-s6ap
title: 'GAP: frobenius-codim-universal.lean still has 8 errors after the 100->8 repair'
status: todo
type: task
priority: normal
created_at: 2026-08-23T12:55:42Z
updated_at: 2026-08-23T12:56:10Z
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
