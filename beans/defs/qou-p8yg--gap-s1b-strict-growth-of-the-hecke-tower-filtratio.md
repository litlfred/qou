---
# qou-p8yg
title: 'GAP S1b: strict growth of the Hecke tower filtration -- H 1 < H 2 is a WIRE (H3 exists sorry-free); general n needs the (n+1)! lower bound'
status: todo
type: task
priority: normal
created_at: 2026-09-12T19:02:09Z
updated_at: 2026-09-26T15:15:50Z
---

Parent: qou-cins / plan qou-0fmb, epic qou-08a2. Opened 2026-09-12 after S1 merged (#7228, 3653e9ce).

## What S1 left open
QOU/MathlibExt/HeckeTowerWitness.lean proves twH_mono (<=) and twH_zero_lt_one (H 0 < H 1, via the rank-2 collapse). It does NOT prove H n < H (n+1) for n >= 1: the collapse map sends every generator to the same element, so it cannot separate H 1 from H 2.

## H 1 < H 2 is a WIRING job, not a build -- the separator already exists sorry-free
Corpus-grep 2026-09-12 (path 3) found the rank-6 object this needs, already proved:
  QOU/SchurWeyl/HeckeDim3Dim.lean   finrank_hecke3 : finrank R (Hecke R q q^-1 2) = 6
                                    sixBasis : Module.Basis (Fin 6), sixFamily_indep
  QOU/SchurWeyl/HeckeDim3Indep.lean sixWords_indep
  QOU/SchurWeyl/HeckeDim3.lean      braid3 : s0*s1*s0 = s1*s0*s1
All sorry-free (verified: the 10 'sorry' grep hits in HeckeCoset.lean are ALL the words "sorry-free" in docstrings -- prose, not code; qou-uoal's sorry-free claim HOLDS).

PROOF SKETCH (worked out, not guessed). Define phi : HeckeTower R h -> Hecke R q q^-1 2 by
    g0 |-> sigma0,  g1 |-> sigma1,  g m |-> q*1  for m >= 2.
Relation check:
  * far(m,k) for m >= 3 forces phi(g m) to commute with BOTH sigma0 and sigma1, i.e. to be central. A scalar is.
  * quad on a scalar c needs c^2 = h*c + 1; with h = q - q^-1 the root c = q works exactly.
  * braid(0) is g1 g0 g1 = g0 g1 g0 |-> sigma1 sigma0 sigma1 = sigma0 sigma1 sigma0 = HeckeDim3.braid3.
  * braid(m>=1) and far(2,0) reduce to scalar identities.
Then phi(twH 1) = adjoin{sigma0} = span{1, sigma0} (2-dim) while phi(g 1) = sigma1, and sigma1 is not in span{1,sigma0} by sixWords_indep. Hence twH 1 < twH 2.

NOTE the h = q - q^-1 specialisation: this separator needs a base ring carrying q, so the wired theorem is at R = the Hecke base ring, not the fully generic {R : CommRing}. That is a real scope narrowing and must be stated, not glossed.

## What is GENUINELY open: general n
H n < H (n+1) for all n needs dim H_n(q) >= n! -- the LOWER half of the Iwahori-Hecke basis theorem. qou-uoal (COMPLETED) supplies only the upper half, finrank_le_factorial <= (n+1)!, and its own closing note names the blocker: "Lower bound dim>=(n+1)! needs general Hoefsmit (qou-im9l)".

LEAD, not a claim: qou-im9l is itself now COMPLETED (general-lambda Hoefsmit seminormal rep + braid; residual qou-gjg6 also completed). So the stated blocker may already be discharged and the lower bound may ALSO be a wire. NOT verified -- whoever picks this up should corpus-grep whether the (n+1)! lower bound was ever derived from the completed Hoefsmit rep before assuming it is open.

## Also fix while here (minor, from the #7228 verification)
exists_tower_with_nonzero_h takes hne : h != 0 and concludes (forall m, quad) AND h != 0 -- the second conjunct merely restates the hypothesis. Not vacuous (the first conjunct is real content) but it is noise. Restate as the two genuine non-degeneracy facts: (forall m, twGen quad with the given h) AND twH 0 < twH 1, with no restated hypothesis.

## Discipline
No fit. Per rule 13a this stays open until the mathematics closes. Do NOT close it on the strength of the H 1 < H 2 wire alone -- that is one level, not the filtration.


--------
**2026-09-12, SAME DAY: THE PROOF SKETCH ABOVE IS REFUTED. Do not attempt it.**

The sketch sends g m |-> q*1 for m >= 2 and checks quad, far and braid(0). It does
NOT check braid(1), and braid(1) is what kills it.

With phi(g 2) = c*1 central and phi(g 1) = x:

    braid(1)   g2 g1 g2 = g1 g2 g1   =>   c^2 x = c x^2
    quad       x^2 = h x + 1         =>   c^2 x = c(h x + 1) = c h x + c
                                     =>   c (c - h) x = c

so if c is a unit, (c - h) x = 1 and x is a SCALAR. But x = sigma_1 is not a
scalar in H_3 (sixWords_indep). Contradiction: the algebra map DOES NOT EXIST.

This is not special to c = q. It is scope (b), a STRUCTURAL exclusion, and the
invariant is named: the braid relation together with the quadratic forces a
generator adjacent to a central-scalar generator to be a scalar itself. So EVERY
assignment sending all but finitely many generators to scalars collapses the low
generators too, and the whole "cheap finite separator" family is dead, not just
this member.

**Consequence: H 1 < H 2 is NOT a wire.** The rank-6 objects (HeckeDim3Dim /
HeckeDim3Indep) are real and sorry-free, but they cannot RECEIVE a map from the
N-indexed tower, so they do not yield strict growth. Strict growth needs the
Iwahori-Hecke coset basis, or the direct limit of HeckeInclusion.heckeIncl
together with injectivity of that inclusion -- i.e. exactly what the merged
HeckeTowerWitness docstring said before this bean narrowed it. The merged
docstring is CORRECT as written; this bean's narrowing was the error.

What survives from the narrowing, and is still worth having:
* HeckeMarkov3.markovTrace3 (finding 2) is untouched by this -- it is about the
  TRACE (S2 / qou-g8i1), not about separating the filtration, and remains a
  materially better S2 starting point than the rank-2 collapse.
* the obstruction itself is a formalize-first result worth recording in Lean,
  alongside #7153's braid_forces_eq_of_commuting_involutions, which is the same
  genre: a proved statement about which cheap witnesses CANNOT work.

Method note for the next agent: this was caught by reading the target's actual
API before writing the map, not by a probe. The sketch had been checked against
quad, far and braid(0) and looked complete; braid(m) for the INTERIOR index m=1
is the case a boundary-only check misses.


--------
**2026-09-12, THIRD PASS: the "genuinely open" item above is ALREADY DONE. Re-scope.**

This bean said general-n strict growth "needs the (n+1)! LOWER bound" and recorded
a LEAD that qou-im9l being completed might mean it exists. Measured: it does, and
it is not merely the lower bound but the EQUALITY.

  QOU/SchurWeyl/HeckeWedderburnGeneral.lean:77
    theorem finrank_hecke_eq_factorial {K} [Field K] [CharZero K] (q : K)
        (hq0 : q != 0) (hq2 : NotRootOfUnity q) (n : N) :
      Module.finrank K (Hecke K q q^-1 n) = (n + 1).factorial

Sorry-free, measured raw AND code-stripped: 0 sorry, 0 axiom declarations. Its own
docstring explains why the hard half was cheap -- "the lower bound is not proved by
hand here: it is forced by the surjection onto a space of dimension (n+1)!", via
heckeProduct_surjective onto the Wedderburn block product (finrank_blocks_eq_factorial,
which rests on sum_dLambda_sq / RSK-Burnside). So the Groebner-Shirshov route
(qou-auq3) was never on the critical path, and general Hoefsmit was not needed either.

**qou-uoal's closing note is STALE and is what misdirected this bean.** It reads
"Lower bound dim>=(n+1)! needs general Hoefsmit (qou-im9l)". That has been false
since HeckeWedderburnGeneral landed. Anyone reading qou-uoal for the state of the
basis theorem will conclude a build is required when the theorem is on main.

## The frontier, re-scoped -- ONE question, not a theory

No dimension theorem is missing. What is missing is the IDENTIFICATION between the
N-indexed presented tower and the finite Hecke algebras:

  There is a natural algebra map  Hecke K q q^-1 n  ->  HeckeTower R h
  sending sigma_i |-> twGen h i. The relations match exactly:
    - SchurWeyl HeckeRel.quadratic  sigma_i^2 = (q - qi) sigma_i + (q*qi) 1
      is twGen_quad with h = q - q^-1, using q*q^-1 = 1;
    - HeckeRel.braid                matches twGen_braid;
    - HeckeRel.commute (j+2 <= i)   matches twGen_far (k+1 < m).
  Its image is exactly twH n (adjoin of the first n generators).

  **OPEN: is that map INJECTIVE?**

If yes, then dim (twH n) = n! < (n+1)! = dim (twH (n+1)) by finrank_hecke_eq_factorial,
and twH n < twH (n+1) follows immediately for every n -- the whole of this bean,
discharged. If no, the presented N-tower is NOT the colimit of the finite ones and
that is itself a significant (and surprising) finding worth recording.

This is the classical embedding H_n -> H_infinity. It is one well-posed statement
about one map, not a program. Note the scope it carries: finrank_hecke_eq_factorial
needs [Field K] [CharZero K], q != 0 and NotRootOfUnity q, so any strict-growth
theorem derived this way inherits the GENERIC-q hypothesis and is not available over
a bare CommRing. State that, do not gloss it.

Do NOT re-attempt the tail-to-scalars route: it is refuted, and the refutation is now
a theorem on main (scalar_tail_forces_central + tail_scalar_is_automatically_a_unit,
#7231 / #7238), covering every tail assignment rather than the invertible ones.


**Method caveat on the re-scope above, added the same hour -- read before starting.**

The re-scope calls the injectivity of Hecke K q q^-1 n -> HeckeTower R h "one
well-posed statement, not a program". The STATEMENT is well-posed. The METHOD is
not obvious, and this bean has already over-narrowed once today, so state the
difficulty rather than discovering it.

The tempting route is a RETRACTION: build psi : HeckeTower R h -> Hecke K q q^-1 n
with psi . phi_n = id, which gives injectivity of phi_n immediately. But psi is an
algebra map OUT of a PRESENTED tower, so it must assign EVERY generator g m,
m in N, to an element of the finite H_n(q), satisfying quad + braid + far
throughout, with g m |-> sigma_m for m < n. The two obvious tail assignments are
both dead:

  * tail |-> a central scalar -- refuted by scalar_tail_forces_central, together
    with tail_scalar_is_automatically_a_unit (this bean's own theorems, merged in
    #7231 / #7238). They cover EVERY scalar, not just the invertible ones.
  * tail |-> sigma_{n-1} -- dies at far(m, n-2), which for m >= n demands
    sigma_{n-1} sigma_{n-2} = sigma_{n-2} sigma_{n-1}. False: adjacent generators
    do not commute.

So the obstruction this bean proved for the SEPARATOR route obstructs the
RETRACTION route too. That is a recurring structural feature of the presented
N-tower -- the infinite tail has to go somewhere and the relations constrain it
hard -- not a coincidence of one attempt. Whether ANY tail assignment into a
finite H_n exists is OPEN and is worth settling first, because a NEGATIVE there
would be informative: it would say the presented N-tower admits no algebra
retraction onto its finite stages, and injectivity must then come from a basis.

The classical route does not use a retraction at all: it uses the T_w basis of
H_infinity over the Coxeter group S_infinity, which for this carrier means
establishing a basis for the PRESENTED N-tower -- the analogue of qou-uoal's
spanning argument plus the Wedderburn lower bound, at S_infinity rather than S_n.
That is a build, and should be scoped as one.


--------
**2026-09-12: the sub-question this bean asked is ANSWERED -- NO tail assignment exists, for ANY finite target. The bean stays open; only the method question closes.**

The previous entry asked: "Whether ANY tail assignment into a finite H_n exists is OPEN and is worth settling first, because a NEGATIVE there would be informative." Settled, negative, and the proof is one identity.

  braid_central_forces_eq: if y is CENTRAL, x and y both satisfy the Hecke
  quadratic, and the two braid, then x = y.

    y x y = y (y x) = y^2 x = (h y + 1) x = h(yx) + x
    x y x = (y x) x = y x^2 = y (h x + 1) = h(yx) + y

  The braid relation equates them, so it IS x = y.

Centrality therefore does NOT stay put -- it propagates DOWN the tower, dragging
each generator onto the one above (central_step, central_forces_below), so

  central_tail_collapses_all: x n central  =>  x k = x n for EVERY k <= n.

In any finite target the `far` relations force every sufficiently high generator
to commute with all the low ones -- i.e. to be central -- and the collapse then
drags the ENTIRE image onto that single element. So no map from the N-tower into
a finite stage separates g 0 from g 1, whatever the target and whatever the tail
assignment. The retraction route is dead, not merely unpromising.

This SUBSUMES scalar_tail_forces_central (#7231/#7238): a scalar is central, so
that theorem is the special case, and this is strictly stronger -- it concludes
x = y rather than merely that x is central. The older theorem is kept because it
is cited.

Verified in-session: lean -DautoImplicit=false -s 65536, exit 0 (captured
directly, not through a pipe), 0 errors, 0 warnings. All four new declarations
are [propext, Quot.sound] -- no Classical.choice, no sorryAx. 0 code-level sorry,
0 axiom declarations.

**WHAT THIS BEAN STILL NEEDS, and why it stays open.** Strict growth
twH n < twH (n+1) is NOT proved and is not closed by this. What is now settled is
the METHOD: it cannot come from mapping into a finite stage, by any route. It has
to come from the Iwahori-Hecke coset basis for the PRESENTED N-tower -- the
analogue of qou-uoal's spanning argument plus the Wedderburn lower bound at
S_infinity rather than S_n -- or from the direct limit of
SchurWeyl.HeckeInclusion.heckeIncl together with injectivity of that inclusion.
Note finrank_hecke_eq_factorial supplies every DIMENSION fact already; it is the
identification of twH n with Hecke (n-1) that is missing, and per the entry above
that identification inherits generic-q hypotheses (Field, CharZero, q != 0,
NotRootOfUnity).


--------

**2026-09-26 — GENERAL n IS PROVED for the CONCRETE tower (PR #7456). Bean stays OPEN: `twH` is
not closed, per this bean's own discipline line.**

  QOU/SchurWeyl/HeckeTowerStrict.lean       heckeIncl_range_lt_top
  QOU/SchurWeyl/HeckeTowerStrictSharp.lean  finrank_range_heckeIncl

**This bean's stated blocker was STALE, exactly as its own LEAD suspected.** It says general n
needs the LOWER bound dim H_n(q) >= (n+1)!, citing qou-uoal's note that only the upper half
`finrank_le_factorial` was proved, and then adds: "LEAD, not a claim ... whoever picks this up
should corpus-grep whether the (n+1)! lower bound was ever derived ... before assuming it is
open." Corpus-grepped: `HeckeWedderburnGeneral.finrank_hecke_eq_factorial` is an EQUALITY, and its
own docstring says the lower bound "is forced by the surjection onto a space of dimension
(n+1)!". So the blocker was already discharged and general n was a wire, not a build.

**And it needed LESS than expected: no injectivity.** `heckeIncl_range_lt_top` holds over any
characteristic-zero field at generic q from the dimension count alone
(`LinearMap.finrank_range_le`, no injectivity hypothesis). Enforced structurally --
`HeckeTowerStrict` does not import `HeckeInclInjective`, compiles RC=0 alone. This refutes
`qou-ejde`'s claim that its injectivity result is what makes the filtration strict; noted on that
bean too. Injectivity buys the sharp value `= (m+1)!`, which is the second file and the only one
confined to R.

**Why this bean STAYS OPEN.** The statement proved is about the concrete Hecke tower, not about
`twH` in MathlibExt/HeckeTowerWitness -- whose `twH_zero_lt_one` goes through the rank-2 collapse
that provably cannot separate H 1 from H 2. Transferring needs the bridge, which qou-ejde measures
as separate and unbuilt. This bean's own discipline line already anticipates exactly this: "Do NOT
close it on the strength of the H 1 < H 2 wire alone -- that is one level, not the filtration."
Same principle, one level up: a theorem about the concrete tower is not the `twH` statement.

The REFUTED `g m |-> q*1` sketch recorded above is untouched and stays refuted; nothing here
revives it. The minor `exists_tower_with_nonzero_h` restated-hypothesis cleanup noted in this bean
is also NOT done.


--------

**2026-09-26 (same PR #7456, second commit): strict growth now holds at the COLIMIT
level too -- `H_lt_succ : H n < H (n+1)`. Bean STILL stays open; `twH` is untouched.**

The earlier append recorded strict growth for the concrete tower
(`heckeIncl_range_lt_top`). This adds it for the colimit's range filtration, which is
the mathematically meaningful version: `H n` is now known to be an isomorphic copy of
`Hecke n` rather than merely its image, so `finrank (H n) = (n+1)!` and the levels
separate by dimension.

Route: `ofLim_injective` (faithfulness, proved in the same file via
`DirectLimit.mk_injective` from all-transitions-injective) -> `finrank_H` ->
`H_lt_succ`. **Unlike the concrete-tower half, this one DOES need injectivity** -- so
`qou-ejde`'s third "what this unlocks" claim was right about the colimit and wrong about
the concrete tower. Both corrections are recorded on that bean.

**Why this bean is still open.** Its subject is `twH` in MathlibExt/HeckeTowerWitness,
whose separator is the rank-2 collapse that provably cannot separate H 1 from H 2. The
colimit carrier is a different object. Transferring needs the abstraction bridge, which
is still unbuilt. Also untouched: the minor `exists_tower_with_nonzero_h`
restated-hypothesis cleanup this bean notes, and the REFUTED `g m |-> q*1` sketch stays
refuted.


## 2026-09-26 — strict growth PROVED at the Hecke parameter (PR #7460)

```lean
QOU.SchurWeyl.HeckeTowerWitnessStrict.twH_lt_succ (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) :
    twH (q - q⁻¹) n < twH (q - q⁻¹) (n + 1)
```

`HeckeTowerWitness` had `twH_zero_lt_one` only, and its own docstring warns that
`twH_mono` is `≤`. Every level now.

### The rank-2 collapse is a deeper obstacle than "the target is too small"

This bean's framing is that the separator is a rank-2 collapse. Correct, and the
natural repair — map into a **product** of rank-2 algebras and send one generator
elsewhere — **cannot work**, now machine-checked rather than argued:

```lean
eq_of_braid_of_comm {A} [CommRing A] (h a b : A)
    (ha : a * a = h * a + 1) (hb : b * b = h * b + 1)
    (hbraid : b * a * b = a * b * a) : a = b
```

In a commutative target `b·a·b = a·b·a` becomes `a·b² = b·a²`; substituting the
quadratic on each side gives `h·a·b + a = h·a·b + b`. So braid identifies
**adjacent** generators in any commutative target, hence all of them by chaining,
hence maps every stage onto the same subalgebra. **No commutative algebra
separates two stages — of any rank, product or not.** I tried the product route
first; this is what killed it, before any Lean was written for it. Axioms
`[propext, Quot.sound]`, no choice. Mutant check: dropping the two quadratics
makes `ring` fail, so braid *alone* does not force `a = b`.

### What does separate them

The non-commutative colimit of the honest tower. All three presented relations
hold in `HeckeLim` with **matching indices** (`gLim_quadratic` with `q·q⁻¹ = 1`,
`gLim_braid`, `gLim_far`), so `towerToColimit : HeckeTower ℝ (q−q⁻¹) →ₐ HeckeLim`
is generator-for-generator, not collapsed.

Two supporting facts, and the second is the load-bearing one:

```lean
H_le_adjoin_gLim : H ℝ q q⁻¹ (n+1) ≤ Algebra.adjoin ℝ {g m | m ≤ n}
gLim_notMem_H    : gLim ℝ q q⁻¹ n ∉ H ℝ q q⁻¹ n
```

`H_lt_succ` (PR #7458, merged) says `H n ⊆ H (n+1)` is strict but names **no
witness**. With the generation fact it does: if `g n` were already in `H n`, then
`H (n+1)` — generated by `g 0 … g n` — would collapse into `H n`. That is what
turns a dimension count into a statement about a *generator*, which is exactly
what the `twH` separation needs.

### 🛑 STAYS OPEN — the generic-`R`, generic-`h` case

Not settled, and `eq_of_braid_of_comm` says it is not merely unproved: any
separator for it must be **non-commutative**, and `HeckeTowerWitness` has no
non-commutative model at generic `h`. Constructing one (or finding a different
invariant) is the remaining work. The bean's other item — the restated-hypothesis
cleanup on `exists_tower_with_nonzero_h` — is also untouched.

Verification: `lean -DautoImplicit=false -s 65536` exit 0; `#print axioms` on all
five declarations `[propext, Classical.choice, Quot.sound]`; three mutants all
required to fail and all do.
