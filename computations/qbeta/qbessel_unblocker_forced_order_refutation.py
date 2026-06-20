#!/usr/bin/env python3
"""qbessel_unblocker_forced_order_refutation.py
================================================

The qbk2 wiring gate (PR #2536) verdict DO NOT WIRE rested on the (nu_lambda, w_lambda)
order+argument map being a FREE functional knob (63% swing). The owner asked to attempt
the UNBLOCKER: is there a substrate principle that FORCES the map, making the binding
correction parameter-free after all?

This script tests the strongest candidate forcing principle and REFUTES it structurally.

The forcing candidate (representation theory, not invented)
----------------------------------------------------------
In the SU_q(2) -> E_q(2) harmonic analysis (Vaksman-Korogodsky 1989; Koelink 1994,
cited in 2026-06-13-reeb-phase-qbessel-identification.md), the Hahn-Exton q-Bessel
J_nu(x;q) is the E_q(2) matrix coefficient with:
  * nu = the ANGULAR-MOMENTUM label  (INTEGER), and
  * x  = the RADIAL coordinate        (continuous).
So the only representation-theoretically forced order nu_lambda on a Wedderburn block
is an INTEGER (the rep's angular label / Chebyshev order dim-1 / tower level 2m+1).

The two-part refutation this script makes concrete
--------------------------------------------------
  (R1) FORCED ORDER IS RESONANT. Every integer-order candidate (dim_lambda - 1, and
       the tower levels) is an INTEGER, and at integer nu the power-series 2nd-kind
       solution g2 (PRs #2530/#2533) is SINGULAR: the recurrence denominator
       (q^k - q^nu) vanishes at k = nu (the Neumann log-resonance). So the forced
       order does NOT even admit the #2533 power-series propagator.  [computed here]

  (R2) THE LOG-NEUMANN SOLUTION REINTRODUCES THE UNFORCED RADIAL SCALE. At integer
       order the genuine 2nd solution is the logarithmic Neumann Y_n(x) ~ J_n(x)*log(x)
       + regular. Its value needs the RADIAL argument x. But the framework's per-block
       Markov trace fixes only the ANGULAR Reeb phase theta_lambda = arccos/arccosh
       (chi_lambda/dim_lambda) -- the character PHASE. theta is angular; x is radial;
       in E_q(2) these are INDEPENDENT coordinates. The trace supplies no canonical
       angular->radial map, so the log scale is exactly the free knob that gave the
       63% swing.  [structural; argued in the companion .md]

Conclusion: the unblocker FAILS for a structural reason (forced order = log-resonant,
whose argument is the unforced radial coordinate), not a failed search. qbk2's binding
direction is closed: a parameter-free correction would need a NEW substrate datum (a
canonical radial coordinate per block) that the Markov trace does not provide.

No fit; nothing wired; derive-or-refute.
"""
from __future__ import annotations

import json
import math
import pathlib

from mpmath import mp, mpf, qp, fabs, acos, acosh

mp.dps = 40
Q0 = mpf("1.10997858")
HERE = pathlib.Path(__file__).resolve().parent
DEU = HERE.parent / "atom-chi-rust-d.witness.json"


def dim_sn(lam):
    n = sum(lam)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return math.factorial(n) // den


def g2_powerseries_singular_at(nu, q, K=30):
    """Return True if the power-series 2nd-kind recurrence hits a zero denominator
    (q^k - q^nu) for some k < K -- i.e. nu is an integer Neumann resonance."""
    for k in range(1, K):
        if fabs(q ** k - q ** nu) < mpf("1e-30"):
            return True, k
    return False, None


def main():
    d = json.loads(DEU.read_text())
    free = {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d["data"]["free"]["by_partition"]}

    print("Unblocker refutation — the forced q-Bessel order is the Neumann log-resonance")
    print("=" * 78)
    print(f"deuteron n=6, {len(free)} blocks; q_0={float(Q0)}\n")

    # (R1) the representation-theoretic forced order nu = dim-1 is integer -> resonance
    print("(R1) forced order candidate nu_lambda = dim_lambda - 1  (angular/Chebyshev label)")
    print(f"{'lambda':<16}{'dim':>6}{'nu=dim-1':>10}{'integer?':>10}{'g2 power-series':>18}")
    all_integer = True
    all_resonant = True
    for lam in sorted(free, key=lambda L: dim_sn(list(L)), reverse=True):
        d_ = dim_sn(list(lam))
        nu = d_ - 1
        is_int = float(nu).is_integer()
        sing, k = g2_powerseries_singular_at(mpf(nu), Q0)
        all_integer = all_integer and is_int
        all_resonant = all_resonant and (sing or nu == 0)
        tag = f"SINGULAR (k={k})" if sing else ("trivial nu=0" if nu == 0 else "regular")
        print(f"{str(list(lam)):<16}{d_:>6}{nu:>10}{('yes' if is_int else 'NO'):>10}{tag:>18}")

    print(f"\n  every forced order integer:            {'YES' if all_integer else 'no'}")
    print(f"  every forced order Neumann-resonant:   {'YES' if all_resonant else 'no'}")

    # also the tower-level candidates 2m+1 are integers by construction
    print("\n  (the Jacobi-Anger tower-level orders 2m+1 are integers by construction too;")
    print("   no representation-theoretic order is a non-integer -- the #2533 power-series")
    print("   propagator only exists at the UNPHYSICAL half-integer orders used in #2536.)")

    print("\n--- VERDICT (R1 computed; R2 structural — see companion .md) ---")
    print("  (R1) The forced order nu_lambda = dim_lambda - 1 is INTEGER for every block,")
    print("       and integer order is the Neumann LOG-RESONANCE where the power-series")
    print("       2nd-kind g2 is SINGULAR. So the substrate-forced order does not admit")
    print("       the #2533 power-series propagator at all.")
    print("  (R2) At integer order the true 2nd solution is the logarithmic Neumann")
    print("       Y_n(x) ~ J_n(x) log(x) + regular, whose value needs the RADIAL x. The")
    print("       Markov trace fixes only the ANGULAR Reeb phase theta_lambda; angular and")
    print("       radial are independent E_q(2) coordinates, so x (the log scale) is the")
    print("       SAME free knob that gave the 63% swing in #2536.")
    print("  => UNBLOCKER REFUTED structurally. A parameter-free binding correction would")
    print("     need a NEW substrate datum (a canonical per-block radial coordinate) that")
    print("     the Markov trace does not provide. qbk2 binding direction CLOSED. No fit.")

    print("\nREFUTATION COMPLETE.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
