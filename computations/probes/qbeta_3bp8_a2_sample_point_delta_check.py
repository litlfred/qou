#!/usr/bin/env python3
"""Full-settings A2 residual at the qou-vbw1 changed sample point — RESUMABLE.

The probe's own A2 needs longer than this container's restart interval (killed
twice). The dominant cost is building the I(m,e) cache, which is INDEPENDENT of
w, so it is persisted to disk: each restart resumes instead of starting over.

Runs at the probe's real settings (ORD_SEQ=1600, E_GF=60, dps from
set_compute_dps) so the residual is in the converged regime, unlike the reduced
proxy — which came out truncation-dominated at O(0.8), exactly as the probe's
comment warns.

Evaluates BOTH the old (typed, stale) and new (derived) sample point from the
same cache, so the comparison is exact and free once the cache exists.
"""
import json
import sys
import time
from pathlib import Path

import mpmath as mp

# Repo-root-relative (bean qou-c7g8/qou-6inm). These were absolute paths into a
# DIFFERENT machine's checkout (/home/user/qou), which resolve to nothing in any
# clone not at that exact path. A sys.path insert of a missing directory raises
# NOTHING, so the failure was silent until an unrelated-looking import died.
_QOU_ROOT = Path(__file__).resolve().parents[2]
ROOT = _QOU_ROOT
sys.path.insert(0, str(ROOT / "computations" / "probes"))
sys.path.insert(0, str(ROOT / "computations"))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from _awpk_fast_index import eval_I41_at  # noqa: E402
from qbeta_g3_fourone_index_assembly_corrected import e2_window_for  # noqa: E402
from qbeta_t4_anchors import theta_t4  # noqa: E402

set_compute_dps()

ORD_SEQ = 1600
E_GF = 60
MS = (-1, 0, 1, 2)                       # the probe's m values
CACHE = _QOU_ROOT / ".a2_icache.json"   # survives container restarts

q0 = q_at(50)
q = 1 / q0
qh = mp.sqrt(q)

_cache = {}
if CACHE.exists():
    raw = json.loads(CACHE.read_text())
    for k, v in raw.items():
        m, e = k.split(",")
        _cache[(int(m), int(e))] = mp.mpf(v)
    print(f"resumed: {len(_cache)} cached I(m,e) values", flush=True)


def _flush():
    CACHE.write_text(json.dumps(
        {f"{m},{e}": mp.nstr(v, 60) for (m, e), v in _cache.items()}))


def I(m, e):
    k = (m, e)
    if k not in _cache:
        _cache[k] = eval_I41_at(m, e, mp.sqrt(q), ORD_SEQ,
                                e2_window_for(ORD_SEQ, m, e))
        if len(_cache) % 10 == 0:
            _flush()
            print(f"    cache {len(_cache)}  [{time.time()-T0:.0f}s]", flush=True)
    return _cache[k]


T0 = time.time()

# Prebuild every I(m,e) the composition touches: m in [-2, 3], |e| <= E_GF.
need = [(m, e) for m in range(min(MS) - 1, max(MS) + 2)
        for e in range(-E_GF, E_GF + 1)]
todo = [k for k in need if k not in _cache]
print(f"need {len(need)} values, {len(todo)} still to compute", flush=True)
for m, e in todo:
    I(m, e)
_flush()
print(f"cache complete: {len(_cache)} values  [{time.time()-T0:.0f}s]", flush=True)


def F(m, w):
    return mp.fsum(I(m, e) * w ** e for e in range(-E_GF, E_GF + 1))


gf_If = lambda m, w: F(m, w)
gf_Mhat = lambda g: (lambda m, w: q ** (mp.mpf(m) / 2) * w * g(m, w))
gf_Minv = lambda g: (lambda m, w: q ** (-mp.mpf(m) / 2) / w * g(m, w))
gf_Lhat = lambda g: (lambda m, w: -g(m + 1, qh * w))
gf_Linv = lambda g: (lambda m, w: -g(m - 1, w / qh))
gf_add = lambda *gs: (lambda m, w: mp.fsum(h(m, w) for h in gs))
gf_scale = lambda c, g: (lambda m, w: c * g(m, w))

gM2, gMm2 = gf_Mhat(gf_Mhat(gf_If)), gf_Minv(gf_Minv(gf_If))
g_mid_in = gf_add(gM2, gMm2, gf_scale(-1, gf_Mhat(gf_If)),
                  gf_scale(-1, gf_Minv(gf_If)), gf_scale(-(q + 1 / q), gf_If))
g_mid = gf_add(gf_Mhat(g_mid_in), gf_scale(-1, gf_Minv(g_mid_in)))
g_t1 = gf_add(gf_scale(qh, gf_Mhat(gf_Linv(gf_If))),
              gf_scale(-1 / qh, gf_Minv(gf_Linv(gf_If))))
g_t3 = gf_add(gf_scale(1 / qh, gf_Mhat(gf_Lhat(gf_If))),
              gf_scale(-qh, gf_Minv(gf_Lhat(gf_If))))
g_L = gf_add(g_t1, gf_scale(-1, g_mid), g_t3)

THETA_OLD = mp.mpf("0.20323503")
THETA_NEW = theta_t4("proton")
A2_TOL = mp.mpf("1e-8")

print(f"\nORD_SEQ={ORD_SEQ}  E_GF=±{E_GF}  dps={mp.mp.dps}")
res = {}
for label, th in (("old (typed, stale)", THETA_OLD), ("new (derived)", THETA_NEW)):
    w = mp.mpf("0.8") * mp.e ** (2j * th)
    worst = mp.mpf(0)
    for m in MS:
        rel = abs(g_L(m, w)) / max(abs(F(m, w)), mp.mpf(1))
        worst = max(worst, rel)
    res[label] = worst
    print(f"  {label:<22} |w|={mp.nstr(abs(w),20)}  "
          f"max rel residual = {mp.nstr(worst, 8)}  "
          f"< 1e-8: {worst < A2_TOL}", flush=True)

o, n = res["old (typed, stale)"], res["new (derived)"]
print("\n" + "=" * 72)
print(f"  A2 verdict unchanged by the substitution: "
      f"{(o < A2_TOL) == (n < A2_TOL)}")
print(f"  old = {mp.nstr(o, 8)}   new = {mp.nstr(n, 8)}"
      f"   ratio = {mp.nstr(n/o, 8) if o > 0 else 'n/a'}")
print(f"  total wall {time.time()-T0:.0f}s")
print("=" * 72)
