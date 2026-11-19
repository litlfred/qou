#!/usr/bin/env python3
"""Re-run of qbeta_delta_net_four_values_probe on the CANONICAL (borromean) word.

Bean qou-vtlj.  That probe's `hecke_word(g0, g1)` multiplies ALL gen-0 letters,
then ALL gen-1 letters -- the GROUPED (pre-2026-09-05) assembly.  Every factor
`sigma_g + d` lies in the 2-dim subalgebra span{1, sigma_g}, which is closed
under multiplication (sigma_g^2 = h sigma_g + 1).  So a grouped word is

    (a + b sigma_0)(c + d sigma_1)  in  span{1, sigma_0, sigma_1, sigma_0 sigma_1}

and its L_- = sigma_1 sigma_0 and e_- = sigma_0 sigma_1 sigma_0 coordinates are
ZERO FOR EVERY WORD, every q, every shift.  The "exactly 0" and the
negative-definite parabola built on it are therefore properties of the
assembly, not of the nucleon.

This probe:
  (1) proves that algebraically (symbolic, generic shifts);
  (2) re-derives the six NF coordinates, nets, the 6-component match against
      tbl:categorical-neutron-table-data, and the gamma-gamma exclusion on the
      BORROMEAN word from `pyhecke.atom.nucleon_word_letters` (default
      intra_order), exactly in Q(q), read out at the proton-pinned q0;
  (3) reproduces the grouped numbers as a control.

Exact symbolic Q(q) arithmetic, mpf readout at 50 dps, proton pin. Writes no
witness (report-only re-run; scope-(a); adjudicates nothing).

-- Ref: [manuscript] computations/qbeta/qbeta_delta_net_four_values_probe.py
"""
from __future__ import annotations

import sys
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS_NAMES, L, ONE, basis_vec,
)
from pyhecke.atom import nucleon_word_letters  # noqa: E402

set_compute_dps(60)
Q0 = sp.Rational(Q_50_DIGIT_STR)
TGT = [mp.mpf(x) for x in ("-0.0096", "-0.0481", "0.0461",
                           "-0.2206", "0.0189", "1.0109")]
T49 = mp.mpf("0.0445860283330804029291040528152801211016800484547")


def num(e):
    return mp.mpf(str(sp.N(sp.sympify(e).subs(q, Q0), 55)))


def element(letters):
    M = ONE
    for c, d, g in letters:
        M = M * (sp.sympify(c) * L[g] + sp.sympify(d) * ONE)
    return [sp.factor(sp.simplify(x)) for x in (M * basis_vec(0))]


def main() -> int:
    fails = 0
    # (1) algebra: grouped word with GENERIC shifts
    a = sp.symbols("a0:4")
    b = sp.symbols("b0:3")
    M = ONE
    for s in a:
        M = M * (L[0] + s * ONE)
    for s in b:
        M = M * (L[1] + s * ONE)
    v = sp.expand(M * basis_vec(0))
    ok = sp.simplify(v[4]) == 0 and sp.simplify(v[5]) == 0
    print(f"[{'PASS' if ok else 'FAIL'}] grouped word, generic shifts: "
          f"L_- = {sp.simplify(v[4])}, e_- = {sp.simplify(v[5])}")
    fails += not ok

    res = {}
    for order in ("grouped", "borromean"):
        for nuc, qk in (("p", ["u", "u", "d"]), ("n", ["u", "d", "d"])):
            lw = nucleon_word_letters(qk, q=q, intra_order=order)
            res[(order, nuc)] = element(lw)
            word = "".join(f"s{g}" + ("" if sp.simplify(d) == 0 else
                                      ("^-1" if sp.simplify(d + h) == 0 else "~"))
                           + " " for _, d, g in lw)
            print(f"\n{order:9s} {nuc}: {word}")
            for i, nm in enumerate(BASIS_NAMES):
                print(f"   {nm:8s} {mp.nstr(num(res[(order, nuc)][i]), 20):>26}"
                      f"    exact: {res[(order, nuc)][i]}")
            print(f"   net      {mp.nstr(num(sum(res[(order, nuc)])), 20)}")

    zD = q**3 / (q**2 + 1)
    zC = sp.sqrt(q) / (q + 1)
    for order in ("grouped", "borromean"):
        nv = [num(x) for x in res[(order, "n")]]
        hits = sum(1 for i in range(N) if abs(nv[i] - TGT[i]) < mp.mpf("5e-4"))
        err = max(abs(nv[i] - TGT[i]) for i in range(N))
        print(f"\n[{order}] neutron NF vs tbl:categorical-neutron-table-data: "
              f"{hits}/6 within 5e-4, max|err| {mp.nstr(err, 6)}")
        print(f"[{order}] Delta net (n-p) = "
              f"{mp.nstr(num(sum(res[(order,'n')]) - sum(res[(order,'p')])), 20)}")
        dv = [sp.simplify(res[(order, "n")][i] - res[(order, "p")][i])
              for i in range(N)]
        # tr_M(z) = d0 + (d1+d2) z + (d3+d4) z^2 + d5 z(hz+1)
        A = sp.factor(sp.simplify(dv[3] + dv[4] + dv[5] * h))
        B = sp.factor(sp.simplify(dv[1] + dv[2] + dv[5]))
        C = sp.factor(sp.simplify(dv[0]))
        An, Bn, Cn = num(A), num(B), num(C)
        print(f"[{order}] Delta tr_M(z) = A z^2 + B z + C")
        print(f"     A = {A}  = {mp.nstr(An, 15)}")
        print(f"     B = {B}  = {mp.nstr(Bn, 15)}")
        print(f"     C = {C}  = {mp.nstr(Cn, 15)}")
        if An != 0:
            vz = -Bn / (2 * An)
            vv = Cn - Bn**2 / (4 * An)
            kind = "MAX" if An < 0 else "MIN"
            print(f"     vertex ({kind}) z* = {mp.nstr(vz, 15)}, value "
                  f"{mp.nstr(vv, 15)}")
            for T in (T49, -T49):
                disc = Bn**2 - 4 * An * (Cn - T)
                if disc >= 0:
                    rts = [(-Bn + s * mp.sqrt(disc)) / (2 * An) for s in (1, -1)]
                    print(f"     reaches {mp.nstr(T, 12)} at z = "
                          + ", ".join(mp.nstr(r, 15) for r in rts))
                else:
                    print(f"     does NOT reach {mp.nstr(T, 12)} at any real z")
        for nm, z in (("z_D", zD), ("z_C", zC)):
            val = num(C + B * z + A * z**2)
            print(f"     Delta tr_M at {nm} = {mp.nstr(val, 20)}")
        # theorem-in-q check of the old claim: L_-, e_- identically zero?
        print(f"     (n-p) L_- = {dv[4]};  e_- = {dv[5]}")

    print(f"\n{fails} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
