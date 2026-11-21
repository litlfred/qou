#!/usr/bin/env python3
"""qbeta_colour_factor_probe — a colour tensor factor on the ruled Q_β cell (issue #8833, front 3).

Closed family, value and reporting rules: PREREGISTRATION.md (committed first, e7a96d0061).
Lean: QOU/QBeta/ColourFactorDeligne.lean (sorry-free).

Mechanism. Each quark strand is C² ⊠ C³ (isospin ⊠ colour) in the Deligne product of
Rep U_q(sl₂) and Rep U_q(sl₃). The braid acts by ρ₂ ⊗ ρ₃ (Jimbo R on each factor), the quantum
trace uses K = K₂ ⊗ K₃, and the ruled flavour projections act on the isospin factor. Members:
  C1 full colour trace / [3]³;  C2 colour singlet Λ³_q / [3]³;  C3 colour singlet / 1;
each with gl₃ framing and sl₃ framing c = q^(-1/3). Words: V³ (ruled), V⁶, V⁹ (reported).

Arithmetic: mpmath at the proton pin (q_parameter.Q_50_DIGIT_STR), 60 dps; exact Fractions at
q = 2, 3; the singlet vector by exact sympy linear algebra at the pin as a rational. No float.
Nothing is selected, nothing is mapped to MeV.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
F_REQUIRED = mp.mpf("0.78233341") / mp.mpf("0.325433929")
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def V(k):
    """V^k, V = σ₀σ₁⁻¹, as (position, sign) crossings."""
    return [(0, 1), (1, -1)] * k


def crossing(vec, n, N, i, s, q, c=None):
    """Jimbo R (s=+1) or R⁻¹ (s=-1) of gl_N on positions (i, i+1) of (C^N)^{⊗n}, times c^s.

    Basis index tuples; for x < y: R e_x e_y = e_y e_x, R e_y e_x = e_x e_y + h e_y e_x,
    R e_x e_x = q e_x e_x. For N = 2 this is the convention of the γγ probes (bit 0 = up)."""
    h = q - 1 / q
    sc = None if c is None else (c if s > 0 else 1 / c)
    out = {}

    def add(k, v):
        if v:
            out[k] = out.get(k, 0) + v
    for b, val in vec.items():
        x, y = b[i], b[i + 1]
        sw = b[:i] + (y, x) + b[i + 2:]
        if sc is not None:
            val = val * sc
        if x == y:
            add(b, val * (q if s > 0 else 1 / q))
        elif x < y:
            add(sw, val)
            if s < 0:
                add(b, -h * val)
        else:
            add(sw, val)
            if s > 0:
                add(b, h * val)
    return out


def apply(word, vec, n, N, q, c=None):
    for (i, s) in reversed(word):
        vec = crossing(vec, n, N, i, s, q, c)
    return vec


def kweight(b, N, q):
    w = 1
    for x in b:
        w = w * q ** (N - 1 - 2 * x)
    return w


def qtrace(word, n, N, q, basis=None, c=None):
    tot = 0
    for b in (basis if basis is not None else itertools.product(range(N), repeat=n)):
        v = apply(word, {b: 1}, n, N, q, c)
        if v.get(b):
            tot += kweight(b, N, q) * v[b]
    return tot


def qint(N, q):
    return (q ** N - q ** (-N)) / (q - 1 / q)


def closed_C1(N, q):
    h = q - 1 / q
    return 1 - h ** 4 * qint(N - 1, q) * qint(N + 1, q) / qint(N, q) ** 2


def Wp():
    return [b for b in itertools.product(range(2), repeat=3) if sum(b) == 1]


def Wn():
    return [b for b in itertools.product(range(2), repeat=3) if sum(b) == 2]


def deligne_trace(word, q, iso_basis, colour_proj, c=None):
    """Tr((K₂⊗K₃)^{⊗3} (P_iso ⊗ P_col) (ρ₂⊗ρ₃)(word)) on the 216-dim space, brute force.

    colour_proj None = identity; else (v, wl) with P_col = v wlᵀ / (wlᵀ v)."""
    tot = 0
    cols = list(itertools.product(range(3), repeat=3))
    for bi in iso_basis:
        for bc in cols:
            st = {(bi, bc): 1}
            for (i, s) in reversed(word):
                new = {}
                for (ki, kc), val in st.items():
                    vi = crossing({ki: 1}, 3, 2, i, s, q)
                    vc = crossing({kc: 1}, 3, 3, i, s, q, c)
                    for a, x in vi.items():
                        for b2, y in vc.items():
                            new[(a, b2)] = new.get((a, b2), 0) + val * x * y
                st = new
            if colour_proj is None:
                tot += kweight(bi, 2, q) * kweight(bc, 3, q) * st.get((bi, bc), 0)
    return tot


def singlet_vector(qr):
    """The (1³)-isotypic line of (C³)^{⊗3}: common −q⁻¹ eigenvector of σ₀, σ₁ (exact)."""
    basis = list(itertools.permutations(range(3)))
    idx = {b: k for k, b in enumerate(basis)}

    def mat(i):
        M = sp.zeros(6, 6)
        for b in basis:
            for k, v in crossing({b: 1}, 3, 3, i, 1, qr).items():
                M[idx[k], idx[b]] += v
        return M
    A = (mat(0) + sp.eye(6) / qr).col_join(mat(1) + sp.eye(6) / qr)
    ns = A.nullspace()
    return basis, ns


def main() -> int:
    # E1 Markov parameter of the colour factor and of isospin (exact)
    ok = True
    for N in (2, 3):
        for q in (Fr(2), Fr(3)):
            zN = q ** (2 * N - 1) * (q ** 2 - 1) / (q ** (2 * N) - 1)
            ok &= qtrace([(0, 1)], 2, N, q) / qint(N, q) ** 2 == zN
    check("E1_markov_parameter", ok,
          "Tr(K⊗K Ř)/[N]² = z_N = q^(2N-1)(q²-1)/(q^(2N)-1) exactly at q = 2, 3 for N = 2, 3 "
          "(z_2 = z_D).")

    # E2 the ruled cell at q0
    d2 = Q0 + 1 / Q0
    eps_p = qtrace(V(3), 3, 2, Q0, Wp()) / d2 ** 3
    eps_n = qtrace(V(3), 3, 2, Q0, Wn()) / d2 ** 3
    eps_f = eps_n - eps_p
    check("E2_ruled_cell_reproduced",
          abs(eps_p - mp.mpf("0.40872")) < mp.mpf("1e-5")
          and abs(eps_n - mp.mpf("0.33174")) < mp.mpf("1e-5")
          and abs(eps_f - mp.mpf("-0.07698053460")) < mp.mpf("1e-10"),
          f"eps_p = {mp.nstr(eps_p, 15)}, eps_n = {mp.nstr(eps_n, 15)}, "
          f"eps_flavour = {mp.nstr(eps_f, 15)}.")

    # E3 C1 closed form (Lean colourFactorV3_eq), exact at q = 2, 3, ranks 2..4
    ok = True
    for N in (2, 3, 4):
        for q in (Fr(2), Fr(3)):
            ok &= qtrace(V(3), 3, N, q) / qint(N, q) ** 3 == closed_C1(N, q)
    check("E3_C1_closed_form_exact", ok,
          "Tr(K^{⊗3} ρ_N(V³))/[N]³ = 1 − h⁴[N−1][N+1]/[N]² exactly at q = 2, 3, N = 2, 3, 4 "
          "(computed from the 27/8/64-dim matrices, not from the Lean formula).")

    # Members at q0, framings gl3 / sl3, words V3 V6 V9
    d3 = Q0 ** 2 + 1 + Q0 ** -2
    c_sl3 = Q0 ** (mp.mpf(-1) / 3)
    rows = []
    C1 = {}
    for k in (3, 6, 9):
        for fr, c in (("gl3", None), ("sl3", c_sl3)):
            C1[(k, fr)] = qtrace(V(k), 3, 3, Q0, c=c) / d3 ** 3
    check("E5_framing_drops",
          all(abs(C1[(k, "gl3")] - C1[(k, "sl3")]) < mp.mpf("1e-50") for k in (3, 6, 9)),
          "sl3 framing c = q^(-1/3) leaves C1 unchanged on V³, V⁶, V⁹ (exponent sum 0; Lean "
          "framing_drops).")
    check("E3b_C1_V3_at_q0", abs(C1[(3, "gl3")] - closed_C1(3, Q0)) < mp.mpf("1e-50"),
          f"C1(V³) at q0 = {mp.nstr(C1[(3, 'gl3')], 20)} = closed form "
          f"{mp.nstr(closed_C1(3, Q0), 20)}.")

    # E4 brute-force factorisation on (C²⊗C³)^{⊗3}
    bp = deligne_trace(V(3), Q0, Wp(), None) / (d2 * d3) ** 3
    bn = deligne_trace(V(3), Q0, Wn(), None) / (d2 * d3) ** 3
    c1 = C1[(3, "gl3")]
    bp_s = deligne_trace(V(3), Q0, Wp(), None, c=c_sl3) / (d2 * d3) ** 3
    check("E4_factorisation_216dim",
          abs(bp - eps_p * c1) < mp.mpf("1e-50") and abs(bn - eps_n * c1) < mp.mpf("1e-50")
          and abs(bp_s - bp) < mp.mpf("1e-50"),
          f"brute-force 216-dim trace: proton {mp.nstr(bp, 18)} = eps_p·C1, neutron "
          f"{mp.nstr(bn, 18)} = eps_n·C1 (both framings). Flavour-blind factor.")

    # Singlet members C2, C3: exact singlet line at the pin as a rational
    qr = sp.Rational(Q_50_DIGIT_STR)
    basis, ns = singlet_vector(qr)
    ok = len(ns) == 1
    sc = {}
    kw = None
    if ok:
        v = ns[0]
        vec = {b: v[j] for j, b in enumerate(basis) if v[j] != 0}
        kw = kweight(basis[0], 3, qr)
        ok &= all(kweight(b, 3, qr) == kw for b in vec)
        for k in (3, 6, 9):
            w = apply(V(k), dict(vec), 3, 3, qr)
            ratios = {sp.simplify(w.get(b, 0) / vec[b]) for b in vec}
            ok &= len(ratios) == 1
            sc[k] = ratios.pop() if len(ratios) == 1 else None
            ok &= set(w) <= set(vec)
    check("E6_singlet_line", ok and kw == 1 and all(sc[k] == 1 for k in sc),
          f"(1³)-isotypic line of (C³)^{{⊗3}} is 1-dim ({len(ns)}), K-weight {kw}; V^k acts on "
          f"it by {[sc.get(k) for k in (3, 6, 9)]} for k = 3, 6, 9 (exact, at the pin).")
    C2 = 1 / d3 ** 3
    C3 = mp.mpf(1)

    # Report
    for k in (3, 6, 9):
        ep = qtrace(V(k), 3, 2, Q0, Wp()) / d2 ** 3
        en = qtrace(V(k), 3, 2, Q0, Wn()) / d2 ** 3
        for name, F in (("C1", C1[(k, "gl3")]), ("C2", C2), ("C3", C3)):
            for fr in ("gl3", "sl3"):
                Fv = C1[(k, fr)] if name == "C1" else F
                rows.append({"word": f"V^{k}", "member": name, "framing": fr,
                             "F": mp.nstr(Fv, 25), "F_eps_p": mp.nstr(Fv * ep, 20),
                             "F_eps_n": mp.nstr(Fv * en, 20),
                             "F_eps_flavour": mp.nstr(Fv * (en - ep), 20),
                             "F_over_F_required": mp.nstr(Fv / F_REQUIRED, 15)})
    Fs = [mp.mpf(r["F"]) for r in rows]
    hits = [r for r in rows if mp.mpf(r["F"]) > 1]
    check("E7_report", len(hits) == 0,
          f"{len(rows)} member×framing×word cells. F range [{mp.nstr(min(Fs), 12)}, "
          f"{mp.nstr(max(Fs), 12)}]; F_required = {mp.nstr(F_REQUIRED, 8)}. Cells with F > 1: "
          f"{len(hits)}. None selected.")
    for r in rows:
        if r["framing"] == "gl3":
            print("   ", r["word"], r["member"], "F =", r["F"][:16],
                  " F/F_req =", r["F_over_F_required"][:10])

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-colour-factor", engine="mpmath")
    for nm, o, d in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact" if nm.startswith(("E1", "E3_", "E6")) else "1e-50",
                         source=d)
    wb.save({
        "description": ("Colour tensor factor (Deligne product sl2 x sl3) on the ruled D1 Q_beta "
                        "cell. Flavour-blind; every member F <= 1. Nothing selected."),
        "q0": Q_50_DIGIT_STR, "eps_p": mp.nstr(eps_p, 30), "eps_n": mp.nstr(eps_n, 30),
        "eps_flavour": mp.nstr(eps_f, 30), "F_required": mp.nstr(F_REQUIRED, 20),
        "C1_V3_closed_form": "1 - h^4 [2][4]/[3]^2 = 1 - h^4 + h^4/[3]^2",
        "lean": "QOU/QBeta/ColourFactorDeligne.lean (colourFactorV3_eq, colourFactorV3_lt_one)",
        "rows": rows,
        "caveats": ["The family is the Deligne-product colour factor only; a colour mechanism "
                    "that does not factor as a tensor product (e.g. a gl_6 = iso+colour "
                    "Jimbo R) is outside it.",
                    "Q_beta is not assumed linear in eps; F is reported at the eps level."],
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
