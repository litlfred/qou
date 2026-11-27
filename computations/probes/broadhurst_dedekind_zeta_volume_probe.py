#!/usr/bin/env python3
"""broadhurst_dedekind_zeta_volume_probe.py — bean qou-2pp7.

Cross-check of Broadhurst, "Determinations of rational Dedekind-zeta
invariants of hyperbolic manifolds and Feynman knots and links" (1998)
[broadhurst1998], library/arxiv-hep-th-9811173v1/ (LaTeX source), against the
corpus link/knot volumes in computations/binding-link-volumes.witness.json
(producer computations/binding_link_volumes.py). Cross-check only: no external
number is adopted into any witness.

PRE-REGISTERED (written before running):

  Source facts used (LaTeX source bblink.tex):
    S1  eq (ZK): Z_K = (-D)^{3/2} / (2 pi)^{2n-4} * zeta_K(2) / (2 zeta(2)) for
        a field K of degree n with one complex place; eq (ab): (a/b) vol(M) = Z_K
        when K is the invariant trace field of M.
    S2  eq (ZKq), quadratic K: Z_{|D|} = |D| sum_{0<2k<|D|} chi_D(k) Cl_2(2 pi k/|D|).
    S3  Sec 4.3-4.5: a/b = 1 for 4_1 (D=-3) and the Whitehead link 5^2_1
        (D=-4); a/b = 2 for the link 6^3_1 (D=-7).

  Checks (mpmath 60 dps; cypari at 60 digits for zeta_K; SnapPy high precision):
    D  S1 and S2 agree for D = -3, -4, -7 (pari lfun on nfinit), rel < 1e-40
       (checks my transcription of both formulas).
    B  S3 reproduced with SnapPy volumes: 4_1, 5^2_1 at a/b = 1 and 6^3_1 at
       a/b = 2, rel < 1e-40.
    A  The corpus Borromean volume Vol_B3_8G = 7.327724753417752 (witness) and
       SnapPy Vol(L6a4) give a/b = 1/2 against Z_4, rel < 1e-14 for the
       15-digit witness value and < 1e-40 for SnapPy.
    C  The corpus triton knot 8_11: the witness value 8.2863168178 matches
       SnapPy to 10 digits. Reported, not gated: the shape field from pari
       algdep, its number of complex places, and a/b when it has exactly one
       complex place (bestappr, b <= 1000, residual < 1e-30 required to report).
    PASS iff D, B, A, C.

  AMENDMENT after the first run (thresholds unchanged): D failed at rel ~1e-20
  because cypari's Python-level pari.lfun(nf, 2) returns ~19 digits whatever
  realprecision is set (measured: 1.5067030099229850309 vs the string-evaluated
  1.50670300992298503088656504818...). That was my harness, not the source.
  zeta_K(2) is now evaluated as pari("lfun(nfinit(poly),2)"), which honours
  realprecision 70.

  Premise note (read before running): the witness's deuteron row uses
  vol_eff = Vol(B3) for a Hopf link (Vol 0), and its 3H/3He rows assign the
  census knot 8_11 and link L6a4. AGENTS.md records owner ruling A (2026-08-29:
  the deuteron binding is not a hyperbolic-volume term) and the 2026-09-05
  retirement of census selection. This probe checks the volumes only, not the
  binding assignments.

Run: python3 -u computations/probes/broadhurst_dedekind_zeta_volume_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]


def ZK_pari(poly, pari):
    nf = pari.nfinit(poly)
    n = int(pari.poldegree(poly))
    D = mp.mpf(str(nf.disc()))
    zk = mp.mpf(str(pari(f"lfun(nfinit({poly}),2)")))
    return (-D) ** (mp.mpf(3) / 2) / (2 * mp.pi) ** (2 * n - 4) * zk / (2 * mp.zeta(2))


def kron(D, k):
    import sympy
    return int(sympy.kronecker_symbol(D, k))


def ZKq(D):
    a = abs(D)
    return a * mp.fsum(kron(D, k) * mp.clsin(2, 2 * mp.pi * k / a)
                       for k in range(1, a) if 2 * k < a)


def main() -> int:
    from cypari import pari
    import snappy
    mp.mp.dps = 60
    pari.set_real_precision(70)
    t40 = mp.mpf(10) ** -40
    polys = {-3: "x^2+x+1", -4: "x^2+1", -7: "x^2+x+2"}
    d_ok = True
    for D, p in polys.items():
        r = abs(ZK_pari(p, pari) / ZKq(D) - 1)
        d_ok &= r < t40
        print(f"D  Z_{abs(D)}: (ZK) {mp.nstr(ZK_pari(p, pari), 20)}  (ZKq) {mp.nstr(ZKq(D), 20)}  rel {mp.nstr(r, 3)}")
    print(f"D  S1 = S2 for D = -3, -4, -7: {d_ok}")

    def vol(name):
        return mp.mpf(str(snappy.Manifold(name).high_precision().volume()))
    b_ok = True
    for name, D, ab in (("4_1", -3, 1), ("5^2_1", -4, 1), ("6^3_1", -7, 2)):
        r = abs(ab * vol(name) / ZKq(D) - 1)
        b_ok &= r < t40
        print(f"B  {name}: a/b = {ab} * vol = Z_{abs(D)}, rel {mp.nstr(r, 3)}")
    print(f"B  source Sec 4.3-4.5 reproduced: {b_ok}")
    w = json.loads((ROOT / "computations/binding-link-volumes.witness.json").read_text())
    vb = mp.mpf(w["data"]["binding_link_volumes"]["Vol_B3_8G"])
    v8 = mp.mpf(w["data"]["binding_link_volumes"]["knot_8_11_3H"])
    z4 = ZKq(-4)
    r1 = abs(vb / 2 / z4 - 1)
    r2 = abs(vol("L6a4") / 2 / z4 - 1)
    a_ok = r1 < mp.mpf(10) ** -14 and r2 < t40
    print(f"A  corpus Vol(B3)/2 vs Z_4: rel {mp.nstr(r1, 3)}; SnapPy L6a4: rel {mp.nstr(r2, 3)}: {a_ok}")
    M = snappy.Manifold("8_11").high_precision()
    v811 = mp.mpf(str(M.volume()))
    c_ok = abs(v811 - v8) < mp.mpf(10) ** -9
    print(f"C  8_11: witness {v8} vs SnapPy {mp.nstr(v811, 25)}: {c_ok}")
    shapes = M.tetrahedra_shapes("rect")
    z = shapes[0]
    zp = pari(f"{mp.nstr(mp.mpf(str(z.real())), 60)} + I*({mp.nstr(mp.mpf(str(z.imag())), 60)})")
    found = None
    for deg in range(2, 13):
        P = pari.algdep(zp, deg)
        if abs(pari.subst(P, "x", zp)) < pari("1e-50") and pari.polisirreducible(P):
            found = pari.polredabs(P)
            break
    if found is None:
        print("C  shape field: no algebraic relation of degree <= 12 found at 60 digits")
    else:
        n = int(pari.poldegree(found))
        r2c = int(pari.polsturm(found))
        ncx = (n - r2c) // 2
        print(f"C  shape field of 8_11: {found}, degree {n}, complex places {ncx}")
        if ncx == 1:
            zk = ZK_pari(found, pari)
            ratio = zk / v811
            ap = pari.bestappr(pari(mp.nstr(ratio, 50)), 1000)
            res = abs(mp.mpf(str(pari.numerator(ap))) / mp.mpf(str(pari.denominator(ap))) - ratio)
            if res < mp.mpf(10) ** -30:
                print(f"C  a/b(8_11) = {ap}  (residual {mp.nstr(res, 3)})")
            else:
                print(f"C  no a/b with b <= 1000 (best {ap}, residual {mp.nstr(res, 3)})")
    ok = d_ok and b_ok and a_ok and c_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
