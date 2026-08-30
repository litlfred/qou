---
# qou-b5h9
title: 'OPEN: 8_11 (triton knot-ID) KVC is not in Murakami 3.3 - Ohtsuki machinery stops at 6 crossings, this is a paper'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T19:18:13Z
updated_at: 2026-08-30T15:10:00Z
parent: qou-9ot5
---

## ANSWERED 2026-08-25 — partly. See docs/audits/2026-08-25-is-8-11-kvc-attackable.md

NUMERICALLY YES, today. Colored Jones DOES exist in the repo - kashaev_link_statesum.py
(planar state sum + tensor network) is general over any PD code at roots of unity, and it
reproduces fig-8's closed form exactly and runs on 8_11. Cost is N^6 and 8_11 is only
~1.8x Whitehead at equal N (treewidth-bounded 2-bridge); N=61 ~ 10 min. Precision is NOT
the bottleneck - complex128 has ~14 digits of headroom.

THE BLOCKER IS THE CONVENTION, NOT COMPUTE. deficit_face_of returns None (non-unique) for
8_11; 1200 (strand-pair, outer-face) choices give 1184 distinct values at N=7, spanning
[5.205, 15.623]. And 19 of 1200 land within 5% of Vol=8.2863 BY CHANCE, 1 within 2%. So
scanning conventions against the volume is numerology. Needs an independent reference:
generalize norm_weightblock from 3 strands to arbitrary m (the one concrete build item).

PROVABLY NO. Ohtsuki-Yokota's homotopy step is 'quite non-trivial' and they state it FAILS
at 7_2 - an obstruction one crossing lower. Takata's 8-crossing paper is 'in preparation'
and whether 8_11 is in it is UNVERIFIED. And the repo's own squeeze method needs a
positive sum: 4_1 has one (proved), Whitehead does not (3556 Lean lines, two programmes,
both open on exactly that gap), 8_11 has none.

QOU BARELY NEEDS IT. The 3H->8_11 assignment is the same conj:canonical-knot-id-sdp shown
to be AME-driven census fitting, so a volume justification is CIRCULAR. Eleven consumers
use Vol(8_11) as a number, independently certified by SnapPy.

Bug caught: kashaev_link_statesum._solve_mod inverts via Fermat pow(a,N-2,N), valid ONLY
for prime N. Composite N are silently wrong.

---

## 2026-08-30 — the Fermat bug is REAL but LATENT; fixed so it stays that way

