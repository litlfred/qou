#!/usr/bin/env python3
"""H6 -> H3 residue of the six-strand reading-3 survivors (bean qou-cds1, route C step 2).

Reads the 58 survivors recorded by six_strand_neutral_selection_probe.py and, for
each, computes chi_mu(E_{6->m}(W)) exactly over Q(q) for m = 3..6 and two-row
mu |- m, using the convention-D conditional expectation of gg_ntower_probe
(level_chars). Records the level-3 residue, compares it with the H3 Borromean
core V^3 = (s0 s1^-1)^3, and reports whether every level-m character is
non-negative on q > 1.

No measured value enters. q0 is used only to print a sign check.
"""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gg_ntower"))
import gg_ntower_probe as g  # noqa: E402
import sympy as sp  # noqa: E402

SRC = HERE / "six-strand-neutral-selection.witness.json"
OUT = HERE / "six-strand-h3-residue.witness.json"


def main():
    t0 = time.time()
    src = json.loads(SRC.read_text())
    surv = [r for r in src["rows"] if r["reading3_q0"]]
    print(f"{len(surv)} survivors", flush=True)
    core = [(0, 1), (1, -1)] * 3
    core3 = g.level_chars(core, 3)
    core_str = {str(k[1]): str(v) for k, v in core3.items()}
    print("H3 core V^3:", core_str, flush=True)
    rows = []
    for i, r in enumerate(surv):
        letters = [tuple(x) for x in r["reduced"]]
        ch = g.level_chars(letters, 6)
        lvl = {}
        all_nonneg = True
        for (m, mu), f in ch.items():
            si = g.sign_info(f)
            all_nonneg &= bool(si["nonneg_on_(1,inf)"])
            lvl.setdefault(str(m), {})[str(mu)] = {"chi": str(f), "sign": si}
        res3 = {mu: ch[(3, tuple(map(int, mu.strip("()").split(","))))] for mu in core_str}
        ratio = {mu: str(sp.factor(sp.cancel(res3[mu] / core3[(3, tuple(map(int, mu.strip("()").split(","))))])))
                 if core3[(3, tuple(map(int, mu.strip("()").split(","))))] != 0 else None
                 for mu in core_str}
        rows.append({
            "V_indices": r["V_indices"], "crossings": r["crossings"], "reduced": r["reduced"],
            "level_chars": lvl, "all_levels_nonneg_on_q_gt_1": all_nonneg,
            "level3_over_core": ratio,
        })
        print(f"[{i+1}/{len(surv)}] {''.join(map(str, r['V_indices']))} "
              f"nonneg={all_nonneg} ratio3={ratio} ({time.time()-t0:.0f}s)", flush=True)
    w = {
        "computation": "six-strand-h3-residue",
        "scriptFile": "computations/probes/gg_six_strand/six_strand_h3_residue_probe.py",
        "kind": "probe",
        "beans": ["qou-cds1", "qou-4f8t"],
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 used only for a printed sign check; all characters are exact in Q(q)",
        "markov_convention": "D",
        "source_witness": "computations/probes/gg_six_strand/six-strand-neutral-selection.witness.json",
        "core_V3_level3_chars": core_str,
        "summary": {
            "survivors": len(rows),
            "all_levels_nonneg_count": sum(r["all_levels_nonneg_on_q_gt_1"] for r in rows),
        },
        "rows": rows,
    }
    OUT.write_text(json.dumps(w, indent=1, sort_keys=False) + "\n")
    print("wrote", OUT, f"{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
