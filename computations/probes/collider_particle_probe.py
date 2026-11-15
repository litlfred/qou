"""A collider as an explicit particle: which products can it reach?  (issue #7962, round 6f.)

Follows jostle_barrier_probe (reading 3 per bonded group and per particle alone;
convention D, proton pin).  There the energy for a jump was a budget of crossings.
Here it is carried by a fourth particle, the collider, and crossings are conserved.

Derived, not chosen: under the per-particle rule a 3-strand particle V^k is feasible
alone only for k in {3, 6} (jostle_barrier_probe; violations for k = 1..6 are
1.04, 0.91, 0, 1.17, 0.77, 0).  So a feasible collider can change only between V^6
and V^3, and it exchanges energy only in steps of 3V = 6 crossings.

Stated choices: the collider is never bonded to the system (it only exchanges V
letters); total crossings, system + collider, are conserved; the collider starts at
V^6 and the system at the chain product (3,3,3; 2,1), cost 30.  Bond costs as in
the "local" convention (4m).  The system then moves among feasible states with
height <= 30 + 6 = 36 while the collider sits at V^3, and may hand the 3V back only
from a state of height exactly 36 to one of height exactly 30 (collider back at
V^6) -- that is the exact-quantum rule, read off from the conservation.

Reported: the feasible system states reachable at height <= 36; which of them have
height exactly 36 (the system holds the 3V) or exactly 30 (the 3V can return); and
whether the mirror chain product and the ring are reachable.  Model units; no
temperature, no rates.  Mathematics only; mpmath only.
"""
from __future__ import annotations

import sys
import time
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chain_vs_ring_products_probe as R  # noqa: E402
import chain_reaction_cascade_probe as P  # noqa: E402
import jostle_barrier_probe as J  # noqa: E402
import mpmath as mp  # noqa: E402

QUANTUM = 6  # crossings released by V^6 -> V^3, the only feasible collider move


def main() -> int:
    t0 = time.time()
    R._init()
    ns = J.nodes()
    with Pool(4, initializer=R._init) as pool:
        feas = dict(pool.map(J.job, ns, chunksize=4))
    print(f"nodes {len(ns)}, feasible {sum(feas.values())}, wall {time.time() - t0:.0f} s", flush=True)

    # collider alone: feasible k values among 1..6 (re-derived, not quoted)
    h = R._G["h"]
    coll = {}
    for k in range(1, 7):
        v = R.viol(R._G["C3"].chi(P.V(0, h) * k, ("collider", k)))
        coll[k] = v == 0
    print(f"collider alone feasible: {[k for k, ok in coll.items() if ok]}", flush=True)
    assert [k for k, ok in coll.items() if ok] == [3, 6]

    start = ("chain", (3, 3, 3), (2, 1, 1))
    mirror = ("chain", (3, 3, 3), (1, 2, 1))
    base = J.height(start, "local")
    cap = base + QUANTUM
    best = J.bottleneck(start, feas, "local")
    reach = sorted([n for n, hm in best.items() if hm <= cap], key=lambda n: (J.height(n, "local"), n))

    def show(n):
        return {"stage": n[0], "k": list(n[1]), "m": list(n[2][:2] if n[0] == "chain" else n[2]),
                "cost": J.height(n, "local")}

    at_cap = [n for n in reach if J.height(n, "local") == cap]
    at_base = [n for n in reach if J.height(n, "local") == base]
    rings = [n for n in reach if n[0] == "ring"]
    print(f"reachable with collider at V^3 (height <= {cap}): {len(reach)}", flush=True)
    for n in reach:
        print(f"   {show(n)}", flush=True)
    print(f"holding the 3V (height == {cap}): {len(at_cap)}; can return it (height == {base}): "
          f"{[show(n) for n in at_base]}", flush=True)
    print(f"mirror reachable: {mirror in reach}; ring states reachable: {len(rings)}", flush=True)
    print(f"wall {time.time() - t0:.0f} s", flush=True)

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("collider-particle-probe", engine="python", start_time=t0)
    wb.set_description("Reachable products of three gamma-gamma particles when the collision energy is "
                       "carried by a fourth, unbonded collider particle with conserved crossings. Under "
                       "reading 3 per particle the collider moves only between V^6 and V^3, so it exchanges "
                       "energy in steps of 3V = 6 crossings. Model units; no rates.")
    wb.add_parameter("q0", P.Q_50_DIGIT_STR)
    wb.add_parameter("dps", P.DPS)
    wb.add_parameter("quantum_crossings", QUANTUM)
    wb.add_parameter("start", show(start))
    wb.add_parameter("bond_cost", "local 4m")
    wb.add_data("collider_alone_feasible_k", [k for k, ok in coll.items() if ok])
    wb.add_data("reachable", [show(n) for n in reach])
    wb.add_data("holding_quantum", [show(n) for n in at_cap])
    wb.add_data("can_return_quantum", [show(n) for n in at_base])
    wb.add_data("mirror_reachable", mirror in reach)
    wb.add_data("ring_reachable", [show(n) for n in rings])
    print(f"witness -> {wb.save()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
