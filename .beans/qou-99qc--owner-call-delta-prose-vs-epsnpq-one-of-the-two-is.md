---
# qou-99qc
title: 'OWNER CALL: Delta prose vs epsNPq — one of the two is wrong (fork forced by qou-avt6)'
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:35:22Z
updated_at: 2026-09-05T06:15:00Z
---

## Option (1) NARROWED, 2026-08-26 — the colour-weighted carve-out is closed

qou-avt6 fenced itself: "colour-weighted crossings fall outside the
q^m([2]/2)^c normal form, so do NOT quote the exclusion for words that do."
That carve-out was the last place the prose could still be right. It is gone.

`computations/qbeta/qbeta_epsnpq_colour_weighted_exclusion_probe.py` (15/15).
The fourth template `averaged_weighted` has counit
w(q) = q - h(1/2 - delta/4) with delta = (q-1)^2(1-q^-4)/3 exact
(flavor_split_leading), so eps of any word over ALL FOUR templates is
q^m ([2]/2)^c w^k. At the silver ratio h = 2 exactly, [2]/2 = sqrt2, and

    w(1+sqrt2) = 5*sqrt2 - 16/3,   |N(w)| = 194/9 = 2 * 97 / 3^2

so the vanishing condition gives 2^(C+K) * 97^K * 3^(-2K) = 1, and unique
factorisation reads off K = 0 from the 97, then C = 0, then M = 0. The
difference is identically zero; epsNPq is not.

The 97 is doing the work and nobody arranged it -- it is whatever prime the
flavour split contributes at that point. CHECK 4 TESTS that rather than
assuming it: had |N(w)| been a pure power of 2 the argument would fail, and
the probe would say so.

Control survives: chi_block_3 is found at (m,c,k) = (1,2,0) vs (3,2,0),
matching avt6's exponents.

ALSO DISPOSED OF, so it is not re-raised: "does ANY element have counit
epsNPq" is vacuous. eps is an algebra hom onto Q(q) hence surjective, and the
skein relation makes sigma - sigma^-1 = h a scalar outright, so epsNPq * 1
has counit epsNPq trivially. The content was always the CLASS.

## What is still open, and still yours

Two escapes remain from option (1), and neither is mine to pick:
  (a) Delta is not a difference of TWO words at all -- some other combination,
      which the prose would then have to name; or
  (b) epsNPq is simply wrong, and with it Q_A and the ladder phase.

Widening the crossing vocabulary is no longer among the options.

## 2026-08-26 — the FORK'S PREMISE DOES NOT HOLD (investigated on owner request)

Neither (a) nor (b) is forced, because the contradiction that forced the
choice is between two DIFFERENT functionals both written `eps`.

  avt6's eps    the AUGMENTATION sigma -> q. Its probe evaluates a word as a
                PRODUCT of per-letter counits (line 207:
                COUNIT["sigma"]**m1 * COUNIT["averaged"]**c1 * ...), which is
                legitimate only for an algebra map, and its table opens
                COUNIT["sigma"] = q.

  epsNPq        a value of the COORDINATE SUM sigma -> 1.
                QBetaCounitTrace.epsNP is defined as the functional "which
                weights every basis element by 1", applied to the stated
                normal-form vector

                    (n - p) = [h^2/2, -h/2, -h/2, 0, 0, 0]

                in basis [gamma, sigma_0, sigma_1, L+, L-, e^-]. Its
                coordinates sum to h^2/2 - h = h(h-2)/2 = epsNPq, EXACTLY
                (verified symbolically, difference 0).

sigma -> 1 is not an algebra map unless h = 0: push sigma^2 = h*sigma + 1
through a unital multiplicative map sending sigma -> 1 and get 1 = h + 1.
Lean, sorry-free (propext only):
`QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one`.

So avt6's theorem is TRUE and its scope is the multiplicative eps. Quoting it
against epsNPq is a functional mismatch -- the arity/shape class AGENTS.md
already names. On the SAME vector the two differ by exactly h(q-1).

WHAT THIS DOES NOT DO, and the distinction is the point. It does not vindicate
epsNPq. Measured at q0, the stated NF vector is not the exhibited nucleon-word
difference under EITHER functional:

    chi_(3)(beta_n - beta_p)  = -0.26038764179012078   (recomputed from the
                                                        words, not quoted)
    coordinate sum (epsNPq)   = -0.18720719452937831
    augmentation on same vec  = -0.21019934990050292

