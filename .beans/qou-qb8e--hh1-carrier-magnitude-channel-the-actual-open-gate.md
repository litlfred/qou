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
