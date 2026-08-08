---
# qou-up56
title: 'REFACTOR: thread [C] through 22 consumers of 8 laundered conjecture classes'
status: completed
type: task
priority: normal
created_at: 2026-08-08T14:57:07Z
updated_at: 2026-08-08T15:27:45Z
---


## CORRECTION (2026-08-08, same session) — the premise was wrong; closing

**The "22 consumers of 8 laundered classes" figure was a grep artifact.**
It is recorded here rather than edited away, because the mistake is
instructive and the same trap will catch the next agent.

What actually happened: I counted consumers with a bare-name grep
(`grep -rl "\bq_oper_hecke\b"`). Two distinct false-positive sources:

1. **Same-named theorem in the aggregator.**
   `QOU/QGeometricLanglands.lean` declares *theorems* named
   `q_gl_kummer_filtration`, `q_gl_fiber_functor`, and `q_oper_hecke` —
   the same identifiers as the three conjecture *classes* in
   `QOU/QGeometricLanglands/`. Those theorems correctly take
   `[QGeometricLanglandsConjecture ...]` as explicit hypotheses; they
   never mention the classes. Three "2-consumer" entries → zero.
2. **Directory name matching a class name.**
   `HabiroResidueSumEquivalence` is a *directory*, not a class. Every
   path under it matched the grep for a class of that name, which does
   not exist. One "4-consumer" entry → zero.

Corrected tally of the eight:

| class | claimed | actual | disposition |
|---|---|---|---|
| `TorusKnotMass` | 1 | 1 (declares `[C]`) | de-laundered |
| `VacuumEpsilon` | 3 | 3 (all declare `[C]`) | de-laundered |
| `TwoFiltrationBridge` | 1 | 1 (declares `[C]`) | de-laundered |
| `q_gl_kummer_filtration` | 1 | **0** | de-laundered |
| `q_gl_fiber_functor` | 2 | **0** | de-laundered |
| `q_oper_hecke` | 2 | **0** | de-laundered |
| `archimedean_agreement` | 4 | **0** | de-laundered |
| `archimedean_agreement` (protonExample) | 4 | **0** | de-laundered |

All eight are done. **No refactor is required — there was never a
22-file blast radius.** A corpus re-scan for the
`axiom X : C` + `instance : C := X` shape now returns exactly one hit,
`QOU/MathlibExt/SDPRealUniqueness.lean`, which is deliberately left (see
below).

## Method note for the next agent

Do not count Lean consumers with a bare-name grep. In this corpus,
identifiers collide across kinds (a class and a theorem may share a
name) and directory names shadow class names. Count instance-binder
uses specifically — `grep -rn "\[C\b"` — or better, ask the LSP
(`lean_references`), and always eyeball each hit before quoting a
number in a PR body. I quoted "22 files" in the #4750 description on
the strength of a grep I had not opened.

## The one remaining axiom-discharged instance is NOT laundering

`QOU/MathlibExt/SDPRealUniqueness.lean` carries

```lean
axiom slater_strict_complementarity_kernel_axiom : …
instance : SlaterStrictComplementarityKernel where
  kernel_uniqueness := @slater_strict_complementarity_kernel_axiom
```

This is a different thing from the conjecture cases and should stay:

- The axiom asserts a **published theorem** (Boyd–Vandenberghe §5.5.4,
  Alizadeh–Haeberly–Overton: Slater + strict complementarity ⟹ the SDP
  optimal face is a point), cited on the declaration. It is a **Mathlib
  gap**, not an open QOU conjecture.
- The class is genuinely content-bearing — `kernel_uniqueness` carries
  five real hypotheses and a nontrivial conclusion, not a `residual = 0`
  placeholder.
- The surrounding proof *constructs* every other step and cites the
  axiom only for the final kernel-uniqueness move.
- It is visible: a custom `axiom` shows up by name under
  `#print axioms`, so nothing is hidden.

The distinction that matters: laundering is discharging *an open
conjecture of this framework* so that `[C]` resolves for free.
Axiomatising a citable external result while the Mathlib proof is
missing is the established repo pattern (cf. `SDPRankEquality`), and
AGENTS.md §1 sanctions it with the `-- Ref:` citation, which is present.
