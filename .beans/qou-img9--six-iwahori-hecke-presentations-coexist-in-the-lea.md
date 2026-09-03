---
# qou-img9
title: Six Iwahori-Hecke presentations coexist in the Lean tree
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T04:13:13Z
updated_at: 2026-09-03T04:11:03Z
---

Measured 2026-08-30 with

    grep -rn "def IwahoriHecke\|structure IwahoriHecke\|abbrev IwahoriHecke" --include=*.lean content/

| declaration | file | shape |
|---|---|---|
| `IwahoriHecke W R q` | `QOU/IwahoriHecke/Defn.lean` | quotient over `Set.univ : Set W` — the `qou-b5gu` defect: it imposes the quadratic relation on **every** group element, but `T_w` satisfies it only when `ℓ(w) = 1` |
| `IwahoriHeckeQuot` | `QOU/IwahoriHecke/Quotient.lean` | the underlying quotient of the above |
| `IwahoriHeckeOfSn` | `QOU/IwahoriHecke/TypeA.lean` | type-A specialisation of the above |
| `IwahoriHeckeAlgebra n R` | `QOU/BraidKnot/IwahoriHeckeAPI.lean` | a `structure`, not a quotient |
| `IwahoriHecke K q n` | `QOU/Hecke/IwahoriHecke.lean` | `RingQuot` on `Fin n` generators — what PR #6053's `T_w` programme builds on |
| `HeckeAlgebra R q M` | `QOU/MathlibExt/IwahoriHeckeAlgebra.lean` | general Coxeter matrix, ℕ-indexed type A, with `lift` / `hom_ext` / `exists_unique_lift` (PR #6055) |

Found while answering a sibling's coordination comment on #6053, which named two
of the six and asked whether the `Set.univ` one should be repaired or retired.

## Why this matters beyond tidiness

Conventions differ across them. `QOU/Hecke/IwahoriHecke.lean` uses
`σ² = (q−1)σ + q`, i.e. Iwahori normalisation `(σ − q)(σ + 1) = 0`. AGENTS.md
§7a states the corpus convention as the Hecke-skein `σ² = (q − q⁻¹)σ + 1`.
Those are different normalisations, related by `σ_skein = q⁻¹ σ_Iwahori` at
`Q = q²`. So a result proved against one presentation is not automatically a
result about the object the paper names, and nothing currently flags a
cross-presentation citation.

`QOU/MathlibExt/HeckeIwahoriConventionBridge.lean` (#6055) crosses one such
pair. There is no map between the other presentations at all.

## Recommendation (judgement, not a finding)

Retire rather than repair the `Set.univ` family. Re-indexing
`QOU/IwahoriHecke/Defn.lean` by simple reflections produces a *seventh* correct
presentation rather than removing a wrong one; `QOU/Hecke/IwahoriHecke.lean`
already is that object for type A, and `QOU/MathlibExt/IwahoriHeckeAlgebra.lean`
already is it for a general Coxeter matrix. Before retiring, count the
downstream consumers of each — not done here.

Not started. No consolidation attempted on any branch.


## 2026-08-30 — CORRECTED: my six was an undercount, and the reason is nameable

A sibling agent (#6055) re-measured and reported ten. **They are right that six was
low, and my grep is why**: it keyed on the *name* `IwahoriHecke`
(`def|structure|abbrev IwahoriHecke`), so it was structurally incapable of seeing
anything declared as `HeckeAlgebra`. Same detector-blindness class the corpus
documents elsewhere — a detector that can only find what it already names.

**Measured on `main` + this branch** (their grep, run here):

```
grep -rnE "^\s*(noncomputable )?(def|abbrev|structure) (IwahoriHecke|HeckeAlgebra|IwahoriHeckeQuot|IwahoriHeckeOfSn|IwahoriHeckeAlgebra)\b" --include=*.lean content/
```

**9 declarations, no false positives.** The four I missed:

| declaration | file |
|---|---|
| `structure HeckeAlgebra` | `braids-and-knots/knot-eigenbasis-complete.lean:53` |
| `structure HeckeAlgebra (_n : ℕ) (_q : ℝ)` | `braids-and-knots/frobenius-antipode-lean-stub.lean:35` |
| `structure HeckeAlgebra` | `QOU/PathIntegrals.lean:294` |
| `structure HeckeAlgebra` | `QOU/BraidKnot/CasimirShared.lean:176` |

### Three of the sibling's specifics do NOT survive measurement

**(a) "Ten" and "twelve raw" are tree-dependent; here it is 9 with no fence
noise.** Their 10 includes their own unmerged `HeckeAlgebra R q M`; their 12 raw
includes false positives from their own docstring ` ```lean ` fences. Neither is
present on `main`. Quote the count with the tree it was taken on.

**(b) "Three of them are verbatim identical" — no, and the difference is the
load-bearing part.** All three share `n`, `carrier : Type*`, `q`, `q_ne_zero`,
but the base ring differs three ways:

| file | `q :` | `R_q` is |
|---|---|---|
| `knot-eigenbasis-complete.lean` | `R_q` | `LaurentPolynomial ℤ` |
| `QOU/BraidKnot/CasimirShared.lean` | `R_q` | `RatFunc ℚ` |
| `QOU/PathIntegrals.lean` | `ℝ` | — |

So **`R_q` denotes two different rings in two different files**, and the third is
`ℝ`. Same structure name, same field names, three base rings. That is worse than
verbatim duplication, which would at least be consistent.

**(c) "No relation of any kind — the only assertion is `q ≠ 0`" — false.**
`knot-eigenbasis` and `CasimirShared` both carry `q_inv` with
`q_mul_inv : q * q_inv = 1`; `PathIntegrals` carries
`q_not_root_of_unity : ∀ k ≥ 1, q ^ k ≠ 1` — which is precisely the genericity
condition semisimplicity turns on. All three carry
`mul : carrier → carrier → carrier`. They are thin algebra-with-parameter
records, **not** empty. Still not Hecke algebras (no quadratic, no braid), but
the sharper true statement is *"the name promises a Hecke algebra and the
structure delivers a parametrised carrier"*, not *"it asserts nothing"*.

### And a correction to my own retire-vs-repair reasoning

I argued repairing `QOU/IwahoriHecke/Defn.lean` "produces a seventh correct
presentation rather than removing a wrong one". The sibling replies that on
**their branch** it is already a definitional alias forwarding to
`HeckeAlgebra` — adding a name, not an object. That is right *about their
branch* and does not describe `main`, where `Defn.lean` is still the `Set.univ`
quotient. So my objection holds for the tree as it stands and is superseded only
if #6055 lands. Both statements are true of different trees; neither supersedes
the other unconditionally.

### Scope note

Whether the four content-free `HeckeAlgebra` structures should be renamed or
deleted is a **different question** from reconciling the genuine presentations,
and the sibling is right to keep them as separate rows. Nothing is consolidated
and no consolidation is proposed here.

## 2026-09-03 — TWO more presentations proved to be one algebra (the pair that mattered)

QOU/SchurWeyl/HeckeCarrierEquiv.lean (new, sorry-free):

  carrierEquiv          Hecke K q qi n  =~a  IwahoriHecke K Q n   (CommRing, given the two
                        matching conditions below)
  skeinIwahoriEquiv     Hecke K q q^-1 n =~a IwahoriHecke K (q^2) n  (any Field, q != 0)
  isSemisimpleRing_iwahoriHecke   1 < Q  =>  IsSemisimpleRing (IwahoriHecke R Q n), EVERY rank

### Why it is short: the relations differ in ONE clause

  SchurWeyl.HeckeRel K q qi n :  sigma^2 = (q - qi) sigma + (q*qi)
  QOU.Hecke.HeckeRel  K Q  n  :  sigma^2 = (Q - 1)  sigma + Q

Braid and far-commutation are VERBATIM IDENTICAL, on the same FreeAlgebra K (Fin n). So
the entire content is the quadratic, and sigma |-> c . T moves it under exactly two
conditions, carried as hypotheses rather than assumed:

  c (Q - 1) = q - qi        and        c^2 Q = q qi

The braid and commute clauses are PROVED scale-invariant (homogeneous of equal degree
both sides), not asserted to be.

At the skein normalisation qi = q^-1, Q = q^2 with c = q^-1 satisfies both identically.
THE PARAMETER MOVES, NOT THE RING: no square root is adjoined, nothing leaves a generic
[Field K]. Same rescaling QOU/BraidKnot/HeckeIwahoriConventionBridge.lean derives for
GENERATOR FAMILIES; new here is the upgrade to an AlgEquiv of the two RingQuot carriers,
which is what transports a ring-theoretic property.

Independent confirmation: this is the same bridge the character-sum probe measured
EMPIRICALLY in #6417 (Q = q^2, sigma_Iwahori = q sigma_skein) — reached there from
numerics, here from the relations.

### Also supplied

The IwahoriHecke side had generators and relations but NO universal property.
iwahoriLift / iwahoriLift_sigma / iwahori_hom_ext fill that in, mirroring what
SchurWeyl.Hecke already had.

### Count

QOU/BraidKnot/HeckeTypeAPresentationEquiv.lean crosses IwahoriHeckeOfSn <->
QOU.Hecke.IwahoriHecke. This file crosses SchurWeyl.Hecke <-> QOU.Hecke.IwahoriHecke.
Different pairs; between them THREE of the presentations this bean counts are now
provably one algebra.

### Path correction to this bean

This bean says the convention bridge is at QOU/MathlibExt/HeckeIwahoriConventionBridge.lean.
It is at QOU/BraidKnot/HeckeIwahoriConventionBridge.lean. Corrected here so the next
reader does not conclude it is missing.

### Still open on this bean

The Set.univ family (QOU/IwahoriHecke/Defn.lean, the qou-b5gu defect) is untouched, and
the recommendation to retire rather than repair it still stands with its downstream
consumers still uncounted. The two structure-shaped HeckeAlgebra declarations under
braids-and-knots/ are untouched.
