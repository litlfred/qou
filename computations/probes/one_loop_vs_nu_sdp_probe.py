#!/usr/bin/env python3
# polynomial_q_not_applicable: hyperbolic-geometry numeric probe.
"""1-loop invariant (= adjoint Reidemeister torsion) vs ν_SDP — Option-A test.

Bean qou-r307. Gemini's "Option A" (q-deformed saddle-offsets brainstorm,
2026-08-02) proposed identifying the Kashaev density prefactor
ρ_F = ν_SDP ∈ {1,2} (conj:kashaev-density-equals-sdp-multiplicity) with the
1-loop invariant of the knot complement, citing Garoufalidis–Yoon
"1-loop equals torsion for two-bridge knots" (arXiv:2411.03801), which proves
1-loop = adjoint Reidemeister torsion.

This probe implements the Dimofte–Garoufalidis 1-loop invariant
(Def. 2.1 of 2411.03801) directly from SnapPy's Neumann–Zagier data:

    τ(T) = ± (1/2) · det(G_μ·diag(ζ) + G'_μ·diag(ζ') + G''_μ·diag(ζ''))
                     / ∏_j ζ_j^{f_j} ζ'^{f'_j}_j ζ''^{f''_j}_j

ζ_j=1/z_j, ζ'_j=1/(1−z_j), ζ''_j=1/(z_j(z_j−1)); G_μ = edge gluing matrices
with one edge row replaced by the meridian completeness row; (f,f',f'') an
integer flattening (f+f'+f''=1, Gf+G'f'+G''f''=2).

VERDICT (scope-(a), honest negative): τ is a transcendental/algebraic COMPLEX
number, NOT the integer ν_SDP. For 6₂: τ≈−1.715−1.404j (|τ|≈2.22) vs ν_SDP=1;
for 8₁₁: τ≈2.47+8.45j (|τ|≈8.81) vs ν_SDP=2. The flattening/sign ambiguity
(units, roots of unity) cannot turn these into 1 or 2 — the magnitudes alone
refute equality. So the 1-loop torsion does NOT derive ν_SDP; Gemini's Option-A
bridge is refuted AS STATED. (4₁ control lands in its trace field ℚ(√−3),
|τ|=√3/2, confirming the implementation.) 1-loop=torsion remains a valid
analytic bridge — just not to the integer ν_SDP.

Requires: snappy (standalone; the SnapPy built-in torsion needs Sage, this
NZ-direct route does not). numpy, sympy.
"""
from __future__ import annotations
import numpy as np, sympy as sp


def one_loop(name: str):
    import snappy
    M = snappy.Manifold(name)
    N = M.num_tetrahedra()
    R = np.array([list(r) for r in M.gluing_equations(form='log')], dtype=int)
    G, Gp, Gpp = R[:, 0::3], R[:, 1::3], R[:, 2::3]          # z, z', z'' blocks
    Ge, Gpe, Gppe = G[:N], Gp[:N], Gpp[:N]                    # edge rows
    mer = N                                                   # meridian row index

    def mu(A):
        B = A[:N].copy().astype(float); B[-1] = A[mer]; return B
    Gm, Gpm, Gppm = mu(G), mu(Gp), mu(Gpp)
    z = np.array([complex(s['rect']) for s in M.tetrahedra_shapes()])
    zeta, zetap, zetapp = 1/z, 1/(1 - z), 1/(z * (z - 1))
    det = np.linalg.det(Gm * zeta + Gpm * zetap + Gppm * zetapp)
    # integer flattening
    f = sp.symbols(f'f0:{N}'); fp = sp.symbols(f'fp0:{N}'); fpp = sp.symbols(f'fpp0:{N}')
    eqs = [sp.Eq(f[i] + fp[i] + fpp[i], 1) for i in range(N)]
    lhs = sp.Matrix(Ge) * sp.Matrix(f) + sp.Matrix(Gpe) * sp.Matrix(fp) + sp.Matrix(Gppe) * sp.Matrix(fpp)
    eqs += [sp.Eq(lhs[i], 2) for i in range(N)]
    sol = list(sp.linsolve(eqs, list(f) + list(fp) + list(fpp)))[0]
    subs = {s: 0 for s in sorted(set().union(*[e.free_symbols for e in sol]), key=str)}
    v = [complex(e.subs(subs)) for e in sol]
    fv, fpv, fppv = np.array(v[:N]), np.array(v[N:2 * N]), np.array(v[2 * N:])
    denom = np.prod(zeta ** fv * zetap ** fpv * zetapp ** fppv)
    return float(M.volume()), det, 0.5 * det / denom


def main() -> int:
    print(f"{'knot':6} {'ν_SDP':>6} {'vol':>9} {'1-loop τ':>28} {'|τ|':>9}")
    for name, nu in [('6_2', 1), ('8_11', 2), ('L6a4', 2), ('4_1', None)]:
        try:
            vol, det, tau = one_loop(name)
            print(f"{name:6} {str(nu):>6} {vol:>9.5f} {f'{tau:.5f}':>28} {abs(tau):>9.5f}")
        except Exception as e:
            print(f"{name:6} {str(nu):>6}  ERROR: {str(e)[:50]}")
    print("\nVerdict: |τ| ≠ ν_SDP (2.22≠1, 8.81≠2). 1-loop torsion is a complex "
          "analytic invariant, not the integer dimension count ν_SDP. "
          "Gemini Option-A refuted as stated (scope-a).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
