"""aomega_m3_pretzel_level2_stokes_probe.py

Route C, M3 (bean qou-lzzi): the level-2 Stokes route for the (-2,3,7) pretzel
(SnapPy m016 = K12n242), and the s(x) = x + 1 + 1/x hypothesis.

THE QUESTION.  Garoufalidis-Gu-Marino, "Peacock patterns and resurgence in complex
Chern-Simons theory" (held: library/arxiv-2012.00062v3/) print the q -> 0 Stokes
matrices of 4_1 and 5_2 as polynomials in the ADJOINT WEIGHT s(x) = x^-1 + 1 + x
(their (239)):

  (188)  S+(x;0) = [[1, s(x)], [0, 1]],     S-(x;0) = [[1, 0], [-s(x), 1]]      (4_1)
  (307)  S+(x;0) = Ssig3sig1(x) Ssig3sig2(x) Ssig1sig2(x)                        (5_2)
         = [[1,0,0],[0,1,0],[-s,0,1]] [[1,0,0],[0,1,0],[0,s,1]] [[1,s+1,0],[0,1,0],[0,0,1]]

Is the rank-6, level-2 pretzel's q -> 0 Stokes data also built from s(x)?

THE ROUTE (this probe), and how it differs from the parent session's.  The parent
session (branch claude/binding-gap-categorical-research-cem5tp, PR #7152,
docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md SS3f-3m) attacked the
BLOCKS: residues of the state integral -> six (q^1/4, x^1/2)-series -> fusion ->
sigma_1 sigma_1 index.  That route stalled at the level-2 FUSION rule (SS3k, SS3l): the
index is the weight-1 component of an epsilon-expansion at collided triple poles
(Garoufalidis-Zagier Obs 3.9), which no reweighting of the bare families reproduces.

This probe attacks the OPERATOR instead.  GGM's Stokes matrices (187a), (305a) are
built from the fundamental solution matrix W_m(x;q) of a linear q-difference
equation -- GGM (332) for the Theorem-28 family, GGM (276) for 5_2.  The q -> 0
Stokes data is controlled by that operator's q -> 0 exponents, which are its
characteristic roots.  So the s(x) question can be answered by DERIVING the pretzel's
descendant q-difference operator, without ever needing the blocks or the fusion.

WHAT IS DERIVED HERE (from held text; nothing transcribed):

  Faddeev's functional equation, from the held product form (GK arxiv-1304.2705v1 (1);
  the dictionary is gate G0 of the sibling probe aomega_m3_pretzel_one_dim_reduction):
      Phi_b(z) = (e^{2 pi b (z + c_b)}; q)_inf / (e^{2 pi b^-1 (z - c_b)}; q~)_inf
  gives, since e^{2 pi b c_b} = -q^{1/2} and e^{2 pi i b^-1 b} = 1,
      Phi_b(z + i b) = Phi_b(z) / (1 + q^{1/2} e^{2 pi b z}),
      Phi_b(z - i b) = Phi_b(z) (1 + q^{-1/2} e^{2 pi b z}).                     (FE)

  For a one-dimensional state integral with descendant variable t,
      Z(t) = int_{R + i eps} F(v) e^{-A pi i v^2 + 2 pi i v t} dv,
  shifting the contour v -> v - i b and using (FE) on every dilogarithm expresses
  Z(t) as a FINITE linear combination of the Z(t - i k b) -- the descendant
  q-difference equation.  Inside the integral, multiplication by X^k, X = e^{2 pi b v},
  is exactly t -> t - i k b; the Gaussian contributes X^{-A} q^{A/2} and
  e^{2 pi i v t} contributes w = e^{2 pi b t}.  Writing N(X) for the product of the
  (FE) factors, the operator is

      P(X) = q^{A/2} w N(X) - X^A ,        P(X) . Z = 0.                          (OP)

GATES:

  G1  5_2: N(X) has coefficients (1, s, s, 1) in s(x) -- EXACTLY GGM (276) / (332)
      with pole offsets {1, x, 1/x}, the adjoint weight set.  Exact sympy.
  G2  4_1: N(X) has coefficients (1, 1+x, x) -- GGM (332) with (A,r) = (1,2),
      offsets {x, 1}.  Exact sympy.
  G3  the (FE)-rearranged integrand identity holds POINTWISE (mpmath), for all three
      knots: this is the algebra of (OP), checked independently of any contour.
  G4  the derived recurrence holds on the ACTUAL state integrals (mpmath): this tests
      the contour shift as well.  For the pretzel that is a DEGREE-6 recurrence.
  G5  the rank: degree 6 = the pretzel's rank 6 (GZ's twelve H_j^pm, six per side).
  G6  GGM (188) and (307), multiplied out, lie in Z[s(x)] -- the criterion, on the
      two knots where the answer is printed.
  G7  the pretzel's q -> 0 exponents, by Newton polygon.
  G8  the Z/2 level grading, and sigma^2 = s(x) + 1.

CONVENTIONS.  x = e^{2 pi b u}, w = e^{2 pi b t}, q = e^{2 pi i b^2},
c_b = i(b + b^-1)/2, sigma := x^{1/2} + x^{-1/2}, s(x) = x + 1 + 1/x (GGM (239)).
Integrands (SS3h-3i of the audit doc, derived there from the Neumann-Zagier datum):
  4_1       int Phi_b(v + u) Phi_b(v) e^{-pi i v^2 + 2 pi i v t} dv        (A=1, r=2)
  5_2       int Phi_b(v) Phi_b(v+u) Phi_b(v-u) e^{-2 pi i v^2 + ...} dv    (A=2, r=3)
  pretzel   int Phi_b(v+u/2) Phi_b(v-u/2) Phi_b(2v-c_b) e^{-2 pi i v^2 + ...} dv

PRECISION.  All operator algebra is exact (sympy over Q(q^{1/2}, x^{1/2}, w)).
mpmath appears only in the numerical gates, at mp.dps = 30.  No float64 anywhere.
"""

