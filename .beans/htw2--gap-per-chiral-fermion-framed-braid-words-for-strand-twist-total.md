---
# htw2
title: 'GAP: per-chiral-fermion framed braid words — derive strand-twist totals (not enumerate). Residual of qou-q377 after the total-twist reduction.'
status: open
type: task
priority: normal
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-08-02T00:00:00Z
---

Child of `qou-q377` (hypercharge Y second invariant). PR #4561 /
`claude/hypercharge-twist-derivation-2026-08-02`.

## What was closed (derived, Lean sorry-free)

The candidate `Y = 2(totalTwist/3 − I₃)` is a function of the **total
twist alone**, not the multiset (`TwistDatum.Ycand_factors_totalTwist`);
and reproducing a prescribed `Y` against `I₃` is **equivalent** to
`totalTwist = 3(I₃ + Y/2) = 3Q` (`TwistDatum.totalTwist_pinned_of_Ycand`).
So the SM first-generation spectrum **uniquely pins** each fermion's
total twist: `(u,d,ν,e) = (2,−1,0,−3) = 3Q`. The enumeration battery's
"4 of 10 000 survivors" is `1·2·2·1` — the count of size-3 `{−1,0,1}`
multisets realising each pinned total; the residual is `Y`-invisible
strand-refinement at fixed total, NOT hypercharge non-uniqueness.

## The precise residual (still open)

1. **Per-chiral-fermion framed braid words are missing.** The corpus
   carries no braid word `β_f` (with framing) for `u_L, d_L, ν_L, e_L,
   u_R, …`. Without them, `totalTwist(f)` cannot be *computed* from the
   framework — it is currently *pinned by the SM target* (an inversion,
   i.e. an anchor, not a derivation).
2. **`totalTwist = 3Q` is a consistency requirement, not a derivation.**
   It is `Q_twist = Q` (the falsifiable clause of
   `conj:sm-hypercharge-invariant`). Deriving the individual-fermion
   electric charge `Q(f)` — equivalently the framed braid word — from the
   framework is the actual open object. Note the framework's derived
   `Q = w/2` (Coulomb) is a *hadron-level* result; it does not assign a
   writhe/charge to an individual chiral fermion.
3. **The `1/3` normalisation is the helon (Bilson-Thompson) precedent,
   NOT derived.** `Q_twist = totalTwist/3` is assumed; a framework
   derivation of the colour-tube charge quantum is a sub-gap.

## Why the `1·2·2·1` residual can't be narrowed by hypercharge

The two `d`-survivors `{−1,−1,1}`, `{−1,0,0}` (total −1) and the two
`ν`-survivors `{−1,0,1}`, `{0,0,0}` (total 0) are provably
indistinguishable by `Y` (`TwistDatum.Ycand_factors_totalTwist`; concrete
witness in the same file). The `ℤ₆` condition and bar-negation are also
total-only, so none of them separate the multisets. A separating
constraint must see the **per-strand** assignment — i.e. the braid word
/ colour structure of item 1. That is the whole gap.

## Next honest step

Assign a *framework* framed braid word to each first-generation chiral
fermion (candidate home: the abelian-H, t=0 crossed-module datum +
level-k string extension recorded in the 2026-08-01 uploads-round-2
audit), then COMPUTE its total twist and check `= 3Q` — rather than
inverting the SM spectrum. Until then Y stays enumerated, not derived,
and `conj:sm-hypercharge-invariant` stays open.

## A separating constraint exists, and it is shape-sensitive (2026-08-17)

This bean asks for exactly one thing:

  > "A separating constraint must see the PER-STRAND assignment -- i.e. the
  >  braid word / colour structure of item 1. That is the whole gap."

Component-constancy (bean qou-kebu,
`QOU/StandardModel/ComponentFraming.lean`) is such a constraint. It is
sensitive to the multiset's SHAPE, where Y, the Z6 condition and bar-negation
are all total-only -- so it can see what they provably cannot. Tested against
this bean's own 1.2.2.1 residual, it separates one ambiguous pair and is blind
to the other. Both halves recorded; the negative matters as much as the
positive.

    fermion  total  survivors                 shape(s)          separated?
    u         2     {0,1,1}                   (2,1)             n/a (unique)
    d        -1     {-1,-1,1} / {-1,0,0}      (2,1) / (2,1)     NO  -- blind
    nu        0     {-1,0,1} / {0,0,0}        (1,1,1) / (3)     YES
    e        -3     {-1,-1,-1}                (3)               n/a (unique)

### nu IS separated

`nu_residual_separated_at_swap`: at pi = swap 0 1 the constant framing {0,0,0}
is component-compatible, while NO component framing of that pi is injective. So
{-1,0,1} requires pi = 1 (totally split), and:

    if nu's closure is not totally split, nu = {0,0,0} is FORCED

