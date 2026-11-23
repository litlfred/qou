"""Bridge A, gap 4 (P2 for n >= 4): do log poles + Reeb invariance force constant residues?

Class C_n: eta = sum_m f_m dz_m, f_m = P_m / prod_{j != m}(z_m - z_j), with P_m translation
invariant and homogeneous of degree n - 2 (dilation invariance), and
  (i)  iota_T eta = sum_m f_m = 0              (translation invariance of the connection)
  (ii) P_i = P_j on z_i = z_j                  (Saito log poles along every diagonal)
The Arnold forms sum c_ij dlog(z_i - z_j) lie in C_n.  This probe measures, in exact rational
arithmetic (sympy), the dimension of C_n against the Arnold subspace, then adds flatness:
  * closed scalar forms                         d eta = 0
  * abelian twists                              d eta + lam ^ eta = 0
  * first-order flat deformations of KZ         d eta + [A_KZ ^ eta] = 0, n = 4,
    A_KZ = kappa sum s_ij dlog(z_i - z_j) on the 2-dim irrep of S_4 (via S_4 -> S_3).
No floats anywhere.  Lean consumer: QOU/Mass/BridgeAP2Regular.lean (module docstring).

Usage: python3 p2_triple_collision_probe.py [--nonabelian]   (non-abelian part ~2 min/kappa)
"""
import itertools, random, sys
import sympy as sp


def setup(n, rows=1, cols=1):
    z = sp.symbols(f"z1:{n+1}")
    w = [z[k] - z[0] for k in range(1, n)]
    d = n - 2
    monos = [sp.Mul(*[w[i] ** e for i, e in enumerate(es)])
             for es in itertools.product(range(d + 1), repeat=n - 1) if sum(es) == d]
    unk, P = [], []
    for m in range(n):
        Pm = sp.zeros(rows, cols)
        for r in range(rows):
            for c in range(cols):
                a = sp.symbols(f"a{m}_{r}{c}_0:{len(monos)}")
                unk += a
                Pm[r, c] = sum(x * y for x, y in zip(a, monos))
        P.append(Pm)
    Dm = [sp.Mul(*[z[m] - z[j] for j in range(n) if j != m]) for m in range(n)]
    Delta = sp.Mul(*[z[i] - z[j] for i in range(n) for j in range(i + 1, n)])
    return z, unk, P, Dm, Delta


def coeffs(e, z):
    e = sp.expand(e)
    return sp.Poly(e, *z).coeffs() if e != 0 else []


def class_equations(n, z, P, Dm, Delta):
    t = sp.Symbol("t")
    rows, cols = P[0].shape
    eqs = []
    for r in range(rows):
        for c in range(cols):
            eqs += coeffs(sp.cancel(sum(P[m][r, c] / Dm[m] for m in range(n)) * Delta), z)
    for i in range(n):
        for j in range(i + 1, n):
            for r in range(rows):
                for c in range(cols):
                    eqs += coeffs(P[i][r, c].subs({z[i]: t, z[j]: t})
                                  - P[j][r, c].subs({z[i]: t, z[j]: t}), z)
    return eqs


def flat_equations(n, z, eta, Delta, A0):
    """d eta + A0 ^ eta + eta ^ A0 = 0 (A0 = list of matrices, or scalars)."""
    eqs = []
    for a in range(n):
        for b in range(a + 1, n):
            F = (sp.diff(eta[b], z[a]) - sp.diff(eta[a], z[b])
                 + A0[a] * eta[b] - eta[b] * A0[a] + eta[a] * A0[b] - A0[b] * eta[a]) \
                if isinstance(eta[0], sp.MatrixBase) else \
                (sp.diff(eta[b], z[a]) - sp.diff(eta[a], z[b]) + A0[a] * eta[b] - A0[b] * eta[a])
            ents = list(F) if isinstance(F, sp.MatrixBase) else [F]
            for e in ents:
                eqs += coeffs(sp.cancel(sp.together(e) * Delta ** 2), z)
    return eqs


def nullity(eqs, unk):
    eqs = [e for e in eqs if e != 0]
    if not eqs:
        return len(unk), None
    M = sp.Matrix([[sp.diff(e, u) for u in unk] for e in eqs])
    return len(unk) - M.rank(), M


def arnold_eta(n, z, rows, cols):
    R, ru = {}, []
    for i in range(n):
        for j in range(i + 1, n):
            Rij = sp.Matrix(rows, cols, lambda r, c: sp.Symbol(f"r{i}{j}_{r}{c}"))
            R[(i, j)] = Rij
            ru += list(Rij)
    eta = [sum((R[(min(m, j), max(m, j))] / (z[m] - z[j]) for j in range(n) if j != m),
               sp.zeros(rows, cols)) for m in range(n)]
    return eta, ru


