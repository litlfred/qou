---
# qou-qb8g
title: c_3's bar-parity is UNDETERMINED — neither named split is derived
status: in-progress
pr: 8245
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T11:45:00Z
updated_at: 2026-11-17T07:09:00Z
parent: qou-avtq
---

*** REWRITTEN 2026-08-08 (same day). The original title was "Prove c_3^even = 0".
    That premise came from an argument in qou-qb8f that turned out to be
    CIRCULAR and was withdrawn. c_3^even = 0 is NOT indicated. The real question
    is below. ***

## What the withdrawal changed

qb8f first argued: the canonical `c_3^odd = kappa_(2,1)(q)*S` split reproduces
the 2026-07-07 audit's S values under `c_3^even = 0`, therefore c_3 is purely
bar-odd. That was circular — S is DEFINED as `S := a_1/kappa_(2,1)` with
`a_1 = -c_3` (qbeta_s_complex_volume_rigidity_probe.py:69;
2026-06-13-qbeta-root-of-unity-residue-program.md:177), so the "reconstruction"
was an identity. The agreement (4.1e-5 / 1.1e-5) sat inside the 4-s.f. rounding
window (5.5e-5 / 5.6e-5) of the quoted numbers — the signature of the same
number.

So `c_3^even = 0` has NO support. Nor does `c_3^even = -Vol(4_1)`.

## The actual open question

**c_3's bar-parity is undetermined by the present corpus.** Two obstacles, both
structural:

1. **Not empirically accessible.** `c_3^even(q) = (c_3(q)+c_3(1/q))/2` needs c_3
   at `q ~ 0.901`. Both anchors sit at `q ~ 1.10998`. No amount of anchor data
   determines the split.

2. **Neither named "split" is derived.** Both are definitions applied to c_3:
       S_leak := c_3 + Vol(4_1)
       S      := -c_3 / kappa_(2,1)
   c_3 is recovered exactly from either, both ways (<1e-40) — reparametrisations
   carrying no information. Neither can adjudicate the other, and neither
   supplies a parity.

## What would actually settle it

A genuinely DERIVED decomposition of c_3 — one where the bar-even and bar-odd
parts come out of a construction with their normalisation pinned in advance,
rather than being defined as "c_3 minus/over <fixed thing>".

Candidate route, unstarted: c_3 as an archimedean evaluation of a fibre-level
(Habiro) element, where the bar-involution acts on the FIBRE object and the
parity is read off there — not inferred from two archimedean anchors that
cannot see it. This is the same target as qou-qb8e (magnitude channel), so the
two may close together.

## A parity tension to resolve on the way (recorded in qb8f)

`kappa_(2,1) = (q-1)^3(q+1)/q^2` is verifiably bar-ODD. The 2026-07-07 audit
also says S "inherits bar-odd from Q_beta". odd x odd = EVEN would make
`c_3 = -kappa*S` bar-EVEN and the label "c_3^odd" a misnomer. With
`S := -c_3/kappa` the tension dissolves (S's parity is whatever makes the
identity hold) — but it is worth stating explicitly in whichever artifact
carries the split, because as written the labels invite the wrong reading.

## Anti-fit guardrail

Do not resolve this by choosing whichever parity makes a downstream number work.
A derived parity comes from the construction; a chosen one is a fit.


---

# *** UPDATED 2026-08-08 (second correction) ***

The claim "neither split is derived" is too strong on the S_leak side.
S_leak = c_3 + Vol(4_1) HAS geometric backing: the Phi_b saddle volume deficit
0.0094 ~ |S(muon)| = 0.00968, fit-free and anchor-blind (PR #3654; KC21;
2026-07-12 capstone result 5).

Corrected framing of this bean:
 - S := -c_3/kappa_(2,1) IS definitional and carries no parity information.
 - S_leak IS geometrically motivated, at ~2.9% on the SCALE. The exact
   normalisation is open and conj:im-q-physical-role is still a conjecture.
 - So c_3's bar-parity is not "undetermined by everything" -- the geometric
   route is live and is the one to push. See KC21 + the capstone's open item:
   the exact D(u-tilde) ladder function.

Do NOT re-derive the 1/u^3 hypersensitivity result or the S = h*D factorisation
-- both are already in the corpus (KC21). Start from the capstone's own stated
open item.


---

