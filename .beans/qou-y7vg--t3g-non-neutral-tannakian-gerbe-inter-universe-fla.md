---
# qou-y7vg
title: 'T3g: non-neutral Tannakian / gerbe -- inter-universe flavour'
status: todo
type: task
priority: normal
created_at: 2026-08-04T00:07:01Z
updated_at: 2026-08-26T15:18:09Z
parent: qou-8lxd
---

Formal home for 'flavour SU(3) is an inter-universe phenomenon'. Deligne: a Tannakian category with no fibre functor over the base but one over an extension reconstructs a GERBE with a band (lien), i.e. a groupoid scheme, not a group. Test: does QOU's category admit inequivalent fibre functors (is H^1(base, Aut^otimes) nontrivial)? WARNING: naive 'permute 3 fibres' FAILS the Sym^2 gate -- permutation representations are self-dual. It yields S_3 = W(A_2), the Weyl group / hexagon symmetry, not the fundamental.


---

## LIVE SURFACE COLLAPSED (2026-08-07) — see the synthesis audit

`docs/audits/2026-08-07-eightfold-live-surface-collapse.md`.

Three independent threads now terminate on the **same** requirement:
* the Sym^2-gate result — no **odd-dimensional** summand of any
  `V^{tensor n}` passes (Frobenius–Schur parity: odd-dim SU(2) irreps are
  orthogonal, so their singlet lands in `Sym^2`), so "inequivalent fibre
  objects" must mean genuinely non-isomorphic fibres. *Corrected 2026-08-07:
  self-duality alone does NOT decide the gate — even-dimensional summands are
  symplectic and do pass it, they are just the wrong dimension;*
* the Ocneanu result — an N = 3 channel must be the categorical trace on a
  genuinely 3-dimensional object, since the parameter is the fibre's quantum
  dimension;
* T3g's own question — does the braided category admit inequivalent fibre
  *functors* (a non-neutral Tannakian gerbe)?

**`qou-8p1i` (T3b) and `qou-y7vg` (T3g) are the same question.** Merge their
scope.

**And T3g's stand-down is VOID.** It deferred to the S₄/Fano route ("the Fano/S₄
route subsumes the structural content of this bean") — and that route was
excluded today, scope-(b). T3g is now the *surviving* direction, not the
subsumed one, and should be re-prioritised.


---

## THE CORPUS ALREADY ASSERTS AN ANSWER — as an unproved remark (2026-08-07)

`rem:fivefold-affine-charts-generations`
(`brings-surface/fivefold-affine-charts-generations.md`) states, verbatim:

> "Each fibre functor `tau : C -> Vect` serves as an **affine chart**. The
> `S_5` symmetry acts directly on **the space of these affine charts**. The
> five sheets of Bring's surface correspond to **five classes of affine
> charts**. ... There are **five topologically distinct embeddings of a fibre
> functor**. Three sheets carry the matter families (`T_{2,3}, T_{2,5},
> T_{2,7}`), while the remaining two carry the force mediators (`T_{2,9},
> T_{3,5}`). ... Transition functions between distinct sheets invoke **5-fold
> monodromy**."

So T3g's existence question — *does QOU's braided category admit inequivalent
fibre functors?* — is **already answered affirmatively in the corpus**, with a
specific count (five) and a specific `S_5` action. "Transition functions
between distinct sheets" is literally cocycle/gerbe language.

### But check the status before building on it

The block is a **`remark`**, `interprets: def:quantum-universe`, **no `.lean`
sibling, no proof, no witness**. Per AGENTS.md §3a a remark carries "physical
interpretation, motivation, or examples — **not new mathematical claims**". So
this is **asserted, not established**. It cannot be cited as settling T3g.

### Two things this changes

1. **The count is FIVE, and its 3 is the wrong 3.** Three of the five sheets
   carry *matter families* — i.e. **generations**, not colour or flavour. Even
   granting the remark in full, it delivers a 5-fold structure with a 3+2 split,
   not an `SU(3)`.
2. **T3g may have analysed the wrong extension degree.** T3g §5 rules out the
   *degree-3* extension route on the grounds that `Out(SU(3)) = Z/2`, not `Z/3`
   — it assumed three fibres because `SU(3)` wants a 3. But the corpus's actual
   multi-fibre structure is **five-fold with `S_5`**. **Nobody has analysed the
   degree-5 / `S_5` case.** T3g's obstruction does not obviously transfer:
   `S_5` has plenty of subgroups and quotients, and the relevant question is
   which band an `S_5`-glued gerbe can carry, not a `Z/3` one.

