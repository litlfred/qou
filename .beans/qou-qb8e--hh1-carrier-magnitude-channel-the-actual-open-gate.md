---
# qou-qb8e
title: 'HH^1 carrier: the MAGNITUDE channel — the actual open gate for c_3'
status: todo
type: task
priority: high
created_at: 2026-08-08T10:15:00Z
updated_at: 2026-08-08T10:15:00Z
---

Successor to qou-qb8b + qou-qb8d, which between them settled the PARITY channel
for the HH^1 fibre-level c_3 carrier:

- qou-qb8b: bar-parity of the outer CLASS is normalization-dependent
  (Hilbert 90 over Q(zeta)/Q(zeta)^+) -- carries no information.
- qou-qb8d: bar-parity of the tr_M-PAIRED NUMBER is well defined against
  structural pins (He-Nie generator + Ocneanu trace), is NOT trace-blind, and
  is MIXED with a NONZERO bar-ODD component.

Net: the bar-parity obstruction that closed every real-q0 route does NOT close
the HH^1 route. The parity screen is PASSED. That was the cheap channel.

THE ACTUAL GATE IS MAGNITUDE, and it is untouched. Nothing so far reproduces
c_3's value (-2.0202 at the cache q0) or, more importantly, its ANCHOR SWING
-- the cross-anchor variation that is the whole reason c_3 is tier
'cal-anchored' rather than 'derived'
(docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md).

What a real attack needs, in order:

1. **A map from the outer class to a NUMBER at the substrate anchor.** The
   n=3 pairing gives numbers in Q(zeta)[z]. c_3 is evaluated at real q0 ~
   1.10998, which is NOT a root of unity. Per AGENTS.md §"Im(q) at fibre vs
   observable level" the correct target is a HABIRO-RING element whose
   archimedean evaluation at q0 reproduces c_3 at THAT anchor. So the
   root-of-unity values must ASSEMBLE (over all zeta) into a Habiro element --
   that assembly is the real content and is not started.

2. **The Bring case.** n=3 is the mechanism; the Bring fibre is H_5 at zeta_5
   (bean qou-jcmw, for the DIMENSION count -- explicitly NOT its parity leg,
   see qou-qb8b).

3. **A falsifiable magnitude prediction BEFORE looking at the target.**
   Formalize-first: state what the construction predicts, then compare. Fitting
   a normalization to land on -2.0202 is a FIT, is the seventh-ansatz failure
   mode the corpus already names, and must not be wired.

ANTI-FIT GUARDRAIL (load-bearing): the parity result is NECESSARY, NOT
SUFFICIENT. Do not let "the parity works" license a magnitude fit. A derived
c_3 must come out of the construction with its normalization pinned in advance.

---

# FRONT-STATE CORRECTION (2026-08-08) — this bean was STALE; read before probing

I attacked this bean and generated four "findings", ALL of which were already in
the corpus. Recording the accurate front state so the next agent does not repeat
it. **The c_3 front is ~20 probes deep. Read the ledger + the capstone FIRST.**

## What this bean got wrong

