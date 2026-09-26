---
# qou-fr7j
title: 'Certify n>=9 triangulations: iterate Fin.prod_univ_succ past Mathlib eight-tetrahedron ceiling'
status: completed
type: task
created_at: 2026-08-15T15:48:26Z
updated_at: 2026-08-15T15:48:26Z
---


Successor to `qou-glhi`, which delivered edge identities for 27 manifolds at shape-field
degrees 2–14 and certified 16 of them as `ShapedTriangulation.SatisfiesEdgeEquations`.

## The limit, stated exactly

`scripts/gen-gluing-lean.py`'s `emit_certification` unfolds `∏ i, …` over `Fin n` with
`Fin.prod_univ_{two..eight}`. **Mathlib provides those and stops at eight.** So every
manifold with `n ≥ 9` tetrahedra gets a comment instead of a certification:

```
-- 9_35: 9 tetrahedra — no `Fin.prod_univ_9` in Mathlib, so the
-- certification template does not apply.  Needs iterated
-- `Fin.prod_univ_succ`.  NOT emitted rather than emitted broken.
```

Currently uncertified for this reason: **9₃₅**, **o9_00000** (both n = 9), **10₁₀₀**
(n = 14). Their standalone edge identities exist and are proved — `GeneratedGluing.lean`
for the first two, `GeneratedGluingHigh.lean` for 10₁₀₀. Only the wrapper is missing.

## What to do

`Fin.prod_univ_succ` iterates to any `n`; the question is whether the resulting goal still
reduces under the template's full `simp`. **Do not assume it does.** `glhi` recorded three
separate failures where the mathematics was right and a *tactic state* was wrong, and two
of them were exactly about `Fin`-indexed matrix applications not reducing:

1. `fin_cases k` leaves `⟨0, ⋯⟩`, on which `Matrix.cons_val_zero` does not fire;
2. there is no `Matrix.cons_val_four`, and `cons_val_succ` does not fire on a literal
   `4 : Fin 5`, so a curated `simp only` silently stops at n ≥ 5 — full `simp` is required.

Both failed with a bare "ring expressions not equal", which reads as a wrong cofactor and
sends you to check arithmetic that was already asserted exact. Expect a third variant of
the same thing here and **dump the goal with `trace_state` early** rather than
re-deriving cofactors.

Cheapest probe: take **9₃₅** (n = 9, one past the ceiling) and try to certify just it by
hand. If that works, generalise the emitter; if it does not, the failure at n = 9 is the
whole finding and 10₁₀₀ at n = 14 will not behave differently.

## Also worth doing while here

**Degrees beyond 14 are untested.** `glhi` predicted a compile-time wall in 7–14 and there
wasn't one — 10₁₀₀ at degree 14, 384 KB, with a 30,193-character cofactor, builds in 131 s.
It also found that cost tracks the **number** of `ring` normalisations rather than the size
of any one, so wide-but-few is cheap. Route 75's reach is the real constraint on what can
be attempted, not Lean's. Worth finding where the actual ceiling is, now that the
predicted one turned out to be imaginary.

---
**2026-08-15 — DONE. The ceiling was not real, and the bean's own caution is what makes
that worth recording.**

Branch `claude/fivetwo-level7-ladder-numerators`.

### Result

| module | manifolds | n range | degrees | `lake build` |
|---|---|---|---|---|
| `GeneratedCertified.lean` | **19** (was 16) | 2–9 | 2–6 | 50 s |
| `GeneratedCertifiedHigh.lean` (new) | **8** | 5–14 | 7–14 | 50 s |

**27 manifolds certified**, all `satisfiesEdgeEquations` verified
`[propext, Classical.choice, Quot.sound]`, `lake` exit 0 with the `.olean` deleted first.
Every manifold Route 75 verifies in Python and `GeneratedGluing`/`High` proves in Lean is
now also certified as a *structure*.

### The fix is one line, and the bean was right to demand a probe first

    simp [Fin.prod_univ_succ, triangulation, gluing]

`simp` iterates `Fin.prod_univ_succ` unaided, so it unfolds the product at **any** `n`.
The old refusal — *"no `Fin.prod_univ_9` in Mathlib, so the certification template does not
apply"* — was true about Mathlib and false about the difficulty.

**This bean predicted the probe might fail and told me to expect a third variant of the
`Matrix`-index trap.** It did not fail: `9_35` (n = 9, one past the ceiling) certified in
95 s, sorry-free, **first try**. Following the bean's own advice — probe the smallest case
past the ceiling by hand before generalising — is what made that cheap to establish either
way. The caution was correct even though the prediction was wrong; a one-manifold probe
costs 95 s and a wrong generaliser costs a debugging session.

### The generator drops the table rather than keeping a fast path

`_PROD_UNIV` (the `Fin.prod_univ_{two..eight}` map) and the `n not in _PROD_UNIV` guard are
both gone. Keeping the named lemmas for `n ≤ 8` would be a second unfolding rule and a
second thing to get wrong; measured, it buys nothing — **19 manifolds now build in less
time than 16 did**, because the `ring` normalisation dominates rather than the unfolding.

### Traps recorded

- ⚠ **Illegal import order.** A `/-!` module docstring above `import` fails with
  *"invalid 'import' command, it must be used in the beginning of the file"*. `/-!` is a
  module docstring and must follow the imports; use a plain `/- -/` comment above them.
  Cost one build cycle, and it is the same class the corpus already gates for in
  `lean-content-siblings.yml`.
- ⚠ **A naive axiom-check grep reports false failures.** `#print axioms` wraps the axiom
  list across lines for long declaration names, so
  `grep -v "axioms: \[propext, Classical.choice, Quot.sound\]$"` reported 3 of 19 as
  non-standard when all 19 were clean. Parse with a multiline regex, not a line grep — an
  axiom check that cries wolf is as bad as one that stays silent.

### The bean's second item, restated rather than done

"Degrees beyond 14 are untested" — still untested. `glhi` established that cost tracks the
number of `ring` normalisations rather than cofactor size, and nothing found here suggests
a barrier; the real constraint is Route 75's reach, not Lean's. Worth a separate bean if
anyone wants the actual ceiling, since two predicted ceilings have now failed to appear.

Status **completed** for both enumerated items: n ≥ 9 certification is done through n = 14,
and the emitter is general.
