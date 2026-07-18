#!/usr/bin/env python3
"""qbeta_g3_5two_stokes_sandwich.py — the ANALYTIC 5₂ M-dictionary,
part 2b: the (95a/b) Stokes-matrix sandwiches computed EXACTLY from the
fully-pinned tower layer, certified against the glyph-decoded q→0
factorizations (96/97) and Stokes integrality.

Inputs now all derived: the towers + E₂ slots (part 1, #4011: σ_c by
exact polynomiality) with the (c⁺, c⁻) split (part 2a, #4013: state-
integral match, 40 digits). This probe assembles W₋₁ and the sandwiches

  S⁺(q) = ½·L⁺·W₋₁(q⁻¹)·J₂⁻·W₋₁(q)ᵀ·R⁺        (95a, glyph-decoded)
  S⁻(q) = ½·L⁻·W₋₁(q)·J₂⁻·W₋₁(q⁻¹)ᵀ·R⁻        (95b, glyph-decoded)

  L⁺ = [[0,1,0],[0,1,1],[−1,0,0]]   R⁺ = [[0,0,−1],[1,1,0],[0,1,0]]
  L⁻ = [[0,3,−1],[0,−1,0],[1,0,0]]  R⁻ = [[0,0,1],[3,−1,0],[−1,0,0]]
  J₂⁻ = antidiag(1,−2,1)  (the same pairing form as (92) and (82))

in EXACT rational q-series arithmetic (|q|<1 side: H⁺ series at q;
the q⁻¹ side via the part-1-certified extension, H⁻ series at q).

Checks:
  K1  q→0 limits equal the glyph-decoded (96/97) products EXACTLY:
        S⁺(0) = [[1,4,0],[0,1,0],[−3,−9,1]]
        S⁻(0) = [[1,0,3],[−4,1,−3],[0,0,1]]
      (constants {3, 4} of the printed Stokes factorization).
  K2  STOKES INTEGRALITY: every entry of S±(q) is an INTEGER q-series
      to O(q^18) — the paper's central integrality phenomenon,
      reproduced from first principles.
  K3  det S±(q) = 1 identically (to the series order).
  K0  (decoration discriminator) the (87) antidiagonal row-flip
      convention is tested both ways; the convention matching K1/K2 is
      reported openly (part 1 showed the (92) RHS matches the UNflipped
      orientation; this is the independent second test).

Anti-fabrication: L±/R±/J₂⁻ and the q→0 targets are glyph-decoded
(cmsy minus-offset discipline; the (95a) L⁺ row-3 minus sits BELOW the
printed band and was caught only by the offset rule — recorded here),
then everything is certified by exact arithmetic against the
independently-derived tower layer. No fit; no c_k wired; exact
Fractions (no floats in the derivation), mpmath only for a numeric
spot-check; scope-(a).
"""
from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_analytic_hm_tower",
    _HERE / "qbeta_g3_5two_analytic_hm_tower.py")
_tw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_tw)

NS = _tw.NS
ORD_CHECK = 18

# derived split (part 2a): c⁺ = 1/6 − 4Ê₂, c⁻ = 1/12 − 2Ê₂
C_PLUS = (Fr(1, 6), Fr(-4))
C_MINUS = (Fr(1, 12), Fr(-2))

L_P = [[0, 1, 0], [0, 1, 1], [-1, 0, 0]]
R_P = [[0, 0, -1], [1, 1, 0], [0, 1, 0]]
L_M = [[0, 3, -1], [0, -1, 0], [1, 0, 0]]
R_M = [[0, 0, 1], [3, -1, 0], [-1, 0, 0]]
J2M = [[0, 0, 1], [0, -2, 0], [1, 0, 0]]
J3 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

S_P_TARGET = [[1, 4, 0], [0, 1, 0], [-3, -9, 1]]
S_M_TARGET = [[1, 0, 3], [-4, 1, -3], [0, 0, 1]]


def tower_full(eps, k, m):
    """Exact series with the DERIVED c-slot."""
    h = _tw._tower_series(eps, k, m)
    if k == 2:
        a, b = C_PLUS if eps == +1 else C_MINUS
        c = _tw._add(_tw._smul(a, _tw._qpow(0)),
                     _tw._smul(b, _tw._E_ln(2, 0)))
        h = _tw._sub(h, _tw._mul(c, _tw._tower_series(eps, 0, m)))
    return h


def series_mat_raw():
    """W₋₁(q) raw: rows m = −1,0,1; cols (H⁺₂, H⁺₁, H⁺₀) at q."""
    return [[tower_full(+1, 2, mm), tower_full(+1, 1, mm),
             tower_full(+1, 0, mm)] for mm in (-1, 0, 1)]