from __future__ import annotations

import json
import os
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------------------
# exact symbols.  Q := q^{1/2}, XR := x^{1/2}; q = Q^2, x = XR^2.
# --------------------------------------------------------------------------------------
Q, XR, W = sp.symbols("Q XR W", positive=True)
X = sp.Symbol("X")
Y = sp.Symbol("Y")
q = Q**2
x = XR**2
s_of = lambda y: y + 1 + 1 / y                      # GGM (239)
SIGMA = XR + 1 / XR                                 # sigma = x^{1/2} + x^{-1/2}
SX = s_of(x)


def shift_factors(offsets, doubled):
    """Product of the (FE) factors picked up by the contour shift v -> v - i b.

    `offsets` are the a_j = e^{2 pi b u_j} of the UNIT dilogarithms Phi_b(v + u_j);
    each contributes (1 + q^{-1/2} a_j X).  `doubled` adds one factor
    Phi_b(2 v - c_b), which is shifted by -2 i b and contributes
    (1 - q^{-1} X^2)(1 - q^{-2} X^2), because e^{2 pi b (2 v - c_b)} = -q^{-1/2} X^2.
    """
    p = sp.Integer(1)
    for a in offsets:
        p *= 1 + a * X / Q
    if doubled:
        p *= (1 - X**2 / q) * (1 - X**2 / q**2)
    return sp.expand(p)


def descendant_operator(offsets, A, doubled=False):
    """(OP): returns (N as Poly in X, P = q^{A/2} w N - X^A as Poly in X)."""
    N = shift_factors(offsets, doubled)
    P = sp.expand(q ** sp.Rational(A, 2) * W * N - X**A)
    return sp.Poly(N, X), sp.Poly(P, X)


def coeffs(P):
    return [sp.simplify(sp.expand(P.coeff_monomial(X**j) if j else P.coeff_monomial(1)))
            for j in range(P.degree() + 1)]


def _monomials(e):
    """[(exponent of Q as a Rational in q, coefficient)] for an expanded Laurent expr."""
    out = []
    for term in sp.Add.make_args(sp.expand(e)):
        pw = term.as_powers_dict()
        k = pw.get(Q, sp.Integer(0))
        out.append((sp.Rational(k, 2), sp.simplify(term / Q**k)))
    return out


def val_q(e):
    """Lowest power of q (Q = q^{1/2}) appearing in e; None if e == 0."""
    ms = _monomials(e)
    return min((m[0] for m in ms), default=None) if sp.expand(e) != 0 else None


def lead_q(e, target):
    """Coefficient of q^target in e (0 if absent)."""
    tot = sp.Integer(0)
    for k, c in _monomials(e):
        if k == target:
            tot += c
    return sp.simplify(tot)


def newton(P):
    """Newton polygon of Poly P in X, valuations in q.  Returns (points, lower hull)."""
    pts = []
    for j in range(P.degree() + 1):
        c = sp.expand(P.coeff_monomial(X**j) if j else P.coeff_monomial(1))
        v = val_q(c)
        if v is not None:
            pts.append((sp.Integer(j), v))
    pts.sort()
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (y2 - y1) * (p[0] - x1) >= (p[1] - y1) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append(p)
    return pts, hull


def segment_leading_poly(P, j0, v0, slope):
    """Leading Y-polynomial of the Newton segment starting at (j0, v0) with given slope.

    Substituting X = q^{-slope} Y keeps exactly the coefficients on the hull line
    val_q(c_j) = v0 + slope * (j - j0).
    """
    out = sp.Integer(0)
    for j in range(j0, P.degree() + 1):
        c = sp.expand(P.coeff_monomial(X**j) if j else P.coeff_monomial(1))
        if sp.expand(c) == 0:
            continue
        target = v0 + slope * (j - j0)
        if val_q(c) == target:
            out += lead_q(c, target) * Y ** (j - j0)
    return sp.expand(out)


