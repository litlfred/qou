---
# qou-24w9
title: 'HIDDEN ASSUMPTION: F_Bor''s /q^3 is asserted, breaks bar-symmetry, and carries 37% of m_p'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-18T20:45:53Z
updated_at: 2026-11-16T19:28:00Z
parent: qou-2002
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

## Which normalisation is DERIVABLE? -- the option table, measured (2026-08-19)

Owner asked which convention QOU can derive. Computed the required N (from
F_Bor = |tr_M| . N and the m_p target) and tested every structurally-motivated
candidate. Required N = 4.4755738777400674, |tr_M(b_Bor)| = 0.99856216383679.

  option                              N          m_p (MeV)     vs CODATA   bar-sym  derivable
  1 writhe rule (w=0), N=1            1.0000     204.88        -78.16 %    YES      YES (corpus rule)
  2 Markov/TL delta^(n-1) = [2]^2     4.0437     847.14         -9.71 %    YES      YES (standard)
  3 [3]_q! , no division              6.1206    1285.39        +37.00 %    YES      YES (Poincare/dim)
  4 [3]_q!/q^3   CURRENT              4.4756     938.272089    -2.9e-10 %  no       NO (proved)
  5 [3]_q!/q^(3/2) half-centering     5.2338    1098.28        +17.05 %    no       partly
  6 q.[2]^2      near-miss            4.4884     940.98         +0.29 %    no       NO

### The structural result

Every DERIVABLE option is bar-symmetric, and every bar-symmetric option MISSES.
The only option that hits is the one proved non-derivable. That is not a gap in
the search -- it follows from the earlier theorems: tr_M and [3]_q! are both
bar-symmetric, so any braid-derived N is bar-symmetric, and the required N is
not (F_Bor(q^-1) = q^6 F_Bor(q)).

Searched bar-symmetric products [2]^b [3]^c [4]^e over b,c,e in [-4,4]x[-4,4]x
[-2,2] (~400 candidates). Closest is [2]^3[3]^2[4]^-2 at 0.34 %. That is
NUMEROLOGY, not evidence: three free exponents over ~400 candidates spanning a
wide range will produce a sub-percent hit by chance, which is the
search-space-entropy argument AGENTS.md uses against the 12-constant PSLQ basis.
It is recorded so nobody mistakes it for a find.

### The one principled bar-symmetric candidate

delta^(n-1) = [2]_q^2 -- the standard Markov/Temperley-Lieb strand
normalisation, the loop value raised to (n-1). It is DERIVABLE, bar-symmetric,
and misses by 9.71 %. That is the honest best available, and 9.71 % is far too
large to be a residual.

### What this means

The question "which normalisation is derivable from QOU?" has a definite answer:
  - DERIVABLE: the writhe rule (gives 1), and the Markov/TL strand
    normalisation (gives [2]^2). Both bar-symmetric, both miss badly.
  - NOT DERIVABLE: the one in use.

So this is not a matter of finding the right derivation -- the derivable options
are enumerated and none reproduces m_p. Either the mass identity needs a factor
that is genuinely a declared convention (and should be labelled one), or
something upstream of F_Bor -- the hbar_q convention, the muon anchor, or the
trace convention -- is absorbing a q-power that belongs elsewhere. The second is
worth checking: 1/hbar_q^2 is ALSO bar-asymmetric (hbar_q = 1 - 1/q), and the
two asymmetries combine to a net q^-2 across m_mu . F_Bor.

## The hbar_q repair hypothesis: TESTED and REFUTED (2026-08-19)

`computations/qbeta/fbor_normalisation_barsymmetry_probe.py` +
`fbor-normalisation-barsymmetry.witness.json` (2 assertions, both pass).

Last note here proposed the remaining repair: since `1/hbar_q^2` is ALSO
bar-asymmetric (hbar_q = 1 - 1/q) and the two asymmetries combine to a net q^-2
across m_mu . F_Bor, perhaps the q-power is simply MISPLACED -- use the
bar-symmetric hbar_sym^2 = (q^{1/2} - q^{-1/2})^2 = q - 2 + 1/q and drop /q^3,
giving a fully bar-symmetric mass identity.

I proposed it, tested it, and it fails.

### Why it is a real test rather than a reshuffle

q_0 is NOT free -- it is solved from the proton pin. So the alternative was
re-solved for its own q, and then scored on m_mu/m_e, which was NOT used in the
solve. That ratio is the corpus's own 9.5-sigma cross-check (proton-pinned =>
m_mu is a prediction), so it discriminates.

