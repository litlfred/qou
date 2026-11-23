"""S1 of PREREG.md: is there a U_q(g2)-equivariant TWO-eigenvalue braiding on V7 (q-deformed Im O)?

Exact. The U_q(g2) module V7 and Jantzen coproduct are those of
computations/eightfold/quantum_g2_braiding_on_colour_triplet_probe.py (alpha1 short, q1 = q;
alpha2 long, q2 = q^3). At a sample q in {2, 3} (exact rational):
 1. commutant C = End_{U_q(g2)}(V7 (x) V7) over Q (sympy nullspace, exact rationals);
 2. C is commutative and split (V7 (x) V7 = 1 + 7 + 14 + 27, multiplicity free), so a generic
    element has 4 distinct rational eigenvalues; the primitive idempotents P_1..P_4 are its
    Lagrange projectors (exact rationals);
 3. every two-eigenvalue element is, up to an overall scalar, x(t) = P_S + t P_{S^c}; the braid
    relation x1 x2 x1 - x2 x1 x2 = A0 + A1 t + A2 t^2 + A3 t^3 on V7^{(x)3} (343-dim). The
    coefficient matrices are computed mod a prime p < 2^26 (integer matmul, no overflow); a
    common root t of all entries (t != 0, 1) is searched in F_p. A nonzero residue proves the
    rational identity fails (denominators are checked invertible mod p); any surviving t would
    be re-checked over Q (none is expected).
A failure at a sample q proves failure of the generic (Q(q)) identity, because a generic
identity specialises.
"""
import sys, json, os, itertools
import sympy as sp
import numpy as np  # float64-ok: exact int64 modular matmul over F_p (p = 67108859 < 2^26; 343 * p^2 < 2^63, zero floats)

P_MOD = 67108859  # prime < 2^26
assert sp.isprime(P_MOD)

LAB = [(1, 0), (-1, 1), (2, -1), (0, 0), (-2, 1), (1, -1), (-1, 0)]


def qint(n, x):
    return sum(x ** (n - 1 - 2 * k) for k in range(n))


def module(q):
    q1, q2 = q, q ** 3
    Z = lambda: sp.zeros(7)
    E = {1: Z(), 2: Z()}; F = {1: Z(), 2: Z()}; K = {1: Z(), 2: Z()}; Ki = {1: Z(), 2: Z()}
    for v, (a, b) in enumerate(LAB):
        K[1][v, v] = q1 ** a; K[2][v, v] = q2 ** b; Ki[1][v, v] = q1 ** -a; Ki[2][v, v] = q2 ** -b
    strings = {1: [[0, 1], [2, 3, 4], [5, 6]], 2: [[1, 2], [4, 5]]}
    for i, sts in strings.items():
        qi = q1 if i == 1 else q2
        for st in sts:
            n = len(st)
            for k in range(1, n):
                a, b = st[k - 1], st[k]; F[i][b, a] = 1; E[i][a, b] = qint(k, qi) * qint(n - k, qi)
    return E, F, K, Ki


def commutant(q):
    from sympy.physics.quantum import TensorProduct as TP
    E, F, K, Ki = module(q)
    I = sp.eye(7)
    G = []
    for i in (1, 2):
        G.append(TP(E[i], I) + TP(K[i], E[i])); G.append(TP(F[i], Ki[i]) + TP(I, F[i]))
    basis = [(a, b) for a in range(7) for b in range(7)]
    tw = lambda i: (LAB[basis[i][0]][0] + LAB[basis[i][1]][0], LAB[basis[i][0]][1] + LAB[basis[i][1]][1])
    var = [(r, c) for r in range(49) for c in range(49) if tw(r) == tw(c)]
    idx = {rc: k for k, rc in enumerate(var)}
    rows = []
    for X in G:
        for r in range(49):
            for c in range(49):
                row = {}
                for t in range(49):
                    if X[t, c] != 0 and (r, t) in idx: row[idx[(r, t)]] = row.get(idx[(r, t)], 0) + X[t, c]
                    if X[r, t] != 0 and (t, c) in idx: row[idx[(t, c)]] = row.get(idx[(t, c)], 0) - X[r, t]
                row = {k: v for k, v in row.items() if v != 0}
                if row: rows.append(row)
    A = sp.zeros(len(rows), len(var))
    for i, row in enumerate(rows):
        for k, v in row.items(): A[i, k] = v
    from sympy.polys.matrices import DomainMatrix
    N = DomainMatrix.from_Matrix(A).convert_to(sp.QQ).nullspace().to_Matrix()
    mats = []
    for s in range(N.shape[0]):
        Mx = sp.zeros(49)
        for k, (r, c) in enumerate(var): Mx[r, c] = N[s, k]
        mats.append(Mx)
    return mats


def idempotents(mats):
    # generic element: combination with small integer coefficients; retry until 4 distinct eigenvalues
    for coeffs in itertools.product(range(1, 6), repeat=len(mats)):
        X = sum((c * m for c, m in zip(coeffs, mats)), sp.zeros(49))
        ev = list(X.eigenvals().keys())
        if len(ev) == len(mats) and all(e.is_rational for e in ev):
            Ps = []
            for i, e in enumerate(ev):
                Pm = sp.eye(49)
                for j, f in enumerate(ev):
                    if j != i: Pm = Pm * (X - f * sp.eye(49)) / (e - f)
                Ps.append(Pm)
            return Ps
    raise RuntimeError("no generic element found")


