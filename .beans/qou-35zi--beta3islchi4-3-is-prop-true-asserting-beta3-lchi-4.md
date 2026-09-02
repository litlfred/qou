---
# qou-35zi
title: beta3IsLChi4_3 is Prop := True asserting beta(3) = L(chi_4, 3)
status: completed
type: bug
priority: low
created_at: 2026-08-24T19:40:58Z
updated_at: 2026-08-24T19:45:55Z
---

`QOU/Infra/DirichletL.lean:55`.

```
/-- The classical identity `beta(3) = L(chi_4, 3)` -- encoded as a
    proposition.  Its proof from Theorem A (via Im Li_3(i) = beta(3))
    is in `prop:cyclotomic-l-value-decomposition`. -/
def beta3IsLChi4_3 : Prop := True   -- placeholder for axiomatic class
```

The docstring says the declaration *is* the identity. It is `True`.

**Inert, and that is the whole reason to record it.** `grep -rn beta3IsLChi4_3`
over the corpus returns exactly one line — its own definition. Nothing imports
it, nothing applies it, no sidecar cites it. So there is no live claim resting on
it and the priority is low; the risk is only that a later reader (or a later
grep for `beta(3)`) finds a declaration whose name promises a proved identity.

## Fixed 2026-08-24 (branch `claude/mt7r-archimedean-eval-2026-08-24`)

Docstring now says the body is `True`, that the declaration names the identity
rather than stating it, that nothing references it, and what stating it properly
would cost — `beta` and `L(chi, s)` as Mathlib objects, neither of which is in
scope in this file, which is why the placeholder exists at all. The `def` is
unchanged.

Gates: `scripts/lean-direct-cone.sh QOU.Infra.DirichletL` exit 0;
`bun run scripts/run-validate.ts` **Valid — 26 issues, 0 errors** (baseline,
unchanged).

## If someone wants to drain it properly

Two honest endings, and deleting is the cheaper one:

1. **Delete it.** Zero references; nothing breaks. The identity is already
   recorded where it belongs, in `prop:cyclotomic-l-value-decomposition`.
2. **State it**, which needs `Real.beta`-style Catalan values and Dirichlet
   `L`-functions in scope. That is a Mathlib-gap question, not a five-minute
   edit, and it is not obviously worth doing for a declaration nothing uses.

Deliberately not chosen here: deleting a public declaration is an API decision,
not a disclosure fix.
