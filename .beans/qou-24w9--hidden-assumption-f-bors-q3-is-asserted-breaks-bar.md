---
# qou-24w9
title: 'HIDDEN ASSUMPTION: F_Bor''s /q^3 is asserted, breaks bar-symmetry, and carries 37% of m_p'
status: todo
type: task
created_at: 2026-08-18T20:45:53Z
updated_at: 2026-08-18T20:45:53Z
---


## Measured 2026-08-18 (owner asked: is there a hidden assumption in /q^3?)

Yes. Five findings, one of which RETRACTS my own earlier claim.

### 1. It is ASSERTED, not derived

`m_p_substrate_identity_50dps.py:175-177`:

    def F_Bor(q):
        """The natural categorical observable F_Bor(q) := |tr_M(b_Bor,q)| . [3]_q! / q^3."""
        return trM_borromean(q) * qfact_three(q) / q ** 3

A `:=` and the word "natural". `|tr_M|` is Lean-proved (BorromeanMarkovTrace)
and `[3]_q!` is a closed form, but the exponent 3 has no derivation trail.

### 2. The existing justification is INVERTED

`docs/audits/2026-06-24-fbor-q3-exact-habiro-ratio-fit.md` calls /q^3 "the exact
q-factorial BALANCING (NOT a fit)". Its algebra is right and its meaning is
backwards. With the balanced q-integer this file actually uses
(`q_int(q,n) = (q^n - q^-n)/(q - q^-1)`):

    [3]_q!        = q^3 + 2q + 2q^-1 + q^-3      bar-symmetric: TRUE
    [3]_q! / q^3  = 1 + 2q^-2 + 2q^-4 + q^-6     bar-symmetric: FALSE