So qou-avt5's scope-(a) finding stands untouched: Q_A still rests on a vector
nobody has derived. The fork was the wrong question -- not a question with a
reassuring answer.

Probe: computations/qbeta/qbeta_epsnpq_functional_mismatch_probe.py (7/7).
Lean:  content/quantum-observable-universe/lean/QOU/QBeta/CounitSigmaOneForcesHZero.lean

STILL AN OWNER CALL, but a different one. Not "which of (a)/(b)", rather:
which functional is `eps` MEANT to be in the Q_beta ansatz, and what is the
element it should act on? Answering that is what would actually close Q_A.

## 2026-08-26 (later) — THE CONVENTION FEE, priced

Owner asked whether "a convention fee or non-colour-weighted [choice] is
sneaking around". Yes -- three, and each is larger than the residual it
supports. Probe: computations/qbeta/qbeta_ladder_convention_fee_probe.py (4/4).

  choice, canonicalised                              err (ppb)   vs published
  as published (proton pin, conv C, colour-blind)         37.7         --
  canonical COLOUR-WEIGHTED crossing (R3)              80332.6      2130x worse
  canonical convention D (z = q^3/(q^2+1))            601191.5     15944x worse
  muon pin (the block's own frame)                         7.34      0.19x BETTER
  ALL THREE canonical at once                         681534.7     18074x worse

1. NON-COLOUR-WEIGHTED AT THE BASE. Step 3 of the fitting-finding audit
   publishes the mixed u-d crossing as C(u,d;sigma) = sigma - h/2 --
   COLOUR-BLIND. Owner ruling R3 makes bring_color_weighted canonical,
   w = h(1/2 - delta/4). Swapping it moves Q_A by 80 ppm. So Q_beta's
   headline agreement is built on the PRE-R3 crossing.

2. CONVENTION C IN THE COS RUNG. alpha = (z-1)h/2. Under canonical z_D the
   same five rungs converge to 601192 ppb instead of 37.7. AGENTS.md flags the
   c_k ladder as C-frame (qou-cds1); this is the number.

3. MUON PIN. The block claims -0.0066 ppm. That reproduces at the MUON q0
   (7.34 ppb), not the canonical proton pin (37.7 ppb, 5.14x worse).

ALSO MEASURED, and it corrects the dashboard reading: AGENTS.md's "1279 ppb"
is EXACTLY the 2-rung truncation (computed 1279.465 ppb). The full five rungs
reach 37.7 ppb -- 4.8x short of the 7.8 ppb L2 target, not 164x. The
convergence is 1677569 -> 73828 -> 1279 -> 43.7 -> 37.8 -> 37.7 ppb.

The FIRST rung is a genuinely derivable piece -- Hoefsmit V_(2,1)
cos-symmetrization, no fit -- and it does the heavy lifting (1677569 ->
73828 ppb). That part is real and worth keeping.

TWO CORRECTIONS TO MY OWN EARLIER CLAIMS IN THIS BEAN:
 - "Q_A rests on a vector nobody has derived" is WRONG. Step 5 of the
   2026-05-24 audit derives it and I verified it: pure expansion of the
   single-wrap words, no Hecke reduction needed (no sigma^2 appears), L+
   cancels, coordinate sum = h(h-2)/2 exactly.
 - I first asserted every canonical swap DEGRADES the agreement. False for
   the pin: the muon frame BEATS canonical proton. That is the stronger fit
   signature, not a weaker one, and the failing assertion caught it.

THE CAP, restated with this in hand. Step 8 stays postulated, so Q_beta's
empirical content is one scalar. But the binding constraint is sharper: the
37.7 ppb figure exists only in a frame that is non-canonical in THREE
independent ways. Canonicalise all three and it is 681535 ppb -- 87000x short
of the L2 target.

### RETRACTION (same day): the "convention D = 601192 ppb" row was mislabelled

Owner challenged it -- "convention D makes everything else better, this seems
odd" -- and the challenge is correct.

THE ARITHMETIC IS RIGHT. alpha_C = -0.052336, alpha_D = -0.040486; cos rungs
0.9983986 vs 0.9989990; rungs 2-5 are z-independent. 601192 ppb reproduces.

THE LABEL WAS WRONG, and the corpus says so explicitly. AGENTS.md: "The ladder
must be RE-DERIVED under D, and that is not a z-swap". And
QOU.QBeta.decayLadder_zC_threeRow_ne_zero (sorry-free): if the decay channel's
decomposition kills the third row then its trace IS z_D and "the existing
C-frame ladder is not that trace (re-derivation, not substitution)".

I performed exactly the substitution the corpus forbids. So 601192 ppb is NOT
"what convention D gives" -- it is what an invalid move gives. What convention
D gives is UNKNOWN pending the re-derivation (qou-cds1).

WHAT THE ROW DOES ESTABLISH, restated: the ladder is z_C-LOCKED. Its cos rung
must supply exactly the 0.168 % that Q_A overshoots, and only alpha_C is large
enough to do it (alpha_D is 23 % smaller in magnitude, delivering 0.100 %).
That is evidence FOR the C-conditionality AGENTS.md already asserts -- it is
not a measurement of D's accuracy.

Items 1 (colour-blind crossing, 80 ppm) and 3 (muon pin) are unaffected.


## 2026-08-26 — the mislabelling has a hard consequence under convention D

From `qou-879g` (now answered): the corpus's own
[`prf:algebraic-gns-embedding`](content/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md)
places the convention-D theory in the **Temperley–Lieb quotient**
`H_∞(q)/rad ≅ TL_∞(q)` — the radical being exactly the `ℓ(λ) ≥ 3` blocks, since
`y_λ = 0` there.

A functional descends to a quotient iff it annihilates the ideal. Measured
(`qbeta_which_algebra_the_decay_channel_lives_in_probe.py`, 11/11):

- the **augmentation** `σ ↦ q` annihilates `J_(1³)` → **it descends**;
- the **coordinate sum** `net` does not — `net(e) = q³(q−1)/((q²+1)(q²+q+1))` → **it does not**.

Δ has a nonzero `(1³)` component, so `epsNPq` assigns different values to two
representatives of the same TL class.

**This sharpens the question this bean asks.** It is no longer only "which ε was
meant". Under the canonical convention, one of the two candidates **cannot** be
the answer on structural grounds: the coordinate sum is not a functional on the
space the framework's own GNS proof says the theory lives in. The augmentation
is. That does not by itself make the augmentation right — `qou-avt5`'s finding
stands that the stated NF vector is not the exhibited element under *either*
functional — but it removes a symmetry the fork used to have.


## 2026-08-26 (2) — the two admissible functionals BRACKET Q_β, and the matching one is inadmissible

`qbeta_admissible_functionals_bracket_probe.py` (15/15). Forced follow-on to the
TL answer (`qou-879g`), not a search.

Descent is annihilation of the ideal, so under D this bean's question has
exactly two admissible answers, each giving one determined number:

- **Multiplicative** functionals into a commutative ring are exactly the 1-dim
  reps. `H₃(q)` has two — `σ ↦ q` and `σ ↦ −1/q` — and the second **is** the
  block D quotients away. So exactly one survives: the augmentation.
  **Uniqueness, not a choice.**
- The Markov trace at `z_D` survives by construction.
- The coordinate sum the ansatz evaluates does not.

Measured, all three on the **same** object (the NF vector), against Q_codata:

| functional | admissible under D? | err |
|---|---|---|
| coordinate sum (`epsNPq`) | **no** | **+0.168 %** |
| augmentation `σ ↦ q` | yes | +12.470 % |
| Markov trace at `z_D` | yes | −43.157 % |

**The functional that reproduces the measured Q-value is precisely the one the
canonical convention forbids**, and both permitted ones miss by more than an
order of magnitude in opposite directions. That is evidence against the ansatz
as it stands, not a step toward repairing it.

**The trap, named:** the bracket means some convex combination hits Q_codata
exactly. That is a one-parameter fit against a single anchor. Deliberately not
computed; any weight must be **derived** from the representation.

### A calibration I wrote wrong, kept because the mistake is the point

I asserted the trace row should reproduce `qbeta-d-frame-trace-baseline`'s
−15.451 %. It **failed** at −43.157 %, and the failure is correct: that probe
evaluates `tr_M` on the **exhibited nucleon words**, this one on the **NF
vector**, and `qou-avt5` established those are different objects. Two numbers
both called "tr_M(Δ)" are not comparable and I nearly quoted them as if they
were. Now pinned as
`the_NF_vector_and_the_exhibited_words_give_DIFFERENT_traces`, and it is why
this probe holds the object fixed and varies only the functional.


### Strengthened: the admissible set is COMPLETE, solved not sampled

The structural condition **is** `y_(1³)(z) = 0`. Solved rather than checked
against candidates, it is quadratic in `z` with exactly two roots:

    z = q        and        z = z_D = q³/(q²+1)

Two things follow that were not visible when I listed candidates:

- **The two-row forcing is not unique to `z_D`** — `z = q` kills the `(1³)`
  block too.
- **At `z = q` the Markov trace IS the augmentation**, verified on all six basis
  elements and not merely on Δ. So the second root adds no third option; it
  reproduces the augmentation exactly.

The admissible set is therefore **closed at two elements**, and the bracket is a
completeness statement rather than a sample:

| root | functional | err |
|---|---|---|
| `z = z_D` | Markov trace at `z_D` | −43.157 % |
| `z = q` | ≡ the augmentation | +12.470 % |

And `epsNPq` is `tr_M` at `z = 1` on Δ, with **`z = 1` neither root**. So the
ansatz's +0.168 % comes from an evaluation inadmissible twice over: at a loop
value the corpus itself calls never attained on the substrate, and one that does
not survive the convention-D quotient.


### 🛑 SCOPE RETRACTION — the rank-one identity is n=3 only

`qbeta_rank_one_identity_is_n3_only_probe.py` (6/6). Caught by taking a sibling's
warning seriously rather than assuming my claims were exempt. PR #5337, on this
very bean, five days before I wrote the identity:

> *"One trap: at n = 3, Ξ coincides numerically with `y_(3)` … **`Ξ ≠ y_(n)` in
> general — do not generalise the n=3 coincidence.**"*

That is about a different coincidence. Mine is the same failure mode.

**Measured**, with the Ocneanu trace **solved** at each n from unital + cyclic +
the full Markov property at **every** level of the chain (not read off the stated
recursion, so this is an independent route):

| | rank | `net = tr_M^{z=1} − h·δ_{w₀}` |
|---|---|---|
| n = 3 | 6/6 unique | **holds**, defect exactly `−h` |
| n = 4 | 24/24 unique | **FAILS** — nonzero on **11 of 24**, four distinct values |

At n = 4 the trace at `z = 1` also takes **five** distinct values rather than
being constant off `w₀`. Not a near miss.

**Everything drawn from it stands** — each conclusion is evaluated on Δ, and
Δ ∈ H₃(q): `ε(Δ) = tr_M^{z=1}(Δ)` follows from Δ's *support*; the phase is a
transport within one family; the floor is `net(dC) = −h·y_(2,1)(1)`. The original
probe still passes 20/20 and no number moves. What was wrong is the **sentence**,
which read as a characterisation of the two functionals.

**Also found:** imposing the Markov property only at the **top** generator leaves
the Ocneanu trace **underdetermined** — rank 5 of 6 at n = 3. A partial Markov
condition does not pin it.


## 2026-08-28 — an independent probe re-derived the mismatch you already named, and got it wrong

PR #5893 (`qbeta_counit_silver_ratio_adjudication_probe.py`, merged
`4135ad98e2`) applied avt6's invariant to `epsNPq` and to a typed coordinate
sum, and concluded the fork is asymmetric. That is the functional mismatch this
bean diagnosed on 2026-08-26. The probe has been scope-corrected in place and
the conclusion retracted; the re-derivation of the typed coordinate sum from
live source survives and is hash-pinned.

