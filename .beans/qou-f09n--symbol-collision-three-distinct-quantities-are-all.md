---
# qou-f09n
title: 'SYMBOL COLLISION: three distinct quantities are all called c_2, and AGENTS.md calls the wrong one Taylor-exact'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T11:48:34Z
updated_at: 2026-08-17T00:51:45Z
---


## Not a contradiction — a collision. Retracting my own call.

I reported on PR #5210 that `qbeta_alpha_eff_ladder_reconciliation_probe`'s
`c_2 = -9/8` and the committed extraction's `c_2 = -1` were "two different
ladders" and "a live contradiction". **That was wrong.** They are the same
model, expanded two ways. Symbolically, `cos(alpha - u/2)*(1 - u^2)` divided
by its own `u^0` value `cos(alpha)`:

    u^0 coefficient = 1
    u^1 coefficient = tan(alpha)/2
    u^2 coefficient = -9/8          <-- = -1  +  (-1/8)

The `-1` is the coefficient of the **explicit multiplicative factor**
`(1 + c_2 u^2)`. The `-1/8` falls out of expanding the cosine. Their sum is
the total `u^2` coefficient of the normalised series. No number is wrong.

The `c_1 = tan(alpha)/2 != 0` vs the #1887 reframe's `c_1 = 0` is the SAME
issue, not a second one: the two parameterisations do not share a base point
(`Phi(0) = cos(alpha) != 1`), so their `c_k` are not the same coefficients.

## Three live meanings of `c_2`

| value | what it is | where |
|---|---|---|
| `-1` | coefficient of the explicit factor `(1 + c_2 u^2)` | `qbeta_utils.c3_target_at`, hardcoded |
| `-9/8` | total `u^2` coefficient of the normalised committed model | `qbeta_alpha_eff_ladder_reconciliation_probe` |
| `-8.00641` | bar-even part, exact in Q[sqrt 3] | `qbeta_c3even_exact_sseries_probe`, bean `8we6` |

Registry §2 already warns that attributes do not transfer across overloaded
symbols. This is that, three ways, in one channel.

## The actionable defect: AGENTS.md's "PROVED Taylor-exact"

AGENTS.md line 1062 (the `c_k` truncation-order banner) says:

> `c_2 = -1` is PROVED Taylor-exact

Under the natural reading of "Taylor" — the Taylor coefficient of the ladder
series — **the `u^2` coefficient is `-9/8`, not `-1`**. `-1` is the
coefficient of the explicit factor, which is *hardcoded* in the extractor
(`qbeta_utils.py`: `Q_N2 = Q_N1 * (1 + c_2 u^2)`, `c_2 = -1`), i.e.
definitional rather than derived. And per PR #5187 the Lean lemma about it is
a renaming: `1 - b^2 hbar^4 = 1 - (b hbar^2)^2` is `ring`-true, with the
substantive identification `asserted`, proved nowhere.

So the phrase is wrong on both halves: not "Taylor" (wrong coefficient) and
not "PROVED" (tautological lemma + hardcoded value).

**The irony is the point.** That same banner exists to stop a four-session
flip-flop caused by *"conflating 'N=3 beats 100x experimental' (true) with
'c_3 = -2 is Taylor-exact' (false)"*. It warns against this exact error class
for `c_3` while committing a version of it for `c_2`.

## What to do

1. **Do NOT change any number.** Nothing computes wrongly. This is naming.
2. **Register the three meanings** in the `ck-dk-canonical-registry` §2
   overloaded-symbol table, with distinct names — e.g. `c_2^factor = -1`,
   `c_2^series = -9/8`, `c_2^even = -8.00641`.
3. **Re-word AGENTS.md line 1062.** Proposed, for owner sign-off rather than
   unilateral edit (it is a STRICT banner and a contested channel):
   *"`c_2^factor = -1` is the explicit ladder factor's coefficient, fixed by
   construction, not derived; the normalised series' `u^2` coefficient is
   `-9/8`."*
4. **Withdraw the "contradiction" framing** wherever I put it — done here;
   also stated on #5210.

## Scope

No fit, nothing wired, no value changed. This is a naming/provenance defect,
not a numerical one — which is exactly why it survived: every consumer
computes correctly with its own `c_2`, and only a reader comparing two of
them sees a problem.

## Owner ruling on naming (2026-08-16): `c_2` and `\tilde c_2`

Owner: *"1 y but shorter c_2 and \tilde{c}_2 or so?"* — recommendation 1
(register the meanings) is APPROVED, with short names rather than my
superscripted `c_2^factor` / `c_2^series` / `c_2^even`.

Use the register's existing distinct-families convention, which already
carries `w_lambda` vs `\tilde w_lambda` for exactly this situation:

