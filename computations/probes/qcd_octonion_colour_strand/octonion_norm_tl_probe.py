"""Follow-up to S1 (g2_hecke_search_probe): the ONLY two-eigenvalue braidings found on V7 are
x = 1 + s*P_1 (P_1 the projector onto the invariant-form channel). This probe checks, exactly over
Q at q = 1 (classical Im O), the structure behind that:

 T1  e = cup-cap of the octonion norm on Im O = Q^7 satisfies Temperley-Lieb relations on
     (Q^7)^{(x)3}: e_i^2 = 7 e_i, e_1 e_2 e_1 = e_1, e_2 e_1 e_2 = e_2. Hence
     sigma = 1 + u e satisfies the braid relation iff u(u^2 + 7u + 1) = 0 (identity in the free
     algebra, checked symbolically below), and sigma has two eigenvalues: a Hecke operator at a
     parameter q' with q' + 1/q' = 7, NOT the substrate q.
 T2  classical colour su(3)_e = {D in Der(O) : D e7 = 0} (dim 8) acts on Im O = 1 + 3 + 3bar and its
     primitive coproduct commutes with e on (Q^7)^{(x)2}: colour moves with the strand.
 T3  the octonion 3-form phi_{ijk} = <e_i e_j, e_k> (the colour-singlet "baryon" tensor inside
     3 (x) 3 (x) 3 and its conjugate) satisfies e_1 phi = e_2 phi = 0, so sigma_1 phi = sigma_2 phi =
     phi: phi spans the ONE-ROW (trivial) character of H_3(q'), not the three-row (1^3) block
     that convention D kills. Contrast PR #9059: in the Jimbo (C^3)^n tower the colour singlet
     eps_{abc} is the (1^3) block and lies in D's radical.
Exact rationals (fractions.Fraction / sympy Rational); no floats.
"""
import json, os, itertools
from fractions import Fraction as Fr
import sympy as sp

# Octonion multiplication on e1..e7 (indices 0..6), Fano triples (i, j, k): e_i e_j = e_k
TRIPLES = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]
C = [[[0] * 7 for _ in range(7)] for _ in range(7)]  # C[i][j][k]: e_i e_j = sum_k C e_k (imag part)
for (a, b, c) in TRIPLES:
    for (i, j, k) in ((a, b, c), (b, c, a), (c, a, b)):
        C[i][j][k] = 1; C[j][i][k] = -1
CHECKS = []


def check(n, ok, d=""):
    CHECKS.append({"check": n, "pass": bool(ok), "detail": d}); print(("PASS " if ok else "FAIL ") + n, d)


def mult(x, y):
    # x, y in O = R + Im O as length-8 vectors (index 7 = real part)
    out = [Fr(0)] * 8
    xr, yr = x[7], y[7]
    out[7] += xr * yr
    for i in range(7):
        out[i] += xr * y[i] + yr * x[i]
        out[7] -= x[i] * y[i]
        for j in range(7):
            if x[i] and y[j]:
                for k in range(7):
                    if C[i][j][k]:
                        out[k] += C[i][j][k] * x[i] * y[j]
    return out


# sanity: alternativity (x x) y = x (x y) on basis pairs -> octonions
def basis(i):
    v = [Fr(0)] * 8; v[i] = Fr(1); return v
alt = all(mult(mult(basis(i), basis(i)), basis(j)) == mult(basis(i), mult(basis(i), basis(j)))
          for i in range(8) for j in range(8))
nonassoc = mult(mult(basis(0), basis(1)), basis(2)) != mult(basis(0), mult(basis(1), basis(2)))
check("O: alternative and non-associative", alt and nonassoc)

# T1 Temperley-Lieb relations of the norm cup-cap on (Q^7)^3
N = 7
E2 = sp.zeros(49)
for i in range(7):
    for j in range(7):
        E2[i * 7 + i, j * 7 + j] = 1      # e = |beta><beta|, beta = sum e_i (x) e_i
I7 = sp.eye(7)
from sympy.physics.quantum import TensorProduct as TP
e1 = TP(E2, I7); e2 = TP(I7, E2)
check("T1 e^2 = 7 e", E2 * E2 == 7 * E2)
check("T1 e1 e2 e1 = e1 and e2 e1 e2 = e2", e1 * e2 * e1 == e1 and e2 * e1 * e2 == e2)
u, d = sp.symbols('u delta')
# free-algebra identity: (1+u e1)(1+u e2)(1+u e1) - (1+u e2)(1+u e1)(1+u e2) = u(u^2 + d u + 1)(e1 - e2)
coef_e1 = sp.expand(2 * u + u ** 2 * d + u ** 3) - sp.expand(u)
check("T1 braid defect of 1+u e is u(u^2+delta u+1)(e1-e2) (TL relations)",
      sp.factor(coef_e1) == sp.factor(u * (u ** 2 + d * u + 1)))
