"""aomega_m3_pretzel_one_dim_reduction_probe.py

Route C, M3, Part 11 (bean qou-x3iv): the EXACT one-dimensional reduction of the
Dimofte-Garoufalidis state integral (DG arxiv-1202.6268v2 eq 5.2, u = 0) at a
rank-one quad choice, applied to 4_1 = m004, 5_2 = m015 and the (-2,3,7) pretzel
m016 = K12n242.  Everything is derived from held text; the one step that is not a
held equation verbatim (the Fourier transform of psi_hbar, obtained from DG (C.25)
by Fourier inversion) is checked numerically.

Held inputs
  DG (5.2)  Z_T = sqrt(8 pi^3/(hbar^3 det B)) int d^N Z/(2 pi hbar)^{N/2}
              exp[(1/hbar)( 1/2 (i pi + hbar/2)^2 f.B^-1 nu - (i pi + hbar/2) Z.B^-1 nu
                            + 1/2 Z.B^-1 A Z )] prod_i psi_hbar(Z_i)
  DG (2.7)-(2.8)  A, B, nu from the gluing matrices (Part 10, re-derived here).
  DG (5.5)-(5.6)  psi_hbar(Z) = prod_{r>=1} (1 - q^r e^{-Z}) / (1 - Lq^{-r+1} e^{-LZ}),
              q = e^hbar, Lq = e^{-4 pi^2/hbar}, LZ = 2 pi i Z/hbar.
  GK 1304.2705 (1)  Phi_b(x) = (e^{2 pi b (x + c_b)}; q)_inf / (e^{2 pi b^-1 (x - c_b)}; q~)_inf,
              q = e^{2 pi i b^2}, q~ = e^{-2 pi i b^-2}, c_b = i(b + b^-1)/2;
              Phi_b(x) Phi_b(-x) = e^{pi i x^2} Phi_b(0)^2;  I_{A,B} = int Phi_b^B e^{-A pi i x^2}.
  DG (C.18)  Fourier transform  f^(W) = int dZ/(2 pi i hbar)^{1/2} e^{Z W/hbar} f(Z).
  DG (C.25)  int dZ/sqrt(2 pi i hbar) e^{(1/2hbar)(Z^2 + 2 Z Z' - (2 pi i + hbar) Z)} psi(Z)
              = C psi(Z'),  C = e^{pi^2/(6 hbar) +- i pi/4 - hbar/24}.
  DG (5.4)   the integral is defined up to  exp(pi^2 a/(6 hbar) + i pi b/4 + hbar c/24), a,b,c in Z.
  GGM 2012.00062 (125), (240) at u = m = mu = 0 and GK §1.3:  I_{4_1} = I_{1,2}, I_{5_2} = I_{2,3}.

Derivation (all exact; carried out symbolically below)
  D1  dictionary: matching the two product formulas term by term gives
        psi_hbar(Z) = Phi_b(c_b - Z/(2 pi b)),  hbar = 2 pi i b^2,  i pi + hbar/2 = 2 pi b c_b.
  D2  Fourier transform of psi (invert (C.25): the (C.18) transform applied twice is
      reflection, f^^(Z) = f(-Z), for pure-imaginary hbar):
        psi^(P) = C^-1 exp[(P^2 + (2 pi i + hbar) P)/(2 hbar)] psi(-P)      (up to (5.4)).
  D3  rank one, B^-1 A = c v v^T, w := B^-1 nu.  Hubbard-Stratonovich on s = v.Z:
        exp[c s^2/(2 hbar)] = sqrt(c/(2 pi hbar)) int dW exp[-c W^2/(2 hbar) + c W s/hbar],
      after which every Z_i appears linearly, exp[P_i Z_i/hbar] with
        P_i = c v_i W - (i pi + hbar/2) w_i,
      and integrates to sqrt(2 pi i hbar) psi^(P_i) by (C.18).  With t := -c W and D2:
        Z_T ∝ int dt exp[ (sum v_i^2 - 1/c) t^2/(2 hbar)
                           - (i pi + hbar/2) (t/hbar) sum_i v_i (1 - w_i) ]  prod_i psi_hbar(v_i t + (i pi+hbar/2) w_i).
  D4  in Faddeev variables, t = -2 pi b x:
        Z_T ∝ int dx e^{-pi i A x^2 - 2 pi i c_b Lambda x} prod_i Phi_b(v_i x + (1 - w_i) c_b),
        A = sum v_i^2 - 1/c,   Lambda = sum_i v_i (1 - w_i);
      completing the square (x -> x - c_b Lambda/A) gives the centred form
        Z_T ∝ e^{pi i c_b^2 Lambda^2/A} int dx e^{-pi i A x^2} prod_i Phi_b(v_i x + sigma_i c_b),
        sigma_i = 1 - w_i - v_i Lambda/A.

Results (exact)
  4_1   A = 1, sigma = (0,0):        int Phi_b(x)^2 e^{-pi i x^2}                 = GK I_{1,2}  (gate G1)
  5_2   A = 1, sigma = (0,0,0):      int Phi_b(x)^3 e^{-pi i x^2}                 = GK I_{1,3}  (gate G2, see below)
  m016  A = 2, sigma = (0,0,-1):     int Phi_b(x)^2 Phi_b(2x - c_b) e^{-2 pi i x^2}                (test T1)
Gate G2 does NOT land on the printed I_{2,3}: it lands on I_{1,3}.  Measured numerically
(gate G3): I_{1,3}(b) and I_{2,3}(b) are DIFFERENT functions of b (their ratio is not a
(5.4)-class constant and its modulus is not constant in b), but at |b| = 1 they satisfy
I_{1,3} = (unit) * conj(Phi_b(0)^6 I_{2,3}) with a (5.4)-class unit — the relation of a state
integral to that of the ORIENTATION-REVERSED manifold.  So DG (5.2) on SnapPy's m015 datum
is the 5_2 state integral with the opposite orientation to the one GK/GGM print; the
reduction is exact and the gate passes as "mirror".  This also EXPLAINS Part 9: the (1,3)
and (2,3) block bilinears coincide because I_{1,3} and I_{2,3} are the two orientations of
the same knot, and the sigma_1 sigma_1 index does not see orientation.
  Mirror form (x -> -x and the functional equation, then conjugation at |b| = 1):
        A_mirror = sum v_i^2 - A = 1/c:   4_1 -> 1, 5_2 -> 2 (= I_{2,3} as printed), m016 -> 4,
        pretzel mirror: int Phi_b(x)^2 Phi_b(2x - c_b) e^{-4 pi i x^2 + 4 pi i c_b x} dx.
Scope (measured in the one-cusped census, 2-4 tetrahedra, gate S1): rank one alone gives a
one-dimensional integral; the COLLINEARITY w ∥ v that makes all shifts land on the doubled
factor holds for these three knots and for 10 of the 17 rank-one quads found, and the
unit-factor-unshifted identity c sum v^2 + kappa = 1 + c sum v holds for 9 of those 10 (fails
at m019, c = -1).  Neither is claimed in general.
No q0, no float64 (mpmath at 22 dps for the numerical gates only; every recorded structure
constant is exact sympy).  Orientation of the derived pretzel integral = SnapPy's m016.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

KNOTS = [("m004", "4_1", (0, 0)), ("m015", "5_2", (2, 2, 2)), ("m016", "(-2,3,7) = K12n242", (0, 2, 1))]


def rows_of(G):
    try:
        return [[int(v) for v in row] for row in G]
    except TypeError:
        return [[int(v) for v in row] for row in G.list()]


def nz_datum(Gm, n, quad):
    """DG (2.7)-(2.8) from SnapPy's interleaved log-form matrix (as in Part 10)."""
    cols = lambda k: [3 * i + k for i in range(n)]
    Gz, Gzp, Gzpp = sp.zeros(n + 2, n), sp.zeros(n + 2, n), sp.zeros(n + 2, n)
    for i in range(n):
        s = quad[i]
        Gz[:, i] = Gm[:, cols(s % 3)[i]]
        Gzp[:, i] = Gm[:, cols((s + 1) % 3)[i]]
        Gzpp[:, i] = Gm[:, cols((s + 2) % 3)[i]]
    rows = list(range(n - 1)) + [n]
    A = (Gz - Gzp)[rows, :]
    B = (Gzpp - Gzp)[rows, :]
    nu = sp.Matrix([2 - sum(Gzp[i, :]) for i in range(n - 1)] + [-sum(Gzp[n, :])])
    return A, B, nu


