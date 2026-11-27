#!/usr/bin/env python3
"""80-dps numbers for the nucleon split from the four-strand lepton reading.

Lean: ``QOU.Nuclear.NucleonSplitFourStrand`` (on the T^3 = 0 block N + P of V^{(x)4} of
``QOU.MassTheory.NeutronFourStrand``: explicit L = s3 s2 s1^2 s2 s3, L^-1 and A_{k4}^{+-1}; L commutes
with s1, s2; B_3-conjugation invariance of the sector traces of M.L; exact tr_N, tr_P of V^3.X;
trP(V^3 L)/trN(V^3 L) = q^2 S/Lambda and ratio(L^-1) = ratio(L)^-1). Pre-registration:
``computations/probes/nucleon_split_four_strand/PREREGISTRATION.md``. Audit:
``docs/audits/2026-11-27-nucleon-split-four-strand.md``. Beans ``qou-myts``, ``qou-99qc``.

Gibbs map (route 1, ``NucleonSplitGibbsCoulomb``, no Coulomb term):
    m_n - m_p = E0 * log(tau_p / tau_n),  E0 = k_B T_q (qbeta_e0.order_zero).
Pre-registered headline: S1-closed (same four-strand block, K^{(x)4} = 1, [2]^4 on both), word
V^3 . L, ratio tr_P(V^3 L)/tr_N(V^3 L). Other variants are printed unselected. A ratio <= 0 is
reported as "log undefined". CODATA enters only the gap column and selects nothing.

Exact arithmetic: the 6x6 block is rebuilt from the Jimbo R-matrix on the full 16-dim V^{(x)4}
over Fraction, checked against the Lean block matrices, the Lean closed forms and L = D4^2 D3^-2
at rational test points; then evaluated in mpmath at q0.

Run:  python3 -u computations/probes/nucleon_split_four_strand_probe.py
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

DPS = 80
M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
M_P_EXP = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
M_N_EXP = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
DM_NP_EXP = M_N_EXP - M_P_EXP          # comparison only

N_BASIS = ("uddu", "dudu", "dduu")     # N = n (x) nu
P_BASIS = ("uudd", "udud", "duud")     # P = p (x) e
BLOCK = N_BASIS + P_BASIS


# --- generic small matrix algebra (works over Fraction and mpf) ------------------------------
def mm(a, b):
    n, k, m = len(a), len(b), len(b[0])
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def eye(n, one=1):
    return [[one if i == j else 0 * one for j in range(n)] for i in range(n)]


def prod(mats, n=6, one=1):
    out = eye(n, one)
    for x in mats:
        out = mm(out, x)
    return out


def inv(a):
    n = len(a)
    m = [row[:] + eye(n, a[0][0] * 0 + 1)[i] for i, row in enumerate(a)]
    for c in range(n):
        p = next(r for r in range(c, n) if m[r][c] != 0)
        m[c], m[p] = m[p], m[c]
        pv = m[c][c]
        m[c] = [x / pv for x in m[c]]
        for r in range(n):
            if r != c and m[r][c] != 0:
                f = m[r][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [row[n:] for row in m]


def tr(a, idx):
    return sum(a[i][i] for i in idx)


# --- Jimbo R-matrix on V^{(x)4}, restricted to the T^3 = 0 block ------------------------------
def rcheck(q, a, b):
    """R(ab) as dict {(c,d): coeff}: R(uu)=q uu, R(dd)=q dd, R(ud)=du, R(du)=ud + h du."""
    h = q - 1 / q
    if a == b:
        return {(a, b): q}
    if (a, b) == ("u", "d"):
        return {("d", "u"): 1}
    return {("u", "d"): 1, ("d", "u"): h}


def sigma_block(q, k):
    """sigma_k (strands k, k+1, 1-based) on the 6-dim block, column convention M[out][in]."""
    idx = {s: i for i, s in enumerate(BLOCK)}
    M = [[0 * q for _ in range(6)] for _ in range(6)]
    for s in BLOCK:
        for (c, d), v in rcheck(q, s[k - 1], s[k]).items():
            t = s[:k - 1] + c + d + s[k + 1:]
            M[idx[t]][idx[s]] += v
    return M


def full_space_closed(q):
    """The 6 states are closed under sigma_1..3 on the full 16-dim space (T^3 conservation)."""
    states = ["".join(p) for p in itertools.product("ud", repeat=4)]
    blk = {s for s in states if s.count("u") == 2}
    return blk == set(BLOCK) and all(
        "".join(s[:k - 1] + c + d + s[k + 1:]) in blk
        for s in blk for k in (1, 2, 3) for (c, d) in rcheck(q, s[k - 1], s[k]))


def lean_blocks(q):
    """NeutronFourStrand.s1, s2, s3 as 6x6 (N first, P second)."""
    h = q - 1 / q
    z = 0 * q

    def fb(a, b, c, d):
        return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]
    Z = [[z] * 3 for _ in range(3)]
    A1 = [[q, z, z], [z, z, 1 + z], [z, 1 + z, h]]
    A2 = [[z, 1 + z, z], [1 + z, h, z], [z, z, q]]
    B1, B2 = A2, A1
    E = [[z, 1 + z, z], [z, z, 1 + z], [z, z, z]]
    Et = [list(r) for r in zip(*E)]
    s3 = fb([[h, z, z], [z, h, z], [z, z, q]], E, Et, [[q, z, z], [z, z, z], [z, z, z]])
    return fb(B1, Z, Z, A1), fb(B2, Z, Z, A2), s3


def gens(q):
    s1, s2, s3 = (sigma_block(q, k) for k in (1, 2, 3))
    return {"s1": s1, "s2": s2, "s3": s3, "s1Inv": inv(s1), "s2Inv": inv(s2), "s3Inv": inv(s3)}


WORDS = {   # name: (letters, description); X in beta = V^3 . X
    "1": ([], "spectator (null test)"),
    "s3": (["s3"], "single crossing (lepton not closed)"),
    "s3Inv": (["s3Inv"], "single crossing^-1 (lepton not closed)"),
    "A34p": (["s3", "s3"], "lepton loops quark 3"),
    "A34m": (["s3Inv", "s3Inv"], "lepton loops quark 3, mirror"),
    "A24p": (["s3", "s2", "s2", "s3Inv"], "lepton loops quark 2"),
    "A24m": (["s3", "s2Inv", "s2Inv", "s3Inv"], "lepton loops quark 2, mirror"),
    "A14p": (["s3", "s2", "s1", "s1", "s2Inv", "s3Inv"], "lepton loops quark 1"),
    "A14m": (["s3", "s2", "s1Inv", "s1Inv", "s2Inv", "s3Inv"], "lepton loops quark 1, mirror"),
    "Lp": (["s3", "s2", "s1", "s1", "s2", "s3"], "lepton loops whole nucleon (HEADLINE)"),
    "Lm": (["s3Inv", "s2Inv", "s1Inv", "s1Inv", "s2Inv", "s3Inv"], "lepton loops nucleon, mirror"),
}
PURE = {"1", "A34p", "A34m", "A24p", "A24m", "A14p", "A14m", "Lp", "Lm"}


def S(q): return q**12 - 3 * q**10 + 3 * q**8 - 5 * q**6 + 3 * q**4 - 3 * q**2 + 1
def LAM(q): return q**16 - 4 * q**14 + 6 * q**12 - 10 * q**10 + 11 * q**8 - 10 * q**6 + 6 * q**4 - 4 * q**2 + 1


# Lean closed forms (NucleonSplitFourStrand.trN_V3_*, trP_V3_*): (tr_N, tr_P)
def lean_closed(q):
    return {
        "1": (-S(q) / q**6, -S(q) / q**6),
        "Lp": (-LAM(q) / q**6, -S(q) / q**4),
        "Lm": (-S(q) / q**8, -LAM(q) / q**10),
        "A34p": (-(q**16 - 4*q**14 + 8*q**12 - 15*q**10 + 16*q**8 - 14*q**6 + 8*q**4 - 4*q**2 + 1) / q**8,
                 -(q**14 - 3*q**12 + 3*q**10 - 2*q**8 - 3*q**6 + 3*q**4 - 3*q**2 + 1) / q**6),
        "A34m": (-(q**12 - 4*q**10 + 7*q**8 - 10*q**6 + 6*q**4 - 4*q**2 + 1) / q**6,
                 -(q**4 - q**2 + 1) * (q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1) / q**8),
        "A24p": (-(q**4 - q**2 + 1) * (q**8 - 3*q**6 + 3*q**4 - 5*q**2 + 1) / q**4,
                 -(q**12 - 4*q**10 + 6*q**8 - 10*q**6 + 7*q**4 - 4*q**2 + 1) / q**6),
        "A24m": (-(q**14 - 3*q**12 + 3*q**10 - 3*q**8 - 2*q**6 + 3*q**4 - 3*q**2 + 1) / q**8,
                 -(q**16 - 4*q**14 + 8*q**12 - 14*q**10 + 16*q**8 - 15*q**6 + 8*q**4 - 4*q**2 + 1) / q**8),
        "s3": (-(q**3 - q**2 + 1) * (q**3 + q**2 - 1) * (q**8 - 3*q**6 + 2*q**4 - 2*q**2 + 1) / q**7,
               -q * (q**2 - 2) * (q**4 - q**2 + 1)),
        "s3Inv": (-(q**6 - 3*q**4 + 2*q**2 - 1) / q**3,
                  -(q**12 - 3*q**10 + 6*q**8 - 8*q**6 + 6*q**4 - 4*q**2 + 1) / q**7),
    } | {"A14p": None, "A14m": None}


def sector_traces(q):
    g = gens(q)
    V = mm(g["s1"], g["s2Inv"])
    V3 = prod([V, V, V], one=q**0)
    out = {}
    for name, (letters, _) in WORDS.items():
        X = prod([g[x] for x in letters], one=q**0)
        T = mm(V3, X)
        out[name] = (tr(T, range(3)), tr(T, range(3, 6)))
    trA = tr(V3, range(3, 6))
    return out, trA, g


def exact_checks():
    ok = True
    for q in (Fraction(3, 2), Fraction(111, 100), Fraction(7, 5)):
        ok &= full_space_closed(q)
        g = gens(q)
        ok &= all(g[k] == m for k, m in zip(("s1", "s2", "s3"), lean_blocks(q)))
        out, trA, g = sector_traces(q)
        lc = lean_closed(q)
        lc["A14p"], lc["A14m"] = lc["A24p"], lc["A24m"]     # Lean: same closed forms
        ok &= all(out[k] == lc[k] for k in WORDS)
        L = prod([g[x] for x in WORDS["Lp"][0]], one=q**0)
        ok &= mm(g["s1"], L) == mm(L, g["s1"]) and mm(g["s2"], L) == mm(L, g["s2"])
        D4 = prod([g["s1"], g["s2"], g["s3"]] * 4, one=q**0)
        D3 = prod([g["s1"], g["s2"]] * 3, one=q**0)
        ok &= D4 == mm(D3, L)                                   # L = D4^2 D3^-2
        ok &= all(L[i][j] == (q**2 if i == j else 0) for i in range(3, 6) for j in range(3, 6))
        rp = out["Lp"][1] / out["Lp"][0]
        rm = out["Lm"][1] / out["Lm"][0]
        ok &= rp == q**2 * S(q) / LAM(q) and rm == 1 / rp
    return ok


def variants(q, out, trA):
    """ratio tau_p/tau_n for each (trace variant, word)."""
    rows = []
    two = q + 1 / q
    for name, (letters, desc) in WORDS.items():
        trN, trP = out[name]
        r = trP / trN
        rows.append(("S1-closed", name, desc, r))
        rows.append(("S1-open", name, desc, q**2 * r))
        if name in PURE:
            rows.append(("S2a", name, desc, q * two * trA / trP))
            rows.append(("S2b", name, desc, q * trA / trP))
    return rows


def s(x, n=10):
    return "log undefined" if x is None else mp.nstr(x, n)


def main():
    wb = WitnessBuilder("nucleon-split-four-strand", engine="mpmath")
    wb.set_description(
        "80-dps Gibbs n-p split E0*log(tau_p/tau_n) for the four-strand lepton reading "
        "(QOU.Nuclear.NucleonSplitFourStrand): S1-closed/S1-open/S2a/S2b trace variants x lepton "
        "words; pre-registered headline S1-closed, V^3 . L (lepton loops the whole nucleon). "
        "CODATA enters only the gap column."
    )
    ok = exact_checks()
    print(f"exact block / closed-form / commutation / L = D4^2 D3^-2 / reciprocity checks "
          f"(Fraction): {'PASS' if ok else 'FAIL'}")
    wb.add_assertion("block_closed_forms_symmetry_exact", computed=bool(ok), expected=True)
    res = {}
    headline = {}
    for anchor, q0 in (("proton", mpf(q_at(DPS))), ("muon", mpf(q_muon_at(DPS)))):
        E = qbeta_e0.order_zero(q=q0, m_e=M_E)
        E_twr = qbeta_e0.canonical(q=q0, m_e=M_E)
        out, trA, _ = sector_traces(q0)
        rows = variants(q0, out, trA)
        w_ref = 1 - (q0 - 1 / q0) ** 2        # NeutronFourStrand.trP_w / trN_w (#8636 word alone)
        rows.append(("S1-closed", "w", "#8636 word s1 s3^-1 alone (reference)", w_ref))
        print(f"\n[{anchor}] q0 = {mp.nstr(q0, 20)}  E0(ord0) = {mp.nstr(E, 12)}  "
              f"E0(tower) = {mp.nstr(E_twr, 12)} MeV")
        print(f"  {'trace':<10}{'word':<7}{'tau_p/tau_n':>16}{'MeV ord0':>15}{'MeV tower':>15}"
              f"{'gap ord0':>15}  description")
        recs = []
        for var, name, desc, r in rows:
            if r > 0:
                a = mp.chop(E * mp.log(r), tol=mpf(10) ** -60)
                b = mp.chop(E_twr * mp.log(r), tol=mpf(10) ** -60)
                g = a - DM_NP_EXP
            else:
                a = b = g = None
            tag = "  <- HEADLINE" if (var, name) == ("S1-closed", "Lp") else ""
            print(f"  {var:<10}{name:<7}{mp.nstr(r, 10):>16} {s(a):>14} {s(b):>14} {s(g):>14}  "
                  f"{desc}{tag}")
            rec = {"trace": var, "word": name, "description": desc, "ratio": fmt(r),
                   "split_ord0": None if a is None else fmt(a),
                   "split_tower": None if b is None else fmt(b),
                   "gap_ord0": None if g is None else fmt(g), "ratio_positive": bool(r > 0)}
            recs.append(rec)
            if tag:
                headline[anchor] = rec
        hl_ok = abs(out["Lp"][1] / out["Lp"][0] - q0**2 * S(q0) / LAM(q0)) < mpf(10) ** -70
        wb.add_assertion(f"{anchor}_headline_closed_form", computed=bool(hl_ok), expected=True)
        ok &= bool(hl_ok)
        res[anchor] = {"q0": fmt(q0), "E0_ord0": fmt(E), "E0_tower": fmt(E_twr), "rows": recs}
    print(f"\nCODATA m_n - m_p = {mp.nstr(DM_NP_EXP, 10)} MeV (comparison only)")
    wb.add_data("lean_module", "QOU.Nuclear.NucleonSplitFourStrand")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("headline_preregistered",
                "S1-closed (K^{(x)4}=1, [2]^4 both sectors), beta = V^3 . L, L = s3 s2 s1^2 s2 s3")
    wb.add_data("headline", headline)
    wb.add_data("anchors", res)
    wb.add_data("codata_comparison_only", {"dm_np": fmt(DM_NP_EXP)})
    path = wb.save({"q0Anchor": "comparison"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
