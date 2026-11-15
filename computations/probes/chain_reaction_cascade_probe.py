"""Chain reaction after a bond (issue #7895, PR #7896, round 6).

Question (owner, 2026-11-15).  A two-letter bond that reaches two particles
correlates them only weakly, but it changes the selection problem of the joined
word.  Does re-selection then run as a cascade through the joined words and
settle in a stable state?

Model (stated choices, not derived).
  * Particle i is the gamma-gamma power V^{k_i} on its own strand window,
    V = sigma_{3i} sigma_{3i+1}^{-1}, k_i in 1..KMAX.  Alone in H_3 the
    reading-3 ILP picks k = 3 (collision_gradient_lagrangian_probe).
  * The bond between windows i and i+1 is the fixed word
    V_right.V_left = sigma_{3i+2} sigma_{3i+3}^{-1} sigma_{3i+1} sigma_{3i+2}^{-1}
    (the only bond type that correlates the two windows, round 5).
  * The joint word is W(k) = (prod_i V_i^{k_i}) (prod bonds).  The constraint is
    reading 3 on the JOINT word: chi_lambda(W) >= 0 on every lambda |- 3A with
    y_lambda > 0, convention D (N = 2), proton pin.
  * The energy is lexicographic: first the total negative character mass
    viol(k) = sum_lambda max(0, -chi_lambda(W)), then the crossing cost
    sum_i 2 k_i.  This ordering is a choice.  On a finite state space any strict
    order is a natural-number potential, so every cascade of strictly improving
    moves stops (Lean QOU.Optimization.ChainReaction.no_infinite_cascade).
  * A move is a particle's best response: re-choose its own k_i, others fixed.

Reported: (1) the unbonded joint selection (does reading 3 on a product of
disjoint words select each factor independently?); (2) for A = 2 and A = 3, the
cascade started from the isolated optimum k = (3,...,3) after the bonds are
added, sequential and synchronous; (3) the brute-force optimum over all k; (4)
a perturbation run: A = 3 settled with one bond, then the second bond added,
recording which particles move in which synchronous round (the light cone, Lean
light_cone); (5) A = 3 with the bond powers as players too: bond word
(V_right.V_left)^m, m in 1..3, cost 4m crossings; (6) the same under the
owner's rule of 2026-11-15: reading 3 per bonded group (each bonded group
tested on its own word, unbonded particles alone).  Fully bonded chains are a
single group, so (2)-(5) for them are the same under both rules.  Mathematics only; no physical value.  mpmath only.
"""
from __future__ import annotations

import sys
import time
from itertools import product
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
           "computations/hecke", "computations", "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp, chi_lambda_of_word_sparse_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n, partitions_of  # noqa: E402

DPS = 40
set_compute_dps(DPS)
TOL = mp.mpf("1e-30")
KMAX = 6


def V(g, h):
    return [(mp.mpf(1), mp.mpf(0), g), (mp.mpf(1), -h, g + 1)]


def bond(i, h):
    return V(3 * i + 2, h) + V(3 * i + 1, h)


class Chars:
    """Characters chi_lambda on the blocks with y_lambda > 0 (convention D)."""

    def __init__(self, n, q):
        self.n = n
        cache = BlockCacheMP(q, q - 1 / q)
        y = {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(n, q, 2).items()}
        self.blocks = []
        for lam in partitions_of(n):
            lam = tuple(lam)
            if y[lam] > TOL:
                sig, dim, _ = seminormal_matrices_mp(lam, cache=cache)
                self.blocks.append((lam, sig, dim))
        self.memo = {}

    def chi(self, word, key):
        if key not in self.memo:
            self.memo[key] = [chi_lambda_of_word_sparse_mp(sig, dim, word, self.n - 1)
                              for _, sig, dim in self.blocks]
        return self.memo[key]


def joint(k, bonds, h):
    w = []
    for i, ki in enumerate(k):
        w += V(3 * i, h) * ki
    for b in bonds:
        w += bond(b, h)
    return w


def components(A, bonds):
    """Bonded groups: maximal runs of windows joined by bonds b (b joins b, b+1)."""
    comps, cur = [], [0]
    for i in range(1, A):
        if (i - 1) in bonds:
            cur.append(i)
        else:
            comps.append(cur)
            cur = [i]
    comps.append(cur)
    return comps


