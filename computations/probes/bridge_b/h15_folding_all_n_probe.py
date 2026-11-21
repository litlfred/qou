"""H15: Lusztig quasisplit folding of S_n by iota = conj(w0), n = 3..7: shape, KL parity/bound, equal-weight control."""
import sys, time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import importlib.util
spec = importlib.util.spec_from_file_location("h14", __file__.rsplit("/", 1)[0] + "/h14_kl_folding_probe.py")
src = open(spec.origin).read().split("n = 6\namb_gens")[0]   # reuse definitions only
ns = {}; exec(src, ns)
kl_basis, compose, coxeter = ns["kl_basis"], ns["compose"], ns["coxeter"]
from math import factorial

def s(j, n):
    p = list(range(n)); p[j-1], p[j] = p[j], p[j-1]; return tuple(p)

def compare(Cf, Ca):
    ok2 = okab = True; pairs = diffs = neg = 0
    for x, row in Cf.items():
        for y in Cf:
            p, pt = row.get(y, {}), Ca[x].get(y, {})
            if not p and not pt: continue
            pairs += 1
            for e in set(p) | set(pt):
                a, at = p.get(e, 0), pt.get(e, 0)
                if (a - at) % 2: ok2 = False
                if abs(a) > abs(at): okab = False
                if a != at: diffs += 1; neg += a < 0
    return ok2, okab, pairs, diffs, neg

for n in range(3, 8):
    t0 = time.time()
    amb = [s(j, n) for j in range(1, n)]
    gens, L, desc = [], [], []
    for j in range(1, n):
        k = n - j
        if j > k: break
        if j == k: gens.append(s(j, n)); L.append(1); desc.append(f"s{j}")
        elif k == j + 1: gens.append(compose(compose(s(j, n), s(k, n)), s(j, n))); L.append(3); desc.append(f"s{j}s{k}s{j}")
        else: gens.append(compose(s(j, n), s(k, n))); L.append(2); desc.append(f"s{j}s{k}")
    W = coxeter(gens, n)
    m = len(gens)
    pred = 2 if n == 3 else 2**m * factorial(m)
    w0 = tuple(reversed(range(n)))
    fixed = sum(1 for w in coxeter(amb, n) if compose(compose(w0, w), w0) == w)
    Ca, _ = kl_basis(amb, [1]*(n-1), n)
    Cf, _ = kl_basis(gens, L, n)
    r = compare(Cf, Ca)
    Cc, _ = kl_basis(gens, [1]*m, n)
    rc = compare(Cc, Ca)
    print(f"n={n}: generators {desc} weights {L}; |W| = {len(W)}, predicted {pred}, centraliser of w0 = {fixed}; "
          f"B parity {r[0]}, bound {r[1]} over {r[2]} pairs, differing {r[3]} (negative {r[4]}); "
          f"C control equal weights passes B: {rc[0] and rc[1]}  [{time.time()-t0:.1f}s]", flush=True)