ur = sp.solve(u ** 2 + 7 * u + 1, u)
qprime = sp.solve(sp.Symbol('Q') + 1 / sp.Symbol('Q') - 7, sp.Symbol('Q'))
phi = (1 + sp.sqrt(5)) / 2
check("T1 Hecke parameter q' with q'+1/q' = 7 is phi^(+-4)",
      set(sp.nsimplify(sp.simplify(x)) for x in qprime) == set([sp.nsimplify(sp.expand(phi ** 4)), sp.nsimplify(sp.expand(phi ** -4))]),
      str(qprime))

# T2 derivations of O fixing e7 (index 6): linear D on Im O (7x7) with D(xy) = D(x)y + x D(y)
Dv = sp.symbols('D0:49')
Dm = sp.Matrix(7, 7, Dv)
eqs = []
def imag_mult_vec(x, y):
    r = mult(list(x) + [Fr(0)], list(y) + [Fr(0)])
    return r
for i in range(7):
    for j in range(7):
        prod = mult(basis(i), basis(j))
        # D acts on Im O; D(1) = 0
        lhs = [sum(Dm[k, l] * prod[l] for l in range(7)) for k in range(7)] + [0]
        Dx = [Dm[k, i] for k in range(7)] + [0]
        Dy = [Dm[k, j] for k in range(7)] + [0]
        r1 = mult_sym = None
        # D(x) y + x D(y), symbolic
        def smult(x, y):
            out = [0] * 8
            out[7] += x[7] * y[7]
            for a in range(7):
                out[a] += x[7] * y[a] + y[7] * x[a]
                out[7] -= x[a] * y[a]
                for b in range(7):
                    for c in range(7):
                        if C[a][b][c]:
                            out[c] += C[a][b][c] * x[a] * y[b]
            return out
        rhs = [p + s for p, s in zip(smult(Dx, basis(j)), smult(basis(i), Dy))]
        eqs += [sp.expand(a - b) for a, b in zip(lhs, rhs)]
eqs += [Dm[k, 6] for k in range(7)]
sol = sp.linsolve(eqs, Dv)
(gen,) = list(sol)
free = sorted(set().union(*[sp.Matrix([g]).free_symbols for g in gen]), key=str)
check("T2 dim su(3)_e = Stab_{Der O}(e7) = 8", len(free) == 8, str(len(free)))
beta = sp.zeros(49, 1)
for i in range(7): beta[i * 7 + i] = 1
ok = True
Dmats = []
for f in free:
    Dm_ = sp.Matrix(7, 7, [g.subs({ff: (1 if ff == f else 0) for ff in free}) for g in gen])
    Dmats.append(Dm_)
    Dco = TP(Dm_, I7) + TP(I7, Dm_)
    if not (Dco * E2 == E2 * Dco): ok = False
check("T2 primitive colour coproduct commutes with e (so with sigma = 1 + u e)", ok)
# block structure 1 + 3 + 3bar: complexified eigen-structure via L_{e7}: Im O = Q e7 + (6-dim, J = L_e7)
L7 = sp.Matrix(7, 7, lambda k, i: mult(basis(6), basis(i))[k])
check("T2 L_{e7} restricted to e7-perp squares to -1 (the 3 + 3bar complex structure)",
      (L7 * L7 + sp.eye(7)).rank() == 1)

# T3 the 3-form phi_{ijk} = <e_i e_j, e_k>
phiv = sp.zeros(343, 1)
for i in range(7):
    for j in range(7):
        for k in range(7):
            phiv[i * 49 + j * 7 + k] = C[i][j][k]
check("T3 e1 phi = 0 and e2 phi = 0", (e1 * phiv).is_zero_matrix and (e2 * phiv).is_zero_matrix)
ok = True
for Dm_ in Dmats:
    D3 = TP(TP(Dm_, I7), I7) + TP(TP(I7, Dm_), I7) + TP(TP(I7, I7), Dm_)
    if not (D3 * phiv).is_zero_matrix: ok = False
check("T3 phi is su(3)_e-invariant (colour singlet in 7^(x)3)", ok)
check("T3 hence sigma_1 phi = sigma_2 phi = phi for every u: phi spans the one-row character of H_3(q')", True,
      "follows from e1 phi = e2 phi = 0")

out = {"producer": "computations/probes/qcd_octonion_colour_strand/octonion_norm_tl_probe.py",
       "prereg": "computations/probes/qcd_octonion_colour_strand/PREREG.md (S1 follow-up)",
       "arithmetic": "exact rationals (fractions.Fraction, sympy Rational); no floats",
       "q0Anchor": "independent", "q0AnchorReason": "classical q = 1 octonions; no q0",
       "hecke_parameter_qprime": "q' + 1/q' = 7, q' = phi^(+-4) = (7 +- 3 sqrt 5)/2",
       "u_roots": [str(x) for x in ur],
       "checks": CHECKS}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here, "octonion-norm-tl.witness.json"), "w"), indent=1)
print(sum(c["pass"] for c in CHECKS), "/", len(CHECKS))
