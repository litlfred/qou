"""Several pathways, several products (issue #7895, PR #7896, round 6b).

Owner question (2026-11-15): does the bond cascade explain why a reaction can
have several pathways and several products?  Test: the same three particles,
the same bonds, different ORDERS (which bond forms first, and in which order
the players re-select), and count the distinct stable end states.

Model = chain_reaction_cascade_probe, under the owner's rule of 2026-11-15:
reading 3 per bonded group (convention D, proton pin).  Players: the three
particle powers k_i in 1..6 and the bond powers m_b in 1..3 (bond word
(V_right.V_left)^m, 4m crossings).  Energy: lexicographic (violation,
crossings) -- a stated choice.  A move: one player's best response (ties keep
the current value).  A state is STABLE when no single player can strictly
improve (Lean QOU.Optimization.ChainReaction.Stable); every cascade reaches one
(no_infinite_cascade).

Reported: (1) every stable state of the fully bonded chain (the possible
"products"), with its cost and whether it passes reading 3; (2) the end state of
every pathway: start from the separated optimum (3,3,3), bond orders
{0 then 1, 1 then 0, both at once}, and all 5! sweep orders of the players;
(3) the product distribution over pathways.  No rates: this counts reachable
products, not their likelihood.  Mathematics only; mpmath only.
"""
from __future__ import annotations

import sys
import time
from collections import Counter
from itertools import permutations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chain_reaction_cascade_probe as P  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt  # noqa: E402

A = 3
PLAYERS = ["k0", "k1", "k2", "m0", "m1"]
# --alone: the owner's ruling of 2026-11-15 (H2 electron card): every particle must
# ALSO pass reading 3 on its own three strands. The violation of each particle
# tested alone is added to the bonded-group violation.
ALONE = "--alone" in sys.argv


def main() -> int:
    t0 = time.time()
    mp.mp.dps = P.DPS
    q = mp.mpf(P.Q_50_DIGIT_STR)
    h = q - 1 / q
    Cs = {s: P.Chars(3 * s, q) for s in (1, 2, 3)}
    cache = {}

    def E(state, bonds):
        k = state[:A]
        m = [state[A + b] for b in bonds]
        key = (tuple(k), tuple(bonds), tuple(m))
        if key not in cache:
            e = P.energy(Cs, list(k), list(bonds), h, m if bonds else None)[0]
            if ALONE:
                v = e[0] + mp.fsum(P.energy(Cs[1], [ki], [], h)[0][0] for ki in k)
                e = (v, e[1])
            cache[key] = e
        return cache[key]

    def rng(i):
        return range(1, (P.KMAX if i < A else P.MMAX) + 1)

    def players(bonds):
        return list(range(A)) + [A + b for b in bonds]

    def best(state, i, bonds):
        cur = E(state, bonds)
        bc = state[i]
        for c in rng(i):
            t = list(state)
            t[i] = c
            e = E(t, bonds)
            if P.better(e, cur):
                cur, bc = e, c
        return bc

    def stable(state, bonds):
        return all(best(state, i, bonds) == state[i] for i in players(bonds))

    # (1) all stable states of the fully bonded chain
    full = [0, 1]
    stables = []
    for st in product(*[rng(i) for i in range(A + 2)]):
        st = list(st)
        if stable(st, full):
            e = E(st, full)
            stables.append({"state": st, "viol": fmt(e[0]), "cost": e[1], "feasible": bool(e[0] == 0)})
    gmin = min(stables, key=lambda r: (mp.mpf(r["viol"]), r["cost"]))
    print(f"stable states of the bonded chain: {len(stables)}  (wall {time.time() - t0:.0f} s)", flush=True)
    for r in sorted(stables, key=lambda r: (mp.mpf(r['viol']), r['cost'])):
        print(f"  {r['state']}  viol {mp.nstr(mp.mpf(r['viol']), 5)}  cost {r['cost']}", flush=True)

    # (2) pathways
    stages_by_order = {"bond0_then_bond1": [[0], [0, 1]], "bond1_then_bond0": [[1], [0, 1]],
                       "both_at_once": [[0, 1]]}
    paths = []
    for oname, stages in stages_by_order.items():
        for perm in permutations(range(A + 2)):
            st = [3, 3, 3, 1, 1]
            moves = 0
            for bonds in stages:
                order = [i for i in perm if i in players(bonds)]
                for _ in range(100):
                    moved = False
                    for i in order:
                        c = best(st, i, bonds)
                        if c != st[i]:
                            st[i] = c
                            moves += 1
                            moved = True
                    if not moved:
                        break
            paths.append({"bond_order": oname, "sweep_order": [PLAYERS[i] for i in perm],
                          "end": list(st), "moves": moves})
    dist = Counter((p["bond_order"], tuple(p["end"])) for p in paths)
    tot = Counter(tuple(p["end"]) for p in paths)
    print(f"\npathways: {len(paths)}; distinct products: {len(tot)}", flush=True)
    for end, n in tot.most_common():
        e = E(list(end), full)
        print(f"  product {list(end)}: {n} pathways, viol {mp.nstr(e[0], 5)}, cost {e[1]}", flush=True)
    for (o, end), n in sorted(dist.items()):
        print(f"    {o}: {list(end)} x {n}", flush=True)
    print(f"global optimum {gmin['state']} cost {gmin['cost']}; wall {time.time() - t0:.0f} s", flush=True)

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    name = "chain-reaction-product-distribution-alone-probe" if ALONE else "chain-reaction-product-distribution-probe"
    wb = WitnessBuilder(name, engine="python", start_time=t0)
    wb.set_description("Stable states and pathway end states of the bonded three-particle gamma-gamma "
                       "chain under reading 3 per bonded group (convention D, proton pin); lexicographic "
                       "(violation, crossings) energy is a stated choice. Counts reachable products, no rates.")
    wb.add_parameter("q0", P.Q_50_DIGIT_STR)
    wb.add_parameter("dps", P.DPS)
    wb.add_parameter("kmax", P.KMAX)
    wb.add_parameter("mmax", P.MMAX)
    wb.add_parameter("rule", "per bonded group + each particle alone" if ALONE else "per bonded group")
    wb.add_data("stable_states", stables)
    wb.add_data("global_optimum", gmin)
    wb.add_data("pathways", paths)
    wb.add_data("product_counts", [{"end": list(e), "pathways": n} for e, n in tot.most_common()])
    path = wb.save()
    print(f"witness -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