It says "Nothing so far reproduces c_3's value or, more importantly, its ANCHOR
SWING". That framing is superseded. The swing is UNDERSTOOD:

 - the extractor is c_3 = (Q_beta/Q_N2 - 1)/u^3; S'(q*) = 2.37 x (1/u^3) is a
   SMOOTH O(1) prefactor over a tiny u^3 (2026-07-12 capstone result 3, #3636)
 - capstone verdict: "the wall was never physical". It has an explicit
   "what NOT to re-chase" section.
 - the swing is the 1/u^3 extractor acting on experimental Q_beta -- it is NOT
   a property of any fibre-level u-tilde function.

## The ACTUAL open gate (replaces items 1-3 above)

log R = E(u~) + h*D(u~) HOLDS exactly (h = q - 1/q, u~ = q*u, verified to
ORD 19 with 9 over-determining orders zero; d_1..d_9 exact in Q(sqrt3);
extended to k=31 at ORD 63).

The D-ladder is DIVERGENT -- Gevrey class exp(Bk + Ck*log k), triple-confirmed.
So closing S needs RESUMMATION, and that is the open front:

 - NO instanton action identified (Borel-plane singularity unlocated)
 - Leroy estimator gate FAILS at every scanned s at k=21; parity-split branches
   0/9 and 0/9; the k=21 dlog-Pade/root-test inconsistency persists
 - fixed-base Jackson q-Borel REFUTED (over/under-accelerates; only the Q->1
   Leroy boundary matches the growth class)
 - D is SMOOTH through q*; the S=0 zero lives in the h*D -> S BRIDGE, not in D
 - the k=31 extension exists and the carrier SATURATES there
   (|O_31 - O_21| ~ 6.94e-29), so more terms alone will not move it

## Do NOT re-derive these (I did; all four were already known)

 1. "the hypersensitivity is an artifact not structure" -> capstone result 3
 2. the Skein bar-odd factorisation (q - q^-1) x bar-even -> KC21's S = h*D
 3. "h*D is anchor-blind and cannot be the swinging S" -> stated verbatim in
    qbeta-c3-qstar-k31-repin.witness.json: "the carrier is anchor-blind
    (spread 1.23e-9) and is NOT the swinging empirical S, so 'S=h*D(u)' is
    schematic, not a tight identity"
 4. "S_leak is a ~200x cancellation" -> the 1/u^3 ladder inversion, same result 3

## Where a real contribution could come from

The resummation arm, specifically: identify the Borel-plane instanton action for
the exp(Bk + Ck log k) class. Everything else is downstream of that. This is a
hard analysis problem, not a probe -- do not approach it by scanning.

Read first, in order:
  docs/coordination/ck-dk-canonical-registry.md  (KC21 row)
  docs/audits/2026-07-12-c3-wall-resolution-capstone.md  (+ its "do not re-chase")
  docs/audits/2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md
  computations/qbeta/qbeta-dladder-*.witness.json  (~20 arms, check before probing)

---

# SECOND FRONT-STATE CORRECTION (2026-08-09) — the resummation arm is DISSOLVED,
# not blocked. The premise was false.

I took the "ACTUAL open gate" above at face value ("identify the Borel-plane
instanton action for the exp(Bk + Ck log k) class") and went at it analytically
rather than by scanning, as instructed. There is no such class.

**The D-ladder is CONVERGENT.** Radius

    rho  = u~(q*) = 0.14279999664468968890572088577932032058109273315046...
    1/rho          = 7.0028012849899955047002755670642702546578912740699...

where q* = 1.4898947996883652482253115227781736826531279179281... is the unique
real root > 1 of the irreducible degree-12 factor of the Delta_net numerator --
i.e. **a zero of Q_b**, at which log R has a plain logarithmic branch point.

    d_k = -(1/(2h*)) * rho^-k / k * (1 + O(1/k)),   h* = q* - 1/q* = 0.8187064713519...
    1/(2h*) = 0.61071949165658530740674396151590239...

Amplitude predicted from the residue BEFORE looking at any d_k. Measured
k|d_k|rho^k / (1/(2h*)) = 0.9763 (k=21), 0.9874 (k=41), 0.9950 (k=101),
0.9975 (k=201), correction -0.51/k, no oscillation. Ladder extended to k=201
(the k=41 block was sympy `radsimp∘cancel∘together` per coefficient plus two
O(ORD^3) steps -- purely computational; a numeric-coefficient rebuild of the
same pipeline does ORD 403 in 53 s and matches the exact Q(sqrt3) ladder to
200+ digits for every k <= 41).

**What the 2026-07-12 divergence correction missed:** its singularity search
covered the sqrt branch points, the u~'=0 folds, the Q_A zeros and the
cos(alpha_eff) zeros -- but not the zeros of **Q_b**. The three nearest
singularities in the u~ plane are all Q_b zeros (0.14280, 0.25754, 0.25754).
The original PR #3716 Domb-Sykes "rho ~ 0.143" was RIGHT.

Every published diagnostic reproduces exactly and is re-explained by the
convergent law -- root test 5.91@21 / 6.08@27, log|d|/(k log k)=0.4963972525@41,
log|d|/k^2=0.04496114563@41, C=0.077/0.062/0.048 (the SAME C comes out of
fitting A+Bk+Ck log k to the exact convergent law: 0.084/0.072/0.051), and
|O_31 - O_21| = 6.94484e-29 which is not saturation but geometric convergence
(next increments 7.79e-41, 9.63e-53, 7.56e-124).

Cheap discriminator nobody ran: **k^2 * Delta^2 log|d_k| -> 1** (measured 0.960,
0.975, 0.987, 0.990 at k=20,40,80,99) while **k * Delta^2 -> 0** => Gevrey index
kappa = 0. The single-instanton probe fit Delta^2 = m/k + b and read b->0 as
"ordinary Gevrey", but both hypotheses give b->0; 1/k vs 1/k^2 is the test.

**Named invariant / falsifier** (so this negative is reusable): any claim of
Gevrey growth, a nonzero instanton action, or a Stokes ambiguity in D must first
exhibit a singularity of log R(q) - log R(1/q) strictly inside |u~| < rho. The
complete singular set is enumerated in the audit; none is.

**Payoff, and its limit.** At the CAL-2/muon pin u~(q0) = 0.00945395003124 is
15.10x INSIDE rho, so h*D(u~0) = -0.003486063636129187405605313929674524979867
is already pinned to 38 digits by the committed k<=41 ladder with a rigorous
tail bound. But this does NOT derive c_3, does NOT change its cal-anchored tier,
and does NOT close L2: the mu-p anchor swing on Q_beta is 29.96 ppb = 3.84x the
7.797 ppb target, and this bean's own earlier note stands -- the carrier is
anchor-BLIND (spread 1.23e-9) and is therefore not the swinging empirical S.

**So: the resummation arm was never the gate; it was an artifact.** The gate is
still the map from a bar-odd, anchor-blind fibre-level object to an
anchor-DEPENDENT number. Do not open another Borel/Leroy/Stokes/Ecalle probe on
this ladder.

Full write-up, with the singularity inventory, the exact minimal polynomials,
the reproduction recipe, and the corrections owed to registry row KC22 and
docs/precision-goals.md §"Open compute levers" (i):
  docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md
