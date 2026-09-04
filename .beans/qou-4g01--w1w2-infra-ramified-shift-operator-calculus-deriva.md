---
# qou-4g01
title: 'W1/W2 infra: ramified shift-operator calculus — derivative-like q-prolongations of shift 1 or 2 cannot produce a residue'
status: completed
type: task
priority: normal
created_at: 2026-09-03T05:06:17Z
updated_at: 2026-09-03T05:18:51Z
---

RESOLVED 2026-09-03, branch claude/ramified-shift-calculus-2026-09-03.

BUILT: QOU.Mathlib.RamifiedShiftCalculus -- the q-D-module symbol calculus at
a simple ramification point on the coefficient model f : Z -> R that
RamificationParityMonodromy already uses. A shift operator
shiftOp k c f = fun e => c e * f (e+k); (k, c) IS the symbol; symbols compose
(shifts add, multipliers multiply along the shift); iterate formula;
residue-slot formula; annihilatesConstants c(-k) = 0 characterised as killing
the constant term. Generic CommRing. Existing modules covered the Jackson
operator in z (QDiffProlongationBaseOperator) and the classical ddz in t
(RamificationParityMonodromy) but not the calculus; nothing rebuilt.

THE W1 PRUNE, exact: every derivative-like operator -- classical d/dz,
q-deformed d/dz in EITHER q-integer convention, Jackson in the local
coordinate -- annihilates constants ([0]_q = 0), and for shift 2 (any seed) or
shift 1 (power-series seed) that kills the t^-2 residue slot at every jet
level. So no derivative-like prolongation of shift 1 or 2 can produce the
binding period; a residue needs a zeroth-order component with c(-k) != 0.
PARITY: even shifts commute with t -> -t, odd shifts anti-commute and alternate
the monodromy eigenvalue as (-1)^n -- the Door-v residual. Together: any
single-shift D_q needs an ODD shift and a NON-DERIVATIVE component. No C1
coefficient enters (W3 anti-fit respected).

NON-VACUOUS: the prune needs sorry without its hypothesis (checked); a
non-annihilating shift-1 operator yields residue f(0), and the probe's
c(-1) = lambda example yields a nonzero multiple of lambda.

HONEST SCOPE: D_q NOT constructed -- W1 remains a wall, narrowed. Single-shift
only; sums of shifts and shift >= 3 not claimed. Keystone untouched.

VERIFIED: lean-direct exit 0 vs real import cone, standard axioms; probe exit
0 (26 exact checks); sidecar swept with hashes matching; render-QA clean.