### Result

    CURRENT  hbar = 1 - 1/q, with /q^3      (bar-ASYMMETRIC)
       q                  = 1.10997858275138
       m_mu/m_e predicted = 206.768326370674
       error              = 211.16 ppb          <- the known mu-p tension

    ALTERNATIVE  hbar^2 = q - 2 + 1/q, no /q^3  (bar-SYMMETRIC)
       q re-solved        = 1.12303052937477
       m_mu/m_e predicted = 150.604111821442
       error              = -2.716e8 ppb  (-27.16 %)

    ratio: the symmetric form is 1 286 334x WORSE on the cross-check.

### What this changes -- and it is a real update

The bar-symmetric alternative reproduces the proton pin (it has a q that does),
but misses the untouched muon ratio by 27 %. So the /q^3 is NOT a misplaced
q-power that symmetry would repair.

The status of the factor is therefore sharper than "unjustified convention":

  NOT DERIVABLE   -- proved (unreachable by the writhe rule; double Poincare
                     centering; sole bar-asymmetric step)
  NOT ARBITRARY   -- it and the hbar_q convention JOINTLY satisfy TWO
                     independent observables (m_p pin and m_mu ratio) to ~200
                     ppb, where the natural symmetric alternative misses the
                     second by six orders of magnitude

A wrong normalisation would generally not survive an independent cross-check.
This one does. So the honest target is no longer "replace it with a derivable
one" -- the derivable options are enumerated and all fail (option table above).
It is "explain why THIS combination is the one that works".

That is a harder and more interesting question, and it is the one I would put to
the owner: the factor behaves like it encodes something real that the current
derivation vocabulary cannot express.


## WHERE /q^3 COMES FROM — it is the q-Schur Plancherel weight of the trivial block (2026-08-19)

Owner asked what the corpus and the literature say about the options. The
option table above was INCOMPLETE: it never considered normalising by a single
Wedderburn BLOCK weight. The corpus does exactly that, and the missing entry is
the one in use.

`computations/qbeta/fbor_q3_is_qschur_plancherel_weight_probe.py` (8/8, proton
pin, convention D).

### The provenance, and it is not arbitrary at all

`phase5/phase2b_dim_v21_bridge_derivation.py:29` states

    F_Bor = |tr_M| . [3]_q!/q^3 = |tr_M| / y_(3),   y_lam = q^{c(lam)}/[n]_q!

and that is an EXACT identity: `c((3)) = 0+1+2 = 3` is the CONTENT SUM of the
trivial partition. Measured: `1/y^Schur_(3) = 4.475573877740067446` = the
current factor, to the last digit.

This also explains the bar-asymmetry structurally, which nothing before did:
bar sends `lam -> lam'`, and `c(lam') = -c(lam)`. So the factor is
bar-asymmetric BECAUSE it is a single-block weight, and the block it picks is
the chirality-extremal one. That is the first candidate to escape the
bar-symmetry wall this bean hit — the wall was an artifact of only considering
normalisers built from tr_M and [3]_q!, both bar-even.

### The catch, measured

`y_lam = q^{c(lam)}/[n]_q!` is the q-SCHUR PLANCHEREL family
(`QSchurYLambdaClosedForm.lean` — and note the identification with the
categorical weight there is a CONJECTURE CLASS, not a theorem). The `tr_M` in
`F_Bor` is the WENZL/MARKOV trace. At the proton pin:

    sum_lam y^Wenzl_lam . chi^lam(beta_Bor) = 0.99856216383678726595
                                              = the Lean tr_M, residual 1.8e-71
    sum_lam y^Schur_lam . chi^lam(beta_Bor) = 0.66872287272701215631

    sum_lam dim_lam . y^Wenzl_lam = 1  EXACTLY   (= tr_M(1), the Markov
                                                  normalisation)
    sum_lam dim_lam . y^Schur_lam = 0.66967281337086841549

The first line is a THREE-WAY independent check — Lean closed form, the Wenzl
weight formula, and the Phase-1c character — agreeing to 71 digits. So the
Wenzl family is unambiguously the one that decomposes this trace, and the
q-Schur family is not.

So `/q^3` is a CROSS-FAMILY IMPORT: a q-Schur block weight applied to a Markov
trace. AGENTS.md's notation register forbids exactly this ("three
partition-weight families y_lam / w_lam / w~_lam are distinct at q != 1 --
never conflate").

### Two options collapse into one

    1/y^Wenzl_(2,1) = [2]_q^2   EXACTLY (22 digits, both pins)

So "normalise by the standard-rep block weight" and "the Markov/TL strand
normalisation delta^(n-1)" are the SAME option, not two. It remains the best
principled bar-symmetric candidate and still misses by 9.71 %.

    1/y^Wenzl_(3)   = 1.9786142409559419401  ->  m_p = 411.38  (-56.2 %)
    y^Wenzl_(1,1,1) = 0  in convention D — the bar-partner of the trivial block
                         is not available as a normaliser at all.

