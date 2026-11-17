---
# qou-xzd5
title: 'confinement_categorical: MarkovTraceContext has NO instance anywhere — may be vacuously true, not unclosable'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T11:07:51Z
updated_at: 2026-11-17T06:48:00Z
parent: qou-rtxm
---


The last unresolved item from the qou-octr sweep (18 of 18 others refuted).
`confinement_categorical` could **not** be attempted, and the reason turns out
to be more interesting than the result would have been.

## Why it is blocked

`ConfinementCategoricalContext extends QOU.Shared.MarkovTraceContext`, whose
fields are not data but *structure*:

    R : Type u,  ringR : CommRing R,  invR : Inv R,  q : R,  n : ℕ,
    A : Type u,  ringA : Ring A,  algebraA : Algebra R A,
    heckeInst  : QOU.Hecke.HeckeAlgebra R n q A …,
    markovInst : QOU.Hecke.MarkovTrace  R n q A …

Refuting the theorem needs an instance, and an instance needs a Hecke algebra
carrying a Markov trace.

**Grepped the whole tree: there is no concrete instance of `MarkovTraceContext`,
and none of `QOU.Hecke.MarkovTrace` either.** Both appear only as hypotheses
(`[markovInst : QOU.Hecke.MarkovTrace n q A]`), never constructed.

## Why that matters more than the refutation would have

If `MarkovTraceContext` is **uninhabited**, then every
`theorem foo [ctx : MarkovTraceContext] : P ctx` is **vacuously true** — and
that is criterion **#3 `proof-no-false-premise`**, not #10. A different defect
with a different fix, and one that would apply to the *whole* family of
theorems quantified over this class, not just this one.

So the status of `confinement_categorical` is genuinely open in a way none of
the other 18 were: it is either

- **#10 unclosable** — if the class is inhabitable and the free fields
  (`E_infinity_00`, `e_block`, `integral`, `pi_centre`, `observable`) can
  disagree, which they plainly can once an instance exists; or
- **#3 vacuous** — if no instance can exist, in which case the `sorry` is
  closeable *and worthless*, and so is everything else over this class.

Deciding it decides the family.

## How to settle it

1. Try to build any instance of `QOU.Hecke.HeckeAlgebra R n q A` — the
   degenerate `n = 0`, `A = R` case is the obvious candidate. If it goes
   through, the class is inhabited and the #10 refutation follows immediately
   by the qou-octr method.
2. If it does not, find out whether the axioms are jointly satisfiable at all.
   An unsatisfiable `HeckeAlgebra` class would be a much larger finding: every
   `[HeckeAlgebra …]`-quantified result in the corpus would be vacuous.

Step 1 is an hour's work and settles the common case.

## Count

With this one outstanding, the sweep stands at **18 attempted, 18 refutable, 0
survivors**, plus this one blocked. The only statement to survive any check
remains `covariance_kernel_conjecture` (proved on `k ≤ 8`).

---

## RESOLVED 2026-08-09 — the class IS inhabited, so it is #10 not #3

The deciding experiment worked. `Generator n` is `structure Generator (n : ℕ)
where idx : Fin (n - 1)` — **ℕ subtraction**, so at `n = 0` *and* `n = 1` the
index type is `Fin 0`, i.e. empty. `embed` is then trivial and `quadratic`,
`braid`, `farCommute` hold vacuously. Taking `A := R := ℤ` reduces
`spans : Algebra.adjoin R (Set.range embed) = ⊤` to `⊥ = ⊤` in
`Subalgebra ℤ ℤ`, which is a subsingleton.

```lean
noncomputable instance degenerateHecke : HeckeAlgebra ℤ 0 0 ℤ where
  embed      := fun i => absurd i.idx.isLt (by omega)
  quadratic  := fun i => absurd i.idx.isLt (by omega)
  braid      := fun i _ _ => absurd i.idx.isLt (by omega)
  farCommute := fun i _ _ => absurd i.idx.isLt (by omega)
  spans      := Subsingleton.elim _ _

noncomputable instance degenerateMarkov : MarkovTrace 0 (0 : ℤ) ℤ where
  trace := LinearMap.id;  normalised := rfl
  cyclic := fun x y => by simp [mul_comm];  z_param := 0
  trace_gen := fun i => absurd i.idx.isLt (by omega)
  trace_prod_gen := fun i _ _ => absurd i.idx.isLt (by omega)
```

`witness : MarkovTraceContext` follows. All in
`docs/audits/2026-08-09-unclosable-context-sorries.lean.txt`.

### Consequences

1. **`MarkovTraceContext` is inhabited**, so nothing quantified over it is
   vacuous. The #3 branch of this bean is closed: it does **not** apply, here
   or to the rest of the family.
2. **`confinement_categorical` is therefore #10**, and refuted:
   `n_blocks := 0` empties the sum while `E_infinity_00 := 1`.
3. The sweep is complete — **19 attempted, 19 refutable, 0 survivors.**

### Worth knowing about the witness

It is *degenerate on purpose*: `n = 0` means no generators, so it satisfies the
Hecke axioms by having nothing to satisfy them about. That is exactly what makes
it a good refutation instrument, and exactly why it is **not** evidence that the
substantive Hecke infrastructure exists. Nothing here builds `H_n(q)` for `n ≥ 2`.

An `n ≥ 2` instance remains unbuilt anywhere in the tree, which is the real
missing infra the manuscript keeps citing.

## 2026-11-17 — Concrete `n = 3` (`H₃(q)`) Specht–Markov Trace Instance (`litlfred/qou#8234`)
- Formalized `h3ConcreteMarkovTrace` and `h3ConcreteMarkovTrace_T1_eq_T2` combining the trivial (`q`), sign (`-1`), and `2 × 2` `q`-Specht (`S^{(2,1)}_q`) representations over generic `CommRingOps R` in `folio/quantum-observable-universe/lean/QOU/Foundations/SpechtH4MarkovCascadeFoundations.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `586d33b13c7ee8fa730d8f63e5c0a4eab181c898`, PR [https://github.com/litlfred/qou/pull/8234](https://github.com/litlfred/qou/pull/8234)).
- Kept `status: in-progress` per no-unilateral-closure policy.
