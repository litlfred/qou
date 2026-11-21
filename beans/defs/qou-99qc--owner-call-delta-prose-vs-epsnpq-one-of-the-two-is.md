---
# qou-99qc
title: 'OWNER CALL: Delta prose vs epsNPq — one of the two is wrong (fork forced by qou-avt6)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-26T07:35:22Z
updated_at: 2026-11-21T06:59:28Z
parent: qou-10v9
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
Lean:  folio/quantum-observable-universe/lean/QOU/QBeta/CounitSigmaOneForcesHZero.lean

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
[`prf:algebraic-gns-embedding`](folio/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md)
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


## 2026-09-05 (2) — "closed at two" is closed in ONE class. The hierarchy, measured.

Owner asked, on the two admissible options: *"what are options for admissible?
others?"*

Probe: `computations/qbeta/qbeta_admissible_functional_hierarchy_probe.py`
(13/13, exact sympy over ℚ(q); every dimension computed, none asserted).

This bean says the admissible set is **"closed at two elements"**. That is true
and it is closed **within the one-parameter Markov family `tr_M^z`** — it comes
from solving `y_(1³)(z) = 0`, a quadratic. It was never a statement about every
functional that descends. Measured across three nested classes:

| class | admissible subspace |
|---|---|
| all linear functionals on `H₃(q)` | **5 of 6** dimensions |
| **trace** functionals (`φ(ab) = φ(ba)`) | **2 of 3** |
| Markov traces `tr_M^z` | **2 points** — `z = q`, `z = z_D` |

The `(1³)` ideal is computed as the common `(−1/q)`-eigenspace of both
generators (dim 1, so admissibility is exactly one linear condition), not
quoted.

### The load-bearing result: relaxing the class adds NO new direction

    rank{aug, tr_M(z_D)}                        = 2
    rank{aug, tr_M(z_D), χ_(3), χ_(2,1)}        = 2      ← equal

**The two Markov points already SPAN the admissible trace space.** So going
from "Markov trace" to "any trace" buys only the *line through the two you
already have* — which is precisely the one-parameter fit this bean refuses. It
does not widen the honest options.

Going further, to **all linear functionals**, does add three dimensions. But a
non-trace functional is not a Markov trace, and the trace property is what
connects the functional to knot invariants at all. That is the trade, stated
rather than taken.

Control included: `net` sits outside the admissible trace space
(`rank{aug, tr_D, net} = 3`), reproducing this bean's rank-3 exclusion from a
different construction — the character basis rather than the covector one.

### And `w*` is the fit in closed form, not a derivation

`Δ` is supported on `{γ, σ₀, σ₁}`, so `tr_M^z(Δ) = h²/2 − h·z` is **affine in
`z`** — which is *why* a weight always exists. Matching any target is then
interpolation of the parameter:

    w* = (1 − z_D)/(q − z_D) = −(q³ − q² − 1)/q      (= this bean's w*, verified)

So `w*` is just where the inadmissible `z = 1` sits between the two admissible
roots. A restatement of one-equation-one-unknown.

**A near-miss worth recording.** `w*` carries the factor `q³ − q² − 1`, and so
does `N(q,1) = (q−1)(q³−q²−1)` — the admissibility numerator at the
inadmissible point. That looked like structure. It is a **shared cause**, not
independent evidence: both quantities measure how far `z = 1` is from being a
root, so the same polynomial must appear in both. Recorded because the
coincidence is attractive and would support a "the weight is forced" reading
that the algebra does not license.

**Answer to the question as asked: no, there are no other honest options.** The
two remain the two; everything between them is a fit; everything outside them
costs the trace property.

Scope-(a); nothing wired, no content block edited, no `c_k` proposed.


## 2026-09-05 (3) — DECISION DOCUMENT: the seven options, costed

Owner: *"Do a deep analysis of all the options. Include the pros and cons
downstream impacts recommendations."*

[`docs/audits/2026-09-05-qbeta-functional-decision-options.md`](../docs/audits/2026-09-05-qbeta-functional-decision-options.md).

The two existing audits state the *finding*; neither enumerates what can be
**done**. That gap is what this fills. Seven options, each with what it means /
costs / risks / commits to, plus the downstream map and a recommendation.

Two facts established here that change how the whole thing reads:

- **The 0.17 % is not a fit.** The ansatz appears in audit docs from
  **2026-05-01**; convention D was ruled **2026-08-15**. The number predates
  the constraint that excludes its functional by ~3.5 months. *(Chronology from
  authored filename dates — `git log` dates are rebase-rewritten here and are
  not a valid signal. I tried `git log -S` first and it returned the landing
  commit, not the authoring one.)*
- **No calibration moves under any option.** AGENTS.md: Q_β is a
  *"cross-check, not a fourth input"*. q₀, m_e, m_π, the mass channel and the
  binding channel are all untouched whichever way this goes. That makes the
  decision far lower-stakes than the +0.168 % vs +12.470 % gap suggests.

And **one hope killed**: passing to the TL quotient does *not* collapse `Δ_S`
and `Δ_L` into one class — the augmentation is admissible and separates them
(+12.470 % vs +39.324 %). **The functional question and the element question
are independent**; settling either leaves the other open.

**Recommendation (judgement, not finding): Option A** — keep the published
value, disclose the inadmissibility, and reclassify it as a pre-D / C-frame
conditional result, exactly as the `c_k` ladder is already handled. It is the
only option that describes the situation accurately, the blast radius is near
zero, and it forecloses nothing. Explicitly **not** recommended: adopting the
augmentation or the `z_D` trace, which replace a correct-but-inadmissible
number with an admissible-but-wrong one.

Option G (drop the trace condition) is listed but **struck**, not weighed:
without the trace property the value depends on the braid word rather than the
link, so the element ambiguity becomes permanent rather than open.

Scope-(a); nothing wired, no content block edited, no `c_k` proposed.
## 2026-09-05 (4) — OPTION E, formalize-first: the requirement is "scalar mod radical", and Δ_S provably fails it

Owner: *"formalize first!!! E"*.

Lean: `QOU/QBeta/AdmissibleAgreementDeterminesClass.lean` — **5 theorems, 0
sorries, `lean`-direct exit 0** against the real import cone.
Probe: `computations/qbeta/qbeta_option_e_forced_class_probe.py` (9/9, exact
sympy over ℚ(q); the pin enters only at readout).

### The narrowing, stated before computing

Option E is a trap attacked numerically: a functional on `H₃(q)` is surjective,
so a free `Δ` reproduces **any** target and the "derivation" is a six-parameter
fit against one anchor. Two structural facts remove all six:

- an admissible trace sees `Δ` only through `(χ_(3)(Δ), χ_(2,1)(Δ))` — 6 → 2;
- **both** candidate functionals are *normalised* (`ε(1) = 1`). Measured
  symbolically: `tr_M(z_D) = α·χ_(3) + β·χ_(2,1)` with
  `α = (q⁴+1)/(q²+1)²`, `β = q²/(q²+1)²`, and **`α + 2β = 1` exactly**. Since
  `χ_(3)(1) = 1` and `χ_(2,1)(1) = dim V_(2,1) = 2`, that line *is* the
  normalised admissible family — **one** parameter, not two.

### The sharp theorem, and it is better than what I set out to prove

I began with a 2×2 system ("two functionals agreeing pins the class"). The
numbers then showed `(1−α)/β = 2` **exactly, for all q** — and 2 is
`dim V_(2,1)`. That upgrades the result:

> **`normalised_agreement_iff_scalar`** (sorry-free): writing `a = χ_(3)(x)`,
> `b = χ_(2,1)(x)`, a normalised admissible trace gives `(1−2β)a + βb`. This is
> independent of `β` — i.e. **every** normalised admissible trace agrees, not
> merely the two named — **iff `b = 2a`**.

`b = 2a` says `χ_λ(x)/dim V_λ` is equal across both surviving blocks, which is
exactly **"`x` is a scalar modulo the radical"** (for `x = c·1`,
`χ_λ(x) = c·dim V_λ`). So the requirement is not an arbitrary extra condition
invented to close a gap — it is the statement that `Δ` is central-scalar in the
quotient the theory lives in, and it fixes the common value to `χ_(3)(Δ)`.

### And Δ_S fails it identically — scope-(b), invariant cited

    chi_(2,1)(Delta_S) = 0          exactly over Q(q)
    chi_(3)(Delta_S)   = (1-q^4)/(2q^2)  != 0

**`Δ_S` is supported, modulo the radical, entirely in the trivial block.** So
`b = 2a` fails identically and **no** admissible functional makes the Q-value
independent of the choice.

Two consequences worth keeping:

1. **The +12.470 % and −43.157 % cells are not two independent estimates.**
   Verified exactly: `tr_M(z_D)(Δ_S) = α·aug(Δ_S)`. They are *one* number
   rescaled by `α ≈ 0.5054`. The apparent "bracket" on `Δ_S` is an artifact of
   that single scaling, which weakens the bracket framing further than
   `2026-08-29` already did.
2. **The forced class is `χ_(3) = T`, `χ_(2,1) = 2T`** with `T = Q_codata/E₀ =
   0.1868936675566543…`. `Δ_S` is `+12.470 %` off in the first coordinate
   (calibration: this *must* equal the known augmentation cell, and does) and
   **−100 %** off in the second.

### What this does NOT establish

- **Functional-independence is POSITED.** It is not a theorem of the framework
  that a physical quantity must survive swapping the augmentation for the Markov
  trace, any more than an operator's trace must equal its determinant. What the
  formalisation buys is that the requirement is now *precise and falsifiable* —
  "scalar modulo the radical" — rather than a vague appeal.
- **No element realising the forced class is exhibited**, and none is claimed to
  exist among legitimate braid-word differences. That is the next step and it is
  where Option E either closes or dies.
- `Δ_L` is untouched here; `qou-avt5`'s finding that `Δ_S ≠ Δ_L` stands.

Nothing wired, no content block edited, no `c_k` proposed.

### Extension, same day — BOTH candidate elements are excluded for every physical q

The Δ_L row was extracted from the two admissible evaluations rather than a
coordinate vector (`tr_M` at `z = q` **is** `χ_(3)`; at `z_D` it is
`α·χ_(3) + β·χ_(2,1)`, so `χ_(2,1)` follows by inversion). Calibrated: that
route reproduces `χ_(2,1)(Δ_S) = 0`, matching the direct covector computation.

| element | `b − 2a` | positive real roots | any with `q > 1`? |
|---|---|---|---|
| `Δ_S` | `(q−1)(q+1)(q²+1)/q²` | `1` | **no** |
| `Δ_L` | `(q−1)(q+1)(2q⁶+3q⁴+2q²−1)/(4q³)` | `0.5632`, `1` | **no** |

**Neither element is scalar modulo the radical at any `q > 1`.** Scope-(b), and
the invariant is cited: a polynomial with no root in the physical regime.

**And the `q = 1` root is degenerate, not a solution.** At `h = 0` the proton and
neutron words *coincide* — `σ₀(σ₁ − h/2) → σ₀σ₁ ← (σ₀ − h/2)(σ₁ − h)` — so
`Δ → 0` and the condition holds only as `0 = 0`. Both residuals carry the factor
`(q−1)(q+1) = q·h` for exactly that reason. Do **not** read the shared `h` factor
as "the condition is nearly satisfied": it is the statement that the whole
difference vanishes classically.

**What this does not say.** It excludes the two candidates, not the route: `b −
2a` is surjective over general elements, so there is no general obstruction. A
third element could satisfy the condition. What is now known is that neither
element the corpus currently has does, for any physical `q`.

### Closing enumeration, same day — the choice is a LINE, and it is surjective

`qbeta_admissible_line_exhausts_the_choice_probe.py` (12/12). The bean's
question is *"which functional evaluates Δ"*. The answer is that **the Q-value
cannot determine it**, because the candidates form a one-parameter family whose
value map is affine and onto.

Decomposing the Markov trace in the character basis of `H₃(q)` — derived here,
not assumed — gives

```
tr_M(z) = a(z)·χ_(3) + b(z)·χ_(2,1) + c(z)·χ_(1³)
c(z) numerator = q²·(z − q)·((q²+1)z − q³)
```

so the admissibility condition `N(q,z) = 0` of the 2026-08-29 audit **falls out
of the decomposition** rather than being posited, and `c(1) = q²(q−1)(q³−q²−1)/…
≠ 0` re-derives the `z = 1` inadmissibility of PR #6722 from a second route.

Normalising `φ(1) = 1` collapses the admissible trace space to the line
`φ_β = (1−2β)·χ_(3) + β·χ_(2,1)` — because `χ_(3)(1) = 1` and `χ_(2,1)(1) = 2`.
Both Markov points already lie on it: `z = q` at `β = 0`, `z_D` at
`β = q²/(q²+1)² ≈ 0.24730`.

On any element the value map is affine with slope exactly the scalar-mod-radical
residual:

```
φ_β(Δ) = χ_(3)(Δ) + β·( χ_(2,1)(Δ) − 2·χ_(3)(Δ) )
```

and that slope has **no root at any `q > 1`** (previous section), so the map is
**surjective**: solving `φ_β(Δ) = t` for a *symbolic* target `t` returns exactly
one `β`, on both elements.

| | `β` | `Δ_S` | `Δ_L` |
|---|---|---|---|
| `z = q` (augmentation) | `0` | **+12.470 %** | **+39.324 %** |
| `z = z_D` | `0.24730` | **−43.157 %** | **−15.451 %** |
| hits CODATA | — | `0.055437` | `0.177538` |

All four published grid cells are **reproduced from the character route**, which
is the calibration that makes the rest of the table trustworthy; and the
CODATA-hitting `β` is neither Markov point, on either element.

**So the four doors are now all enumerated:**

| door | what it costs | outcome |
|---|---|---|
| Markov **and** admissible | nothing — no free parameter | two points only: +12.470 % / −43.157 % |
| Markov, drop admissible | one parameter (`z`), fitted | `z = 1` exactly, and it is outside the TL quotient (#6722) |
| admissible, drop Markov | one parameter (`β`), fitted | reachable at `β* ≈ 0.0554`, with no independent characterisation |
| **neither choice matters** (functional-independence) | no parameter | impossible on both candidate elements at every `q > 1` |

**The consequence for the decision.** "Maybe some *other* admissible functional
works" is *true and empty* — one parameter fitted to one anchor has no
predictive content, and it is the same fit the published form already is, moved
from `z` to `β`. The only door that removes the parameter without an anchor is
functional-independence, and it is closed for the elements the corpus has. The
recommendation in
`docs/audits/2026-09-05-qbeta-functional-decision-options.md` (Option A — keep,
disclose, reclassify) is unchanged by this; what changes is that the option
space is now known to be exhausted rather than merely unexplored.

Nothing wired. No content block edited.

### 🟥 The 2026-09-05 anti-fitting directive eliminates `z = 1` — my Option A recommendation is WITHDRAWN

`AGENTS.md` gained **§NO FITTING, EXCEPT CAL-1/2/3** on `main` in `af1368d43ed`,
dated today, after the analysis above was written. It decides most of this bean,
against what I recommended.

Two of its clauses are directly on point:

> **Selection against the target.** Choosing an *object* — a knot from a census,
> a partition, a truncation order, **a branch** — because the choice reproduces
> the measured value. No continuous parameter is tuned and it is still a fit.

> **Accuracy is not evidence of correctness here, and a more accurate fitted
> route is worth LESS than a less accurate derived one.**

`z = 1` is precisely a **branch** of the Markov family, sitting outside the
admissible set (`c(1) = q²(q−1)(q³−q²−1)/… ≠ 0`, so it does not annihilate the
`(1³)` block the GNS/TL quotient kills), and its entire case is that it lands at
0.17 %. Under the directive that case is not merely weak — it is the fit
signature itself.

**So Option A (keep the published number, disclose, reclassify as pre-D
conditional) is withdrawn.** My argument for it was that the 0.17 % predates the
convention-D ruling by ~3.5 months and so was not fitted *when written*. That
does not survive the directive, which asks whether the number the paper
**publishes today** comes from a derived route — not whether its author was
fitting at the time. It does not.

**What survives is the two derived options**, and the directive explicitly
forbids choosing between them by accuracy:

| functional | `β` | Q_β | vs CODATA `0.7823334` MeV |
|---|---|---|---|
| `z = 1` (published) | *not on the admissible line* | `0.7836458` | **+0.168 %** — **eliminated** |
| `z = q`, the augmentation | `0` | `0.8798906` | **+12.470 %** |
| `z_D = q³/(q²+1)`, the convention-D Markov trace | `q²/(q²+1)²` | `0.4447004` | **−43.157 %** |

Choosing `z = q` over `z_D` *because* 12 % beats 43 % would be the same defect
one level down. The choice has to come from what `ε` **means** in
`Q_β = |ε(Δ)|·E₀`, and the corpus carries two functionals under that name — the
augmentation (an algebra map, `σ ↦ q`) and the coordinate sum
`net`/`epsNPq` — which is this bean's original question and is unchanged.

**Agent reading, marked as judgement, not a finding:** if `ε` is the *Markov
trace* in the canonical convention then the 2026-08-15 ruling names `z_D`, and
the answer is **−43.157 %**; if `ε` is the *augmentation* the answer is
**+12.470 %**. Nothing measured this session distinguishes them — the directive
removes one option, it does not pick between the remaining two.

**Not enacted.** Changing the published number touches ~8 content blocks and the
`AGENTS.md` canonical-chain cheat-sheet line (`Q_β … ≈ 0.784 MeV (0.17 %)`), and
which of the two derived values replaces it is the owner's call.


### Robustness: the `z = 1` inadmissibility is not a Skein-normalisation artifact (2026-09-05, PR #6832)

Bean `qou-8bxv` landed the same morning as #6722/#6763, measuring that **two Skein
normalisations are live** and are provably not bracket rescalings:

    (H)  L+ - L-           = (q - 1/q) L0            AGENTS.md §7a, STRICT
    (J)  q[L+] - q^-1[L-]  = (q^1/2 - q^-1/2) [L0]   8 live blocks, 5 chapters

**Both of this bean's merged results were computed in (H).** That made the shared
finding — the published `Q_β` form sits at `z = 1`, inadmissible under convention D —
a candidate convention artifact, which would have **dissolved** this bean's decision
rather than answered it. Tested; it does not.

**Transport.** Under (J) the generator has eigenvalues `u⁻¹, −u⁻³` with `u = √q`, so
`σ_J = u⁻²·σ̃(u)` — the (J) algebra is the (H) algebra in the square-root variable with
the *generator* rescaled. `ζ = u⁻²·z̃` carries convention D's roots to `ζ = u⁻¹`
(= 0.9491671528 at `q₀`) and `ζ = kernel(u) = u/(u²+1)` (= 0.4993203342).

**Result, both defensible readings of the element** (`Δ_S` is convention-laden — its
typed-crossing shift `d ∈ {−h/2, −h}` is a multiple of the bridge, so there is no unique
(J) counterpart):

| reading | outcome |
|---|---|
| element unchanged | `z = 1` inadmissible under (J) at **every `q > 1`**, no pin needed — *stronger* than (H), which excludes it only because `q₀` is not the supergolden root of `q³ = q²+1` |
| shift follows the bridge (`d → −s/2, −s`) | roots `−1.7411834668`, `+1.8455715251`; neither admissible |

No (J) admissible cell lands within 1 % of CODATA (closest `−5.518 %`). A **negative
control** (solver recovers an admissible parameter from a target synthesised at it) and a
**calibration** (reproduces the merged `+12.470 %` / `−43.157 %` to eight figures) make the
NONE mean something.

**Byproduct, and it is NOT new:** `z_C(q) = z_D(√q)/q` is the one-line composition of
`markovZC_eq_kernel_sqrt` and `markovZD_eq_sq_mul_kernel`, sorry-free on main in
`QOU/BraidKnot/MarkovConventionSeparation.lean`. The contribution is reading that module's
`q²` rescale as the (H)→(J) Skein normalisation — and it **supports** the convention-C
excision rather than softening it: `z_C(q) = kernel(√q)` is correctly normalised for the
algebra at `√q`, i.e. the *wrong specialisation point*, which is why `qou-cxjq` /
`qou-lp5d` / `qou-pmkh` are right that substitution cannot repair such sites.

Two arity gaps are machine-checked, not asserted:
`no_kernel_instantiation_is_conventionD` quantifies no rescaling factor, and
`no_rescaling_of_skein_weights` binds one constant on the **bracket** at fixed `q` while
this map rescales the **generator** and substitutes `q = u²`. Both theorems stand.

The symbol `z_J` is deliberately avoided — `qou-qlma` owns it for a different number
(`0.0274199478`), and `1/δ = 0.497290545` already sits 0.408 % from `ζ` (`qou-98g5`).

**This closes one way the decision could have been dissolved. It does not pick an option.**
The owner call is unchanged: `z = q` (`0.8798906` MeV, +12.470 %) or `z_D` (`0.4447004` MeV,
−43.157 %) against CODATA `0.7823334` MeV, decided by what `ε` *means* — not by residual,
which §NO FITTING's corollary forbids.


### Correction: the registry count is 13, not eight (2026-09-05, PR #6832)

The `qou-99qc` write-ups — PR #6832's body, its probe docstring, and this bean's
robustness section — cited **"eight `blocked_on_rederivation` rows of the
trace-convention registry"** as support for *a convention-C site is not
repairable by substituting `z_D`*.

**Measured:** `docs/coordination/trace-convention-registry.json` carries
`blocked_on_rederivation` as a **top-level array with 13 entries over 12 distinct
files** (`deltalambda_bareven_b4_magnitude_probe.py` appears twice). It is not a
per-row `status` value at all — a `status` histogram of that file returns
`agreed 4 / agreed-migration-pending 3 / disputed 1` and **zero**
`blocked_on_rederivation`, which is why a naive status-keyed count reads 0 and a
naive `grep -c` reads 4 (the key, a note, and two prose mentions).

**Not staleness — my error.** The array held **13 at this branch's own base
commit** as well as on current `main`, so 181 commits of drift did not make the
figure wrong. It came from a corpus-grep report and I relayed it without opening
the file. The registry did move in that window (+44/−15 lines) and the count did
not, so the coincidence that would have excused it does not exist either.

**Substance unaffected.** The registry states the claim in its own words:
*"Sites that must NOT stay on convention C but cannot be migrated by substituting
`z_D`, because the substitution changes the site's asserted RESULT rather than
its spelling."* Only the cardinality was wrong; the corrected text now quotes
that sentence instead of paraphrasing it.

**Contamination surface, all four checked:**

| carrier | state |
|---|---|
| probe docstring (`qbeta_skein_normalisation_admissibility_robustness_probe.py`) | fixed, producer re-run 13/13 |
| its witness `caveats` | fixed by the re-run |
| #6832 PR body | fixed |
| this bean | this entry |
| #6820 sibling comment | **no edit needed** — it makes the claim without a cardinality |

**Two different eights — do not sweep the token.** The same probe says the (J)
Skein normalisation is live in *"eight content blocks across five chapters"*
(lines 17 and 378). That eight is `qou-8bxv`'s and is **correct**. A
token-level fix would have broken a right number while repairing a wrong one —
the failure mode AGENTS.md names for figures that differ only in what they count.

No result changed: 13/13 before and after.

## 2026-09-07 16:45Z — the transport's rescale half is now a sibling's Lean, not my arithmetic

`492ad4221f6` (bean `qou-d0qq`) landed
`QOU.Mass.KZLevelFromHeckeNormalisation.ratio_invariant` on main — sorry-free,
generic field:

```lean
theorem ratio_invariant (c a b : K) (hc : c ≠ 0) (hb : b ≠ 0) : (c * a) / (c * b) = a / b
```

That is exactly the scalar-rescale half of #6832's transport
`σ_J = u⁻²·σ̃(u)`. Two checks added to
`qbeta_skein_normalisation_admissibility_robustness_probe.py` (now **15/15**,
was 13/13; every prior check unchanged and still passing):

- `H_and_J_generator_ratios_are_MINUS_q2_and_MINUS_q` — derived from each Skein
  relation directly, not asserted. In the **same variable `q`**: (H)
  `L₊ − L₋ = (q−q⁻¹)L₀` has eigenvalues `{q, −q⁻¹}`, ratio **`−q²`**; (J)
  `q[L₊] − q⁻¹[L₋] = (q^½−q^−½)[L₀]` has `{q^{−1/2}, −q^{−3/2}}`, ratio
  **`−q`**. The ratios differ, so the two normalisations are not rescalings of
  each other — the ratio-side restatement of this probe's separation premise
  (`qou-8bxv`).
- `the_u2_rescale_half_of_the_transport_is_INERT_on_the_ratio` — cites the Lean
  above rather than re-deriving it.

**What this buys:** the transport has two parts, a rescale and a
reparametrisation `q → u`. The rescale is now closed by someone else's Lean, so
the **reparametrisation is the whole content** of the (H)→(J) move.

## Same landing carries a scope over-claim — reported, not fixed by me

`KZLevelFromHeckeNormalisation.lean` says its `e^{iπħ} = q²` is *"stated so no
convention can move it"*. It guards the `ħ`-vs-`k` bookkeeping axis correctly,
but the ratio `−q²` is read off **(H)**, and feeding (J)'s ratio `−q` into the
same matching step `λ₁/λ₂ = −e^{iπħ}` gives `e^{iπħ} = q`, i.e. **`ħ` halves**
(`|ħ|` `0.066425366` → `0.033212683` at the proton pin) and `k+2` doubles.

Not a refutation: AGENTS.md §7a makes (H) STRICT, so their number is right under
the canonical reading. The defect is the scope sentence — the relation is
conditional on the Skein normalisation, and that is a live fork here
(`qou-8bxv`: 8 content blocks, 5 chapters). Reported on #7088, comment
5573521151; theirs to fix.

## `qou-37j2` / #7084 scopes my own `ε` recommendation

#7084 verified the merged `z = 1` inadmissibility at source (re-ran the probe,
15/15) and wired it into the L2 dashboard as `functional_admissibility_qbeta`.
Its framing adds a caveat I should carry: it names **Option E** — *keep an
admissible functional and find the element it should act on* — as the only one
of the seven options that could give a parameter-free admissible sub-1 % result.

My standing recommendation (`z_D`) chooses between the two admissible roots **for
the existing element `Δ = 𝓑_n − 𝓑_p`**. It should be stated with that scope:
*if the element stays `Δ`, then `z_D`*. If the element is the thing that moves,
the root question is downstream of a different choice and my recommendation does
not bind.


## 2026-09-08 — Option E has a SHARP acceptance test, and it is aimable

`computations/qbeta/qbeta_option_e_required_level_probe.py` (23/23), witness
`qbeta-option-e-required-level.witness.json`. Scope-(a). Wires nothing, selects
nothing, proposes no element.

THE REFRAME. On the H_3(q) normal-form basis the Markov trace is
`TR(z) = [1, z, z, z^2, z^2, z(hz+1)]`, so for a FIXED element `Delta` the
prediction is QUADRATIC in z. Requiring it to reproduce Q_beta therefore does
not leave a free choice -- it DETERMINES z. So "which element" and "which
functional" are not independent questions: each candidate Delta names the
functional it would need, and by the Wenzl relation that functional is a LEVEL
(r = 1 augmentation, r = 2 convention D; r = 1.1238831038 is why z = 1 fails).

MEASURED, on the corpus's own candidates (imported from
`qbeta_delta_candidate_census_probe`, not re-derived):

    candidate                  level 1      level 2     required r
    delta_S short NF           +12.470 %    -43.157 %     1.1257859
    nuc9 build_nucleon_nf      +13.083 %    -30.936 %     1.1343880
    nuc11 interleaved          +39.324 %    -17.496 %     1.4600767
    nuc11 gen-grouped          +39.324 %    -15.451 %     1.4912011
    16 constructed readings    +39.324 %       (varies)   1.1948 .. 1.2165

20 required levels; ZERO within 1e-3 of an admissible one; closest approach
0.126 away.

TWO RESULTS THAT WERE NOT WHAT I WENT LOOKING FOR.

1. LEVEL 1 IS BLIND TO BRAID ORDER. eps_aug is multiplicative, hence a product
   over letters, hence order-independent. Interleaved and gen-grouped carry the
   same typed-crossing multiset in a different order and agree to 20 digits at
   level 1 (-0.26038764179012080207) while differing in the third digit at
   level 2. All 16 assignment readings likewise share ONE augmentation. So an
   Option E element differing from an existing one only by ordering or by quark-
   generator assignment is, at level 1, the same number. To move the level-1
   value you must change the crossing MULTISET, not the braid.

2. THE BRACKETING IS UNIVERSAL, AND THAT IS THE OBSTRUCTION. On every candidate
   level 1 overshoots Q_beta and level 2 undershoots it, so by IVT the required
   level lies strictly BETWEEN the two admissible ones -- which is exactly why
   it is never one of them. This makes Option E's acceptance test aimable:

       AN ELEMENT THAT CLOSES OPTION E MUST HAVE ITS LEVEL-1 AND LEVEL-2 VALUES
       ON THE SAME SIDE OF Q_beta.

   A candidate that brackets is rejectable without solving anything.

DELIBERATELY NOT A SEARCH. Enumerating elements until one lands on r = 1 or 2
would be selection against the target, i.e. a fit under AGENTS.md NO FITTING.
The 16-variant family is reported as a RANGE for that reason; its best-landing
member is not a result.

A CALIBRATION DEFECT FOUND EN ROUTE, already flagged by the census but worth
stating in one line: the census's \`net\` is the COORDINATE SUM, and it differs
from tr^{z=1} by exactly h*(e^- coordinate) -- proved symbolically here, before
any pin. Only the gen-grouped model has e^- = 0, so the corpus's "coordinate sum
= tr at z=1" identification holds on that model alone.

THE OWNER CALL IS UNCHANGED. This narrows Option E; it does not decide which
functional eps is. That is still yours, and still the question of whether D7's
scoping of convention D to the decay channel reaches the choice of functional
WITHIN that channel or only the convention its objects are expressed in.

## 2026-09-08 — OWNER DECISION (chat, AskUserQuestion on PR #7159 session): the AUGMENTATION.
Option presented and selected: *'1. Decide ε in Q_β (qou-99qc) — Augmentation σ↦q (+12.47 %), z_D trace (−43.16 %), or retract Q_β; I recommend the augmentation.'* The owner selected it (together with three other items). Recorded reading: ε(Δ) := the augmentation σ ↦ q (option B of 2026-09-05-qbeta-functional-decision-options.md §3), i.e. Q_β base = 0.8798906 MeV, +12.470 %. Note the selection endorsed an option that carried the agent's recommendation; if the owner intended only 'decide it', this line is the place to overrule.
Consequences: (i) the published 0.17 % closed form is retired as the base — cite it only as the C-frame / z=1 historical cross-check; (ii) qou-cds1's ladder re-derivation now has its base (the augmentation), so S1 can start on the phase question (qou-pdix); (iii) dashboard rows Q_β / m_n / Δ_pn are to be re-scored on the augmentation base and stamped ADMISSIBLE-AUGMENTATION — NOT done in this session (witness sweep needs the producer under D; ask-before-change); (iv) AGENTS.md scoping note updated to record the ruling. Status stays todo until (iii) lands.

## 2026-09-08 (later) — the selection above is IN TENSION with D7, per 13bb8243d8 on main (qbeta_augmentation_is_a_markov_trace_probe.py): the augmentation IS the Markov trace at z = q, so 'which functional' = 'which Markov parameter', and D7 (convention D governs the decay channel; D = two-row truncation) selects z_D (−43.157 %), the augmentation being the one-row truncation (y_(2,1) = 0) and not D. The owner selected the augmentation on an option written before that commit was known. Owner confirmation requested in chat; neither base wired until it arrives. Default if nothing: the record stands as 'augmentation selected, D7-tension flagged', and no witness moves.

## 2026-09-08 (final) — OWNER RULING: ε := the Markov trace at z_D = q³/(q²+1) (option C), following D7. Put to the owner with both options framed after 13bb8243d8; answer: 'A. z_D — follow D7'. Base 0.4447004 MeV, −43.157 % vs CODATA — a documented honest miss on the canonical base, not a fit. The augmentation (+12.470 %) is the other admissible point, proportional (α=(q⁴+1)/(q²+1)²). Consequences: (i) published 0.17 % retired as base (z=1 cell), historical C-frame cross-check only; (ii) qou-cds1's ladder base is z_D; S1 reduces to the phase (qou-pdix); (iii) dashboard rows Q_β / m_n / Δ_pn to be re-scored on z_D and stamped ADMISSIBLE-zD — NOT done this session (producer under D; ask-before-change); (iv) AGENTS.md scoping note, precision-goals.md, cheat-sheet row 11 and the 2026-09-08 audit §8 all record this. Status stays todo until (iii) lands.


## 2026-09-12 — what the ruling re-weights in the Lean layer (PR #7188)

The ruling is recorded above; this does not restate it. What it adds is the
effect on the acceptance-test side, which is not a restatement.

**1. The canonical eps is the NON-multiplicative one, so braid ORDER is now a
live degree of freedom for the observable.** Sorry-free in #7188:

    multiplicative_forces_eigenvalue   a unital multiplicative functional sends
                                       the Hecke generator to z, and s^2 = hs+1
                                       forces z^2 = hz + 1, so z is one of the
                                       TWO eigenvalues q, -1/q.
    zD_lt_self, zD_pos                 z_D = q^3/(q^2+1) is strictly below q and
                                       strictly positive, hence above -1/q.
    conventionD_not_multiplicative     therefore z_D is neither eigenvalue.

The corpus had only the z -> 1 instance (QOU.QBeta.CounitSigmaOne); this is the
general statement it is a case of.

SCOPE: this REMOVES THE OBSTRUCTION, it does not prove order-sensitivity.
Non-multiplicativity permits a functional to see order; it does not force it.
That level 2 actually separates two same-multiset words stays a measurement
(#7176), not a corollary.

**2. Level-1 order-blindness is now a statement about a NON-canonical
functional — and that is its value.** monoidHom_order_blind and its difference
form explain why the augmentation route looked deceptively insensitive to
modelling choices: all sixteen readings of the properties blocks' recipe share
ONE level-1 number. So agreement there was never evidence about the element.
Under the ruling that insensitivity is gone.

**3. The Option E target is now ONE-SIDED, and aimable.** With eps pinned there
is no second admissible endpoint to run to. Every candidate the corpus has built
UNDERSHOOTS at level 2, so a closing element needs a strictly LARGER |tr_{z_D}|:

    nuc11 gen-grouped   -15.4514 %   x 1.182752
    nuc11 interleaved   -17.4959 %   x 1.212061
    nuc9                -30.9364 %   x 1.447941
    Delta_S             -43.1572 %   x 1.759237

Read from the committed witness on main (qbeta-option-e-required-level), not
from memory. Arithmetic on measured residuals, NOT theorems, and deliberately
not dressed as theorems in the Lean.

**Status stays todo**, for two reasons and not one: (iii) the dashboard
re-score is still outstanding, AND the element half of this bean is open. Per
§13a a bean whose subject includes an open question does not close because one
half of it was answered.


## 2026-09-12 — the ORDER lever, measured exhaustively: WIDE BUT COARSE

`computations/qbeta/qbeta_option_e_order_dof_range_probe.py` (8/8), witness
`qbeta-option-e-order-dof-range`. Scope-(a). Names no ordering.

WHY THE QUESTION EXISTS AT ALL, AND ONLY SINCE THE RULING. Level 2 is not
multiplicative (proved, #7188), so unlike the augmentation it CAN see the order
of the letters in a braid word. Braid order became a live degree of freedom for
the observable on the day of the z_D ruling. Under the augmentation it was
provably invisible, so it never needed deriving.

MEASURED, exhaustively over both nucleon multisets — 6930 neutron orderings and
9240 proton, 64,033,200 pairs (tr is linear on the NF vector, so the words
enumerate separately rather than as pairs):

    tr_{z_D}(Delta) reachable   [-0.7795980, +0.5476330]   span 1.3272311
    target                      +-0.1868937
    span / target               7.1015x
    pairs within 1 sigma (780 ppb)              0  of 64,033,200
    NEAREST approach                2.7232758e-5  = 0.014571 % of target
                                                  = 186.88x the window
    the canonical gen-grouped neutron ordering ranks 6667 of 6930

🛑 I WAS WRONG TWICE AND BOTH GUESSES ARE RECORDED BECAUSE THE SHAPE MATTERS.
First I wrote the probe to show order was TOO SMALL a lever, on the strength of
the single order pair the corpus had measured (interleaved -17.496 % vs
gen-grouped -15.451 %, a 2.04-point move). Wrong by two orders of magnitude —
the span is 7.1x the target. Then I expected it to be so free as to be
UNFALSIFIABLE. Also wrong: zero of 64 million pairs land in the window.

THE ACTUAL SHAPE IS WIDE BUT COARSE, and that is the good outcome: reordering
CANNOT manufacture agreement with Q_beta, so an ordering claim here would be
falsifiable rather than fitted.

🛑 LIVE FIT HAZARD, and it is the sharpest thing in this entry. "Order cannot
manufacture agreement" is true against the EXPERIMENTAL WINDOW and badly
misleading as a summary: some ordering reaches 0.0146 % of the target against
the canonical ordering's -15.45 %. Anyone exhibiting it would be quoting a
result an order of magnitude better than the retired published 0.17 %, and it
would be PURE SELECTION — no continuous parameter tuned, an object chosen
because it reproduces the measured value, exactly what NO FITTING names. What
makes it refutable rather than unfalsifiable is only that it misses the window
by 187x. The probe deliberately does not name it, and neither does this bean.

CONSEQUENCE FOR OPTION E. Order is priced and it is not the lever: it cannot
reach Q_beta from these multisets. The freedom is in the MULTISET, which is
where augmentation_difference_order_blind already said it had to be — changing
the multiset is the only thing that moves level 1, and it moves level 2 too.

SCOPE: measured on THESE two multisets. It prices the order lever; it does not
exclude Option E.


## 2026-09-12 — item (iii) is PRICED. It degrades three rows by ~5–7 orders, and that is the ruling working as designed.

Consequence (iii) of the 2026-09-08 ruling — re-score the L2 dashboard rows
`Q_β` / `m_n` / `Δ_pn` on the ruled base — has been declined twice as
ask-before-change, which is correct: it moves the L2 headline, so it is neither
a precision increase nor corpus-derived. But it was declined **without the
numbers**, i.e. the owner was being asked to authorise a change whose size
nobody had measured. Measured now, changing nothing:
[`qbeta_zd_rescore_price_probe.py`](computations/qbeta/qbeta_zd_rescore_price_probe.py)
(6/6), witness `qbeta-zd-rescore-price.witness.json`.

**Calibration first, because the numbers are worthless without it.** The probe
reproduces the dashboard's CURRENT `m_n` and `Δ_pn` rows from its CURRENT
`Q_β` row through the producer's own relation
`m_n = m_p(substrate) + Q_β + m_e`: predicted 0.895408 / 650.486 ppb against
the committed 0.9029 / 658.0 ppb — **ratios 0.9917 / 0.9886**. So the dependent
rows ARE a plain function of the scored `Q_β`, and the re-score below is the
row, not a sketch.

| cell | `Q_β` ppb | `m_n` ppb | `Δ_pn` ppb |
|---|---|---|---|
| `z = 1` (published, **inadmissible**) | 1 678 440.4 | 1 397.3915 | 1 015 161.0 |
| **`z_D` (RULED)** | **4.3157176e+8** | **359 350.35** | **2.6105673e+8** |
| `z = q` (augmentation) | 1.2470029e+8 | 103 832.09 | 75 430 750.0 |

**The ruled cell is the worse admissible one — 3.4609× farther from CODATA than
the augmentation.** That is not an argument against the ruling; it is the
anti-fit directive visible in the numbers. Ranking these cells by residual is
exactly the selection-against-the-target the directive forbids, and the ruling
turned on what `ε` *means* under D7, not on which column is smaller.

**🛑 THE LOAD-BEARING CAVEAT: these are BASE figures, zero `c_k` rungs.** No
ladder exists on an admissible base (`qou-cds1`, blocked on the phase
`qou-pdix`). On the `z = 1` base the five rungs bought 1 677 569 → 37.7 ppb —
about 4.5 orders — so a `z_D` ladder could move these a long way. **Do not
quote the `z_D` column as "convention D's accuracy"**; that is the same
mislabelling this bean already had to retract once.

**Producer staleness found, reported not fixed.**
[`per_observable_100x_status.py`](computations/per_observable_100x_status.py)
still says *"Which functional to adopt is an open owner decision (bean
qou-99qc)"* — ruled four days ago — and its emitted
`best_admissible_err_pct` names **`z=q (augmentation)`** as the best admissible
cell. The second is the sharper one: a reader of that witness field takes the
augmentation for the adopted functional, and the ruling chose `z_D`. Both are
one edit away, and both change an emitted witness field, so they go to the
owner with (iii) rather than under exemption 2.

**Correction to my own earlier count in this bean's arc:** I reported this probe
as "8/8 checks". The total was a hardcoded `5 + 3`; there are **six**
`check()` calls. It is now derived from the recorded list, and the six verdicts
are carried in the witness as assertions (it previously emitted **0
assertions** for a probe whose entire content is checks).

**Status stays `todo`** per §13a — the element half (Option E / the phase
`qou-pdix`) is an open question, and (iii) is now waiting on the owner rather
than on a measurement.


## 2026-09-12 (same day, later) — item (iii) is DONE. The owner authorised the re-score; the three rows are on the ruled z_D base.

Put to the owner with the prices above. Answer: **both** "re-score now to z_D"
**and** "re-score after qou-pdix" — read as *move now, and move again once a
ladder exists*. First half landed (PR #7221, `606e7e304b1`); second half is bean
**`qou-iagg`**, blocked on `qou-pdix` → `qou-cds1`.

| row | before (`z = 1`, laddered) | after (`z_D` base) | miss factor |
|---|---|---|---|
| `Q_β` | 1279 ppb | **4.316e+8 ppb** | 5.535e+7 |
| `m_n` | 0.9029 ppb | **3.594e+5 ppb** | 7.034e+7 |
| `Δ_pn` | 658.0 ppb | **2.611e+8 ppb** | 6.021e+7 |

Landed figures match the prices to <1e-3 relative; the probe's new CHECK 6
asserts it against the live witness, so a future drift is caught rather than
assumed. **The L2 headline is unchanged at 1/6 scoreable** — all three already
failed, so this degrades three misses without moving the count.

**Derived from q₀, not inverted from CODATA.** `_qbeta_ruled_base()` evaluates
`|tr_M(Δ_S)(z_D)|·E₀` with `tr_M(Δ_S)(z) = q²/2 − qz − 1 + z/q + 1/(2q²)` and
`E₀ = m_e/(q(q−1))`, then calibrates against this bean's own probe witness
(`−43.157175 %`, agreement 2.9e-7). Reading that recorded residual and
inverting it would have been arithmetically exact and circular — the row's
residual would have been a pass-through of a number computed against CODATA.
If the calibration fails, the producer publishes the **old** row and says so.

**Question 2 answered too: fix both, renaming the field.**
`best_admissible_err_pct` → **`ruled_cell_err_pct`**, repointed from the
augmentation to `z_D`, and the "open owner decision" prose is gone from the
producer (0 occurrences). The rename was the owner's pick for a reason worth
recording: the old name carried *two* defects, not one — it named a functional
the ruling did not choose, **and** "best" ranked the admissible cells **by
residual**, which is the selection-against-the-target the anti-fit directive
forbids. Both cells stay visible in `err_pct_by_functional`.

**🛑 Still a base, zero rungs.** Every affected row now carries that scope in
its own `note` rather than cross-referenced from the `Q_β` row — the
"fixed in one place, survives in the others" failure this corpus keeps
recording. Do not quote these as convention D's accuracy.

**Correction to my own verification claim, and it reached the PR body.** I
reported the first `precision-gates.sh --changed` run as **exit 0**. It was
not: that run was piped through `tail`, so the 0 was `tail`'s status. Re-run
un-piped it is **exit 1** — but the reds are pre-existing, not mine: the `RED:`
line is byte-identical before and after the producer change, both ratchets
report `NEW dirty 0 / REGRESSED 0`, none of the gate's NEW items names either
of my files, and `main` is independently recorded red on the ratchet (#7161
open). PR body corrected.

**Status stays `todo`** per §13a — the element half (Option E) and the phase
(`qou-pdix`) are open questions. What has closed is item (iii).


## 2026-09-12 — 🛑 CORRECTION to my own re-score entry above, plus the anatomy of the 257x and three undone migrations

**The entry above quoted "1279 ppb → 4.316e+8 ppb" as the re-score's effect. That
comparison is the one the corpus forbids, and I made it.** 1279 ppb is
**post-ladder** on `z = 1`; 4.316e+8 ppb is a **base**. The apparent 337,429× is
two factors:

| factor | what it is |
|---|---|
| **1312×** | the **missing `c_k` ladder** (`z=1` base 1 678 440 ppb → `z=1` published 1279 ppb) |
| **257×** | the **functional** (`z=1` base → `z_D` base) |

So **most of the degradation is "no ladder yet"** (`qou-cds1` / `qou-pdix`), not
convention D. **Base to base, D costs 257×. Never quote the 337,429×.**

**Why the gap is structural, not a botched substitution.** `tr^z(Δ_S)` rewrites
exactly as `h²/2 − z·h` with `h = q − 1/q` (verified to 1e-60 against the
2026-08-29 affine form). The `z` term dominates by **5.86×**, so `Q_β` is nearly
*proportional* to `z`. Inverting for CODATA gives **`z* = 0.99850`** — **0.15 %
from the inadmissible `z = 1`**, while `z = q` is +11.17 % and `z_D` is −38.64 %
away. **The published 0.168 % was reachable only at `z ≈ 1`, the coordinate sum.**
It was a property of an inadmissible functional, not of the framework. Scope-(a):
this excludes `Δ_S` *paired with an admissible functional*, not convention D.

**The missing-normalisation hypothesis is REFUTED** — `Σ_λ y_λ f^λ = 1.0` exactly
under D at n = 3, 6, 9, 12 (worst |·−1| < 1e-50). It is the first thing a next
agent will reach for; do not spend a session on it.

**Three migrations the ruling did not get** — new beans, all directions recorded:

- **`qou-wfvl` (high)** — the **element** is census-derived (`Δ_S`, short NF) while
  the owner's γγ ruling the same day forbids census selection. The γγ-selected
  nucleon word gives **−17.496 %**, 2.5× closer *and* derived (PR #7212).
  **Owner decision; subsumes the accuracy question.**
- **`qou-46ys` (high)** — the **binding/mass channel is still convention C**, by
  its own source comments (`gap_a3_overshoot_robustness_check.py:52-67`). And it
  is the most exposed channel: `z` *is* the `y_λ`, binding is the same Frobenius
  pairing, and D's two-row truncation keeps **7 of 77 blocks at A=4** (0.043 % of
  the dimension). Nobody owned this.
- **`qou-y3bm`** — `E₀` had two live forms (+0.9915 %); **unified 2026-09-12 on
  owner instruction** in `qbeta_e0.py`, tower-summed canonical. The tower
  **series** is assumed, not derived — canonical by ruling, open by proof.

Probe: `qbeta_zd_gap_anatomy_probe.py` (9/9). Audit:
`docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md`.
**Status stays `todo`** (§13a).
## 2026-09-12 — BOTH routes to Delta are now priced, and both are negative

PR #7212. The owner's word-selection ruling (2026-09-08, qou-ales) applied to
the DECAY channel for the first time — #7192 applied it to mass/binding.

PROVED (sorry-free, QOU/QBeta/GammaGammaSelectedDeltaVanishes.lean, lean-direct
exit 0 first attempt): a functional multiplicative over concatenation and equal
to 1 on a pair-production vertex is 1 on EVERY γγ-word, hence annihilates every
γγ DIFFERENCE. Both one-dimensional blocks of H_3 are of that shape. Therefore:

  * LEVEL 1 gives EXACTLY ZERO — the augmentation's support is the (3) block
    alone, so a γγ-selected Delta predicts Q_beta = 0 identically, for every
    pair of words, with no computation to do.
  * LEVEL 2, the ruled functional, is carried ENTIRELY by the (2,1) block, which
    is what makes the scan one-dimensional and finite.

MEASURED (5/5), V^k with k <= 5 from the 11-crossing budget, 36 pairs:

  level 1, max over all 36 pairs   1.34e-51        (the proof, confirmed)
  reachable below target           7 values, all <= 0.0985019929
  reachable above target           8 values, all >= 0.6841593612
  the GAP                          0.5856573683 = 3.13364x the target
  Q_beta target                    0.1868936677    -- INSIDE the gap
  nearest reachable                47.295168 % away

The γγ sector does not merely miss; it CANNOT COME CLOSE. Structural.

THE TWO ROUTES, SIDE BY SIDE:

  re-read the existing recipe (#7188)   0 of 37,459,422,000 configurations
  the ruled γγ selection (#7212)        target in a 3.13x gap, nearest 47.3 %

Neither reaches Q_beta. The live conclusion is that Delta needs the FLAVOUR
LETTERS: γγ-words carry no flavour index at all (the corpus's Crossing is
(gen, pos) and nothing else), so a flavour-blind principle cannot distinguish a
proton word from a neutron word. That is the open point GammaGammaSelectorH3
names for itself.

SCOPE-(a) on both: #7188 prices the freedom the SOURCE BLOCKS declare; #7212
prices the ruled principle APPLIED ALONE. Neither refutes the ruling, and an
element combining γγ selection WITH flavour letters is outside both.

Bean stays todo. The element question is SHARPER, not closed — two routes
priced, both negative, and what is missing is now named.



## 2026-09-12 CORRECTION — 'Delta differs in one letter' was WRONG; it retypes TWO

PR #7212, commit c2b8c7e8c0. This retracts a claim I made the same day, which
reached that PR's TITLE, its BODY, a Lean docstring and a comment on the PR.

THE CLAIM: the nucleon words 'differ in exactly one letter: a single sigma
becomes a single sigma^-1'. Wrong at the LETTER level. The corpus's own data,
_GEN_CHAINS in qbeta_delta_candidate_census_probe.py:

  p : gen0 [0,0,0,   0,-1/2,0,0]   gen1 [-1,-1,-1,-1/2]
  n : gen0 [0,0,0,-1/2,-1/2,0,0]   gen1 [-1,-1,-1,  -1]

TWO slots differ, gen0[3] and gen1[3], each by exactly -1/2.

WHAT WAS AND WAS NOT WRONG. The COUNTS are correct and unchanged: proton
(1,2,0), neutron (0,2,1), and the Lean theorem about them stands. The READING
was wrong. Beta-decay flips ONE quark, and each quark sits in TWO of a
nucleon's three pair-crossings, so one uu becomes ud and one ud becomes dd:

  (u1,u2)  uu -> ud     retyped
  (u2,d3)  ud -> dd     retyped
  (u1,d3)  ud -> ud     untouched

The preserved ud count is a CANCELLATION -- one gained against one lost -- not
evidence the mixed crossings are untouched. (1,2,0) -> (0,2,1) is consistent
with a single uu |-> dd substitution AND with the flip that actually happens,
and only the second is a possible decay. I read the weaker hypothesis off the
counts without checking it against the chains. The misleading theorem name
nucleon_difference_is_one_letter is renamed
nucleon_pairCounts_differ_by_one_uu_and_one_dd; the statement is unchanged.

WHAT THE CORRECTION BOUGHT, which is worth more than the retraction cost. Both
retyped letters pick up the SAME central scalar s = -h/2, so Delta expands
EXACTLY:

  Delta = s*(S_A + S_B) + s^2*S_AB

with S_A, S_B the proton word with ONE flavour crossing SMOOTHED (10 crossings)
and S_AB with BOTH (9). Measured, 60 dps, proton pin, convention D:

  direct tr(Delta) vs expansion     agree to 7.8e-62
  s = -h/2                          -0.1045301493978196577
  tr(S_A) / tr(S_B) / tr(S_AB)      1.271097000 / 0.272140496 / 0.301910575
  s^2 term / s term                 2.045 %
  crossings                         11 -> 10 -> 9
  residual                          -15.451387 %  -- UNCHANGED

THE OLD READING IS REFUTED NUMERICALLY, not merely withdrawn: under it Delta
would be -h times ONE smoothed word, and both candidates sit 68.2 % and 64.0 %
from Delta. CHECK 4 of the probe.

ALSO: the typing table is ONE scalar, not three conventions. sigma - h =
sigma^-1 follows straight from the Hecke relation (skein_letter_inv), so the dd
letter IS the inverse crossing and the ud letter is exactly (sigma+sigma^-1)/2
(ud_letter_is_average). Both sorry-free.

LEAN, all sorry-free, lean-direct -DautoImplicit=false -s 65536 exit 0:
  flip_retypes_pairs                general form, any (m+1 ups, n downs)
  nucleon_flip_retypes_two_of_three the proton case: 2 of 3
  two_shift_expansion               the element identity, over a NONCOMMUTATIVE
                                    ring with centrality of s explicit -- a
                                    CommRing proof would be unsound for the
                                    braid algebra
  skein_letter_inv                  needs only the Hecke relation
  ud_letter_is_average              needs (2:R) != 0, stated explicitly
  succChooseTwo                     C(m+1,2) = C(m,2) + m
#print axioms: no sorryAx anywhere; two_shift_expansion needs only [propext].

WHAT DOES NOT MOVE. No number: this is an exact rewriting of the same element,
so the residual and everything downstream are identical. The 3.13x gap result
of #7212 Part 1 is untouched -- it prices the whole reachable set and never
used the letter count.

WHAT IT CHANGES FOR THIS BEAN. Delta's FORM inside this construction is now
known exactly: a fixed rational combination of 10- and 9-crossing traces rather
than an opaque 11-crossing difference, and |s| ~ 0.1045 is the quantitative
reason the two nucleon traces sit so close together. Whether those lower-
crossing words are more tractable, or coincide with words the mass channel
already computes, is NOT claimed and is the live question.

BEAN STAYS todo. The epsilon/Delta fork is an open conjecture; per AGENTS.md
13a a bean whose subject is an open conjecture is not closed because the
recording of its openness is done.

SCOPE-(a): two_shift_expansion holds for ANY two slots carrying a common
central shift; that the nucleon words are in that shape is read off _GEN_CHAINS
and re-verified numerically, not proved.



## 2026-09-12 DERIVATION — the gg ruling DECIDES the braid ordering, and picks the WORSE one

PR #7212, commit 3a76d49fc9. This CLOSES the ordering question #7188 raised.

WHAT #7188 LEFT OPEN, in its own words: "the corpus now owes a DERIVATION of
the braid ordering of the nucleon word. Until it has one, tr_{z_D}(Delta) is
not predicted by the framework -- it is selected by an unstated modelling
choice." The owner's gamma-gamma ruling (2026-09-08, qou-ales) supplies it.

THE ARGUMENT, STRUCTURAL NOT NUMERICAL. The census carries two orderings of the
SAME eleven-letter multiset (verified: identical Counter for both nucleons).
Their confinement cores are:

  interleaved  nuc9:        for _ in range(3): sigma_0 ; (sigma_1 - h)
  gen-grouped  _GEN_CHAINS: all sigma_0 letters first, then all sigma_1

sigma_1 - h = sigma_1^-1 by the Hecke relation (skein_letter_inv, proved on
this branch), so the interleaved core is (sigma_0 sigma_1^-1)^3 = `vertex 0`
three times -- a GAMMA-GAMMA WORD. The gen-grouped core has a POSITIVE crossing
in SECOND position, and a gg-word's second letter is always negative. So of the
two models exactly one is gg-produced and the ruling selects it. Scope-(b): it
cites a proved invariant, not a bad number.

LEAN, all five depend on NO AXIOMS AT ALL (lean-direct exit 0):
  gammaGamma_snd_neg             a gg-word's second letter is negative
  not_gammaGamma_of_snd_pos      hence a positive 2nd letter excludes it
  interleavedCore_isGammaGamma   three applications of the constructor
  not_gammaGamma_genGroupedCore  the exclusion
  cores_ne                       the two cores are different words

The linter earned its keep: the exclusion lemma was first stated with BOTH of
the first two letters positive as hypotheses and the first is never used, so it
was restated STRONGER (the first letter's sign is irrelevant) and renamed.

🛑 THE RULED ORDER IS THE LESS ACCURATE ONE, and that is the correct outcome.
Proton pin, convention D, 60 dps:

  interleaved (RULED)   -17.495929 %      <- reproduces #7188's documented -17.496
  gen-grouped (unruled) -15.451387 %      <- the merged Option-E witness
  cost of the ruling      2.04454 points

Under AGENTS.md NO FITTING, "rank by derivational cleanliness first, treat
accuracy as a diagnostic, never as a tie-breaker that promotes a fitted route."
Preferring -15.45 % BECAUSE it is closer is selection against the target. Do
not revert this.

CONSEQUENCE FOR THIS BEAN. The -15.4514 % that #7188 and #7212 calibrate
against is the GEN-GROUPED, i.e. UNRULED, order. Nothing there is retracted --
both state their ordering -- but the CANONICAL residual under the ruling is
-17.4959 %, and the witness qbeta-gamma-gamma-ruling-selects-ordering is the
record of which figure is which.

WHAT SURVIVES THE ORDER CHANGE, checked rather than assumed:
  * the two-letter flip is ORDER-INDEPENDENT: two slots, each -h/2, in both
    orderings (expected for a flavour statement, but measured);
  * the three-term skein expansion is EXACT on the ruled order too, 3.9e-62 at
    60 dps -- only the term sizes move, s^2/s going 2.045 % -> 4.874 %;
  * the 3.13x gap of #7212 Part 1 is UNTOUCHED: it prices V^k differences, a
    gg-only construction carrying no nucleon ordering at all.

CROSS-CHECK WORTH NOTING, two independent routes to the same k. The sibling's
Frobenius-positivity selection (owner ruling 2026-09-12, reading 3) picks
k = 3 = beta_Bor on #7207. The census's confinement core is independently V^3.
Same k, from two different principles -- recorded as a coincidence of two
derivations, NOT offered as evidence for either.

🛑 TRAP, recorded in the probe. "Interleaved" reconstructed by ZIPPING the two
_GEN_CHAINS lists alternately gives -13.5712 %, which is NEITHER census model
-- a third ordering, invented, and plausible-looking. I produced it before
reading nuc9. The census's interleaved model emits the core as three
(sigma_0, sigma_1^-1) PAIRS, then an ORDERED quark block, then two gluon
letters. Reproducing the documented -17.496 % is the calibration that catches a
lookalike reconstruction; CHECK 3 asserts it.

BEAN STAYS todo. The epsilon/Delta fork is an open conjecture (§13a). What is
closed is the ORDERING sub-question, which is a genuine narrowing: the order is
no longer a free modelling choice. The residual did not improve and was not
expected to.

STILL OPEN: the ruling constrains the CORE. The flavour letters are determined
(this branch) but their PLACEMENT, and the two gluon letters, are not gg-words
and are not settled by the ruling. That is the remaining freedom.



## 2026-09-12 PARITY BOUND — the ruling reaches 6 of 11 letters, provably

PR #7212, commit 49bae3625e. Companion to the ordering derivation above: that
one settles the CORE, this settles how much the gg principle can settle AT ALL.

Every pair-production vertex contributes exactly TWO letters, so a gg-word has
EVEN length. The nucleon crossing budget is 11 (qou-1qsw), which is ODD.
Therefore NO 11-crossing word is gg-produced -- not this one, not any
reordering of it, not any other candidate at that budget. At least one letter
necessarily lies outside the principle's reach, and that is a fact about the
budget, not a shortfall in the construction.

Block decomposition of the census word:

  core (sigma_0 sigma_1^-1)^3    6 letters   gg-produced (constructor x3)
  quark                          3 letters   NOT -- odd length
  gluon sigma_0 sigma_0          2 letters   NOT -- 2nd letter positive
                                ----
                                11 = the budget

So the ruling reaches 6 of 11; the other 5 are the freedom that survives it.
The gluon pair is excluded twice over -- directly by the vertex sign pattern,
and by following an odd-length block.

LEAN (lean-direct exit 0, no sorryAx):
  gammaGamma_length_even        2 | w.length for any gg-word
  not_gammaGamma_of_odd_length  the contrapositive
  eleven_not_gammaGamma         no 11-crossing word is gg-produced
  gluonPair_not_gammaGamma      NO AXIOMS AT ALL
  three_not_gammaGamma          the quark block's length is odd

Scope-(b) throughout: every exclusion cites a proved invariant (vertex length,
or the vertex sign pattern), never a measured miss.

🛑 THIS IS A LIMIT ON THE RULING, NOT A DEFECT IN IT, and not the construction
failing to apply it. The principle does what it can; what it cannot do is fix
an odd number of letters out of even-length building blocks.

WHY IT MATTERS FOR THIS BEAN. It converts "the flavour placement and gluon
letters are still open" from an observation into a THEOREM about where the
remaining freedom lives: exactly 5 letters, and no amount of gg reasoning will
reduce that number. Any closing Delta has to come from those 5 or from a
different principle. That is a much sharper statement of the open problem than
the bean carried before.

Probe 12/12 (CHECK 6 added to qbeta_gamma_gamma_ruling_selects_ordering_probe).

BEAN STAYS todo (§13a).



## 2026-09-12 — the SDP half applied, and the scope question ANSWERED (A, core only)

PR #7212, commit 426af792b8 + follow-up. The gamma-gamma half was applied above
(ordering 3a76d49fc9, parity bound 49bae3625e). This is the SDP half.

METHOD, needing no new machinery. chi_(3) is the 1-dim character sigma -> q, so
a letter (sigma_g + dc*h) has value q + dc*h and chi_(3)(w) = prod(q + dc_i*h)
-- multiplicative and GENERATOR-INDEPENDENT. From
tr_{z_D} = y_(3) chi_(3) + y_(2,1) chi_(2,1) at level 2 (y_(1^3) = 0),
chi_(2,1) = (tr - y_(3) chi_(3)) / y_(2,1). Calibrated three ways before use:
chi_(2,1)(1) = 2 exactly (block dimension), chi_(3)(V^k) = 1 exactly for all k
(reproducing the sorry-free unit_on_vertices_eq_one from the OPPOSITE
direction), y_(3) + 2 y_(2,1) = 1.

RESULT 1 -- the (3) block is STRUCTURALLY SILENT. chi_(3) depends only on the
shift multiset, and flavour determines the shifts (pairCounts_determined), so
it is one positive number per nucleon (1.3825 p / 1.1221 n) across all 32
generator assignments, spread exactly 0. The whole content of reading 3 here is
chi_(2,1) >= 0.

RESULT 2 -- it NARROWS AND DOES NOT CLOSE. 20/32 proton and 16/32 neutron
assignments survive: 320 admissible Delta pairs of 1024, a 3.2x narrowing. The
target (0 %) is INSIDE the admissible range [-98.57 %, +35.17 %], and the
nearest admissible pair misses the ~780 ppb window by 122573x. Falsifiable and
currently failing -- the same shape as #7188's ordering result, NOT a rescue.

RESULT 3 -- THE SCOPE FORK, now answered. Reading 3 applied to the gg-selected
CORE admits V^3 (chi_(2,1) = +1.9942) and selects k = 3 = beta_Bor. Applied to
the WHOLE 11-crossing word it EXCLUDES the census assignment (chi_(2,1) =
-0.2806 proton, -0.3720 neutron) -- which would make every residual on this
bean inadmissible. Both fit the ruling as relayed.

ANSWER, recorded verbatim: **"test,A — core only (Recommended)"** -- option (A)
plus a free-text token `test`. Recorded as SELECTED, not as a clean ruling: that
token reads as much like exercising the question UI as like a directive, and an
ambiguous answer should not be laundered into an owner ruling in a bean that
later agents read as authority.

Acting on it is safe either way because (A) IS THE STATUS QUO -- the sibling
applied it on #7207 (frobeniusSelected_borromean), and adopting it moves no
number and re-runs no producer. If the intent was otherwise, nothing has to be
undone; only this paragraph is wrong.

CONSEQUENCE UNDER (A). The census element stands, and so does every residual on
this bean. Reading 3 constrains 6 of the word's 11 letters and prunes NOTHING
among the 5 the parity bound leaves free -- so the SDP half does no work on the
open part of the problem, and the 5 letters still have no derived constraint.
That is the live gap.

BEAN STAYS todo (§13a).

## 2026-09-12 — the element migration LANDED on main, and `element_is_ruled: true` over-reaches by 5 letters

**Not a numerical dispute. The migration is right, the number is right, and my own
work is what supports it.** What is wrong is one provenance field, and it is the
field an owner reads.

**What landed.** `573b2ece24` moved the scored `Q_β` element from `delta_S` (short
normal form) to `nuc11_interleaved`, and `b021216ab6` closed `qou-wfvl` as
`completed`. The row improved 2.55× (4.259e+8 → 1.668e+8 ppb). The producer writes

    "element_is_ruled": true,
    "element_authority": "owner gamma-gamma ruling qou-ales 2026-09-08 +
       GammaGammaWordSelection.vertex on main (a gamma-gamma word's 2nd letter is
       negative, which excludes the gen-grouped core)"

and it calibrates at `err_pct_at_order_zero_E0 = -17.4959286063` against my
`-17.495929`. Their `delta_S` `tr_conv_D = -0.106235639848` reproduces mine to ten
digits. The exclusion argument they cite **is** my Lean lemma
`not_gammaGamma_of_snd_pos`. None of that is in question.

**The over-claim, measured.** `nuc11_interleaved` is **11 letters** — read off
`_GEN_CHAINS`, `gen0 = 7`, `gen1 = 4`, for both `p` and `n`. Every γγ word has
**even** length: a γγ word is a concatenation of 2-letter vertices
(`gammaGamma_length_even`, sorry-free). 11 is odd. **Therefore
`nuc11_interleaved` is not a γγ word** — `eleven_not_gammaGamma`, sorry-free, on
this branch.

So the ruling does not select the element. It selects the **6-letter core**
`(σ₀σ₁⁻¹)³` = three γγ vertices, and provably cannot reach the other five:

| block | letters | γγ-reachable? |
|---|---|---|
| core | 6 | **yes** — three vertices |
| quark | 3 | no — odd (`three_not_gammaGamma`) |
| gluon | 2 | no — even, but both positive (`gluonPair_not_gammaGamma`) |

The gluon pair is excluded **twice over**: its second letter is positive, and it
follows an odd-length block so no vertex boundary can align with it.

**Why this matters rather than being pedantry.** `qou-ales` says *"Shouldn't use
census."* The element now scored is **6/11 γγ-derived and 5/11 census-derived**.
`qou-wfvl` — whose title is *"the Q_β element is census-derived"* — is therefore
closed on an element that is still census-derived in 5 of its 11 letters. The
migration is 6/11 done, not done.

**What the correct label would say.** The binary field cannot express this. Either
`element_is_ruled` becomes scoped (`"core"`), or it keeps `true` alongside
`element_ruled_letters: 6` / `element_census_letters: 5`. **My judgement, marked as
judgement:** the second — keep the boolean for consumers, add the two counts, and
open a successor bean for the 5 free letters, because that is where a closing `Δ`
would have to come from and it is now the only place left.

**I have not changed it.** It is a sibling's producer and an owner-facing
provenance label; §"ASK THE OWNER BEFORE CHANGING THINGS" covers it and it is
neither a precision increase nor corpus-derived (the corpus currently *asserts*
`true`). Recorded here; surfaced to the owner.

**Second item, smaller.** `173da443b6` made the tower-summed `E₀` canonical. This
probe and `qbeta_option_e_order_dof_range_probe` still inherit the **order-zero**
form, so every percentage on this bean is on the retired base, low by 0.9915 %. On
the canonical base: interleaved `-16.677940 %`, gen-grouped `-14.613128 %`. CHECK 7
reports both and does not switch, because the cells these are calibrated against
were computed at order-zero and mixing bases is the silent-revert trap that
commit's own audit records at §6. **The ranking is invariant** — residual is
strictly increasing in `E₀`, and `E₀ > 0` is common to every candidate — so no
conclusion on this bean depends on the base.



## 2026-09-13 — the element question: ordering is provably not the lever (PR #7295)

The alternating character `sigma_i |-> -1/q` is a 1-dim rep of `H_3(q)`, so a
word's character is a product of SCALARS and depends only on the MULTISET of
its letter shifts. Measured on 3840 (permutation, generator-assignment) pairs:
exactly ONE distinct value. Lean `wordChar_of_perm` (sorry-free).

Consequence for this bean's element half. R2 of the gamma-gamma ruling
(`qou-ales`, #7212) picked the nucleon ORDERING. **An ordering choice cannot
make a word gamma-gamma-produced** — the invariant that `altChar_eq_one` pins
at +1 cannot see one. So the 5 census-derived letters of `nuc11_interleaved`
are not repairable by re-ordering or by re-assigning generators; a
gamma-gamma-derived replacement has to change WHICH letters are present.

Closed form over the three-shift alphabet the census uses, with a/b/c counting
the shifts 0 / -h / -h/2:

    altChar(w) = (-1)^(a+b+c) q^(b-a-c) ((q^2+1)/2)^c  = 1  <=>  c = 0 and a = b

Every corpus nucleon carries c = 2, and `-h/2` — the mixed ud crossing — is
BOTH the unique bar-fixed shift (#7283) and the unique shift whose character
pairs with nothing to give 1. One letter, two independent obstructions;
`qou-e58e` measured that bar IS p<->n conjugation, so that is not a notational
coincidence.

Coverage, stated honestly: FIVE of the census's six Delta families —
four at word level (`nuc9`, `nuc11_interleaved`, `nuc11_gen_grouped`, the 16
`blocks CONSTRUCTED` readings = 19 readings = 38 words), one (`delta_S`, the
short model) only at the Delta level because it is given as an NF vector and has
no shift multiset. `blocks AS STATED` is NOT covered — nothing constructs it.

NOT NEW: `qou-avt6` (2026-08-26) already has the monomial shape
`q^m ([2]_q/2)^c`, for the COUNIT rep `sigma |-> q`. This is the ALTERNATING
rep, which is the one the gamma-gamma lemma pins — a different functional, same
shape.

OPEN, spun out as `qou-efqx`: the fourth (`averaged_weighted`, colour-weighted)
template, which R3 makes canonical. Its character carries an irreducible sextic,
so the argument does not extend; only the pin-level pairing fact is measured.

Bean stays `todo` (AGENTS.md §13a — the element is an open conjecture; this
narrows it, it does not close it).



### Same day, the positive half (PR #7295 part 2)

On three strands the gamma-gamma ruling leaves **one integer**. `H_3(q)` has two
Artin generators, so a vertex `sigma_i sigma_{i+1}^-1` needs `i+1 < 2`, i.e.
`i = 0`: every gamma-gamma word is `(sigma_0 sigma_1^-1)^k`. Lean
`gammaGamma_threeStrand`, sorry-free. `k = 3` is `borromean`.

Two structural findings. Every member has a **vanishing `e^-` coordinate**
(symbolic, k = 0..24) — so `qbeta-counit-closed-form.md`'s "which both nucleon
models happen to satisfy" is FORCED under gamma-gamma, not accidental; and
`tr_M|_{z=1} - net = h*nf[e^-]` identically, so net and the retired z=1 cell
COINCIDE on every gamma-gamma word.

**The derived member misses by 440 %.** `|tr_M^{z_D}(core^3)|*E_0 = 4.22140`
MeV against `Q_beta = 0.78233`: **+439.592 %**. That is the honest number for
the route as a single-word Q_beta carrier on three strands.

**And the matching members are selected, measurably.** The k=1 (mod 3) band
descends monotonically THROUGH the target (k=7 gives +0.610 %); the difference
grid over k,l <= 24 is 300 pairs straddling it, local spacing 1.29 %, best
(8,23) at +0.455 % — against **0.322 % expected by chance** from that spacing.
The best match is not even better than chance. Choosing k or (k,l) by residual
is selection against the target and is forbidden.

So the live question is sharper: **either `k` is derived from something other
than the residual, or the gamma-gamma carrier for Q_beta is not a single
three-strand word.** Both open. Scope-(a) — no invariant here forbids the
gamma-gamma route; what is excluded is the METHOD.



### Part 3, same day — the H_3 collapse is an ACCIDENT OF THREE STRANDS (PR #7295)

The three-strand collapse was never about the Hecke algebra. Lean, sorry-free:
`gammaGamma_iff_vertexWord` — the gamma-gamma words are EXACTLY the free monoid
on the vertices; `gammaGamma_index_lt` — on n strands only n-2 vertex indices
exist. ONE at n=3 (hence the cyclic monoid), TWO at n=4.

Measured (general-n T-basis reducer, validated against the corpus's hand-coded
H_3 tables, and independently recovering growth k+1 at n=3):

                      n = 3                 n = 4
  vertices            1                     2
  growth (k <= 8)     k+1 = 1..9            2^(k+1)-1 = 1,3,7,...,511
  span rank           3 of 6                21 of 24

At n=4 EVERY one of the 2^k words of length 2k is a distinct element of H_4 —
the Hecke relations impose no collapse at all — and the span goes from half the
algebra to seven eighths.

**So the +439.592 % H_3 miss must NOT be quoted for H_4.** It is a fact about a
one-integer family. At four strands the family is free and nearly fills the
algebra.

Caveat stated: growth and rank are measured at a generic rational h, so both
are LOWER bounds on the symbolic answer — the safe direction, since reaching
the maximum establishes it exactly. Two generic values agree.

NOT claimed: no four-strand Markov trace is computed, so nothing is said about
whether an H_4 gamma-gamma element reproduces an observable. And which 3 of the
24 dimensions are missing from the span is not measured.



### Part 4, same day — the general-n Ocneanu trace, and the H_4 trace set (PR #7295)

The corpus had NO general-n Markov trace: `pyhecke.gram` carries the H_3 vector
`[1, z, z, z^2, z^2, z(hz+1)]` as a hand-coded literal and nothing generalises
it. Built one from the three defining properties via the S_{n-1}-coset
decomposition, validated three ways — it reproduces the H_3 literal exactly
(symbolic in h AND z), satisfies tr(xy)=tr(yx) on H_4 pairs, and satisfies the
Markov property at n=4 against n=3. The latter two are NOT inputs to the
recursion, so they are real tests; the first `coset_factor` failed them.

Measured, gamma-gamma trace sets at z_D, proton pin, k <= 8 vertices:

                  count    range                    median gap
    n = 3            9     [0.18618696, 1.0]        0.032897756
    n = 4          511     [0.11139758, 1.1374052]  0.0025322918

**13.0x denser**, so the anti-fit conclusion sharpens — selection by residual
was already forbidden at n=3 and at n=4 is not even tempting.

**And barely wider.** 511 distinct elements spanning 21 of 24 dimensions have
traces confined to a band only ~1.3x the n=3 one. The trace is a very LOSSY
functional on the gamma-gamma set: free growth in the algebra does not buy a
wide trace image. That is a constraint in its own right and was invisible
before this.

Scope-(a). NO four-strand Q_beta prediction — E_0 and the
element-to-observable map are H_3 constructions and the corpus does not define
their n=4 analogue. The n=4 set is compared to ITSELF at n=3, structurally.



### Part 5, same day — the SDP half of qou-ales, and it is a REAL selector (PR #7295)

The ruling says selection is via gamma-gamma production AND the confinement SDP.
Parts 1-4 did the gamma-gamma half; this is the SDP half, and it is the first
DERIVED selector on this arc (PSD feasibility is structural, not a residual).

**Three strands: the conjunction is EMPTY.** In the (2,1) block, exactly:
`a = -1/(q(q^2+1))`, `a' = q^3/(q^2+1)` — **a' IS z_D** — and the gamma-gamma
vertex has `det V = 1`, `tr V = -1 - h^2`. So V is an ELLIPTIC SL_2(R) element,
and `V^3 = 1` forces `q = 1`: **the Borromean baryon is SDP-feasible only in the
classical limit.** New Lean `QOU.Mass.PsdDetOneTrace` (sorry-free) proves a real
PSD 2x2 of det 1 has trace >= 2 with equality only at the identity, and measured
`tr(V^k) < 2` for k = 1..200 — so the exclusion is a theorem about the PSD cone,
not arithmetic. This also EXPLAINS the k mod 3 banding of Part 2: a near-order-3
rotation, exactly order 3 only at q = 1, so the bands drift.

**Four strands: NON-empty and very selective — and my first draft was wrong.**
It asserted infeasibility at n=4 too, having tested only the powers of ONE
vertex; over all 2^k words the assertion FAILED. Of **8190** words to 12
vertices, exactly **5** are feasible: `(v0v1)^2`, `(v0v1)^4`, `(v0v1)^6`, and two
sporadic 10-vertex words. `(v0v1)^m` is feasible **iff m is even**.

**The mechanism, not an analogy.** In BOTH 3-dim blocks the spectrum of `v0v1` is
exactly `{-q^2, -q^-2, 1}` — two NEGATIVE eigenvalues — so odd powers cannot be
PSD and even powers have spectrum `{q^-4, 1, q^4}`. Same cause as the H_2 rule
(`sigma_0` has eigenvalue `-1/q`). The 1-dim and (2,2) blocks send every power to
the identity; all discrimination lives in the two 3-dim blocks. And `(v0v1)^2` is
NOT the identity there (max |M-I| = 0.348, 0.518), so its feasibility is genuine
positivity rather than triviality.

So the ruling's two halves are NOT in conflict — they simply have no common
solution on three strands. **Smallest derived candidate: `(v0 v1)^2`, four
vertices, eight letters.**

NOT claimed: the feasible set is not characterised (only enumerated to 12
vertices; the two sporadic words are unexplained); no cost/minimality is
computed, so this NARROWS the candidate set without selecting a word; no
observable is computed.



### Part 6, same day — SDPSelected has a UNIQUE solution (PR #7295)

Part 5 did the feasibility half and said it did not compute minimality. This is
minimality, and it closes the selection.

The cost is the corpus's: `mba-step10-confinement-sdp.md` states
`minimize Sum_i t_i x_i` with `t_i = tr_M(b_i)`, so the objective on a word is
its Markov trace. Evaluated with the general-n Ocneanu recursion from Part 4
(re-verified against pyhecke.gram's H_3 vector so this cannot inherit a silent
breakage).

Costs at z_D, proton pin, over the five PSD-feasible words:

    (v0 v1)^2    (0,1,0,1)                   1.032897755524660383   <- MIN
    sporadic A   (0,0,1,1,0,1,1,0,0,1)       1.073238807935729209
    sporadic B   (0,1,1,0,0,1,0,0,1,1)       1.073238807935729209
    (v0 v1)^4    (0,1,0,1,0,1,0,1)           1.137405209118677445
    (v0 v1)^6    (0,1,0,1,0,1,0,1,0,1,0,1)   1.331992492573499969

The minimum is STRICT and ATTAINED, not merely least-in-a-truncation: cost on
the even alternating family is strictly increasing in m (1.0329 -> 4.0944 for
m = 2..14), so extending the enumeration cannot beat m = 2.

**SDPSelected -> `(v0 v1)^2`: four vertices, eight letters, four strands.**
DERIVED — no continuous parameter tuned, no discrete choice made against a
measured value, no observable entering at any point. This is the arc's first
complete derived selection.

Observation flagged as such: the two sporadic words have EXACTLY equal cost
(< 1e-30) while their `net` differs (1.1426 vs 0.9495), so whatever relates
them does not preserve net. Unexplained; two data points are not a pattern.

TWO GAPS, and the result may not be quoted without them:
1. the LP's `net(x) = n_target` constraint is NOT imposed (it belongs to the
   mixture formulation; net is reported per word so it can be applied later);
2. "unique" means among gamma-gamma words of at most 12 vertices on four
   strands — a cheaper feasible word at 13+ vertices is not excluded, though a
   cheaper ALTERNATING one is, by monotonicity.

NOT DONE, deliberately: no Q_beta comparison. E_0 and the
element-to-observable map are H_3 constructions with no corpus-defined n = 4
analogue, and reporting a residual would re-introduce the
selection-against-the-target the earlier parts measured and rejected. The word
is derived; what it predicts is a separate question.



### 🛑 Part 6 RETRACTED, same day (PR #7295)

Part 6 above claimed SDPSelected has a unique solution, `(v0 v1)^2`. **It does
not, and I withdraw that.**

The EMPTY gamma-gamma word — zero vertices, `GammaGammaWord.nil`, the identity
of `H_n` — is PSD-feasible in every block (the identity matrix is PSD) and its
Markov trace is exactly **1.0**, against 1.032897755524660383 for `(v0 v1)^2`.
So over the candidate set as the Lean states it, **SDPSelected selects the empty
word**, vacuously. Part 6 silently restricted to words with >= 1 vertex.

**The corpus already proved this one level up, and I cited the block without
reading it.** `prop:operator-selection-lp` §"Degeneracy of this program":
`b_1 = 1` so `G_1j = t_j`, hence the first Frobenius positivity constraint IS
the objective bounded below by zero — optimal value identically 0 for every n,
q and trace convention; and the minimiser set is a positive-dimensional
mirror-closed face, so which vertex a solver returns is its pivoting rule. That
block states outright that *"downstream blocks have read the program as a
selection principle, which it is not"*. I became one of those readers before
becoming an independent confirmation of it in the discrete setting.

**WHAT SURVIVES, quote these separately:**
1. **Feasibility does the real work and is untouched** — Part 5's 5-of-8190 at
   n=4, none at n=3. A genuine structural zero-parameter filter.
2. Among **NON-EMPTY** gamma-gamma words of <= 12 vertices on four strands,
   `(v0 v1)^2` is the strict minimiser with the minimum ATTAINED. True about a
   RESTRICTED set; **not** SDPSelected.

So the arc does NOT have a complete derived selection. It has a derived
*filter* (feasibility) and no derived *selector*. The open problem is what
breaks the tie among the 5 — and the corpus's own degeneracy result says the LP
objective cannot be it.


## Part 7 (PR #7304) — crossing energy is the THIRD degenerate functional, and no γγ word binds

`computations/qbeta/qbeta_gamma_gamma_crossing_energy_probe.py` (6/6).

**Calibrated first, by data, not by reading.** `def:crossing-energy` gives the
electron (left trefoil `T_(2,3)`, three POSITIVE crossings) `E_cross = 3q =
3.329935748` against the `~3.330` in `pair-creation-energy.md`, and the positron
(mirror) `-3/q = -2.702754852` against `~-2.703`. A reversed sign convention
would have swapped these, so the orientation is pinned.

**Closed form.** `E_cross(k-vertex γγ word) = k*h` EXACTLY (k = 0..14). A vertex
`σ_i σ_{i+1}^{-1}` is one positive crossing and one negative: `q + (-1/q) = h`.

**Order-blind, again.** 3840 (permutation, index-assignment) pairs of a 5-vertex
word → 1 distinct value. Same blindness as #7295's alternating character, for
the same structural reason (a sum over letters). Second order-blind functional
on this family.

**The substantive finding.** `h > 0` for every `q > 1`, so `E_cross > 0` for
every non-empty γγ word, and `def:crossing-energy` reads positive as *repulsion
dominates*. **NO γγ word is binding-dominated — any number of strands, any
q > 1.** At q_0, `h = 0.20906029879563932`.

**Degenerate again.** `E_cross(empty) = 0`, below all five PSD-feasible words
(0.8362 / 1.6725 / 2.0906 / 2.0906 / 2.5087). So this is the THIRD functional
here whose unconstrained optimum is the trivial answer, after the Markov trace
and the LP objective — the latter proved degenerate by
`prop:operator-selection-lp`'s own "Degeneracy of this program" section.

**It does not separate.** Ordering among non-empty words is by vertex count
alone; the two sporadic 10-vertex words TIE exactly.

**NOT implemented, deliberately:** `knot-operator-selection-proof.md`'s demand
constraint `⟨Φ, dem(K)⟩_F ≥ ‖dem(K)‖_F`, which is the stated reason an
unconstrained minimum need not be the last word. Building `dem(K)` requires
choosing which K the nucleon is, which is the question — implementing it here
would be circular.

Scope-(a): one functional, one family. It does not exclude a binding-dominated
canonical word; it says the γγ construction alone cannot supply one under this
energy.


## Part 8 (PR #7304) — what the ruling PREDICTS for Q_β: +458 % to +620 %, and the 0.11 % near-hit is worse than chance

`computations/qbeta/qbeta_gamma_gamma_qbeta_prediction_probe.py` (7/7).

Nobody had scored the γγ + confinement-SDP admissible set against Q_β. This
does, through the dashboard's own path (`|tr^{z_D}| · E_0`, canonical
tower-summed `E_0`), calibrated first: the census element `nuc11_interleaved`
scores -16.67794 % against the -16.678 % AGENTS.md records.

**All five PSD-feasible words of #7295**, ordered by vertex count, NOT residual:

    (v0 v1)^2     4 vertices   4.36655806955 MeV   +458.1454 %
    (v0 v1)^4     8            4.80836159015       +514.618  %
    sporadic A   10            4.53709919716       +479.9445 %
    sporadic B   10            4.53709919716       +479.9445 %
    (v0 v1)^6    12            5.63097609218       +619.7668 %

**The structural point.** The five agree with EACH OTHER to a factor 1.28957
while missing the measurement by 5.58x to 7.20x. Internal spread < smallest
miss, so **no re-selection inside the admissible set can reach Q_β** — the
choice of word is not the free parameter.

**It is the SDP half that excludes the measured value, not γγ.** Target
`|tr^{z_D}| = 0.185059` sits BELOW 1 = tr(empty word) and below the smallest
feasible trace 1.032898. PSD feasibility pushes the trace up; the target is
under the whole feasible set.

**THE TRAP, disarmed.** Drop the SDP half and the unconstrained family straddles
the target (8190 words, |tr| in [0.003435, 1.331992]) with a best match at
**0.110577 %** — eleven `v_0` and one `v_1`. Worth nothing, and MEASURED to be:
529 distinct trace values, 50 within ±10 % of the target, median spacing
0.000346646 → expected best-by-chance **0.04683 %**, observed **0.110577 %** —
**worse than chance**. Same control and verdict as the H_3 difference-grid check
(0.455 % observed vs 0.322 % expected). The twelve tying words are one
order-blind orbit, none PSD-feasible.

Scope-(a): one functional, one family, n = 4. Says nothing about n > 4, a
different E_0, or a tower correction. The demand constraint is still NOT imposed.


## Part 9 (PR #7304) — the PSD trace FLOOR: scope-(b) exclusion for n ≤ 5, no enumeration

`computations/qbeta/qbeta_gamma_gamma_psd_trace_floor_probe.py` (7/7).

Part 8 left "enumerate the feasible set at n = 5, then n = 6" as next. **That
search is unnecessary at n = 5.** Formalize-first: the invariant prunes the
class before the scan runs.

**Three ingredients, each machine-verified:**

1. **Convention D IS the two-row truncation with strictly positive weights.**
   `y_(n−k,k) = [n−2k+1]_q/[2]_q^n`, and `y = 0` on three rows or more. Checked
   n = 3..8: all 42 partitions with ≥3 rows carry exactly 0; all 21 one- and
   two-row partitions carry `y > 0`.
2. **PSD feasibility ⟹ every character is non-negative.** A PosSemidef matrix
   has non-negative trace, so `χ_λ(w) = Tr(ρ_λ(w)) ≥ 0`.
3. **The trivial block is pinned at exactly 1.** Trivial rep: `σ ↦ q`, so
   `σ⁻¹ = σ − h ↦ q − h = 1/q`, and a γγ vertex ↦ `q·(1/q) = 1`. Measured to
   2.2e-40 on 80 words at n = 3..6. **Counit twin of
   `GammaGammaWordSelection.altChar_eq_one`** (sorry-free, alternating char).

**Hence** in `tr_M = Σ_λ y_λ χ_λ` every term is ≥ 0 and the trivial term is
exactly `y_(n)`:

    tr_M(w)  ≥  y_(n)  =  [n+1]_q / [2]_q^n

for EVERY PSD-feasible γγ word on n strands — no enumeration, word-independent.

**What it excludes.** Target `|tr_M| = 0.185059`. Floor: **0.7527 / 0.5054 /
0.3193 / 0.1943** at n = 2/3/4/5 (all exclude), **0.1153** at n = 6 (does not).
So **no γγ + confinement-SDP word on five strands or fewer can reproduce
Q_β** — scope-(b), invariant named above.

The floor decays like `(q/[2]_q)^n ≈ 0.552^n` against a fixed target, so the
crossing is **one-sided**: the exclusion is a prefix of the strand counts,
never scattered. And it is **loose** where checkable (measured min at n = 4 is
1.0329, 3.2× the floor), which makes the exclusion conservative.

**NOTHING claimed at n ≥ 6**, recorded as a machine assertion rather than a
prose caveat: the floor dropping below the target means the ARGUMENT stops, not
that a feasible word reaches it.

Cross-checked: the Frobenius pairing agrees with the independent Ocneanu
recursion to 5.0e-36 over 28 words at n = 3, 4, 5.

**Lean status: NOT formalised.** Ingredient 3 has a sorry-free alternating
twin; `WedderburnBlocks.PSDFeasible` already carries ingredient 2's hypothesis
shape. The composite bound is the open formalisation.


## Part 10 (PR #7304) — 🛑 tr_M ≥ 1 at EVERY n, which SUPERSEDES part 9's floor

`computations/qbeta/qbeta_gamma_gamma_trace_ge_one_probe.py` (8/8) + Lean
`PsdDetOneTrace.card_le_trace_of_det_one`, `GammaGammaTraceFloor.pairing_ge_one_of_psdFeasible`
(both sorry-free).

**Part 9's floor was mine and it was weak.** It kept the trivial block's term of
the Frobenius pairing and discarded the rest as *merely* non-negative. They are
not merely non-negative — each is bounded below by its own block dimension —
and keeping them gives a bound that is stronger AND n-independent.

**Four ingredients, all measured:**

1. **Every γγ vertex has determinant 1 in every block.** `σᵢ` and `σᵢ₊₁` are
   conjugate in the braid group ⟹ same block determinant ⟹
   `det(σᵢσᵢ₊₁⁻¹) = 1`. Measured 7.2e-40 over 78 (block, vertex) cases at
   n = 3..6; the conjugacy fact itself to 4.9e-40. Multiplicative, so every
   WORD inherits it — 2.1e-39 over 590 (word, block) pairs.
2. **PSD + det 1 ⟹ trace ≥ dim** (AM-GM). Now **general-dimension Lean**
   (`card_le_trace_of_det_one`); #7295 had only the 2×2 case, and blocks reach
   dim 16 at n = 6.
3. **Convention-D weights are non-negative.**
4. **`Σ y_λ dim_λ = 1`** — the Markov normalisation, 4.6e-41 at n = 3..8. This
   is what makes the bound the value **1**.

⟹ **`tr_M(w) ≥ 1` for every PSD-feasible γγ word, at every n.** **TIGHT** —
the empty word is the identity in every block, measured exactly 1.0.

**Consequence.** Target `|tr_M| = 0.185059` is below 1 by a factor **5.4037**,
so the γγ + confinement-SDP route **cannot reach Q_β at ANY strand count**. The
smallest Q_β the family can predict is exactly `E₀ = 4.2274834 MeV` =
**+440.369 %**; the five measured n=4 words land +458 %..+620 %, above that
minimum as they must.

**Part 9 is superseded in strength, not retracted** — its numbers stand, its
scope ("excluded n ≤ 5, open n ≥ 6") was short. Its floor is below 1 at every
n ≥ 2. Kept in the corpus because stopping at the first block is an easy
mistake, and its decay lemma is why the weaker exclusion was one-sided.

**Scope (b), ALL n**, for this functional (`ε` = Markov trace at `z_D`) and this
`E₀` only. Says nothing about another route, a different `E₀`, or a **tower
correction** — and the tower correction is LIVE, since `E₀` is canonical by
ruling with an OPEN series (`qou-y3bm`).


## 🛑 Part 11 (PR #7304) — RETRACTION of parts 9 and 10's Q_β reading

`computations/qbeta/qbeta_qbeta_scores_a_difference_probe.py` (6/6).

**Both over-claims were mine, and the calibration step caught them.**

**What I asserted** (parts 9 and 10): the floor `[n+1]_q/[2]_q^n` and then
`tr_M ≥ 1` mean "no γγ + confinement-SDP word can reproduce Q_β" — for n ≤ 5,
then at every n, with minimum prediction `E₀` = +440.369 %.

**What is true.** `Q_β = |ε(Δ)|·E₀` where **Δ = NEUTRON element − PROTON
element**. Source says so verbatim: `delta_of` — *"Delta = neutron - proton,
coordinatewise in the NF basis"*. The Markov trace is **linear**, so
`tr(Δ) = tr(n-word) − tr(p-word)`, and two quantities each ≥ 1 have a difference
bounded by **nothing**. Neither exclusion follows. Both withdrawn.

**How caught.** Reconstructing `nuc11_interleaved` letter by letter gave
tr(p) = 0.6293284022029219, tr(n) = 0.4751335171556822 — **neither** matching
the recorded `tr_conv_D = -0.1541948850472397056592555`. Their **difference**
matches to 1.4e-26, every recorded digit.

**What the difference functional gives**, all 15 pairs reported (picking the
closest would be selection against the target): **−100 % to +79.4 %**. They
**STRADDLE** the target rather than sitting above it — the opposite of the
retracted claim. Best +5.15 % against expected-by-chance **7.73 %** on an
11-value grid: same order, not evidence.

**Survives untouched** (measured, not inferred): `tr_M ≥ 1` per **individual**
PSD-feasible γγ word, tight; the det-1 fact; AM-GM; weight non-negativity; the
Markov normalisation; the floor and its decay; **every Lean theorem** (they are
about pairings and PSD matrices, none mentions Q_β); the crossing-energy results.

**One NEW finding survives:** the scored element's proton and neutron words are
**both PSD-infeasible** — `(2,1)` and `(1,1,1)` fail for each — with `det ≠ 1`
in every block. So the **SDP half** of the ruling excludes the scored element
directly at the element level, independently of the altChar exclusion.

**Fixed in the same commit**, so nothing false is left standing: both probes'
title lines, descriptions, scope paragraphs and assertion names (one was
*named* `Q_beta_is_excluded_at_every_strand_count`); a scoping note on the
prediction probe (it scores single words, also not the scoring path); and a
docstring note on `GammaGammaTraceFloor.lean`.

**Now OPEN:** whether any **pair** of PSD-feasible γγ words reproduces Q_β.


## Part 12 (PR #7304) — under the ruling the p/n asymmetry has ONE home, and the corpus keeps it where the ruling forbids

`computations/qbeta/qbeta_pn_asymmetry_has_one_home_under_the_ruling_probe.py` (6/6).

Part 11 established Q_β is scored on `Δ = n-word − p-word`, so the ruling must
select **two** words and something must separate them. This asks *what*.

**The corpus's answer today.** `nuc11_interleaved` = `core(6 γγ letters) ·
quark(3) · gluon(2)`, and **the core and gluon pair are IDENTICAL between
proton and neutron**. Three letters of eleven carry the whole asymmetry:
`(σ₀)(σ₀−h/2)(σ₁−h/2)` vs `(σ₀−h/2)(σ₀−h/2)(σ₁−h)`.

**Why that is exactly what the ruling fixes.** altChar is multiplicative and
pinned at **1** on every γγ word (`altChar_eq_one`, sorry-free). Measured: core
= **1.0 exactly**; quark blocks = **−0.9108** (p) and **−1.1221** (n), both
negative ⟹ neither is γγ-expressible — and they are precisely where the
nucleons diverge, by **23.2 %** in that invariant. Under the ruling both words
would be 1 and the invariant could not separate them at all.

Not a defect in corpus or ruling — it is **the tension between them, localised
to three letters**.

**What is left.** A γγ word's only freedom is which vertices and how many, and
the trace is blind to their **order**. So under the ruling the p/n asymmetry
has exactly one home: **the vertex multiset**. (Argument, not measurement;
asserted so it is machine-recorded; holds at every n.)

**Upgrades part 11:** at n = 4 the PSD-feasible set is 6 words, so exactly
**15** unordered (n, p) assignments — the 15-pair table is **EXHAUSTIVE** at
that strand count, not a sample. Its −100 %..+79.4 % span is therefore a
statement about the ruling, not about a selection.

**Cross-checked by two routes** — per-letter altChar product vs the `(1,1,1)`
Hoefsmit block trace, agreeing to **4.6e-39**. This is the check whose absence
caused part 11's retraction: without it the letter encoding is an unchecked
convention, which is what it was when I read `tr_conv_D` as one word's trace.

Scope-(a) + one structural observation. No pair is selected; doing so by
residual would be selection against the target.


## Part 13 (PR #7304) — BAR PARITY forces a unique Q_β from the un-ruled letter, and the census assignment FAILS it

`computations/qbeta/qbeta_bar_parity_forces_a_unique_quark_letter_probe.py` (6/6).

Working this bean's own open problem: the parity bound proves 5 of 11 letters
lie outside the ruling; of those, the two bar-fixed (`−h/2`) and the gluon pair
are **shared** between the nucleons, so **one** quark letter carries the whole
p/n asymmetry. What selects it?

**The hypothesis is the corpus's, not mine.** AGENTS.md line 2182: Q_β is *"the
bar-odd `sinh` partner of the bar-even `cosh` meson scale m_π"*. That is
attached to the **published closed form** — the `z = 1` cell the 2026-09-08
ruling retired as a base — so whether it survives to `z_D` is precisely the
open question. Impose it and see.

**The freedom.** Odd letter in any of 3 quark slots, either member of the
bar-pair (`σ` shift 0, `σ⁻¹` shift `−h`). Slots 0 and 1 are both generator 0
and give **exactly** the same trace ⟹ only **4 distinct elements**, and 26 of
the 30 ordered (p,n) pairs have nonzero Δ.

**The result.** Requiring `tr^{z_D}(Δ)(1/q) = −tr^{z_D}(Δ)(q)` leaves **8 of
26**, and **the census assignment is NOT among them**. Every survivor gives both
nucleons the **same** member of the bar-pair, differing only in generator; the
census gives them **opposite** members — exactly what destroys the parity.

**And the 8 need no choosing between.** Symbolically
`Δ(σ,σ) = −Δ(σ⁻¹,σ⁻¹)` **exactly**, so all eight share one magnitude:

    |tr(Δ)| = (q⁶−1)(q⁴+1)(q¹²−4q¹⁰+6q⁸−7q⁶+6q⁴−4q²+1) / (4q⁹(q²+1)²)

forcing **Q_β = 0.353415698 MeV, −54.825 %**.

🛑 **No selection was made** — the constraint is a parity in `q`, never
proximity to the measured value; it narrows 26 → 8; the 8 collapse. Nothing
left to pick. And the forced answer is **worse** than the census's −16.678 %,
which is the ranking AGENTS.md mandates: report what the specification gives
even when worse; rank by derivational cleanliness, never by residual.

🛑 **It does not close Q_β.** All four distinct elements **FAIL PSD**, so the
SDP half rejects this entire one-letter family — census and bar-odd alike.
Narrows the problem; does not solve it.

**Calibrated first** (the check whose absence caused part 11's retraction): the
(slot, kind) coordinates reproduce `tr_conv_D = -0.1541948850472397056592555`
to 1.4e-26.

Scope-(a). **Unconditional:** the census assignment is not bar-odd; the bar-odd
family collapses to one magnitude; no member is PSD-feasible. **Conditional:**
that bar-oddness transfers from the retired `z = 1` cell to `z_D`.

**BEAN STAYS todo (§13a)** — the subject is an open derivation.


## LANDED 2026-09-13 — PR #7304 (`49e015595d4`), and the bean stays OPEN

Seven probes (46 checks), two sorry-free Lean files. The bean's own open
problem — what selects the un-ruled letters — was **worked, not deferred**.

### The result: bar parity FORCES one number

The parity bound proves no 11-crossing word is γγ-produced, so 5 of 11
letters lie outside the ruling. The two bar-fixed (`-h/2`) letters and the
gluon pair are shared between the nucleons, so **one** quark letter carries
the whole p/n asymmetry. Imposing the corpus's own bar-odd property on
`tr^{z_D}(Delta)`:

* 26 nonzero-`Delta` ordered pairs -> **8 survivors**; the census assignment
  is **not** among them.
* The 8 collapse to ONE magnitude by the exact identity
  `Delta(sigma,sigma) = -Delta(sigma^-1,sigma^-1)`, forcing
  **Q_beta = 0.353415698 MeV, -54.825 %**.

No selection was made — the constraint is a parity in `q`, never proximity
to the measured value — and the forced answer is WORSE than the census's
-16.678 %. That is the AGENTS.md ranking: derived beats selected.

### The retraction, mine

Parts 3 and 4 inferred from `tr_M >= 1` that the γγ route cannot reproduce
Q_beta. **Wrong.** `Delta` is the neutron element MINUS the proton element,
the trace is linear, and a lower bound on each word bounds no difference.
Caught by calibration: `tr(p)` and `tr(n)` each failed to match the recorded
cell while their difference matched to 1.4e-26. The Lean stands untouched;
only prose was scoped, and a note in `GammaGammaTraceFloor.lean` stops a
reader re-deriving it.

### The SCOPE defect, also mine, fixed before merge (`04edd8b5d75`)

I wrote "all four elements fail PSD, so the SDP half of the ruling rejects
this family". That is **whole-element PSD = reading (B)**. This bean records
the selected scope as **(A) core only**, under which reading 3 prunes
nothing among the 5 free letters and the census element stands. So the PSD
result is a MEASUREMENT under (B), not a rejection by the ruling — and under
(A) it excludes nothing. Assertion renamed
`no_configuration_is_whole_element_PSD_feasible_reading_B_only`.

### STILL OPEN — do not close this bean

1. **Which reading of the SDP scope the ruling means.** (A) and (B) give
   opposite verdicts on this family. Owner call, not an agent one.
2. **Whether the bar-odd hypothesis survives the move to `z_D`.** It is
   attached to the retired `z = 1` closed form. Imposing it costs -54.825 %;
   that is reported, not avoided.


## 🟧 OWNER RULING 2026-09-13 — SDP scope is **(B) whole element**

The fork this bean carried as *"(A) core only, SELECTED-with-ambiguity"* was put
to the owner with both options framed. **The owner answered "B".**

**What (B) means.** The confinement SDP of `qou-ales` constrains **every
Wedderburn projection of the full 11-letter word**, not only the 6 gamma-gamma
core letters. Reading (A) — the core-only reading, under which reading 3 prunes
nothing among the 5 letters the parity bound leaves free and "the census element
stands" — is NOT the ruling.

### Consequence 1 — the one-letter quark family is rejected outright

All **6** (slot, kind) configurations fail `Matrix.PosSemidef` on at least one
Wedderburn block. Under (B) that is a rejection by the ruling, not a
measurement. It takes out BOTH arms at once:

* the **8 bar-odd survivors** and their forced `Q_beta = 0.353415698 MeV`
  (-54.825 %), and
* the **census assignment**.

So the bar-parity derivation forces an element the SDP half then excludes. Both
halves stand — the parity narrowing is real and forced, and the element it
forces is inadmissible. That is a stronger negative than "does not close".

### Consequence 2 — the DASHBOARD'S SCORED ELEMENT is excluded

`nuc11_interleaved` — the element `per-observable-100x-status.witness.json`
currently scores for the **Q_beta, m_n and Delta_pn** rows — fails
`Matrix.PosSemidef` on `(2,1)` and `(1,1,1)` for **both** nucleons. Block
determinants, proton: `(3,) 1.38249446339`, `(2,1) -1.02197249381`,
`(1,1,1) -0.739223570776`; neutron: `1.1221068216`, `-1.02197249381`,
`-0.910762214553`. The `(1,1,1)` entries are the alternating character and are
the already-recorded sign exclusion; the `(2,1)` failure is additional.

So under the ruled scope the L2 dashboard scores an element the selection rule
that is supposed to produce it rejects.

### What was NOT done, deliberately

**The dashboard is not re-scored.** Choosing what replaces the element is a
separate decision with its own blast radius (three L2 rows and every figure
quoted from them), and it is not an agent's to take. See "still open" below.

### Recorded in

`qbeta_bar_parity_forces_a_unique_quark_letter_probe.py` and
`qbeta_qbeta_scores_a_difference_probe.py` — docstrings, witness descriptions,
`scope` blocks and the two assertion names inverted; both re-run 6/6, both
witnesses verified to carry the ruling and to no longer carry the superseded
"(A) core only / NOT a rejection" text.

The scoping of these two probes has now moved **twice**, and both moves were
mine: asserted unscoped, demoted to "measurement under unselected (B)", and now
reinstated by ruling. The verdict matches the first draft; it is reinstated by
the owner's answer, not by the argument that first produced it.

## STILL OPEN after this ruling — the bean stays `todo`

1. **What replaces `nuc11_interleaved`** on the three L2 dashboard rows. The
   ruled scope excludes it and nothing derived replaces it yet. Re-scoring is
   an owner decision (cf. `qou-iagg`, which records the authorisation pattern).
2. **A principle for the 5 un-ruled letters that is BOTH bar-consistent AND
   whole-element PSD-admissible.** The one-letter family supplies neither
   jointly — that is now the sharp form of the open problem.
3. **Whether the bar-odd hypothesis survives the move to `z_D`** at all. It is
   attached to the retired `z = 1` closed form; imposing it costs -54.825 %.


## 2026-09-13 — item 2 is REFRAMED, not answered: the obstruction is the LENGTH

Working item 2 ("a principle for the 5 un-ruled letters that is both
bar-consistent and whole-element PSD-admissible"), formalize-first found an
invariant that prunes the search instead of narrowing it.

**The theorem** (`QOU.Mass.AltCharShiftMultiset`, sorry-free, lean-direct exit 0,
`#print axioms` clean on all six new declarations):

* `letterChar_neg` — EVERY letter of the corpus alphabet has strictly negative
  alternating character: `sigma -> -1/q = -0.9009`, bar-fixed
  `-> -(q^2+1)/(2q) = -1.0054`, `sigma^-1 -> -q = -1.1100`.
* `wordChar_sign` — therefore `sign(wordChar w) = (-1)^len(w)` for ANY letters,
  ANY order, ANY generator labelling.
* `no_eleven_letter_word_is_alt_psd` — the alternating block is
  ONE-DIMENSIONAL, so under scope (B) PSD there is exactly `0 <= character`.
  Eleven is odd. So **every** 11-letter word over this alphabet is excluded.

**Why this reframes item 2.** The obstruction does not depend on which letters
carry the p/n asymmetry, so no choice among the 5 un-ruled letters can repair
it. Item 2 as posed has no answer AT LENGTH 11. The question to ask instead is
about the crossing budget.

**What the corpus already had, and why this is not a re-derivation.**
`protonWord_char_neg` / `neutronWord_char_neg` were already proved — each for
ONE word, by computing that word's closed form. The mechanism (per-letter
negativity, hence parity) was not, and it is the part that generalises. Found
by corpus-grep before writing; without it I would have re-derived the two-word
case and called it new.

**Two independent parity obstructions, same direction.** Gamma-gamma words have
even length (`gammaGamma_length_even`), which is why the CONSTRUCTION half of
the ruling reaches only 6 of the 11 letters. The SDP half under (B) ALSO
demands even length, by a completely different argument. Neither uses the other.

**Confirmation** (`qbeta_altchar_sign_is_length_parity_probe.py`, 6/6):
exhaustive over all **1092** words at lengths 1..6 with ZERO exceptions, and the
INDEPENDENT engine route (Hoefsmit `(1,1,1)` matrices, never the scalar model)
agrees to **2.28e-39**. Per-letter products also reproduce every block value
recorded in #7304 to 15 digits.

**Honest limit, from the Lean docstring rather than discovered later:**
per-letter negativity fails for a letter with shift `d >= 1/(q^2-1) ~ 4.3094`.
Every corpus letter has `d` in {0, -1/2, -1}; the closest is `d = 0`, short by
4.3094. So this excludes words over the CORPUS ALPHABET, not over every
conceivable alphabet. A letter with a large positive shift is the only escape
this argument leaves open, and nothing in the corpus supplies one.

**What is NOT claimed:** that no nucleon word exists. Only that no ODD-length
word over this alphabet is admissible in the alternating block under scope (B).

### The open items, restated after this

1. **What replaces `nuc11_interleaved`** on the three L2 rows. Owner decision,
   unchanged, and now sharper: the replacement cannot be another 11-letter word
   over this alphabet.
2. ~~A principle for the 5 un-ruled letters~~ **superseded** — no such principle
   exists at length 11. The live question is whether the **11-crossing budget**
   is correct, given that scope (B) and the gamma-gamma construction BOTH
   require even length. That is a question about the corpus's crossing
   accounting, not about letter selection.
3. **Whether the bar-odd hypothesis survives the move to `z_D`** — unchanged.


## 2026-09-14 — 🛑 I ATTACHED THREE MERGED PRs TO THE WRONG PSD READING. The parity exclusion is reading 1; the live reading is 3, and under it the budget is unconstrained.

**What was wrong, and it was mine.** #7319 / #7325 / #7336 built a length-parity
exclusion on the alternating block `(1,1,1)`, and I recorded the 2026-09-13 owner
answer in AGENTS.md as *"every Wedderburn projection of the full 11-letter word
must be `Matrix.PosSemidef`"*. **That sentence is reading 1.** The corpus
enumerates three PSD readings and the owner selected **3** on 2026-09-12 —
*"try PSD condfinement 3 for now, but keep 1 2 for later"* (`qou-ales`):

| | criterion | status |
|---|---|---|
| reading 1 | literal `Matrix.PosSemidef` on every block | **parked** |
| reading 2 | symmetric-part PSD | **parked** |
| reading 3 | `χ_λ(w) ≥ 0` on every block with `y_λ > 0` | **SELECTED** |

The 2026-09-13 fork was explicitly about **reading 3's** scope —
`qbeta_reading3_scope_fork_probe` states it as *"(A) reading 3 applies to the
γγ-selected core only / (B) reading 3 applies to the whole 11-crossing word"*.
So **(B) moved the letter scope and left the reading alone.** Live criterion:
reading 3, whole word.

**Why that is fatal to the parity result specifically.** Under convention D
`y_(1³) = 0`, and that vanishing *is* convention D (the two-row truncation,
`markovWeights_eq_jones_of_threeRow_eq_zero`) — verified here exactly, `y_(3) +
2y_(2,1) = 1.0`. So reading 3 never looks at the alternating block, which is
where the entire parity theorem lives.

**Measured — reading 3 does not constrain the crossing budget** (all generator
assignments × all dressings over the corpus alphabet):

| k | length | parity | admissible (p) | admissible (n) |
|---|---|---|---|---|
| 0 | 9 | odd | 4/8 | 4/8 |
| 1 | 10 | even | 18/48 | 18/48 |
| 2 | 11 | odd | 149/288 | 145/288 |
| 3 | 12 | even | 594/1728 | 594/1728 |

Odd lengths 9 and 11 are admissible in quantity; there is no parity signal and
no monotone in k. **#7336's "the gluon dressing must be ODD" has no force under
the live reading.**

**Second correction — the quark family is NOT empty.**
`qbeta_bar_parity_forces_a_unique_quark_letter_probe` checks
`all(is_psd(M) for every block)` (reading 1) and concludes the SDP half rejects
the whole family. Under reading 3 **one of six survives**: `(slot 2, sigma)`,
`χ_(2,1) = +0.0574586606`. So **item 1 below has a candidate the reading-1
measurement hid.** Not adopted — selecting it because it survives would be
selection against the target.

**What is UNCHANGED: the element rejection.** Both census assignments stay
excluded under reading 3 — p `(0,sigma)` `χ_(2,1) = −0.2805933509`, n
`(2,inv)` `−0.3719563247` — and `y_(2,1) = 0.2473 > 0`, so `(2,1)` **binds**.
AGENTS.md called `(1,1,1)` the exclusion "already on record" with `(2,1)`
"additional"; it is the other way round, and `(2,1)` alone is enough. Nothing
downstream moves; **the L2 rows stay un-re-scored.**

**What the parity theorem DOES say, and it is decision-relevant.** Under reading
1 no odd-length word over the corpus alphabet is admissible, and **all three
nucleon constructions are odd** (`qou-1qsw`). So adopting reading 1 would not
tighten the selection, it would **empty** it — every nucleon model dies on
length whatever its dressing, and a survivor would need an even-length model or
a letter with shift `d ≥ 1/(q²−1) = 4.3094` against the alphabet's `{0, −½, −1}`.
That is an argument about reading 1's viability for this corpus.

Probe: `computations/qbeta/qbeta_reading3_does_not_constrain_the_budget_probe.py`
(8/8, proton pin, convention D, 60 dps). The Lean stays sorry-free and unedited —
only its scope line changes.

**Open items, restated.**
1. **What replaces `nuc11_interleaved`** on Q_β / m_n / Δ_pn — owner decision.
   Now has at least one reading-3-admissible candidate in the corpus's own
   family, and is **no longer** constrained to odd dressings.
2. Superseded twice over: first by the length reframing, now by the reading
   correction. The letters are not where the live constraint sits — `χ_(2,1)` is.
3. Whether the bar-odd hypothesis survives the move to `z_D` — untouched.


## 2026-09-14 — what DOES fix the budget: the corpus's own cost function. It selects k = 0 (or 1), never the live 11.

The correction above leaves the budget question OPEN rather than answered —
reading 3 admits every dressing count. **The answer was already in the corpus.**

**The selection principle, from the Lean.** `FrobeniusSelected B y cands cost w`
= `w` is reading-3-feasible **and** `cost w ≤ cost w'` for every feasible
candidate, with the corpus instantiating `cost = fun w => (w.length : R)` — the
**crossing count**. That is exactly how `frobeniusSelected_borromean` picks the
6-letter core. So the budget has a derived answer: the minimal-cost
reading-3-feasible dressing.

**Measured** (all generator assignments × all dressings, 4144 words):

| k | length | parity | reading 3 (p) | reading 3 (n) | reading 1 (p/n) |
|---|---|---|---|---|---|
| 0 | 9 | odd | 4/8 | 4/8 | **0/0** |
| 1 | 10 | even | 18/48 | 18/48 | **0/0** |
| 2 | 11 | odd | 149/288 | 145/288 | **0/0** |
| 3 | 12 | even | 594/1728 | 594/1728 | **0/0** |

1. **Minimal cost selects `k = 0`** — the empty dressing is reading-3-feasible
   (4/8, both nucleons), so the cost-minimal word is the **9-letter** core+quark
   with **no gluon crossings**.
2. **Excluding the empty dressing gives `k = 1`, still not 2.**
   `frobeniusSelected_nil` records that the crossing-count cost makes the empty
   word trivially selected — which is why the core selection restricts to
   non-zero vertex powers. Whether the same exclusion applies to the dressing is
   an **unstated modelling choice**. It does not rescue 11.
3. **So the live `nuc11_interleaved` (k = 2) is cost-minimal under NEITHER
   convention.** That is a second, independent reason the scored element is not
   what the ruling produces — the first being its `(2,1)` failure.
4. **The principle fixes the BUDGET, not the WORD.** At k = 0 four assignments
   tie, carrying **two** distinct traces per nucleon (p `0.6121259628` /
   `0.6263353681`; n `0.4830505246` / `0.4902320181`). `cost_eq` gives equal
   cost, not a unique word. A 2-fold degeneracy survives and is **not** closed.

**🛑 And this corrects my own correction, one level down.** The entry above says
reading 1 would empty the selection *by parity* (all corpus nucleon models are
odd). Measured, **reading 1 admits ZERO words at every k — including k = 1 and
k = 3, which are EVEN total lengths that `alt_psd_iff_even` permits.** The
`(2,1)` block excludes those independently of parity. So reading 1 is
annihilating **outright**, and the parity theorem is not the binding constraint
even where it applies. The parity result is still true and still the clean
structural statement for odd lengths; it is simply not what does the work.

Probe: `computations/qbeta/qbeta_cost_minimal_budget_under_reading3_probe.py`
(7/7, proton pin, convention D, 60 dps).

**Not claimed, deliberately.** That `k = 0` should be adopted — that is an owner
call and it hangs on the unstated empty-dressing convention. That the
crossing-count cost is the right cost for the *dressing* (extending the core's
cost to it is an extrapolation of the principle, not a theorem about it). **No
Q_β residual was computed for any of these**, precisely so the selection cannot
be contaminated by proximity to the measured value. The dashboard stays
un-re-scored.


## 2026-09-14 — 🟧 OWNER OBJECTION: crossing COUNT is the wrong cost. Measured — and it changes the answer.

Owner, verbatim: *"The selection rule shouldn't be minimum crossing... It may be
higher energy than a non-minimal crossing. A sibling has worked on connecting
hecke energy to O'Hara energy via brings embedding. Can we compare that as a
selection principle... You're minimizing not just the hecke energy but how the
knot is embedded into brings surface."*

**The objection holds, measured.** Probe
`computations/qbeta/qbeta_crossing_energy_separates_the_gluon_probe.py` (7/7).

**Part 7's verdict is right and is about γγ words.** `E_cross(k-vertex γγ word)
= k·h` exactly (reproduced), so there energy is *proportional to* count and
swapping the cost changes nothing; `E_cross(empty) = 0` sits below every
non-empty γγ word, which is the degeneracy that retired the functional.

**The gluon is not a γγ word, and there the two costs DISAGREE:**

| gluon | \|G\| | reading-3 | `E_cross` | Q_β MeV | vs CODATA |
|---|---|---|---|---|---|
| (empty) | 0 | no | 0 | 0.5457 | −30.25 % |
| σ₁ | 1 | **yes** | **+1.10998** | 0.5111 | −34.68 % |
| **σ₁⁻¹** | 1 | **yes** | **−0.90092** | 0.3970 | −49.26 % |
| σ₀σ₀ (live) | 2 | no | +2.21996 | 0.6519 | −16.68 % |
| σ₁σ₀ | 2 | yes | +2.21996 | 0.6822 | −12.80 % |
| **σ₀σ₁** | 2 | yes | **+2.21996** | **0.3357** | **−57.09 %** |
| σ₁σ₁ | 2 | yes | +2.21996 | 0.6525 | −16.60 % |

1. **Count ties σ₁ and σ₁⁻¹ at 1; energy strictly prefers σ₁⁻¹.** A negative
   crossing carries negative energy, which no count can see. The choice of cost
   is a real decision, not a formality.
2. **The degeneracy dissolves here.** `E_cross(empty) = 0` but `σ₁⁻¹ < 0`, so
   the empty word is *not* the energy minimum. γγ words are sign-**balanced** by
   construction and never offer a bare negative crossing; the gluon does. Part
   7's verdict does not transfer, and the functional is **usable** on the gluon.
3. **🛑 But it is a letter-sum, so it is order-blind — and that is the sharp
   part.** `σ₁σ₀` and `σ₀σ₁` tie **exactly** at `2q`, while their Q_β differ by
   a **factor of two** (0.6822 vs 0.3357 MeV). The observable depends on the
   ordering and the functional cannot see it. All three feasible 2-crossing
   gluons tie at one energy.

**So the owner's proposed direction is the right class of fix**, and for the
reason point 3 exposes: an embedding energy is *not* a letter-sum — it is
order-sensitive and can rank a longer word below a shorter one.

**What exists / what is missing (searched `computations/`, `tools/`):**

- **Exists** — `mobius_cross_energy_hopf_calibration.py`, calibrated against the
  **proved** `E(Hopf) = 2π²` (Agol–Marques–Neves, arXiv:1205.0825); a Borromean
  companion; `QOU.MobiusEnergy` with a categorical `E_cat` from the
  Frobenius–Hopf comultiplication and the encoded `E_cat = ¼·E_classical +
  const`; Bring period-matrix / mapping-torus-residue machinery. Beans `qou-zfs6`
  (Möbius invariance / FHW bound / minimiser as Lean gates) and `qou-dux3` are
  `completed`.
- **Missing** — **any map from a braid word to a curve in or on the Bring
  surface.** The integrators consume hand-parametrised *named* embeddings (Hopf,
  Borromean). An absence on the surfaces searched, not a proof of absence.
- **Caveat** — `MobiusEnergy.lean` carries **2 sorries**, and its own header
  records a prior vacuity incident in which `classicalLimit` made `E_cat` blind
  (`E_cat = 1 + const` for every knot) *with no `sorry` to flag it*. That leg
  cannot bear weight unexamined.
- **The hard part** — Möbius energy is a property of an **embedding**, not a knot
  invariant; the invariant is the **infimum** over the isotopy class. So a bridge
  needs either the minimiser (FHW) or a **canonical** embedding — which is
  exactly what the Bring surface would supply. That is the research content, not
  a wiring job.

**Nothing adopted.** σ₁⁻¹ is not selected — that would swap one proxy for
another, and point 3 shows the energy does not separate what remains. The Q_β
column is a reported consequence, never an input to an ordering.


## ILP does NOT escape the S4 relative-interior exclusion (2026-09-14)

Owner asked to "make sure you are doing ILP". Checked, and it is excluded —
for a proved reason, not a failed search. Probe
`computations/meson/operator_selection_ilp_does_not_escape_s4.py` (9/9, exact
sympy over Q, emits no witness per qou-pb1w); Lean
`QOU/QBeta/IntegralityDoesNotEscapeRelativeInterior.lean` (7 decls, sorry-free,
lean-direct exit 0).

**The escape was real and had to be closed.** S4 (`qou-v7qj`) excludes every
linear objective from selecting B_3 by the FACE argument — extrema on a face,
so a relative-interior minimiser is constant. That is a statement about a
CONVEX POLYHEDRON. An ILP's feasible set is not convex; the governing object
is the integer hull `conv(P ∩ L)`, whose faces need not be faces of `P`, so a
relative-interior point of `P` genuinely can be a vertex of the integer hull.

**Reading 1, over Z^6 — B_3 is not feasible at all.** Its NF coordinates are
Z-Laurent polynomials in q at q_0 and are not integers; worst coordinate (L+)
is 0.0456 from Z. Stronger and cheaper than S4's negative: not "no objective
picks it out" but "it is not in the set".

**Reading 2, over Z[q_0,q_0^-1]^6 — that is not a lattice, it is DENSE.** For
real q > 1, Z[q] is discrete in R iff q is Pisot (classical); the smallest
Pisot number is the plastic number 1.3247... (Siegel 1944); q_0 = 1.10998 is
below it. A dense feasible subset has the same closed convex hull, so the
integer hull adds no faces. Made constructive: [A6] exhibits a feasible
lattice point beating B_3, 0.8642 against 0.9986.

**The Lean strengthens rather than restates S4:** convexity was never what the
face argument used. `linear_min_two_sided_kills_direction` gets `f d = 0` over
an ARBITRARY set S from two-sided reachability and linearity alone. So an ILP
cannot escape by non-convexity; it could only escape by the lattice being
COARSE near the point, which density rules out.

**Unconditional — does not need q_0 irrational** (which this corpus cannot
prove; q_0 is pinned through Vol(4_1) = 2 Cl_2(pi/3)). All three cases give
density; only q_0 in Z is discrete, and 1 < q_0 < 2. The Pisot test needs no
decimal expansion of theta: x^3-x-1 is increasing on (1,oo), so q_0 < theta is
exactly the sign of q_0^3 - q_0 - 1 — proved as an iff in §3 of the Lean.

**Correction made in the writing, worth keeping:** the ring is Z[1/(p*r)], NOT
Z[1/r] — q_0^-1 = r/p puts powers of p in denominators, and B_3's own
coordinates carry 192- to 479-digit denominators for that reason. The first
run tested membership against Z[1/r] and FAILED [A6] on a point plainly in the
ring. The false negative was indistinguishable from a real one.

**SCOPE (b)**, structural, invariant cited: the Pisot bound for reading 2,
non-membership for reading 1. It excludes LINEAR objectives over these
lattices. It says nothing about non-linear principles (S4 refuted two
separately) and nothing about other elements.

**Still open, unchanged:** what replaces `nuc11_interleaved` after the
2026-09-13 reading-3 whole-word ruling rejected it on (2,1). That is an owner
decision and this prune narrows the search without answering it.


## TOWER (2026-09-15): the H_3 ILP answer was a truncation artifact

Owner: *"Have O'Hara on the full tower.... I suspect the longer words (which are
from gamma gamma production are higher in tower), only do order 0 when we need
the observables."* Confirmed, and worse than stated: **the H_3 probe could not
SEE the gamma-gamma operator.**

`GammaGammaH6Interface.lean:37` records the gamma-gamma-produced bond as
`(sigma_2 sigma_3^-1)^m` -- generators 2 and 3, i.e. **H_6**. My ILP alphabet was
`{sigma_0, sigma_1}` = H_3, so that operator is outside the catalogue at EVERY
length, and reading 3 was evaluated in the wrong algebra (3 blocks, not 11).

`computations/qbeta/qbeta_knot_operator_ilp_h6_tower_probe.py` (6/6):

* **Convention D IS the two-row truncation**, exactly: `y_lambda > 0` iff the
  partition has <= 2 rows. At H_6 that is (6), (5,1), (4,2), (3,3) -- FOUR of
  eleven bind. The H_3 rule `y_(1^3) = 0` is the n = 3 case of the same fact.
* **The gamma-gamma bond is INFEASIBLE at m = 1, 2 and FEASIBLE at m = 3**
  (E = 3.0990) -- the same `3 | k` pattern as the vertex-power family.
* **The decisive table**, at FIXED length (a mixed-length argmin is vacuous by
  `PairEnergyRewardsShort.pairEnergy_singleton_le`):

      len   H_6 feas   H_6 min         H_3sub feas   H_3sub min      same?
        1         10   0.0                       4   0.0             yes
        2         68   0.1629153512              8   0.9156174644    NO
        3        551   1.1261598926             62   1.2414481668    NO

  At length 2 the H_3 answer is **5.6x worse** than the true optimum. The H_6
  winners `s0is2i` and `s0s1s3` use generators an H_3 catalogue cannot express.
  The previously reported `1.2414 / s0is0is1i` is **RETRACTED as an artifact**.

Precision: `chi_lambda_braid_mpf` at 60 dps, NOT
`mass_at_3A_proper.chi_lambda_of_word`, whose own docstring says "This is a
float64 kernel, and the return annotation is the contract".

Landed on `claude/lp-dual-radical-formalize-first-2026-09-14` (PR #7399) as
commit `9078329dd68`.

**Still open (unchanged):** what replaces `nuc11_interleaved`. The H_6 table
says which operator the ILP selects at each fixed length; it does not settle the
element, because the reading-3 + PSD-3 whole-word criterion is the owner's and
five of `nuc11_interleaved`'s eleven letters remain census-derived.

## 2026-09-14 — the owner's proposed cost is the one it replaces: crossing ENERGY = crossing COUNT + a writhe term

The section above records the owner's objection to crossing count as the
selection cost, and measures that crossing energy disagrees with it on the
gluon. It left open **when** they disagree. Answered exactly, and from the
corpus's own decomposition rather than a new principle.

**The structure is already in the tree.** `QOU.Braiding.crossingEnergy p m q =
p·q − m·q⁻¹` splits (`crossingEnergy_split`,
`lean/QOU/Braiding/crossing_energy_channels.lean`) into

    symChannel  = (p − m)·(q + q⁻¹)/2      multiplicity = the WRITHE
    asymChannel = (p + m)·(q − q⁻¹)/2      multiplicity = the COUNT

and the writhe is a braid invariant while the crossing count is not. Every
result below is that one asymmetry.

**THE LEAN** —
`lean/QOU/Mass/CrossingEnergySelectionEqualsCount.lean`, 9 theorems,
sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, `#print axioms` clean
on all nine (`propext, Classical.choice, Quot.sound` only):

* `energy_le_iff_count_le_of_writhe_eq` — at fixed writhe the energy ordering
  and the count ordering are **the same ordering**, as an `iff`. Swapping the
  cost changes **no** selection inside a fixed-writhe family.
* `crossingEnergy_sub_eq_writhe_term_of_count_eq` — at fixed count the two
  energies differ by exactly `(W₁ − W₂)·symmetricWeight q`.
* `crossingEnergy_lt_of_cancelling_pair` — a cancelling pair leaves the braid
  element alone and strictly raises the energy by `q − q⁻¹ > 0`.

**THE MEASUREMENT** — `qbeta_crossing_energy_is_count_plus_writhe_probe.py`,
8/8, 60 dps, proton pin, convention D:

| check | result |
|---|---|
| `E_cross = n₊·h + W/q` on 11 candidates | exact, `< 1e-50` |
| `tr_M` over all 10 cyclic rotations of the 11-letter word | max deviation `1.55575e-61` |
| `tr_M` with the gluon **prepended** instead of appended | delta **exactly 0** |
| `tr_M` with `σ₁σ₁⁻¹` appended | delta **exactly 0** |
| `E_cross` under that same insertion | `+h = 0.20906029879563931543` exactly |
| equal-writhe ordered pairs, orderings agree | **9 / 9** |
| differing-writhe pairs where the costs disagree | 20 of 46 |
| the sibling's headline `σ₁` vs `σ₁⁻¹` gap | `2.0108968667071222998` = the writhe term exactly |

**THREE CONSEQUENCES.**

1. **The objection to the count is not answered by the energy.** Crossing energy
   *is* crossing count plus a writhe correction. It re-ranks candidates **iff**
   their writhes differ, never otherwise — so the measured disagreement the
   sibling probe found (`σ₁` vs `σ₁⁻¹`, tied at count 1) is a writhe difference
   and is the *only* kind of disagreement available. **A genuine upgrade must be
   a functional that is not a function of `(n₊, n₋)` at all.** An embedding
   energy is exactly that, which is the structural reason the owner's direction
   is the right class rather than an analogy. It remains unbuilt.

2. **The cost is a WORD functional; the observable is a BRAID-ELEMENT one.**
   Inserting a cancelling pair leaves `tr_M` exactly unchanged and raises
   `E_cross` by `h`. So `E_cross` ranks two presentations of one object
   differently while the thing being predicted ranks them identically. That is
   an admissibility problem for any letter-sum cost, independent of which one.

3. **A free prune on the candidate set.** `tr_M` is cyclic, so a *contiguous*
   gluon's **position** in the word is not a degree of freedom — prepended and
   appended give the identical trace. Only genuinely non-contiguous
   interleavings differ. Nothing in the corpus was relying on the placement, but
   it narrows what an enumeration has to cover.

**WHAT IS NOT CLAIMED, and one thing explicitly NOT measured.** Neither cost is
adopted or retired; no candidate is selected; **no Q_β is computed in the
probe at all**, deliberately — a target that is never evaluated cannot be
selected on. The converse of consequence 1 is **not** claimed: a
differing-writhe pair may still agree, and 26 of the 46 do. What is established
is the one-way implication, which is what bounds the upgrade.

**🛑 RETRACTED, same session — my "incidental finding" was a re-derivation, and
bean `qou-hv27` had it first, better.** I wrote here that the sweep's
`UNVERIFIED — missing olean` on `QOU.Braiding.crossing_energy_channels` was a
new discovery contradicting AGENTS.md, having measured root 3480 vs paper 2337
mathlib oleans. `qou-hv27` (**completed 2026-09-07**) records the same asymmetry
with a **sharper mechanism** and a **better repair**:

* **Mechanism.** It is not that the paper tree is short — it is that a *partial*
  tree **shadows** a complete one, and the sweep's `LEAN_PATH` ordering decides
  which. Lean commits to the first root containing the module's top-level
  namespace directory and never falls through (`qou-tpdg`). My framing missed
  this entirely.
* **Repair.** `cp -rln` — **hardlinks, zero disk cost**. I used plain `cp` for 94
  files on a container already at 93 % full. Strictly worse, for no benefit.

**How I got here is the instructive part.** I ran the six-path corpus-grep for
the bean's *subject* and not for my own *incidental* observation, which is
exactly the gap path 6 exists to close — a prior agent's conclusion sitting in a
bean before it reaches any other artifact. A finding noticed in passing needs
the checklist just as much as the one you went looking for.

**What survives, and it is small:** AGENTS.md's own text still describes this
UNVERIFIED class as the cache branch being short, "absent from the **paper and
root trees alike**", which is not what either measurement shows. That wording is
worth correcting against `qou-hv27`, and it is a docs fix rather than a finding.

**And the limitation it caused is now gone.** Applying `qou-hv27`'s documented
per-session repair (it does not survive a fresh container), the sweep gate runs
the new module properly: **2 ok, 0 RED, 0 UNVERIFIED** — dependency rebuilt from
source, not linked from a snapshot. So the verification below is the sound gate,
not lean-direct against an olean whose source I had to argue was unchanged.

**Open items unchanged.** Item 1 (what replaces `nuc11_interleaved` on the three
L2 rows) is still the owner's decision and is untouched here. Item 3 (whether
the bar-odd hypothesis survives the move to `z_D`) is untouched. This narrows
the cost question that superseded item 2; it does not close it, because the
functional the argument points at is not built.

### Same day, the closing move: the energy's only ADMISSIBLE form *is* the count

The section above shows the energy is a **word** functional. A word functional
has exactly one canonical descent to the object — its extremum over the fibre —
and here that extremum is computable, because the writhe is constant on a braid
class while the count is not. `crossingEnergy = symChannel(W) + (p+m)·(q−q⁻¹)/2`
with `W` invariant and `q − q⁻¹ > 0`, so:

**`isLeast_energy_iff_isLeast_count_of_writhe_eq`** (sorry-free; the file is now
10 theorems, `lean`-direct exit 0, `#print axioms` clean on all of them) — over
any finite family of presentations sharing a writhe, which is what a braid class
is, **the energy-minimal presentation is exactly the count-minimal one.**

So making the energy admissible turns it **into** the crossing-count cost it was
proposed to replace, up to an additive invariant. That closes the "energy
instead of count" proposal as posed, rather than merely bounding it.

**And the proposed replacement inherits the same defect.** Checked directly:
`QOU.MobiusEnergy.ClassicalMobiusEnergy` is a functional of an **embedding**,
and its own docstring says so — *"this structure holds no isotopy-class data"*.
So as encoded it is no more a braid-element invariant than `E_cross` is, and
swapping it in would swap one presentation-dependent cost for another.

**This is what makes the Bring embedding load-bearing rather than an
implementation detail.** What repairs an embedding functional is either the FHW
minimiser (the infimum over the isotopy class — bean `qou-zfs6`) or a
**canonical** embedding, and the Bring surface is the candidate canonical
embedding. The owner's instinct that the Bring half matters is therefore right
for a sharper reason than "it is where the geometry lives": without it the
proposal does not clear the admissibility bar its own objection implies.

**Caveat carried forward, not re-derived:** `MobiusEnergy.lean` has 2 sorries
and its header records a prior vacuity incident in which `unknot_iff` read
`value = 4 ↔ True`, forcing `value = 4` for every instance and making `E_cat`
blind to the knot, with no `sorry` to flag it. That leg cannot bear weight
unexamined — the observation above is about the structure's *arity*, which is
visible from the docstring and is unaffected by the sorries.

### 2026-09-14, ~1 h later — 🛑 my "it remains unbuilt" went STALE while the PR was open, and a sibling reached the same exclusion by a different invariant

The entry above ends by naming the open target: *"a genuine upgrade must be a
functional that is not a function of `(n₊, n₋)` at all... An embedding energy is
exactly that... It remains unbuilt."* **Three commits landed on `main` between
18:34 and 19:10 that make that false**, and the convergence is worth recording
rather than quietly deleting.

**What landed** (branch `claude/lean-crossing-budget-invariants-2026-09-14`,
PR #7391, now closed):

* `380f5935c2` — **`QOU/QBeta/LetterSumBlindness.lean`**, sorry-free.
  `letterSum_perm_invariant`, `no_letterSum_separates`,
  `crossingCount_perm_blind`, **`crossingEnergy_perm_blind`**,
  `factorsThrough_blind`, plus a scope lemma
  (`objective_blindness_does_not_transfer_to_constrained_optimum`) delimiting
  the exclusion so it does not kill the SDP route.
* `aa224aba03` — **`QOU/QBeta/ECatBlockDecomposition.lean`** + probe
  `qbeta_ecat_pair_kernel_probe.py` (4/4): a **pair kernel** dropped into the
  `cost : W → R` socket of `GammaGammaWordSelection`, with
  `pairSum_not_perm_invariant` — a pair sum whose kernel reads the **separation**
  of the two letters escapes the letter-sum exclusion. Four distinct values over
  the four 2-crossing gluons against one value for every letter-sum.
* `27250649ff` — the per-block cost vector `t_λ`.

**The two results are COMPLEMENTARY, and neither implies the other.** Stating
this precisely because "both exclude letter-sums" invites collapsing them:

| | invariant used | what it says |
|---|---|---|
| **theirs** | permutation of letters | `E_cross` cannot **separate** two reorderings — a statement about the letter *multiset* |
| **mine** | the writhe/count channel split | `E_cross` and the count are **the same ordering** at fixed writhe; they differ by exactly the writhe term at fixed count; the energy's admissible descent **is** count-minimisation |

Permutation-blindness says nothing about how the energy *compares to the count*
across different multisets, which is my whole result. And
`crossingEnergy_lt_of_cancelling_pair` is orthogonal to both: a cancelling pair
**changes** the multiset, so permutation-invariance cannot reach it — that
lemma is about the map word → braid *element*, not word → multiset.

**Their control is my `crossingEnergy_eq_of_writhe_and_count_eq`, measured.**
With the separation weight removed, the sharp pair — *"same multiset, same
writhe, differing only in ORDER"* — reads `34.6134315674846072` for **both**, a
difference of **exactly 0.0**, against `0.91996925` weighted. That is the forced
tie my Lean states, arrived at from the other direction and used as a control
rather than as a theorem.

**What is corrected in my PR body:** "It remains unbuilt" → built, with the
citation. **What is NOT corrected:** every theorem and every measured figure in
the entry above stands; the re-verification after merging `main` (69 commits) is
**2 ok, 0 RED, 0 UNVERIFIED**.

**What their own commit message declines to claim, carried here so it is not
lost downstream:** the discretisation is **not** `E_cat` (whether its continuum
limit is `E_cat` is unproved), **nothing selects a word** — *"a cost that
separates is a precondition for selection, not a selection"* — the per-block
`t_λ` is proved a refinement but **not computed**, and the `MobiusEnergy`
classical-limit leg stays assumed with its blindness incident unretired
(`qou-pzsi`). So the open item is narrower than before and is **not** closed:
a separating cost now exists; **which** cost, and whether minimising it is
legitimate, is untouched.

**Coordination note.** I posted intent on #7391 at 18:44 naming my distinct
angle; it landed ~30 min later. That is the sanctioned research-overlap pattern
working as intended (AGENTS.md §Parallel exploration) — two routes, one
exclusion, neither re-deriving the other. Converging per that rule: I do not
re-derive their pair kernel, and this bean cites it.

### 2026-09-14 21:46–22:29Z — the classical-limit BRIDGE FIELD is vacuous, and an attribution correction

Two cross-branch notes landed on #7390. Both verified here rather than taken.

**1. `MobiusEnergy.classicalLimit` constrains nothing** (reported by #7262;
checked at the structure, not at their theorem, because it is **not on `main`**):

```lean
classicalLimitConst : ℝ
classicalLimit : energy = (1 / 4) * classicalEnergy.value + classicalLimitConst
```

`classicalLimitConst` is a **free field of the same structure**, so for any pair
`(energy, classicalEnergy)` exactly one `k` satisfies it — the field relates the
two energies **not at all**. #7262 proves it sorry-free as
`classicalLimit_unconstraining` / `classicalLimitConst_eq`, on that branch only;
the structure field is checkable on `main` today.

**This compounds with the entry above rather than repeating it.** That entry
established `ClassicalMobiusEnergy` is a functional of an **embedding** (its own
docstring: *"this structure holds no isotopy-class data"*). Now the **bridge**
field is vacuous too. So there are **two independent reasons** the
classical-limit route cannot bear weight: the functional is of a presentation,
and the field that would connect it to `E_cat` asserts nothing. It is also the
same defect class as the header's recorded incident (`unknot_iff : value = 4 ↔
True`) **one field over** — a structure whose constraint is discharged by a free
companion field, with no `sorry` to flag it. Not repaired: §ASK THE OWNER,
neither exemption applies.

**2. An attribution correction, made because the commenter said they would cite
it.** #7262 credited `blockCost_can_separate`, `pairSum_not_perm_invariant`,
`bridgeClass_perm_blind` and `qbeta_ecat_pair_kernel_probe` to #7390. **All four
are #7391's** (`aa224aba03` / `380f5935c2`, both on `main`). Measured: this
branch's `git diff --name-only origin/main...HEAD` is exactly four files — the
bean, the probe, its witness, and
`QOU/Mass/CrossingEnergySelectionEqualsCount.lean` — and none contains those
names. Cause is partly mine: `cf2cc9d011`'s body *describes* #7391's work next
to my own, which is presumably how it got attached. **Lesson worth keeping: when
a PR body summarises a sibling's landing, name the sibling in the same sentence
as the declaration, not in a heading two paragraphs up.**

**3. From #7399 — the ILP escape is closed, and it composes with this entry.**
A linear objective cannot select `𝓑₃` by the face argument (S4, `qou-v7qj`), and
the obvious reply — *"the face argument needs convexity, an integer program is
not convex"* — is measured not to escape: over `ℤ⁶` `𝓑₃` is not feasible at all
(worst coordinate `0.0456` from ℤ), and over `ℤ[q₀,q₀⁻¹]⁶` **that ring is
dense**, because `ℤ[q]` is discrete iff `q` is Pisot and `q₀ = 1.10998` sits
below the plastic number `1.3247…` (Siegel 1944); constructively a feasible
lattice point beats `𝓑₃` at `0.8642` vs `0.9986`. Their
`linear_min_two_sided_kills_direction` gets `f d = 0` over an arbitrary set from
two-sided reachability and linearity alone — **convexity was never the
load-bearing hypothesis**, so non-convexity buys nothing.

Composed with this entry: **if crossing energy IS the count, then the count is
both permutation-blind and unable to select by any linear program, integer or
not.** That is a constraint on where the selection can come from — not a problem
with the reduction.

### 2026-09-15 10:25Z — twelve `qou-99qc` commits landed overnight; what they do to this entry, checked rather than assumed

`main` moved 24 → 85 while #7390 sat open, and **twelve** of those are on this
bean. The merge conflicted on exactly the file AGENTS.md predicts — this bean —
and was resolved losslessly with the prescribed
[`scripts/bean-append-merge.py`](scripts/bean-append-merge.py) (`+16309 ch
appended`, `main` byte-for-byte preserved), not by hand.

**THE ONE THAT CONTINUES THIS ENTRY DIRECTLY.** `b7b5e3e290` adds
`QOU/Mass/PairEnergyRewardsShort.lean` (7 decls, sorry-free), stated for an
**arbitrary** kernel `K`:

* `pairEnergy_singleton_le` — under non-negativity a **1-letter word is a global
  minimiser over every word**;
* `exists_singleton_minimiser` — any catalogue containing a singleton has its
  optimum there, whatever else it holds;
* the contrapositive — **to select anything longer, the kernel must go negative
  somewhere.**

**Composed with this entry, the lesson is sharper than either half.** Mine:
minimising `E_cross` *is* minimising the count
(`isLeast_energy_iff_isLeast_count_of_writhe_eq`). Theirs: minimising a
non-negative pair energy picks the shortest word. Both say the same thing about
a different functional — **plain minimisation drives you to the degenerate short
end, so the pathology is the MINIMISATION FRAME, not the particular cost.** A
cost that *separates* (the pair kernel of `aa224aba03`) is therefore still not
enough: separation is necessary, and the selection rule must additionally not be
bare minimisation of a non-negative functional.

**An observation, marked as suggestive and NOT a theorem.** Their contrapositive
says a selecting kernel must go negative somewhere, and the table in the entry
above already *exhibits* negativity: `E_cross(σ₁⁻¹) = −0.90091828395574` and
`E_cross(σ₀⁻¹σ₁⁻¹) = −1.8018365679115` — a negative crossing carries negative
energy. **Scope: mine is a letter-sum, negative per LETTER; theirs is a kernel
on letter PAIRS.** So this is not an instance of their hypothesis, only evidence
that the corpus's own energy convention supplies the sign structure their design
constraint asks for. Do not cite it as satisfying the hypothesis.

**WHAT DOES NOT TOUCH THIS ENTRY, checked three ways rather than assumed.**
`6fb8dafe3c` reports two hazards that look like they should land on my probe —
*"the H_3 legacy path is float64"* (`atom_per_generator_volumes` warns but
RETURNS, and its `mpf` is bit-exactly a padded float64; 32 callers) and *"the
H_3 answer is a truncation artifact at every length ≥ 2"*. Neither reaches it:

1. **Import cone.** Walked all 19 modules reachable from
   `qbeta_crossing_energy_is_count_plus_writhe_probe`: `atom_per_generator_volumes`
   appears in **none**.
2. **Re-ran the probe on the merged tree — 8/8, and the witness is byte-
   UNCHANGED**, so no import-cone drift moved a number.
3. **Structurally, and this is the durable half.** Checks 1, 3, 4, 5 and 6 use
   **no `tr_M` at all** — they are algebra on `E_cross`. Checks 2 are
   *invariance* claims (cyclic rotation, contiguous-block position, cancelling
   pair), which hold for **any** trace, whatever algebra it is taken in; the
   measured `1.55575e-61` and exact-`0` deltas are what establish that `tr_at`
   *is* a trace. So **no claim in this arc depends on H_3 vs H_6** — only on
   tr_M being a trace. That was luck rather than design, and is worth stating
   explicitly so a future reader does not re-litigate it.

**Verification after the merge:** library sweep on
`QOU.Mass.CrossingEnergySelectionEqualsCount` — **2 ok, 0 RED, 0 TIMEOUT,
0 UNVERIFIED, 0 skipped** (176 s), dependency rebuilt from source.

**Also worth carrying: they caught a LAYER STRADDLE in their own measuring
script** — it rebound `q` in the character kernel but not in `_order`, whose
`word_nf` folds with `_order.H0`, so the NF was at the anchor while `χ` was at
the perturbed `q`. That produced three false claims, including a "root of
`χ_(2,1)` at `q₀` agreeing to 40 digits"; measured correctly, `χ_(2,1)(s0s1s1)`
shrinks like `10^-dps` at **every** `q` and is identically zero, with no root.
Exactly the straddle class AGENTS.md §"Never straddle the two layers" warns
about, one layer over — and it was caught by the author, not by a gate.

## 2026-09-14 (session gifted-feynman) — the Lean step `cost_eq` stops short of, and a wrong turn worth keeping

**Claim.** `FrobeniusSelected.cost_eq` says two *selected* words have equal
**cost**. The step this bean needs is the next one: that the selection predicate
can hold of **two different words**, so the rule does not determine the word.
Nothing in the corpus drew it. `QOU.Mass.CostOrderSensitivity` now does, for an
**arbitrary quotient** the cost factors through — sorry-free, `lean`-direct
exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` clean on all eight
declarations (two depend on **no axioms at all**; the rest only `propext` /
`Quot.sound`).

| declaration | statement |
|---|---|
| `minimal_transfers_along_fibre` | minimality transfers along a fibre of `π` |
| `selected_not_determined_of_cost_factors` | …so **both** words are selected |
| `lengthCost_not_determined` | the corpus's own crossing-count cost |
| `letterSumCost_not_determined` | any letter-sum cost |

**Cited, not re-derived.** The *invariance* half is already held four times
over and the file says so: `OptionELevelAcceptanceTest.monoidHom_order_blind`
(the multiplicative twin), `AltCharShiftMultiset.wordChar_of_perm`,
`YekutieliIntegration.holonomy_perm`, and **definitionally** in
`crossing-energy.lean`, which models `BraidWord := List Bool` and reads only two
counts. The letter-sum scope-(b) exclusion is already prose on `main`
(`qbeta_embedding_energy_can_discriminate_probe.py:46–52`, bean `qou-pzsi`).

**🛑 The wrong turn, recorded because it is the interesting part.** This was
first drafted around the **abelianization** — *"a cost factoring through
`B_n^ab ≅ ℤ` cannot separate two words of equal exponent sum"*. **That framing
is wrong for its own targets.** `B_n^ab` records only `e = n₊ − n₋`, so of the
corpus's own three crossing-energy components only `baseline` (the writhe)
factors through it. **Crossing count `n₊ + n₋` does not** — and it is
`FrobeniusSelected`'s *only* instantiation in the entire corpus — and neither
does `E_cross = n₊q − n₋q⁻¹`. An abelianization-quantified theorem would have
claimed a family it provably does not cover: the `da-arity-conflation` shape.
The right invariant is the **multiset** (equivalently `List.Perm`), strictly
coarser, and it is what the sibling probe already names. **Caught by the
corpus-grep checklist before anything was committed** — paths 1–6 with the
claim SHAPE rather than the topic, which is exactly the case §"Grep the claim
SHAPE" exists for.

**Scope, deliberately narrow.** It does **not** prove a selection cost must be
order-sensitive — blindness *precludes separating these candidates*, it does not
*force* a replacement to see order. That caution is this bean's own (~line 1100)
and is restated inside the file so the theorems are not read as more than they
are. It does **not** exhibit a rearrangement pair inside the live `cands` that
is also feasible; that stays a measurement. It proposes **no** replacement cost
and re-scores **nothing**.

**What this leaves as the live open item** is unchanged and is `qou-pzsi`: there
is still **no map from a braid word to a curve in or on the Bring surface**, so
the order-sensitive functional the owner's objection points at has nothing to
consume. This result says what any replacement must have (it must not be
constant on the multiset); it does not supply one.

## 2026-09-14 (session gifted-feynman, 2) — my retraction was HALF wrong: the abelianization is right for the EMBEDDING

The entry above retracts an abelianization framing as *"wrong for its own
targets"*. That retraction is **correct for costs and wrong one step over**, and
a sibling's merged bridge is what shows it.

**The claim.** `qbeta_bring_ohara_bridge_probe.py` (7/7, merged #7374) sends a
braid word to a cusp-torus lattice class

    (m, ℓ) = (exponent sum, strand count)

— verified at source, `:36-37` and `:65`, and again at `:343-344`
(`m = BASE_WRITHE + writhe(g)`, `ell = STRANDS`). **`m` is exactly the
abelianization**: `e : B_d → ℤ`, `σ_i ↦ 1`, induces `B_d/[B_d,B_d] ≅ ℤ`
(Black–Samson, `library/black-samson-phd2010sp/…/sec-008-12-summary-of-thesis.md:126`),
and `ℓ` does not depend on the word at all.

**So the same quotient under-prunes on one side of the pipeline and
over-collapses on the other.** Against the *cost* functions it is too coarse to
bite — crossing count `n₊ + n₋` and `E_cross = n₊q − n₋q⁻¹` both survive it,
which is why the retraction stands. Against the *embedding map* it is precisely
what the corpus does, and it is **strictly coarser than the multiset**, so it
loses strictly more.

**Consequence for the Lean.** `selected_not_determined_of_cost_factors` is
quantified over an **arbitrary** quotient `π`, so it covers this instance with
no change: put `π = (writhe, strands)` and the sibling's measured negative —
all four two-crossing gluon dressings share one class, one geodesic and one
energy — is an instance of the general theorem rather than a separate fact.
The docstring now records this beside the retraction.

**The reusable lesson is about attachment, not about the invariant.** "X is
blind to Y" is a claim about a *particular map*; carrying it to a neighbouring
map in the same pipeline is not a corollary. I made that error in one direction
and would have missed the true instance in the other.

**Nothing re-scored, nothing selected.** The sibling's own scoping stands: the
bridge does not select, the dashboard rows stay un-re-scored, and the
`u = ln q₀` vs `u = 2 ln q₀` meridian-normalisation binary stays open with
neither branch adopted.


## 2026-09-14 (session gifted-feynman, 6) — the replacement my theorem demanded HAS been built, by a sibling; I am not re-deriving it

My entry above ends: *"This result says what any replacement must have (it must
not be constant on the multiset); it does not supply one."* **A sibling
supplied one, and it is on `main`.**

`claude/99qc-crossing-budget-parity-2026-09-14` (PR #7390), commits
`380f5935c2` / `aa224aba03` / `27250649ff`:

* `QOU.QBeta.ECatBlockDecomposition.pairSum_not_perm_invariant` and
  `blockCost_can_separate` — a **pair kernel** in the cost socket, with the
  O'Hara `1/d_arc²` separation weight doing the work;
* `qbeta_ecat_pair_kernel_probe` (4/4), run here against the merged tree: four
  distinct proton values over the four gluon dressings
  (`8.68872560885`, `7.76875635932`, `8.89780952920`, `9.06507666548`) against
  **one** value for every letter-sum, and a control showing the sharp pair
  separating by `0.91996925` weighted against **exactly 0.0** unweighted.

**It escapes MY quotient, not only permutation — and that composition is
already measured, so there is nothing for me to add.**
`LetterSumBlindness.bridgeClass_perm_blind` is exactly the
`(exponent sum, strands)` map my own entry identified as the corpus's
embedding map; all four candidates sit at **writhe +2, length 2**, one fibre
of it; the kernel separates them. That is assertions 1 and 2 of their probe.

**Deliberately not re-derived.** Per the convergence rule the second route
verifies and cites. I added no companion lemma; `CostOrderSensitivity.lean`
gains a docstring section recording the finding and the credit, nothing more.
Their commit's own account of the complementarity is correct: theirs turns on
**permutation** of letters, mine on the **writhe/count split** at fixed
writhe, and neither implies the other.

**What stays open is narrower, not closed**, and their assertion 4 scopes it
themselves: the kernel is a **discretisation**, its continuum limit is not
proved to be `E_cat`, and the classical-limit leg it would need is *assumed*.

**That leg is worse than assumed, and I proved it this session.**
`CategoricalMobiusEnergy.classicalLimit` has `classicalLimitConst` as a **free
field of the same structure**, so it is satisfiable for any pair of energies by
exactly one `k` — `QOU.MobiusEnergy.classicalLimit_unconstraining` and
`classicalLimitConst_eq` (sorry-free). So a future agent cannot close the
continuum-limit question by appealing to that field. Reported on #7390;
**not repaired** — §ASK THE OWNER applies and it stays an owner decision.

**The replacement ELEMENT is still an owner call.** None of this selects a
word. Their own declined claims stand (not `E_cat`; nothing selects a word;
`t_lambda` not computed), and this bean's first open item — what replaces
`nuc11_interleaved` after the confinement-SDP reading-3 rejection — is
untouched by all of it.


## 🛑 Citation correction 2026-09-26 (bean `qou-6moa`) — the reading is unaffected

This bean cites `markovWeights_eq_jones_of_threeRow_eq_zero` for the claim that
under convention D the three-row weight vanishes. **That lemma proves the
converse.** Read its signature (`BraidsAndKnots/MarkovTraceTLUniqueness.lean:119`):
`hTL : y₁₃ = 0` is a **hypothesis** and `z * (q + qi) = q ^ 2` — convention D — is
the **conclusion**. So it gives TL ⟹ D, which is the direction
`docs/coordination/trace-convention-registry.json:173` correctly cites it for.

It also carries `hfaith : y₂₁ ≠ 0`, and that is load-bearing rather than
decorative: the sibling `markovWeights_degenerate_root` (`:154`) proves that
dropping it makes the conclusion **false**, not merely unprovable — the trivial
character `y = (1,0,0)` at `z = q` satisfies all three moment equations and gives
`q·(q+qi) = q² + 1 ≠ q²`. A lemma that *assumes* a form of faithfulness on the
two-row block cannot be evidence about the three-row block vanishing.

**Cite instead**, matching the frame:

| lemma | typeclass | scope |
|---|---|---|
| `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (`:142`) | `[Field R]`, sole hypothesis `q²+1 ≠ 0` | general `n`, on the actual Ocneanu weight |
| `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu` (`:179`) | `[CommRing R] [IsDomain R]`, division-free | `n = 3`, same variable frame |
| `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` (`:368`) | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` — **an ordered field** | `n = 3`, archimedean only |

The third is the wrong citation at any §7c generic-`R` site.

**Nothing in this bean's conclusions changes** — only the authority cited for one
step. Measured: the reversal is a class of 14 across 9 files against 49 correct
citations, and 3 further files carry the same assertion with no lemma named at
all, so a grep on the identifier cannot find them. Full per-site table and blast
radius on `qou-6moa`; fixed so far in AGENTS.md and
`QOU/Mass/AltCharShiftMultiset.lean` (PR #7459).


## 2026-10-10 — the energy / O'Hara selection principle, route 1: what an embedding energy can and cannot select

Full entry on `qou-pzsi`; probe `computations/probes/ohara_link_energy/`.

- **The 2-crossing gluon dressings close to two links, not four.** `gluon_s0_s1` ≅ `gluon_s0_s0` = `nuc11_interleaved`, and `gluon_s1_s0` ≅ `gluon_s1_s1`, by hand-checked braid conjugacy. Any closure or embedding energy therefore ties the live element with `gluon_s0_s1` by construction.
- **Flowed link Möbius energy (upper bounds, multi-start).** It ranks `nuc9` (234.2) well below both dressing classes (≈291), which sit well below `gen_grouped` (>311). It does **not** separate the two dressing classes: the gap is 1.1 against a combined error of 1.2.
- **So the owner's 2026-09-14 direction is confirmed as the right class.** The energy is order-sensitive where letter-sums are not. But on this candidate set it **cannot pick among the gluon dressings**, and it cannot see the letter decoration at all.
- The gluon dressing stays unselected. No dashboard row was re-scored.

## 2026-10-11 route 2 status

- The gluon tail is ALLOWED (owner ruling, 2026-10-11).
- The q-deformed recipe uses t = −q₀ (owner ruling). PR #7647 merged; it gives no ranking.
- Option 1, ropelength on fresh 11-letter words, FAILED its pre-registered test (24-way tie). PR #7651 merged.
- Option 1b pre-registers a same-loop-up-to-symmetry rule on fresh 13-letter words (branch claude/bring-route2-sameloop-2026-10-11).
- No word is selected by route 2.

**2026-10-11 (route 2, options 1b/1c, PRs #7672 merged, #7679).** On fresh 13-letter words: 316 classes = 33 braids; the shortest Bring loop carries 3 braids (88 spellings of one), so Bring-loop energies select loops, not words. The owner-ruled q-length at t = -q0 separates braids: alone it picks sigma0*Delta^4 (length ln q0, no Bring loop); Bring-loop-first picks a different braid. Contaminated read-across to the seen candidates: rule A -> nuc11_interleaved (the scored element), rule B -> class A. The two rules disagree; which (if either) is the selection principle is an OPEN owner decision. Nothing selected. Bean stays open.

## 2026-10-11 — option 1d (11-letter, all 94 classes; PR #7679, 007720dbbf)

Pre-registered rules on all 94 positive 11-letter word classes (16 braids). Rule A (q-length at t=−q₀ alone) picks the braid of nuc11_interleaved (parabolic, E_q = ln q₀, no Bring loop). Rule B (shortest Bring loop, L = 4.6031833095, then q-length) picks the braid of class A (gluon_s1_s0/s1_s1, E_q = 2.6496). Both decided, they disagree; contaminated (seen q-lengths known beforehand). The selection rule remains an OPEN owner decision — this bean stays open.

## 2026-10-11 — CORRECTION: route 2 used sign-erased candidates (results_signed.md)

Route 2 and options 1 through 1d (and route 1, ohara_link_energy) took the seen candidates from the sign-erased generator list in qbeta_candidate_closures_are_links_probe. The canonical nucleon (pyhecke.atom.build_nucleon_nf) has a (σ₀σ₁⁻¹)³ core and averaged ud letters, so it is a SUM OF FOUR BRAIDS. Under route 2 every proton term has a Bring loop (L = 9.21 / 15.94 / 6.37 / 20.44), whereas the sign-erased nuc11 is parabolic with no loop. Every seen-candidate read-across from route 2 is WITHDRAWN, including 1d's "Rule A → nuc11, Rule B → class A". The fresh-positive-word results stand. γγ words (σ₀σ₁⁻¹)^k never get a Bring loop under route 2's "exactly one fixed point" rule: this is a limit of the rule (3 ∤ k: no conjugate of Γ₀(2) contains the word; 3 | k: the word is pure, so all three conjugates contain it). Scope (a). The selection rule stays OPEN.


## 2026-10-11 (PR #7695)

Neutron expansion in `signed_candidates_probe.py` was wrong (uu→dd instead of ud·ud·dd); fixed and now checked against `build_nucleon_nf_mp`. Core (σ₀σ₁⁻¹)³ and 00001100011 are the same Bring loop though not conjugate. B3: under Hecke H₃(q₀) the 2×2 quantity reduces to Wedderburn characters, x = |χ_(2,1)|/√|χ_(3)χ_(1³)|, det = −([2]_q/2)⁴ for both nucleons; under Burau t = −q₀, det = χ_(3). The normalisations disagree in type on every row; neither adopted; B4 (no energy for sums) stays default. Selection still OPEN.

**2026-10-11 — strand-count tower of γγ production** (issue #7727, branch `claude/gg-production-ntower-2026-10-11`, `computations/probes/gg_ntower/`). Pre-registered (4544d19380) before computing. Collisions V_i = σ_iσ_{i+1}⁻¹ (and the bare U_i = σ_iσ_{i+1}, separate column) placed with a rigid shift s ∈ {0, ±1, ±2, +3}, up to 9 strands; strands closed from the top by the convention-D Markov conditional expectation; reading 3 tested at every level. Exact over ℚ(q); 5/5 checks.
- s = +1 telescopes in any group: V_0⋯V_{k−1} = σ_0σ_k⁻¹ (Lean `QOU/QBeta/GammaGammaStaircaseTelescopes.lean`, sorry-free). Degenerate.
- s = −1, ±2, +3: no k admissible, for either vertex. After three collisions closed down to three strands, χ_(2,1) is already negative at q = 1 (−1/4 or −1/16) and stays negative for every q > 1.
- Only s = 0 (all collisions on the same three strands, k = 3, 6) confines. Its χ_(2,1) leaves the q = 1 value at h⁴; the climbing placements leave at h¹ or h².
- Scope (a): rigid shifts with top closing only. Jones pair creation, bottom closing, quarks, gluons and two nucleons were not tested. Selection stays open.

**2026-10-12 — 🟧 OWNER RULING (chat): "every level" means EVERY STRAND COUNT, not only H_{3k}.** Asked in session https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB with two options (1 every strand count m = 3..n; 2 only the nucleus levels H_3, H_6, H_9, …). Owner chose 1. Measured consequence on the #7733 witness: five rows pass at level 3 and fail only at an in-between level (V s=+1 k=2 at 4; V s=+1 k=3 at 5; V s=−1 k=2 at 4; U s=+1 k=2 at 4; U s=−1 k=2 at 4). Under reading 2 they would be admissible; under the ruled reading 1 they are excluded, which is what #7733 reported. None is a genuine cascade (s=+1 telescopes to σ₀σ_k⁻¹; s=−1 k=2 is two collisions sharing two strands). Bean stays open (rule 13a).

## 2026-10-11 — quark template tracked order by order in q (reading 3)

Probe `computations/probes/quark_template/` (pre-registered at 6b9dd5d172; exact over Q(q); 4/4 checks).

- **Flavour is invisible at order t⁰** (t = q − 1): since σ⁻¹ = σ − h, every quark letter equals σ at q = 1, all 8 template variants give the same element, and χ_(2,1) = 0 there. So reading 3 holds with equality at order zero for every template. The verdict is decided at order t¹ (where the sign bits enter), or at t³ when t¹ cancels. No verdict flips between truncation orders t¹…t⁶ or across the sub-interval of (1, ∞) containing q₀.
- **k = 0, builder placement:** the corpus template (u = σ, d = σ⁻¹, ud = average) FAILS reading 3 for both nucleons (χ_(2,1) = −0.09198 p, −0.18200 n). Its sign changes exactly at q*² + q*⁻² = 1 + 2cos(2π/7), q* = 1.27890, above q₀. Every bar-swapped template (u = σ⁻¹, d = σ) passes for both nucleons, under every pair rule. The two flavour-blind templates also pass.
- **With the gluon pair σ₀σ₀:** no template passes for both nucleons.
- **Placement varied too:** the corpus template has 4/8 admissible placements per nucleon; the builder's is not one of them. So reading 3 constrains sign map and placement jointly, not the template alone.
- **Tension, unresolved:** this bean's 2026-09-05 "swap refuted" rests on a comparison with measured binding data, which cannot select under the no-fitting rule. Reading 3, the ruled derived test, points to the swap at k = 0 and the builder placement. This is an owner decision. The bean stays open.

## 🟧 OWNER RULING 2026-10-12 — quark sign map: option 4, derive it, do not pick it

Asked in the six-part frame on PR #7718 (comment 6130340849). The four options were: 1 keep S+ (status quo); 2 adopt the swap S− (u = σ⁻¹, d = σ), which passes reading 3 at the builder placement; 3 keep S+ and move the letters to placement 011 or 100; 4 pick nothing by hand. **The owner chose 4.** The quark sign map and the letter placement must be outputs of the γγ construction plus reading 3 at every tower level (`qou-ales`), not a template choice. The template stays open and nothing is re-scored. The dashboard knowingly keeps scoring an element that reading 3 rejects until a derivation lands. The 2026-09-05 data-based "swap refuted" in `qou-y2np` is a comparison with data, so it counts as a selection neither way. This bean stays open (rule 13a). Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

**2026-10-11 — 🟧 OWNER RULING (thread chat, ofri, verbatim): "3... but let's go through γγ production step by step to get to one and two nucleons. each collision/interaction shifts things up the tower".** Option 3 of the #7702 decision: **reading 3 applies at EVERY level of the tower** (nucleon in H_3, A nucleons in H_{3A}, all checked). On the #7702 family this coincides with the H_3 verdicts; the live element stays excluded. Next: walk γγ production step by step, tracking the tower level of each collision (h-order and n). Walk-through: /mnt/project-files/qbeta-ohara/gg-production-walkthrough.md. Bean stays open (rule 13a).

### Cross-link (2026-10-11)

the p-n interface convention R3 made canonical is the one the corpus's uniqueness theorem does NOT cover (it fails `BarInvariant`), so "canonical" there is not proved canonicity. Record: [`2026-10-11-atom-word-provenance.md`](../../docs/audits/2026-10-11-atom-word-provenance.md).

## 2026-11-15 — four-strand doublet candidates priced under the ruled functional (branch claude/qbeta-delta-doublet-candidates-2026-11-15, bc6872c35)

Probe `computations/probes/qbeta_delta_doublet/delta_doublet_candidates_probe.py` (ALL PASS, exact over Q(q), calibrated on the H_3 ruled base 0.444700408522 MeV). Candidates taken as given from the doublet thread (labels A = sigma_3 lines, B = J_4 lines on sigma_1's left line) and the SM thread's reading-3 passing gamma-gamma words (000, 111, 0101, 1010, all orientations). Delta = YWY - XWX; |eps| does not depend on which state is n.

- Label A: all 48 overshoot, Q in [1.006, 2.397] MeV (F_required in [0.326, 0.778]).
- Label B: all 48 undershoot, Q in [0.0087, 0.4607] MeV (F_required >= 1.698), 4 with eps = 0.
- Every p-state and n-state passes reading 3 at strand counts 3 and 4.

Scope (a). Nothing selected. Label B is outside the cos <= 1 ladder cap, exactly as the H_3 ruled base is. Label A is inside it, but only with the ladder phase alpha chosen, which is a fit until alpha is derived (qou-pdix). The word choice within a label stays open. Bean stays open (rule 13a).


## 2026-11-15 — route 3 (γγ + reading-3 element search): the Hecke side cannot carry n vs p

The owner chose route 3 to replace nuc11, as part of the m_n / Q_β factor question (bean qou-cds1). This synthesises existing results; no new compute was run.

- **3 strands:** the γγ nucleon is Vᵐ, and only V³ and V⁶ pass reading 3 at every level (h2_gg_atom, PR #7741 results.md). The proton and neutron are the **same word**, so Δ = n − p = 0. Any linear ε then gives ε(Δ) = 0, so Q_β = 0. This is exact, within that family.
- **4 strands:** many γγ words pass (#8046 / gg_four_strand). But PR #7975 (sorry-free) shows Hecke elements commute with the U_q action, so **no braid word and no weak vertex changes T³**. Neither J₄ state is n or p. Assigning "neutron" and "proton" to two passing words would be a label choice, and making it by Q_β would be a fit.
- **Verdict, scope (a)+(b):** inside the Hecke algebra the element search cannot produce a flavour-distinguished pair. The invariant is #7975's commutation. So the factor question merges into what ε means: flavour (T³) lives on the U_q / weight side of Schur–Weyl, not in the word. The candidate taken to the owner is a weight-graded split of the rank-2 (convention D) quantum trace into T³ = ∓½ parts. It is not derived here.

## 2026-11-15 22:45Z — weak-vertex thread: structure of Δ_S and one candidate ε (DIAGNOSTIC, not selected)
Handed over by the c_k thread (owner card 22:30Z). Exact sympy on (C²)^⊗3, Jimbo Ř, convention-D K.
1. **Derived identity:** Δ_S = (h²/2)·1 − (h/2)(σ₁+σ₂) = −(q·h·[2]/4)·(W₁ + W₂), with W_i = q⁻¹J_i the corpus weak vertex on crossing i (prop:weak-vertex-left-projector). So the Q_β element is already the weak vertex summed over the two crossings. Since W ∈ span{1,σ} commutes with E, F, K, every trace ε(Δ_S) is T³-blind, consistent with PR #7975.
2. **Candidate ε_B (emission reading B, #7998):** replace each W_i by its Ř coefficient b = 2/(q[2]), the W⁻ emission amplitude from coev pair creation (#7973, #7977). Then ε_B(Δ_S) = −(q h [2]/4)·2b = −h exactly. Q = h·E₀·m_e = m_e(q+1)/q² = 0.875123 MeV at q₀, +11.861 % vs CODATA. Factor over the z_D base: F = 2q(q²+1)/(q⁴+1) = 1.96789 (required 1.75924 order-zero E₀).
**Contamination:** I found ε_B analytically and saw its value before writing this note; it was not pre-registered. Choices inside it: reading B (open on qou-g0jn), the W ansatz plus the owner's definition of left, and the existing Δ_S. It does not see the nucleon word (V³) and does not separate n from p. Scope (a). Not a selection; scoring is diagnostic only.


## PRE-REGISTRATION ε-W1 (2026-11-15 22:36Z, before computing) — word-level ε from the emission process
Requested by the c_k thread; owner card on the weak-vertex thread pending (recommended 'both, word-level first'). Space (C²)^⊗3 ⊗ V ⊗ V* as in #7981. Jimbo Ř 'std', K = diag(q, q⁻¹), u = e₁. Initial state N ⊗ coev₄₅ (plain coev Σᵢ eᵢ⊗eᵢ), with N ∈ {|udd⟩; |udd⟩+|dud⟩+|ddu⟩ (T³ = −½ weight space, equal K weights)}. Apply X on quark strands, then the emission crossing Ř on strands (3,4) (#7973 arm A). A(X) = sum of components on {two u, one d on 1–3} ⊗ (d on 4, u on 5).
Quantities: A(Δ_S·V³), A(V³), and ε_W := A(Δ_S·V³)/A(V³) (per-emission normalisation). Q = |ε_W|·E₀·m_e, E₀ = 1/(q(q−1)). Also the same with V⁶. Reported exactly and at q₀.
Prediction (stated before running, no number): if ε_W = −h for both N and both words, reading B's word-blindness holds at word level and the candidate is just ε_B again. Any other value is reported as found. Not a selector; scored as a diagnostic only. Not scored against the required factor for choosing between variants.


## RESULT ε-W1 (2026-11-15 22:45Z)
Identity check passes: Δ_S = −(q h [2]/4)(W₁+W₂) (8×8, exact). ε_W = A(Δ_S·Vᵏ)/A(Vᵏ) at q₀: V³ |udd⟩ −0.209475 (Q 0.876858 MeV, +12.08 %); V³ T³=−½ sum −0.204726 (0.856981, +9.54 %); V⁶ |udd⟩ −0.221471 (0.927074, +18.50 %); V⁶ sum −0.205606 (0.860665, +10.01 %). −h = −0.209061. Prediction (ε_W = −h everywhere) FAILED: the emission step sees the word and the state. The neutron-state choice moves Q by up to 8 %, and nothing in the corpus fixes it, so no row is selectable. Probe computations/probes/word_level_epsilon_probe.py. Diagnostic only.


### PRE-REGISTRATION ε-NP1 (2026-11-15 22:45Z, owner pick 'Both, compare first')
Question: does the emission step break n↔p symmetry? Δ_S = −(q h [2]/4)(W₁+W₂) is T³-blind inside H₃, so any asymmetry must come from the state plus the emission crossing.
Setup: same as ε-W1 (computations/probes/word_level_epsilon_probe.py). n→p: start |udd⟩ or the T³=−½ sum, project onto (two u, one d) ⊗ (d on 4, u on 5). p→n mirror: start |uud⟩ or the T³=+½ sum, project onto (one u, two d) ⊗ (u on 4, d on 5). Words V³ and V⁶; same Δ_S; same Ř on (3,4).
Report for each word and state pair: ε_np, ε_pn, ratio ε_pn/ε_np (exact), plus check whether ε_pn(q) = ε_np(q⁻¹) (the u↔d flip).
Prediction (H0): ε_pn = ε_np exactly (no asymmetry from emission). Alternative H1: they are related by q→q⁻¹ only. Anything else is reported as found.
Scope: structural only. There is no measured p→n width to score against, so nothing is compared to data and no row is selected.


### PRE-REGISTRATION ε-TW1 (2026-11-15 22:46Z, owner: 'ΔS followed by something like 1⊗twist ... like the involution?')
Same process as ε-NP1. The new element is X·Δ_S, where X is applied after Δ_S and before the emission crossing (X is in the numerator only): ε_X = A(X·Δ_S·V^k)/A(V^k).
X candidates, all fixed before computing:
(1) T23 = Ř² on quark strands 2,3 (the ribbon twist on V⊗V, without the θ_V² scalar);
(2) J23 = P₊ − P₋ on strands 2,3 (the involution, J² = 1);
(3) F3 = the u↔d flip on quark strand 3 (the emitting strand);
(4) Fall = the u↔d flip on all three quark strands;
(5) F4 = the u↔d flip on the emitted strand 4, applied after the crossing.
Words V³ and V⁶; both state choices; both n→p and p→n.
No numerical prediction. Nothing is selected by closeness to −h or to CODATA. Q at q₀ is shown for display only.


### RESULT ε-NP1 (2026-11-15 22:58Z), np_emission_asymmetry_probe.py
H0 (ε_pn = ε_np) FAILS and H1 (ε_pn(q) = ε_np(1/q)) FAILS for all four (word, state) pairs. Emission does break n↔p.
- T³ sums: ratio ε_pn/ε_np at q₀ = 1.0446 (V³), 1.0353 (V⁶). Near q=1 it is 1 + (q−1)/2 + O((q−1)²).
- Single states |udd⟩ vs |uud⟩: ratio 29.7 (V³), 12.1 (V⁶), because the p→n amplitude without Δ_S nearly vanishes. Caveat: |uud⟩ is not the u↔d image of |udd⟩ (that would be |duu⟩). This is recorded as pre-registered, not changed afterwards.
So the size of the asymmetry depends on the free state choice.

### RESULT ε-TW1 (2026-11-15 22:58Z), twist_involution_epsilon_probe.py
- The flips F3, Fall and F4 give ε = 0 in every case. A u↔d flip changes the charge content, so the charge-projected amplitude vanishes. A flip is only meaningful with the projection flipped too, and that is just the n↔p map.
- T23 (Ř² on strands 2,3) raises |ε| in both directions. The n→p over p→n ratio stays near 1.05.
- J23 (the involution P₊−P₋ on strands 2,3), T³ sums: ε_np = −0.198078 (V³), −0.198057 (V⁶); ε_pn = −0.219804, −0.219591. Exact series: ε_pn/ε_np = q − 22(q−1)⁵ + … (V³) and q − 92(q−1)⁵ + … (V⁶). It matches q through order (q−1)⁴, but it is NOT equal to q, and the deviation coefficient grows with word length. At q₀ the ratio is 1.10968 (V³) and 1.10873 (V⁶), against q₀ = 1.10998.
- Q values at q₀ are display only; none is selected.


### PRE-REGISTRATION ε-N1 and ε-J1 (2026-11-15 23:05Z; owner 'go' via coordinator; PR #8068 holds ε-W1/NP1/TW1)
**ε-N1: which T³ = −½ vector is the neutron?** Rule: the vector must be fixed by a corpus construction (U_q(sl₂) isospin, Schur–Weyl, γγ pair creation), never by matching data.
Step 1 (forced): the nucleon has isospin ½, so it lies in the (2,1) isotypic part of V^⊗3 at T³ = −½, which has dimension 2. NOTE: the 'T3 sum' state used in ε-W1/NP1/TW1, |udd⟩+|dud⟩+|ddu⟩, is the classical symmetric vector. At q = 1 it is pure isospin 3/2 (the Δ⁰), and at q ≠ 1 it is not even a U_q weight-space eigenvector of the Casimir. So those rows are NOT neutron rows.
Step 2: compute the T = ½ subspace at T³ = −½ exactly, as the kernel of the U_q(sl₂) raising operator E restricted to that weight (the coproduct convention matching Ř 'std'). Report ε_np for a general vector in that 2-dim space, as a rational function of the multiplicity coordinate.
Step 3: grep the corpus for a construction that fixes the multiplicity vector (γγ pair creation; seminormal basis; diquark channel). If one is found, cite it and evaluate. If none is found, report the family and say the choice is open.
Prediction: ε_np depends on the multiplicity coordinate (it is not constant on the 2-dim space).
**ε-J1: why does J give ε_pn/ε_np ≈ q?** Compute the J23-dressed ratio for words V⁰ (none), V¹ and V² as well as V³ and V⁶, on the same (pre-registered, |udd⟩/|uud⟩ and sum) states. Prediction: with no word (V⁰) the ratio is exactly q, and the (q−1)⁵ deviation comes from the word. If V⁰ is not exactly q, report as found.


### RESULT ε-N1 and ε-J1 (2026-11-15 23:25Z), neutron_vector_epsilon_probe.py
**ε-N1.** The T=½ neutron space at T³=−½ is ker F (Δ(F) = F⊗1 + K⁻¹⊗F, which commutes with Ř std). It is spanned by n_A = [ud]₁₂⊗d and n_B = d⊗[ud]₂₃. The old states |udd⟩ and the symmetric sum are NOT in it (checked). Prediction (ε depends on the multiplicity coordinate t) CONFIRMED, and strongly so. ε_np at q₀, with no extra element:

| | n_A (t=0) | n_B | t=1 | t=−1 |
|---|---|---|---|---|
| V³ | −6.390 | −0.0184 | −0.114 | +0.080 |
| V⁶ | +1.423 | −0.0261 | −0.125 | +0.061 |

It even changes sign and changes with the word. Conclusion: the word-level ratio ε = A(Δ_S·Vᵏn)/A(Vᵏn) is not a stable functional on T=½ neutron states. The ≈ −h values of ε-W1 belonged to non-isospin states. A quick corpus grep (QuarkState/, eightfold, h3 idempotents) found no construction that fixes t, so the choice is OPEN, and that is a shallow grep, not a full corpus-grep.
**ε-J1.** Prediction CONFIRMED: with no word (V⁰), on the symmetric sum states, ε_pn/ε_np = q exactly. ε_np = −(q−1)(q+1)⁴/(4q²(q²+1)) and ε_pn = q·ε_np. The single state has a zero amplitude at V⁰. For V¹ and V² the ratio departs from q at FIRST order (ratio − q = −(3/2)(q−1) + …), so ≈ q is not generic. V³ and V⁶ return to agreement through (q−1)⁴. Mechanism at V⁰: the p→n channel has one more power of q from the K-weights of the emitted pair, and J does not change it. The return at V³ and V⁶ is unexplained (it may be because the word length is a multiple of 3).


### PRE-REGISTRATION ε-TR1 (2026-11-15 23:32Z): remove the neutron-vector choice by a trace
The emission projections are taken over isospin-½ states.
- At T³ = +½, the weight space splits canonically into the T=½ part, span{p_A, p_B} = E·span{n_A, n_B}, and the T=3/2 line F₃·uuu.
- Let π be the projection onto the T=½ part along the T=3/2 line, with coordinates in the basis p_A, p_B.
- Define the 2×2 matrix M(X)_{ij} = coordinate i of π[(quark part of) the component on pair (d on 4, u on 5) of Ř₃₄·X·Vᵏ·(n_j ⊗ coev)].
- ε_tr = Tr M(Δ_S) / Tr M(1). It is independent of the basis of the multiplicity space.
- p→n is the mirror: start p_j; final projection onto the T=½ part at T³ = −½ along F₃²·uuu, in the basis n_A, n_B; pair (u on 4, d on 5).
Words V⁰, V³, V⁶; X = none and J23.
Questions: is ε_tr stable across words, and what is ε_tr,pn/ε_tr,np? No numerical prediction. Nothing compared to data.


### RESULT ε-TR1 (2026-11-15 23:45Z), multiplicity_trace_epsilon_probe.py
With the neutron-vector choice traced out over the isospin-½ multiplicity space, **ε_tr,pn = ε_tr,np EXACTLY**, as rational functions in q, for V⁰, V³ and V⁶, with and without J23. Tr M(1) is also identical in both directions.
- V⁰: ε_tr = (q−1)(q+1)(q²+1)/(2(q⁴+1)) = 0.10285 at q₀; with J23 it is −(q²−1)/(2(q²+1)) = −0.05198.
- V³ gives 0.11369, V⁶ gives 0.12406 (with J23: −0.04651, −0.04126). So ε_tr is word-dependent, not −h, and not stable in k.
Reading: every n↔p asymmetry seen in ε-NP1, ε-TW1 and ε-N1 came from states that are not U_q-isospin-covariant, or from a choice of multiplicity vector. On canonically traced isospin-½ states, Δ_S plus this emission is n↔p symmetric. That is consistent with a Wigner–Eckart reduction, but the symmetry is not proved here. So this route does not break the n–p asymmetry. A source of asymmetry has to be non-U_q-covariant (e.g. electric charge or the external field), scope (a).


### PRE-REGISTRATION ε-EM1 (2026-11-15 23:40Z; owner 'keep pushing', coordinator: n–p break via a non-U_q-covariant ingredient)
Corpus status, checked first:
- Hypercharge Y is OPEN (eightfold-open-problems; strand-twist-datum is a free label).
- The derivation-chain thread's EM1 (/mnt/project-files/qou-derivation-chain/bridge-b/em1_result.md) did static photon exchange inside the nucleon, with Y = 1/3 imported. Result: the classical −2/3 plus an O(h⁴) braid correction.
- My distinct angle: Coulomb exchange in the DECAY's intermediate state, before the emission crossing, where the created pair is still a superposition, so the charge operator does not reduce to a scalar. Y is kept as a SYMBOL, not imported.
Setup: as in ε-TR1, with the trace over the isospin-½ multiplicity space. Charge per strand: Q = T³ + Y/2 on V (strands 1–4), and Q = −(T³ + Y/2) of the index on the V* strand 5. X = Σ_{a<b≤5} Q_a Q_b (diagonal), inserted after Δ_S and before Ř₃₄. Report the first-order shift δε = d/dg [Tr M(Δ_S then 1+gX) / Tr M(1)] at g=0 for n→p and p→n, as exact functions of (q, Y), for words V⁰, V³ and V⁶.
Questions: (i) is δε_np ≠ δε_pn? (ii) Which part is Y-independent? (iii) Does the asymmetry survive at q = 1 (classical) or vanish there?
Prediction: the asymmetry is nonzero. At q = 1 it reduces to classical charge algebra (as in EM1), and the braid adds corrections. No coupling value is chosen and nothing is compared to data.


### RESULT ε-EM1 (2026-11-15 23:50Z), coulomb_in_decay_epsilon_probe.py
With the Coulomb insertion X = Σ_{a<b≤5} Q_aQ_b between Δ_S and the emission crossing, traced over the isospin-½ space:
- δε/ε = (Y² − 2Y − 1)/2 for n→p, and (Y² + 2Y − 1)/2 for p→n.
- These are EXACTLY independent of q and of the word (V⁰, V³, V⁶).
- Asymmetry = 2Y exactly. It is zero at Y = 0.
Prediction (i) holds only for Y ≠ 0. Prediction (iii) 'the braid adds corrections' FAILS: in this placement the braid adds nothing, and the charge enters as pure classical charge algebra (the Y·T³ cross term).
Reading (scope a): on canonically traced isospin-½ states, the whole n↔p asymmetry this route can produce is carried by the hypercharge Y, linearly. Since Y is OPEN in the corpus (eightfold-open-problems; conj:sm-hypercharge-invariant; strand-twist-datum is a free label), the n–p break via charge is gated on deriving Y. It is not gated on the braid.


### PRE-REGISTRATION ε-Y1 (2026-11-16 00:05Z; route chosen: "Derive Y from colour", the stated default on the open card)
Hypothesis under test: the source is the untested line in bean qou-sl3f, "the stripped u1 factor q^(1/N) per crossing reads as baryon number 1/N per quark".
Setup:
- Jimbo gl_N R on V⊗V versus sl_N R. The ratio is the u1 factor.
- Model a U(1) braiding with charges a, b as q^(c·a·b). Here c is the pairing normalisation and is NOT chosen in advance.
Questions:
- (i) Does the u1 factor fix a alone, or only the product c·a²?
- (ii) What does singlet transparency (V around Λ^N V) add to (i): an independent constraint, or the same one?
- (iii) Which further input, if any, sets a = 1/N?
- (iv) Is that input data, a convention, or a derived fact?
- (v) Does a = 1/N give Y = 1/3 for the quark doublet in the ε-EM1 convention Q = T³ + Y/2? Or does that need Y = B − L, which brings in lepton-sector input?
Prediction: (i) only c·a² is fixed; (ii) it is the same constraint; (iii) a lattice normalisation "the baryon Λ^N V has unit charge" is needed. So the route gives the RATIO quark : baryon = 1 : N categorically, while Y = B for quarks stays an identification.
No value of Y is compared to data. The δε numbers at Y = 1/3 are reported only as consequences.


### RESULT ε-Y1 (2026-11-16 00:15Z), colour_hypercharge_y1_probe.py (exact sympy, N = 2, 3)
- Every prediction held.
- (i) The u1 factor of gl_N over sl_N on V⊗V is q^(1/N) per crossing. In a U(1) braiding q^(c·a·b) this fixes only c·a² = 1/N, not a.
- (ii) The gl_N monodromy of V around Λ^N V is q² (computed for N = 2, 3, matching qou-sl3f). Given (i), it is REDUNDANT: 2c·a·(N a) = 2N·c a² = 2. So it adds no constraint.
- (iii) Both constraints keep the scale freedom (a, c) → (λa, c/λ²). So a = 1/N needs one more input: the lattice normalisation "Λ^N V carries unit charge".
- (iv) That input is a normalisation convention (the primitive generator of the charge lattice), not data. Colour does derive the RATIO quark : baryon = 1 : N.
- (v) Reaching Y = 1/3 in ε-EM1's convention Q = T³ + Y/2 needs two things that are not derived:
  - that this colour u1 IS hypercharge;
  - Y = B − L with L = 0 for quarks (lepton-sector input).
- So the hypothesis in qou-sl3f is confirmed only as "baryon number 1/N given unit-charge normalisation". Y stays OPEN (scope a).
- Consequence only, not a prediction: at Y = 1/3, ε-EM1 gives δε/ε = −7/9 (n→p) and −1/9 (p→n), with asymmetry 2/3. These are O(1) because X carries no coupling constant. They are not physical magnitudes.
- Next honest options:
  - (a) derive the u1 ↔ hypercharge identification, e.g. from the strand-twist datum or the anomaly-free trace condition, without importing lepton charges;
  - (b) use only the colour-fixed ratio and accept Y as a labelled open input.


### PRE-REGISTRATION ε-Y2 (2026-11-16 06:40Z; owner tapped "Derive Y from colour" after ε-Y1, so the remaining step is pursued)
Goal: derive the colour-u1 ↔ hypercharge identification that ε-Y1 left open, without importing lepton charges.
Steps:
1. Corpus check first: strand-twist-datum, conj:sm-hypercharge-invariant, eightfold-open-problems, QuarkStrandConsequences (integer charge ⟺ triality zero).
2. Test whether "integer charge ⟺ triality zero", applied with the colour-fixed ratio (quark : baryon = 1 : N), forces Q − T³ ≡ B mod ℤ on quark strands. That would fix Y/2 = B/2 mod integers.
3. Report the residual freedom; do not pick from it.
No data, and no lepton charges as input.


### RESULT ε-Y2 (2026-11-16 06:55Z), triality_hypercharge_y2_probe.py (exact Fractions)
- Input: the principle "total charge ∈ ℤ ⟺ (n_q − n_q̄) ≡ 0 mod 3" on all quark and antiquark strand lists up to length 6, with Q = T³ + Y/2.
- This principle is the reverse of QuarkStrandConsequences Result 2. It is a physical input (colour confinement plus charge quantisation), NOT derived from the braid.
- Output: the solution set is exactly Y ∈ ±1/3 + 2ℤ (scan k/36, |Y| ≤ 4).
- Residual freedom has two parts:
  - (a) the sign. Y → −Y is charge conjugation (V ↔ V*: which strand is called the quark). A labelling convention.
  - (b) an integer shift Y → Y + 2k. Nothing here fixes k = 0. Taking the minimal |Y| = 1/3 would be a choice, and is NOT made here.
- Combined with ε-Y1, colour plus triality give Y ≡ ±B (mod 2) for the quark doublet, with B = 1/3. The value 1/3 itself needs the minimality choice, or a further structure that picks k.
- So Y is constrained but NOT derived (scope a). The ε-EM1 asymmetry 2Y is fixed up to sign and an even-integer shift: 2/3 at the minimal choice.


### NOTE ε-Y3 (2026-11-16 06:50Z), corpus check for the even shift k
- Anomaly cancellation cannot fix k from quarks alone: every U(1)_Y anomaly that involves the left doublet's Y also needs the lepton content.
- The strand-twist datum (def:strand-twist-datum) does fix k, but only under a bound. Its candidate Y_t = 2(T/3 − I₃), with T the total twist of three sub-strands, gives the following for a doublet with T_u − T_d = 3 and fractional Q:
  - per-strand bound |t_i| ≤ 1: Y ∈ {−1/3, +1/3}, so k = 0;
  - bound |t_i| ≤ 2: Y ∈ {±1/3, ±5/3, ±7/3}.
- So k = 0 is equivalent to the helon bound |t_i| ≤ 1, which is imported (bilson-thompson2005). The datum itself is t: {1..n} → ℤ and is unbounded.
- Also, Q_twist = Q is the defining equation (TwistBatteryVacuity), not a test.
- Status: Y = ±1/3 is CONDITIONAL on the helon twist bound. The sign is a convention (C). Y stays OPEN until the bound |t_i| ≤ 1 is derived, e.g. from a ribbon-twist eigenvalue constraint.


### NOTE ε-Y4 (2026-11-16 07:10Z), where the helon twist bound comes from (owner: "try derive twist bound")
Source (held in the library: arxiv-hep-ph-0503213v2, §2):
- A helon is a PAIR of tweedles, each a ±π half-twist ("Unordered pairing").
- So the helon twist is +2π, 0 or −2π, i.e. |t_i| ≤ 1. The bound is a consequence of "a strand carries exactly two half-twists". It is not an independent axiom.
Categorical translation (proposal, not proved):
- a half-twist ±π corresponds to one Hecke letter σ^{±1} (two eigen-channels only);
- a helon corresponds to a two-letter unit;
- the corpus γγ rule already gives words of even length (gammaGamma_length_even), and the gluon unit is V = σ₀σ₁⁻¹.
- If each strand's twist datum = the exponent sum of ONE γγ two-letter unit, then t_i ∈ {−2, 0, 2}/2 = {−1, 0, 1}, and ε-Y3 gives Y = ±1/3.
Remaining assumption: "one γγ unit per strand". This is a minimality statement, the same kind of choice as k = 0. So the bound is MOVED onto the γγ construction, not yet derived. A derivation would need the γγ pair-production construction to put exactly one pair on each strand.


### RESULT ε-Y5 (2026-11-16 07:20Z): the γγ route to the twist bound is EXCLUDED
- The ε-Y4 proposal ("a strand's twist = exponent sum of one γγ two-letter unit") fails structurally.
- vertex i = [σ_i, σ_{i+1}⁻¹] has writhe 0 (QOU.Mass.GammaGammaWordSelection.writhe_vertex), and every γγ word has writhe 0 (writhe_eq_zero, sorry-free).
- Any ADDITIVE attribution of crossing signs to strands gives a total Σt_i that is a multiple of the writhe. So on γγ words T = 0, hence Q_twist = 0, for every strand assignment.
- A fractional quark charge needs T ≠ 0, so the twist datum of a charged strand cannot come from γγ letters at all. Scope (b), invariant: writhe_eq_zero.
- This agrees with def:strand-twist-datum, which calls the datum "an independent label, not the ambient twist".
- Status: the bound |t_i| ≤ 1 is NOT derivable on this route. Y = ±1/3 stays conditional on the imported helon bound (two ±π tweedles per strand). Y stays OPEN.


### LABEL (owner tap 2026-11-16 07:06Z "Label Y, switch to element")
Y = ±1/3 for the quark doublet is recorded as a LABELLED CONDITIONAL INPUT. Its conditions: the triality principle (ε-Y2) and the helon twist bound |t_i| ≤ 1 (arxiv-hep-ph-0503213v2). The sign is a C-convention. Y is not derived. Work moves to the nucleon element choice.


### RESULT ε-Y6 (2026-11-16 07:15Z; owner "and B": ribbon-twist route too)
- Treat a helon as a 2-strand ribbon of V⊗V, and read its twist as the exponent in units of q² of the full-twist monodromy Ř^{2k}.
- Exact eigenvalues (gl_2 Jimbo): Ř² has q² (×3, symmetric) and q⁻² (×1, antisymmetric). Ř^{2k} has q^{±2k}.
- So ONE full twist gives t ∈ {+1 (sym), −1 (antisym)}, and no twist gives 0: exactly the helon set {UU, EE, UE}. As a bonus, the twist SIGN is tied to the symmetry channel.
- But Ř^{2k} gives ±k, and nothing in the braiding bounds k.
- Verdict: like the γγ route, this moves the bound onto a minimality statement ("at most one full twist per helon"); it does not derive it. Scope (a). Y stays a labelled conditional input.


### FINDING ε-Y7 (2026-11-16 07:25Z; owner asked: "are we missing ribbon twist in γγ setup? does it come from 3rd term in photon?")
Yes, there is a mismatch inside the corpus.
- The Lean γγ grammar (GammaGammaWordSelection.vertex i = [σ_i, σ_{i+1}⁻¹]) keeps only writhe-0 vertices, so every γγ word has writhe 0.
- The corpus's own photon blocks give the photon a twist channel:
  - trivial-knot-photon-interpretation says "the photon's internal twist is inherently positive (L₊)" and "electrons cannot emerge from photons lacking twist content";
  - breit-wheeler-vertex says σ₀·σ₁ = L₊ (the Hopf link, writhe +2), then L₊·σ₀ = e⁻ (writhe 3), with the mirror L₋ for e⁺.
- So the photon has two linear channels (σ₀, σ₁) and a third, twist-carrying Hopf channel L± (writhe ±2 = one full twist). The Lean γγ vertex omits that third channel.
- Consequence for Y: if each photon carries twist content in {L₊, none, L₋} = {+1, 0, −1} full twists, and a strand's twist datum is supplied by ONE photon, then |t_i| ≤ 1 follows. That is the helon bound, with each photon playing the tweedle pair.
- It still rests on "one photon per strand", but that is how pair production naturally counts, not a free minimality choice.
- Caveat: adding L± to the γγ rule changes an owner-ruled grammar (qou-ales). The writhe-0, reading-3 and element results (V³, V⁶; the trefoil electron as the non-γγ blocker) would all need re-checking. Owner decision.


### PRE-REGISTRATION ε-L1 (2026-11-16 07:30Z; owner tap: test the γγ grammar with the photon twist channel L±)
- Extended grammar units:
  - the existing V = σ₁σ₂⁻¹ (writhe 0);
  - L₊ = σ₁σ₂ (writhe +2), from breit-wheeler-vertex;
  - L₋ = σ₁⁻¹σ₂⁻¹.
- Words to test on the ε-TR1 traced setup (isospin-½ multiplicity trace, Δ_S, emission Ř₃₄):
  - L₊, L₋, L₊V³, V³L₊, L₊L₋;
  - the Breit–Wheeler electron-type word L₊σ₁ = σ₁σ₂σ₁.
- Questions:
  - (i) does any word give ε_pn ≠ ε_np, i.e. break u↔d?
  - (ii) does the twist content per photon lie in {−1, 0, +1} full twists, so that |t| ≤ 1 follows from one photon per strand?
  - (iii) reading 3 on the nucleon words with L±: which pass?
- Prediction for (i): NO breaking. Every Ř word commutes with the U_q(sl₂) action, so on canonically traced isospin-½ states n↔p symmetry should hold whatever the writhe, exactly as in ε-TR1.
- Prediction for (ii): yes by construction (writhe ±2 per unit).
- Nothing is compared to data, and no element is picked by residual.


### RESULT ε-L1 (2026-11-16 07:40Z), gg_twist_channel_np_probe.py (exact over Q(q))
- (i) NO breaking, as predicted. For L₊, L₋, L₊V³, V³L₊, L₊L₋ and the electron-type σ₁σ₂σ₁ (writhe 2, −2, 2, 2, 0, 3), ε_tr,pn = ε_tr,np exactly, and Tr M(1) is identical in both directions.
- Reading: the twist channel changes ε's value (L₊: −(q²−1)(q⁴+1)/(2q⁶) = −0.156 at q₀; L₋: −0.292; the e-type word: +0.106) but not its n↔p symmetry. Every Ř word is U_q(sl₂)-covariant, so adding writhe does not help.
- Conclusion, scope (a) on these six words: L± does NOT break u↔d. The break still needs a non-U_q-covariant ingredient, which so far is the hypercharge (ε-EM1: asymmetry 2Y).
- (ii) L± supplies twist ±1 per photon, so one photon per strand gives |t| ≤ 1 and hence Y = ±1/3 (ε-Y3/Y7). This is the only place the twist channel matters for n–p: through Y, not through the braid. L₊ being "inherently positive" (trivial-knot-photon-interpretation) would also fix the SIGN of Y, if that statement is derived. It is currently prose.
- (iii) Reading 3 on L± nucleon words: NOT run here. It belongs to the γγ-grammar owner (colour/gluon thread).
- No mass or compute change. The element choice is unaffected.


### NOTE (2026-11-16 07:32Z), from the thread "Pin down what ε means for Q_β"
- On Δ_S = −(h[2]/4)(J₁ + J₂) (Lean: QuarkState/DeltaSIsWeakVertexSum.lean, merged) we have χ₍₂,₁₎(Δ_S) = 0. So every block-weighted trace gives τ(Δ_S) = −(h[2]/2)(y₃ − y₁₁₁) = −(h[2]/2)τ(J).
- The ε question on Δ_S is therefore the single chirality expectation τ(P_L) − τ(P_R):
  - augmentation: y₃ = 1, +12.47 %;
  - z_D: y₃ = (q⁴+1)/(q²+1)², −43.16 %.
- The long elements nuc9 and nuc11 have χ₍₂,₁₎ ≠ 0, so for them ε is affine in y₃.
- The AME-implied y₃ = 0.889 is recorded as a TARGET only, never a selector. Their probe: /mnt/project-files/qou-qbeta-epsilon/qbeta_epsilon_chirality_reduction_probe.py.


### NOTE (2026-11-16 07:35Z), from the crossing-energy thread (PR #8108; /mnt/project-files/qou-crossing-energy/result-pn-mirror-gg-walk.md)
Setting: H₃, convention D, exact.
- The only mirror fixing the γγ vertex σ₀σ₁⁻¹ is M = bar ∘ flip ∘ reverse, which acts as bar on traces.
- The γγ core (σ₀σ₁⁻¹)³ is M-fixed and bar-even.
- Full p and n are NOT mirrors. Their quark blocks form a partial mirror:
  - χ₃(q_n) = bar χ₃(q_p) exactly;
  - in (2,1) both bar-even parts are 0, and the bar-odd parts differ by exactly −h/2.
- So the element asymmetry sits only in the (2,1) sector, as a −h/2 shift, and lies in the 5 non-γγ letters.
- Relevance to the element choice: any rule fixing the quark block decides the (2,1) shift. Since χ₍₂,₁₎(Δ_S) = 0 (ε thread), the short element Δ_S does not see it, while nuc9 and nuc11 do. bar is semilinear, so F₃-commutation (Bridge B) does not apply to it directly.

### NOTE 2026-11-16 — gluon thread stage 1 (L± in the reading-3 re-check), relayed
Over 5,460 words of length 1–6 in {V, V⁻¹, L₊, L₋}: a word passes reading 3 iff it is a pure braid (1,778 pass, 3,682 knots fail). Adding L± changes character SIZES (L₊³ lowest char 1, L₋³ 0.5347), not pass/fail; no knot passes, so the trefoil electron is still not γγ-reachable. For this bean: L± is F₃-covariant (ε-L1), so it cannot be the n–p break, and it does not rescue nuc11's (2,1) failure. Stage 2 (H₂, V³/V⁶ + length-2 chiral electrons) pending. Adding L± to the rule stays the user's ruling.

### NOTE 2026-11-16 — gluon thread stage 2 (PR #8128), relayed
H₂ with nucleon V³/V⁶ × four chiral length-2 electrons (σ₁²=V⁻¹L₊, V⁻¹L₋, L₊V⁻¹, L₋V⁻¹): bare molecule passes reading 3 in all 16 cells; V³ bond passes everywhere. Trefoil fails reading 3 at every q, alone and in composites; its negative trace is forced by the Hecke relation (only a z=q truncation removes it). Handed-electron candidates = pure braids with nonzero writhe. No effect on the n–p break (all F₃-covariant) or on the nucleon element choice.

### NOTE 2026-11-16 — y₃ result, re-measured (PR #8130 probe, 15/15 pass, 60 dps, proton pin)
ε on a block-weighted trace on the normalised convention-D line (y₁₁₁ = 0, y₂₁ = (1−y₃)/2) is affine in y₃. Values for the convention-D weight y₃(z_D) = (q⁴+1)/(q²+1)² = 0.505404226504 and the augmentation y₃ = 1:

| element | χ₍₂,₁₎ | E₀ | z_D | augmentation | y₃ that would give AME |
|---|---|---|---|---|---|
| Δ_S | 0 | order zero | −43.157 % | +12.470 % | 0.889126 |
| Δ_S | 0 | tower (#8124) | −42.594 % | +13.585 % | 0.880397 |
| nuc9 | −0.0900 | tower | −30.252 % | +14.204 % | 0.841972 |
| nuc11_interleaved | −0.0914 | tower | −16.678 % | +40.705 % | 0.649154 |
| nuc11_gen_grouped | −0.1068 | tower | −14.613 % | +40.705 % | 0.636059 |

- The "y₃ for AME" column is diagnostic only. It is obtained by inverting the target, so it is a fit and may not select a functional or a weight (§NO FITTING). No derived trace on record has y₃ near 0.88. The two derived points, z_D (0.505) and the augmentation (1), are on either side of it.
- The ruled base (2026-09-08: z_D, tower E₀) on Δ_S gives Q_β = 0.4491 MeV, −42.59 % (#8124).
- Open, and the reason this bean stays open: what decides y₃ (equivalently the chirality expectation τ(P_L) − τ(P_R)) from the corpus, and the element choice (nuc11 fails reading-3 confinement on (2,1)).
- Five blocks still print the superseded order-zero 0.4447 MeV: epistemic-status-of-calibrations, mass-comparison-table, three-calibration-discipline-remark, np-discrepancy-resolution, q-beta-over-e0-classical-vanishing-ladder-reading. q-beta-c-2-eq-neg-one-structural also prints it, but that block is explicitly order-zero.

### NOTE 2026-11-16 — gluon thread stage 2 (PR #8128), relayed
H₂ with nucleon V³/V⁶ × four chiral length-2 electrons (σ₁²=V⁻¹L₊, V⁻¹L₋, L₊V⁻¹, L₋V⁻¹): bare molecule passes reading 3 in all 16 cells; V³ bond passes everywhere. Trefoil fails reading 3 at every q, alone and in composites; its negative trace is forced by the Hecke relation (only a z=q truncation removes it). Handed-electron candidates = pure braids with nonzero writhe. No effect on the n–p break (all F₃-covariant) or on the nucleon element choice.

### NOTE 2026-11-16 09:50Z — thread "Find the n–p break and nucleon element" resumed
- PR #8104 (ε-L1 probe) re-run here: reproduces the committed witness byte-for-byte (exact sympy). Precision gate not examined (qou_substrate absent in container). Merge card posted to the owner.
- Owner card posted: does L± = σ₀σ₁ join the γγ rule (add / keep as is / decide later). Agent recommendation: keep as is (no corpus derivation of L± as a γγ letter; adopting it for its handedness would be selection by outcome). No selection rule is adopted or computed until the owner rules; any rule will be pre-registered here first.
- Status unchanged: n–p break still needs a non-U_q-covariant ingredient beyond the Coulomb/Y insertion; no element rule derived. Bean stays OPEN (open conjecture).

### OWNER RULING 2026-11-16 09:46Z — L± joins the γγ word rule
Owner tapped "Add L± to γγ" (card in thread "Find the n–p break and nucleon element"; agent had recommended keep-as-is). From now on the γγ alphabet is {V, V⁻¹, L₊, L₋} with L± = σ₀σ₁ (resp. inverse). Recorded consequences, NOT yet re-derived:
- Reading 3 then passes exactly the pure braids (gluon thread stage 1); handed (nonzero-writhe) pure words are admissible.
- Δ_S is no longer guaranteed canonical, so Q_β = 0.4491 MeV (#8124) is provisional, and the level-1 "Q_β = 0" prune (GammaGammaSelectedDeltaVanishes.lean) must be re-checked over the enlarged alphabet.
- n–p break: unaffected (every L± word is F₃-covariant, ε-L1 ratio 1).
- Canonical word reselection over the new alphabet is required. Any selection rule will be PRE-REGISTERED here before computing; no element picked by residual; any m_n move flagged in project chat.
Bean stays OPEN.

### CORRECTION 2026-11-16 19:50Z — the L± recommendation was wrong (agent's own error)
The agent recommended "keep the rule as is" on the grounds that "nothing in the corpus derives L± as a γγ letter". False: prop:gamma-gamma-generates-particles (predicted-spectra/gamma-gamma-generates-particles.md) reduces the product of two three-term photons γ = 1 + φ₀σ₀ + φ₁σ₁ with the Hecke relation, and the normal form already contains L₊ = σ₀σ₁ (coefficient φ₀ψ₁) and L₋ = σ₁σ₀ (coefficient φ₁ψ₀). So L± follows from the photon definition applied to γγ; the owner's ruling restores what the definition gives, and the earlier {V, V⁻¹} rule was a truncation of it. Search gap: the agent read the bean history and the trivial-knot remark tables but not this proposition.
Open discrepancy to check: in that proposition L₋ = σ₁σ₀ (writhe +2, opposite ORDER), while the ε-L1 probe (#8104) and the gluon-thread stages used L₋ = σ₀⁻¹σ₁⁻¹ (writhe −2, the INVERSE). ε-L1's conclusion (p/n ratio 1) holds for every Ř word, so it is unaffected; the reading-3 stage results that used L₋ as an inverse need re-checking against L₋ = σ₁σ₀.

### NOTE 2026-11-17 10:50Z — the photon has FOUR terms / three parameters (owner query)
prop:gamma-gamma-generates-particles writes γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁: four terms, three colour parameters (φ₀, φ₁, φ₀₁). The 19:50Z CORRECTION called it "three-term"; that is the block's first reduction step with φ₀₁ = ψ₀₁ = 0, not the definition. Consequences, from the block itself:
- L₊ = σ₀σ₁ is already in a SINGLE photon (the φ₀₁ Hopf-dressing term); L₋ = σ₁σ₀ is not, and arises only from the γγ cross term φ₁ψ₀.
- With φ₀₁ ≠ 0 the γγ product also reaches e⁻ = σ₀σ₁σ₀; the two-photon span is all of H₃(q).
- No `def:` block for the photon exists; the definition lives inside this proposition's prose.
Owner asked (2026-11-17 06:27Z) that the γγ thread re-run stage 1 over the alphabet the definition gives; request relayed.

### PRE-REGISTRATION 2026-11-17 18:15Z — stage 1 re-run, L₋ = σ₁σ₀, four-term photon (γγ thread)
Pre-registered before any computation. Re-run of gluon-thread stage 1 over the alphabet that prop:gamma-gamma-generates-particles gives (owner query 2026-11-17 06:27Z).
- Alphabet (a): {V, V⁻¹, L₊, L₋} with V = σ₀σ₁⁻¹, L₊ = σ₀σ₁, L₋ = σ₁σ₀ (NOT the inverse σ₀⁻¹σ₁⁻¹ used before). All words of length 1..6 on three strands.
- Alphabet (b): (a) plus e⁻ = σ₀σ₁σ₀, reachable from γγ once φ₀₁ ≠ 0. All words of length 1..5.
- Measured: reading 3 (Frobenius positivity, every level, convention D, proton pin, mpmath 40 dps), components, writhe; for each alphabet the pass count, whether pass ⟺ pure braid still holds, the writhe distribution of passers, the shortest passing word of each writhe.
- Old stage-1 table kept as the record for the inverse reading; this run is reported beside it, not in place of it.
- Questions, no predicted answer: 1. Does pass ⟺ pure survive? 2. Are passing writhes still symmetric, or one-signed (all letters except V⁻¹ are positive)? 3. Does adding e⁻ let any knot (1 component) pass?
- Not allowed: choosing a canonical word, letter or length from these results. This run measures admissibility only; selection is a separate, separately pre-registered step.

### RESULT 2026-11-17 — stage 1b (γγ thread, PR #8128, witness gg-twist-reading3-stage1b)
(a) {V, V⁻¹, L₊ = σ₀σ₁, L₋ = σ₁σ₀}, lengths 1–6: pass ⟺ pure braid survives (1848/1848 pure pass, 0/3612 knots). All writhes ≥ 0, which the alphabet forces (L± both +2). (b) Adding e⁻ = σ₀σ₁σ₀, lengths 1–5: every pure word passes and no knot does, but 526/1771 two-component words also pass, so pass ⟺ pure breaks (shortest: V⁻¹L₋e⁻, L₊L₋e⁻). 274 words sit at a numerical zero (~1e-42, sign flips 40→80 dps) and are counted as failures. Admissibility only; no selection. Bean stays OPEN.

## 2026-11-17 — photon audit (PR #8367, issue #8366)

Owner asked for a single `def:photon` block: γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁ ∈ H₃, three colour weights, bare photon = 1 (empty knot, not 0₁). Audit `docs/audits/2026-11-17-photon-usage-audit.md` lists 12 conflicts. **C8 bears on this bean:** the γγ vertex V = σᵢσᵢ₊₁⁻¹ ("photon + anti-photon") traces to `gamma_gamma_pair_production_decomposition.py`, which takes photon = σ₀, anti-photon = σ₁⁻¹. That is not the photon of `def:photon`, so every γγ-selected word (nucleon words included) rests on an underived vertex. Decision card posted 2026-11-17: re-derive the alphabet from γ(φ)γ(ψ) (recommended) vs keep V. Nothing changed yet. Stays open.

## 2026-11-17 sibling sweep
Scope note only (bean stays OPEN): a sibling measured that the reading-3 whole-word search space is about 1024 candidate words. No word selected.
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.

### PRE-REGISTRATION 2026-11-18 04:30Z — canonical-word reselection from γ(φ)γ(ψ) (γγ thread)
Trigger: owner tapped "Re-derive from γ(φ)γ(ψ)" (n–p thread, 2026-11-17 23:18Z), after audit finding C8 (docs/audits/2026-11-17-photon-usage-audit.md): the vertex V = σᵢσᵢ₊₁⁻¹ came from a script that takes photon = σ₀ plus an "anti-photon" σ₁⁻¹, both rejected by def:photon (PR #8367). Written before any computation.

**Expansion (exact, braid words before any Hecke reduction).** With γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁:
- degree 0: 1
- one photon bare (coefficient has a factor 1): σ₀ (φ₀ + ψ₀), σ₁ (φ₁ + ψ₁), σ₀σ₁ (φ₀₁ + ψ₀₁)
- both photons dressed (bilinear φ·ψ): σ₀² (φ₀ψ₀), σ₀σ₁ (φ₀ψ₁), σ₁σ₀ (φ₁ψ₀), σ₁² (φ₁ψ₁), σ₀²σ₁ (φ₀ψ₀₁), σ₀σ₁σ₀ (φ₀₁ψ₀), σ₁σ₀σ₁ = σ₀σ₁σ₀ (φ₁ψ₀₁), σ₀σ₁² (φ₀₁ψ₁), (σ₀σ₁)² (φ₀₁ψ₀₁).
- **No inverse letter occurs.** V = σ₀σ₁⁻¹ and V⁻¹ are not terms of γ(φ)γ(ψ). Every word built from these terms is a positive braid.

**Letter set (rule A, primary).** The letters are the nine bilinear terms above, i.e. the words that need BOTH photons dressed (a pair-production event). Reason: a term with a factor 1 is one photon passing through unchanged, not γγ. Rule B (comparison arm, labelled, not selectable): all eleven non-identity terms, which generate every positive B₃ word. Rule A is the rule unless the owner picks otherwise on the card.

**Selection (unchanged from qou-ales, FrobeniusSelected).** Candidates: non-empty products of letters on 3 strands, by crossing count up to 12. Feasible: reading 3, χ_λ(w) ≥ 0 on every level with y_λ > 0, convention D, proton pin. Exact zero counts as feasible (≥ 0); a value under 1e-30 is decided by re-evaluating at 120 dps and calling it zero only if it stays under 1e-100 there. Cost: crossing count. Selected: every feasible word of minimal cost — all ties reported, none broken by any residual or measured value.
- Sectors: the nucleon (3 strands; closure has 3 components, any word); recorded, not filtered by, split vs non-split closure.
- Reported per word: letters, braid word, writhe, components, level characters χ₃, χ₂₁, χ₁₁₁.
- Questions, no predicted answer: 1. Which words are selected, and is the minimum split (e.g. σ₀² = Hopf ⊔ unknot)? 2. Does any selected word equal β_Bor up to conjugacy? (It cannot: β_Bor has writhe 0 and every rule-A word has writhe > 0.) 3. Does rule B select a different minimum?
- Not allowed: changing letters, cost, sector or the floor after seeing results; choosing among tied words by Q_β or any mass.
- Downstream: χ₃/χ₂₁/χ₁₁₁ of the selected element go to the Q_β ε thread; the words go to the n–p thread. Q_β = 0.4491 MeV stays provisional.
Bean stays OPEN.

### RESULT 2026-11-18 — stage 7 reselection from γ(φ)γ(ψ) (γγ thread, branch claude/gg-photon-product-selection-2026-11-18, commit 68ef4b266)
Run under the 04:30Z pre-registration: proton pin, convention D, words up to 12 crossings. Near-zero characters were decided exactly with symbolic q. This replaces the pre-registered 120 dps check, which the engine cannot do; the exact test is stronger.

Rule A (pair terms): 8007 braids, 2578 feasible, minimum cost 2. Selected: σ₀² and σ₁², a tie. Both close to a split link (Hopf link plus unknot).
- χ₍₃₎ = q² ≈ 1.2321, χ₍₂₁₎ ≈ 2.0437, χ₍₁₁₁₎ = q⁻² ≈ 0.8117. The last is unconstrained, since y₍₁³₎ = 0.

Rule B (all terms, comparison): minimum is σ₁ (cost 1).

So this grammar and this rule select no nucleon-like element, and β_Bor (writhe 0) cannot be reached. Scope (a). The nucleon element stays underived, and Q_β 0.4491 MeV stays provisional. The owner's card on which letters to use (pair terms / all terms / keep V) is open.

Bean stays OPEN.

### NOTE 2026-11-18 — merges + teraplectic finding (relayed from sibling sweep, re-measured)
- Merged: #8130 (rebase, `73205840a`; Lean source-verified 7/7, standard axioms only) and #8124 (rebase, `7642fc6da`; tower E₀, 0.4491 MeV, marked provisional after the L± ruling). Five-block follow-up: PR #8376 (issue #8375).
- Re-ran `qbeta/qbeta_ruled_base_affine_solve_probe.py` (2/2 pass): reaching CODATA on the ruled assembly needs z = 0.99850030441113. That is not an admissible convention-D root (0.0015 from the excluded z = 1). So the base shortfall cannot be fixed through z; any fix must change the element or the functional. This is consistent with the y₃ reduction: no derived trace reaches y₃ ≈ 0.88.

### NOTE 2026-11-18 09:30Z — option C explored (owner asked for the implications of A/B/C), post-hoc, not a selection
Same FrobeniusSelected rule over {V, V⁻¹, L₊, L₋, e⁻}, braids free-reduced, at most 12 crossings: 4428 braids, 1535 feasible, minimum cost 2, giving σ₀² / σ₁². This is the SAME minimum as rule A, because V·L₋ = σ₀². β_Bor is feasible at 6 crossings but not minimal. So the letter set does not decide the nucleon: under A, B and C alike, the crossing-count minimum is a split pair.

Words that are non-split and three-component appear in the run list at cost 4 and are also rule-A words: σ₀²σ₁², σ₁²σ₀², L₊L₋, L₋L₊, each a 3-ring chain. The cheapest non-split word of any component count is σ₀σ₁σ₀ (cost 3, χ₍₂₁₎ exactly 0).

Owner card posted: whether the nucleon closure must be non-split / three-component. Any filter is to be pre-registered before use. Script: /tmp scratch (ruleC.py); to be committed with the probe if adopted.

Bean stays OPEN.

## 2026-11-18 — γγ as Hecke elements: reachability (measurement, no selection)

Owner asked to explore reading γ(φ)γ(ψ) as an H₃ element rather than as braid words (braid-word reading is positive-only, so β_Bor unreachable). Measured at proton q₀, mp.dps 40 + exact sympy Gröbner (scratch scripts, not committed):
1. β_Bor = λ·γ(φ)γ(ψ) has REAL solutions, e.g. φ=(2.5,−2.124435039,−2.285617294), ψ=(−0.8224825298,0.5366867306,0.7224010393), λ=−2.20056601312; residual 3.9e-37 by direct multiplication.
2. Solutions form a 1-parameter curve: for fixed φ, membership in γ(φ)·span{1,σ₀,σ₁,σ₀σ₁} is 2 equations in φ's 3 weights; λ drops out.
3. Product map has generic rank 6 = dim H₃, so a generic H₃ element is a scalar times some γγ. Reachability does NOT select β_Bor.
4. γ(φ)² = λβ_Bor has no solution (Gröbner reduces to (q²−1)²(q²+1)²(q⁴+1)=0): two different photons are needed.
Implication: any nucleon selection in this reading must come from a pre-registered rule on (φ,ψ), the SDP, or the trace functional; p and n on one element cannot be split by moving along the curve. Stays open.

## 2026-11-18 (later) — exact factorisation of β_Bor into two photons (measurement)

Exact in H₃ for generic q (sympy, symbolic; numerically found first at proton q₀, then identified and verified):
  β_Bor = (σ₀σ₁⁻¹)³ = γ(−qh², 0, qh) · γ(q⁻¹h², 0, −q⁻¹h),  λ = 1,
and each factor is 1 + ε·h·V with V = σ₀σ₁⁻¹ = σ₀σ₁ − hσ₀ (a four-term photon with φ₁ = 0) and ε ∈ {q, −q⁻¹}, the two eigenvalues of σᵢ. Reason: V³ + h²V² − h²V − 1 = (V−1)(V² + (1+h²)V + 1) = 0 in H₃.
Consequences: the old γγ vertex V lies inside the photon (it is the φ₁=0 direction), so the old grammar is partly recovered from def:photon; the two factors commute (both polynomials in V), so photon order cannot split p from n. No three-term (φ₀₁=0) point found numerically. Not formalised in Lean yet. Stays open.

## 2026-11-18 14:10Z — γγ → H H̄ through γp → H e⁺ (owner chose the full-strand hydrogen)

On the card, the owner chose: H = β_Bor on strands 0–2, electron on strand 3, Hopf-linked by σ₂²; H̄ = mirror. Recorded before computing, so this fixes the construction:
- Layout in H₈: strands 0–2 are the proton, 3 the electron, 4 the positron, 5–7 the antiproton.
- ρ: σᵢ ↦ σ₆₋ᵢ⁻¹ (reflect strand order, then mirror). H̄ = ρ(H) = (σ₆⁻¹σ₅)³ σ₄⁻².
- Test: HH̄ = X·ρ(X), with X the γp → He⁺ element. The cofactor is fixed to the mirror, with nothing free.

Result. This is exact, needs no numerics, and holds at any q.
1. σᵢ² = 1 + hσᵢ, and σᵢ⁻² = (1+h²)(1 − h/(1+h²)·σᵢ). The Hopf link is a one-term (degenerate) photon γ(h,0,0), and its mirror is a scalar times one.
2. H uses only σ₀, σ₁, σ₂, and H̄ uses only σ₄, σ₅, σ₆. They commute, so HH̄ = H·ρ(H). The factor test holds with X = H. That makes it VACUOUS: the positron strand 4 enters nowhere.
3. Both photon versions give the same answer, because φ₀₁ = 0 makes the last-term switch inert.

Scope (a): this construction alone carries no information about BFPP vs γγ → HH̄. A non-vacuous test needs a crossing that links the electron and positron strands (σ₃, pair creation), and nothing in the corpus fixes how that crossing is weighted. Do NOT read this as evidence for or against crossing symmetry.

## 2026-11-18 16:05Z — PRE-REGISTRATION: typed crossings on the six crossings of β_Bor (owner asked for this in the thread, 15:59Z)

Recorded before any computation. This is a measurement only. Nothing is selected and no residual is used.

Construction:
- β_Bor = (σ₀σ₁⁻¹)³ in H₃. Strand positions 0, 1, 2 carry flavours. Each crossing permutes the flavours (the permutation is the braid's image in S₃).
- A positive crossing σ_k between flavours (f, f′) is replaced by C(f, f′; σ_k) from def:typed-crossing-operator: uu → σ_k, dd → σ_k − h, ud → σ_k − h/2.
- A negative crossing σ_k⁻¹ is replaced by C(f, f′; σ_k)⁻¹. This choice is mine; the corpus types σ only.
- Every placement is reported: uud with d at position 0, 1 or 2, and udd with u at 0, 1 or 2. No placement is chosen.

Outputs, all exact in q:
1. The six H₃ coefficients of each typed element, and whether the p and n elements differ.
2. Reachability as λ·γ(φ)γ(ψ) for each photon variant:
   - four-term (def:photon);
   - switched last term σ₀σ₁⁻¹;
   - three-term (φ₀₁ = 0, as in prop:gamma-gamma-generates-particles);
   - one-term (one nonzero weight).
   Report existence only, not which (φ, ψ) is "best".
3. tr_M at z_D = q³/(q²+1), evaluated at the proton q₀ with mpmath; the ratio n/p.

No outcome changes the corpus. The corpus nucleon (β_Bor × Δ₃, def:typed-crossing-operator) is untouched.

## NOTE 2026-11-18 16:20Z — one-sided β-flip on β_Bor (exploratory, scope (a))
Owner idea: p and n as conjugate Borromean words differing by a quark/β-decay flip.
Conjugates have equal traces (Δ=0), so the split must be a single one-sided vertex
W ∈ {qJ_i, q⁻¹J_i} (audit 2026-11-15 one-sided weak vertex). Replacing one crossing of
β_Bor=(σ₀σ₁⁻¹)³ by W, Markov trace at z_D, proton pin, exact sympy (2-dim + 1-dim irreps,
y_(1³)=0): Δtr/tr = σ₀: +5.81% (qJ) / −14.12% (q⁻¹J); σ₁⁻¹: +17.56% / −4.58%.
Identical across the three positions of each letter type (cyclic conjugacy), so no uud/udu
asymmetry from position. All 30–125× larger than (m_n−m_p)/m_p ≈ 0.14%. No row selected.
Scratch script /tmp/claude-0/np/flip.py, not committed. Not pre-registered as a selection rule.

## NOTE 2026-11-18 16:40Z — owner idea: nucleon = (σ₀σ₁⁻¹ − X)³ (exploratory, scope (a))
Enumerated 29 parameter-free X (scalars 0,±1,±q,±q⁻¹,±h; σ_i^±1; ±J_i, qJ_i, q⁻¹J_i;
P±_i; σ₀σ₁, σ₁σ₀; V^±1). Markov trace at z_D, proton pin, exact sympy
(/tmp/claude-0/np/cubes.py, not committed). tr(V³)=0.998562163837 matches the closed form.
- Only X ∈ {h, −h, P−₀} keep |tr| within 25 % of tr(V³) (−15.3 %, +21.8 %, −5.7 %);
  every other X moves m_p by O(1).
- Natural p/n pairs (bar partners W_L/W_R, J₀/J₁, σ/σ⁻¹, P±): smallest split is P+₁ vs P−₁
  at +5.9 %; others 26 %–3600 %. Leading order in h is h⁰ or h¹ for all except σ₀σ₁/σ₁σ₀ (h²).
- tr((V − V⁻¹)³) ≡ 0 exactly (V has eigenvalues λ,1/λ on V_(2,1) and 1 on the 1-dim irreps).
None reaches (m_n−m_p)/m_p ≈ 0.14 %. A split that small needs X of size ~h⁴ or a first-order
zero tr(V²X)=0; no parameter-free X here supplies either. Setting X's size from CAL-2 would be
circular for Δ_pn (Q_β = Δ_pn − m_e). No row selected.

## NOTE 2026-11-18 17:05Z — entangled electron loop on β_Bor in H₄ (exploratory, scope (a))
Owner reading: −X = remainder of a previously entangled e⁻ strand (BFPP / γγ→HH̄ topologies).
H₄ Markov trace at z_D (seminormal reps (4),(3,1),(2,2); y=0 on three-row shapes; checked
Markov property and tr₄(β_Bor) = closed form). Loop = σ₂^a … σ₂^b around nucleon letters,
reference = same two crossings adjacent. Scripts /tmp/claude-0/np/loop4.py, dsym.py (not committed).
- Enclosed σ₀ letters commute with σ₂, so only loops enclosing ≥1 σ₁⁻¹ differ from reference.
- Exact: D := tr₄(loop) − tr₄(adjacent) is the SAME for all four (a,b) ∈ {±1}²:
  D = (q²−q+1)(q²+q+1)(q⁶−3q⁴+2q²−2)/(q²+1)³;  D/tr(β_Bor) = −3/4 − ε²/4 + … at q = 1+ε;
  −0.74957 at the proton pin.
- Unweighted loops: O(1) shifts (−66 %, −75 %, −82 % of the reference trace).
- Photon-weighted crossings (1+φσ₂^a)…(1+φσ₂^b): single-crossing terms cancel (Markov z),
  so Δtr/tr(β) = φ²·D/tr(β) exactly. φ = h → −3.28 %; φ = h² → −0.1432 % (≈ −0.144 % in m);
  φ = qh → −4.04 %; φ = q⁻¹h → −2.66 %.
  ⚠ φ = h² lands within ~4 % of |m_n−m_p|/m_p = 0.138 %, but φ is NOT derived; picking φ = h²
  because it matches would be selection against the target. Sign: entangled element is
  LIGHTER, so "neutron = entangled" gives the wrong sign. Recorded as near-match, not a result.

### Result (2026-11-18 16:35Z) — for the pre-registration above
- **tr_M at z_D:** identical for all six placements, q²(3q⁴+2q²+3)²/(q²+1)⁶, which is 0.99991206734 at the proton q₀. Reason: n = (σ₀↔σ₁ flip ∘ word reversal)(p), and the trace is invariant under that map. Under this rule the trace cannot split p from n.
- **Elements:** they differ as elements. For each placement, n is the flip-reverse image of p.
- **Four-term and switched photon pairs** (the same set): reach all six placements. Measured numerically at q = 11/10; n:u@0 follows from p:d@2 because flip-reverse maps photons to photons. Nothing is selected.
- **Three-term photon pairs** (φ₀₁ = 0): reach ONLY the placements with the odd quark in the middle (p:d@1, n:u@1). There are two real pairs each, with the same λ for p and n. Exact Gröbner computation at q = 11/10, 13/10 and 3; for the other four placements the Gröbner basis is {1}. The bare β_Bor is NOT reachable this way.
- **One-term photons:** reach none (only λ = 0).
- **Scope (a):** this is a measurement under one typing rule, and the C⁻¹ choice for negative crossings is mine. The middle-placement result is not a selection of the nucleon.

- 17:30Z owner asked: p/n backwards? Swapping (proton = loop-dressed, neutron = bare β_Bor)
  gives m_n/m_p − 1 = +0.144 % vs measured +0.138 % (4.5 % off). Now TWO post-hoc choices
  (φ = h², assignment), and the swap moves the proton anchor m_p = 2(m_μF_Bor − 6m_e) by
  ≈ −1.35 MeV. Needs: derived φ = h², a reason the closed loop sits on the charged nucleon,
  and an anchor fix from the same reason. Near-match only.

## PRE-REGISTRATION 2026-11-18 17:35Z — photon–electron crossing weight from the γγ factorisation
Rule (stated before evaluating): β_Bor = γ(φ⁺)γ(φ⁻), φ⁺=(−qh²,0,qh), φ⁻=(q⁻¹h²,0,−q⁻¹h)
(PR #8502). An e⁻–nucleon crossing σ₂ is the single-crossing (φ₀) term of one of the two
photon factors, so it carries weight φ₀⁺ = −qh² or φ₀⁻ = q⁻¹h². A loop has two crossings, so
the split is φ_aφ_b·D/tr(β_Bor) with D the exact sign-independent loop coefficient.
All three pairings are reported: (+,+), (−,−), (+,−). Neutron = loop-dressed (no swap).
Known before registration: the φ = h² magnitude match (16:40–17:05Z). NOT known: the sign
under this rule. Caveat: the φ₀₁ (σ₂σ₃) pair term needs a 5th strand (e⁺) and is not included.
RESULT 17:40Z (exact): weights φ_aφ_b = q²h⁴ (+,+), q⁻²h⁴ (−,−), −h⁴ (+,−).
Split (neutron = loop-dressed): (+,+) −0.1764 %, (−,−) −0.1162 %, (+,−) +0.1432 %.
Only the mixed pairing gives a heavier neutron, and it is the bar-symmetric product (q-powers cancel).
Measured (m_n−m_p)/m_p = +0.1378 %; mass-level (+,−) ≈ +0.144 %. Mixed pairing NOT derived:
open whether a closed loop must take one crossing from each factor. Near-match status unchanged.

## PRE-REGISTRATION 2026-11-18 17:45Z — H₅ with e⁺ strand (full four-term photons)
Strands 0–2 nucleon (β_Bor on σ₀,σ₁), strand 3 e⁻, strand 4 e⁺. The two photon factors act
on the lepton pair generators: γ(φ)_lep = 1 + φ₀σ₂ + φ₁σ₃ + φ₀₁σ₂σ₃, φ ∈ {φ⁺, φ⁻} from PR #8502.
Neutron word = β_Bor with γ(φ_a)_lep inserted at slot i and γ(φ_b)_lep at slot j (i<j);
reference = both inserted adjacent at slot i. Split = tr₅(word)/tr₅(reference) − 1, Markov
trace at z_D (y = 0 on three-row shapes), proton pin, exact. Report all (a,b) ∈ {+,−}² and all
slot pairs; no selection. Proton = β_Bor with the same two photons adjacent (= reference).

## PRE-REGISTRATION 2026-11-18 17:55Z — charge-weighted EM dressing (step 2)
Both nucleons = β_Bor (closure permutation is the identity, so strand k = component k).
Photon strand = strand 3 in H₄. Pure-braid generators A₂₃ = σ₂², A₁₃ = σ₂σ₁²σ₂⁻¹,
A₀₃ = σ₂σ₁σ₀²σ₁⁻¹σ₂⁻¹. Loop matrix D_ij := tr₄(β·A_i3·A_j3) − tr₄(β) (ordered, i,j ∈ {0,1,2}).
EM term E(Q) := Σ_ij Q_iQ_j D_ij / tr(β), quark charges u = +2/3, d = −1/3.
Report E for p (uud) and n (udd) at every placement of the odd quark, and
ΔE = E(n) − E(p) for all 3×3 placement pairs. The photon weight w multiplies ΔE; its sign is
not derived (the γγ mixed pairing gave w = −h⁴; same-photon pairings give w > 0), so the
sign test is reported for both signs of w. No selection.

RESULT 2026-11-18 19:05Z (H₅ full four-term photons, pre-registered 17:45Z). Exact sympy, convention D,
evaluated at proton q₀. Quantity: tr(β with photons a,b at slots i<j)/tr(β with a,b adjacent at i) − 1.
All 4 pairings × 21 slot pairs reported in /tmp scratch (h5.out); the value takes only two forms:
  0 when β[i:j] is a single σ₀ (commutes with σ₂,σ₃) or the separation is cyclically trivial;
  otherwise a pairing-only constant, the same for every slot pair:
    (+,+)  +0.30145 %    (−,−)  +0.24474 %    (+,−) = (−,+)  −0.27684 %
Target m_n/m_p − 1 = +0.1378 %. No pairing matches; the mixed pairing that gave +0.1432 % with the
h⁴-only H₄ loop weight changes sign and doubles once the full four-term photon is used, so that
earlier near-match does not survive. None of these splits p from n: slot position does not enter.
Scope (a): this construction alone; not an exclusion of photon dressing.
EM D_ij run (pre-registered 17:55Z) produced no output the first time; re-running.

## 2026-11-18 19:05Z — OWNER WORKING ASSUMPTION: photon last term σ₀σ₁⁻¹ (switched)
Owner, in the n–p thread: "Switched last term seems most promising... let's make a working assumption."
This is a working assumption, not a ruling to edit def:photon. The new photon is γ′(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹.

What changes and what does not:
- **Same set of photons.** γ′(φ₀, φ₁, φ₀₁) = γ(φ₀ − hφ₀₁, φ₁, φ₀₁). Every reachability result over the full family is unchanged, including the typed-crossing result of 16:35Z.
- **Same three-term photon.** With φ₀₁ = 0 the last term is absent, so the three-term variant is identical.
- **What changes:** β_Bor = γ′(0,0,qh)·γ′(0,0,−q⁻¹h). The Borromean core is a product of two photons that each carry ONLY the switched last term, weighted by h·q and −h·q⁻¹ (the two Hecke eigenvalues). Under the old photon the same factors needed φ₀ = ∓q^{±1}h².
- **Mass / L2:** there is no numerical impact on any scored quantity. confinement-universality says the nucleon NF does not depend on the photon coefficients once flavours are supplied. The 16:35Z result shows the Markov trace is identical for p and n under typed crossings. So Δ_pn and the L2 dashboard do not move, and the assumption buys no ppQ by itself. Its effect is on which word class the γγ re-derivation selects. That is the ansatz, and any selection under it still needs pre-registration here.

## 2026-11-18 19:20Z — PRE-REGISTRATION: flavour ingredient A (down quark = reversed strand), then B

Owner tapped "A and B, A first" (19:13Z). Registered before any computation.

Model A, as fixed now:
- u strand oriented +, d strand oriented − (corpus's own motivation in def:typed-crossing-operator). The typed-crossing shifts are NOT used; the orientation replaces them.
- Word: beta_Bor = (s0 s1^-1)^3, unchanged. Its closure is 3 components, one per strand, so a placement = an orientation pattern on the Borromean rings.
- p = uud (one component reversed), n = udd (two reversed). All 3 placements per nucleon are computed.
- Invariants reported, all as functions of the free HOMFLY variable v (no specialisation chosen here, so no selection): (T1) oriented HOMFLY of the closure for every orientation pattern; (T2) the open element in the walled Brauer / oriented skein algebra (H_{2,1} for p, H_{1,2} for n), compared through a quantity that is not a closure invariant, to be named in a second registration before it is computed.
- Prediction stated in advance: if the oriented Borromean rings with different orientation patterns are isotopic (linking numbers are all 0, so at least Jones is orientation-blind by Morton's reversal formula), then T1 gives p = n and only T2 can split them. T1 is run to settle this, not to score.
- Nothing is scored against m_n − m_p until a v-specialisation is derived, not chosen.
- B (one-strand blob / Ariki–Koike generator) follows A, with its own registration.

## 2026-11-18 19:20Z — RESULT T1 (model A, closure): p = n, as predicted

SnapPy 3.3.2, L6a4 (Borromean rings, vol 7.32772475342), all 48 self-isometries with their cusp maps. Among the ambient-orientation-preserving ones (det +1 on every cusp), with meridians sent to meridians:
- identity permutation with meridian signs (1,−1,−1), (−1,1,−1), (−1,−1,1): reverses two components;
- permutation (0,2,1) with signs (1,1,−1), (−1,1,1), etc.: reverses one component.
Meridians go to meridians, so each extends to an isotopy of S³. Hence EVERY orientation pattern of the Borromean rings is the same oriented link (up to permuting components). So uud and udd closures are isotopic and every closed-link invariant (HOMFLY at any v, any specialisation) gives p = n. Scope (b): the invariant is the isotopy itself. Model A survives only as an OPEN-element (non-closure) quantity, T2, to be registered before computing.
Also: sibling PR #8517 `trace_flip_reverse` now proves the reversal invariance my 16:35Z no-go needed (for products of factors α+βσᵢ, any R-linear cyclic trace).

## 2026-11-18 19:30Z — Model A at U_q(sl2): every V-module trace also gives p = n (argument, not yet Lean)

For U_q(sl2) the dual V* is isomorphic to V as a module (φ: V → V*). Braiding is natural, so each crossing satisfies c_{V*,U} = (φ⊗1) c_{V,U} (φ⁻¹⊗1) and likewise for inverse crossings. β_Bor is a pure braid (each strand returns to its slot), so ρ_{uud}(β_Bor) = Φ ρ_{uuu}(β_Bor) Φ⁻¹ with Φ = φ on the d slot, and likewise for udd. Any functional Tr(X·ρ(β)) where X is built from K's on each slot (φ intertwines K) is therefore the same for uuu, uud and udd. That covers the plain trace, the quantum trace and the corpus's K-twisted partial traces. Scope: U_q(sl2) only. A can split p from n only where V* ≇ V, i.e. U_q(gl_N) with N ≥ 3, which introduces N as a choice. Owner decision requested (card), not computed.
(The corpus's n/p = q^∓2 comes from projecting onto different TOTAL-WEIGHT spaces of V^{⊗3}, an isospin projection, not from orientation.)

## 2026-11-18 19:35Z — PRE-REGISTRATION: C (weight-space trace) and B (one-strand blob). Owner: "explore B and C" (19:26Z)

C (registered and evaluated now, because it is exact from existing sorry-free Lean):
- Functional: quantum trace Tr(K^{⊗3} ρ(β)) of the level-2 Jimbo braiding restricted to the (2,1) weight space (p) and to the (1,2) weight space (n), NucleonWeightSpaceTraces.lean.
- trace_word_eq gives equal plain traces for EVERY word, and K^{⊗3} acts by the scalar q on (2,1) and q⁻¹ on (1,2). So n/p = q⁻² EXACTLY for every word, β_Bor included. It does not depend on the word, the photon or the typing.
- At the proton q₀: q₀² = 1.23205..., so the ratio is a 23 % effect, not 0.138 %. Scope (a): as a direct mass ratio C misses by ~170×. Any rescaling that brings it to 0.138 % would be a chosen exponent, i.e. selection; not attempted.

B (registered, not yet computed):
- Algebra: type-B Hecke H₃^B(q,Q): σ₀, σ₁ as in H₃; blob t with (t − Q)(t + Q⁻¹) = 0, tσ₀tσ₀ = σ₀tσ₀t, tσ₁ = σ₁t.
- Flavour: a d strand at slot k carries the type-B Jucys–Murphy loop t_k (t₀ = t, t₁ = σ₀tσ₀, t₂ = σ₁σ₀tσ₀σ₁). p = β_Bor·t_d for d at each of slots 0,1,2; n = β_Bor·t_{d1}t_{d2} for each pair. β_Bor is pure, so t_k commutes past it up to the JM relations; computed as written anyway.
- Trace: Geck–Lambropoulou Markov trace on H^B, z = z_D, tr(t) = y. Q and y stay SYMBOLIC.
- Report: p and n traces and their ratio as exact functions of (q, Q, y), plus whether the result depends on slot (the flip symmetry is broken by construction, since t sits on strand 0).
- Nothing is scored against m_n − m_p until Q and y are derived, not chosen.



## 2026-11-18 21:20Z — Switched Four-Term Photon Factorisation & C+B Weight-Space Quark-Charge Trace Formalised in Lean 4 (`NucleonWeightSpaceTwoTerm.lean` §1–§9, Epic `qou-7xl8`)

Formalised in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean` (`868` lines, `0 sorry`, `0 axiom`, `✓ exit 0 — checks` on branch `feat/qou-7xl8-two-term-mass-qed-trace`):

1. **Switched Four-Term Photon Factorisation of `β_Bor = V³ = (σ₀σ₁⁻¹)³` (§9, `borromeanV3A_eq_switched_photon_product`, `borromeanV3B_eq_switched_photon_product`, `borromeanV3A_eq_one_add_h_sq_V_sub_V_sq`, `borromeanV3B_eq_one_add_h_sq_V_sub_V_sq`):**
   - For the switched 4-term photon `γ'(φ₀, φ₁, φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁(σ₀σ₁⁻¹)` (`V = σ₀σ₁⁻¹`), `V³ = γ'(0, 0, +q h) · γ'(0, 0, -q⁻¹ h) = 1 + h² V - h² V²` (`h = q - q⁻¹`) holds identically on both the `(2,1)` proton weight space and the `(1,2)` neutron weight space.
2. **Why Combining C (`(2,1)` vs `(1,2)` Weight Spaces) with the Quark Electric Charge Operator `Q = diag(+2/3, -1/3) = (1/6)I₂ + T³` Splits `p` from `n` Word-Dependently on `β_Bor = V³` (§2–§9):**
   - In entry `19:35Z` above, pure `K^{⊗3}` on `(2,1)` vs `(1,2)` gave a word-independent ratio `q⁻²` because `P(q)` intertwines `A_i` and `B_i` (`NucleonWeightSpaceTraces.trace_word_eq`).
   - However, when the strands carry the Gell-Mann–Nishijima quark electric charge `Q = (1/6)I₂ + T³` (which mixes `ω`-even hypercharge `Y/2 = 1/6` with `ω`-odd isospin `T³`), the adjacent-crossing charge operators `Q₁₂ = Q₁ ⊗ Q₂ ⊗ 1` and `Q₂₃ = 1 ⊗ Q₂ ⊗ Q₃` on `(2,1)` and `(1,2)`:
     - commute identically with their local crossings (`[Q₁₂, σ₁^{±1}] = 0`, `[Q₂₃, σ₂^{±1}] = 0`: `Q12p_comm_A1`, `Q23p_comm_A2Inv`, `Q12n_comm_B1`, `Q23n_comm_B2Inv`),
     - **break** the `P(q)` intertwiner (`intertwine_Q12_ne`, `intertwine_Q23_ne`, `intertwine_QAdj_ne`), and
     - satisfy the exact matrix decomposition `Q₁₂^{(n)} + Q₂₃^{(n)} = (-2/9) I₃ + (1/2)(Q₁₂^{(p)} + Q₂₃^{(p)})` (`QAdjn_eq_static_add_half_QAdjp`).
   - On a single switched-photon fourth term `V = σ₀σ₁⁻¹`, `tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p) = -2(q² - 1)² / (9 q²) = -(2/9)h²` (`trace_QAdjp_borromeanVA`), while the connected neutron trace has the exact opposite sign `tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n) + (2/9)tr(V_n) = +(2/9)h²` (`trace_QAdjn_borromeanVB_connected`).
   - Multiplying by the `h²` two-photon factor in `V³ = 1 + h²(V - V²)` yields the fourth-order `O(h⁴) = O((q - 1)⁴)` connected traces on `β_Bor = V³`:
     - Proton (`trace_QAdjp_borromeanV3`): `tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p³) = -2(q - 1)⁴(q + 1)⁴(q⁴ + q² + 1) / (9 q⁶)` (`(1/3)|tr| = 0.00043068`, which in units of `m_e` is `+0.22008 keV`, within `0.36σ` of the `+0.22881 keV` `211 ppb` `μ--p` anchor gap).
     - Connected Neutron (`trace_QAdjn_borromeanV3_connected`): `tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n³) + (2/9)tr(V_n³) = +(q - 1)⁴(q + 1)⁴(2q⁴ - q² + 2) / (9 q⁶)`.
     - Connected `(n - p)` difference (`trace_QAdj_connected_diff_borromeanV3`): `(q - 1)⁴(q + 1)⁴(4q⁴ + q² + 4) / (9 q⁶)`.
## 2026-11-19 00:05Z — PRE-REGISTRATION: charge-tensor insertion on the weight spaces (owner pasted agy's two-term discussion, 19:32Z)
- Spaces: Wp = (2,1), Wn = (1,2), matrices A, B of NucleonWeightSpaceTraces.lean; β_Bor = (σ₁σ₂⁻¹)³.
- Charge Q = diag(2/3, −1/3) per strand (an input charge assignment, Gell-Mann–Nishijima; not derived here).
- Reported, exact in q: E_ij = Tr(K^{⊗3} Q_iQ_j ρ(β)) / Tr(K^{⊗3} ρ(β)) for each pair i<j, and the self terms Σ Q_i² (diagonal, word-independent), for p and n.
- This is a measurement of whether the insertion is word-sensitive. No coupling constant is applied and nothing is scored against MeV.

## 2026-11-19 00:10Z — RESULT: charge-tensor insertion
Exact in q (sympy), β_Bor on Wp/Wn:
- Tr_K β: p = −P(q)/q⁵, n = −P(q)/q⁷ with P = q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1; ratio n/p = q⁻² as C predicts. At q₀: 3.32348, 2.69752.
- Pair-resolved E_ij depend on the word: p (−0.002351, +0.001919, +0.000432), each ∝ h³ or h⁴; n (−0.112024, −0.109979, −0.111330).
- But the SUMS are word-independent: Σ_{i<j} E_ij = 0 (p), −1/3 (n), and Σ Q_i² = 1 (p), 2/3 (n), because Q_iQ_j is diagonal and its pair-sum is constant on each weight space. So a uniform Coulomb sum is static charge counting: the braid only redistributes it among pairs. The word can matter only through a pair-dependent weight (a distance or crossing-number kernel), which is underived. Scope (a).

PRE-REGISTRATION 2026-11-18 19:25Z (one-strand marker, owner "go"). Marker = Jucys–Murphy element of
the marked strand, which lives in H₃ itself, so no new parameter: L₀ = 1, L₁ = σ₀², L₂ = σ₁σ₀²σ₁
(strands 0,1,2; β_Bor = (σ₀σ₁⁻¹)³ is a pure braid, so strand k ends at k). Compute exactly at z_D:
  M_k := tr(β L_k)/tr(β) − 1,  k = 0,1,2.
Report all three readings below, for every placement (uud: d at 0/1/2; udd: u at 0/1/2), and
the n − p difference for all 3×3 placement pairs. Charges u = +2/3, d = −1/3. Readings fixed now:
  (A) Σ_k Q_k M_k      (B) Σ_k Q_k² M_k      (C) M_{k_odd} (odd-quark strand only).
No reading is selected after the fact; target +0.1378 % is compared, not fitted. The trace no-go
(PR #8517) does not forbid a split here: L_k is a product of σ's, but θ maps strand k to strand
2−k, so a split must come from comparing different strands.

WITHDRAWN 2026-11-18 19:23Z: the 19:25Z one-strand marker pre-registration above is withdrawn unrun; the owner said "no" to it. Nothing was computed.

PRE-REGISTRATION 2026-11-19 05:10Z (owner "A" + "derive instead of 4 choices"). Charge-insertion EM term, ONE rule, fixed before computing:
  Δ_EM := m_e · [ t(W_n) − t(W_p) ],  t(W_N) := Tr_{W_N}( K^{⊗3} (Q₁₂+Q₂₃) V³ ) / [2]_q³
where V = σ₁σ₂⁻¹ on the 3-dim weight spaces of PR #8518 (NucleonWeightSpaceTwoTerm.lean), K = diag(q,q⁻¹) per strand, [2]_q³ = quantum dim of V^{⊗3}.
Derivation of the weighting (closes #8518's plain/KnKp/Kp3/q menu): convention D's Markov trace IS the U_q(sl2) quantum trace Tr(K^{⊗n}·)/[2]^n (check: Tr_q(σ)/[2]² = q³/(q²+1) = z_D). K commutes with the braid, so restricting to a weight space multiplies by q^{2T³}: q on W_p, q⁻¹ on W_n. No "connected" subtraction, no α_EM factor, no per-anchor normalisation. Target n−p EM part is lattice comparison only (≈ −0.6 to −1.0 MeV); total 1.29333 MeV. Value is reported whatever it is.

RESULT 2026-11-19 05:15Z (rule pre-registered 05:10Z, exact sympy, /tmp scratch emA.py; proton q₀ = 1.1099785827513808, mp.dps 60):
  check: Tr(K⊗K Ř)/[2]² = q³/(q²+1) = z_D symbolically (weighting derived, not chosen).
  t(W_n) − t(W_p) = (2q¹⁴−2q¹²−9q¹⁰+20q⁸−26q⁶+18q⁴−13q²+4) / (9q⁴(q²+1)³);  q→1 limit −1/12 (classical Σ QᵢQⱼ).
  at q₀: −0.0734705048628237;  Δ_EM = m_e·(…) = −0.0375433509 MeV.
  Sign matches lattice (proton heavier from EM); magnitude ~15–25× short of lattice −0.6…−1.0 MeV (comparison only).
  87 % of the value is the q=1 classical charge sum; the q-dependence moves it 12 %.
  Same rule on the bare V³ gives tq(W_n)/tq(W_p) = q⁻² exactly (−18.8 % at q₀), the strong-side 150× problem, unchanged.
  Remaining gap is the ENERGY UNIT of the charge term, not the trace: no trace choice can supply ×15–25; adding α_EM makes it 137× smaller.


## 2026-11-15 — gluon segment by the γγ rule (PR #7876, child bean qou-ggls)

**What the γγ rule gives.** On three strands the rule gives the unit V = σ0σ1⁻¹, which is the corpus gluonUnit. It does not fix how many units the gluon segment carries. The output is therefore the family {V^k}.

**What was enumerated.** CORE·TAIL·V^k for k = 0..3, pre-registered, with the census quark tail held fixed.
- g_odd = 0 for every k, so the qou-z08b obstruction belongs to σ0².
- Whole-word reading 3 admits **k = 1 only**, for both nucleons: χ_(2,1) = +0.2170 (p) and +0.4294 (n).
- Q_β at z_D for that element is 0.229517 MeV (−70.66 %). This is reported only and played no part in any choice.

Nothing is selected or re-scored.

**Owner decisions still open:**
1. Does the γγ rule or the H2-parity rule (σ0², owner 2026-08-30) govern the gluon segment?
2. Does the survivor replace nuc11_interleaved?

This bean stays open (rule 13a).

(Ported to the bean mount 2026-11-20 by W3 from PR #7876, whose bean-file edits cannot merge now that beans are branch-mounted.)

**2026-11-20 (session 01VQDpPd):** measured two ruled-base Q_β elements live on main at once —
content blocks (mass-comparison-table.md:33, neutron-qvalue-symbolic.md:53) score Δ_S, tower E0,
0.4491 MeV (−42.6 %); the L2 scorecard scores nuc11_interleaved, 0.6519 MeV (−16.68 %), which
fails reading-3 SDP on (2,1). Recorded in the scorecard witness as content_blocks_element /
element_conflict_open (PR #8549). Not resolved — still the owner's call. γγ+SDP base search
(qou-ales / qou-vd7j) running on claude/qbeta-gg-sdp-base-2026-11-20.

**2026-11-20T14:40:21Z — OWNER RULING (Carl, session 01VQDpPd): record Q_β = 0 as the γγ base's scope-(a) prediction; derive flavour on the U_q / weight side.**
PR #8564: under γγ words + reading 3 (whole word, every tower level) p and n share the survivor set {V³,V⁶,V⁹}; minimal cost p = n = V³ ⇒ Q_β = 0 on the ruled z_D base (Lean qbeta_delta_vanishes_of_frobeniusSelected, frobeniusSelected_ten_unique). Scope (a): the grammar carries no flavour index; the ruling is not excluded. Assigning different survivors to p and n by Q_β is a fit (not adopted). Next: T³-graded split of the trace on V³ (follow-up task opened). Scorecard unchanged. Bean stays open.

**2026-11-20T14:44:09Z — CORRECTION to the entry above (owner, 15:43).** The "Q_β = 0" result of PR #8564 is for the OLD γγ reading only (GammaGammaWordSelection.GammaGammaWord = products of bare σᵢσᵢ₊₁⁻¹; no colour weights, no chirality). It is NOT the prediction of the canonical four-term coloured photon def:photon γ(φ)=1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁ (#8367), whose two-photon product carries independent chiral L₊/L₋ coefficients, nor of the bar-odd (sinh) channel where Q_β lives. "The grammar cannot separate n from p" was mis-stated. Selection is being redone with the four-term chiral photon + odd channel (branch claude/qbeta-flavour-weight-split-2026-11-20).

## 2026-11-20T14:50:40Z — OWNER RULING (not a working assumption): photon last term is σ₀σ₁⁻¹
Owner (Carl, 2026-11-20 15:47–15:48): "Use γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹ … That was already decided. Why did it get changed back to the wrong form? … Who overrode my decision". The 2026-11-18 19:05Z entry above recorded this as "a working assumption, not a ruling to edit def:photon" — that classification was the recording agent's, and it is why the merged def:photon (8fe7dbecf4, authored 11-17 before the decision; moved to the library e3c658a58b 11-20 07:44; merged in #8367 11-20 08:34) still carries σ₀σ₁. It is now a ruling: def:photon is being corrected (branch claude/photon-chiral-vertex-2026-11-20). All running agents told to use σ₀σ₁⁻¹.

## 2026-11-20 — W2: where the "good" Q_beta came from (measured at the proton pin, 50 dps, CODATA 0.78233341 MeV)
| construction | Q_beta (MeV) | error |
|---|---|---|
| Form A closed form (z = 1 base) | 0.7836458 | +1677.6 ppm |
| + Kashiwara N1, convention C | 0.7823912 | +73.8 ppm |
| + Kashiwara N2, convention C | 0.7823344 | **+1.28 ppm** (the remembered "good" number) |
| + Kashiwara N1, convention D | 0.7828615 | +675.0 ppm |
| + Kashiwara N2, convention D | 0.7828047 | +602.4 ppm |
| D N2 + connected Borromean QED (plain) | 0.7824730 | +178.4 ppm (recorded as a selection, not a prediction) |
| scorecard primary (z_D Markov trace, nuc11_interleaved, two-term) | 0.6515246 | -16.7 % |

The +1.28 ppm needs BOTH a z = 1 base (retired 2026-09-08: not a convention-D Markov trace, fails to annihilate the (1^3) block) AND a convention-C phase (excised 2026-08-15). It also needs N = 2 truncation, a near-match rung. Keeping the base and moving only the phase to D gives +602 ppm. Every admissible D base is below CODATA (F_required > 1), so no cosine ladder can close it (qou-cds1).

**2026-11-20 — flavour weight split + chiral photon (PR #8586, stacks on #8564).** Photon used: γ(φ)=1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹. Arm γ: corpus-derived colour weights (eigenvalue pair) give γ(0,0,qh)γ(0,0,−q⁻¹h)=V³ for p and n ⇒ Q_β=0 for every linear ε; antipode mirror, V⁻³ and photon order are trace-invisible (scope b). Arm W: ε_flavour=ε_n−ε_p of the z_D trace = Tr(K^{⊗3}·)/[2]³ on W_n, W_p; on V³ = (q²−1)P(q)/(q⁴(q²+1)³), exactly bar-odd (bar swaps the T³ sectors), negative on (1,23/20] (Lean FlavourWeightSplit.lean, sorry-free). Q_β = 0.325434 MeV (V³, −58.40 %), 0.323542 (V⁶), 0.320400 (V⁹); tower E₀, 70 dps. Not blind: np-splitting §18 already carries 0.3254 as Δm. Per-sector-normalised split = 0. Owner decisions: D1 adopt ε_flavour as the scored ε? D2 is 0.3254 Q_β or m_n−m_p (the latter forces Q_β<0)? Audit docs/audits/2026-11-20-qbeta-flavour-weight-split.md. Bean stays open (rule 13a).

## 2026-11-20 — W2: epsilon is RULED, not derived (audit docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md)
Delta (typed crossings) is a definition, epsilon a ruling and E0 posited. The mass-channel scale (945.76 MeV per unit trace) applied to this Delta gives ~100-177 MeV, so Delta and E0 are not the mass channel's objects. [corrected 2026-11-20: u and d already exist as separate lines of the (3,1) rep of H4 (QOU/QuarkState); the open step is which label is n<->p and why epsilon is the flavour round trip, audit section 9.]

**2026-11-20T16:55Z — derived weighting implemented across the compute (owner request 16:00; PR #8591, branch claude/two-term-derived-trace-weighting-2026-11-20).**
The 05:10Z pre-registered rule now lives in `computations/two_term_qtrace_weighting.py` (library + producer, witness `two-term-qtrace-weighting.witness.json`, 70 dps, proton q₀) and `lean/QOU/BraidsAndKnots/NucleonWeightSpaceQTrace.lean` (7 theorems, sorry-free, axioms propext/choice/Quot.sound). Reproduced: Δt_adj,raw = (2q¹⁴−2q¹²−9q¹⁰+20q⁸−26q⁶+18q⁴−13q²+4)/(9q⁴(q²+1)³) = −0.0734705048628237, Δ_EM = −0.0375433508915675 MeV.
Symbolic map: 'KnKp' (on the connected traces) = ([2]_q³/3)·Δt_derived,conn EXACTLY — derived weight, wrong normalisation (1/3 vs 1/[2]³; 8/3 at q=1). 'plain', 'Kp3', 'q' are not proportional. On the raw insertion KnKp differs further by the static (2/27)q⁻¹tr(V³). All-pairs: raw −0.0565058628 MeV (q→1 −1/8), connected ≡ 0.
`weighting='derived'` is now the default/only canonical path in canonical_mass, derived_masses, qbeta_utils, qou_substrate.q_two_term_borromean_at, m_p_substrate_identity, free-neutron-decay, two_term_qed_isotope, mass_binding_dashboard, and the L2 scorecard (scored_form two_term_plain_me → two_term_derived_qtrace_me). Moved: M_p^QED,conn +0.2201→+0.0901 keV; Δm_QED^conn −0.3317→−0.1272 keV; m_mu +8.058→+128.0 ppb (miss 37.02→588.1, loses beats-1×); Q_β 1.672e8→1.669e8; m_n 1.392e5→1.390e5; Δ_pn 1.011e8→1.010e8 ppb. q₀ not re-pinned.
Kept unchanged because the corpus does not fix them (owner decision framed in the PR): adjacent vs all-pairs insertion, connected vs raw, sign −m_e·t (compute) vs +m_e·t (pre-registered). Alternatives are unscored labelled rows in the scorecard. Probes (np_two_term_qed_mup_tension, two_term_qed_pair_choice, qbeta_pdix_cds1 bridge) and level1-qvalues (long compute, not re-run) still carry the 1/3 'plain' form as records. Bean stays open (rule 13a).

**2026-11-20: compute, content and Lean on the chiral four-term photon (PR #8595, companion to #8583).** Weights: only the eigenvalue pair γ(0,0,qh), γ(0,0,−q⁻¹h) is evaluated (V³ = γ₊γ₋, exact); 0.0487/0.0978 kept as labelled fits. Moved at q₀: in the knot-operator key table, tr_M(σ₀Tσ₀) → γ₊Tγ₋ (T₁,₀ 1.12809 → 0.99856, and e⁻ appears for T₂,₁, T₂,₂). The "bare photon pair" σ₀² becomes 𝟏 (bare) or V³ (eigenvalue pair). β_Bor reads as 2 photons, not 3 γγ̄ events. In photon_electron, the single-crossing V^k/V̄^k charge-like sign split does NOT survive the four-term photon: all words respond negatively, and absorption passes on all seven. Breit–Wheeler promote/split holds for the σ terms, but a vertex photon spans grades 0–2. tbl:four-term-pair-nucleon-table1-data has no producer; it is reconstructed as γ_straight(0.0487,0.0487,0.02)², and with the ruled photon σ₀ goes 0.09887 → 0.09043 (not edited: the weights are a fit and unsourced; owner call). Content/Lean C1–C4 and C10 are restated on QOU.Photon.photon (lean-direct exit 0, no sorryAx). **Open (gap):** V-word probes are the φ₀ = φ₁ = 0 specialisation, and at the eigenvalue pair tr_M/χ have O(1) first-order sensitivity to the chiral single-crossing part (tr_M 0.53/0.50/0.72/0.75). The corpus has no derived φ₀, φ₁, so a per-probe re-run is blocked on deriving them, not on compute. Re-asking ε-L1 of V is still an owner call. Bean stays open (rule 13a).

## 2026-11-20 — W2 LEAD (not derived): J4 flavour coupling cJ/2 as the chirality expectation y3
QBetaChiralityReduction: Q_beta = (h[2]/2)*y3*E0 for every block-weighted trace. y3 = cS/2 (sigma3 label A) IS Markov z_D (-43%). The label-B analogue y3 = cJ/2 = [2]^2[2]_{q^2}/[3]^2 = 0.892057 gives +0.33% (order-zero E0) / +1.32% (tower E0); CODATA needs 0.8891 / 0.8804. Three candidates were tried, so this is selection against the target until a trace with (3)-block weight cJ/2 on the gamma-gamma four-strand sector is derived. Audit section 8.

**2026-11-20T17:30Z — OWNER RULING (Carl, 16:44): the L2 scorecard scores OPTION 2, the covariant all-pairs insertion Q₁₂+Q₂₃+Q₁₃ with the derived weighting Tr(K^{⊗3}·)/[2]_q³ (PR #8591).** Its connected part is ≡ 0 on V³ (Lean `NucleonWeightSpaceQTrace.deltaT_allPairs_connected_eq_zero`, sorry-free), so every scored two-term row equals its one-term row. Options 1 (adjacent, connected, −m_e·t), 3 and 4 stay as unscored labelled rows. Implemented in #8591 (commits 764f905a1c, e64a4240dc, 5ec37345d6 and later): `insertion=None` + derived = all-pairs is the canonical default in two_term_qtrace_weighting, canonical_mass, derived_masses, qbeta_utils, qou_substrate.q_two_term_borromean_at (pin = one-term proton pin to 50 digits), m_p substrate identity, free-neutron-decay, isotope compute, dashboard, scorecard (scored_form two_term_covariant_all_pairs_qtrace). Scorecard moved main(plain) → adjacent-derived → ruled: m_μ +8.058 → +128.0 → **+211.2 ppb (970.2×, = one-term)**; Q_β 1.672e8 → 1.669e8 → 1.668e8 ppb; m_n 1.392e5 → 1.390e5 → 1.389e5; Δ_pn 1.011e8 → 1.010e8 → 1.009e8; headline 1/6 unchanged. Content blocks neutron-proton-mass-splitting and isospin-mass-split-em-localisation now state the ruled form with a dated note that +0.2201 / −0.3317 keV / 8.06 ppb (0.37σ) were the 1/3-normalised plain adjacent weighting; the probe does not close the μ–p tension. derived_masses default pin moved muon → proton (qou-aj91; Q_β +30.37 ppb rel.). The ruling settles the insertion and weighting of the two-term QED probe only; it derives no non-zero Q_β/Δ_pn contribution, so the open question of this bean (what ε is, and the u/d derivation) is untouched. Bean stays open (rule 13a).

## 2026-11-20 — W2: flavour round trip PROVED (FlavourRoundTrip.lean, sorry-free)
tr(Lu s2 Ld s2) = (q^4+1)/(q^2+1)^2 = the ruled convention-D y3 (label A); tr(Ja s3 Jb s3) = cJ/2 (label B), also via the gamma-gamma vertex. Label B gives Q_beta +0.33% / +1.32%, but J4 labels (3) vs (2,1) = isospin 3/2 vs 1/2, not n<->p. Label C (T3) is the physical n<->p label, and no braid word changes it (qou-0whz C2). Options are in audit section 9; the default is to keep both labels with no ruling.

## 2026-11-20 — W5 (session 01VQDpPf): independent check of #8564 and #8586, and the decision framed

Independent recomputation (own sympy Jimbo Ř on (C²)^⊗3, not the PRs' code), proton pin, dps 60:
- Tr(K^⊗3·)/[2]³ = Markov trace at z_D: verified (tr σ₁ = q³/(q²+1) exactly; Markov property on 1, σ₁, σ₁⁻¹).
- #8564: at H₃, χ_(2,1)(V^k) ≥ 0 only for k = 3, 6, 9 (1.994, 1.977, 1.948): verified. Pair values 0.0182 / 0.0302 / 0.0484 MeV: verified. Q_β = 0 follows from `frobeniusSelected_ten_unique` alone; the stated hypothesis (pairing = altChar) is used only in the vd7j side result. H₆ placement enumeration not re-run. Both probes pass (13/13, 24/24).
- #8586: ε_n − ε_p = (q²−1)P(q)/(q⁴(q²+1)³), exactly bar-odd: verified. |ε|·E₀ = 0.325433928735 MeV (−58.40 %), F_required 2.404: verified. The SIGN of ε flips with K ↔ K⁻¹ (which basis vector is "up"); |ε| does not move. So "ε < 0, neutron smaller" is convention-dependent.
- Lean: both files lean-direct exit 0 against a private rebuilt cone; #print axioms on all declarations: propext, Classical.choice, Quot.sound only.

Decision put to the owner in the session chat (options: strict γγ+reading-3 base, Q_β = 0; base + T³ flavour split, 0.3254 MeV; keep nuc11_interleaved, 0.6519 MeV, fails reading 3; CORE·TAIL·V¹, 0.2295 MeV). Bean stays todo (rule 13a).

### PRE-REGISTRATION ε-L1V (2026-11-20; re-ask ε-L1 of the ruled photon vertex V = σ₀σ₁⁻¹; PR #8616)
- Full text: computations/probes/gg_twist_vertex_channel/PREREGISTRATION.md (commit bc02ecd75c), written before computing.
- Functionals: F1 = ε-L1's multiplicity-trace ε_tr (verbatim); F2 = z_D trace Tr(K^{⊗3}·)/[2]³ split over W_p, W_n (plain-sector difference D = tr_Wn − tr_Wp is the channel's u↔d asymmetry).
- Arms: V-words (V, V⁻¹, V·V³, V³·V, VV⁻¹, V·σ₀); four-term photon at the eigenvalue pair γ(0,0,qh), γ(0,0,−q⁻¹h) and products; symbolic φ₀,φ₁ first-order coefficients.
- Prediction: symmetric everywhere (Hecke image commutes with U_q(sl₂); Δ = σ₀σ₁σ₀ swaps σ₀↔σ₁). No physical target compared.

## 2026-11-20 ~17:40Z — owner picked option B, then: "rulings are only temporary conjectures; formalize first, Lean-prove, derive" (W5, session 01VQDpPf)

Owner chose **B** (γγ + reading-3 base V³ with the T³ weight split of the z_D trace, 0.3254 MeV, −58.4 %), and in the next message said rulings are temporary conjectures. Accordingly the three inputs of Q_β = |ε(Δ)|·E₀ are now Lean conjecture classes, with Q_β derived from them (PR #8617, stacked on #8586; `QOU/QBeta/DecayConjectures.lean`, lean-direct exit 0, no sorryAx):
- C1 `DecayFunctionalIsWeightTrace` (was rulings 09-08 + 11-20), C2 `NucleonElementsAreGammaGammaBase` (V³ for both), C3 `DecayEnergyScale` (posited E₀).
- `qbeta_eq_of_conjectures`: Q_β = |(q²−1)P(q)/(q⁴(q²+1)³)|·E₀; `qbeta_pos_of_conjectures`: Q_β > 0 on 1 < q ≤ 23/20.
Open: derive C1 (weak-vertex amplitude → weight-trace difference), C2 (transport #8564's selection to the weight-space rep; derive per-nucleon photon weights φ₀, φ₁ — only the eigenvalue pair is derived, and it gives V³ for both), C3 (E₀ from the mass channel; scale mismatch 945.76 vs ~4.2 MeV). Dashboard re-score not done: proposed as a row labelled conditional on C1–C3, after #8572. Bean stays todo (rule 13a).

## 2026-11-20 — owner choice "3 2" (W2)
No label ruling: labels A and B stay side by side, and the round-trip theorem is merged (#8615). Label C research, first result (PR #8618, exact probe): quantum-trace restrictions give tau(J) = z_D (whole space), 1/3 (a T3 charge sector), 0 (the nucleon isospin-1/2 block) or 1 (the isospin-3/2 block). Q_beta reads only the weight on the isospin-3/2 block (chi_21(Delta_S) = 0). CODATA needs ~0.889. Next: derive why the decay functional weights the isospin-3/2 channel that way. Bean stays open (rule 13a).

**2026-11-20T18:40Z — OWNER RULING (Carl, 18:27): #8586's T³ weight-split Q_β (|ε|·E₀ = 0.3254 MeV, −58.40 % vs CODATA) is the SCORED Q_β cell.** Applied by the merge queue on PR #8586. PR #8591 (derived weighting, covariant all-pairs two-term rows) keeps both on rebase: the Q_β cell from #8586, the two-term rows covariant (connected part 0 on V³, so two-term = one-term; m_μ +211.2 ppb / 970.2×). Options 1, 3, 4 remain unscored labelled rows. The ruling selects the scored cell only; it does not close this bean (rule 13a: the T³ split's derivation and F_required 2.404 stay open).

**2026-11-20 ~18:00Z (W5):** owner "Go" → dashboard Q_β row now scores option B as CONDITIONAL on C1–C3 (PR #8626, after #8564 → #8586 → #8617): Q_β 0.3254 MeV (−58.4  %, completing the line above), m_n / Δ_pn inherit with a note; nuc11_interleaved kept as the superseded element. Calibrated: closed form vs explicit weight-space traces, gap 1e-72.

## 2026-11-20 ~19:15Z — ε-L1V result: the photon vertex V = σ₀σ₁⁻¹ does NOT break u↔d (PR #8616, draft)

Pre-registered (bc02ecd75c), prediction confirmed. Same functionals as ε-L1: F1 multiplicity-trace ε_tr, F2 z_D trace split over W_p/W_n.
- Arm V (V, V⁻¹, V⁴ both orders, VV⁻¹, V·σ₀, ε-L1 applied order): F1 ratio ε_pn/ε_np = 1 exactly; F2 D = tr_Wn − tr_Wp = 0. Same as L± in ε-L1.
- Arm γ (γ(0,0,qh), γ(0,0,−h/q), γ₊γ₋ = V³, γ₋γ₊): all symmetric.
- Arm φ (symbolic φ₀,φ₁,ψ₀,ψ₁; single γ(φ₀,φ₁,φ₀₁)): first-order u↔d coefficients 0; asymmetry vanishes identically.
- Proof scope (b): F2 in Lean, `QOU.BraidsAndKnots.HeckeWeightSpaceSymmetry` (generic CommRing, q·qi = 1, sorry-free): `trace_ρn_eq_trace_ρp` (Δ = σ₀σ₁σ₀ conjugates W_p's rep into W_n's for every free-algebra element), `photon_symmetric`, `vertex_symmetric`, `trace_vertex` (tr_W V = −h²), `flavour_split` ((qi·tr_Wn − q·tr_Wp) = −h·tr_Wp for every element). F1 by exact basis check on the six standard words of H₃(q) (not in Lean).
- Implication for the scored Q_β cell (#8586, 18:27 ruling): ε_flavour(V³) = (q²−1)P(q)/(q⁴(q²+1)³) is exactly −h·tr_W(V³)/[2]³. Every bit of its n/p asymmetry is the K^{⊗3} weighting h; the γγ element enters only through a u↔d-symmetric trace. So the photon's weights φ₀, φ₁ cannot produce an n−p split when both nucleons carry the same element. Under these functionals a γγ derivation of Q_β can put the n/p difference only in (i) the trace's K-weighting (conjecture C1), or (ii) different elements for n and p (C2), never in the photon channel.

## 2026-11-20T19:45Z — pair-nucleon data table restated with the ruled photon (PR #8629)

Owner 18:22: "pair-nucleon table: restate it with the new photon." `tbl:four-term-pair-nucleon-table1-data` had no producer or recorded weights. New producer `computations/four_term_pair_nucleon_table.py` (exact ℚ(q), proton q₀, 70 dps, 7/7): the OLD form γ_old(0.0487, 0.0487, 0.02)² reproduces all six recorded entries at 3 dp; the ruled photon at the same weights gives 1 1.005→1.004, σ₀ 0.099→0.090 (0.0988698→0.0904259), others unchanged at 3 dp (moves ≤ 4e-4), via γ(φ₀,φ₁,φ₀₁) = γ_old(φ₀ − hφ₀₁, φ₁, φ₀₁). Weights labelled in block + witness: 0.0487 = fit to 2m_e (Breit–Wheeler), 0.02 unsourced; the record pins only a ∈ [0.0486, 0.0490], b = 0.020 on a 1e-4 × 1e-3 grid. Worked illustration, not a prediction. Second column: eigenvalue pair γ₊γ₋ = V³ (no e⁻ term). Nucleon nets 0.999/0.811 photon-independent by construction (confinement universality), not recomputed — no producer for them is on record. Not merged.

## 2026-11-20T21:00Z — R2/R5/R3: n↔p as T⁺ on the U_q side (label C); T(3,5) claims checked (PR #8632, draft)

Owner 18:30 ("Q_β must be DERIVED, not chosen"), routes R2/R5/R3. Pre-registered (`computations/probes/qbeta_r253/PREREGISTRATION.md`, not blind: a symbolic ℚ(q) run came first and is disclosed). Lean `QOU/QuarkState/IsospinRaisingRoundTrip.lean` + `T35WeakVertexTrace.lean`, generic Field, sorry-free, axioms propext/choice/Quot.sound.
- **Charge exclusion of A/B (scope b):** Jimbo Ř commutes with Δ(K), Δ(E), Δ(F) (`Rc_comm_*`), so every Hecke word, the γγ vertex included, preserves charge. Labels A and B are Hecke-internal, so they cannot be n↔p (ΔQ = 1).
- **Label C:** T⁺ = Δ²(E): W₋ → W₊ intertwines H₃ (`Eu_sm1/2`). ε_C(X) = tr_W₋(T⁻T⁺X)/tr_W₋(T⁻T⁺) gives **y₃ = (q²+1)²/(q⁴+4q²+1) = [2]²/([2]²+2)** (`epsC_J1`, same from p). Q_β = 0.588715 MeV (−24.75 %, order-zero E₀) / 0.594552 MeV (−24.00 %, tower E₀). Comparison only, not wired.
- **`isospinHalf_deltaS`:** the isospin-½ part of the round trip does not see Δ_S, so Δ_S lives entirely in (3) = isospin 3/2. On pure isospin-½ nucleons Q_β(Δ_S) = 0. The label-C value comes only from the isospin-3/2 content of the weight space, which makes the typed-crossing Δ_S suspect as the object to difference.
- **`qtrace_J1`:** the full quantum trace (all strands closed by pair creation/annihilation) is exactly convention-D y₃, so label A's z_D is the γγ/cup-cap closure. Label C is that closure restricted to the neutron charge sector with a T⁺ round trip.
- Remaining choices: the state set (full weight space vs isospin ½ → 0); normalisation ε(1) = 1; E₀ (posited); the Δ_S definition.
- **R3:** these hold: 10 letters, knot closure, σ₁³ left-divides (σ₁σ₂)⁵ (6 cofactors). These do not hold as stated: the split is not unique (40 placements) and is not produced by GS reduction; no R2 move exists in a positive word; the quadratic-step count is order-dependent (25/30); tr_zD((σ₁σ₂)⁵) = q²(q¹²+q⁸−1)/(q²+1)² ∉ ℤ[q^{±1/2}] (`zD_T35`); B_n W ≠ c·B_p. The block's Q formula is not defined under convention D. A dated authorNote was added to `beta-decay-skein-properties.ts`.
Bean stays open.
- Addendum (relation to #8616 `flavour_split`): T⁻T⁺ on W₋ is the commutant element [2]²P₃/₂ + P₁/₂ (`FE_quad`), not a Hecke element. ε_C is n/p symmetric (`epsC_J1_from_p`, consistent with `trace_ρn_eq_trace_ρp`) and uses no K-weighting. It fixes only the block weights y₃:y₂₁ = [2]²:1. The n/p difference enters only through the element Δ_S (channel (ii)), and `isospinHalf_deltaS` shows that element is invisible on isospin ½. A γγ derivation still needs an n/p-distinct element that reaches the isospin-½ block.

## 2026-11-20 — photon colour weights φ₀, φ₁: what forces them (PR #8634, Lean sorry-free, scope stated per item)
Photon γ(φ)=1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹. Lean `QOU/QuarkState/PhotonColourWeightConstraints.lean`.
- NF(β_Bor)=[1−h⁴,−h³−h⁵,h³,−h²,h²+h⁴,0]: e⁻ coordinate 0, so EVERY factorisation γ(φ)γ(ψ)=β_Bor has e⁻ channel φ₀₁ψ₀+φ₁ψ₀₁=0 (`FactorsBorromean.eChannel_eq_zero`). The e⁻ needed for Q_β cannot come from factorising β_Bor, whatever φ₀, φ₁ are.
- Factorisation alone does NOT force φ₀=φ₁=0: measured 8 solutions at h=1/2, 2/9, 3 (probe `computations/probes/photon_colour_weights_solution_set_probe.py`, mpmath 60 dps); 2 = Borromean pair, 6 have φ₀,φ₁≠0. Proved: φ₁=0 ⟺ ψ₀=0 on the solution set, and either forces the Borromean pair with vertex weights {qh, −q⁻¹h}.
- Bar image of a photon is a photon iff φ₀+φ₁=0; bar-closed pair + factorisation ⇒ Borromean pair (`borromean_of_barClosed`, needs h≠0, h²+2≠0). Then e⁻ channel = φ₀₁ψ₀−φ₀ψ₀₁.
- Flip (Δ-conjugation) closure forces φ₀₁=0; three-term photons never factor β_Bor (scope b, certificate h²(h²+2)=0). Neutral in trivial+sign blocks forces φ₀₁=0, φ₀+φ₁=0 (same no-go).
OWNER DECISION: is "bar image of a photon is a photon" an admissible premise? Yes ⇒ φ₀=φ₁=0 derived. No ⇒ φ₀,φ₁ underived (8-point set; picking by residual would be a fit). Default if no answer: nothing changes; φ₀,φ₁ stay recorded as underived. Bean stays open (rule 13a).

## 2026-11-20T21:10Z — R4 (energy conservation) and R1 (four-strand γγ process), PR #8623 (draft)
Pre-registered at 3e41aab22b. Lean `QOU/QuarkState/DecayGammaGammaFourStrand.lean` (generic Field, 26 theorems, sorry-free, axioms std only); probe `computations/probes/qbeta_derivation_r4_r1/` 20/20 at 70 dps, proton q₀. Nothing wired.
- R4, mass channel (S = 2m_μ[3]!/q³ = 945.764 MeV/unit trace; full z_D trace of V³ returns the pinned m_p). With equal plain traces on T³ = ±½ for every X ∈ H₃ (#8616), the only readings give: sectors/[2]³ → τ_n = q⁻²τ_p, Q_β = −73.32 MeV (`qbeta_sector_neg`: Q_β < 0 for all q > 1); sectors/own dim or full trace + u↔d → Q_β = −m_e. Scope (b) on three strands. Label A/B lines: rel. diff +0.00591 / −0.01704 (diagnostic only; need 1.378e-3).
- R1: d→u flip functional on H₃ NF words (1,σ₀,σ₁,L₋,L₊,e⁻) = (0,0,1,q,q,q²) (`flip_pair`). At the derived weights the pair is V³, e⁻ coordinate 0, V³ flips at order h³ (q²h³·eS); round trip (q²h³)²y_D. Label B: Ja·γ(φ) = t(φ)Ja, so Ja·Γ·V₄·Jb = t(φ)t(ψ)q·eJ and t = 1: label B's cJ/2 is independent of the γγ pair.
- Closed form for every reading (order-zero E₀): Q_β/m_e = (q+1)(q²+1)/(2q³)·y₃. y₃ = y_D → −43.2 %; (q²h³)²y_D (γγ base, label A) → 5.6e-5 MeV (−99.99 %); cJ/2 (label B, pair-independent) → +0.33 % (selection against target, as before).
- Remaining choices (none selected): flavour label; round trip vs amplitude and return path; scale E₀ vs S; Δ_S prefactor h[2]/2; φ₀, φ₁. Bean stays open (rule 13a).

## 2026-11-20T18:20Z — owner rulings D1 = A, D2 = Q_β applied; PR #8586 merged (b47929e610)

- **D1 = A (owner, 18:25).** Scored Q_β on the L2 scorecard = |ε_flavour(V³)|·E₀^tower = **0.325433929 MeV (−58.402 %)**: ε = T³ weight split of the z_D trace Tr(K^{⊗3}·)/[2]³ on W_n − W_p (global [2]³), element V³ = (σ₀σ₁⁻¹)³ (γγ + reading 3, #8564), proton q₀. `per_observable_100x_status.py::_qbeta_ruled_base` evaluates it from q₀, calibrated against `probes/qbeta_flavour_weight_split`. nuc11_interleaved (0.6519) and Δ_S (0.4491) kept as unscored history cells; `element_conflict_open` resolved.
- **Rows moved** (scored = two-term primary, one-term + Δm_QED −0.3317 keV): Q_β 0.65152 → 0.32510 MeV (1.672e8 → 5.844e8 ppb); m_n 939.43461 → 939.10819 (1.392e5 → 4.866e5 ppb); Δ_pn 1.16252 → 0.83610 MeV (1.011e8 → 3.535e8 ppb). HEADLINE 1/6 unchanged.
- **D2 = Q_β (owner, 18:27).** Not m_n − m_p; implied m_n − m_p = 0.8364 MeV (−35.3 %). Recorded in np-splitting audit §23 and in `neutron-qvalue-symbolic` / `mass-comparison-table`.
- **Still open (rule 13a, bean stays todo):** the mass-ordering sign (neutron sector smaller under mass ∝ trace); F_required ≈ 2.40 is outside the cos-ladder cap, so no c_k ladder of that form closes the 58 % gap.

## 2026-11-20T19:25 — OWNER RULING (Carl): the premise "the bar image of a photon is a photon" is REJECTED
Answers the OWNER DECISION of the PR #8634 entry above. Verbatim intent (relayed by coordinator, 19:25): reject the premise.
- Consequence: `borromean_of_barClosed` (#8634) stays a proved conditional, but its hypothesis φ₀+φ₁=0 is NOT a corpus premise. φ₀, φ₁ are NOT fixed to 0; they stay underived inside the 8-point factorisation set of β_Bor (2 Borromean-pair points + 6 with φ₀,φ₁≠0). Selecting a point by residual is a fit and is forbidden.
- `eChannel_barClosed` (determinant form of the e⁻ channel) is therefore not the e⁻ channel of the corpus photon.
- Owner direction in the same message: pursue N1 — derive the W as a CHARGED element and the β-decay electron channel, so Q_β (re-aimed 19:33: the decay AMPLITUDE M(q) and RATE 𝔇_n(q)) is derived from γγ / gauge-boson production, not chosen. Branch `claude/qbeta-n1-charged-w-element-2026-11-20`.
- Per owner rulings-are-conjectures preference: the rejection is recorded as a ruling about admissible premises, not as a derived statement. Bean stays open (rule 13a).

## 2026-11-20 ~20:00Z — N3: Q_β / 𝔇_n as a T⁺ matrix element (PR #8639, draft; not merged)
Lean `QOU/QuarkState/TPlusChargedCurrentElement.lean`, sorry-free; probe `computations/probes/qbeta_n3/` 15/15. Pre-registration committed before any number.
- FORCED: normalised |⟨p|T⁺|n⟩|² equals the T⁻T⁺ eigenvalue: 1 on isospin ½, [2]² on isospin 3/2 (`tplus_norm_sq` + `Fd_eq_transpose`). It does not depend on any invariant normalisation.
- FORCED NEGATIVE (scope b; invariant: T⁺ intertwines σ₁ and σ₂): every H₃ operator, β_Bor = V³ included, has the same spectrum on n and on T⁺n (`hecke_energy_transport`). So the bimodule produces no Q_β and no energy scale. G_F does not emerge.
- Leptonic factor: the charge-exchange amplitude of the weak insertion −h·P_L on one quark–lepton crossing is −h·q/[2] when the quark strand is on the left and −h·q⁻¹/[2] when it is on the right (`exchange_quark_left/right`). This is −tanh(λ)e^{±λ} with λ = ln q. It is O(h) as q→1 and vanishes iff h = 0. Bar maps the left amplitude to minus the right one.
- |M|² at proton q₀: 0.01332 / 0.00877 (isospin ½, quark left / right); 0.05385 / 0.03547 (isospin 3/2). Comparison only: 𝔇_n/m_e = 1.466e-24.
- Open choices: (1) quark-strand placement; (2) isospin ½ vs 3/2 (Δ_S lives on 3/2); (3) current–current factorisation; (4) every energy or rate scale. Bean stays open (13a).

## 2026-11-20 — W2 cross-workstream briefing (owner: "make sure they know")
Full briefing: PR #8526 comment 7047864732 and docs/coordination/2026-11-20-w2-qbeta-ud-briefing.md. Record: docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md sections 1-11.
Key points: Q_beta = (h[2]/2)*y3*E0 and sees only the isospin-3/2 block. The ruled epsilon (z_D, -43%) = label-A round trip = whole-space quantum trace. Label B (J4, strand-4 gamma-gamma) gives +0.33% and is NOT adopted (it labels isospin multiplicity, not n<->p). Label C gives 1/3, 0 and 0.202, none close. The owner made no label ruling ("3 2"). u/d are separate lines of the (3,1) rep of H4, not orientation-only (def:up/down-quark are stale). Convention-D volumes lie past the Phi_q pole. The six-term -2.43e15 was a truncated divergent series (fixed). The +0.17% / ~1 ppm Q_beta values and the April BW run are superseded or circular.

### 2026-11-20 ~20:30 — N2: n and p as distinct γγ-selected elements? (PR #8636, branch claude/qbeta-n2-derived-nucleon-elements-2026-11-20)

Pre-registered (eb81985791) before any number. Selection = γγ words (products of V_i = σ_iσ_{i+1}^{-1}, k ≤ 5 vertices) + reading 3, minimal non-zero cost. A nucleon label can enter only through a STATE-WEIGHTED reading 3 (choice S-w): tr(Π^λ_s ρ(w)) ≥ 0 on the H₃-isotypic blocks of the nucleon's own weight space s. The ruled reading 3 has no state argument, so it selects the same word for n and p by definition.

- PROVED, scope (b), three strands: `QOU.QuarkState.NucleonStateWeighted.isoChar_eq` / `feasible_iff` (lean-direct exit 0, axioms propext/choice/Quot.sound). Invariant: the unitriangular D = [[1,h,qh],[0,1,h],[0,0,1]] intertwines the H₃ action on W_n and W_p and carries the (3)-projector. Every isotypic character of every 3-strand word is equal on n and p, so S-w selects the same element. Extends #8616 from plain to isotypic traces.
- FOUR STRANDS, choice C-lep (strand 4 = lepton doublet, T³=0 space = N ⊕ P with N = n⊗ν = span(uddu,dudu,dduu), P = p⊗e = span(duud,udud,uudd); σ₃ maps N→P with no T⁺): exact probe over Z[q,q⁻¹], 62 words, 17/17 checks. All 57 strand-4 words have DIFFERENT characters on N and P, yet at the proton q₀ the feasible sets agree word-for-word. Selected for BOTH: {V₁V₂ = σ₁σ₃⁻¹, V₂V₁} (tie, 4 crossings).
- The coincidence is q-dependent, not structural: it holds on (1, q*) with q*⁶ − q*² − 1 = 0, q* = √(plastic number) = 1.150963925. Above q*, p's selection moves to {V₁³, V₂³}. q₀ = 1.10998 < q*. Lean: `charP3_nonneg_iff`.
- So no distinct n, p ELEMENTS at q₀; the selected-element difference is 0, hence ε_C(Δ) = 0 and R1 Q_β = 0. The n/p difference lives in the STATES: on the selected word the isospin-½ character difference is −(q²−1)(2q⁴+q²+1)/(q²(q⁴+q²+1)) = −0.264586341842031 at q₀ (`stateDiff_21`), first order in q−1; the (3) difference is (q²−1)(q²+1)²/(q⁴+q²+1) = 0.308292550374553.
- Charge-conserving amplitude for N1/N3: ⟨P|σ₁σ₃⁻¹|N⟩ = [[1,(q²−1)/q,0],[0,1,0],[0,0,0]], |·|² = (q⁴+1)/q², non-vanishing at q = 1 (σ₃ → swap).
- Remaining choices: S-w itself; C-lep; the tie {V₁V₂, V₂V₁}; whether "nucleon element" may include a strand-4 letter. Bean stays open (13a).

## 2026-11-20T22:30Z — N1: charged W exchange and the n → p e⁻ ν̄ amplitude M(q) (PR #8638, draft)
Pre-registered at 5ab8166249. Lean `QOU/QuarkState/ChargedCurrentW.lean` (generic Field, sorry-free, lean-direct -DautoImplicit=false exit 0); probe `computations/probes/qbeta_n1_charged_w/` 26/26 exact + 70 dps, proton q₀. Nothing wired.
- **W = the h term of the strand-tracked crossing.** P·Ř = R₀ + h·E⊗F for σ, R₀' − h·F⊗E for σ⁻¹ (`Rc_strand`, `Rcinv_strand`). The Ř off-diagonal is a transposition (no flavour change; that is what qou-g0jn RESULT 1 measured). Chiral: σ gives d ν → u e⁻ = h, σ⁻¹ gives 0 (`beta_vertex_pos/neg`). Not bar-closed: σ ↦ σ⁻¹ sends +h·E⊗F to −h·F⊗E. Charge conjugation swaps the two (`chargeConj_EF`).
- **T⁺ derived from the lepton crossing the nucleon.** ASSUMPTION (flagged, as g0jn PRE-REG 3): the lepton is a 4th strand, a second doublet, ν = u, e⁻ = d. The block n⊗ν → e⁻⊗p of σ₁σ₂σ₃ is exactly (q²−1)·Δ²(E) = h·q·T⁺ (`beta_amp_left_pos`). The general rule h·q^{N_d−1}·Δ^{(n)}(E) is measured for n ≤ 5. The same braid gives 0 for p e⁻ → n ν; the leftward negative passage gives 0; the rightward negative gives −(h/q)·T⁺, the bar image of hq (`bar_coupling`).
- **|M|²:** T⁺ᵀ = T⁻, so ‖Av‖² = (q²−1)²‖v‖² on isospin ½ and (q²−1)²[2]² on isospin 3/2. Vanishes ∝ h² at q→1 (4(q−1)²). Strictly increasing for q>1. d ln|M|²/d ln q = 4q²/(q²−1) = 21.24 at q₀. No definite bar parity (bar = mirror passage, ratio q⁴). At q₀: (q²−1)² = 0.053848; mirror 0.035474.
- **Rate family** 𝔇 = G²|M|²m_e⁵f(W₀)/(2π³), F = 1. G does NOT emerge (dimensionless construction) — gap. Q_β from the same construction: label C (T⁺ round trip, posited order-zero E₀) 0.588715 MeV → f = 0.5382, d ln f/d ln Q = 3.87 (Sargent Q⁵ only for W₀ ≫ 1). d ln 𝔇/d ln q along label C = 16.20. Owner-scored 0.325434 → f = 0.05679.
- Comparison only: implied Λ = G^{-1/2} = 68.27 GeV (label C) / 38.91 GeV (scored), against the Fermi scale 292.8 GeV. With imported G_F, 𝔇/𝔇_n = 2.96e-3 / 3.12e-4 (𝔇_n = 7.493e-25 MeV). The standard Fermi+GT factor 1+3λ² ≈ 5.8 is absent (no spin sector).
- Not derived / remaining choices: lepton-as-doublet-strand; which passage (hq or −h/q) is physical; G scale; GT part; the γγ e⁻ = σ₀σ₁σ₀ coordinate is NOT where the electron sits here (photon weights φ do not enter). Bean stays open (rule 13a).

## 2026-11-20 — fundamentals walk (PR #8662, audit §13)

- The chain Frobenius pairing → mass identity (ordered holonomy) → `feynman-categorical-trace` DERIVES ε = z_D, given C = Rep(SU_q(2)). Q_β is −43.16 % (order-zero E₀) / −42.59 % (tower E₀).
- Closed form for SU_q(N), with a = q^N: |ε_N(Δ_S)| = (h²/2)·coth(N ln q). Proved sorry-free in `QuantumTraceFamilyCoth.lean`.
  - N = 1 is the augmentation, +12.47 %.
  - N = 2 is z_D.
  - N = ∞ is the standard trace, −88.3 %.
  - No integer N lands. The diagnostic real N* = 1.126 is not adopted.
- The framed mass gives σ and σ⁻¹ the same value, 1/[2], so Δ vanishes under the braid-class mass definition. Q_β here is a writhe effect; this is a tension in the definitions.
- The scale is not on the chain. On z_D, CODATA needs 1.7592 × E₀. The mass-channel scale sends Δ to 100.5 MeV.
- So the gap points at the scale, not the functional. Still open.

### 2026-11-20 ~21:00 — Q_β from U_q(gl₂) outside H_n (PR #8661, branch claude/beta-rate-qbeta-energy-beyond-hn-2026-11-20)

Owner asked (~20:15): derive Q_β as an energy, consistent with the q-rate, with nothing chosen. **Result: not derived.**
- Derived: the amplitude (q²−1)T⁺ = Ad_K(T⁺) − T⁺. So the rate's q-dependence is the Cartan charge 2 of T⁺ (e^{2λ}−1, λ = ln q). It contains no MeV scale.
- Scope (b): twist, Casimir and anything central agree on n and p (`eigen_eq_of_commute`). n⊗ν and p⊗e⁻ lie in one K^{⊗4} weight space (`exchange_preserves_weight`). So any K-weighted 4-strand split, and any one-coefficient linear Cartan energy, gives Q_β = 0. The scored 0.3254 MeV (#8586) is the quark-only half of a conserved quantity, and is non-zero only because the lepton strand is kept out of the K-grading (a premise).
- Scope (a) table at proton q₀: h·E₀^tow = 0.8838 MeV (+13.0 %), 2 ln q·E₀^tow = 0.8822 (+12.8 %), h·m_e = 0.1068 (−86.3 %). These are one cell, since h = 2 sinh λ. They need a scale, the log/linear choice, and the lepton strand dropped. **Not a lead.**
- Lepton strand under the #8586 functional: |ε_ℓ|E₀ = m_e(q+1)/(q(q²+1)) = 0.4395 MeV, which is not m_e. The additive (ε_q − ε_ℓ)E₀ = 0.114 MeV needs m_n < m_p and m_e < m_ν.
- E₀: E₀·g = m_e only for g = q(q−1), the K-gap between q² and q, which no doublet carries. Still posited (qou-mkm8).
Lean `QOU/QuarkState/CartanEnergyTransport.lean` (generic Field, sorry-free). Probe `computations/probes/qbeta_uq_energy/` 14/14. Audit `docs/audits/2026-11-20-qbeta-energy-outside-hn.md`. Bean stays open (13a).

### 2026-11-20 ~21:00 — Q_β from U_q(gl₂) outside H_n (PR #8661, branch claude/beta-rate-qbeta-energy-beyond-hn-2026-11-20)

Owner asked (~20:15): derive Q_β as an energy, consistent with the q-rate, with nothing chosen. **Result: not derived.**
- Derived: the amplitude (q²−1)T⁺ = Ad_K(T⁺) − T⁺. So the rate's q-dependence is the Cartan charge 2 of T⁺ (e^{2λ}−1, λ = ln q). It contains no MeV scale.
- Scope (b): twist, Casimir and anything central agree on n and p (`eigen_eq_of_commute`). n⊗ν and p⊗e⁻ lie in one K^{⊗4} weight space (`exchange_preserves_weight`). So any K-weighted 4-strand split, and any one-coefficient linear Cartan energy, gives Q_β = 0. The scored 0.3254 MeV (#8586) is the quark-only half of a conserved quantity, and is non-zero only because the lepton strand is kept out of the K-grading (a premise).
- Scope (a) table at proton q₀: h·E₀^tow = 0.8838 MeV (+13.0 %), 2 ln q·E₀^tow = 0.8822 (+12.8 %), h·m_e = 0.1068 (−86.3 %). These are one cell, since h = 2 sinh λ. They need a scale, the log/linear choice, and the lepton strand dropped. **Not a lead.**
- Lepton strand under the #8586 functional: |ε_ℓ|E₀ = m_e(q+1)/(q(q²+1)) = 0.4395 MeV, which is not m_e. The additive (ε_q − ε_ℓ)E₀ = 0.114 MeV needs m_n < m_p and m_e < m_ν.
- E₀: E₀·g = m_e only for g = q(q−1), the K-gap between q² and q, which no doublet carries. Still posited (qou-mkm8).
Lean `QOU/QuarkState/CartanEnergyTransport.lean` (generic Field, sorry-free). Probe `computations/probes/qbeta_uq_energy/` 14/14. Audit `docs/audits/2026-11-20-qbeta-energy-outside-hn.md`. Bean stays open (13a).

## 2026-11-20 — Gamow–Teller / spin sector of the β rate (PR #8670, branch claude/beta-rate-gamow-teller-spin-2026-11-20)

Owner ask (~20:15): derive the rate as a function of q, nothing chosen. #8638 gives a Fermi-only |M|² = (q²−1)²; this entry covers the factor 1+3λ². Pre-registered at 43739c0575.
- Corpus: no object carries Lorentz spin. The one U_q(sl₂) doublet is used as isospin in #8638 and is called "spin" in spin-labels / q-angular-momentum. QuarkStrandConsequences Result 1 allows at most one q-braided factor. AxialCoupling.lean (5/3·tr ratio) and gt_matrix_pslq_probe ([5]_q/[4]_q) select against the target 1.2754, so they are not used.
- (A) Factorised iso⊗spin, spin braided by the swap: λ ≡ 0 for every q, including q → 1. Lean: `crossing_commutes_spin`, `swap_commutes_sym`. Scope (a): crossings of this form give no axial current.
- (W) Unfactorised U_q(gl₄), u labels ranked first: quark-level block h·P_spin = (h/2)(1+σ⃗·σ⃗), so λ_q = 1 exactly. Lean: `beta_block_isoMajor`, `swap_fierz`, `beta_block_zero_of_lt`. The other 20 orderings give no block in σ (4) or a partial, rotation-violating one (16).
- (W) nucleon level, CONDITIONAL on the C-SU6 nucleon choice: |λ| → 5/3 at q → 1. At q₀ the u↑u↓d↑d↓ ordering gives λ_⊥ = 1.66744, λ_z = 1.66295 and R = 9.328; anisotropic, with a (σ_N×σ_ℓ)_z term at O((q−1)²). The u↑/u↓ order changes λ (not pre-registered). Against PDG (comparison only): +30.6 % in λ_eff, +58.6 % in R.
- Choices still open, each with no derivation: (1) where spin lives, (A) or (W); (2) the gl₄ label ordering; (3) the N/Δ separation inside the q-symmetric 20; (4) the lepton premise inherited from #8638. Bean stays open.

## 2026-11-20T23:40Z — the lepton-strand premise of N1 (PR #8673, `LeptonStrandPremise.lean`, 28 decls, sorry-free)
- Given L (the lepton is a V-strand in the same K-grading), ν=u and e⁻=d are DERIVED by total-T³ conservation and by GMN with one Y (Y=−1). Swapped labels and a singlet lepton are EXCLUDED, scope (b).
- L itself is UNDERDETERMINED. The corpus defines leptons as knots (trefoil, unknot) and β⁻ as the L₀⁻ smoothing.
- The left line does NOT select the passage. σ and σ⁻¹ are scalars on the same line. W_L flips flavour in both strand orientations. W_R = q²·W_L.
- Only left+ ((q²−1)T⁺) and right− (−((q²−1)/q²)T⁺) carry a β block. The corpus positive electron braid σ₁³ selects left+ (C-lep), via a bridge that is not proved.
- γγ e⁻ = σ₀σ₁σ₀ closes to ≥2 components, T(2,3) to 1. These are different objects.
- With #8661: L ⇒ the K-weighted Q_β = 0. Without L, the 0.3254 cell stands, but #8638/#8636 lose their derived labels.
- OPEN, owner: adopt L or reject it (framed in the #8673 body). Bean stays open.

## 2026-11-20 — option 1 attempted: is E₀ on the chain? (owner "Try"; PR #8662, audit §14)

Scope-(a) negative.
- E₀ = m_e c_q² ℏ_q exactly: the chain's 𝔈 = 𝔪 c_q² times an extra "per tick" ℏ_q that no step of the chain supplies. CODATA needs 1.7592 ℏ_q instead.
- At single wrap, Δt/t_p = −0.341, against a physical 0.00138 (248× smaller). So any scale shared between the nucleon and Δ overshoots:
  - 320 MeV (linear);
  - 531 MeV (Frobenius norm ⟨x,x⟩);
  - 100 MeV (mass channel).
- Q_β needs a scale decoupled from the nucleon mass. Which m_e·ℚ(q₀) element that is, and why, is open.

## 2026-11-20T21:30Z — up-quark (unknot) vs electron-knot ("shares trefoil") clash, investigate-and-propose (PR #8677)

Owner asked to investigate the clash surfaced by #8673. Audit doc `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`, no content changed.
- 13 sites call the up quark an unknot in B3 (def:up-quark, def:down-quark, rem:knot-particle-dictionary, conj:borromean-quark, categorical-proton, particle-nf-table, ParticleKnots.lean); 14 call it T(2,3) (def:electron-knot + .lean docstring, torus-knot-prime-powers, generation/building-block tables, strangelet blocks, jet-planck spectrum, transfer-matrix appendix, TorusKnot.lean:74 docstring).
- No owner ruling, no deriving Lean (knot-type theorems are rfl on structure defaults), no producer consumes a quark knot type.
- Structural (b, given Borromean reading): B3=(s0 s1^-1)^3 is pure (borromean_perm_eq_one) => each closure component is an unknot, so a B3 quark cannot be a trefoil. Strand-deletion step not formalised.
- "Lepton descent" (u <- T(2,3)) refterms the jet-level descent homomorphism; no derived knot->quark map. Undefined relation.
- Options A (reword electron block: trefoil = up quark's lepton partner; 4 files), B (A + 13-site sweep, rescopes transfer-matrix appendix and strangelet), C (trefoil canonical, drops Borromean model), D no-op (default). Agent recommendation (judgement): A now, B separately.
- OPEN, owner. Adjacent: sdp_gamma_gamma_to_qqbar.py:15,124 says s0s1s0 closes to a trefoil, contradicting perm_e_gg; unchanged.

## 2026-11-20T22:30Z — hypercharge as a second strand grading (PR #8676, `HyperchargeGradingNoGo.lean`, sorry-free)
- Owner Q: under L, is ν "the same as u" or at a higher q power? Test: dress strands by q^{cY} (Y_q=1/3, Y_ℓ=−1). Coordinator redirect recorded in PREREGISTRATION.md.
- No-go, scope (b), invariant = separability (T³ on flavour, Y on type): `total_eq_iff`, `T3_Y_conserved`, `split_zero_of_total`, `grouplike_weight_eq` — every grading that is a function of conserved totals gives split 0 for EVERY c. Y(nν)=Y(pe)=0.
- Matrices: `EF_commutes_dressed`, `EF_commutes_charge` (total Q conserved), `Rc_intertwines_dressed`, `weight_transport`.
- Ruled functional blind to c: `normalised_trace_dressing_cancels` (per-strand scalar cancels in Tr(K·)/Tr K).
- Only a per-strand UNnormalised additive energy separates: `split_eq` (g_ℓ−g_q)(q−q⁻¹); `split_hyper_eq_zero_iff` zero iff c=0; q=e^λ: −(8c/3)λ²+O(λ³). This is NOT the ruled ε; it is a new premise.
- Forced c: none (Y open in eightfold-open-problems; gl₂ centre K₁K₂ = q on every fundamental strand). c=1 = electric-charge grading, a premise. No Q_β number computed (pre-registered).
- Candidates not conserved by the vertex: Higgs vacuum idempotent e_H (HiggsVacuumResidual.lean, no strand action defined); colour (no colour action on strands; ColourBridge only q=1). OPEN.

## 2026-11-20T22:30Z — owner ruled OPTION B on the up-quark/electron knot clash (PR #8677, now ready, not merged)

Applied: def:electron-knot (+ TorusKnot.lean:74, categorical-proton.lean docstrings) says the trefoil is the up quark's LEPTON PARTNER; the 5 tables, transfer-matrix appendix (3 blocks), strangelet (2), torus-knot-prime-powers, jet-planck, knot-formula-table (+tbl 2: quark genus/crossings now 0, as ParticleKnots.UpQuark), unmapped-torus-knots reworded; argument-bearing blocks carry dated refined-framing authorNotes (assumed / still valid / needs re-scoping); sdp_gamma_gamma_to_qqbar.py:15,124 comments fixed (perm_e_gg). Lean-direct exit 0 on 3 docstring-only files.
CORRECTION of my 21:30Z note: "no producer consumes a quark knot type" was WRONG. Meson/weak-isospin cluster gives quarks T(2,n) writhes ±3/5/7 and proves things about it: WeakIsospinT3Grading, MesonOperatorSelectionT3, MesonFluxTubeReduction, MesonFusionIndexSelection, lepton-meson-torus-knot-dictionary.lean; meson_braid_length_cap_probe.py -> meson-braid-length-cap.witness.json; weak-isospin-t3-grading.witness.json; knot-notation-convention. NOT changed (report-before-change). m_K/m_π credited Lean unaffected.
OPEN, owner: (i) re-read |κ| as the lepton partner's crossing count (relabel; all theorems kept) [agent recommends, judgement]; (ii) rebuild on single crossing letters; (iii) default no-op = two quark models in the paper.
Not run: qa-sweep (light platform lacks fast-xml-parser), precision-gates (timeout; comment-only compute change). Bean stays open.

## 2026-11-20T20:15Z — P1/P4: β decay as ONE GS reduction in H₆ (PR #8681, draft; pre-reg c59f09c7fb)

Owner 20:52 local: "a beta decay is not standalone … a Gröbner basis calculation". Words: β_Bor=(σ₀σ₁⁻¹)³ on strands 0–2 (n and p are one element, #8636), pair Γ=γ(φ)γ(ψ) on 3–5 (owner photon, φ symbolic), bridge letters. Exact H₆ engine on T_w, validated vs #8634 NF(β_Bor), pairNFChiral e⁻ coord, BorromeanMarkovTrace; ρ(word)=ρ(NF) checked. Probe 25/25, witness proton q₀ 70 dps.
- P1 cross term C=tr(W)−tr(β)tr(Γ)tr(bridge) is identically 0 for split, one bridge σ₂, clasp σ₂², β σ₂Γσ₂^{±1}, shared strand (H₅): every connected-sum assembly factorises (scope b, Markov multiplicativity; exact, not Lean). Non-zero only when a bridge strand wraps ≥2 strands of the other side: loop round 2 nucleon strands O(h⁵), round 3 / passage-and-return O(h⁶), single passage O(h²). Even then C=κ(q)·tr(Γ) (pair joins at one strand); only two pair strands wrapping (W4b) give a genuine pair functional, e⁻ coefficient ∝ −h²·tr(β)·…. All flavour-blind (same element for n,p).
- Energy E_N=m_μ|tr|[N]!/q^N: S₆=47391 MeV/unit; E(e⁻_BW)=327, E(e⁻_K σ³)=146 MeV ≫ m_e. Q principal = −30 GeV … +28 GeV; S₆·C = 9.85 (W3), 3.12 (W4/W6), −940 (W7) MeV. None near 0.782, none selected.
- P4 (Jimbo, lepton=second doublet, #8638 assumption): K-weighted sector trace (sums to the z_D trace, Lean `qtr_markov`) gives n⊗ν = p⊗e⁻ for the split word and ≠ for EVERY entangled word (incl. a single σ₂); kernel `secDiff_H2`: separation = h × σ-coefficient = the strand-tracked W term. Q₄ = S₆·Δ̂ = 180 MeV … 6.7 GeV. Escape from the factorisation no-gos is real in states, not in elements; no MeV-scale functional emerges.
- OPEN: what energy functional is additive across subsystems (trace is multiplicative, so "same functional on initial and final" is not an energy balance); whether the lepton strand count/scale S_N is admissible at all.

## 2026-11-20 P3: energy as Δ of a normal-form invariant (PR #8682, draft)
Owner 20:52 ("higher q power"?). Pre-reg `7f9016bf4e`. Lean `QOU/QBeta/NormalFormLengthInvariants.lean` (sorry-free, generic ring): GS rewrites at any position preserve the T_w coefficient vector in H₃ (`eval_quad`, `eval_braid`), so leading Bruhat length, χ = Σc_w q^{ℓ(w)} (index character = q^{writhe}) and corpus E_gs = Σ|c_w|ℓ(w) are rewrite-order independent; the R3 step count (25 vs 30) is not.
- χ(p) = q²·χ(n) in both typed models (Lean short model): proton two q-powers higher; = Cartan charge 2 of T⁺ (#8661).
- V³ (γγ base, n = p): Δ = 0 for every invariant. Leading length never separates n, p.
- Decay Δ: Δℓ_lead = 1 (e⁻ = σ₁³) or 3 (σ₁σ₂σ₁); Δlog_q χ = 5 (typed) / 3 (V³).
- Required κ/m_e (comparison only): 1.53099 (Δℓ=1), 0.51033 (Δ=3), 0.30620 (Δ=5) vs Q 0.78233; no corpus scale per unit exists.
- One linear scale on χ-degree has a sign conflict (p higher but lighter; e⁻ at +3, massive). Scope (a).
- Side: `beta_decay_energy_negative` (E_gs daughter < parent) holds in the short model (−0.209), fails in the 11-letter model (+0.064), equal on V³.

## 2026-11-20T21:45Z — P2: e⁻ν̄ pair as ONE word entangled with the proton (PR #8680)

Leptons from the knot blocks (e⁻ = σ³ trefoil, ν̄ = 1-strand unknot); exact conv-D Markov trace over ℚ(q); 777 six-strand final-state words, proton pin 70 dps. Audit `docs/audits/2026-11-20-beta-entangled-lepton-pair.md`.
- Clasp σ₁^{±2} multiplies ANY 2-strand trace by λ₊=(q⁴+1)/(q²+1), λ₋=(q⁴+1)/(q²(q²+1)) (Lean sorry-free, `QOU/QBeta/EntangledLeptonPairTrace.lean`).
- Leptons attached through ONE nucleon strand are nucleon-blind: tr(W)/tr(N) identical for p, n, β_Bor in 9+729+27 words (connected sum; families A,B proved by Jones multiplicativity, C measured). Only a full twist on ≥2 nucleon strands + e⁻ is nucleon-sensitive (12/12); its trace cross term ∝ q⁶−1 (ν̄ unlinked), → 0 at q→1.
- Trace channel |tr|[N]!/q^N extended uniformly (my extension; corpus defines N=3 only): E(ν̄)=m_μ/q₀=95.19 MeV, E(n)−E(p)=−72.92 MeV, X∈[8.5e3, 8.3e4] MeV, Q∈[−8.3e4, −8.8e3] MeV vs CODATA 0.78233. Scope (a). Volume channel gives e⁻, ν̄ zero; entangled volumes not computed (no SnapPy).
- Linking letters are chosen: the corpus writes the pair only as ⊔. Still open; not closing.

## 2026-11-19 — PR #8518's "70–76% of the N=2 residual" is measured on the retired base

Probe `computations/probes/np_two_term_qed_mup_tension_probe.py`, run on main. Its `Q_N2^D` is `Q_A·cos(α−u/2)·(1−u²)` with `Q_A` = Form A (z=1, 0.7836458 MeV); only the phase uses z_D. The N=2 residual there is +600.6 ppm (0.00046988 MeV). The four DERIVED-Bor-V3-Conn weightings (−0.000332 to −0.000368 MeV) cut it to 177–130 ppm, i.e. 62–78%. On the ruled z_D base the same terms close 0.10–0.11% of the gap (order-zero E0, Q = 0.4447004, gap 0.3376 MeV) or 0.25–0.28% (dashboard cell 0.6518563, gap 0.1305 MeV). Four weightings of one term plus ~30 other candidates are listed, so taking the best match is selection against the target. Not a closure on the ruled base.
## 2026-11-21 01:10Z — RESULT B (one-strand blob), sample point q = 11/10, Q = 3/2, y = 1/3 (exact rationals)
Method: Ariki–Koike seminormal representations of H₃^B for all 10 bipartitions (relations checked symbolically); Geck–Lambropoulou trace weights solved from the Markov conditions (z = z_D, tr t'_k = y), unique at n = 2 and n = 3.
- tr(β_Bor) = 0.99900075 (matches the type-A value at this q, as it must).
- One loop (p, d at slot 0/1/2): tr(β·t_d)/tr(β) = y EXACTLY for every slot. A single blob only multiplies by y.
- Two loops (n): slots (0,1) 0.106602, (1,2) 0.116568, (0,2) 0.106602, against y² = 0.111111. Slot-dependent, so the flip symmetry is broken, as expected.
So B can separate p from n, but the split is set by the free blob data (Q, y), which nothing in the corpus fixes. Scope (a): B is a parametrised ingredient, not a derived split. Nothing scored. Symbolic (Q, y) run not done (timed out); scripts in session scratchpad blob/.

2026-11-21 01:20Z — corpus search for the energy unit of the charge term (owner "go").
- Only derived assignment found: PR #8518's own Lagrangian bridge (CategoricalLagrangianTwoTermBridge.lean, hadronicScale_mul_q_sq_hbar_eq_me): matter/charge term unit = E₀·ħ_q = m_e/q². With the 05:10Z rule: Δ_EM = −0.0305 MeV (smaller still). Not a new choice: it is the unit that bridge already states.
- The same obstruction is already on record for ³H/³He: docs/audits/2026-06-03-em-linking-invariant.md names the missing object as "a categorical brane-separation / nuclear-charge-radius length scale" (3.2× factor = r_strong/r_charge). The nucleon EM gap is the same class.
- Other corpus energy units (E₀, α_bind = 8G·m_e) exist but none is derived as the unit of a Coulomb term; choosing one by its result would be a fit. Not computed.
- Status: OPEN. Needs a derived categorical length (or crossing-energy) scale for the nucleon. Not closable by trace or weighting choices.

## 2026-11-21 — owner option 1 applied: meson/weak-isospin quark 3/5/7 are lepton-partner labels (PR #8698)

Owner ruling 2026-11-21 (option 1 of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md` §"Still open"): the ±3/±5/±7 carried by quarks in the meson cluster is re-read as the LEPTON PARTNER's crossing count (generation label); the sign is the quark strand's crossing orientation. Prose and docstrings only.
- Lean (all lean-direct exit 0, `-DautoImplicit=false -s 65536`, imports Mathlib only): WeakIsospinT3Grading, MesonOperatorSelectionT3, MesonFluxTubeReduction, MesonFusionIndexSelection, lepton-meson-torus-knot-dictionary.lean. No theorem statement or def body changed; none asserts a quark is a torus knot (all are integer arithmetic). Identifiers `signedWrithe`/`genWinding`/`quarkTorusIndex` kept as names.
- `scanPair_four_not_dictionary_index` ("4 is not a quark index"): premise lost as a statement about quarks; dated docstring note, kept.
- For the owner: `CanonicalWeakIsospinFromBowtie.writhe_magnitude_is_generation` can no longer be met by a quark strand's own net crossing (±1); only via the partner label. Docstring note added, statement unchanged.
- Content: dictionary prop+proof+authorNote; knot-notation-convention (+table 1 charm row); also q-chromaticity and strangelet-merger-signature (two quark=trefoil sites #8677 did not list), with re-scoping flags.
- Compute: meson_braid_length_cap_probe docstring only — the 14-crossing cap premise is not supplied by the ruling; scriptHash drift, not re-run. weak-isospin-t3-grading / meson-braid-length-cap witnesses untouched.
- m_K/m_π row unaffected: per_observable_100x_status.py reads none of these files or witnesses.

## 2026-11-21 — route Y: Higgs-vacuum Yukawa-type pairing with doublet strands (PR #8694, draft)
Owner route Y. Pre-reg `76ddb991d3`. Lean `QOU/QuarkState/YukawaVacuumPairing.lean` (sorry-free, generic field; axioms propext/choice/Quot.sound). Probe 23/23, witness proton q₀ 70 dps.
- Forced: an operator commuting with the unbroken grading is weight-diagonal (`eq_diag_of_commute`); a trace-1 idempotent is P_u or P_d (`idem_commute_trace_one`). tr e_H = 1 puts the vev in a grading-weight-0 slot (`vev_charge_zero_of_trace_one`); impossible on bare q^{2T³} (`no_vev_on_bare_T3`).
- Type-blind pairings (one morphism on all strands) give split 0 (`split_typeBlind`). Compressed a·1+b·Ř: diag(a, a+bq) vev d, diag(a+bq, a+b(q−q⁻¹)) vev u. General diagonal: split = (a_q−b_q)−(a_ℓ−b_ℓ), 4 free.
- Charge selection (only non-type-blind candidate): q^{3Q}-invariant 2-point pairing with the neutral vev vanishes on charged slots — quark couplings 0 (`pairing_quark_zero`), e⁻ 0 (`pairing_lepton`), ν free (`nu_coupling_free`); split = y_ν² (`split_neutral`), order q⁰, ≠ 0 at q=1. Gives energy to ν: opposite of SM (needs a right-handed singlet the strand model lacks).
- No magnitude forced → no Q_β number (pre-registered). Comparison only: CODATA Q_β/m_e = 1.53099. Premise L assumed in arms 3–4, still open.

## 2026-11-21 — route L (additive log-trace energy), PR #8693
Owner-selected route L. E_κ = κ·log|tr| (conv-D Markov trace, no [N]!/q^N factor). It is the corpus's own B_sym channel (α = E₀), applied to the β words. Lean `QOU/QBeta/LogTraceAdditiveEnergy.lean` (sorry-free).
- Additive on one-strand joins, unconditional (`logEnergy_tr_mul_adjoin_gen`); on disjoint blocks only conditional on `TowerSpan` (`logEnergy_disjoint_of_towerSpan`). Cross term = κ·log|trW/Πtr| (`crossTerm_eq_log_ratio`); ν̄ strand ↦ 0.
- κ NOT fixed: additivity is invariant under κ ↦ cκ. α = E₀ is a named normalisation. The volume conjecture cannot supply κ (coloured Jones at e^{2πi/N}, not tr_M at real q₀; Vol(3₁) = 0 but log|tr(3₁)| = −0.16425).
- P3 sign problem survives (`no_kappa_for_index_character`).
- On the P2 Markov traces, both Q > 0 and E(e⁻) > 0 need κ < 0 (`markov_log_signs`; hypotheses checked exactly). The corpus sign (+E₀) makes β⁻ endothermic: split Q = −0.4889 MeV. At κ = −E₀ it is +0.4889 (−37.5 %), but that is sign selection, not derivation. κ needed = −13.107 m_e.
- P1 wrapping words: C_log = 1.63e-4 (W3), 4.59e-5 (W4/W6), −0.0903 (W7); all R → 1 at q → 1. Family D: the sign of Q follows the chosen twist sign.
Audit `docs/audits/2026-11-21-qbeta-route-l-additive-logtrace-energy.md`. Still open; not closing.

## 2026-11-21 — task W: which word creates the β⁻ lepton pair (PR #8696, draft)
Pre-reg `ee04d3c394`. Lean `QOU/QBeta/PairCreationWordGammaGamma.lean` (sorry-free, lean-direct exit 0). Probe 8/8, witness proton q₀ 70 dps, exact ℚ(q). Setting: H₄, β_Bor on strands 0–2, one lepton strand [premise L].
- Writhe excludes from γγ (scope b): passage σ₀σ₁σ₂, trefoil σ₀³, T(3,5), single σ₂.
- CC + minimality forces σ₂ alone (nucleon-blind, cross term 0). G∧CC forces V₁ (fails R3). G∧CC∧R3 + crossing-count minimality forces **V₁³ = (σ₁σ₂⁻¹)³** uniquely (V-only grammar; 8 ties with mirror V̄). V₁³: CC O(h²), NOT chiral, cross term order 6, lepton closes to unknot.
- Passage (chiral, (q²−1)T⁺) fails R3 (χ_(3,1) = −1.218); T(3,5) fails (χ_(2,2) = −1.133).
- Proposal `docs/audits/2026-11-21-beta-pair-creation-word-proposal.md`: options A (V₁³), B (passage, amend qou-ales), C (σ₂), D (rule mirror vertices first). Default: nothing ruled, pair stays ⊔. Recommendation (judgement): D then A. Still open; not closing.

---
# qou-99qc
title: 'OWNER CALL: Delta prose vs epsNPq — one of the two is wrong (fork forced by qou-avt6)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-26T07:35:22Z
updated_at: 2026-11-21T06:59:28Z
parent: qou-10v9
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
Lean:  folio/quantum-observable-universe/lean/QOU/QBeta/CounitSigmaOneForcesHZero.lean

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
[`prf:algebraic-gns-embedding`](folio/quantum-observable-universe/observations/algebraic-gns-embedding-proof.md)
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


## 2026-09-05 (2) — "closed at two" is closed in ONE class. The hierarchy, measured.

Owner asked, on the two admissible options: *"what are options for admissible?
others?"*

Probe: `computations/qbeta/qbeta_admissible_functional_hierarchy_probe.py`
(13/13, exact sympy over ℚ(q); every dimension computed, none asserted).

This bean says the admissible set is **"closed at two elements"**. That is true
and it is closed **within the one-parameter Markov family `tr_M^z`** — it comes
from solving `y_(1³)(z) = 0`, a quadratic. It was never a statement about every
functional that descends. Measured across three nested classes:

| class | admissible subspace |
|---|---|
| all linear functionals on `H₃(q)` | **5 of 6** dimensions |
| **trace** functionals (`φ(ab) = φ(ba)`) | **2 of 3** |
| Markov traces `tr_M^z` | **2 points** — `z = q`, `z = z_D` |

The `(1³)` ideal is computed as the common `(−1/q)`-eigenspace of both
generators (dim 1, so admissibility is exactly one linear condition), not
quoted.

### The load-bearing result: relaxing the class adds NO new direction

    rank{aug, tr_M(z_D)}                        = 2
    rank{aug, tr_M(z_D), χ_(3), χ_(2,1)}        = 2      ← equal

**The two Markov points already SPAN the admissible trace space.** So going
from "Markov trace" to "any trace" buys only the *line through the two you
already have* — which is precisely the one-parameter fit this bean refuses. It
does not widen the honest options.

Going further, to **all linear functionals**, does add three dimensions. But a
non-trace functional is not a Markov trace, and the trace property is what
connects the functional to knot invariants at all. That is the trade, stated
rather than taken.

Control included: `net` sits outside the admissible trace space
(`rank{aug, tr_D, net} = 3`), reproducing this bean's rank-3 exclusion from a
different construction — the character basis rather than the covector one.

### And `w*` is the fit in closed form, not a derivation

`Δ` is supported on `{γ, σ₀, σ₁}`, so `tr_M^z(Δ) = h²/2 − h·z` is **affine in
`z`** — which is *why* a weight always exists. Matching any target is then
interpolation of the parameter:

    w* = (1 − z_D)/(q − z_D) = −(q³ − q² − 1)/q      (= this bean's w*, verified)

So `w*` is just where the inadmissible `z = 1` sits between the two admissible
roots. A restatement of one-equation-one-unknown.

**A near-miss worth recording.** `w*` carries the factor `q³ − q² − 1`, and so
does `N(q,1) = (q−1)(q³−q²−1)` — the admissibility numerator at the
inadmissible point. That looked like structure. It is a **shared cause**, not
independent evidence: both quantities measure how far `z = 1` is from being a
root, so the same polynomial must appear in both. Recorded because the
coincidence is attractive and would support a "the weight is forced" reading
that the algebra does not license.

**Answer to the question as asked: no, there are no other honest options.** The
two remain the two; everything between them is a fit; everything outside them
costs the trace property.

Scope-(a); nothing wired, no content block edited, no `c_k` proposed.


## 2026-09-05 (3) — DECISION DOCUMENT: the seven options, costed

Owner: *"Do a deep analysis of all the options. Include the pros and cons
downstream impacts recommendations."*

[`docs/audits/2026-09-05-qbeta-functional-decision-options.md`](../docs/audits/2026-09-05-qbeta-functional-decision-options.md).

The two existing audits state the *finding*; neither enumerates what can be
**done**. That gap is what this fills. Seven options, each with what it means /
costs / risks / commits to, plus the downstream map and a recommendation.

Two facts established here that change how the whole thing reads:

- **The 0.17 % is not a fit.** The ansatz appears in audit docs from
  **2026-05-01**; convention D was ruled **2026-08-15**. The number predates
  the constraint that excludes its functional by ~3.5 months. *(Chronology from
  authored filename dates — `git log` dates are rebase-rewritten here and are
  not a valid signal. I tried `git log -S` first and it returned the landing
  commit, not the authoring one.)*
- **No calibration moves under any option.** AGENTS.md: Q_β is a
  *"cross-check, not a fourth input"*. q₀, m_e, m_π, the mass channel and the
  binding channel are all untouched whichever way this goes. That makes the
  decision far lower-stakes than the +0.168 % vs +12.470 % gap suggests.

And **one hope killed**: passing to the TL quotient does *not* collapse `Δ_S`
and `Δ_L` into one class — the augmentation is admissible and separates them
(+12.470 % vs +39.324 %). **The functional question and the element question
are independent**; settling either leaves the other open.

**Recommendation (judgement, not finding): Option A** — keep the published
value, disclose the inadmissibility, and reclassify it as a pre-D / C-frame
conditional result, exactly as the `c_k` ladder is already handled. It is the
only option that describes the situation accurately, the blast radius is near
zero, and it forecloses nothing. Explicitly **not** recommended: adopting the
augmentation or the `z_D` trace, which replace a correct-but-inadmissible
number with an admissible-but-wrong one.

Option G (drop the trace condition) is listed but **struck**, not weighed:
without the trace property the value depends on the braid word rather than the
link, so the element ambiguity becomes permanent rather than open.

Scope-(a); nothing wired, no content block edited, no `c_k` proposed.
## 2026-09-05 (4) — OPTION E, formalize-first: the requirement is "scalar mod radical", and Δ_S provably fails it

Owner: *"formalize first!!! E"*.

Lean: `QOU/QBeta/AdmissibleAgreementDeterminesClass.lean` — **5 theorems, 0
sorries, `lean`-direct exit 0** against the real import cone.
Probe: `computations/qbeta/qbeta_option_e_forced_class_probe.py` (9/9, exact
sympy over ℚ(q); the pin enters only at readout).

### The narrowing, stated before computing

Option E is a trap attacked numerically: a functional on `H₃(q)` is surjective,
so a free `Δ` reproduces **any** target and the "derivation" is a six-parameter
fit against one anchor. Two structural facts remove all six:

- an admissible trace sees `Δ` only through `(χ_(3)(Δ), χ_(2,1)(Δ))` — 6 → 2;
- **both** candidate functionals are *normalised* (`ε(1) = 1`). Measured
  symbolically: `tr_M(z_D) = α·χ_(3) + β·χ_(2,1)` with
  `α = (q⁴+1)/(q²+1)²`, `β = q²/(q²+1)²`, and **`α + 2β = 1` exactly**. Since
  `χ_(3)(1) = 1` and `χ_(2,1)(1) = dim V_(2,1) = 2`, that line *is* the
  normalised admissible family — **one** parameter, not two.

### The sharp theorem, and it is better than what I set out to prove

I began with a 2×2 system ("two functionals agreeing pins the class"). The
numbers then showed `(1−α)/β = 2` **exactly, for all q** — and 2 is
`dim V_(2,1)`. That upgrades the result:

> **`normalised_agreement_iff_scalar`** (sorry-free): writing `a = χ_(3)(x)`,
> `b = χ_(2,1)(x)`, a normalised admissible trace gives `(1−2β)a + βb`. This is
> independent of `β` — i.e. **every** normalised admissible trace agrees, not
> merely the two named — **iff `b = 2a`**.

`b = 2a` says `χ_λ(x)/dim V_λ` is equal across both surviving blocks, which is
exactly **"`x` is a scalar modulo the radical"** (for `x = c·1`,
`χ_λ(x) = c·dim V_λ`). So the requirement is not an arbitrary extra condition
invented to close a gap — it is the statement that `Δ` is central-scalar in the
quotient the theory lives in, and it fixes the common value to `χ_(3)(Δ)`.

### And Δ_S fails it identically — scope-(b), invariant cited

    chi_(2,1)(Delta_S) = 0          exactly over Q(q)
    chi_(3)(Delta_S)   = (1-q^4)/(2q^2)  != 0

**`Δ_S` is supported, modulo the radical, entirely in the trivial block.** So
`b = 2a` fails identically and **no** admissible functional makes the Q-value
independent of the choice.

Two consequences worth keeping:

1. **The +12.470 % and −43.157 % cells are not two independent estimates.**
   Verified exactly: `tr_M(z_D)(Δ_S) = α·aug(Δ_S)`. They are *one* number
   rescaled by `α ≈ 0.5054`. The apparent "bracket" on `Δ_S` is an artifact of
   that single scaling, which weakens the bracket framing further than
   `2026-08-29` already did.
2. **The forced class is `χ_(3) = T`, `χ_(2,1) = 2T`** with `T = Q_codata/E₀ =
   0.1868936675566543…`. `Δ_S` is `+12.470 %` off in the first coordinate
   (calibration: this *must* equal the known augmentation cell, and does) and
   **−100 %** off in the second.

### What this does NOT establish

- **Functional-independence is POSITED.** It is not a theorem of the framework
  that a physical quantity must survive swapping the augmentation for the Markov
  trace, any more than an operator's trace must equal its determinant. What the
  formalisation buys is that the requirement is now *precise and falsifiable* —
  "scalar modulo the radical" — rather than a vague appeal.
- **No element realising the forced class is exhibited**, and none is claimed to
  exist among legitimate braid-word differences. That is the next step and it is
  where Option E either closes or dies.
- `Δ_L` is untouched here; `qou-avt5`'s finding that `Δ_S ≠ Δ_L` stands.

Nothing wired, no content block edited, no `c_k` proposed.

### Extension, same day — BOTH candidate elements are excluded for every physical q

The Δ_L row was extracted from the two admissible evaluations rather than a
coordinate vector (`tr_M` at `z = q` **is** `χ_(3)`; at `z_D` it is
`α·χ_(3) + β·χ_(2,1)`, so `χ_(2,1)` follows by inversion). Calibrated: that
route reproduces `χ_(2,1)(Δ_S) = 0`, matching the direct covector computation.

| element | `b − 2a` | positive real roots | any with `q > 1`? |
|---|---|---|---|
| `Δ_S` | `(q−1)(q+1)(q²+1)/q²` | `1` | **no** |
| `Δ_L` | `(q−1)(q+1)(2q⁶+3q⁴+2q²−1)/(4q³)` | `0.5632`, `1` | **no** |

**Neither element is scalar modulo the radical at any `q > 1`.** Scope-(b), and
the invariant is cited: a polynomial with no root in the physical regime.

**And the `q = 1` root is degenerate, not a solution.** At `h = 0` the proton and
neutron words *coincide* — `σ₀(σ₁ − h/2) → σ₀σ₁ ← (σ₀ − h/2)(σ₁ − h)` — so
`Δ → 0` and the condition holds only as `0 = 0`. Both residuals carry the factor
`(q−1)(q+1) = q·h` for exactly that reason. Do **not** read the shared `h` factor
as "the condition is nearly satisfied": it is the statement that the whole
difference vanishes classically.

**What this does not say.** It excludes the two candidates, not the route: `b −
2a` is surjective over general elements, so there is no general obstruction. A
third element could satisfy the condition. What is now known is that neither
element the corpus currently has does, for any physical `q`.

### Closing enumeration, same day — the choice is a LINE, and it is surjective

`qbeta_admissible_line_exhausts_the_choice_probe.py` (12/12). The bean's
question is *"which functional evaluates Δ"*. The answer is that **the Q-value
cannot determine it**, because the candidates form a one-parameter family whose
value map is affine and onto.

Decomposing the Markov trace in the character basis of `H₃(q)` — derived here,
not assumed — gives

```
tr_M(z) = a(z)·χ_(3) + b(z)·χ_(2,1) + c(z)·χ_(1³)
c(z) numerator = q²·(z − q)·((q²+1)z − q³)
```

so the admissibility condition `N(q,z) = 0` of the 2026-08-29 audit **falls out
of the decomposition** rather than being posited, and `c(1) = q²(q−1)(q³−q²−1)/…
≠ 0` re-derives the `z = 1` inadmissibility of PR #6722 from a second route.

Normalising `φ(1) = 1` collapses the admissible trace space to the line
`φ_β = (1−2β)·χ_(3) + β·χ_(2,1)` — because `χ_(3)(1) = 1` and `χ_(2,1)(1) = 2`.
Both Markov points already lie on it: `z = q` at `β = 0`, `z_D` at
`β = q²/(q²+1)² ≈ 0.24730`.

On any element the value map is affine with slope exactly the scalar-mod-radical
residual:

```
φ_β(Δ) = χ_(3)(Δ) + β·( χ_(2,1)(Δ) − 2·χ_(3)(Δ) )
```

and that slope has **no root at any `q > 1`** (previous section), so the map is
**surjective**: solving `φ_β(Δ) = t` for a *symbolic* target `t` returns exactly
one `β`, on both elements.

| | `β` | `Δ_S` | `Δ_L` |
|---|---|---|---|
| `z = q` (augmentation) | `0` | **+12.470 %** | **+39.324 %** |
| `z = z_D` | `0.24730` | **−43.157 %** | **−15.451 %** |
| hits CODATA | — | `0.055437` | `0.177538` |

All four published grid cells are **reproduced from the character route**, which
is the calibration that makes the rest of the table trustworthy; and the
CODATA-hitting `β` is neither Markov point, on either element.

**So the four doors are now all enumerated:**

| door | what it costs | outcome |
|---|---|---|
| Markov **and** admissible | nothing — no free parameter | two points only: +12.470 % / −43.157 % |
| Markov, drop admissible | one parameter (`z`), fitted | `z = 1` exactly, and it is outside the TL quotient (#6722) |
| admissible, drop Markov | one parameter (`β`), fitted | reachable at `β* ≈ 0.0554`, with no independent characterisation |
| **neither choice matters** (functional-independence) | no parameter | impossible on both candidate elements at every `q > 1` |

**The consequence for the decision.** "Maybe some *other* admissible functional
works" is *true and empty* — one parameter fitted to one anchor has no
predictive content, and it is the same fit the published form already is, moved
from `z` to `β`. The only door that removes the parameter without an anchor is
functional-independence, and it is closed for the elements the corpus has. The
recommendation in
`docs/audits/2026-09-05-qbeta-functional-decision-options.md` (Option A — keep,
disclose, reclassify) is unchanged by this; what changes is that the option
space is now known to be exhausted rather than merely unexplored.

Nothing wired. No content block edited.

### 🟥 The 2026-09-05 anti-fitting directive eliminates `z = 1` — my Option A recommendation is WITHDRAWN

`AGENTS.md` gained **§NO FITTING, EXCEPT CAL-1/2/3** on `main` in `af1368d43ed`,
dated today, after the analysis above was written. It decides most of this bean,
against what I recommended.

Two of its clauses are directly on point:

> **Selection against the target.** Choosing an *object* — a knot from a census,
> a partition, a truncation order, **a branch** — because the choice reproduces
> the measured value. No continuous parameter is tuned and it is still a fit.

> **Accuracy is not evidence of correctness here, and a more accurate fitted
> route is worth LESS than a less accurate derived one.**

`z = 1` is precisely a **branch** of the Markov family, sitting outside the
admissible set (`c(1) = q²(q−1)(q³−q²−1)/… ≠ 0`, so it does not annihilate the
`(1³)` block the GNS/TL quotient kills), and its entire case is that it lands at
0.17 %. Under the directive that case is not merely weak — it is the fit
signature itself.

**So Option A (keep the published number, disclose, reclassify as pre-D
conditional) is withdrawn.** My argument for it was that the 0.17 % predates the
convention-D ruling by ~3.5 months and so was not fitted *when written*. That
does not survive the directive, which asks whether the number the paper
**publishes today** comes from a derived route — not whether its author was
fitting at the time. It does not.

**What survives is the two derived options**, and the directive explicitly
forbids choosing between them by accuracy:

| functional | `β` | Q_β | vs CODATA `0.7823334` MeV |
|---|---|---|---|
| `z = 1` (published) | *not on the admissible line* | `0.7836458` | **+0.168 %** — **eliminated** |
| `z = q`, the augmentation | `0` | `0.8798906` | **+12.470 %** |
| `z_D = q³/(q²+1)`, the convention-D Markov trace | `q²/(q²+1)²` | `0.4447004` | **−43.157 %** |

Choosing `z = q` over `z_D` *because* 12 % beats 43 % would be the same defect
one level down. The choice has to come from what `ε` **means** in
`Q_β = |ε(Δ)|·E₀`, and the corpus carries two functionals under that name — the
augmentation (an algebra map, `σ ↦ q`) and the coordinate sum
`net`/`epsNPq` — which is this bean's original question and is unchanged.

**Agent reading, marked as judgement, not a finding:** if `ε` is the *Markov
trace* in the canonical convention then the 2026-08-15 ruling names `z_D`, and
the answer is **−43.157 %**; if `ε` is the *augmentation* the answer is
**+12.470 %**. Nothing measured this session distinguishes them — the directive
removes one option, it does not pick between the remaining two.

**Not enacted.** Changing the published number touches ~8 content blocks and the
`AGENTS.md` canonical-chain cheat-sheet line (`Q_β … ≈ 0.784 MeV (0.17 %)`), and
which of the two derived values replaces it is the owner's call.


### Robustness: the `z = 1` inadmissibility is not a Skein-normalisation artifact (2026-09-05, PR #6832)

Bean `qou-8bxv` landed the same morning as #6722/#6763, measuring that **two Skein
normalisations are live** and are provably not bracket rescalings:

    (H)  L+ - L-           = (q - 1/q) L0            AGENTS.md §7a, STRICT
    (J)  q[L+] - q^-1[L-]  = (q^1/2 - q^-1/2) [L0]   8 live blocks, 5 chapters

**Both of this bean's merged results were computed in (H).** That made the shared
finding — the published `Q_β` form sits at `z = 1`, inadmissible under convention D —
a candidate convention artifact, which would have **dissolved** this bean's decision
rather than answered it. Tested; it does not.

**Transport.** Under (J) the generator has eigenvalues `u⁻¹, −u⁻³` with `u = √q`, so
`σ_J = u⁻²·σ̃(u)` — the (J) algebra is the (H) algebra in the square-root variable with
the *generator* rescaled. `ζ = u⁻²·z̃` carries convention D's roots to `ζ = u⁻¹`
(= 0.9491671528 at `q₀`) and `ζ = kernel(u) = u/(u²+1)` (= 0.4993203342).

**Result, both defensible readings of the element** (`Δ_S` is convention-laden — its
typed-crossing shift `d ∈ {−h/2, −h}` is a multiple of the bridge, so there is no unique
(J) counterpart):

| reading | outcome |
|---|---|
| element unchanged | `z = 1` inadmissible under (J) at **every `q > 1`**, no pin needed — *stronger* than (H), which excludes it only because `q₀` is not the supergolden root of `q³ = q²+1` |
| shift follows the bridge (`d → −s/2, −s`) | roots `−1.7411834668`, `+1.8455715251`; neither admissible |

No (J) admissible cell lands within 1 % of CODATA (closest `−5.518 %`). A **negative
control** (solver recovers an admissible parameter from a target synthesised at it) and a
**calibration** (reproduces the merged `+12.470 %` / `−43.157 %` to eight figures) make the
NONE mean something.

**Byproduct, and it is NOT new:** `z_C(q) = z_D(√q)/q` is the one-line composition of
`markovZC_eq_kernel_sqrt` and `markovZD_eq_sq_mul_kernel`, sorry-free on main in
`QOU/BraidKnot/MarkovConventionSeparation.lean`. The contribution is reading that module's
`q²` rescale as the (H)→(J) Skein normalisation — and it **supports** the convention-C
excision rather than softening it: `z_C(q) = kernel(√q)` is correctly normalised for the
algebra at `√q`, i.e. the *wrong specialisation point*, which is why `qou-cxjq` /
`qou-lp5d` / `qou-pmkh` are right that substitution cannot repair such sites.

Two arity gaps are machine-checked, not asserted:
`no_kernel_instantiation_is_conventionD` quantifies no rescaling factor, and
`no_rescaling_of_skein_weights` binds one constant on the **bracket** at fixed `q` while
this map rescales the **generator** and substitutes `q = u²`. Both theorems stand.

The symbol `z_J` is deliberately avoided — `qou-qlma` owns it for a different number
(`0.0274199478`), and `1/δ = 0.497290545` already sits 0.408 % from `ζ` (`qou-98g5`).

**This closes one way the decision could have been dissolved. It does not pick an option.**
The owner call is unchanged: `z = q` (`0.8798906` MeV, +12.470 %) or `z_D` (`0.4447004` MeV,
−43.157 %) against CODATA `0.7823334` MeV, decided by what `ε` *means* — not by residual,
which §NO FITTING's corollary forbids.


### Correction: the registry count is 13, not eight (2026-09-05, PR #6832)

The `qou-99qc` write-ups — PR #6832's body, its probe docstring, and this bean's
robustness section — cited **"eight `blocked_on_rederivation` rows of the
trace-convention registry"** as support for *a convention-C site is not
repairable by substituting `z_D`*.

**Measured:** `docs/coordination/trace-convention-registry.json` carries
`blocked_on_rederivation` as a **top-level array with 13 entries over 12 distinct
files** (`deltalambda_bareven_b4_magnitude_probe.py` appears twice). It is not a
per-row `status` value at all — a `status` histogram of that file returns
`agreed 4 / agreed-migration-pending 3 / disputed 1` and **zero**
`blocked_on_rederivation`, which is why a naive status-keyed count reads 0 and a
naive `grep -c` reads 4 (the key, a note, and two prose mentions).

**Not staleness — my error.** The array held **13 at this branch's own base
commit** as well as on current `main`, so 181 commits of drift did not make the
figure wrong. It came from a corpus-grep report and I relayed it without opening
the file. The registry did move in that window (+44/−15 lines) and the count did
not, so the coincidence that would have excused it does not exist either.

**Substance unaffected.** The registry states the claim in its own words:
*"Sites that must NOT stay on convention C but cannot be migrated by substituting
`z_D`, because the substitution changes the site's asserted RESULT rather than
its spelling."* Only the cardinality was wrong; the corrected text now quotes
that sentence instead of paraphrasing it.

**Contamination surface, all four checked:**

| carrier | state |
|---|---|
| probe docstring (`qbeta_skein_normalisation_admissibility_robustness_probe.py`) | fixed, producer re-run 13/13 |
| its witness `caveats` | fixed by the re-run |
| #6832 PR body | fixed |
| this bean | this entry |
| #6820 sibling comment | **no edit needed** — it makes the claim without a cardinality |

**Two different eights — do not sweep the token.** The same probe says the (J)
Skein normalisation is live in *"eight content blocks across five chapters"*
(lines 17 and 378). That eight is `qou-8bxv`'s and is **correct**. A
token-level fix would have broken a right number while repairing a wrong one —
the failure mode AGENTS.md names for figures that differ only in what they count.

No result changed: 13/13 before and after.

## 2026-09-07 16:45Z — the transport's rescale half is now a sibling's Lean, not my arithmetic

`492ad4221f6` (bean `qou-d0qq`) landed
`QOU.Mass.KZLevelFromHeckeNormalisation.ratio_invariant` on main — sorry-free,
generic field:

```lean
theorem ratio_invariant (c a b : K) (hc : c ≠ 0) (hb : b ≠ 0) : (c * a) / (c * b) = a / b
```

That is exactly the scalar-rescale half of #6832's transport
`σ_J = u⁻²·σ̃(u)`. Two checks added to
`qbeta_skein_normalisation_admissibility_robustness_probe.py` (now **15/15**,
was 13/13; every prior check unchanged and still passing):

- `H_and_J_generator_ratios_are_MINUS_q2_and_MINUS_q` — derived from each Skein
  relation directly, not asserted. In the **same variable `q`**: (H)
  `L₊ − L₋ = (q−q⁻¹)L₀` has eigenvalues `{q, −q⁻¹}`, ratio **`−q²`**; (J)
  `q[L₊] − q⁻¹[L₋] = (q^½−q^−½)[L₀]` has `{q^{−1/2}, −q^{−3/2}}`, ratio
  **`−q`**. The ratios differ, so the two normalisations are not rescalings of
  each other — the ratio-side restatement of this probe's separation premise
  (`qou-8bxv`).
- `the_u2_rescale_half_of_the_transport_is_INERT_on_the_ratio` — cites the Lean
  above rather than re-deriving it.

**What this buys:** the transport has two parts, a rescale and a
reparametrisation `q → u`. The rescale is now closed by someone else's Lean, so
the **reparametrisation is the whole content** of the (H)→(J) move.

## Same landing carries a scope over-claim — reported, not fixed by me

`KZLevelFromHeckeNormalisation.lean` says its `e^{iπħ} = q²` is *"stated so no
convention can move it"*. It guards the `ħ`-vs-`k` bookkeeping axis correctly,
but the ratio `−q²` is read off **(H)**, and feeding (J)'s ratio `−q` into the
same matching step `λ₁/λ₂ = −e^{iπħ}` gives `e^{iπħ} = q`, i.e. **`ħ` halves**
(`|ħ|` `0.066425366` → `0.033212683` at the proton pin) and `k+2` doubles.

Not a refutation: AGENTS.md §7a makes (H) STRICT, so their number is right under
the canonical reading. The defect is the scope sentence — the relation is
conditional on the Skein normalisation, and that is a live fork here
(`qou-8bxv`: 8 content blocks, 5 chapters). Reported on #7088, comment
5573521151; theirs to fix.

## `qou-37j2` / #7084 scopes my own `ε` recommendation

#7084 verified the merged `z = 1` inadmissibility at source (re-ran the probe,
15/15) and wired it into the L2 dashboard as `functional_admissibility_qbeta`.
Its framing adds a caveat I should carry: it names **Option E** — *keep an
admissible functional and find the element it should act on* — as the only one
of the seven options that could give a parameter-free admissible sub-1 % result.

My standing recommendation (`z_D`) chooses between the two admissible roots **for
the existing element `Δ = 𝓑_n − 𝓑_p`**. It should be stated with that scope:
*if the element stays `Δ`, then `z_D`*. If the element is the thing that moves,
the root question is downstream of a different choice and my recommendation does
not bind.


## 2026-09-08 — Option E has a SHARP acceptance test, and it is aimable

`computations/qbeta/qbeta_option_e_required_level_probe.py` (23/23), witness
`qbeta-option-e-required-level.witness.json`. Scope-(a). Wires nothing, selects
nothing, proposes no element.

THE REFRAME. On the H_3(q) normal-form basis the Markov trace is
`TR(z) = [1, z, z, z^2, z^2, z(hz+1)]`, so for a FIXED element `Delta` the
prediction is QUADRATIC in z. Requiring it to reproduce Q_beta therefore does
not leave a free choice -- it DETERMINES z. So "which element" and "which
functional" are not independent questions: each candidate Delta names the
functional it would need, and by the Wenzl relation that functional is a LEVEL
(r = 1 augmentation, r = 2 convention D; r = 1.1238831038 is why z = 1 fails).

MEASURED, on the corpus's own candidates (imported from
`qbeta_delta_candidate_census_probe`, not re-derived):

    candidate                  level 1      level 2     required r
    delta_S short NF           +12.470 %    -43.157 %     1.1257859
    nuc9 build_nucleon_nf      +13.083 %    -30.936 %     1.1343880
    nuc11 interleaved          +39.324 %    -17.496 %     1.4600767
    nuc11 gen-grouped          +39.324 %    -15.451 %     1.4912011
    16 constructed readings    +39.324 %       (varies)   1.1948 .. 1.2165

20 required levels; ZERO within 1e-3 of an admissible one; closest approach
0.126 away.

TWO RESULTS THAT WERE NOT WHAT I WENT LOOKING FOR.

1. LEVEL 1 IS BLIND TO BRAID ORDER. eps_aug is multiplicative, hence a product
   over letters, hence order-independent. Interleaved and gen-grouped carry the
   same typed-crossing multiset in a different order and agree to 20 digits at
   level 1 (-0.26038764179012080207) while differing in the third digit at
   level 2. All 16 assignment readings likewise share ONE augmentation. So an
   Option E element differing from an existing one only by ordering or by quark-
   generator assignment is, at level 1, the same number. To move the level-1
   value you must change the crossing MULTISET, not the braid.

2. THE BRACKETING IS UNIVERSAL, AND THAT IS THE OBSTRUCTION. On every candidate
   level 1 overshoots Q_beta and level 2 undershoots it, so by IVT the required
   level lies strictly BETWEEN the two admissible ones -- which is exactly why
   it is never one of them. This makes Option E's acceptance test aimable:

       AN ELEMENT THAT CLOSES OPTION E MUST HAVE ITS LEVEL-1 AND LEVEL-2 VALUES
       ON THE SAME SIDE OF Q_beta.

   A candidate that brackets is rejectable without solving anything.

DELIBERATELY NOT A SEARCH. Enumerating elements until one lands on r = 1 or 2
would be selection against the target, i.e. a fit under AGENTS.md NO FITTING.
The 16-variant family is reported as a RANGE for that reason; its best-landing
member is not a result.

A CALIBRATION DEFECT FOUND EN ROUTE, already flagged by the census but worth
stating in one line: the census's \`net\` is the COORDINATE SUM, and it differs
from tr^{z=1} by exactly h*(e^- coordinate) -- proved symbolically here, before
any pin. Only the gen-grouped model has e^- = 0, so the corpus's "coordinate sum
= tr at z=1" identification holds on that model alone.

THE OWNER CALL IS UNCHANGED. This narrows Option E; it does not decide which
functional eps is. That is still yours, and still the question of whether D7's
scoping of convention D to the decay channel reaches the choice of functional
WITHIN that channel or only the convention its objects are expressed in.

## 2026-09-08 — OWNER DECISION (chat, AskUserQuestion on PR #7159 session): the AUGMENTATION.
Option presented and selected: *'1. Decide ε in Q_β (qou-99qc) — Augmentation σ↦q (+12.47 %), z_D trace (−43.16 %), or retract Q_β; I recommend the augmentation.'* The owner selected it (together with three other items). Recorded reading: ε(Δ) := the augmentation σ ↦ q (option B of 2026-09-05-qbeta-functional-decision-options.md §3), i.e. Q_β base = 0.8798906 MeV, +12.470 %. Note the selection endorsed an option that carried the agent's recommendation; if the owner intended only 'decide it', this line is the place to overrule.
Consequences: (i) the published 0.17 % closed form is retired as the base — cite it only as the C-frame / z=1 historical cross-check; (ii) qou-cds1's ladder re-derivation now has its base (the augmentation), so S1 can start on the phase question (qou-pdix); (iii) dashboard rows Q_β / m_n / Δ_pn are to be re-scored on the augmentation base and stamped ADMISSIBLE-AUGMENTATION — NOT done in this session (witness sweep needs the producer under D; ask-before-change); (iv) AGENTS.md scoping note updated to record the ruling. Status stays todo until (iii) lands.

## 2026-09-08 (later) — the selection above is IN TENSION with D7, per 13bb8243d8 on main (qbeta_augmentation_is_a_markov_trace_probe.py): the augmentation IS the Markov trace at z = q, so 'which functional' = 'which Markov parameter', and D7 (convention D governs the decay channel; D = two-row truncation) selects z_D (−43.157 %), the augmentation being the one-row truncation (y_(2,1) = 0) and not D. The owner selected the augmentation on an option written before that commit was known. Owner confirmation requested in chat; neither base wired until it arrives. Default if nothing: the record stands as 'augmentation selected, D7-tension flagged', and no witness moves.

## 2026-09-08 (final) — OWNER RULING: ε := the Markov trace at z_D = q³/(q²+1) (option C), following D7. Put to the owner with both options framed after 13bb8243d8; answer: 'A. z_D — follow D7'. Base 0.4447004 MeV, −43.157 % vs CODATA — a documented honest miss on the canonical base, not a fit. The augmentation (+12.470 %) is the other admissible point, proportional (α=(q⁴+1)/(q²+1)²). Consequences: (i) published 0.17 % retired as base (z=1 cell), historical C-frame cross-check only; (ii) qou-cds1's ladder base is z_D; S1 reduces to the phase (qou-pdix); (iii) dashboard rows Q_β / m_n / Δ_pn to be re-scored on z_D and stamped ADMISSIBLE-zD — NOT done this session (producer under D; ask-before-change); (iv) AGENTS.md scoping note, precision-goals.md, cheat-sheet row 11 and the 2026-09-08 audit §8 all record this. Status stays todo until (iii) lands.


## 2026-09-12 — what the ruling re-weights in the Lean layer (PR #7188)

The ruling is recorded above; this does not restate it. What it adds is the
effect on the acceptance-test side, which is not a restatement.

**1. The canonical eps is the NON-multiplicative one, so braid ORDER is now a
live degree of freedom for the observable.** Sorry-free in #7188:

    multiplicative_forces_eigenvalue   a unital multiplicative functional sends
                                       the Hecke generator to z, and s^2 = hs+1
                                       forces z^2 = hz + 1, so z is one of the
                                       TWO eigenvalues q, -1/q.
    zD_lt_self, zD_pos                 z_D = q^3/(q^2+1) is strictly below q and
                                       strictly positive, hence above -1/q.
    conventionD_not_multiplicative     therefore z_D is neither eigenvalue.

The corpus had only the z -> 1 instance (QOU.QBeta.CounitSigmaOne); this is the
general statement it is a case of.

SCOPE: this REMOVES THE OBSTRUCTION, it does not prove order-sensitivity.
Non-multiplicativity permits a functional to see order; it does not force it.
That level 2 actually separates two same-multiset words stays a measurement
(#7176), not a corollary.

**2. Level-1 order-blindness is now a statement about a NON-canonical
functional — and that is its value.** monoidHom_order_blind and its difference
form explain why the augmentation route looked deceptively insensitive to
modelling choices: all sixteen readings of the properties blocks' recipe share
ONE level-1 number. So agreement there was never evidence about the element.
Under the ruling that insensitivity is gone.

**3. The Option E target is now ONE-SIDED, and aimable.** With eps pinned there
is no second admissible endpoint to run to. Every candidate the corpus has built
UNDERSHOOTS at level 2, so a closing element needs a strictly LARGER |tr_{z_D}|:

    nuc11 gen-grouped   -15.4514 %   x 1.182752
    nuc11 interleaved   -17.4959 %   x 1.212061
    nuc9                -30.9364 %   x 1.447941
    Delta_S             -43.1572 %   x 1.759237

Read from the committed witness on main (qbeta-option-e-required-level), not
from memory. Arithmetic on measured residuals, NOT theorems, and deliberately
not dressed as theorems in the Lean.

**Status stays todo**, for two reasons and not one: (iii) the dashboard
re-score is still outstanding, AND the element half of this bean is open. Per
§13a a bean whose subject includes an open question does not close because one
half of it was answered.


## 2026-09-12 — the ORDER lever, measured exhaustively: WIDE BUT COARSE

`computations/qbeta/qbeta_option_e_order_dof_range_probe.py` (8/8), witness
`qbeta-option-e-order-dof-range`. Scope-(a). Names no ordering.

WHY THE QUESTION EXISTS AT ALL, AND ONLY SINCE THE RULING. Level 2 is not
multiplicative (proved, #7188), so unlike the augmentation it CAN see the order
of the letters in a braid word. Braid order became a live degree of freedom for
the observable on the day of the z_D ruling. Under the augmentation it was
provably invisible, so it never needed deriving.

MEASURED, exhaustively over both nucleon multisets — 6930 neutron orderings and
9240 proton, 64,033,200 pairs (tr is linear on the NF vector, so the words
enumerate separately rather than as pairs):

    tr_{z_D}(Delta) reachable   [-0.7795980, +0.5476330]   span 1.3272311
    target                      +-0.1868937
    span / target               7.1015x
    pairs within 1 sigma (780 ppb)              0  of 64,033,200
    NEAREST approach                2.7232758e-5  = 0.014571 % of target
                                                  = 186.88x the window
    the canonical gen-grouped neutron ordering ranks 6667 of 6930

🛑 I WAS WRONG TWICE AND BOTH GUESSES ARE RECORDED BECAUSE THE SHAPE MATTERS.
First I wrote the probe to show order was TOO SMALL a lever, on the strength of
the single order pair the corpus had measured (interleaved -17.496 % vs
gen-grouped -15.451 %, a 2.04-point move). Wrong by two orders of magnitude —
the span is 7.1x the target. Then I expected it to be so free as to be
UNFALSIFIABLE. Also wrong: zero of 64 million pairs land in the window.

THE ACTUAL SHAPE IS WIDE BUT COARSE, and that is the good outcome: reordering
CANNOT manufacture agreement with Q_beta, so an ordering claim here would be
falsifiable rather than fitted.

🛑 LIVE FIT HAZARD, and it is the sharpest thing in this entry. "Order cannot
manufacture agreement" is true against the EXPERIMENTAL WINDOW and badly
misleading as a summary: some ordering reaches 0.0146 % of the target against
the canonical ordering's -15.45 %. Anyone exhibiting it would be quoting a
result an order of magnitude better than the retired published 0.17 %, and it
would be PURE SELECTION — no continuous parameter tuned, an object chosen
because it reproduces the measured value, exactly what NO FITTING names. What
makes it refutable rather than unfalsifiable is only that it misses the window
by 187x. The probe deliberately does not name it, and neither does this bean.

CONSEQUENCE FOR OPTION E. Order is priced and it is not the lever: it cannot
reach Q_beta from these multisets. The freedom is in the MULTISET, which is
where augmentation_difference_order_blind already said it had to be — changing
the multiset is the only thing that moves level 1, and it moves level 2 too.

SCOPE: measured on THESE two multisets. It prices the order lever; it does not
exclude Option E.


## 2026-09-12 — item (iii) is PRICED. It degrades three rows by ~5–7 orders, and that is the ruling working as designed.

Consequence (iii) of the 2026-09-08 ruling — re-score the L2 dashboard rows
`Q_β` / `m_n` / `Δ_pn` on the ruled base — has been declined twice as
ask-before-change, which is correct: it moves the L2 headline, so it is neither
a precision increase nor corpus-derived. But it was declined **without the
numbers**, i.e. the owner was being asked to authorise a change whose size
nobody had measured. Measured now, changing nothing:
[`qbeta_zd_rescore_price_probe.py`](computations/qbeta/qbeta_zd_rescore_price_probe.py)
(6/6), witness `qbeta-zd-rescore-price.witness.json`.

**Calibration first, because the numbers are worthless without it.** The probe
reproduces the dashboard's CURRENT `m_n` and `Δ_pn` rows from its CURRENT
`Q_β` row through the producer's own relation
`m_n = m_p(substrate) + Q_β + m_e`: predicted 0.895408 / 650.486 ppb against
the committed 0.9029 / 658.0 ppb — **ratios 0.9917 / 0.9886**. So the dependent
rows ARE a plain function of the scored `Q_β`, and the re-score below is the
row, not a sketch.

| cell | `Q_β` ppb | `m_n` ppb | `Δ_pn` ppb |
|---|---|---|---|
| `z = 1` (published, **inadmissible**) | 1 678 440.4 | 1 397.3915 | 1 015 161.0 |
| **`z_D` (RULED)** | **4.3157176e+8** | **359 350.35** | **2.6105673e+8** |
| `z = q` (augmentation) | 1.2470029e+8 | 103 832.09 | 75 430 750.0 |

**The ruled cell is the worse admissible one — 3.4609× farther from CODATA than
the augmentation.** That is not an argument against the ruling; it is the
anti-fit directive visible in the numbers. Ranking these cells by residual is
exactly the selection-against-the-target the directive forbids, and the ruling
turned on what `ε` *means* under D7, not on which column is smaller.

**🛑 THE LOAD-BEARING CAVEAT: these are BASE figures, zero `c_k` rungs.** No
ladder exists on an admissible base (`qou-cds1`, blocked on the phase
`qou-pdix`). On the `z = 1` base the five rungs bought 1 677 569 → 37.7 ppb —
about 4.5 orders — so a `z_D` ladder could move these a long way. **Do not
quote the `z_D` column as "convention D's accuracy"**; that is the same
mislabelling this bean already had to retract once.

**Producer staleness found, reported not fixed.**
[`per_observable_100x_status.py`](computations/per_observable_100x_status.py)
still says *"Which functional to adopt is an open owner decision (bean
qou-99qc)"* — ruled four days ago — and its emitted
`best_admissible_err_pct` names **`z=q (augmentation)`** as the best admissible
cell. The second is the sharper one: a reader of that witness field takes the
augmentation for the adopted functional, and the ruling chose `z_D`. Both are
one edit away, and both change an emitted witness field, so they go to the
owner with (iii) rather than under exemption 2.

**Correction to my own earlier count in this bean's arc:** I reported this probe
as "8/8 checks". The total was a hardcoded `5 + 3`; there are **six**
`check()` calls. It is now derived from the recorded list, and the six verdicts
are carried in the witness as assertions (it previously emitted **0
assertions** for a probe whose entire content is checks).

**Status stays `todo`** per §13a — the element half (Option E / the phase
`qou-pdix`) is an open question, and (iii) is now waiting on the owner rather
than on a measurement.


## 2026-09-12 (same day, later) — item (iii) is DONE. The owner authorised the re-score; the three rows are on the ruled z_D base.

Put to the owner with the prices above. Answer: **both** "re-score now to z_D"
**and** "re-score after qou-pdix" — read as *move now, and move again once a
ladder exists*. First half landed (PR #7221, `606e7e304b1`); second half is bean
**`qou-iagg`**, blocked on `qou-pdix` → `qou-cds1`.

| row | before (`z = 1`, laddered) | after (`z_D` base) | miss factor |
|---|---|---|---|
| `Q_β` | 1279 ppb | **4.316e+8 ppb** | 5.535e+7 |
| `m_n` | 0.9029 ppb | **3.594e+5 ppb** | 7.034e+7 |
| `Δ_pn` | 658.0 ppb | **2.611e+8 ppb** | 6.021e+7 |

Landed figures match the prices to <1e-3 relative; the probe's new CHECK 6
asserts it against the live witness, so a future drift is caught rather than
assumed. **The L2 headline is unchanged at 1/6 scoreable** — all three already
failed, so this degrades three misses without moving the count.

**Derived from q₀, not inverted from CODATA.** `_qbeta_ruled_base()` evaluates
`|tr_M(Δ_S)(z_D)|·E₀` with `tr_M(Δ_S)(z) = q²/2 − qz − 1 + z/q + 1/(2q²)` and
`E₀ = m_e/(q(q−1))`, then calibrates against this bean's own probe witness
(`−43.157175 %`, agreement 2.9e-7). Reading that recorded residual and
inverting it would have been arithmetically exact and circular — the row's
residual would have been a pass-through of a number computed against CODATA.
If the calibration fails, the producer publishes the **old** row and says so.

**Question 2 answered too: fix both, renaming the field.**
`best_admissible_err_pct` → **`ruled_cell_err_pct`**, repointed from the
augmentation to `z_D`, and the "open owner decision" prose is gone from the
producer (0 occurrences). The rename was the owner's pick for a reason worth
recording: the old name carried *two* defects, not one — it named a functional
the ruling did not choose, **and** "best" ranked the admissible cells **by
residual**, which is the selection-against-the-target the anti-fit directive
forbids. Both cells stay visible in `err_pct_by_functional`.

**🛑 Still a base, zero rungs.** Every affected row now carries that scope in
its own `note` rather than cross-referenced from the `Q_β` row — the
"fixed in one place, survives in the others" failure this corpus keeps
recording. Do not quote these as convention D's accuracy.

**Correction to my own verification claim, and it reached the PR body.** I
reported the first `precision-gates.sh --changed` run as **exit 0**. It was
not: that run was piped through `tail`, so the 0 was `tail`'s status. Re-run
un-piped it is **exit 1** — but the reds are pre-existing, not mine: the `RED:`
line is byte-identical before and after the producer change, both ratchets
report `NEW dirty 0 / REGRESSED 0`, none of the gate's NEW items names either
of my files, and `main` is independently recorded red on the ratchet (#7161
open). PR body corrected.

**Status stays `todo`** per §13a — the element half (Option E) and the phase
(`qou-pdix`) are open questions. What has closed is item (iii).


## 2026-09-12 — 🛑 CORRECTION to my own re-score entry above, plus the anatomy of the 257x and three undone migrations

**The entry above quoted "1279 ppb → 4.316e+8 ppb" as the re-score's effect. That
comparison is the one the corpus forbids, and I made it.** 1279 ppb is
**post-ladder** on `z = 1`; 4.316e+8 ppb is a **base**. The apparent 337,429× is
two factors:

| factor | what it is |
|---|---|
| **1312×** | the **missing `c_k` ladder** (`z=1` base 1 678 440 ppb → `z=1` published 1279 ppb) |
| **257×** | the **functional** (`z=1` base → `z_D` base) |

So **most of the degradation is "no ladder yet"** (`qou-cds1` / `qou-pdix`), not
convention D. **Base to base, D costs 257×. Never quote the 337,429×.**

**Why the gap is structural, not a botched substitution.** `tr^z(Δ_S)` rewrites
exactly as `h²/2 − z·h` with `h = q − 1/q` (verified to 1e-60 against the
2026-08-29 affine form). The `z` term dominates by **5.86×**, so `Q_β` is nearly
*proportional* to `z`. Inverting for CODATA gives **`z* = 0.99850`** — **0.15 %
from the inadmissible `z = 1`**, while `z = q` is +11.17 % and `z_D` is −38.64 %
away. **The published 0.168 % was reachable only at `z ≈ 1`, the coordinate sum.**
It was a property of an inadmissible functional, not of the framework. Scope-(a):
this excludes `Δ_S` *paired with an admissible functional*, not convention D.

**The missing-normalisation hypothesis is REFUTED** — `Σ_λ y_λ f^λ = 1.0` exactly
under D at n = 3, 6, 9, 12 (worst |·−1| < 1e-50). It is the first thing a next
agent will reach for; do not spend a session on it.

**Three migrations the ruling did not get** — new beans, all directions recorded:

- **`qou-wfvl` (high)** — the **element** is census-derived (`Δ_S`, short NF) while
  the owner's γγ ruling the same day forbids census selection. The γγ-selected
  nucleon word gives **−17.496 %**, 2.5× closer *and* derived (PR #7212).
  **Owner decision; subsumes the accuracy question.**
- **`qou-46ys` (high)** — the **binding/mass channel is still convention C**, by
  its own source comments (`gap_a3_overshoot_robustness_check.py:52-67`). And it
  is the most exposed channel: `z` *is* the `y_λ`, binding is the same Frobenius
  pairing, and D's two-row truncation keeps **7 of 77 blocks at A=4** (0.043 % of
  the dimension). Nobody owned this.
- **`qou-y3bm`** — `E₀` had two live forms (+0.9915 %); **unified 2026-09-12 on
  owner instruction** in `qbeta_e0.py`, tower-summed canonical. The tower
  **series** is assumed, not derived — canonical by ruling, open by proof.

Probe: `qbeta_zd_gap_anatomy_probe.py` (9/9). Audit:
`docs/audits/2026-09-12-zd-gap-anatomy-and-three-undone-migrations.md`.
**Status stays `todo`** (§13a).
## 2026-09-12 — BOTH routes to Delta are now priced, and both are negative

PR #7212. The owner's word-selection ruling (2026-09-08, qou-ales) applied to
the DECAY channel for the first time — #7192 applied it to mass/binding.

PROVED (sorry-free, QOU/QBeta/GammaGammaSelectedDeltaVanishes.lean, lean-direct
exit 0 first attempt): a functional multiplicative over concatenation and equal
to 1 on a pair-production vertex is 1 on EVERY γγ-word, hence annihilates every
γγ DIFFERENCE. Both one-dimensional blocks of H_3 are of that shape. Therefore:

  * LEVEL 1 gives EXACTLY ZERO — the augmentation's support is the (3) block
    alone, so a γγ-selected Delta predicts Q_beta = 0 identically, for every
    pair of words, with no computation to do.
  * LEVEL 2, the ruled functional, is carried ENTIRELY by the (2,1) block, which
    is what makes the scan one-dimensional and finite.

MEASURED (5/5), V^k with k <= 5 from the 11-crossing budget, 36 pairs:

  level 1, max over all 36 pairs   1.34e-51        (the proof, confirmed)
  reachable below target           7 values, all <= 0.0985019929
  reachable above target           8 values, all >= 0.6841593612
  the GAP                          0.5856573683 = 3.13364x the target
  Q_beta target                    0.1868936677    -- INSIDE the gap
  nearest reachable                47.295168 % away

The γγ sector does not merely miss; it CANNOT COME CLOSE. Structural.

THE TWO ROUTES, SIDE BY SIDE:

  re-read the existing recipe (#7188)   0 of 37,459,422,000 configurations
  the ruled γγ selection (#7212)        target in a 3.13x gap, nearest 47.3 %

Neither reaches Q_beta. The live conclusion is that Delta needs the FLAVOUR
LETTERS: γγ-words carry no flavour index at all (the corpus's Crossing is
(gen, pos) and nothing else), so a flavour-blind principle cannot distinguish a
proton word from a neutron word. That is the open point GammaGammaSelectorH3
names for itself.

SCOPE-(a) on both: #7188 prices the freedom the SOURCE BLOCKS declare; #7212
prices the ruled principle APPLIED ALONE. Neither refutes the ruling, and an
element combining γγ selection WITH flavour letters is outside both.

Bean stays todo. The element question is SHARPER, not closed — two routes
priced, both negative, and what is missing is now named.



## 2026-09-12 CORRECTION — 'Delta differs in one letter' was WRONG; it retypes TWO

PR #7212, commit c2b8c7e8c0. This retracts a claim I made the same day, which
reached that PR's TITLE, its BODY, a Lean docstring and a comment on the PR.

THE CLAIM: the nucleon words 'differ in exactly one letter: a single sigma
becomes a single sigma^-1'. Wrong at the LETTER level. The corpus's own data,
_GEN_CHAINS in qbeta_delta_candidate_census_probe.py:

  p : gen0 [0,0,0,   0,-1/2,0,0]   gen1 [-1,-1,-1,-1/2]
  n : gen0 [0,0,0,-1/2,-1/2,0,0]   gen1 [-1,-1,-1,  -1]

TWO slots differ, gen0[3] and gen1[3], each by exactly -1/2.

WHAT WAS AND WAS NOT WRONG. The COUNTS are correct and unchanged: proton
(1,2,0), neutron (0,2,1), and the Lean theorem about them stands. The READING
was wrong. Beta-decay flips ONE quark, and each quark sits in TWO of a
nucleon's three pair-crossings, so one uu becomes ud and one ud becomes dd:

  (u1,u2)  uu -> ud     retyped
  (u2,d3)  ud -> dd     retyped
  (u1,d3)  ud -> ud     untouched

The preserved ud count is a CANCELLATION -- one gained against one lost -- not
evidence the mixed crossings are untouched. (1,2,0) -> (0,2,1) is consistent
with a single uu |-> dd substitution AND with the flip that actually happens,
and only the second is a possible decay. I read the weaker hypothesis off the
counts without checking it against the chains. The misleading theorem name
nucleon_difference_is_one_letter is renamed
nucleon_pairCounts_differ_by_one_uu_and_one_dd; the statement is unchanged.

WHAT THE CORRECTION BOUGHT, which is worth more than the retraction cost. Both
retyped letters pick up the SAME central scalar s = -h/2, so Delta expands
EXACTLY:

  Delta = s*(S_A + S_B) + s^2*S_AB

with S_A, S_B the proton word with ONE flavour crossing SMOOTHED (10 crossings)
and S_AB with BOTH (9). Measured, 60 dps, proton pin, convention D:

  direct tr(Delta) vs expansion     agree to 7.8e-62
  s = -h/2                          -0.1045301493978196577
  tr(S_A) / tr(S_B) / tr(S_AB)      1.271097000 / 0.272140496 / 0.301910575
  s^2 term / s term                 2.045 %
  crossings                         11 -> 10 -> 9
  residual                          -15.451387 %  -- UNCHANGED

THE OLD READING IS REFUTED NUMERICALLY, not merely withdrawn: under it Delta
would be -h times ONE smoothed word, and both candidates sit 68.2 % and 64.0 %
from Delta. CHECK 4 of the probe.

ALSO: the typing table is ONE scalar, not three conventions. sigma - h =
sigma^-1 follows straight from the Hecke relation (skein_letter_inv), so the dd
letter IS the inverse crossing and the ud letter is exactly (sigma+sigma^-1)/2
(ud_letter_is_average). Both sorry-free.

LEAN, all sorry-free, lean-direct -DautoImplicit=false -s 65536 exit 0:
  flip_retypes_pairs                general form, any (m+1 ups, n downs)
  nucleon_flip_retypes_two_of_three the proton case: 2 of 3
  two_shift_expansion               the element identity, over a NONCOMMUTATIVE
                                    ring with centrality of s explicit -- a
                                    CommRing proof would be unsound for the
                                    braid algebra
  skein_letter_inv                  needs only the Hecke relation
  ud_letter_is_average              needs (2:R) != 0, stated explicitly
  succChooseTwo                     C(m+1,2) = C(m,2) + m
#print axioms: no sorryAx anywhere; two_shift_expansion needs only [propext].

WHAT DOES NOT MOVE. No number: this is an exact rewriting of the same element,
so the residual and everything downstream are identical. The 3.13x gap result
of #7212 Part 1 is untouched -- it prices the whole reachable set and never
used the letter count.

WHAT IT CHANGES FOR THIS BEAN. Delta's FORM inside this construction is now
known exactly: a fixed rational combination of 10- and 9-crossing traces rather
than an opaque 11-crossing difference, and |s| ~ 0.1045 is the quantitative
reason the two nucleon traces sit so close together. Whether those lower-
crossing words are more tractable, or coincide with words the mass channel
already computes, is NOT claimed and is the live question.

BEAN STAYS todo. The epsilon/Delta fork is an open conjecture; per AGENTS.md
13a a bean whose subject is an open conjecture is not closed because the
recording of its openness is done.

SCOPE-(a): two_shift_expansion holds for ANY two slots carrying a common
central shift; that the nucleon words are in that shape is read off _GEN_CHAINS
and re-verified numerically, not proved.



## 2026-09-12 DERIVATION — the gg ruling DECIDES the braid ordering, and picks the WORSE one

PR #7212, commit 3a76d49fc9. This CLOSES the ordering question #7188 raised.

WHAT #7188 LEFT OPEN, in its own words: "the corpus now owes a DERIVATION of
the braid ordering of the nucleon word. Until it has one, tr_{z_D}(Delta) is
not predicted by the framework -- it is selected by an unstated modelling
choice." The owner's gamma-gamma ruling (2026-09-08, qou-ales) supplies it.

THE ARGUMENT, STRUCTURAL NOT NUMERICAL. The census carries two orderings of the
SAME eleven-letter multiset (verified: identical Counter for both nucleons).
Their confinement cores are:

  interleaved  nuc9:        for _ in range(3): sigma_0 ; (sigma_1 - h)
  gen-grouped  _GEN_CHAINS: all sigma_0 letters first, then all sigma_1

sigma_1 - h = sigma_1^-1 by the Hecke relation (skein_letter_inv, proved on
this branch), so the interleaved core is (sigma_0 sigma_1^-1)^3 = `vertex 0`
three times -- a GAMMA-GAMMA WORD. The gen-grouped core has a POSITIVE crossing
in SECOND position, and a gg-word's second letter is always negative. So of the
two models exactly one is gg-produced and the ruling selects it. Scope-(b): it
cites a proved invariant, not a bad number.

LEAN, all five depend on NO AXIOMS AT ALL (lean-direct exit 0):
  gammaGamma_snd_neg             a gg-word's second letter is negative
  not_gammaGamma_of_snd_pos      hence a positive 2nd letter excludes it
  interleavedCore_isGammaGamma   three applications of the constructor
  not_gammaGamma_genGroupedCore  the exclusion
  cores_ne                       the two cores are different words

The linter earned its keep: the exclusion lemma was first stated with BOTH of
the first two letters positive as hypotheses and the first is never used, so it
was restated STRONGER (the first letter's sign is irrelevant) and renamed.

🛑 THE RULED ORDER IS THE LESS ACCURATE ONE, and that is the correct outcome.
Proton pin, convention D, 60 dps:

  interleaved (RULED)   -17.495929 %      <- reproduces #7188's documented -17.496
  gen-grouped (unruled) -15.451387 %      <- the merged Option-E witness
  cost of the ruling      2.04454 points

Under AGENTS.md NO FITTING, "rank by derivational cleanliness first, treat
accuracy as a diagnostic, never as a tie-breaker that promotes a fitted route."
Preferring -15.45 % BECAUSE it is closer is selection against the target. Do
not revert this.

CONSEQUENCE FOR THIS BEAN. The -15.4514 % that #7188 and #7212 calibrate
against is the GEN-GROUPED, i.e. UNRULED, order. Nothing there is retracted --
both state their ordering -- but the CANONICAL residual under the ruling is
-17.4959 %, and the witness qbeta-gamma-gamma-ruling-selects-ordering is the
record of which figure is which.

WHAT SURVIVES THE ORDER CHANGE, checked rather than assumed:
  * the two-letter flip is ORDER-INDEPENDENT: two slots, each -h/2, in both
    orderings (expected for a flavour statement, but measured);
  * the three-term skein expansion is EXACT on the ruled order too, 3.9e-62 at
    60 dps -- only the term sizes move, s^2/s going 2.045 % -> 4.874 %;
  * the 3.13x gap of #7212 Part 1 is UNTOUCHED: it prices V^k differences, a
    gg-only construction carrying no nucleon ordering at all.

CROSS-CHECK WORTH NOTING, two independent routes to the same k. The sibling's
Frobenius-positivity selection (owner ruling 2026-09-12, reading 3) picks
k = 3 = beta_Bor on #7207. The census's confinement core is independently V^3.
Same k, from two different principles -- recorded as a coincidence of two
derivations, NOT offered as evidence for either.

🛑 TRAP, recorded in the probe. "Interleaved" reconstructed by ZIPPING the two
_GEN_CHAINS lists alternately gives -13.5712 %, which is NEITHER census model
-- a third ordering, invented, and plausible-looking. I produced it before
reading nuc9. The census's interleaved model emits the core as three
(sigma_0, sigma_1^-1) PAIRS, then an ORDERED quark block, then two gluon
letters. Reproducing the documented -17.496 % is the calibration that catches a
lookalike reconstruction; CHECK 3 asserts it.

BEAN STAYS todo. The epsilon/Delta fork is an open conjecture (§13a). What is
closed is the ORDERING sub-question, which is a genuine narrowing: the order is
no longer a free modelling choice. The residual did not improve and was not
expected to.

STILL OPEN: the ruling constrains the CORE. The flavour letters are determined
(this branch) but their PLACEMENT, and the two gluon letters, are not gg-words
and are not settled by the ruling. That is the remaining freedom.



## 2026-09-12 PARITY BOUND — the ruling reaches 6 of 11 letters, provably

PR #7212, commit 49bae3625e. Companion to the ordering derivation above: that
one settles the CORE, this settles how much the gg principle can settle AT ALL.

Every pair-production vertex contributes exactly TWO letters, so a gg-word has
EVEN length. The nucleon crossing budget is 11 (qou-1qsw), which is ODD.
Therefore NO 11-crossing word is gg-produced -- not this one, not any
reordering of it, not any other candidate at that budget. At least one letter
necessarily lies outside the principle's reach, and that is a fact about the
budget, not a shortfall in the construction.

Block decomposition of the census word:

  core (sigma_0 sigma_1^-1)^3    6 letters   gg-produced (constructor x3)
  quark                          3 letters   NOT -- odd length
  gluon sigma_0 sigma_0          2 letters   NOT -- 2nd letter positive
                                ----
                                11 = the budget

So the ruling reaches 6 of 11; the other 5 are the freedom that survives it.
The gluon pair is excluded twice over -- directly by the vertex sign pattern,
and by following an odd-length block.

LEAN (lean-direct exit 0, no sorryAx):
  gammaGamma_length_even        2 | w.length for any gg-word
  not_gammaGamma_of_odd_length  the contrapositive
  eleven_not_gammaGamma         no 11-crossing word is gg-produced
  gluonPair_not_gammaGamma      NO AXIOMS AT ALL
  three_not_gammaGamma          the quark block's length is odd

Scope-(b) throughout: every exclusion cites a proved invariant (vertex length,
or the vertex sign pattern), never a measured miss.

🛑 THIS IS A LIMIT ON THE RULING, NOT A DEFECT IN IT, and not the construction
failing to apply it. The principle does what it can; what it cannot do is fix
an odd number of letters out of even-length building blocks.

WHY IT MATTERS FOR THIS BEAN. It converts "the flavour placement and gluon
letters are still open" from an observation into a THEOREM about where the
remaining freedom lives: exactly 5 letters, and no amount of gg reasoning will
reduce that number. Any closing Delta has to come from those 5 or from a
different principle. That is a much sharper statement of the open problem than
the bean carried before.

Probe 12/12 (CHECK 6 added to qbeta_gamma_gamma_ruling_selects_ordering_probe).

BEAN STAYS todo (§13a).



## 2026-09-12 — the SDP half applied, and the scope question ANSWERED (A, core only)

PR #7212, commit 426af792b8 + follow-up. The gamma-gamma half was applied above
(ordering 3a76d49fc9, parity bound 49bae3625e). This is the SDP half.

METHOD, needing no new machinery. chi_(3) is the 1-dim character sigma -> q, so
a letter (sigma_g + dc*h) has value q + dc*h and chi_(3)(w) = prod(q + dc_i*h)
-- multiplicative and GENERATOR-INDEPENDENT. From
tr_{z_D} = y_(3) chi_(3) + y_(2,1) chi_(2,1) at level 2 (y_(1^3) = 0),
chi_(2,1) = (tr - y_(3) chi_(3)) / y_(2,1). Calibrated three ways before use:
chi_(2,1)(1) = 2 exactly (block dimension), chi_(3)(V^k) = 1 exactly for all k
(reproducing the sorry-free unit_on_vertices_eq_one from the OPPOSITE
direction), y_(3) + 2 y_(2,1) = 1.

RESULT 1 -- the (3) block is STRUCTURALLY SILENT. chi_(3) depends only on the
shift multiset, and flavour determines the shifts (pairCounts_determined), so
it is one positive number per nucleon (1.3825 p / 1.1221 n) across all 32
generator assignments, spread exactly 0. The whole content of reading 3 here is
chi_(2,1) >= 0.

RESULT 2 -- it NARROWS AND DOES NOT CLOSE. 20/32 proton and 16/32 neutron
assignments survive: 320 admissible Delta pairs of 1024, a 3.2x narrowing. The
target (0 %) is INSIDE the admissible range [-98.57 %, +35.17 %], and the
nearest admissible pair misses the ~780 ppb window by 122573x. Falsifiable and
currently failing -- the same shape as #7188's ordering result, NOT a rescue.

RESULT 3 -- THE SCOPE FORK, now answered. Reading 3 applied to the gg-selected
CORE admits V^3 (chi_(2,1) = +1.9942) and selects k = 3 = beta_Bor. Applied to
the WHOLE 11-crossing word it EXCLUDES the census assignment (chi_(2,1) =
-0.2806 proton, -0.3720 neutron) -- which would make every residual on this
bean inadmissible. Both fit the ruling as relayed.

ANSWER, recorded verbatim: **"test,A — core only (Recommended)"** -- option (A)
plus a free-text token `test`. Recorded as SELECTED, not as a clean ruling: that
token reads as much like exercising the question UI as like a directive, and an
ambiguous answer should not be laundered into an owner ruling in a bean that
later agents read as authority.

Acting on it is safe either way because (A) IS THE STATUS QUO -- the sibling
applied it on #7207 (frobeniusSelected_borromean), and adopting it moves no
number and re-runs no producer. If the intent was otherwise, nothing has to be
undone; only this paragraph is wrong.

CONSEQUENCE UNDER (A). The census element stands, and so does every residual on
this bean. Reading 3 constrains 6 of the word's 11 letters and prunes NOTHING
among the 5 the parity bound leaves free -- so the SDP half does no work on the
open part of the problem, and the 5 letters still have no derived constraint.
That is the live gap.

BEAN STAYS todo (§13a).

## 2026-09-12 — the element migration LANDED on main, and `element_is_ruled: true` over-reaches by 5 letters

**Not a numerical dispute. The migration is right, the number is right, and my own
work is what supports it.** What is wrong is one provenance field, and it is the
field an owner reads.

**What landed.** `573b2ece24` moved the scored `Q_β` element from `delta_S` (short
normal form) to `nuc11_interleaved`, and `b021216ab6` closed `qou-wfvl` as
`completed`. The row improved 2.55× (4.259e+8 → 1.668e+8 ppb). The producer writes

    "element_is_ruled": true,
    "element_authority": "owner gamma-gamma ruling qou-ales 2026-09-08 +
       GammaGammaWordSelection.vertex on main (a gamma-gamma word's 2nd letter is
       negative, which excludes the gen-grouped core)"

and it calibrates at `err_pct_at_order_zero_E0 = -17.4959286063` against my
`-17.495929`. Their `delta_S` `tr_conv_D = -0.106235639848` reproduces mine to ten
digits. The exclusion argument they cite **is** my Lean lemma
`not_gammaGamma_of_snd_pos`. None of that is in question.

**The over-claim, measured.** `nuc11_interleaved` is **11 letters** — read off
`_GEN_CHAINS`, `gen0 = 7`, `gen1 = 4`, for both `p` and `n`. Every γγ word has
**even** length: a γγ word is a concatenation of 2-letter vertices
(`gammaGamma_length_even`, sorry-free). 11 is odd. **Therefore
`nuc11_interleaved` is not a γγ word** — `eleven_not_gammaGamma`, sorry-free, on
this branch.

So the ruling does not select the element. It selects the **6-letter core**
`(σ₀σ₁⁻¹)³` = three γγ vertices, and provably cannot reach the other five:

| block | letters | γγ-reachable? |
|---|---|---|
| core | 6 | **yes** — three vertices |
| quark | 3 | no — odd (`three_not_gammaGamma`) |
| gluon | 2 | no — even, but both positive (`gluonPair_not_gammaGamma`) |

The gluon pair is excluded **twice over**: its second letter is positive, and it
follows an odd-length block so no vertex boundary can align with it.

**Why this matters rather than being pedantry.** `qou-ales` says *"Shouldn't use
census."* The element now scored is **6/11 γγ-derived and 5/11 census-derived**.
`qou-wfvl` — whose title is *"the Q_β element is census-derived"* — is therefore
closed on an element that is still census-derived in 5 of its 11 letters. The
migration is 6/11 done, not done.

**What the correct label would say.** The binary field cannot express this. Either
`element_is_ruled` becomes scoped (`"core"`), or it keeps `true` alongside
`element_ruled_letters: 6` / `element_census_letters: 5`. **My judgement, marked as
judgement:** the second — keep the boolean for consumers, add the two counts, and
open a successor bean for the 5 free letters, because that is where a closing `Δ`
would have to come from and it is now the only place left.

**I have not changed it.** It is a sibling's producer and an owner-facing
provenance label; §"ASK THE OWNER BEFORE CHANGING THINGS" covers it and it is
neither a precision increase nor corpus-derived (the corpus currently *asserts*
`true`). Recorded here; surfaced to the owner.

**Second item, smaller.** `173da443b6` made the tower-summed `E₀` canonical. This
probe and `qbeta_option_e_order_dof_range_probe` still inherit the **order-zero**
form, so every percentage on this bean is on the retired base, low by 0.9915 %. On
the canonical base: interleaved `-16.677940 %`, gen-grouped `-14.613128 %`. CHECK 7
reports both and does not switch, because the cells these are calibrated against
were computed at order-zero and mixing bases is the silent-revert trap that
commit's own audit records at §6. **The ranking is invariant** — residual is
strictly increasing in `E₀`, and `E₀ > 0` is common to every candidate — so no
conclusion on this bean depends on the base.



## 2026-09-13 — the element question: ordering is provably not the lever (PR #7295)

The alternating character `sigma_i |-> -1/q` is a 1-dim rep of `H_3(q)`, so a
word's character is a product of SCALARS and depends only on the MULTISET of
its letter shifts. Measured on 3840 (permutation, generator-assignment) pairs:
exactly ONE distinct value. Lean `wordChar_of_perm` (sorry-free).

Consequence for this bean's element half. R2 of the gamma-gamma ruling
(`qou-ales`, #7212) picked the nucleon ORDERING. **An ordering choice cannot
make a word gamma-gamma-produced** — the invariant that `altChar_eq_one` pins
at +1 cannot see one. So the 5 census-derived letters of `nuc11_interleaved`
are not repairable by re-ordering or by re-assigning generators; a
gamma-gamma-derived replacement has to change WHICH letters are present.

Closed form over the three-shift alphabet the census uses, with a/b/c counting
the shifts 0 / -h / -h/2:

    altChar(w) = (-1)^(a+b+c) q^(b-a-c) ((q^2+1)/2)^c  = 1  <=>  c = 0 and a = b

Every corpus nucleon carries c = 2, and `-h/2` — the mixed ud crossing — is
BOTH the unique bar-fixed shift (#7283) and the unique shift whose character
pairs with nothing to give 1. One letter, two independent obstructions;
`qou-e58e` measured that bar IS p<->n conjugation, so that is not a notational
coincidence.

Coverage, stated honestly: FIVE of the census's six Delta families —
four at word level (`nuc9`, `nuc11_interleaved`, `nuc11_gen_grouped`, the 16
`blocks CONSTRUCTED` readings = 19 readings = 38 words), one (`delta_S`, the
short model) only at the Delta level because it is given as an NF vector and has
no shift multiset. `blocks AS STATED` is NOT covered — nothing constructs it.

NOT NEW: `qou-avt6` (2026-08-26) already has the monomial shape
`q^m ([2]_q/2)^c`, for the COUNIT rep `sigma |-> q`. This is the ALTERNATING
rep, which is the one the gamma-gamma lemma pins — a different functional, same
shape.

OPEN, spun out as `qou-efqx`: the fourth (`averaged_weighted`, colour-weighted)
template, which R3 makes canonical. Its character carries an irreducible sextic,
so the argument does not extend; only the pin-level pairing fact is measured.

Bean stays `todo` (AGENTS.md §13a — the element is an open conjecture; this
narrows it, it does not close it).



### Same day, the positive half (PR #7295 part 2)

On three strands the gamma-gamma ruling leaves **one integer**. `H_3(q)` has two
Artin generators, so a vertex `sigma_i sigma_{i+1}^-1` needs `i+1 < 2`, i.e.
`i = 0`: every gamma-gamma word is `(sigma_0 sigma_1^-1)^k`. Lean
`gammaGamma_threeStrand`, sorry-free. `k = 3` is `borromean`.

Two structural findings. Every member has a **vanishing `e^-` coordinate**
(symbolic, k = 0..24) — so `qbeta-counit-closed-form.md`'s "which both nucleon
models happen to satisfy" is FORCED under gamma-gamma, not accidental; and
`tr_M|_{z=1} - net = h*nf[e^-]` identically, so net and the retired z=1 cell
COINCIDE on every gamma-gamma word.

**The derived member misses by 440 %.** `|tr_M^{z_D}(core^3)|*E_0 = 4.22140`
MeV against `Q_beta = 0.78233`: **+439.592 %**. That is the honest number for
the route as a single-word Q_beta carrier on three strands.

**And the matching members are selected, measurably.** The k=1 (mod 3) band
descends monotonically THROUGH the target (k=7 gives +0.610 %); the difference
grid over k,l <= 24 is 300 pairs straddling it, local spacing 1.29 %, best
(8,23) at +0.455 % — against **0.322 % expected by chance** from that spacing.
The best match is not even better than chance. Choosing k or (k,l) by residual
is selection against the target and is forbidden.

So the live question is sharper: **either `k` is derived from something other
than the residual, or the gamma-gamma carrier for Q_beta is not a single
three-strand word.** Both open. Scope-(a) — no invariant here forbids the
gamma-gamma route; what is excluded is the METHOD.



### Part 3, same day — the H_3 collapse is an ACCIDENT OF THREE STRANDS (PR #7295)

The three-strand collapse was never about the Hecke algebra. Lean, sorry-free:
`gammaGamma_iff_vertexWord` — the gamma-gamma words are EXACTLY the free monoid
on the vertices; `gammaGamma_index_lt` — on n strands only n-2 vertex indices
exist. ONE at n=3 (hence the cyclic monoid), TWO at n=4.

Measured (general-n T-basis reducer, validated against the corpus's hand-coded
H_3 tables, and independently recovering growth k+1 at n=3):

                      n = 3                 n = 4
  vertices            1                     2
  growth (k <= 8)     k+1 = 1..9            2^(k+1)-1 = 1,3,7,...,511
  span rank           3 of 6                21 of 24

At n=4 EVERY one of the 2^k words of length 2k is a distinct element of H_4 —
the Hecke relations impose no collapse at all — and the span goes from half the
algebra to seven eighths.

**So the +439.592 % H_3 miss must NOT be quoted for H_4.** It is a fact about a
one-integer family. At four strands the family is free and nearly fills the
algebra.

Caveat stated: growth and rank are measured at a generic rational h, so both
are LOWER bounds on the symbolic answer — the safe direction, since reaching
the maximum establishes it exactly. Two generic values agree.

NOT claimed: no four-strand Markov trace is computed, so nothing is said about
whether an H_4 gamma-gamma element reproduces an observable. And which 3 of the
24 dimensions are missing from the span is not measured.



### Part 4, same day — the general-n Ocneanu trace, and the H_4 trace set (PR #7295)

The corpus had NO general-n Markov trace: `pyhecke.gram` carries the H_3 vector
`[1, z, z, z^2, z^2, z(hz+1)]` as a hand-coded literal and nothing generalises
it. Built one from the three defining properties via the S_{n-1}-coset
decomposition, validated three ways — it reproduces the H_3 literal exactly
(symbolic in h AND z), satisfies tr(xy)=tr(yx) on H_4 pairs, and satisfies the
Markov property at n=4 against n=3. The latter two are NOT inputs to the
recursion, so they are real tests; the first `coset_factor` failed them.

Measured, gamma-gamma trace sets at z_D, proton pin, k <= 8 vertices:

                  count    range                    median gap
    n = 3            9     [0.18618696, 1.0]        0.032897756
    n = 4          511     [0.11139758, 1.1374052]  0.0025322918

**13.0x denser**, so the anti-fit conclusion sharpens — selection by residual
was already forbidden at n=3 and at n=4 is not even tempting.

**And barely wider.** 511 distinct elements spanning 21 of 24 dimensions have
traces confined to a band only ~1.3x the n=3 one. The trace is a very LOSSY
functional on the gamma-gamma set: free growth in the algebra does not buy a
wide trace image. That is a constraint in its own right and was invisible
before this.

Scope-(a). NO four-strand Q_beta prediction — E_0 and the
element-to-observable map are H_3 constructions and the corpus does not define
their n=4 analogue. The n=4 set is compared to ITSELF at n=3, structurally.



### Part 5, same day — the SDP half of qou-ales, and it is a REAL selector (PR #7295)

The ruling says selection is via gamma-gamma production AND the confinement SDP.
Parts 1-4 did the gamma-gamma half; this is the SDP half, and it is the first
DERIVED selector on this arc (PSD feasibility is structural, not a residual).

**Three strands: the conjunction is EMPTY.** In the (2,1) block, exactly:
`a = -1/(q(q^2+1))`, `a' = q^3/(q^2+1)` — **a' IS z_D** — and the gamma-gamma
vertex has `det V = 1`, `tr V = -1 - h^2`. So V is an ELLIPTIC SL_2(R) element,
and `V^3 = 1` forces `q = 1`: **the Borromean baryon is SDP-feasible only in the
classical limit.** New Lean `QOU.Mass.PsdDetOneTrace` (sorry-free) proves a real
PSD 2x2 of det 1 has trace >= 2 with equality only at the identity, and measured
`tr(V^k) < 2` for k = 1..200 — so the exclusion is a theorem about the PSD cone,
not arithmetic. This also EXPLAINS the k mod 3 banding of Part 2: a near-order-3
rotation, exactly order 3 only at q = 1, so the bands drift.

**Four strands: NON-empty and very selective — and my first draft was wrong.**
It asserted infeasibility at n=4 too, having tested only the powers of ONE
vertex; over all 2^k words the assertion FAILED. Of **8190** words to 12
vertices, exactly **5** are feasible: `(v0v1)^2`, `(v0v1)^4`, `(v0v1)^6`, and two
sporadic 10-vertex words. `(v0v1)^m` is feasible **iff m is even**.

**The mechanism, not an analogy.** In BOTH 3-dim blocks the spectrum of `v0v1` is
exactly `{-q^2, -q^-2, 1}` — two NEGATIVE eigenvalues — so odd powers cannot be
PSD and even powers have spectrum `{q^-4, 1, q^4}`. Same cause as the H_2 rule
(`sigma_0` has eigenvalue `-1/q`). The 1-dim and (2,2) blocks send every power to
the identity; all discrimination lives in the two 3-dim blocks. And `(v0v1)^2` is
NOT the identity there (max |M-I| = 0.348, 0.518), so its feasibility is genuine
positivity rather than triviality.

So the ruling's two halves are NOT in conflict — they simply have no common
solution on three strands. **Smallest derived candidate: `(v0 v1)^2`, four
vertices, eight letters.**

NOT claimed: the feasible set is not characterised (only enumerated to 12
vertices; the two sporadic words are unexplained); no cost/minimality is
computed, so this NARROWS the candidate set without selecting a word; no
observable is computed.



### Part 6, same day — SDPSelected has a UNIQUE solution (PR #7295)

Part 5 did the feasibility half and said it did not compute minimality. This is
minimality, and it closes the selection.

The cost is the corpus's: `mba-step10-confinement-sdp.md` states
`minimize Sum_i t_i x_i` with `t_i = tr_M(b_i)`, so the objective on a word is
its Markov trace. Evaluated with the general-n Ocneanu recursion from Part 4
(re-verified against pyhecke.gram's H_3 vector so this cannot inherit a silent
breakage).

Costs at z_D, proton pin, over the five PSD-feasible words:

    (v0 v1)^2    (0,1,0,1)                   1.032897755524660383   <- MIN
    sporadic A   (0,0,1,1,0,1,1,0,0,1)       1.073238807935729209
    sporadic B   (0,1,1,0,0,1,0,0,1,1)       1.073238807935729209
    (v0 v1)^4    (0,1,0,1,0,1,0,1)           1.137405209118677445
    (v0 v1)^6    (0,1,0,1,0,1,0,1,0,1,0,1)   1.331992492573499969

The minimum is STRICT and ATTAINED, not merely least-in-a-truncation: cost on
the even alternating family is strictly increasing in m (1.0329 -> 4.0944 for
m = 2..14), so extending the enumeration cannot beat m = 2.

**SDPSelected -> `(v0 v1)^2`: four vertices, eight letters, four strands.**
DERIVED — no continuous parameter tuned, no discrete choice made against a
measured value, no observable entering at any point. This is the arc's first
complete derived selection.

Observation flagged as such: the two sporadic words have EXACTLY equal cost
(< 1e-30) while their `net` differs (1.1426 vs 0.9495), so whatever relates
them does not preserve net. Unexplained; two data points are not a pattern.

TWO GAPS, and the result may not be quoted without them:
1. the LP's `net(x) = n_target` constraint is NOT imposed (it belongs to the
   mixture formulation; net is reported per word so it can be applied later);
2. "unique" means among gamma-gamma words of at most 12 vertices on four
   strands — a cheaper feasible word at 13+ vertices is not excluded, though a
   cheaper ALTERNATING one is, by monotonicity.

NOT DONE, deliberately: no Q_beta comparison. E_0 and the
element-to-observable map are H_3 constructions with no corpus-defined n = 4
analogue, and reporting a residual would re-introduce the
selection-against-the-target the earlier parts measured and rejected. The word
is derived; what it predicts is a separate question.



### 🛑 Part 6 RETRACTED, same day (PR #7295)

Part 6 above claimed SDPSelected has a unique solution, `(v0 v1)^2`. **It does
not, and I withdraw that.**

The EMPTY gamma-gamma word — zero vertices, `GammaGammaWord.nil`, the identity
of `H_n` — is PSD-feasible in every block (the identity matrix is PSD) and its
Markov trace is exactly **1.0**, against 1.032897755524660383 for `(v0 v1)^2`.
So over the candidate set as the Lean states it, **SDPSelected selects the empty
word**, vacuously. Part 6 silently restricted to words with >= 1 vertex.

**The corpus already proved this one level up, and I cited the block without
reading it.** `prop:operator-selection-lp` §"Degeneracy of this program":
`b_1 = 1` so `G_1j = t_j`, hence the first Frobenius positivity constraint IS
the objective bounded below by zero — optimal value identically 0 for every n,
q and trace convention; and the minimiser set is a positive-dimensional
mirror-closed face, so which vertex a solver returns is its pivoting rule. That
block states outright that *"downstream blocks have read the program as a
selection principle, which it is not"*. I became one of those readers before
becoming an independent confirmation of it in the discrete setting.

**WHAT SURVIVES, quote these separately:**
1. **Feasibility does the real work and is untouched** — Part 5's 5-of-8190 at
   n=4, none at n=3. A genuine structural zero-parameter filter.
2. Among **NON-EMPTY** gamma-gamma words of <= 12 vertices on four strands,
   `(v0 v1)^2` is the strict minimiser with the minimum ATTAINED. True about a
   RESTRICTED set; **not** SDPSelected.

So the arc does NOT have a complete derived selection. It has a derived
*filter* (feasibility) and no derived *selector*. The open problem is what
breaks the tie among the 5 — and the corpus's own degeneracy result says the LP
objective cannot be it.


## Part 7 (PR #7304) — crossing energy is the THIRD degenerate functional, and no γγ word binds

`computations/qbeta/qbeta_gamma_gamma_crossing_energy_probe.py` (6/6).

**Calibrated first, by data, not by reading.** `def:crossing-energy` gives the
electron (left trefoil `T_(2,3)`, three POSITIVE crossings) `E_cross = 3q =
3.329935748` against the `~3.330` in `pair-creation-energy.md`, and the positron
(mirror) `-3/q = -2.702754852` against `~-2.703`. A reversed sign convention
would have swapped these, so the orientation is pinned.

**Closed form.** `E_cross(k-vertex γγ word) = k*h` EXACTLY (k = 0..14). A vertex
`σ_i σ_{i+1}^{-1}` is one positive crossing and one negative: `q + (-1/q) = h`.

**Order-blind, again.** 3840 (permutation, index-assignment) pairs of a 5-vertex
word → 1 distinct value. Same blindness as #7295's alternating character, for
the same structural reason (a sum over letters). Second order-blind functional
on this family.

**The substantive finding.** `h > 0` for every `q > 1`, so `E_cross > 0` for
every non-empty γγ word, and `def:crossing-energy` reads positive as *repulsion
dominates*. **NO γγ word is binding-dominated — any number of strands, any
q > 1.** At q_0, `h = 0.20906029879563932`.

**Degenerate again.** `E_cross(empty) = 0`, below all five PSD-feasible words
(0.8362 / 1.6725 / 2.0906 / 2.0906 / 2.5087). So this is the THIRD functional
here whose unconstrained optimum is the trivial answer, after the Markov trace
and the LP objective — the latter proved degenerate by
`prop:operator-selection-lp`'s own "Degeneracy of this program" section.

**It does not separate.** Ordering among non-empty words is by vertex count
alone; the two sporadic 10-vertex words TIE exactly.

**NOT implemented, deliberately:** `knot-operator-selection-proof.md`'s demand
constraint `⟨Φ, dem(K)⟩_F ≥ ‖dem(K)‖_F`, which is the stated reason an
unconstrained minimum need not be the last word. Building `dem(K)` requires
choosing which K the nucleon is, which is the question — implementing it here
would be circular.

Scope-(a): one functional, one family. It does not exclude a binding-dominated
canonical word; it says the γγ construction alone cannot supply one under this
energy.


## Part 8 (PR #7304) — what the ruling PREDICTS for Q_β: +458 % to +620 %, and the 0.11 % near-hit is worse than chance

`computations/qbeta/qbeta_gamma_gamma_qbeta_prediction_probe.py` (7/7).

Nobody had scored the γγ + confinement-SDP admissible set against Q_β. This
does, through the dashboard's own path (`|tr^{z_D}| · E_0`, canonical
tower-summed `E_0`), calibrated first: the census element `nuc11_interleaved`
scores -16.67794 % against the -16.678 % AGENTS.md records.

**All five PSD-feasible words of #7295**, ordered by vertex count, NOT residual:

    (v0 v1)^2     4 vertices   4.36655806955 MeV   +458.1454 %
    (v0 v1)^4     8            4.80836159015       +514.618  %
    sporadic A   10            4.53709919716       +479.9445 %
    sporadic B   10            4.53709919716       +479.9445 %
    (v0 v1)^6    12            5.63097609218       +619.7668 %

**The structural point.** The five agree with EACH OTHER to a factor 1.28957
while missing the measurement by 5.58x to 7.20x. Internal spread < smallest
miss, so **no re-selection inside the admissible set can reach Q_β** — the
choice of word is not the free parameter.

**It is the SDP half that excludes the measured value, not γγ.** Target
`|tr^{z_D}| = 0.185059` sits BELOW 1 = tr(empty word) and below the smallest
feasible trace 1.032898. PSD feasibility pushes the trace up; the target is
under the whole feasible set.

**THE TRAP, disarmed.** Drop the SDP half and the unconstrained family straddles
the target (8190 words, |tr| in [0.003435, 1.331992]) with a best match at
**0.110577 %** — eleven `v_0` and one `v_1`. Worth nothing, and MEASURED to be:
529 distinct trace values, 50 within ±10 % of the target, median spacing
0.000346646 → expected best-by-chance **0.04683 %**, observed **0.110577 %** —
**worse than chance**. Same control and verdict as the H_3 difference-grid check
(0.455 % observed vs 0.322 % expected). The twelve tying words are one
order-blind orbit, none PSD-feasible.

Scope-(a): one functional, one family, n = 4. Says nothing about n > 4, a
different E_0, or a tower correction. The demand constraint is still NOT imposed.


## Part 9 (PR #7304) — the PSD trace FLOOR: scope-(b) exclusion for n ≤ 5, no enumeration

`computations/qbeta/qbeta_gamma_gamma_psd_trace_floor_probe.py` (7/7).

Part 8 left "enumerate the feasible set at n = 5, then n = 6" as next. **That
search is unnecessary at n = 5.** Formalize-first: the invariant prunes the
class before the scan runs.

**Three ingredients, each machine-verified:**

1. **Convention D IS the two-row truncation with strictly positive weights.**
   `y_(n−k,k) = [n−2k+1]_q/[2]_q^n`, and `y = 0` on three rows or more. Checked
   n = 3..8: all 42 partitions with ≥3 rows carry exactly 0; all 21 one- and
   two-row partitions carry `y > 0`.
2. **PSD feasibility ⟹ every character is non-negative.** A PosSemidef matrix
   has non-negative trace, so `χ_λ(w) = Tr(ρ_λ(w)) ≥ 0`.
3. **The trivial block is pinned at exactly 1.** Trivial rep: `σ ↦ q`, so
   `σ⁻¹ = σ − h ↦ q − h = 1/q`, and a γγ vertex ↦ `q·(1/q) = 1`. Measured to
   2.2e-40 on 80 words at n = 3..6. **Counit twin of
   `GammaGammaWordSelection.altChar_eq_one`** (sorry-free, alternating char).

**Hence** in `tr_M = Σ_λ y_λ χ_λ` every term is ≥ 0 and the trivial term is
exactly `y_(n)`:

    tr_M(w)  ≥  y_(n)  =  [n+1]_q / [2]_q^n

for EVERY PSD-feasible γγ word on n strands — no enumeration, word-independent.

**What it excludes.** Target `|tr_M| = 0.185059`. Floor: **0.7527 / 0.5054 /
0.3193 / 0.1943** at n = 2/3/4/5 (all exclude), **0.1153** at n = 6 (does not).
So **no γγ + confinement-SDP word on five strands or fewer can reproduce
Q_β** — scope-(b), invariant named above.

The floor decays like `(q/[2]_q)^n ≈ 0.552^n` against a fixed target, so the
crossing is **one-sided**: the exclusion is a prefix of the strand counts,
never scattered. And it is **loose** where checkable (measured min at n = 4 is
1.0329, 3.2× the floor), which makes the exclusion conservative.

**NOTHING claimed at n ≥ 6**, recorded as a machine assertion rather than a
prose caveat: the floor dropping below the target means the ARGUMENT stops, not
that a feasible word reaches it.

Cross-checked: the Frobenius pairing agrees with the independent Ocneanu
recursion to 5.0e-36 over 28 words at n = 3, 4, 5.

**Lean status: NOT formalised.** Ingredient 3 has a sorry-free alternating
twin; `WedderburnBlocks.PSDFeasible` already carries ingredient 2's hypothesis
shape. The composite bound is the open formalisation.


## Part 10 (PR #7304) — 🛑 tr_M ≥ 1 at EVERY n, which SUPERSEDES part 9's floor

`computations/qbeta/qbeta_gamma_gamma_trace_ge_one_probe.py` (8/8) + Lean
`PsdDetOneTrace.card_le_trace_of_det_one`, `GammaGammaTraceFloor.pairing_ge_one_of_psdFeasible`
(both sorry-free).

**Part 9's floor was mine and it was weak.** It kept the trivial block's term of
the Frobenius pairing and discarded the rest as *merely* non-negative. They are
not merely non-negative — each is bounded below by its own block dimension —
and keeping them gives a bound that is stronger AND n-independent.

**Four ingredients, all measured:**

1. **Every γγ vertex has determinant 1 in every block.** `σᵢ` and `σᵢ₊₁` are
   conjugate in the braid group ⟹ same block determinant ⟹
   `det(σᵢσᵢ₊₁⁻¹) = 1`. Measured 7.2e-40 over 78 (block, vertex) cases at
   n = 3..6; the conjugacy fact itself to 4.9e-40. Multiplicative, so every
   WORD inherits it — 2.1e-39 over 590 (word, block) pairs.
2. **PSD + det 1 ⟹ trace ≥ dim** (AM-GM). Now **general-dimension Lean**
   (`card_le_trace_of_det_one`); #7295 had only the 2×2 case, and blocks reach
   dim 16 at n = 6.
3. **Convention-D weights are non-negative.**
4. **`Σ y_λ dim_λ = 1`** — the Markov normalisation, 4.6e-41 at n = 3..8. This
   is what makes the bound the value **1**.

⟹ **`tr_M(w) ≥ 1` for every PSD-feasible γγ word, at every n.** **TIGHT** —
the empty word is the identity in every block, measured exactly 1.0.

**Consequence.** Target `|tr_M| = 0.185059` is below 1 by a factor **5.4037**,
so the γγ + confinement-SDP route **cannot reach Q_β at ANY strand count**. The
smallest Q_β the family can predict is exactly `E₀ = 4.2274834 MeV` =
**+440.369 %**; the five measured n=4 words land +458 %..+620 %, above that
minimum as they must.

**Part 9 is superseded in strength, not retracted** — its numbers stand, its
scope ("excluded n ≤ 5, open n ≥ 6") was short. Its floor is below 1 at every
n ≥ 2. Kept in the corpus because stopping at the first block is an easy
mistake, and its decay lemma is why the weaker exclusion was one-sided.

**Scope (b), ALL n**, for this functional (`ε` = Markov trace at `z_D`) and this
`E₀` only. Says nothing about another route, a different `E₀`, or a **tower
correction** — and the tower correction is LIVE, since `E₀` is canonical by
ruling with an OPEN series (`qou-y3bm`).


## 🛑 Part 11 (PR #7304) — RETRACTION of parts 9 and 10's Q_β reading

`computations/qbeta/qbeta_qbeta_scores_a_difference_probe.py` (6/6).

**Both over-claims were mine, and the calibration step caught them.**

**What I asserted** (parts 9 and 10): the floor `[n+1]_q/[2]_q^n` and then
`tr_M ≥ 1` mean "no γγ + confinement-SDP word can reproduce Q_β" — for n ≤ 5,
then at every n, with minimum prediction `E₀` = +440.369 %.

**What is true.** `Q_β = |ε(Δ)|·E₀` where **Δ = NEUTRON element − PROTON
element**. Source says so verbatim: `delta_of` — *"Delta = neutron - proton,
coordinatewise in the NF basis"*. The Markov trace is **linear**, so
`tr(Δ) = tr(n-word) − tr(p-word)`, and two quantities each ≥ 1 have a difference
bounded by **nothing**. Neither exclusion follows. Both withdrawn.

**How caught.** Reconstructing `nuc11_interleaved` letter by letter gave
tr(p) = 0.6293284022029219, tr(n) = 0.4751335171556822 — **neither** matching
the recorded `tr_conv_D = -0.1541948850472397056592555`. Their **difference**
matches to 1.4e-26, every recorded digit.

**What the difference functional gives**, all 15 pairs reported (picking the
closest would be selection against the target): **−100 % to +79.4 %**. They
**STRADDLE** the target rather than sitting above it — the opposite of the
retracted claim. Best +5.15 % against expected-by-chance **7.73 %** on an
11-value grid: same order, not evidence.

**Survives untouched** (measured, not inferred): `tr_M ≥ 1` per **individual**
PSD-feasible γγ word, tight; the det-1 fact; AM-GM; weight non-negativity; the
Markov normalisation; the floor and its decay; **every Lean theorem** (they are
about pairings and PSD matrices, none mentions Q_β); the crossing-energy results.

**One NEW finding survives:** the scored element's proton and neutron words are
**both PSD-infeasible** — `(2,1)` and `(1,1,1)` fail for each — with `det ≠ 1`
in every block. So the **SDP half** of the ruling excludes the scored element
directly at the element level, independently of the altChar exclusion.

**Fixed in the same commit**, so nothing false is left standing: both probes'
title lines, descriptions, scope paragraphs and assertion names (one was
*named* `Q_beta_is_excluded_at_every_strand_count`); a scoping note on the
prediction probe (it scores single words, also not the scoring path); and a
docstring note on `GammaGammaTraceFloor.lean`.

**Now OPEN:** whether any **pair** of PSD-feasible γγ words reproduces Q_β.


## Part 12 (PR #7304) — under the ruling the p/n asymmetry has ONE home, and the corpus keeps it where the ruling forbids

`computations/qbeta/qbeta_pn_asymmetry_has_one_home_under_the_ruling_probe.py` (6/6).

Part 11 established Q_β is scored on `Δ = n-word − p-word`, so the ruling must
select **two** words and something must separate them. This asks *what*.

**The corpus's answer today.** `nuc11_interleaved` = `core(6 γγ letters) ·
quark(3) · gluon(2)`, and **the core and gluon pair are IDENTICAL between
proton and neutron**. Three letters of eleven carry the whole asymmetry:
`(σ₀)(σ₀−h/2)(σ₁−h/2)` vs `(σ₀−h/2)(σ₀−h/2)(σ₁−h)`.

**Why that is exactly what the ruling fixes.** altChar is multiplicative and
pinned at **1** on every γγ word (`altChar_eq_one`, sorry-free). Measured: core
= **1.0 exactly**; quark blocks = **−0.9108** (p) and **−1.1221** (n), both
negative ⟹ neither is γγ-expressible — and they are precisely where the
nucleons diverge, by **23.2 %** in that invariant. Under the ruling both words
would be 1 and the invariant could not separate them at all.

Not a defect in corpus or ruling — it is **the tension between them, localised
to three letters**.

**What is left.** A γγ word's only freedom is which vertices and how many, and
the trace is blind to their **order**. So under the ruling the p/n asymmetry
has exactly one home: **the vertex multiset**. (Argument, not measurement;
asserted so it is machine-recorded; holds at every n.)

**Upgrades part 11:** at n = 4 the PSD-feasible set is 6 words, so exactly
**15** unordered (n, p) assignments — the 15-pair table is **EXHAUSTIVE** at
that strand count, not a sample. Its −100 %..+79.4 % span is therefore a
statement about the ruling, not about a selection.

**Cross-checked by two routes** — per-letter altChar product vs the `(1,1,1)`
Hoefsmit block trace, agreeing to **4.6e-39**. This is the check whose absence
caused part 11's retraction: without it the letter encoding is an unchecked
convention, which is what it was when I read `tr_conv_D` as one word's trace.

Scope-(a) + one structural observation. No pair is selected; doing so by
residual would be selection against the target.


## Part 13 (PR #7304) — BAR PARITY forces a unique Q_β from the un-ruled letter, and the census assignment FAILS it

`computations/qbeta/qbeta_bar_parity_forces_a_unique_quark_letter_probe.py` (6/6).

Working this bean's own open problem: the parity bound proves 5 of 11 letters
lie outside the ruling; of those, the two bar-fixed (`−h/2`) and the gluon pair
are **shared** between the nucleons, so **one** quark letter carries the whole
p/n asymmetry. What selects it?

**The hypothesis is the corpus's, not mine.** AGENTS.md line 2182: Q_β is *"the
bar-odd `sinh` partner of the bar-even `cosh` meson scale m_π"*. That is
attached to the **published closed form** — the `z = 1` cell the 2026-09-08
ruling retired as a base — so whether it survives to `z_D` is precisely the
open question. Impose it and see.

**The freedom.** Odd letter in any of 3 quark slots, either member of the
bar-pair (`σ` shift 0, `σ⁻¹` shift `−h`). Slots 0 and 1 are both generator 0
and give **exactly** the same trace ⟹ only **4 distinct elements**, and 26 of
the 30 ordered (p,n) pairs have nonzero Δ.

**The result.** Requiring `tr^{z_D}(Δ)(1/q) = −tr^{z_D}(Δ)(q)` leaves **8 of
26**, and **the census assignment is NOT among them**. Every survivor gives both
nucleons the **same** member of the bar-pair, differing only in generator; the
census gives them **opposite** members — exactly what destroys the parity.

**And the 8 need no choosing between.** Symbolically
`Δ(σ,σ) = −Δ(σ⁻¹,σ⁻¹)` **exactly**, so all eight share one magnitude:

    |tr(Δ)| = (q⁶−1)(q⁴+1)(q¹²−4q¹⁰+6q⁸−7q⁶+6q⁴−4q²+1) / (4q⁹(q²+1)²)

forcing **Q_β = 0.353415698 MeV, −54.825 %**.

🛑 **No selection was made** — the constraint is a parity in `q`, never
proximity to the measured value; it narrows 26 → 8; the 8 collapse. Nothing
left to pick. And the forced answer is **worse** than the census's −16.678 %,
which is the ranking AGENTS.md mandates: report what the specification gives
even when worse; rank by derivational cleanliness, never by residual.

🛑 **It does not close Q_β.** All four distinct elements **FAIL PSD**, so the
SDP half rejects this entire one-letter family — census and bar-odd alike.
Narrows the problem; does not solve it.

**Calibrated first** (the check whose absence caused part 11's retraction): the
(slot, kind) coordinates reproduce `tr_conv_D = -0.1541948850472397056592555`
to 1.4e-26.

Scope-(a). **Unconditional:** the census assignment is not bar-odd; the bar-odd
family collapses to one magnitude; no member is PSD-feasible. **Conditional:**
that bar-oddness transfers from the retired `z = 1` cell to `z_D`.

**BEAN STAYS todo (§13a)** — the subject is an open derivation.


## LANDED 2026-09-13 — PR #7304 (`49e015595d4`), and the bean stays OPEN

Seven probes (46 checks), two sorry-free Lean files. The bean's own open
problem — what selects the un-ruled letters — was **worked, not deferred**.

### The result: bar parity FORCES one number

The parity bound proves no 11-crossing word is γγ-produced, so 5 of 11
letters lie outside the ruling. The two bar-fixed (`-h/2`) letters and the
gluon pair are shared between the nucleons, so **one** quark letter carries
the whole p/n asymmetry. Imposing the corpus's own bar-odd property on
`tr^{z_D}(Delta)`:

* 26 nonzero-`Delta` ordered pairs -> **8 survivors**; the census assignment
  is **not** among them.
* The 8 collapse to ONE magnitude by the exact identity
  `Delta(sigma,sigma) = -Delta(sigma^-1,sigma^-1)`, forcing
  **Q_beta = 0.353415698 MeV, -54.825 %**.

No selection was made — the constraint is a parity in `q`, never proximity
to the measured value — and the forced answer is WORSE than the census's
-16.678 %. That is the AGENTS.md ranking: derived beats selected.

### The retraction, mine

Parts 3 and 4 inferred from `tr_M >= 1` that the γγ route cannot reproduce
Q_beta. **Wrong.** `Delta` is the neutron element MINUS the proton element,
the trace is linear, and a lower bound on each word bounds no difference.
Caught by calibration: `tr(p)` and `tr(n)` each failed to match the recorded
cell while their difference matched to 1.4e-26. The Lean stands untouched;
only prose was scoped, and a note in `GammaGammaTraceFloor.lean` stops a
reader re-deriving it.

### The SCOPE defect, also mine, fixed before merge (`04edd8b5d75`)

I wrote "all four elements fail PSD, so the SDP half of the ruling rejects
this family". That is **whole-element PSD = reading (B)**. This bean records
the selected scope as **(A) core only**, under which reading 3 prunes
nothing among the 5 free letters and the census element stands. So the PSD
result is a MEASUREMENT under (B), not a rejection by the ruling — and under
(A) it excludes nothing. Assertion renamed
`no_configuration_is_whole_element_PSD_feasible_reading_B_only`.

### STILL OPEN — do not close this bean

1. **Which reading of the SDP scope the ruling means.** (A) and (B) give
   opposite verdicts on this family. Owner call, not an agent one.
2. **Whether the bar-odd hypothesis survives the move to `z_D`.** It is
   attached to the retired `z = 1` closed form. Imposing it costs -54.825 %;
   that is reported, not avoided.


## 🟧 OWNER RULING 2026-09-13 — SDP scope is **(B) whole element**

The fork this bean carried as *"(A) core only, SELECTED-with-ambiguity"* was put
to the owner with both options framed. **The owner answered "B".**

**What (B) means.** The confinement SDP of `qou-ales` constrains **every
Wedderburn projection of the full 11-letter word**, not only the 6 gamma-gamma
core letters. Reading (A) — the core-only reading, under which reading 3 prunes
nothing among the 5 letters the parity bound leaves free and "the census element
stands" — is NOT the ruling.

### Consequence 1 — the one-letter quark family is rejected outright

All **6** (slot, kind) configurations fail `Matrix.PosSemidef` on at least one
Wedderburn block. Under (B) that is a rejection by the ruling, not a
measurement. It takes out BOTH arms at once:

* the **8 bar-odd survivors** and their forced `Q_beta = 0.353415698 MeV`
  (-54.825 %), and
* the **census assignment**.

So the bar-parity derivation forces an element the SDP half then excludes. Both
halves stand — the parity narrowing is real and forced, and the element it
forces is inadmissible. That is a stronger negative than "does not close".

### Consequence 2 — the DASHBOARD'S SCORED ELEMENT is excluded

`nuc11_interleaved` — the element `per-observable-100x-status.witness.json`
currently scores for the **Q_beta, m_n and Delta_pn** rows — fails
`Matrix.PosSemidef` on `(2,1)` and `(1,1,1)` for **both** nucleons. Block
determinants, proton: `(3,) 1.38249446339`, `(2,1) -1.02197249381`,
`(1,1,1) -0.739223570776`; neutron: `1.1221068216`, `-1.02197249381`,
`-0.910762214553`. The `(1,1,1)` entries are the alternating character and are
the already-recorded sign exclusion; the `(2,1)` failure is additional.

So under the ruled scope the L2 dashboard scores an element the selection rule
that is supposed to produce it rejects.

### What was NOT done, deliberately

**The dashboard is not re-scored.** Choosing what replaces the element is a
separate decision with its own blast radius (three L2 rows and every figure
quoted from them), and it is not an agent's to take. See "still open" below.

### Recorded in

`qbeta_bar_parity_forces_a_unique_quark_letter_probe.py` and
`qbeta_qbeta_scores_a_difference_probe.py` — docstrings, witness descriptions,
`scope` blocks and the two assertion names inverted; both re-run 6/6, both
witnesses verified to carry the ruling and to no longer carry the superseded
"(A) core only / NOT a rejection" text.

The scoping of these two probes has now moved **twice**, and both moves were
mine: asserted unscoped, demoted to "measurement under unselected (B)", and now
reinstated by ruling. The verdict matches the first draft; it is reinstated by
the owner's answer, not by the argument that first produced it.

## STILL OPEN after this ruling — the bean stays `todo`

1. **What replaces `nuc11_interleaved`** on the three L2 dashboard rows. The
   ruled scope excludes it and nothing derived replaces it yet. Re-scoring is
   an owner decision (cf. `qou-iagg`, which records the authorisation pattern).
2. **A principle for the 5 un-ruled letters that is BOTH bar-consistent AND
   whole-element PSD-admissible.** The one-letter family supplies neither
   jointly — that is now the sharp form of the open problem.
3. **Whether the bar-odd hypothesis survives the move to `z_D`** at all. It is
   attached to the retired `z = 1` closed form; imposing it costs -54.825 %.


## 2026-09-13 — item 2 is REFRAMED, not answered: the obstruction is the LENGTH

Working item 2 ("a principle for the 5 un-ruled letters that is both
bar-consistent and whole-element PSD-admissible"), formalize-first found an
invariant that prunes the search instead of narrowing it.

**The theorem** (`QOU.Mass.AltCharShiftMultiset`, sorry-free, lean-direct exit 0,
`#print axioms` clean on all six new declarations):

* `letterChar_neg` — EVERY letter of the corpus alphabet has strictly negative
  alternating character: `sigma -> -1/q = -0.9009`, bar-fixed
  `-> -(q^2+1)/(2q) = -1.0054`, `sigma^-1 -> -q = -1.1100`.
* `wordChar_sign` — therefore `sign(wordChar w) = (-1)^len(w)` for ANY letters,
  ANY order, ANY generator labelling.
* `no_eleven_letter_word_is_alt_psd` — the alternating block is
  ONE-DIMENSIONAL, so under scope (B) PSD there is exactly `0 <= character`.
  Eleven is odd. So **every** 11-letter word over this alphabet is excluded.

**Why this reframes item 2.** The obstruction does not depend on which letters
carry the p/n asymmetry, so no choice among the 5 un-ruled letters can repair
it. Item 2 as posed has no answer AT LENGTH 11. The question to ask instead is
about the crossing budget.

**What the corpus already had, and why this is not a re-derivation.**
`protonWord_char_neg` / `neutronWord_char_neg` were already proved — each for
ONE word, by computing that word's closed form. The mechanism (per-letter
negativity, hence parity) was not, and it is the part that generalises. Found
by corpus-grep before writing; without it I would have re-derived the two-word
case and called it new.

**Two independent parity obstructions, same direction.** Gamma-gamma words have
even length (`gammaGamma_length_even`), which is why the CONSTRUCTION half of
the ruling reaches only 6 of the 11 letters. The SDP half under (B) ALSO
demands even length, by a completely different argument. Neither uses the other.

**Confirmation** (`qbeta_altchar_sign_is_length_parity_probe.py`, 6/6):
exhaustive over all **1092** words at lengths 1..6 with ZERO exceptions, and the
INDEPENDENT engine route (Hoefsmit `(1,1,1)` matrices, never the scalar model)
agrees to **2.28e-39**. Per-letter products also reproduce every block value
recorded in #7304 to 15 digits.

**Honest limit, from the Lean docstring rather than discovered later:**
per-letter negativity fails for a letter with shift `d >= 1/(q^2-1) ~ 4.3094`.
Every corpus letter has `d` in {0, -1/2, -1}; the closest is `d = 0`, short by
4.3094. So this excludes words over the CORPUS ALPHABET, not over every
conceivable alphabet. A letter with a large positive shift is the only escape
this argument leaves open, and nothing in the corpus supplies one.

**What is NOT claimed:** that no nucleon word exists. Only that no ODD-length
word over this alphabet is admissible in the alternating block under scope (B).

### The open items, restated after this

1. **What replaces `nuc11_interleaved`** on the three L2 rows. Owner decision,
   unchanged, and now sharper: the replacement cannot be another 11-letter word
   over this alphabet.
2. ~~A principle for the 5 un-ruled letters~~ **superseded** — no such principle
   exists at length 11. The live question is whether the **11-crossing budget**
   is correct, given that scope (B) and the gamma-gamma construction BOTH
   require even length. That is a question about the corpus's crossing
   accounting, not about letter selection.
3. **Whether the bar-odd hypothesis survives the move to `z_D`** — unchanged.


## 2026-09-14 — 🛑 I ATTACHED THREE MERGED PRs TO THE WRONG PSD READING. The parity exclusion is reading 1; the live reading is 3, and under it the budget is unconstrained.

**What was wrong, and it was mine.** #7319 / #7325 / #7336 built a length-parity
exclusion on the alternating block `(1,1,1)`, and I recorded the 2026-09-13 owner
answer in AGENTS.md as *"every Wedderburn projection of the full 11-letter word
must be `Matrix.PosSemidef`"*. **That sentence is reading 1.** The corpus
enumerates three PSD readings and the owner selected **3** on 2026-09-12 —
*"try PSD condfinement 3 for now, but keep 1 2 for later"* (`qou-ales`):

| | criterion | status |
|---|---|---|
| reading 1 | literal `Matrix.PosSemidef` on every block | **parked** |
| reading 2 | symmetric-part PSD | **parked** |
| reading 3 | `χ_λ(w) ≥ 0` on every block with `y_λ > 0` | **SELECTED** |

The 2026-09-13 fork was explicitly about **reading 3's** scope —
`qbeta_reading3_scope_fork_probe` states it as *"(A) reading 3 applies to the
γγ-selected core only / (B) reading 3 applies to the whole 11-crossing word"*.
So **(B) moved the letter scope and left the reading alone.** Live criterion:
reading 3, whole word.

**Why that is fatal to the parity result specifically.** Under convention D
`y_(1³) = 0`, and that vanishing *is* convention D (the two-row truncation,
`markovWeights_eq_jones_of_threeRow_eq_zero`) — verified here exactly, `y_(3) +
2y_(2,1) = 1.0`. So reading 3 never looks at the alternating block, which is
where the entire parity theorem lives.

**Measured — reading 3 does not constrain the crossing budget** (all generator
assignments × all dressings over the corpus alphabet):

| k | length | parity | admissible (p) | admissible (n) |
|---|---|---|---|---|
| 0 | 9 | odd | 4/8 | 4/8 |
| 1 | 10 | even | 18/48 | 18/48 |
| 2 | 11 | odd | 149/288 | 145/288 |
| 3 | 12 | even | 594/1728 | 594/1728 |

Odd lengths 9 and 11 are admissible in quantity; there is no parity signal and
no monotone in k. **#7336's "the gluon dressing must be ODD" has no force under
the live reading.**

**Second correction — the quark family is NOT empty.**
`qbeta_bar_parity_forces_a_unique_quark_letter_probe` checks
`all(is_psd(M) for every block)` (reading 1) and concludes the SDP half rejects
the whole family. Under reading 3 **one of six survives**: `(slot 2, sigma)`,
`χ_(2,1) = +0.0574586606`. So **item 1 below has a candidate the reading-1
measurement hid.** Not adopted — selecting it because it survives would be
selection against the target.

**What is UNCHANGED: the element rejection.** Both census assignments stay
excluded under reading 3 — p `(0,sigma)` `χ_(2,1) = −0.2805933509`, n
`(2,inv)` `−0.3719563247` — and `y_(2,1) = 0.2473 > 0`, so `(2,1)` **binds**.
AGENTS.md called `(1,1,1)` the exclusion "already on record" with `(2,1)`
"additional"; it is the other way round, and `(2,1)` alone is enough. Nothing
downstream moves; **the L2 rows stay un-re-scored.**

**What the parity theorem DOES say, and it is decision-relevant.** Under reading
1 no odd-length word over the corpus alphabet is admissible, and **all three
nucleon constructions are odd** (`qou-1qsw`). So adopting reading 1 would not
tighten the selection, it would **empty** it — every nucleon model dies on
length whatever its dressing, and a survivor would need an even-length model or
a letter with shift `d ≥ 1/(q²−1) = 4.3094` against the alphabet's `{0, −½, −1}`.
That is an argument about reading 1's viability for this corpus.

Probe: `computations/qbeta/qbeta_reading3_does_not_constrain_the_budget_probe.py`
(8/8, proton pin, convention D, 60 dps). The Lean stays sorry-free and unedited —
only its scope line changes.

**Open items, restated.**
1. **What replaces `nuc11_interleaved`** on Q_β / m_n / Δ_pn — owner decision.
   Now has at least one reading-3-admissible candidate in the corpus's own
   family, and is **no longer** constrained to odd dressings.
2. Superseded twice over: first by the length reframing, now by the reading
   correction. The letters are not where the live constraint sits — `χ_(2,1)` is.
3. Whether the bar-odd hypothesis survives the move to `z_D` — untouched.


## 2026-09-14 — what DOES fix the budget: the corpus's own cost function. It selects k = 0 (or 1), never the live 11.

The correction above leaves the budget question OPEN rather than answered —
reading 3 admits every dressing count. **The answer was already in the corpus.**

**The selection principle, from the Lean.** `FrobeniusSelected B y cands cost w`
= `w` is reading-3-feasible **and** `cost w ≤ cost w'` for every feasible
candidate, with the corpus instantiating `cost = fun w => (w.length : R)` — the
**crossing count**. That is exactly how `frobeniusSelected_borromean` picks the
6-letter core. So the budget has a derived answer: the minimal-cost
reading-3-feasible dressing.

**Measured** (all generator assignments × all dressings, 4144 words):

| k | length | parity | reading 3 (p) | reading 3 (n) | reading 1 (p/n) |
|---|---|---|---|---|---|
| 0 | 9 | odd | 4/8 | 4/8 | **0/0** |
| 1 | 10 | even | 18/48 | 18/48 | **0/0** |
| 2 | 11 | odd | 149/288 | 145/288 | **0/0** |
| 3 | 12 | even | 594/1728 | 594/1728 | **0/0** |

1. **Minimal cost selects `k = 0`** — the empty dressing is reading-3-feasible
   (4/8, both nucleons), so the cost-minimal word is the **9-letter** core+quark
   with **no gluon crossings**.
2. **Excluding the empty dressing gives `k = 1`, still not 2.**
   `frobeniusSelected_nil` records that the crossing-count cost makes the empty
   word trivially selected — which is why the core selection restricts to
   non-zero vertex powers. Whether the same exclusion applies to the dressing is
   an **unstated modelling choice**. It does not rescue 11.
3. **So the live `nuc11_interleaved` (k = 2) is cost-minimal under NEITHER
   convention.** That is a second, independent reason the scored element is not
   what the ruling produces — the first being its `(2,1)` failure.
4. **The principle fixes the BUDGET, not the WORD.** At k = 0 four assignments
   tie, carrying **two** distinct traces per nucleon (p `0.6121259628` /
   `0.6263353681`; n `0.4830505246` / `0.4902320181`). `cost_eq` gives equal
   cost, not a unique word. A 2-fold degeneracy survives and is **not** closed.

**🛑 And this corrects my own correction, one level down.** The entry above says
reading 1 would empty the selection *by parity* (all corpus nucleon models are
odd). Measured, **reading 1 admits ZERO words at every k — including k = 1 and
k = 3, which are EVEN total lengths that `alt_psd_iff_even` permits.** The
`(2,1)` block excludes those independently of parity. So reading 1 is
annihilating **outright**, and the parity theorem is not the binding constraint
even where it applies. The parity result is still true and still the clean
structural statement for odd lengths; it is simply not what does the work.

Probe: `computations/qbeta/qbeta_cost_minimal_budget_under_reading3_probe.py`
(7/7, proton pin, convention D, 60 dps).

**Not claimed, deliberately.** That `k = 0` should be adopted — that is an owner
call and it hangs on the unstated empty-dressing convention. That the
crossing-count cost is the right cost for the *dressing* (extending the core's
cost to it is an extrapolation of the principle, not a theorem about it). **No
Q_β residual was computed for any of these**, precisely so the selection cannot
be contaminated by proximity to the measured value. The dashboard stays
un-re-scored.


## 2026-09-14 — 🟧 OWNER OBJECTION: crossing COUNT is the wrong cost. Measured — and it changes the answer.

Owner, verbatim: *"The selection rule shouldn't be minimum crossing... It may be
higher energy than a non-minimal crossing. A sibling has worked on connecting
hecke energy to O'Hara energy via brings embedding. Can we compare that as a
selection principle... You're minimizing not just the hecke energy but how the
knot is embedded into brings surface."*

**The objection holds, measured.** Probe
`computations/qbeta/qbeta_crossing_energy_separates_the_gluon_probe.py` (7/7).

**Part 7's verdict is right and is about γγ words.** `E_cross(k-vertex γγ word)
= k·h` exactly (reproduced), so there energy is *proportional to* count and
swapping the cost changes nothing; `E_cross(empty) = 0` sits below every
non-empty γγ word, which is the degeneracy that retired the functional.

**The gluon is not a γγ word, and there the two costs DISAGREE:**

| gluon | \|G\| | reading-3 | `E_cross` | Q_β MeV | vs CODATA |
|---|---|---|---|---|---|
| (empty) | 0 | no | 0 | 0.5457 | −30.25 % |
| σ₁ | 1 | **yes** | **+1.10998** | 0.5111 | −34.68 % |
| **σ₁⁻¹** | 1 | **yes** | **−0.90092** | 0.3970 | −49.26 % |
| σ₀σ₀ (live) | 2 | no | +2.21996 | 0.6519 | −16.68 % |
| σ₁σ₀ | 2 | yes | +2.21996 | 0.6822 | −12.80 % |
| **σ₀σ₁** | 2 | yes | **+2.21996** | **0.3357** | **−57.09 %** |
| σ₁σ₁ | 2 | yes | +2.21996 | 0.6525 | −16.60 % |

1. **Count ties σ₁ and σ₁⁻¹ at 1; energy strictly prefers σ₁⁻¹.** A negative
   crossing carries negative energy, which no count can see. The choice of cost
   is a real decision, not a formality.
2. **The degeneracy dissolves here.** `E_cross(empty) = 0` but `σ₁⁻¹ < 0`, so
   the empty word is *not* the energy minimum. γγ words are sign-**balanced** by
   construction and never offer a bare negative crossing; the gluon does. Part
   7's verdict does not transfer, and the functional is **usable** on the gluon.
3. **🛑 But it is a letter-sum, so it is order-blind — and that is the sharp
   part.** `σ₁σ₀` and `σ₀σ₁` tie **exactly** at `2q`, while their Q_β differ by
   a **factor of two** (0.6822 vs 0.3357 MeV). The observable depends on the
   ordering and the functional cannot see it. All three feasible 2-crossing
   gluons tie at one energy.

**So the owner's proposed direction is the right class of fix**, and for the
reason point 3 exposes: an embedding energy is *not* a letter-sum — it is
order-sensitive and can rank a longer word below a shorter one.

**What exists / what is missing (searched `computations/`, `tools/`):**

- **Exists** — `mobius_cross_energy_hopf_calibration.py`, calibrated against the
  **proved** `E(Hopf) = 2π²` (Agol–Marques–Neves, arXiv:1205.0825); a Borromean
  companion; `QOU.MobiusEnergy` with a categorical `E_cat` from the
  Frobenius–Hopf comultiplication and the encoded `E_cat = ¼·E_classical +
  const`; Bring period-matrix / mapping-torus-residue machinery. Beans `qou-zfs6`
  (Möbius invariance / FHW bound / minimiser as Lean gates) and `qou-dux3` are
  `completed`.
- **Missing** — **any map from a braid word to a curve in or on the Bring
  surface.** The integrators consume hand-parametrised *named* embeddings (Hopf,
  Borromean). An absence on the surfaces searched, not a proof of absence.
- **Caveat** — `MobiusEnergy.lean` carries **2 sorries**, and its own header
  records a prior vacuity incident in which `classicalLimit` made `E_cat` blind
  (`E_cat = 1 + const` for every knot) *with no `sorry` to flag it*. That leg
  cannot bear weight unexamined.
- **The hard part** — Möbius energy is a property of an **embedding**, not a knot
  invariant; the invariant is the **infimum** over the isotopy class. So a bridge
  needs either the minimiser (FHW) or a **canonical** embedding — which is
  exactly what the Bring surface would supply. That is the research content, not
  a wiring job.

**Nothing adopted.** σ₁⁻¹ is not selected — that would swap one proxy for
another, and point 3 shows the energy does not separate what remains. The Q_β
column is a reported consequence, never an input to an ordering.


## ILP does NOT escape the S4 relative-interior exclusion (2026-09-14)

Owner asked to "make sure you are doing ILP". Checked, and it is excluded —
for a proved reason, not a failed search. Probe
`computations/meson/operator_selection_ilp_does_not_escape_s4.py` (9/9, exact
sympy over Q, emits no witness per qou-pb1w); Lean
`QOU/QBeta/IntegralityDoesNotEscapeRelativeInterior.lean` (7 decls, sorry-free,
lean-direct exit 0).

**The escape was real and had to be closed.** S4 (`qou-v7qj`) excludes every
linear objective from selecting B_3 by the FACE argument — extrema on a face,
so a relative-interior minimiser is constant. That is a statement about a
CONVEX POLYHEDRON. An ILP's feasible set is not convex; the governing object
is the integer hull `conv(P ∩ L)`, whose faces need not be faces of `P`, so a
relative-interior point of `P` genuinely can be a vertex of the integer hull.

**Reading 1, over Z^6 — B_3 is not feasible at all.** Its NF coordinates are
Z-Laurent polynomials in q at q_0 and are not integers; worst coordinate (L+)
is 0.0456 from Z. Stronger and cheaper than S4's negative: not "no objective
picks it out" but "it is not in the set".

**Reading 2, over Z[q_0,q_0^-1]^6 — that is not a lattice, it is DENSE.** For
real q > 1, Z[q] is discrete in R iff q is Pisot (classical); the smallest
Pisot number is the plastic number 1.3247... (Siegel 1944); q_0 = 1.10998 is
below it. A dense feasible subset has the same closed convex hull, so the
integer hull adds no faces. Made constructive: [A6] exhibits a feasible
lattice point beating B_3, 0.8642 against 0.9986.

**The Lean strengthens rather than restates S4:** convexity was never what the
face argument used. `linear_min_two_sided_kills_direction` gets `f d = 0` over
an ARBITRARY set S from two-sided reachability and linearity alone. So an ILP
cannot escape by non-convexity; it could only escape by the lattice being
COARSE near the point, which density rules out.

**Unconditional — does not need q_0 irrational** (which this corpus cannot
prove; q_0 is pinned through Vol(4_1) = 2 Cl_2(pi/3)). All three cases give
density; only q_0 in Z is discrete, and 1 < q_0 < 2. The Pisot test needs no
decimal expansion of theta: x^3-x-1 is increasing on (1,oo), so q_0 < theta is
exactly the sign of q_0^3 - q_0 - 1 — proved as an iff in §3 of the Lean.

**Correction made in the writing, worth keeping:** the ring is Z[1/(p*r)], NOT
Z[1/r] — q_0^-1 = r/p puts powers of p in denominators, and B_3's own
coordinates carry 192- to 479-digit denominators for that reason. The first
run tested membership against Z[1/r] and FAILED [A6] on a point plainly in the
ring. The false negative was indistinguishable from a real one.

**SCOPE (b)**, structural, invariant cited: the Pisot bound for reading 2,
non-membership for reading 1. It excludes LINEAR objectives over these
lattices. It says nothing about non-linear principles (S4 refuted two
separately) and nothing about other elements.

**Still open, unchanged:** what replaces `nuc11_interleaved` after the
2026-09-13 reading-3 whole-word ruling rejected it on (2,1). That is an owner
decision and this prune narrows the search without answering it.


## TOWER (2026-09-15): the H_3 ILP answer was a truncation artifact

Owner: *"Have O'Hara on the full tower.... I suspect the longer words (which are
from gamma gamma production are higher in tower), only do order 0 when we need
the observables."* Confirmed, and worse than stated: **the H_3 probe could not
SEE the gamma-gamma operator.**

`GammaGammaH6Interface.lean:37` records the gamma-gamma-produced bond as
`(sigma_2 sigma_3^-1)^m` -- generators 2 and 3, i.e. **H_6**. My ILP alphabet was
`{sigma_0, sigma_1}` = H_3, so that operator is outside the catalogue at EVERY
length, and reading 3 was evaluated in the wrong algebra (3 blocks, not 11).

`computations/qbeta/qbeta_knot_operator_ilp_h6_tower_probe.py` (6/6):

* **Convention D IS the two-row truncation**, exactly: `y_lambda > 0` iff the
  partition has <= 2 rows. At H_6 that is (6), (5,1), (4,2), (3,3) -- FOUR of
  eleven bind. The H_3 rule `y_(1^3) = 0` is the n = 3 case of the same fact.
* **The gamma-gamma bond is INFEASIBLE at m = 1, 2 and FEASIBLE at m = 3**
  (E = 3.0990) -- the same `3 | k` pattern as the vertex-power family.
* **The decisive table**, at FIXED length (a mixed-length argmin is vacuous by
  `PairEnergyRewardsShort.pairEnergy_singleton_le`):

      len   H_6 feas   H_6 min         H_3sub feas   H_3sub min      same?
        1         10   0.0                       4   0.0             yes
        2         68   0.1629153512              8   0.9156174644    NO
        3        551   1.1261598926             62   1.2414481668    NO

  At length 2 the H_3 answer is **5.6x worse** than the true optimum. The H_6
  winners `s0is2i` and `s0s1s3` use generators an H_3 catalogue cannot express.
  The previously reported `1.2414 / s0is0is1i` is **RETRACTED as an artifact**.

Precision: `chi_lambda_braid_mpf` at 60 dps, NOT
`mass_at_3A_proper.chi_lambda_of_word`, whose own docstring says "This is a
float64 kernel, and the return annotation is the contract".

Landed on `claude/lp-dual-radical-formalize-first-2026-09-14` (PR #7399) as
commit `9078329dd68`.

**Still open (unchanged):** what replaces `nuc11_interleaved`. The H_6 table
says which operator the ILP selects at each fixed length; it does not settle the
element, because the reading-3 + PSD-3 whole-word criterion is the owner's and
five of `nuc11_interleaved`'s eleven letters remain census-derived.

## 2026-09-14 — the owner's proposed cost is the one it replaces: crossing ENERGY = crossing COUNT + a writhe term

The section above records the owner's objection to crossing count as the
selection cost, and measures that crossing energy disagrees with it on the
gluon. It left open **when** they disagree. Answered exactly, and from the
corpus's own decomposition rather than a new principle.

**The structure is already in the tree.** `QOU.Braiding.crossingEnergy p m q =
p·q − m·q⁻¹` splits (`crossingEnergy_split`,
`lean/QOU/Braiding/crossing_energy_channels.lean`) into

    symChannel  = (p − m)·(q + q⁻¹)/2      multiplicity = the WRITHE
    asymChannel = (p + m)·(q − q⁻¹)/2      multiplicity = the COUNT

and the writhe is a braid invariant while the crossing count is not. Every
result below is that one asymmetry.

**THE LEAN** —
`lean/QOU/Mass/CrossingEnergySelectionEqualsCount.lean`, 9 theorems,
sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, `#print axioms` clean
on all nine (`propext, Classical.choice, Quot.sound` only):

* `energy_le_iff_count_le_of_writhe_eq` — at fixed writhe the energy ordering
  and the count ordering are **the same ordering**, as an `iff`. Swapping the
  cost changes **no** selection inside a fixed-writhe family.
* `crossingEnergy_sub_eq_writhe_term_of_count_eq` — at fixed count the two
  energies differ by exactly `(W₁ − W₂)·symmetricWeight q`.
* `crossingEnergy_lt_of_cancelling_pair` — a cancelling pair leaves the braid
  element alone and strictly raises the energy by `q − q⁻¹ > 0`.

**THE MEASUREMENT** — `qbeta_crossing_energy_is_count_plus_writhe_probe.py`,
8/8, 60 dps, proton pin, convention D:

| check | result |
|---|---|
| `E_cross = n₊·h + W/q` on 11 candidates | exact, `< 1e-50` |
| `tr_M` over all 10 cyclic rotations of the 11-letter word | max deviation `1.55575e-61` |
| `tr_M` with the gluon **prepended** instead of appended | delta **exactly 0** |
| `tr_M` with `σ₁σ₁⁻¹` appended | delta **exactly 0** |
| `E_cross` under that same insertion | `+h = 0.20906029879563931543` exactly |
| equal-writhe ordered pairs, orderings agree | **9 / 9** |
| differing-writhe pairs where the costs disagree | 20 of 46 |
| the sibling's headline `σ₁` vs `σ₁⁻¹` gap | `2.0108968667071222998` = the writhe term exactly |

**THREE CONSEQUENCES.**

1. **The objection to the count is not answered by the energy.** Crossing energy
   *is* crossing count plus a writhe correction. It re-ranks candidates **iff**
   their writhes differ, never otherwise — so the measured disagreement the
   sibling probe found (`σ₁` vs `σ₁⁻¹`, tied at count 1) is a writhe difference
   and is the *only* kind of disagreement available. **A genuine upgrade must be
   a functional that is not a function of `(n₊, n₋)` at all.** An embedding
   energy is exactly that, which is the structural reason the owner's direction
   is the right class rather than an analogy. It remains unbuilt.

2. **The cost is a WORD functional; the observable is a BRAID-ELEMENT one.**
   Inserting a cancelling pair leaves `tr_M` exactly unchanged and raises
   `E_cross` by `h`. So `E_cross` ranks two presentations of one object
   differently while the thing being predicted ranks them identically. That is
   an admissibility problem for any letter-sum cost, independent of which one.

3. **A free prune on the candidate set.** `tr_M` is cyclic, so a *contiguous*
   gluon's **position** in the word is not a degree of freedom — prepended and
   appended give the identical trace. Only genuinely non-contiguous
   interleavings differ. Nothing in the corpus was relying on the placement, but
   it narrows what an enumeration has to cover.

**WHAT IS NOT CLAIMED, and one thing explicitly NOT measured.** Neither cost is
adopted or retired; no candidate is selected; **no Q_β is computed in the
probe at all**, deliberately — a target that is never evaluated cannot be
selected on. The converse of consequence 1 is **not** claimed: a
differing-writhe pair may still agree, and 26 of the 46 do. What is established
is the one-way implication, which is what bounds the upgrade.

**🛑 RETRACTED, same session — my "incidental finding" was a re-derivation, and
bean `qou-hv27` had it first, better.** I wrote here that the sweep's
`UNVERIFIED — missing olean` on `QOU.Braiding.crossing_energy_channels` was a
new discovery contradicting AGENTS.md, having measured root 3480 vs paper 2337
mathlib oleans. `qou-hv27` (**completed 2026-09-07**) records the same asymmetry
with a **sharper mechanism** and a **better repair**:

* **Mechanism.** It is not that the paper tree is short — it is that a *partial*
  tree **shadows** a complete one, and the sweep's `LEAN_PATH` ordering decides
  which. Lean commits to the first root containing the module's top-level
  namespace directory and never falls through (`qou-tpdg`). My framing missed
  this entirely.
* **Repair.** `cp -rln` — **hardlinks, zero disk cost**. I used plain `cp` for 94
  files on a container already at 93 % full. Strictly worse, for no benefit.

**How I got here is the instructive part.** I ran the six-path corpus-grep for
the bean's *subject* and not for my own *incidental* observation, which is
exactly the gap path 6 exists to close — a prior agent's conclusion sitting in a
bean before it reaches any other artifact. A finding noticed in passing needs
the checklist just as much as the one you went looking for.

**What survives, and it is small:** AGENTS.md's own text still describes this
UNVERIFIED class as the cache branch being short, "absent from the **paper and
root trees alike**", which is not what either measurement shows. That wording is
worth correcting against `qou-hv27`, and it is a docs fix rather than a finding.

**And the limitation it caused is now gone.** Applying `qou-hv27`'s documented
per-session repair (it does not survive a fresh container), the sweep gate runs
the new module properly: **2 ok, 0 RED, 0 UNVERIFIED** — dependency rebuilt from
source, not linked from a snapshot. So the verification below is the sound gate,
not lean-direct against an olean whose source I had to argue was unchanged.

**Open items unchanged.** Item 1 (what replaces `nuc11_interleaved` on the three
L2 rows) is still the owner's decision and is untouched here. Item 3 (whether
the bar-odd hypothesis survives the move to `z_D`) is untouched. This narrows
the cost question that superseded item 2; it does not close it, because the
functional the argument points at is not built.

### Same day, the closing move: the energy's only ADMISSIBLE form *is* the count

The section above shows the energy is a **word** functional. A word functional
has exactly one canonical descent to the object — its extremum over the fibre —
and here that extremum is computable, because the writhe is constant on a braid
class while the count is not. `crossingEnergy = symChannel(W) + (p+m)·(q−q⁻¹)/2`
with `W` invariant and `q − q⁻¹ > 0`, so:

**`isLeast_energy_iff_isLeast_count_of_writhe_eq`** (sorry-free; the file is now
10 theorems, `lean`-direct exit 0, `#print axioms` clean on all of them) — over
any finite family of presentations sharing a writhe, which is what a braid class
is, **the energy-minimal presentation is exactly the count-minimal one.**

So making the energy admissible turns it **into** the crossing-count cost it was
proposed to replace, up to an additive invariant. That closes the "energy
instead of count" proposal as posed, rather than merely bounding it.

**And the proposed replacement inherits the same defect.** Checked directly:
`QOU.MobiusEnergy.ClassicalMobiusEnergy` is a functional of an **embedding**,
and its own docstring says so — *"this structure holds no isotopy-class data"*.
So as encoded it is no more a braid-element invariant than `E_cross` is, and
swapping it in would swap one presentation-dependent cost for another.

**This is what makes the Bring embedding load-bearing rather than an
implementation detail.** What repairs an embedding functional is either the FHW
minimiser (the infimum over the isotopy class — bean `qou-zfs6`) or a
**canonical** embedding, and the Bring surface is the candidate canonical
embedding. The owner's instinct that the Bring half matters is therefore right
for a sharper reason than "it is where the geometry lives": without it the
proposal does not clear the admissibility bar its own objection implies.

**Caveat carried forward, not re-derived:** `MobiusEnergy.lean` has 2 sorries
and its header records a prior vacuity incident in which `unknot_iff` read
`value = 4 ↔ True`, forcing `value = 4` for every instance and making `E_cat`
blind to the knot, with no `sorry` to flag it. That leg cannot bear weight
unexamined — the observation above is about the structure's *arity*, which is
visible from the docstring and is unaffected by the sorries.

### 2026-09-14, ~1 h later — 🛑 my "it remains unbuilt" went STALE while the PR was open, and a sibling reached the same exclusion by a different invariant

The entry above ends by naming the open target: *"a genuine upgrade must be a
functional that is not a function of `(n₊, n₋)` at all... An embedding energy is
exactly that... It remains unbuilt."* **Three commits landed on `main` between
18:34 and 19:10 that make that false**, and the convergence is worth recording
rather than quietly deleting.

**What landed** (branch `claude/lean-crossing-budget-invariants-2026-09-14`,
PR #7391, now closed):

* `380f5935c2` — **`QOU/QBeta/LetterSumBlindness.lean`**, sorry-free.
  `letterSum_perm_invariant`, `no_letterSum_separates`,
  `crossingCount_perm_blind`, **`crossingEnergy_perm_blind`**,
  `factorsThrough_blind`, plus a scope lemma
  (`objective_blindness_does_not_transfer_to_constrained_optimum`) delimiting
  the exclusion so it does not kill the SDP route.
* `aa224aba03` — **`QOU/QBeta/ECatBlockDecomposition.lean`** + probe
  `qbeta_ecat_pair_kernel_probe.py` (4/4): a **pair kernel** dropped into the
  `cost : W → R` socket of `GammaGammaWordSelection`, with
  `pairSum_not_perm_invariant` — a pair sum whose kernel reads the **separation**
  of the two letters escapes the letter-sum exclusion. Four distinct values over
  the four 2-crossing gluons against one value for every letter-sum.
* `27250649ff` — the per-block cost vector `t_λ`.

**The two results are COMPLEMENTARY, and neither implies the other.** Stating
this precisely because "both exclude letter-sums" invites collapsing them:

| | invariant used | what it says |
|---|---|---|
| **theirs** | permutation of letters | `E_cross` cannot **separate** two reorderings — a statement about the letter *multiset* |
| **mine** | the writhe/count channel split | `E_cross` and the count are **the same ordering** at fixed writhe; they differ by exactly the writhe term at fixed count; the energy's admissible descent **is** count-minimisation |

Permutation-blindness says nothing about how the energy *compares to the count*
across different multisets, which is my whole result. And
`crossingEnergy_lt_of_cancelling_pair` is orthogonal to both: a cancelling pair
**changes** the multiset, so permutation-invariance cannot reach it — that
lemma is about the map word → braid *element*, not word → multiset.

**Their control is my `crossingEnergy_eq_of_writhe_and_count_eq`, measured.**
With the separation weight removed, the sharp pair — *"same multiset, same
writhe, differing only in ORDER"* — reads `34.6134315674846072` for **both**, a
difference of **exactly 0.0**, against `0.91996925` weighted. That is the forced
tie my Lean states, arrived at from the other direction and used as a control
rather than as a theorem.

**What is corrected in my PR body:** "It remains unbuilt" → built, with the
citation. **What is NOT corrected:** every theorem and every measured figure in
the entry above stands; the re-verification after merging `main` (69 commits) is
**2 ok, 0 RED, 0 UNVERIFIED**.

**What their own commit message declines to claim, carried here so it is not
lost downstream:** the discretisation is **not** `E_cat` (whether its continuum
limit is `E_cat` is unproved), **nothing selects a word** — *"a cost that
separates is a precondition for selection, not a selection"* — the per-block
`t_λ` is proved a refinement but **not computed**, and the `MobiusEnergy`
classical-limit leg stays assumed with its blindness incident unretired
(`qou-pzsi`). So the open item is narrower than before and is **not** closed:
a separating cost now exists; **which** cost, and whether minimising it is
legitimate, is untouched.

**Coordination note.** I posted intent on #7391 at 18:44 naming my distinct
angle; it landed ~30 min later. That is the sanctioned research-overlap pattern
working as intended (AGENTS.md §Parallel exploration) — two routes, one
exclusion, neither re-deriving the other. Converging per that rule: I do not
re-derive their pair kernel, and this bean cites it.

### 2026-09-14 21:46–22:29Z — the classical-limit BRIDGE FIELD is vacuous, and an attribution correction

Two cross-branch notes landed on #7390. Both verified here rather than taken.

**1. `MobiusEnergy.classicalLimit` constrains nothing** (reported by #7262;
checked at the structure, not at their theorem, because it is **not on `main`**):

```lean
classicalLimitConst : ℝ
classicalLimit : energy = (1 / 4) * classicalEnergy.value + classicalLimitConst
```

`classicalLimitConst` is a **free field of the same structure**, so for any pair
`(energy, classicalEnergy)` exactly one `k` satisfies it — the field relates the
two energies **not at all**. #7262 proves it sorry-free as
`classicalLimit_unconstraining` / `classicalLimitConst_eq`, on that branch only;
the structure field is checkable on `main` today.

**This compounds with the entry above rather than repeating it.** That entry
established `ClassicalMobiusEnergy` is a functional of an **embedding** (its own
docstring: *"this structure holds no isotopy-class data"*). Now the **bridge**
field is vacuous too. So there are **two independent reasons** the
classical-limit route cannot bear weight: the functional is of a presentation,
and the field that would connect it to `E_cat` asserts nothing. It is also the
same defect class as the header's recorded incident (`unknot_iff : value = 4 ↔
True`) **one field over** — a structure whose constraint is discharged by a free
companion field, with no `sorry` to flag it. Not repaired: §ASK THE OWNER,
neither exemption applies.

**2. An attribution correction, made because the commenter said they would cite
it.** #7262 credited `blockCost_can_separate`, `pairSum_not_perm_invariant`,
`bridgeClass_perm_blind` and `qbeta_ecat_pair_kernel_probe` to #7390. **All four
are #7391's** (`aa224aba03` / `380f5935c2`, both on `main`). Measured: this
branch's `git diff --name-only origin/main...HEAD` is exactly four files — the
bean, the probe, its witness, and
`QOU/Mass/CrossingEnergySelectionEqualsCount.lean` — and none contains those
names. Cause is partly mine: `cf2cc9d011`'s body *describes* #7391's work next
to my own, which is presumably how it got attached. **Lesson worth keeping: when
a PR body summarises a sibling's landing, name the sibling in the same sentence
as the declaration, not in a heading two paragraphs up.**

**3. From #7399 — the ILP escape is closed, and it composes with this entry.**
A linear objective cannot select `𝓑₃` by the face argument (S4, `qou-v7qj`), and
the obvious reply — *"the face argument needs convexity, an integer program is
not convex"* — is measured not to escape: over `ℤ⁶` `𝓑₃` is not feasible at all
(worst coordinate `0.0456` from ℤ), and over `ℤ[q₀,q₀⁻¹]⁶` **that ring is
dense**, because `ℤ[q]` is discrete iff `q` is Pisot and `q₀ = 1.10998` sits
below the plastic number `1.3247…` (Siegel 1944); constructively a feasible
lattice point beats `𝓑₃` at `0.8642` vs `0.9986`. Their
`linear_min_two_sided_kills_direction` gets `f d = 0` over an arbitrary set from
two-sided reachability and linearity alone — **convexity was never the
load-bearing hypothesis**, so non-convexity buys nothing.

Composed with this entry: **if crossing energy IS the count, then the count is
both permutation-blind and unable to select by any linear program, integer or
not.** That is a constraint on where the selection can come from — not a problem
with the reduction.

### 2026-09-15 10:25Z — twelve `qou-99qc` commits landed overnight; what they do to this entry, checked rather than assumed

`main` moved 24 → 85 while #7390 sat open, and **twelve** of those are on this
bean. The merge conflicted on exactly the file AGENTS.md predicts — this bean —
and was resolved losslessly with the prescribed
[`scripts/bean-append-merge.py`](scripts/bean-append-merge.py) (`+16309 ch
appended`, `main` byte-for-byte preserved), not by hand.

**THE ONE THAT CONTINUES THIS ENTRY DIRECTLY.** `b7b5e3e290` adds
`QOU/Mass/PairEnergyRewardsShort.lean` (7 decls, sorry-free), stated for an
**arbitrary** kernel `K`:

* `pairEnergy_singleton_le` — under non-negativity a **1-letter word is a global
  minimiser over every word**;
* `exists_singleton_minimiser` — any catalogue containing a singleton has its
  optimum there, whatever else it holds;
* the contrapositive — **to select anything longer, the kernel must go negative
  somewhere.**

**Composed with this entry, the lesson is sharper than either half.** Mine:
minimising `E_cross` *is* minimising the count
(`isLeast_energy_iff_isLeast_count_of_writhe_eq`). Theirs: minimising a
non-negative pair energy picks the shortest word. Both say the same thing about
a different functional — **plain minimisation drives you to the degenerate short
end, so the pathology is the MINIMISATION FRAME, not the particular cost.** A
cost that *separates* (the pair kernel of `aa224aba03`) is therefore still not
enough: separation is necessary, and the selection rule must additionally not be
bare minimisation of a non-negative functional.

**An observation, marked as suggestive and NOT a theorem.** Their contrapositive
says a selecting kernel must go negative somewhere, and the table in the entry
above already *exhibits* negativity: `E_cross(σ₁⁻¹) = −0.90091828395574` and
`E_cross(σ₀⁻¹σ₁⁻¹) = −1.8018365679115` — a negative crossing carries negative
energy. **Scope: mine is a letter-sum, negative per LETTER; theirs is a kernel
on letter PAIRS.** So this is not an instance of their hypothesis, only evidence
that the corpus's own energy convention supplies the sign structure their design
constraint asks for. Do not cite it as satisfying the hypothesis.

**WHAT DOES NOT TOUCH THIS ENTRY, checked three ways rather than assumed.**
`6fb8dafe3c` reports two hazards that look like they should land on my probe —
*"the H_3 legacy path is float64"* (`atom_per_generator_volumes` warns but
RETURNS, and its `mpf` is bit-exactly a padded float64; 32 callers) and *"the
H_3 answer is a truncation artifact at every length ≥ 2"*. Neither reaches it:

1. **Import cone.** Walked all 19 modules reachable from
   `qbeta_crossing_energy_is_count_plus_writhe_probe`: `atom_per_generator_volumes`
   appears in **none**.
2. **Re-ran the probe on the merged tree — 8/8, and the witness is byte-
   UNCHANGED**, so no import-cone drift moved a number.
3. **Structurally, and this is the durable half.** Checks 1, 3, 4, 5 and 6 use
   **no `tr_M` at all** — they are algebra on `E_cross`. Checks 2 are
   *invariance* claims (cyclic rotation, contiguous-block position, cancelling
   pair), which hold for **any** trace, whatever algebra it is taken in; the
   measured `1.55575e-61` and exact-`0` deltas are what establish that `tr_at`
   *is* a trace. So **no claim in this arc depends on H_3 vs H_6** — only on
   tr_M being a trace. That was luck rather than design, and is worth stating
   explicitly so a future reader does not re-litigate it.

**Verification after the merge:** library sweep on
`QOU.Mass.CrossingEnergySelectionEqualsCount` — **2 ok, 0 RED, 0 TIMEOUT,
0 UNVERIFIED, 0 skipped** (176 s), dependency rebuilt from source.

**Also worth carrying: they caught a LAYER STRADDLE in their own measuring
script** — it rebound `q` in the character kernel but not in `_order`, whose
`word_nf` folds with `_order.H0`, so the NF was at the anchor while `χ` was at
the perturbed `q`. That produced three false claims, including a "root of
`χ_(2,1)` at `q₀` agreeing to 40 digits"; measured correctly, `χ_(2,1)(s0s1s1)`
shrinks like `10^-dps` at **every** `q` and is identically zero, with no root.
Exactly the straddle class AGENTS.md §"Never straddle the two layers" warns
about, one layer over — and it was caught by the author, not by a gate.

## 2026-09-14 (session gifted-feynman) — the Lean step `cost_eq` stops short of, and a wrong turn worth keeping

**Claim.** `FrobeniusSelected.cost_eq` says two *selected* words have equal
**cost**. The step this bean needs is the next one: that the selection predicate
can hold of **two different words**, so the rule does not determine the word.
Nothing in the corpus drew it. `QOU.Mass.CostOrderSensitivity` now does, for an
**arbitrary quotient** the cost factors through — sorry-free, `lean`-direct
exit 0 (`-DautoImplicit=false -s 65536`), `#print axioms` clean on all eight
declarations (two depend on **no axioms at all**; the rest only `propext` /
`Quot.sound`).

| declaration | statement |
|---|---|
| `minimal_transfers_along_fibre` | minimality transfers along a fibre of `π` |
| `selected_not_determined_of_cost_factors` | …so **both** words are selected |
| `lengthCost_not_determined` | the corpus's own crossing-count cost |
| `letterSumCost_not_determined` | any letter-sum cost |

**Cited, not re-derived.** The *invariance* half is already held four times
over and the file says so: `OptionELevelAcceptanceTest.monoidHom_order_blind`
(the multiplicative twin), `AltCharShiftMultiset.wordChar_of_perm`,
`YekutieliIntegration.holonomy_perm`, and **definitionally** in
`crossing-energy.lean`, which models `BraidWord := List Bool` and reads only two
counts. The letter-sum scope-(b) exclusion is already prose on `main`
(`qbeta_embedding_energy_can_discriminate_probe.py:46–52`, bean `qou-pzsi`).

**🛑 The wrong turn, recorded because it is the interesting part.** This was
first drafted around the **abelianization** — *"a cost factoring through
`B_n^ab ≅ ℤ` cannot separate two words of equal exponent sum"*. **That framing
is wrong for its own targets.** `B_n^ab` records only `e = n₊ − n₋`, so of the
corpus's own three crossing-energy components only `baseline` (the writhe)
factors through it. **Crossing count `n₊ + n₋` does not** — and it is
`FrobeniusSelected`'s *only* instantiation in the entire corpus — and neither
does `E_cross = n₊q − n₋q⁻¹`. An abelianization-quantified theorem would have
claimed a family it provably does not cover: the `da-arity-conflation` shape.
The right invariant is the **multiset** (equivalently `List.Perm`), strictly
coarser, and it is what the sibling probe already names. **Caught by the
corpus-grep checklist before anything was committed** — paths 1–6 with the
claim SHAPE rather than the topic, which is exactly the case §"Grep the claim
SHAPE" exists for.

**Scope, deliberately narrow.** It does **not** prove a selection cost must be
order-sensitive — blindness *precludes separating these candidates*, it does not
*force* a replacement to see order. That caution is this bean's own (~line 1100)
and is restated inside the file so the theorems are not read as more than they
are. It does **not** exhibit a rearrangement pair inside the live `cands` that
is also feasible; that stays a measurement. It proposes **no** replacement cost
and re-scores **nothing**.

**What this leaves as the live open item** is unchanged and is `qou-pzsi`: there
is still **no map from a braid word to a curve in or on the Bring surface**, so
the order-sensitive functional the owner's objection points at has nothing to
consume. This result says what any replacement must have (it must not be
constant on the multiset); it does not supply one.

## 2026-09-14 (session gifted-feynman, 2) — my retraction was HALF wrong: the abelianization is right for the EMBEDDING

The entry above retracts an abelianization framing as *"wrong for its own
targets"*. That retraction is **correct for costs and wrong one step over**, and
a sibling's merged bridge is what shows it.

**The claim.** `qbeta_bring_ohara_bridge_probe.py` (7/7, merged #7374) sends a
braid word to a cusp-torus lattice class

    (m, ℓ) = (exponent sum, strand count)

— verified at source, `:36-37` and `:65`, and again at `:343-344`
(`m = BASE_WRITHE + writhe(g)`, `ell = STRANDS`). **`m` is exactly the
abelianization**: `e : B_d → ℤ`, `σ_i ↦ 1`, induces `B_d/[B_d,B_d] ≅ ℤ`
(Black–Samson, `library/black-samson-phd2010sp/…/sec-008-12-summary-of-thesis.md:126`),
and `ℓ` does not depend on the word at all.

**So the same quotient under-prunes on one side of the pipeline and
over-collapses on the other.** Against the *cost* functions it is too coarse to
bite — crossing count `n₊ + n₋` and `E_cross = n₊q − n₋q⁻¹` both survive it,
which is why the retraction stands. Against the *embedding map* it is precisely
what the corpus does, and it is **strictly coarser than the multiset**, so it
loses strictly more.

**Consequence for the Lean.** `selected_not_determined_of_cost_factors` is
quantified over an **arbitrary** quotient `π`, so it covers this instance with
no change: put `π = (writhe, strands)` and the sibling's measured negative —
all four two-crossing gluon dressings share one class, one geodesic and one
energy — is an instance of the general theorem rather than a separate fact.
The docstring now records this beside the retraction.

**The reusable lesson is about attachment, not about the invariant.** "X is
blind to Y" is a claim about a *particular map*; carrying it to a neighbouring
map in the same pipeline is not a corollary. I made that error in one direction
and would have missed the true instance in the other.

**Nothing re-scored, nothing selected.** The sibling's own scoping stands: the
bridge does not select, the dashboard rows stay un-re-scored, and the
`u = ln q₀` vs `u = 2 ln q₀` meridian-normalisation binary stays open with
neither branch adopted.


## 2026-09-14 (session gifted-feynman, 6) — the replacement my theorem demanded HAS been built, by a sibling; I am not re-deriving it

My entry above ends: *"This result says what any replacement must have (it must
not be constant on the multiset); it does not supply one."* **A sibling
supplied one, and it is on `main`.**

`claude/99qc-crossing-budget-parity-2026-09-14` (PR #7390), commits
`380f5935c2` / `aa224aba03` / `27250649ff`:

* `QOU.QBeta.ECatBlockDecomposition.pairSum_not_perm_invariant` and
  `blockCost_can_separate` — a **pair kernel** in the cost socket, with the
  O'Hara `1/d_arc²` separation weight doing the work;
* `qbeta_ecat_pair_kernel_probe` (4/4), run here against the merged tree: four
  distinct proton values over the four gluon dressings
  (`8.68872560885`, `7.76875635932`, `8.89780952920`, `9.06507666548`) against
  **one** value for every letter-sum, and a control showing the sharp pair
  separating by `0.91996925` weighted against **exactly 0.0** unweighted.

**It escapes MY quotient, not only permutation — and that composition is
already measured, so there is nothing for me to add.**
`LetterSumBlindness.bridgeClass_perm_blind` is exactly the
`(exponent sum, strands)` map my own entry identified as the corpus's
embedding map; all four candidates sit at **writhe +2, length 2**, one fibre
of it; the kernel separates them. That is assertions 1 and 2 of their probe.

**Deliberately not re-derived.** Per the convergence rule the second route
verifies and cites. I added no companion lemma; `CostOrderSensitivity.lean`
gains a docstring section recording the finding and the credit, nothing more.
Their commit's own account of the complementarity is correct: theirs turns on
**permutation** of letters, mine on the **writhe/count split** at fixed
writhe, and neither implies the other.

**What stays open is narrower, not closed**, and their assertion 4 scopes it
themselves: the kernel is a **discretisation**, its continuum limit is not
proved to be `E_cat`, and the classical-limit leg it would need is *assumed*.

**That leg is worse than assumed, and I proved it this session.**
`CategoricalMobiusEnergy.classicalLimit` has `classicalLimitConst` as a **free
field of the same structure**, so it is satisfiable for any pair of energies by
exactly one `k` — `QOU.MobiusEnergy.classicalLimit_unconstraining` and
`classicalLimitConst_eq` (sorry-free). So a future agent cannot close the
continuum-limit question by appealing to that field. Reported on #7390;
**not repaired** — §ASK THE OWNER applies and it stays an owner decision.

**The replacement ELEMENT is still an owner call.** None of this selects a
word. Their own declined claims stand (not `E_cat`; nothing selects a word;
`t_lambda` not computed), and this bean's first open item — what replaces
`nuc11_interleaved` after the confinement-SDP reading-3 rejection — is
untouched by all of it.


## 🛑 Citation correction 2026-09-26 (bean `qou-6moa`) — the reading is unaffected

This bean cites `markovWeights_eq_jones_of_threeRow_eq_zero` for the claim that
under convention D the three-row weight vanishes. **That lemma proves the
converse.** Read its signature (`BraidsAndKnots/MarkovTraceTLUniqueness.lean:119`):
`hTL : y₁₃ = 0` is a **hypothesis** and `z * (q + qi) = q ^ 2` — convention D — is
the **conclusion**. So it gives TL ⟹ D, which is the direction
`docs/coordination/trace-convention-registry.json:173` correctly cites it for.

It also carries `hfaith : y₂₁ ≠ 0`, and that is load-bearing rather than
decorative: the sibling `markovWeights_degenerate_root` (`:154`) proves that
dropping it makes the conclusion **false**, not merely unprovable — the trivial
character `y = (1,0,0)` at `z = q` satisfies all three moment equations and gives
`q·(q+qi) = q² + 1 ≠ q²`. A lemma that *assumes* a form of faithfulness on the
two-row block cannot be evidence about the three-row block vanishing.

**Cite instead**, matching the frame:

| lemma | typeclass | scope |
|---|---|---|
| `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (`:142`) | `[Field R]`, sole hypothesis `q²+1 ≠ 0` | general `n`, on the actual Ocneanu weight |
| `QOU.BraidsAndKnots.FibreDimensionForcesTL.threeRow_eq_zero_of_jones_ocneanu` (`:179`) | `[CommRing R] [IsDomain R]`, division-free | `n = 3`, same variable frame |
| `QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` (`:368`) | `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` — **an ordered field** | `n = 3`, archimedean only |

The third is the wrong citation at any §7c generic-`R` site.

**Nothing in this bean's conclusions changes** — only the authority cited for one
step. Measured: the reversal is a class of 14 across 9 files against 49 correct
citations, and 3 further files carry the same assertion with no lemma named at
all, so a grep on the identifier cannot find them. Full per-site table and blast
radius on `qou-6moa`; fixed so far in AGENTS.md and
`QOU/Mass/AltCharShiftMultiset.lean` (PR #7459).


## 2026-10-10 — the energy / O'Hara selection principle, route 1: what an embedding energy can and cannot select

Full entry on `qou-pzsi`; probe `computations/probes/ohara_link_energy/`.

- **The 2-crossing gluon dressings close to two links, not four.** `gluon_s0_s1` ≅ `gluon_s0_s0` = `nuc11_interleaved`, and `gluon_s1_s0` ≅ `gluon_s1_s1`, by hand-checked braid conjugacy. Any closure or embedding energy therefore ties the live element with `gluon_s0_s1` by construction.
- **Flowed link Möbius energy (upper bounds, multi-start).** It ranks `nuc9` (234.2) well below both dressing classes (≈291), which sit well below `gen_grouped` (>311). It does **not** separate the two dressing classes: the gap is 1.1 against a combined error of 1.2.
- **So the owner's 2026-09-14 direction is confirmed as the right class.** The energy is order-sensitive where letter-sums are not. But on this candidate set it **cannot pick among the gluon dressings**, and it cannot see the letter decoration at all.
- The gluon dressing stays unselected. No dashboard row was re-scored.

## 2026-10-11 route 2 status

- The gluon tail is ALLOWED (owner ruling, 2026-10-11).
- The q-deformed recipe uses t = −q₀ (owner ruling). PR #7647 merged; it gives no ranking.
- Option 1, ropelength on fresh 11-letter words, FAILED its pre-registered test (24-way tie). PR #7651 merged.
- Option 1b pre-registers a same-loop-up-to-symmetry rule on fresh 13-letter words (branch claude/bring-route2-sameloop-2026-10-11).
- No word is selected by route 2.

**2026-10-11 (route 2, options 1b/1c, PRs #7672 merged, #7679).** On fresh 13-letter words: 316 classes = 33 braids; the shortest Bring loop carries 3 braids (88 spellings of one), so Bring-loop energies select loops, not words. The owner-ruled q-length at t = -q0 separates braids: alone it picks sigma0*Delta^4 (length ln q0, no Bring loop); Bring-loop-first picks a different braid. Contaminated read-across to the seen candidates: rule A -> nuc11_interleaved (the scored element), rule B -> class A. The two rules disagree; which (if either) is the selection principle is an OPEN owner decision. Nothing selected. Bean stays open.

## 2026-10-11 — option 1d (11-letter, all 94 classes; PR #7679, 007720dbbf)

Pre-registered rules on all 94 positive 11-letter word classes (16 braids). Rule A (q-length at t=−q₀ alone) picks the braid of nuc11_interleaved (parabolic, E_q = ln q₀, no Bring loop). Rule B (shortest Bring loop, L = 4.6031833095, then q-length) picks the braid of class A (gluon_s1_s0/s1_s1, E_q = 2.6496). Both decided, they disagree; contaminated (seen q-lengths known beforehand). The selection rule remains an OPEN owner decision — this bean stays open.

## 2026-10-11 — CORRECTION: route 2 used sign-erased candidates (results_signed.md)

Route 2 and options 1 through 1d (and route 1, ohara_link_energy) took the seen candidates from the sign-erased generator list in qbeta_candidate_closures_are_links_probe. The canonical nucleon (pyhecke.atom.build_nucleon_nf) has a (σ₀σ₁⁻¹)³ core and averaged ud letters, so it is a SUM OF FOUR BRAIDS. Under route 2 every proton term has a Bring loop (L = 9.21 / 15.94 / 6.37 / 20.44), whereas the sign-erased nuc11 is parabolic with no loop. Every seen-candidate read-across from route 2 is WITHDRAWN, including 1d's "Rule A → nuc11, Rule B → class A". The fresh-positive-word results stand. γγ words (σ₀σ₁⁻¹)^k never get a Bring loop under route 2's "exactly one fixed point" rule: this is a limit of the rule (3 ∤ k: no conjugate of Γ₀(2) contains the word; 3 | k: the word is pure, so all three conjugates contain it). Scope (a). The selection rule stays OPEN.


## 2026-10-11 (PR #7695)

Neutron expansion in `signed_candidates_probe.py` was wrong (uu→dd instead of ud·ud·dd); fixed and now checked against `build_nucleon_nf_mp`. Core (σ₀σ₁⁻¹)³ and 00001100011 are the same Bring loop though not conjugate. B3: under Hecke H₃(q₀) the 2×2 quantity reduces to Wedderburn characters, x = |χ_(2,1)|/√|χ_(3)χ_(1³)|, det = −([2]_q/2)⁴ for both nucleons; under Burau t = −q₀, det = χ_(3). The normalisations disagree in type on every row; neither adopted; B4 (no energy for sums) stays default. Selection still OPEN.

**2026-10-11 — strand-count tower of γγ production** (issue #7727, branch `claude/gg-production-ntower-2026-10-11`, `computations/probes/gg_ntower/`). Pre-registered (4544d19380) before computing. Collisions V_i = σ_iσ_{i+1}⁻¹ (and the bare U_i = σ_iσ_{i+1}, separate column) placed with a rigid shift s ∈ {0, ±1, ±2, +3}, up to 9 strands; strands closed from the top by the convention-D Markov conditional expectation; reading 3 tested at every level. Exact over ℚ(q); 5/5 checks.
- s = +1 telescopes in any group: V_0⋯V_{k−1} = σ_0σ_k⁻¹ (Lean `QOU/QBeta/GammaGammaStaircaseTelescopes.lean`, sorry-free). Degenerate.
- s = −1, ±2, +3: no k admissible, for either vertex. After three collisions closed down to three strands, χ_(2,1) is already negative at q = 1 (−1/4 or −1/16) and stays negative for every q > 1.
- Only s = 0 (all collisions on the same three strands, k = 3, 6) confines. Its χ_(2,1) leaves the q = 1 value at h⁴; the climbing placements leave at h¹ or h².
- Scope (a): rigid shifts with top closing only. Jones pair creation, bottom closing, quarks, gluons and two nucleons were not tested. Selection stays open.

**2026-10-12 — 🟧 OWNER RULING (chat): "every level" means EVERY STRAND COUNT, not only H_{3k}.** Asked in session https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB with two options (1 every strand count m = 3..n; 2 only the nucleus levels H_3, H_6, H_9, …). Owner chose 1. Measured consequence on the #7733 witness: five rows pass at level 3 and fail only at an in-between level (V s=+1 k=2 at 4; V s=+1 k=3 at 5; V s=−1 k=2 at 4; U s=+1 k=2 at 4; U s=−1 k=2 at 4). Under reading 2 they would be admissible; under the ruled reading 1 they are excluded, which is what #7733 reported. None is a genuine cascade (s=+1 telescopes to σ₀σ_k⁻¹; s=−1 k=2 is two collisions sharing two strands). Bean stays open (rule 13a).

## 2026-10-11 — quark template tracked order by order in q (reading 3)

Probe `computations/probes/quark_template/` (pre-registered at 6b9dd5d172; exact over Q(q); 4/4 checks).

- **Flavour is invisible at order t⁰** (t = q − 1): since σ⁻¹ = σ − h, every quark letter equals σ at q = 1, all 8 template variants give the same element, and χ_(2,1) = 0 there. So reading 3 holds with equality at order zero for every template. The verdict is decided at order t¹ (where the sign bits enter), or at t³ when t¹ cancels. No verdict flips between truncation orders t¹…t⁶ or across the sub-interval of (1, ∞) containing q₀.
- **k = 0, builder placement:** the corpus template (u = σ, d = σ⁻¹, ud = average) FAILS reading 3 for both nucleons (χ_(2,1) = −0.09198 p, −0.18200 n). Its sign changes exactly at q*² + q*⁻² = 1 + 2cos(2π/7), q* = 1.27890, above q₀. Every bar-swapped template (u = σ⁻¹, d = σ) passes for both nucleons, under every pair rule. The two flavour-blind templates also pass.
- **With the gluon pair σ₀σ₀:** no template passes for both nucleons.
- **Placement varied too:** the corpus template has 4/8 admissible placements per nucleon; the builder's is not one of them. So reading 3 constrains sign map and placement jointly, not the template alone.
- **Tension, unresolved:** this bean's 2026-09-05 "swap refuted" rests on a comparison with measured binding data, which cannot select under the no-fitting rule. Reading 3, the ruled derived test, points to the swap at k = 0 and the builder placement. This is an owner decision. The bean stays open.

## 🟧 OWNER RULING 2026-10-12 — quark sign map: option 4, derive it, do not pick it

Asked in the six-part frame on PR #7718 (comment 6130340849). The four options were: 1 keep S+ (status quo); 2 adopt the swap S− (u = σ⁻¹, d = σ), which passes reading 3 at the builder placement; 3 keep S+ and move the letters to placement 011 or 100; 4 pick nothing by hand. **The owner chose 4.** The quark sign map and the letter placement must be outputs of the γγ construction plus reading 3 at every tower level (`qou-ales`), not a template choice. The template stays open and nothing is re-scored. The dashboard knowingly keeps scoring an element that reading 3 rejects until a derivation lands. The 2026-09-05 data-based "swap refuted" in `qou-y2np` is a comparison with data, so it counts as a selection neither way. This bean stays open (rule 13a). Session: https://claude.ai/code/session_01A1NHnUY3QMcdoxDYQmLCXB

**2026-10-11 — 🟧 OWNER RULING (thread chat, ofri, verbatim): "3... but let's go through γγ production step by step to get to one and two nucleons. each collision/interaction shifts things up the tower".** Option 3 of the #7702 decision: **reading 3 applies at EVERY level of the tower** (nucleon in H_3, A nucleons in H_{3A}, all checked). On the #7702 family this coincides with the H_3 verdicts; the live element stays excluded. Next: walk γγ production step by step, tracking the tower level of each collision (h-order and n). Walk-through: /mnt/project-files/qbeta-ohara/gg-production-walkthrough.md. Bean stays open (rule 13a).

### Cross-link (2026-10-11)

the p-n interface convention R3 made canonical is the one the corpus's uniqueness theorem does NOT cover (it fails `BarInvariant`), so "canonical" there is not proved canonicity. Record: [`2026-10-11-atom-word-provenance.md`](../../docs/audits/2026-10-11-atom-word-provenance.md).

## 2026-11-15 — four-strand doublet candidates priced under the ruled functional (branch claude/qbeta-delta-doublet-candidates-2026-11-15, bc6872c35)

Probe `computations/probes/qbeta_delta_doublet/delta_doublet_candidates_probe.py` (ALL PASS, exact over Q(q), calibrated on the H_3 ruled base 0.444700408522 MeV). Candidates taken as given from the doublet thread (labels A = sigma_3 lines, B = J_4 lines on sigma_1's left line) and the SM thread's reading-3 passing gamma-gamma words (000, 111, 0101, 1010, all orientations). Delta = YWY - XWX; |eps| does not depend on which state is n.

- Label A: all 48 overshoot, Q in [1.006, 2.397] MeV (F_required in [0.326, 0.778]).
- Label B: all 48 undershoot, Q in [0.0087, 0.4607] MeV (F_required >= 1.698), 4 with eps = 0.
- Every p-state and n-state passes reading 3 at strand counts 3 and 4.

Scope (a). Nothing selected. Label B is outside the cos <= 1 ladder cap, exactly as the H_3 ruled base is. Label A is inside it, but only with the ladder phase alpha chosen, which is a fit until alpha is derived (qou-pdix). The word choice within a label stays open. Bean stays open (rule 13a).


## 2026-11-15 — route 3 (γγ + reading-3 element search): the Hecke side cannot carry n vs p

The owner chose route 3 to replace nuc11, as part of the m_n / Q_β factor question (bean qou-cds1). This synthesises existing results; no new compute was run.

- **3 strands:** the γγ nucleon is Vᵐ, and only V³ and V⁶ pass reading 3 at every level (h2_gg_atom, PR #7741 results.md). The proton and neutron are the **same word**, so Δ = n − p = 0. Any linear ε then gives ε(Δ) = 0, so Q_β = 0. This is exact, within that family.
- **4 strands:** many γγ words pass (#8046 / gg_four_strand). But PR #7975 (sorry-free) shows Hecke elements commute with the U_q action, so **no braid word and no weak vertex changes T³**. Neither J₄ state is n or p. Assigning "neutron" and "proton" to two passing words would be a label choice, and making it by Q_β would be a fit.
- **Verdict, scope (a)+(b):** inside the Hecke algebra the element search cannot produce a flavour-distinguished pair. The invariant is #7975's commutation. So the factor question merges into what ε means: flavour (T³) lives on the U_q / weight side of Schur–Weyl, not in the word. The candidate taken to the owner is a weight-graded split of the rank-2 (convention D) quantum trace into T³ = ∓½ parts. It is not derived here.

## 2026-11-15 22:45Z — weak-vertex thread: structure of Δ_S and one candidate ε (DIAGNOSTIC, not selected)
Handed over by the c_k thread (owner card 22:30Z). Exact sympy on (C²)^⊗3, Jimbo Ř, convention-D K.
1. **Derived identity:** Δ_S = (h²/2)·1 − (h/2)(σ₁+σ₂) = −(q·h·[2]/4)·(W₁ + W₂), with W_i = q⁻¹J_i the corpus weak vertex on crossing i (prop:weak-vertex-left-projector). So the Q_β element is already the weak vertex summed over the two crossings. Since W ∈ span{1,σ} commutes with E, F, K, every trace ε(Δ_S) is T³-blind, consistent with PR #7975.
2. **Candidate ε_B (emission reading B, #7998):** replace each W_i by its Ř coefficient b = 2/(q[2]), the W⁻ emission amplitude from coev pair creation (#7973, #7977). Then ε_B(Δ_S) = −(q h [2]/4)·2b = −h exactly. Q = h·E₀·m_e = m_e(q+1)/q² = 0.875123 MeV at q₀, +11.861 % vs CODATA. Factor over the z_D base: F = 2q(q²+1)/(q⁴+1) = 1.96789 (required 1.75924 order-zero E₀).
**Contamination:** I found ε_B analytically and saw its value before writing this note; it was not pre-registered. Choices inside it: reading B (open on qou-g0jn), the W ansatz plus the owner's definition of left, and the existing Δ_S. It does not see the nucleon word (V³) and does not separate n from p. Scope (a). Not a selection; scoring is diagnostic only.


## PRE-REGISTRATION ε-W1 (2026-11-15 22:36Z, before computing) — word-level ε from the emission process
Requested by the c_k thread; owner card on the weak-vertex thread pending (recommended 'both, word-level first'). Space (C²)^⊗3 ⊗ V ⊗ V* as in #7981. Jimbo Ř 'std', K = diag(q, q⁻¹), u = e₁. Initial state N ⊗ coev₄₅ (plain coev Σᵢ eᵢ⊗eᵢ), with N ∈ {|udd⟩; |udd⟩+|dud⟩+|ddu⟩ (T³ = −½ weight space, equal K weights)}. Apply X on quark strands, then the emission crossing Ř on strands (3,4) (#7973 arm A). A(X) = sum of components on {two u, one d on 1–3} ⊗ (d on 4, u on 5).
Quantities: A(Δ_S·V³), A(V³), and ε_W := A(Δ_S·V³)/A(V³) (per-emission normalisation). Q = |ε_W|·E₀·m_e, E₀ = 1/(q(q−1)). Also the same with V⁶. Reported exactly and at q₀.
Prediction (stated before running, no number): if ε_W = −h for both N and both words, reading B's word-blindness holds at word level and the candidate is just ε_B again. Any other value is reported as found. Not a selector; scored as a diagnostic only. Not scored against the required factor for choosing between variants.


## RESULT ε-W1 (2026-11-15 22:45Z)
Identity check passes: Δ_S = −(q h [2]/4)(W₁+W₂) (8×8, exact). ε_W = A(Δ_S·Vᵏ)/A(Vᵏ) at q₀: V³ |udd⟩ −0.209475 (Q 0.876858 MeV, +12.08 %); V³ T³=−½ sum −0.204726 (0.856981, +9.54 %); V⁶ |udd⟩ −0.221471 (0.927074, +18.50 %); V⁶ sum −0.205606 (0.860665, +10.01 %). −h = −0.209061. Prediction (ε_W = −h everywhere) FAILED: the emission step sees the word and the state. The neutron-state choice moves Q by up to 8 %, and nothing in the corpus fixes it, so no row is selectable. Probe computations/probes/word_level_epsilon_probe.py. Diagnostic only.


### PRE-REGISTRATION ε-NP1 (2026-11-15 22:45Z, owner pick 'Both, compare first')
Question: does the emission step break n↔p symmetry? Δ_S = −(q h [2]/4)(W₁+W₂) is T³-blind inside H₃, so any asymmetry must come from the state plus the emission crossing.
Setup: same as ε-W1 (computations/probes/word_level_epsilon_probe.py). n→p: start |udd⟩ or the T³=−½ sum, project onto (two u, one d) ⊗ (d on 4, u on 5). p→n mirror: start |uud⟩ or the T³=+½ sum, project onto (one u, two d) ⊗ (u on 4, d on 5). Words V³ and V⁶; same Δ_S; same Ř on (3,4).
Report for each word and state pair: ε_np, ε_pn, ratio ε_pn/ε_np (exact), plus check whether ε_pn(q) = ε_np(q⁻¹) (the u↔d flip).
Prediction (H0): ε_pn = ε_np exactly (no asymmetry from emission). Alternative H1: they are related by q→q⁻¹ only. Anything else is reported as found.
Scope: structural only. There is no measured p→n width to score against, so nothing is compared to data and no row is selected.


### PRE-REGISTRATION ε-TW1 (2026-11-15 22:46Z, owner: 'ΔS followed by something like 1⊗twist ... like the involution?')
Same process as ε-NP1. The new element is X·Δ_S, where X is applied after Δ_S and before the emission crossing (X is in the numerator only): ε_X = A(X·Δ_S·V^k)/A(V^k).
X candidates, all fixed before computing:
(1) T23 = Ř² on quark strands 2,3 (the ribbon twist on V⊗V, without the θ_V² scalar);
(2) J23 = P₊ − P₋ on strands 2,3 (the involution, J² = 1);
(3) F3 = the u↔d flip on quark strand 3 (the emitting strand);
(4) Fall = the u↔d flip on all three quark strands;
(5) F4 = the u↔d flip on the emitted strand 4, applied after the crossing.
Words V³ and V⁶; both state choices; both n→p and p→n.
No numerical prediction. Nothing is selected by closeness to −h or to CODATA. Q at q₀ is shown for display only.


### RESULT ε-NP1 (2026-11-15 22:58Z), np_emission_asymmetry_probe.py
H0 (ε_pn = ε_np) FAILS and H1 (ε_pn(q) = ε_np(1/q)) FAILS for all four (word, state) pairs. Emission does break n↔p.
- T³ sums: ratio ε_pn/ε_np at q₀ = 1.0446 (V³), 1.0353 (V⁶). Near q=1 it is 1 + (q−1)/2 + O((q−1)²).
- Single states |udd⟩ vs |uud⟩: ratio 29.7 (V³), 12.1 (V⁶), because the p→n amplitude without Δ_S nearly vanishes. Caveat: |uud⟩ is not the u↔d image of |udd⟩ (that would be |duu⟩). This is recorded as pre-registered, not changed afterwards.
So the size of the asymmetry depends on the free state choice.

### RESULT ε-TW1 (2026-11-15 22:58Z), twist_involution_epsilon_probe.py
- The flips F3, Fall and F4 give ε = 0 in every case. A u↔d flip changes the charge content, so the charge-projected amplitude vanishes. A flip is only meaningful with the projection flipped too, and that is just the n↔p map.
- T23 (Ř² on strands 2,3) raises |ε| in both directions. The n→p over p→n ratio stays near 1.05.
- J23 (the involution P₊−P₋ on strands 2,3), T³ sums: ε_np = −0.198078 (V³), −0.198057 (V⁶); ε_pn = −0.219804, −0.219591. Exact series: ε_pn/ε_np = q − 22(q−1)⁵ + … (V³) and q − 92(q−1)⁵ + … (V⁶). It matches q through order (q−1)⁴, but it is NOT equal to q, and the deviation coefficient grows with word length. At q₀ the ratio is 1.10968 (V³) and 1.10873 (V⁶), against q₀ = 1.10998.
- Q values at q₀ are display only; none is selected.


### PRE-REGISTRATION ε-N1 and ε-J1 (2026-11-15 23:05Z; owner 'go' via coordinator; PR #8068 holds ε-W1/NP1/TW1)
**ε-N1: which T³ = −½ vector is the neutron?** Rule: the vector must be fixed by a corpus construction (U_q(sl₂) isospin, Schur–Weyl, γγ pair creation), never by matching data.
Step 1 (forced): the nucleon has isospin ½, so it lies in the (2,1) isotypic part of V^⊗3 at T³ = −½, which has dimension 2. NOTE: the 'T3 sum' state used in ε-W1/NP1/TW1, |udd⟩+|dud⟩+|ddu⟩, is the classical symmetric vector. At q = 1 it is pure isospin 3/2 (the Δ⁰), and at q ≠ 1 it is not even a U_q weight-space eigenvector of the Casimir. So those rows are NOT neutron rows.
Step 2: compute the T = ½ subspace at T³ = −½ exactly, as the kernel of the U_q(sl₂) raising operator E restricted to that weight (the coproduct convention matching Ř 'std'). Report ε_np for a general vector in that 2-dim space, as a rational function of the multiplicity coordinate.
Step 3: grep the corpus for a construction that fixes the multiplicity vector (γγ pair creation; seminormal basis; diquark channel). If one is found, cite it and evaluate. If none is found, report the family and say the choice is open.
Prediction: ε_np depends on the multiplicity coordinate (it is not constant on the 2-dim space).
**ε-J1: why does J give ε_pn/ε_np ≈ q?** Compute the J23-dressed ratio for words V⁰ (none), V¹ and V² as well as V³ and V⁶, on the same (pre-registered, |udd⟩/|uud⟩ and sum) states. Prediction: with no word (V⁰) the ratio is exactly q, and the (q−1)⁵ deviation comes from the word. If V⁰ is not exactly q, report as found.


### RESULT ε-N1 and ε-J1 (2026-11-15 23:25Z), neutron_vector_epsilon_probe.py
**ε-N1.** The T=½ neutron space at T³=−½ is ker F (Δ(F) = F⊗1 + K⁻¹⊗F, which commutes with Ř std). It is spanned by n_A = [ud]₁₂⊗d and n_B = d⊗[ud]₂₃. The old states |udd⟩ and the symmetric sum are NOT in it (checked). Prediction (ε depends on the multiplicity coordinate t) CONFIRMED, and strongly so. ε_np at q₀, with no extra element:

| | n_A (t=0) | n_B | t=1 | t=−1 |
|---|---|---|---|---|
| V³ | −6.390 | −0.0184 | −0.114 | +0.080 |
| V⁶ | +1.423 | −0.0261 | −0.125 | +0.061 |

It even changes sign and changes with the word. Conclusion: the word-level ratio ε = A(Δ_S·Vᵏn)/A(Vᵏn) is not a stable functional on T=½ neutron states. The ≈ −h values of ε-W1 belonged to non-isospin states. A quick corpus grep (QuarkState/, eightfold, h3 idempotents) found no construction that fixes t, so the choice is OPEN, and that is a shallow grep, not a full corpus-grep.
**ε-J1.** Prediction CONFIRMED: with no word (V⁰), on the symmetric sum states, ε_pn/ε_np = q exactly. ε_np = −(q−1)(q+1)⁴/(4q²(q²+1)) and ε_pn = q·ε_np. The single state has a zero amplitude at V⁰. For V¹ and V² the ratio departs from q at FIRST order (ratio − q = −(3/2)(q−1) + …), so ≈ q is not generic. V³ and V⁶ return to agreement through (q−1)⁴. Mechanism at V⁰: the p→n channel has one more power of q from the K-weights of the emitted pair, and J does not change it. The return at V³ and V⁶ is unexplained (it may be because the word length is a multiple of 3).


### PRE-REGISTRATION ε-TR1 (2026-11-15 23:32Z): remove the neutron-vector choice by a trace
The emission projections are taken over isospin-½ states.
- At T³ = +½, the weight space splits canonically into the T=½ part, span{p_A, p_B} = E·span{n_A, n_B}, and the T=3/2 line F₃·uuu.
- Let π be the projection onto the T=½ part along the T=3/2 line, with coordinates in the basis p_A, p_B.
- Define the 2×2 matrix M(X)_{ij} = coordinate i of π[(quark part of) the component on pair (d on 4, u on 5) of Ř₃₄·X·Vᵏ·(n_j ⊗ coev)].
- ε_tr = Tr M(Δ_S) / Tr M(1). It is independent of the basis of the multiplicity space.
- p→n is the mirror: start p_j; final projection onto the T=½ part at T³ = −½ along F₃²·uuu, in the basis n_A, n_B; pair (u on 4, d on 5).
Words V⁰, V³, V⁶; X = none and J23.
Questions: is ε_tr stable across words, and what is ε_tr,pn/ε_tr,np? No numerical prediction. Nothing compared to data.


### RESULT ε-TR1 (2026-11-15 23:45Z), multiplicity_trace_epsilon_probe.py
With the neutron-vector choice traced out over the isospin-½ multiplicity space, **ε_tr,pn = ε_tr,np EXACTLY**, as rational functions in q, for V⁰, V³ and V⁶, with and without J23. Tr M(1) is also identical in both directions.
- V⁰: ε_tr = (q−1)(q+1)(q²+1)/(2(q⁴+1)) = 0.10285 at q₀; with J23 it is −(q²−1)/(2(q²+1)) = −0.05198.
- V³ gives 0.11369, V⁶ gives 0.12406 (with J23: −0.04651, −0.04126). So ε_tr is word-dependent, not −h, and not stable in k.
Reading: every n↔p asymmetry seen in ε-NP1, ε-TW1 and ε-N1 came from states that are not U_q-isospin-covariant, or from a choice of multiplicity vector. On canonically traced isospin-½ states, Δ_S plus this emission is n↔p symmetric. That is consistent with a Wigner–Eckart reduction, but the symmetry is not proved here. So this route does not break the n–p asymmetry. A source of asymmetry has to be non-U_q-covariant (e.g. electric charge or the external field), scope (a).


### PRE-REGISTRATION ε-EM1 (2026-11-15 23:40Z; owner 'keep pushing', coordinator: n–p break via a non-U_q-covariant ingredient)
Corpus status, checked first:
- Hypercharge Y is OPEN (eightfold-open-problems; strand-twist-datum is a free label).
- The derivation-chain thread's EM1 (/mnt/project-files/qou-derivation-chain/bridge-b/em1_result.md) did static photon exchange inside the nucleon, with Y = 1/3 imported. Result: the classical −2/3 plus an O(h⁴) braid correction.
- My distinct angle: Coulomb exchange in the DECAY's intermediate state, before the emission crossing, where the created pair is still a superposition, so the charge operator does not reduce to a scalar. Y is kept as a SYMBOL, not imported.
Setup: as in ε-TR1, with the trace over the isospin-½ multiplicity space. Charge per strand: Q = T³ + Y/2 on V (strands 1–4), and Q = −(T³ + Y/2) of the index on the V* strand 5. X = Σ_{a<b≤5} Q_a Q_b (diagonal), inserted after Δ_S and before Ř₃₄. Report the first-order shift δε = d/dg [Tr M(Δ_S then 1+gX) / Tr M(1)] at g=0 for n→p and p→n, as exact functions of (q, Y), for words V⁰, V³ and V⁶.
Questions: (i) is δε_np ≠ δε_pn? (ii) Which part is Y-independent? (iii) Does the asymmetry survive at q = 1 (classical) or vanish there?
Prediction: the asymmetry is nonzero. At q = 1 it reduces to classical charge algebra (as in EM1), and the braid adds corrections. No coupling value is chosen and nothing is compared to data.


### RESULT ε-EM1 (2026-11-15 23:50Z), coulomb_in_decay_epsilon_probe.py
With the Coulomb insertion X = Σ_{a<b≤5} Q_aQ_b between Δ_S and the emission crossing, traced over the isospin-½ space:
- δε/ε = (Y² − 2Y − 1)/2 for n→p, and (Y² + 2Y − 1)/2 for p→n.
- These are EXACTLY independent of q and of the word (V⁰, V³, V⁶).
- Asymmetry = 2Y exactly. It is zero at Y = 0.
Prediction (i) holds only for Y ≠ 0. Prediction (iii) 'the braid adds corrections' FAILS: in this placement the braid adds nothing, and the charge enters as pure classical charge algebra (the Y·T³ cross term).
Reading (scope a): on canonically traced isospin-½ states, the whole n↔p asymmetry this route can produce is carried by the hypercharge Y, linearly. Since Y is OPEN in the corpus (eightfold-open-problems; conj:sm-hypercharge-invariant; strand-twist-datum is a free label), the n–p break via charge is gated on deriving Y. It is not gated on the braid.


### PRE-REGISTRATION ε-Y1 (2026-11-16 00:05Z; route chosen: "Derive Y from colour", the stated default on the open card)
Hypothesis under test: the source is the untested line in bean qou-sl3f, "the stripped u1 factor q^(1/N) per crossing reads as baryon number 1/N per quark".
Setup:
- Jimbo gl_N R on V⊗V versus sl_N R. The ratio is the u1 factor.
- Model a U(1) braiding with charges a, b as q^(c·a·b). Here c is the pairing normalisation and is NOT chosen in advance.
Questions:
- (i) Does the u1 factor fix a alone, or only the product c·a²?
- (ii) What does singlet transparency (V around Λ^N V) add to (i): an independent constraint, or the same one?
- (iii) Which further input, if any, sets a = 1/N?
- (iv) Is that input data, a convention, or a derived fact?
- (v) Does a = 1/N give Y = 1/3 for the quark doublet in the ε-EM1 convention Q = T³ + Y/2? Or does that need Y = B − L, which brings in lepton-sector input?
Prediction: (i) only c·a² is fixed; (ii) it is the same constraint; (iii) a lattice normalisation "the baryon Λ^N V has unit charge" is needed. So the route gives the RATIO quark : baryon = 1 : N categorically, while Y = B for quarks stays an identification.
No value of Y is compared to data. The δε numbers at Y = 1/3 are reported only as consequences.


### RESULT ε-Y1 (2026-11-16 00:15Z), colour_hypercharge_y1_probe.py (exact sympy, N = 2, 3)
- Every prediction held.
- (i) The u1 factor of gl_N over sl_N on V⊗V is q^(1/N) per crossing. In a U(1) braiding q^(c·a·b) this fixes only c·a² = 1/N, not a.
- (ii) The gl_N monodromy of V around Λ^N V is q² (computed for N = 2, 3, matching qou-sl3f). Given (i), it is REDUNDANT: 2c·a·(N a) = 2N·c a² = 2. So it adds no constraint.
- (iii) Both constraints keep the scale freedom (a, c) → (λa, c/λ²). So a = 1/N needs one more input: the lattice normalisation "Λ^N V carries unit charge".
- (iv) That input is a normalisation convention (the primitive generator of the charge lattice), not data. Colour does derive the RATIO quark : baryon = 1 : N.
- (v) Reaching Y = 1/3 in ε-EM1's convention Q = T³ + Y/2 needs two things that are not derived:
  - that this colour u1 IS hypercharge;
  - Y = B − L with L = 0 for quarks (lepton-sector input).
- So the hypothesis in qou-sl3f is confirmed only as "baryon number 1/N given unit-charge normalisation". Y stays OPEN (scope a).
- Consequence only, not a prediction: at Y = 1/3, ε-EM1 gives δε/ε = −7/9 (n→p) and −1/9 (p→n), with asymmetry 2/3. These are O(1) because X carries no coupling constant. They are not physical magnitudes.
- Next honest options:
  - (a) derive the u1 ↔ hypercharge identification, e.g. from the strand-twist datum or the anomaly-free trace condition, without importing lepton charges;
  - (b) use only the colour-fixed ratio and accept Y as a labelled open input.


### PRE-REGISTRATION ε-Y2 (2026-11-16 06:40Z; owner tapped "Derive Y from colour" after ε-Y1, so the remaining step is pursued)
Goal: derive the colour-u1 ↔ hypercharge identification that ε-Y1 left open, without importing lepton charges.
Steps:
1. Corpus check first: strand-twist-datum, conj:sm-hypercharge-invariant, eightfold-open-problems, QuarkStrandConsequences (integer charge ⟺ triality zero).
2. Test whether "integer charge ⟺ triality zero", applied with the colour-fixed ratio (quark : baryon = 1 : N), forces Q − T³ ≡ B mod ℤ on quark strands. That would fix Y/2 = B/2 mod integers.
3. Report the residual freedom; do not pick from it.
No data, and no lepton charges as input.


### RESULT ε-Y2 (2026-11-16 06:55Z), triality_hypercharge_y2_probe.py (exact Fractions)
- Input: the principle "total charge ∈ ℤ ⟺ (n_q − n_q̄) ≡ 0 mod 3" on all quark and antiquark strand lists up to length 6, with Q = T³ + Y/2.
- This principle is the reverse of QuarkStrandConsequences Result 2. It is a physical input (colour confinement plus charge quantisation), NOT derived from the braid.
- Output: the solution set is exactly Y ∈ ±1/3 + 2ℤ (scan k/36, |Y| ≤ 4).
- Residual freedom has two parts:
  - (a) the sign. Y → −Y is charge conjugation (V ↔ V*: which strand is called the quark). A labelling convention.
  - (b) an integer shift Y → Y + 2k. Nothing here fixes k = 0. Taking the minimal |Y| = 1/3 would be a choice, and is NOT made here.
- Combined with ε-Y1, colour plus triality give Y ≡ ±B (mod 2) for the quark doublet, with B = 1/3. The value 1/3 itself needs the minimality choice, or a further structure that picks k.
- So Y is constrained but NOT derived (scope a). The ε-EM1 asymmetry 2Y is fixed up to sign and an even-integer shift: 2/3 at the minimal choice.


### NOTE ε-Y3 (2026-11-16 06:50Z), corpus check for the even shift k
- Anomaly cancellation cannot fix k from quarks alone: every U(1)_Y anomaly that involves the left doublet's Y also needs the lepton content.
- The strand-twist datum (def:strand-twist-datum) does fix k, but only under a bound. Its candidate Y_t = 2(T/3 − I₃), with T the total twist of three sub-strands, gives the following for a doublet with T_u − T_d = 3 and fractional Q:
  - per-strand bound |t_i| ≤ 1: Y ∈ {−1/3, +1/3}, so k = 0;
  - bound |t_i| ≤ 2: Y ∈ {±1/3, ±5/3, ±7/3}.
- So k = 0 is equivalent to the helon bound |t_i| ≤ 1, which is imported (bilson-thompson2005). The datum itself is t: {1..n} → ℤ and is unbounded.
- Also, Q_twist = Q is the defining equation (TwistBatteryVacuity), not a test.
- Status: Y = ±1/3 is CONDITIONAL on the helon twist bound. The sign is a convention (C). Y stays OPEN until the bound |t_i| ≤ 1 is derived, e.g. from a ribbon-twist eigenvalue constraint.


### NOTE ε-Y4 (2026-11-16 07:10Z), where the helon twist bound comes from (owner: "try derive twist bound")
Source (held in the library: arxiv-hep-ph-0503213v2, §2):
- A helon is a PAIR of tweedles, each a ±π half-twist ("Unordered pairing").
- So the helon twist is +2π, 0 or −2π, i.e. |t_i| ≤ 1. The bound is a consequence of "a strand carries exactly two half-twists". It is not an independent axiom.
Categorical translation (proposal, not proved):
- a half-twist ±π corresponds to one Hecke letter σ^{±1} (two eigen-channels only);
- a helon corresponds to a two-letter unit;
- the corpus γγ rule already gives words of even length (gammaGamma_length_even), and the gluon unit is V = σ₀σ₁⁻¹.
- If each strand's twist datum = the exponent sum of ONE γγ two-letter unit, then t_i ∈ {−2, 0, 2}/2 = {−1, 0, 1}, and ε-Y3 gives Y = ±1/3.
Remaining assumption: "one γγ unit per strand". This is a minimality statement, the same kind of choice as k = 0. So the bound is MOVED onto the γγ construction, not yet derived. A derivation would need the γγ pair-production construction to put exactly one pair on each strand.


### RESULT ε-Y5 (2026-11-16 07:20Z): the γγ route to the twist bound is EXCLUDED
- The ε-Y4 proposal ("a strand's twist = exponent sum of one γγ two-letter unit") fails structurally.
- vertex i = [σ_i, σ_{i+1}⁻¹] has writhe 0 (QOU.Mass.GammaGammaWordSelection.writhe_vertex), and every γγ word has writhe 0 (writhe_eq_zero, sorry-free).
- Any ADDITIVE attribution of crossing signs to strands gives a total Σt_i that is a multiple of the writhe. So on γγ words T = 0, hence Q_twist = 0, for every strand assignment.
- A fractional quark charge needs T ≠ 0, so the twist datum of a charged strand cannot come from γγ letters at all. Scope (b), invariant: writhe_eq_zero.
- This agrees with def:strand-twist-datum, which calls the datum "an independent label, not the ambient twist".
- Status: the bound |t_i| ≤ 1 is NOT derivable on this route. Y = ±1/3 stays conditional on the imported helon bound (two ±π tweedles per strand). Y stays OPEN.


### LABEL (owner tap 2026-11-16 07:06Z "Label Y, switch to element")
Y = ±1/3 for the quark doublet is recorded as a LABELLED CONDITIONAL INPUT. Its conditions: the triality principle (ε-Y2) and the helon twist bound |t_i| ≤ 1 (arxiv-hep-ph-0503213v2). The sign is a C-convention. Y is not derived. Work moves to the nucleon element choice.


### RESULT ε-Y6 (2026-11-16 07:15Z; owner "and B": ribbon-twist route too)
- Treat a helon as a 2-strand ribbon of V⊗V, and read its twist as the exponent in units of q² of the full-twist monodromy Ř^{2k}.
- Exact eigenvalues (gl_2 Jimbo): Ř² has q² (×3, symmetric) and q⁻² (×1, antisymmetric). Ř^{2k} has q^{±2k}.
- So ONE full twist gives t ∈ {+1 (sym), −1 (antisym)}, and no twist gives 0: exactly the helon set {UU, EE, UE}. As a bonus, the twist SIGN is tied to the symmetry channel.
- But Ř^{2k} gives ±k, and nothing in the braiding bounds k.
- Verdict: like the γγ route, this moves the bound onto a minimality statement ("at most one full twist per helon"); it does not derive it. Scope (a). Y stays a labelled conditional input.


### FINDING ε-Y7 (2026-11-16 07:25Z; owner asked: "are we missing ribbon twist in γγ setup? does it come from 3rd term in photon?")
Yes, there is a mismatch inside the corpus.
- The Lean γγ grammar (GammaGammaWordSelection.vertex i = [σ_i, σ_{i+1}⁻¹]) keeps only writhe-0 vertices, so every γγ word has writhe 0.
- The corpus's own photon blocks give the photon a twist channel:
  - trivial-knot-photon-interpretation says "the photon's internal twist is inherently positive (L₊)" and "electrons cannot emerge from photons lacking twist content";
  - breit-wheeler-vertex says σ₀·σ₁ = L₊ (the Hopf link, writhe +2), then L₊·σ₀ = e⁻ (writhe 3), with the mirror L₋ for e⁺.
- So the photon has two linear channels (σ₀, σ₁) and a third, twist-carrying Hopf channel L± (writhe ±2 = one full twist). The Lean γγ vertex omits that third channel.
- Consequence for Y: if each photon carries twist content in {L₊, none, L₋} = {+1, 0, −1} full twists, and a strand's twist datum is supplied by ONE photon, then |t_i| ≤ 1 follows. That is the helon bound, with each photon playing the tweedle pair.
- It still rests on "one photon per strand", but that is how pair production naturally counts, not a free minimality choice.
- Caveat: adding L± to the γγ rule changes an owner-ruled grammar (qou-ales). The writhe-0, reading-3 and element results (V³, V⁶; the trefoil electron as the non-γγ blocker) would all need re-checking. Owner decision.


### PRE-REGISTRATION ε-L1 (2026-11-16 07:30Z; owner tap: test the γγ grammar with the photon twist channel L±)
- Extended grammar units:
  - the existing V = σ₁σ₂⁻¹ (writhe 0);
  - L₊ = σ₁σ₂ (writhe +2), from breit-wheeler-vertex;
  - L₋ = σ₁⁻¹σ₂⁻¹.
- Words to test on the ε-TR1 traced setup (isospin-½ multiplicity trace, Δ_S, emission Ř₃₄):
  - L₊, L₋, L₊V³, V³L₊, L₊L₋;
  - the Breit–Wheeler electron-type word L₊σ₁ = σ₁σ₂σ₁.
- Questions:
  - (i) does any word give ε_pn ≠ ε_np, i.e. break u↔d?
  - (ii) does the twist content per photon lie in {−1, 0, +1} full twists, so that |t| ≤ 1 follows from one photon per strand?
  - (iii) reading 3 on the nucleon words with L±: which pass?
- Prediction for (i): NO breaking. Every Ř word commutes with the U_q(sl₂) action, so on canonically traced isospin-½ states n↔p symmetry should hold whatever the writhe, exactly as in ε-TR1.
- Prediction for (ii): yes by construction (writhe ±2 per unit).
- Nothing is compared to data, and no element is picked by residual.


### RESULT ε-L1 (2026-11-16 07:40Z), gg_twist_channel_np_probe.py (exact over Q(q))
- (i) NO breaking, as predicted. For L₊, L₋, L₊V³, V³L₊, L₊L₋ and the electron-type σ₁σ₂σ₁ (writhe 2, −2, 2, 2, 0, 3), ε_tr,pn = ε_tr,np exactly, and Tr M(1) is identical in both directions.
- Reading: the twist channel changes ε's value (L₊: −(q²−1)(q⁴+1)/(2q⁶) = −0.156 at q₀; L₋: −0.292; the e-type word: +0.106) but not its n↔p symmetry. Every Ř word is U_q(sl₂)-covariant, so adding writhe does not help.
- Conclusion, scope (a) on these six words: L± does NOT break u↔d. The break still needs a non-U_q-covariant ingredient, which so far is the hypercharge (ε-EM1: asymmetry 2Y).
- (ii) L± supplies twist ±1 per photon, so one photon per strand gives |t| ≤ 1 and hence Y = ±1/3 (ε-Y3/Y7). This is the only place the twist channel matters for n–p: through Y, not through the braid. L₊ being "inherently positive" (trivial-knot-photon-interpretation) would also fix the SIGN of Y, if that statement is derived. It is currently prose.
- (iii) Reading 3 on L± nucleon words: NOT run here. It belongs to the γγ-grammar owner (colour/gluon thread).
- No mass or compute change. The element choice is unaffected.


### NOTE (2026-11-16 07:32Z), from the thread "Pin down what ε means for Q_β"
- On Δ_S = −(h[2]/4)(J₁ + J₂) (Lean: QuarkState/DeltaSIsWeakVertexSum.lean, merged) we have χ₍₂,₁₎(Δ_S) = 0. So every block-weighted trace gives τ(Δ_S) = −(h[2]/2)(y₃ − y₁₁₁) = −(h[2]/2)τ(J).
- The ε question on Δ_S is therefore the single chirality expectation τ(P_L) − τ(P_R):
  - augmentation: y₃ = 1, +12.47 %;
  - z_D: y₃ = (q⁴+1)/(q²+1)², −43.16 %.
- The long elements nuc9 and nuc11 have χ₍₂,₁₎ ≠ 0, so for them ε is affine in y₃.
- The AME-implied y₃ = 0.889 is recorded as a TARGET only, never a selector. Their probe: /mnt/project-files/qou-qbeta-epsilon/qbeta_epsilon_chirality_reduction_probe.py.


### NOTE (2026-11-16 07:35Z), from the crossing-energy thread (PR #8108; /mnt/project-files/qou-crossing-energy/result-pn-mirror-gg-walk.md)
Setting: H₃, convention D, exact.
- The only mirror fixing the γγ vertex σ₀σ₁⁻¹ is M = bar ∘ flip ∘ reverse, which acts as bar on traces.
- The γγ core (σ₀σ₁⁻¹)³ is M-fixed and bar-even.
- Full p and n are NOT mirrors. Their quark blocks form a partial mirror:
  - χ₃(q_n) = bar χ₃(q_p) exactly;
  - in (2,1) both bar-even parts are 0, and the bar-odd parts differ by exactly −h/2.
- So the element asymmetry sits only in the (2,1) sector, as a −h/2 shift, and lies in the 5 non-γγ letters.
- Relevance to the element choice: any rule fixing the quark block decides the (2,1) shift. Since χ₍₂,₁₎(Δ_S) = 0 (ε thread), the short element Δ_S does not see it, while nuc9 and nuc11 do. bar is semilinear, so F₃-commutation (Bridge B) does not apply to it directly.

### NOTE 2026-11-16 — gluon thread stage 1 (L± in the reading-3 re-check), relayed
Over 5,460 words of length 1–6 in {V, V⁻¹, L₊, L₋}: a word passes reading 3 iff it is a pure braid (1,778 pass, 3,682 knots fail). Adding L± changes character SIZES (L₊³ lowest char 1, L₋³ 0.5347), not pass/fail; no knot passes, so the trefoil electron is still not γγ-reachable. For this bean: L± is F₃-covariant (ε-L1), so it cannot be the n–p break, and it does not rescue nuc11's (2,1) failure. Stage 2 (H₂, V³/V⁶ + length-2 chiral electrons) pending. Adding L± to the rule stays the user's ruling.

### NOTE 2026-11-16 — gluon thread stage 2 (PR #8128), relayed
H₂ with nucleon V³/V⁶ × four chiral length-2 electrons (σ₁²=V⁻¹L₊, V⁻¹L₋, L₊V⁻¹, L₋V⁻¹): bare molecule passes reading 3 in all 16 cells; V³ bond passes everywhere. Trefoil fails reading 3 at every q, alone and in composites; its negative trace is forced by the Hecke relation (only a z=q truncation removes it). Handed-electron candidates = pure braids with nonzero writhe. No effect on the n–p break (all F₃-covariant) or on the nucleon element choice.

### NOTE 2026-11-16 — y₃ result, re-measured (PR #8130 probe, 15/15 pass, 60 dps, proton pin)
ε on a block-weighted trace on the normalised convention-D line (y₁₁₁ = 0, y₂₁ = (1−y₃)/2) is affine in y₃. Values for the convention-D weight y₃(z_D) = (q⁴+1)/(q²+1)² = 0.505404226504 and the augmentation y₃ = 1:

| element | χ₍₂,₁₎ | E₀ | z_D | augmentation | y₃ that would give AME |
|---|---|---|---|---|---|
| Δ_S | 0 | order zero | −43.157 % | +12.470 % | 0.889126 |
| Δ_S | 0 | tower (#8124) | −42.594 % | +13.585 % | 0.880397 |
| nuc9 | −0.0900 | tower | −30.252 % | +14.204 % | 0.841972 |
| nuc11_interleaved | −0.0914 | tower | −16.678 % | +40.705 % | 0.649154 |
| nuc11_gen_grouped | −0.1068 | tower | −14.613 % | +40.705 % | 0.636059 |

- The "y₃ for AME" column is diagnostic only. It is obtained by inverting the target, so it is a fit and may not select a functional or a weight (§NO FITTING). No derived trace on record has y₃ near 0.88. The two derived points, z_D (0.505) and the augmentation (1), are on either side of it.
- The ruled base (2026-09-08: z_D, tower E₀) on Δ_S gives Q_β = 0.4491 MeV, −42.59 % (#8124).
- Open, and the reason this bean stays open: what decides y₃ (equivalently the chirality expectation τ(P_L) − τ(P_R)) from the corpus, and the element choice (nuc11 fails reading-3 confinement on (2,1)).
- Five blocks still print the superseded order-zero 0.4447 MeV: epistemic-status-of-calibrations, mass-comparison-table, three-calibration-discipline-remark, np-discrepancy-resolution, q-beta-over-e0-classical-vanishing-ladder-reading. q-beta-c-2-eq-neg-one-structural also prints it, but that block is explicitly order-zero.

### NOTE 2026-11-16 — gluon thread stage 2 (PR #8128), relayed
H₂ with nucleon V³/V⁶ × four chiral length-2 electrons (σ₁²=V⁻¹L₊, V⁻¹L₋, L₊V⁻¹, L₋V⁻¹): bare molecule passes reading 3 in all 16 cells; V³ bond passes everywhere. Trefoil fails reading 3 at every q, alone and in composites; its negative trace is forced by the Hecke relation (only a z=q truncation removes it). Handed-electron candidates = pure braids with nonzero writhe. No effect on the n–p break (all F₃-covariant) or on the nucleon element choice.

### NOTE 2026-11-16 09:50Z — thread "Find the n–p break and nucleon element" resumed
- PR #8104 (ε-L1 probe) re-run here: reproduces the committed witness byte-for-byte (exact sympy). Precision gate not examined (qou_substrate absent in container). Merge card posted to the owner.
- Owner card posted: does L± = σ₀σ₁ join the γγ rule (add / keep as is / decide later). Agent recommendation: keep as is (no corpus derivation of L± as a γγ letter; adopting it for its handedness would be selection by outcome). No selection rule is adopted or computed until the owner rules; any rule will be pre-registered here first.
- Status unchanged: n–p break still needs a non-U_q-covariant ingredient beyond the Coulomb/Y insertion; no element rule derived. Bean stays OPEN (open conjecture).

### OWNER RULING 2026-11-16 09:46Z — L± joins the γγ word rule
Owner tapped "Add L± to γγ" (card in thread "Find the n–p break and nucleon element"; agent had recommended keep-as-is). From now on the γγ alphabet is {V, V⁻¹, L₊, L₋} with L± = σ₀σ₁ (resp. inverse). Recorded consequences, NOT yet re-derived:
- Reading 3 then passes exactly the pure braids (gluon thread stage 1); handed (nonzero-writhe) pure words are admissible.
- Δ_S is no longer guaranteed canonical, so Q_β = 0.4491 MeV (#8124) is provisional, and the level-1 "Q_β = 0" prune (GammaGammaSelectedDeltaVanishes.lean) must be re-checked over the enlarged alphabet.
- n–p break: unaffected (every L± word is F₃-covariant, ε-L1 ratio 1).
- Canonical word reselection over the new alphabet is required. Any selection rule will be PRE-REGISTERED here before computing; no element picked by residual; any m_n move flagged in project chat.
Bean stays OPEN.

### CORRECTION 2026-11-16 19:50Z — the L± recommendation was wrong (agent's own error)
The agent recommended "keep the rule as is" on the grounds that "nothing in the corpus derives L± as a γγ letter". False: prop:gamma-gamma-generates-particles (predicted-spectra/gamma-gamma-generates-particles.md) reduces the product of two three-term photons γ = 1 + φ₀σ₀ + φ₁σ₁ with the Hecke relation, and the normal form already contains L₊ = σ₀σ₁ (coefficient φ₀ψ₁) and L₋ = σ₁σ₀ (coefficient φ₁ψ₀). So L± follows from the photon definition applied to γγ; the owner's ruling restores what the definition gives, and the earlier {V, V⁻¹} rule was a truncation of it. Search gap: the agent read the bean history and the trivial-knot remark tables but not this proposition.
Open discrepancy to check: in that proposition L₋ = σ₁σ₀ (writhe +2, opposite ORDER), while the ε-L1 probe (#8104) and the gluon-thread stages used L₋ = σ₀⁻¹σ₁⁻¹ (writhe −2, the INVERSE). ε-L1's conclusion (p/n ratio 1) holds for every Ř word, so it is unaffected; the reading-3 stage results that used L₋ as an inverse need re-checking against L₋ = σ₁σ₀.

### NOTE 2026-11-17 10:50Z — the photon has FOUR terms / three parameters (owner query)
prop:gamma-gamma-generates-particles writes γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁: four terms, three colour parameters (φ₀, φ₁, φ₀₁). The 19:50Z CORRECTION called it "three-term"; that is the block's first reduction step with φ₀₁ = ψ₀₁ = 0, not the definition. Consequences, from the block itself:
- L₊ = σ₀σ₁ is already in a SINGLE photon (the φ₀₁ Hopf-dressing term); L₋ = σ₁σ₀ is not, and arises only from the γγ cross term φ₁ψ₀.
- With φ₀₁ ≠ 0 the γγ product also reaches e⁻ = σ₀σ₁σ₀; the two-photon span is all of H₃(q).
- No `def:` block for the photon exists; the definition lives inside this proposition's prose.
Owner asked (2026-11-17 06:27Z) that the γγ thread re-run stage 1 over the alphabet the definition gives; request relayed.

### PRE-REGISTRATION 2026-11-17 18:15Z — stage 1 re-run, L₋ = σ₁σ₀, four-term photon (γγ thread)
Pre-registered before any computation. Re-run of gluon-thread stage 1 over the alphabet that prop:gamma-gamma-generates-particles gives (owner query 2026-11-17 06:27Z).
- Alphabet (a): {V, V⁻¹, L₊, L₋} with V = σ₀σ₁⁻¹, L₊ = σ₀σ₁, L₋ = σ₁σ₀ (NOT the inverse σ₀⁻¹σ₁⁻¹ used before). All words of length 1..6 on three strands.
- Alphabet (b): (a) plus e⁻ = σ₀σ₁σ₀, reachable from γγ once φ₀₁ ≠ 0. All words of length 1..5.
- Measured: reading 3 (Frobenius positivity, every level, convention D, proton pin, mpmath 40 dps), components, writhe; for each alphabet the pass count, whether pass ⟺ pure braid still holds, the writhe distribution of passers, the shortest passing word of each writhe.
- Old stage-1 table kept as the record for the inverse reading; this run is reported beside it, not in place of it.
- Questions, no predicted answer: 1. Does pass ⟺ pure survive? 2. Are passing writhes still symmetric, or one-signed (all letters except V⁻¹ are positive)? 3. Does adding e⁻ let any knot (1 component) pass?
- Not allowed: choosing a canonical word, letter or length from these results. This run measures admissibility only; selection is a separate, separately pre-registered step.

### RESULT 2026-11-17 — stage 1b (γγ thread, PR #8128, witness gg-twist-reading3-stage1b)
(a) {V, V⁻¹, L₊ = σ₀σ₁, L₋ = σ₁σ₀}, lengths 1–6: pass ⟺ pure braid survives (1848/1848 pure pass, 0/3612 knots). All writhes ≥ 0, which the alphabet forces (L± both +2). (b) Adding e⁻ = σ₀σ₁σ₀, lengths 1–5: every pure word passes and no knot does, but 526/1771 two-component words also pass, so pass ⟺ pure breaks (shortest: V⁻¹L₋e⁻, L₊L₋e⁻). 274 words sit at a numerical zero (~1e-42, sign flips 40→80 dps) and are counted as failures. Admissibility only; no selection. Bean stays OPEN.

## 2026-11-17 — photon audit (PR #8367, issue #8366)

Owner asked for a single `def:photon` block: γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁ ∈ H₃, three colour weights, bare photon = 1 (empty knot, not 0₁). Audit `docs/audits/2026-11-17-photon-usage-audit.md` lists 12 conflicts. **C8 bears on this bean:** the γγ vertex V = σᵢσᵢ₊₁⁻¹ ("photon + anti-photon") traces to `gamma_gamma_pair_production_decomposition.py`, which takes photon = σ₀, anti-photon = σ₁⁻¹. That is not the photon of `def:photon`, so every γγ-selected word (nucleon words included) rests on an underived vertex. Decision card posted 2026-11-17: re-derive the alphabet from γ(φ)γ(ψ) (recommended) vs keep V. Nothing changed yet. Stays open.

## 2026-11-17 sibling sweep
Scope note only (bean stays OPEN): a sibling measured that the reading-3 whole-word search space is about 1024 candidate words. No word selected.
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.

### PRE-REGISTRATION 2026-11-18 04:30Z — canonical-word reselection from γ(φ)γ(ψ) (γγ thread)
Trigger: owner tapped "Re-derive from γ(φ)γ(ψ)" (n–p thread, 2026-11-17 23:18Z), after audit finding C8 (docs/audits/2026-11-17-photon-usage-audit.md): the vertex V = σᵢσᵢ₊₁⁻¹ came from a script that takes photon = σ₀ plus an "anti-photon" σ₁⁻¹, both rejected by def:photon (PR #8367). Written before any computation.

**Expansion (exact, braid words before any Hecke reduction).** With γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁:
- degree 0: 1
- one photon bare (coefficient has a factor 1): σ₀ (φ₀ + ψ₀), σ₁ (φ₁ + ψ₁), σ₀σ₁ (φ₀₁ + ψ₀₁)
- both photons dressed (bilinear φ·ψ): σ₀² (φ₀ψ₀), σ₀σ₁ (φ₀ψ₁), σ₁σ₀ (φ₁ψ₀), σ₁² (φ₁ψ₁), σ₀²σ₁ (φ₀ψ₀₁), σ₀σ₁σ₀ (φ₀₁ψ₀), σ₁σ₀σ₁ = σ₀σ₁σ₀ (φ₁ψ₀₁), σ₀σ₁² (φ₀₁ψ₁), (σ₀σ₁)² (φ₀₁ψ₀₁).
- **No inverse letter occurs.** V = σ₀σ₁⁻¹ and V⁻¹ are not terms of γ(φ)γ(ψ). Every word built from these terms is a positive braid.

**Letter set (rule A, primary).** The letters are the nine bilinear terms above, i.e. the words that need BOTH photons dressed (a pair-production event). Reason: a term with a factor 1 is one photon passing through unchanged, not γγ. Rule B (comparison arm, labelled, not selectable): all eleven non-identity terms, which generate every positive B₃ word. Rule A is the rule unless the owner picks otherwise on the card.

**Selection (unchanged from qou-ales, FrobeniusSelected).** Candidates: non-empty products of letters on 3 strands, by crossing count up to 12. Feasible: reading 3, χ_λ(w) ≥ 0 on every level with y_λ > 0, convention D, proton pin. Exact zero counts as feasible (≥ 0); a value under 1e-30 is decided by re-evaluating at 120 dps and calling it zero only if it stays under 1e-100 there. Cost: crossing count. Selected: every feasible word of minimal cost — all ties reported, none broken by any residual or measured value.
- Sectors: the nucleon (3 strands; closure has 3 components, any word); recorded, not filtered by, split vs non-split closure.
- Reported per word: letters, braid word, writhe, components, level characters χ₃, χ₂₁, χ₁₁₁.
- Questions, no predicted answer: 1. Which words are selected, and is the minimum split (e.g. σ₀² = Hopf ⊔ unknot)? 2. Does any selected word equal β_Bor up to conjugacy? (It cannot: β_Bor has writhe 0 and every rule-A word has writhe > 0.) 3. Does rule B select a different minimum?
- Not allowed: changing letters, cost, sector or the floor after seeing results; choosing among tied words by Q_β or any mass.
- Downstream: χ₃/χ₂₁/χ₁₁₁ of the selected element go to the Q_β ε thread; the words go to the n–p thread. Q_β = 0.4491 MeV stays provisional.
Bean stays OPEN.

### RESULT 2026-11-18 — stage 7 reselection from γ(φ)γ(ψ) (γγ thread, branch claude/gg-photon-product-selection-2026-11-18, commit 68ef4b266)
Run under the 04:30Z pre-registration: proton pin, convention D, words up to 12 crossings. Near-zero characters were decided exactly with symbolic q. This replaces the pre-registered 120 dps check, which the engine cannot do; the exact test is stronger.

Rule A (pair terms): 8007 braids, 2578 feasible, minimum cost 2. Selected: σ₀² and σ₁², a tie. Both close to a split link (Hopf link plus unknot).
- χ₍₃₎ = q² ≈ 1.2321, χ₍₂₁₎ ≈ 2.0437, χ₍₁₁₁₎ = q⁻² ≈ 0.8117. The last is unconstrained, since y₍₁³₎ = 0.

Rule B (all terms, comparison): minimum is σ₁ (cost 1).

So this grammar and this rule select no nucleon-like element, and β_Bor (writhe 0) cannot be reached. Scope (a). The nucleon element stays underived, and Q_β 0.4491 MeV stays provisional. The owner's card on which letters to use (pair terms / all terms / keep V) is open.

Bean stays OPEN.

### NOTE 2026-11-18 — merges + teraplectic finding (relayed from sibling sweep, re-measured)
- Merged: #8130 (rebase, `73205840a`; Lean source-verified 7/7, standard axioms only) and #8124 (rebase, `7642fc6da`; tower E₀, 0.4491 MeV, marked provisional after the L± ruling). Five-block follow-up: PR #8376 (issue #8375).
- Re-ran `qbeta/qbeta_ruled_base_affine_solve_probe.py` (2/2 pass): reaching CODATA on the ruled assembly needs z = 0.99850030441113. That is not an admissible convention-D root (0.0015 from the excluded z = 1). So the base shortfall cannot be fixed through z; any fix must change the element or the functional. This is consistent with the y₃ reduction: no derived trace reaches y₃ ≈ 0.88.

### NOTE 2026-11-18 09:30Z — option C explored (owner asked for the implications of A/B/C), post-hoc, not a selection
Same FrobeniusSelected rule over {V, V⁻¹, L₊, L₋, e⁻}, braids free-reduced, at most 12 crossings: 4428 braids, 1535 feasible, minimum cost 2, giving σ₀² / σ₁². This is the SAME minimum as rule A, because V·L₋ = σ₀². β_Bor is feasible at 6 crossings but not minimal. So the letter set does not decide the nucleon: under A, B and C alike, the crossing-count minimum is a split pair.

Words that are non-split and three-component appear in the run list at cost 4 and are also rule-A words: σ₀²σ₁², σ₁²σ₀², L₊L₋, L₋L₊, each a 3-ring chain. The cheapest non-split word of any component count is σ₀σ₁σ₀ (cost 3, χ₍₂₁₎ exactly 0).

Owner card posted: whether the nucleon closure must be non-split / three-component. Any filter is to be pre-registered before use. Script: /tmp scratch (ruleC.py); to be committed with the probe if adopted.

Bean stays OPEN.

## 2026-11-18 — γγ as Hecke elements: reachability (measurement, no selection)

Owner asked to explore reading γ(φ)γ(ψ) as an H₃ element rather than as braid words (braid-word reading is positive-only, so β_Bor unreachable). Measured at proton q₀, mp.dps 40 + exact sympy Gröbner (scratch scripts, not committed):
1. β_Bor = λ·γ(φ)γ(ψ) has REAL solutions, e.g. φ=(2.5,−2.124435039,−2.285617294), ψ=(−0.8224825298,0.5366867306,0.7224010393), λ=−2.20056601312; residual 3.9e-37 by direct multiplication.
2. Solutions form a 1-parameter curve: for fixed φ, membership in γ(φ)·span{1,σ₀,σ₁,σ₀σ₁} is 2 equations in φ's 3 weights; λ drops out.
3. Product map has generic rank 6 = dim H₃, so a generic H₃ element is a scalar times some γγ. Reachability does NOT select β_Bor.
4. γ(φ)² = λβ_Bor has no solution (Gröbner reduces to (q²−1)²(q²+1)²(q⁴+1)=0): two different photons are needed.
Implication: any nucleon selection in this reading must come from a pre-registered rule on (φ,ψ), the SDP, or the trace functional; p and n on one element cannot be split by moving along the curve. Stays open.

## 2026-11-18 (later) — exact factorisation of β_Bor into two photons (measurement)

Exact in H₃ for generic q (sympy, symbolic; numerically found first at proton q₀, then identified and verified):
  β_Bor = (σ₀σ₁⁻¹)³ = γ(−qh², 0, qh) · γ(q⁻¹h², 0, −q⁻¹h),  λ = 1,
and each factor is 1 + ε·h·V with V = σ₀σ₁⁻¹ = σ₀σ₁ − hσ₀ (a four-term photon with φ₁ = 0) and ε ∈ {q, −q⁻¹}, the two eigenvalues of σᵢ. Reason: V³ + h²V² − h²V − 1 = (V−1)(V² + (1+h²)V + 1) = 0 in H₃.
Consequences: the old γγ vertex V lies inside the photon (it is the φ₁=0 direction), so the old grammar is partly recovered from def:photon; the two factors commute (both polynomials in V), so photon order cannot split p from n. No three-term (φ₀₁=0) point found numerically. Not formalised in Lean yet. Stays open.

## 2026-11-18 14:10Z — γγ → H H̄ through γp → H e⁺ (owner chose the full-strand hydrogen)

On the card, the owner chose: H = β_Bor on strands 0–2, electron on strand 3, Hopf-linked by σ₂²; H̄ = mirror. Recorded before computing, so this fixes the construction:
- Layout in H₈: strands 0–2 are the proton, 3 the electron, 4 the positron, 5–7 the antiproton.
- ρ: σᵢ ↦ σ₆₋ᵢ⁻¹ (reflect strand order, then mirror). H̄ = ρ(H) = (σ₆⁻¹σ₅)³ σ₄⁻².
- Test: HH̄ = X·ρ(X), with X the γp → He⁺ element. The cofactor is fixed to the mirror, with nothing free.

Result. This is exact, needs no numerics, and holds at any q.
1. σᵢ² = 1 + hσᵢ, and σᵢ⁻² = (1+h²)(1 − h/(1+h²)·σᵢ). The Hopf link is a one-term (degenerate) photon γ(h,0,0), and its mirror is a scalar times one.
2. H uses only σ₀, σ₁, σ₂, and H̄ uses only σ₄, σ₅, σ₆. They commute, so HH̄ = H·ρ(H). The factor test holds with X = H. That makes it VACUOUS: the positron strand 4 enters nowhere.
3. Both photon versions give the same answer, because φ₀₁ = 0 makes the last-term switch inert.

Scope (a): this construction alone carries no information about BFPP vs γγ → HH̄. A non-vacuous test needs a crossing that links the electron and positron strands (σ₃, pair creation), and nothing in the corpus fixes how that crossing is weighted. Do NOT read this as evidence for or against crossing symmetry.

## 2026-11-18 16:05Z — PRE-REGISTRATION: typed crossings on the six crossings of β_Bor (owner asked for this in the thread, 15:59Z)

Recorded before any computation. This is a measurement only. Nothing is selected and no residual is used.

Construction:
- β_Bor = (σ₀σ₁⁻¹)³ in H₃. Strand positions 0, 1, 2 carry flavours. Each crossing permutes the flavours (the permutation is the braid's image in S₃).
- A positive crossing σ_k between flavours (f, f′) is replaced by C(f, f′; σ_k) from def:typed-crossing-operator: uu → σ_k, dd → σ_k − h, ud → σ_k − h/2.
- A negative crossing σ_k⁻¹ is replaced by C(f, f′; σ_k)⁻¹. This choice is mine; the corpus types σ only.
- Every placement is reported: uud with d at position 0, 1 or 2, and udd with u at 0, 1 or 2. No placement is chosen.

Outputs, all exact in q:
1. The six H₃ coefficients of each typed element, and whether the p and n elements differ.
2. Reachability as λ·γ(φ)γ(ψ) for each photon variant:
   - four-term (def:photon);
   - switched last term σ₀σ₁⁻¹;
   - three-term (φ₀₁ = 0, as in prop:gamma-gamma-generates-particles);
   - one-term (one nonzero weight).
   Report existence only, not which (φ, ψ) is "best".
3. tr_M at z_D = q³/(q²+1), evaluated at the proton q₀ with mpmath; the ratio n/p.

No outcome changes the corpus. The corpus nucleon (β_Bor × Δ₃, def:typed-crossing-operator) is untouched.

## NOTE 2026-11-18 16:20Z — one-sided β-flip on β_Bor (exploratory, scope (a))
Owner idea: p and n as conjugate Borromean words differing by a quark/β-decay flip.
Conjugates have equal traces (Δ=0), so the split must be a single one-sided vertex
W ∈ {qJ_i, q⁻¹J_i} (audit 2026-11-15 one-sided weak vertex). Replacing one crossing of
β_Bor=(σ₀σ₁⁻¹)³ by W, Markov trace at z_D, proton pin, exact sympy (2-dim + 1-dim irreps,
y_(1³)=0): Δtr/tr = σ₀: +5.81% (qJ) / −14.12% (q⁻¹J); σ₁⁻¹: +17.56% / −4.58%.
Identical across the three positions of each letter type (cyclic conjugacy), so no uud/udu
asymmetry from position. All 30–125× larger than (m_n−m_p)/m_p ≈ 0.14%. No row selected.
Scratch script /tmp/claude-0/np/flip.py, not committed. Not pre-registered as a selection rule.

## NOTE 2026-11-18 16:40Z — owner idea: nucleon = (σ₀σ₁⁻¹ − X)³ (exploratory, scope (a))
Enumerated 29 parameter-free X (scalars 0,±1,±q,±q⁻¹,±h; σ_i^±1; ±J_i, qJ_i, q⁻¹J_i;
P±_i; σ₀σ₁, σ₁σ₀; V^±1). Markov trace at z_D, proton pin, exact sympy
(/tmp/claude-0/np/cubes.py, not committed). tr(V³)=0.998562163837 matches the closed form.
- Only X ∈ {h, −h, P−₀} keep |tr| within 25 % of tr(V³) (−15.3 %, +21.8 %, −5.7 %);
  every other X moves m_p by O(1).
- Natural p/n pairs (bar partners W_L/W_R, J₀/J₁, σ/σ⁻¹, P±): smallest split is P+₁ vs P−₁
  at +5.9 %; others 26 %–3600 %. Leading order in h is h⁰ or h¹ for all except σ₀σ₁/σ₁σ₀ (h²).
- tr((V − V⁻¹)³) ≡ 0 exactly (V has eigenvalues λ,1/λ on V_(2,1) and 1 on the 1-dim irreps).
None reaches (m_n−m_p)/m_p ≈ 0.14 %. A split that small needs X of size ~h⁴ or a first-order
zero tr(V²X)=0; no parameter-free X here supplies either. Setting X's size from CAL-2 would be
circular for Δ_pn (Q_β = Δ_pn − m_e). No row selected.

## NOTE 2026-11-18 17:05Z — entangled electron loop on β_Bor in H₄ (exploratory, scope (a))
Owner reading: −X = remainder of a previously entangled e⁻ strand (BFPP / γγ→HH̄ topologies).
H₄ Markov trace at z_D (seminormal reps (4),(3,1),(2,2); y=0 on three-row shapes; checked
Markov property and tr₄(β_Bor) = closed form). Loop = σ₂^a … σ₂^b around nucleon letters,
reference = same two crossings adjacent. Scripts /tmp/claude-0/np/loop4.py, dsym.py (not committed).
- Enclosed σ₀ letters commute with σ₂, so only loops enclosing ≥1 σ₁⁻¹ differ from reference.
- Exact: D := tr₄(loop) − tr₄(adjacent) is the SAME for all four (a,b) ∈ {±1}²:
  D = (q²−q+1)(q²+q+1)(q⁶−3q⁴+2q²−2)/(q²+1)³;  D/tr(β_Bor) = −3/4 − ε²/4 + … at q = 1+ε;
  −0.74957 at the proton pin.
- Unweighted loops: O(1) shifts (−66 %, −75 %, −82 % of the reference trace).
- Photon-weighted crossings (1+φσ₂^a)…(1+φσ₂^b): single-crossing terms cancel (Markov z),
  so Δtr/tr(β) = φ²·D/tr(β) exactly. φ = h → −3.28 %; φ = h² → −0.1432 % (≈ −0.144 % in m);
  φ = qh → −4.04 %; φ = q⁻¹h → −2.66 %.
  ⚠ φ = h² lands within ~4 % of |m_n−m_p|/m_p = 0.138 %, but φ is NOT derived; picking φ = h²
  because it matches would be selection against the target. Sign: entangled element is
  LIGHTER, so "neutron = entangled" gives the wrong sign. Recorded as near-match, not a result.

### Result (2026-11-18 16:35Z) — for the pre-registration above
- **tr_M at z_D:** identical for all six placements, q²(3q⁴+2q²+3)²/(q²+1)⁶, which is 0.99991206734 at the proton q₀. Reason: n = (σ₀↔σ₁ flip ∘ word reversal)(p), and the trace is invariant under that map. Under this rule the trace cannot split p from n.
- **Elements:** they differ as elements. For each placement, n is the flip-reverse image of p.
- **Four-term and switched photon pairs** (the same set): reach all six placements. Measured numerically at q = 11/10; n:u@0 follows from p:d@2 because flip-reverse maps photons to photons. Nothing is selected.
- **Three-term photon pairs** (φ₀₁ = 0): reach ONLY the placements with the odd quark in the middle (p:d@1, n:u@1). There are two real pairs each, with the same λ for p and n. Exact Gröbner computation at q = 11/10, 13/10 and 3; for the other four placements the Gröbner basis is {1}. The bare β_Bor is NOT reachable this way.
- **One-term photons:** reach none (only λ = 0).
- **Scope (a):** this is a measurement under one typing rule, and the C⁻¹ choice for negative crossings is mine. The middle-placement result is not a selection of the nucleon.

- 17:30Z owner asked: p/n backwards? Swapping (proton = loop-dressed, neutron = bare β_Bor)
  gives m_n/m_p − 1 = +0.144 % vs measured +0.138 % (4.5 % off). Now TWO post-hoc choices
  (φ = h², assignment), and the swap moves the proton anchor m_p = 2(m_μF_Bor − 6m_e) by
  ≈ −1.35 MeV. Needs: derived φ = h², a reason the closed loop sits on the charged nucleon,
  and an anchor fix from the same reason. Near-match only.

## PRE-REGISTRATION 2026-11-18 17:35Z — photon–electron crossing weight from the γγ factorisation
Rule (stated before evaluating): β_Bor = γ(φ⁺)γ(φ⁻), φ⁺=(−qh²,0,qh), φ⁻=(q⁻¹h²,0,−q⁻¹h)
(PR #8502). An e⁻–nucleon crossing σ₂ is the single-crossing (φ₀) term of one of the two
photon factors, so it carries weight φ₀⁺ = −qh² or φ₀⁻ = q⁻¹h². A loop has two crossings, so
the split is φ_aφ_b·D/tr(β_Bor) with D the exact sign-independent loop coefficient.
All three pairings are reported: (+,+), (−,−), (+,−). Neutron = loop-dressed (no swap).
Known before registration: the φ = h² magnitude match (16:40–17:05Z). NOT known: the sign
under this rule. Caveat: the φ₀₁ (σ₂σ₃) pair term needs a 5th strand (e⁺) and is not included.
RESULT 17:40Z (exact): weights φ_aφ_b = q²h⁴ (+,+), q⁻²h⁴ (−,−), −h⁴ (+,−).
Split (neutron = loop-dressed): (+,+) −0.1764 %, (−,−) −0.1162 %, (+,−) +0.1432 %.
Only the mixed pairing gives a heavier neutron, and it is the bar-symmetric product (q-powers cancel).
Measured (m_n−m_p)/m_p = +0.1378 %; mass-level (+,−) ≈ +0.144 %. Mixed pairing NOT derived:
open whether a closed loop must take one crossing from each factor. Near-match status unchanged.

## PRE-REGISTRATION 2026-11-18 17:45Z — H₅ with e⁺ strand (full four-term photons)
Strands 0–2 nucleon (β_Bor on σ₀,σ₁), strand 3 e⁻, strand 4 e⁺. The two photon factors act
on the lepton pair generators: γ(φ)_lep = 1 + φ₀σ₂ + φ₁σ₃ + φ₀₁σ₂σ₃, φ ∈ {φ⁺, φ⁻} from PR #8502.
Neutron word = β_Bor with γ(φ_a)_lep inserted at slot i and γ(φ_b)_lep at slot j (i<j);
reference = both inserted adjacent at slot i. Split = tr₅(word)/tr₅(reference) − 1, Markov
trace at z_D (y = 0 on three-row shapes), proton pin, exact. Report all (a,b) ∈ {+,−}² and all
slot pairs; no selection. Proton = β_Bor with the same two photons adjacent (= reference).

## PRE-REGISTRATION 2026-11-18 17:55Z — charge-weighted EM dressing (step 2)
Both nucleons = β_Bor (closure permutation is the identity, so strand k = component k).
Photon strand = strand 3 in H₄. Pure-braid generators A₂₃ = σ₂², A₁₃ = σ₂σ₁²σ₂⁻¹,
A₀₃ = σ₂σ₁σ₀²σ₁⁻¹σ₂⁻¹. Loop matrix D_ij := tr₄(β·A_i3·A_j3) − tr₄(β) (ordered, i,j ∈ {0,1,2}).
EM term E(Q) := Σ_ij Q_iQ_j D_ij / tr(β), quark charges u = +2/3, d = −1/3.
Report E for p (uud) and n (udd) at every placement of the odd quark, and
ΔE = E(n) − E(p) for all 3×3 placement pairs. The photon weight w multiplies ΔE; its sign is
not derived (the γγ mixed pairing gave w = −h⁴; same-photon pairings give w > 0), so the
sign test is reported for both signs of w. No selection.

RESULT 2026-11-18 19:05Z (H₅ full four-term photons, pre-registered 17:45Z). Exact sympy, convention D,
evaluated at proton q₀. Quantity: tr(β with photons a,b at slots i<j)/tr(β with a,b adjacent at i) − 1.
All 4 pairings × 21 slot pairs reported in /tmp scratch (h5.out); the value takes only two forms:
  0 when β[i:j] is a single σ₀ (commutes with σ₂,σ₃) or the separation is cyclically trivial;
  otherwise a pairing-only constant, the same for every slot pair:
    (+,+)  +0.30145 %    (−,−)  +0.24474 %    (+,−) = (−,+)  −0.27684 %
Target m_n/m_p − 1 = +0.1378 %. No pairing matches; the mixed pairing that gave +0.1432 % with the
h⁴-only H₄ loop weight changes sign and doubles once the full four-term photon is used, so that
earlier near-match does not survive. None of these splits p from n: slot position does not enter.
Scope (a): this construction alone; not an exclusion of photon dressing.
EM D_ij run (pre-registered 17:55Z) produced no output the first time; re-running.

## 2026-11-18 19:05Z — OWNER WORKING ASSUMPTION: photon last term σ₀σ₁⁻¹ (switched)
Owner, in the n–p thread: "Switched last term seems most promising... let's make a working assumption."
This is a working assumption, not a ruling to edit def:photon. The new photon is γ′(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹.

What changes and what does not:
- **Same set of photons.** γ′(φ₀, φ₁, φ₀₁) = γ(φ₀ − hφ₀₁, φ₁, φ₀₁). Every reachability result over the full family is unchanged, including the typed-crossing result of 16:35Z.
- **Same three-term photon.** With φ₀₁ = 0 the last term is absent, so the three-term variant is identical.
- **What changes:** β_Bor = γ′(0,0,qh)·γ′(0,0,−q⁻¹h). The Borromean core is a product of two photons that each carry ONLY the switched last term, weighted by h·q and −h·q⁻¹ (the two Hecke eigenvalues). Under the old photon the same factors needed φ₀ = ∓q^{±1}h².
- **Mass / L2:** there is no numerical impact on any scored quantity. confinement-universality says the nucleon NF does not depend on the photon coefficients once flavours are supplied. The 16:35Z result shows the Markov trace is identical for p and n under typed crossings. So Δ_pn and the L2 dashboard do not move, and the assumption buys no ppQ by itself. Its effect is on which word class the γγ re-derivation selects. That is the ansatz, and any selection under it still needs pre-registration here.

## 2026-11-18 19:20Z — PRE-REGISTRATION: flavour ingredient A (down quark = reversed strand), then B

Owner tapped "A and B, A first" (19:13Z). Registered before any computation.

Model A, as fixed now:
- u strand oriented +, d strand oriented − (corpus's own motivation in def:typed-crossing-operator). The typed-crossing shifts are NOT used; the orientation replaces them.
- Word: beta_Bor = (s0 s1^-1)^3, unchanged. Its closure is 3 components, one per strand, so a placement = an orientation pattern on the Borromean rings.
- p = uud (one component reversed), n = udd (two reversed). All 3 placements per nucleon are computed.
- Invariants reported, all as functions of the free HOMFLY variable v (no specialisation chosen here, so no selection): (T1) oriented HOMFLY of the closure for every orientation pattern; (T2) the open element in the walled Brauer / oriented skein algebra (H_{2,1} for p, H_{1,2} for n), compared through a quantity that is not a closure invariant, to be named in a second registration before it is computed.
- Prediction stated in advance: if the oriented Borromean rings with different orientation patterns are isotopic (linking numbers are all 0, so at least Jones is orientation-blind by Morton's reversal formula), then T1 gives p = n and only T2 can split them. T1 is run to settle this, not to score.
- Nothing is scored against m_n − m_p until a v-specialisation is derived, not chosen.
- B (one-strand blob / Ariki–Koike generator) follows A, with its own registration.

## 2026-11-18 19:20Z — RESULT T1 (model A, closure): p = n, as predicted

SnapPy 3.3.2, L6a4 (Borromean rings, vol 7.32772475342), all 48 self-isometries with their cusp maps. Among the ambient-orientation-preserving ones (det +1 on every cusp), with meridians sent to meridians:
- identity permutation with meridian signs (1,−1,−1), (−1,1,−1), (−1,−1,1): reverses two components;
- permutation (0,2,1) with signs (1,1,−1), (−1,1,1), etc.: reverses one component.
Meridians go to meridians, so each extends to an isotopy of S³. Hence EVERY orientation pattern of the Borromean rings is the same oriented link (up to permuting components). So uud and udd closures are isotopic and every closed-link invariant (HOMFLY at any v, any specialisation) gives p = n. Scope (b): the invariant is the isotopy itself. Model A survives only as an OPEN-element (non-closure) quantity, T2, to be registered before computing.
Also: sibling PR #8517 `trace_flip_reverse` now proves the reversal invariance my 16:35Z no-go needed (for products of factors α+βσᵢ, any R-linear cyclic trace).

## 2026-11-18 19:30Z — Model A at U_q(sl2): every V-module trace also gives p = n (argument, not yet Lean)

For U_q(sl2) the dual V* is isomorphic to V as a module (φ: V → V*). Braiding is natural, so each crossing satisfies c_{V*,U} = (φ⊗1) c_{V,U} (φ⁻¹⊗1) and likewise for inverse crossings. β_Bor is a pure braid (each strand returns to its slot), so ρ_{uud}(β_Bor) = Φ ρ_{uuu}(β_Bor) Φ⁻¹ with Φ = φ on the d slot, and likewise for udd. Any functional Tr(X·ρ(β)) where X is built from K's on each slot (φ intertwines K) is therefore the same for uuu, uud and udd. That covers the plain trace, the quantum trace and the corpus's K-twisted partial traces. Scope: U_q(sl2) only. A can split p from n only where V* ≇ V, i.e. U_q(gl_N) with N ≥ 3, which introduces N as a choice. Owner decision requested (card), not computed.
(The corpus's n/p = q^∓2 comes from projecting onto different TOTAL-WEIGHT spaces of V^{⊗3}, an isospin projection, not from orientation.)

## 2026-11-18 19:35Z — PRE-REGISTRATION: C (weight-space trace) and B (one-strand blob). Owner: "explore B and C" (19:26Z)

C (registered and evaluated now, because it is exact from existing sorry-free Lean):
- Functional: quantum trace Tr(K^{⊗3} ρ(β)) of the level-2 Jimbo braiding restricted to the (2,1) weight space (p) and to the (1,2) weight space (n), NucleonWeightSpaceTraces.lean.
- trace_word_eq gives equal plain traces for EVERY word, and K^{⊗3} acts by the scalar q on (2,1) and q⁻¹ on (1,2). So n/p = q⁻² EXACTLY for every word, β_Bor included. It does not depend on the word, the photon or the typing.
- At the proton q₀: q₀² = 1.23205..., so the ratio is a 23 % effect, not 0.138 %. Scope (a): as a direct mass ratio C misses by ~170×. Any rescaling that brings it to 0.138 % would be a chosen exponent, i.e. selection; not attempted.

B (registered, not yet computed):
- Algebra: type-B Hecke H₃^B(q,Q): σ₀, σ₁ as in H₃; blob t with (t − Q)(t + Q⁻¹) = 0, tσ₀tσ₀ = σ₀tσ₀t, tσ₁ = σ₁t.
- Flavour: a d strand at slot k carries the type-B Jucys–Murphy loop t_k (t₀ = t, t₁ = σ₀tσ₀, t₂ = σ₁σ₀tσ₀σ₁). p = β_Bor·t_d for d at each of slots 0,1,2; n = β_Bor·t_{d1}t_{d2} for each pair. β_Bor is pure, so t_k commutes past it up to the JM relations; computed as written anyway.
- Trace: Geck–Lambropoulou Markov trace on H^B, z = z_D, tr(t) = y. Q and y stay SYMBOLIC.
- Report: p and n traces and their ratio as exact functions of (q, Q, y), plus whether the result depends on slot (the flip symmetry is broken by construction, since t sits on strand 0).
- Nothing is scored against m_n − m_p until Q and y are derived, not chosen.



## 2026-11-18 21:20Z — Switched Four-Term Photon Factorisation & C+B Weight-Space Quark-Charge Trace Formalised in Lean 4 (`NucleonWeightSpaceTwoTerm.lean` §1–§9, Epic `qou-7xl8`)

Formalised in `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonWeightSpaceTwoTerm.lean` (`868` lines, `0 sorry`, `0 axiom`, `✓ exit 0 — checks` on branch `feat/qou-7xl8-two-term-mass-qed-trace`):

1. **Switched Four-Term Photon Factorisation of `β_Bor = V³ = (σ₀σ₁⁻¹)³` (§9, `borromeanV3A_eq_switched_photon_product`, `borromeanV3B_eq_switched_photon_product`, `borromeanV3A_eq_one_add_h_sq_V_sub_V_sq`, `borromeanV3B_eq_one_add_h_sq_V_sub_V_sq`):**
   - For the switched 4-term photon `γ'(φ₀, φ₁, φ₀₁) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁(σ₀σ₁⁻¹)` (`V = σ₀σ₁⁻¹`), `V³ = γ'(0, 0, +q h) · γ'(0, 0, -q⁻¹ h) = 1 + h² V - h² V²` (`h = q - q⁻¹`) holds identically on both the `(2,1)` proton weight space and the `(1,2)` neutron weight space.
2. **Why Combining C (`(2,1)` vs `(1,2)` Weight Spaces) with the Quark Electric Charge Operator `Q = diag(+2/3, -1/3) = (1/6)I₂ + T³` Splits `p` from `n` Word-Dependently on `β_Bor = V³` (§2–§9):**
   - In entry `19:35Z` above, pure `K^{⊗3}` on `(2,1)` vs `(1,2)` gave a word-independent ratio `q⁻²` because `P(q)` intertwines `A_i` and `B_i` (`NucleonWeightSpaceTraces.trace_word_eq`).
   - However, when the strands carry the Gell-Mann–Nishijima quark electric charge `Q = (1/6)I₂ + T³` (which mixes `ω`-even hypercharge `Y/2 = 1/6` with `ω`-odd isospin `T³`), the adjacent-crossing charge operators `Q₁₂ = Q₁ ⊗ Q₂ ⊗ 1` and `Q₂₃ = 1 ⊗ Q₂ ⊗ Q₃` on `(2,1)` and `(1,2)`:
     - commute identically with their local crossings (`[Q₁₂, σ₁^{±1}] = 0`, `[Q₂₃, σ₂^{±1}] = 0`: `Q12p_comm_A1`, `Q23p_comm_A2Inv`, `Q12n_comm_B1`, `Q23n_comm_B2Inv`),
     - **break** the `P(q)` intertwiner (`intertwine_Q12_ne`, `intertwine_Q23_ne`, `intertwine_QAdj_ne`), and
     - satisfy the exact matrix decomposition `Q₁₂^{(n)} + Q₂₃^{(n)} = (-2/9) I₃ + (1/2)(Q₁₂^{(p)} + Q₂₃^{(p)})` (`QAdjn_eq_static_add_half_QAdjp`).
   - On a single switched-photon fourth term `V = σ₀σ₁⁻¹`, `tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p) = -2(q² - 1)² / (9 q²) = -(2/9)h²` (`trace_QAdjp_borromeanVA`), while the connected neutron trace has the exact opposite sign `tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n) + (2/9)tr(V_n) = +(2/9)h²` (`trace_QAdjn_borromeanVB_connected`).
   - Multiplying by the `h²` two-photon factor in `V³ = 1 + h²(V - V²)` yields the fourth-order `O(h⁴) = O((q - 1)⁴)` connected traces on `β_Bor = V³`:
     - Proton (`trace_QAdjp_borromeanV3`): `tr((Q₁₂^{(p)} + Q₂₃^{(p)}) V_p³) = -2(q - 1)⁴(q + 1)⁴(q⁴ + q² + 1) / (9 q⁶)` (`(1/3)|tr| = 0.00043068`, which in units of `m_e` is `+0.22008 keV`, within `0.36σ` of the `+0.22881 keV` `211 ppb` `μ--p` anchor gap).
     - Connected Neutron (`trace_QAdjn_borromeanV3_connected`): `tr((Q₁₂^{(n)} + Q₂₃^{(n)}) V_n³) + (2/9)tr(V_n³) = +(q - 1)⁴(q + 1)⁴(2q⁴ - q² + 2) / (9 q⁶)`.
     - Connected `(n - p)` difference (`trace_QAdj_connected_diff_borromeanV3`): `(q - 1)⁴(q + 1)⁴(4q⁴ + q² + 4) / (9 q⁶)`.
## 2026-11-19 00:05Z — PRE-REGISTRATION: charge-tensor insertion on the weight spaces (owner pasted agy's two-term discussion, 19:32Z)
- Spaces: Wp = (2,1), Wn = (1,2), matrices A, B of NucleonWeightSpaceTraces.lean; β_Bor = (σ₁σ₂⁻¹)³.
- Charge Q = diag(2/3, −1/3) per strand (an input charge assignment, Gell-Mann–Nishijima; not derived here).
- Reported, exact in q: E_ij = Tr(K^{⊗3} Q_iQ_j ρ(β)) / Tr(K^{⊗3} ρ(β)) for each pair i<j, and the self terms Σ Q_i² (diagonal, word-independent), for p and n.
- This is a measurement of whether the insertion is word-sensitive. No coupling constant is applied and nothing is scored against MeV.

## 2026-11-19 00:10Z — RESULT: charge-tensor insertion
Exact in q (sympy), β_Bor on Wp/Wn:
- Tr_K β: p = −P(q)/q⁵, n = −P(q)/q⁷ with P = q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1; ratio n/p = q⁻² as C predicts. At q₀: 3.32348, 2.69752.
- Pair-resolved E_ij depend on the word: p (−0.002351, +0.001919, +0.000432), each ∝ h³ or h⁴; n (−0.112024, −0.109979, −0.111330).
- But the SUMS are word-independent: Σ_{i<j} E_ij = 0 (p), −1/3 (n), and Σ Q_i² = 1 (p), 2/3 (n), because Q_iQ_j is diagonal and its pair-sum is constant on each weight space. So a uniform Coulomb sum is static charge counting: the braid only redistributes it among pairs. The word can matter only through a pair-dependent weight (a distance or crossing-number kernel), which is underived. Scope (a).

PRE-REGISTRATION 2026-11-18 19:25Z (one-strand marker, owner "go"). Marker = Jucys–Murphy element of
the marked strand, which lives in H₃ itself, so no new parameter: L₀ = 1, L₁ = σ₀², L₂ = σ₁σ₀²σ₁
(strands 0,1,2; β_Bor = (σ₀σ₁⁻¹)³ is a pure braid, so strand k ends at k). Compute exactly at z_D:
  M_k := tr(β L_k)/tr(β) − 1,  k = 0,1,2.
Report all three readings below, for every placement (uud: d at 0/1/2; udd: u at 0/1/2), and
the n − p difference for all 3×3 placement pairs. Charges u = +2/3, d = −1/3. Readings fixed now:
  (A) Σ_k Q_k M_k      (B) Σ_k Q_k² M_k      (C) M_{k_odd} (odd-quark strand only).
No reading is selected after the fact; target +0.1378 % is compared, not fitted. The trace no-go
(PR #8517) does not forbid a split here: L_k is a product of σ's, but θ maps strand k to strand
2−k, so a split must come from comparing different strands.

WITHDRAWN 2026-11-18 19:23Z: the 19:25Z one-strand marker pre-registration above is withdrawn unrun; the owner said "no" to it. Nothing was computed.

PRE-REGISTRATION 2026-11-19 05:10Z (owner "A" + "derive instead of 4 choices"). Charge-insertion EM term, ONE rule, fixed before computing:
  Δ_EM := m_e · [ t(W_n) − t(W_p) ],  t(W_N) := Tr_{W_N}( K^{⊗3} (Q₁₂+Q₂₃) V³ ) / [2]_q³
where V = σ₁σ₂⁻¹ on the 3-dim weight spaces of PR #8518 (NucleonWeightSpaceTwoTerm.lean), K = diag(q,q⁻¹) per strand, [2]_q³ = quantum dim of V^{⊗3}.
Derivation of the weighting (closes #8518's plain/KnKp/Kp3/q menu): convention D's Markov trace IS the U_q(sl2) quantum trace Tr(K^{⊗n}·)/[2]^n (check: Tr_q(σ)/[2]² = q³/(q²+1) = z_D). K commutes with the braid, so restricting to a weight space multiplies by q^{2T³}: q on W_p, q⁻¹ on W_n. No "connected" subtraction, no α_EM factor, no per-anchor normalisation. Target n−p EM part is lattice comparison only (≈ −0.6 to −1.0 MeV); total 1.29333 MeV. Value is reported whatever it is.

RESULT 2026-11-19 05:15Z (rule pre-registered 05:10Z, exact sympy, /tmp scratch emA.py; proton q₀ = 1.1099785827513808, mp.dps 60):
  check: Tr(K⊗K Ř)/[2]² = q³/(q²+1) = z_D symbolically (weighting derived, not chosen).
  t(W_n) − t(W_p) = (2q¹⁴−2q¹²−9q¹⁰+20q⁸−26q⁶+18q⁴−13q²+4) / (9q⁴(q²+1)³);  q→1 limit −1/12 (classical Σ QᵢQⱼ).
  at q₀: −0.0734705048628237;  Δ_EM = m_e·(…) = −0.0375433509 MeV.
  Sign matches lattice (proton heavier from EM); magnitude ~15–25× short of lattice −0.6…−1.0 MeV (comparison only).
  87 % of the value is the q=1 classical charge sum; the q-dependence moves it 12 %.
  Same rule on the bare V³ gives tq(W_n)/tq(W_p) = q⁻² exactly (−18.8 % at q₀), the strong-side 150× problem, unchanged.
  Remaining gap is the ENERGY UNIT of the charge term, not the trace: no trace choice can supply ×15–25; adding α_EM makes it 137× smaller.


## 2026-11-15 — gluon segment by the γγ rule (PR #7876, child bean qou-ggls)

**What the γγ rule gives.** On three strands the rule gives the unit V = σ0σ1⁻¹, which is the corpus gluonUnit. It does not fix how many units the gluon segment carries. The output is therefore the family {V^k}.

**What was enumerated.** CORE·TAIL·V^k for k = 0..3, pre-registered, with the census quark tail held fixed.
- g_odd = 0 for every k, so the qou-z08b obstruction belongs to σ0².
- Whole-word reading 3 admits **k = 1 only**, for both nucleons: χ_(2,1) = +0.2170 (p) and +0.4294 (n).
- Q_β at z_D for that element is 0.229517 MeV (−70.66 %). This is reported only and played no part in any choice.

Nothing is selected or re-scored.

**Owner decisions still open:**
1. Does the γγ rule or the H2-parity rule (σ0², owner 2026-08-30) govern the gluon segment?
2. Does the survivor replace nuc11_interleaved?

This bean stays open (rule 13a).

(Ported to the bean mount 2026-11-20 by W3 from PR #7876, whose bean-file edits cannot merge now that beans are branch-mounted.)

**2026-11-20 (session 01VQDpPd):** measured two ruled-base Q_β elements live on main at once —
content blocks (mass-comparison-table.md:33, neutron-qvalue-symbolic.md:53) score Δ_S, tower E0,
0.4491 MeV (−42.6 %); the L2 scorecard scores nuc11_interleaved, 0.6519 MeV (−16.68 %), which
fails reading-3 SDP on (2,1). Recorded in the scorecard witness as content_blocks_element /
element_conflict_open (PR #8549). Not resolved — still the owner's call. γγ+SDP base search
(qou-ales / qou-vd7j) running on claude/qbeta-gg-sdp-base-2026-11-20.

**2026-11-20T14:40:21Z — OWNER RULING (Carl, session 01VQDpPd): record Q_β = 0 as the γγ base's scope-(a) prediction; derive flavour on the U_q / weight side.**
PR #8564: under γγ words + reading 3 (whole word, every tower level) p and n share the survivor set {V³,V⁶,V⁹}; minimal cost p = n = V³ ⇒ Q_β = 0 on the ruled z_D base (Lean qbeta_delta_vanishes_of_frobeniusSelected, frobeniusSelected_ten_unique). Scope (a): the grammar carries no flavour index; the ruling is not excluded. Assigning different survivors to p and n by Q_β is a fit (not adopted). Next: T³-graded split of the trace on V³ (follow-up task opened). Scorecard unchanged. Bean stays open.

**2026-11-20T14:44:09Z — CORRECTION to the entry above (owner, 15:43).** The "Q_β = 0" result of PR #8564 is for the OLD γγ reading only (GammaGammaWordSelection.GammaGammaWord = products of bare σᵢσᵢ₊₁⁻¹; no colour weights, no chirality). It is NOT the prediction of the canonical four-term coloured photon def:photon γ(φ)=1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁ (#8367), whose two-photon product carries independent chiral L₊/L₋ coefficients, nor of the bar-odd (sinh) channel where Q_β lives. "The grammar cannot separate n from p" was mis-stated. Selection is being redone with the four-term chiral photon + odd channel (branch claude/qbeta-flavour-weight-split-2026-11-20).

## 2026-11-20T14:50:40Z — OWNER RULING (not a working assumption): photon last term is σ₀σ₁⁻¹
Owner (Carl, 2026-11-20 15:47–15:48): "Use γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹ … That was already decided. Why did it get changed back to the wrong form? … Who overrode my decision". The 2026-11-18 19:05Z entry above recorded this as "a working assumption, not a ruling to edit def:photon" — that classification was the recording agent's, and it is why the merged def:photon (8fe7dbecf4, authored 11-17 before the decision; moved to the library e3c658a58b 11-20 07:44; merged in #8367 11-20 08:34) still carries σ₀σ₁. It is now a ruling: def:photon is being corrected (branch claude/photon-chiral-vertex-2026-11-20). All running agents told to use σ₀σ₁⁻¹.

## 2026-11-20 — W2: where the "good" Q_beta came from (measured at the proton pin, 50 dps, CODATA 0.78233341 MeV)
| construction | Q_beta (MeV) | error |
|---|---|---|
| Form A closed form (z = 1 base) | 0.7836458 | +1677.6 ppm |
| + Kashiwara N1, convention C | 0.7823912 | +73.8 ppm |
| + Kashiwara N2, convention C | 0.7823344 | **+1.28 ppm** (the remembered "good" number) |
| + Kashiwara N1, convention D | 0.7828615 | +675.0 ppm |
| + Kashiwara N2, convention D | 0.7828047 | +602.4 ppm |
| D N2 + connected Borromean QED (plain) | 0.7824730 | +178.4 ppm (recorded as a selection, not a prediction) |
| scorecard primary (z_D Markov trace, nuc11_interleaved, two-term) | 0.6515246 | -16.7 % |

The +1.28 ppm needs BOTH a z = 1 base (retired 2026-09-08: not a convention-D Markov trace, fails to annihilate the (1^3) block) AND a convention-C phase (excised 2026-08-15). It also needs N = 2 truncation, a near-match rung. Keeping the base and moving only the phase to D gives +602 ppm. Every admissible D base is below CODATA (F_required > 1), so no cosine ladder can close it (qou-cds1).

**2026-11-20 — flavour weight split + chiral photon (PR #8586, stacks on #8564).** Photon used: γ(φ)=1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹. Arm γ: corpus-derived colour weights (eigenvalue pair) give γ(0,0,qh)γ(0,0,−q⁻¹h)=V³ for p and n ⇒ Q_β=0 for every linear ε; antipode mirror, V⁻³ and photon order are trace-invisible (scope b). Arm W: ε_flavour=ε_n−ε_p of the z_D trace = Tr(K^{⊗3}·)/[2]³ on W_n, W_p; on V³ = (q²−1)P(q)/(q⁴(q²+1)³), exactly bar-odd (bar swaps the T³ sectors), negative on (1,23/20] (Lean FlavourWeightSplit.lean, sorry-free). Q_β = 0.325434 MeV (V³, −58.40 %), 0.323542 (V⁶), 0.320400 (V⁹); tower E₀, 70 dps. Not blind: np-splitting §18 already carries 0.3254 as Δm. Per-sector-normalised split = 0. Owner decisions: D1 adopt ε_flavour as the scored ε? D2 is 0.3254 Q_β or m_n−m_p (the latter forces Q_β<0)? Audit docs/audits/2026-11-20-qbeta-flavour-weight-split.md. Bean stays open (rule 13a).

## 2026-11-20 — W2: epsilon is RULED, not derived (audit docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md)
Delta (typed crossings) is a definition, epsilon a ruling and E0 posited. The mass-channel scale (945.76 MeV per unit trace) applied to this Delta gives ~100-177 MeV, so Delta and E0 are not the mass channel's objects. [corrected 2026-11-20: u and d already exist as separate lines of the (3,1) rep of H4 (QOU/QuarkState); the open step is which label is n<->p and why epsilon is the flavour round trip, audit section 9.]

**2026-11-20T16:55Z — derived weighting implemented across the compute (owner request 16:00; PR #8591, branch claude/two-term-derived-trace-weighting-2026-11-20).**
The 05:10Z pre-registered rule now lives in `computations/two_term_qtrace_weighting.py` (library + producer, witness `two-term-qtrace-weighting.witness.json`, 70 dps, proton q₀) and `lean/QOU/BraidsAndKnots/NucleonWeightSpaceQTrace.lean` (7 theorems, sorry-free, axioms propext/choice/Quot.sound). Reproduced: Δt_adj,raw = (2q¹⁴−2q¹²−9q¹⁰+20q⁸−26q⁶+18q⁴−13q²+4)/(9q⁴(q²+1)³) = −0.0734705048628237, Δ_EM = −0.0375433508915675 MeV.
Symbolic map: 'KnKp' (on the connected traces) = ([2]_q³/3)·Δt_derived,conn EXACTLY — derived weight, wrong normalisation (1/3 vs 1/[2]³; 8/3 at q=1). 'plain', 'Kp3', 'q' are not proportional. On the raw insertion KnKp differs further by the static (2/27)q⁻¹tr(V³). All-pairs: raw −0.0565058628 MeV (q→1 −1/8), connected ≡ 0.
`weighting='derived'` is now the default/only canonical path in canonical_mass, derived_masses, qbeta_utils, qou_substrate.q_two_term_borromean_at, m_p_substrate_identity, free-neutron-decay, two_term_qed_isotope, mass_binding_dashboard, and the L2 scorecard (scored_form two_term_plain_me → two_term_derived_qtrace_me). Moved: M_p^QED,conn +0.2201→+0.0901 keV; Δm_QED^conn −0.3317→−0.1272 keV; m_mu +8.058→+128.0 ppb (miss 37.02→588.1, loses beats-1×); Q_β 1.672e8→1.669e8; m_n 1.392e5→1.390e5; Δ_pn 1.011e8→1.010e8 ppb. q₀ not re-pinned.
Kept unchanged because the corpus does not fix them (owner decision framed in the PR): adjacent vs all-pairs insertion, connected vs raw, sign −m_e·t (compute) vs +m_e·t (pre-registered). Alternatives are unscored labelled rows in the scorecard. Probes (np_two_term_qed_mup_tension, two_term_qed_pair_choice, qbeta_pdix_cds1 bridge) and level1-qvalues (long compute, not re-run) still carry the 1/3 'plain' form as records. Bean stays open (rule 13a).

**2026-11-20: compute, content and Lean on the chiral four-term photon (PR #8595, companion to #8583).** Weights: only the eigenvalue pair γ(0,0,qh), γ(0,0,−q⁻¹h) is evaluated (V³ = γ₊γ₋, exact); 0.0487/0.0978 kept as labelled fits. Moved at q₀: in the knot-operator key table, tr_M(σ₀Tσ₀) → γ₊Tγ₋ (T₁,₀ 1.12809 → 0.99856, and e⁻ appears for T₂,₁, T₂,₂). The "bare photon pair" σ₀² becomes 𝟏 (bare) or V³ (eigenvalue pair). β_Bor reads as 2 photons, not 3 γγ̄ events. In photon_electron, the single-crossing V^k/V̄^k charge-like sign split does NOT survive the four-term photon: all words respond negatively, and absorption passes on all seven. Breit–Wheeler promote/split holds for the σ terms, but a vertex photon spans grades 0–2. tbl:four-term-pair-nucleon-table1-data has no producer; it is reconstructed as γ_straight(0.0487,0.0487,0.02)², and with the ruled photon σ₀ goes 0.09887 → 0.09043 (not edited: the weights are a fit and unsourced; owner call). Content/Lean C1–C4 and C10 are restated on QOU.Photon.photon (lean-direct exit 0, no sorryAx). **Open (gap):** V-word probes are the φ₀ = φ₁ = 0 specialisation, and at the eigenvalue pair tr_M/χ have O(1) first-order sensitivity to the chiral single-crossing part (tr_M 0.53/0.50/0.72/0.75). The corpus has no derived φ₀, φ₁, so a per-probe re-run is blocked on deriving them, not on compute. Re-asking ε-L1 of V is still an owner call. Bean stays open (rule 13a).

## 2026-11-20 — W2 LEAD (not derived): J4 flavour coupling cJ/2 as the chirality expectation y3
QBetaChiralityReduction: Q_beta = (h[2]/2)*y3*E0 for every block-weighted trace. y3 = cS/2 (sigma3 label A) IS Markov z_D (-43%). The label-B analogue y3 = cJ/2 = [2]^2[2]_{q^2}/[3]^2 = 0.892057 gives +0.33% (order-zero E0) / +1.32% (tower E0); CODATA needs 0.8891 / 0.8804. Three candidates were tried, so this is selection against the target until a trace with (3)-block weight cJ/2 on the gamma-gamma four-strand sector is derived. Audit section 8.

**2026-11-20T17:30Z — OWNER RULING (Carl, 16:44): the L2 scorecard scores OPTION 2, the covariant all-pairs insertion Q₁₂+Q₂₃+Q₁₃ with the derived weighting Tr(K^{⊗3}·)/[2]_q³ (PR #8591).** Its connected part is ≡ 0 on V³ (Lean `NucleonWeightSpaceQTrace.deltaT_allPairs_connected_eq_zero`, sorry-free), so every scored two-term row equals its one-term row. Options 1 (adjacent, connected, −m_e·t), 3 and 4 stay as unscored labelled rows. Implemented in #8591 (commits 764f905a1c, e64a4240dc, 5ec37345d6 and later): `insertion=None` + derived = all-pairs is the canonical default in two_term_qtrace_weighting, canonical_mass, derived_masses, qbeta_utils, qou_substrate.q_two_term_borromean_at (pin = one-term proton pin to 50 digits), m_p substrate identity, free-neutron-decay, isotope compute, dashboard, scorecard (scored_form two_term_covariant_all_pairs_qtrace). Scorecard moved main(plain) → adjacent-derived → ruled: m_μ +8.058 → +128.0 → **+211.2 ppb (970.2×, = one-term)**; Q_β 1.672e8 → 1.669e8 → 1.668e8 ppb; m_n 1.392e5 → 1.390e5 → 1.389e5; Δ_pn 1.011e8 → 1.010e8 → 1.009e8; headline 1/6 unchanged. Content blocks neutron-proton-mass-splitting and isospin-mass-split-em-localisation now state the ruled form with a dated note that +0.2201 / −0.3317 keV / 8.06 ppb (0.37σ) were the 1/3-normalised plain adjacent weighting; the probe does not close the μ–p tension. derived_masses default pin moved muon → proton (qou-aj91; Q_β +30.37 ppb rel.). The ruling settles the insertion and weighting of the two-term QED probe only; it derives no non-zero Q_β/Δ_pn contribution, so the open question of this bean (what ε is, and the u/d derivation) is untouched. Bean stays open (rule 13a).

## 2026-11-20 — W2: flavour round trip PROVED (FlavourRoundTrip.lean, sorry-free)
tr(Lu s2 Ld s2) = (q^4+1)/(q^2+1)^2 = the ruled convention-D y3 (label A); tr(Ja s3 Jb s3) = cJ/2 (label B), also via the gamma-gamma vertex. Label B gives Q_beta +0.33% / +1.32%, but J4 labels (3) vs (2,1) = isospin 3/2 vs 1/2, not n<->p. Label C (T3) is the physical n<->p label, and no braid word changes it (qou-0whz C2). Options are in audit section 9; the default is to keep both labels with no ruling.

## 2026-11-20 — W5 (session 01VQDpPf): independent check of #8564 and #8586, and the decision framed

Independent recomputation (own sympy Jimbo Ř on (C²)^⊗3, not the PRs' code), proton pin, dps 60:
- Tr(K^⊗3·)/[2]³ = Markov trace at z_D: verified (tr σ₁ = q³/(q²+1) exactly; Markov property on 1, σ₁, σ₁⁻¹).
- #8564: at H₃, χ_(2,1)(V^k) ≥ 0 only for k = 3, 6, 9 (1.994, 1.977, 1.948): verified. Pair values 0.0182 / 0.0302 / 0.0484 MeV: verified. Q_β = 0 follows from `frobeniusSelected_ten_unique` alone; the stated hypothesis (pairing = altChar) is used only in the vd7j side result. H₆ placement enumeration not re-run. Both probes pass (13/13, 24/24).
- #8586: ε_n − ε_p = (q²−1)P(q)/(q⁴(q²+1)³), exactly bar-odd: verified. |ε|·E₀ = 0.325433928735 MeV (−58.40 %), F_required 2.404: verified. The SIGN of ε flips with K ↔ K⁻¹ (which basis vector is "up"); |ε| does not move. So "ε < 0, neutron smaller" is convention-dependent.
- Lean: both files lean-direct exit 0 against a private rebuilt cone; #print axioms on all declarations: propext, Classical.choice, Quot.sound only.

Decision put to the owner in the session chat (options: strict γγ+reading-3 base, Q_β = 0; base + T³ flavour split, 0.3254 MeV; keep nuc11_interleaved, 0.6519 MeV, fails reading 3; CORE·TAIL·V¹, 0.2295 MeV). Bean stays todo (rule 13a).

### PRE-REGISTRATION ε-L1V (2026-11-20; re-ask ε-L1 of the ruled photon vertex V = σ₀σ₁⁻¹; PR #8616)
- Full text: computations/probes/gg_twist_vertex_channel/PREREGISTRATION.md (commit bc02ecd75c), written before computing.
- Functionals: F1 = ε-L1's multiplicity-trace ε_tr (verbatim); F2 = z_D trace Tr(K^{⊗3}·)/[2]³ split over W_p, W_n (plain-sector difference D = tr_Wn − tr_Wp is the channel's u↔d asymmetry).
- Arms: V-words (V, V⁻¹, V·V³, V³·V, VV⁻¹, V·σ₀); four-term photon at the eigenvalue pair γ(0,0,qh), γ(0,0,−q⁻¹h) and products; symbolic φ₀,φ₁ first-order coefficients.
- Prediction: symmetric everywhere (Hecke image commutes with U_q(sl₂); Δ = σ₀σ₁σ₀ swaps σ₀↔σ₁). No physical target compared.

## 2026-11-20 ~17:40Z — owner picked option B, then: "rulings are only temporary conjectures; formalize first, Lean-prove, derive" (W5, session 01VQDpPf)

Owner chose **B** (γγ + reading-3 base V³ with the T³ weight split of the z_D trace, 0.3254 MeV, −58.4 %), and in the next message said rulings are temporary conjectures. Accordingly the three inputs of Q_β = |ε(Δ)|·E₀ are now Lean conjecture classes, with Q_β derived from them (PR #8617, stacked on #8586; `QOU/QBeta/DecayConjectures.lean`, lean-direct exit 0, no sorryAx):
- C1 `DecayFunctionalIsWeightTrace` (was rulings 09-08 + 11-20), C2 `NucleonElementsAreGammaGammaBase` (V³ for both), C3 `DecayEnergyScale` (posited E₀).
- `qbeta_eq_of_conjectures`: Q_β = |(q²−1)P(q)/(q⁴(q²+1)³)|·E₀; `qbeta_pos_of_conjectures`: Q_β > 0 on 1 < q ≤ 23/20.
Open: derive C1 (weak-vertex amplitude → weight-trace difference), C2 (transport #8564's selection to the weight-space rep; derive per-nucleon photon weights φ₀, φ₁ — only the eigenvalue pair is derived, and it gives V³ for both), C3 (E₀ from the mass channel; scale mismatch 945.76 vs ~4.2 MeV). Dashboard re-score not done: proposed as a row labelled conditional on C1–C3, after #8572. Bean stays todo (rule 13a).

## 2026-11-20 — owner choice "3 2" (W2)
No label ruling: labels A and B stay side by side, and the round-trip theorem is merged (#8615). Label C research, first result (PR #8618, exact probe): quantum-trace restrictions give tau(J) = z_D (whole space), 1/3 (a T3 charge sector), 0 (the nucleon isospin-1/2 block) or 1 (the isospin-3/2 block). Q_beta reads only the weight on the isospin-3/2 block (chi_21(Delta_S) = 0). CODATA needs ~0.889. Next: derive why the decay functional weights the isospin-3/2 channel that way. Bean stays open (rule 13a).

**2026-11-20T18:40Z — OWNER RULING (Carl, 18:27): #8586's T³ weight-split Q_β (|ε|·E₀ = 0.3254 MeV, −58.40 % vs CODATA) is the SCORED Q_β cell.** Applied by the merge queue on PR #8586. PR #8591 (derived weighting, covariant all-pairs two-term rows) keeps both on rebase: the Q_β cell from #8586, the two-term rows covariant (connected part 0 on V³, so two-term = one-term; m_μ +211.2 ppb / 970.2×). Options 1, 3, 4 remain unscored labelled rows. The ruling selects the scored cell only; it does not close this bean (rule 13a: the T³ split's derivation and F_required 2.404 stay open).

**2026-11-20 ~18:00Z (W5):** owner "Go" → dashboard Q_β row now scores option B as CONDITIONAL on C1–C3 (PR #8626, after #8564 → #8586 → #8617): Q_β 0.3254 MeV (−58.4  %, completing the line above), m_n / Δ_pn inherit with a note; nuc11_interleaved kept as the superseded element. Calibrated: closed form vs explicit weight-space traces, gap 1e-72.

## 2026-11-20 ~19:15Z — ε-L1V result: the photon vertex V = σ₀σ₁⁻¹ does NOT break u↔d (PR #8616, draft)

Pre-registered (bc02ecd75c), prediction confirmed. Same functionals as ε-L1: F1 multiplicity-trace ε_tr, F2 z_D trace split over W_p/W_n.
- Arm V (V, V⁻¹, V⁴ both orders, VV⁻¹, V·σ₀, ε-L1 applied order): F1 ratio ε_pn/ε_np = 1 exactly; F2 D = tr_Wn − tr_Wp = 0. Same as L± in ε-L1.
- Arm γ (γ(0,0,qh), γ(0,0,−h/q), γ₊γ₋ = V³, γ₋γ₊): all symmetric.
- Arm φ (symbolic φ₀,φ₁,ψ₀,ψ₁; single γ(φ₀,φ₁,φ₀₁)): first-order u↔d coefficients 0; asymmetry vanishes identically.
- Proof scope (b): F2 in Lean, `QOU.BraidsAndKnots.HeckeWeightSpaceSymmetry` (generic CommRing, q·qi = 1, sorry-free): `trace_ρn_eq_trace_ρp` (Δ = σ₀σ₁σ₀ conjugates W_p's rep into W_n's for every free-algebra element), `photon_symmetric`, `vertex_symmetric`, `trace_vertex` (tr_W V = −h²), `flavour_split` ((qi·tr_Wn − q·tr_Wp) = −h·tr_Wp for every element). F1 by exact basis check on the six standard words of H₃(q) (not in Lean).
- Implication for the scored Q_β cell (#8586, 18:27 ruling): ε_flavour(V³) = (q²−1)P(q)/(q⁴(q²+1)³) is exactly −h·tr_W(V³)/[2]³. Every bit of its n/p asymmetry is the K^{⊗3} weighting h; the γγ element enters only through a u↔d-symmetric trace. So the photon's weights φ₀, φ₁ cannot produce an n−p split when both nucleons carry the same element. Under these functionals a γγ derivation of Q_β can put the n/p difference only in (i) the trace's K-weighting (conjecture C1), or (ii) different elements for n and p (C2), never in the photon channel.

## 2026-11-20T19:45Z — pair-nucleon data table restated with the ruled photon (PR #8629)

Owner 18:22: "pair-nucleon table: restate it with the new photon." `tbl:four-term-pair-nucleon-table1-data` had no producer or recorded weights. New producer `computations/four_term_pair_nucleon_table.py` (exact ℚ(q), proton q₀, 70 dps, 7/7): the OLD form γ_old(0.0487, 0.0487, 0.02)² reproduces all six recorded entries at 3 dp; the ruled photon at the same weights gives 1 1.005→1.004, σ₀ 0.099→0.090 (0.0988698→0.0904259), others unchanged at 3 dp (moves ≤ 4e-4), via γ(φ₀,φ₁,φ₀₁) = γ_old(φ₀ − hφ₀₁, φ₁, φ₀₁). Weights labelled in block + witness: 0.0487 = fit to 2m_e (Breit–Wheeler), 0.02 unsourced; the record pins only a ∈ [0.0486, 0.0490], b = 0.020 on a 1e-4 × 1e-3 grid. Worked illustration, not a prediction. Second column: eigenvalue pair γ₊γ₋ = V³ (no e⁻ term). Nucleon nets 0.999/0.811 photon-independent by construction (confinement universality), not recomputed — no producer for them is on record. Not merged.

## 2026-11-20T21:00Z — R2/R5/R3: n↔p as T⁺ on the U_q side (label C); T(3,5) claims checked (PR #8632, draft)

Owner 18:30 ("Q_β must be DERIVED, not chosen"), routes R2/R5/R3. Pre-registered (`computations/probes/qbeta_r253/PREREGISTRATION.md`, not blind: a symbolic ℚ(q) run came first and is disclosed). Lean `QOU/QuarkState/IsospinRaisingRoundTrip.lean` + `T35WeakVertexTrace.lean`, generic Field, sorry-free, axioms propext/choice/Quot.sound.
- **Charge exclusion of A/B (scope b):** Jimbo Ř commutes with Δ(K), Δ(E), Δ(F) (`Rc_comm_*`), so every Hecke word, the γγ vertex included, preserves charge. Labels A and B are Hecke-internal, so they cannot be n↔p (ΔQ = 1).
- **Label C:** T⁺ = Δ²(E): W₋ → W₊ intertwines H₃ (`Eu_sm1/2`). ε_C(X) = tr_W₋(T⁻T⁺X)/tr_W₋(T⁻T⁺) gives **y₃ = (q²+1)²/(q⁴+4q²+1) = [2]²/([2]²+2)** (`epsC_J1`, same from p). Q_β = 0.588715 MeV (−24.75 %, order-zero E₀) / 0.594552 MeV (−24.00 %, tower E₀). Comparison only, not wired.
- **`isospinHalf_deltaS`:** the isospin-½ part of the round trip does not see Δ_S, so Δ_S lives entirely in (3) = isospin 3/2. On pure isospin-½ nucleons Q_β(Δ_S) = 0. The label-C value comes only from the isospin-3/2 content of the weight space, which makes the typed-crossing Δ_S suspect as the object to difference.
- **`qtrace_J1`:** the full quantum trace (all strands closed by pair creation/annihilation) is exactly convention-D y₃, so label A's z_D is the γγ/cup-cap closure. Label C is that closure restricted to the neutron charge sector with a T⁺ round trip.
- Remaining choices: the state set (full weight space vs isospin ½ → 0); normalisation ε(1) = 1; E₀ (posited); the Δ_S definition.
- **R3:** these hold: 10 letters, knot closure, σ₁³ left-divides (σ₁σ₂)⁵ (6 cofactors). These do not hold as stated: the split is not unique (40 placements) and is not produced by GS reduction; no R2 move exists in a positive word; the quadratic-step count is order-dependent (25/30); tr_zD((σ₁σ₂)⁵) = q²(q¹²+q⁸−1)/(q²+1)² ∉ ℤ[q^{±1/2}] (`zD_T35`); B_n W ≠ c·B_p. The block's Q formula is not defined under convention D. A dated authorNote was added to `beta-decay-skein-properties.ts`.
Bean stays open.
- Addendum (relation to #8616 `flavour_split`): T⁻T⁺ on W₋ is the commutant element [2]²P₃/₂ + P₁/₂ (`FE_quad`), not a Hecke element. ε_C is n/p symmetric (`epsC_J1_from_p`, consistent with `trace_ρn_eq_trace_ρp`) and uses no K-weighting. It fixes only the block weights y₃:y₂₁ = [2]²:1. The n/p difference enters only through the element Δ_S (channel (ii)), and `isospinHalf_deltaS` shows that element is invisible on isospin ½. A γγ derivation still needs an n/p-distinct element that reaches the isospin-½ block.

## 2026-11-20 — photon colour weights φ₀, φ₁: what forces them (PR #8634, Lean sorry-free, scope stated per item)
Photon γ(φ)=1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹. Lean `QOU/QuarkState/PhotonColourWeightConstraints.lean`.
- NF(β_Bor)=[1−h⁴,−h³−h⁵,h³,−h²,h²+h⁴,0]: e⁻ coordinate 0, so EVERY factorisation γ(φ)γ(ψ)=β_Bor has e⁻ channel φ₀₁ψ₀+φ₁ψ₀₁=0 (`FactorsBorromean.eChannel_eq_zero`). The e⁻ needed for Q_β cannot come from factorising β_Bor, whatever φ₀, φ₁ are.
- Factorisation alone does NOT force φ₀=φ₁=0: measured 8 solutions at h=1/2, 2/9, 3 (probe `computations/probes/photon_colour_weights_solution_set_probe.py`, mpmath 60 dps); 2 = Borromean pair, 6 have φ₀,φ₁≠0. Proved: φ₁=0 ⟺ ψ₀=0 on the solution set, and either forces the Borromean pair with vertex weights {qh, −q⁻¹h}.
- Bar image of a photon is a photon iff φ₀+φ₁=0; bar-closed pair + factorisation ⇒ Borromean pair (`borromean_of_barClosed`, needs h≠0, h²+2≠0). Then e⁻ channel = φ₀₁ψ₀−φ₀ψ₀₁.
- Flip (Δ-conjugation) closure forces φ₀₁=0; three-term photons never factor β_Bor (scope b, certificate h²(h²+2)=0). Neutral in trivial+sign blocks forces φ₀₁=0, φ₀+φ₁=0 (same no-go).
OWNER DECISION: is "bar image of a photon is a photon" an admissible premise? Yes ⇒ φ₀=φ₁=0 derived. No ⇒ φ₀,φ₁ underived (8-point set; picking by residual would be a fit). Default if no answer: nothing changes; φ₀,φ₁ stay recorded as underived. Bean stays open (rule 13a).

## 2026-11-20T21:10Z — R4 (energy conservation) and R1 (four-strand γγ process), PR #8623 (draft)
Pre-registered at 3e41aab22b. Lean `QOU/QuarkState/DecayGammaGammaFourStrand.lean` (generic Field, 26 theorems, sorry-free, axioms std only); probe `computations/probes/qbeta_derivation_r4_r1/` 20/20 at 70 dps, proton q₀. Nothing wired.
- R4, mass channel (S = 2m_μ[3]!/q³ = 945.764 MeV/unit trace; full z_D trace of V³ returns the pinned m_p). With equal plain traces on T³ = ±½ for every X ∈ H₃ (#8616), the only readings give: sectors/[2]³ → τ_n = q⁻²τ_p, Q_β = −73.32 MeV (`qbeta_sector_neg`: Q_β < 0 for all q > 1); sectors/own dim or full trace + u↔d → Q_β = −m_e. Scope (b) on three strands. Label A/B lines: rel. diff +0.00591 / −0.01704 (diagnostic only; need 1.378e-3).
- R1: d→u flip functional on H₃ NF words (1,σ₀,σ₁,L₋,L₊,e⁻) = (0,0,1,q,q,q²) (`flip_pair`). At the derived weights the pair is V³, e⁻ coordinate 0, V³ flips at order h³ (q²h³·eS); round trip (q²h³)²y_D. Label B: Ja·γ(φ) = t(φ)Ja, so Ja·Γ·V₄·Jb = t(φ)t(ψ)q·eJ and t = 1: label B's cJ/2 is independent of the γγ pair.
- Closed form for every reading (order-zero E₀): Q_β/m_e = (q+1)(q²+1)/(2q³)·y₃. y₃ = y_D → −43.2 %; (q²h³)²y_D (γγ base, label A) → 5.6e-5 MeV (−99.99 %); cJ/2 (label B, pair-independent) → +0.33 % (selection against target, as before).
- Remaining choices (none selected): flavour label; round trip vs amplitude and return path; scale E₀ vs S; Δ_S prefactor h[2]/2; φ₀, φ₁. Bean stays open (rule 13a).

## 2026-11-20T18:20Z — owner rulings D1 = A, D2 = Q_β applied; PR #8586 merged (b47929e610)

- **D1 = A (owner, 18:25).** Scored Q_β on the L2 scorecard = |ε_flavour(V³)|·E₀^tower = **0.325433929 MeV (−58.402 %)**: ε = T³ weight split of the z_D trace Tr(K^{⊗3}·)/[2]³ on W_n − W_p (global [2]³), element V³ = (σ₀σ₁⁻¹)³ (γγ + reading 3, #8564), proton q₀. `per_observable_100x_status.py::_qbeta_ruled_base` evaluates it from q₀, calibrated against `probes/qbeta_flavour_weight_split`. nuc11_interleaved (0.6519) and Δ_S (0.4491) kept as unscored history cells; `element_conflict_open` resolved.
- **Rows moved** (scored = two-term primary, one-term + Δm_QED −0.3317 keV): Q_β 0.65152 → 0.32510 MeV (1.672e8 → 5.844e8 ppb); m_n 939.43461 → 939.10819 (1.392e5 → 4.866e5 ppb); Δ_pn 1.16252 → 0.83610 MeV (1.011e8 → 3.535e8 ppb). HEADLINE 1/6 unchanged.
- **D2 = Q_β (owner, 18:27).** Not m_n − m_p; implied m_n − m_p = 0.8364 MeV (−35.3 %). Recorded in np-splitting audit §23 and in `neutron-qvalue-symbolic` / `mass-comparison-table`.
- **Still open (rule 13a, bean stays todo):** the mass-ordering sign (neutron sector smaller under mass ∝ trace); F_required ≈ 2.40 is outside the cos-ladder cap, so no c_k ladder of that form closes the 58 % gap.

## 2026-11-20T19:25 — OWNER RULING (Carl): the premise "the bar image of a photon is a photon" is REJECTED
Answers the OWNER DECISION of the PR #8634 entry above. Verbatim intent (relayed by coordinator, 19:25): reject the premise.
- Consequence: `borromean_of_barClosed` (#8634) stays a proved conditional, but its hypothesis φ₀+φ₁=0 is NOT a corpus premise. φ₀, φ₁ are NOT fixed to 0; they stay underived inside the 8-point factorisation set of β_Bor (2 Borromean-pair points + 6 with φ₀,φ₁≠0). Selecting a point by residual is a fit and is forbidden.
- `eChannel_barClosed` (determinant form of the e⁻ channel) is therefore not the e⁻ channel of the corpus photon.
- Owner direction in the same message: pursue N1 — derive the W as a CHARGED element and the β-decay electron channel, so Q_β (re-aimed 19:33: the decay AMPLITUDE M(q) and RATE 𝔇_n(q)) is derived from γγ / gauge-boson production, not chosen. Branch `claude/qbeta-n1-charged-w-element-2026-11-20`.
- Per owner rulings-are-conjectures preference: the rejection is recorded as a ruling about admissible premises, not as a derived statement. Bean stays open (rule 13a).

## 2026-11-20 ~20:00Z — N3: Q_β / 𝔇_n as a T⁺ matrix element (PR #8639, draft; not merged)
Lean `QOU/QuarkState/TPlusChargedCurrentElement.lean`, sorry-free; probe `computations/probes/qbeta_n3/` 15/15. Pre-registration committed before any number.
- FORCED: normalised |⟨p|T⁺|n⟩|² equals the T⁻T⁺ eigenvalue: 1 on isospin ½, [2]² on isospin 3/2 (`tplus_norm_sq` + `Fd_eq_transpose`). It does not depend on any invariant normalisation.
- FORCED NEGATIVE (scope b; invariant: T⁺ intertwines σ₁ and σ₂): every H₃ operator, β_Bor = V³ included, has the same spectrum on n and on T⁺n (`hecke_energy_transport`). So the bimodule produces no Q_β and no energy scale. G_F does not emerge.
- Leptonic factor: the charge-exchange amplitude of the weak insertion −h·P_L on one quark–lepton crossing is −h·q/[2] when the quark strand is on the left and −h·q⁻¹/[2] when it is on the right (`exchange_quark_left/right`). This is −tanh(λ)e^{±λ} with λ = ln q. It is O(h) as q→1 and vanishes iff h = 0. Bar maps the left amplitude to minus the right one.
- |M|² at proton q₀: 0.01332 / 0.00877 (isospin ½, quark left / right); 0.05385 / 0.03547 (isospin 3/2). Comparison only: 𝔇_n/m_e = 1.466e-24.
- Open choices: (1) quark-strand placement; (2) isospin ½ vs 3/2 (Δ_S lives on 3/2); (3) current–current factorisation; (4) every energy or rate scale. Bean stays open (13a).

## 2026-11-20 — W2 cross-workstream briefing (owner: "make sure they know")
Full briefing: PR #8526 comment 7047864732 and docs/coordination/2026-11-20-w2-qbeta-ud-briefing.md. Record: docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md sections 1-11.
Key points: Q_beta = (h[2]/2)*y3*E0 and sees only the isospin-3/2 block. The ruled epsilon (z_D, -43%) = label-A round trip = whole-space quantum trace. Label B (J4, strand-4 gamma-gamma) gives +0.33% and is NOT adopted (it labels isospin multiplicity, not n<->p). Label C gives 1/3, 0 and 0.202, none close. The owner made no label ruling ("3 2"). u/d are separate lines of the (3,1) rep of H4, not orientation-only (def:up/down-quark are stale). Convention-D volumes lie past the Phi_q pole. The six-term -2.43e15 was a truncated divergent series (fixed). The +0.17% / ~1 ppm Q_beta values and the April BW run are superseded or circular.

### 2026-11-20 ~20:30 — N2: n and p as distinct γγ-selected elements? (PR #8636, branch claude/qbeta-n2-derived-nucleon-elements-2026-11-20)

Pre-registered (eb81985791) before any number. Selection = γγ words (products of V_i = σ_iσ_{i+1}^{-1}, k ≤ 5 vertices) + reading 3, minimal non-zero cost. A nucleon label can enter only through a STATE-WEIGHTED reading 3 (choice S-w): tr(Π^λ_s ρ(w)) ≥ 0 on the H₃-isotypic blocks of the nucleon's own weight space s. The ruled reading 3 has no state argument, so it selects the same word for n and p by definition.

- PROVED, scope (b), three strands: `QOU.QuarkState.NucleonStateWeighted.isoChar_eq` / `feasible_iff` (lean-direct exit 0, axioms propext/choice/Quot.sound). Invariant: the unitriangular D = [[1,h,qh],[0,1,h],[0,0,1]] intertwines the H₃ action on W_n and W_p and carries the (3)-projector. Every isotypic character of every 3-strand word is equal on n and p, so S-w selects the same element. Extends #8616 from plain to isotypic traces.
- FOUR STRANDS, choice C-lep (strand 4 = lepton doublet, T³=0 space = N ⊕ P with N = n⊗ν = span(uddu,dudu,dduu), P = p⊗e = span(duud,udud,uudd); σ₃ maps N→P with no T⁺): exact probe over Z[q,q⁻¹], 62 words, 17/17 checks. All 57 strand-4 words have DIFFERENT characters on N and P, yet at the proton q₀ the feasible sets agree word-for-word. Selected for BOTH: {V₁V₂ = σ₁σ₃⁻¹, V₂V₁} (tie, 4 crossings).
- The coincidence is q-dependent, not structural: it holds on (1, q*) with q*⁶ − q*² − 1 = 0, q* = √(plastic number) = 1.150963925. Above q*, p's selection moves to {V₁³, V₂³}. q₀ = 1.10998 < q*. Lean: `charP3_nonneg_iff`.
- So no distinct n, p ELEMENTS at q₀; the selected-element difference is 0, hence ε_C(Δ) = 0 and R1 Q_β = 0. The n/p difference lives in the STATES: on the selected word the isospin-½ character difference is −(q²−1)(2q⁴+q²+1)/(q²(q⁴+q²+1)) = −0.264586341842031 at q₀ (`stateDiff_21`), first order in q−1; the (3) difference is (q²−1)(q²+1)²/(q⁴+q²+1) = 0.308292550374553.
- Charge-conserving amplitude for N1/N3: ⟨P|σ₁σ₃⁻¹|N⟩ = [[1,(q²−1)/q,0],[0,1,0],[0,0,0]], |·|² = (q⁴+1)/q², non-vanishing at q = 1 (σ₃ → swap).
- Remaining choices: S-w itself; C-lep; the tie {V₁V₂, V₂V₁}; whether "nucleon element" may include a strand-4 letter. Bean stays open (13a).

## 2026-11-20T22:30Z — N1: charged W exchange and the n → p e⁻ ν̄ amplitude M(q) (PR #8638, draft)
Pre-registered at 5ab8166249. Lean `QOU/QuarkState/ChargedCurrentW.lean` (generic Field, sorry-free, lean-direct -DautoImplicit=false exit 0); probe `computations/probes/qbeta_n1_charged_w/` 26/26 exact + 70 dps, proton q₀. Nothing wired.
- **W = the h term of the strand-tracked crossing.** P·Ř = R₀ + h·E⊗F for σ, R₀' − h·F⊗E for σ⁻¹ (`Rc_strand`, `Rcinv_strand`). The Ř off-diagonal is a transposition (no flavour change; that is what qou-g0jn RESULT 1 measured). Chiral: σ gives d ν → u e⁻ = h, σ⁻¹ gives 0 (`beta_vertex_pos/neg`). Not bar-closed: σ ↦ σ⁻¹ sends +h·E⊗F to −h·F⊗E. Charge conjugation swaps the two (`chargeConj_EF`).
- **T⁺ derived from the lepton crossing the nucleon.** ASSUMPTION (flagged, as g0jn PRE-REG 3): the lepton is a 4th strand, a second doublet, ν = u, e⁻ = d. The block n⊗ν → e⁻⊗p of σ₁σ₂σ₃ is exactly (q²−1)·Δ²(E) = h·q·T⁺ (`beta_amp_left_pos`). The general rule h·q^{N_d−1}·Δ^{(n)}(E) is measured for n ≤ 5. The same braid gives 0 for p e⁻ → n ν; the leftward negative passage gives 0; the rightward negative gives −(h/q)·T⁺, the bar image of hq (`bar_coupling`).
- **|M|²:** T⁺ᵀ = T⁻, so ‖Av‖² = (q²−1)²‖v‖² on isospin ½ and (q²−1)²[2]² on isospin 3/2. Vanishes ∝ h² at q→1 (4(q−1)²). Strictly increasing for q>1. d ln|M|²/d ln q = 4q²/(q²−1) = 21.24 at q₀. No definite bar parity (bar = mirror passage, ratio q⁴). At q₀: (q²−1)² = 0.053848; mirror 0.035474.
- **Rate family** 𝔇 = G²|M|²m_e⁵f(W₀)/(2π³), F = 1. G does NOT emerge (dimensionless construction) — gap. Q_β from the same construction: label C (T⁺ round trip, posited order-zero E₀) 0.588715 MeV → f = 0.5382, d ln f/d ln Q = 3.87 (Sargent Q⁵ only for W₀ ≫ 1). d ln 𝔇/d ln q along label C = 16.20. Owner-scored 0.325434 → f = 0.05679.
- Comparison only: implied Λ = G^{-1/2} = 68.27 GeV (label C) / 38.91 GeV (scored), against the Fermi scale 292.8 GeV. With imported G_F, 𝔇/𝔇_n = 2.96e-3 / 3.12e-4 (𝔇_n = 7.493e-25 MeV). The standard Fermi+GT factor 1+3λ² ≈ 5.8 is absent (no spin sector).
- Not derived / remaining choices: lepton-as-doublet-strand; which passage (hq or −h/q) is physical; G scale; GT part; the γγ e⁻ = σ₀σ₁σ₀ coordinate is NOT where the electron sits here (photon weights φ do not enter). Bean stays open (rule 13a).

## 2026-11-20 — fundamentals walk (PR #8662, audit §13)

- The chain Frobenius pairing → mass identity (ordered holonomy) → `feynman-categorical-trace` DERIVES ε = z_D, given C = Rep(SU_q(2)). Q_β is −43.16 % (order-zero E₀) / −42.59 % (tower E₀).
- Closed form for SU_q(N), with a = q^N: |ε_N(Δ_S)| = (h²/2)·coth(N ln q). Proved sorry-free in `QuantumTraceFamilyCoth.lean`.
  - N = 1 is the augmentation, +12.47 %.
  - N = 2 is z_D.
  - N = ∞ is the standard trace, −88.3 %.
  - No integer N lands. The diagnostic real N* = 1.126 is not adopted.
- The framed mass gives σ and σ⁻¹ the same value, 1/[2], so Δ vanishes under the braid-class mass definition. Q_β here is a writhe effect; this is a tension in the definitions.
- The scale is not on the chain. On z_D, CODATA needs 1.7592 × E₀. The mass-channel scale sends Δ to 100.5 MeV.
- So the gap points at the scale, not the functional. Still open.

### 2026-11-20 ~21:00 — Q_β from U_q(gl₂) outside H_n (PR #8661, branch claude/beta-rate-qbeta-energy-beyond-hn-2026-11-20)

Owner asked (~20:15): derive Q_β as an energy, consistent with the q-rate, with nothing chosen. **Result: not derived.**
- Derived: the amplitude (q²−1)T⁺ = Ad_K(T⁺) − T⁺. So the rate's q-dependence is the Cartan charge 2 of T⁺ (e^{2λ}−1, λ = ln q). It contains no MeV scale.
- Scope (b): twist, Casimir and anything central agree on n and p (`eigen_eq_of_commute`). n⊗ν and p⊗e⁻ lie in one K^{⊗4} weight space (`exchange_preserves_weight`). So any K-weighted 4-strand split, and any one-coefficient linear Cartan energy, gives Q_β = 0. The scored 0.3254 MeV (#8586) is the quark-only half of a conserved quantity, and is non-zero only because the lepton strand is kept out of the K-grading (a premise).
- Scope (a) table at proton q₀: h·E₀^tow = 0.8838 MeV (+13.0 %), 2 ln q·E₀^tow = 0.8822 (+12.8 %), h·m_e = 0.1068 (−86.3 %). These are one cell, since h = 2 sinh λ. They need a scale, the log/linear choice, and the lepton strand dropped. **Not a lead.**
- Lepton strand under the #8586 functional: |ε_ℓ|E₀ = m_e(q+1)/(q(q²+1)) = 0.4395 MeV, which is not m_e. The additive (ε_q − ε_ℓ)E₀ = 0.114 MeV needs m_n < m_p and m_e < m_ν.
- E₀: E₀·g = m_e only for g = q(q−1), the K-gap between q² and q, which no doublet carries. Still posited (qou-mkm8).
Lean `QOU/QuarkState/CartanEnergyTransport.lean` (generic Field, sorry-free). Probe `computations/probes/qbeta_uq_energy/` 14/14. Audit `docs/audits/2026-11-20-qbeta-energy-outside-hn.md`. Bean stays open (13a).

### 2026-11-20 ~21:00 — Q_β from U_q(gl₂) outside H_n (PR #8661, branch claude/beta-rate-qbeta-energy-beyond-hn-2026-11-20)

Owner asked (~20:15): derive Q_β as an energy, consistent with the q-rate, with nothing chosen. **Result: not derived.**
- Derived: the amplitude (q²−1)T⁺ = Ad_K(T⁺) − T⁺. So the rate's q-dependence is the Cartan charge 2 of T⁺ (e^{2λ}−1, λ = ln q). It contains no MeV scale.
- Scope (b): twist, Casimir and anything central agree on n and p (`eigen_eq_of_commute`). n⊗ν and p⊗e⁻ lie in one K^{⊗4} weight space (`exchange_preserves_weight`). So any K-weighted 4-strand split, and any one-coefficient linear Cartan energy, gives Q_β = 0. The scored 0.3254 MeV (#8586) is the quark-only half of a conserved quantity, and is non-zero only because the lepton strand is kept out of the K-grading (a premise).
- Scope (a) table at proton q₀: h·E₀^tow = 0.8838 MeV (+13.0 %), 2 ln q·E₀^tow = 0.8822 (+12.8 %), h·m_e = 0.1068 (−86.3 %). These are one cell, since h = 2 sinh λ. They need a scale, the log/linear choice, and the lepton strand dropped. **Not a lead.**
- Lepton strand under the #8586 functional: |ε_ℓ|E₀ = m_e(q+1)/(q(q²+1)) = 0.4395 MeV, which is not m_e. The additive (ε_q − ε_ℓ)E₀ = 0.114 MeV needs m_n < m_p and m_e < m_ν.
- E₀: E₀·g = m_e only for g = q(q−1), the K-gap between q² and q, which no doublet carries. Still posited (qou-mkm8).
Lean `QOU/QuarkState/CartanEnergyTransport.lean` (generic Field, sorry-free). Probe `computations/probes/qbeta_uq_energy/` 14/14. Audit `docs/audits/2026-11-20-qbeta-energy-outside-hn.md`. Bean stays open (13a).

## 2026-11-20 — Gamow–Teller / spin sector of the β rate (PR #8670, branch claude/beta-rate-gamow-teller-spin-2026-11-20)

Owner ask (~20:15): derive the rate as a function of q, nothing chosen. #8638 gives a Fermi-only |M|² = (q²−1)²; this entry covers the factor 1+3λ². Pre-registered at 43739c0575.
- Corpus: no object carries Lorentz spin. The one U_q(sl₂) doublet is used as isospin in #8638 and is called "spin" in spin-labels / q-angular-momentum. QuarkStrandConsequences Result 1 allows at most one q-braided factor. AxialCoupling.lean (5/3·tr ratio) and gt_matrix_pslq_probe ([5]_q/[4]_q) select against the target 1.2754, so they are not used.
- (A) Factorised iso⊗spin, spin braided by the swap: λ ≡ 0 for every q, including q → 1. Lean: `crossing_commutes_spin`, `swap_commutes_sym`. Scope (a): crossings of this form give no axial current.
- (W) Unfactorised U_q(gl₄), u labels ranked first: quark-level block h·P_spin = (h/2)(1+σ⃗·σ⃗), so λ_q = 1 exactly. Lean: `beta_block_isoMajor`, `swap_fierz`, `beta_block_zero_of_lt`. The other 20 orderings give no block in σ (4) or a partial, rotation-violating one (16).
- (W) nucleon level, CONDITIONAL on the C-SU6 nucleon choice: |λ| → 5/3 at q → 1. At q₀ the u↑u↓d↑d↓ ordering gives λ_⊥ = 1.66744, λ_z = 1.66295 and R = 9.328; anisotropic, with a (σ_N×σ_ℓ)_z term at O((q−1)²). The u↑/u↓ order changes λ (not pre-registered). Against PDG (comparison only): +30.6 % in λ_eff, +58.6 % in R.
- Choices still open, each with no derivation: (1) where spin lives, (A) or (W); (2) the gl₄ label ordering; (3) the N/Δ separation inside the q-symmetric 20; (4) the lepton premise inherited from #8638. Bean stays open.

## 2026-11-20T23:40Z — the lepton-strand premise of N1 (PR #8673, `LeptonStrandPremise.lean`, 28 decls, sorry-free)
- Given L (the lepton is a V-strand in the same K-grading), ν=u and e⁻=d are DERIVED by total-T³ conservation and by GMN with one Y (Y=−1). Swapped labels and a singlet lepton are EXCLUDED, scope (b).
- L itself is UNDERDETERMINED. The corpus defines leptons as knots (trefoil, unknot) and β⁻ as the L₀⁻ smoothing.
- The left line does NOT select the passage. σ and σ⁻¹ are scalars on the same line. W_L flips flavour in both strand orientations. W_R = q²·W_L.
- Only left+ ((q²−1)T⁺) and right− (−((q²−1)/q²)T⁺) carry a β block. The corpus positive electron braid σ₁³ selects left+ (C-lep), via a bridge that is not proved.
- γγ e⁻ = σ₀σ₁σ₀ closes to ≥2 components, T(2,3) to 1. These are different objects.
- With #8661: L ⇒ the K-weighted Q_β = 0. Without L, the 0.3254 cell stands, but #8638/#8636 lose their derived labels.
- OPEN, owner: adopt L or reject it (framed in the #8673 body). Bean stays open.

## 2026-11-20 — option 1 attempted: is E₀ on the chain? (owner "Try"; PR #8662, audit §14)

Scope-(a) negative.
- E₀ = m_e c_q² ℏ_q exactly: the chain's 𝔈 = 𝔪 c_q² times an extra "per tick" ℏ_q that no step of the chain supplies. CODATA needs 1.7592 ℏ_q instead.
- At single wrap, Δt/t_p = −0.341, against a physical 0.00138 (248× smaller). So any scale shared between the nucleon and Δ overshoots:
  - 320 MeV (linear);
  - 531 MeV (Frobenius norm ⟨x,x⟩);
  - 100 MeV (mass channel).
- Q_β needs a scale decoupled from the nucleon mass. Which m_e·ℚ(q₀) element that is, and why, is open.

## 2026-11-20T21:30Z — up-quark (unknot) vs electron-knot ("shares trefoil") clash, investigate-and-propose (PR #8677)

Owner asked to investigate the clash surfaced by #8673. Audit doc `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`, no content changed.
- 13 sites call the up quark an unknot in B3 (def:up-quark, def:down-quark, rem:knot-particle-dictionary, conj:borromean-quark, categorical-proton, particle-nf-table, ParticleKnots.lean); 14 call it T(2,3) (def:electron-knot + .lean docstring, torus-knot-prime-powers, generation/building-block tables, strangelet blocks, jet-planck spectrum, transfer-matrix appendix, TorusKnot.lean:74 docstring).
- No owner ruling, no deriving Lean (knot-type theorems are rfl on structure defaults), no producer consumes a quark knot type.
- Structural (b, given Borromean reading): B3=(s0 s1^-1)^3 is pure (borromean_perm_eq_one) => each closure component is an unknot, so a B3 quark cannot be a trefoil. Strand-deletion step not formalised.
- "Lepton descent" (u <- T(2,3)) refterms the jet-level descent homomorphism; no derived knot->quark map. Undefined relation.
- Options A (reword electron block: trefoil = up quark's lepton partner; 4 files), B (A + 13-site sweep, rescopes transfer-matrix appendix and strangelet), C (trefoil canonical, drops Borromean model), D no-op (default). Agent recommendation (judgement): A now, B separately.
- OPEN, owner. Adjacent: sdp_gamma_gamma_to_qqbar.py:15,124 says s0s1s0 closes to a trefoil, contradicting perm_e_gg; unchanged.

## 2026-11-20T22:30Z — hypercharge as a second strand grading (PR #8676, `HyperchargeGradingNoGo.lean`, sorry-free)
- Owner Q: under L, is ν "the same as u" or at a higher q power? Test: dress strands by q^{cY} (Y_q=1/3, Y_ℓ=−1). Coordinator redirect recorded in PREREGISTRATION.md.
- No-go, scope (b), invariant = separability (T³ on flavour, Y on type): `total_eq_iff`, `T3_Y_conserved`, `split_zero_of_total`, `grouplike_weight_eq` — every grading that is a function of conserved totals gives split 0 for EVERY c. Y(nν)=Y(pe)=0.
- Matrices: `EF_commutes_dressed`, `EF_commutes_charge` (total Q conserved), `Rc_intertwines_dressed`, `weight_transport`.
- Ruled functional blind to c: `normalised_trace_dressing_cancels` (per-strand scalar cancels in Tr(K·)/Tr K).
- Only a per-strand UNnormalised additive energy separates: `split_eq` (g_ℓ−g_q)(q−q⁻¹); `split_hyper_eq_zero_iff` zero iff c=0; q=e^λ: −(8c/3)λ²+O(λ³). This is NOT the ruled ε; it is a new premise.
- Forced c: none (Y open in eightfold-open-problems; gl₂ centre K₁K₂ = q on every fundamental strand). c=1 = electric-charge grading, a premise. No Q_β number computed (pre-registered).
- Candidates not conserved by the vertex: Higgs vacuum idempotent e_H (HiggsVacuumResidual.lean, no strand action defined); colour (no colour action on strands; ColourBridge only q=1). OPEN.

## 2026-11-20T22:30Z — owner ruled OPTION B on the up-quark/electron knot clash (PR #8677, now ready, not merged)

Applied: def:electron-knot (+ TorusKnot.lean:74, categorical-proton.lean docstrings) says the trefoil is the up quark's LEPTON PARTNER; the 5 tables, transfer-matrix appendix (3 blocks), strangelet (2), torus-knot-prime-powers, jet-planck, knot-formula-table (+tbl 2: quark genus/crossings now 0, as ParticleKnots.UpQuark), unmapped-torus-knots reworded; argument-bearing blocks carry dated refined-framing authorNotes (assumed / still valid / needs re-scoping); sdp_gamma_gamma_to_qqbar.py:15,124 comments fixed (perm_e_gg). Lean-direct exit 0 on 3 docstring-only files.
CORRECTION of my 21:30Z note: "no producer consumes a quark knot type" was WRONG. Meson/weak-isospin cluster gives quarks T(2,n) writhes ±3/5/7 and proves things about it: WeakIsospinT3Grading, MesonOperatorSelectionT3, MesonFluxTubeReduction, MesonFusionIndexSelection, lepton-meson-torus-knot-dictionary.lean; meson_braid_length_cap_probe.py -> meson-braid-length-cap.witness.json; weak-isospin-t3-grading.witness.json; knot-notation-convention. NOT changed (report-before-change). m_K/m_π credited Lean unaffected.
OPEN, owner: (i) re-read |κ| as the lepton partner's crossing count (relabel; all theorems kept) [agent recommends, judgement]; (ii) rebuild on single crossing letters; (iii) default no-op = two quark models in the paper.
Not run: qa-sweep (light platform lacks fast-xml-parser), precision-gates (timeout; comment-only compute change). Bean stays open.

## 2026-11-20T20:15Z — P1/P4: β decay as ONE GS reduction in H₆ (PR #8681, draft; pre-reg c59f09c7fb)

Owner 20:52 local: "a beta decay is not standalone … a Gröbner basis calculation". Words: β_Bor=(σ₀σ₁⁻¹)³ on strands 0–2 (n and p are one element, #8636), pair Γ=γ(φ)γ(ψ) on 3–5 (owner photon, φ symbolic), bridge letters. Exact H₆ engine on T_w, validated vs #8634 NF(β_Bor), pairNFChiral e⁻ coord, BorromeanMarkovTrace; ρ(word)=ρ(NF) checked. Probe 25/25, witness proton q₀ 70 dps.
- P1 cross term C=tr(W)−tr(β)tr(Γ)tr(bridge) is identically 0 for split, one bridge σ₂, clasp σ₂², β σ₂Γσ₂^{±1}, shared strand (H₅): every connected-sum assembly factorises (scope b, Markov multiplicativity; exact, not Lean). Non-zero only when a bridge strand wraps ≥2 strands of the other side: loop round 2 nucleon strands O(h⁵), round 3 / passage-and-return O(h⁶), single passage O(h²). Even then C=κ(q)·tr(Γ) (pair joins at one strand); only two pair strands wrapping (W4b) give a genuine pair functional, e⁻ coefficient ∝ −h²·tr(β)·…. All flavour-blind (same element for n,p).
- Energy E_N=m_μ|tr|[N]!/q^N: S₆=47391 MeV/unit; E(e⁻_BW)=327, E(e⁻_K σ³)=146 MeV ≫ m_e. Q principal = −30 GeV … +28 GeV; S₆·C = 9.85 (W3), 3.12 (W4/W6), −940 (W7) MeV. None near 0.782, none selected.
- P4 (Jimbo, lepton=second doublet, #8638 assumption): K-weighted sector trace (sums to the z_D trace, Lean `qtr_markov`) gives n⊗ν = p⊗e⁻ for the split word and ≠ for EVERY entangled word (incl. a single σ₂); kernel `secDiff_H2`: separation = h × σ-coefficient = the strand-tracked W term. Q₄ = S₆·Δ̂ = 180 MeV … 6.7 GeV. Escape from the factorisation no-gos is real in states, not in elements; no MeV-scale functional emerges.
- OPEN: what energy functional is additive across subsystems (trace is multiplicative, so "same functional on initial and final" is not an energy balance); whether the lepton strand count/scale S_N is admissible at all.

## 2026-11-20 P3: energy as Δ of a normal-form invariant (PR #8682, draft)
Owner 20:52 ("higher q power"?). Pre-reg `7f9016bf4e`. Lean `QOU/QBeta/NormalFormLengthInvariants.lean` (sorry-free, generic ring): GS rewrites at any position preserve the T_w coefficient vector in H₃ (`eval_quad`, `eval_braid`), so leading Bruhat length, χ = Σc_w q^{ℓ(w)} (index character = q^{writhe}) and corpus E_gs = Σ|c_w|ℓ(w) are rewrite-order independent; the R3 step count (25 vs 30) is not.
- χ(p) = q²·χ(n) in both typed models (Lean short model): proton two q-powers higher; = Cartan charge 2 of T⁺ (#8661).
- V³ (γγ base, n = p): Δ = 0 for every invariant. Leading length never separates n, p.
- Decay Δ: Δℓ_lead = 1 (e⁻ = σ₁³) or 3 (σ₁σ₂σ₁); Δlog_q χ = 5 (typed) / 3 (V³).
- Required κ/m_e (comparison only): 1.53099 (Δℓ=1), 0.51033 (Δ=3), 0.30620 (Δ=5) vs Q 0.78233; no corpus scale per unit exists.
- One linear scale on χ-degree has a sign conflict (p higher but lighter; e⁻ at +3, massive). Scope (a).
- Side: `beta_decay_energy_negative` (E_gs daughter < parent) holds in the short model (−0.209), fails in the 11-letter model (+0.064), equal on V³.

## 2026-11-20T21:45Z — P2: e⁻ν̄ pair as ONE word entangled with the proton (PR #8680)

Leptons from the knot blocks (e⁻ = σ³ trefoil, ν̄ = 1-strand unknot); exact conv-D Markov trace over ℚ(q); 777 six-strand final-state words, proton pin 70 dps. Audit `docs/audits/2026-11-20-beta-entangled-lepton-pair.md`.
- Clasp σ₁^{±2} multiplies ANY 2-strand trace by λ₊=(q⁴+1)/(q²+1), λ₋=(q⁴+1)/(q²(q²+1)) (Lean sorry-free, `QOU/QBeta/EntangledLeptonPairTrace.lean`).
- Leptons attached through ONE nucleon strand are nucleon-blind: tr(W)/tr(N) identical for p, n, β_Bor in 9+729+27 words (connected sum; families A,B proved by Jones multiplicativity, C measured). Only a full twist on ≥2 nucleon strands + e⁻ is nucleon-sensitive (12/12); its trace cross term ∝ q⁶−1 (ν̄ unlinked), → 0 at q→1.
- Trace channel |tr|[N]!/q^N extended uniformly (my extension; corpus defines N=3 only): E(ν̄)=m_μ/q₀=95.19 MeV, E(n)−E(p)=−72.92 MeV, X∈[8.5e3, 8.3e4] MeV, Q∈[−8.3e4, −8.8e3] MeV vs CODATA 0.78233. Scope (a). Volume channel gives e⁻, ν̄ zero; entangled volumes not computed (no SnapPy).
- Linking letters are chosen: the corpus writes the pair only as ⊔. Still open; not closing.

## 2026-11-19 — PR #8518's "70–76% of the N=2 residual" is measured on the retired base

Probe `computations/probes/np_two_term_qed_mup_tension_probe.py`, run on main. Its `Q_N2^D` is `Q_A·cos(α−u/2)·(1−u²)` with `Q_A` = Form A (z=1, 0.7836458 MeV); only the phase uses z_D. The N=2 residual there is +600.6 ppm (0.00046988 MeV). The four DERIVED-Bor-V3-Conn weightings (−0.000332 to −0.000368 MeV) cut it to 177–130 ppm, i.e. 62–78%. On the ruled z_D base the same terms close 0.10–0.11% of the gap (order-zero E0, Q = 0.4447004, gap 0.3376 MeV) or 0.25–0.28% (dashboard cell 0.6518563, gap 0.1305 MeV). Four weightings of one term plus ~30 other candidates are listed, so taking the best match is selection against the target. Not a closure on the ruled base.
## 2026-11-21 01:10Z — RESULT B (one-strand blob), sample point q = 11/10, Q = 3/2, y = 1/3 (exact rationals)
Method: Ariki–Koike seminormal representations of H₃^B for all 10 bipartitions (relations checked symbolically); Geck–Lambropoulou trace weights solved from the Markov conditions (z = z_D, tr t'_k = y), unique at n = 2 and n = 3.
- tr(β_Bor) = 0.99900075 (matches the type-A value at this q, as it must).
- One loop (p, d at slot 0/1/2): tr(β·t_d)/tr(β) = y EXACTLY for every slot. A single blob only multiplies by y.
- Two loops (n): slots (0,1) 0.106602, (1,2) 0.116568, (0,2) 0.106602, against y² = 0.111111. Slot-dependent, so the flip symmetry is broken, as expected.
So B can separate p from n, but the split is set by the free blob data (Q, y), which nothing in the corpus fixes. Scope (a): B is a parametrised ingredient, not a derived split. Nothing scored. Symbolic (Q, y) run not done (timed out); scripts in session scratchpad blob/.

2026-11-21 01:20Z — corpus search for the energy unit of the charge term (owner "go").
- Only derived assignment found: PR #8518's own Lagrangian bridge (CategoricalLagrangianTwoTermBridge.lean, hadronicScale_mul_q_sq_hbar_eq_me): matter/charge term unit = E₀·ħ_q = m_e/q². With the 05:10Z rule: Δ_EM = −0.0305 MeV (smaller still). Not a new choice: it is the unit that bridge already states.
- The same obstruction is already on record for ³H/³He: docs/audits/2026-06-03-em-linking-invariant.md names the missing object as "a categorical brane-separation / nuclear-charge-radius length scale" (3.2× factor = r_strong/r_charge). The nucleon EM gap is the same class.
- Other corpus energy units (E₀, α_bind = 8G·m_e) exist but none is derived as the unit of a Coulomb term; choosing one by its result would be a fit. Not computed.
- Status: OPEN. Needs a derived categorical length (or crossing-energy) scale for the nucleon. Not closable by trace or weighting choices.

## 2026-11-21 — owner option 1 applied: meson/weak-isospin quark 3/5/7 are lepton-partner labels (PR #8698)

Owner ruling 2026-11-21 (option 1 of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md` §"Still open"): the ±3/±5/±7 carried by quarks in the meson cluster is re-read as the LEPTON PARTNER's crossing count (generation label); the sign is the quark strand's crossing orientation. Prose and docstrings only.
- Lean (all lean-direct exit 0, `-DautoImplicit=false -s 65536`, imports Mathlib only): WeakIsospinT3Grading, MesonOperatorSelectionT3, MesonFluxTubeReduction, MesonFusionIndexSelection, lepton-meson-torus-knot-dictionary.lean. No theorem statement or def body changed; none asserts a quark is a torus knot (all are integer arithmetic). Identifiers `signedWrithe`/`genWinding`/`quarkTorusIndex` kept as names.
- `scanPair_four_not_dictionary_index` ("4 is not a quark index"): premise lost as a statement about quarks; dated docstring note, kept.
- For the owner: `CanonicalWeakIsospinFromBowtie.writhe_magnitude_is_generation` can no longer be met by a quark strand's own net crossing (±1); only via the partner label. Docstring note added, statement unchanged.
- Content: dictionary prop+proof+authorNote; knot-notation-convention (+table 1 charm row); also q-chromaticity and strangelet-merger-signature (two quark=trefoil sites #8677 did not list), with re-scoping flags.
- Compute: meson_braid_length_cap_probe docstring only — the 14-crossing cap premise is not supplied by the ruling; scriptHash drift, not re-run. weak-isospin-t3-grading / meson-braid-length-cap witnesses untouched.
- m_K/m_π row unaffected: per_observable_100x_status.py reads none of these files or witnesses.

## 2026-11-21 — route Y: Higgs-vacuum Yukawa-type pairing with doublet strands (PR #8694, draft)
Owner route Y. Pre-reg `76ddb991d3`. Lean `QOU/QuarkState/YukawaVacuumPairing.lean` (sorry-free, generic field; axioms propext/choice/Quot.sound). Probe 23/23, witness proton q₀ 70 dps.
- Forced: an operator commuting with the unbroken grading is weight-diagonal (`eq_diag_of_commute`); a trace-1 idempotent is P_u or P_d (`idem_commute_trace_one`). tr e_H = 1 puts the vev in a grading-weight-0 slot (`vev_charge_zero_of_trace_one`); impossible on bare q^{2T³} (`no_vev_on_bare_T3`).
- Type-blind pairings (one morphism on all strands) give split 0 (`split_typeBlind`). Compressed a·1+b·Ř: diag(a, a+bq) vev d, diag(a+bq, a+b(q−q⁻¹)) vev u. General diagonal: split = (a_q−b_q)−(a_ℓ−b_ℓ), 4 free.
- Charge selection (only non-type-blind candidate): q^{3Q}-invariant 2-point pairing with the neutral vev vanishes on charged slots — quark couplings 0 (`pairing_quark_zero`), e⁻ 0 (`pairing_lepton`), ν free (`nu_coupling_free`); split = y_ν² (`split_neutral`), order q⁰, ≠ 0 at q=1. Gives energy to ν: opposite of SM (needs a right-handed singlet the strand model lacks).
- No magnitude forced → no Q_β number (pre-registered). Comparison only: CODATA Q_β/m_e = 1.53099. Premise L assumed in arms 3–4, still open.

## 2026-11-21 (PR #8699): E_gs β-decay sign, short model only
The P3 side finding about `beta_decay_energy_negative` is resolved in Lean: the vacuous existential is removed and replaced by the sorry-free short-model statement E(p) − E(n) = −|h|. It does not bear on Q_β. The sign is model-dependent (11-letter +0.064, V³ 0, per #8682), so nothing about which nucleon element is canonical follows. Nothing wired.

## 2026-11-21 owner rulings (routes V/L/W/Y)

- **V (#8699): merged** (4bd48b65ca). Vacuous `beta_decay_energy_negative` replaced by the proved short-model theorem E(p) − E(n) = −|h|.
- **L (#8693): STOPPED as an energy theory** (owner option 3) until the nucleon and lepton words are derived. κ·log|tr| is additive for every κ, so it fixes neither scale nor sign; +E₀ gives Q = −0.489 MeV. PR stays draft as a recorded result.
- **W (#8696): all four words kept open** (D mirror-vertex grammar, A V₁³, B passage σ₀σ₁σ₂, C σ₂). Owner asked for the implications of each and which can be ruled out; follow-up agent dispatched.
- **Y (#8694): owner asked whether a right-handed singlet strand is consistent with physics**; answered in chat, no ruling yet.
- #8698 (meson cluster, option 1) merged with the conjecture restated (option A): κ = ε · partnerCrossings.

- **Correction (owner, 2026-11-21 04:52 CET):** route L is **HELD, not stopped by ruling**. The entry above ("STOPPED as an energy theory (owner option 3)") overstated it. L is paused pending derived nucleon/lepton words; κ's sign and scale stay open choices, nothing ruled against the route. Same correction posted on PR #8693.

## 2026-11-21 — order of an n/p splitting (PR #8714 merged, audit §15)

- Every n/p construction on record (Δ_S, the #8636 state split) is O(h) relative to the nucleon. The O(h) term comes from a writhe change: uu→dd lowers w by 2.
- γγ words have writhe 0. Between two such words of equal strand count, a trace difference is a link-invariant difference. For knots V(1)=1 and V′(1)=0, and the x^k coefficients are integer Vassiliev invariants (Jones; Birman–Lin), so the difference starts at order ≥ 2.
- At q₀, x = 0.232. The physical ratio would need |d_k| of 0.026 (k=2), 0.11 (k=3), 0.48 (k=4) or 2.0 (k=5), so orders 2–3 are excluded as leading terms. This is heuristic: the tail is not small.
- Test for any future γγ n/p pair: a single-scale route with no E₀ needs n and p to be Jones-equal through x³.
- Still open.

- **2026-11-21 (PR #8704, branch claude/beta-em-self-energy-split-2026-11-21) — pairwise EM escapes the β conserved-charge no-go (proved), but only in the static part the scored two-term convention discards.** Lean `QOU.QuarkState.PairwiseChargeEnergyBeta` (sorry-free, generic field). #8676's no-go assumes an energy that is a function of the total of a per-strand additive SEPARABLE charge. A pairwise energy w·Σ_{i<j}Q_iQ_j + s·ΣQ² = (w/2)Q_tot² + (s−w/2)ΣQ², and ΣQ² is additive but not separable (Q² = (T³+Y/2)² has a T³·Y cross term), so the n⊗ν − p⊗e⁻ split is (s−w/2)(Q_u−Q_d)(Y_ℓ−Y_q) = (2w−4s)/3 at SM charges (`uniform_split`, `uniform_split_SM`; zero iff w = 2s). Two weights: w_L − w_N/3 − s_q/3 − s_ℓ (`twoWeight_split_SM`); nucleon-only −w_N/3 − s_q/3 < 0 for w_N>0, s_q≥0 (`nucleon_em_split_neg`: EM makes p heavier, physical sign). Corpus two-term term: the covariant all-pairs insertion is a scalar on each weight space (−1/3 on n⊗ν, −1 on p⊗e⁻ with a spectator lepton strand, premise E1, [2]_q⁴ normalisation E2), raw split −2P/(3q²(q²+1)⁴) (`covariant_raw_split`), connected identically 0 (`covariant_connected_split`, `connTrace_smul_one`): the 'connected' subtraction removes exactly the pairwise EM term. Numbers (proton q₀, 70 dps, m_e·t, + sign; − sign is the negation): nucleon all-pairs raw n−p −0.0565059 MeV (−4.37 % of CODATA m_n−m_p 1.29333); β covariant raw +0.0623804 MeV (7.97 % of Q_β 0.78233); adjacent comparison raw +0.0107875, connected +0.000390788 MeV. DERIVED: charge structure, quantum-trace weighting, covariant all-pairs (owner-ruled). SELECTED/not fixed: coupling w (never derived; NeutronProtonEMSign), raw vs connected, overall sign of m_e·t, lepton-strand extension E1/E2, w_N vs w_L. Not identified with Q_β.

## 2026-11-21 — owner "1 2": correction to the entry above, Lean, γγ beyond 4 strands (PR #8721 merged, audit §16)

- **CORRECTION** to the "order of an n/p splitting" entry above. "γγ (writhe-0) differences start at order ≥ 2" holds for KNOTS only. Measured exactly (3 strands up to length 7, 4 strands up to length 6):
  - tr_{z_D} = 2^{−(n−c)}(1 + (2w − 3·lk)e + O(e²)), with e = q − 1.
  - So a difference in c gives order 0, and a difference in lk gives order 1.
  - The test "Jones-equal through x³" stands, because it already requires equal c and lk.
- **Lean** (`CrossingChangeTrace.lean`, sorry-free):
  - g² = hg + 1 ⇒ g⁻¹ = g − h;
  - tr(agb) − tr(ag⁻¹b) = h·tr(ab).
  - The closed first-order formula is NOT proved (no braid / Ocneanu infrastructure in Lean).
- **γγ beyond 4 strands:**
  - Reading 3 has no nucleon argument, so it gives the same word for n and p on any strand count (scope b).
  - #8636's split above q* has 2 vs 4 components and fails at order 0.
  - S-w on 5–6 strands was not run: no ruling fixes how the lepton pair attaches.
- Still open.

## 2026-11-21 — scoreboard on the two-term Lagrangian trace, every row (PR #8723)

Owner, 04:57: *"Update the scoreboard to use the two-term Lagrangian trace."* Every row of `per-observable-100x-status` now records how the two-term object reaches it, in `two_term_entry` and `summary.two_term_coverage`:
- mass_decomposition: m_p (anchor, unscored), Q_β, m_n, Δ_pn.
- q0_pin_only: m_μ, α_em⁻¹, m_K/m_π. The row's own QED term is `not_defined`: muon carrier (qou-6gf9); no meson QED operator on V⊗V*; α_em is a coupling.
- not_defined: m_e (CAL-1 unit).
α_em⁻¹ and m_K/m_π are switched to `two_term_covariant_all_pairs_qtrace` with `one_term` kept. **No scored value moved**: the covariant pin equals the one-term pin (`deltaT_allPairs_connected_eq_zero`), asserted to 1e-65. Scoreable count is 1/6 before and after. Unscored adjacent-pin alternatives: α_em⁻¹ 30.895 ppb (derived weighting) and 75.970 ppb (#8554 plain); m_K/m_π 53.283 and 55.889 ppb. Already stale before this PR: docs/precision-goals.md:55 and the AGENTS.md precision section quote the old trio miss factors.

- **2026-11-21 route Y step 2 (#8694): "find e_R in corpus".** Corpus-grep (6 paths + corpus-search CLI) found 8 candidates. One qualifies: the right line (−q⁻¹ eigenline, corpus `rightLine`) of the Jimbo crossing on (matter strand)⊗(Higgs strand), spanned by s = q·ud − du. Lean `QOU/QuarkState/RightHandedSingletChannel.lean` (sorry-free, generic Field): one line (`functional_eq_of_rightLine`), T³ = 0 with additive hypercharge (`singlet_weight_hypercharge`), qdim 1 (`qtrace_PR`), weak insertion blind (`weak_insertion_kills_singlet`); channel charges lepton⊗Φ̃ → −1 (e_R), quark⊗Φ̃ → −1/3 (d_R), quark⊗Φ → 2/3 (u_R), lepton⊗Φ → 0 (ν_R) = B2 right-handed row (`channel_charges`). Probe 26/26 also shows s is a genuine U_q(sl2) singlet (ΔE s = ΔF s = 0). Forced: vertex shape up to one scalar per channel. Free: y_u, y_d, y_ν, y_e and the strand order. Split (one-term qtrace; two-term forms add only pair terms, so identical) = (y_d²−y_e²)/(q²+1) + (y_ν²−y_u²)q²/(q²+1) (matter left; swap entries if Higgs left); equal strengths → 0. At proton q₀: q²/(q²+1) = 0.551981855026…, 1/(q²+1) = 0.448018144973…. No Q_β number. Fails: H₄ (3,1) right line (no T³), mirror/bar (doublet→doublet), σ₀σ₁⁻¹ (operator), sign block (Λ³V=0), Gen1Quark labels, Furey (literature). OPEN, owner call: whether to read this two-strand channel AS e_R (makes e_R a lepton⊗Higgs composite); framed in the PR #8694 body. Default: nothing adopted.

**2026-11-21 ring-coloured trace of the Borromean nucleon (owner question "why not a trace on the Borromean ring with the strands?", PR #8706).** Pre-registered 390bd49834. τ_c(V³) = Tr(K^{⊗3}P_c ρ(V³))/[2]³, c ∈ {u,d}³, Jimbo level 2, corpus normalisation [2]³. Lean `QOU/BraidsAndKnots/BorromeanRingColouredTrace.lean` (sorry-free, lean-direct exit 0): (1) six closed forms, e.g. τ_udu = q⁴/(q²+1)³, τ_uud = −q⁴(q²−2)(q⁴−q²+1)/(q²+1)³; not constant on a class. (2) NOT a link invariant, scope (b): conjugating by the pure braid σ₁² (same closure) moves ⟨udu|V³|udu⟩ by −(q−1)³(q+1)³(q⁴+1)(q⁴−q²+1)/q⁸ (`tauP_not_conj_invariant`); invariant = the strand-tracked crossing P·Ř = R₀ + h·(W exchange) (`strand_crossing_pos/neg`), so flavour is not constant along a component; "flavour of a ring" is a boundary condition on the open braid. RT/Habiro colours components by reps; u,d are weights of one rep. (3) The two invariant versions both give τ_p = q²τ_n (P3's χ(p)=q²χ(n) ratio): class sums = the already-scored ε_p, ε_n (`sum_tauP_eq_epsP`, `epsP_V3_eq_qsq_mul_epsN_V3`), Q = 0.3254339287 MeV (tower E₀) / 0.3222390832 (order-zero E₀), −58.40 / −58.81 % vs CODATA — no new number; W-free strict colouring (each ring keeps its flavour): amplitude = 1 because every strand pair crosses once with each sign (lk = 0, `strictAmp_V3`), n−p = −3q²(q²−1)/(q²+1)³, Q = 0.3260658647 / 0.3228648153 MeV (−58.32 / −58.73 %). (4) flip u↔d = mirror + bar (`flip_diag`). (5) Two-term: covariant all-pairs insertion is a scalar per class (0 on W_p, −1/3 on W_n) so its connected part is 0 colouring by colouring; adjacent (non-covariant, labelled) weights colourings (2,−4,2)/9 and (−1,−4,−1)/9 and sums to deltaT_adjacent_connected_eq. Probe 16/16. Nothing adopted; no colouring selected.

## 2026-11-21 — photon colour weights do not separate n and p (PR #8705, branch claude/nucleon-photon-colour-weights-np-2026-11-21)

Owner 2026-11-21 chose both arms. Photon γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹ throughout. Pre-registered before compute (computations/probes/nucleon_photon_colour_weights/PREREGISTRATION.md); predictions P1–P5 held, P6 held (adjacent differs).

**Arm 1 (8-point set, PR #8634).** Re-solved at the proton pin q₀, 70 dps: 8 points, 4 real (Borromean pair in both orders; two non-trivial real points, φ₀+φ₁ = −0.01785 and −0.01787), 4 non-real (two conjugate pairs). As q → 1 every point shrinks like h; the two non-trivial real points merge into the Borromean pair (their φ₀, φ₁ are O(h²)).
- Rule R-pt (proton pair = point i, neutron pair = point j, all 64): every product is β_Bor (4.5e-69). Nothing separates n and p, to all orders. Definitional (factorisations_same_functional).
- Rule R-maj (X_p = γ(w_u)γ(w_d), X_n = γ(w_d)γ(w_u), all 120 photon pairs): the elements differ (pair_comm_e; O((q−1)³)/(q−1)⁴ for real photons), but every character agrees (chi*_pair_comm, proved), hence T₁, ε_C and the D1=A split agree. The split ε_n(X_n) − ε_p(X_p) = (q⁻¹−q)·tr_W(X)/[2]³ ranges −0.07590 … −0.07827 over the real rows against V³'s −0.07698: the colour weights move the common element's trace, not the n−p mechanism (that is the K^{⊗3} weight, present at φ = 0).
- Scored two-term covariant all-pairs connected term: 0 for EVERY element (Q_pair scalar on W_p, W_n), proved in allPairs_connected_zero_P/N; measured ≤ 3e-72 on all 256 products. It does not become non-zero for φ ≠ 0.
- Adjacent Q₁₂+Q₂₃ (labelled, non-covariant, not scored): differs under R-maj, order (q−1)³ or (q−1)⁴; includes the V³ baseline 2.49e-4.

**Arm 2 (reading 3 with φ symbolic).** Reading 3 is flavour-blind by definition. One photon: χ₃ = 1 + q(φ₀+φ₁) + φ₀₁, χ₂₁ = 2 + h(φ₀+φ₁) − (1+h²)φ₀₁ — only φ₀+φ₁ enters (chi_photon_shift), and the whole line γ(t,−t,0) is feasible (reading3_line_nonneg). On pair products χ is order-symmetric. Measured: of 256 products of the 16 photon factors, 80 have real characters and all 80 pass; 0 fail; 176 non-real (undefined). So reading 3 forces nothing and cannot force u and d differently; its intersection with the 8-point set is all 4 real points (the whole word is β_Bor, χ₃ = 1, χ₂₁ = 1.99419).

**Corpus.** No assignment of colour weights to flavour found: def:photon, quark-antiquark-production ("independent color weights"), pn-averaging-uniqueness ("choosing that weight is open"), bring_color_weighted (interface factor z − h(1/2 − δ/4), not φ). Searched those surfaces + grep of content/ for "colour weight"; corpus_search not run. So an n/p split through colour weights would be a new assignment needing an owner ruling; within the R-pt and R-maj rules none separates n and p in any trace.

Lean: QOU/QuarkState/NucleonPhotonColourWeights.lean (sorry-free, lean-direct exit 0, axioms propext/choice/Quot.sound). Ring-coloured trace (sibling branch claude/borromean-ring-coloured-trace-np-2026-11-21) was not on the remote when this ran; not included.

### 2026-11-21 — β routes re-run under the covariant two-term trace (PR #8707)

The finished one-term routes were re-run under the scored two-term object, with the all-pairs charge insertion generalised to N strands. Those routes are P1/P4 (#8681), P2 (#8680), P3 (#8682), L (#8693) and N2 (#8636).
- **Assumptions.** The lepton strands carry ν 0 / e⁻ −1 (the "C-lep" assumption). The photon-pair strands are run both as lepton strands and as neutral strands.
- **Lean.** `QOU.QBeta.BetaRoutesTwoTerm` has 19 theorems, all sorry-free, over a generic CommRing or Field.

**Main finding: once a lepton strand is present, "braid-covariant" has two readings.**
- **H_N commutant (as pre-registered).** The connected term is non-zero: h/3 for one quark–lepton crossing (`trace_conn_crossing`). It is non-zero even on split words, because the projection is a polynomial in the full twist. That breaks two things the routes relied on: P1's split multiplicativity, and P2's family-A nucleon-blindness. Under this reading n⊗ν and p⊗e⁻ separate on P4's W0 (D = 0.00869, order (q−1)²).
- **Colour-block commutant.** The connected term is identically 0 on every word (`pairSum_union`). Two-term then equals one-term on every route.

Other results:
- P3 is unchanged: its space is one-dimensional.
- N2's selection is unchanged for |c_em| < 3.55.
- No route gives Q_β without choosing c_em (scope a).

**Owner decision (framed in the audit §4).** Which covariance group defines two-term with lepton strands. My recommendation is colour-block. Audit: docs/audits/2026-11-21-beta-routes-two-term-rerun.md.

## 2026-11-21 — task W parts 2–3: can the pair-creation candidates A–D be excluded? (PR #8696)

Owner: *"Keep these as options and explore the implications of each. Can we rule out some of them?"* Pre-registered f816f993c8 / 3e36b55843. Lean `QOU/QBeta/PairCreationExclusions.lean` (sorry-free, generic). Probe `beta_pair_exclusions_probe.py` 12/12 (exact ℚ(q), proton q₀, 70 dps). Doc §3–4.
- **B (passage σ₀σ₁σ₂) excluded, scope (b):** writhe 3 (not γγ); whole-word reading 3 fails at every q>0 and every scale/conjugate (χ₄ = q³, χ₃₁ = −(q⁶−q⁴+1)/q exact; sign step `passage_readingThree_mixed`). Admitted only with two amendments (R3 on bound states only + weak words exempt from γγ).
- **C (σ₂) excluded as energy-carrying, scope (b), ONE-TERM trace only:** `crossTerm_lastLetter_eq_zero` (Markov) kills C₁ on span{1,σ₂}, incl. P_L(σ₂) and the one-sided weak vertex. Not blind in the lepton-labelled two-term comparison (C₂ order 4).
- **A (V₁³) not excluded under premise L.** Not chiral (P_L either side does not fix it); pure process word ⇒ lepton closes alone, unknot (`trackA`), so excluded conditionally under the knot reading — as is every 4-strand candidate. Not unique on 5 strands: V₁³ and V₂³ tie (G∧CC₅∧R3, singlet-cup pair [L5]).
- **D undecidable by invariant:** 1 + cV̄₀ = γ(hc,−hc,c); writhe 0, alt. char 1; grammar not bar-closed. With mirrors: 7 ties + V₁³ at 4 strands; four length-4 words at 5 strands.
- **Two-term:** scored covariant all-pairs connected term is 0 for EVERY element on any number of strands (`twoTerm_allPairs_formula`); lepton-labelled (non-covariant) reading non-zero already on β.
- **Element-level γγ vacuous** (`photon_adjoin_eq`).
- Chiral ∧ γγ ∧ CC ∧ R3: empty on 4 strands (len ≤ 8); on 5 strands only V₂V₀V₁V₂.
- Ring-coloured trace (#8706) open, not evaluated.
- OPEN, owner: chirality required? (recommendation, judgement: yes → characterise V₂V₀V₁V₂); D; R3 scope on transition words. Nothing ruled.

2026-11-21T05:10Z — CORRECTION (my own claims, 2026-11-20). (1) The 15:xx note above said C2 needed "per-nucleon photon weights phi0, phi1". FALSE: DecayConjectures.photonPair_trace_n_eq_p (PR #8725, merged, sorry-free) proves tr_n = tr_p for any photon pair gamma(phi)gamma(psi), all six weights free; the neutron rep is the proton rep with sigma0<->sigma1, an inner automorphism of H3. Varying or tuning phi cannot split p/n. (2) I then said only the T^3 (Cartan K) grading breaks p/n. INCOMPLETE: the two-term Lagrangian trace (CategoricalLagrangianTwoTermBridge, tau L = tau(D D) + tau(psibar psi D)) has a second breaker, the quark-charge insertion Q_iQ_j in its matter term. The scored conditional Q_beta (0.3254 MeV) uses only the first (Cartan) term; the matter term is not included. Under the ruled all-pairs insertion its connected part on V^3 is 0 (deltaT_allPairs_connected_eq_zero) and a static -(1/3) tr V^3 charge term remains. Dashboard note now says so (no number moved). Owner decision open: score Q_beta on the full two-term trace (recommended) vs adjacent-pair arm vs as-is. All 19 sibling beta/Q_beta PRs notified (owner request). Bean stays todo (rule 13a).

## 2026-11-21 owner ruling: right-handed singlet (PR #8694)

- **Adopted (option 1):** the matter⊗Higgs right line of the Jimbo crossing (s = q·ud − du; `RightHandedSingletChannel.lean`) is the right-handed singlet. lepton⊗Φ̃ = e_R (Q −1, Y −2), quark⊗Φ̃ = d_R, quark⊗Φ = u_R, lepton⊗Φ = ν_R. Right-handed fields are two-strand composites, not new strands.
- **Still open, not ruled:** strand order (matter-left vs Higgs-left, which swaps the weights q²/(q²+1) and 1/(q²+1)) and the four Yukawa strengths. Split = (y_d²−y_e²)/(q²+1) + (y_ν²−y_u²)q²/(q²+1) (matter-left); no Q_β number until these are derived.

## 2026-11-21 owner answers (07:xx CET)

- **Photon colour weights (#8705): no new rule.** n and p keep one nucleon element; colour weights are not assigned to flavour.
- **e_R next step:** derive the strand order (matter-left vs Higgs-left) and the Yukawa strengths from the corpus — agent dispatched (branch claude/eR-strand-order-yukawa-derivation-2026-11-21).
- **Two-term with a lepton strand (#8707): not picked from the two readings.** Owner: "The two term came out from looking at the Lagrangian and tracking through non-abelian Stokes. Do the same for the lepton." Agent dispatched to derive the lepton two-term the same way (branch claude/lepton-two-term-from-lagrangian-stokes-2026-11-21).
- **Pair-creation word (#8696): leaning b (require chirality) and d (rule mirror vertices first), NOT ruled.** Owner asks for more context first: what is derived, what is aligned with physics, downstream implications. Analysis agent dispatched.

## 2026-11-21 — decision brief for #8696 rulings (b)/(d) (PR #8742)

Owner asked: "What is derivation? What is aligned to physical?" Brief: docs/audits/2026-11-21-pair-word-derivation-vs-physics-brief.md (PR #8742). Nothing ruled.

Measured (probe computations/probes/pair_word_brief/mirror_vertex_nucleon_probe.py, exact Q(q), proton q0 70 dps):
- eps_flavour (scored Q_beta split, #8586) is identical on V^3 and Vbar^3. The 6 mixed {V,Vbar} 3-vertex words share -(q^2-1)(q^8-q^6+3q^4-q^2+1)/(q^2(q^2+1)^3) = -0.0805502 vs -0.0769805 (ratio 1.04637). (d)-in therefore turns the nucleon selection into an 8-way tie; the scored row moves only if a mixed word is chosen.
- V2V0V1V2 free-reduces to s2 s3^-1 s0 s3^-1 (4 crossings). Closed with beta_Bor, nucleon strands 0 and 1 merge and nu-bar is Hopf-linked (lk -1) to the e- component.
- #8696 "chiral" = zero reverse block = directionality, NOT V-A handedness. The SM H_W is Hermitian: electron capture is its h.c. term. Open, cheap check: are A's two blocks adjoints?
- Which corpus involution is P/CP is unruled (bar and iota send V to Vbar; the group inverse and C do not). "(d)-out breaks CPT" is neither shown nor refuted.
- Recommendation (judgement): (d)-out for now, with a stated reason; hold (b) until the adjointness check is done.

## 2026-11-21 e_R strand order + Yukawa strengths — derivation attempt (PR #8740, stacked on #8694)

Pre-registered (`computations/probes/qbeta_yukawa_strand_order/PREREGISTRATION.md`, 0629a1398d); Lean `QOU/QuarkState/YukawaStrandOrder.lean` (sorry-free, generic Field); probe 21/21.
- **Strand order: NOT forced.** `Cc_Rc_Cc`: C·Ř·C = P·Ř·P, so the two orders are charge conjugates and swap the vev entries q²/(q²+1) ↔ 1/(q²+1) (= q↦q⁻¹). A fixed coproduct fixes the singlet inside each tensor product; nothing in the corpus places the Higgs strand (#8638's quark-left/lepton-right is a quark–lepton convention). The weak insertion −h·P_L kills the singlet in both orders. The only order-free reduction, the pivotal partial trace over the Higgs strand, is [2]⁻¹·1 (module map iff weight ratio q²) but sums BOTH Higgs slots, so it does not use the vacuum; with the vacuum and tr e_H = 1 it is the order-dependent compression.
- **Strengths: NOT derived.** Generation label (all four carry 3), channel qdim (all 1), tr e_H = 1: all slot/type-blind ⇒ split 0, and each would be a NEW rule. Partner-knot Vol·ρ = 0 (unknot, Hopf link, trefoil). Vol(4₁)/ℏ_q² is a μ/e ratio. No CategoricalHiggsIdempotent Yukawa field.
- Split classes: slot-only ⇒ 0 (both orders); type-only ⇒ −(y_q²−y_ℓ²)(q²−1)/(q²+1) matter-left, + Higgs-left (order-odd); balanced pivotal ⇒ (y_d²−y_e²+y_ν²−y_u²)/[2]. At proton q₀: (q²−1)/(q²+1) = 0.10396371005…, q→1 order t. No Q_β number, no CODATA comparison.
- OPEN, owner: which (if any) rule fixes the strengths; strand order. Bean stays todo (rule 13a).

## 2026-11-21 — selection over all k; how much of the scored Q_β the word fixes (PRs #8747, #8752 merged; qou-99qc audit §17)

- `GammaGammaSelectionAllK.lean` (sorry-free): reading 3 selects β_Bor = V³ among ALL non-empty γγ words of H₃ on 1 < q ≤ 23/20, and it is the unique selection. Only V¹ and V² infeasible, V³ feasible and cost 2k are used.
- "V^k feasible ⇔ 3∣k" is FALSE at q₀ (measured at 60 digits): θ = 2π/3 + 0.025423. The first violation is k = 23 (≡ 2 mod 3, feasible); the first infeasible multiple of 3 is k = 63. The selection is unaffected.
- D1 = A: ε_flavour(X) = −h·tr_W(X)/[2]³, and tr_W(V³) = 3 − h⁴[3] (`FlavourSplitWordShare.lean`, sorry-free). The word fixes −0.194 % of the scored 0.325434 MeV. The other 99.8 % comes from the T³ split, the K-weight, [2]³ and E₀, none of which the selection rule supplies.
- Still open.

**2026-11-21 — lepton two-term DERIVED from Lagrangian + non-abelian Stokes (PR #8743, owner: "Do the same for the lepton").** Pre-reg e4ad92f18d. The Stokes step carries the matter (QED) charge insertion round the closed boundary word, so it must be carried through EVERY crossing with each strand's charge moving with the strand. That is the full braid group on all strands with species carried, not either #8707 reading. Lean `QOU.QBeta.LeptonTwoTermStokesCovariance` (24 thms, generic Field, sorry-free, lean-direct exit 0). (1) One crossing: α₁Q₁²+α₂Q₂²+βQ₁Q₂ is carried ⇔ h·((2α₁−β)y₁−(2α₂−β)y₂)=0 (`quad_carry_iff`), and a spectator strand forces uniform pair weights (`pairWeight_uniform`). (2) Pairs-only (16:44 object) is carried at quark–quark crossings and NOT at quark–lepton ones (`pairOnly_quark_lepton_not_carried`; probe 0/6); scope (b) within species-weighted quadratic insertions. (3) The carried family is (β/2)Q_tot²+κΣQ²/y. The nucleon ruling forces κ=−βy_q/2, so the lepton insertion is all pairs + (2/3)Q_ℓ² (`lepton_self_weight_forced`, `natural_family_lepton`). It is a function of T³_tot and the species content (`natVal_eq_totals`), hence scalar on every W_m: connected two-term ≡ 0 on every word, and n⊗ν = p⊗e⁻ = −1/3 (`natural_beta_split_zero`). (4) A charge-0 neutral doublet is inadmissible (`singleCharge_not_carried`). Probe 15/15: scored two-term = one-term exactly on all 91 route quantities (P1/P4, P2 A/D, N2; route L moves 0). The derived two-term contributes NOTHING to Q_β. #8707's H_N non-zeros come from projecting a positional charge the lepton strand does not carry. Premise L (lepton = braided strand) is still undecided, but L′ also gives 0. Not identified with Q_β. Bean stays todo (rule 13a). Audit docs/audits/2026-11-21-lepton-two-term-from-lagrangian-stokes.md.

2026-11-21T06:50Z — CORRECTION of my 05:10Z note, part (2). Main ALREADY scores Q_beta, m_n, Delta_pn on the two-term trace (owner ruling 2026-11-20 "Put two term in scorecards and ALL compute"), with the ruled covariant all-pairs insertion whose connected part is exactly 0 on V^3. So the two-term score = Cartan term alone = 0.3254 MeV (-58.4 %). The raw static all-pairs term (-0.0565 MeV -> 0.2689 MeV, -65.6 %) is a labelled unscored row. My claim "the matter term is not included" was wrong; fixed in PR #8754 (note + Lean docstring), correction posted to the 19 sibling PRs. Open owner question is now only: raw (static) vs connected all-pairs.

**2026-11-21 — which map is parity (owner: "Settle which map is parity"; PR #8742, branch `claude/pair-word-derivation-context-2026-11-21`).** Lean `QOU/QBeta/ParityMapCandidates.lean`, 16 declarations, sorry-free, lean-direct exit 0. Exact probe `computations/probes/pair_word_brief/parity_map_probe.py`, 33/33 checks.
- No letter map is parity P. D-H5 = D (2026-11-15) stands. Under the RULED left line (eigenvalue modulus > 1), bar (`σ ↦ σ⁻¹`, `q ↦ q⁻¹`) and `ι` (`σ ↦ −σ⁻¹`) exchange the left and right lines, while `neg` (`σ ↦ −σ`) keeps them (`neg_leftLine`). This changes the helicity column of the D-H5 table, which took `P₊` as helicity.
- Under reading R1 (`q ↦ q⁻¹` antilinear) the assignment is CP = `ι`, T = `neg`, CPT = bar, a closed Klein group. Under reading R2 the assignment degenerates. Which reading holds is a premise. `neg` loses P's profile, which bears on bean `qou-hlxp`.
- `neg` fixes `V` (`neg_vertex`). So a P argument cannot force the mirror vertices into the grammar. `ι` and bar send `V ↦ V̄`.
- `V̄ = (σ₁σ₀)V(σ₁σ₀)⁻¹` (`mirror_conj`). So `V̄ᵏ` is conjugate to `Vᵏ`, and every trace agrees on them (`trace_mirror_pow`). The V-only nucleon set is therefore CPT-closed up to conjugacy. This is proved only for powers of a single vertex; the multi-index β⁻ words are not covered.
- `ι` moves `z_D` to `h − z_D = −z_D(1/q)` and does not descend to the Jimbo image (`iota_not_descend`, with its hypotheses checked exactly in the probe). The corpus's P (braid mirror at fixed `q`) fails the trace-preservation component of `conj:cpt-d6-d7-d8-closure` at `n = 2`. This is reported only; the conjecture was not edited.
- Recommendation (judgement): (d)-out, with the reason recorded as closure-level CPT. The brief section "Which map is parity" gives the six-part frame. Still open: reading R1 vs R2, and conjugacy for multi-index words.
- Correction: the brief first said that the lemma `ι(V) = V̄` was unwritten (it is `ChiralityPairBit.iota_vertex`) and that the corpus had not ruled on P (it had: D-H5). Both are corrected in the brief. Neither claim appears in the PR body or in this bean.

### NOTE 2026-11-21 07:45Z — re-check of this thread's Nov-16 results against the current framework (owner standing rule: two-term trace, three-term photon with L±, no virtual photons, electron strands)
- ε-Y1 (#8068), ε-Y2 (#8087): about the colour u1 phase and the triality/charge rule only; no photon word, no trace convention. Unaffected.
- ε-L1 (#8104): used the photon twist channel L± with the one-term multiplicity trace and no lepton strand. SUPERSEDED in its photon definition by ε-L1V (#8616, ruled vertex V = σ₀σ₁⁻¹) and by DecayConjectures.photonPair_trace_n_eq_p (#8725: tr_n = tr_p for any γ(φ)γ(ψ), all weights free). The conclusion (no braid-only n↔p break) is consistent with both; not re-run here.
- ε-Y5/Y6 (writhe-0 argument for the twist bound) were stated for the OLD γγ grammar. With L± (writhe ±2) now in the photon, the writhe-0 premise no longer holds, so ε-Y5's scope-(b) exclusion must be RE-CHECKED before citing. Flagged, not re-done (stale session; live sessions own qou-99qc).

### PRE-REGISTRATION 2026-11-21 12:20Z — stage 7R: γγ grammar re-derived on the RULED photon (owner: "Redo Gamma gamma gramma")
Written before any computation. Ruled photon (#8583, owner-rulings 2026-11-18/20): γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁V, V = σ₀σ₁⁻¹. Stage 7 (2026-11-18, commit 68ef4b266, never merged) used the superseded fourth term σ₀σ₁, so it is redone here with the same rules.
**Terms of γ(φ)γ(ψ), as braid words, free-reduced:** one-photon-bare: σ₀, σ₁, V. Bilinear: σ₀² (φ₀ψ₀), σ₀σ₁ (φ₀ψ₁), σ₁σ₀ (φ₁ψ₀), σ₁² (φ₁ψ₁), σ₀V = σ₀²σ₁⁻¹ (φ₀ψ₀₁), Vσ₀ = σ₀σ₁⁻¹σ₀ (φ₀₁ψ₀), σ₁V = σ₁σ₀σ₁⁻¹ (φ₁ψ₀₁), Vσ₁ = σ₀ (φ₀₁ψ₁, free-reduces), V² (φ₀₁ψ₀₁).
**Arms.** V (the current Lean grammar, GammaGammaWordSelection: products of V only, = the φ₀₁ψ₀₁ sector). A (primary, same rule as stage 7): products of the nine bilinear terms. B (comparison, not selectable): all twelve non-identity terms.
**Selection (unchanged, qou-ales FrobeniusSelected):** 3 strands; words free-reduced, ≤ 10 crossings (stage 7 used 12 on positive words; the inverse letter makes 12 too large to enumerate here — stated now, not after results); feasible = reading 3, χ ≥ 0 on every level with y > 0, convention D, proton pin; near-zero (< 1e-30) decided exactly with symbolic q; cost = crossing count of the free-reduced word; every minimum reported, no tie broken.
**Also measured (the reason for the redo, ε-Y5):** writhe of each letter and of each selected word; whether the arm is writhe-0. ε-Y5 excluded the γγ route to the twist bound on the premise "every γγ word has writhe 0".
**Questions, no predicted answer:** 1. Arm A minimum, and is it split? 2. Is β_Bor = V³ feasible / minimal in arm A? 3. Does the writhe-0 premise of ε-Y5 hold for arm A, or only for arm V?
**Not allowed:** changing letters, cost, bound or floor after results; choosing among ties by Q_β or any mass. Nothing compared with measurement.
