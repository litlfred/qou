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

CONFIGURATION the numbers above were taken at -- state this whenever you quote
them (added 2026-09-12 after a sibling on #7245 reported an apparently
conflicting figure; bean `qou-sv7h`).

`binding_energy(Z, N)` takes no `k_exact`, so this probe runs the DEFAULTS,
and the defaults are the expensive end:

    k_exact = k_max = K_PARTITION_MAX = 11
    active EXACT set     193 partitions,  sum(dim) = 48926,  max dim = 2310
    active GAUSSIAN set    0 partitions   (the window k_exact < k <= k_max is
                                           empty when they are equal)

For contrast, k_exact=4 is 10 partitions / sum(dim) 16, and k_exact=5 is 17 /
42. So a cost measured at k_exact=4 is NOT comparable to the rows above, and
816.811 s is the FULLY-EXACT figure rather than a cheap configuration.

**The kernel arm is asserted, not assumed** (`assert H._HAS_LP_KERNEL`), and
that is the discriminator against the sibling's number. #7245 reports the same
default `k_exact = 11` not finishing its first atom in ~25 min; the dim-2310
A/B on this branch measured the Python fallback at 31.2x the kernel, and
13.6 min x 31.2 ~ 7.1 h, so a 25-minute non-finish is what the FALLBACK arm
predicts and is not in tension with 816.811 s. `pyhecke_native` is not on PyPI,
so a container without it is the default state -- print `H._HAS_LP_KERNEL`
before comparing any wall-time row to these.

SCOPE — what the timing is and is not a claim about (added after sibling
coordination on PR #7229, from #7221 / #7235 / #7236).

**The wall-time rows are convention-independent.** A second is a second; nothing
about `z` changes how long the accumulator runs.

**The `value` field is not**, and a reader should not lift it as a canonical
binding number. The sibling raised that the binding/mass channel is still
convention C. MEASURED against this probe's own cone rather than taken on
trust, and the answer is more specific than that:

  - the C literals the sibling names (`TRM`, `TRM["D"] = 0.38835725751524`)
    live in `computations/gap_a3_overshoot_robustness_check.py`, and
    `hecke_core_legacy` neither references them nor imports that module
    (AST scan of all 20 imports: no `gap_a3` / `overshoot`);
  - `hecke_core_legacy` carries convention-D markers in its own source --
    line ~1288 `q^3/(q^2+1) = z_D, the convention-D Markov parameter`, and
    line ~86 `G_INV is gone under convention D`.

So the C exposure the sibling found is in the A3-overshoot producers, NOT in
`binding_energy`'s cone. What this probe does NOT establish is that every
constant reached downstream of `binding_energy` is D-consistent -- the sibling
separately reports `Vol_hyp` and `B/m_e` as C-era assignments (`qou-e5jf`
open), and that was not audited here.

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
