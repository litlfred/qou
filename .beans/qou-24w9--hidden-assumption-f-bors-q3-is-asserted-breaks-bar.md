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