Recorded here so the count is right: this bean's diagnosis has now been
**independently re-encountered**, which is evidence it is correct and evidence
that the entry is hard to find — it lives in a bean body, reachable only by
corpus-grep path 6.

No change to what is open. The decision in this bean is untouched and still
yours.


## 2026-08-28 — TRACK 3 CLOSED BY EXCLUSION: there is no weight to derive

Owner selected all four tracks. Track 3 was "hunt a derived weight for the
bracket". It does not need hunting — the answer is a rank computation.

`computations/qbeta/qbeta_admissible_span_prune_probe.py` (8/8, exact symbolic
over Q(q)).

**The prior question the bracket framing skips.** Matching on `Delta` alone is
ONE equation; agreeing as FUNCTIONALS on H_3(q) is SIX. A functional here is a
covector in a 6-dimensional space, so "is there a weight w with
w*aug + (1-w)*tr_M(z_D) = net?" has a definite linear-algebra answer:

    rank{aug, tr_M(z_D)}       = 2
    rank{aug, tr_M(z_D), net}  = 3        ->  net is NOT in the span

**So no weight — derived, fitted, convex or affine — reproduces the coordinate
sum as a functional.** There is nothing to derive. The bracket is a statement
about one number on one element, not about the functionals.

Exhibited concretely rather than left abstract: the weight that reproduces
`Delta` exists and is unique,

    w* = -q^2 + q + 1/q,    w*(q0) = 0.77884441254035836848...