# --------------------------------------------------------------------------------------
# numerics (mpmath only below this line)
# --------------------------------------------------------------------------------------
KNOTS = {
    # dilogarithm factors as (alpha, beta) meaning Phi_b(alpha * v + beta),
    # beta given as a callable of (u, c_b)
    "4_1": dict(A=1, offsets_sym=[x, sp.Integer(1)], doubled=False,
                dilogs=[(1, lambda u, cb: u), (1, lambda u, cb: 0)],
                r_eff=2),
    "5_2": dict(A=2, offsets_sym=[sp.Integer(1), x, 1 / x], doubled=False,
                dilogs=[(1, lambda u, cb: 0), (1, lambda u, cb: u), (1, lambda u, cb: -u)],
                r_eff=3),
    "pretzel": dict(A=2, offsets_sym=[XR, 1 / XR], doubled=True,
                    dilogs=[(1, lambda u, cb: u / 2), (1, lambda u, cb: -u / 2),
                            (2, lambda u, cb: -cb)],
                    r_eff=6),
}


def mp_eval(expr, Qv, XRv, Wv, Xv=None):
    """Evaluate a sympy expression in (Q, XR, W, X) at mpmath values, WITHOUT float64.

    `sp.N(...)` followed by `complex(...)` would downcast to float64 and floor every
    numerical gate at ~1e-16; `lambdify(..., 'mpmath')` keeps mpf/mpc throughout.
    """
    f = sp.lambdify((Q, XR, W, X), expr, "mpmath")
    return f(Qv, XRv, Wv, Xv if Xv is not None else 1)


def _mp_setup(dps=30):
    import mpmath as mp
    mp.mp.dps = dps

    def qpoch(a, qq):
        p = mp.mpf(1)
        t = a
        for _ in range(8000):
            if abs(t) < mp.mpf(10) ** (-mp.mp.dps - 5):
                break
            p *= 1 - t
            t *= qq
        return p

    def make(b):
        qq = mp.exp(2j * mp.pi * b**2)
        qt = mp.exp(-2j * mp.pi / b**2)
        cb = 1j * (b + 1 / b) / 2
        Phi = lambda z: (qpoch(mp.exp(2 * mp.pi * b * (z + cb)), qq)
                         / qpoch(mp.exp(2 * mp.pi / b * (z - cb)), qt))
        return Phi, qq, qt, cb

    return mp, make


def pointwise_identity(name, dps=30):
    """G3: the (FE)-rearranged integrand identity, checked pointwise.

    integrand(v - i b) / integrand(v)  ==  q^{A/2} w X^{-A} N(X),  X = e^{2 pi b v}.
    This is the algebra of (OP), independent of any contour or convergence question.
    """
    mp, make = _mp_setup(dps)
    spec = KNOTS[name]
    A = spec["A"]
    Nsym, _ = descendant_operator(spec["offsets_sym"], A, spec["doubled"])
    worst = mp.mpf(0)
    samples = []
    for b in (mp.mpf("0.75") * mp.exp(1j * mp.pi / 6),
              mp.mpf("1.1") * mp.exp(1j * mp.pi / 5)):
        Phi, qq, qt, cb = make(b)
        u = mp.mpf("0.13")
        t = mp.mpf("0.07") - mp.mpf("0.04") * 1j
        xv = mp.exp(2 * mp.pi * b * u)
        wv = mp.exp(2 * mp.pi * b * t)
        for v in (mp.mpf("0.3") + mp.mpf("0.21") * 1j,
                  mp.mpf("-0.8") + mp.mpf("0.5") * 1j,
                  mp.mpf("1.4") - mp.mpf("0.15") * 1j):
            def integrand(vv):
                g = mp.mpc(1)
                for (al, be) in spec["dilogs"]:
                    g *= Phi(al * vv + be(u, cb))
                return g * mp.exp(-A * 1j * mp.pi * vv**2 + 2j * mp.pi * vv * t)
            lhs = integrand(v - 1j * b) / integrand(v)
            Xv = mp.exp(2 * mp.pi * b * v)
            Nv = mp_eval(Nsym.as_expr(), mp.sqrt(qq), mp.sqrt(xv), wv, Xv)
            rhs = mp.power(qq, mp.mpf(A) / 2) * wv * mp.power(Xv, -A) * Nv
            rel = abs(lhs / rhs - 1)
            worst = max(worst, rel)
            samples.append(mp.nstr(rel, 4))
    return {"knot": name, "worst_rel_err": mp.nstr(worst, 6), "samples": samples,
            "worst_float": float(worst)}


