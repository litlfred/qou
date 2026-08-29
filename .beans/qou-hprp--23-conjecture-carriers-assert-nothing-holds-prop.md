---
# qou-hprp
title: '23 conjecture carriers assert nothing — the `holds : Prop` shape'
status: todo
type: task
priority: medium
created_at: 2026-08-29T18:10:00Z
updated_at: 2026-08-29T18:10:00Z
---

Found sweeping the q-geometric-langlands Lean siblings after the four
`False`-proving axioms (`qou-hwax`, `qou-qexf`).

```lean
class QuantumLanglandsDual where
  holds : Prop
```

`⟨True⟩` inhabits this. So a downstream `[QuantumLanglandsDual]`-conditional
theorem proves nothing modulo the conjecture, and the carrier records only that
*someone intends a proposition to go here*. It is the `true-class-field` variant
of `proof-claims-unencoded` — one step less obvious than an empty carrier, and it
passes every existing check.

## Measured, and the first number was wrong

| measure | files |
|---|---|
| naive grep `holds : Prop` | 38 |
| **live, comments stripped** | **23** |
| prose-only false positives | 15 |

A 39 % false-positive rate for the naive grep. The false positives are
docstrings describing a stub that was *already replaced* — including
`modular-s-transform-q-q-tilde.lean`, whose docstring records that it
"replac[ed] the former `holds : Prop` stub". A grep that reads comments as code
would have sent an agent to fix the one file in the chapter that is already
correct.

By chapter: mass-theory 7, `lean/` 6, nuclear-interactions 4,
stochastic-mechanics 2, q-geometric-langlands 2, appendix-surreals 1,
appendix-surreals-archimedean 1.

Detector: [`scripts/lean-overclaim-audit.py`](../scripts/lean-overclaim-audit.py)
reports 39 such *declarations* under `contentless-carrier`, plus 9
`empty-carrier`. That is the trustworthy family in that script; read its
docstring for what is not.

## The model to copy is in the same chapter

`ModularSTransformQQTilde` shows the right shape — a conjectural continuation
`F : ℂ → ℂ`, a `nondegenerate` field so the duality is not vacuous, and the
`s_automorphy` law carrying the actual claim. Three carriers in one chapter, two
dispositions, and the good one already documents its own migration.

## Why this is NOT a mechanical drain

**Do not sweep these.** Filling in a carrier means deciding what the conjecture
claims, which is a mathematical judgment about the author's intent, not a
repair. The specific trap, worked through on `QuantumLanglandsDual`: its `.md`
claims `H_n(q) ↔ H_n(q^{-1})` via Cartan folding. An encoding restricted to the
*parameter* — an involution `q ↦ q⁻¹` on `ℝ`, nontrivial for `q > 1` — is
content-bearing, satisfiable, and **provable**, so supplying it with an instance
would report an open conjecture as closed. That is strictly worse than the stub
it replaced.

A faithful encoding has to reach the algebra. `QOU.Hecke.HeckeAlgebra R n q A`
exists (`QOU/StaircaseCornerHook.lean` uses it as an instance binder), so the
statement is expressible — an algebra equivalence `A ≃+* B` between `H_n(q)` and
`H_n(q⁻¹)` compatible with folding — but that is a per-conjecture piece of work
needing the author's reading of each claim, and it carries a build cost the
content-block siblings do not currently pay.

Suggested order: take the ones whose `.md` states a single crisp identity or
inequality first; leave the ones whose `.md` is a multi-part correspondence
(3d–3d, Langlands duality) until someone with the domain context can say what
the minimal faithful statement is.