| name | value | what it is |
|---|---|---|
| `c_2` | `-1` | coefficient of the explicit ladder factor `(1 + c_2 u^2)` |
| `\tilde c_2` | `-9/8` | `u^2` coefficient of the normalised series |
| `c_2^even` | `-8.00641` | bar-even part, exact in Q[sqrt 3] (bean `8we6`) |

The third keeps its existing name — it is already established and is not part
of the confusion the owner is resolving.

Goes in `ck-dk-canonical-registry` §2 (overloaded symbols) and the notation
register's collision table, alongside the `w_lambda`/`\tilde w_lambda` entry.

## The u^1 rung: it EXISTS, and the corpus already knew

Question raised alongside the naming: does a `u^1` rung exist? Yes.

**Confirmed exactly** (sympy, series in `s = q - 1` then converted to `u`):

    a_1 = -sqrt(3)/12 = -0.14433756729740643

reproducing `qbeta-eigenphase-taylor-in-u.witness.json` to the digit. That
witness already concluded, correctly, that *"the eigenphase carries an
odd-order correction the ladder lacks — it is NOT the c_k generating factor
by itself."*

**And the deeper fact is also already corpus knowledge**, which is why this
is a confirmation rather than a finding. `qbeta_ck_from_operator_markov_trace_probe`
records: *"u ~ (q-1)^2 near q=1, so q->u reversion needs sqrt(u); the c_k
ladder is non-analytic at u=0."* Measured here independently: the `s^3`
coefficient of `cos(alpha - u/2)` is `(1 - sqrt 3)/8 ~ -0.0915`, nonzero, and
odd powers of `s` map to HALF-INTEGER powers of `u`. So the expansion is a
Puiseux series carrying `u^{3/2}`, not a Taylor series.

**The useful synthesis, which is a formalize-first prune:** any object
proposed as the generating function for the `c_k` ladder must be ANALYTIC in
`u` at `u = 0`. The eigenphase is not. That rules out a class of candidates
before any of them is fitted, and it is a stronger statement than "the u^1
coefficient does not match".

Note this is a FOURTH parameterisation-dependent reading of the same
coefficients, reinforcing why the naming fix matters: `tan(alpha)/2` (alpha
held fixed) and `-sqrt(3)/12` (expanded about u=0, alpha co-varying) are both
"the u^1 coefficient" of the same function.

## Literature check — the half-integer powers are the VARIABLE's fault, not the eigenphase's

Searched math + physics (paper-search MCP down; WebSearch used).

**Math side.** The Ohtsuki series is a formal power series in `h = q - 1` --
INTEGER powers of `(q-1)` -- with integral coefficients (conjectured Lawrence,
proved Rozansky). The Habiro ring is described as a ring of "analytic
functions at roots of unity", carrying a Taylor series at every root of unity.
Reparametrisations of LMO are Gevrey. So the literature's natural expansion
variable is `h`, and in it the series is analytic with integer powers.

**Physics side.** The Kashaev/volume-conjecture asymptotic has the form
`N^{3/2} * Phi(1/N)`. The `N^{3/2}` -- a half-integer power -- comes from the
Gaussian saddle-point integration. So half-integer powers are the EXPECTED
shape there, not an anomaly.

**The synthesis, and it reverses my own prune.** I wrote above that "any
candidate generating function for the c_k ladder must be analytic in u at
u=0, and the eigenphase is not." That prune is WRONG as stated. The ladder
chose `u = b*hbar_q^2`, which is QUADRATIC in the natural variable
`h = q - 1`. Reverting `u -> h` needs `sqrt(u)`; that is the whole source of
the half-integer powers. It is a variable-choice artifact, not a property of
the eigenphase -- the same disease as the phase's branch point, which was an
artifact of the cos parameterisation.

Measured: expanded in `s = q - 1` the SAME function is perfectly analytic,

    cos(alpha - u/2) = 1 + 0*s - (1/8)s^2 + ((1-sqrt3)/8)s^3
                         + (-107/384 + 5sqrt3/16)s^4 + ...

integer powers throughout. Note `s^1 = 0` exactly: in the h-variable there is
NO linear rung. The u^1 rung that started this whole question is an artifact
of expanding in a squared variable.

Cross-confirmation, unlooked-for: `qbeta_c3_phib_kappa_tower_scale_probe`
already records "odd rungs carry sqrt3, even rungs pure-rational -- the
Q(sqrt -3) trace-field". The h-expansion shows exactly that at the first two
orders: `s^2 = -1/8` is rational, `s^3 = (1-sqrt3)/8` is the first sqrt3.
(Do not over-read it -- s^4 and s^5 also carry sqrt3, so the parity split is
not a clean all-orders statement from this data alone.)

