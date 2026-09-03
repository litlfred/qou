#!/usr/bin/env python3
"""The ℏ_q⁰ floor of `tr_M(W_free) − tr_M(W_atom)` in closed form (bean qou-zrx2).

WHAT WAS OPEN. `hbar_q_order_of_binding_observables_probe` established that the
signed trace difference does NOT vanish at q = 1 — it leaves a classical
remainder, measured as 1/8 for the deuteron and 7/128 for ⁴He. Those are dyadic
rationals, which is not what a numerical artefact looks like, but no closed form
was identified and the bean records the floor only as a *difference*.

THE ANSWER, and it is that each LEG is separately exact:

    tr_M(W_free)(q→1) = z^A          z = z_D(1) = q³/(q²+1) at q=1 = 1/2
    tr_M(W_atom)(q→1) = z^(2A−1)
    floor             = 2^−A − 2^−(2A−1)

WHY DYADIC AT ALL. Under the production convention D the Markov parameter is
z = q³/(q²+1), so **z(1) = 1/2 exactly**. The floor is built from powers of
one half because the classical Markov parameter IS one half; nothing else is
needed to explain the 2-adic character.

WHAT THE EXPONENTS SAY. 2A−1 = A + (A−1). The free word contributes one factor
per nucleon (A of them — its underlying permutation is the IDENTITY, so it
closes to the A-component unlink). The atom word contributes those A plus
**A−1 more**. A−1 is the bond count of a minimal connected graph on A nodes.
That reading is an INTERPRETATION, not a measurement — what is measured is the
exponent arithmetic. It is recorded because A−1 is the interesting number: the
corpus has already PROVED (QOU.Mass.CoordinationSaturation, sorry-free) that
complete-graph coordination M = C(A,2) is excluded and bounded degree forced.

EVIDENCE. A = 2 and A = 4 fix the two parameters; **A = 3 is out-of-sample** and
was not used to fit. All three agree to ~1e-9, the Richardson floor:

    A=2  free 1/4    atom 1/8     floor 1/8      (fitted)
    A=4  free 1/16   atom 1/128   floor 7/128    (fitted)
    A=3  free 1/8    atom 1/32    floor 3/32     PREDICTED, then measured

A REFUTED ROUTE, recorded so it is not re-attempted. The obvious mechanism is
the cycle-count trace z^(n−c) with c the cycle count of the underlying
permutation and n = 3A strands. It FAILS: measured c_free = n and c_atom = n−1,
which gives 1/2 for every atom. The exponents that work are in A, the nucleon
count — not in n, the strand count.

Scope: this identifies the classical floor. It does NOT resolve the ℏ_q index
or the E₀ convention collision that qou-zrx2 also records; it removes the
excuse that the floor was unexplained.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tr_m_atom_via_transfer as TR  # noqa: E402

DPS = 60
ETAS = ("1e-4", "1e-5", "1e-6")
ATOMS = ((1, 1, "deuteron", 2), (1, 2, "triton", 3), (2, 2, "helium-4", 4))


def _richardson(vals, etas):
    """f(η) = f₀ + c·η + O(η²) — two-point elimination of the linear term."""
    return (vals[-1] * etas[-2] - vals[-2] * etas[-1]) / (etas[-2] - etas[-1])


def classical_limits(Z: int, N: int):
    """(free, atom) traces extrapolated to q → 1 along q = exp(η)."""
    etas, fr, at = [], [], []
    for e in ETAS:
        eta = mp.mpf(e)
        ta, tf, _chi, _w = TR.tr_m_atom_zn(Z, N, dps=DPS, q=mp.exp(eta))
        etas.append(eta); at.append(ta); fr.append(tf)
    return _richardson(fr, etas), _richardson(at, etas)


def main() -> int:
    mp.dps = DPS
    half = mp.mpf(1) / 2
    print("=" * 78)
    print(" classical (ℏ_q⁰) floor of tr_M(W_free) − tr_M(W_atom), in closed form")
    print(f" z_D(q=1) = q³/(q²+1) at q=1 = {mp.nstr(half, 4)}  ← why the floor is dyadic")
    print("=" * 78)
    worst = mp.mpf(0)
    for Z, N, label, A in ATOMS:
        free, atom = classical_limits(Z, N)
        p_free, p_atom = half ** A, half ** (2 * A - 1)
        r_free = abs(free - p_free) / p_free
        r_atom = abs(atom - p_atom) / p_atom
        worst = max(worst, r_free, r_atom)
        tag = "  [OUT-OF-SAMPLE]" if A == 3 else ""
        print(f"\n  {label} (A={A}){tag}")
        print(f"    tr_M(W_free) → {mp.nstr(free, 14):>20}   z^A       = {mp.nstr(p_free, 14):>20}  rel {mp.nstr(r_free, 3)}")
        print(f"    tr_M(W_atom) → {mp.nstr(atom, 14):>20}   z^(2A−1)  = {mp.nstr(p_atom, 14):>20}  rel {mp.nstr(r_atom, 3)}")
        print(f"    floor        → {mp.nstr(free - atom, 14):>20}   2^−A − 2^−(2A−1)")

    ok = worst < mp.mpf(10) ** -7
    print("\n" + "=" * 78)
    print(f"  worst relative deviation over 6 legs: {mp.nstr(worst, 3)}")
    print(f"  VERDICT: {'closed form holds on all three atoms' if ok else 'DISAGREES — investigate'}")
    print("  Bound is the Richardson floor at η=1e-6, not the arithmetic (60 dps).")
    print("=" * 78)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