# *** THIRD CORRECTION 2026-08-15 — the SECOND correction is itself WITHDRAWN ***

**The section immediately above is refuted. This bean's ORIGINAL framing was
right: c_3's bar-parity is undetermined by the present corpus.**

The second correction reversed that on one piece of evidence — the Phi_b saddle
volume deficit `0.0094 ~ |S(muon)| = 0.00968`, described there as "fit-free and
**anchor-blind**" — and concluded "the geometric route is live and is the one to
push". Measured in PR #5022 (merged; registry §9b, and
[`2026-08-14-c3-registry-glyph-collision-and-anchor-selective-scale.md`](../docs/audits/2026-08-14-c3-registry-glyph-collision-and-anchor-selective-scale.md)):

| | value |
|---|---|
| deficit spread across anchors | `2.2e-7` (anchor-BLIND) |
| `\|S_leak\|` swing across anchors | **4.075x** (anchor-DEPENDENT) |
| deficit vs `\|S_leak(muon)\|` | **2.896 %** <- the quoted match |
| deficit vs `\|S_leak(proton)\|` | **76.17 %** <- not quoted |
| ratio of misses | **26.3x** |

**The anchor-blindness is the defect, not the virtue.** The second correction
cites it as evidence *for* the geometric backing; it is the reason that backing
cannot work. A quantity identical at both anchors cannot reproduce one that
differs by 4x between them — the match holds at **at most one** anchor, and only
the muon one was quoted. Registry §9b now states this in as many words.

**Calibration:** the deficit is **5.32x closer** to the ladder's own expansion
variable `u_0` (0.544 %) than to `|S(muon)|` (2.896 %). `u_0` carries no
4_1-volume content, so at a 2.9 % tolerance the match does not discriminate a
geometric reading from a numerological one.

The producing witness was never wrong -- it records both anchors and says
`"|S(muon)|"` explicitly. The over-generalisation happened in the KC21 summary,
and this bean inherited it.

## Net effect on this bean

- **Restored:** "c_3's bar-parity is undetermined by the present corpus", with
  both structural obstacles above intact (not empirically accessible at one
  anchor pair; neither named split is derived).
- **Withdrawn:** "S_leak IS geometrically motivated at ~2.9% on the SCALE" as a
  *live route to push*. It is muon-only. Registry §9c records the verdict:
  **(H1) `c_3^even = -Vol(4_1)` is NOT derived** -- geometrically motivated, but
  not supported at the tolerance at which it was asserted.
- **Unchanged:** everything the second correction did not touch. The
  `10/3 = lim_{q->1}[10]_q/[3]_q` writhe-ratio identity is exact. The Phi_b
  saddle itself, 4_1 amphichirality, and `Vol(4_1)` elsewhere are untouched.

Scope-(a): no invariant is named forbidding a 4_1-volume ingredient in c_3's
bar-even part. (H1) is **unsupported**, not refuted. Do not convert this into a
scope-(b) exclusion.

## What this means for the route

The "candidate route, unstarted" in the ORIGINAL framing is now the live one,
and it is sharper than when written:

> c_3 as an archimedean evaluation of a fibre-level (Habiro) element, where the
> bar-involution acts on the FIBRE object and the parity is read off there --
> not inferred from two archimedean anchors that cannot see it.

The 2026-08-09 convergence correction independently reached the same wall from
the other side: "the gate is still the map from a bar-odd fibre-level object to
an anchor-*dependent* number", noting the carrier is anchor-blind (spread
1.23e-9) and so `S = h*D(u)` is "schematic rather than a tight identity".

## *** CORRECTED 2026-08-15 — the "anchor-blind -> anchor-dependent" wall is CIRCULAR ***

An earlier revision of this section read: *"Two independent objects, one wall: an
anchor-blind quantity cannot deliver an anchor-dependent one."* **Withdraw that
phrasing.** Measured over the same anchor gap `dq = 1.28e-8`:

    carrier h*D   moves 1.23e-9   => slope ~ 0.096     (an ORDINARY smooth function)
    S_leak        moves 0.0491    => slope ~ 3.84e6    (within 17.7% of dc_3/dq ~ 4.66e6)