**Recommendation: express the ladder in `h` (or `hbar_q`), not in `u`.** Then
the series is analytic, the rungs are integer-power, the odd/even parity
question becomes well-posed, and it aligns with the Ohtsuki/Habiro framework
AGENTS.md already names as the permanent fix ("the Q_beta Habiro element").

Sources: Ohtsuki, asymptotic expansions of the Kashaev invariant (RIMS);
Garoufalidis-Le, Gevrey series in quantum topology; Habiro, unified quantum
SO(3) invariant; Garoufalidis-Scholze-Wheeler-Zagier, The Habiro ring of a
number field.


## T2 landed (2026-08-16, PR #5258) — naming registered, backed by a theorem

Item 1 (do not change any number): honoured — no number changed.

Item 2 (register the three meanings): DONE, with SHORT names per the owner
ruling rather than my proposed superscripts:

  c_2        = -1        explicit-factor coefficient   (hardcoded)
  c-tilde_2  = -9/8      normalised-series coefficient (measured)
  c_2^even   ~ -8.00641  bar-even part, exact in Q(sqrt 3)

Landed in ck-dk-canonical-registry §2 (rows), §9i (new subsection), and
notation-collisions.md (the symbol-lookup point).

**And the relation is now PROVED rather than measured** —
QOU/QBeta/LadderCoeffNormalisation.lean, sorry-free, #print axioms clean:

  normalisedQuadCoeff_eq         c-tilde_2 = c_2 - 1/8, for every A with cos A != 0
  normalisedQuadCoeff_at_neg_one c_2 = -1  =>  c-tilde_2 = -9/8

The -1/8 comes from the HALF-argument in cos(A - x/2): second derivative at 0
is -cos A / 4, quadratic Taylor coefficient -cos A / 8.  The A-dependence
CANCELS in the normalisation, which is the part worth a theorem -- the offset
is a clean rational, not an anchor-dependent quantity.  That is what makes the
two names legitimate rather than a papered-over discrepancy.

Item 4 (withdraw the 'contradiction' framing): done here, on #5210, and now in
the registry §9i itself.

## Item 3 (AGENTS.md line 1062) — STILL OPEN, owner sign-off

Not applied.  It is a STRICT banner in a contested channel.

Partial, defensible action taken instead: notation-collisions.md carried the
same 'proved Taylor-exact' phrase on the SYMBOL line, and that adjective is
removed there as a symbol-level claim, with an explicit note saying so.  No
tier changed anywhere -- the registry's c_2 row keeps its tier and its §9g
convention scoping untouched.  AGENTS.md is unmodified and awaits the owner.

## One correction to my own draft

I first justified the tilde as 'following the register's existing w_lambda /
w-tilde_lambda convention'.  That precedent is NOT available: the same register
retired the w-tilde pairing on the same day (owner ruling, further down the
same file).  The tilde device is fine; the citation was wrong and now says so.


## RETRACTION of this bean's own central claim (2026-08-16, owner-authorised T3/T4)

This bean said AGENTS.md line 1062 was 'wrong on both halves'.  Measured: only
ONE half is.  The bean's wording was:

  'Under the natural reading of "Taylor" -- the Taylor coefficient of the
   ladder series -- the u^2 coefficient is -9/8, not -1.'

That is A reading presented as THE reading.  Symbolically (sympy):

  u^2 coeff of prod_{k>=2}(1 + c_k u^k)            =  c_2        <- trivially
  u^2 coeff of [cos(A - u/2) * prod] / value_at_0  =  c_2 - 1/8

So c_2 = -1 IS a genuine Taylor coefficient -- of the explicit-factor product.
There is no k=1 factor, so nothing else contributes at order 2.  It is -9/8
only when the cosine is inside the series.  'Taylor-exact' is therefore
UNDER-SPECIFIED, not false, and the rule is SAY WHICH SERIES, never delete the
word.  I nearly swept 12 published sites deleting a correct claim.

The OTHER half stands and was the real defect.  Corpus-grepped: N2_factor is a
bare def in QBetaCategoricalPrecisionLadder.lean with NO theorem deriving it --
every use merely unfolds it, and the Kashiwara f-tilde_1 provenance lives in a
docstring.  The Lean proves only the re-reading.  So 'PROVED' overstates;
'structural' is right, and is what the source block itself already claimed.
The over-compression happened in AGENTS.md, not in the block.

## A third claim checked and deliberately LEFT ALONE

The banner's '3.47%' looked stale.  It is not: 3.4671% = |-2 - c_3| / 2, while
the ladder witness's own err_pct reports 3.3509% -- the SAME gap normalised by
the extracted c_3 = -2.06934258.  Neither should be rewritten into the other.

That this normalisation trap sits in the same banner as the c_2 / c-tilde_2 one
is the lesson of this bean, and I walked into it twice in one session.

The 'approx 3% cross-anchor' does measure loose: 2.3748% proton-normalised.