### Adversarial note, recorded so it is not skipped

The remark's supporting language — 5-fold monodromy, "globally aperiodic
structure similar to a quasicrystal", Penrose-tiling analogy — is evocative and
entirely unformalised, and the assignment of specific torus knots
`T_{2,3}/T_{2,5}/T_{2,7}` to the three generations has the shape of a pattern
match rather than a derivation. Establishing the remark is a real research task,
not a citation.

### Concrete next step

Before any gerbe construction: **promote or refute the existence claim.** Is
"five topologically distinct embeddings of a fibre functor" a theorem, or a
picture? That is prior to asking what band the gerbe has, and it is the honest
first move on the merged `qou-8p1i`/`qou-y7vg` scope.


## T3g EXISTENCE CLAIM CHECKED 2026-08-26 (PR #5819) -- IT DOES NOT SUPPLY THE PREMISE

This bean's next step was 'promote or refute' rem:fivefold-affine-charts-generations,
the block that supposedly already answers T3g's existence question. Checked.
Verdict SCOPE-(a): the remark as written does not establish what T3g needs. NOT a
claim that inequivalent fibre functors fail to exist -- that is untouched.

Audit: docs/audits/2026-08-26-fivefold-charts-does-not-supply-t3g.md

GAP 1 -- TARGET CATEGORY CONTRADICTS THE DEFINITION IT INTERPRETS. Literal, not
interpretive. def:quantum-universe item 3 reads 'an R-linear faithful fibre
functor tau : C -> R-Mod', and the same block says R is a commutative ring NOT a
field (R_q = Z[q,q^-1]). The remark opens 'Each fibre functor tau : C -> Vect',
and its manifest declares interprets: def:quantum-universe. Vect vs R-Mod.
This is load-bearing: fibre functors to Vect_k over a FIELD are classified by
Galois H^1(k, Aut^ot); fibre functors to R-Mod over Z[q,q^-1] are a question
about Spec R, i.e. a Tannakian gerbe over a BASE SCHEME with H^1 in fppf/etale.
Deligne's theorem is relative to a base. UNTIL THE BASE IS NAMED THE QUESTION HAS
NO DETERMINATE ANSWER TO PROMOTE OR REFUTE.

GAP 2 -- EMBEDDINGS ARE NOT ISOMORPHISM CLASSES. T3g needs tau_1 !~ tau_2. The
remark supplies 'five topologically distinct EMBEDDINGS of A fibre functor' --
singular, and an embedding is a placement, not a functor. Five placements of one
functor are consistent with exactly ONE isomorphism class. da-arity-conflation.

GAP 3 -- A TRANSITIVE ORBIT IS WHAT ONE CLASS LOOKS LIKE. S_5 acting on five
sheets is the ordinary picture of one object with an index-5 stabiliser. Whether
an S_5 element moves the ISOMORPHISM CLASS of tau is the unproved step, and it is
the step that decides neutrality. Genuinely open in both directions --
precomposition with a tensor-autoequivalence CAN move the class -- but the remark
does not address it, and the orbit reads as evidence when it is neutral.

WHAT WOULD SETTLE IT (so the next attempt is not another reading of this remark):
  1. NAME THE BASE. Spec R with R = Z[q,q^-1], or a specialisation to a field.
     Neutrality is not a property of C alone. Cheap, and prerequisite for 2-3.
  2. Identify Aut^ot(tau) as a group scheme over that base.
  3. Compute or bound H^1 of the base in the relevant topology.

TWO FACTS MAKING THIS SAFE: (a) NOTHING CITES THE BLOCK -- corpus-wide grep over
content/, docs/ and .beans/ finds no consumer besides the beans discussing it, so
scoping it breaks no downstream argument. (b) Its numbers do not match T3g's
target anyway: three of five sheets carry GENERATIONS, a 5-fold 3+2 split, not an
SU(3) -- this bean already recorded that.

DELIBERATELY NOT DONE: the remark is NOT rewritten. The Vect/R-Mod mismatch could
be a typo or could mean an intended implicit base change to a field, and those
need different repairs; correcting it either way changes a mathematical claim and
belongs with the author. And NO LEAN -- the finding is that two prose claims
differ from each other and from what a third needs; there is no invariant to
prove, and a toy formalisation would be a trivial-true dressing up a reading.


## STEP 1 (NAME THE BASE) WORKED 2026-08-26 -- IT IS A DECISION, NOT A LOOKUP

Audit: docs/audits/2026-08-26-t3g-step1-name-the-base.md