def modp(Mx):
    out = np.zeros(Mx.shape, dtype=np.int64)
    for i in range(Mx.shape[0]):
        for j in range(Mx.shape[1]):
            v = sp.Rational(Mx[i, j])
            if v != 0:
                num, den = int(v.p), int(v.q)
                assert den % P_MOD != 0
                out[i, j] = (num % P_MOD) * pow(den, P_MOD - 2, P_MOD) % P_MOD
    return out


def mm(a, b):
    return (a @ b) % P_MOD


def kron(a, b):
    return np.kron(a, b) % P_MOD


def run(qv):
    q = sp.Integer(qv)
    mats = commutant(q)
    res = {"q": qv, "commutant_dim": len(mats)}
    Ps = idempotents(mats)
    ranks = [int(sp.trace(Pm)) for Pm in Ps]
    res["idempotent_ranks"] = ranks  # expect {1, 7, 14, 27}
    Pp = [modp(Pm) for Pm in Ps]
    I7 = np.eye(7, dtype=np.int64)
    out = []
    labels = {1: "1", 7: "7", 14: "14", 27: "27"}
    seen = set()
    for r in range(1, 4):
        for S in itertools.combinations(range(4), r):
            Sc = tuple(i for i in range(4) if i not in S)
            key = frozenset([S, Sc])
            if key in seen: continue
            seen.add(key)
            A = sum(Pp[i] for i in S) % P_MOD
            B = sum(Pp[i] for i in Sc) % P_MOD
            # x(t) = A + t B ; x1 = x (x) I, x2 = I (x) x
            A1, B1 = kron(A, I7), kron(B, I7)
            A2, B2 = kron(I7, A), kron(I7, B)
            # x1 x2 x1 - x2 x1 x2, coefficient of t^k
            def tri(X, Y, Z): return mm(mm(X, Y), Z)
            coef = []
            terms = {0: (A1, A2), 1: (B1, B2)}
            for k in range(4):
                C = np.zeros((343, 343), dtype=np.int64)
                for bits in itertools.product((0, 1), repeat=3):
                    if sum(bits) != k: continue
                    a, b, c = bits
                    X1 = terms[a][0]; Y2 = terms[b][1]; Z1 = terms[c][0]
                    X2 = terms[a][1]; Y1 = terms[b][0]; Z2 = terms[c][1]
                    C = (C + tri(X1, Y2, Z1) - tri(X2, Y1, Z2)) % P_MOD
                coef.append(C)
            # common roots in F_p: take entries; find gcd of entry polynomials via a few entries
            nz = [(i, j) for i in range(343) for j in range(343)
                  if any(int(coef[k][i, j]) for k in range(4))]
            x = sp.symbols('x')
            g = None
            for (i, j) in nz[:400]:
                pl = sp.Poly(sum(int(coef[k][i, j]) * x ** k for k in range(4)), x, modulus=P_MOD)
                g = pl if g is None else sp.gcd(g, pl)
                if g.degree() <= 0: break
            roots = []
            if g is not None and g.degree() > 0:
                for f, _ in sp.factor_list(g.as_expr(), modulus=P_MOD)[1]:
                    fp = sp.Poly(f, x, modulus=P_MOD)
                    if fp.degree() == 1:
                        c1, c0 = [int(c) for c in fp.all_coeffs()]
                        roots.append((-c0 * pow(c1, P_MOD - 2, P_MOD)) % P_MOD)
            # verify candidate roots against ALL entries
            good = []
            for t0 in roots:
                if t0 in (0, 1): continue
                ok = True
                tot = (coef[0] + t0 * coef[1] % P_MOD + (t0 * t0 % P_MOD) * coef[2] % P_MOD
                       + (pow(t0, 3, P_MOD)) * coef[3] % P_MOD) % P_MOD
                if tot.any(): ok = False
                if ok: good.append(t0)
            out.append({"S": [labels.get(ranks[i], ranks[i]) for i in S],
                        "Sc": [labels.get(ranks[i], ranks[i]) for i in Sc],
                        "nonzero_entries": len(nz),
                        "gcd_degree": (g.degree() if g is not None else None),
                        "common_roots_modp_excluding_0_1": good})
            print(qv, out[-1], flush=True)
    res["splits"] = out
    res["any_two_eigenvalue_braiding"] = any(o["common_roots_modp_excluding_0_1"] for o in out)
    return res


if __name__ == "__main__":
    results = [run(2), run(3)]
    here = os.path.dirname(os.path.abspath(__file__))
    out = {"producer": "computations/probes/qcd_octonion_colour_strand/g2_hecke_search_probe.py",
           "prereg": "computations/probes/qcd_octonion_colour_strand/PREREG.md (S1)",
           "arithmetic": "sympy exact rationals for the commutant and idempotents; braid-relation "
                         "coefficient matrices mod p = 67108859 (exact in F_p; a nonzero residue "
                         "is a proof of failure over Q)",
           "q0Anchor": "independent",
           "q0AnchorReason": "exact rational sample points q in {2, 3}; q0 never read",
           "results": results}
    with open(os.path.join(here, "g2-hecke-search.witness.json"), "w") as f:
        json.dump(out, f, indent=1)
    print("ANY two-eigenvalue U_q(g2)-equivariant braiding on V7:",
          [r["any_two_eigenvalue_braiding"] for r in results])
