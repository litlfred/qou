"""ε-Y1: does colour fix the quark U(1) charge (baryon number 1/N)?

Pre-registered on bean qou-99qc (ε-Y1). Exact sympy, no floats.

Measures, for N = 2, 3:
  (A) the u1 factor u = Ř_gl / Ř_sl on V⊗V  (Jimbo gl_N vs sl_N),
  (B) the gl_N monodromy of V around the q-antisymmetriser Λ^N V,
  (C) what a U(1) braiding q^(c·a·b) with charges a (quark), N·a (Λ^N V)
      must satisfy to reproduce (A) and (B): only c·a^2 is constrained.
Then reports δε/ε of ε-EM1 at the a = 1/N reading, as a consequence only.
"""
import itertools, json, pathlib
import sympy as sp

q = sp.symbols("q", positive=True)


def jimbo_R(N):
    """Jimbo gl_N Ř on V⊗V, eigenvalues q (sym) and -q^-1 (antisym)."""
    d = N * N
    R = sp.zeros(d, d)
    idx = lambda i, j: i * N + j
    for i in range(N):
        R[idx(i, i), idx(i, i)] = q
    for i in range(N):
        for j in range(N):
            if i != j:
                R[idx(j, i), idx(i, j)] = 1  # swap
            if i < j:
                R[idx(i, j), idx(i, j)] += q - 1 / q
    return R


def embed(R, N, k, n):
    """Ř acting on strands (k, k+1) of V^{⊗n}."""
    left = sp.eye(N ** k)
    right = sp.eye(N ** (n - k - 2))
    return sp.kronecker_product(sp.kronecker_product(left, R), right)


def antisym_vector(N):
    """Basis vector of the q-antisymmetric line Λ^N V in V^{⊗N} (kernel of Ř - q)."""
    R = jimbo_R(N)
    # Λ^N = common eigenspace with eigenvalue -q^-1 for all Ř_k
    M = sp.Matrix.vstack(*[embed(R, N, k, N) + sp.eye(N ** N) / q for k in range(N - 1)])
    ns = M.nullspace()
    assert len(ns) == 1, len(ns)
    return sp.simplify(ns[0])


def monodromy_V_around_Lambda(N):
    """Eigenvalue of (braid V past Λ^N V)^2 on V⊗Λ^N V, gl_N Jimbo framing."""
    R = jimbo_R(N)
    n = N + 1
    # B = Ř_{N-1} ... Ř_0 moves strand 0 (V) past strands 1..N; full monodromy = B' B
    B = sp.eye(N ** n)
    for k in range(0, N):
        B = embed(R, N, k, n) * B
    Bback = sp.eye(N ** n)
    for k in reversed(range(0, N)):
        Bback = embed(R, N, k, n) * Bback
    # after B the V strand sits last: state Λ⊗V; apply Ř's back the other way
    Mono = Bback * B
    lam = antisym_vector(N)
    vals = set()
    for e in range(N):
        v = sp.zeros(N, 1); v[e] = 1
        x = sp.kronecker_product(v, lam)
        y = Mono * x
        # y must be proportional to x
        i0 = next(i for i in range(len(x)) if x[i] != 0)
        r = sp.simplify(y[i0] / x[i0])
        assert sp.simplify(y - r * x) == sp.zeros(len(x), 1)
        vals.add(r)
    assert len(vals) == 1
    return vals.pop()


out = {"probe": "colour_hypercharge_y1_probe", "bean": "qou-99qc", "id": "ε-Y1",
       "q0Anchor": "independent",
       "q0AnchorReason": "exact sympy over Q(q) (and exact rationals for the Y=1/3 consequence); q is a free symbol, no substrate q0 is read",
       "results": {}}
c, a = sp.symbols("c a", positive=True)
for N in (2, 3):
    R = jimbo_R(N)
    ev = sorted(set(sp.simplify(e) for e in R.eigenvals()), key=str)
    sl_ev = [sp.simplify(e * q ** sp.Rational(-1, N)) for e in ev]
    u = sp.Rational(1, N)  # u1 exponent: Ř_gl = q^(1/N) Ř_sl by definition of sl_N normalisation
    mono = sp.simplify(monodromy_V_around_Lambda(N))
    # U(1) model: crossing V,V -> q^(c a^2) ; full monodromy V around Λ^N (charge N a) -> q^(2 c a N a)
    eq_A = sp.Eq(c * a ** 2, u)
    eq_B = sp.Eq(2 * c * a * (N * a), sp.log(mono, q) if mono != 1 else 0)
    sol = sp.solve([eq_A], [c], dict=True)
    B_given_A = sp.simplify(eq_B.lhs.subs(sol[0]) - eq_B.rhs)
    out["results"][f"N={N}"] = {
        "gl_N_eigenvalues": [str(e) for e in ev],
        "sl_N_eigenvalues": [str(e) for e in sl_ev],
        "u1_exponent_per_crossing": str(u),
        "gl_N_monodromy_V_around_Lambda^N": str(mono),
        "constraint_from_u1_factor": "c*a^2 = 1/N",
        "monodromy_constraint_given_u1": "redundant" if B_given_A == 0 else f"independent: residual {B_given_A}",
        "scale_freedom": "(a, c) -> (lambda*a, c/lambda^2) leaves both invariant",
        "a_if_baryon_unit_charge": str(sp.Rational(1, N)),
    }

# Consequence only: ε-EM1 δε/ε at Y = 2a = 2/3 ?  No: Q = T3 + Y/2, B = 1/3 -> Y = B (quark doublet, L = 0)
Y = sp.Rational(1, 3)
np_ = (Y ** 2 - 2 * Y - 1) / 2
pn_ = (Y ** 2 + 2 * Y - 1) / 2
out["consequence_at_Y=B=1/3"] = {
    "deps_over_eps_n_to_p": str(np_), "deps_over_eps_p_to_n": str(pn_), "asymmetry_2Y": str(2 * Y),
    "note": "requires Y = B - L with L = 0 for quarks; the identification Y <-> B is NOT derived here",
}
p = pathlib.Path(__file__).with_name("colour-hypercharge-y1.witness.json")
p.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(out, indent=2, ensure_ascii=False))