and that same w* then **disagrees with `net` on 3 of the 6 basis elements**
(indices 3, 4, 5). That is the one-parameter-one-anchor fit this bean already
named, now with its failure exhibited off the anchor.

**Scope-(b), and the invariant is cited** per the AGENTS.md refutation rule: a
rank computation is a dimension bound, which is one of the permitted grounds.
This is an exclusion, not a failed search — re-running it will not change it.

**What it does NOT show.** Not that the Q-value is wrong; not that the ansatz is
irreparable. It removes exactly one repair route — the convex combination. The
honest options remaining are (i) adopt an admissible functional and accept its
error (+12.470 % or -43.157 %), or (ii) derive a different ELEMENT for an
admissible functional to act on. Option (ii) is where `qou-avt5`'s standing
finding bites: the stated NF vector is not the exhibited nucleon-word difference
under either functional.

Controls included so the rank is not an artifact: each covector is verified to
reproduce its functional on every basis element, and the augmentation is
verified multiplicative on the generators rather than assumed from its shape.

## 2026-09-04 — CORRECTION to this bean: the "1279 ppb is a truncation" reading is backwards

This bean records, under §"THE CONVENTION FEE, priced":

> "ALSO MEASURED, and it corrects the dashboard reading: AGENTS.md's '1279 ppb'
>  is EXACTLY the 2-rung truncation (computed 1279.465 ppb). The full five
>  rungs reach 37.7 ppb -- 4.8x short of the 7.8 ppb L2 target, not 164x."

