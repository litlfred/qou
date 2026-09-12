"""End-to-end binding wall-time vs A — the measurement bean `qou-sv7h`'s TITLE asks for.

`qou-sv7h` is titled "binding compute cannot scale". Every figure that arc has
produced is PER PARTITION (the dead-scipy census, the 25 `_matmul_dim` calls,
the dim-2310 kernel A/B at 18m26s vs 35.6s). None of them time
`binding_energy(Z, N)` itself, which is what the title is about.

This probe does. Kernel arm only; one timed call per isotope, A = 2..4.

MEASURED SO FAR (2026-09-12, this container, pyhecke_native 0.9.0, COMPUTE_DPS):

    2H   A=2   816.811 s   ok      (13.6 min)
    2H   A=2   818.807 s   ok      -- independent earlier run, 0.24 % apart
    3H   A=3   NO RESULT           -- see below

**The A=3 row is NOT a measurement and must not be quoted as one.** The run
started 3H at 12:34:31 UTC and the process was gone by 18:04 with no output and
no traceback -- but the CONTAINER REBOOTED at 17:55 (`who -b`), and the script's
own `timeout 21000` would not have fired until ~18:11. So the arm was killed by
infrastructure, not by its own budget, and the session was idle across the
window so the process may not have been running throughout. It establishes
NEITHER "3H takes > 5 h" NOR "3H completes".

To finish the measurement, re-run this with a budget you can sit through, or
checkpoint per isotope so a reclaim leaves partial evidence rather than none.
Do NOT pipe it through `tail` -- a buffered pipe turns a partial result into a
blank file (that trap cost a 20-minute run on 2026-09-12; bean `qou-sv7h`).
"""

import sys, time, json
sys.path.insert(0, '/home/user/qou/computations')
import mpmath as mp, hecke_core_legacy as H
from _precision import COMPUTE_DPS as DPS
mp.mp.dps = DPS
print(f"kernel: {H._HAS_LP_KERNEL}   dps: {DPS}", flush=True)
assert H._HAS_LP_KERNEL

ISOS = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"), (2, 2, "4He")]
out = []
for Z, N, name in ISOS:
    A = Z + N
    t0 = time.perf_counter()
    try:
        r = H.binding_energy(Z, N)
        dt = time.perf_counter() - t0
        val = (mp.nstr(r, 25) if isinstance(r, mp.mpf)
               else {k: (mp.nstr(v, 25) if isinstance(v, mp.mpf) else repr(v)) for k, v in r.items()}
               if isinstance(r, dict) else repr(r))
        out.append({"iso": name, "A": A, "sec": round(dt, 3), "ok": True, "value": val})
        print(f"  {name:>4}  A={A}  {dt:10.3f}s  ok", flush=True)
    except Exception as e:
        dt = time.perf_counter() - t0
        out.append({"iso": name, "A": A, "sec": round(dt, 3), "ok": False,
                    "error": f"{type(e).__name__}: {e}"})
        print(f"  {name:>4}  A={A}  {dt:10.3f}s  {type(e).__name__}: {e}", flush=True)
print(json.dumps(out, indent=1), flush=True)