### Updated option table (proton pin, convention D)

  option                                        N            m_p (MeV)   family
  writhe rule (w=0)                             1.0000       204.88      corpus rule
  1/y^Wenzl_(3)   trivial block                 1.9786       411.38      Wenzl
  1/y^Wenzl_(2,1) = [2]_q^2 = TL delta^(n-1)    4.0437       847.14      Wenzl
  [3]_q!  no division                           6.1206      1285.39      Poincare
  1/y^Schur_(3) = [3]_q!/q^3   CURRENT          4.4756       938.272089  q-SCHUR

Every entry from the Wenzl family — the family that actually decomposes tr_M —
misses. The only hit is the q-Schur import.

### What the literature says

  * The Wenzl weight is the HOOK-CONTENT formula, and the witness records it as
    such: `s_{lam,X}(Q) = Q^{n(lam)} prod_x (1 - X Q^{c(x)})/(1 - Q^{h(x)})`.
    That is Stanley's principal specialisation
    `s_lam(1,q,...,q^{N-1}) = q^{n(lam)} prod_x [N+c(x)]/[h(x)] = q^{n(lam)}
    dim_q(lam)` — so a q-power carrying CONTENT is standard in this setting;
    what the q-Schur closed form drops is the hook/dimension half.
  * The weights at the minimal idempotents were first computed by Ocneanu (that
    work is lost) and reproved by Geck; Jones (Ann. Math. 126 (1987) 335-388)
    is the canonical source for the Markov trace -> HOMFLY construction.
  * HOMFLY framing: `H(D) = v^{-w(D)} P(D)`, so the framing correction is a
    WRITHE power and is 1 at w = 0 — which is what the Lean theorem
    `no_writhe_prefactor_yields_inv_cube` already says for beta_Bor.
  * The remaining standard normaliser is the `(n-1)`-power of the loop value,
    i.e. `delta^{n-1} = [2]_q^2` — the option that collapses with the Wenzl
    standard block above.

  Sources fetched 2026-08-19 via WebSearch (arxiv.org is egress-blocked from
  this sandbox, so the Ocneanu/Geck and hook-content statements are from search
  summaries of arXiv math/9806163 "Weights of Markov Traces on Hecke Algebras"
  and ncatlab's hook-content page, NOT from the full texts).

### What this changes for the open question

"Which normalisation is derivable?" now has a sharper answer than
"none of them". The factor IS a canonical object — the q-Schur Plancherel
weight of the trivial block, exponent = content sum — imported across a family
boundary. So the live question becomes:

    is there a reason the MASS channel should be normalised by the q-Schur
    Plancherel weight rather than by the Markov weight of its own trace?

That is answerable in principle (the two families differ by the hook/dimension
half of the hook-content formula), and it is a much better-posed target than
"what derives 3". Not attempted here.

Scope-(a). Does not refute F_Bor; does not touch the Lean-proved |tr_M|.

## 2026-11-16 — Lean 4 Plancherel Normalisation & Three-Way Reconstruction Formalized (PR #8169)

- **Lean 4 formalization** (`folio/quantum-observable-universe/lean/QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean`, `0` `sorry`, wired into `QOU.lean`):
  - `qschur_trivial_inv_eq_fbor_normaliser` & `qschur_bar_conjugate_duality`: proves `(y_{(3)}^Schur(q))⁻¹ = [3]_q!^bal / q³` and `y_{(1,1,1)}^Schur(q) = y_{(3)}^Schur(q⁻¹)` with `(y_{(1,1,1)}^Schur(q))⁻¹ = q⁶ · (y_{(3)}^Schur(q))⁻¹`.
  - `wenzl_weights_trace_normalised`, `wenzl_standard_block_inv_eq_two_bracket_sq`, & `wenzl_reconstructs_borromean_trM`: proves exact trace normalisation `1·y_{(3)}^Wenzl + 2·y_{(2,1)}^Wenzl + 1·y_{(1,1,1)}^Wenzl = 1`, `(y_{(2,1)}^Wenzl(q))⁻¹ = (q + q⁻¹)² = [2]_q²`, and exact algebraic reconstruction `y_{(3)}^Wenzl(q)·1 + y_{(2,1)}^Wenzl(q)·χ^{(2,1)}(β_Bor, q) + y_{(1,1,1)}^Wenzl(q)·1 = tr_M(β_Bor, q)`.
  - `net_bar_asymmetry_mmu_fbor`: proves `(1/ℏ_q²)([3]_q!^bal / q³) = [3]_q!^bal / (q² ℏ_sym²)`.
- **50-dps probe & witness**: `computations/probes/plancherel_normalisation_and_scale_bounds_probe.py` and `computations/probes/plancherel-normalisation-and-scale-bounds-probe.witness.json` (PR `litlfred/qou#8169`, head `32d6039de208cfa3dab898932c88023a55ef3267`).
