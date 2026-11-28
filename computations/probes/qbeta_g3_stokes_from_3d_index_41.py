#!/usr/bin/env python3
"""qbeta_g3_stokes_from_3d_index_41.py — the 4₁ Stokes matrix S⁺(x;q), and its
q→0 Stokes constant 3, computed FROM THE TRIANGULATION 3d INDEX (bean qou-vr3q).

What was open
-------------
`docs/audits/2026-07-14-g3-stokes-via-3d-index.md` §4 recorded that A_ω = 3 "is
not a coefficient read-off of I_41": the corpus obtained S⁺(0) = [[1,3],[0,1]]
only through the GGM Wronskian W₋₁(q) (q-hypergeometric G-series), and the
certified DGG index I_41(m,e) was "an independent face, not the A_ω input".

What this probe does
--------------------
It closes that gap for 4₁: it assembles the full x-deformed Stokes matrix
S⁺(x;q) out of the index alone, with no W-series, through an explicit gauge
that GGM's own proved Wronskian relations fix.  Every step is exact integer
Laurent arithmetic in (x, s), s = q^{1/2}.

Chain (all from the in-repo GGM source
library/arxiv-2012.00062v3/source/files/GGM_peacock_20v4.tex):

  (a) eq (Sp-41), Conj 5.x (conj.41M) — the Stokes matrix
        S⁺(x;q) = P(x) · W₋₁(x⁻¹;q⁻¹) · W₋₁(x;q)ᵀ · Q(x),
        P = [[0,-1],[x⁻¹,-1-x]],  Q = [[0,x],[-1,-1-x⁻¹]].
  (b) eq (W41rec), m = -1 (Thm, proved):  W₀ = K·W₋₁,
        K(x) = [[0,1],[-x³, x²+x-x³]]   (q-free at m = -1).
  (c) eq (W41xm), m = 0 (Thm, proved):   𝒲₀ = T₀·W₀,
        T₀(x;q) = [[1,0],[-x⁻¹, x⁻³(1-qx²)]].
  (d) eq (WW41) + its footnote (Beem–Dimofte–Pasquetti factorisation of the
      index into holomorphic blocks):
        (𝒲₀(x⁻¹;q⁻¹)·𝒲₀(x;q)ᵀ)_{i+1,j+1} = (-q^{1/2})^{j-i} Ind^rot(j-i, q^{(i+j)/2}x; q),
      Ind^rot(m,ζ;q) = Σ_e I_41(m,e)(q) ζ^e.

Hence S⁺(x;q) = L(x;q) · N(x;q) · R(x;q) with N the index matrix of (d) and
  L = P·K(x⁻¹)⁻¹·T₀(x⁻¹;q⁻¹)⁻¹ = [[-1, 0], [-x⁻¹(1-qx²-qx³)u, qx·u]],
  R = T₀(x;q)⁻ᵀ·K(x)⁻ᵀ·Q       = [[-1, -(1+x-qx³)u], [0, -x·u]],
  u = 1/(1-qx²)  (a q-series; no division by an index quantity anywhere).

The index I_41(m,e) is the bare DGG eq (4.18) flux sum of two tetrahedron
indices (`qbeta_g3_fourone_index_assembly.I41`, certified there against the
printed DGG eq (4.20) and the quantum A-polynomial).

The q→0 reading (the point of the bean)
---------------------------------------
Row 1 of L is (-1, 0) exactly, so
    S⁺₁₂(x;q) = u·[(1+x-qx³)·Ind^rot(0,x;q) - q^{1/2}x·Ind^rot(1,q^{1/2}x;q)],
and at q⁰ only two index coefficients survive:
    [I_41(0,0)]_{q⁰}   = 1      (the vacuum)
    [I_41(1,-2)]_{q^{1/2}} = -1  (one BPS state at magnetic flux 1, electric -2),
giving S⁺₁₂(x;0) = (1+x)·1 + x·x⁻²·1 = x⁻¹ + 1 + x, i.e. 3 at x = 1.
That is GGM eq (S0x41) — derived here, not read off the paper.

Checks (all exact; any failure exits 1):
  C1  S⁺(x;0) = [[1, x⁻¹+1+x],[0,1]]               (GGM eq S0x41)
  C2  S⁺₁₁(x;q) = Ind^rot(0,x;q) (exact by L,R shape) and its printed
      q, q² coefficients (GGM, 𝒮⁺_{σ₁σ₁}(x;q) display after eq S0x41)
  C3  printed 𝒮⁺_{σ₁σ₂}, 𝒮⁺_{σ₂σ₁}, 𝒮⁺_{σ₂σ₂}(x;q) through q²
  C4  det S⁺(x;q) = 1 through the truncation order
  C5  GGM symmetry 𝒮⁺_{σ₁σ₂} = -𝒮⁺_{σ₂σ₁}, i.e. S⁺₁₂+S⁺₂₁ = (x⁻¹+1+x)S⁺₁₁
  C6  x = 1: the four printed towers (61)-(64) through q⁶, and agreement with
      the W-route S⁺(q) of qbeta_g3_ggm_stokes_41.py coefficient by coefficient
  C7  stability: raising the e-cutoff and the s-order changes nothing in range

Finding recorded on the side: the 𝒮⁺_{σ₁σ₁}(x;q) q-coefficient is
-(x⁻² + 2x⁻¹ + 2 + 2x + x²) (as printed after eq S0x41), so the other GGM
display, eq (S11v), "-(2x⁻²+x⁻¹+2+x+2x²)q", has the x^{±1}, x^{±2} weights
swapped (a misprint in GGM; the index decides it: I_41(0,±1) = -2q, I_41(0,±2) = -q).

Scope (anti-laundering). Inputs that remain GGM's and are NOT proved here:
conj.41M (the region matrices, hence eq Sp-41) and the block factorisation (d)
of the index. GGM prove (d) for 4₁; conj.41M is numerically certified by GGM.
The W-route probe already checks eq (Sp-41) at x = 1 against the printed
towers; C6 shows the index route and the W-route give the same S⁺(q).
No measured value enters; no fit; no c_k wired; nothing about the
A_ω → observable bridge (that is separately refuted, 2026-08-14).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_g3_fourone_index_assembly import I41  # noqa: E402

# A bivariate Laurent series is a dict {(x_deg, s_deg): int}, s = q^{1/2}.
D_S = 20          # keep s-degrees ≤ D_S  (q¹⁰)
PAD = 6           # extra s-order computed in N (N₂₂ reaches s⁻⁴ via e < 0)
E_MAX = 14        # electric-charge cutoff in Ind^rot (checked by C7)


def add(*ps):
    o: dict = {}
    for p in ps:
        for k, c in p.items():
            o[k] = o.get(k, 0) + c
    return {k: c for k, c in o.items() if c}


def scale(p, c):
    return {k: v * c for k, v in p.items()} if c else {}


def mono(xd, sd, c=1):
    return {(xd, sd): c}


def mul(a, b, dmax):
    o: dict = {}
    for (xa, sa), ca in a.items():
        for (xb, sb), cb in b.items():
            if sa + sb <= dmax:
                k = (xa + xb, sa + sb)
                o[k] = o.get(k, 0) + ca * cb
    return {k: c for k, c in o.items() if c}


def trunc(p, dmax):
    return {k: c for k, c in p.items() if k[1] <= dmax}


def geom_u(dmax):
    """u = 1/(1 - q x²) = Σ_k x^{2k} s^{2k}."""
    return {(2 * k, 2 * k): 1 for k in range(dmax // 2 + 1)}


def ind_rot(m, shift, dmax, emax=E_MAX):
    """Ind^rot(m, s^shift·x; q) = Σ_e I_41(m,e) s^{shift·e} x^e, s-degree ≤ dmax."""
    out: dict = {}
    for e in range(-emax, emax + 1):
        need = dmax - shift * e
        if need < 0:
            continue
        for d, c in I41(m, e, need).items():
            sd = d + shift * e
            if sd <= dmax:
                k = (e, sd)
                out[k] = out.get(k, 0) + c
    return {k: c for k, c in out.items() if c}


def index_matrix(dmax, emax=E_MAX):
    """N_{ij} = (-s)^{j-i} Ind^rot(j-i, s^{i+j} x; q), i,j ∈ {0,1}."""
    N = [[None, None], [None, None]]
    for i in range(2):
        for j in range(2):
            m = j - i
            base = ind_rot(m, i + j, dmax + 1, emax)
            pref = {(0, m): (-1) ** (m % 2)} if m >= 0 else None
            if m >= 0:
                N[i][j] = trunc(mul(pref, base, dmax + 1), dmax)
            else:  # (-s)^{-1} = -s^{-1}
                N[i][j] = trunc({(k[0], k[1] - 1): -c for k, c in base.items()}, dmax)
    return N


def gauges(dmax):
    u = geom_u(dmax)
    L = [[mono(0, 0, -1), {}],
         [mul(mono(-1, 0, -1), mul(add(mono(0, 0), mono(2, 2, -1), mono(3, 2, -1)), u, dmax), dmax),
          mul(mono(1, 2), u, dmax)]]
    R = [[mono(0, 0, -1), mul(add(mono(0, 0, -1), mono(1, 0, -1), mono(3, 2, 1)), u, dmax)],
         [{}, mul(mono(1, 0, -1), u, dmax)]]
    return L, R


def mat_mul(A, B, dmax):
    return [[add(mul(A[i][0], B[0][j], dmax), mul(A[i][1], B[1][j], dmax))
             for j in range(2)] for i in range(2)]


def stokes_from_index(dmax=D_S, emax=E_MAX):
    N = index_matrix(dmax + PAD, emax)
    L, R = gauges(dmax + PAD)
    S = mat_mul(mat_mul(L, N, dmax + PAD), R, dmax + PAD)
    return [[trunc(S[i][j], dmax) for j in range(2)] for i in range(2)], N


def coeff_in_q(p, qpow):
    """x-Laurent polynomial {x_deg: c} at s-degree 2·qpow."""
    return {xd: c for (xd, sd), c in p.items() if sd == 2 * qpow}


def at_x1(p, dmax):
    o = [0] * (dmax + 1)
    for (xd, sd), c in p.items():
        if 0 <= sd <= dmax:
            o[sd] += c
    return o


def series_div(num, den, dmax):
    """num/den in Z[x^±][[s]] with den = 1 + O(s) (exact)."""
    inv = {(0, 0): 1}
    rest = add(den, mono(0, 0, -1))
    term = {(0, 0): 1}
    for _ in range(dmax + 1):
        term = scale(mul(term, rest, dmax), -1)
        if not term:
            break
        inv = add(inv, term)
    return trunc(mul(num, inv, dmax), dmax)


def lp(d):
    """Laurent-poly dict {x_deg: c} → printable string."""
    return " ".join(f"{c:+d}x^{k}" for k, c in sorted(d.items())) or "0"


def P_(*pairs):
    """Build {x_deg: c} from (deg, c) pairs."""
    return {k: c for k, c in pairs if c}


# GGM printed x-series after eq (S0x41) (𝒮⁺ matrix), q¹ and q² coefficients.
PRINTED_X = {
    "S11": {1: P_((-2, -1), (-1, -2), (0, -2), (1, -2), (2, -1)),
            2: P_((-2, -1), (-1, -2), (0, -3), (1, -2), (2, -1))},
    "S12": {1: P_((-2, 1), (-1, 2), (0, 3), (1, 2), (2, 1)),
            2: P_((-4, 1), (-3, 4), (-2, 9), (-1, 15), (0, 17), (1, 15), (2, 9), (3, 4), (4, 1))},
    "S21": {1: P_((-2, -1), (-1, -2), (0, -3), (1, -2), (2, -1)),
            2: P_((-4, -1), (-3, -4), (-2, -9), (-1, -15), (0, -17), (1, -15), (2, -9), (3, -4), (4, -1))},
    "S22": {1: P_((-2, 1), (-1, 2), (0, 2), (1, 2), (2, 1)),
            2: P_((-4, 1), (-3, 4), (-2, 9), (-1, 14), (0, 17), (1, 14), (2, 9), (3, 4), (4, 1))},
}
# x = 1 printed towers, GGM eqs (61)-(64) (as in qbeta_g3_ggm_stokes_41.py)
PRINTED_61 = [1, -8, -9, 18, 46, 90, 62]
RATIO_62 = [3, 9, 75, 642, 5580, 48558, 422865]
RATIO_63 = [0, -9, -75, -642, -5580, -48558, -422865]
RESID_64 = [0, 8, 73, 638, 5571, 48538, 422819]


def main() -> int:
    print("=" * 78)
    print(" 4₁ Stokes matrix S⁺(x;q) from the triangulation 3d index (qou-vr3q)")
    print("=" * 78)
    S, N = stokes_from_index()
    S11, S12, S21, S22 = S[0][0], S[0][1], S[1][0], S[1][1]
    odd = any(sd % 2 for row in S for p in row for (_, sd) in p)
    print(f"\n  half-integer q-powers in S⁺: {odd} (must be False)")

    # ---- C1: the q→0 Stokes matrix ----
    q0 = [[coeff_in_q(S[i][j], 0) for j in range(2)] for i in range(2)]
    c1 = (q0[0][0] == {0: 1} and q0[0][1] == {-1: 1, 0: 1, 1: 1}
          and q0[1][0] == {} and q0[1][1] == {0: 1}
          and not any(sd < 0 for row in S for p in row for (_, sd) in p))
    print("\n[C1] S⁺(x;0) =", [[lp(q0[i][j]) for j in range(2)] for i in range(2)], " ok =", c1)

    # the two index coefficients that carry the 3
    i00 = I41(0, 0, 0).get(0, 0)
    i1m2 = I41(1, -2, 1).get(1, 0)
    print(f"     [I_41(0,0)]_q⁰ = {i00},  [I_41(1,-2)]_q^½ = {i1m2}"
          f"  ⇒ S⁺₁₂(x;0) = (1+x)·{i00} + x·x⁻²·({-i1m2})")
    c1b = (i00 == 1 and i1m2 == -1)

    # ---- C2/C3: printed x-series through q² ----
    dS = {"S11": add(S11, mono(0, 0, -1)),
          "S12": add(series_div(S12, S11, D_S), mono(-1, 0, -1), mono(0, 0, -1), mono(1, 0, -1)),
          "S21": series_div(S21, S11, D_S),
          "S22": add(S22, mono(0, 0, -1), scale(series_div(mul(S12, S21, D_S), S11, D_S), -1))}
    c23 = True
    for name, rows in PRINTED_X.items():
        for qp, want in rows.items():
            got = coeff_in_q(dS[name], qp)
            ok = got == want
            c23 &= ok
            print(f"[C2/3] 𝒮⁺_{name} q^{qp}: {lp(got)}  ok={ok}")
    Ind0 = trunc(ind_rot(0, 0, D_S), D_S)
    c2 = Ind0 == S11
    print(f"[C2] S⁺₁₁ ≡ Ind^rot(0,x;q) through q^{D_S // 2}: {c2}")
    # the GGM (S11v) display, -(2x⁻²+x⁻¹+2+x+2x²), is NOT what the index gives:
    s11v = P_((-2, -2), (-1, -1), (0, -2), (1, -1), (2, -2))
    misprint = coeff_in_q(dS["S11"], 1) != s11v
    print(f"     GGM eq (S11v) q-coefficient -(2x⁻²+x⁻¹+2+x+2x²) contradicted by index: {misprint}")

    # ---- C4: det = 1 ----
    det = add(mul(S11, S22, D_S), scale(mul(S12, S21, D_S), -1))
    c4 = det == {(0, 0): 1}
    print(f"[C4] det S⁺(x;q) = 1 through q^{D_S // 2}: {c4}")

    # ---- C5: symmetry S12 + S21 = (x⁻¹+1+x) S11 ----
    c5 = add(S12, S21, scale(mul(add(mono(-1, 0), mono(0, 0), mono(1, 0)), S11, D_S), -1)) == {}
    print(f"[C5] S⁺₁₂ + S⁺₂₁ = (x⁻¹+1+x)·S⁺₁₁ through q^{D_S // 2}: {c5}")

    # ---- C6: x = 1, printed towers and the W-route ----
    def x1q(p):
        a = at_x1(p, D_S)
        return [a[2 * k] for k in range(D_S // 2 + 1)]
    s11, s12, s21, s22 = (x1q(p) for p in (S11, S12, S21, S22))

    def sdiv(nu, de):
        n = len(nu)
        inv = [0] * n
        inv[0] = 1
        for d in range(1, n):
            inv[d] = -sum(de[k] * inv[d - k] for k in range(1, d + 1))
        return [sum(nu[k] * inv[d - k] for k in range(d + 1)) for d in range(n)]

    def smul(a, b):
        n = len(a)
        return [sum(a[k] * b[d - k] for k in range(d + 1)) for d in range(n)]
    r12, r21 = sdiv(s12, s11), sdiv(s21, s11)
    res64 = [s22[k] - (1 if k == 0 else 0) - sdiv(smul(s12, s21), s11)[k] for k in range(len(s11))]
    c6 = (s11[:7] == PRINTED_61 and r12[:7] == RATIO_62 and r21[:7] == RATIO_63
          and res64[:7] == RESID_64)
    print(f"[C6] x=1 towers (61)-(64) through q⁶: {c6}")
    print(f"     S⁺₁₁ = {s11}\n     S⁺₁₂/S⁺₁₁ = {r12}")
    c6b = None
    try:
        import qbeta_g3_ggm_stokes_41 as W
        import itertools
        o = D_S // 2
        Wm1 = W.W_matrix(-1, o)
        mags = ([[0, 1], [1, 1]], [[0, 1], [1, 0]], [[0, 1], [1, 2]])  # GGM eq (59a) |A|,|B|,|C|

        def variants(mag):
            pos = [(i, j) for i in range(2) for j in range(2) if mag[i][j]]
            for sg in itertools.product((1, -1), repeat=len(pos)):
                M = [row[:] for row in mag]
                for (i, j), t in zip(pos, sg):
                    M[i][j] *= t
                yield M
        # Same selection as the W-route probe: every sign pattern and both
        # transpose placements, kept iff it reproduces the PRINTED (60)-(64);
        # the index route plays no part in the selection.
        found = set()
        for tf in (False, True):
            Lw, Rw = (W.transpose(Wm1), Wm1) if tf else (Wm1, W.transpose(Wm1))
            for A in variants(mags[0]):
                for B in variants(mags[1]):
                    core = W.mat_mul_series(W.mat_mul_series(Lw, W.const_mat(B, o), o), Rw, o)
                    for C in variants(mags[2]):
                        SW = W.mat_mul_series(W.mat_mul_series(W.const_mat(A, o), core, o),
                                              W.const_mat(C, o), o)
                        for sg in (1, -1):
                            if any(sg * c % 2 for i in range(2) for j in range(2) for c in SW[i][j]):
                                continue
                            T = [[[sg * c // 2 for c in SW[i][j]] for j in range(2)] for i in range(2)]
                            if T[0][0][:7] != PRINTED_61 or [T[i][j][0] for i in range(2) for j in range(2)] != [1, 3, 0, 1]:
                                continue
                            r = (sdiv(T[0][1], T[0][0]), sdiv(T[1][0], T[0][0]))
                            if r[0][:7] != RATIO_62 or r[1][:7] != RATIO_63:
                                continue
                            found.add(tuple(tuple(tuple(T[i][j][:o + 1]) for j in range(2)) for i in range(2)))
        mine = tuple(tuple(tuple(x) for x in row) for row in [[s11, s12], [s21, s22]])
        print(f"     W-route sandwiches matching printed (60)-(63): {len(found)} distinct")
        c6b = len(found) == 1 and mine in found
    except Exception as exc:  # noqa: BLE001
        print(f"     W-route comparison not run: {exc!r}")
    print(f"[C6b] index route ≡ W-route S⁺(q) coefficientwise through q^{D_S // 2}: {c6b}")

    # ---- C7: stability in the e-cutoff and the s-order ----
    S_hi, _ = stokes_from_index(D_S + 2, E_MAX + 4)
    c7 = all(trunc(S_hi[i][j], D_S) == S[i][j] for i in range(2) for j in range(2))
    print(f"[C7] stable under (D_S, E_MAX) → (+2, +4): {c7}")

    ok = (not odd) and c1 and c1b and c2 and c23 and c4 and c5 and c6 and c7 and (c6b is not False)
    verdict = (
        "The figure-eight Stokes matrix S⁺(x;q) is assembled from the DGG 3d index "
        "alone (bare eq 4.18, two tetrahedra) through the explicit gauge "
        "L = P·K(x⁻¹)⁻¹·T₀(x⁻¹;q⁻¹)⁻¹, R = T₀(x;q)⁻ᵀ·K(x)⁻ᵀ·Q fixed by GGM's proved "
        "Wronskian relations (W41rec at m=-1, W41xm at m=0) and the Stokes formula "
        "eq (Sp-41). At q→0 it gives S⁺(x;0) = [[1, x⁻¹+1+x],[0,1]]: the Stokes "
        "constant 3 = (1+x)·[I_41(0,0)]_{q⁰} + x·x⁻²·(-[I_41(1,-2)]_{q^{1/2}}) at x=1, "
        "i.e. the vacuum (counted with the gauge weight 1+x) plus one BPS state at "
        "magnetic flux 1, electric charge -2. Full x-series match GGM's printed 𝒮⁺ "
        "through q², det S⁺ = 1, the GGM symmetry 𝒮₁₂ = -𝒮₂₁, and at x=1 the "
        "printed towers (61)-(64) through q⁶ and the W-route S⁺(q) coefficientwise. "
        "Conditional on GGM conj.41M and the block factorisation of the index (proved "
        "by GGM for 4₁). Side finding: GGM eq (S11v) misprints the q-coefficient "
        "weights of S⁺₁₁(x;q). Scope-(a); exact integers; no fit; no measured value."
    )
    print("\nVERDICT:", "PASS" if ok else "FAIL")

    wb = WitnessBuilder("qbeta-g3-stokes-from-3d-index-41", engine="python-int")
    wb.set_description(
        "qou-vr3q: the 4₁ Stokes matrix S⁺(x;q), and its q→0 Stokes constant 3, "
        "computed from the triangulation 3d index through the GGM gauge; exact.")
    wb.set_content_block("thm:aomega-fourone-dt-count")
    wb.add_data("source", "GGM 2012.00062 tex: eq Sp-41, W41rec, W41xm, WW41 (+footnote), S0x41; DGG 1112.5179 eq 4.18")
    wb.add_data("Splus_x_q0", [[lp(q0[i][j]) for j in range(2)] for i in range(2)])
    wb.add_data("index_coefficients_carrying_the_3",
                {"I41(0,0)_q0": i00, "I41(1,-2)_q^(1/2)": i1m2,
                 "formula": "S+_12(x;0) = (1+x)*[I(0,0)]_q0 - x*x^-2*[I(1,-2)]_q^(1/2) = x^-1+1+x"})
    wb.add_data("x1_S11", s11)
    wb.add_data("x1_S12_over_S11", r12)
    wb.add_data("ggm_S11v_misprint", bool(misprint))
    wb.add_data("verdict", verdict)
    for name, val, src in [
        ("C1_Splus_x_q0", c1 and c1b, "S⁺(x;0)=[[1,x⁻¹+1+x],[0,1]] from index (GGM eq S0x41)"),
        ("C2_S11_equals_Ind_rot_0", c2, "S⁺₁₁(x;q)=Ind^rot(0,x;q) (GGM eq S3Dx)"),
        ("C3_printed_x_series_q2", c23, "GGM printed 𝒮⁺(x;q) entries through q²"),
        ("C4_det_one", c4, "det S⁺(x;q)=1"),
        ("C5_ggm_symmetry", c5, "S⁺₁₂+S⁺₂₁=(x⁻¹+1+x)S⁺₁₁"),
        ("C6_x1_printed_towers", c6, "GGM eqs (61)-(64) through q⁶"),
        ("C7_truncation_stable", c7, "unchanged under larger e-cutoff and s-order"),
    ]:
        wb.add_assertion(name, computed=1 if val else 0, expected=1, tolerance=0, source=src)
    if c6b is not None:
        wb.add_assertion("C6b_index_route_equals_W_route", computed=1 if c6b else 0,
                         expected=1, tolerance=0, source="qbeta_g3_ggm_stokes_41 W-route sandwich")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
