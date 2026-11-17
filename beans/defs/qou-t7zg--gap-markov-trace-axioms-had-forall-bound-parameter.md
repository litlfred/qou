---
# qou-t7zg
title: 'GAP: Markov-trace axioms had forall-bound parameters that collapsed tr_M to zero'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T15:43:35Z
updated_at: 2026-11-17T06:48:00Z
parent: qou-rtxm
---


## The defect

`QOU/HeckeAlgebra/MarkovTrace.lean` carried

```lean
axiom MarkovTrace_markov_axiom :
    ∀ {n : ℕ} (x : HeckeElement n) (z : ℝ),
    markovTrace (n + 1) (heckeStab x) = z * markovTrace n x
```

`z` is `∀`-bound, so it can be instantiated twice:

```
z := 0  ⟹  markovTrace (n+1) (heckeStab x) = 0
z := 1  ⟹  markovTrace (n+1) (heckeStab x) = markovTrace n x
```

hence **`markovTrace n x = 0` for every `n` and every `x`**. Proved in
Lean against the pre-fix corpus (`exit 0`), not inferred by reading.

`tr_M` is the central object of the mass chain
`M = ρ · m_e · |tr_M(T_w)|`, so every Lean statement downstream of this
was vacuously a statement about `0`.

**Scope, stated carefully (AGENTS.md §"Before declaring refuted"): this
is a scope-(a) finding about the Lean corpus, not a claim about the
framework.** The corpus stayed *consistent* — the zero map satisfies
`markovTrace_linear`, the only other constraint on `markovTrace` — so
nothing false was derivable and no published result is affected. The
Python compute layer (`wedderburn_jones_markov.py`,
`tr_m_q_hecke_seminormal.py`) computes `tr_M` independently and is
untouched. What was lost was only the Lean side's *content*: the axioms
pinned the object they were meant to characterise.

The docstring already read *"z is the Markov parameter; for the QOU
substrate z := QSubstrate.markovParameter"*. The author knew what `z`
was. Only the binder was wrong.

## Same defect, second site

```lean
axiom wenzlBridge :
    ∀ {n : ℕ} (q : ℝ) (x : WedderburnDecomposition n),
    markovTraceOnWedderburn x = ∑ lam ∈ …, JonesMarkovCoefficient lam q * (x lam).trace
```

The left side does not mention `q`, so `∀ q` makes the weighted
block-sum **provably independent of `q`** — and the `q`-dependence of
`y_λ(q)` is the entire content of the Wenzl bridge. The axiom asserted
the negation of its own purpose. `WedderburnDecomposition n` is defined
in `Wedderburn.lean` as the decomposition of `H_n(q_0)`, so `q_0` is the
only `q` the statement can honestly mean.

## Fix (landed)

Both binders replaced by the intended constants —
`QSubstrate.markovParameter` and `QSubstrate.q_0` — plus two regression
witnesses in the same file that are **vacuous against the pre-fix
axioms** and so fail loudly if either binder is re-universalised:

- `markovParameter_pos : 0 < QSubstrate.markovParameter`
- `markovTrace_stab_pos : 0 < markovTrace n x → 0 < markovTrace (n+1) (heckeStab x)`

The second had an unsatisfiable hypothesis before the fix (nothing was
positive) and a `0 < 0` conclusion.

Neither axiom had any consumer in the corpus, so the fix broke nothing —
which is also why the defect survived: nothing exercised these axioms.

## Generalise this — the `∀`-bound-constant scan

This is a **new vacuity class**, distinct from the three already
catalogued (trivial-true, collapsed-definition, placeholder-carrier). The
shape:

> an `axiom` or `theorem` whose statement universally quantifies a
> variable that appears on only **one** side of an equation, where the
> intended reading is a fixed constant.

Any such statement forces the other side to be constant / zero. It is
invisible to every existing detector: no `sorry`, no trivial `True`, no
`native_decide`, and `#print axioms` looks normal.

Suggested detector, for `scripts/lean-definition-collapsed-audit.py`:
flag `∀ (v : τ) …, lhs = rhs` where `v` occurs in exactly one of
`lhs`/`rhs`. Expect false positives (genuine "for all `ε`" statements),
so this is an agent-confirmed candidate class like the others.

**Nobody has run this scan.** The two hits here were found by reading one
file. There are 29 axiom-bearing library files (bean `qou-i6cn`) that
have not been read.

## 2026-11-17 — `∀`-Bound Markov Parameter Collapse vs Fixed-Parameter Non-Collapse (`litlfred/qou#8234`)
- Formalized `forall_bound_markov_param_collapses` and `canonicalFixedParamWitness_nondegenerate` over generic `CommRingOps R` in `folio/quantum-observable-universe/lean/QOU/Foundations/SpechtH4MarkovCascadeFoundations.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `586d33b13c7ee8fa730d8f63e5c0a4eab181c898`, PR [https://github.com/litlfred/qou/pull/8234](https://github.com/litlfred/qou/pull/8234)).
- Kept `status: in-progress` per no-unilateral-closure policy.