The bug this bean recorded ("`_solve_mod` inverts via Fermat `pow(a,N-2,N)`,
valid ONLY for prime N. Composite N are silently wrong") is real, and worse in
detail than recorded — but it has **never corrupted a published number**, and
the reason is structural rather than lucky.

### Why it is worse than stated

At N = 9, `pow(a, 7, 9)` does not merely lose accuracy. φ(9) = 6, so for every
unit `a^7 = a^(6+1) = a` — the "inverse" returned **is the pivot itself**. And
the pivot test accepted any entry nonzero mod N, so a zero divisor (3 or 6
mod 9) could be selected, where `pow` returns **0** and the row is silently
annihilated. Measured on 2×2 systems, composite N = 9 and N = 15 returned
vectors that do not satisfy their own system, and returned them without
complaint (no `None`).

### Why it never bit

Instrumenting the pivots this module actually encounters, across N = 3…15 on
the Whitehead face system: **every pivot is 1 or N−1**. Both are self-inverse,
so Fermat's wrong formula coincides with the right answer. That is structural —
the (3.3)-(3.4) matrix is a 0/1 face-incidence matrix and elimination on it
keeps pivots at ±1.

Recomputing `whitehead_state_sum` at N = 3, 5, 7, 9, 11, 15 with a
provably-correct extended-Euclid solver reproduces the current values
**exactly**. So the N = 9 and N = 11 figures are NOT corrupted, and no
downstream claim moves. This bean's "composite N are silently wrong" should be
read as *would be, in general* — not *were*.

### Fixed

`_solve_mod` now inverts by extended Euclid (correct for any modulus), pivots
only on units, and **raises** rather than continuing if a column offers only
non-unit pivots — the case needing Howell/Smith normal form. A future diagram
whose incidence structure produces a non-unit pivot now fails loudly instead of
returning a plausible wrong answer. Numerically neutral today; the point is that
it stays correct when the input class widens, which is exactly what an 8₁₁
attack would do.

### Separate discrepancy, flagged not chased

The module docstring claims the b(8,3) sum "matches EXACTLY at N=3,5,7,9,11
(27.495, 165.383, 774.957, 3415.876, 14452.890)". Recomputed here:
27.495, 165.383, 774.956, **3415.862**, **14452.775**. The N=9 and N=11 figures
disagree in the 5th–6th significant digit, and identically before and after the
solver fix, so this is not caused by it. Either the docstring quotes a different
variant (b(8,3) sum vs TN evaluator) or one of the two is stale. Worth an hour
from whoever owns that comparison; it is cited as evidence the state sum is
correct, so a mismatch there is load-bearing.

## ROAST of my own "framing" answer (2026-08-30)

Asked whether the saddle structure is "somehow framing data", I answered:

> "Framing enters colored Jones as an overall q-power, so it shifts the phase
> (the CS/imaginary part), not the volume. It is therefore a common twist
> across saddles, not what indexes them."

The first half is textbook-correct and the second half is right — saddles are
indexed by boundary-parabolic PSL(2,ℂ) representations, not by framing. But the
answer was **falsely reassuring**, in a way that matters for this bean.

**I called the 8₁₁ blocker "framing-like" and then applied a theorem about
framing to it.** They are not the same object:

* **Framing proper** is a `q`-power / `e^{iπ…}` factor of modulus 1 at a root of
  unity. It moves the phase. It cannot move `|⟨K⟩_N|`, hence cannot move the
  volume. True.
* **The 8₁₁ blocker** is the `deficit_face` / `outer_face` choice in
  `kashaev_link_statesum`. Measured in this bean: 1200 (strand-pair, outer-face)
  choices give **1184 distinct values spanning [5.205, 15.623]** at N = 7. That
  is a **modulus** spread of a factor of three. It is a gauge/normalisation
  ambiguity in the state sum, not a framing factor.

So the sentence "framing only moves the phase" is true and irrelevant here, and
putting it next to the 8₁₁ obstruction implied the obstruction was harmless in
the same way. It is the opposite: the thing that is unpinned moves exactly the
quantity the volume conjecture is about.

Second, smaller: "shifts the phase" understates framing. The Chern–Simons
invariant is only well-defined **modulo** a framing-dependent constant, so if
`Im V` is ever used as data (it is — `fivetwo_stokes_matrix_zq` carries
`V(σ₁) = Vol(5₂) + i·CS(5₂)`), the normalisation has to be pinned before the
imaginary part means anything. Saying "it's just a phase" hides that.

**Corrected statement.** Framing is a phase and does not index the saddles.
The 8₁₁ obstruction is *not* framing — it is an unpinned diagram/gauge
convention in the state sum that changes the modulus by a factor of three, and
is therefore squarely on the volume side. The owner's instinct that
"framing-type data" is where the trouble lives was right; my reply pointed at
the wrong invariant and made the situation sound settled.

## 2026-08-30 — 8₁₁ IS two-bridge (8, 27), and 17 of the corpus's 19 knots are

Measured with SnapPy `Manifold(k).is_two_bridge()`:

| knot | 2-bridge | role |
|---|---|---|
| 4₁ | (2, 5) | muon anchor — VC proven in-repo |
| 5₂ | (−2, 7) | VC proven (Ohtsuki) |
| 6₁ / 6₂ / 6₃ | (−2,9) / (3,11) / (5,13) | VC proven (Ohtsuki–Yokota); 6₂ is the ²H closure |
| 7₂ / 7₃ / 7₄ | (2,11) / (−3,13) / (−4,15) | Tier-1 PSLQ basis |
| 8₃ / 8₉ / **8₁₁** / 8₁₂ | (4,17) / (7,25) / **(8, 27)** / (12,29) | τ candidates; **8₁₁ is the ³H closure** |
| 8₁₇, 8₁₈ | **no** | τ candidates |
| 10₁₇ / 10₃₃ / 10₃₇ / 10₄₃ / 10₄₅ | (9,41) / (18,65) / (23,53) / (27,73) / (34,89) | τ candidates |

**Why this matters now.** The owner has supplied Ohtsuki, *On the Kashaev
invariant and the twisted Reidemeister torsion of **two-bridge** knots*
(Geometry & Topology 19 (2015) 853–952) — `library/download-1/Download (1).pdf`. If its
main theorem is an **unconditional** statement for all two-bridge knots, it
reaches 8₁₁ directly, and this bean's load-bearing open VC instance closes.
Every 10-crossing τ candidate would close with it.

That is a large *if*, and the title argues against it: "twisted Reidemeister
torsion" suggests the **subleading (1-loop) term**, which is normally studied
*given* the asymptotic expansion rather than establishing it. The companion
upload Garoufalidis–Yoon, *1-loop equals torsion for two-bridge knots* (2024,
`library/arxiv-2411.03801v2/2411.03801v2.pdf`) points the same way. So the likely reading is that
these refine the expansion rather than prove the volume conjecture — but that
is a prediction, and the papers are being read now rather than guessed at.

**What is settled regardless:** 8₁₁'s two-bridge-ness is not the obstruction.
Whatever blocks it is the strength of the available theorem, not the knot's
position in the classification. And 8₁₇/8₁₈ are outside the two-bridge class
entirely, so no two-bridge result will ever reach them — worth knowing before
the τ search settles on a candidate.
