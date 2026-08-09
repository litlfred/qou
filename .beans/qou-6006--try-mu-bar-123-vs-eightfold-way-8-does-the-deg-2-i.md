---
# qou-6006
title: 'TRY: mu-bar-123 vs eightfold-way §8 -- does the deg-2 invariant fill the falsified-writhe Y slot?'
status: completed
type: task
priority: normal
created_at: 2026-08-09T03:05:01Z
updated_at: 2026-08-09T10:33:06Z
parent: qou-5b8n
---

RESULT (2026-08-09): battery reduction PROVED sorry-free (HyperchargeBatteryReduction.lean).
RH half of battery 2 is an identity (GMN at I3=0 pins Y=2Q uniquely) -> 0 independent
conditions, same vacuity as Gell-Mann-Okubo. LH half is exactly B - L. Battery 1 is the
L=0 restriction Y=B. So battery 2 imposes ONE condition: derive B-L on the LH sector.
mu-bar_123 = B supplies the B half only; the L half stays open.

REMAINS OPEN - needs OWNER decision, not an agent call:
PR #4597's candidate table EXCLUDES the framing phase q^(w.c)/ribbon twist ('factors
through w'), while the LANDED flavor-charge-assignments.md names the ribbon-framing
twist T(t) as THE candidate direction, asserting T(t) is independent of the crossing
word. Possibly different objects (a phase built from w factors through w; an independent
per-strand twist datum need not). As written the two documents contradict; one is wrong.
Cannot resolve without the owner's definition of T(t).


RESOLVED 2026-08-09 — the contradiction was MY mislabelling, not a real disagreement.
def:strand-twist-datum's T(t) is a free per-strand Z label; its Lean sibling proves
exists_same_writhe_ne_totalTwist, so it provably does NOT factor through w. My audit
table had lumped 'framing phase q^(w.c) / ribbon twist' into ONE row and excluded it;
the phase does factor through w, the twist datum does not. Split into 1a/1b + appended
correction. No owner decision needed after all.

FOLLOW-ON (new, open): T(t) is independent precisely because it is FREELY ASSIGNABLE,
so the published enumeration gives no corroboration -- TwistBatteryVacuity.lean proves
the battery collapses to T = 3Q per flavour and 4 = 1x2x2x1 is multiset counting.
The parameter-free repair (canonical ribbon twist, Q = contentSum(lambda)/3) was TESTED
and FAILS: n=3 gives integer charges {+1,0,-1}, no n<=8 gives both quark charges.
Scope-(a), plain content-sum reading only. Remaining untested normalisations:
kappa = <lambda,lambda+2rho>, colour-tube-weighted content, framed braid words per
chiral fermion (the chapter's own route).