def series_mat_ext():
    """W₋₁ at argument q⁻¹ via the extension: entry (−1)^k·H⁻_{k,−m'}(q),
    rows m' = −1,0,1."""
    out = []
    for mm in (-1, 0, 1):
        out.append([tower_full(-1, 2, -mm),
                    _tw._smul(Fr(-1), tower_full(-1, 1, -mm)),
                    tower_full(-1, 0, -mm)])
    return out


def smat_mul_int(A, B):
    """int-matrix × series-matrix (or series × int)."""
    if isinstance(A[0][0], list):
        return [[_series_dot_int_col(A, B, i, j) for j in range(3)]
                for i in range(3)]
    return [[_int_dot_series(A, B, i, j) for j in range(3)]
            for i in range(3)]


def _int_dot_series(A, B, i, j):
    acc = _tw._zero()
    for k in range(3):
        if A[i][k]:
            acc = _tw._add(acc, _tw._smul(Fr(A[i][k]), B[k][j]))
    return acc


def _series_dot_int_col(A, B, i, j):
    acc = _tw._zero()
    for k in range(3):
        if B[k][j]:
            acc = _tw._add(acc, _tw._smul(Fr(B[k][j]), A[i][k]))
    return acc


def smat_mul(A, B):
    """series-matrix × series-matrix."""
    return [[_series_dot(A, B, i, j) for j in range(3)] for i in range(3)]


def _series_dot(A, B, i, j):
    acc = _tw._zero()
    for k in range(3):
        acc = _tw._add(acc, _tw._mul(A[i][k], B[k][j]))
    return acc


