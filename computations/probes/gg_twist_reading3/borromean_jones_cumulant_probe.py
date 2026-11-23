"""Exact Jones cumulants of the Borromean braid V^3 = (s0 s1^-1)^3.

Tests the convolution-cumulant principle (QOU.VirtualSubword.connected,
connected_eq_zero_of_split) on a link whose pairwise sublinks are unlinks.

G(L) := delta * V_L(t), delta = -(t^{1/2} + t^{-1/2}), is multiplicative under
split union (V(L1 u L2) = delta V(L1) V(L2)) and G(unknot) = delta. The
normalised log F(T) = log G(L_T) - |T| log delta is additive on splits and 0 on
unlinks; F(empty) := 0. Its connected part on T = {1,2,3} is then the GHZ-level
(three-party) entanglement measure.

Exact arithmetic: the Kauffman bracket is computed by a state sum in sympy over
Z[A, A^-1]; evaluation at q0 is in mpmath at 70 dps. No float64.

Convention: A = t^(-1/4). The t <-> q dictionary is not fixed here, so the
evaluation is reported at both t = q0 and t = q0^2. The Borromean rings are
amphichiral, so t -> 1/t does not change V, and those two cover the readings
t = q^{+-1}, t = q^{+-2}.
"""
import itertools, json, os, sys, time
import sympy as sp
import mpmath as mp

mp.mp.dps = 70
A, t = sp.symbols("A t", positive=True)
d = -A**2 - A**-2

def bracket(word, n):
    """Kauffman bracket of the braid closure, normalised <unknot> = 1."""
    m = len(word)
    total = 0
    for state in itertools.product((0, 1), repeat=m):
        parent = {}
        def f(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def u(x, y): parent[f(x)] = f(y)
        nA = 0
        for k, (i, s) in enumerate(word):
            nxt = (k + 1) % m  # closure: level m == level 0
            for j in range(n):
                if j not in (i, i + 1):
                    u((k, j), (nxt, j))
            vertical = (state[k] == 0)
            # A-smoothing is vertical for s=+1, horizontal for s=-1
            isA = vertical if s > 0 else not vertical
            nA += 1 if isA else 0
            if vertical:
                u((k, i), (nxt, i)); u((k, i + 1), (nxt, i + 1))
            else:
                u((k, i), (k, i + 1)); u((nxt, i), (nxt, i + 1))
        loops = len({f((k, j)) for k in range(m) for j in range(n)})
        nB = m - nA
        total += A**nA * A**(-nB) * d**(loops - 1)
    return sp.expand(total)

def jones(word, n):
    w = sum(s for _, s in word)
    V = sp.expand((-A**3)**(-w) * bracket(word, n))
    return sp.expand(V.subs(A, t**sp.Rational(-1, 4)))

def restrict(word, n, keep):
    """Braid word on the strands in `keep` (pure braid: strand = position track)."""
    pos = list(range(n))  # pos[p] = strand currently at position p
    out = []
    for i, s in word:
        a, b = pos[i], pos[i + 1]
        if a in keep and b in keep:
            # positions among kept strands
            kept = [x for x in pos if x in keep]
            out.append((kept.index(a), s))
        pos[i], pos[i + 1] = b, a
    return out, len(keep)

def main():
    V3 = [(0, 1), (1, -1)] * 3
    checks = []
    t0 = time.time()
    J = {}
    for T in itertools.chain.from_iterable(itertools.combinations(range(3), r) for r in (1, 2, 3)):
        w, k = restrict(V3, 3, set(T))
        J[T] = sp.simplify(jones(w, k)) if w else (-(t**sp.Rational(1,2) + t**sp.Rational(-1,2)))**(k - 1)
        print(T, J[T], f"{time.time()-t0:.1f}s", flush=True)

    delta = -(sp.sqrt(t) + 1/sp.sqrt(t))
    known_bor = -t**3 + 3*t**2 - 2*t + 4 - 2/t + 3/t**2 - 1/t**3
    c1 = sp.simplify(J[(0, 1, 2)] - known_bor) == 0
    checks.append(("V(Borromean) matches the tabulated Jones polynomial", c1))
    c2 = all(sp.simplify(J[T] - delta**(len(T) - 1)) == 0 for T in J if len(T) < 3)
    checks.append(("every proper sublink is an unlink (pairs: V = delta, singles: V = 1)", c2))

    ratio = sp.simplify(J[(0, 1, 2)] / delta**2)   # = G(L_T) / delta^{|T|}
    c3 = sp.simplify(ratio.subs(t, 1) - 1) == 0
    checks.append(("ratio V_Bor/delta^2 = 1 at t = 1 (cumulant vanishes classically)", c3))

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../tools/qou-substrate/python"))
    from qou_substrate.constants import q_at
    q0 = mp.mpf(q_at())
    f = sp.lambdify(t, ratio, "mpmath")
    res = {}
    for lab, tv in (("t=q0", q0), ("t=q0^2", q0**2)):
        r = f(tv)
        phi = mp.log(r) if r > 0 else None
        res[lab] = {"ratio": mp.nstr(r, 30), "phi_123": mp.nstr(phi, 30) if phi is not None else "ratio<=0"}
        print(lab, res[lab])
    c4 = all(mp.mpf(v["ratio"]) != 1 for v in res.values())
    checks.append(("phi_123 != 0 at q0 under both t readings (three-party entanglement detected)", c4))

    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
    out = {
        "description": "Exact Jones cumulants of the Borromean braid (s0 s1^-1)^3; GHZ-level connected part.",
        "producer": "computations/probes/gg_twist_reading3/borromean_jones_cumulant_probe.py",
        "q0Value": mp.nstr(q0, 50), "q0Anchor": "proton",
        "jones": {",".join(map(str, T)): str(J[T]) for T in J},
        "ratio_symbolic": str(ratio),
        "evaluations": res,
        "pairwise_connected_parts": "0 exactly (every pair sublink is an unlink)",
        "checks": [{"name": n, "pass": bool(o)} for n, o in checks],
    }
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "borromean-jones-cumulant.witness.json"), "w"), indent=2)
    sys.exit(0 if all(o for _, o in checks) else 1)


if __name__ == "__main__":
    main()
