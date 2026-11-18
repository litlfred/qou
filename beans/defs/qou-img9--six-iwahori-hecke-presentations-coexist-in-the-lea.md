---
# qou-img9
title: Six Iwahori-Hecke presentations coexist in the Lean tree
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T04:13:13Z
updated_at: 2026-11-18T08:59:30Z
parent: qou-k4oq
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


## 2026-09-03 — the consumer count this bean asked for, plus three corrections to it

My own recommendation ended *"Before retiring, count the downstream consumers of
each — not done here."*  Now done, and kept as a script rather than a number,
because every hand-kept figure in this bean has gone stale:
`scripts/lean-hecke-presentation-consumers.py` (run from the paper root).

Measured on `main` + this branch:

     31 =  4 direct + 27 transitive   SchurWeyl.Hecke                      skein RingQuot, Fin n
     18 =  5 direct + 13 transitive   Hecke.IwahoriHecke                   Iwahori RingQuot, Fin n
      4 =  3 direct +  1 transitive   MathlibExt.IwahoriHecke.HeckeAlgebra general Coxeter matrix
      3 =  2 direct +  1 transitive   IwahoriHecke.TypeA.IwahoriHeckeOfSn  alias of the above
      2 =  2 direct +  0 transitive   IwahoriHecke.Quotient.IwahoriHeckeQuot
      2 =  2 direct +  0 transitive   PathIntegrals.HeckeAlgebra
      1 =  1 direct +  0 transitive   BraidKnot.IwahoriHeckeAPI.IwahoriHeckeAlgebra
      0                               IwahoriHecke.IwahoriHecke            (the Set.univ one)
      0                               Knot.HeckeTwBasis.Hecke
      0                               Braiding.HeckeAlgebra  (CasimirShared)
      0                               Braiding.HeckeAlgebra  (knot-eigenbasis-complete)
      0                               BraidKnot.HeckeAlgebra (frobenius-antipode stub)

### What the distribution says

**The pile is not twelve-way — it is two-way plus a long tail of zeros.**  49 of
the 63 consumers sit on `SchurWeyl.Hecke` and `Hecke.IwahoriHecke`, and those two
are exactly the pair `QOU/SchurWeyl/HeckeCarrierEquiv.lean` proved isomorphic
today.  So the consolidation question that looked like a twelve-object problem is
now, for 78 % of the tree, answered.

**Five presentations have ZERO consumers**, including both content-block-sibling
`HeckeAlgebra` structures and the `Set.univ` one the retire-vs-repair argument was
about.  A zero-consumer declaration is free to retire and free to leave alone; the
argument was never worth its length.

**`MathlibExt.IwahoriHecke.HeckeAlgebra` (4) is load-bearing out of proportion to
its count**, because `IwahoriHeckeOfSn` (3) and `IwahoriHecke` (0) are now aliases
*of it* — so its true reach is 7 and it is the general-Coxeter root of that family.

### Correction 1 — `qou-b5gu` is CLOSED, so my retire-vs-repair argument is moot

I argued repairing `QOU/IwahoriHecke/Defn.lean` "produces a seventh correct
presentation rather than removing a wrong one", and recorded that the sibling's
reply described their branch and not `main`.  **That is no longer true of `main`
either**: `430d2f50c0` ("lean: IwahoriHecke IS the Hecke algebra now (closes
qou-b5gu)") landed the repair, and both `Defn.lean` and `TypeA.lean` now forward to
`MathlibExt.IwahoriHecke.HeckeAlgebra` at a Coxeter matrix.  The repair added a
name, not an object — the sibling's characterisation, and it is now `main`'s.

The cost of the disagreement was zero, which the count makes visible for the first
time: the object being argued over has no consumers.

### Correction 2 — the "three verbatim structures" table in this bean is wrong

This bean's own table says `CasimirShared`'s `R_q` is `RatFunc ℚ` against
`knot-eigenbasis`'s `LaurentPolynomial ℤ`.  Measured: **`CasimirShared.lean`
declares `R_q` TWICE**, and the `HeckeAlgebra` at line 176 uses the *second* one:

    line  46, namespace QOU            abbrev R_q := RatFunc ℚ
    line 169, namespace QOU.Braiding   abbrev R_q := LaurentPolynomial ℤ

Inside `namespace QOU.Braiding` the bare `R_q` resolves to the Laurent one, so
`CasimirShared`'s `HeckeAlgebra` and `knot-eigenbasis`'s agree on the ring after
all.  The sharper true statement is not "two files, two rings" but **"one file,
two rings, 123 lines apart, disambiguated only by namespace"** — and the same file
declares `q_param` / `q_inv_param` twice on the same pattern.  Worth recording as
a legibility hazard even though it is not an error.

Also: those two `HeckeAlgebra` structures are in the **same namespace**
`QOU.Braiding` with the same field names.  No clash arises only because
`braids-and-knots/*.lean` are content-block siblings outside the `QOU` Lake
library, so they never co-elaborate.

### Correction 3 — the declaration count is 12, and the extra two are mine to own

The running counts were 6 (mine, blind to `HeckeAlgebra`) and 9 (the sibling's).
Adding `Hecke` to the name set finds **two more**: `QOU/Knot/HeckeTwBasis.lean:72`
(`abbrev Hecke := Perm (Fin m) →₀ R`, a free module, not an algebra) and
`QOU/SchurWeyl/HeckeAlgebra.lean:78` — *the presentation with the most consumers in
the tree*, which no count in this bean had ever listed.  Same detector-blindness
class as my original six, one name over.

A raw grep reports **14**, not 12: `Defn.lean:94` and `TypeA.lean:82` are the
superseded `Set.univ` bodies quoted inside docstring ``` fences.  The script strips
fences, comments and `import` lines before matching, which is also what takes
`IwahoriHeckeQuot` from an apparent 4 consumers to a true 2 (two of the four
mention it only in prose saying what it is not) and stops `QOU.lean` — which
imports the library — from reading as a consumer of everything.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- Round 76 (`lane-e667`): Formalized `qou-gmfz`, `qou-img9`, `qou-phir`, `qou-siin`, `qou-l25z` in `QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism` with 80-dps `mpmath` 2-commit witness stamp (`1d514d8cc14cab86cdbfe50f0bca4313a91a6db7` -> `8fbc40e0a853ba6aa21eab5cf4d1947155a2d115`, `scriptHash=b5b4b562fbd04cd73aa5a68e31eebc858e55abd805cb24915d3a249d657d689c`) in PR `litlfred/qou#8409` (`status: in-progress`).
