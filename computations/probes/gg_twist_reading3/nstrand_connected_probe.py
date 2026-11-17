#!/usr/bin/env python3
"""nstrand_connected_probe.py — stage 6: n-strand chains, rings and Brunnian loops.

Pre-registered in preregistration.md §Stage 6 before this file was written. Exact arithmetic
throughout: the Kauffman bracket is a Laurent polynomial in A with integer coefficients (Temperley-
Lieb basis, tl_bracket.py), and every zero / nonzero verdict is an exact polynomial identity. The
only floating step is the reported value of log(ratio) at t = q0 (mpmath, 70 dps, proton pin).

F(T) = log(delta * V_T) - |T| log delta, delta = -(A^2 + A^-2), A = t^(-1/4).
phi(T) = sum_{U subset T} (-1)^{|T|-|U|} F(U)  (Lean: QOU.VirtualSubword.connected).

* Chain: tests the HYPOTHESIS of QOU.VirtualSubword.connected_eq_zero_of_bonds exactly, i.e. that
  delta V_U / delta^|U| equals the product over bonds inside U of delta V_e / delta^2. When it holds
  for every U, the Lean theorem gives phi(T) = 0 for every |T| >= 3, with no further computation.
* Ring: exact phi(full set); order and leading coefficient of log(ratio) in s = log t.
* Brunnian: every proper sublink is checked to be an unlink, so phi(full) = F(full).

Nothing is fitted or selected; every pre-registered word is run.
-- Ref: [leitner2026] def:virtual-subword; bean qou-a1hh
"""
from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction
from math import factorial
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tl_bracket as tl  # noqa: E402
from borromean_jones_cumulant_probe import restrict  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

DELTA = {2: -1, -2: -1}


def inv(w):
    return [(g, -s) for g, s in reversed(w)]


def jones(w, k):
    """delta-free Jones V = (-A^3)^(-writhe) <closure>, as a Laurent dict in A."""
    if not w:
        return tl.ppow(DELTA, k - 1)
    wr = sum(s for _, s in w)
    sign = -1 if wr % 2 else 1
    return {e - 3 * wr: sign * v for e, v in tl.bracket(w, k).items()}


def chain(n, e):
    return [(i, 1 if e > 0 else -1) for i in range(n - 1) for _ in range(abs(e))]


def ring(n, e):
    rho = [(g, 1) for g in range(n - 1)]
    core = [(n - 2, 1 if e > 0 else -1)] * abs(e)
    return chain(n, e) + rho + core + inv(rho)


def A0(j):
    """Pure-braid generator A_{0,j}: strand j loops once around strand 0."""
    return [(i, 1) for i in range(j - 1, 0, -1)] + [(0, 1), (0, 1)] + [(i, -1) for i in range(1, j)]


def brunnian(n):
    c = A0(1)
    for k in range(3, n + 1):
        a = A0(k - 1)
        c = c + a + inv(c) + inv(a)
    return c