So "anchor-blind" means *ordinary derivative* and "anchor-dependent" means *the
`1/u^3` ladder inversion* — which the 2026-07-12 capstone already closed ("the
wall was never physical"). Stating it as an open gate re-imports a settled
result. There is nothing to explain in a smooth function failing to track a
quantity whose slope is 4e7x larger; that is arithmetic.

**The real content is a ZERO, not a magnitude.** `S_leak`'s zero `q*_S` sits
BETWEEN the anchors (80.28% of the way from proton to muon), and `S_leak` is
linear through it — lever arm 4.0700 vs measured ratio 4.0751, agreeing to
0.12%. This is **Route A** (2026-08-01), Lean-proved sorry-free in
`SLeakMagnitudeOffsetRatio.lean` (`linear_ratio_slope_independent`: the slope
*cancels*). The carrier `h*D(u~0) = -0.003486` is a nonzero near-constant while
`S_leak` crosses zero — and a nonzero constant cannot equal a function crossing
zero.

**Restated gate, checkable:** the fibre carrier must reproduce the **zero
location `q*_S`**, not any magnitude. That is why magnitude-matching has failed —
`|S_leak|` at an anchor is `slope x (distance to the zero)`, and the distance is
a calibration accident carrying no scale content. `qou-qb8e` and this bean still
close together or not at all, but the target is the zero.

## Discipline note

Three corrections on one bean, alternating direction. Before a FOURTH: the
failure mode here has been re-reading a *scale* agreement at one anchor as
structural support. Any future reversal must state, up front, what it predicts
at the **proton** anchor -- not just the muon one.


---

# OBSTACLE 1 MADE QUANTITATIVE — the extractor cannot be continued to 1/q0
# (2026-08-15, PR #5084; probe `qbeta_c3_bar_partner_extractor_breakdown.py`)

Obstacle 1 above reads: *"Not empirically accessible. `c_3^even(q) =
(c_3(q)+c_3(1/q))/2` needs c_3 at `q ~ 0.901`. Both anchors sit at
`q ~ 1.10998`."* True, but it understates the situation in a way that matters:
**the extractor CAN be evaluated at 1/q0, and what comes out is an artifact.**

    c_3(q) = (Q_beta^exp / Q_N2(q) - 1) / u(q)^3        qbeta_utils.c3_target_at

`Q_beta^exp` is held FIXED while q moves ~21% — `c3_target_at`'s own docstring
says so ("the SAME at every substrate anchor ... not a function of q"). Away
from the anchor the numerator is O(1) rather than O(u^3), and the `1/u^3`
inversion returns O(1e5). Measured:

    point    u          numerator        c_3^extr
    q0       0.008517   -1.2786e-6       -2.0693        <- the familiar value
    1/q0     0.010494   -0.40744         -352599.7      <- 1.7e5 x larger

The `u` shift is TAME and exactly predictable: `hbar_q = 1 - 1/q` gives
`u(1/q) = q^2 u(q)`, verified to rel.err 1.26e-61. **The entire blow-up is the
numerator** (ratio 3.19e5) — i.e. the fixed-Q_beta artifact, nothing else.

Consequently the extractor's "bar decomposition" is meaningless:

    extractor bar-even  = -176300.9      (86853 x Vol(4_1))
    extractor bar-odd   =  176298.8
    -Vol(4_1)           =      -2.0299

**Do NOT evaluate `c3_target_at` at 1/q0 and read the result as c_3 there.**

## What (H1) demands at 1/q0 — and why it is NOT new information

(H1) `c_3^even = -Vol(4_1)` forces `c_3(1/q0) = -2 Vol(4_1) - c_3(q0) =
-1.9904238`, an O(1) number, against the extractor's -352600 (factor 1.77e5).

But this is the anchor datum transported, not an independent measurement: (H1)
is EQUIVALENT to "S_leak IS the bar-odd part", and the implied bar-odd value
comes out identically `S_leak(q0) = -0.039459364295861` (difference exactly
0.0, asserted in the probe). Per AGENTS.md "Defined residual != derived
decomposition", it must not be reported as an out-of-sample test. It also
inherits the +/-1.262 CAL-3 band.

## What IS gained — methodological, and it is the actionable part

PR #5084 (`HabiroEvaluationTrichotomy.lean`, sorry-free) proves a fibre carrier
written as a q-series converges at `1/q0 < 1` and NOT at `q0 > 1`. So:

  - the bar-even combination `(F(q0) + F(1/q0))/2` **cannot be formed from a
    single q-series** — one term is outside the domain. The object required is a
    PAIR, or a state integral holomorphic off the reals (the Garoufalidis-Zagier
    shape), not one series. That is a DOMAIN obstruction to the parity read-off
    as this bean states it.
  - at 1/q0 the extractor is useless but (H1) still names a value AND the
    carrier is inside its domain of convergence. So a carrier can be compared to
    (H1) **without ever evaluating on the divergent side**. The comparison
    becomes possible; it does not become sharper.

## Net effect on this bean

- **Obstacle 1 STRENGTHENED**, not resolved: it is not merely that we lack data
  at 1/q0 — the naive continuation there is dominated by a fixed-Q_beta
  artifact by five orders of magnitude, and the domain obstruction above says a
  single q-series cannot supply the split either.
- **Obstacle 2 unchanged.** Neither named split is derived.
- **The live route is unchanged and now has a concrete evaluation point**: read
  the parity off the FIBRE object at `1/q0`, where it converges. That is where
  qb8g and qb8e meet.

Scope-(a) throughout. Nothing here refutes (H1); it shows the EXTRACTOR cannot
test it at the bar-partner, and names what a carrier must return instead.


---

# FRONT (e) — (H1)'s STATED EVIDENCE HAS NO DISCRIMINATING POWER
# (2026-08-15, PR #5093; probe `qbeta_h1_significance_against_cal3_band.py`)

Owner picked "(e) re-examine (H1) itself" alongside (a) and (b). Result: the
evidence cited for (H1) does not discriminate at present resolution, and the
corpus phrasing overstates it two ways. **Both defects are in text I wrote
earlier the same day (PR #5074).**

## Defect 1 — the percentage omits the error bar on what is being compared

`sigma(c_3) = +/-1.262` per anchor, CAL-3 propagated — **61 %** of `|c_3|`.
DERIVED in the probe as `sigma(Q_beta)/(Q_N2 u^3)` from the committed CAL-3
input, reproducing the corpus's quoted 1.262 to `4.1e-5` rather than assuming
it. In sigma:

    proton   |c_3 - (-Vol(4_1))| = 0.03946   ->  0.031 sigma
    muon                         = 0.00968   ->  0.008 sigma

A 0.03-sigma agreement is not strong evidence; it is NO evidence. Every
candidate within the band agrees at least as well. This is precisely the
standard the O2 probe (`qou-ws1w`) already applied to the `A_omega -> S`
bridge — "neither confirmed nor excluded ... the signature of a fit, not a
derivation" — and fired O1-remove on. **That test had never been turned on (H1)
itself**, the hypothesis that DEFINES S.

## Defect 2 — the "0.48 %" is the MUON figure, labelled as the substrate anchor

    muon    0.479 %      <- this is the published "0.48 %"
    proton  1.907 %      <- 4.0x worse, not quoted

Since the 2026-08-07 owner directive makes the proton pin the default for new
compute, "the substrate anchor" reads as proton today, so the headline attaches
the muon's number to it and flatters (H1) fourfold.

## Consequence for the genericity result

The 1-sigma acceptance for `V` in `c_3 ~ -V` is `[0.807, 3.331]`, width
**2.524**, against the **0.0491** genericity window the 7/7-unrelated-constants
check was computed over. **The window understates the ambiguity by 51x.**

## What would make (H1) testable

    32x  sharper Q_beta  ->  proton agreement reaches 1 sigma
    130x sharper Q_beta  ->  muon agreement reaches 1 sigma

bracketing the **25.68x** the zero-location test needs (PR #5084). All three
thresholds are the SAME lever — a sharper neutron Q-value — and they order
sensibly, which is a consistency check on all three numbers.

## Scope — and it cuts BOTH ways

Scope-(a). (H1) is **NOT refuted**: no invariant forbids a `4_1`-volume
ingredient in `c_3`'s bar-even part, and `0.031 sigma` is not evidence AGAINST
(H1) either. Nothing is being measured. Do not convert this into a scope-(b)
exclusion, and do not cite it as a reason to drop (H1) — cite it as the reason
(H1) cannot currently be tested.

## Net effect on this bean

- Obstacle 2 ("neither named split is derived") is unchanged and now has a
  quantitative floor under it: even if a split were proposed, the anchor data
  could not adjudicate it.
- Re-scoped in the same PR: registry section 9f's "surviving empirical fact"
  paragraph, and the `rem-qstar-decay-sector-q0` paper block, both of which
  carried the bare "0.48 %".

---

# CONVENTION PROVENANCE (2026-08-15, owner redirect)

The validity audit
(docs/audits/2026-08-15-c3-refutation-chain-convention-validity-audit.md)
adds a third structural obstacle to the two above, and it is upstream of
both: **c_3 itself is a convention-C-frame quantity** (the extractor's N=1
phase consumes z_C; the Q_beta channel is unregistered in the
trace-convention registry — bean qou-b3nk). Under convention D the same
ladder shape extracts c_3 ~ -974, so "c_3's bar-parity" is only defined once
the channel's convention is settled. Also directly relevant to this bean's
live route: KC13's "z exactly bar-even" is proved for z_C only —
bar(z_D) = q^-4 * z_D exactly (probe
qbeta-c3-ladder-trace-convention-sensitivity, 9/9) — so under D the trace
parameter itself carries a monomial bar-twist (KC16-style). Scope-(a):
observation, not a parity result.


## 2026-08-29 — workflow (symbolic-exact, both lenses survive): the alpha_C/alpha_D bar-homogeneity discriminant
NEW derived structural obstruction to porting the C bar-split to D: alpha_C=(z_C-1)h/2 is PURE bar-odd (bar-even part exactly 0) -- which is WHY log R = E(u-tilde)+h*D(u-tilde) can pin the even channel E with normalisation in advance. alpha_D=(z_D-1)h/2 is bar-MIXED (even part (q^2-1)^2/(4q^2) != 0 AND odd part != 0) because z_D-1 is not bar-homogeneous (z_D bar-weight -4, const 1 weight 0). So the pure-odd-phase mechanism has NO D analog yet. Does not supply a parity; identifies the exact obstruction. No D-frame c3 exists until cds1 lands -> no D-frame parity. (bar(z_D)=q^-4 z_D exact.) Audit 2026-08-29-convention-d-qbeta-front.


## 2026-08-29 — the alpha_D bar-mixed obstruction is now PROVED-LEAN (landed)
QOU/QBeta/EigenphaseBarMixedD.lean committed (0f4df6eed6), sorry-free (clean axioms): twoAlphaD_bar_even_sum (2a_D(1/q)+2a_D(q)=(q^2-1)^2/q^2) + twoAlphaD_not_bar_odd. Contrast alpha_C pure bar-odd (QOU.Interactions.eigenphase_bar_involution). This machine-checks the exact obstruction to porting the C bar-split to D. Parity still OPEN (blocked on cds1 D ladder).


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: BLOCKED.** Parity is undetermined and stays blocked until qou-cds1 produces a D-frame c_3. The "(H1) is 0.03σ" evidence probe has a committed red witness (allPassed:false). Its 0.48% assertion predates the CODATA-2022 muon re-pin and needs fixing at the producer.

Evidence: Blocked on `qou-cds1`, as its own last line says. `EigenphaseBarMixedD.lean` and `MarkovZFullBarCondition.lean` are sorry-free by grep: under D the eigenphase is bar-mixed, with even part (q²-1)²/(4q²). `qbeta_c3_bar_partner_extractor_breakdown.py` re-run exits 0 and reproduces. **Broken witness:** `qbeta_h1_significance_against_cal3_band.py` exits **1**, and the committed witness at HEAD already records `allPassed:false`. Assertion `quoted_048pct_is_the_muon_not_the_substrate_anchor` fails because the muon figure is now 0.4962% (CODATA-2022 pin), not 0.48%.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## 2026-11-17 — Round 53 formalization & probe witness (PR #8245, status: in-progress)

- [x] PR #8245 (`dea5885f0b662330ff1d63757512b50427bbc370`): formalized `sleak_reparametrisation_bijective`, `kappa21_numerator_antipalindromic`, and `c3_bar_parity_from_odd_kappa` in `QOU/QBeta/ThetaKChannelC3BarParityAndHabiroRigidity.lean` (`0 sorry`, `0 axiom`, `0 vacuity`), proving `kappa_{(2,1)}` is bar-odd and `c_3 = -kappa*S` is bar-odd iff `S` is bar-even.
- [ ] Awaiting Merge Manager integration and owner review (kept `in-progress` per no-unilateral-closure policy).
