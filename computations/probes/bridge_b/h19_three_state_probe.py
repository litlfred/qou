"""H19: twisted-trace weight test on the gl_N vector module (C^N)^n. See h19_preregistration.md."""
from fractions import Fraction as Fr
import itertools, sys
v = Fr(2); h = v - 1/v

def run(N, n):
    def R_apply(i, vec):   # strands i, i+1 (1-based)
        out = {}
        for b, c in vec.items():
            x, y = b[i-1], b[i]
            def add(t, w):
                out[t] = out.get(t, 0) + w
            if x == y: add(b, c*v)
            else:
                sw = b[:i-1] + (y, x) + b[i+1:]
                if x < y: add(sw, c)
                else: add(sw, c); add(b, c*h)
        return {k: w for k, w in out.items() if w}
    def J_apply(vec):
        return {tuple(N-1-a for a in reversed(b)): c for b, c in vec.items()}
    basis = list(itertools.product(range(N), repeat=n))
    ok_inv = all(J_apply(J_apply({b: Fr(1)})) == {b: Fr(1)} for b in basis)
    ok_int = all(J_apply(R_apply(i, J_apply({b: Fr(1)}))) == R_apply(n-i, {b: Fr(1)})
                 for i in range(1, n) for b in basis)
    print(f"N = {N}, n = {n}: J^2 = 1 {ok_inv}; J rho(T_i) J = rho(T_(n-i)) {ok_int}")
    if not (ok_inv and ok_int): return
    fixed_w = [b for b in basis if sorted(b) == sorted(N-1-a for a in b)]  # J preserves the weight
    print(f"  basis vectors in J-stable weight spaces: {len(fixed_w)} of {len(basis)}")
    orbits = sorted({tuple(sorted({i, n-i})) for i in range(1, n)})
    for I in orbits:
        if len(I) == 1: word, L = [I[0]], 1
        elif I[1] - I[0] == 1: word, L = [I[0], I[1], I[0]], 3
        else: word, L = [I[0], I[1]], 2
        def A(vec):
            for i in reversed(word): vec = R_apply(i, vec)
            return vec
        p = [Fr(0)]*11
        for b in fixed_w:
            vec = {b: Fr(1)}
            for k in range(11):
                Jv = J_apply(vec)
                p[k] += Jv.get(b, 0)
                vec = A(vec)
        passing = []
        for Lc in (1, 2, 3, 4, 5):
            for sgn in (-1, 1):
                a, bb = v**Lc, sgn*v**(-Lc)
                if all(p[k+2] == (a+bb)*p[k+1] - a*bb*p[k] for k in range(9)): passing.append((Lc, sgn))
        nz = any(x != 0 for x in p)
        verdict = "inconclusive (all zero)" if not nz else str(bool(passing) and all(Lc == L for Lc, _ in passing))
        print(f"  orbit {I}, word {word}, L = {L}: passing (L', sign) = {passing}; weight forced to L: {verdict}")
        print(f"     p_0..p_3 = {[str(x) for x in p[:4]]}")
    sys.stdout.flush()

print("control: N = 2 must reproduce H18")
for n in (4, 6): run(2, n)
print("test: N = 3")
for n in (4, 5, 6, 7): run(3, n)