def integral_recurrence(name, dps=30):
    """G4: sum_j c_j Z(t - i (j - A) b) = 0 on the actual state integrals.

    Convergence of Z(t') on R + i eps needs  -(r_eff - A) eps < Im(t') < A eps,
    with r_eff = sum alpha_j^2 (the pretzel's doubled factor contributes 4, not 1,
    because Phi_b(2v - c_b) ~ exp(pi i (2v)^2) at +infinity).  The shifts move
    Im(t') by -k Re(b) for k = j - A, so the whole ladder fits only if
    r_eff * eps exceeds (deg) * Re(b).

    b is chosen with |b| < 1: for |b| = rho, Im(c_b)/Re(b) = (1 + rho^-2)/2, which
    is exactly 1 at rho = 1 (marginal) and grows as rho falls.  rho ~ 0.55 leaves a
    real margin, which is what makes mp.quad converge -- at rho = 1 the decay rate
    at one end of the ladder is ~0.7 and the quadrature floors at ~1e-6 no matter
    what dps is set to.  eps must also satisfy eps < Im(c_b) (stay below the first
    pole of the unit dilogarithms) and, for the pretzel, eps > Im(c_b)/2 (the
    doubled factor's -c_b shift makes the integrand grow otherwise).
    """
    mp, make = _mp_setup(dps)
    spec = KNOTS[name]
    A = spec["A"]
    r_eff = spec["r_eff"]
    _, Psym = descendant_operator(spec["offsets_sym"], A, spec["doubled"])
    cs = coeffs(Psym)
    rows = []
    for bmod, bang, eps_frac in (("0.55", sp.Rational(1, 6), "0.90"),
                                 ("0.60", sp.Rational(1, 5), "0.88")):
        b = mp.mpf(bmod) * mp.exp(1j * mp.pi * float(bang))
        Phi, qq, qt, cb = make(b)
        eps = mp.mpf(eps_frac) * mp.im(cb)
        bR = mp.re(b)
        ks = [j - A for j in range(len(cs))]
        # centre t_I in the intersection of the per-k windows
        lo = max(float(-(r_eff - A) * eps + k * bR) for k in ks)
        hi = min(float(A * eps + k * bR) for k in ks)
        if not lo < hi:
            rows.append({"knot": name, "b": mp.nstr(b, 8), "eps": mp.nstr(eps, 6),
                         "status": "no common convergence window",
                         "window": [lo, hi]})
            continue
        tI = mp.mpf((lo + hi) / 2)
        t = mp.mpf("0.07") + 1j * tI
        u = mp.mpf("0.13")
        xv = mp.exp(2 * mp.pi * b * u)
        wv = mp.exp(2 * mp.pi * b * t)

        def Z(tp):
            def f(sv):
                v = sv + 1j * eps
                g = mp.mpc(1)
                for (al, be) in spec["dilogs"]:
                    g *= Phi(al * v + be(u, cb))
                return g * mp.exp(-A * 1j * mp.pi * v**2 + 2j * mp.pi * v * tp)
            return mp.quad(f, [-60, -30, -15, -8, -4, -2, -1, 0, 1, 2, 4, 8, 15, 30, 60])

        tot = mp.mpc(0)
        mag = mp.mpf(0)
        for j, c in enumerate(cs):
            if sp.expand(c) == 0:
                continue
            cv = mp_eval(c, mp.sqrt(qq), mp.sqrt(xv), wv)
            zj = Z(t - 1j * (j - A) * b)
            tot += cv * zj
            mag = max(mag, abs(cv * zj))
        rows.append({"knot": name, "b": mp.nstr(b, 8), "eps": mp.nstr(eps, 6),
                     "t": mp.nstr(t, 8), "u": "0.13", "degree": len(cs) - 1,
                     "abs_residual": mp.nstr(abs(tot), 6),
                     "abs_largest_term": mp.nstr(mag, 6),
                     "rel_residual": mp.nstr(abs(tot) / mag, 6),
                     "rel_float": float(abs(tot) / mag),
                     "convergence_window_tI": [lo, hi]})
    return rows


