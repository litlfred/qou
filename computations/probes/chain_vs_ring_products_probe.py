"""Chain versus ring: do the reaction products depend on the bond topology?
(issue #7895, PR #7896 follow-up, round 6d; owner chose this test 2026-11-15.)

Setup, as in chain_reaction_product_distribution_probe --alone, on 9 strands:
three particles V^{k_i} (k_i in 1..6) on windows {0,1,2}, {3,4,5}, {6,7,8};
bond b joins window b to window b+1 with the word (V_right.V_left)^{m_b},
m_b in 1..3.  Rule (owner, 2026-11-15): reading 3 on the bonded group AND on
each particle alone (convention D, proton pin).  Energy: lexicographic
(violation, crossings); crossings = 2*sum k + 4*sum m.  Stated choices.

The ring needs a third bond joining window 2 back to window 0.  Strands 8 and
0 are not adjacent in the braid group B_9, so that bond is not a word in the
standard generators.  CHOICE (stated, not derived): the ring bond is the
annular bond, obtained by rotating bond 1 by three strands,
    wrap^{m} := delta^3 . bond(1)^{m} . delta^{-3},   delta = sigma_0 ... sigma_7.
delta sigma_i delta^{-1} = sigma_{i+1} (checked numerically below), so this is
bond 1 moved to the windows (2, 0) of the annulus.  Its crossing cost is taken
to be 4m, the same as any other bond: the conjugating delta^{+-3} are the
rotation of the picture, not part of the bond.  Under this choice a cyclic
rotation of (k, m) would be a conjugation of the whole word IF the bond factors
were also rotated in place.  They are not: the word is (particles)(bond 0)(bond
1)(ring bond) in that fixed order, the bonds do not commute, and a rotation turns
it into (bond 1)(ring bond)(bond 0), a different element.  So energies need NOT
be rotation invariant; the probe counts how many ring states differ.  The bond
order in the word is a further stated choice.

Reported: (1) all stable states of the ring (and of each two-bond chain stage);
(2) pathways from (3,3,3; 1,1,1): bond orders {all three at once, or any two
first and then the third}, and all 6! sweep orders of the players; (3) the
product distribution, compared with the chain result (mirror pair
(3,3,3;2,1) / (3,3,3;1,2), cost 30).  Mathematics only; mpmath only.
"""
from __future__ import annotations

import sys
import time
from collections import Counter
from itertools import permutations, product
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import chain_reaction_cascade_probe as P  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt  # noqa: E402

A, N = 3, 9
# Under the per-particle rule only k in {3, 6} passes reading 3 alone (checked:
# alone violations for k = 1..6 are 1.04, 0.91, 0, 1.17, 0.77, 0).  The energy is
# lexicographic, so a descent from a feasible start never enters a violating
# state, and a best response never picks an infeasible k.  The search is
# therefore restricted to k in {3, 6} with no loss for the pathway results; the
# stable-state lists below are the FEASIBLE stable states.
KVALS = (3, 6)
NAMES = ["k0", "k1", "k2", "m0", "m1", "m2"]
_G = {}


def _init():
    mp.mp.dps = P.DPS
    q = mp.mpf(P.Q_50_DIGIT_STR)
    h = q - 1 / q
    _G["h"] = h
    _G["C9"] = P.Chars(N, q)
    _G["C3"] = P.Chars(3, q)
    one, zero = mp.mpf(1), mp.mpf(0)
    _G["delta"] = [(one, zero, g) for g in range(N - 1)]
    _G["deltai"] = [(one, -h, g) for g in reversed(range(N - 1))]


def bond_word(b, m):
    h = _G["h"]
    if b < 2:
        return P.bond(b, h) * m
    d3, d3i = _G["delta"] * 3, _G["deltai"] * 3
    return d3 + P.bond(1, h) * m + d3i


def viol(ch):
    v = mp.fsum(max(mp.mpf(0), -c) for c in ch)
    return mp.mpf(0) if v < P.TOL else v


def energy_job(args):
    k, bonds, m = args
    h = _G["h"]
    w = P.joint(list(k), [], h)
    for b in bonds:
        w += bond_word(b, m[b])
    v = viol(_G["C9"].chi(w, ("w",) + tuple(k) + tuple(bonds) + tuple(m)))
    for ki in k:
        v += viol(_G["C3"].chi(P.V(0, h) * ki, ("a", ki)))
    cost = 2 * sum(k) + 4 * sum(m[b] for b in bonds)
    return (k, tuple(bonds), m), (v, cost)


def check_rotation():
    """delta sigma_i delta^{-1} = sigma_{i+1}, i = 0..6, on every y>0 block."""
    h, C = _G["h"], _G["C9"]
    one, zero = mp.mpf(1), mp.mpf(0)
    X = [(one, zero, 0), (one, -h, 3), (one, zero, 5), (one, zero, 7)]
    worst = mp.mpf(0)
    for i in range(N - 2):
        a = C.chi(_G["delta"] + [(one, zero, i)] + _G["deltai"] + X, ("rotA", i))
        b = C.chi([(one, zero, i + 1)] + X, ("rotB", i))
        worst = max(worst, max(abs(x - y) for x, y in zip(a, b)))
    return worst


