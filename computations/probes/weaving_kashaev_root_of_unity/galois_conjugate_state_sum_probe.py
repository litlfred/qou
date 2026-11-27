#!/usr/bin/env python3
"""Kashaev value <K>_N at every Galois conjugate, by the R-matrix state sum (bean qou-pc7n).

Extends galois_total_positivity_probe.py past N = 14. That probe evaluates the
Habiro expansion and needs c_k for k < N; c_k for 8_18 costs ~2.5x more per step
(c_15 took ~2000 s, so k = 19 is a multi-day run). This probe instead evaluates the
state sum of weaving_kashaev_probe.py (W(3,m) = closure of V0^m: m = 2 is 4_1,
m = 4 is 8_18, m = 5 is 10_123) at q = e^{2 pi i a/N}, gcd(a, N) = 1, by replacing
the fourth root w = e^{i pi/(2N)} with w_a = e^{i pi a/(2N)}. The state model is a
Laurent polynomial in w, so this is the Galois image of the a = 1 value.

Branch: w_a^4 = q, but q^{1/4} is fixed only up to i^k. The value is a framed-knot
invariant; any branch phase would show up as a nonzero imaginary part, which is
reported. Controls:
  (1) 4_1 is checked against the Habiro sum prod (2 - q^j - q^-j) at every conjugate
      (proved positive in QOU/Core/KashaevReflection.lean);
  (2) for N <= 14, every conjugate is checked against galois-total-positivity.result.json
      (independent route: exact Habiro c_k).

Arithmetic: mpmath at mp.dps = 60, no float. a and N - a give complex-conjugate
values, so a <= N/2 suffices.

Run: python3 -u computations/probes/weaving_kashaev_root_of_unity/galois_conjugate_state_sum_probe.py Nmin Nmax
Writes galois-state-sum-N<Nmin>-<Nmax>.result.json after every N (resumable by range).
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import mpmath as mp

import weaving_kashaev_probe as W

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


class RingA(W.Ring):
    """Evaluation at w = e^{2 pi i a/(4N)}, q = w^4 = e^{2 pi i a/N}."""

    def __init__(self, N: int, a: int):
        super().__init__(N)
        self.w = mp.expjpi(mp.mpf(a) / (2 * N))


def habiro41(N: int, a: int):
    th = 2 * mp.pi * a / N
    s, p = mp.mpf(0), mp.mpf(1)
    for k in range(N):
        if k > 0:
            p *= 2 - 2 * mp.cos(k * th)
        s += p
    return s


def main() -> int:
    Nmin, Nmax = int(sys.argv[1]), int(sys.argv[2])
    ref = {}
    refp = HERE / "galois-total-positivity.result.json"
    if refp.exists():
        for name, rec in json.loads(refp.read_text())["knots"].items():
            for row in rec["rows"]:
                for c in row["conjugates"]:
                    ref[(name, row["N"], c["a"])] = mp.mpf(c["re"])
    outp = HERE / f"galois-state-sum-N{Nmin}-{Nmax}.result.json"
    out = {"description": "Kashaev value at every Galois conjugate via the R-matrix state "
                          "sum; bean qou-pc7n", "dps": mp.mp.dps, "rows": []}
    t0 = time.time()
    for N in range(Nmin, Nmax + 1):
        for a in range(1, N // 2 + 1):
            if math.gcd(a, N) != 1:
                continue
            R = RingA(N, a)
            F = W.f_table(R)
            rec = {"N": N, "a": a}
            for m in (2, 4, 5):
                v = W.kashaev(R, F, m)
                name = W.NAME[m]
                e = {"re": mp.nstr(v.real, 25), "im_abs": mp.nstr(abs(v.imag), 3),
                     "negative": bool(v.real < 0)}
                if m == 2:
                    h = habiro41(N, a)
                    e["habiro_absdiff"] = mp.nstr(abs(v - h), 3)
                if (name, N, a) in ref:
                    r = ref[(name, N, a)]
                    e["habiro_ck_reldiff"] = mp.nstr(abs(v.real - r) / max(1, abs(r)), 3)
                rec[name] = e
            out["rows"].append(rec)
            print(f"N={N:2d} a={a:2d} " + "  ".join(
                f"{k}:{mp.nstr(mp.mpf(rec[k]['re']), 10)}(im {rec[k]['im_abs']})"
                + (" NEG" if rec[k]["negative"] else "") for k in ("4_1", "8_18", "10_123"))
                + f"  4_1-habiro {rec['4_1']['habiro_absdiff']}"
                + "".join(f"  {k}-ck {rec[k]['habiro_ck_reldiff']}" for k in ("4_1", "8_18", "10_123")
                          if "habiro_ck_reldiff" in rec[k])
                + f"  [{time.time()-t0:.0f}s]", flush=True)
        outp.write_text(json.dumps(out, indent=1))
    negs = [(r["N"], r["a"], k) for r in out["rows"] for k in ("4_1", "8_18", "10_123")
            if r[k]["negative"]]
    out["negative"] = negs
    outp.write_text(json.dumps(out, indent=1))
    print("negative conjugates:", negs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
