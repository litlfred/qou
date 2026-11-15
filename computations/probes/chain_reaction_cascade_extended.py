"""Extended scan for chain_reaction_cascade_probe (issue #7895): A = 3 chain,
(a) fixed bond power m = 1, 2, 3 with k <= 6; (b) m = 1 with k <= 12.
Prints only.  Result 2026-11-15: m=1 0 feasible, m=2 84 feasible (best
(1,3,2), cost 12 in k), m=3 0 feasible; k <= 12, m = 1: 2 feasible,
(12,12,9) and (12,12,12).  mpmath only."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import chain_reaction_cascade_probe as P
import mpmath as mp
from itertools import product
mp.mp.dps = P.DPS
q = mp.mpf(P.Q_50_DIGIT_STR); h = q - 1/q
C = P.Chars(9, q)
t0 = time.time()
# (a) bond power m in 1..3, k <= 6
def bondm(i, m):
    return P.bond(i, h) * m
for m in (1, 2, 3):
    feas = []; best = None
    for k in product(range(1, 7), repeat=3):
        w = P.joint(list(k), [], h) + bondm(0, m) + bondm(1, m)
        ch = C.chi(w, ("m", m, k))
        viol = mp.fsum(max(mp.mpf(0), -c) for c in ch)
        if viol < P.TOL: feas.append(list(k))
        e = (viol, 2*sum(k))
        if best is None or P.better(e, best[0]): best = (e, list(k))
    print(f"bond power m={m}: {len(feas)} feasible, first {feas[:8]}, best {best[1]} viol {mp.nstr(best[0][0],5)} cost {best[0][1]}  wall {time.time()-t0:.0f}s", flush=True)
# (b) k <= 12, bond power 1
P.KMAX = 12
feas = []; best=None
for k in product(range(1, 13), repeat=3):
    e, _ = P.energy(C, list(k), [0, 1], h)
    if e[0] == 0: feas.append(list(k))
    if best is None or P.better(e, best[0]): best = (e, list(k))
print(f"k<=12, m=1: {len(feas)} feasible, first {feas[:10]}, best {best[1]} viol {mp.nstr(best[0][0],5)} cost {best[0][1]} wall {time.time()-t0:.0f}s", flush=True)