def energy(C, k, bonds, h, m=None):
    """m: optional bond powers (one per bond); the bond word is then (V_right.V_left)^m.

    C is either one Chars on H_{3A} (rule "whole joined word") or a dict
    {size: Chars on H_{3 size}} (rule "per bonded group", owner 2026-11-15):
    each bonded group is tested on its own word, unbonded particles alone."""
    if isinstance(C, dict):
        viol, chs = mp.mpf(0), []
        for comp in components(len(k), bonds):
            a = comp[0]
            sub_b = [b - a for b in bonds if b in comp and b + 1 in comp]
            sub_m = None if m is None else [m[j] for j, b in enumerate(bonds) if b in comp and b + 1 in comp]
            e, ch = energy(C[len(comp)], k[a:a + len(comp)], sub_b, h, sub_m)
            viol += e[0]
            chs += ch
        return (viol, 2 * sum(k) + (0 if m is None else 4 * sum(m))), chs
    w = joint(k, [], h)
    for j, b in enumerate(bonds):
        w += bond(b, h) * (1 if m is None else m[j])
    ch = C.chi(w, (tuple(k), tuple(bonds), None if m is None else tuple(m)))
    viol = mp.fsum(max(mp.mpf(0), -c) for c in ch)
    if viol < TOL:
        viol = mp.mpf(0)
    return (viol, 2 * sum(k) + (0 if m is None else 4 * sum(m))), ch


MMAX = 3


def joint_bond_cascade(C, A, h, log):
    """Bond powers are players too: state (k_0..k_{A-1}, m_0..m_{A-2}), bond word
    (V_right.V_left)^m costs 4m crossings.  Sequential best response from
    k = 3, m = 1, and the brute-force optimum."""
    bonds = list(range(A - 1))

    def E(s):
        return energy(C, s[:A], bonds, h, s[A:])[0]

    s = [3] * A + [1] * (A - 1)
    path = [list(s)]
    for _ in range(50):
        moved = False
        for i in range(len(s)):
            rng = range(1, (KMAX if i < A else MMAX) + 1)
            best, bc = E(s), s[i]
            for c in rng:
                t = list(s)
                t[i] = c
                e = E(t)
                if better(e, best):
                    best, bc = e, c
            if bc != s[i]:
                s[i] = bc
                moved = True
                path.append(list(s))
        if not moved:
            break
    es = E(s)
    best, arg, nfeas = None, None, 0
    for st in product(*([range(1, KMAX + 1)] * A + [range(1, MMAX + 1)] * (A - 1))):
        e = E(list(st))
        nfeas += e[0] == 0
        if best is None or better(e, best):
            best, arg = e, list(st)
    log(f"    bond powers as players: path {path} -> stable {s} (viol {mp.nstr(es[0], 5)}, cost {es[1]}); "
        f"global optimum {arg} (viol {mp.nstr(best[0], 5)}, cost {best[1]}); {nfeas} feasible states")
    return {"path": path, "stable": s, "stable_viol": fmt(es[0]), "stable_cost": es[1],
            "optimum": arg, "optimum_viol": fmt(best[0]), "optimum_cost": best[1], "n_feasible": int(nfeas)}


def better(e1, e2):
    """strict lexicographic e1 < e2."""
    if e1[0] < e2[0] - TOL:
        return True
    if abs(e1[0] - e2[0]) <= TOL:
        return e1[1] < e2[1]
    return False


def best_response(C, k, i, bonds, h):
    best, bk = energy(C, k, bonds, h)[0], k[i]
    for c in range(1, KMAX + 1):
        kk = list(k)
        kk[i] = c
        e = energy(C, kk, bonds, h)[0]
        if better(e, best):
            best, bk = e, c
    return bk


def cascade_sequential(C, k0, bonds, h, log):
    k = list(k0)
    path = [list(k)]
    for sweep in range(50):
        moved = False
        for i in range(len(k)):
            c = best_response(C, k, i, bonds, h)
            if c != k[i]:
                k[i] = c
                moved = True
                path.append(list(k))
        if not moved:
            break
    e, _ = energy(C, k, bonds, h)
    log(f"      sequential: path {path} -> stable {k}, viol {mp.nstr(e[0], 5)}, cost {e[1]}")
    return {"path": path, "stable": k, "viol": fmt(e[0]), "cost": e[1]}


def cascade_sync(C, k0, bonds, h, log, label):
    k = list(k0)
    rounds = [list(k)]
    seen = {tuple(k)}
    cycled = False
    for r in range(30):
        new = [best_response(C, k, i, bonds, h) for i in range(len(k))]
        if new == k:
            break
        k = new
        rounds.append(list(k))
        if tuple(k) in seen:
            cycled = True
            break
        seen.add(tuple(k))
    e, _ = energy(C, k, bonds, h)
    moved_at = [[i for i in range(len(k)) if rounds[t][i] != rounds[t - 1][i]] for t in range(1, len(rounds))]
    log(f"      synchronous{label}: rounds {rounds}, movers per round {moved_at}, "
        f"{'CYCLE' if cycled else 'stable'} {k}, viol {mp.nstr(e[0], 5)}, cost {e[1]}")
    return {"rounds": rounds, "movers": moved_at, "cycled": cycled, "end": k,
            "viol": fmt(e[0]), "cost": e[1]}


