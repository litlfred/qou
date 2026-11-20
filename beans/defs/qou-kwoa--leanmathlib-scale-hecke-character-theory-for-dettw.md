---
# qou-kwoa
title: 'Lean/Mathlib-scale: Hecke character theory for det(twGram) at rank >= 2 (Geck-Pfeiffer 7.2.6)'
status: completed
type: task
priority: normal
tags:
    - verify-build
    - reorg-2026-10-04
created_at: 2026-09-02T21:39:20Z
updated_at: 2026-10-04T15:30:48Z
---

Successor to qou-0y6h, split out on owner instruction 2026-09-02 because that
bean's title reads as though a lemma is missing when the remainder is a
book-length development. qou-0y6h is CLOSED at what is proved; this carries the
rest.

## The single deliverable

  det (QOU.Hecke.TwBasis.twGram K q n) != 0  for n >= 2, in Lean.

Everything downstream of it already exists and is sorry-free on main:
isSemisimpleRing_of_twGram_det_ne_zero gives semisimplicity of H_n(q) at every
rank from that one input.

## What is already supplied — do NOT re-derive any of it

* THE BASIS. basisTwOfField, a Module.Basis indexed by Equiv.Perm (Fin (n+1))
  whose vectors are the T_w, with finrank_eq_factorial. Reached WITHOUT
  Matsumoto (still a Mathlib TODO at Coxeter/Basic.lean:78).
* THE MULTIPLICATION TABLE. TwMul.σ_mul_Tw, both branches. Handedness is
  T_v . T_w = T_{wv} (right factor acts first); it is documented, not a typo.
* THE GENERATOR TRACE. TwTrace.trace_lmul_σ and two_mul_trace_lmul_σ.
* THE RANK-ONE CASE, END TO END. twGram_det_rank_one = (1+q)^2 and
  isSemisimpleRing_rank_one, unconditional, no cited class.
* THE TARGET VALUES at n = 1,2,3, exactly, with the integer constant identified
  as prod_lambda d_lambda^(d_lambda^2) — computations/hecke/
  tw_gram_determinant_probe.py, n=3 verified as a POLYNOMIAL IDENTITY (degree
  bound 216, candidate 122, 298 points).
* THE CHARACTERS, SYMBOLICALLY, AT GENERAL n. This is the part that makes this
  bean tractable and it is easy to miss: qou-avt2 (in-progress, Halverson-Ram /
  Jing-Liu) put exact symbolic chi_lambda into
  computations/hecke/hecke_characters.chi_lambda_braid(precision='symbolic_q').

## The identity that ties them together — MEASURED, not assumed

computations/hecke/tw_trace_equals_character_sum_probe.py:

    tr(L_{T_u}) = sum_lambda d_lambda chi_lambda(T_u)

verified for every element of S_3 as exact rational functions, computing the two
sides by wholly independent routes (the T_w multiplication rule, which knows
nothing about Young tableaux, against the Hoefsmit seminormal engine, which
knows nothing about T_w).

CONVENTION BRIDGE, and the identity is FALSE without it:

    QOU.Hecke.IwahoriHecke / the T_w side :  sigma^2 = (Q - 1) sigma + Q
    hecke_characters (seminormal)         :  sigma^2 = (q - 1/q) sigma + 1
    =>  Q = q^2   and   sigma_mine = q sigma_theirs
    =>  tr_mine(L_{T_u}) = q^length(u) * sum_lambda d_lambda chi_lambda(word)

The engine wants a SIGNED, 1-BASED braid word: [(1, i+1), ...].

So the COMPUTE side of the blocker is solved at every rank. What is missing is
the LEAN formalisation of the character theory — the discovery is done.

## Two bounds on this bean, both measured, both permanent

1. THE ROUTE IS ONE-DIRECTIONAL. det(twGram) carries the integer constant
   prod_lambda d_lambda^(d_lambda^2), so in a characteristic dividing it the
   determinant VANISHES even where H_n(q) is semisimple (the regular trace form
   of M_d(K) is degenerate exactly when char K | d). det != 0 => semisimple is
   all this can ever give; the converse is FALSE, counterexample char 2 with q
   of order > 3 at n = 2. Any general theorem here MUST carry a characteristic
   hypothesis, which QGeneric q n does not supply. Costs nothing for the
   substrate (K = R, q > 1). Audit: docs/audits/
   2026-08-30-tw-gram-determinant-measured.md.
2. NO COMBINATORIAL SHORTCUT EXISTS. tr(L_{T_u}) is determined by NONE of
   length(u), cycleType(u), or the pair. Witness in S_5, same length 4 and same
   cycle type (2,2,1): u=(0,3,4,1,2) gives 5(q-1)^2(q^2+4q+1); u=(1,0,4,3,2)
   gives 10(q-1)^2(q^2+q+1). Exact finite computation => refutation with a
   witness. Audit: docs/audits/2026-09-02-tw-regular-trace-not-combinatorial.md.

## TRAP — read before claiming any new pattern here

S_2 satisfies all three of those statistics, S_3 two, S_4 the joint one, S_5
none. I generalised from S_3, then from S_4, and was wrong both times; each
reading was consistent with every datum available when I made it. In this corpus
a Hecke pattern first breaks at n = 4 or n = 5, because that is where S_n first
has two elements of equal length in one conjugacy class. TEST S_5 before
promoting any rank-3 or rank-4 pattern. The probe asserts both halves of the
S_4/S_5 split so a future edit that breaks either fails loudly.

## Scope

Mathlib-scale, multi-session, a research formalisation rather than a proof to be
typed out. Crosses no barrier: semisimplicity is a magnitude-axis fact and
nothing here bears on the P!=NP wall. SchurElementCriterion still has no
instance; both obligations that docs/audits/
2026-08-29-pneqnp-gap-inventory-refresh.md §3b separates (the combinatorial
schurElement equalling the algebra-theoretic one, and GP 7.2.6 proper) remain
open.

## Coordinate

qou-avt2 (in-progress) is the mathematical supplier — cite it, do not duplicate
it. qou-mtx9 records that the GP reduction is the compute bottleneck and scales
with WORD LENGTH, with a batched entry point (chi_lambdas_via_gp) unused in 9
producers; relevant if this bean's verification ever needs characters in bulk.


## Claimed 2026-09-02 by branch claude/p-neq-np-gaps-n8dxxl

First move is a SCOPING CHECK, not construction: is the character-sum route
this bean prescribes circular for the semisimplicity goal? See the entry below.

## 2026-09-02 — SUPERSEDED IN ITS CONCLUSION. Semisimplicity at every rank is DONE.

The bean asked for Geck-Pfeiffer character theory because det(twGram) at rank
>= 2 needs tr(L_{T_u}) for general u. That is still true and still Mathlib-scale.
But the CONCLUSION the determinant route was chasing — semisimplicity of the
Hecke algebra at every rank — did not need it, and was reachable by composing
four things that already existed in the corpus and had never been put together.

QOU/SchurWeyl/HeckeSemisimpleGeneral.lean (new, sorry-free, #print axioms clean
on all four declarations):

  isSemisimpleRing_hecke              q != 0, q^2 != 1  =>  IsSemisimpleRing (Hecke R q q^-1 n)
  isSemisimpleRing_hecke_of_one_lt    1 < q             =>  same, at every n
  wenzlCriterion_of_one_lt            a MODEL for the cited WenzlCriterion
  semisimple_of_one_lt_unconditional  the composition, no cited class left

### The four pieces, all pre-existing

