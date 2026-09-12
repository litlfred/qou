---
# qou-99qc
title: 'OWNER CALL: Delta prose vs epsNPq — one of the two is wrong (fork forced by qou-avt6)'
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:35:22Z
updated_at: 2026-09-12T19:41:51Z
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