Expected a lookup. The corpus offers THREE candidate bases, two sharing a
symbol, and designates none:

  1. Spec R, R = Z[q,q^-1] -- def:quantum-universe's ground ring, the one
     tau : C -> R-Mod is literally linear over. Strongest claim by construction.
  2. Spec(R_q), R_q = the COORDINATE RING OF BRING'S CURVE --
     def:categorical-mordell-weil. SAME SYMBOL AS (1), DIFFERENT RING:
     Z[q,q^-1] is the coordinate ring of G_m/Z (affine, genus 0); Bring's curve
     is genus 4. R_q appears NOWHERE in the notation register, so nothing
     adjudicates the collision.
  3. Spec(xi_q), the Reeb-eigenvalue SPECTRAL BASE.

THE FIND THAT MATTERS -- THIS BEAN IS MISSING A CARRIER. def:categorical-mordell-weil
states, verbatim:

    'The fibre functor atlas of the QOU forms a G-gerbe over the spectral base.'

That is T3g's own claim, in T3g's own vocabulary, and THIS BEAN DOES NOT CITE
IT. This bean records the fivefold remark as the corpus's only assertion, and
#5744's audit measured the external shelf as empty (one Tannakian hit in
library/, zero on gerbes). Both readings missed this block.

It is a STRONGER carrier than the fivefold remark: a `definition` with a .lean
sibling, not a `remark`. Two caveats keep it from settling anything: the Lean is
registered validation: "not_checked", and the gerbe is used as SETTING inside a
Mordell-Weil / L-function block, not proved as a RESULT. Read it before any
further T3g work.

A FOURTH OBJECT, and the hazard. The same block defines H^1_ot(C, E_q) as 'the
first cohomology of the monoidal category (classifying torsors under E_q in C)'
-- a CATEGORICAL H^1, of C itself, under an OBJECT. T3g's question is
H^1(base, Aut^ot(tau)) -- cohomology of a BASE, classifying FIBRE FUNCTORS.
Different groups, different questions, both written H^1. Say which one, over
which base, in which topology. This is the da-arity-conflation shape and the arc
has now hit it three times.

STATUS: step 1 NOT completed as a lookup; CONVERTED into a decision. The
question 'is H^1(base, Aut^ot) nontrivial?' still cannot be posed -- and now for
a sharper reason: not that nobody wrote the base down, but that the corpus
contains three and reconciles none. Steps 2 and 3 have no determinate target
until the owner answers:

  (a) which ring is R_q -- Z[q,q^-1], or Bring's coordinate ring? Register the
      survivor, rename the other.
  (b) is T3g's base Spec R or the spectral base Spec(xi_q)? Different cohomology,
      different topologies, different answers.

DELIBERATELY NOT DONE: no symbol renamed, no base designated. Both are changes
to mathematical claims across chapters that already depend on them, and the R_q
collision may be a naming slip in one place or a genuine identification the
author intends. Agents should not pick.


## CORRECTION 2026-08-26 -- CARRIER 3 HAS NO FORMAL CONTENT. I SAID OTHERWISE AN HOUR AGO.

Audit: docs/audits/2026-08-26-t3g-carrier3-has-no-formal-content.md

The step-1 entry above called def:categorical-mordell-weil 'a STRONGER carrier
than the fivefold remark: a definition with a .lean sibling, not a remark'. WRONG,
and wrong in the direction that flatters the finding. I read the manifest (kind:
definition, lean.ref present) and inferred formal content from the SHAPE OF THE
METADATA without opening the file. The entire sibling is:

    def CategoricalMordellWeil   :=
      -- Ref: [manuscript] def:categorical-mordell-weil
      trivial

trivial : True, so the inferred type IS True. That is def-disguised-true, the
pattern AGENTS.md 1a names as a forbidden audit-dodge. A .lean sibling whose body
is `trivial` is WEAKER than none -- it reads as formalised.

BOTH CANDIDATE CARRIERS FOR T3G'S PREMISE ARE PROSE. The fivefold block is a
remark with no Lean; this one is a definition whose Lean is a tautology.