* QOU.SchurWeyl.heckeWedderburn (SW-7): H_{n+1}(q) = prod_lambda M_{d_lambda}(R)
  at EVERY n. I verified the whole chain sorry-free: rskBurnsideHolds
  (sum d^2 = n! from Robinson-Schensted), heckeProduct_surjective, the
  dimension squeeze, heckeProduct_bijective, heckeWedderburn.
* QOU.MathlibExt.MatrixSemisimple.instIsSemisimpleRing_matrix — fills Mathlib's
  proof_wanted IsSemisimpleRing.matrix for division rings.
* Mathlib's finite-product IsSemisimpleRing instance.
* Mathlib's RingEquiv.isSemisimpleRing.

### What this discharges

WenzlCriterion (Information/PNeqNpEquivalence.lean) calls itself a "hypothesis
class, not a theorem of this development" and had NO INSTANCE anywhere in the
corpus. Every consumer of semisimple_of_one_lt was therefore conditional on an
assumption with no known model. It has one now.

NOT an instance, deliberately: a blanket instance over all q would be FALSE as
the class is stated, since WenzlGeneric 0 n holds vacuously (0^k = 0 != 1)
while q = 0 is degenerate. Hence a theorem taking 1 < q.

### What is NOT superseded — the bean stays open for this

* CARRIER. This is QOU.SchurWeyl.Hecke R q q^-1 n, NOT QOU.Hecke.IwahoriHecke
  K q n. Different RingQuots of different relations; bridging them is qou-img9.
  The T_w route remains the only one that reaches IwahoriHecke itself, so
  twGram is NOT retired.
* FIELD. R only. The genericity hypotheses are exactly right over the reals
  (q != 0 and q^2 != 1 force [k]_q != 0 for every k there) and would be wrong
  over a general field, where a root-of-unity hypothesis is needed.
* det(twGram) at rank >= 2 is still open and still Mathlib-scale. What changed
  is that it is no longer the only road to the conclusion — so pursue it for
  the IwahoriHecke carrier and for the determinant value, not because
  semisimplicity depends on it.

### Method note worth keeping

This is the corpus-grep discipline paying at maximum value: a bean scoped as
multi-session research collapsed to one composition file because the pre-build
check found the conclusion already reachable. Run the checklist BEFORE building.

### Tooling trap, recorded because it cost a repair

`beans update --body-append "..."` with a DOUBLE-QUOTED shell argument lets the
shell expand backticks as command substitution. Backticked identifiers were
executed ("proof_wanted: command not found") and their text was DELETED from
the bean, silently truncating the rest of the append. Pass long bodies through
a file, or single-quote the argument.

## 2026-09-03 — the CARRIER item is now CLOSED (qou-img9 / PR follow-on)

One of this bean's three remaining items is done. QOU/SchurWeyl/HeckeCarrierEquiv.lean:

  isSemisimpleRing_iwahoriHecke : 1 < Q -> IsSemisimpleRing (QOU.Hecke.IwahoriHecke R Q n)

at EVERY rank, sorry-free. That is the T_w / twGram carrier, which this bean recorded as
NOT reached by HeckeSemisimpleGeneral.

Mechanism: the two RingQuot relations differ in exactly one clause (the quadratic); braid
and far-commutation are verbatim identical on the same FreeAlgebra. A generator rescaling
sigma |-> c . T moves the quadratic under c(Q-1) = q - qi and c^2 Q = q qi, satisfied
identically by Q = q^2, c = q^-1 at qi = q^-1. Upgraded to an AlgEquiv of carriers, which
is what transports IsSemisimpleRing.

### Remaining items on this bean, now TWO not three

* GENERAL FIELD. Everything is over R, inherited from heckeWedderburn (SW-7), which is an
  R-only construction. carrierEquiv itself is over a CommRing and skeinIwahoriEquiv over
  any Field, so the restriction is upstream, not here.