def rank_one_factor(Q):
    n = Q.shape[0]
    col = [j for j in range(n) if any(Q[:, j])][0]
    v = Q[:, col] / Q[col, col]
    g = sp.gcd([sp.nsimplify(x) for x in v])
    v = (v / g).applyfunc(sp.nsimplify)
    c = sp.nsimplify(Q[col, col] / (v[col] ** 2))
    assert Q == c * v * v.T
    return c, v


def reduce_symbolic(c, v, w):
    """Steps D3-D4 carried out exactly in sympy on the exponent.  Returns the exact
    structure constants of the reduced one-dimensional integral."""
    hbar, t, W = sp.symbols("hbar t W")
    lam = sp.I * sp.pi + hbar / 2                         # i pi + hbar/2  (= 2 pi b c_b)
    n = len(v)
    # HS + Fourier: exponent in W after every Z_i has been integrated (D2, D3)
    P = [c * v[i] * W - lam * w[i] for i in range(n)]
    E = -c * W**2 / (2 * hbar) + sum((P[i] ** 2 + 2 * lam * P[i]) / (2 * hbar) for i in range(n))
    E = sp.expand(E.subs(W, -t / c))
    poly = sp.Poly(E, t)
    quad_coeff = sp.simplify(poly.coeff_monomial(t**2) * 2 * hbar)          # A_eff
    lin_coeff = sp.simplify(poly.coeff_monomial(t) * hbar / lam)             # coefficient of lam t/hbar
    const = sp.simplify(poly.coeff_monomial(1) * hbar / lam**2)              # coefficient of lam^2/hbar
    A_eff = sp.nsimplify(quad_coeff)
    Lambda = sp.nsimplify(-lin_coeff)                                          # exponent is -lam (t/hbar) Lambda
    assert A_eff == sum(x * x for x in v) - 1 / c
    assert Lambda == sum(v[i] * (1 - w[i]) for i in range(n))
    # psi arguments: -P_i = v_i t + lam w_i  ->  Phi_b(c_b - (v_i t + 2 pi b c_b w_i)/(2 pi b)) = Phi_b(v_i x + (1 - w_i) c_b), x = -t/(2 pi b)
    shifts_uncentred = [sp.nsimplify(1 - w[i]) for i in range(n)]
    # centre the Gaussian: x -> x - c_b Lambda/A
    sigma = [sp.nsimplify(1 - w[i] - v[i] * Lambda / A_eff) for i in range(n)]
    A_mirror = sp.nsimplify(sum(x * x for x in v) - A_eff)
    return {"A": A_eff, "Lambda": Lambda, "shifts_uncentred": shifts_uncentred, "sigma": sigma,
            "A_mirror": A_mirror, "const_lam2_over_hbar": sp.nsimplify(const)}