(the second line reproduces the audit's expansion exactly). So `[3]_q!` was
ALREADY balanced, and dividing by q^3 BREAKS the bar-symmetry. /q^3 is not a
balancing; it is an un-balancing.

That matters because bar-symmetry is the symmetry a Markov-trace/ribbon object
is expected to carry -- so the normalisation is fighting the structure, not
implementing it.

### 3. It is load-bearing at 37 %

    F_Bor = |tr_M| . [3]_q! / q^3   ->  m_p = 938.272089427    (-2.9e-10 % vs CODATA)
    F_Bor = |tr_M| . [3]_q!         ->  m_p = 1285.38954269    (+37.00 %)

Removing it does not perturb m_p, it destroys it. A factor worth 37 % justified
by the word "natural" is exactly a hidden assumption.

### 4. Nothing available can currently fix the exponent

  - CLASSICAL LIMIT IS BLIND. [3]_q! -> 6 and [3]_q!/q^3 -> 6 as q -> 1; the
    ratio q^3 -> 1. Any q^a is invisible at q=1, so the classical boundary
    cannot determine a.
  - THE WRITHE CANNOT SOURCE IT. The Borromean word (s1 s2^-1)^3 has writhe 0,
    so no q^writhe factor arises.
  - THE PER-STRAND READING IS UNFALSIFIABLE HERE. "q^-3 = q^-n at n=3" fits by
    construction: q^3 occurs exactly ONCE in the file (line 177), there is no
    qfact_two/qfact_four and no second F-observable at a different strand count.
    With one instance, any exponent can be rationalised as some f(3).

### 5. RETRACTION of my own qou-gzs0 Q2 claim

I recorded that "q^-3 = q^{T/2} at T = -6 EXACTLY -- framing shape, not
q^writhe". The exactness is VACUOUS: -3 = -6/2 is arithmetic, and EVERY integer
power q^a equals q^{(2a)/2}. So "has framing shape" is satisfied by any q-power
and is not evidence of anything. The observation carried no content and I
presented it as a structural identification. Retracted; the qou-gzs0 Q1 result
(the 5.36 % ladder is ~4e4 too coarse for the L2 gaps) is unaffected and stands.

### The well-posed derivation target

Derive the exponent from the MARKOV TRACE NORMALISATION for an n-strand closure
(standard HOMFLY/Jones normalisation carries an (n-1)-power factor and a
writhe-power; the writhe half is 0 here, so any q-power must come from the
strand/trace half). Then CHECK IT AGAINST A SECOND KNOT AT A DIFFERENT STRAND
COUNT -- that second instance is what makes the rule falsifiable, and the corpus
does not currently have one.

Until then /q^3 should be labelled a normalisation CONVENTION carrying 37 % of
m_p, not "the natural categorical observable".

## Tried to prove it: the exponent IS canonical, but it is applied TWICE (2026-08-18)

`QOU/MassTheory/PoincareCenteringOfQ3.lean` -- lean-direct exit 0, four
theorems, #print axioms standard-Mathlib only, no sorry / axiom / native_decide.

### The candidate derivation, and it half-works

The UNBALANCED [n]_q! is the Poincare polynomial of S_n,

    [n]_q!^unbal = SUM_{w in S_n} q^{l(w)},   deg = l(w_0) = n(n-1)/2

so q^{-l(w_0)} is its canonical CENTERING. Converting to the balanced
convention carries exactly that factor -- verified symbolically n = 1..6:

    [n]_q!^bal  =  q^{-n(n-1)/2} . [n]_{q^2}!^unbal

At n = 3 that is q^{-3}: the exponent in question. So it is NOT arbitrary --
3 = l(w_0), the length of the longest element of S_3, which is a canonical
Hecke-theoretic quantity.

### But the code already uses balanced integers, so /q^3 centers a SECOND time

`m_p_substrate_identity_50dps.q_int` is (q^n - q^-n)/(q - q^-1) -- BALANCED. So
`qfact_three` is already the once-centered object and F_Bor divides again:

    balanced_is_already_centered   [3]_q!^bal      = P(q) / q^3
    code_form_is_doubly_centered   [3]_q!^bal/q^3  = P(q) / q^6

with P(q) = 1 + 2q^2 + 2q^4 + q^6 the Poincare polynomial of S_3 in q^2. The
code's object sits at q^{-2 l(w_0)} -- twice the canonical centering.

That is also exactly WHY the bar-symmetry breaks: `balanced_is_bar_symmetric`
shows the once-centered form IS invariant under q -> q^-1, and the second
division destroys it. The two findings are the same fact seen twice.

### Why one instance cannot settle it

`ell_w0_eq_n_iff_three` : n(n-1) = 2n  <->  n = 0 or n = 3.

l(w_0) coincides with n EXACTLY at n = 3. So the corpus's single 3-strand
observable cannot distinguish "center by l(w_0)" from "one power per strand" --
they agree there and nowhere else. A 2- or 4-strand F-observable would decide
it; none exists.

### VERDICT: identified, not derived

I did not prove the /q^3. What I proved is what it IS: a second Poincare
centering, applied on top of the one already inside the balanced convention, and
that second application is the step that breaks bar-symmetry. No standard
convention calls for it.

The numerics still require it (dropping it moves m_p to +37.0 %), so the open
question is sharpened rather than closed: what derives a DOUBLE centering? Until
that is answered, /q^3 remains a normalisation convention carrying 37 % of m_p.

Scope (a). Does not refute F_Bor and does not touch the Lean-proved
|tr_M(beta_Bor)|.

## Second derivation attempt: the corpus's OWN rule predicts no q-power (2026-08-18)

### What "double centering" means, stated exactly

P(q) = 1 + 2q^2 + 2q^4 + q^6 is the Poincare polynomial of S_3 in q^2,
SUM_w q^{2 l(w)} -- one-sided, degrees 0..6, palindromic. Centering means
multiplying by q^{-l(w_0)} = q^-3 to spread it symmetrically about q^0:

    P(q)  --/q^3-->  q^-3 + 2q^-1 + 2q + q^3   = [3]_q!^bal   SYMMETRIC
          --/q^3-->  1 + 2q^-2 + 2q^-4 + q^-6  = the code's factor

The second division overshoots the symmetric point by exactly the amount that
reached it, landing one-sided again on the negative side. Sharpest form
(verified symbolically, residual 0):

    [3]_q!^bal / q^3  =  P(1/q)

i.e. the code's normalisation is the BAR-CONJUGATE of the Poincare polynomial.
That is what "double centering" means: raw -> symmetric -> bar-conjugate.

### What the sanctioned normalisations give -- all of them say "no q-power"

beta_Bor = (sigma_1^-1 sigma_2)^3 (borromean-markov-trace-closed-form.md:2):
6 crossings, 3 negative + 3 positive, so **writhe e(beta) = 0**.

  - CORPUS RULE. markov-axioms-primitive.md:13 states link invariance "is
    restored by the WRITHE PREFACTOR OUTSIDE THE TRACE". Any writhe prefactor at
    e = 0 is 1. So the corpus's own Markov axioms predict NO q-power for
    beta_Bor.
  - JONES/TL. V = (-A^3)^{-w} <L>/delta; at w = 0 the framing factor is 1.
  - HOMFLY (Jones 1987). prefactor ((1-lambda q)/(sqrt(lambda)(1-q)))^{n-1} .
    sqrt(lambda)^{e(beta)}: the framing half dies at e = 0, and the (n-1) half is
    a delta-factor (delta = [2]_q = q + q^-1), NOT a pure q-power.

None yields q^-3. The one rule the corpus itself sanctions gives exactly 1.

CAVEAT ON SOURCES: the paper-search MCP was disconnected, so the Jones/HOMFLY
statements are standard-reference knowledge plus in-repo text, NOT a fresh
literature fetch. The CORPUS-internal half (markov-axioms-primitive.md, the
braid word) is directly cited and is the load-bearing part.

### Verdict: derivation FAILED, and now for a reason

Attempt 1 (Poincare centering) identified the exponent as l(w_0) but showed it
is applied twice. Attempt 2 shows the corpus's own normalisation rule -- writhe
prefactor -- gives 1 for this braid, because its writhe is 0.

So /q^3 is not merely unjustified; it CONFLICTS with the normalisation rule the
corpus states, on the corpus's own braid word. That is a stronger negative than
"no derivation trail".

UNTESTED CANDIDATE, recorded not claimed: q^-3 = q^{-l(w_0)} is also
q^{-writhe(Delta)} for the Garside half-twist Delta of B_3 (3 crossings). If the
intended normalisation were "divide by the Garside element's writhe" rather than
the braid's own, that would produce 3. beta_Bor is not Delta and the corpus
states the rule in terms of the braid's writhe, so this is a guess at intent,
not a derivation.

## Both attempts now Lean-proved (2026-08-19)

Added to `QOU/MassTheory/PoincareCenteringOfQ3.lean` -- lean-direct exit 0,
#print axioms standard-Mathlib on all eight decls, no sorry / axiom /
native_decide.

### Attempt 1 (double centering), sharpest form

    code_form_eq_poincare_bar :  [3]_q!^bal / q^3  =  P(q^-1)

P is palindromic, so one centering reaches the symmetric point and the second
overshoots it by the same amount, landing on P at the INVERSE variable. That is
what "double centering" means, now as a theorem rather than a computation.

Together with the existing three:
    balanced_is_already_centered   [3]_q!^bal      = P(q)/q^3
    code_form_is_doubly_centered   [3]_q!^bal/q^3  = P(q)/q^6
    balanced_is_bar_symmetric      the once-centered form is q -> q^-1 invariant

### Attempt 2 (the writhe obstruction) -- an IMPOSSIBILITY, not just an absence

    borromean_writhe_zero              writhe (sigma_1^-1 sigma_2)^3 = 0
    writhe_prefactor_is_one            a ^ writhe(beta_Bor) = 1, for ANY a
    no_writhe_prefactor_yields_inv_cube
        a ^ writhe(beta_Bor) != (q^3)^-1   whenever q^3 != 1

markov-axioms-primitive.md states link invariance is restored by the writhe
prefactor outside the trace. Such a prefactor is a function of the writhe alone
and multiplicative in it, w -> a^w. Since beta_Bor's writhe is 0, EVERY such
prefactor is 1 regardless of a -- so none can be q^-3 unless q^3 = 1, which
fails at q_0 ~ 1.11.

This upgrades the finding from "no derivation trail" to "UNREACHABLE by the
normalisation rule the corpus states, on the corpus's own braid word". The
negative is now a theorem quantified over all writhe prefactors, not an
observation about the ones I happened to check.

Still open and unchanged: what DOES derive q^-3, given the numerics require it
(dropping it moves m_p to +37.0 %). The Garside-element guess (l(w_0) = 3 =
crossings of the B_3 half-twist Delta) remains recorded, not claimed.
