#!/usr/bin/env python3
"""Markov-trace WEIGHTING sub-problem of conj:s5-so3-fiber-action (the last open
piece after the generation SELECTION was realized by the Hopf moment map mu).

After mu realizes the ell->lambda SELECTION (spatial SO(3)-equivariance), the
remaining open piece is the WEIGHTING: a geometric structure whose Reeb-trace
reproduces the Ocneanu/Plancherel weights  W_lambda = d_q(lambda)^2 / [n]_q!  of
H_n(q).  The candidate arena (from the round-S^5 transversality obstruction) is an
SU(3)/SO(3)-homogeneous Sasakian whose Reeb sits in the SPATIAL SO(3)_colour.

This script records the VERIFIABLE compatibility facts (it does NOT construct the
Sasakian structure -- that is genuine differential geometry, the handoff point):
  * dim SU(3)/SO(3) = 8 - 3 = 5 (odd -> Sasakian-dimension-compatible).
  * the forced target weights W_lambda for the generation blocks at q0.
The OPEN geometric sub-questions are stated in the companion .md.

deps: pyhecke (qou_substrate, mpmath, numpy).
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
for sub in ("tools/qou-substrate/python", "tools/pyhecke/python", "tools/pyhecke-native/python"):
    p = os.path.join(ROOT, sub)
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from pyhecke import atom
    import pyhecke.constants as c
except ImportError as e:  # pragma: no cover
    atom = None
    c = None
    print(f"SKIP: pyhecke unavailable ({type(e).__name__}: {e}).")
    if os.environ.get("CI"):
        sys.exit(1)   # do NOT silently pass in CI where deps are expected
    sys.exit(0)

DIM_SU3 = 8        # dim SU(3)
DIM_SO3 = 3        # dim SO(3)
dim_quot = DIM_SU3 - DIM_SO3

print("=" * 70)
print("Markov-weighting sub-problem: compatibility facts (NOT a construction)")
print("=" * 70)
print(f"  dim SU(3)/SO(3) = {DIM_SU3} - {DIM_SO3} = {dim_quot}  "
      f"(odd: {dim_quot % 2 == 1} -> Sasakian-dimension-compatible)")

q5 = float(atom.q_factorial(5))
print(f"\n  forced target: Ocneanu/Plancherel weights W_lambda = d_q(lambda)^2 / [5]_q!")
print(f"  [5]_q! = {q5:.6f}  at q0 = {float(c.q0):.6f}")
weights = {}
for lam in [(3, 1, 1), (3, 2), (2, 2, 1), (4, 1), (5,)]:
    dq = float(atom.q_dimension(lam))
    w = dq * dq / q5
    weights[lam] = w
    tag = "  <- electron block" if lam == (3, 1, 1) else ("  <- muon block" if lam == (3, 2) else "")
    print(f"    {str(lam):<12} d_q={dq:8.5f}  W={w:.6f}{tag}")

print()
print("=" * 70)
print("OPEN geometric sub-questions (the handoff to differential geometry)")
print("=" * 70)
print("  (Q1) Does SU(3)/SO(3) (the Wu manifold) admit a REGULAR Sasakian")
print("       structure whose Reeb lies in the spatial SO(3)_colour? (Boothby-Wang:")
print("       it must be an S^1-bundle over a Kahler-Einstein 4-base; necessary")
print("       condition chi=0 -- the Wu manifold has chi=0, so NOT obstructed here.)")
print("  (Q2) Does that Reeb's equivariant index / volume reproduce the W_lambda")
print("       above?  This is the geometric origin of the Markov weighting.")
print("  Neither is settled in-session: this is genuine differential geometry.")

assert dim_quot == 5 and dim_quot % 2 == 1, "SU(3)/SO(3) must be 5-dim odd"
assert abs(weights[(3, 1, 1)] - 0.294669) < 1e-5, "electron-block weight drift"
assert abs(weights[(3, 2)] - 0.207542) < 1e-5, "muon-block weight drift"
assert abs(weights[(2, 2, 1)] - 0.207542) < 1e-5, "conjugate muon-block weight drift"
print("\nWEIGHTING COMPATIBILITY + FORCED-TARGET ASSERTIONS VERIFIED.")
sys.exit(0)
