---
# qou-qb8b
title: 'Is the HH^1 outer class bar-ODD? The decisive cheap c_3 prune'
status: todo
type: task
priority: high
created_at: 2026-08-08T08:10:00Z
updated_at: 2026-08-08T08:10:00Z
---

Formalize-first prune for the one surviving c_3 route. Depends on / extends
qou-jcmw (PROBE A1, dim HH^1(H_5(zeta_5))) and qou-dilv (PROBE A2, He-Nie
cocenter -> HH^1 lift). Both are `todo`; nobody is on either.

The setup (all merged, all sorry-free):
- Surviving c_3 carrier after the real-q0 exclusion chain (#4282/#4288/#4293,
  scope-(b) for STRICTLY REAL q0) is a fibre-level COMPLEX phase: q-Pochhammer
  pole x = q^{-k} + cusp phase omega = e^{i pi/3}
  (docs/audits/2026-07-19-c3-q0-real-routes-closed-fibre-phase-survives.md).
- The invariant that closed the real routes is BAR-PARITY: a real, trace-built
  (bar-EVEN) Gram resolvent cannot carry the bar-ODD S.
- Landed 2026-08-07: CocenterTraceFactor.lean (trace factors through
  HH_0 = A/[A,A]); OuterDerivationResidue.lean (every INNER derivation is
  trace-blind); hh1_hecke_outer_derivations.py (dim HH^1(H_3(q)) = 0 generic,
  = 1 at roots of unity [2]_q = 0, [3]_q = 0).

The observation nobody has recorded: the derivation-theoretic content surviving
the Markov trace is exactly the OUTER part, and the outer part exists exactly at
ROOTS OF UNITY -- the same address (fibre-level, cyclotomic, invisible to real
trace data) as the surviving c_3 carrier.

CAVEATS THAT ARE LOAD-BEARING (do not skip):
- Co-location is NOT a derivation. HH^1 was built for the P!=NP residue.
- Degree mismatch: c_3 arrives via tr_M => lives in HH_0 (cocenter); derivations
  are HH^1. The link is the ACTION of HH^1 on HH_0 -- exactly qou-dilv.
- q0 ~ 1.10998 is NOT a root of unity ([2]_q ~ 2.011 != 0). Not fatal: per
  AGENTS.md §"Im(q) at fibre vs observable level" the c_k live in the FIBRE and
  the target is a Habiro-ring element evaluated at q0. The Habiro ring is
  assembled from evaluations at ALL roots of unity, so a class whose dimension
  jumps 0 -> 1 exactly on the cyclotomic locus is the right KIND of object.
  "Right kind" is not "is".

THE TEST (decisive either way, one finite-dim linear-algebra computation):
compute the outer class's action on the cocenter at the Bring root of unity and
read its BAR-PARITY. If bar-EVEN, the route dies to the same bar-parity
invariant that killed the real resolvent -- a real prune, cheaply bought. If
bar-ODD, it is the first object that clears the obstruction and the route earns
a Lean statement.

Anti-fit guardrail: a per-anchor-fitted phase is a FIT, must be labelled one,
and may NOT be wired. Nothing here is wired.

Analysis: docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md §5.