# ---------------------------------------------------------------- numerical gates (mpmath, |q|,|q~| < 1)
def numerics():
    import mpmath as mp
    mp.mp.dps = 22

    def qpoch(a, q):
        p = mp.mpf(1); tt = a; k = 0
        while abs(tt) > mp.mpf(10) ** (-mp.mp.dps - 3):
            p *= (1 - tt); tt *= q; k += 1
            if k > 5000:
                break
        return p

    def make(b):
        q = mp.exp(2j * mp.pi * b**2); qt = mp.exp(-2j * mp.pi / b**2); cb = 1j * (b + 1 / b) / 2
        assert abs(q) < 1 and abs(qt) < 1
        Phi = lambda x: qpoch(mp.exp(2 * mp.pi * b * (x + cb)), q) / qpoch(mp.exp(2 * mp.pi / b * (x - cb)), qt)
        hbar = 2j * mp.pi * b**2
        Lq = mp.exp(-4 * mp.pi**2 / hbar)                   # DG (5.6); |Lq| > 1, Lq^{-1} = q~
        Lq_inv = 1 / Lq
        assert abs(Lq_inv - qt) < mp.mpf(10) ** (-mp.mp.dps + 2)
        def psi(Z):                                          # DG (5.5): prod_{r>=1} (1 - q^r e^{-Z}) / (1 - Lq^{-(r-1)} e^{-LZ})
            return qpoch(q * mp.exp(-Z), q) / qpoch(mp.exp(-2j * mp.pi * Z / hbar), Lq_inv)
        return Phi, psi, q, qt, cb, hbar

    out = {}
    # G0: dictionary psi_hbar(Z) = Phi_b(c_b - Z/(2 pi b))
    b = mp.exp(1j * mp.pi / 6)
    Phi, psi, q, qt, cb, hbar = make(b)
    worst = 0
    for Z in [mp.mpf('0.7') + 0.2j, mp.mpf('-1.3') + 0.5j, mp.mpf('2.1') - 0.4j]:
        lhs = psi(Z); rhs = Phi(cb - Z / (2 * mp.pi * b))
        worst = max(worst, abs(lhs / rhs - 1))
    out["G0_dictionary_max_rel_err"] = mp.nstr(worst, 5)

    # G_FT: psi^(P) := int dZ/sqrt(2 pi i hbar) e^{Z P/hbar} psi(Z)  vs  C^-1 e^{(P^2+(2 pi i+hbar)P)/2hbar} psi(-P);
    # the ratio must be INDEPENDENT of P (it is a (5.4)-class constant from orientation/inversion normalisation).
    # Contour: Z = 2 pi b (c_b - x), x in R + i eps; frequency P = 2 pi b pi_, with -eps < Im pi_ < 0.
    eps = float(mp.im(cb)) * 0.45
    def psi_hat(pi_):
        P = 2 * mp.pi * b * pi_
        f = lambda s: psi(2 * mp.pi * b * (cb - (s + 1j * eps))) * mp.exp(2 * mp.pi * b * (cb - (s + 1j * eps)) * P / hbar)
        val = mp.quad(f, [-36, -24, -12, -6, -3, 0, 3, 6, 12, 24, 36]) * (2 * mp.pi * b) / mp.sqrt(2j * mp.pi * hbar)
        rhs = mp.exp((P**2 + (2j * mp.pi + hbar) * P) / (2 * hbar)) * psi(-P)
        return val / rhs
    # convergence on x in R + i eps needs  -eps < Im pi_ < 0  with margin at both ends: decay rates 2 pi |Im pi_| (x -> -inf)
    # and 2 pi (eps - |Im pi_|) (x -> +inf); eps = 0.45 Im c_b ~ 0.39 here, so |Im pi_| in [0.12, 0.2] and L = 36 give < 1e-14.
    ratios = [psi_hat(pi_) for pi_ in [mp.mpf('0.3') - 0.15j, mp.mpf('-0.5') - 0.2j, mp.mpf('0.9') - 0.12j]]
    spread = max(abs(r / ratios[0] - 1) for r in ratios)
    out["G_FT_ratio_P_independence_spread"] = mp.nstr(spread, 5)
    out["G_FT_ratio_value"] = mp.nstr(ratios[0], 12)
    # is the constant of (5.4) class?  exp(pi^2 a/(6 hbar) + i pi b'/4 + hbar c/24) = q~^{a/24}... test small a,b',c
    cls = None
    for a in range(-6, 7):
        for c_ in range(-6, 7):
            for bb in range(8):
                cand = mp.exp(mp.pi**2 * a / (6 * hbar) + 1j * mp.pi * bb / 4 + hbar * c_ / 24)
                if abs(ratios[0] / cand - 1) < 1e-6:
                    cls = (a, bb, c_)
    out["G_FT_ratio_is_(5.4)-class"] = cls

    # G3: I_{1,3} vs I_{2,3}: different functions, conjugate at |b| = 1 up to a (5.4)-class unit
    def I(A, B_, b_, Phi_, eps_, L=16):
        f = lambda s: Phi_(s + 1j * eps_) ** B_ * mp.exp(-A * 1j * mp.pi * (s + 1j * eps_) ** 2)
        return mp.quad(f, [-L, -L / 2, -4, -2, -1, 0, 1, 2, 4, L / 2, L])
    g3 = []
    for b_ in [mp.exp(1j * mp.pi / 6), mp.exp(1j * mp.pi / 5), mp.mpf('0.8') * mp.exp(1j * mp.pi / 7)]:
        Phi_, _, q_, qt_, cb_, _ = make(b_)
        e_ = float(mp.im(cb_)) * 0.45
        i13 = I(1, 3, b_, Phi_, e_); i23 = I(2, 3, b_, Phi_, e_); i12 = I(1, 2, b_, Phi_, e_)
        r = i13 / i23
        conj_rel = i13 / mp.conj(Phi_(0) ** 6 * i23)
        hb_ = 2j * mp.pi * b_**2
        unit = []
        for a_ in range(-12, 13):
            for c_ in range(-12, 13):
                for m_ in range(8):
                    cand = mp.exp(mp.pi**2 * a_ / (6 * hb_) + 1j * mp.pi * m_ / 4 + hb_ * c_ / 24)   # DG (5.4) class
                    if abs(conj_rel / cand - 1) < 1e-7:
                        unit.append((a_, m_, c_))
                    if abs(r / cand - 1) < 1e-7:
                        out.setdefault("G3_ratio_is_constant_at", []).append(mp.nstr(b_, 6))
        unit = unit or None
        g3.append({"b": mp.nstr(b_, 8), "abs_b": mp.nstr(abs(b_), 6), "I12": mp.nstr(i12, 12), "I13": mp.nstr(i13, 12),
                   "I23": mp.nstr(i23, 12), "I13_over_I23": mp.nstr(r, 10), "abs_ratio": mp.nstr(abs(r), 10),
                   "I13_over_conj(Phi0^6 I23)": mp.nstr(conj_rel, 10), "conj_unit_(5.4)_triples_(a,b,c)": unit})
    out["G3"] = g3
    return out


