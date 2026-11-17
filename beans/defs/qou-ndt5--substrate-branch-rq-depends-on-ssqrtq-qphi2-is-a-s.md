---
# qou-ndt5
title: 'Substrate branch: r(q) depends on s=sqrt(q); q=phi^2 is a second degeneration missing from the regime table'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T12:24:17Z
updated_at: 2026-11-17T10:13:44Z
parent: b9cj
---

ALGEBRA SETTLED (2026-09-07, PR #7077, issue #7076). s^2+s-1 has root set {1/phi, -phi}; q=s^2 gives {(3-sqrt5)/2, (3+sqrt5)/2} = {phi^-2, phi^2}, exactly reciprocal. Quartic 4s^4-s^3-4s^2+s+4 has NO real roots (all four complex), so that is the whole real locus. s -> -1/s is the UNIQUE lift of q -> 1/q preserving it (s -> 1/s maps the quadratic to s^2-s-1, a different polynomial). Source formula in descartes-elliptic-curve.md carries q^(3/2) and sqrt(q), so r depends on s not q; its 'expressible directly in q' claim is false. NOT closing this bean: whether s = -sqrt(q) is PHYSICALLY admissible is an open question about the framework, not settled by the algebra (AGENTS.md 13a).

REFRAMED + FORMALISED 2026-09-07. My earlier framing was wrong twice. (1) 'r depends on s not q' misses the point: the modulus is z = s - 1/s (the corpus's own spacetime ratio) and r is a clean POLYNOMIAL in z, r = (5/27)(z+1)(4z^2-z+4) = (5/27)(4z^3+3z^2+3z+4) — which is EXACTLY the q_W(z) already in t-duality-elliptic.md. Two blocks agree; one sentence of presentation in a third is wrong. (2) 'the corpus lists half the locus' is wrong: there is ONE degeneration, at z = -1 (since z+1=0 <=> s^2+s-1=0), whose two q-preimages are phi^-2 and phi^2. The table lists one preimage of one point. Now Lean: QOU/BringsSurface/ColourCurveModulus.lean, 6 theorems, lean-direct exit 0 with -DautoImplicit=false, 0 sorry, axioms = {propext, Classical.choice, Quot.sound} only.

OWNER RULING 2026-09-07, verbatim: 'not sure. don't exclude but maybe not observable.' So the negative branch s = -sqrt(q) stays OPEN, not excluded, with the live possibility that the two sheets are physically identified and the branch carries no observable. Bean stays open per AGENTS.md 13a. GATES: the bounded window (phi^-2, phi^2) depends on this — if the negative branch is unreachable, q = phi^2 is not a reachable degeneration and the window is NOT bounded above. The Lean and the bar-defect results are unaffected: they are statements about z, and z = -1 is one point regardless of how many q-preimages are physical.


---

## 2026-09-13 — the 7.878 % is a BRANCH defect, not a BAR defect (and this settles nothing the owner left open)

Reached from `qou-fi93` and `qou-hjs8`. **Two involutions are in play here and
they are not the same one**, which is the whole content:

| | acts on q | acts on z = s − 1/s |
|---|---|---|
| **the BAR**, `q -> 1/q`, lifted `s -> −1/s` | inverts | **FIXES it** |
| **the BRANCH**, `s -> −s` (same q, other root) | fixes | **NEGATES it** |

Verified exactly: `z(−1/s) − z(s) = 0` and `z(−s) + z(s) = 0`, and each map
really does what is claimed to `q = s²`. Also re-verified this bean's own
uniqueness claim from the other side: `s -> −1/s` sends `s²+s−1` to
`−(s²+s−1)`, while `s -> 1/s` sends it to `−(s²−s−1)`, a different polynomial.

### Consequences

1. **`r` is EXACTLY bar-invariant.** It is a polynomial in `z`, and the bar
   fixes `z`, so `r(bar s) − r(s) = 0` identically — zero defect, not a small
   one.

2. **`qou-fi93`'s `bar_defect` is the BRANCH defect.** Verified symbolically
   that `r(z) − r(−z)` IS `(10/27)·z·(4z²+3)`, this bean's and `qou-fi93`'s
   own formula. So that 7.878 % is a difference between the two square roots
   of ONE q — not between q and 1/q. **The name `bar_defect` is a misnomer**;
   it is a branch defect.

3. **A second, independent route to `qou-fi93`'s exclusion.** Matter and
   antimatter are related by the BAR
   (`prop:antiparticle-crossing-reversal` sends `q <-> q^-1`), and a
   bar-invariant quantity cannot distinguish them at all. So the colour curve
   is the wrong parity to carry a matter/antimatter asymmetry — structurally,
   not because the available counting measures happen to be bar-even.
   `qou-fi93` reached that by surveying the counting objects; this reaches it
   from the other side: the colour curve has no bar-odd part to couple TO.

### A normalisation trap I walked into, recorded so nobody else does

My first run reported the branch defect as **15.757 %** against this bean's
**7.878 %** — exactly a factor of 2, because I divided by the MEAN while
`qou-fi93` divides by the SUM. AGENTS.md names this class directly ("a
quantity differing only by normalisation, mistaken for a discrepancy"). The
probe now prints **both**, labelled, and asserts the ratio is exactly 2, so
the two figures cannot be read as disagreeing.

Sum-normalised: **7.87846669404 %**, reproducing this bean exactly.

### A bonus identity tying this to the companion probe

    z0 * (s0 + 1/s0) = q0 - 1/q0     (verified to 1e-50)

i.e. the sqrt-variable bar-odd factor times the sqrt-variable bar-EVEN factor
is the q-variable bar-odd factor. Same structure one level down from
`crossing_energy_bar_split_probe.py`.

### WHAT THIS DOES NOT SETTLE — the owner's open call is untouched

* **Whether the negative branch is observable.** The owner's standing ruling
  is *"not sure. don't exclude but maybe not observable."* Nothing here bears
  on it. This says only which involution the defect belongs to.
* **Whether the window `(phi^-2, phi^2)` is bounded above.** That gate depends
  on the observability question above and is unchanged.
* **Whether the 7.878 % is physical.** It is a real difference between two
  square-root branches. Calling it branch-parity rather than bar-parity says
  what it is, not whether it is realised.

Bean stays open per §13a and per the owner's ruling.

Artifacts: `computations/barparity/colour_curve_bar_vs_branch_probe.py`
(exact sympy, one mpmath mpf at 60 dps, no float64, rc 0);
`QOU/BringsSurface/ColourCurveBarVsBranch.lean` (8 declarations, sorry-free,
`lean`-direct exit 0 with zero output, generic over a Field with no anchor).
Note `zOf_barLift` needs NO `s != 0` hypothesis — in a field `0^-1 = 0`, so
the bar-invariance of z is unconditional, and carrying a hypothesis the proof
does not use would have suggested otherwise.


--------

## 2026-09-13 (later) — CORRECTION to the append above: the BAR HAS TWO LIFTS to sqrt(q), and the append picked one without saying so

PR #7313 (commit aa6e877569), Lean QOU/BringsSurface/BarLiftAmbiguity.lean
(11 decls, sorry-free), probe
computations/barparity/bar_lift_ambiguity_probe.py (rc 0).

THE APPEND ABOVE IS MINE, FROM EARLIER TODAY, AND IT OVERSTATED TWO THINGS.
Both are conditional on a convention the corpus has never ruled on.

### The collision, read off two existing definitions

    QOU/Braiding/SkeinNormalisation.lean:74           sJ  (u) := u - u^-1
    QOU/BringsSurface/ColourCurveBarVsBranch.lean:45  zOf (s) := s - s^-1

BYTE-IDENTICAL. One is the half-power skein normalisation's bar-ODD
generator; the other is this bean's spacetime modulus z. Neither arc cites
the other.

The two arcs then lift the bar q -> q^-1 to the square root DIFFERENTLY, and
BOTH lifts are legitimate -- each squares to q^-1:

    SkeinNormalisation (sJ_bar_antiinvariant)    u ->  u^-1
    ColourCurveBarVsBranch (barLift)             u -> -u^-1

and they differ by EXACTLY the branch swap u -> -u. So "WHICH LIFT" and this
bean's "IS THE NEGATIVE BRANCH OBSERVABLE" are ONE question, not two.

### The same object, opposite parity

    under u ->  u^-1 :  z -> -z    bar-ODD
    under u -> -u^-1 :  z ->  z    bar-EVEN

THE BAR PARITY OF z IS NOT DETERMINED BY THE BAR ON q (Lean:
z_parity_not_determined). Fixing it requires choosing a lift.

### What that corrects

  1. "The name bar_defect is a MISNOMER; it is a BRANCH defect."
     CONDITIONAL. True under barLift. Under the skein lift the bar ITSELF
     negates z, the defect is a bar defect, and the original name was right.
  2. Consequence 3, offered as "a second, INDEPENDENT route to qou-fi93's
     exclusion" -- "the colour curve has no bar-odd part to couple TO."
     ALSO CONDITIONAL. Under the skein lift it HAS one.

  qou-fi93's PRIMARY route is UNAFFECTED: its survey showing every counting
  measure is bar-even never passes through the square root. What is weakened
  is the second route only, and the second route was mine.

### Measured

The colour curve's defect is EXACTLY 0 under barLift and 10 z (4z^2+3) under
the skein lift -- the same formula both beans call the bar defect. At the
proton pin, 60 dps: 7.87846669404 % in qou-fi93's (sum) normalisation,
15.7569333881 % in the mean normalisation, ratio asserted exactly 2 so the
two cannot be read as disagreeing.

### Why barLift was chosen, and what that choice actually buys

This bean selects s -> -s^-1 as "the UNIQUE lift of q -> 1/q preserving the
degeneration locus s^2 + s - 1". THAT UNIQUENESS IS CORRECT -- and it is
uniqueness SUBJECT TO PRESERVING THAT POLYNOMIAL, not uniqueness among lifts
of the bar. The skein lift is an equally valid lift preserving something else
(its own parity grading). Two defensible conventions and no ruling between
them.

### THE DECISION THIS PUTS IN FRONT OF THE OWNER, and it is this bean's own

The standing ruling is "not sure. don't exclude but maybe not observable."
What is new is that the choice is NOT FREE. Naming the lift decides whether
the colour curve has bar-odd content at all, and therefore whether the second
route to qou-fi93's exclusion exists:

  * choose u -> -u^-1 (barLift, the current ColourCurveBarVsBranch
    convention): z is bar-EVEN, r is exactly bar-invariant, the 7.878 % is a
    BRANCH defect, and qou-fi93's exclusion gains a second independent route.
    The negative branch is then the thing that carries the asymmetry, so
    "maybe not observable" would make the 7.878 % unobservable too.
  * choose u -> u^-1 (the skein convention): z is bar-ODD, it IS the
    half-power ring's bar-odd generator, the 7.878 % is a BAR defect after
    all, and the colour curve has bar-odd content that a matter/antimatter
    asymmetry could in principle couple to. The second route to qou-fi93's
    exclusion then does not exist (the primary one still does).

NEITHER ARTIFACT CHOOSES, and neither should. Recorded so that whoever rules
knows the price.

This bean stays OPEN (sec 13a) -- the observability question is untouched and
now has a measured consequence attached to it.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 82 Execution Note (2026-11-17T10:13:44Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8294`](https://github.com/litlfred/qou/pull/8294) (`feat/qou-b9cj-ck2w-k5r5-ndt5-x3iv-x631`, HEAD `22907bca8b5dd626221c15ea2658a1f14545c5be`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/PretzelSymmetryAdaptedGradingAndSubstrateBranchBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/pretzel_symmetry_adapted_grading_and_substrate_branch_brick_probe.py` & `computations/probes/pretzel-symmetry-adapted-grading-and-substrate-branch-brick.witness.json` (`scriptCommitSha = caec3a2639d9338bfaf9aa9d455a0ab97b427071`, `scriptHash = 428700c5c7bd`, `outputHash = 27ee54e84b99cf035202cc1272490bd167d1f4ad8e861ae3bd043848cca760e3`).