That is a falsifiable narrowing of the residual this bean calls unnarrowable by
hypercharge -- and it is unnarrowable by hypercharge, correctly; it just is not
unnarrowable in general.

### d is NOT separated -- honest negative

`d_residual_not_separated_at_swap`: both d-survivors have shape (2,1), so at a
pi with orbits {0,1} and {2} BOTH are realisable -- {-1,-1,1} with the doubled
value on the 2-orbit, {-1,0,0} with 0 there. Separating d needs which VALUE sits
on which orbit, which the framing condition alone does not supply. So this
constraint halves the residual (2.2 -> 2.1), it does not close it.

### What this does and does not change

Does NOT change: the totals are still PINNED BY THE SM TARGET, not computed
(item 1 stands). Y stays enumerated, not derived, and
conj:sm-hypercharge-invariant stays open. This adds no braid word.

Does change: the residual is no longer a free choice among enumerated survivors.
Half of it is now a PREDICTION about the braid -- "nu's closure is totally split
iff nu = {-1,0,1}" -- testable the moment the framed braid words of item 1
exist. The next honest step in this bean is unchanged, but its payoff is larger:
those words now decide a recorded question rather than merely being checked
against 3Q.

lean-direct exit 0; #print axioms clean on all eight decls (const_ is
[Quot.sound] only); no sorry / axiom / native_decide.

## ν RESOLVED: the framed braid word, and {-1,0,1} refuted (2026-08-17)

The missing input was in the corpus. `knot-particle-dictionary.md:4`:

  > "Fermions (n odd) are KNOTS (1 component, half-integer spin) ... Quarks are
  >  Borromean-linked unknots in the exceptional divisor."

Leptons close to ONE component; quarks sit in the THREE-component Borromean
braid. Verified on the words themselves (permutation of the braid word):

    sigma1 sigma2          3-cycle    1 component   the unknot
    (sigma1 sigma2)^2      3-cycle    1 component   the trefoil
    (sigma1 sigma2^-1)^3   identity   3 components  Borromean

### The framed braid word for nu

    beta_nu = sigma1 sigma2  in B_3,  framing t = (0,0,0)

Its closure is the unknot -- one component, transitive permutation -- so
component-constancy forces a CONSTANT framing, and the pinned total 3Q(nu) = 0
fixes the common value to 0.

### Lean (all sorry-free, lean-direct exit 0)

    lepton_framing_determined     transitive pi + total 3Q  =>  t == Q
    nu_framing_is_zero            Q = 0  =>  nu = {0,0,0}
    nu_distinct_multiset_excluded a knot closure cannot have an injective
                                  framing  =>  {-1,0,1} is REFUTED
    e_framing_is_neg_one          Q = -1  =>  e = {-1,-1,-1}, derived not enumerated
    u_multiset_available_at_identity  Borromean identity-pi keeps {0,1,1} available

So the residual is 1.2.2.1 -> 1.2.1.1: nu's ambiguity is CLOSED, d's remains
(both d-survivors share shape (2,1); see d_residual_not_separated_at_swap).

### What is now derived vs still anchored -- do not overstate

DERIVED: given the total, the lepton multiset is FORCED, not selected. e's
unique survivor and nu's {0,0,0} both follow from "leptons are knots" plus
component-constancy. The exclusion of {-1,0,1} needs no total at all -- a knot
closure simply cannot carry an injective framing.

STILL ANCHORED: the TOTAL twist is pinned by the SM target (3Q), exactly as htw2
item 1 says. This does not derive Q(f), and conj:sm-hypercharge-invariant stays
open. What changed is that the strand-refinement residual -- the part htw2 shows
hypercharge provably cannot reach -- is now decided for the leptons by framework
structure rather than left to enumeration.

The u/quark side is CONSISTENT rather than derived: identity-pi leaves {0,1,1}
available, and a transitive pi would have KILLED it. That the corpus assigns
quarks to the 3-component Borromean braid is what makes the battery's u-answer
survivable at all -- a nontrivial cross-check that passes.

## d closed -- CONDITIONALLY, and the condition is named (2026-08-17)

`QOU/StandardModel/SignCoherentTwist.lean` -- lean-direct exit 0, no sorry /
axiom / native_decide, #print axioms standard-Mathlib only.

Component-constancy is PROVABLY blind to d (both survivors have shape (2,1)),
so separating d needs a constraint on which VALUE sits where. Exactly one
uniform rule does it:

    SignCoherent t  :=  no strand pair carries twists of opposite sign