* det(twGram) AT RANK >= 2 ITSELF. Still Mathlib-scale, still open, and still worth doing
  for the DETERMINANT VALUE — but no longer for the semisimplicity conclusion, which now
  has two independent routes to it. tr(L_{T_u}) is not combinatorial (refuted with an S_5
  witness, #6417); the closed form is Geck-Pfeiffer.

### Note for whoever reads twGram next

isSemisimpleRing_rank_one (#6134) proves semisimplicity of IwahoriHecke at n = 1 over ANY
field with 1 + q != 0, via the determinant. isSemisimpleRing_iwahoriHecke proves it at
EVERY n over R with Q > 1, via Wedderburn. Neither subsumes the other: one is general in
the field, the other general in the rank.


## 2026-09-03 — the "blocked upstream" item is characterised, and it is not an accident

This bean's general-field item read *"blocked upstream — `heckeWedderburn` is
`ℝ`-only"*.  True, and it says nothing about **why**, so it reads as an accident
of statement that a `variable {K : Type*} [Field K]` would fix.  It is not.

Measured on `heckeWedderburn`'s **103-module in-repo import cone**: `Real.sqrt`
does not occur in it at all (so the seminormal form needs no square roots), and
**exactly two** modules use anything `Real.*` in code — both only the `Real.log`
family, both in the single idiom
`zpow_ne_one : q ≠ 0 → q² ≠ 1 → ∀ m ≠ 0, qᵐ ≠ 1`.

**Over `ℝ` that two-line hypothesis IS "q is not a root of unity"** (its own
docstring says it is sharp: `qᵐ = 1 ⇒ |q| = 1 ⇒ q = ±1 ⇒ q² = 1`).  Over a
general field it is not — a primitive cube root of unity satisfies both.

So the general-field statement needs the **classical criterion carried as a
hypothesis**, which is what `QOU/SchurWeyl/GenericParameter.lean` now supplies
(sorry-free): `NotRootOfUnity`, `pow_left_injective`, `zpow_ne_one`,
`poly_eq_zero_of_eval_pow`, and `ofSqNeOne` — the bridge proving the `ℝ` form
implies it, so generalising the cone strengthens no hypothesis.

**Remaining cost, measured: 13 files, 248 occurrences of `ℝ`.**  A tranche, not
an idle-pass step.  Tracked with the rest of the general-field work on
`qou-j377`, whose own headline ("`q` generic, not a root of unity") turns out to
name exactly this; that bean's blocker list was stale — it cited SW-5 and SW-3,
both of which have landed.


## 2026-09-03 — NON-VANISHING IS DONE. The remaining scope is the VALUE only.

Landed on claude/p-neq-np-gaps-n8dxxl, PR #6517 (commits c6986748f3, 6154eac0e7,
3b39d577a9). All sorry-free, [propext, Classical.choice, Quot.sound].

    twGram_det_ne_zero {K} [Field K] [CharZero K] (q : K)
        (hq0 : q != 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : N) :
      (twGram K (q ^ 2) n).det != 0

at EVERY n. No determinant is evaluated anywhere in the proof.

### The bean's framing was right and its route was not the only one

This bean says the deliverable is det != 0 for n >= 2 and lists what is supplied so it
is not re-derived: the basis, the multiplication table, the generator trace, the
rank-one case, the target VALUES at n=1,2,3, and the symbolic characters from qou-avt2.
Every one of those is aimed at COMPUTING the determinant, because Geck-Pfeiffer 7.2.6
is how one normally gets non-vanishing.

None of it was needed. Semisimplicity is proved independently via heckeWedderburn
(#6437, #6486, and Part 1 of #6517), which owes the Gram determinant nothing, so the
implication can be run BACKWARDS: semisimple => regular trace form nondegenerate =>
det != 0 in every basis. The missing piece was the converse of the Gram criterion,
which is three short lemmas.

### What was actually written

QOU/MathlibExt/RegTraceGramNondegenerate.lean

  regTraceForm_mul_assoc   B(xy,z) = B(x,yz). This is what makes the form's radical a
                           TWO-SIDED ideal rather than merely a subspace. Left-closure
                           needs it TOGETHER WITH regTraceForm_comm, because the form
                           is associative only in that one shape.
  regTraceRadical          the radical as a TwoSidedIdeal.
  ..._of_isSimpleRing      the key step: on a simple ring the radical is bot or top,
                           and top would put 1 in it, giving B(1,1) = 0.
  regTraceForm_one_one     B(1,1) = finrank K A, since L_1 = id.
  ..._matrix               the block. Matrix i i K is simple for nonempty i. EMPTY i is
                           handled separately: it is the zero ring and is NOT simple
                           (simplicity requires Nontrivial), but its form is
                           nondegenerate because 0 is its only element.
  regTraceForm_pi / _pi    reassembly over a finite product. A product of matrix
                           algebras is NOT simple, so block verdicts are SUMMED, not
                           transported.
  ..._algEquiv / _congr    transport along an AlgEquiv.

QOU/MathlibExt/TracePi.lean — a pure Mathlib gap, no algebra structure in it.

  trace_piDiag             trace (sum_i f_i) = sum_i trace f_i. Mathlib has ONLY the
                           binary case (LinearMap.trace_prodMap' for M x N).

QOU/Hecke/TwGramDetNonzero.lean — composes skeinIwahoriEquiv with heckeWedderburn.

### Cross-checked against the one rank computed by hand

twGram_det_ne_zero_rank_one_agrees. twGram_det_rank_one evaluates the four
Markov-trace entries directly and gives det = (1+Q)^2; at Q = q^2 its non-vanishing is
q^4 != 1, which is exactly what NotRootOfUnity q supplies. Same conclusion, same
hypothesis, two entirely different routes. Kept as a regression.

### The characteristic hypothesis is load-bearing here, not inherited noise

On Matrix (Fin d) (Fin d) K the regular trace is d * the ordinary matrix trace (left
multiplication acts on d copies of the column space), so the form degenerates EXACTLY
when d = 0 in K. At char p | d_lambda the Gram determinant of a genuinely semisimple
algebra really does vanish. The [CharZero K] carried down from #6486 is spent here.

### STILL OPEN — do not close this bean on the above

1. THE VALUE. det(Gram) = prod_lambda (Schur_lambda)^(f^lambda) is untouched, and it
   is still the book-length development this bean was split out to carry. Everything
   the bean lists as supplied (qou-avt2's symbolic characters especially) is still the
   right material for it. A consumer needing the Schur-element product gets nothing
   from #6517.

2. THE SQUARE ROOT. The statement is at Q = q^2, the same caveat as
   isSemisimpleRing_iwahoriHecke_sq (qou-j377) and for the same reason:
   skeinIwahoriEquiv relates the skein algebra at q to the Iwahori carrier at q^2, and
   a general field need not contain a root. Removing it needs BASE CHANGE of
   IwahoriHecke along a field extension. Note the hypothesis would survive that move
   for free -- NotRootOfUnity Q => NotRootOfUnity q when q^2 = Q, since q^m = 1
   implies Q^m = 1 -- so the missing piece is only the algebra's scalar extension.
   Over R with Q > 0, or any field where Q is a square, twGram_det_ne_zero_of_sq
   already gives the statement at Q.

Build note for whoever picks this up: Mathlib.RingTheory.SimpleRing.Matrix and two of
its deps are NOT in the lake-cache/qou-v4-24-0 restore. Build them lean-direct INTO the
mathlib build tree (7 s for all three). A scratch LEAN_PATH directory does NOT work --
Lean commits to the first path root containing Mathlib/, so a partial scratch tree
silently shadows the entire real one.


## 2026-09-03 21:58 — item 3 (the square root) PRICED. The ideal-quotient route is CLOSED.

Measured against Mathlib at lake-cache/qou-v4-24-0, not estimated. Recording because
"needs base change of IwahoriHecke" is not actionable on its own, and the obvious way to
do it does not work.

### What exists

  LinearMap.trace_baseChange              Mathlib/LinearAlgebra/Trace.lean:336
  RingQuot.ringQuotEquivIdealQuotient     Mathlib/Algebra/RingQuot.lean:505
  quotIdealMapEquivTensorQuot             Mathlib/RingTheory/TensorProduct/Quotient.lean:42

That reads like a complete chain: IwahoriHecke is a RingQuot, turn it into an ideal
quotient, base-change the ideal quotient, base-change the trace. It is not.

### Why it is closed

ringQuotEquivIdealQuotient sits inside `section CommRing` with `variable [CommRing B]`
(RingQuot.lean:470). IwahoriHecke K Q n is RingQuot (HeckeRel K q n) on
FreeAlgebra K (Fin n), which is NONCOMMUTATIVE for n >= 2 -- and n >= 2 is the entire
content of this bean. So the bridge does not apply, and neither does
quotIdealMapEquivTensorQuot downstream of it: Mathlib's `Ideal B = Submodule B B` is a
LEFT ideal, and the whole ideal-quotient machinery is commutative-only here.

Nor is there a free-algebra base change to start from. Searched: every file mentioning
FreeAlgebra intersected with every file mentioning TensorProduct or baseChange gives one
hit, Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean, and that is FreeAlgebra being USED to
define TensorAlgebra -- not a scalar-extension lemma. There is no
`L (x)_K FreeAlgebra K X = FreeAlgebra L X` in Mathlib.

### The route that IS open, and it is cheaper than it looks

Do the base change on RingQuot directly via the UNIVERSAL PROPERTY, never touching ideals.
The corpus already has both halves of that property for this algebra:

  QOU.SchurWeyl.iwahoriLift        HeckeCarrierEquiv.lean:104  -- generators -> AlgHom out
  QOU.SchurWeyl.iwahori_hom_ext    HeckeCarrierEquiv.lean:130  -- two AlgHoms agreeing on
                                                                  generators are equal

They are the same tools carrierEquiv / skeinIwahoriEquiv are built from, so the pattern is
already worked in this file. Build AlgHoms both ways between L (x)_K IwahoriHecke K Q n and
IwahoriHecke L Q n and kill the composites with iwahori_hom_ext.

Four pieces, in dependency order:

  1. L (x)_K H_K as an L-algebra whose `1 (x) sigma_i` satisfy HeckeRel L Q n. Needs
     Algebra.TensorProduct.lift for the map OUT of the tensor.
  2. The two AlgHoms and the round trips (iwahori_hom_ext both ways).
  3. Basis compatibility: basisTwOfField L Q n corresponds to 1 (x) basisTwOfField K Q n.
     Probably the fiddliest piece -- Module.Basis.baseChange exists but tying it to the
     T_w indexing is work.
  4. Gram compatibility: twGram L Q n = (twGram K Q n).map (algebraMap K L), then
     det commutes with a ring hom and algebraMap of a field is injective.

The hypothesis needs nothing: NotRootOfUnity Q => NotRootOfUnity q when q^2 = Q, since
q^m = 1 forces Q^m = 1. So this buys the statement at a general Iwahori parameter Q, over
any characteristic-zero field, with no square root assumed.

### Recommendation (my judgement, not a finding)

LOW priority relative to the value (item 1). It never bites in the corpus's own use: the
substrate q0 ~ 1.11 is real and positive, so a square root always exists, and over any
algebraically closed field every Q is a square. It is a mathematical tidying of a
statement that is already sharp where the framework stands. Worth doing if someone wants
the clean general-field theorem; not worth pre-empting the Schur-element work for.


## 2026-09-03 22:20 — RE-VERIFIED against a purged tree, and two harness traps

Ran an adversarial re-check of the whole PR (nothing had changed on it: no reviews, no
comments, no check runs, zero drift across 137 main commits).  Everything holds, and the
verification is now stronger than it was -- but only because a false-green mechanism turned
up in the process.

RESULT: all six touched modules exit 0, twelve declarations
[propext, Classical.choice, Quot.sound], against a tree with the stale dependency oleans
DELETED and rebuilt from source.  Trust that pass, not the earlier file-by-file one.

### Trap 1 — LEAN_PATH shadowing applies to QOU/, not just Mathlib/

Lean commits to the FIRST LEAN_PATH root containing the module's top-level directory and
does NOT fall through.  So /tmp/qoubuild + qb.sh is sound only while the ENTIRE cone lives
in the scratch dir.  Reproduced deliberately: after emptying it, five of six modules failed
naming dependencies that were sitting in .lake/build the whole time.

### Trap 2 — the restored olean cache goes stale, and "skip if present" then FALSE-GREENS

lake-cache/qou-<toolchain> is a snapshot.  A module whose source changed since has an olean
that is present, loadable and WRONG.  Proved by CONTENT, not timestamps:

    strings .lake/build/lib/lean/QOU/SchurWeyl/HeckeWedderburnGeneral.olean \
      | grep -c NotRootOfUnity        ->  0

while the source defines heckeWedderburn with exactly that hypothesis.  The cache still held
the pre-#6486 R-only signature, and a builder that skipped on existence typechecked new code
against it, reporting the new code's own hypotheses as unknown identifiers.

### CAVEAT ON MY OWN MEASUREMENT — do not quote "21 stale oleans"

A first pass counted 21 by comparing mtimes.  `git checkout` sets source mtimes to checkout
time, so an mtime comparison over a fresh clone flags files whose content never changed.
Established BY CONTENT: exactly one file, HeckeWedderburnGeneral.  The rest of the group is
consistent with the general-field tranche landing after the snapshot but was not verified
one by one.

That same unsoundness killed a helper script I started writing to automate this: an
mtime-driven dependency walker treats every Mathlib source as stale and walks the whole
import graph.  Its own --selftest caught a SECOND bug first (deciding staleness BEFORE
recursing, so a stale grandchild is invisible -- the exact trap the script existed to
prevent).  Script DROPPED rather than shipped half-working; it is build tooling, not this
bean's work.  Anyone who wants it must not key on mtime.

### The rule that survives all of the above

After restoring the olean cache, a lean-direct verification is only as current as the
dependency oleans it loads.  Rebuild the cone from source before trusting a green on any
module whose dependencies this branch or a recent merge touched.


## 2026-09-04 — the VALUE: two steps landed, and the next one is a NAMED Mathlib gap

Branch claude/p-neq-np-gaps-n8dxxl, PR #6552 (commits d978d1b6df, e6993c2692).
Sorry-free, [propext, Classical.choice, Quot.sound].

### Corpus-grep re-priced this item DOWNWARD before anything was written

QOU/MathlibExt/WenzlSchurElement.lean (597 lines) ALREADY formalises the concrete Schur
element s_{lambda,X}(Q) = Q^{n(lambda)} prod_x (1 - X Q^{c(x)})/(1 - Q^{h(x)}) and proves
sorry-free: schurElement_ne_zero, schurElement_tl_eq_zero_iff (an iff), substrate_avoids_tl_locus.
The Schur element is NOT the missing piece.  The IDENTITY linking it to the Gram determinant
is, and SchurElementCriterion is currently a CITED CLASS in
content/.../information-theory/qou-p-neq-np.md rather than a derived result.

### What landed

QOU/MathlibExt/RegTraceMatrix.lean

  regTraceForm_matrix        regTraceForm K (Matrix i i K) x y = (card i) * (x*y).trace.
                             The SHARP form; regTraceForm_one_one was only the diagonal.
                             Short because trace_piDiag (#6517) applies directly: lmul M
                             acts on each COLUMN independently, so it is literally
                             block-diagonal with card i identical blocks.  The Pi trace
                             lemma has now paid for itself twice.
  regTraceForm_single        tr(E_ij E_kl) = delta_jk delta_il, scaled by d.
  regTraceGram_stdBasis_eq   the Gram IS (d . 1).submatrix prodComm id.
  regTraceGram_stdBasis_det  det = sign(prodComm) * d^(d^2).
  ..._det_ne_zero_iff        vanishes exactly when (d : K) = 0 -- the SHARP form of the
                             obstruction that 2026-08-30-tw-gram-determinant-measured.md
                             states as the PREMISE of its scope-(b) exclusion.  It was
                             asserted there; it is proved now.
  card_mul_trace_one_eq_finrank_matrix
                             regression: regTraceForm_one_one (from L_1 = id) and
                             regTraceForm_matrix (from the column decomposition) share no
                             argument, so their agreement at (1,1) checks both.

### Cross-check against the probe, and it is not circular

Assembling d^(d^2) over the Wedderburn blocks reproduces the integer constant that
tw_gram_determinant_probe.py got by factoring EXACT symbolic determinants:

    n=1  dims 1,1        -> 1              probe 1
    n=2  dims 1,2,1      -> 16             probe 2^4
    n=3  dims 1,3,2,3,1  -> 6198727824     probe 2^4 . 3^18

The probe did not use the lemma and the lemma did not use the probe.  First time that
constant has been DERIVED rather than observed.

### THE NEXT STEP IS BLOCKED ON A NAMED MATHLIB GAP — measured, not guessed

The ASSEMBLY (per-block factor -> full constant) needs the Gram of a product form in a
product basis to be block diagonal, then its determinant.  Mathlib has

    Matrix.det_blockDiagonal   (Determinant/Basic.lean:600)   -- UNIFORM block size only:
                               (blockDiagonal M).det = prod_k (M k).det,  M : o -> Matrix n n R

and has NO determinant lemma for Matrix.blockDiagonal' (Data/Matrix/Block.lean:566), the
DEPENDENT/sigma-indexed version.  Searched: every file in Mathlib mentioning blockDiagonal'
(6 files) intersected with every mention of det -- 3 files, none stating a determinant
formula for it.  The Wedderburn blocks have DIFFERENT sizes d_lambda, so the uniform lemma
does not apply.

This is the same SHAPE of gap as trace_piDiag was in #6517: Mathlib had the binary
trace_prodMap' but not the Pi version; here it has the uniform det_blockDiagonal but not
the dependent one.

COST WARNING: Mathlib's proof of the uniform det_blockDiagonal is ~60 lines of permutation
combinatorics (sum over permutations, sign_prodCongrLeft).  The dependent version is HARDER
-- permutations of Sigma i, m' i that preserve fibres.  This is a real tranche, not a
one-liner.  Do not start it believing otherwise.

### Still not claimed

Nothing here touches the q-part of the determinant, where the Schur elements live.  This is
NOT a proof of Geck-Pfeiffer 7.2.6.  Small characteristic and the square root (Q = q^2)
are both untouched.


## 2026-09-04 — the assembly landed, and the blocker I named was not one

PR #6552, commit 7cc1e15899. QOU/MathlibExt/RegTraceGramProduct.lean, 210 lines,
10 declarations, all sorry-free ([propext, Classical.choice, Quot.sound]).

**CORRECTION to this bean's own prior 'next' line.** I recorded the assembly as
blocked on a named Mathlib gap: Matrix.det_blockDiagonal is uniform-block-size
only and there is no det lemma for Matrix.blockDiagonal'. Both halves are true.
NEITHER IS THE OBSTRUCTION. Matrix.BlockTriangular.det_fintype
(LinearAlgebra/Matrix/Block.lean:276) already gives
    M.det = prod over k of (M.toSquareBlock b k).det
for fibres of arbitrary, DIFFERING size, and a block-diagonal matrix is
block-triangular for every b. My search was 'det' intersected with
'blockDiagonal'' — the capability is filed under the weaker hypothesis that
makes it true, not under the data structure I had in hand. Recorded as a TRAP in
.claude/agent-memory/corpus-grepper/MEMORY.md ('in an UPSTREAM library, grep the
statement SHAPE, not the data structure'). The cost estimate that travelled with
the wrong verdict ('~60 lines of permutation combinatorics') was wrong too.

**What is now proved.** det_eq_prod_of_offDiagonal_eq_zero (the general reusable
statement); det_blockDiagonal' as an immediate corollary (stated for evidence,
not use); regTraceForm_pi_single_of_ne/_same; regTraceGram_pi_offDiagonal/
_diagonal/_det/_det'; regTraceGram_pi_matrix_det; and
regTraceGram_pi_matrix_det_ne_zero_iff — the product Gram determinant vanishes
EXACTLY when a block dimension dies in K, so RegTraceGramNondegenerate's
char-zero hypothesis is not merely sufficient but exactly right.

**The integer constant is DERIVED, not observed.** prod_lambda d^(d^2) over the
Wedderburn blocks of H_{n+1} gives 1 / 16 / 6198727824 at n = 1,2,3 — exactly
tw_gram_determinant_probe.py's measured constants, obtained independently by
factoring exact symbolic determinants. Re-verified in exact integer arithmetic
this session (hook-length formula, no floats); it also yields an n=4 value the
probe never computed.

**STILL OPEN, and the scope is unchanged:**
1. The T_w transport. This is the determinant in the PRODUCT basis; moving to
   the T_w basis changes it by (det P)^2, so the constant is pinned only up to a
   square. This is now the smallest remaining piece of the value item.
2. The q-part, where the Schur elements live. Untouched. NOT Geck-Pfeiffer.
3. Small characteristic — unreachable by this route at all (and item (1) of the
   new file says why: the obstruction is exactly a block dimension dying in K).
4. The square root Q = q^2 — low priority; never bites in the corpus's use.


## 2026-09-04 (later) — the T_w transport landed; the square class is now exact

PR #6617, commits b9577649e6 + cf132314f0. Two files, seven declarations, all
sorry-free at [propext, Classical.choice, Quot.sound].

**The payoff.** twGram_det_eq_sq_mul_prod: the LEFT side is literally
(twGram K (q^2) n).det, and it equals P.det^2 * prod_lambda +/- d_lambda^(d_lambda^2)
with IsUnit P.det, where d_lambda = card of the standard Young tableaux of shape
lambda. So the integer constant #6552 derived is now attached to the corpus's
ACTUAL object, not just to a product basis.

**The general transport** (QOU/MathlibExt/RegTraceGramBasisChange.lean):
bilin_toMatrix_det_basis_change (the square), bilin_toMatrix_det_reindex
(relabelling moves nothing — this is what lets a sigma-indexed product basis be
compared with a permutation-indexed T_w basis at all), isUnit_det_basis_toMatrix,
regTraceGram_toMatrix_map (an ALGEBRA equivalence contributes NO factor, since
the regular trace form is an algebra invariant — so the Wedderburn isomorphism
is free and the only square comes from the change of basis within the algebra),
and the composition.

**Two corrections to my own work, both caught by re-reading the prose against
the Lean.** (1) I wrote 'this gets the same non-vanishing as a corollary' over an
existential that carried nothing about P.det being nonzero — the corollary did
NOT follow. Fixed by STRENGTHENING the statement to include IsUnit P.det, not by
softening the prose. (2) I claimed each block factor 'is nonzero in
characteristic zero'; true, but not proved here (needs 0 < d_lambda, i.e. every
shape admits a standard tableau). It is now an explicit hypothesis on
twGram_det_ne_zero_of_blocks.

**Cross-check.** twGram_det_ne_zero_of_blocks reaches non-vanishing THROUGH the
determinant; TwGramDetNonzero reaches it via semisimplicity without computing a
determinant at all. Independent, neither derived from the other.

**STILL OPEN, and the shape of what remains has changed:**
1. det P is NOT evaluated. Note this is NOT merely 'not done yet' — a Gram
   determinant is an invariant only UP TO SQUARES OF UNITS, because congruence
   G -> P^T G P is the transformation law of a bilinear form. So no theorem of
   this shape can pin the integer on the nose. What IS true, and is now proved,
   is that prod d_lambda^(d_lambda^2) is exactly the SQUARE CLASS of det(twGram).
   Pinning a representative would need det P for the specific Wedderburn matrix.
2. The q-part, where the Schur elements live. Untouched, and now clearly the
   large remaining item. WenzlSchurElement.lean already has the concrete Schur
   element with non-vanishing proved; the missing piece is the IDENTITY linking
   it to the Gram determinant, and SchurElementCriterion is still a CITED CLASS.
3. 0 < d_lambda — small, separate, would discharge the corollary's hypothesis.
4. Small characteristic — unreachable by this route; #6552's
   regTraceGram_pi_matrix_det_ne_zero_iff says exactly why.
5. The square root Q = q^2 — low priority, never bites.


## 2026-09-04 (later still) — the theorem's prediction TESTED against independent data

PR #6648, commit f5b3cc8a90. #6617 merged as 14af928227.

The T_w transport theorem makes two predictions about det(twGram), a quantity
tw_gram_determinant_probe.py measured EARLIER by factoring exact symbolic
determinants of the regular representation. Both hold at all three ranks it
reached.

 (A) SIGN: prodComm on J x J with |J| = d fixes the d diagonal pairs and swaps
     the other d(d-1)/2, so signature (-1)^(d(d-1)/2); the determinant's sign is
     the product over blocks.
 (B) SQUARE CLASS: all q-dependence sits inside (det P)^2, so dividing out the
     signed integer constant must leave a PERFECT SQUARE in Q(q).

(B) is the substantive one — a determinant of this size has no reason for every
exponent to be even, and ONE odd exponent anywhere refutes the theorem's claim
that the Wedderburn isomorphism contributes no factor.

MEASURED (computations/hecke/tw_gram_square_class_crosscheck.py, exact):
  n=1  dims 1,1        sign +1  const 1            q-part (q+1)^2
  n=2  dims 1,2,1      sign -1  const -16          q-part q^2(q+1)^2(q^2+q+1)^6
  n=3  dims 1,3,2,3,1  sign -1  const -6198727824
                       q-part q^22(q+1)^48(q^2+1)^20(q^2+q+1)^6
All perfect squares; sign correct at all three.

NOT CIRCULAR: the probe predates the theorem and neither used the other.
NOT A PROOF: three ranks are three data points. det P is still not evaluated —
the square roots tabulated are READ OFF the measurement.

**A DISTINCTION THAT MATTERS AND WAS NOT PREVIOUSLY WRITTEN DOWN HERE.** twGram
is the REGULAR trace form tr(L_xy). Geck-Pfeiffer's Schur elements belong to the
CANONICAL SYMMETRIZING trace tau, with tau(T_w) = delta_{w,1}. THESE ARE
DIFFERENT FORMS. So prod_lambda d_lambda^(d_lambda^2), derived for the regular
form, is the ANALOGUE of prod_lambda s_lambda^(f^lambda), not the same object.
Any future attempt on the q-part must start from this: the corpus's Gram is not
the Gram that Geck-Pfeiffer 7.2.6 is about. Conflating them would produce a
confident wrong identification.

**SharpElementCriterion is unaffected and remains a CITED CLASS.** Note the
tempting shortcut and why it is NOT taken: since semisimplicity at
NotRootOfUnity q is already proved independently via heckeWedderburn, an
instance of SchurElementCriterion could be discharged trivially (the implication
holds because its conclusion is separately available). That instance would be
mathematically true and epistemically worthless — it would make
semisimple_of_substrate LOOK like a Schur-theoretic result when it is a
Wedderburn one, with the Schur elements doing no work. Do not declare it.

**NEXT, priced with its route named:** the Lean sign lemma
  Equiv.Perm.sign (Equiv.prodComm i i) = (-1)^(card i * (card i - 1) / 2)
via Equiv.Perm.sign_of_cycleType (Mathlib/GroupTheory/Perm/Cycle/Type.lean:164)
— prodComm squares to 1 so its cycle type is all 2s — plus #support = d^2 - d
(the fixed points are exactly the diagonal), with two_dvd_card_support (:194)
for the divisibility. The support computation is the bulk. Not free, not a
tranche. Naming the route rather than asserting a gap is deliberate, after the
det_blockDiagonal' error earlier in this same arc.


## 2026-09-04 (evening) — the block sign is now EVALUATED, not abstract

PR #6680, commit 73d7636618. #6648 merged as 18d1c3b6aa.

QOU/MathlibExt/SignProdComm.lean: sign_prodComm gives
  Equiv.Perm.sign (Equiv.prodComm i i) = (-1)^(card i * (card i - 1) / 2)
so the per-block sign in twGram_det_eq_sq_mul_prod is explicit rather than a
black box. Seven declarations plus three decide checks, all sorry-free.

THE STEP WORTH REMEMBERING. sign_of_cycleType gives (-1)^(sum + card), i.e.
(-1)^(s + s/2) for an involution with support s. The support is the OFF-DIAGONAL
(prodComm fixes exactly the (a,a)), so s = d^2 - d = d(d-1). That s is EVEN —
a product of consecutive integers — is what kills the first summand and collapses
the formula to (-1)^(s/2). Without it there is no simplification to the half-count.

THE ROUTE WAS NAMED BEFORE IT WAS WALKED, and that is the process point. #6648's
audit doc priced this lemma and named its Mathlib route (sign_of_cycleType,
#support = d^2-d via Finset.offDiag, two_dvd_card_support) instead of asserting a
gap. Everything was there; the support computation was the bulk, as predicted.
Contrast the det_blockDiagonal' error earlier in this same arc, where a blocking
Mathlib gap was recorded for a capability filed under a weaker hypothesis.

FOUR INDEPENDENT CONFIRMATIONS. decide at d = 1,2,3 evaluates the signature by
BRUTE FORCE (not via the cycle-type argument) giving 1, -1, -1 against (-1)^0,
(-1)^1, (-1)^3; and tw_gram_square_class_crosscheck.py on main matches the measured
determinant signs +, -, - at n = 1,2,3.

A LEAN TRAP RECORDED IN THE FILE. (Equiv.prodComm i i : Equiv.Perm (i x i)).support
does NOT work — the ascription is unfolded before dot-notation resolves, so Lean
looks for Equiv.support. Hence the named prodSwap wrapper whose declared type has
head constant Equiv.Perm. Cost a build cycle; not obvious from the error text.

**STILL OPEN, unchanged in substance:**
1. det P is NOT evaluated. The constant stays pinned only up to a square, and that
   is not merely unfinished — a Gram determinant is an invariant only up to squares
   of units.
2. THE Q-PART, where the Schur elements live. Untouched, and the large item. Read
   the trace-form caveat first: twGram is the REGULAR trace form; Geck-Pfeiffer's
   Schur elements belong to the CANONICAL SYMMETRIZING trace tau.
3. 0 < d_lambda — small; discharges twGram_det_ne_zero_of_blocks's hypothesis.
4. Small characteristic — unreachable by this route.
5. The square root Q = q^2 — low priority, never bites.


### 2026-09-05 — increment 2: `τ` exists, and my own blocker claim was wrong

**Commit `e0f192c5e6`** on `claude/p-neq-np-gaps-n8dxxl`, PR #6758.
`QOU/MathlibExt/InvMonomialDet.lean` + `QOU/Hecke/TauSymmetrizing.lean`, 11
declarations, all `[propext, Classical.choice, Quot.sound]`, `lean`-direct
exit 0 with no warnings.

**CORRECTION of the previous increment's docstring (mine, one day old).**
#6758 recorded that Mathlib has no symmetric-algebra theory — measured, and
still true — and inferred from that that constructing the canonical
symmetrizing trace `τ` would require building that theory first. **The
inference does not follow.** `τ` is the `T_1`-coordinate in the `T_w` basis,
and `basisTwOfField` already supplies the basis:

    tau := (basisTwOfField K q n).coord 1

`τ(T_w) = δ_{w,1}` then falls out of `Module.Basis.repr_self`. So the first of
the two "open facts" named in #6758 is **closed**. Absence of a library is
evidence about the library, not about the construction — the same shape as the
`det_blockDiagonal'` retraction earlier in this arc.

**What is genuinely open, narrower and newly legible.** The structure-constant
identity

    τ(T_v · T_w) = δ_{w, v⁻¹} · q^{ℓ(v)}

— this is what makes the Gram monomial, and it is the whole remaining content.
`QOU.Hecke.TwBasis.σ_mul_Tw` is the **full** structure-constant table (up and
down cases in one identity), so the induction is available in principle. It
does **not** close on `ℓ(v)` alone: `τ(σ_i · z) = q · [T_{s_i}-coefficient of
z]`, a different coordinate. Geck–Pfeiffer 8.1.1 inducts on `ℓ(v) + ℓ(w)`
instead, using a common descent `s` to write
`T_v T_w = (q−1)·T_{vs}T_w + q·T_{vs}T_{sw}` — both terms of smaller total
length, so the recursion closes on `τ` alone. Still missing: the descent
decomposition in this corpus's handedness (`T_v T_w = T_{wv}`, **not**
`T_{vw}` — `TwMul` docstring says this is the representation's handedness, not
a typo), and the exchange fact supplying a common descent.

**Proved outright:** `tau_Tw_mul_Tw_of_length_add` — the identity on its
length-additive locus. Worth noting *why that is weak evidence*: on that locus
`w = v⁻¹` forces `ℓ(w)+ℓ(v) = ℓ(1) = 0`, so `q^{ℓ(v)} = q^0 = 1` and the locus
never exercises the `q`-powers at all. It is a consistency check, not a
partial proof.

**Proved conditionally:** `tauGram_det_of_structure_constants` and
`tauGram_det_ne_zero_of_structure_constants` take the identity as an explicit
**hypothesis** — never an axiom, never a `sorry`. Discharging it later makes
both unconditional with no change to either proof.

**Scope of the non-vanishing, stated so it is not over-read.** `det(τ-Gram) ≠ 0`
for all `q ≠ 0` is **not** semisimplicity — that is false at roots of unity. It
says `H_n(q)` is a *symmetric Frobenius* algebra, true for every `q ≠ 0`.
Combined with #6758's `weightedGram_det_ne_zero_iff` at weights `1/s_λ` it
would give **one** direction of the criterion: some `s_λ = 0` ⟹ not split
semisimple. The converse (Tits deformation) is a separate argument, not here.

`SchurElementCriterion` remains a cited class with **no instance**.

**Remaining fact 2, unchanged:** that `τ`'s weights are `1/s_λ` for the Wenzl
`schurElement` in `WenzlSchurElement.lean`. That identification is where `q`
enters and is where the Schur elements do their work.


### 2026-09-05 — CORRECTION: the induction does NOT need the exchange condition

I wrote two hours ago that the remaining step needs *"the exchange fact
supplying a common descent"*, following the usual statement of Geck–Pfeiffer
8.1.1 (induct on `ℓ(v) + ℓ(w)`, pick a descent common to both). **Measured:**
Mathlib's `Mathlib/GroupTheory/Coxeter/` has the descent API in full —
`IsLeftDescent`, `IsRightDescent`, `isLeftDescent_inv_iff`,
`exists_leftDescent_of_ne_one`, `length_inv`, `length_eq_zero_iff`, the `+1`
characterisations — and **no exchange condition at all**: zero occurrences of
`xchange` in the directory. So that route was blocked on a Mathlib gap I would
have had to fill first.

**It is not needed.** Worked on paper: induct on `ℓ(v)` **alone**, take *any*
left descent `i` of `v` (`exists_leftDescent_of_ne_one`), and split on whether
`i` is a right descent of `w`. With `v' = s v`, `w' = w s`, in this corpus's
handedness (`T_a T_b = T_{ba}`, so `T_v = T_{v'} T_s`):

* **ascent** (`i` not a right descent of `w`): `T_s T_w = T_{ws}`, so
  `τ(T_v T_w) = τ(T_{v'} T_{w'})`, at `ℓ(v') = ℓ(v) − 1`. The IH's delta needs
  `w s = v'⁻¹`, i.e. `w = v⁻¹`, which forces `ℓ(ws) < ℓ(w)` — contradicting the
  ascent. Both sides vanish.
* **descent**: `T_w = T_s T_{w'}`, so
  `T_v T_w = T_{v'} T_s² T_{w'} = (q−1)·T_{v'}T_w + q·T_{v'}T_{w'}`, both at
  `ℓ(v')`. The first term's delta needs `w = v'⁻¹ = v⁻¹s`, which forces
  `ℓ(v⁻¹s) < ℓ(v⁻¹)` from the left descent and `ℓ(v⁻¹) < ℓ(v⁻¹s)` from the
  right — contradictory, so it drops. The second gives `q · δ_{w,v⁻¹}
  q^{ℓ(v)−1}` = the claim.

Both branches turn on one observation: a left descent of `v` and a right
descent of `w` at the **same** `i` are contradictory once `w` is pinned to
`v⁻¹` or `v⁻¹s`, because `ℓ(sv) = ℓ(v⁻¹s)` (`length_inv`). The `(q−1)` term
never contributes, which is why no common descent is required.

**Remaining corpus obligations, now the whole list:**

1. `Tw v = Tw (s*v) * Tw s` when `i` is a left descent of `v` — `Tw_mul_Tw`
   under the right length hypothesis.
2. `Tw s * Tw w = Tw (w*s)` when `i` is not a right descent of `w` — same
   lemma.
3. `Tw s * Tw s = (q−1)·Tw s + q·1` — the `v = swap` case of `σ_mul_Tw`,
   plus `Tw (s i) = σ i`.
4. The bridge from this corpus's concrete condition `v i.castSucc < v i.succ`
   to `CoxeterSystem.IsLeftDescent` / `IsRightDescent`. `LengthAdditive.lean`'s
   `length_mul_eq_add_iff` is the likely hook.

Docstring in `QOU/Hecke/TauSymmetrizing.lean` corrected to match; `lean`-direct
still exit 0.


### 2026-09-05 — PROVED. `τ(T_v T_w) = δ_{w,v⁻¹} q^{ℓ(v)}`

Commit `f7cfe5059a`. `QOU/Hecke/TauStructureConstants.lean`, 10 declarations,
all `[propext, Classical.choice, Quot.sound]`, `lean`-direct exit 0 no
warnings. The hypothesis `TauSymmetrizing` was carrying is discharged, so
`tauGram_det` and `tauGram_det_ne_zero` are **unconditional**.

The four obligations listed two hours ago all landed, and each was smaller than
billed:

| obligation | what it actually took |
|---|---|
| bridge `cs.simple i` ↔ `s n i` | `rw [CoxeterSystem.simple]; exact toPerm_simple n i` |
| `Tw (s n i) = σ i` | `orbitMap_injective` + `Rs_single_perm` at `v = 1` |
| `T_s² = (q−1)T_s + q` | the `v = s` case of `σ_mul_Tw` — it lands in the DOWN branch because `s_i` inverts its own pair by construction |
| the three decompositions | all `Tw_mul_Tw` under the length hypothesis the descent supplies |

Obligation 4 as I stated it ("bridge the concrete `v i.castSucc < v i.succ` to
`IsLeftDescent`") **was not needed at all**: phrasing everything through
`Tw_mul_Tw`, which takes a *length* hypothesis, keeps the concrete inversion
condition out of the argument entirely. `σ_mul_Tw` is used exactly once, for
the quadratic relation, where the condition is decidable on the spot.

**The route is the result.** No exchange condition — Mathlib has none — and the
`(q−1)` term never contributes. Both branches close on: a left descent of `v`
and a right descent of `w` at the *same* `i` are contradictory once `w` is
pinned to `v⁻¹` or `v⁻¹s_i`, since `ℓ(s_i v) = ℓ(v⁻¹ s_i)` (`length_inv`).

**Scope unchanged, and this is worth restating because the result looks
stronger than it is.** `det(τ-Gram) ≠ 0` for every `q ≠ 0` is **Frobenius-ness,
not semisimplicity** — semisimplicity is false at roots of unity, so any
reading of this as a semisimplicity criterion is wrong. Combined with
`weightedGram_det_ne_zero_iff` at weights `1/s_λ` it gives one direction of the
Schur criterion: some `s_λ = 0` ⟹ not split semisimple.

**One fact remains between here and `SchurElementCriterion`:** that `τ`'s
Wedderburn weights are `1/s_λ` for the Wenzl `schurElement`. That identification
is where `q` enters and is where the Schur elements do their work. Plus, for the
converse direction, Tits deformation. `SchurElementCriterion` still has **no
instance**, and the `heckeWedderburn` shortcut is still refused in the file.


### 2026-09-05 — option 2 under way (owner picked 2 **and** 3)

Two bricks landed, both needed before an abstract Schur element is even
*definable*.

**`tau_mul_comm` (`15c28feb2a`)** — τ is a **trace**. Falls out of the structure
constants: swapping `v,w` in `δ_{w,v⁻¹}q^{ℓ(v)}` gives `δ_{v,w⁻¹}q^{ℓ(w)}`, equal
because `w = v⁻¹ ↔ v = w⁻¹` and `ℓ(v⁻¹) = ℓ(v)`. Extended off the basis with
`LinearMap.ext_basis` on `(x,y) ↦ τ(xy)` against its flip. Not available before
the identity.

**`QOU/MathlibExt/TraceIsWeighted.lean` (`4d0e8a3468`)** — 8 declarations. Proves
what `WeightedTraceGram`'s docstring had only **asserted** as motivation:

> a linear `t` on `∏_i M_{d_i}(K)` with `t(xy) = t(yx)` is exactly
> `weightedTrace c`, with `c i = t(E^{(i)}_{aa})` for any diagonal unit.

Two matrix-unit identities, both *consequences* of the trace property:
`E_ab = E_aa E_ab` with `E_ab E_aa = 0` for `b ≠ a` (kills off-diagonal units);
`E_aa = E_ab E_ba` and `E_bb = E_ba E_ab` (a trace is **constant** on a block's
diagonal units). The second is the load-bearing one: it is what makes "τ's
weight on block λ" well defined independently of the chosen unit, hence what
makes `1/c_λ` a definable object.

Also: `weightedTraceₗ` (bundled as a `LinearMap` so `Basis.ext` applies) and
`blockUnitBasis` (the matrix units **are** a basis, indexed by the same
`Σ i, J i × J i` that `weightedGram` uses).

**Next in option 2:** transport `eq_weightedTrace` along the Wedderburn
equivalence to get τ's block weights `c_λ` for `H_n(q)`, define the abstract
Schur element `s_λ := 1/c_λ`, and state the vanishing criterion on those. Then
option 3: pin `X`, identify Wenzl's `schurElement Q X` with `s_λ`, and build
Tits deformation for the criterion's forward direction.


### 2026-09-05 — OPTION 2 COMPLETE (`a2484e8797`)

`QOU/MathlibExt/TraceWeightsOfAlgEquiv.lean` (5) + `QOU/Hecke/TauSchurElement.lean`
(7). Arc total **62 declarations across 7 files**, all `[propext,
Classical.choice, Quot.sound]`, zero `sorryAx`.

The abstract Schur element `s_λ := 1/c_λ` now **exists and is nonzero**, for any
splitting and every `q ≠ 0`:

`tau_eq_zero_of_forall_mul` (τ nondegenerate — the `T_w` coordinates of an
annihilated `z` are a left null vector of `tauGram`, det ≠ 0) →
`traceWeight_tau_ne_zero` (no block weight can vanish, since one would put a
whole block in the radical) → `abstractSchurElement_ne_zero`, plus
`tau_eq_weightedTrace_inv_abstractSchurElement` (`τ = Σ_λ (1/s_λ)χ_λ`, the
identity they are named for) and `abstractSchurElement_indep`.

**The conclusion side of the criterion, derived.** Contrapositively: a candidate
weight system with a zero is realised by **no** splitting. Not the criterion
itself — that is the converse (Tits deformation), and it is stated with Wenzl's
two-parameter `schurElement Q X`, a different object from `s_λ`.

**Splittings are a hypothesis `E`, never produced here** — so nothing depends on
which `q` admit one. Deliberate.

One hypothesis dropped on re-reading:
`tau_eq_weightedTrace_inv_abstractSchurElement` needs no `q ≠ 0`, since
`(c⁻¹)⁻¹ = c` holds in a field unconditionally; only the *interpretation* of
`s_λ` as a Schur element needs the weights nonzero.

PR #6758 is **out of draft** (sixth attempt; the rate-limit error is emitted by
the GraphQL draft step *after* the REST body update succeeds) and
`mergeable_state: clean` even with main 577 commits ahead.

**Option 3, next, in order:** (i) pin `X` — `schurElement Q X` is Wenzl's
*two-parameter* formula and the corpus uses `X ≤ 0` in
`substrate_avoids_tl_locus` while the physical specialisation is `X = Q^{-N}`,
so the statement is not even well posed until that is decided; (ii) prove the
hook-length product equals `abstractSchurElement`; (iii) Tits deformation for
the converse. Expect more gaps of the `xchange` kind — Mathlib has neither
symmetric-algebra theory nor deformation theory.


### 2026-09-05 — option 3 step (i) RESOLVED by measurement: `X = 0`, normalisation `(1−Q)^n`

I flagged pinning `X` as possibly needing an owner ruling. It did not — the
corpus answers it, and reading `WenzlSchurElement.lean` rather than inferring
from the name turned up a **convention clash** I had been about to walk into.

**The clash.** In this corpus `schurElement Q X` feeds
`jonesMarkovCoeff Q X lam = schurElement / wenzlNormalisation`, documented as
the **Jones–Markov coefficient `y_λ`** — i.e. a *weight* of the **Markov**
trace. Geck–Pfeiffer's Schur element is a *reciprocal* weight of the
**canonical** trace (`τ = Σ (1/s_λ) χ_λ`). So the two names denote
reciprocal-flavoured objects **of two different traces**, and "τ's weights are
`1/s_λ`" cannot be read off the names — which is exactly how I had been
stating the remaining fact.

**What pins X.** The content factors `(1 − X·Q^{c(x)})` are precisely what
distinguishes the Markov trace from `τ`; they vanish identically at `X = 0`.
Candidate: `c_λ = (1 − Q)^n · schurElement(Q, 0, λ)`.

**Measured exactly**, [`computations/hecke/tau_weights_vs_wenzl_schur_probe.py`](computations/hecke/tau_weights_vs_wenzl_schur_probe.py)
— sympy symbolic in `Q` throughout, no float anywhere; `probe-float64-guard
--strict` clean:

| tier | what | result |
|---|---|---|
| 1 | `Σ_λ f_λ c_λ = 1` (τ(1)=1), `n = 1…8` | **PASS**, all eight |
| 2 | per-block weights at `n = 2` | **MATCH**, both |
| 2 | per-block weights at `n = 3` | **MATCH**, all three |

Tier 2 is the evidence: it builds the regular representation of `H_n(q)` in the
`T_w` basis **from the corpus's own `σ_mul_Tw` structure constants**, reads the
character table off it, solves `Σ_λ c_λ χ_λ(T_w) = δ_{w,1}`, and compares each
weight. At `n = 3`, e.g. `c_{(2,1)} = Q/(Q²+Q+1)` from both sides.

**Tier 1 is NOT independent evidence and the probe says so in its own output.**
It is implied by the Macdonald hook telescope the corpus already carries, so it
corroborates the *normalisation* and says nothing per-block.

**Scope, stated as a scope-(a) limit.** Tier 2 stops at `n = 3` because the
character table is recoverable from `χ_reg`, `χ_triv`, `χ_sign` alone only up to
`n = 3` (at `n = 4` the dims are 1,3,2,3,1 and that trick no longer isolates
them). So this **pins the statement option 3 must prove; it does not prove it**
for general `n`.

**Option 3 remaining:** (ii) prove `c_λ = (1−Q)^n · schurElement(Q,0,λ)` in Lean
for all `n` — now a precise target rather than an ill-posed one; (iii) Tits
deformation for the converse direction. `SchurElementCriterion` keeps no
instance.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: [M] HeckeSemisimpleGeneral.lean "Bean qou-kwoa" general-n semisimplicity sorry-free; PR #7136 (Geck-Pfeiffer route) becomes optional story | previously stalled; last update 2026-09-05



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.

## 2026-11-20 — W5 (legacy PR triage): the Lean never reached main

This bean is `completed`, but the six Lean files of PR #7136 (TauDualBasis, CasimirBasisIndependence, CasimirBlockScalar, CasimirTransport, CasimirBlockValue, WenzlCandidateNormalisation) were not on main at `917b69399` (`TwDual` occurs nowhere). Ported in PR #8559 (content/→folio/ move only), verified lean-direct against a 142-module -B cone, 46 decls, no sorryAx. Not re-opened: the work is done once #8559 merges.