def scalar_run(n, lam_c, label):
    z, unk, P, Dm, Delta = setup(n)
    eta = [P[m][0, 0] / Dm[m] for m in range(n)]
    lam = [sum(lam_c[(min(a, j), max(a, j))] / (z[a] - z[j]) for j in range(n) if j != a)
           for a in range(n)]
    base = class_equations(n, z, P, Dm, Delta)
    dim_class, _ = nullity(base, unk)
    dim_flat, _ = nullity(base + flat_equations(n, z, eta, Delta, lam), unk)
    etaA, ru = arnold_eta(n, z, 1, 1)
    etaA = [e[0, 0] for e in etaA]
    eqA = []
    eqA += coeffs(sp.cancel(sum(etaA) * Delta), z)
    dim_arn, _ = nullity(eqA, ru)
    dim_arn_flat, _ = nullity(eqA + flat_equations(n, z, etaA, Delta, lam), ru)
    print(f"n={n} {label}: class={dim_class} arnold={dim_arn} | flat class={dim_flat} "
          f"flat arnold={dim_arn_flat}", flush=True)
    return dict(n=n, twist=label, class_dim=dim_class, arnold_dim=dim_arn,
                flat_class_dim=dim_flat, flat_arnold_dim=dim_arn_flat)


def non_arnold_example():
    """An explicit element of C_4 outside the Arnold span, with its residue along z1 = z2."""
    n = 4
    z, unk, P, Dm, Delta = setup(n)
    _, M = nullity(class_equations(n, z, P, Dm, Delta), unk)
    for v in M.nullspace():
        sub = dict(zip(unk, v))
        Pm = [sp.factor(P[m][0, 0].subs(sub)) for m in range(n)]
        res12 = sp.factor(sp.cancel(((z[0] - z[1]) * Pm[0] / Dm[0]).subs(z[0], z[1])))
        if sp.Poly(sp.numer(sp.together(res12)), *z).total_degree() > 0 and \
                sp.denom(sp.together(res12)).free_symbols:
            print(f"non-Arnold element of C_4: P_1 = {Pm[0]}; residue along z1=z2: {res12}",
                  flush=True)
            return str(res12)
    return None


def nonabelian_run(kappa):
    n = 4
    pairings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    norm = lambda p: tuple(sorted(tuple(sorted(x)) for x in p))
    B = sp.Matrix([[1, 0], [-1, 1], [0, -1]])
    Bp = (B.T * B).inv() * B.T
    S = {}
    for i in range(n):
        for j in range(i + 1, n):
            perm = list(range(n)); perm[i], perm[j] = j, i
            Mij = sp.zeros(3, 3)
            for c, p in enumerate(pairings):
                Mij[pairings.index(norm(tuple(tuple(perm[k] for k in x) for x in p))), c] = 1
            R = Bp * Mij * B
            assert Mij * B == B * R
            S[(i, j)] = R
    z, unk, P, Dm, Delta = setup(n, 2, 2)
    A0 = [sum((kappa * S[(min(a, j), max(a, j))] / (z[a] - z[j]) for j in range(n) if j != a),
              sp.zeros(2, 2)) for a in range(n)]
    eta = [P[m] / Dm[m] for m in range(n)]
    dim, _ = nullity(class_equations(n, z, P, Dm, Delta) + flat_equations(n, z, eta, Delta, A0),
                     unk)
    etaA, ru = arnold_eta(n, z, 2, 2)
    eqA = []
    for r in range(2):
        for c in range(2):
            eqA += coeffs(sp.cancel(sum(e[r, c] for e in etaA) * Delta), z)
    dimA, _ = nullity(eqA + flat_equations(n, z, etaA, Delta, A0), ru)
    print(f"n=4 KZ first order, kappa={kappa}: flat class={dim} flat arnold={dimA}", flush=True)
    return dict(kappa=str(kappa), flat_class_dim=dim, flat_arnold_dim=dimA)


if __name__ == "__main__":
    results = []
    for n in (3, 4):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        random.seed(1)
        results.append(scalar_run(n, {p: 0 for p in pairs}, "closed (lam=0)"))
        results.append(scalar_run(n, {p: sp.Rational(random.randint(1, 97), random.randint(1, 97))
                                      for p in pairs}, "generic lam"))
        results.append(scalar_run(n, {p: (1 if p == (0, 1) else 0) for p in pairs},
                                  "lam = dlog(z1-z2)"))
    non_arnold_example()
    if "--nonabelian" in sys.argv:
        for k in (sp.Rational(3, 7), sp.Rational(1, 3), sp.Rational(1, 2), sp.Integer(1)):
            nonabelian_run(k)
