#!/usr/bin/env python3
"""PROBE (term-completeness gap G5, epic qou-myts): how many inter-nucleon bonds each corpus
valence premise allows, and what binding that count gives with the ruled bond.

PRE-REGISTRATION HALF. This script never reads AME. It fixes, for each premise, the maximum
bond count M(A) and the binding B(A) = M(A) * b, with b the ruled T_z-even bond
b = -s * ln(z - h/2) (z = q^3/(q^2+1), h = q - 1/q, proton pin) at the two scales on record:
s = alpha = 8 m_e G (mass_table_comprehensive.binding_ruled_tz_even) and s = E0 tower
(qbeta_e0.tower_summed). The comparison with AME is compare_ame.py, committed after this.

Premises (each is a cap on the bond graph; energy minimisation with an attractive bond,
0 < z - h/2 < 1, then selects a graph with the most bonds the cap allows):
  chain   Artin linear layout (LinearLayoutNoBulk, GammaGammaForcesTheLayout): connected, a path.
  V3      colour valence: each nucleon's N_c = 3 quark strands carry at most one bond each,
          so max degree 3 (the K_5 valence obstruction of TetrahedralFluxRingAndMajoranaCluster).
  T3      Tait: as V3, and every bond carries one colour label, distinct at each nucleon
          (a proper 3-edge-colouring, the k4TaitEdgeColour object of the same file).
  V6      strand-end valence: each of a nucleon's 2 N_c strand ends carries at most one bond.
          No corpus object. Listed because it is the cap that matches AME's ~3 bonds per nucleon.
  planar  triangulated 2-sphere, 3A - 6 (deltahedron, gap1_max_contact_a5plus). Imported geometry.
  KA      complete graph, C(A,2). No cap; excluded at A >= 5 by Pauli closure / MaxContactSimplex.

Checks (exact integer arithmetic; the bond value in mpmath at 50 dps, never float):
  1. attainment: an explicit connected graph meeting each bound, A = 2..60, verified edge by
     edge (degree, simplicity, connectivity, and for T3 the colouring);
  2. exhaustive maximum over all simple graphs for A <= 6 equals the formula for V3 and T3;
  3. V3 and T3 differ exactly at odd A >= 5;
  4. the ruled bond is attractive at q0;
  5. ruled bond value reproduces 0.676963077 (dimensionless) and 2.5348609 / 2.8618501 MeV.
The upper bounds themselves are proved in Lean (QOU/MassTheory/NucleusBondValence.lean).
"""
from __future__ import annotations

import itertools
import json
import sys
from math import comb
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for p in ("computations", "computations/qbeta", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / p))

mp.mp.dps = 50
A_MAX = 60
PREMISES = ("chain", "T3", "V3", "V6", "planar", "KA")