def main():
    t0 = time.time()
    import snappy
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    results = {}
    for name, label, quad in KNOTS:
        M = snappy.Manifold(name)
        n = M.num_tetrahedra()
        Gm = sp.Matrix(rows_of(M.gluing_equations()))
        A, B, nu = nz_datum(Gm, n, quad)
        Q = B.inv() * A
        c, v = rank_one_factor(Q)
        w = B.inv() * nu
        kappa = None
        collinear = all((w[i] == 0) if v[i] == 0 else True for i in range(n))
        ks = set(sp.nsimplify(w[i] / v[i]) for i in range(n) if v[i] != 0)
        collinear = collinear and len(ks) == 1
        if collinear:
            kappa = ks.pop()
        red = reduce_symbolic(c, [sp.nsimplify(x) for x in v], [sp.nsimplify(x) for x in w])
        ident = (collinear and (c * sum(x * x for x in v) + kappa == 1 + c * sum(v)))
        factors = " ".join(f"Phi_b({v[i]}x{'' if red['sigma'][i]==0 else ('+' if red['sigma'][i]>0 else '')}{'' if red['sigma'][i]==0 else str(red['sigma'][i])+'c_b'})" for i in range(n))
        form = f"int e^(-{red['A']} pi i x^2) {factors} dx"
        print(f"\n== {name} = {label}, quad {quad}: c = {c}, v = {list(v)}, w = B^-1 nu = {list(w)}, collinear = {collinear}, kappa = {kappa}")
        print(f"   reduced (SnapPy orientation): {form}    [Lambda = {red['Lambda']}, A_mirror = {red['A_mirror']}]")
        results[name] = {"label": label, "quad": list(quad), "c": str(c), "v": [int(x) for x in v], "w": [str(x) for x in w],
                         "collinear": bool(collinear), "kappa": None if kappa is None else str(kappa),
                         "unit_factor_identity_c_sumv2_plus_kappa_eq_1_plus_c_sumv": bool(ident),
                         "A": str(red["A"]), "Lambda": str(red["Lambda"]), "sigma": [str(x) for x in red["sigma"]],
                         "shifts_uncentred_(1-w_i)": [str(x) for x in red["shifts_uncentred"]],
                         "A_mirror": str(red["A_mirror"]), "reduced_form": form,
                         "prefactor_exponent_coefficient_of_(i pi + hbar/2)^2/hbar_before_f_term": str(red["const_lam2_over_hbar"]),
                         "prefactor_note": "multiply by exp[(i pi + hbar/2)^2 f.B^-1 nu/(2 hbar)] (DG 5.2, f a flattening) and by "
                                           "sqrt(8 pi^3/(hbar^3 det B)) (2 pi hbar)^{-N/2} sqrt(c/(2 pi hbar)) (2 pi i hbar)^{N/2} C^{-N} (1/c) "
                                           "(1/(2 pi b)) e^{pi i c_b^2 Lambda^2/A}; all (5.4)-class up to the hbar power."}
        results[name]["exponent_check"] = "A = sum v^2 - 1/c and Lambda = sum v_i (1 - w_i) verified by sympy Poly on the expanded exponent"

    r4, r5, rp = results["m004"], results["m015"], results["m016"]
    check("G1-4_1: reduced integral is int Phi_b(x)^2 e^{-pi i x^2} dx = GK I_{1,2} = GGM (125) at u=m=mu=0 (A=1, no shifts)",
          r4["A"] == "1" and r4["sigma"] == ["0", "0"], form=r4["reduced_form"])
    check("G2-5_2: reduced integral is int Phi_b(x)^3 e^{-pi i x^2} dx = GK I_{1,3} — the (q<->q~) partner of the printed I_{2,3}; "
          "the printed A=2 is recovered as A_mirror = 1/c = 2 (orientation reversal, see G3)",
          r5["A"] == "1" and r5["sigma"] == ["0", "0", "0"] and r5["A_mirror"] == "2", form=r5["reduced_form"])
    check("T1-m016: reduced integral is int Phi_b(x)^2 Phi_b(2x - c_b) e^{-2 pi i x^2} dx (A=2; the doubled factor carries the "
          "residual shift -c_b, the unit factors none)", rp["A"] == "2" and rp["sigma"] == ["0", "0", "-1"], form=rp["reduced_form"])
    check("C1-collinearity w = B^-1 nu ∥ v holds for all three knots (kappa = 1, 1, 1/2)",
          all(results[k]["collinear"] for k in results) and [results[k]["kappa"] for k in ("m004", "m015", "m016")] == ["1", "1", "1/2"])
    check("C2-unit-factor identity c sum v^2 + kappa = 1 + c sum v holds for all three (=> every unit-coefficient factor is unshifted)",
          all(results[k]["unit_factor_identity_c_sumv2_plus_kappa_eq_1_plus_c_sumv"] for k in results))

    # S1: census scope
    scope = {"manifolds": 0, "rank_one_quads": 0, "collinear": 0, "identity": 0, "non_collinear": [], "identity_fails": []}
    for tets in (2, 3, 4):
        for M in snappy.OrientableCuspedCensus(cusps=1, tets=tets):
            scope["manifolds"] += 1
            n = M.num_tetrahedra()
            Gm = sp.Matrix(rows_of(M.gluing_equations()))
            for quad in itertools.product(range(3), repeat=n):
                A, B, nu = nz_datum(Gm, n, quad)
                if B.det() == 0:
                    continue
                Q = B.inv() * A
                if Q.rank() != 1:
                    continue
                scope["rank_one_quads"] += 1
                c, v = rank_one_factor(Q)
                w = B.inv() * nu
                ks = set(sp.nsimplify(w[i] / v[i]) for i in range(n) if v[i] != 0)
                coll = len(ks) == 1 and all(w[i] == 0 for i in range(n) if v[i] == 0)
                if coll:
                    scope["collinear"] += 1
                    kap = ks.pop()
                    if c * sum(x * x for x in v) + kap == 1 + c * sum(v):
                        scope["identity"] += 1
                    else:
                        scope["identity_fails"].append([M.name(), list(quad), [int(x) for x in v], str(c), [str(x) for x in w]])
                else:
                    scope["non_collinear"].append([M.name(), list(quad), [int(x) for x in v], str(c), [str(x) for x in w]])
    print(f"\n census scope (1 cusp, 2-4 tets): {scope['manifolds']} manifolds, {scope['rank_one_quads']} rank-one quads, "
          f"{scope['collinear']} collinear, identity holds for {scope['identity']}; non-collinear: {len(scope['non_collinear'])}, "
          f"identity fails: {len(scope['identity_fails'])}")
    check("S1-scope: collinearity and the unit-factor identity are NOT general (some rank-one census quads violate each) — "
          "the three-knot results are knot-specific measurements, not a theorem",
          len(scope["non_collinear"]) > 0 and len(scope["identity_fails"]) > 0,
          non_collinear=len(scope["non_collinear"]), identity_fails=len(scope["identity_fails"]), rank_one=scope["rank_one_quads"])

    print("\n numerical gates (mpmath, 22 dps) ...")
    num = numerics()
    print(f"   G0 dictionary max rel err: {num['G0_dictionary_max_rel_err']}")
    print(f"   G_FT ratio P-independence spread: {num['G_FT_ratio_P_independence_spread']}, ratio = {num['G_FT_ratio_value']}, (5.4)-class (a,b,c): {num['G_FT_ratio_is_(5.4)-class']}")
    for g in num["G3"]:
        print(f"   G3 b={g['b']} |b|={g['abs_b']}: I13/I23={g['I13_over_I23']} |.|={g['abs_ratio']}; I13/conj(Phi0^6 I23)={g['I13_over_conj(Phi0^6 I23)']} (5.4)-triples={g['conj_unit_(5.4)_triples_(a,b,c)']}")
    check("G0-dictionary psi_hbar(Z) = Phi_b(c_b - Z/(2 pi b)) (DG 5.5 vs GK 1), numerically at three points",
          float(num["G0_dictionary_max_rel_err"]) < 1e-15, max_rel_err=num["G0_dictionary_max_rel_err"])
    check("G_FT-Fourier transform of psi (inverted C.25): psi^(P)/[C^-1 e^{(P^2+(2 pi i+hbar)P)/2hbar} psi(-P)] is P-independent",
          float(num["G_FT_ratio_P_independence_spread"]) < 1e-7 and num["G_FT_ratio_is_(5.4)-class"] is not None,
          spread=num["G_FT_ratio_P_independence_spread"],
          ratio=num["G_FT_ratio_value"], five_four_class=num["G_FT_ratio_is_(5.4)-class"])
    unit_b = [g for g in num["G3"] if abs(float(g["abs_b"]) - 1) < 1e-9]
    check("G3a-I_{1,3} and I_{2,3} are DIFFERENT functions of b (ratio not a (5.4)-class constant; modulus varies with b)",
          "G3_ratio_is_constant_at" not in num and len(set(g["abs_ratio"][:6] for g in num["G3"])) > 1,
          moduli=[g["abs_ratio"] for g in num["G3"]])
    common = None
    for g in unit_b:
        tr = set(map(tuple, g["conj_unit_(5.4)_triples_(a,b,c)"] or []))
        common = tr if common is None else (common & tr)
    check("G3b-at |b| = 1 (where conj Phi_b = 1/Phi_b(conj x)): I_{1,3} = u * conj(Phi_b(0)^6 I_{2,3}) with ONE (5.4)-class "
          "unit u = q~^{a/24} q^{c/24} e^{i pi b/4} common to every unit-modulus b tested — the orientation-reversal relation",
          bool(unit_b) and bool(common), common_triples=sorted(common) if common else None,
          per_b=[g["conj_unit_(5.4)_triples_(a,b,c)"] for g in unit_b])
    check("G3c-at |b| != 1 the conjugation relation is NOT expected (conj Phi_b = 1/Phi_{conj b}(conj x)) and is not found",
          all(g["conj_unit_(5.4)_triples_(a,b,c)"] is None for g in num["G3"] if abs(float(g["abs_b"]) - 1) > 1e-9))

    verdict = ("DERIVED (DG 5.2 + C.18 + C.25 + 5.5, GK 1): at a rank-one quad the DG state integral reduces exactly to "
               "int e^{-pi i A x^2} prod_i Phi_b(v_i x + sigma_i c_b) dx with A = sum v_i^2 - 1/c and sigma from w = B^-1 nu. "
               "4_1 -> I_{1,2} exactly. 5_2 -> I_{1,3}, NOT the printed I_{2,3}: numerically the two are different functions "
               "that are complex conjugates at |b|=1 up to a (5.4)-class unit, i.e. the two ORIENTATIONS of 5_2 (the DG "
               "integral on SnapPy's m015 datum is the mirror of the KLV/AK one; A_mirror = 1/c = 2 recovers the printed "
               "form). This also explains Part 9's finding that the (1,3) and (2,3) block bilinears coincide. The pretzel "
               "(SnapPy orientation): int Phi_b(x)^2 Phi_b(2x - c_b) e^{-2 pi i x^2} dx; mirror: same dilogarithms with "
               "e^{-4 pi i x^2 + 4 pi i c_b x}. The doubled factor carries the residual -c_b shift; its poles at "
               "c_b + (i b m + i b^-1 n)/2 halve the lattice spacing and the Gaussian cross term e^{pi i m n} couples the "
               "q- and q~-halves by parity — the level-2 mechanism, now explicit. Orientation of the derived pretzel "
               "integral is SnapPy's and is NOT matched to GGM/GZ's (open, recorded). Next (Part 12): residues at the "
               "half-lattice (orders 3 and 1) -> q^{1/2}-series blocks -> sigma_1 sigma_1 index vs the derived index.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    wit = {
        "name": "aomega-m3-pretzel-one-dim-reduction",
        "description": "Exact one-dimensional reduction of the DG state integral (1202.6268 eq 5.2) at the rank-one quad for "
                       "4_1, 5_2 and the (-2,3,7) pretzel: Gaussian coefficient, shifts, mirror form; gates at 4_1 (exact) and "
                       "5_2 (mirror of the printed I_{2,3}).",
        "computation": "aomega-m3-pretzel-one-dim-reduction", "engine": "python+sympy+snappy+mpmath",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {"snappy_version": snappy.__version__, "mp_dps_numerical_gates": 22,
                       "dictionary": "psi_hbar(Z) = Phi_b(c_b - Z/(2 pi b)), hbar = 2 pi i b^2, i pi + hbar/2 = 2 pi b c_b",
                       "fourier": "psi^(P) = C^-1 exp[(P^2 + (2 pi i + hbar) P)/(2 hbar)] psi(-P), from DG (C.25) by inversion",
                       "orientation": "SnapPy's, for all three; the printed 5_2 form is the mirror"},
        "data": {"knots": results, "census_scope": scope, "numerical_gates": num},
        "verdict": verdict, "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(wit, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-one-dim-reduction.witness.json")
    with open(out, "w") as fh:
        json.dump(wit, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
