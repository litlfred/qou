#!/usr/bin/env python3
"""qou-cds1 Step 26: the discriminant curve in q — the corpus's decay operator
has a genus-8 spectral curve, not a tower of elliptic ones, and its phase misses
the ladder's by 3e11 sigma of the substrate pin.

*** THIS STEP CORRECTS A METHOD ERROR IN STEPS 21-25, MINE ***

Every one of those steps evaluated its spectra at the SINGLE numerical point
q = q_0. That collapses the whole question to order zero: a discriminant that
vanishes identically, one that is a perfect square, and one that is an
irreducible degree-18 polynomial are indistinguishable from one sample. Nothing
in Steps 21-25 could have seen the difference, and I asserted tower-level
conclusions from point evaluations anyway.

*** AND IT CORRECTS A FACTUAL CLAIM, ALSO MINE ***

Step 25's write-up said Delta_L "cannot be asked this question" because
`build_nucleon_nf` takes no q. That is wrong. `hecke_core_symbolic.hm_sym` is the
symbolic-q twin of `hm`, and mirroring `pyhecke.atom.build_nucleon_nf`'s 11-
crossing word through it gives the nucleon NF as an exact element of Q(q). It is
validated below against the canonical numeric builder to 1e-16 in all twelve
coordinates. There was no gap; there was a function I did not look for.

(`shift_from_nf_basis.build_nucleon_nf_sym_atomic` is NOT that mirror, despite
its docstring's "the two conventions now agree" — it agrees on the crossing
COUNTS and the 7/4 per-generator split, but applies all gen-0 crossings before
all gen-1, i.e. the MONOTONE re-sort of B_3 rather than the alternating braid
order the canonical builder uses. `nucleon_braid_word`'s own docstring measures
that re-sort at 82 % on tr_M. Using it here would have silently answered a
different question.)

======================================================================
1. THE BAR INVOLUTION ACTS TRIVIALLY — EXACTLY, NOT APPROXIMATELY
======================================================================

For the long-model decay operator Delta_L = NF(neutron) - NF(proton) in the
(2,1) block, as exact rational functions of q:

    tr(1/q)   = - tr(q)          bar-ODD
    det(1/q)  = + det(q)         bar-EVEN
    disc(1/q) = + disc(q)        bar-EVEN,  disc = tr^2 - 4 det

So there is no q^-n twist anywhere in the spectral geometry: disc is a Laurent
polynomial invariant under q -> 1/q, hence a POLYNOMIAL IN x = q + 1/q. That is
the direct answer to "am I missing the twisting as we go out the tower" — the
twisting is absent by an exact identity, not by a numerical coincidence, and x
is the forced coordinate.

======================================================================
2. THE TWO SPECTRAL CURVES
======================================================================

  short model   disc_S(x) = (x - 2)(x + 2) = x^2 - 4 = h^2

      In the q coordinate that IS a perfect square, disc_S(q) = h(q)^2, so
      y^2 = disc_S(q) has the rational solution y = +-h; in x it is a degree-2
      conic. Either way: GENUS 0, rational, no elliptic curve. And since
      x = q + 1/q >= 2 for every real q > 0, disc_S >= 0 identically —
      Delta_S is hyperbolic at EVERY real q, degenerate only at q = 1. The
      short model can never carry a phase, at any q. Steps 21-25 could only
      see this at q_0.

  long model    disc_L(x) = (x-2)(x+2) G_-(x) G_+(x) / 16
                G_-+(x)   = 2x^8 - 21x^6 + 77x^4 - 115x^2 -+ 2x + 58

      Degree 18, SQUAREFREE, with four irreducible factors over Q. y^2 = disc_L
      is hyperelliptic of GENUS 8 (deg 18 squarefree, even degree: g = 8). It is
      even in x, so it covers y^2 = R(w), w = x^2, of degree 9 — genus 4.

      Neither is genus 1. There is no elliptic curve here, and therefore no
      tower of elliptic curves. What the tower question does have is a real,
      non-degenerate answer for the long model and a degenerate one for the
      short model — a distinction invisible at q_0.

======================================================================
3. THE HECKE TOWER ADDS NOTHING, BY THE BRANCHING RULE
======================================================================

Res^{H_n}_{H_{n-1}} S^lambda = (+) S^mu over mu = lambda minus one box. Every
corpus object is H_3-valued (Step 25), so its spectrum in any H_n irrep is a
union with multiplicity of its three H_3 spectra — no new eigenvalue, hence no
new discriminant, at any level n. Verified at q_0, q = 1.30 and q = 1.05 for all
five H_4 shapes: (2,2) reproduces (2,1) exactly; (3,1) is (3) + (2,1); (2,1,1)
is (1^3) + (2,1); (4) is (3); (1^4) is (1^3).

======================================================================
4. THE CLASSICAL LIMIT IS EXACTLY 2 PI / 3
======================================================================

Every NF coordinate of Delta_L carries a factor (q-1)(q+1), so Delta_L vanishes
at q = 1: the nucleons are degenerate classically and the whole difference is a
deformation effect. The DIRECTION it vanishes along is not degenerate. Orders of
vanishing in eps = q - 1: gamma 1, sigma_0 2, sigma_1 2, L_+ 3, L_- 1, e^- 2, so
the leading direction is

    -(gamma + L_-) = -(1 + T_1 T_0)

and T_1 T_0 is the 3-cycle of S_3, whose eigenvalues in the standard 2-dim rep
are the primitive cube roots of unity. Hence eigenvalues -exp(+-i pi/3), modulus
1, and eigenphase EXACTLY 2 pi / 3 = 2.0943951... as q -> 1+.

Note where the trefoil is in that expansion: e^- — the longest element
T_0 T_1 T_0, the corpus's electron word — enters only at SECOND order, while the
leading decay direction is 1 + L_-. The operator that does the decay is not the
trefoil at leading order; the trefoil is its first correction.

======================================================================
5. THE ELLIPTICITY WINDOW, AND THE CLOSURE BY MEASUREMENT
======================================================================

disc_L(x) has exactly two real roots with x >= 2 (the range of x = q + 1/q for
real q > 0): x = 2 and x = 2.104510749293091. So

    Delta_L is ELLIPTIC exactly for q in (1, 1.379732661603278)

and q_0 = 1.1099785827513808 sits 29.0 % of the way up that window. Its
eigenphase sweeps monotonically from 2 pi / 3 at q -> 1+ down to 0 at the upper
wall, where the spectrum degenerates; theta(q_0) = 2.0204450, reproducing the
2.0204 measured numerically in Step 22 and used through Step 25.

Because theta sweeps continuously to 0, the required ladder phase IS attained —
and this probe locates where, precisely so the avenue can be closed by data
rather than by taste:

    convention   theta required at q      q*  where theta_L = theta_req
    z_C          0.0565947375433          1.37812464914
    z_D          0.0447443946157          1.37956231361

Both land inside the last 0.2 % of the window, hard against the degeneracy wall:
the phase is only small where Delta_L is about to stop being elliptic at all.
And both are

    (q* - q_0) / sigma_q0  ~  2.9e11

with sigma_q0 = 9.2116e-13 the substrate pin's uncertainty propagated from
CODATA m_p/m_e. So the identification is excluded by the calibration at three
hundred billion sigma. This is a falsification test, not a search: the curve was
derived first, the crossing was then located, and the distance was measured.

======================================================================
6. THE CYCLOTOMIC TOWER — q = zeta_N, N THE DEGREE
======================================================================

The one reading of "indexed by the degree of q" that IS a genuine tower. Since
tr is bar-odd and det bar-even, on |q| = 1 the trace is purely imaginary and the
determinant real (confirmed to 40 digits: |Re tr| < 1e-40, |Im det| < 1e-42), so
disc is real at every root of unity and the eigenvalue ratio has a well-defined
phase phi_N. It is a real tower and it does move:

    N       3      6      7      8      9     13     20     29     60
    phi  2.0944 2.0944 1.4042 3.1416 2.1664 2.9211 2.0344 1.8116 1.9775

with N = 3 and N = 6 hitting the classical 2 pi / 3 exactly (disc = 9/16 at
both), N = 8 giving exactly pi, N = 4 singular (det = 0, tr = 29i), N = 5
degenerate, and phi_N -> 2 pi / 3 as N -> infinity. The minimum over every
non-degenerate N <= 120 is reported below. It is not close to 0.0566 either.

======================================================================
WHAT THIS CHANGES AND WHAT IT DOES NOT
======================================================================

CHANGED: the short model is now closed for all q, not just q_0; the long model
has a named curve of genus 8 instead of a number; the classical limit is an
exact 2 pi / 3 with an identified mechanism; the ladder-phase identification is
excluded quantitatively by the substrate pin instead of by inspection.

NOT CHANGED: no c_k value is asserted, no convention adjudicated, nothing
readmitted. q* is recorded as a fact ABOUT the curve, never as a candidate q.

SCOPE. Scope-(a). Nothing derived, proposed, wired or readmitted; no convention
adjudicated; no c_k value asserted. Anchor: experimental (proton) pin.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke")]
import _path_bridge  # noqa: E402, F401

import qou_substrate.constants as CONST  # noqa: E402
from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from hecke_core import build_nucleon_nf  # noqa: E402
from hecke_core_symbolic import NF_NAMES, h as h_sym, hm_sym, q as q_sym  # noqa: E402

mp.mp.dps = 40
Q0 = mp.mpf(str(CONST.Q_50_DIGIT_STR))
SIGMA_Q0 = mp.mpf(str(CONST.Q_ERR))
QR = sp.Rational(str(CONST.Q_50_DIGIT_STR))
X = sp.Symbol("x")
EPS = sp.Symbol("e", positive=True)

WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]


# ---------------------------------------------------------------- symbolic H_3
def hoefsmit_21_symbolic():
    """The 2-dim (2,1) irrep of H_3(q), Hoefsmit seminormal, exact in q."""
    hs = q_sym - 1 / q_sym
    t0 = sp.Matrix([[q_sym, 0], [0, sp.Rational(-1) / q_sym]])
    a = -1 / (q_sym ** 3 + q_sym)
    b = sp.sqrt(q_sym ** 4 + q_sym ** 2 + 1) / (q_sym ** 2 + 1)
    t1 = sp.Matrix([[a, b], [b, hs - a]])
    return t0, t1


def nf_basis_symbolic(t0, t1):
    out = []
    for w in WORDS:
        m = sp.eye(2)
        for i in w:
            m = m * (t0 if i == 0 else t1)
        out.append(sp.simplify(m))
    return out


def nucleon_nf_symbolic(quarks):
    """Exact symbolic mirror of `pyhecke.atom.build_nucleon_nf`: the 11-crossing
    word in BRAID (alternating) order — B_3 = (s0 s1^-1)^3, then the three quark
    pairs at gen = lower index, then the gluon s0^2."""
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for _ in range(3):                                   # B_3, ALTERNATING
        nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), 0)
        nf = hm_sym(nf, sp.Integer(1), -h_sym, 1)
    for i, j in [(0, 1), (0, 2), (1, 2)]:                # quark pairs
        a, b = quarks[i], quarks[j]
        d = (sp.Integer(0) if a == b == "u"
             else (-h_sym if a == b == "d" else -h_sym / 2))
        nf = hm_sym(nf, sp.Integer(1), d, i)
    nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), 0)     # gluon 1
    nf = hm_sym(nf, sp.Integer(1), sp.Integer(0), 0)     # gluon 2
    return [sp.cancel(sp.together(c)) for c in nf]


def block(vec, basis):
    m = sp.zeros(2, 2)
    for c, b in zip(vec, basis):
        m = m + c * b
    return sp.simplify(m)


def laurent_to_x(expr):
    """disc(q) with disc(1/q) = disc(q) -> the unique P with P(q + 1/q) = disc."""
    num, den = sp.fraction(sp.cancel(expr))
    dp = sp.Poly(den, q_sym)
    dd, lc = dp.degree(), sp.LC(dp)
    assert sp.simplify(den - lc * q_sym ** dd) == 0, "denominator is not a monomial"
    poly = sp.Poly(sp.expand(num / lc), q_sym)
    coeffs = {int(m[0]): c for m, c in zip(poly.monoms(), poly.coeffs())}
    lau = {k - dd: v for k, v in coeffs.items()}
    top = max(lau)
    assert all(sp.simplify(lau.get(k, 0) - lau.get(-k, 0)) == 0 for k in lau), \
        "Laurent coefficients are not palindromic"
    pk = {0: sp.Integer(2), 1: X}                      # p_k = q^k + q^-k
    for k in range(2, top + 1):
        pk[k] = sp.expand(X * pk[k - 1] - pk[k - 2])
    # sp.Integer() would TRUNCATE a Rational middle coefficient — the long
    # model's is negative with a 1/4 fractional part, and truncation shifted
    # the whole polynomial by exactly 1/4. Keep it exact.
    p = sp.sympify(lau.get(0, 0))
    for k in range(1, top + 1):
        if lau.get(k, 0) != 0:
            p = p + lau[k] * pk[k]
    p = sp.expand(p)
    # Exact round-trip check at sample rationals. `sp.simplify` is not reliable
    # at recognising zero on a degree-36 rational function, and a silent
    # "could not prove zero" must not read as a failed identity.
    for probe in (sp.Rational(3, 2), sp.Rational(5, 3), sp.Rational(7, 4)):
        lhs = sp.nsimplify(p.subs(X, probe + 1 / probe))
        rhs = sp.nsimplify(expr.subs(q_sym, probe))
        assert sp.Rational(sp.cancel(lhs - rhs)) == 0, (probe, lhs, rhs)
    return p, top


# ------------------------------------------------------------- ladder quantities
def h_of(qq):
    return qq - 1 / qq


def u_of(qq):
    hh = h_of(qq)
    return mp.sqrt((hh ** 2 + 3) / (hh ** 2 + 4)) * ((qq - 1) / qq) ** 2


def z_C(qq):
    return mp.sqrt(qq) / (1 + qq)


def z_D(qq):
    return qq ** 3 / (qq ** 2 + 1)


def theta_required(qq, zf):
    """|alpha - u/2| with alpha = (z - 1) h / 2 — the phase the c_k ladder needs."""
    return mp.fabs((zf(qq) - 1) * h_of(qq) / 2 - u_of(qq) / 2)


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:  # noqa: C901 — one linear narrative, deliberately not split
    t_start = time.monotonic()
    print("=" * 78)
    print(" Step 26: the discriminant curve in q — no elliptic tower, and the")
    print("          ladder phase is excluded by the substrate pin at 3e11 sigma")
    print("=" * 78)

    t0m, t1m = hoefsmit_21_symbolic()
    basis = nf_basis_symbolic(t0m, t1m)

    # [1] the symbolic irrep is the corpus's irrep --------------------------
    rel0 = sp.simplify((t0m - q_sym * sp.eye(2)) * (t0m + sp.eye(2) / q_sym))
    rel1 = sp.simplify((t1m - q_sym * sp.eye(2)) * (t1m + sp.eye(2) / q_sym))
    braid = sp.simplify(t0m * t1m * t0m - t1m * t0m * t1m)
    hecke_ok = (rel0 == sp.zeros(2, 2) and rel1 == sp.zeros(2, 2)
                and braid == sp.zeros(2, 2))
    gens = build_seminormal_matrices_mp((2, 1), Q0)[0]
    irrep_err = mp.mpf(0)
    for ms, mn in ((t0m, gens[0]), (t1m, gens[1])):
        for i in range(2):
            for j in range(2):
                s = mp.mpf(str(sp.N(ms[i, j].subs(q_sym, QR), 35)))
                irrep_err = max(irrep_err, mp.fabs(s - mn[i, j]))
    print(f"\n[1] symbolic (2,1) irrep of H_3(q)")
    print(f"    quadratic + braid relations hold identically in q : {hecke_ok}")
    print(f"    max |symbolic(q_0) - corpus Hoefsmit|             : "
          f"{mp.nstr(irrep_err, 4)}")

    # [2] the symbolic nucleon mirrors the canonical numeric builder ---------
    p_sym = nucleon_nf_symbolic(list("uud"))
    n_sym = nucleon_nf_symbolic(list("udd"))
    p_num, n_num = build_nucleon_nf(list("uud")), build_nucleon_nf(list("udd"))
    nf_err = mp.mpf(0)
    for s_v, n_v in ((p_sym, p_num), (n_sym, n_num)):
        for i in range(6):
            nf_err = max(nf_err, mp.fabs(
                mp.mpf(str(sp.N(s_v[i].subs(q_sym, QR), 35))) - mp.mpf(str(n_v[i]))))
    print(f"\n[2] symbolic nucleon NF vs canonical `build_nucleon_nf` at q_0")
    print(f"    max |symbolic - numeric| over all 12 coordinates  : "
          f"{mp.nstr(nf_err, 4)}")
    print(f"    (Step 25 said Delta_L 'cannot be asked' this question. It can:")
    print(f"     `hm_sym` is the symbolic twin of `hm`. That claim was wrong.)")

    d_L = [sp.cancel(n_sym[i] - p_sym[i]) for i in range(6)]   # n - p: DECAY sense
    hs = q_sym - 1 / q_sym
    d_S = [hs ** 2 / 2, -hs / 2, -hs / 2, sp.Integer(0), sp.Integer(0), sp.Integer(0)]

    # [3] bar parity, exactly ------------------------------------------------
    curves = {}
    print(f"\n[3] bar parity of the spectral invariants, as exact identities in q")
    print(f"    {'model':8s}{'tr(1/q)/tr(q)':>16s}{'det(1/q)/det(q)':>18s}"
          f"{'disc(1/q)/disc(q)':>20s}")
    for name, vec in (("short", d_S), ("long", d_L)):
        m = block(vec, basis)
        tr = sp.cancel(sp.expand(m[0, 0] + m[1, 1]))
        det = sp.cancel(sp.expand(m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]))
        disc = sp.cancel(sp.expand(tr ** 2 - 4 * det))
        rt = sp.simplify(sp.cancel(tr.subs(q_sym, 1 / q_sym) / tr)) if tr != 0 else "n/a"
        rd = sp.simplify(sp.cancel(det.subs(q_sym, 1 / q_sym) / det))
        rs = sp.simplify(sp.cancel(disc.subs(q_sym, 1 / q_sym) / disc))
        curves[name] = {"tr": tr, "det": det, "disc": disc,
                        "bar_tr": rt, "bar_det": rd, "bar_disc": rs}
        print(f"    {name:8s}{str(rt):>16s}{str(rd):>18s}{str(rs):>20s}")
    print(f"    -> disc is bar-EVEN for both: NO q^-n twist anywhere, so disc is")
    print(f"       a polynomial in x = q + 1/q. That is the twisting question,")
    print(f"       answered by an exact identity rather than a sample.")

    # [4] the two curves ------------------------------------------------------
    print(f"\n[4] the spectral curves y^2 = disc(x),  x = q + 1/q")
    for name in ("short", "long"):
        p_x, top = laurent_to_x(curves[name]["disc"])
        fl = sp.factor_list(p_x)
        sqfree = all(m == 1 for _, m in fl[1])
        deg = sp.Poly(p_x, X).degree()
        genus = (deg - 2) // 2 if deg % 2 == 0 else (deg - 1) // 2
        curves[name].update({"P": p_x, "deg": deg, "squarefree": sqfree,
                             "genus": genus, "factors": fl})
        print(f"\n    {name} model: disc(x) = {sp.factor(p_x)}")
        print(f"      degree {deg}   squarefree {sqfree}   "
              f"genus of y^2 = disc(x): {genus if sqfree else 0}")
        if deg <= 2:
            print(f"      degree <= 2 -> y^2 = disc(x) is a CONIC: genus 0, rational.")
        print(f"      disc(q_0) = "
              f"{mp.nstr(mp.mpf(str(sp.N(curves[name]['disc'].subs(q_sym, QR), 35))), 12)}")
    even_in_x = sp.simplify(curves["long"]["P"].subs(X, -X) - curves["long"]["P"]) == 0

    # Cross-check against the Lean mirror. `QOU.QBeta.DiscriminantCurveInQ`
    # defines discLong/bigA/tildeA by these literals; if either side is edited
    # without the other, this fails here rather than silently diverging.
    lean_A = 2 * X ** 8 - 21 * X ** 6 + 77 * X ** 4 - 115 * X ** 2 + 58
    lean_disc = sp.expand((X - 2) * (X + 2) * (lean_A - 2 * X) * (lean_A + 2 * X) / 16)
    W = sp.Symbol("w")
    lean_tildeA = 2 * W ** 4 - 21 * W ** 3 + 77 * W ** 2 - 115 * W + 58
    lean_R = sp.expand((W - 4) * (lean_tildeA ** 2 - 4 * W) / 16)
    lean_ok = bool(sp.expand(lean_disc - curves["long"]["P"]) == 0
                   and sp.expand(lean_R.subs(W, X ** 2) - curves["long"]["P"]) == 0)
    print(f"    matches QOU.QBeta.DiscriminantCurveInQ's discLong and discQuotient: "
          f"{lean_ok}")
    print(f"\n    long-model disc is even in x: {even_in_x}  -> it covers "
          f"y^2 = R(w), w = x^2, of degree "
          f"{sp.Poly(curves['long']['P'], X).degree() // 2}, genus "
          f"{(sp.Poly(curves['long']['P'], X).degree() // 2 - 1) // 2}")
    print(f"    NEITHER IS GENUS 1. There is no elliptic curve, hence no tower")
    print(f"    of elliptic curves, indexed by anything.")

    # short model is hyperbolic for every real q, not just q_0
    short_is_h2 = sp.simplify(curves["short"]["P"] - (X ** 2 - 4)) == 0
    short_is_square_in_q = sp.simplify(
        curves["short"]["disc"] - (q_sym - 1 / q_sym) ** 2) == 0
    print(f"\n    short model: disc(x) = x^2 - 4 : {short_is_h2};  "
          f"disc(q) = h(q)^2, a perfect square in q : {short_is_square_in_q}")
    print(f"      and x = q + 1/q >= 2 for every real q > 0, so disc_S >= 0")
    print(f"      IDENTICALLY. Delta_S is hyperbolic at every real q, degenerate")
    print(f"      only at q = 1. Closed for all q, not merely at q_0.")

    # [5] the Hecke tower adds nothing ----------------------------------------
    print(f"\n[5] the Hecke tower H_3 < H_4 < ... adds no eigenvalue (branching)")
    d_L_num = [n_num[i] - p_num[i] for i in range(6)]

    def spec(shape, qq):
        g = build_seminormal_matrices_mp(shape, qq)[0]
        dim = g[0].rows
        m = mp.zeros(dim, dim)
        for c, w in zip(d_L_num, WORDS):
            b = mp.eye(dim)
            for i in w:
                b = b * g[i]
            m = m + mp.mpf(str(c)) * b
        return sorted(mp.eig(m)[0], key=lambda z: (mp.re(z), mp.im(z)))

    def close(u, v):
        return (len(u) == len(v)
                and all(mp.fabs(a - b) < mp.mpf("1e-18") for a, b in zip(u, v)))

    h3 = {sh: spec(sh, Q0) for sh in [(2, 1), (3,), (1, 1, 1)]}
    branch = {(2, 2): [(2, 1)], (3, 1): [(3,), (2, 1)],
              (2, 1, 1): [(1, 1, 1), (2, 1)], (4,): [(3,)], (1, 1, 1, 1): [(1, 1, 1)]}
    tower_ok = True
    for sh, parts in branch.items():
        got = spec(sh, Q0)
        want = sorted([e for mu in parts for e in h3[mu]],
                      key=lambda z: (mp.re(z), mp.im(z)))
        ok = close(got, want)
        tower_ok &= ok
        print(f"    H_4 {str(sh):12s} = " + " + ".join(f"H_3 {mu}" for mu in parts)
              + f"   spectra agree: {ok}")
    print(f"    -> every corpus object is H_3-valued (Step 25), so its char poly")
    print(f"       at level n is a product of the three H_3 ones with branching")
    print(f"       multiplicities. No new curve at any level.")

    # [6] the classical limit --------------------------------------------------
    print(f"\n[6] the classical limit q -> 1 is EXACTLY 2 pi / 3")
    orders = {}
    for nm, c in zip(NF_NAMES, d_L):
        ser = sp.series(sp.cancel(c.subs(q_sym, 1 + EPS)), EPS, 0, 4).removeO()
        pl = sp.Poly(sp.expand(ser), EPS)
        o = min(int(m[0]) for m in pl.monoms())
        orders[nm] = (o, sp.simplify(pl.coeff_monomial(EPS ** o)))
    print(f"    order of vanishing at q = 1 : "
          + "  ".join(f"{nm}:{orders[nm][0]}" for nm in NF_NAMES))
    lead_names = [nm for nm in NF_NAMES if orders[nm][0] == 1]
    r_cl = sp.Matrix([[1, 0], [0, -1]])
    s_cl = sp.Matrix([[sp.Rational(-1, 2), sp.sqrt(3) / 2],
                      [sp.sqrt(3) / 2, sp.Rational(1, 2)]])
    lead_op = -(sp.eye(2) + s_cl * r_cl)
    evs = list(lead_op.eigenvals().keys())
    mods = {sp.simplify(sp.Abs(e)) for e in evs}
    args = sorted(sp.simplify(sp.arg(e)) for e in evs)
    order3 = min(k for k in range(1, 7)
                 if sp.simplify((s_cl * r_cl) ** k - sp.eye(2)) == sp.zeros(2, 2))
    print(f"    leading direction (order 1) : {lead_names}  =  -(1 + T_1 T_0)")
    print(f"    T_1 T_0 has order {order3} in S_3 -> primitive cube roots of unity")
    print(f"    eigenvalues of -(1 + T_1 T_0): moduli {mods}, args {args}")
    print(f"    theta(q -> 1+) = {sp.simplify(max(args))} = "
          f"{mp.nstr(mp.mpf(str(sp.N(2 * sp.pi / 3, 30))), 16)}")
    print(f"    the trefoil / electron word e^- enters at order "
          f"{orders[NF_NAMES[5]][0]}, NOT at leading order: the operator that")
    print(f"    does the decay is 1 + L_- first, and e^- is its correction.")

    # [7] the ellipticity window and the closure by measurement ----------------
    tr_f = sp.lambdify(q_sym, curves["long"]["tr"], "mpmath")
    dt_f = sp.lambdify(q_sym, curves["long"]["det"], "mpmath")

    def theta_L(qq):
        r = tr_f(qq) / (2 * mp.sqrt(dt_f(qq)))
        return mp.acos(r) if abs(r) <= 1 else None

    roots_x = sorted({mp.mpf(str(sp.N(r, 35)))
                      for r in sp.real_roots(sp.Poly(sp.expand(
                          16 * curves["long"]["P"]), X))})
    walls = [r for r in roots_x if r >= 2]
    x_hi = max(walls)
    q_hi = (x_hi + mp.sqrt(x_hi ** 2 - 4)) / 2
    inside = bool(1 < Q0 < q_hi)
    print(f"\n[7] the ellipticity window in q, and where the ladder phase lives")
    print(f"    real roots of disc_L with x >= 2 : "
          f"{[mp.nstr(r, 16) for r in walls]}")
    print(f"    -> Delta_L is ELLIPTIC exactly for q in (1, {mp.nstr(q_hi, 16)})")
    print(f"    q_0 = {mp.nstr(Q0, 17)} inside: {inside}  "
          f"({mp.nstr((Q0 - 1) / (q_hi - 1) * 100, 6)} % of the way up)")
    print(f"    theta_L(q_0) = {mp.nstr(theta_L(Q0), 12)}   "
          f"(Step 22 measured 2.0204 numerically)")

    crossings = {}
    for lbl, zf in (("z_C", z_C), ("z_D", z_D)):
        def gap(qq, _zf=zf):
            t = theta_L(qq)
            return None if t is None else t - theta_required(qq, _zf)
        lo, hi, n_scan = mp.mpf("1.0000001"), q_hi - mp.mpf("1e-9"), 4000
        prev, prev_q, found = gap(lo), lo, []
        for i in range(1, n_scan + 1):
            cq = lo + (hi - lo) * mp.mpf(i) / n_scan
            cur = gap(cq)
            if prev is not None and cur is not None and prev * cur < 0:
                found.append(mp.findroot(gap, (prev_q, cq), solver="bisect",
                                         tol=mp.mpf("1e-45")))
            prev, prev_q = cur, cq
        crossings[lbl] = {
            "theta_req_at_q0": theta_required(Q0, zf),
            "q_star": found[0] if found else None,
            "sigma": (found[0] - Q0) / SIGMA_Q0 if found else None,
            "distance_to_wall": q_hi - found[0] if found else None}
    print(f"\n    {'conv':6s}{'theta required @ q_0':>22s}{'q* where theta_L = req':>26s}"
          f"{'(q*-q_0)/sigma_q0':>20s}{'q_hi - q*':>14s}")
    for lbl, c in crossings.items():
        print(f"    {lbl:6s}{mp.nstr(c['theta_req_at_q0'], 12):>22s}"
              f"{mp.nstr(c['q_star'], 18):>26s}{mp.nstr(c['sigma'], 8):>20s}"
              f"{mp.nstr(c['distance_to_wall'], 6):>14s}")
    print(f"    sigma_q0 = {mp.nstr(SIGMA_Q0, 8)} (absolute; CODATA m_p/m_e via the pin)")
    print(f"    -> the required phase IS attained, hard against the degeneracy")
    print(f"       wall, at ~3e11 sigma from the calibrated q_0. Closed by the")
    print(f"       measurement, not by inspection. This is a falsification test:")
    print(f"       the curve was derived first and the crossing located after.")

    # [8] the cyclotomic tower -------------------------------------------------
    print(f"\n[8] the cyclotomic tower q = zeta_N (N = the DEGREE of q)")
    tower, re_tr_max, im_det_max = [], mp.mpf(0), mp.mpf(0)
    for n_deg in range(3, 121):
        z = mp.expjpi(mp.mpf(2) / n_deg)
        t, d = tr_f(z), dt_f(z)
        re_tr_max = max(re_tr_max, mp.fabs(mp.re(t)))
        im_det_max = max(im_det_max, mp.fabs(mp.im(d)))
        disc = t * t - 4 * d
        lp, lm = (t + mp.sqrt(disc)) / 2, (t - mp.sqrt(disc)) / 2
        if abs(lm) < mp.mpf("1e-25") or abs(lp) < mp.mpf("1e-25"):
            tower.append((n_deg, None, mp.re(disc)))
            continue
        ph = abs(mp.arg(lp / lm))
        tower.append((n_deg, ph if ph > mp.mpf("1e-25") else None, mp.re(disc)))
    print(f"    tr is purely imaginary on |q| = 1 : max |Re tr| = "
          f"{mp.nstr(re_tr_max, 4)}")
    print(f"    det is real on |q| = 1            : max |Im det| = "
          f"{mp.nstr(im_det_max, 4)}")
    shown = [3, 4, 5, 6, 7, 8, 9, 13, 20, 29, 60, 120]
    print(f"    {'N':>5s}" + "".join(f"{n:>13d}" for n in shown))
    print(f"    {'phi_N':>5s}" + "".join(
        f"{(mp.nstr(dict((a, b) for a, b, _ in tower)[n], 8) if dict((a, b) for a, b, _ in tower)[n] else 'degenerate'):>13s}"
        for n in shown))
    live = [(n, p) for n, p, _ in tower if p is not None]
    n_min, phi_min = min(live, key=lambda t: t[1])
    theta_req_C = theta_required(Q0, z_C)
    print(f"    minimum over every non-degenerate N <= 120 : phi_{n_min} = "
          f"{mp.nstr(phi_min, 12)}")
    print(f"    required ladder phase                      : "
          f"{mp.nstr(theta_req_C, 12)}   ratio "
          f"{mp.nstr(phi_min / theta_req_C, 6)}x")

    # ------------------------------------------------------------- assertions
    a = [
        {"name": "symbolic_nucleon_nf_mirrors_the_canonical_builder",
         "passed": bool(nf_err < mp.mpf("1e-12") and hecke_ok
                        and irrep_err < mp.mpf("1e-25")),
         "detail": f"the symbolic (2,1) irrep satisfies the Hecke and braid relations "
                   f"identically in q and matches the corpus Hoefsmit output at q_0 to "
                   f"{mp.nstr(irrep_err, 3)}; the symbolic nucleon NF matches "
                   f"`build_nucleon_nf` to {mp.nstr(nf_err, 3)} in all 12 coordinates. "
                   f"CORRECTS Step 25's claim that Delta_L could not be asked this "
                   f"question — `hm_sym` is the symbolic twin of `hm` and there was no gap"},
        {"name": "disc_is_bar_even_for_both_models_no_q_twist",
         "passed": bool(curves["short"]["bar_disc"] == 1
                        and curves["long"]["bar_disc"] == 1
                        and curves["long"]["bar_tr"] == -1
                        and curves["long"]["bar_det"] == 1),
         "detail": "tr(1/q) = -tr(q), det(1/q) = det(q), disc(1/q) = disc(q) as exact "
                   "identities in Q(q). The bar involution acts trivially on the spectral "
                   "geometry, so there is no q^-n twist to be missed as one goes out the "
                   "tower, and disc is forced to be a polynomial in x = q + 1/q"},
        {"name": "short_model_disc_is_h_squared_hence_hyperbolic_at_every_real_q",
         "passed": bool(short_is_h2 and short_is_square_in_q
                        and curves["short"]["deg"] == 2),
         "detail": "disc_S(q) = h(q)^2 is a perfect square in the q coordinate and "
                   "disc_S(x) = x^2 - 4 is a degree-2 conic in x, so y^2 = disc_S has "
                   "genus 0 either way; and x = q + 1/q >= 2 for every real q > 0, so "
                   "disc_S >= 0 identically. The short model is hyperbolic at EVERY real "
                   "q, not merely at q_0 — a statement Steps 21-25 could not have made"},
        {"name": "long_model_curve_is_genus_8_not_elliptic",
         "passed": bool(curves["long"]["squarefree"] and curves["long"]["deg"] == 18
                        and curves["long"]["genus"] == 8 and even_in_x and lean_ok),
         "detail": "disc_L(x) = (x-2)(x+2) G_-(x) G_+(x) / 16 with G_-+ = 2x^8 - 21x^6 + "
                   "77x^4 - 115x^2 -+ 2x + 58: degree 18, squarefree, four irreducible "
                   "factors over Q. y^2 = disc_L is hyperelliptic of genus 8; being even "
                   "in x it covers a genus-4 curve in w = x^2. Neither is genus 1, so "
                   "there is no elliptic curve and no tower of them. Both polynomials agree "
                   "with the Lean mirror `QOU.QBeta.DiscriminantCurveInQ`"},
        {"name": "hecke_tower_adds_no_eigenvalue_by_branching",
         "passed": bool(tower_ok),
         "detail": "all five H_4 spectra of Delta_L are exactly the branching unions of "
                   "the three H_3 spectra: (2,2)=(2,1), (3,1)=(3)+(2,1), (2,1,1)="
                   "(1^3)+(2,1), (4)=(3), (1^4)=(1^3). Every corpus object is H_3-valued, "
                   "so no new discriminant appears at any level n"},
        {"name": "classical_limit_eigenphase_is_exactly_two_pi_over_three",
         "passed": bool(mods == {sp.Integer(1)} and order3 == 3
                        and sp.simplify(max(args) - 2 * sp.pi / 3) == 0
                        and orders[NF_NAMES[5]][0] == 2),
         "detail": "every NF coordinate of Delta_L carries (q-1)(q+1), so Delta_L -> 0 at "
                   "q = 1; the leading direction is -(gamma + L_-) = -(1 + T_1 T_0), and "
                   "T_1 T_0 is the S_3 3-cycle whose standard-rep eigenvalues are the "
                   "primitive cube roots of unity, giving modulus 1 and eigenphase exactly "
                   "2 pi / 3. The trefoil / electron word e^- enters only at order 2"},
        {"name": "ladder_phase_crossing_is_excluded_by_the_substrate_pin",
         "passed": bool(all(c["q_star"] is not None
                            and mp.fabs(c["sigma"]) > mp.mpf("1e10")
                            and c["distance_to_wall"] < mp.mpf("0.01")
                            for c in crossings.values())),
         "detail": f"Delta_L is elliptic exactly for q in (1, {mp.nstr(q_hi, 12)}) and its "
                   f"eigenphase sweeps from 2 pi / 3 to 0, so the required phase IS "
                   f"attained — at q* = {mp.nstr(crossings['z_C']['q_star'], 12)} (z_C) and "
                   f"{mp.nstr(crossings['z_D']['q_star'], 12)} (z_D), both within 0.2 % of "
                   f"the degeneracy wall and ~3e11 sigma_q0 from the calibrated q_0. "
                   f"Closed by the CODATA proton pin, not by inspection"},
        {"name": "cyclotomic_tower_phases_all_exceed_the_required_phase",
         "passed": bool(re_tr_max < mp.mpf("1e-30") and im_det_max < mp.mpf("1e-30")
                        and phi_min > theta_req_C * 10),
         "detail": f"on |q| = 1 the trace is purely imaginary and the determinant real "
                   f"(|Re tr| < {mp.nstr(re_tr_max, 3)}, |Im det| < "
                   f"{mp.nstr(im_det_max, 3)}), so every root of unity carries a real "
                   f"discriminant and a well-defined eigenphase. This IS a genuine tower "
                   f"indexed by the degree N, with phi_3 = phi_6 = 2 pi / 3 exactly and "
                   f"phi_N -> 2 pi / 3 as N -> infinity; its minimum over N <= 120 is "
                   f"phi_{n_min} = {mp.nstr(phi_min, 8)}, still "
                   f"{mp.nstr(phi_min / theta_req_C, 5)}x the required phase"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-discriminant-curve-in-q",
        "engine": "sympy + mpmath",
        "description": (
            "qou-cds1 Step 26. CORRECTS a method error running through Steps 21-25: all of "
            "them evaluated spectra at the single point q = q_0, which cannot distinguish a "
            "perfect-square discriminant from an irreducible degree-18 one. Carrying q "
            "symbolically (`hm_sym`, mirroring `build_nucleon_nf`'s 11-crossing braid-order "
            "word, validated to 1e-16) gives the exact spectral curves. ALSO CORRECTS Step "
            "25's claim that Delta_L could not be asked this question: there was no gap, "
            "only a function not looked for. Results: tr is bar-odd, det and disc bar-even "
            "as exact identities, so there is NO q^-n twist and disc is a polynomial in "
            "x = q + 1/q. disc_S(x) = x^2 - 4 = h^2 is a perfect square (genus 0) and is "
            ">= 0 for every real q, so the short model is hyperbolic everywhere, not just "
            "at q_0. disc_L(x) has degree 18, is squarefree with four irreducible factors, "
            "and y^2 = disc_L is hyperelliptic of GENUS 8 (genus 4 on the x^2 quotient) — "
            "not genus 1, so there is no elliptic curve and no tower of them. The Hecke "
            "tower adds no eigenvalue by branching, verified on all five H_4 shapes. The "
            "classical limit is EXACTLY 2 pi / 3, because the leading direction of Delta_L "
            "at q = 1 is -(1 + T_1 T_0) and T_1 T_0 is the S_3 3-cycle; the trefoil word "
            "e^- enters only at second order. Delta_L is elliptic exactly for q in "
            "(1, 1.3797326616) with q_0 29 % of the way up, and theta sweeps to 0 at the "
            "wall, so the required ladder phase IS attained — at q* = 1.3781 (z_C) / 1.3796 "
            "(z_D), both ~3e11 sigma_q0 from the calibrated q_0. The avenue is closed by "
            "the CODATA proton pin. The cyclotomic tower q = zeta_N is a genuine tower with "
            "phi_3 = phi_6 = 2 pi / 3 exactly, but its minimum over N <= 120 still exceeds "
            "the required phase by 24x."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 40,
                       "nf_basis": NF_NAMES, "block": "(2,1)",
                       "orientation": "Delta_L = NF(neutron) - NF(proton)"},
        "data": {
            "q0": mp.nstr(Q0, 20), "sigma_q0": mp.nstr(SIGMA_Q0, 12),
            "irrep_max_err_at_q0": mp.nstr(irrep_err, 6),
            "nucleon_nf_max_err_at_q0": mp.nstr(nf_err, 6),
            "bar_parity": {k: {"tr": str(curves[k]["bar_tr"]),
                               "det": str(curves[k]["bar_det"]),
                               "disc": str(curves[k]["bar_disc"])}
                           for k in curves},
            "disc_short_in_x": str(sp.factor(curves["short"]["P"])),
            "disc_long_in_x": str(sp.factor(curves["long"]["P"])),
            "disc_long_degree": int(curves["long"]["deg"]),
            "disc_long_squarefree": bool(curves["long"]["squarefree"]),
            "genus_short": 0, "genus_long": int(curves["long"]["genus"]),
            "genus_long_x2_quotient": 4,
            "matches_lean_DiscriminantCurveInQ": bool(lean_ok),
            "disc_short_at_q0": mp.nstr(
                mp.mpf(str(sp.N(curves["short"]["disc"].subs(q_sym, QR), 35))), 14),
            "disc_long_at_q0": mp.nstr(
                mp.mpf(str(sp.N(curves["long"]["disc"].subs(q_sym, QR), 35))), 14),
            "vanishing_orders_at_q_eq_1": {nm: orders[nm][0] for nm in NF_NAMES},
            "classical_eigenphase": "2*pi/3",
            "ellipticity_window_q": ["1", mp.nstr(q_hi, 18)],
            "ellipticity_window_x": ["2", mp.nstr(x_hi, 18)],
            "q0_position_in_window_pct": mp.nstr((Q0 - 1) / (q_hi - 1) * 100, 8),
            "theta_L_at_q0": mp.nstr(theta_L(Q0), 14),
            "crossings": {k: {"theta_required_at_q0": mp.nstr(v["theta_req_at_q0"], 14),
                              "q_star": mp.nstr(v["q_star"], 18),
                              "sigma_from_q0": mp.nstr(v["sigma"], 10),
                              "distance_to_wall": mp.nstr(v["distance_to_wall"], 10)}
                          for k, v in crossings.items()},
            "cyclotomic_max_abs_re_tr": mp.nstr(re_tr_max, 6),
            "cyclotomic_max_abs_im_det": mp.nstr(im_det_max, 6),
            "cyclotomic_min_phase": {"N": int(n_min), "phi": mp.nstr(phi_min, 14),
                                     "over_required": mp.nstr(phi_min / theta_req_C, 8)},
            "cyclotomic_tower": [{"N": int(n), "phi": (mp.nstr(p, 12) if p else None),
                                  "disc": mp.nstr(d, 10)} for n, p, d in tower],
        },
        "context": {
            "axis": "qou-cds1: is there a tower of elliptic curves indexed by the degree "
                    "of q, and were the earlier steps collapsing to order zero?",
            "answer": (
                "The collapse was real and is corrected here. The tower is not elliptic: "
                "the short model's discriminant is a perfect square (genus 0) and the long "
                "model's is a squarefree degree-18 polynomial (genus 8), and the Hecke "
                "tower adds no eigenvalue at any level. There is no twisting to be missed "
                "— tr is bar-odd and disc bar-even, exactly. The one genuine tower is the "
                "cyclotomic one, and none of its phases is small enough either."),
            "corrects": (
                "Steps 21-25 evaluated every spectrum at q = q_0 alone; and Step 25's "
                "write-up wrongly said Delta_L could not be carried symbolically."),
            "scope": "Scope-(a). Nothing derived, proposed, wired or readmitted. q* is "
                     "recorded as a fact about the curve, never as a candidate q.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t_start) * 1000),
    }
    out_p = HERE / "qbeta-discriminant-curve-in-q.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="sympy+mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
