"""Jostling: how much uphill kick connects the products?  (issue #7895, round 6e.)

Owner idea (2026-11-15): "something that jostles to give a bit more energy".
Reading (agent's, stated): an activation energy.  A jostle lets the state climb
above a stable state and then settle elsewhere.

Model, as in chain_vs_ring_products_probe (reading 3 per bonded group and per
particle alone; convention D, proton pin).  Energy is lexicographic
(violation, crossings).  A violating state has infinite height here: no kick in
crossings buys a violation, so every path stays among FEASIBLE states.  Under
the per-particle rule only k in {3, 6} is feasible (V^k on three strands), so
the state space is k in {3,6}^3, bond powers m_b in 1..3.

Graph.  Nodes: the open chain (bonds 0,1) and the ring (bonds 0,1 + the
annular bond 2).  Edges: change one player's value; close the ring (add bond 2
at m = 1) or open it.  The HEIGHT of a node is its crossing count.  The
BARRIER between two states is the least, over paths, of the highest node on
the path, minus the starting height (a bottleneck path).  Two costs for the
annular bond, both stated:
    "local": 4m (the bond as drawn on the annulus),
    "routed": 4m + 48 (the full word delta^3 . bond^m . delta^-3 in B_9).
Reported: feasible states and costs; the barrier between the two mirror chain
products; the barrier from the chain products to the cheapest ring state, and
whether that ring state is cheaper than the chain.  Model energy units
(crossings); no temperature, no rates.  Mathematics only; mpmath only.
"""
from __future__ import annotations

import heapq
import sys
import time
from itertools import product
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chain_vs_ring_products_probe as R  # noqa: E402
import chain_reaction_cascade_probe as P  # noqa: E402
import mpmath as mp  # noqa: E402

KS = (3, 6)
MS = (1, 2, 3)


def nodes():
    out = []
    for k in product(KS, repeat=3):
        for m0, m1 in product(MS, repeat=2):
            out.append(("chain", k, (m0, m1, 1)))
            for m2 in MS:
                out.append(("ring", k, (m0, m1, m2)))
    return out


def job(node):
    stage, k, m = node
    bonds = [0, 1] if stage == "chain" else [0, 1, 2]
    _, (v, _c) = R.energy_job((k, bonds, m))
    return node, v == 0


def height(node, conv):
    stage, k, m = node
    c = 2 * sum(k) + 4 * (m[0] + m[1])
    if stage == "ring":
        c += 4 * m[2] + (48 if conv == "routed" else 0)
    return c


def neighbours(node):
    stage, k, m = node
    for i in range(3):
        for x in KS:
            if x != k[i]:
                kk = list(k)
                kk[i] = x
                yield (stage, tuple(kk), m)
    nb = 2 if stage == "chain" else 3
    for b in range(nb):
        for x in MS:
            if x != m[b]:
                mm = list(m)
                mm[b] = x
                yield (stage, k, tuple(mm))
    if stage == "chain":
        yield ("ring", k, (m[0], m[1], 1))
    elif m[2] == 1:
        yield ("chain", k, (m[0], m[1], 1))


def bottleneck(src, feas, conv):
    """least achievable max-height to every feasible node from src."""
    best = {src: height(src, conv)}
    pq = [(best[src], src)]
    while pq:
        hmax, u = heapq.heappop(pq)
        if hmax > best[u]:
            continue
        for v in neighbours(u):
            if not feas.get(v):
                continue
            nh = max(hmax, height(v, conv))
            if nh < best.get(v, 10 ** 9):
                best[v] = nh
                heapq.heappush(pq, (nh, v))
    return best


def main() -> int:
    t0 = time.time()
    R._init()
    ns = nodes()
    with Pool(4, initializer=R._init) as pool:
        feas = dict(pool.map(job, ns, chunksize=4))
    print(f"nodes {len(ns)}, feasible {sum(feas.values())}, wall {time.time() - t0:.0f} s", flush=True)
    res = {"feasible": {}, "conventions": {}}
    for stage in ("chain", "ring"):
        fs = sorted([n for n in ns if n[0] == stage and feas[n]], key=lambda n: height(n, "local"))
        res["feasible"][stage] = [{"k": list(n[1]), "m": list(n[2][:2] if stage == "chain" else n[2]),
                                   "cost_local": height(n, "local"), "cost_routed": height(n, "routed")}
                                  for n in fs]
        print(f"feasible {stage}: {len(fs)}", flush=True)
        for n in fs[:12]:
            print(f"   k {n[1]} m {n[2][:2] if stage == 'chain' else n[2]} "
                  f"cost {height(n, 'local')} / routed {height(n, 'routed')}", flush=True)
    A = ("chain", (3, 3, 3), (2, 1, 1))
    B = ("chain", (3, 3, 3), (1, 2, 1))
    for conv in ("local", "routed"):
        ba = bottleneck(A, feas, conv)
        base = height(A, conv)
        ring_feas = [n for n in ns if n[0] == "ring" and feas[n]]
        rmin = min(ring_feas, key=lambda n: height(n, conv)) if ring_feas else None
        out = {"mirror_barrier": (ba.get(B, None) - base) if B in ba else None,
               "ring_min": None if rmin is None else {"k": list(rmin[1]), "m": list(rmin[2]),
                                                     "cost": height(rmin, conv)},
               "ring_min_barrier": None if rmin is None or rmin not in ba else ba[rmin] - base}
        res["conventions"][conv] = out
        print(f"[{conv}] chain {A[2][:2]} -> mirror {B[2][:2]}: barrier {out['mirror_barrier']}; "
              f"cheapest ring {out['ring_min']}, barrier {out['ring_min_barrier']}", flush=True)
    print(f"wall {time.time() - t0:.0f} s", flush=True)

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("jostle-barrier-probe", engine="python", start_time=t0)
    wb.set_description("Bottleneck (activation) barriers in crossings between stable products of three "
                       "gamma-gamma particles, chain and ring, under reading 3 per bonded group and per "
                       "particle (convention D, proton pin). Violating states are impassable. Model units.")
    wb.add_parameter("q0", P.Q_50_DIGIT_STR)
    wb.add_parameter("dps", P.DPS)
    wb.add_parameter("k_values", list(KS))
    wb.add_parameter("m_values", list(MS))
    wb.add_parameter("ring_bond_cost", {"local": "4m", "routed": "4m+48"})
    wb.add_data("results", res)
    print(f"witness -> {wb.save()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
