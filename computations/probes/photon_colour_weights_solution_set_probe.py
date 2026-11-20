"""Solution set of gamma(phi)*gamma(psi) = beta_Bor in H_3(q) (bean qou-99qc).

Photon (def:photon, owner ruling 2026-11-20): gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^{-1}.
NF formula of the pair product: QOU.QuarkState.pairNFChiral_eq (Lean, sorry-free).
NF(beta_Bor) = [1-h^4, -h^3-h^5, h^3, -h^2, h^2+h^4, 0]
(QOU.QuarkState.PhotonColourWeights.borromean_pair_nf).

Measurement, not proof. Method: the e^- and L_- equations are linear in
(a2, a1) and solved by Cramer (their determinant N = a2^2 - h a1 a2 - a1^2 is
nonzero on every solution over a domain, see the Lean file docstring); the
remaining system is reduced to two polynomials in (a1, a2), whose common zeros
are found from the resultant in a2 and refined in mpmath at 60 dps. Each
candidate is re-substituted into all six original equations; a solution is
kept only if every residual is below 1e-40. No float64 arithmetic.

Exact rational sample values of h are used; the count is a statement about
those h only.
"""
import sympy as sp
import mpmath as mm

mm.mp.dps = 60
h, x, y, a0, b1 = sp.symbols("h x y a0 b1")   # x = a1 = phi1, y = a2 = phi01
a1, a2 = x, y
N = a2**2 - h*a1*a2 - a1**2
b0 = h**2*a1/N
b2 = -h**2*a2/N


def pair(a0, a1, a2, b0, b1, b2, h):
    return [1 + a0*b0 + a1*b1 - h*(a0*b2 + a2*b0) + h**2*a2*b2,
            a0 + b0 + h*a0*b0 + a2*b1 - h*(a2 + b2) - h**2*(a0*b2 + a2*b0) + h**3*a2*b2,
            a1 + b1 + h*a1*b1 + a0*b2 - h*a2*b2,
            a1*b0 + a2*b2 - h*a1*b2,
            a2 + b2 + a0*b1 + h*a0*b2 - h**2*a2*b2,
            a2*b0 + a1*b2]


def target(h):
    return [1 - h**4, -h**3 - h**5, h**3, -h**2, h**2 + h**4, 0]


E = [e - t for e, t in zip(pair(a0, a1, a2, b0, b1, b2, h), target(h))]
sol = sp.solve([E[0], E[2]], [a0, b1], dict=True)[0]
A0, B1 = sol[a0], sol[b1]
c1 = E[1].subs({a0: A0, b1: B1})
c4 = E[4].subs({a0: A0, b1: B1})


def run(hv):
    e1 = sp.expand(sp.numer(sp.together(c1.subs(h, hv))))
    e4 = sp.expand(sp.numer(sp.together(c4.subs(h, hv))))
    r = sp.resultant(e1, e4, y)
    f1 = sp.lambdify((x, y), e1, "mpmath")
    f4 = sp.lambdify((x, y), e4, "mpmath")
    fv = sp.lambdify((x, y), [A0.subs(h, hv), a1, a2, b0.subs(h, hv),
                              B1.subs(h, hv), b2.subs(h, hv)], "mpmath")
    fN = sp.lambdify((x, y), N.subs(h, hv), "mpmath")
    hm = mm.mpf(hv.p) / hv.q
    sols = []
    for f, _ in sp.factor_list(r)[1]:
        cs = [mm.mpf(sp.Rational(c).p) / sp.Rational(c).q for c in sp.Poly(f, x).all_coeffs()]
        if len(cs) < 2:
            continue
        for xr in mm.polyroots(cs, maxsteps=800, extraprec=300):
            cy = [sp.lambdify(x, c, "mpmath")(xr) for c in sp.Poly(e1, y).all_coeffs()]
            for yr in mm.polyroots(cy, maxsteps=800, extraprec=300):
                if abs(f4(xr, yr)) > mm.mpf(10)**-30 or abs(fN(xr, yr)) < mm.mpf(10)**-30:
                    continue
                try:
                    v = fv(xr, yr)
                except ZeroDivisionError:
                    continue
                res = max(abs(t) for t in [e - t2 for e, t2 in zip(pair(*v, hm), target(hm))])
                if res > mm.mpf(10)**-40:
                    continue
                if all(max(abs(p - q) for p, q in zip(v, s)) > mm.mpf(10)**-20 for s in sols):
                    sols.append(v)
    return sols


if __name__ == "__main__":
    for hv in [sp.Rational(1, 2), sp.Rational(2, 9), sp.Rational(3)]:
        sols = run(hv)
        print(f"h = {hv}: {len(sols)} verified solutions (residual < 1e-40)")
        for v in sols:
            barclosed = abs(v[0] + v[1]) < mm.mpf(10)**-30 and abs(v[3] + v[4]) < mm.mpf(10)**-30
            print("   (phi0,phi1,phi01 | psi0,psi1,psi01) =",
                  ", ".join(mm.nstr(t, 8) for t in v), "| bar-closed:", barclosed)