THREE-PART DEFECT in that block (someone else's chapter -- repair belongs to its
owner, not drive-by):
  1. sibling is a disguised True, as above;
  2. its header says 'The compiled formalisation lives under QOU/AppendixSurreals/'
     -- that directory has ~200 files and NONE declares CategoricalMordellWeil;
  3. lean.ref says qou:QOU.AppendixSurreals.CategoricalMordellWeil, but the REAL
     decl is QOU.CategoricalMordellWeil at QOU/QBirchSwinnertonDyer.lean:65
     (def CategoricalMordellWeil (E : C) : Type v := (1_C) --> E, plus
     theorem descartes_rank_zero). Sibling-first resolution means the stub SHADOWS
     it -- the 0a 'no shadowing stubs' case. Repair is NOT 'delete the sibling':
     a definition block requires one at type level. Either give the sibling real
     content or re-point the ref. Author's call.

AND THE REAL DECL HAS NO GERBE CONTENT: QBirchSwinnertonDyer defines Hom(1, E)
and proves descartes_rank_zero. Grepping it for gerbe/atlas/spectral base returns
ONE hit, the phrase 'fibre functor' in a docstring about chord-tangent addition.
So 'The fibre functor atlas of the QOU forms a G-gerbe over the spectral base'
has NO formal backing anywhere.

DETECTOR BLIND SPOT, MEASURED NOT INFERRED. Ran the vacuity audit: 3193 .lean
scanned, 134 candidates across 154 files, and categorical-mordell-weil.lean is
NOT among them -- while proof-no-trivial-true fires on other files in the same
run (e.g. e-hartree-categorical-derivation.lean:103). The criterion is live and
does not see this decl. Likely cause: the test keys on the DECLARED CONCLUSION
and `def X := trivial` has no type ascription, so there is no True written down
to match. The cause is an inference; the blindness is the measurement. Candidate
14th entry for the detector-blindness taxonomy.

NOT FIXED, deliberately: widening the criterion touches a checker over 3193 files
and `trivial` is a legitimate body in contexts this would newly flag. Needs a
measured false-positive count and a selftest first -- its own piece of work.

FOR T3G: carrier 3 joins carrier 1 as an assertion in prose. This bean SHOULD
cite it -- it is still the closest thing in the corpus to T3g's own claim and it
names the spectral base -- but it cannot be promoted and nothing should be built
on it as established. The base question is unchanged and still needs the author.


## OWNER DECISION 2026-08-26 -- BASE RING FIXED

    R = Z[q, q^-1][ Phi_d(q)^-1 : d >= 2 ]

(option 2). Spec R is the q-line with the roots of unity of order >= 2 deleted --
exactly the locus axiom 4 forbids.

AND THE DEFINITION SHOULD NOT NAME IT. Owner's second point: neighbouring
communities work over a RELATED but different base (Q(q) for generic-q rep
theory, Lusztig's Z[v,v^-1] with q = v^2, a real or complex algebra past the
wall). A definition hard-wired to one ring silently excludes all of them.

HANDLED BY STATING THE PROPERTY, NOT THE RING.
QOU/AlgebraicSubstrate/QGenericBase.lean (5 decls, sorry-free, lean-direct
exit 0, axioms [propext, Classical.choice, Quot.sound]):

  class IsQGeneric R q     q is a unit, and so is Phi_d(q) for every d >= 2
  qBracket                 [n]_q = prod_{d | n, d >= 2} Phi_d(q)
  isUnit_qBracket          EVERY bracket is a unit -- what axiom 4 needs. The
                           proof is trivial BY CONSTRUCTION because the bracket
                           is literally a product of the inverted elements;
                           that is the argument for the cyclotomic generating
                           set over the bracket one.
  qPow_sub_one_eq_mul_bracket   q^n - 1 = (q-1)*[n]_q, the exact boundary of the
                           d >= 2 choice
  IsQGeneric.map           THE PROPERTY TRANSPORTS ALONG ANY RING HOM
  isQGeneric_real          every real q > 1 is q-generic, substrate q0 included

R is the INITIAL object for the property (universal property of localisation,
applied twice), so every related community ring is DOWNSTREAM of it rather than
in competition. IsQGeneric.map is the working half: a definition stated over the
class is automatically available in every specialisation without restatement.

WHY d >= 2 IS RIGHT, NOT MERELY SUFFICIENT. Phi_1(q) = q - 1, so inverting from
d = 1 would DELETE q = 1 from Spec R -- and the corpus uses that point (the q=1
classical shadow, J_Hopf(1) = -2). Nothing forces it: hbar_q = 1 - q^-1 =
(q-1)/q is the one construct needing Phi_1, and MEASURED, every division by it
is past the archimedean wall in R, where q0 - 1 ~ 0.11 is invertible anyway.
qPow_sub_one_eq_mul_bracket makes the boundary exact: q^n - 1 is a unit IFF q-1
is. So d >= 2 buys every quantum dimension AND keeps q = 1 alive.

