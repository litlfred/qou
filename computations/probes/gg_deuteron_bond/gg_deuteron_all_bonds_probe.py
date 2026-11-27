#!/usr/bin/env python3
"""gg_deuteron_all_bonds_probe.py — Phase A of preregistration.md Addendum 1 (owner: "need all strands").

Every gamma-gamma bond word on all six strands (concatenations of vertices V(0)..V(3), length 1..L; the prereg said V(4),
which does not exist on six strands,
containing V(1) or V(2)) on the free word x = V^m (x) V^m, m in {3, 6}. Reading 3 at every level
selects; the trace ratio and B = -E0 ln r are reported, never used to select (ruling B). Progress
lines every ~5 % with elapsed time and ETA. Nothing fitted or wired.

-- Ref: [leitner2026] bean qou-ales; bean qou-xj4p
"""
from __future__ import annotations

import itertools
import sys
import time

import mpmath as mp
import gg_deuteron_bond_probe as g

base, y, TOL, Q = g.base, g.y, g.TOL, g.Q
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
N = 6


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    E0 = m_e / (Q * (Q - 1))
    words = [w for n in range(1, L + 1) for w in itertools.product(range(4), repeat=n)
             if (1 in w or 2 in w)]
    total = 2 * len(words)
    print(f"Phase A: L={L}, {len(words)} bond words x 2 nucleon words = {total} rows", flush=True)
    t0 = time.time()
    done, step = 0, max(1, total // 20)
    results = {}
    for m in (3, 6):
        x = g.vpow(0, m) + g.shift(g.vpow(0, m), 3)
        trx, fx, _, _ = g.trace_and_chars(x)
        passing, n_fail = [], 0
        for w in words:
            K = [lt for s in w for lt in base.V(s)]
            tr, f, neg, _ = g.trace_and_chars(x + K)
            done += 1
            if done % step == 0:
                el = time.time() - t0
                print(f"  {done}/{total} ({100*done//total}%) elapsed {el:.0f}s ETA {el/done*(total-done):.0f}s",
                      flush=True)
            if f:
                n_fail += 1
                continue
            r = tr / trx
            passing.append({"word": "".join(f"V{s}" for s in w), "length": len(w),
                            "ratio": mp.nstr(r, 25),
                            "B_MeV": mp.nstr(-E0 * mp.log(r), 20) if r > 0 else None,
                            "B_err_vs_AME_pct": mp.nstr((-E0 * mp.log(r) / B_AME - 1) * 100, 12) if r > 0 else None})
        Bs = [mp.mpf(p["B_MeV"]) for p in passing if p["B_MeV"] is not None]
        summary = {"bare_reading3_every_level": not fx, "n_words": len(words), "n_pass": len(passing),
                   "n_fail": n_fail,
                   "B_min_MeV": mp.nstr(min(Bs), 15) if Bs else None,
                   "B_max_MeV": mp.nstr(max(Bs), 15) if Bs else None}
        print(f"m={m}: {summary}", flush=True)
        results[f"V^{m}"] = {"summary": summary, "passing": passing}
    wb = (WitnessBuilder("gg-deuteron-all-bonds", engine="mpmath")
          .set_description(
              "PROBE Phase A (prereg addendum 1, commit 2024623969e; owner 'need all strands'): every "
              f"gamma-gamma bond word of 1..{L} vertices on the six-strand deuteron with gamma-gamma nucleons "
              "V^m, m in {3,6}; reading 3 at every level, convention D, proton pin. Ratio and B reported, "
              "never used to select. Nothing fitted or wired.")
          .set_audit_only("computations/probes/gg_deuteron_bond/results.md")
          .add_parameter("L", L).add_parameter("E0_MeV", mp.nstr(E0, 20))
          .add_data("results", results))
    wb.add_assertion("every_row_evaluated", computed=done, expected=total, tolerance=0,
                     source="all enumerated rows were evaluated")
    wb.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