# --------------------------------------------------------------------------------------
def main():
    t0 = time.time()
    assertions = []

    def check(label, ok, **extra):
        assertions.append({"label": label, "passed": bool(ok), **extra})
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
        for k, v in extra.items():
            print(f"          {k}: {v}")

    data = {}

    print("\n=== Part 1: the derived descendant q-difference operators ===\n")
    ops = {}
    for nm in ("4_1", "5_2", "pretzel"):
        sp_ = KNOTS[nm]
        Nsym, Psym = descendant_operator(sp_["offsets_sym"], sp_["A"], sp_["doubled"])
        ops[nm] = (Nsym, Psym)
        cN = coeffs(Nsym)
        print(f"  {nm}:  degree {Nsym.degree()},  N(X) coefficients")
        for j, c in enumerate(cN):
            print(f"      X^{j}: {c}")
        data[nm] = {"degree": Nsym.degree(),
                    "N_coeffs": [str(c) for c in cN],
                    "P_coeffs": [str(c) for c in coeffs(Psym)]}

    # ---- G2: 4_1
    cN41 = coeffs(ops["4_1"][0])
    g2 = (sp.simplify(cN41[0] - 1) == 0
          and sp.simplify(cN41[1] - (1 + x) / Q) == 0
          and sp.simplify(cN41[2] - x / q) == 0)
    check("G2-4_1: N(X) = 1 + q^{-1/2}(1 + x) X + q^{-1} x X^2, i.e. prod over the pole offsets "
          "{x, 1} -- GGM (332) with (A, r) = (1, 2).  Elementary symmetric functions e1 = 1 + x, e2 = x; "
          "s(x) = (1 + x + x^2)/x = (e1^2 - e2)/e2 is what appears in GGM (188) after the (327) "
          "theta-renormalisation.",
          g2, N_coeffs=[str(c) for c in cN41])

    # ---- G1: 5_2
    cN52 = coeffs(ops["5_2"][0])
    g1 = (sp.simplify(cN52[0] - 1) == 0
          and sp.simplify(cN52[1] - SX / Q) == 0
          and sp.simplify(cN52[2] - SX / q) == 0
          and sp.simplify(cN52[3] - 1 / q ** sp.Rational(3, 2)) == 0)
    check("G1-5_2: N(X) = 1 + q^{-1/2} s(x) X + q^{-1} s(x) X^2 + q^{-3/2} X^3, i.e. coefficients "
          "(1, s, s, 1) -- EXACTLY GGM (276) / (332) with pole offsets {1, x, 1/x}, the ADJOINT WEIGHT "
          "SET.  This is where s(x) comes from: it is e1 = e2 of that set.",
          g1, N_coeffs=[str(c) for c in cN52], s_of_x=str(sp.expand(SX)))

    # ---- G5: rank
    Npz, Ppz = ops["pretzel"]
    check("G5-rank: the derived pretzel operator has degree 6 -- the pretzel's rank 6 (GZ's twelve "
          "level-2 series H_j^pm, j = 0..5, six per side).  The two unit dilogarithms give degree 2; "
          "the DOUBLED dilogarithm Phi_b(2v - c_b) shifts by -2 i b and gives degree 4, not 2.",
          Npz.degree() == 6, degree=Npz.degree(),
          from_unit_dilogarithms=2, from_doubled_dilogarithm=4)

    # ---- G8a: x-dependence only through sigma
    cNpz = coeffs(Npz)
    sym_ok = all(sp.simplify(sp.expand(c - c.subs(XR, 1 / XR))) == 0 for c in cNpz)
    check("G8a-pretzel: every coefficient of N(X) is invariant under x^{1/2} -> x^{-1/2}, so the "
          "x-dependence is entirely through sigma = x^{1/2} + x^{-1/2} = s(x^{1/2}) - 1.",
          sym_ok, N_coeffs=[str(c) for c in cNpz])

    # ---- G8b: the Z/2 level grading
    flip = sp.expand(Ppz.as_expr().subs({Q: -Q, XR: -XR}, simultaneous=True))
    graded = sp.simplify(sp.expand(flip - Ppz.as_expr())) == 0
    check("G8b-pretzel LEVEL GRADING: P(X) is invariant under the simultaneous flip "
          "(q^{1/2}, x^{1/2}) -> (-q^{1/2}, -x^{1/2}).  Equivalently sigma appears to an ODD power "
          "exactly when q appears to a HALF-INTEGER power.  That is level 2: the deck transformation "
          "of the double cover x = (x^{1/2})^2 is tied to the deck transformation of q^{1/2}.",
          graded)

    # ---- G8c: the extension
    id1 = sp.simplify(sp.expand(SIGMA**2 - (SX + 1))) == 0
    Ssym = sp.Symbol("S")
    irred = len(sp.factor_list(Y**2 - (Ssym + 1), Y)[1]) == 1
    check("G8c-the extension: sigma^2 = s(x) + 1, and Y^2 - (S + 1) is irreducible over Q(S).  So "
          "sigma = sqrt(s(x) + 1) generates a DEGREE-2 extension of Z[s(x)] and is NOT a polynomial "
          "in s(x).  Even powers of sigma lie in Z[s(x)]; odd powers do not.",
          id1 and irred, identity="sigma^2 - s(x) - 1 = 0",
          sigma_squared=str(sp.expand(SIGMA**2)), s_plus_1=str(sp.expand(SX + 1)))
    data["extension"] = {"sigma": "x^{1/2} + x^{-1/2}", "minimal_polynomial": "Y^2 - (s(x) + 1)",
                         "degree_over_Z[s]": 2}

    print("\n=== Part 2: q -> 0 exponents by Newton polygon ===\n")
    # The polygon is taken on N(X), the OFFSET polynomial, not on the full P(X).
    # P = q^{A/2} w N(X) - X^A, and the second term is GGM (332)'s descendant term
    # -(-q)^A w^{-1} q^m S^A -- it carries q^m, so at FIXED descendant index it
    # vanishes as q -> 0 and does not contribute an exponent.  GGM (276) shows this
    # directly for 5_2: the coefficient is (s - q^{2+m}), and the q^{2+m} drops.
    # Keeping it would put a w-dependent term ON the 5_2 hull (its valuation ties
    # the X^2 coefficient exactly) and contaminate the leading polynomial with w;
    # that is real, and it is the descendant deformation, not an exponent.
    descendant_on_hull = {}
    for nm in ("4_1", "5_2", "pretzel"):
        _, Pfull = ops[nm]
        A = KNOTS[nm]["A"]
        vN = val_q(sp.expand(q ** sp.Rational(A, 2) * W
                             * (coeffs(ops[nm][0])[A])))
        vD = sp.Integer(0)                       # -X^A has q-valuation 0
        descendant_on_hull[nm] = {"A": A, "val_q_of_offset_term_at_X^A": str(vN),
                                  "val_q_of_descendant_term": str(vD),
                                  "descendant_ties_the_hull": bool(vN == vD)}

    newt = {}
    for nm in ("4_1", "5_2", "pretzel"):
        pts, hull = newton(ops[nm][0])
        segs = [{"from": [int(a[0]), str(a[1])], "to": [int(b_[0]), str(b_[1])],
                 "slope_in_q": str((b_[1] - a[1]) / (b_[0] - a[0])),
                 "n_roots": int(b_[0] - a[0])}
                for a, b_ in zip(hull, hull[1:])]
        newt[nm] = {"points": [[int(p[0]), str(p[1])] for p in pts], "segments": segs}
        print(f"  {nm}: (j, val_q) = {[(int(p[0]), str(p[1])) for p in pts]}")
        for sg in segs:
            print(f"      {sg['from']} -> {sg['to']}   slope {sg['slope_in_q']}   "
                  f"{sg['n_roots']} root(s)")
    data["newton"] = newt
    data["descendant_term_position"] = descendant_on_hull

    # 5_2: single segment, leading polynomial
    pts52, hull52 = newton(ops["5_2"][0])
    a, b_ = hull52[0], hull52[-1]
    slope52 = (b_[1] - a[1]) / (b_[0] - a[0])
    lead52 = segment_leading_poly(ops["5_2"][0], int(a[0]), a[1], slope52)
    tgt52 = sp.expand((Y + 1) * (Y**2 + (x + 1 / x) * Y + 1))
    ok52 = sp.simplify(sp.expand(lead52 / sp.LC(sp.Poly(lead52, Y)) - tgt52)) == 0
    check("G7a-5_2 exponents: the (single) Newton segment has slope -1/2 and leading polynomial "
          "proportional to Y^3 + s Y^2 + s Y + 1 = (Y + 1)(Y^2 + (x + 1/x) Y + 1), roots "
          "Y in {-1, -x, -1/x}.  The q -> 0 exponents are the ADJOINT WEIGHT SET of x, up to sign -- "
          "which is why s(x) = e1 = e2 appears in GGM (188) / (307).",
          ok52, slope=str(slope52), leading_poly=str(lead52),
          factored=str(sp.factor(lead52)),
          roots=[str(r) for r in sp.roots(sp.Poly(sp.expand(lead52), Y))])

    # pretzel: the long segment
    ptspz, hullpz = newton(ops["pretzel"][0])
    longseg = None
    for a, b_ in zip(hullpz, hullpz[1:]):
        sl = (b_[1] - a[1]) / (b_[0] - a[0])
        if int(b_[0] - a[0]) >= 3:
            longseg = (a, b_, sl)
    leadpz = sp.Integer(0)
    if longseg:
        a, b_, sl = longseg
        leadpz = segment_leading_poly(ops["pretzel"][0], int(a[0]), a[1], sl)
    quad = sp.expand(Y**2 + SIGMA * Y + 1)
    rem = sp.simplify(sp.rem(sp.Poly(sp.expand(leadpz), Y), sp.Poly(quad, Y)).as_expr()) \
        if leadpz != 0 else sp.Integer(1)
    print("  pretzel long-segment leading polynomial:", leadpz)
    print("  factored:", sp.factor(leadpz))
    check("G7b-PRETZEL exponents: the Newton polygon splits 2 + 4 across a q^{1/2} step -- the level-2 "
          "signature.  The long (4-root) segment's leading polynomial is divisible by "
          "Y^2 + sigma Y + 1, whose roots are Y = -x^{1/2} and Y = -x^{-1/2}.  So the x-dependent "
          "q -> 0 exponents of the pretzel are the adjoint weights of x^{1/2}, NOT of x.",
          leadpz != 0 and rem == 0,
          n_segments=len(newt["pretzel"]["segments"]),
          segment_root_counts=[s["n_roots"] for s in newt["pretzel"]["segments"]],
          segment_slopes=[s["slope_in_q"] for s in newt["pretzel"]["segments"]],
          leading_poly=str(leadpz), factored=str(sp.factor(leadpz)),
          quadratic_factor="Y^2 + sigma Y + 1  (roots -x^{1/2}, -x^{-1/2})")
    data["pretzel_long_segment"] = {"leading_poly": str(leadpz),
                                    "factored": str(sp.factor(leadpz))}

    print("\n=== Part 3: the criterion, where GGM print the answer ===\n")
    S41p = sp.Matrix([[1, SX], [0, 1]])
    S41m = sp.Matrix([[1, 0], [-SX, 1]])
    M1 = sp.Matrix([[1, 0, 0], [0, 1, 0], [-SX, 0, 1]])
    M2 = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, SX, 1]])
    M3 = sp.Matrix([[1, SX + 1, 0], [0, 1, 0], [0, 0, 1]])
    S52p = sp.expand(M1 * M2 * M3)
    want52 = sp.Matrix([[1, SX + 1, 0], [0, 1, 0], [-SX, -SX**2, 1]])
    ok7 = sp.simplify(S52p - want52) == sp.zeros(3, 3)
    print("  4_1  S+(x;0) =", S41p.tolist())
    print("  5_2  S+(x;0) =", sp.expand(S52p).tolist())
    check("G6-the criterion: GGM (188) for 4_1 and (307) for 5_2, multiplied out, have every entry in "
          "Z[s(x)]: 4_1 gives [[1, s], [0, 1]] and 5_2 gives [[1, s+1, 0], [0, 1, 0], [-s, -s^2, 1]]. "
          "At x = 1, s(1) = 3, and these are GGM (59) / (96) with Stokes constants 3 and (4, 3, 3).",
          ok7, S_plus_41=str(S41p.tolist()), S_minus_41=str(S41m.tolist()),
          S_plus_52=str(sp.expand(S52p).tolist()),
          S_plus_41_at_x1=str(S41p.subs(XR, 1).tolist()),
          S_plus_52_at_x1=str(sp.expand(S52p).subs(XR, 1).tolist()))
    data["printed_stokes_q0"] = {
        "S_plus_41": str(S41p.tolist()), "S_minus_41": str(S41m.tolist()),
        "S_plus_52": str(sp.expand(S52p).tolist()),
        "S_plus_52_at_x1": str(sp.expand(S52p).subs(XR, 1).tolist())}

    print("\n=== Part 4: numerical gates ===\n")
    pw = {}
    for nm in ("4_1", "5_2", "pretzel"):
        pw[nm] = pointwise_identity(nm)
        print(f"  pointwise  {nm:8s}  worst rel err {pw[nm]['worst_rel_err']}")
    data["pointwise_identity"] = pw
    check("G3-the (FE)-rearranged integrand identity  integrand(v - i b)/integrand(v) = "
          "q^{A/2} w X^{-A} N(X)  holds pointwise for ALL THREE knots (mpmath, dps 30; two values of b, "
          "three of v each).  This validates the operator algebra of (OP) independently of any contour.",
          all(pw[nm]["worst_float"] < 1e-25 for nm in pw),
          worst_rel_err={nm: pw[nm]["worst_rel_err"] for nm in pw})

    rec = {}
    for nm in ("4_1", "5_2", "pretzel"):
        rec[nm] = integral_recurrence(nm)
        for r in rec[nm]:
            print(f"  recurrence {nm:8s}  {r.get('rel_residual', r.get('status'))}")
    data["integral_recurrence"] = rec

    for nm, note in (("4_1", "degree 2"), ("5_2", "degree 3, coefficients (1, s, s, 1)"),
                     ("pretzel", "DEGREE 6 -- the decisive gate")):
        vals = [r["rel_float"] for r in rec[nm] if "rel_float" in r]
        check(f"G4-{nm}: the derived recurrence sum_j c_j Z(t - i (j - A) b) = 0 holds on the ACTUAL "
              f"state integral (mpmath, dps 30, two (b, eps) choices, t_I centred in the common "
              f"convergence window).  {note}.  This tests the contour shift as well as the algebra.  "
              f"The residual here is QUADRATURE-limited, not arithmetic-limited: the integrand is a "
              f"Gaussian chirp whose oscillation frequency grows linearly in |v|, so mp.quad's node "
              f"density -- not dps -- sets the floor.  G3 is the exact algebraic gate (~1e-29); this "
              f"one corroborates the CONTOUR SHIFT, which G3 cannot see.",
              bool(vals) and max(vals) < 1e-13,
              worst_rel_residual=max(vals) if vals else None,
              rows=[{k: v for k, v in r.items() if k != "rel_float"} for r in rec[nm]])

    print("\n=== Verdict ===\n")
    verdict = (
        "DERIVED, from held text only (GK arxiv-1304.2705v1 (1) for Phi_b; GGM arxiv-2012.00062v3 "
        "(188), (239), (276), (307), (321), (332)).  The descendant q-difference operator of a "
        "one-dimensional state integral follows from the contour shift v -> v - i b and Faddeev's "
        "functional equation: P(X) = q^{A/2} w N(X) - X^A with N the product of the shift factors. "
        "Its q -> 0 characteristic roots are the exponents the q -> 0 Stokes matrix is built from. "
        "GATE 5_2: offsets {1, x, 1/x} -- the adjoint weight set -- give N = (1, s, s, 1), "
        "reproducing GGM (276) EXACTLY; s(x) is e1 = e2 of that set, which is the mechanism behind "
        "GGM (307).  GATE 4_1: offsets {x, 1}, N = (1, 1+x, x), and s(x) = (1 + x + x^2)/x surfaces "
        "in (188) through the (327) theta-renormalisation.  "
        "PRETZEL (-2,3,7): the doubled dilogarithm Phi_b(2v - c_b) shifts by -2 i b and contributes "
        "TWO factors, so the operator has DEGREE 6 -- the rank, confirmed independently of GZ.  Its "
        "x-dependence is entirely through sigma = x^{1/2} + x^{-1/2} = s(x^{1/2}) - 1.  The Newton "
        "polygon splits the six exponents 2 + 4 across a q^{1/2} step, and the x-dependent pair are "
        "the roots of Y^2 + sigma Y + 1, i.e. -x^{1/2} and -x^{-1/2}.  "
        "S(X) VERDICT: NO -- the pretzel's q -> 0 Stokes data is not built from s(x) = x + 1 + 1/x. "
        "It is built from sigma = s(x^{1/2}) - 1, which satisfies sigma^2 = s(x) + 1 and generates a "
        "DEGREE-2 extension of Z[s(x)].  The operator carries an exact Z/2 grading in which sigma is "
        "odd precisely when q is half-integral, so 'level 2' and 'the quadratic extension of Z[s(x)]' "
        "are the same phenomenon.  The refinement that follows: Stokes entries at INTEGER powers of q "
        "carry EVEN powers of sigma and therefore DO lie in Z[s(x)] -- consistent with the parent "
        "session's independently derived sigma_1 sigma_1 rotated index, whose coefficients are "
        "polynomials in s(zeta) with integer powers of zeta only -- while entries at HALF-INTEGER "
        "powers of q carry odd powers of sigma and do not.  "
        "SCOPE (a).  This is a statement about the q -> 0 exponents of the derived descendant operator, "
        "hence about the RING the Stokes entries lie in.  It does NOT produce the pretzel's S+(x;q) "
        "entry by entry: GGM fix the left and right GL(r) normalisation matrices per knot ((187a) for "
        "4_1, (305a) for 5_2), and those come from the four region matrices M_R(x;q) ((186a)-(186d) for "
        "4_1, (94a)-(94d) for 5_2).  No held source prints the analogue for a rank-6, level-2 knot; "
        "that is the precise missing input, and it is a normalisation, not new q-series data."
    )
    print(" " + verdict)

    from qou_substrate.witness import WitnessBuilder as _WB
    wit = {
        "name": "aomega-m3-pretzel-level2-stokes",
        "description": "The (-2,3,7) pretzel's level-2 descendant q-difference operator, derived from "
                       "its state integral by contour shift + Faddeev's functional equation; its "
                       "q -> 0 exponents by Newton polygon; and the s(x) = x + 1 + 1/x verdict.  "
                       "Gated on 4_1 and 5_2, where the same derivation reproduces GGM (276)/(332) "
                       "exactly and GGM print the q -> 0 Stokes matrices (188)/(307).",
        "computation": "aomega-m3-pretzel-level2-stokes",
        "engine": "python+sympy+mpmath",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-13-pretzel-level2-stokes-matrix.md",
        "parameters": {
            "mp_dps_numerical_gates": 30,
            "symbolic": "exact sympy over Q(q^{1/2}, x^{1/2}, w); no float64 anywhere",
            "conventions": "x = e^{2 pi b u}, w = e^{2 pi b t}, q = e^{2 pi i b^2}, "
                           "c_b = i(b + 1/b)/2, sigma = x^{1/2} + x^{-1/2}, s(x) = x + 1 + 1/x (GGM (239))",
            "held_sources": [
                "library/arxiv-2012.00062v3 (GGM, Peacock patterns and resurgence in complex "
                "Chern-Simons theory): (186), (187a), (188), (239), (276), (305a), (307), (321), "
                "(326), (327), (331), (332)",
                "library/arxiv-2111.06645 (GZ, Knots and their related q-series; the directory is "
                "mis-keyed, the PDF is arXiv 2304.09377v2): SS3.5, SS4, SS4.1, SS5.2",
                "library/arxiv-1304.2705v1 (Garoufalidis-Kashaev, From state integrals to q-series): (1)",
            ],
            "integrands": {
                "4_1": "int Phi_b(v+u) Phi_b(v) e^{-pi i v^2 + 2 pi i v t} dv",
                "5_2": "int Phi_b(v) Phi_b(v+u) Phi_b(v-u) e^{-2 pi i v^2 + 2 pi i v t} dv",
                "pretzel": "int Phi_b(v+u/2) Phi_b(v-u/2) Phi_b(2v-c_b) e^{-2 pi i v^2 + 2 pi i v t} dv",
            },
        },
        "data": data,
        "verdict": verdict,
        "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(wit, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-level2-stokes.witness.json")
    with open(out, "w") as fh:
        json.dump(wit, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  "
          f"[{time.time() - t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
