#!/usr/bin/env python3
"""Kashaev invariant of the weaving knots W(3,m) = closure of V0^m, V0 = s0 s1^-1,
at the root of unity q = e^{2 pi i/N}, and a gauge-invariant test of the external
discussion's claim that <8_18>_N = Tr(M^2) is a term-wise positive sum.

Pre-registration: PREREGISTRATION.md in this directory (written before any run).

State model: [arxiv-2209.06973v1] sec 5, in the convention pinned by
computations/probes/weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py
(conv (True, True, False, 1, 1, 1)); that probe checks it against the corpus
Habiro tower for 4_1 exactly (n = 1, 2, 3).

Arithmetic: mpmath complex, mp.dps = 60. NOT exact; verdicts carry margins.
No float anywhere in the computation.

Run: python3 -u computations/probes/weaving_kashaev_root_of_unity/weaving_kashaev_probe.py [Nmax]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent

# Volumes: SnapPy high-precision (numerical, not certified), computed 2026-11-27,
# snappy.Link(braid_closure=[1,-2]*m).exterior().high_precision().volume().
# Used ONLY as comparison targets in the report, never inside a computation.
VOL = {
    2: mp.mpf("2.029883212819307250042405108549040571883378615060599584034978214"),
    4: mp.mpf("12.350906209158200174736304438426152014199256704119996280612478809"),
    5: mp.mpf("17.085709482982861276900974840483654825038359609430629014436176291"),
}
NAME = {2: "4_1", 3: "Borromean", 4: "8_18", 5: "10_123"}

CONV = (True, True, False, 1, 1, 1)  # (left_over_pos, ij_pos, ij_neg, sgn_pos, sgn_neg, clos_sign)
PERIOD = [-1, 2]  # paper's word for V0 (mirror of s0 s1^-1; W(3,m) amphichiral)


class Ring:
    """Evaluation at w = e^{2 pi i/(4N)}, v = w^2, q = v^2 = e^{2 pi i/N}."""

    def __init__(self, N: int):
        self.N = N
        self.n = N - 1
        self.w = mp.expjpi(mp.mpf(1) / (2 * N))  # e^{i pi/(2N)}

    def wpow(self, k: int):
        return self.w ** k

    def br(self, a: int):  # {a} = v^a - v^-a
        return self.wpow(2 * a) - self.wpow(-2 * a)

    def poch(self, a: int, b: int):
        if b < 0:
            return mp.mpc(0)
        out = mp.mpc(1)
        for k in range(b):
            out *= self.br(a - k)
        return out


def binom_table(R: Ring, amax: int):
    """Balanced quantum binomials C(a,b) = {a}_b/{b}_b via the q-Pascal rule
    C(a,b) = v^{b} C(a-1,b) + v^{-(a-b)} C(a-1,b-1)  (no division)."""
    C = [[mp.mpc(0)] * (amax + 1) for _ in range(amax + 1)]
    for a in range(amax + 1):
        C[a][0] = mp.mpc(1)
        for b in range(1, a + 1):
            C[a][b] = R.wpow(2 * b) * C[a - 1][b] + R.wpow(-2 * (a - b)) * C[a - 1][b - 1]
    return C


def f_table(R: Ring):
    n = R.n
    C = binom_table(R, 2 * n + 2)
    F = {}
    for eps in (1, -1):
        for i in range(n + 1):
            for j in range(n + 1):
                for r in range(n + 1):
                    if eps > 0:
                        val = (-1) ** r * R.wpow(-((n - 2 * i) * (n - 2 * j) + r * (r - 1))) \
                            * C[j + r][r] * R.poch(n + r - i, r)
                    else:
                        val = R.wpow((n - 2 * i - 2 * r) * (n - 2 * j + 2 * r) + r * (r - 1)) \
                            * C[i + r][r] * R.poch(n + r - j, r)
                    F[(eps, i, j, r)] = val
    return F


def apply_crossing(states: dict, g: int, n: int, F: dict) -> dict:
    lop, ijp, ijm, sgp, sgm, _cs = CONV
    p = abs(g) - 1
    eps = 1 if g > 0 else -1
    left_over = lop if eps > 0 else (not lop)
    ij_over_under = ijp if eps > 0 else ijm
    sgn = sgp if eps > 0 else sgm
    new: dict = {}
    for c, wt in states.items():
        a, b = c[p], c[p + 1]
        over, under = (a, b) if left_over else (b, a)
        i, j = (over, under) if ij_over_under else (under, over)
        for r in range(n + 1):
            o2, u2 = over - sgn * r, under + sgn * r
            if not (0 <= o2 <= n and 0 <= u2 <= n):
                continue
            fv = F[(eps, i, j, r)]
            if fv == 0:
                continue
            nc = list(c)
            if left_over:
                nc[p], nc[p + 1] = u2, o2
            else:
                nc[p], nc[p + 1] = o2, u2
            nc = tuple(nc)
            new[nc] = new.get(nc, 0) + wt * fv
    return new


def transfer_rows(start, word, n, F):
    st = {start: mp.mpc(1)}
    for g in word:
        st = apply_crossing(st, g, n, F)
    return st


def clos(R: Ring, rest) -> mp.mpc:
    cs = CONV[5]
    out = mp.mpc(1)
    for b in rest:
        out *= R.wpow(2 * cs * (-R.n + 2 * b))
    return out


def kashaev(R: Ring, F, m: int):
    n = R.n
    total = mp.mpc(0)
    for r1 in range(n + 1):
        for r2 in range(n + 1):
            start = (0, r1, r2)
            row = transfer_rows(start, PERIOD * m, n, F)
            total += row.get(start, 0) * clos(R, (r1, r2))
    return total


def habiro41(N: int):
    s = mp.mpf(0)
    for m in range(N):
        p = mp.mpf(1)
        for j in range(1, m + 1):
            p *= 4 * mp.sin(mp.pi * j / N) ** 2
        s += p
    return s


def termwise(R: Ring, F, k: int):
    """<V0^{2k}> = sum_{a,b} clos(a) P[a,b] P[b,a],  P = M^k (gauge-invariant products)."""
    n = R.n
    word = PERIOD * k
    rows_a = {}
    for r1 in range(n + 1):
        for r2 in range(n + 1):
            a = (0, r1, r2)
            rows_a[a] = transfer_rows(a, word, n, F)
    bs = set()
    for row in rows_a.values():
        bs.update(row.keys())
    rows_b = {b: transfer_rows(b, word, n, F) for b in bs}
    tot = mp.mpc(0)
    abs_sum = mp.mpf(0)
    neg_mass = mp.mpf(0)
    n_terms = n_neg = n_complex = 0
    for a, row in rows_a.items():
        ca = clos(R, a[1:])
        for b, pab in row.items():
            pba = rows_b[b].get(a, 0)
            if pba == 0:
                continue
            t = ca * pab * pba
            n_terms += 1
            tot += t
            at = abs(t)
            abs_sum += at
            if abs(t.imag) > mp.mpf(10) ** -40 * at:
                n_complex += 1
            if t.real < 0:
                n_neg += 1
                neg_mass += -t.real
    return {
        "sum": tot, "n_terms": n_terms, "n_negative_real": n_neg,
        "n_nonreal": n_complex, "abs_sum": abs_sum, "neg_mass": neg_mass,
    }


def s(x, d=25):
    return mp.nstr(x, d)


def main() -> int:
    Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    Nmin = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    q3max = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    tag = sys.argv[4] if len(sys.argv) > 4 else ""
    out = {"preregistration": "PREREGISTRATION.md", "dps": mp.mp.dps, "conv": CONV,
           "Q0": [], "Q1": [], "Q3": []}
    t0 = time.time()
    q0_ok = True
    for N in range(Nmin, Nmax + 1):
        R = Ring(N)
        F = f_table(R)
        k41 = kashaev(R, F, 2)
        h = habiro41(N)
        diff = abs(k41 - h)
        ok = diff < mp.mpf(10) ** -50 * max(1, abs(h))
        q0_ok &= ok
        out["Q0"].append({"N": N, "state_model": s(k41.real, 30), "imag": s(k41.imag, 5),
                          "habiro": s(h, 30), "absdiff": s(diff, 5), "ok": bool(ok)})
        print(f"Q0 N={N:2d} <4_1>={s(k41.real,20)} habiro={s(h,20)} |diff|={s(diff,3)} ok={ok}"
              f"  [{time.time()-t0:.0f}s]", flush=True)
        for m in (3, 4, 5):
            val = kashaev(R, F, m)
            rec = {"m": m, "knot": NAME[m], "N": N, "re": s(val.real, 30), "im": s(val.imag, 5)}
            line = f"Q1 N={N:2d} m={m} {NAME[m]:9s} <K>_N = {s(val.real,20)} (Im {s(val.imag,3)})"
            if m in VOL and abs(val) > 0:
                rate = 2 * mp.pi / N * mp.log(abs(val))
                # diagnostic only: subtract the 1-loop term (3/2) log N predicted by the
                # asymptotic-expansion conjecture; NOT used in any verdict
                rate1 = rate - 2 * mp.pi / N * mp.mpf(3) / 2 * mp.log(N)
                rec["rate"] = s(rate, 20)
                rec["rate_minus_vol"] = s(rate - VOL[m], 10)
                rec["rate_minus_oneloop_minus_vol"] = s(rate1 - VOL[m], 10)
                line += (f"  (2pi/N)log|K| = {s(rate,12)}  - Vol = {s(rate-VOL[m],6)}"
                         f"  [minus 1-loop: {s(rate1-VOL[m],6)}]")
            out["Q1"].append(rec)
            print(line + f"  [{time.time()-t0:.0f}s]", flush=True)
        for k in ((1, 2) if N <= q3max else ()):
            tw = termwise(R, F, k)
            rho = tw["abs_sum"] / abs(tw["sum"]) if abs(tw["sum"]) > 0 else mp.inf
            rec = {"m": 2 * k, "knot": NAME[2 * k], "N": N, "n_terms": tw["n_terms"],
                   "n_negative_real": tw["n_negative_real"], "n_nonreal": tw["n_nonreal"],
                   "abs_sum": s(tw["abs_sum"], 20), "sum": s(tw["sum"].real, 20),
                   "neg_mass": s(tw["neg_mass"], 20), "rho": s(rho, 15),
                   "log_rho_over_N": s(mp.log(rho) / N, 10) if rho not in (mp.inf,) else "inf"}
            out["Q3"].append(rec)
            print(f"Q3 N={N:2d} m={2*k} {NAME[2*k]:5s} terms={tw['n_terms']} neg={tw['n_negative_real']}"
                  f" nonreal={tw['n_nonreal']} rho=sum|T|/|sum T|={s(rho,8)}"
                  f" (1/N)log rho={rec['log_rho_over_N'][:10]}  [{time.time()-t0:.0f}s]", flush=True)
    out["Q0_all_ok"] = bool(q0_ok)
    out["elapsed_s"] = round(time.time() - t0)
    (HERE / f"weaving-kashaev{tag}.result.json").write_text(json.dumps(out, indent=1))
    print("Q0 calibration:", "PASS" if q0_ok else "FAIL")
    return 0 if q0_ok else 1


if __name__ == "__main__":
    sys.exit(main())
