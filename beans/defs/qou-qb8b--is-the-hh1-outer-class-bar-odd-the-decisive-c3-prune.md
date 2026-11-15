---
# qou-qb8b
title: 'Is the HH^1 outer class bar-ODD? The decisive cheap c_3 prune'
status: completed
type: task
priority: high
created_at: 2026-08-08T08:10:00Z
updated_at: 2026-08-08T09:30:00Z
---

## RESULT (2026-08-08): the proposed prune DOES NOT EXIST — answered, scope-(a)

Ran it. `computations/hh1_outer_class_cocenter_bar_parity.py`;
witness `hh1-outer-class-cocenter-bar-parity.witness.json`;
audit `docs/audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`.

The bar-parity of the HH^1 outer class acting on HH_0 is **a choice of
normalization, not an invariant of the class**. Both parities are always
available, so bar-parity can neither kill nor confirm the fibre-level c_3
carrier.

Measured (H_3, exact cyclotomic, 8 assertions/point, all pass):

| point | dim HH^1 | Delta^bar ∝ Delta | lambda | raw parity |
|---|---|---|---|---|
| q = i ([2]_q=0)   | 1 | yes | +1 | bar-EVEN |
| q = zeta_6 ([3]=0)| 1 | yes | -1 | bar-ODD  |
| q = 2 (control)   | 0 | --  | -- | n/a |

Why: dim HH^1 = 1 fixes the representative only up to `D -> cD`, under which
the parity is multiplied by `bar(c)/c`. Involutivity forces
`lambda*bar(lambda) = 1` (asserted), which is the Hilbert-90 hypothesis for
`Q(zeta)/Q(zeta)^+`; H^1 of that extension vanishes so `lambda = bar(c)/c` is
always solvable. Demonstrated constructively, not argued: rescaling by a
bar-ODD scalar FLIPS the parity at BOTH points (q=i: EVEN->ODD via c=2i;
q=zeta_6: ODD->EVEN).

Deeper reason, worth carrying: the real Gram resolvent lived over R where bar
acts TRIVIALLY, so its parity was rigid and the prune was real. At a root of
unity bar is the nontrivial Galois map zeta -> zeta^{-1} and Q(zeta) contains
bar-odd scalars (zeta - zeta^{-1}). The very feature that let the fibre route
survive the real-route exclusion is what makes bar-parity uninformative here.

### Actions for successors

- **qou-jcmw: do NOT run its parity leg expecting a prune.** The
  normalization-dependence is field-theoretic and n-independent. The dimension
  count is still worth having; the parity readout is not. Saves a dim-120
  solve (14 400 unknowns, ~1.7M Leibniz equations).
- A parity test regains content only against a PINNED normalization. Closest
  to what the c_3 front needs: pin the whole construction
  `S = <tr_M, Delta(x)>` for a canonical generator x in HH_0 and read the
  parity of THAT NUMBER (c_3's swing is a number, not a class). Filed as
  qou-qb8d.

Nothing wired. No fit. c_3/Q_beta gap unchanged and open.

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