**Every number there is right. The reading is backwards, and acting on it
would have been an anti-laundering violation.** I set out to correct AGENTS.md
from 164x to 4.8x and the measurement refused.

Probe: `computations/qbeta/qbeta_dashboard_rung_gate_is_not_a_truncation_probe.py`
(7/7).

**`per_observable_100x_status.py` does not truncate.** It walks the c_k cache
and `break`s at the first rung whose `tier` is not `derived`, for the reason
stated in its own source:

    "The dashboard headline reports the deepest cumulative DERIVED rung only;
     cal-anchored rungs are cached for downstream reuse but NEVER counted
     toward a 100x/1x pass (that would be circular)."

And `qbeta-ck-cache.witness.json` holds exactly two rungs:

    k=2  tier=derived       lean-proved, Taylor-exact, q0-independent
    k=3  tier=cal-anchored  extracted from CODATA Q_beta at canonical q0

So the gate fires at k=2 **by design**, and the rungs carrying the error from
1279 ppb to 37.7 ppb are extracted from the very measurement being predicted.

**Both figures are real and they answer different questions:**

    1279 ppb (164.0x)  deepest DERIVED rung -- parameter-free. The L2 status.
    37.7 ppb (4.836x)  full ladder INCLUDING cal-anchored rungs. A statement
                       about ladder convergence, NOT an accuracy result.

