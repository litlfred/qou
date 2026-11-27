#!/usr/bin/env python3
"""Which alpha-decay half-life misses can a preformation factor close at all?

Bean `qou-q0gw` (parent epic `qou-myts`), open-shell preformation item.

With preformation probability S the Gamow half-life is T = T_WKB / S. Because
0 < S <= 1, T >= T_WKB (Lean:
`QOU.Nuclear.AlphaPreformationBound.le_div_preformation`). So:

* if T_WKB <= T_exp, the closing value S_req = T_WKB / T_exp is admissible
  (`required_preformation_admissible`); preformation can close the miss;
* if T_WKB > T_exp, no admissible S reaches T_exp
  (`preformation_cannot_close_of_lt`); the miss lies on the barrier side
  (Q, radius, deformation), not in preformation.

The probe partitions the bare-WKB emitters of the qou-i2jl witness (S_alpha = 1,
Q at AME) by that sign. It also reads the 210Po Mayer-Jensen counting rule
(proton 1/g(1h9/2), neutron g(3p1/2)/g(2g9/2)) literally for the two open-shell
Po isotopes, where the valence neutrons sit in 2g9/2 and the rule gives
1/g(2g9/2) per species. That is a scope-(a) test of the rule as written, not a
fit: no parameter is adjusted. T_exp is the comparison target only.

Precision: mpmath workdps 80, JSON read with parse_float=str, no float64.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 30
set_compute_dps(WORK_DPS)

QI2JL_WITNESS = (_ROOT / "computations" / "probes" / "alpha_decay_n126_and_derived_qalpha"
                 / "alpha_decay_n126_qalpha_probe.witness.json")

# Shell-model degeneracies 2j+1 (exact integers, no measurement).
G_1H9_2 = 10
G_2G9_2 = 10


def main() -> int:
    with mp.workdps(WORK_DPS):
        with QI2JL_WITNESS.open() as f:
            w = json.load(f, parse_float=str)["data"]
        emitters = w["part_a_baseline_gamow_emitters"]["emitters"]
        rows = []
        for e in emitters:
            t_wkb = mp.mpf(e["T_half_WKB_s"])
            t_exp = mp.mpf(e["T_half_exp_s"])
            s_req = t_wkb / t_exp
            closable = s_req <= 1
            rows.append({
                "nuclide": e["nuclide"], "Z": e["Z"], "N": e["N"],
                "regime": e["regime"],
                "dex_bare_WKB": fmt(mp.log10(s_req), dps=12),
                "S_required": fmt(s_req, dps=12),
                "preformation_can_close": bool(closable),
            })
        closable = [r for r in rows if r["preformation_can_close"]]
        blocked = [r for r in rows if not r["preformation_can_close"]]

        # 210Po Mayer-Jensen rule read literally for the N=128,130 Po isotopes.
        s_lit = mp.mpf(1) / G_1H9_2 * mp.mpf(1) / G_2G9_2
        lit = {}
        for nuc in ("212Po", "214Po"):
            r = next(x for x in rows if x["nuclide"] == nuc)
            dex_bare = mp.mpf(r["dex_bare_WKB"])
            dex_lit = dex_bare - mp.log10(s_lit)
            lit[nuc] = {"S_literal_MJ": fmt(s_lit, dps=12),
                        "dex_bare_WKB": fmt(dex_bare, dps=12),
                        "dex_with_literal_MJ": fmt(dex_lit, dps=12),
                        "worse_than_bare": bool(abs(dex_lit) > abs(dex_bare))}

        for r in rows:
            print(f"{r['nuclide']:>6} dex {mp.nstr(mp.mpf(r['dex_bare_WKB']), 4):>8}  "
                  f"S_req {mp.nstr(mp.mpf(r['S_required']), 4):>8}  "
                  f"{'closable' if r['preformation_can_close'] else 'BLOCKED (S>1)'}")
        for k, v in lit.items():
            print(f"{k} literal MJ S={mp.nstr(s_lit, 3)}: dex {mp.nstr(mp.mpf(v['dex_with_literal_MJ']), 4)}")

        q0 = q_at()
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Partition of bare-WKB alpha emitters by whether an admissible preformation "
            "factor 0 < S <= 1 can close the half-life miss (Lean "
            "AlphaPreformationBound); literal reading of the 210Po Mayer-Jensen rule "
            "for 212Po and 214Po (scope-(a) test, no fitting).")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("source_witness", str(QI2JL_WITNESS.relative_to(_ROOT)))
        wb.add_data("emitters", rows)
        wb.add_data("partition", {
            "closable_by_preformation": [r["nuclide"] for r in closable],
            "blocked_barrier_side": [r["nuclide"] for r in blocked],
        })
        wb.add_data("literal_mayer_jensen_open_shell", lit)
        wb.add_assertion("n_emitters", len(rows), 7, 0, source="qou-i2jl witness part A")
        wb.add_assertion("n_blocked_barrier_side", len(blocked), 4, 0,
                         source="S_required > 1 (8Be, 222Rn, 226Ra, 238U)")
        wb.add_assertion("literal_MJ_worse_for_open_shell_Po",
                         int(all(v["worse_than_bare"] for v in lit.values())), 1, 0,
                         source="210Po rule read literally")
        wb.add_caveat(
            "T_exp is the comparison target only. S_required is a diagnostic, not a "
            "predicted value. The bound S <= 1 is the normalisation of a probability.")
        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