NON-VACUITY WHERE IT MATTERS: isQGeneric_real is not a toy witness -- the class
is satisfied at the value the framework actually evaluates at. Mutation-tested:
removing [IsQGeneric R q] from isUnit_qBracket fails to synthesize, so the
hypothesis is load-bearing.


## THE v SIGN: CAN THE AXIOMS PICK IT? NO -- AND IT IS PROVABLE (2026-08-26)

Owner asked whether the QOU axioms, particularly the NON-SYMMETRY of the
braiding, can fix the sign of v = q^(1/2), the way axiom 1 gives time a
direction. Answer: no, and the obstruction is structural rather than a gap.

QOU/AlgebraicSubstrate/TwistSignTorsor.lean (4 decls; three depend on NO AXIOMS
AT ALL, the fourth on propext only; mutation-tested).

A SIGN FLIP IS NOT A FREE CHOICE. Replacing theta by theta' X = eps X * theta X
preserves the ribbon axiom theta(V ot W) = (theta V ot theta W) . c . c IFF
eps(V ot W) = eps V * eps W. So eps is a Z/2-valued MONOIDAL CHARACTER, and the
ribbon structures over one braiding form a TORSOR under the group of such
characters. Consequences:
  sign_trivial_on_unit      eps 1 = 1
  sign_trivial_on_squares   eps (x*x) = 1 -- THE FLIP IS INVISIBLE ON SQUARES,
                            which is exactly why the braiding fixes q = v^2 and
                            not v, and refutes 'just negate v everywhere'
  no_constant_nonunit_sign  a constant sign /= 1 is not a homomorphism

SO THE SIGN IS FREE EXACTLY WHEN THE CATEGORY HAS A NON-TRIVIAL Z/2 GRADING.
Trivial grading => sign already determined. That the choice exists at all is the
SAME FACT as there being a fermion parity.

WHY NON-SYMMETRY CANNOT DO IT. eps acts on the TWIST and leaves the braiding
alone, so checking all four axioms:
  1 temporal braiding  reads only the order on c            -- untouched
  2 Frobenius-Hopf     no twist appears                     -- untouched
  3 symmetric Frobenius left and right traces BOTH scale by eps X, so their
                        EQUALITY survives                   -- invariant
  4 Wedderburn          each datum scales by a unit and invertibility is
                        sign-blind (isUnit_unit_mul_iff)    -- invariant
ALL FOUR ARE eps-INVARIANT. Scope-(b), invariant named.

THE DISANALOGY WITH TIME IS THE POINT. Axiom 1 extracts a direction from an
ORDER, and well-foundedness is not preserved under reversal -- the asymmetry
lives in the SAME datum the axiom constrains. The sign lives in a DIFFERENT
datum: a braided category has many ribbon structures, and the braiding fixes the
monodromy q = v^2, never v. Non-symmetry is the WRONG INVARIANT, not an
unexploited one.

WHAT WOULD FIX IT: an ORDER on the base. Demanding dim_q(lambda) > 0 (unitarity)
selects the sign, since eps(lambda) = -1 on odd-graded blocks makes one branch
negative. That needs R ordered, hence archimedean, hence not categorical -- which
is precisely why rem:sign-as-spin-structure says 'POST-ARCHIMEDEAN, this binary
sign determines the spin structure'. The qualifier was already right; this
explains why it is FORCED.

NOT FORMALISED: the ribbon-axiom computation itself. Mathlib carries Braided but
no ribbon categories, so the file formalises the torsor group theory and the
sign-blindness of invertibility, and argues the categorical step in prose.

## ANSWERED 2026-09-03 (PR #6458, bean qou-yjwg) — yes, inequivalent fibre functors exist; they cannot carry flavour

"Does QOU's braided category admit inequivalent fibre functors?" — YES, by
Bichon 2003: on Rep(SL_q(2)) there is a fibre functor of every dimension n >= 2,
real at q0. But a fibre functor preserves fusion rules, so under a 3-dim one
V^{x3} = 21 + 3 + 3 and never contains the singlet the eightfold 10+8+8+1
needs (Lean-proved, FibreFunctorDimensionNotCategorical.lean). The "non-neutral
gerbe" framing was symmetric-theory (already retracted 2026-08-25); the
non-symmetric answer is that the fibre functor is the wrong knob. Audit:
docs/audits/2026-09-03-fibre-functors-do-not-change-the-category.md. Status
left for the author; recommendation: close as answered-negative, successor is
the axiom-5 question in the audit's §4.
