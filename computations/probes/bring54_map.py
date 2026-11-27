"""bring54_map -- the regular {5,4} map with orientation-preserving group S5
(Bring's surface) as an exact combinatorial cochain complex.

Darts = S5 (120). Vertex rotation sigma: g -> g*y with |y| = 4; edge involution
alpha: g -> g*t with |t| = 2; face rotation phi = sigma o alpha: g -> g*t*y with
|t*y| = 5; <y, t> = S5. Gives V, E, F = 30, 60, 24.

Orientation: edge e is the dart rep[e] = first dart of its alpha-cycle, running
from vertex vert_of[rep[e]] (tail) to vert_of[alpha[rep[e]]] (head). A face
cycle d, phi(d), ... traverses each dart from tail to head, so the face boundary
is sum over its darts of (sign of that dart relative to its edge's rep).

Pure integer combinatorics; imports no numerics. Used by
bring54_cochain_complex_probe.py and bring54_dec_qns_probe.py.
"""
import itertools

N = 5
ID = tuple(range(N))


def mul(a, b):
    return tuple(a[b[i]] for i in range(N))


def order(a):
    k, x = 1, a
    while x != ID:
        x, k = mul(x, a), k + 1
    return k


def _generated(gens):
    seen, frontier = {ID}, [ID]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = mul(g, h)
                if x not in seen:
                    seen.add(x)
                    nxt.append(x)
        frontier = nxt
    return seen


def _cycles(perm):
    seen, out = set(), []
    for d in range(len(perm)):
        if d in seen:
            continue
        c, x = [], d
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = perm[x]
        out.append(c)
    return out


def build():
    """Return a dict describing the map and its integer coboundaries."""
    S5 = list(itertools.permutations(range(N)))
    y = t = None
    for yy in S5:
        if order(yy) != 4:
            continue
        for tt in S5:
            if order(tt) == 2 and order(mul(tt, yy)) == 5 and len(_generated([yy, tt])) == 120:
                y, t = yy, tt
                break
        if y is not None:
            break
    idx = {g: i for i, g in enumerate(S5)}
    sigma = [idx[mul(g, y)] for g in S5]
    alpha = [idx[mul(g, t)] for g in S5]
    phi = [sigma[alpha[d]] for d in range(120)]
    Vc, Ec, Fc = _cycles(sigma), _cycles(alpha), _cycles(phi)
    V, E, F = len(Vc), len(Ec), len(Fc)
    vert_of = {d: i for i, c in enumerate(Vc) for d in c}
    face_of = {d: i for i, c in enumerate(Fc) for d in c}
    rep = [c[0] for c in Ec]
    edge_of = {}
    for e, c in enumerate(Ec):
        edge_of[c[0]] = (e, +1)
        edge_of[c[1]] = (e, -1)
    d0 = [[0] * V for _ in range(E)]
    for e in range(E):
        d = rep[e]
        d0[e][vert_of[d]] -= 1
        d0[e][vert_of[alpha[d]]] += 1
    d1 = [[0] * E for _ in range(F)]
    for f, c in enumerate(Fc):
        for d in c:
            e, s = edge_of[d]
            d1[f][e] += s
    return dict(y=y, t=t, sigma=sigma, alpha=alpha, phi=phi, Vc=Vc, Ec=Ec, Fc=Fc,
                V=V, E=E, F=F, vert_of=vert_of, face_of=face_of, rep=rep,
                edge_of=edge_of, d0=d0, d1=d1)