def bound(premise: str, A: int) -> int:
    if A < 2:
        return 0
    c = comb(A, 2)
    if premise == "chain":
        return A - 1
    if premise == "V3":
        return min(c, (3 * A) // 2)
    if premise == "T3":
        return min(c, 3 * (A // 2)) if A >= 3 else 1
    if premise == "V6":
        return min(c, 3 * A)
    if premise == "planar":
        return 1 if A == 2 else 3 * A - 6
    if premise == "KA":
        return c
    raise ValueError(premise)


def norm(u, v):
    return (u, v) if u < v else (v, u)


def complete(A):
    return [norm(u, v) for u, v in itertools.combinations(range(A), 2)]


def circulant(A, steps):
    return sorted({norm(i, (i + s) % A) for i in range(A) for s in steps if (i + s) % A != i})


def cubic_class1(A):
    """Connected cubic graph on even A >= 4: K_4, the prism C_{A/2} x K_2 when A/2 is even,
    the Moebius ladder C_A(1, A/2) otherwise. Its colouring is checked, not assumed."""
    if A == 4:
        return complete(4)
    m = A // 2
    if m % 2 == 0:
        E = [norm(i, (i + 1) % m) for i in range(m)] + [norm(m + i, m + (i + 1) % m) for i in range(m)] \
            + [norm(i, m + i) for i in range(m)]
        return sorted(set(E))
    return circulant(A, (1, m))


def colour3(E, A):
    """Backtracking proper 3-edge-colouring; returns dict edge->colour or None."""
    order = sorted(E)
    col = {}
    used = {v: set() for v in range(A)}

    def go(k):
        if k == len(order):
            return True
        u, v = order[k]
        for c in range(3):
            if c not in used[u] and c not in used[v]:
                col[(u, v)] = c
                used[u].add(c)
                used[v].add(c)
                if go(k + 1):
                    return True
                used[u].discard(c)
                used[v].discard(c)
                del col[(u, v)]
        return False

    return dict(col) if go(0) else None


def construct(premise: str, A: int):
    if premise == "chain":
        return [(i, i + 1) for i in range(A - 1)]
    if premise == "KA" or (premise in ("V3", "T3") and A <= 4) or (premise == "V6" and A <= 7):
        return complete(A)
    if premise in ("V3", "T3"):
        if A % 2 == 0:
            return cubic_class1(A)
        E = cubic_class1(A - 1)
        w = A - 1
        if premise == "V3":
            # subdivide one edge uv by the new vertex w: count 3(A-1)/2 + 1 = floor(3A/2)
            u, v = E[0]
            return sorted((set(E) - {(u, v)}) | {norm(u, w), norm(v, w)})
        # T3: drop one colour-0 edge uv and hang w on u with colour 0: count 3(A-1)/2, still proper
        col = colour3(E, A - 1)
        u, v = next(e for e in E if col[e] == 0)
        return sorted((set(E) - {(u, v)}) | {norm(u, w)})
    if premise == "V6":
        return circulant(A, (1, 2, 3))
    raise ValueError(premise)


def connected(E, A):
    adj = {v: set() for v in range(A)}
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)
    seen, stack = {0}, [0]
    while stack:
        x = stack.pop()
        for y in adj[x] - seen:
            seen.add(y)
            stack.append(y)
    return len(seen) == A


def maxdeg(E, A):
    d = [0] * A
    for u, v in E:
        d[u] += 1
        d[v] += 1
    return max(d)


def exhaustive(A):
    """Largest simple graph on A vertices with max degree <= 3, and with a proper 3-edge-colouring."""
    pairs = list(itertools.combinations(range(A), 2))
    best_v3 = best_t3 = None
    for r in range(len(pairs), -1, -1):
        for S in itertools.combinations(pairs, r):
            if maxdeg(S, A) > 3:
                continue
            if best_v3 is None:
                best_v3 = r
            if best_t3 is None and colour3(list(S), A) is not None:
                best_t3 = r
            if best_v3 is not None and best_t3 is not None:
                return best_v3, best_t3
    return best_v3, best_t3


def main():
    checks = []
    caps = {"chain": 2, "V3": 3, "T3": 3, "V6": 6, "KA": None}
    fails = []
    for prem, cap in caps.items():
        for A in range(2, A_MAX + 1):
            E = construct(prem, A)
            ok = (len(E) == len(set(E)) == bound(prem, A)) and all(u != v for u, v in E) \
                and connected(E, A) and (cap is None or maxdeg(E, A) <= cap)
            if prem == "T3":
                ok = ok and colour3(E, A) is not None
            if not ok:
                fails.append((prem, A, len(E), bound(prem, A)))
    for f in fails:
        print("construction FAIL", *f)
    checks.append((f"attainment: connected constructions meet every bound, A=2..{A_MAX}", not fails))

    exh = {A: exhaustive(A) for A in range(2, 7)}
    checks.append(("exhaustive max over all simple graphs A<=6 equals V3 and T3 formulas",
                   all(exh[A] == (bound("V3", A), bound("T3", A)) for A in exh)))
    checks.append(("V3 and T3 differ exactly at odd A>=5 (overfull graphs)",
                   all((bound("V3", A) != bound("T3", A)) == (A % 2 == 1 and A >= 5)
                       for A in range(2, A_MAX + 1))))

    import qou_substrate.constants as C
    import qbeta_e0 as E0m
    q = mp.mpf(C.Q_50_DIGIT_STR)
    me = mp.mpf(str(C.M_E_MEV))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    f = z - h / 2
    alpha = me * 8 * mp.catalan
    E0 = E0m.tower_summed()
    L = -mp.log(f)
    b = {"alpha": alpha * L, "E0": E0 * L}
    checks.append(("0 < z - h/2 < 1 at q0 (the ruled bond is attractive)", 0 < f < 1))
    checks.append(("bond value reproduces 0.676963077, 2.5348609, 2.8618501",
                   abs(L - mp.mpf("0.676963077037981")) < mp.mpf("1e-14")
                   and abs(b["alpha"] - mp.mpf("2.53486093323866")) < mp.mpf("1e-13")
                   and abs(b["E0"] - mp.mpf("2.86185014055348")) < mp.mpf("1e-13")))

    table = {}
    for A in list(range(2, 13)) + [16, 20, 24, 40, 56, 60]:
        row = {}
        for prem in PREMISES:
            M = bound(prem, A)
            row[prem] = {"bonds": M, "bonds_per_nucleon": mp.nstr(mp.mpf(M) / A, 20),
                         "B_alpha_MeV": mp.nstr(M * b["alpha"], 20), "B_E0_MeV": mp.nstr(M * b["E0"], 20)}
        table[str(A)] = row

    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    all_ok = all(ok for _, ok in checks)
    print(f"{sum(ok for _, ok in checks)}/{len(checks)}")
    print("A", *PREMISES)
    for A in (2, 3, 4, 5, 6, 7, 8, 12, 16, 56):
        print(A, *[bound(p, A) for p in PREMISES])

    out = {
        "producer": "computations/probes/nucleus_bond_valence/nucleus_bond_valence_probe.py",
        "q0Anchor": "proton", "q0Value": mp.nstr(q, 50),
        "reads_AME": False,
        "bond": {"z_minus_h_over_2": mp.nstr(f, 40), "minus_ln": mp.nstr(L, 40),
                 "alpha_MeV": mp.nstr(alpha, 40), "E0_tower_MeV": mp.nstr(E0, 40),
                 "b_alpha_MeV": mp.nstr(b["alpha"], 40), "b_E0_MeV": mp.nstr(b["E0"], 40)},
        "formulas": {"chain": "A-1", "T3": "min(C(A,2), 3*floor(A/2)) for A>=3; 1 at A=2",
                     "V3": "min(C(A,2), floor(3A/2))", "V6": "min(C(A,2), 3A)",
                     "planar": "3A-6 for A>=3", "KA": "C(A,2)"},
        "exhaustive_A_le_6": {str(A): {"V3": v, "T3": t} for A, (v, t) in exh.items()},
        "table": table,
        "checks": [{"name": n, "pass": bool(o)} for n, o in checks],
        "allPassed": all_ok,
    }
    (HERE / "nucleus-bond-valence.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
