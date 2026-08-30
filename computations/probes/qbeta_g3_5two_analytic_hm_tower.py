#!/usr/bin/env python3
"""qbeta_g3_5two_analytic_hm_tower.py — the ANALYTIC 5₂ M-dictionary,
part 1: the u=0 H^ε_{k,m} tower (GGM eqs 89a-c/90a-c) implemented from
the paper's scalar formulas and SELF-CERTIFIED OCR-free against the
machine-checkable Theorem-11 constraints.

Why this tranche: the dictionary-diagnostic (merged #4000) showed the
numerics lane is drift-limited — the remaining path to a derived-
precision φ_odd is the analytic M-dictionary. Its foundation is the
3×3 fundamental solution W_m(q) of the q-difference equation (86),
built from the towers

  H⁺_{k,m}(q) = Σ_n q^{n(n+1)+nm}/(q;q)ₙ³ · P_k(n,m;q)       (89a-c)
  H⁻_{k,m}(q) = Σ_n (−1)ⁿ q^{n(n+1)/2+nm}/(q;q)ₙ³ · P̃_k     (90a-c)

with P₁ = 1+2n+m−3E₁⁽ⁿ⁾, P₂ = P₁² − 3E₂⁽ⁿ⁾ − c⁺(q),
P̃₁ = ½+n+m−3E₁⁽ⁿ⁾, P̃₂ = P̃₁² − 3E₂⁽ⁿ⁾ − c⁻(q), and
E_l⁽ⁿ⁾(q) = Σ_s s^{l−1} q^{s(n+1)}/(1−q^s)  (eq 79).

OCR-free derivation discipline (the sandwich method at the tower
layer): the PDF text reflow scrambles signs, the E₂(q) constant slot
(printed "−1/6 − E₂" vs "−(1/6)E₂" ambiguous), the (87) assembly
decorations, and the (92) right-hand side (which carries a q^m
entry). Nothing is trusted from the reflow; instead:

  T1  branch recurrences: H⁺ satisfies (86)
        y_m − 3y_{m+1} + (3−q^{2+m})y_{m+2} − y_{m+3} = 0
      directly; H⁻ satisfies the EXTENSION recurrence (derived from
      H⁺_{k,m}(q⁻¹) = (−1)^k H⁻_{k,−m}(q)):
        z_j := H⁻_{k,−j}: z_0 − 3z_1 + (3−q^{−(2+m)})z_2 − z_3 = 0.
      The E₁ sign is pinned by the k=1 defect (unique below tol).
  T2  STRUCTURAL FACT (proved numerically): the k=2 constant slot
      c^ε(q) = a + b·Ê₂(q) enters as −c·H₀ (a column operation), so
      it is (86)-invisible AND det-invisible — only orthogonality
      can pin it.
  T3  EXACT DERIVATION of the c-slot and the (92) right-hand side by
      rational q-series arithmetic (Fractions — exact, no floats at
      all): a second structural fact makes it linear — every
      Theorem-11 bilinear pairs H⁺₂ with H⁻₀ and H⁺₀ with H⁻₂, so
      the two c-slots enter ONLY through their sum σ_c = c⁺ + c⁻ =
      A + B·Ê₂(q). Since the (92) entries must be Laurent
      POLYNOMIALS (the RHS is a constant matrix plus a q^m slot),
      every coefficient of q^t (t ≥ 2 at m = 1) vanishes — an exact
      overdetermined linear system that DERIVES (A, B) and, with
      them, the (92) RHS. Result: A = 1/4, B = −6, i.e.
      σ_c = 1/4 − 6·Ê₂ — exactly the printed reading
      "−(1/6)E₂(q)" / "−(1/12)E₂(q)" under the standard
      normalization E₂ = 1 − 24Ê₂ — and
        (1/2)·W_{m−1}(q)·J₂·W_{−m−1}(q⁻¹)ᵀ
          = [[1,0,0],[0,0,1],[0,1,3−q^m]]
      (J₂ = antidiag(1,2,1)), verified entrywise to O(q^24) at m = 1
      AND held-out m = 2. The individual split (c⁺, c⁻) is
      Theorem-11-INVISIBLE (only σ_c enters); the print-consistent
      split c⁺ = (1/6)E₂, c⁻ = (1/12)E₂ is recorded as the unique
      one matching both printed constants and the derived sum, with
      the split pin deferred to the (82) state-integral match
      (part 2).
  T4  numeric cross-check: the derived (92) identity evaluated with
      the independent mpmath tower implementation at a numeric q.

Anti-fabrication: the only printed inputs are the cleanly-extracted
scalar series formulas (89/90/79) and the constraint STATEMENTS
(86/91/92); every ambiguous glyph (E₁ sign, E₂ normalization and
constants, the (92) RHS including its q^m slot) is DERIVED by the
constraints in exact arithmetic. No fit; no c_k wired; mpmath dps 50
for the numeric legs, exact Fractions for T3, no float64; scope-(a).
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

TOL = mp.mpf("1e-38")

_POCH = {}
_ELN = {}
_TOW = {}


def qpoch3(q, n):
    key = (mp.nstr(q, 30), n)
    if key not in _POCH:
        p = mp.mpf(1) if mp.im(q) == 0 else mp.mpc(1)
        for j in range(1, n + 1):
            p *= (1 - q ** j)
        _POCH[key] = p ** 3
    return _POCH[key]


def E_ln(l, n, q):
    """E_l^(n)(q) = Σ_{s≥1} s^{l−1} q^{s(n+1)}/(1−q^s)   (eq 79)."""
    key = (l, n, mp.nstr(q, 30))
    if key in _ELN:
        return _ELN[key]
    acc = mp.mpf(0)
    s = 1
    while True:
        term = mp.mpf(s) ** (l - 1) * q ** (s * (n + 1)) / (1 - q ** s)
        acc += term
        if abs(term) < mp.mpf("1e-60") and s > 4:
            break
        s += 1
        if s > 4000:
            raise RuntimeError("E_ln did not converge")
    _ELN[key] = acc
    return acc


def E2hat(q):
    """Ê₂(q) = Σ_{s≥1} s·q^s/(1−q^s) (normalization-free weight-2 sum;
    its coefficient in the c-slot is scanned in T3)."""
    return E_ln(2, 0, q)


def tower(eps, k, m, q, s1=+1):
    """H^ε_{k,m}(q) per (89)/(90) with c-slot = 0; |q| < 1 required."""
    key = (eps, k, m, mp.nstr(q, 30), s1)
    if key in _TOW:
        return _TOW[key]
    acc = mp.mpf(0)
    n = 0
    while True:
        if eps == +1:
            w = q ** (n * (n + 1) + n * m) / qpoch3(q, n)
            base = 1 + 2 * n + m
        else:
            w = (-1) ** n * q ** (mp.mpf(n * (n + 1)) / 2 + n * m) \
                / qpoch3(q, n)
            base = mp.mpf(1) / 2 + n + m
        if k == 0:
            p = mp.mpf(1)
        elif k == 1:
            p = base - s1 * 3 * E_ln(1, n, q)
        else:
            p = (base - s1 * 3 * E_ln(1, n, q)) ** 2 - 3 * E_ln(2, n, q)
        acc += w * p
        if n > 6 and abs(w) < mp.mpf("1e-58"):
            break
        n += 1
        if n > 3000:
            raise RuntimeError("H series did not converge")
    _TOW[key] = acc
    return acc


def H_full(eps, k, m, q, s1, a, b):
    """Tower with the c-slot: H₂ − (a + b·Ê₂(q))·H₀ for k=2."""
    h = tower(eps, k, m, q, s1=s1)
    if k == 2:
        h = h - (a + b * E2hat(q)) * tower(eps, 0, m, q, s1=s1)
    return h


J2 = mp.matrix([[0, 0, 1], [0, 2, 0], [1, 0, 0]])


def W_raw(m, q, s1, a, b, eps):
    return mp.matrix([[H_full(eps, 2, mm, q, s1, a, b),
                       H_full(eps, 1, mm, q, s1, a, b),
                       H_full(eps, 0, mm, q, s1, a, b)]
                      for mm in (m, m + 1, m + 2)])


def W_ext(m, q, s1, a, b):
    """W_m(Q) for |Q| > 1 via the extension identity, evaluated at
    q = 1/Q (|q| < 1): entry H_{k,m'}(Q) = (−1)^k·H⁻_{k,−m'}(q)."""
    rows = []
    for mm in (m, m + 1, m + 2):
        rows.append([H_full(-1, 2, -mm, q, s1, a, b),
                     -H_full(-1, 1, -mm, q, s1, a, b),
                     H_full(-1, 0, -mm, q, s1, a, b)])
    return mp.matrix(rows)


# ---------- exact rational q-series arithmetic (T3; no floats) ----------
NS = 26


def _zero():
    return [Fr(0)] * (NS + 1)


def _add(x, y):
    return [u + v for u, v in zip(x, y)]


def _sub(x, y):
    return [u - v for u, v in zip(x, y)]


def _mul(x, y):
    z = _zero()
    for i, u in enumerate(x):
        if u == 0:
            continue
        for j, v in enumerate(y):
            if j > NS - i:
                break
            if v == 0:
                continue
            z[i + j] += u * v
    return z


def _smul(s, x):
    return [s * u for u in x]


def _qpow(k):
    z = _zero()
    if k <= NS:
        z[k] = Fr(1)
    return z


_PINV = {}


def _poch_inv3(n):
    if n not in _PINV:
        s = _qpow(0)
        for j in range(1, n + 1):
            inv = _zero()
            tt = 0
            while tt * j <= NS:
                inv[tt * j] = Fr(1)
                tt += 1
            s = _mul(s, _mul(inv, _mul(inv, inv)))
        _PINV[n] = s
    return _PINV[n]


def _E_ln(l, n):
    z = _zero()
    s = 1
    while s * (n + 1) <= NS:
        base = s * (n + 1)
        tt = 0
        while base + tt * s <= NS:
            z[base + tt * s] += Fr(s) ** (l - 1)
            tt += 1
        s += 1
    return z


def _tower_series(eps, k, m):
    """Exact q-series of the c-slot-free tower H^ε_{k,m}(q)."""
    z = _zero()
    n = 0
    while (n * (n + 1) + n * m if eps == +1
           else n * (n + 1) // 2 + n * m) <= NS:
        if eps == +1:
            w = _mul(_qpow(n * (n + 1) + n * m), _poch_inv3(n))
            base = Fr(1 + 2 * n + m)
        else:
            w = _smul(Fr((-1) ** n),
                      _mul(_qpow(n * (n + 1) // 2 + n * m), _poch_inv3(n)))
            base = Fr(1, 2) + n + m
        if k == 0:
            p = _qpow(0)
        elif k == 1:
            p = _sub(_smul(base, _qpow(0)), _smul(Fr(3), _E_ln(1, n)))
        else:
            p1 = _sub(_smul(base, _qpow(0)), _smul(Fr(3), _E_ln(1, n)))
            p = _sub(_mul(p1, p1), _smul(Fr(3), _E_ln(2, n)))
        z = _add(z, _mul(w, p))
        n += 1
    return z


def _M0_G(mi, mj):
    """Exact series of the (92) bilinear for A-row mi × B-row mj:
    M₀ (c-slot-free part), G = (1/2)H⁺₀H⁻₀, and Ê₂·G."""
    hp = [_tower_series(+1, k, mi) for k in range(3)]
    hm = [_tower_series(-1, k, -mj) for k in range(3)]
    t1 = _mul(hp[2], hm[0])
    t2 = _smul(Fr(-2), _mul(hp[1], hm[1]))
    t3 = _mul(hp[0], hm[2])
    M0 = _smul(Fr(1, 2), _add(_add(t1, t2), t3))
    G = _smul(Fr(1, 2), _mul(hp[0], hm[0]))
    EG = _mul(_E_ln(2, 0), G)
    return M0, G, EG


def main() -> int:
    print("=" * 78)
    print(" 5₂ analytic M-dictionary part 1 — u=0 H^ε_{k,m} tower, "
          "Theorem-11 certified")
    print("=" * 78)

    q1 = mp.mpf("0.13")
    q2 = mp.mpf("0.31")
    q3 = mp.mpf("0.22")

    # T1: branch recurrences + E₁ sign pin
    print("\n[T1] branch recurrences ((86) for H⁺; extension recurrence "
          "for H⁻):")
    defs = {}
    for s1 in (+1, -1):
        worst_p = mp.mpf(0)
        worst_m = mp.mpf(0)
        for k in (0, 1, 2):
            for q in (q1, q2):
                ys = [tower(+1, k, mm, q, s1=s1) for mm in range(4)]
                d = ys[0] - 3 * ys[1] + (3 - q ** 2) * ys[2] - ys[3]
                worst_p = max(worst_p, abs(d) / max(abs(y) for y in ys))
                zs = [tower(-1, k, -j, q, s1=s1) for j in range(4)]
                d = zs[0] - 3 * zs[1] + (3 - q ** -2) * zs[2] - zs[3]
                worst_m = max(worst_m, abs(d) / max(abs(z) for z in zs))
        defs[s1] = (worst_p, worst_m)
        print(f"    s1 = {s1:+d}: H⁺ (86) defect {mp.nstr(worst_p, 4)}; "
              f"H⁻ extension defect {mp.nstr(worst_m, 4)}")
    s1_star = +1 if max(defs[+1]) < max(defs[-1]) else -1
    ok1 = max(defs[s1_star]) < TOL and max(defs[-s1_star]) > mp.mpf("1e-6")
    print(f"    pinned: s1 = {s1_star:+d} (unique below tol); both "
          f"branches certified: {ok1}")
    print("    (the H⁻ extension recurrence itself certifies the (80)-"
          "type relation H⁺_{k,m}(q⁻¹) = (−1)^k H⁻_{k,−m}(q) "
          "structurally)")

    # T2: structural invisibility of the c-slot
    print("\n[T2] c-slot invisibility (structural):")
    ys = [H_full(+1, 2, mm, q1, s1_star, mp.mpf(7) / 3, mp.mpf(2))
          for mm in range(4)]
    d_c = abs(ys[0] - 3 * ys[1] + (3 - q1 ** 2) * ys[2] - ys[3]) \
        / max(abs(y) for y in ys)
    det0 = mp.det(W_raw(0, q1, s1_star, mp.mpf(0), mp.mpf(0), +1))
    detc = mp.det(W_raw(0, q1, s1_star, mp.mpf(7) / 3, mp.mpf(2), +1))
    ok2 = d_c < TOL and abs(det0 - detc) < mp.mpf("1e-40")
    print(f"    (86) defect at c = 7/3 + 2·Ê₂: {mp.nstr(d_c, 4)}; "
          f"det shift {mp.nstr(abs(det0 - detc), 4)} → invisible: {ok2}")

    # T3: EXACT derivation of the c-slot sum + the (92) RHS (Fractions)
    print("\n[T3] exact-series derivation of σ_c = c⁺+c⁻ and the (92) "
          "RHS (rational arithmetic, O(q^24)):")
    rowsA1, rowsB1 = [0, 1, 2], [-2, -1, 0]          # m = 1
    M0, G, EG = _M0_G(rowsA1[0], rowsB1[0])
    det2 = G[2] * EG[3] - EG[2] * G[3]
    A_c = (M0[2] * EG[3] - M0[3] * EG[2]) / det2
    B_c = (G[2] * M0[3] - G[3] * M0[2]) / det2
    print(f"    solved: σ_c = {A_c} + ({B_c})·Ê₂(q)")
    exp_pin = (A_c == Fr(1, 4) and B_c == Fr(-6))
    Cm = [[None] * 3 for _ in range(3)]
    Dm = [[None] * 3 for _ in range(3)]
    poly_ok = True
    for i, mi in enumerate(rowsA1):
        for j, mj in enumerate(rowsB1):
            M0, G, EG = _M0_G(mi, mj)
            ent = [M0[t] - A_c * G[t] - B_c * EG[t] for t in range(NS + 1)]
            if any(ent[t] != 0 for t in range(2, NS - 1)):
                poly_ok = False
            Cm[i][j] = ent[0]
            Dm[i][j] = ent[1]
    int_ok = all(x.denominator == 1 for r in Cm + Dm for x in r)
    # held-out m = 2: same σ_c, model C + D·q²
    ho_ok = True
    for i, mi in enumerate([1, 2, 3]):
        for j, mj in enumerate([-3, -2, -1]):
            M0, G, EG = _M0_G(mi, mj)
            ent = [M0[t] - A_c * G[t] - B_c * EG[t] for t in range(NS + 1)]
            if ent[1] != 0 or any(ent[t] != 0 for t in range(3, NS - 1)):
                ho_ok = False
            if not (ent[0] == Cm[i][j] and ent[2] == Dm[i][j]):
                ho_ok = False
    ok3 = exp_pin and poly_ok and int_ok and ho_ok
    CmI = [[int(x) for x in r] for r in Cm]
    DmI = [[int(x) for x in r] for r in Dm]
    print(f"    all 9 entries Laurent-POLYNOMIAL to O(q^24): {poly_ok}; "
          f"integer RHS: {int_ok}")
    print(f"    DERIVED (92) RHS = C + q^m·D with C = {CmI}, D = {DmI}")
    print(f"    held-out m = 2 (same σ_c, q^m slot moves to q²): {ho_ok}")
    print("    ⇒ σ_c = 1/4 − 6·Ê₂ ≡ (1/6)E₂ + (1/12)E₂ with the standard "
          "E₂ = 1 − 24Ê₂ — the printed '−(1/6)E₂', '−(1/12)E₂' reading "
          "DERIVED; the (c⁺, c⁻) split is Theorem-11-invisible (only "
          "σ_c enters every bilinear) — split pin deferred to the (82) "
          "state-integral match (part 2).")

    # T4: numeric cross-check of the derived identity (independent
    # mpmath implementation; print-consistent split, any split works)
    a_p, b_p = mp.mpf(1) / 6, mp.mpf(-4)      # c⁺ = (1/6)E₂
    a_m, b_m = mp.mpf(1) / 12, mp.mpf(-2)     # c⁻ = (1/12)E₂
    A = mp.matrix([[H_full(+1, 2, mm, q3, s1_star, a_p, b_p),
                    H_full(+1, 1, mm, q3, s1_star, a_p, b_p),
                    H_full(+1, 0, mm, q3, s1_star, a_p, b_p)]
                   for mm in (0, 1, 2)])
    B = W_ext(-2, q3, s1_star, a_m, b_m)
    M = (A * J2 * B.T) / 2
    R = mp.matrix([[CmI[i][j] + DmI[i][j] * q3 for j in range(3)]
                   for i in range(3)])
    dev4 = max(abs(M[i, j] - R[i, j]) for i in range(3) for j in range(3))
    ok4 = dev4 < mp.mpf("1e-40")
    print(f"\n[T4] numeric cross-check at q = {mp.nstr(q3, 4)}: max "
          f"entry deviation from derived RHS = {mp.nstr(dev4, 4)}: {ok4}")

    ok = ok1 and ok2 and ok3 and ok4
    verdict = (
        f"ANALYTIC M-DICTIONARY PART 1 — the u=0 5_2 tower layer derived "
        f"and certified OCR-free: (T1) H+ satisfies the (86) q-difference "
        f"recurrence and H- its q->q^-1 extension recurrence to <1e-38 "
        f"(defect >1e-6 under the E1-sign flip; s1 = {s1_star:+d} pinned; "
        f"the extension identity thereby structurally certified); (T2) "
        f"the k=2 constant slot is proven (86)- and det-invisible "
        f"(column operation), so orthogonality is its only pin; (T3) "
        f"EXACT rational-series derivation: every Theorem-11 bilinear "
        f"carries only the SUM sigma_c = c+ + c-, and (92)-polynomiality "
        f"DERIVES sigma_c = 1/4 - 6*E2hat — identically the printed "
        f"-(1/6)E2 / -(1/12)E2 reading with standard E2 = 1 - 24*E2hat — "
        f"and the (92) RHS = [[1,0,0],[0,0,1],[0,1,3-q^m]], all entries "
        f"exact Laurent polynomials to O(q^24), held-out m=2 verified "
        f"(q^m slot moves correctly); the (c+, c-) split is Theorem-11-"
        f"invisible and its pin is deferred honestly to the (82) state-"
        f"integral match; (T4) independent mpmath implementation "
        f"reproduces the derived identity to {mp.nstr(dev4, 3)}. "
        f"Foundation set for part 2: the W_-1-based (94)-(95) M/S "
        f"sandwiches vs the q->0 targets (96/97, constants 3,4), then "
        f"wall-crossing to deformed x for the derived phi_odd. No fit; "
        f"no c_k wired; scope-(a)."
        if ok else
        f"PART 1 INCOMPLETE (honest): T1={ok1} T2={ok2} T3={ok3} "
        f"T4={ok4} — the failing constraint localizes the next "
        f"derivation step; stage prints carry the data. No fit; no c_k "
        f"wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-analytic-hm-tower",
                        engine="mpmath+fractions")
    wb.set_description(
        "Analytic 5_2 M-dictionary part 1: the u=0 H^eps_{k,m} tower "
        "(GGM 89/90, E-series eq 79) implemented and self-certified "
        "OCR-free against Theorem 11 — branch recurrences pin the E1 "
        "sign and certify the eps-extension identity; exact rational "
        "q-series arithmetic derives the c-slot sum sigma_c = 1/4 - "
        "6*E2hat and the (92) RHS [[1,0,0],[0,0,1],[0,1,3-q^m]] from "
        "polynomiality alone; independent mpmath cross-check.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("t1_recurrences", {
        "pinned_s1": int(s1_star),
        "defects": {f"s1={s}": [mp.nstr(defs[s][0], 8),
                                mp.nstr(defs[s][1], 8)]
                    for s in (+1, -1)}})
    wb.add_data("t2_structural", {"rec_defect_with_c": mp.nstr(d_c, 8),
                                  "det_shift": mp.nstr(abs(det0 - detc), 8)})
    wb.add_data("t3_exact_derivation", {
        "sigma_c_const": str(A_c), "sigma_c_E2hat_coef": str(B_c),
        "matches_printed_reading": bool(exp_pin),
        "rhs_C": CmI, "rhs_D_qm": DmI,
        "all_entries_polynomial": bool(poly_ok),
        "held_out_m2": bool(ho_ok),
        "split_note": "only c+ + c- enters Theorem-11 bilinears; the "
                      "split (1/6)E2 vs (1/12)E2 is print-consistent, "
                      "pinned in part 2 via the (82) state integral"})
    wb.add_data("t4_numeric_crosscheck", {"q": mp.nstr(q3, 8),
                                          "max_dev": mp.nstr(dev4, 8)})
    wb.add_data("verdict", verdict)
    wb.add_assertion("branch_recurrences_certified",
                     computed=1.0 if ok1 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="(86) + extension recurrence < 1e-38 at 2 q "
                            "x 3 k x both branches; E1-sign flip breaks "
                            "at > 1e-6")
    wb.add_assertion("c_slot_invisibility_structural",
                     computed=1.0 if ok2 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="c*H0 column addition preserves (86) and "
                            "det — orthogonality is the only pin")
    wb.add_assertion("sigma_c_and_92_rhs_derived_exactly",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="exact Fractions: sigma_c = 1/4 - 6*E2hat "
                            "solved from polynomiality, all 9 entries "
                            "polynomial to O(q^24), held-out m verified")
    wb.add_assertion("numeric_crosscheck_matches",
                     computed=1.0 if ok4 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="independent mpmath towers reproduce the "
                            "derived (92) identity to < 1e-40")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