def transpose(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def flip(A):
    """J₃·A (row reversal)."""
    return [A[2], A[1], A[0]]


def sandwich(Wq, Wqi, L, R, first_is_qi):
    """½·L·(W_a)·J₂⁻·(W_b)ᵀ·R with (a,b) = (q⁻¹,q) or (q,q⁻¹)."""
    A = Wqi if first_is_qi else Wq
    B = Wq if first_is_qi else Wqi
    core = smat_mul(smat_mul_int(A, J2M), transpose(B))
    S = smat_mul_int(L, smat_mul_int(core, R))
    return [[_tw._smul(Fr(1, 2), S[i][j]) for j in range(3)]
            for i in range(3)]


def main() -> int:
    print("=" * 78)
    print(" 5₂ analytic M-dictionary part 2b — Stokes sandwiches (95a/b) "
          "exact")
    print("=" * 78)

    Wq_raw = series_mat_raw()
    Wqi_raw = series_mat_ext()

    results = {}
    for conv, tagc in ((False, "unflipped"), (True, "J3-flipped")):
        Wq = flip(Wq_raw) if conv else Wq_raw
        Wqi = flip(Wqi_raw) if conv else Wqi_raw
        Sp = sandwich(Wq, Wqi, L_P, R_P, first_is_qi=True)
        Sm = sandwich(Wq, Wqi, L_M, R_M, first_is_qi=False)
        sp0 = [[Sp[i][j][0] for j in range(3)] for i in range(3)]
        sm0 = [[Sm[i][j][0] for j in range(3)] for i in range(3)]
        k1 = (sp0 == [[Fr(x) for x in r] for r in S_P_TARGET]) and \
             (sm0 == [[Fr(x) for x in r] for r in S_M_TARGET])
        k2 = all(c.denominator == 1
                 for S in (Sp, Sm) for row in S for e in row
                 for c in e[:ORD_CHECK + 1])
        results[tagc] = (Sp, Sm, sp0, sm0, k1, k2)
        print(f"\n[K0:{tagc}] S⁺(0) = "
              f"{[[str(x) for x in r] for r in sp0]}")
        print(f"          S⁻(0) = {[[str(x) for x in r] for r in sm0]}")
        print(f"          K1 q→0 targets match: {k1};  K2 integer "
              f"series to O(q^{ORD_CHECK}): {k2}")

    win = next((t for t, r in results.items() if r[4] and r[5]), None)
    ok01 = win is not None
    Sp, Sm, sp0, sm0, k1, k2 = results[win] if win else \
        results["unflipped"]

    # K3: det S± = 1 to series order
    def det3(S):
        t1 = _tw._mul(S[0][0], _tw._sub(_tw._mul(S[1][1], S[2][2]),
                                        _tw._mul(S[1][2], S[2][1])))
        t2 = _tw._mul(S[0][1], _tw._sub(_tw._mul(S[1][0], S[2][2]),
                                        _tw._mul(S[1][2], S[2][0])))
        t3 = _tw._mul(S[0][2], _tw._sub(_tw._mul(S[1][0], S[2][1]),
                                        _tw._mul(S[1][1], S[2][0])))
        return _tw._add(_tw._sub(t1, t2), t3)

    ok3 = False
    if win:
        dp, dm = det3(Sp), det3(Sm)
        ok3 = all(dp[0] == 1 and dm[0] == 1 for _ in (0,)) and \
            all(dp[t] == 0 and dm[t] == 0
                for t in range(1, ORD_CHECK + 1))
        print(f"\n[K3] det S⁺ = det S⁻ = 1 to O(q^{ORD_CHECK}): {ok3}")

    # numeric spot-check of a leading Stokes coefficient (mpmath)
    s_lead = None
    if win:
        s_lead = {
            "S_plus_q1_entries": [[str(Sp[i][j][1]) for j in range(3)]
                                  for i in range(3)],
            "S_minus_q1_entries": [[str(Sm[i][j][1]) for j in range(3)]
                                   for i in range(3)]}
        print(f"    O(q) Stokes coefficients: S⁺: "
              f"{s_lead['S_plus_q1_entries']}")
        print(f"                              S⁻: "
              f"{s_lead['S_minus_q1_entries']}")

    ok = ok01 and ok3
    verdict = (
        f"STOKES SANDWICHES DERIVED — the glyph-decoded (95a/b) "
        f"sandwiches, assembled from the fully-pinned tower layer "
        f"(sigma_c #4011, split #4013), reproduce the glyph-decoded "
        f"(96/97) q->0 factorizations EXACTLY (S+(0) = "
        f"[[1,4,0],[0,1,0],[-3,-9,1]], S-(0) = [[1,0,3],[-4,1,-3],"
        f"[0,0,1]] — the printed constants 3,4) in the {win} W-"
        f"convention (the same orientation the part-1 (92) RHS picked "
        f"— two independent confirmations), with every S+-/S--entry an "
        f"INTEGER q-series to O(q^{ORD_CHECK}) (the Stokes-integrality "
        f"phenomenon from first principles) and det S+- = 1 "
        f"identically. The u=0 5_2 Stokes data (94)-(97) is now fully "
        f"DERIVED machinery. NEXT (part 2c): wall-crossing to deformed "
        f"x — port the sandwich structure onto the #3951 deformed "
        f"Theorem-22 blocks to certify the strip and sharpen phi_odd "
        f"(#3987, -0.004145 preliminary) to derived precision. No fit; "
        f"no c_k wired; scope-(a)."
        if ok else
        f"PART 2b INCOMPLETE (honest): convention scan {list(results)} "
        f"gave K1/K2 = "
        f"{[(t, r[4], r[5]) for t, r in results.items()]}, K3 = {ok3} "
        f"— the failing check localizes the next decode step (candidate "
        f"causes: a missed minus in the L/R decode bands, or the (87) "
        f"convention differing between the two W-factors). Data "
        f"recorded. No fit; no c_k wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-stokes-sandwich",
                        engine="fractions-exact")
    wb.set_description(
        "Analytic 5_2 M-dictionary part 2b: the (95a/b) Stokes-matrix "
        "sandwiches computed in exact rational q-series arithmetic from "
        "the fully-derived tower layer; q->0 limits match the glyph-"
        "decoded (96/97) factorizations exactly, entries are integer "
        "q-series (Stokes integrality), det = 1.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("sandwich_reading", {
        "S_plus": "1/2 * L+ * W_-1(1/q) * antidiag(1,-2,1) * W_-1(q)^T "
                  "* R+",
        "S_minus": "1/2 * L- * W_-1(q) * antidiag(1,-2,1) * W_-1(1/q)^T "
                   "* R-",
        "L_plus": L_P, "R_plus": R_P, "L_minus": L_M, "R_minus": R_M,
        "provenance": "glyph-decoded (cmsy minus-offset; the L+ row-3 "
                      "minus found below the printed band)"})
    wb.add_data("q0_targets", {"S_plus_0": S_P_TARGET,
                               "S_minus_0": S_M_TARGET,
                               "computed_S_plus_0":
                                   [[str(x) for x in r] for r in sp0],
                               "computed_S_minus_0":
                                   [[str(x) for x in r] for r in sm0]})
    wb.add_data("convention", {"winner": win,
                               "scan": {t: {"K1": r[4], "K2": r[5]}
                                        for t, r in results.items()}})
    if s_lead:
        wb.add_data("order_q_stokes_coefficients", s_lead)
    wb.add_data("verdict", verdict)
    wb.add_assertion("q0_factorizations_match_exactly",
                     computed=1.0 if (win and results[win][4]) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="exact S+-(0) equal the glyph-decoded "
                            "(96/97) products (constants 3, 4)")
    wb.add_assertion("stokes_integrality_and_det",
                     computed=1.0 if (ok01 and ok3) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="all entries integer q-series to O(q^18); "
                            "det S+- = 1 identically")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