Applied to the pinned totals it collapses the residual completely:

    u   2   {0,1,1}                 coherent          1
    d  -1   {-1,-1,1} / {-1,0,0}    NO  / yes         2 -> 1
    nu  0   {-1,0,1}  / {0,0,0}     NO  / yes         2 -> 1
    e  -3   {-1,-1,-1}              coherent          1

    1.2.2.1  ->  1.1.1.1

  no_positive_of_negative_total  coherence + negative total => no positive strand
                                 (this is the whole mechanism: {-1,-1,1} dies
                                 because it carries +1 while its total is -1)
  d_multiset_forced              range + total -1 + coherence => {-1,0,0}
  d_mixed_sign_not_coherent      the excluded survivor, named
  {d,u,e,nu}_survivor_coherent   the rule destroys NOTHING else -- uniformity

### Status: ASSUMPTION, not derivation -- do not launder this

SignCoherent is the HELON-MODEL structure (Bilson-Thompson, already cited in the
corpus for the 1/3 normalisation): a fermion's helons carry twists of a single
sign. A corpus grep finds NO framework statement of it. Its physical reading --
that a state carrying +1 and -1 on different strands contains an internal
bar-conjugate pair, since bar negates the twist -- is suggestive, not a proof.

So d = {-1,0,0} is CONDITIONAL on adopting sign-coherence. Under the anti-fit
discipline that import must be named, and it is, in the file's own docstring and
here. It is not wired to anything.

### The corroboration, and why it is only that

Sign-coherence independently forces nu = {0,0,0} -- the SAME answer
ComponentFraming.nu_framing_is_zero DERIVES from "leptons are knots". The two
routes are epistemically different (derived vs imported) and agree where they
overlap. That is evidence the convention is the right one; it is NOT a
derivation of it. d is where only the assumed route reaches, which is precisely
why d stays labelled conditional while nu does not.

### What would upgrade it

Deriving sign-coherence from the framework -- most plausibly from the bar
involution (bar negates the twist, so a mixed-sign state is bar-composite) plus
whatever forbids a fundamental fermion from carrying an internal conjugate pair.
That is a real, well-posed target and it is NOT done here.

## UPGRADE: sign-coherence is a NORMAL FORM, not an import (2026-08-17)

The section above labelled sign-coherence a Bilson-Thompson convention and said
the well-posed upgrade was deriving it. A sibling branch
(claude/agent-discussions-queue-gibk4e, bean qou-pkf3, commit 97d45b51ca) landed
the missing half hours later:

  > "On the defining representation the twist axiom forces theta_V = q^{1/2} . id_V"
  > "Without a twist a braid closure is only a FRAMED link"

Because theta_V is a SCALAR multiple of the identity, opposite framings on two
strands cancel EXACTLY, as morphisms:

    theta_V (x) theta_V^{-1} = q^{1/2} . q^{-1/2} . id = id

So a (+1,-1) strand pair is RIBBON-INVISIBLE. Cancelling it rewrites the same
state; it is not a different physical choice. And cancellation preserves the
total (cancel_preserves_total), hence preserves Q_twist = T/3, Y, and the Z6
layer -- so reduction is invisible to every constraint the battery imposes.

Reducing until no such pair remains lands in a sign-coherent framing, and for
entries in {-1,0,1} the reduced form is UNIQUE per total (verified over all 27
assignments; reduction preserves the total in every case):

    total  -3         -2        -1       0       1       2       3
    form   {-1,-1,-1} {-1,-1,0} {-1,0,0} {0,0,0} {0,0,1} {0,1,1} {1,1,1}

The two survivors sign-coherence excluded are exactly the UN-REDUCED SPELLINGS
of the two it keeps:

    d  {-1,-1,1} -> {-1,0,0}
    nu {-1,0,1}  -> {0,0,0}

### Lean

  coherent_iff_all_same_sign  coherent <-> all non-negative or all non-positive
  d_forms_same_weight         the excluded and kept d forms carry the SAME
                              ribbon weight theta^total -- the choice between
                              them is a choice of representative
  nu_forms_same_weight        same for nu
  cancel_preserves_total      the reduction step leaves the total fixed

lean-direct exit 0; #print axioms [propext] / [propext, Quot.sound]; no sorry /
axiom / native_decide.

### Status change, precisely

WAS: d = {-1,0,0} conditional on an imported helon convention.
NOW: d = {-1,0,0} follows from theta_V being scalar -- categorical structure of
the corpus -- plus the interpretive step that the physical state is the
ribbon-equivalence class rather than a chosen spelling.

The remaining caveat is that second step, and it is stated rather than buried.
It is much weaker than the original import: it is a statement about what counts
as the same state, not a borrowed rule about helon signs.

Cross-check unchanged and now better motivated: sign-coherence forces
nu = {0,0,0}, the same answer ComponentFraming.nu_framing_is_zero DERIVES from
"leptons are knots". Two routes, agreeing.
