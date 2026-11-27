#!/usr/bin/env python3
"""gg_deuteron_bond_probe.py — the deuteron with a gamma-gamma-selected p-n bond.

Bean `qou-xj4p`. Recipe: `preregistration.md` here (committed a06ae62c2b2 before this file).
Reuses the `../h2_one_rule/h2_one_rule_probe.py` helpers (mpmath 40 dps, convention D, proton pin,
seminormal basis, two-row partitions; y_lambda = 0 off two rows under convention D). Six strands:
free word x = V^m (gens 0,1) . V^m (gens 3,4); bond K = V(s)^k, s in {1, 2}, k in {1, 2, 3}.
Reading 3 at every level selects; the trace ratio and B = -E0 ln r are reported, never used to
select (ruling B, 2026-11-15). Nothing fitted, selected against AME, or wired.

-- Ref: [leitner2026] prop:ilp-covalent-bond; bean qou-ales; bean qou-xj4p
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_one_rule"))
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_one_rule_probe as base  # noqa: E402
import h2_gg_atom_probe as gga  # noqa: E402

kct, cf = base.kct, base.cf
ONE, ZERO, TOL, y, log = base.ONE, base.ZERO, base.TOL, base.y, base.log
Q, H, ZD = cf.Q, cf.H, cf.Z_D
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402

N = 6


def vpow(s, k):
    return base.V(s) * k


def shift(word, by):
    return [(c, d, g + by) for (c, d, g) in word]


def trace_and_chars(word):
    d = base.diag_of(word, N)
    lc = gga.level_chars(d, N, 1)
    tr = mp.fsum(y(l) * lc[(N, l)] for l in base.two_row(N))
    fails = sorted({m for (m, mu), v in lc.items() if v < -TOL})
    neg = [f"{m}:{mu}={mp.nstr(v, 10)}" for (m, mu), v in sorted(lc.items()) if v < -TOL]
    return tr, fails, neg, lc


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    E0 = m_e / (Q * (Q - 1))
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")

    # K1: bare nucleon V^m on 3 strands, reading 3 at levels 1..3
    k1 = {}
    for m in (3, 6):
        lc = gga.level_chars(base.diag_of(vpow(0, m), 3), 3, 1)
        k1[m] = not any(v < -TOL for v in lc.values())
    check("K1_nucleon_V3_V6_pass_reading3", k1[3] and k1[6], "h2-gg-atom.witness.json H3 rows")

    rows, results = [], {}
    for m in (3, 6):
        x = vpow(0, m) + shift(vpow(0, m), 3)
        trx, fx, negx, _ = trace_and_chars(x)
        # K2: production-style interface letter sigma_2 + d*1 gives ratio z_D + d (Markov)
        d_pn = -H * (mp.mpf(1) / 2)  # any d works for the identity; the averaged letter's leading term
        trk2, _, _, _ = trace_and_chars(x + [(ONE, d_pn, 2)])
        k2 = abs(trk2 / trx - (ZD + d_pn))
        check(f"K2_interface_ratio_eq_zD_plus_d_m{m}", k2 < mp.mpf("1e-30"), f"|ratio-(z_D+d)| = {mp.nstr(k2, 5)}")
        log(f"m={m}: bare x tr={mp.nstr(trx, 15)} reading3_every_level={not fx} fails={fx} {negx[:4]}")
        rset = []
        for s in (1, 2):
            for k in (1, 2, 3):
                tr, f, neg, lc = trace_and_chars(x + vpow(s, k))
                r = tr / trx
                B = -E0 * mp.log(r) if r > 0 else None
                row = {"m": m, "bond": f"V({s})^{k}", "site": s, "k": k,
                       "reading3_every_level": not f, "failing_levels": f, "negative": neg,
                       "ratio": mp.nstr(r, 25),
                       "B_MeV": None if B is None else mp.nstr(B, 20),
                       "B_err_vs_AME_pct": None if B is None else mp.nstr((B / B_AME - 1) * 100, 15)}
                rset.append(row)
                log(f"  m={m} K=V({s})^{k}: every-level={not f} fails={f} ratio={mp.nstr(r, 12)} "
                    f"B={row['B_MeV'] and row['B_MeV'][:10]} MeV {neg[:3]}")
        results[f"V^{m}"] = {"bare_tr": mp.nstr(trx, 30), "bare_reading3_every_level": not fx,
                             "bare_failing_levels": fx, "bare_negative": negx, "rows": rset}
        rows += rset

    passing = [r for r in rows if r["reading3_every_level"]]
    bare_ok = all(results[k]["bare_reading3_every_level"] for k in results)
    outcome = ("(i) gamma-gamma bond(s) pass" if (passing and bare_ok) else
               "(ii) no gamma-gamma bond passes in this cell")
    log(f"OUTCOME: {outcome}; passing bonds: {[(r['m'], r['bond']) for r in passing]}")

    wb = (WitnessBuilder("gg-deuteron-bond", engine="mpmath")
          .set_description(
              "PROBE (bean qou-xj4p; owner rulings 2026-11-15 A/B, 2026-11-25): deuteron with a "
              "gamma-gamma-selected p-n bond. 6 strands, nucleons V^m (m in {3,6}), bond V(s)^k "
              "(s in {1,2}, k in {1,2,3}); reading 3 at every level, convention D, proton pin. "
              "Pre-registered (a06ae62c2b2). Trace ratio and B = -E0 ln r reported, never used to "
              "select. p and n are the same word in this cell. Nothing fitted or wired.")
          .set_audit_only("computations/probes/gg_deuteron_bond/results.md")
          .add_parameter("q0", mp.nstr(Q, 40))
          .add_parameter("E0_MeV", mp.nstr(E0, 20))
          .add_data("results", results)
          .add_data("outcome", {"outcome": outcome,
                                "passing": [{"m": r["m"], "bond": r["bond"], "B_MeV": r["B_MeV"],
                                             "B_err_vs_AME_pct": r["B_err_vs_AME_pct"]} for r in passing]}))
    for name, ok, src in checks:
        wb.add_assertion(name, computed=ok, expected=True, source=src)
    wb.save()
    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