def main() -> int:
    t0 = time.time()
    _init()
    rot = check_rotation()
    print(f"rotation check max |chi diff| = {mp.nstr(rot, 3)}", flush=True)

    stages = {"ring": [0, 1, 2], "chain01": [0, 1], "chain12": [1, 2], "chain20": [2, 0]}
    jobs = []
    for bonds in stages.values():
        for k in product(KVALS, repeat=A):
            for mm in product(range(1, P.MMAX + 1), repeat=len(bonds)):
                m = [1, 1, 1]
                for b, x in zip(bonds, mm):
                    m[b] = x
                jobs.append((k, sorted(bonds), tuple(m)))
    with Pool(4, initializer=_init) as pool:
        E = {}
        for i, (key, e) in enumerate(pool.imap_unordered(energy_job, jobs, chunksize=8)):
            E[key] = e
            if i % 500 == 0:
                print(f"  {i}/{len(jobs)} energies, wall {time.time() - t0:.0f} s", flush=True)

    def en(st, bonds):
        k = tuple(st[:A])
        m = [1, 1, 1]
        for b in bonds:
            m[b] = st[A + b]
        return E[(k, tuple(sorted(bonds)), tuple(m))]

    def better(a, b):
        return P.better(a, b)

    def rng(i):
        return KVALS if i < A else range(1, P.MMAX + 1)

    def players(bonds):
        return list(range(A)) + [A + b for b in bonds]

    def best(st, i, bonds):
        cur, bc = en(st, bonds), st[i]
        for c in rng(i):
            t = list(st)
            t[i] = c
            e = en(t, bonds)
            if better(e, cur):
                cur, bc = e, c
        return bc

    # rotation invariance of the ring energies
    rot_bad = 0
    for k in product(KVALS, repeat=A):
        for m in product(range(1, P.MMAX + 1), repeat=3):
            st = list(k) + list(m)
            r = [k[2], k[0], k[1], m[2], m[0], m[1]]
            a, b = en(st, [0, 1, 2]), en(r, [0, 1, 2])
            if a[1] != b[1] or abs(a[0] - b[0]) > mp.mpf("1e-25"):
                rot_bad += 1
    print(f"ring states failing rotation invariance: {rot_bad}", flush=True)

    stable_by_stage = {}
    for name, bonds in stages.items():
        rows = []
        for st in product(*[rng(i) for i in range(A + 3)]):
            st = list(st)
            if any(st[A + b] != 1 for b in range(3) if b not in bonds):
                continue
            if all(best(st, i, bonds) == st[i] for i in players(bonds)):
                e = en(st, bonds)
                rows.append({"state": st, "viol": fmt(e[0]), "cost": e[1], "feasible": bool(e[0] == 0)})
        rows.sort(key=lambda r: (mp.mpf(r["viol"]), r["cost"]))
        stable_by_stage[name] = rows
        print(f"stable states, {name}: {len(rows)}", flush=True)
        for r in rows:
            print(f"   {r['state']}  viol {mp.nstr(mp.mpf(r['viol']), 5)}  cost {r['cost']}", flush=True)

    orders = {"all_three": [[0, 1, 2]], "01_then_2": [[0, 1], [0, 1, 2]],
              "12_then_0": [[1, 2], [0, 1, 2]], "20_then_1": [[0, 2], [0, 1, 2]]}
    paths = []
    for oname, st_list in orders.items():
        for perm in permutations(range(A + 3)):
            st = [3, 3, 3, 1, 1, 1]
            moves = 0
            for bonds in st_list:
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
            paths.append({"bond_order": oname, "sweep_order": [NAMES[i] for i in perm],
                          "end": list(st), "moves": moves})
    tot = Counter(tuple(p["end"]) for p in paths)
    byo = Counter((p["bond_order"], tuple(p["end"])) for p in paths)
    print(f"\nring pathways: {len(paths)}; distinct products: {len(tot)}", flush=True)
    for end, n in tot.most_common():
        e = en(list(end), [0, 1, 2])
        print(f"  product {list(end)}: {n} pathways, viol {mp.nstr(e[0], 5)}, cost {e[1]}", flush=True)
    for (o, end), n in sorted(byo.items()):
        print(f"    {o}: {list(end)} x {n}", flush=True)
    print(f"wall {time.time() - t0:.0f} s", flush=True)

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("chain-vs-ring-products-probe", engine="python", start_time=t0)
    wb.set_description("Stable states and pathway products of three gamma-gamma particles bonded as a "
                       "ring (annular third bond, a stated choice) versus as chains, under reading 3 per "
                       "bonded group and per particle (convention D, proton pin). Counts reachable "
                       "products; no rates.")
    wb.add_parameter("q0", P.Q_50_DIGIT_STR)
    wb.add_parameter("dps", P.DPS)
    wb.add_parameter("k_values", list(KVALS))
    wb.add_parameter("mmax", P.MMAX)
    wb.add_parameter("ring_bond", "delta^3 . bond(1)^m . delta^-3, delta = sigma_0..sigma_7; cost 4m")
    wb.add_data("rotation_check_max_abs", fmt(rot))
    wb.add_data("ring_rotation_invariance_failures", rot_bad)
    wb.add_data("stable_states", stable_by_stage)
    wb.add_data("pathways", paths)
    wb.add_data("product_counts", [{"end": list(e), "pathways": n} for e, n in tot.most_common()])
    wb.add_data("product_counts_by_bond_order",
                [{"bond_order": o, "end": list(e), "pathways": n} for (o, e), n in sorted(byo.items())])
    print(f"witness -> {wb.save()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