def free_reduce(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return out


def eq(p, q):
    return {k: v for k, v in p.items() if v} == {k: v for k, v in q.items() if v}


def V_of(w, n, U):
    sw, k = restrict(w, n, set(U))
    return jones(sw, k)


def mobius_ratio(Vs, n):
    """num/den with phi(full) = log(num/den); exact Laurent dicts, delta powers cleared."""
    num, den = {0: 1}, {0: 1}
    for U, V in Vs.items():
        k = len(U)
        if (-1) ** (n - k) > 0:
            num = tl.pmul(num, V)
            den = tl.pmul(den, tl.ppow(DELTA, k - 1))
        else:
            den = tl.pmul(den, V)
            num = tl.pmul(num, tl.ppow(DELTA, k - 1))
    return num, den


def log_series(num, den):
    """Order m and exact leading coefficient c of log(num/den) = c s^m + ..., s = log t."""
    diff = tl.padd(num, den, -1)
    if not diff:
        return None, Fraction(0)
    d0 = sum(den.values())
    m = 0
    while True:
        cm = sum(Fraction(v) * Fraction(-j, 4) ** m for j, v in diff.items()) / factorial(m)
        if cm != 0:
            return m, cm / d0
        m += 1


def at_q0(p, q0):
    A = q0 ** mp.mpf(-0.25)
    return mp.fsum(v * A ** e for e, v in p.items())


def main() -> int:
    t0 = time.time()
    q0 = mp.mpf(q_at())
    out = {"chains": {}, "rings": {}, "brunnian": {}}

    for n in range(3, 9):
        for e in (2, -2):
            w = chain(n, e)
            bondV = {i: V_of(w, n, (i, i + 1)) for i in range(n - 1)}
            holds = True
            for r in range(1, n + 1):
                for U in itertools.combinations(range(n), r):
                    lhs = V_of(w, n, U)
                    rhs = tl.ppow(DELTA, r - 1)
                    for i in range(n - 1):
                        if i in U and i + 1 in U:
                            rhs = tl.pmul(rhs, bondV[i])
                    nb = sum(1 for i in range(n - 1) if i in U and i + 1 in U)
                    # delta V_U / delta^|U| = prod_e (V_e / delta)  <=>  V_U delta^nb = delta^(|U|-1) prod_e V_e
                    if not eq(tl.pmul(lhs, tl.ppow(DELTA, nb)), rhs):
                        holds = False
                        break
                if not holds:
                    break
            out["chains"][f"n={n},e={e}"] = {"bond_additive_exact": holds,
                                             "phi_ge3_zero_by_lean": holds}
            print(f"chain n={n} e={e}: bond-additive {holds} [{time.time()-t0:.0f}s]", flush=True)

    for n in range(3, 9):
        for e in (2, -2):
            w = ring(n, e)
            Vs = {U: V_of(w, n, U) for r in range(1, n + 1) for U in itertools.combinations(range(n), r)}
            num, den = mobius_ratio(Vs, n)
            m, c = log_series(num, den)
            val = mp.log(at_q0(num, q0) / at_q0(den, q0))
            out["rings"][f"n={n},e={e}"] = {
                "letters": len(w), "phi_full_exactly_zero": m is None,
                "log_t_order": m, "leading_coeff": str(c),
                "phi_full_at_t_q0": mp.nstr(val, 20)}
            print(f"ring n={n} e={e}: zero={m is None} order={m} coeff={c} "
                  f"phi(q0)={mp.nstr(val, 8)} [{time.time()-t0:.0f}s]", flush=True)

    for n in range(3, 7):
        w = free_reduce(brunnian(n))
        proper_unlink = all(eq(V_of(w, n, U), tl.ppow(DELTA, len(U) - 1))
                            for r in range(1, n) for U in itertools.combinations(range(n), r))
        V = V_of(w, n, tuple(range(n)))
        num, den = V, tl.ppow(DELTA, n - 1)
        m, c = log_series(num, den)
        val = mp.log(at_q0(num, q0) / at_q0(den, q0))
        out["brunnian"][f"n={n}"] = {
            "letters": len(w), "proper_sublinks_unlinked": proper_unlink,
            "phi_full_exactly_zero": m is None, "log_t_order": m, "leading_coeff": str(c),
            "phi_full_at_t_q0": mp.nstr(val, 20),
            "jones_A": {str(k): v for k, v in sorted(V.items())}}
        print(f"brunnian n={n} len={len(w)}: proper unlinked {proper_unlink} zero={m is None} "
              f"order={m} coeff={c} phi(q0)={mp.nstr(val, 8)} [{time.time()-t0:.0f}s]", flush=True)

    # cross-check against stage 5 (6-carbon ring, +2, front band): 3/64 s^6
    s5 = out["rings"]["n=6,e=2"]
    xok = s5["log_t_order"] == 6 and s5["leading_coeff"] == "3/64"
    print("stage-5 cross-check (n=6, +2: 3/64 s^6):", xok)

    wb = WitnessBuilder("nstrand-connected-stage6", engine="mpmath", output_dir=HERE)
    wb.add_assertion("stage5_ring_cross_check", computed="1" if xok else "0", expected="1",
                     source="carbon-ring-stage5.witness.json phi_all6 ring +2 front")
    wb.save({
        "q0Anchor": "proton", "q0AnchorReason": "q_at() (proton pin), only for the reported value at t = q0",
        "description": "PROBE stage 6 (bean qou-a1hh): exact Jones connected parts of n-strand chains "
                       "(bond-additivity, the hypothesis of connected_eq_zero_of_bonds), rings "
                       "(closing band in front) and iterated-commutator Brunnian loops. Pre-registered.",
        **out,
    })
    print(f"done [{time.time()-t0:.0f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
