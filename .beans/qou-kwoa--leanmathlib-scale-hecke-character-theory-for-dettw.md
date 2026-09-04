---
# qou-kwoa
title: 'Lean/Mathlib-scale: Hecke character theory for det(twGram) at rank >= 2 (Geck-Pfeiffer 7.2.6)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-02T21:39:20Z
updated_at: 2026-09-04T09:02:28Z
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
