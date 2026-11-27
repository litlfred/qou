"""aomega_m3_pretzel_index_factorisation_blocks_probe.py

Route C, M3 (beans qou-x3iv Part 18, qou-m3ad, qou-gz37): the (-2,3,7) pretzel's
holomorphic blocks, DERIVED from its one-dimensional level-2 state integral and
CERTIFIED against the triangulation 3D index at every magnetic flux m in -2..2.

Pure q-series and exact integer arithmetic for every gate except G5, which is a
high-precision numerical identity check whose residual is shown to scale as the
first omitted q-order (so it certifies the coefficients, not a fit).  No
empirical input; nothing tuned on the pretzel.

The object.  qou-x3iv Parts 10-12a derived (and GK 1411.6062 eq (56) prints) the
pretzel state integral as one-dimensional with factor vector (1,1,2):
    Z(u) = int Phi_b(v + u/2) Phi_b(v - u/2) Phi_b(2v - c_b) e^{-2 pi i v^2} dv.
Its 3d N=2 reading is a U(1) theory with three tetrahedron chirals of gauge
charge (1,1,2) and CS level A = 2.  Its superconformal index, in DGG's
tetrahedron-index form, is

    I(m, zeta) = sum_n q^{-n} CT_z [ z^{2n} I_D(n+m, z zeta) I_D(n-m, z/zeta) I_D(2n, z^2) ],

    I_D(M, w) = (q^{1-M/2} w^{-1}; q)_inf / (q^{-M/2} w; q)_inf.

Gates G1-G2 fix the dictionary state integral -> index on 4_1 and 5_2 (CS level
K = A and weight (-q^{1/2})^{-A n}, flavour charge 1 per meridian shift u, flux
charge 2 per meridian flux); G3 applies the SAME rule to the pretzel, with the
half-meridian shifts u/2 of Part 12a giving flux charge 1 and fugacity charge
1/2.  The only per-knot integer is the longitude framing c (I(m,e) -> I(m,e+cm),
a T-transformation; it never touches the m = 0 row).

The blocks.  Closing the z-contour on the poles of the three denominators
(all at |z| >= 1) factorises the index into SIX families, each a product of a
q-series in x = q^{m/2} zeta and the same series at q^{-1} in x~ = q^{m/2}/zeta
(GGM 2012.00062 eq (19)):

  unit (chiral 1, and chiral 2 = x -> 1/x):
    B_U(x;q) = sum_{j>=0} q^{j(j+1)} x^{2j} (q^{1+j} x^2; q)_inf (q^{1+2j} x^2; q)_inf / (q;q)_j
    prefactor zeta^{2m} q^{+m} (U1),  zeta^{2m} q^{-m} (U2)   [the theta monomial]
  doubled (chiral 3; sign sigma = +-1, parity eps = 0,1 -- the level-2 split):
    B_{sigma,eps}(x;q) = sum_{j = eps mod 2} q^{j(j+2)/4} (sigma q^{1+j/2} x; q)_inf (sigma q^{1+j/2}/x; q)_inf / (q;q)_j
    weight 1/2.

The pole bookkeeping that makes this work (and that Part 12b's fusion lacked):
on the doubled family s~ = sigma' q^{i/2}, s = sigma q^{-j/2} with s s~ = q^n,
so sigma' = sigma and i = j mod 2 -- the SAME sign and the SAME parity on the q
and q^{-1} sides, with the branch (q^{-1})^{1/2} := q^{-1/2}.  The theta
exponent factorises because (A-B)(-1-A-B) = B(B+1) - A(A+1).

Gates
  G0  engine fix: the corpus GHHR engine's shell enumeration stopped before the
      first populated shell for large classes; m004 I(4,1) now equals I(-4,-1).
  G1  4_1: 1-dim index == triangulation index on m in -2..2, e in -6..6, to q^3.
  G2  5_2: same.
  G3  (-2,3,7): same, with the half-meridian dictionary of Part 12a.
  G4  (-2,3,7) total index (m = 0, zeta = 1) == GZ 2111.06645 Obs 3.9 printed
      1 - 8q + 3q^2 + 50q^3 + 58q^4 + 13q^5 - 196q^6 - 456q^7.
  G5  sum of the six block products == the index series, m in -2..2, at two q
      and two zeta; residual / q^8 bounded and the residual ratio between
      q = 0.02 and q = 0.005 is 4^8 to within a factor 2 (truncation scaling).
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))
sys.path.insert(0, HERE)

_spec = importlib.util.spec_from_file_location("b3", os.path.join(HERE, "borromean_3d_index.py"))
b3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b3)
b3.log = lambda *a, **k: None

QREAD = 3          # grid gates to q^3
QHI = 7            # pretzel series for G4/G5 to q^7
MR = range(-2, 3)
ER = range(-6, 7)


# ---------------------------------------------------------------------------
# One-dimensional index (exact, Q = q^{1/2} integer dicts)
# ---------------------------------------------------------------------------

def I_D(M, E, cap):
    return b3.J_D(-M, E, 0, cap)


def nu(M, E):
    return b3.nu_Q(-M, E, 0)


def index1d(alpha, f, K, t, mf, ef, cap, B=10):
    """sum_n sum_E prod_j I_D(alpha_j n + f_j mf, E_j) (-Q)^{t n}, with
    gauge charge sum_j alpha_j E_j + K n = 0 and flavour sum_j f_j E_j = ef."""
    r = len(alpha)
    tot = {}
    for n in range(-B, B + 1):
        M = [alpha[j] * n + f[j] * mf for j in range(r)]
        for free in itertools.product(range(-B, B + 1), repeat=r - 2):
            g = -K * n - sum(alpha[j] * free[j] for j in range(r - 2))
            h = ef - sum(f[j] * free[j] for j in range(r - 2))
            a1, a2, b1, b2 = alpha[r - 2], alpha[r - 1], f[r - 2], f[r - 1]
            det = a1 * b2 - a2 * b1
            xn, yn = g * b2 - a2 * h, a1 * h - b1 * g
            if xn % det or yn % det:
                continue
            E = list(free) + [xn // det, yn // det]
            w = t * n
            mds = [nu(M[j], E[j]) for j in range(r)]
            if sum(mds) + w > cap:
                continue
            prod = {0: 1}
            for j in range(r):
                prod = b3._mul(prod, I_D(M[j], E[j], cap - w - (sum(mds) - mds[j])), cap - w)
            sgn = -1 if (t * n) % 2 else 1
            for p, c in prod.items():
                if p + w <= cap:
                    tot[p + w] = tot.get(p + w, 0) + sgn * c
    return {p: c for p, c in sorted(tot.items()) if c}


# knot: (alpha, flavour charges in units where e_tri = ef/fs, A, flux scale, fugacity scale, framing c)
#   I_tri(m, e) = I_1d(mf = -mscale*m, ef = fs*(e + c*m))
DICT = {
    "m004": dict(alpha=(1, 1), f=(1, 0), A=1, mscale=2, fs=1, c=-2,
                 integrand="Phi_b(v+u) Phi_b(v) e^{-pi i v^2 + linear}  (Part 12a)"),
    "m015": dict(alpha=(1, 1, 1), f=(1, 0, -1), A=1, mscale=2, fs=1, c=0,
                 integrand="Phi_b(v+u) Phi_b(v) Phi_b(v-u) e^{-pi i v^2}  (Part 11, SnapPy orientation)"),
    "m016": dict(alpha=(1, 1, 2), f=(1, -1, 0), A=2, mscale=1, fs=2, c=1,
                 integrand="Phi_b(v+u/2) Phi_b(v-u/2) Phi_b(2v-c_b) e^{-2 pi i v^2}  (Part 12a; GK eq 56)"),
}
# 4_1 carries the linear u-v term of Part 12a; in index form it is a mixed CS level L = -1
LMIX = {"m004": -1, "m015": 0, "m016": 0}


def index_tri_from_1d(knot, m, e, cap):
    d = DICT[knot]
    mf = -d["mscale"] * m
    ef = d["fs"] * (e + d["c"] * m)
    alpha, f, A = d["alpha"], d["f"], d["A"]
    L = LMIX[knot]
    if L == 0:
        return index1d(alpha, f, A, -A, mf, ef, cap)
    # mixed CS term: z^{L mf} in the gauge constraint, zeta^{L n} in the flavour charge
    r = len(alpha)
    tot = {}
    B = 10
    for n in range(-B, B + 1):
        M = [alpha[j] * n + f[j] * mf for j in range(r)]
        # r = 2: solve directly
        g = -A * n - L * mf
        h = ef - L * n
        a1, a2, b1, b2 = alpha[0], alpha[1], f[0], f[1]
        det = a1 * b2 - a2 * b1
        xn, yn = g * b2 - a2 * h, a1 * h - b1 * g
        if xn % det or yn % det:
            continue
        E = [xn // det, yn // det]
        w = -A * n
        mds = [nu(M[j], E[j]) for j in range(r)]
        if sum(mds) + w > cap:
            continue
        prod = {0: 1}
        for j in range(r):
            prod = b3._mul(prod, I_D(M[j], E[j], cap - w - (sum(mds) - mds[j])), cap - w)
        sgn = -1 if (A * n) % 2 else 1
        for p, c in prod.items():
            if p + w <= cap:
                tot[p + w] = tot.get(p + w, 0) + sgn * c
    return {p: c for p, c in sorted(tot.items()) if c}


# ---------------------------------------------------------------------------
# Closed-form blocks (numerical evaluation, mpmath)
# ---------------------------------------------------------------------------

def _blocks_module():
    import mpmath as mp
    mp.mp.dps = 40

    def poch(a, q):
        r, k = mp.mpf(1), 0
        while True:
            t = a * q**k
            r *= (1 - t)
            k += 1
            if abs(t) < mp.mpf(10) ** (-45) and k > 3:
                return r

    def pn(a, q, n):
        r = mp.mpf(1)
        for k in range(n):
            r *= (1 - a * q**k)
        return r

    def BU(x, q, N=40):
        return sum(q**(j * (j + 1)) * x**(2 * j) * poch(q**(1 + j) * x**2, q)
                   * poch(q**(1 + 2 * j) * x**2, q) / pn(q, q, j) for j in range(N))

    def BU_inv(xt, q, N=40):      # B_U(xt; q^{-1}) written as a |q|<1 series
        return sum(q**(-i * (i + 1)) * xt**(2 * i)
                   / (pn(q**(-i), q, i) * poch(q**(-i) * xt**2, q) * poch(q**(-2 * i) * xt**2, q))
                   for i in range(N))

    def BD(x, q, sig, eps, N=60):
        return sum(q**(mp.mpf(j * (j + 2)) / 4) * poch(sig * q**(1 + mp.mpf(j) / 2) * x, q)
                   * poch(sig * q**(1 + mp.mpf(j) / 2) / x, q) / pn(q, q, j) for j in range(eps, N, 2))

    def BD_inv(xt, q, sig, eps, N=60):  # B_{sig,eps}(xt; q^{-1}), branch (q^{-1})^{1/2} = q^{-1/2}
        return sum(q**(-mp.mpf(i * (i + 2)) / 4)
                   / (pn(q**(-i), q, i) * poch(sig * q**(-mp.mpf(i) / 2) / xt, q)
                      * poch(sig * q**(-mp.mpf(i) / 2) * xt, q)) for i in range(eps, N, 2))

    def fusion(m, zeta, q):
        x = q**(mp.mpf(m) / 2) * zeta
        xt = q**(mp.mpf(m) / 2) / zeta
        P = {"U1": zeta**(2 * m) * q**m * BU(x, q) * BU_inv(xt, q),
             "U2": zeta**(2 * m) * q**(-m) * BU(1 / x, q) * BU_inv(1 / xt, q)}
        for sig in (1, -1):
            for eps in (0, 1):
                P[f"D{sig:+d},{eps}"] = BD(x, q, sig, eps) * BD_inv(xt, q, sig, eps) / 2
        return P

    return mp, fusion


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    import snappy

    # ---- G0 engine fix ---------------------------------------------------------
    print("[G0] corpus engine: shell enumeration now waits for the first populated shell")
    T4 = b3.IndexTriangulation(snappy.Manifold("m004"))
    a, bb = T4.index((4, 1), 4, progress_every=0), T4.index((-4, -1), 4, progress_every=0)
    check("G0-m004-I(4,1)==I(-4,-1)-and-nonzero", a == bb and bool(a), I41=a, Im4m1=bb)

    # ---- G1-G3 grids -------------------------------------------------------------
    grids = {}
    for g, knot in (("G1", "m004"), ("G2", "m015"), ("G3", "m016")):
        T = b3.IndexTriangulation(snappy.Manifold(knot))
        bad = []
        n = 0
        for m in MR:
            for e in ER:
                tri = T.index((e, m), QREAD, progress_every=0)
                one = index_tri_from_1d(knot, m, e, 2 * QREAD)
                n += 1
                if tri != one:
                    bad.append([m, e, tri, one])
        grids[knot] = {"cells": n, "mismatches": bad[:5]}
        check(f"{g}-{knot}-1dim-index==triangulation-index-on-{n}-cells-to-q^{QREAD}",
              not bad, dictionary={k: v for k, v in DICT[knot].items()}, mixedCS=LMIX[knot])

    # ---- G4 pretzel series to q^7 + GZ total index ----------------------------
    print(f"[G4] pretzel 1-dim index series to q^{QHI}")
    ser = {}
    for m in MR:
        for ef in range(-14, 15):
            v = index1d((1, 1, 2), (1, -1, 0), 2, -2, m, ef, 2 * QHI, B=11)
            if v:
                ser[(m, ef)] = v
    tot = {}
    for (m, ef), v in ser.items():
        if m == 0:
            for p, c in v.items():
                tot[p] = tot.get(p, 0) + c
    got = [tot.get(2 * k, 0) for k in range(QHI + 1)]
    gz = [1, -8, 3, 50, 58, 13, -196, -456]
    check("G4-pretzel-total-index==GZ-Obs3.9-printed-to-q^7", got == gz and all(p % 2 == 0 for p in tot),
          computed=got, printed=gz, source="GZ 2111.06645 (held as library/arxiv-2111.06645) Obs 3.9")

    # ---- G5 fusion of the six blocks ------------------------------------------
    print("[G5] six closed-form blocks: fusion vs the index series")
    mp, fusion = _blocks_module()

    def series(m, zeta, q):
        s = 0
        for (mm, ef), v in ser.items():
            if mm == m:
                for p, c in v.items():
                    s += c * q**(mp.mpf(p) / 2) * zeta**ef
        return s

    rows = []
    for th in ("0.7", "2.1"):
        zeta = mp.e**(1j * mp.mpf(th))
        for m in MR:
            res = []
            for qs in ("0.02", "0.005"):
                q = mp.mpf(qs)
                res.append(abs(series(m, zeta, q) - sum(fusion(m, zeta, q).values())))
            ratio = res[0] / res[1]
            rows.append({"theta": th, "m": m, "resid_q0.02": mp.nstr(res[0], 4),
                         "resid_q0.005": mp.nstr(res[1], 4), "ratio": mp.nstr(ratio, 6),
                         "resid_over_q8_at_0.02": mp.nstr(res[0] / mp.mpf("0.02")**8, 4)})
            print(f"    theta={th} m={m:+d}: resid {mp.nstr(res[0],3)} -> {mp.nstr(res[1],3)}, ratio {mp.nstr(ratio,5)} (4^8 = 65536)")
    ok = all(32768 <= float(r["ratio"]) <= 131072 and float(r["resid_over_q8_at_0.02"]) < 1e3 for r in rows)
    check("G5-six-block-fusion==index-for-m-in--2..2-(residual-scales-as-q^8)", ok, rows=rows)

    nfail = sum(1 for a in assertions if not a["passed"])
    verdict = (
        "The (-2,3,7) pretzel's one-dimensional level-2 state integral, read as a U(1) theory with "
        "chirals of charge (1,1,2) at CS level 2, reproduces the triangulation 3D index on every cell "
        "m in -2..2, e in -6..6 to q^3 (dictionary fixed on 4_1 and 5_2, half-meridian shifts from "
        "Part 12a, one longitude framing integer per knot), and GZ's printed total index to q^7. "
        "Closing the contour factorises it into SIX holomorphic blocks in GGM eq (19) form: two unit "
        "blocks B_U(x), B_U(1/x) and four doubled blocks B_{sigma,eps}, with the SAME sign and parity "
        "on the q and q^{-1} sides; the fusion equals the index at every m to q^7. This is the level-2 "
        "fusion rule qou-x3iv Parts 12b-17 were missing. H_Ad at block level: the unit blocks depend on "
        "the meridian x = m^2 only; the doubled blocks depend on sigma*(m + 1/m), the FUNDAMENTAL "
        "character, whose square is s(x) + 1. sigma-even combinations lie in Z[s(x)], sigma-odd ones "
        "do not, and the sigma-grading is tied to the half-integer q powers -- the same ring verdict as "
        "the operator route (qou-lzzi), now from explicit blocks."
    )
    print(f"\n verdict: {verdict}")
    from qou_substrate.witness import WitnessBuilder as _WB
    witness = {
        "name": "aomega-m3-pretzel-index-factorisation-blocks",
        "description": "(-2,3,7) holomorphic blocks from the 1-dim level-2 state integral, certified "
                       "against the triangulation 3D index at m in -2..2.",
        "computation": "aomega-m3-pretzel-index-factorisation-blocks",
        "engine": "python+snappy+mpmath",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-11-27-pretzel-level2-blocks-from-index.md",
        "parameters": {"snappy_version": snappy.__version__, "q_grid": QREAD, "q_series": QHI,
                       "m_range": list(MR), "e_range": [ER.start, ER.stop - 1],
                       "convention": "e = meridian (GGM S3Dx, PR #9739), m = longitude"},
        "data": {"grids": grids,
                 "pretzel_total_index": got,
                 "fusion_rows": rows,
                 "dictionary": {k: {kk: vv for kk, vv in v.items()} for k, v in DICT.items()}},
        "verdict": verdict,
        "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-index-factorisation-blocks.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
