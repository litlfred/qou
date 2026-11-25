#!/usr/bin/env python3
"""gg_deuteron_flavoured_probe.py — Phase B of preregistration.md Addendum 1 (owner: "need all strands").

Nucleons are gamma-gamma words on their own FOUR strands (vertices V(0), V(1), length 1..L; the
prereg also listed V(2), which needs generator 3 and does not exist on four strands)
that pass reading 3 at every level on four strands, so proton and neutron may differ. The deuteron
is on eight strands, every strand kept in the trace: x = w1 (gens 0-2) . w2 (gens 4-6), bond
K = V(3)^k (enters the newer nucleon, 2026-11-22 ruling) or V(2)^k, k in {1,2,3}. Every ordered
pair (w1, w2) is evaluated; which is the proton is not determined by the corpus, so no pair is
chosen. Ratio and B = -E0 ln r reported, never used to select (ruling B). Nothing fitted or wired.

-- Ref: [leitner2026] bean qou-ales; bean qou-xj4p
"""
from __future__ import annotations

import itertools
import sys
import time

import mpmath as mp
import gg_deuteron_bond_probe as g

base, gga, y, TOL, Q = g.base, g.gga, g.y, g.TOL, g.Q
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402

L = int(sys.argv[1]) if len(sys.argv) > 1 else 6


def tc(word, n):
    d = base.diag_of(word, n)
    lc = gga.level_chars(d, n, 1)
    tr = mp.fsum(y(l) * lc[(n, l)] for l in base.two_row(n))
    fails = sorted({m for (m, mu), v in lc.items() if v < -TOL})
    return tr, fails


def word_of(w):
    return [lt for s in w for lt in base.V(s)]


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    E0 = m_e / (Q * (Q - 1))
    t0 = time.time()
    cands = [w for n in range(1, L + 1) for w in itertools.product(range(2), repeat=n)]
    nucleons = []
    for w in cands:
        tr, f = tc(word_of(w), 4)
        if not f:
            nucleons.append(w)
    print(f"Phase B: L={L}: {len(nucleons)} of {len(cands)} four-strand gamma-gamma words pass reading 3 "
          f"({time.time()-t0:.0f}s)", flush=True)
    bonds = [(s, k) for s in (3, 2) for k in (1, 2, 3)]
    total = len(nucleons) ** 2 * (1 + len(bonds))
    done, step = 0, max(1, total // 20)
    rows, Bs = [], []
    for w1, w2 in itertools.product(nucleons, repeat=2):
        x = word_of(w1) + g.shift(word_of(w2), 4)
        trx, fx = tc(x, 8)
        done += 1
        for s, k in bonds:
            tr, f = tc(x + g.vpow(s, k), 8)
            done += 1
            if done % step < 1 + len(bonds) and done >= step:
                el = time.time() - t0
                print(f"  {done}/{total} elapsed {el:.0f}s ETA {el/done*(total-done):.0f}s", flush=True)
            if f or fx:
                continue
            r = tr / trx
            B = -E0 * mp.log(r) if r > 0 else None
            rows.append({"w1": "".join(f"V{a}" for a in w1), "w2": "".join(f"V{a}" for a in w2),
                         "bond": f"V({s})^{k}", "ratio": mp.nstr(r, 20),
                         "B_MeV": None if B is None else mp.nstr(B, 15),
                         "B_err_vs_AME_pct": None if B is None else mp.nstr((B / B_AME - 1) * 100, 10)})
            if B is not None:
                Bs.append(B)
    summary = {"n_nucleon_words": len(nucleons), "n_pairs": len(nucleons) ** 2,
               "n_passing_atoms": len(rows),
               "B_min_MeV": mp.nstr(min(Bs), 12) if Bs else None,
               "B_max_MeV": mp.nstr(max(Bs), 12) if Bs else None,
               "n_bound": sum(1 for b in Bs if b > 0), "n_unbound": sum(1 for b in Bs if b <= 0)}
    print("SUMMARY", summary, flush=True)
    wb = (WitnessBuilder("gg-deuteron-flavoured", engine="mpmath")
          .set_description(
              "PROBE Phase B (prereg addendum 1, commit 2024623969e; owner 'need all strands'): four-strand "
              f"gamma-gamma nucleon words (1..{L} vertices) passing reading 3, every ordered pair on eight "
              "strands with bonds V(3)^k, V(2)^k; reading 3 at every level, convention D, proton pin. "
              "No pair chosen as 'the deuteron'. Ratio and B reported, never used to select.")
          .set_audit_only("computations/probes/gg_deuteron_bond/results.md")
          .add_parameter("L", L).add_parameter("E0_MeV", mp.nstr(E0, 20))
          .add_data("nucleon_words", ["".join(f"V{a}" for a in w) for w in nucleons])
          .add_data("summary", summary).add_data("passing_atoms", rows))
    wb.add_assertion("every_row_evaluated", computed=done, expected=total, tolerance=0,
                     source="all enumerated rows were evaluated")
    wb.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
