---
# qou-qb8g
title: "c_3's bar-parity is UNDETERMINED — neither named split is derived"
status: todo
type: task
priority: medium
created_at: 2026-08-08T11:45:00Z
updated_at: 2026-08-08T12:05:00Z
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

**Two independent objects, one wall: an anchor-blind quantity cannot deliver an
anchor-dependent one.** The Phi_b deficit (2.2e-7) fails it for `S_leak`; the
`h*D` carrier (1.23e-9) fails it for `S`. That is the actual gate, and it is
`qou-qb8e`'s magnitude channel. These two beans close together or not at all.

## Discipline note

Three corrections on one bean, alternating direction. Before a FOURTH: the
failure mode here has been re-reading a *scale* agreement at one anchor as
structural support. Any future reversal must state, up front, what it predicts
at the **proton** anchor -- not just the muon one.
