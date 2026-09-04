"""Exact A-body hierarchy, full Mobius over all 2^A - A - 1 subsets (so
exchangeability is TESTED, not assumed).  See `_exact_trace_engine.py`.

    EXACT_PROCS=2 python3 computations/_exact_trace_runs/a5.py pnpnn OUTDIR
"""
import json
import sys
import time
from itertools import combinations
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402
import _exact_trace_engine as E  # noqa: E402
import mpmath as mp  # noqa: E402
from codata_constants import M_E_MEV as _ME  # noqa: E402

ME = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
ALPHA = mpfr(mp.nstr(ME, 40)) / (E.Q * (E.Q - 1))
ORDER = sys.argv[1]
OUTDIR = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")
A = len(ORDER)
n = 3 * A
OUT = OUTDIR / f"exact_a{A}_{ORDER}.json"
print(f"A={A} order={ORDER} n={n} bits={E.BITS} procs={E.PROCS}", flush=True)

t0 = time.time()
tf = E.trM(n, E.word(ORDER, set()))
print(f"free trace ({time.time() - t0:.0f}s)", flush=True)
Ls = {}
for r in range(2, A + 1):
    for S in combinations(range(A), r):
        ts = time.time()
        Ls[S] = gmpy2.log(tf / E.trM(n, E.word(ORDER, set(S))))
        print(f"  L{S} = {float(Ls[S]):.15f}  ({time.time() - ts:.0f}s,"
              f" {len(Ls)}/{2 ** A - A - 1})", flush=True)
        json.dump({"order": ORDER, "bits": E.BITS, "partial": True,
                   "L": {str(k): str(v) for k, v in Ls.items()}}, open(OUT, "w"))

cum = {}
for r in range(2, A + 1):
    for S in combinations(range(A), r):
        c = Ls[S]
        for m in range(2, r):
            c -= sum(cum[T] for T in combinations(S, m))
        cum[S] = c
tot = {r: sum(cum[S] for S in combinations(range(A), r)) for r in range(2, A + 1)}
print(f"\n=== A={A} cumulant hierarchy ({ORDER}), {E.BITS}-bit ===", flush=True)
prev = None
for r in range(2, A + 1):
    rt = abs(tot[r] / prev) if prev else None
    print(f"  k={r}  terms {comb(A, r):>2d}  c_k = {float(tot[r]):>+15.9f}"
          f"  MeV {float(ALPHA * tot[r]):>+10.5f}"
          f"  ratio {('%.6f' % float(rt)) if rt is not None else '   -    '}", flush=True)
    prev = tot[r]
full = Ls[tuple(range(A))]
resid = abs(sum(tot.values()) - full)
print(f"  reconstruction resid {float(resid):.3e}", flush=True)
json.dump({"order": ORDER, "bits": E.BITS, "partial": False,
           "L": {str(k): str(v) for k, v in Ls.items()},
           "c": {str(r): str(tot[r]) for r in tot}, "resid": str(resid)},
          open(OUT, "w"), indent=1)
print(f"\ntotal {time.time() - t0:.0f}s", flush=True)