This is the distinction AGENTS.md already draws at CAL-1 and CAL-2 ("an m_mu
value computed at the muon q0 is the calibration tautology, not an accuracy
win"), one tier down on the c_k ladder. **AGENTS.md's 1279 ppb / 164.0x is
correct as written and is deliberately left unedited.**

**Method note, because it nearly produced the opposite report.** The dashboard
stores `err_ppb` as the STRING `'1279.'`. A numeric scan (`isinstance(v,
float)` over the witness tree, looking in [1000, 2000]) returns nothing, and
reads as "the dashboard no longer carries this figure" -- the exact inverse of
the truth. I wrote that conclusion down before catching it. Match on the
string. Pinned as an assertion in the probe so it cannot recur silently.

Nothing in the convention-fee pricing (items 1 and 3, the colour-blind
crossing and the muon pin) is affected; those stand. Scope-(a): nothing wired,
no content block edited.


## 2026-09-05 — the PUBLISHED closed form is the z = 1 cell. The question is no longer "which was meant".

Probe: `computations/qbeta/qbeta_published_form_is_the_inadmissible_z1_probe.py`
(15/15, exact sympy over ℚ(q); the pin enters only at readout).

This bean has asked, since 2026-08-26, *"which functional is `eps` MEANT to be
in the Q_β ansatz?"* — treating it as an open reading of an ansatz. **The
framework's published headline closed form already answers it**, and nothing in
the corpus had said so.

AGENTS.md's canonical-derivation cheat sheet publishes

    Q_β = m_e · |q² − 2q − 1| · (q + 1) / (2q³)

Set that against the ansatz shape `Q_β = |tr_M^z(Δ_S)| · E₀`, `E₀ = m_e/(q(q−1))`,
using the affine trace from
[`2026-08-29-delta-fork-at-admissible-parameters.md`](../docs/audits/2026-08-29-delta-fork-at-admissible-parameters.md),
and **solve for `z`**:

| branch | solved `z` | admissible? |
|---|---|---|
| positive | **`z = 1`** | **no** |
| negative | `z = h − 1 = q − 1 − 1/q` | **no** |

Neither is a root of the `(1³)` weight numerator `N(q,z) = (z−q)((q²+1)z − q³)`,
whose only roots are `z = q` (the augmentation) and `z_D = q³/(q²+1)`.

So the published form is **not neutral** between the two candidate functionals.
It commits to the coordinate sum `net`, and that is precisely the functional
convention D forbids. Verified two ways: the identity `|epsNPq|·E₀ = published`
is exact over ℚ(q) on **both** sides of the silver ratio (so it is not an
artifact of a sign branch), and it agrees to `0.0` at 60 dps at the pin.

**Calibration, run before concluding.** My affine trace reproduces this bean's
own published grid — `+0.168 %`, `+12.470 %`, `−43.157 %` — to within
`2.4e-4` pp across all three cells. Had it not, the trace would have been wrong
and the identity worthless.

### What this changes, and what it does not

- **It does not** show the published Q_β value is wrong *as arithmetic*. It is
  exact and reproduces to 50 digits.
- **It does not** adjudicate which functional *should* be used. That is still
  yours.
- **It does** convert the question from *"which ε was meant?"* — a question
  about intent, which nobody can settle by measurement — into a concrete
  either/or about a number the framework already publishes:

  **either** keep the published headline value, which is produced by a
  functional that does not descend to the algebra the corpus's own GNS proof
  says the theory lives in;
  **or** adopt an admissible functional and accept its error: `+12.470 %`
  (augmentation) or `−43.157 %` (Markov at `z_D`).

  Every route between those two is now closed by measurement, not by search:
  the convex combination (rank-3 exclusion, scope-(b), above), the base
  correction (`qbeta-d-frame-admissible-base-correction-search`: no
  parameter-free admissible correction, and its `√(1−h)` near-match was
  diagnosed as the forbidden `z = 1` returning), and bracketing (a property of
  **both** elements, so evidence for neither).

### 🛑 A naming defect found and fixed on the way: supergolden, not plastic

`ConventionDAdmissibleRoots.lean` scopes `one_not_root` to `q³ − q² − 1 < 0`
and calls that bound *"the plastic number ≈ 1.4656"* — at lines 40, 108 and
123 — and the 2026-08-29 audit repeats it.

**1.4656 is the SUPERGOLDEN ratio**, the root of `x³ = x² + 1` (OEIS A092526).
The **plastic number** is `≈ 1.32472`, the root of `x³ = x + 1` (A060006). A
different constant.

The **value quoted was always right**, which is why no grep for a wrong *number*
would ever have found it — the same shape as the Λ-vs-Cl₂ guard AGENTS.md
records. **Nothing proved is affected**: the Lean hypothesis is the inequality
`q³ − q² − 1 < 0`, never the name, so this is a docstring correction.

Corrected at 4 sites (3 Lean docstrings + the audit line). The `hplastic`
binder name is left alone — it is a local binder, and renaming it is a code
change for no gain. **Eight other "plastic" hits in the Lean tree are correct
and were deliberately not swept**: `FiveTwoOhtsukiBridge` and
`FiveTwoComplexPentagon` are about `u³ = u + 1`, which genuinely *is* the
plastic number.

Verified: `lean`-direct on `ConventionDAdmissibleRoots.lean` exits **0** with no
diagnostics both **before** and **after** the edit, against the real import cone.

Scope-(a) on the physics; the inadmissibility is scope-(b) with the root
computation as the cited invariant. Nothing wired, no content block edited, no
`c_k` proposed.
