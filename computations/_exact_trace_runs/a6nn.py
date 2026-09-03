"""A=6 homonuclear, exact, MINIMAL-n route (see `_exact_trace_engine.py`).

L_k is n-independent (Markov split-link factorisation + exchangeability, both
at 200 bits in `probes/the_binding_arc_was_measured_in_float64_probe.py`), so
each L_k is computed in its own minimal system n=3k.  Only L_6 costs anything:
two traces at n=18.  Every L_k is written to OUT as soon as it lands.

    EXACT_BITS=128 EXACT_PROCS=4 python3 computations/_exact_trace_runs/a6nn.py OUTDIR
"""
import json
import sys
import time
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gmpy2  # noqa: E402
from gmpy2 import mpfr  # noqa: E402
import _exact_trace_engine as E  # noqa: E402
import mpmath as mp  # noqa: E402
from codata_constants import M_E_MEV as _ME  # noqa: E402

OUTDIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
E.VERBOSE = True
ME = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
ALPHA = mpfr(mp.nstr(ME, 40)) / (E.Q * (E.Q - 1))
PART = OUTDIR / "exact_a6nn_L.json"
print(f"bits={E.BITS} procs={E.PROCS}", flush=True)

Lk = {}
for k in range(2, 7):
    order, n = "n" * k, 3 * k
    t0 = time.time()
    print(f"\n--- L_{k}  (n={n}) ---", flush=True)
    tf = E.trM(n, E.word(order, set()))
    print(f"    free done ({time.time() - t0:.0f}s)", flush=True)
    tb = E.trM(n, E.word(order, set(range(k))))
    Lk[k] = gmpy2.log(tf / tb)
    print(f"  L_{k} = {Lk[k]}   ({time.time() - t0:.0f}s)", flush=True)
    json.dump({"bits": E.BITS, "L": {str(j): str(v) for j, v in Lk.items()}},
              open(PART, "w"), indent=1)

cs = {}
for k in range(2, 7):
    cs[k] = Lk[k] - sum(comb(k, j) * cs[j] for j in range(2, k))
print(f"\n=== A=6 homonuclear size-only cumulants, {E.BITS}-bit ===", flush=True)
prev = None
for k in range(2, 7):
    tot = comb(6, k) * cs[k]
    rt = abs(tot / prev) if prev else None
    print(f"  k={k}  terms {comb(6, k):>2d}  c_k(single) {float(cs[k]):>+15.9f}"
          f"  c_k(total) {float(tot):>+15.9f}  MeV {float(ALPHA * tot):>+10.5f}"
          f"  ratio {('%.6f' % float(rt)) if rt is not None else '   -    '}", flush=True)
    prev = tot
json.dump({"bits": E.BITS, "L": {str(k): str(v) for k, v in Lk.items()},
           "c_single": {str(k): str(v) for k, v in cs.items()}},
          open(OUTDIR / "exact_a6nn.json", "w"), indent=1)
print("done", flush=True)
