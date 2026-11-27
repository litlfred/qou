#!/usr/bin/env python3
"""Symbolic solution of the convention-D operator-selection LP on the
H_3(q)/rad quotient, and the lattice-membership test for Phi*.

WHY THIS IS SYMBOLIC, NOT A SEARCH
----------------------------------
The re-derived Route-2 program (audit
`docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md`) selects a
canonical direction `Phi*` in `H_3(q)` by

    min  t . x        subject to    G x >= 0 ,  sum x = n ,  v . x = 0

where `t = TR_M`, `G` is the Markov-trace Gram matrix, and `v` is the
radical `v_i = (-1/q)^len(w_i)` that convention D makes null.  At the
optimum four positivity constraints are tight (active set `[0,1,4,5]`,
measured numerically), so `Phi*` solves **six linear equations in six
unknowns whose coefficients are rational functions of `q`**.

That makes "is `Phi*` in the `Z[q,q^-1]`-lattice spanned by the NF basis?"
a *finite symbolic computation*, not a search: solve the system over
`Q(q)`, clear denominators, and read off whether the numerators are
Laurent polynomials.  Lattice membership is a NECESSARY condition for
`Phi*` to be the image of a braid word (braid images have Laurent-integral
NF coordinates), so a negative here would close Obstruction A outright.

WHAT IT REPORTS
---------------
0. The Markov trace `t(q)` DERIVED from the H_3(q) structure constants --
   normalisation, cyclicity, and the Markov property `t(x sigma_n) = z t(x)`
   -- rather than copied from `pyhecke.gram.TR_M`, so the only
   convention-dependent input is the single scalar `z`.  `G(q)` is then
   `t(T_i . T_j)`, also from the structure constants.  The shipped `TR_M`
   is checked against the derived one.
1. `det G(q) = 0` and `rank G(q) = 5` symbolically (the convention-D
   singularity of `qou-cds2`, confirmed over `Q(q)` rather than at a pin).
2. `G(q) . v(q) = 0` symbolically -- the closed-form radical.
3. `Phi*(q)` as an explicit vector in `Q(q)^6`.
4. The common denominator `D(q)`, its factorisation, and the integral
   representative `Psi(q) = D(q) . Phi*(q)`.
5. A cross-check of `Phi*(q_0)` against the numerically-solved LP
   direction, in mpmath at 50 dps (no float64 anywhere on the value path).
6. THE DECISIVE TEST.  Lattice membership is only *necessary*.  The sharp
   question is whether any element of the coset `Phi* + span(v)` -- the
   whole gauge orbit, since on the quotient `x` is defined only modulo the
   radical -- is a nonzero scalar multiple of a braid image.  Wedderburn
   answers it: `H_3(q) = Q(q) (+) M_2(Q(q)) (+) Q(q)` (sym, std, alt), and a
   braid word `w` of exponent sum `e` lands at

       chi_sym = q^e ,   det rho_std = (-1)^e ,   chi_alt = (-1/q)^e

   so EVERY braid word satisfies `chi_sym . chi_alt = det rho_std`, and
   scaling by `c` preserves it.  In terms of the left-regular determinant
   (`det L = chi_sym . (det rho_std)^2 . chi_alt`) that identity is the
   scale-free, exponent-free invariant

       F(y) := det L(y) - (chi_sym(y) . chi_alt(y))^3 = 0 .

   Verified below on braid words of both signs.  Note also that all three
   components are NONZERO for a braid word, so `chi_alt(y) = 0` already
   forbids `y` from being a nonzero scalar multiple of one.

Bean qou-pb1w.  Emits no witness: this is a decision probe whose output is
an argument, and per AGENTS.md "PROBES ARE NOT EXEMPT" it still carries the
full precision discipline.
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp
from mpmath import mp

_REPO = Path(__file__).resolve().parents[2]
for _p in (_REPO / "computations", _REPO / "computations" / "substrate",
           _REPO / "tools" / "qou-substrate" / "python"):
    sys.path.insert(0, str(_p))

mp.dps = 60

# ── the numerically-solved LP direction this must reproduce ──────────────
# From the convention-D quotient LP (audit section "Route 2 RE-DERIVED").
LP_NUMERIC = [
    "-0.61738763", "-0.68528704", "1.85198003",
    "-0.76065394", "2.05565817", "-0.84430958",
]
ACTIVE_SET = (0, 1, 4, 5)

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]

q = sp.symbols("q", positive=True)
h = q - 1 / q
z = q ** 3 / (q ** 2 + 1)          # convention D (owner ruling 2026-08-15)


def _reduce_nf(terms):
    """Gröbner–Shirshov reduction to the NF basis, over Q(q).

    Mirrors `pyhecke.gram._reduce_nf` exactly, with `abs(c) < 1e-15`
    replaced by exact `sp.simplify(c) == 0` -- the float tolerance is what
    makes the shipped version float64-bound, and it has no meaning here.
    """
    changed = True
    while changed:
        changed = False
        new: dict[tuple[int, ...], sp.Expr] = {}
        for word, coeff in terms.items():
            if sp.simplify(coeff) == 0:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:            # sigma_i^2 = h sigma_i + 1
                    i = word[p]
                    pre, suf = word[:p], word[p + 2:]
                    a = pre + (i,) + suf
                    b = pre + suf
                    new[a] = new.get(a, 0) + coeff * h
                    new[b] = new.get(b, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):            # braid relation
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: sp.together(c) for w, c in new.items()
                 if sp.simplify(c) != 0}
    return terms


def derive_trace(C):
    """Solve for the Markov trace `t(q)` from the H_3(q) structure constants.

    `t` is NOT taken from `pyhecke` here -- it is DERIVED, so that the only
    convention-dependent input to this probe is the single scalar `z`.  The
    Markov-Ocneanu-Wenzl trace is the unique linear functional on H_3(q)
    satisfying

        (N)  t(1) = 1                              normalisation
        (C)  t(T_i T_j) = t(T_j T_i)  for all i,j  cyclicity
        (M)  t(x . sigma_n) = z . t(x)  for x in H_n   Markov property

    and each condition is expressed through the structure constants
    `C[i][j] = NF(T_i . T_j)`, i.e. through the Gröbner-Shirshov reduction
    itself.  The solution is then CHECKED against the convention-D vector
    `[1, z, z, z^2, z^2, h z^2 + z]` that `pyhecke.gram.TR_M` ships, which
    makes the shipped constant a verified consequence rather than an input.
    """
    ts = sp.symbols("t0:6")
    T = list(ts)
    eqs = [sp.Eq(T[0], 1)]                                   # (N)
    for i in range(6):                                       # (C)
        for j in range(i + 1, 6):
            d = sp.expand(sum((C[i][j][k] - C[j][i][k]) * T[k] for k in range(6)))
            if d != 0:
                eqs.append(sp.Eq(d, 0))
    # (M): H_1 = <1> with last generator sigma_0; H_2 = <sigma_0> with sigma_1.
    for sub, gen in (([()], 0), ([(), (0,)], 1)):
        for w in sub:
            x = [sp.Integer(1) if b == w else sp.Integer(0) for b in NF_BASIS]
            xg = rmul_gen(x, gen)
            eqs.append(sp.Eq(
                sp.expand(sum(xg[k] * T[k] for k in range(6))),
                sp.expand(z * sum(x[k] * T[k] for k in range(6))),
            ))
    sol = sp.solve(eqs, ts, dict=True)
    if len(sol) != 1:
        raise RuntimeError(f"trace not uniquely determined: {len(sol)} solutions")
    return [sp.cancel(sp.together(sol[0][x])) for x in ts]


def build_gram(C, t) -> sp.Matrix:
    """G[i][j] = t(T_i . T_j), from the structure constants and the trace."""
    G = sp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            G[i, j] = sp.simplify(sum(C[i][j][k] * t[k] for k in range(6)))
    return G


def structure_constants():
    """C[i][j] = NF(T_i . T_j) as a 6-vector over Q(q)."""
    C = [[None] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            nf = _reduce_nf({NF_BASIS[i] + NF_BASIS[j]: sp.Integer(1)})
            C[i][j] = [sp.simplify(nf.get(b, 0)) for b in NF_BASIS]
    return C


def rmul_gen(y, gen):
    """Right-multiply an NF vector by the generator sigma_gen."""
    terms: dict[tuple[int, ...], sp.Expr] = {}
    for i, b in enumerate(NF_BASIS):
        if y[i] == 0:
            continue
        terms[b + (gen,)] = terms.get(b + (gen,), 0) + y[i]
    red = _reduce_nf(terms)
    return [sp.simplify(red.get(b, 0)) for b in NF_BASIS]


def nf_of_word(word):
    """NF vector of a positive braid word, over Q(q)."""
    y = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for g in word:
        y = rmul_gen(y, g)
    return y


def main() -> int:
    print("=" * 72)
    print("SYMBOLIC OPERATOR-SELECTION LP ON H_3(q)/rad  (convention D)")
    print("=" * 72)
    print(f"  z(q) = {sp.simplify(z)}")
    print(f"  h(q) = {sp.simplify(h)}")

    C = structure_constants()
    t = derive_trace(C)
    print("\n-- Markov trace t(q), DERIVED from the structure constants --")
    for i, (b, e) in enumerate(zip(NF_BASIS, t)):
        print(f"   t[{i}]  ({b or '()'})  =  {sp.factor(e)}")
    shipped = [sp.Integer(1), z, z, z ** 2, z ** 2, h * z ** 2 + z]
    same = all(sp.simplify(a - b) == 0 for a, b in zip(t, shipped))
    print(f"   agrees with pyhecke.gram.TR_M (convention D) : {same}")
    assert same, "derived trace must reproduce the shipped convention-D TR_M"

    G = build_gram(C, t)
    print("\n-- Gram matrix G(q) over Q(q), built as t(T_i . T_j) --")
    for i in range(6):
        print("   [" + ", ".join(str(sp.factor(G[i, j])) for j in range(6)) + "]")

    detG = sp.simplify(G.det())
    print(f"\n  det G(q) = {detG}      (convention-D singularity, qou-cds2)")
    print(f"  rank G(q) = {G.rank()}  of 6")

    v = sp.Matrix([(-1 / q) ** len(w) for w in NF_BASIS])
    Gv = sp.simplify(G * v)
    print(f"  G(q) . v(q) = {list(Gv)}   (radical, closed form)")
    assert detG == 0, "convention D must be singular"
    assert all(sp.simplify(e) == 0 for e in Gv), "v must be the radical"

    # ── the six-equation system ────────────────────────────────────────
    xs = sp.symbols("x0:6")
    X = sp.Matrix(xs)
    GX = G * X
    eqs = [sp.Eq(sp.simplify(GX[i]), 0) for i in ACTIVE_SET]      # tight
    eqs.append(sp.Eq(sum(xs), 1))                                  # net
    eqs.append(sp.Eq(sp.simplify((v.T * X)[0]), 0))                # quotient
    print(f"\n-- solving {len(eqs)} equations in 6 unknowns over Q(q) --")
    print(f"   active set (tight positivity) = {list(ACTIVE_SET)}")

    sol = sp.solve(eqs, xs, dict=True)
    if len(sol) != 1:
        print(f"  !! expected a unique solution, got {len(sol)}")
        return 1
    sol = sol[0]
    phi = [sp.cancel(sp.together(sol[s])) for s in xs]

    print("\n-- Phi*(q) --")
    for i, e in enumerate(phi):
        print(f"   x{i} = {e}")

    # ── lattice membership ─────────────────────────────────────────────
    dens = [sp.denom(e) for e in phi]
    D = sp.simplify(sp.lcm(dens))
    psi = [sp.expand(sp.cancel(e * D)) for e in phi]
    print("\n-- lattice test --")
    print(f"   common denominator  D(q) = {sp.expand(D)}")
    print(f"   factorisation       D(q) = {sp.factor(D)}")
    print("   integral representative  Psi(q) = D(q) . Phi*(q):")
    for i, (e, b) in enumerate(zip(psi, NF_BASIS)):
        print(f"     Psi_{i}  ({b or '()'})  =  {e}")

    def _laurent_int(e):
        """True iff `e` is a Laurent polynomial in q with integer coefficients.

        `q**8` clears any negative powers the NF reduction could introduce
        (max total degree on this basis is 3, so 8 is generous); `Poly`
        then raises for anything that is not polynomial after clearing.
        """
        try:
            pol = sp.Poly(sp.expand(e * q ** 8), q)
        except sp.PolynomialError:
            return False
        return all(c.is_Integer for c in pol.all_coeffs())

    laurent = all(_laurent_int(e) for e in psi)
    integral = laurent
    print(f"\n   every Psi_i a Laurent polynomial in q : {laurent}")
    print(f"   every coefficient an integer  : {integral}")
    verdict = laurent and integral
    print(f"\n   VERDICT: Phi* {'IS' if verdict else 'is NOT'} in the "
          f"Z[q,q^-1]-lattice up to the scale D(q).")
    print("   (Necessary for a braid image, NOT sufficient -- see below.)")

    # ── numerical cross-check at q_0, mpmath only ──────────────────────
    try:
        from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
    except ImportError:
        from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
    q0 = Q_MP
    print(f"\n-- cross-check at q_0 = {mp.nstr(q0, 20)} (proton pin, 60 dps) --")
    worst = mp.mpf(0)
    for i, e in enumerate(phi):
        val = mp.mpf(str(sp.N(e.subs(q, sp.Rational(Q_50_DIGIT_STR)), 55)))
        ref = mp.mpf(LP_NUMERIC[i])
        d = abs(val - ref)
        worst = max(worst, d)
        print(f"   x{i}: symbolic {mp.nstr(val, 12):>16}   "
              f"LP {LP_NUMERIC[i]:>13}   |diff| {mp.nstr(d, 3)}")
    print(f"\n   worst |diff| = {mp.nstr(worst, 4)}  "
          f"(LP reference is quoted to 8 dp, so ~1e-8 is agreement)")
    if worst > mp.mpf("1e-7"):
        print("   !! symbolic solution does NOT reproduce the LP direction")
        return 1
    print("   symbolic solution reproduces the numerically-solved LP direction.")

    # ── phase 2: the Wedderburn braid-image test on the whole coset ────
    print("\n" + "=" * 72)
    print("IS ANY POINT OF THE COSET  Phi* + span(v)  A BRAID IMAGE?")
    print("=" * 72)

    def Lmat(y):
        """Left-multiplication matrix of y = sum y_i T_i on the NF basis."""
        M = sp.zeros(6, 6)
        for j in range(6):
            for k in range(6):
                M[k, j] = sp.expand(sum(y[i] * C[i][j][k] for i in range(6)))
        return M

    def chi_sym(y):
        return sp.expand(sum(y[i] * q ** len(w)
                             for i, w in enumerate(NF_BASIS)))

    def chi_alt(y):
        return sp.expand(sum(y[i] * (-1 / q) ** len(w)
                             for i, w in enumerate(NF_BASIS)))

    def F(y):
        return sp.expand(Lmat(y).det(method="berkowitz")
                         - (chi_sym(y) * chi_alt(y)) ** 3)

    # sanity: F vanishes on braid words of both signs, and on scalings
    print("  sanity -- F(y) = 0 on braid images (necessary condition holds):")
    ok = True
    for w in [(), (0,), (0, 1), (0, 1, 0), (1, 0, 1, 0), (0, 0, 1)]:
        y = nf_of_word(w)
        r = sp.simplify(F(y)) == 0
        ok &= r
        print(f"     w = {str(w):14}  F = 0 : {r}")
    # sigma_0^{-1} = T_0 - h  (from sigma^2 = h.sigma + 1), exponent sum -1
    inv0 = [-h, sp.Integer(1), sp.Integer(0), sp.Integer(0),
            sp.Integer(0), sp.Integer(0)]
    for lbl, y in [("sigma_0^-1", inv0),
                   ("sigma_0^-1 sigma_1", rmul_gen(inv0, 1))]:
        r = sp.simplify(F(y)) == 0
        ok &= r
        print(f"     w = {lbl:14}  F = 0 : {r}   (negative crossings)")
    c = sp.symbols("c")
    r = sp.simplify(F([c * e for e in nf_of_word((0, 1))])) == 0
    ok &= r
    print(f"     w = {'c * NF(01)':14}  F = 0 : {r}   (scale-free)")
    assert ok, "the invariant must vanish on every braid image"

    # the coset, in integral coordinates: Psi + s * (q^3 . v)
    vt = [sp.expand(e * q ** 3) for e in v]
    sy = sp.symbols("s")
    y = [sp.expand(psi[i] + sy * vt[i]) for i in range(6)]

    csP, caP = chi_sym(psi), sp.simplify(chi_alt(psi))
    csV, caV = chi_sym(vt), sp.simplify(chi_alt(vt))
    print(f"\n  chi_sym(Psi) = {sp.factor(csP)}        "
          f"chi_alt(Psi) = {caP}")
    print(f"  chi_sym(qv)  = {sp.factor(csV)}        "
          f"chi_alt(qv)  = {sp.factor(caV)}")
    print("\n  chi_alt(Psi) = 0, and every braid word has chi_alt = (-1/q)^e != 0,")
    print("  so Psi itself is NOT a nonzero scalar multiple of a braid image.")
    print("  chi_sym(qv) = 0, so chi_sym is constant along the coset -- the")
    print("  gauge freedom moves chi_alt and nothing else at the character level.")

    Fp = sp.Poly(F(y), sy)
    print(f"\n  F(s) on the coset -- degree {Fp.degree()} in s:")
    for k, coeff in zip(range(Fp.degree(), -1, -1), Fp.all_coeffs()):
        print(f"     s^{k}: {sp.factor(coeff)}")
    print(f"\n  F(s) = {sp.factor(Fp.as_expr())}")
    roots = sp.solve(sp.Eq(Fp.as_expr(), 0), sy)
    print(f"  roots: {roots}")

    only_zero = (set(sp.simplify(r) for r in roots) == {sp.Integer(0)})
    print("\n" + "=" * 72)
    print("VERDICT")
    print("=" * 72)
    if only_zero:
        print("  The necessary invariant F(s) = 0 holds ONLY at s = 0, and s = 0")
        print("  is Psi itself -- which chi_alt(Psi) = 0 already excludes.  So")
        print("  NO element of the coset Phi* + span(v) is a nonzero scalar")
        print("  multiple of a braid image.")
        print()
        print("  This is a scope-(b) STRUCTURAL EXCLUSION, and the invariant is")
        print("  named: the Wedderburn identity chi_sym . chi_alt = det rho_std,")
        print("  which every element of Q(q).image(B_3 -> H_3(q)) satisfies and")
        print("  which is verified on braid words above.")
        print()
        print("  What it does NOT say: nothing here refutes the framework or the")
        print("  operator-selection program.  It says the convention-D LP, run on")
        print("  the quotient, selects an ALGEBRA element that no braid realises.")
        print("  The lattice test above shows integrality is not what forbids it;")
        print("  the character structure is.")
    else:
        print(f"  F(s) vanishes at {roots} -- the coset is NOT excluded by this")
        print("  invariant, and the braid-image question stays open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