def brute(C, A, bonds, h):
    best, arg, feas = None, None, []
    for k in product(range(1, KMAX + 1), repeat=A):
        e, _ = energy(C, list(k), bonds, h)
        if e[0] == 0:
            feas.append(list(k))
        if best is None or better(e, best):
            best, arg = e, list(k)
    return best, arg, feas


def main() -> int:
    t0 = time.time()
    mp.mp.dps = DPS
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q

    def log(s):
        print(s, flush=True)

    out = {}
    for A in (1, 2, 3):
        C = Chars(3 * A, q)
        log(f"\nA = {A} (H_{3 * A}), live blocks {[b[0] for b in C.blocks]}, wall {time.time() - t0:.0f} s")
        res = {"live_blocks": [list(b[0]) for b in C.blocks]}
        for label, bonds in (("unbonded", []), ("bonded", list(range(A - 1)))):
            if A == 1 and label == "bonded":
                continue
            best, arg, feas = brute(C, A, bonds, h)
            log(f"    {label}: brute-force optimum {arg} (viol {mp.nstr(best[0], 5)}, cost {best[1]}); "
                f"{len(feas)} feasible of {KMAX ** A}: {feas[:12]}{' ...' if len(feas) > 12 else ''}")
            r = {"bonds": bonds, "optimum": arg, "optimum_viol": fmt(best[0]), "optimum_cost": best[1],
                 "n_feasible": len(feas), "feasible": feas}
            if label == "bonded":
                e0, ch0 = energy(C, [3] * A, bonds, h)
                log(f"    start k = {[3] * A} after bonding: viol {mp.nstr(e0[0], 6)}, "
                    f"chi = {[mp.nstr(c, 6) for c in ch0]}")
                r["start_viol"] = fmt(e0[0])
                r["start_chi"] = [fmt(c) for c in ch0]
                r["sequential"] = cascade_sequential(C, [3] * A, bonds, h, log)
                r["synchronous"] = cascade_sync(C, [3] * A, bonds, h, log, "")
            res[label] = r
        if A == 3:
            # perturbation: settle with bond (0,1) only, then add bond (1,2)
            _, a1, _ = brute(C, A, [0], h)
            log(f"    perturbation: optimum with bond 0 only = {a1}")
            seq1 = cascade_sequential(C, [3, 3, 3], [0], h, log)
            pert = cascade_sync(C, seq1["stable"], [0, 1], h, log, " after adding bond 1")
            res["perturbation"] = {"optimum_bond0": a1, "settle_bond0": seq1, "after_bond1": pert}
            res["bond_powers_as_players"] = joint_bond_cascade(C, A, h, log)
        out[f"A{A}"] = res
    # Owner ruling 2026-11-15: reading 3 per bonded group.  Fully bonded chains
    # are one group, so their rows above are unchanged; re-run what differs.
    log(f"\nRULE: reading 3 per bonded group (owner 2026-11-15), wall {time.time() - t0:.0f} s")
    Cs = {s: Chars(3 * s, q) for s in (1, 2, 3)}
    grp = {}
    for A in (2, 3):
        r = {}
        for label, bonds in (("unbonded", []), ("bonded", list(range(A - 1)))):
            best, arg, feas = brute(Cs, A, bonds, h)
            log(f"  A={A} {label}: optimum {arg} (viol {mp.nstr(best[0], 5)}, cost {best[1]}); "
                f"{len(feas)} feasible of {KMAX ** A}")
            r[label] = {"optimum": arg, "optimum_viol": fmt(best[0]), "optimum_cost": best[1],
                        "n_feasible": len(feas)}
        if A == 3:
            _, a1, f1 = brute(Cs, A, [0], h)
            log(f"  A=3 bond 0 only: optimum {a1}, {len(f1)} feasible")
            seq1 = cascade_sequential(Cs, [3, 3, 3], [0], h, log)
            pert = cascade_sync(Cs, seq1["stable"], [0, 1], h, log, " after adding bond 1")
            r["perturbation"] = {"optimum_bond0": a1, "n_feasible_bond0": len(f1),
                                 "settle_bond0": seq1, "after_bond1": pert}
        grp[f"A{A}"] = r
    out["per_bonded_group"] = grp
    log(f"\nwall {time.time() - t0:.0f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("chain-reaction-cascade-probe", engine="python", start_time=t0)
    wb.set_description("Best-response cascade of gamma-gamma powers on joined strand windows after a "
                       "bond is added; reading 3 on the joint word, convention D, proton pin; lexicographic "
                       "(violation, crossing cost) energy is a stated choice. Mathematics only.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_parameter("kmax", KMAX)
    for key, v in out.items():
        wb.add_data(key, v)
    path = wb.save()
    print(f"witness -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
