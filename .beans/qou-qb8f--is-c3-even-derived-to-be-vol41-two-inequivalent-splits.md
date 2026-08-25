---
# qou-qb8f
title: Is c_3^even DERIVED to be -Vol(4_1)? Two inequivalent splits live in the corpus
status: in-progress
type: task
priority: high
created_at: 2026-08-08T10:45:00Z
updated_at: 2026-08-19T21:14:17Z
---

Raised (not adjudicated) from PR #4724 after retracting an S_leak-based filter.
This is for the c_3 owners (#4725 / the ck-dk registry maintainers) to settle.

`SLeakZeroCrossing.lean:11` defines
    S_leak(q0) := c_3(q0) + Vol(4_1)
and calls it "the bar-odd residual of c_3 after removing the bar-even
amphichiral -Vol(4_1) face". That reading requires c_3^even = -Vol(4_1)
EXACTLY. Three problems found; none is a claim the Lean is wrong.

1. NOT EMPIRICALLY ACCESSIBLE. c_3^even(q) = (c_3(q) + c_3(1/q))/2 needs c_3 at
   q ~ 0.901. Both anchors sit at q ~ 1.10998. No anchor data can determine the
   bar-split; it must come from an assumed structural form.

2. THE SIGN FLIP IS OFFSET-GENERIC. S_leak(mu) > 0 > S_leak(p) holds for ANY
   constant V strictly in (-c_3(mu), -c_3(p)) = (2.02020024, 2.06934258), a
   window of width 0.0491. Verified: Vol(4_1), 2+1/36, 2+1/30, 2+1/25, 2+1/24,
   63/31, e^0.708 -- 7/7 give the SAME flip
   (computations/qbeta/sleak_offset_genericity_check.py). So the flip restates
   "c_3 differs between anchors"; it is not evidence about Vol(4_1).

3. TWO INEQUIVALENT SPLITS IN THE CORPUS.
   - 2026-07-07-c3-even-solved-s-complex-volume-rigidity.md (the audit cited for
     "c_3^even is solved"): bar-even channel = exact Q(sqrt3) u-ladder,
     e_1 = 3sqrt3/4, projection rung ~ +86.66; bar-odd scalar S = Q_beta/E_0
     ~ 908, which does NOT sign-flip (S_p/S_mu ~ 1.024).
   - S_leak framing: even part = -Vol(4_1) ~ -2.03, odd residual ~ 0.0097.
   These are not the same decomposition. SLeakZeroCrossing.lean guards the
   SYMBOL collision between the two S's, but that guard does not reconcile the
   two EVEN parts. And the 2026-07-07 audit tiers the V_q identification
   "exploratory" in its own header.

NOT A CLAIM THE LEAN IS WRONG: sleak_zero_between_anchors and
sign_definite_carrier_excluded are stated for a GENERIC continuous function
with the anchor signs as hypotheses, and are fine as stated. What is
unsupported is the interpretive step that S_leak IS c_3's bar-odd part.

Questions to settle:
(a) Is there a derivation of c_3^even = -Vol(4_1), or is it a near-match?
    (D(z)+D(w) = Vol(4_1) to 4e-18 is the volume of 4_1 -- that identity is
    real, but it does not by itself say c_3^even equals it.)
(b) If yes, which of the two even-part claims is canonical, and should the
    other be re-scoped?
(c) Should the registry's c_3 row carry a pointer either way?

Generic guard added so this class does not recur: AGENTS.md
"Defined residual != derived decomposition (STRICT, 2026-08-08)".

---

# ANSWERED (2026-08-08, PR #4742): (H1) is NOT derived — it CONTRADICTS the
# canonical split. Scope-(a).

Probe: computations/qbeta/c3_even_canonical_split_contradiction.py (7/7).
Audit: docs/audits/2026-08-08-c3-even-vol41-contradicts-canonical-split.md.

## (a) Is c_3^even = -Vol(4_1) derived?  NO — and worse than underived.

The bar-split is not measurable from anchor data (needs c_3 at q ~ 0.901; both
anchors sit at q ~ 1.10998), so it was tested for CONSISTENCY against the
corpus's derived split instead.

2026-07-07 audit §2 gives c_3^odd = kappa_(2,1)(q)*S with the DERIVED bar-odd
carrier kappa_(2,1) = (q-1)^3(q+1)/q^2 (verified kappa(1/q) = -kappa(q)
symbolically) and the archimedean scalar S = Q_beta/E_0, quoted INDEPENDENTLY
as S_p ~ 908.4, S_mu ~ 886.8, S_p/S_mu ~ 1.024.

Inverting c_3 = -kappa*S under the hypothesis c_3^even = 0:

  proton  S_recon = 908.3624831   vs audit 908.4   rel dev 4.1e-5
  muon    S_recon = 886.7905751   vs audit 886.8   rel dev 1.1e-5
  S_p/S_mu = 1.02432582           vs audit 1.024

So the canonical decomposition has c_3 essentially PURELY BAR-ODD:
c_3^even ~ 0, NOT -2.03. Separation = 98.09% of |c_3|. The two readings are
INCOMPATIBLE, not merely distinct.

## What S_leak actually is: a 209x cancellation artifact

  proton  c_3 = -2.06934258 + Vol(4_1) -> -0.039459367   (98.093% cancelled)
  muon    c_3 = -2.02020024 + Vol(4_1) -> +0.0096829728  (99.521% cancelled)

  anchor swing of c_3     2.4325%
  anchor swing of S_leak  507.51%
  amplification           208.63x

c_3's own 2.4% swing is REAL (the dc_3/dq ~ 4.6e6 obstruction stands). The extra
209x is arithmetic. Any argument reading S_leak's RELATIVE swing as structural
sensitivity is reading the cancellation.

## (b) Which even-part claim is canonical?  The kappa*S split.

## CORRECTION to this bean's own framing (recorded, not deleted)

This bean said "two inequivalent SPLITS", citing c_3^even ~ +86.66. Imprecise
twice:
 1. +86.66 is a PROJECTION ARTIFACT — the 2026-07-07 audit says so itself
    ("the honest rungs are the e_k"; e_1 = 3sqrt3/4, margin 9, residuals 0).
 2. It is a DIFFERENT OBJECT — the k=3 rung of the bar-even channel of log R,
    not the bar-even PART of the c_3 Taylor coefficient. Same glyph, two
    referents (the overloaded-symbol trap, AGENTS.md conditional-proved rule 4).

Sharp statement: (H1) contradicts the derived kappa*S split. Not "rival values".

## NOT refuted (scope-(a) boundary)

Vol(4_1) as an ingredient elsewhere; 4_1's amphichirality; and EVERY theorem in
SLeakZeroCrossing.lean / SLeakMagnitude{Offset,Taylor}Ratio.lean — all generic
and hypothesis-carrying, all stand. Only the interpretive sentence is affected.
No Lean edited; the docstring fix belongs to those files' owners (#4734 notified).

## (c) Registry pointer — UNANSWERED, left to the registry maintainers.

## Follow-on

c_3^even ~ 0, if right, is itself a structural claim worth PROVING rather than
inferring from a 1e-5 two-anchor cross-check. Filed as a note here, not a bean,
pending the owners' read.


---

# *** CORRECTION (2026-08-08, same day) — the verdict above is PARTLY WITHDRAWN ***

The claim "(H1) CONTRADICTS the canonical kappa*S split" was CIRCULAR. Withdrawn.

S is DEFINED as S := a_1/kappa_(2,1) with a_1 = -c_3:
  - qbeta_s_complex_volume_rigidity_probe.py:69
      "# S = a_1/kappa_(2,1) = Q_beta/E_0 at the two anchors"
  - 2026-06-13-qbeta-root-of-unity-residue-program.md:177
      "| bar-ODD a_1 = -c_3 | live | carrier kappa_(2,1) = (q-1)^3(q+1)/q^2 |"

So "reconstructing" S = -c_3/kappa and recovering 908.4 / 886.8 is an IDENTITY.
The tell: agreement 4.1e-5 / 1.1e-5 sits INSIDE the 4-s.f. rounding window
(5.5e-5 / 5.6e-5) of the quoted values. Agreement at exactly the quoted
precision = the same number, not confirmation.

Root cause: treated "quoted in a different audit" as "independently derived",
without tracing the cross-check target's provenance. Same error class as the
subject under audit.

## CORRECTED VERDICT (stronger)

BOTH named splits are DEFINITIONS:
    S_leak := c_3 + Vol(4_1)
    S      := -c_3 / kappa_(2,1)
c_3 is recovered EXACTLY from either, both ways (<1e-40) -- reparametrisations,
adding no information. Therefore:
  - the kappa*S split does NOT refute (H1); it says nothing about it
  - the kappa*S split is NOT itself a derived decomposition
  - THE BAR-PARITY OF c_3 IS UNDETERMINED BY THE PRESENT CORPUS

(H1) status: UNDERIVED (no derivation found in docs/, content/, computations/)
-- absence of a derivation, NOT a contradiction with one.

## PARITY TENSION (recorded, not resolved)

kappa_(2,1) is verifiably bar-ODD. The 2026-07-07 audit says S "inherits bar-odd
from Q_beta". odd x odd = EVEN, which would make c_3 = -kappa*S bar-EVEN and
"c_3^odd" a misnomer. Resolution: with S := -c_3/kappa, S's parity is whatever
makes the identity hold -- so no parity information is carried. Second route to
the same corrected conclusion.

## STILL STANDS (unaffected by the withdrawal)

  A. bar-split inaccessible from anchors (needs q ~ 0.901; both at ~1.10998)
  B. S_leak is a 98-99.5% cancellation; 2.4325% -> 507.51% swing, 208.63x, and
     that amplification is ARITHMETIC. (Arguments using the ABSOLUTE difference
     |S_1 - S_2| are unaffected -- the offset cancels there identically. So
     sibling #4734's Lipschitz bound is untouched, as told to them.)
  C. Every theorem in SLeakZeroCrossing / SLeakMagnitude{Offset,Taylor}Ratio
     stands -- generic, hypothesis-carrying. No Lean edited.

## Status: reopened -> the real question moves to qou-qb8g

qb8g is no longer "prove c_3^even = 0" (that premise came from the withdrawn
argument). It is now: NEITHER split is derived, so c_3's bar-parity needs a
genuinely derived decomposition before any bar-parity claim can be made.


---

# *** SECOND CORRECTION (2026-08-08) — "(H1) is UNDERIVED" is ALSO WRONG ***

Withdrawn in the opposite direction. The Phi_b state-integral saddle supplies
the |S| scale from GEOMETRY, fit-free and anchor-blind: at the real substrate
meridian, Im V = 0 exactly (amphichirality) and a volume deficit
0.0094 ~ |S(muon)| = 0.00968. PR #3654; 2026-07-12 capstone result 5; registry
KC21, tier symbolic-exact.

So subtracting a 4_1 volume IS geometrically motivated. What remains open is
narrower: ~2.9% SCALE agreement, not an exact identity; exact normalisation
open; conj:im-q-physical-role still a conjecture.

ROOT CAUSE OF THE MISS: AGENTS.md corpus-grep checklist item 4 = "check the
relevant coordination ledger". I grepped docs/, content/, computations/ for the
strings `S_leak` and `c_3^even` and SKIPPED the ledger. KC21 is indexed under
Phi_b / volume-deficit / ladder vocabulary, so a string search for my own
framing could never have found it. LESSON: for any c_k question, read
docs/coordination/ck-dk-canonical-registry.md FIRST.

ALSO NOT NEW (both independently re-derived by me today, neither discovered):
 - the "209x cancellation amplification" is the known 1/u^3 ladder artifact
   (extractor c_3 = (Q_beta/Q_N2 - 1)/u^3; S'(q*) = 2.37 x 1/u^3, SMOOTH).
   Capstone verdict: "the wall was never physical."
 - the Skein bar-odd factorisation (q - q^-1) x bar-even is the corpus's
   S = h*D(u-tilde) with h = q - 1/q (KC21).

## SURVIVING CONTRIBUTION (small, but real)

THE TWO-S COLLISION. Two objects both called "the c_3 bar-odd S":
    S_leak = c_3 + Vol(4_1)    ~ +0.00968   GEOMETRIC BACKING (Phi_b, KC21)
    S      = -c_3/kappa_(2,1)  ~ 886.79     DEFINITION, no information
ratio ~91582 (~5 orders). The 2026-07-12 capstone STRADDLES them: header +
numbers are S_leak; result 1 says "S = Q_beta/E_0". Conflating them transfers
unearned credibility from the backed object to the definitional one.
SLeakZeroCrossing.lean has a collision guard, so it is known -- but the capstone
crosses it anyway and KC21 inherits the vocabulary.

Status: this bean's question is ANSWERED as far as I can take it. (H1) exact =
open; (H1) motivated = yes. Remaining actionable item is the collision, which is
a documentation/registry matter for the c_3 owners.


---

# *** (c) ANSWERED (2026-08-14, PR #5022) — the registry pointer is placed ***

This bean left item (c) ("should the registry's c_3 row carry a pointer either
way?") to the registry maintainers. Done. `ck-dk-canonical-registry.md` now
carries **§9c**, stating the consolidated (H1) verdict:

  (H1) c_3^even = -Vol(4_1) is NOT derived. Geometrically MOTIVATED (Phi_b
  saddle) but muon-only. The bar-split is not determinable from anchor data at
  all. Neither named split is a derivation -- S_leak := c_3 + Vol(4_1) and
  S := -c_3/kappa_(2,1) are both DEFINITIONS. c_3's bar-parity is UNDETERMINED
  by the present corpus.

Also re-scoped §3's phrase "the -Vol(4_1) piece is the solved bar-even part" ->
**motivated, not solved** (it contradicted this bean's own three-round verdict
while sitting in the same bullet that already records the anchor-blind objection
for the keystone form).

## NEW FINDING that sharpens this bean's second correction

The second correction withdrew "(H1) is UNDERIVED" on the strength of the Phi_b
volume deficit supplying the |S| scale "fit-free and anchor-blind", noting
"~2.9% SCALE agreement". Measured (`kc21_kc22_glyph_and_anchor_robustness_check.py`):

  - the deficit IS anchor-blind (spread 2.2e-7); |S_leak| SWINGS 4.075x.
    An anchor-blind quantity cannot supply an anchor-dependent scale, so the
    match holds at MUON (2.896%) and misses PROTON (76.17%) -- 26.3x apart.
    KC21 quotes only the muon. This is the same objection the corpus already
    accepts against h*D(u~); it was never applied to the deficit.
  - the 2.9% window is not discriminating: the deficit is 5.32x CLOSER to the
    ladder's own expansion variable u~_0 (0.544%) than to |S(muon)|. u~_0 carries
    no 4_1-volume content.

So "(H1) motivated = yes" stands only in the weak sense; the geometric backing
does not survive the anchor test. The verdict in §9c is worded accordingly.
The producing witness is honest -- it records both anchors and says
"|S(muon)|" explicitly; the generalisation happened in the KC21 summary.

## SECOND DEFECT found while placing the pointer (qou-kp9f)

KC21 and KC22 are adjacent and both wrote `q*`, `h*`, `u~(q*)` unqualified for
TWO DIFFERENT points (1.10998 vs 1.48989; ratios 1.34x / 3.92x / 15.1x). Fixed:
both rows subscript (q*_S vs q*_rho) and §9a carries the disambiguation table.

Audit: docs/audits/2026-08-14-c3-registry-glyph-collision-and-anchor-selective-scale.md

Scope-(a). No Lean edited; c_3 tier unchanged; nothing wired; no fit.
Remaining open: the bar-parity itself -> qou-qb8g.

── Verification 2026-08-19 (session qou-a6rd, branch n24484) ──
Re-adjudicated against committed corpus. All three sub-questions ARE resolved; no remaining work — ready for owner-close (§4a).
(a) c₃^even = −Vol(4₁): NOT derived — a near-match. Φ_b saddle motivation (vol deficit 0.0094 ≈ |S(muon)| 0.00968) is ~3% off, muon-only + anchor-selective (fails at proton pin), and convention-C-conditional (§9g). q*_S presupposes (H1); WITHDRAWN as independent q₀ determination (#5074 §9f).
(b) rival c₃^even≈+86.66 = projection artifact / different object (same glyph). Two S's are distinct (SLeakZeroCrossing guards collision). Neither split is a genuinely derived decomposition.
(c) registry pointer landed #5022, refined #5074 §9f. KC21 tiers only the STRUCTURAL parity (proved-lean, Im S odd) + S=h·D split / 1/u³ / Φ_b saddle (symbolic-exact) — the EQUALITY c₃^even=−Vol(4₁) stays (H1), untiered.
Open residuals correctly tracked as qb8e (magnitude gate) + qb8g (bar-parity undetermined). NEW live thread beyond qb8f: whole c₃ ladder is C-frame, awaits convention-D re-derivation (qou-cds1).
