"""binding_link_psd_feasibility_probe.py — Topic 3 of PR #1712.

Tests whether the **binding link** K (rather than the whole-atom knot)
is the SDP-canonical object for the deuteron, per the structural
decomposition in `conj-canonical-knot-id-sdp.md §"Structural
decomposition"`:

    T_w(atom) = K(binding) ⊗ ⊗_i T_w(nucleon_i)

For ²H: binding = L_H (Hopf link). For ³H/³He: binding = 8_11-class
link / L6a4 (3-component).

PR #1698 SDP run showed historical D=6_2 is NOT PSD-feasible at H_3
(standard-(2,1) eigenvalue −0.89). If K = L_H is PSD-feasible at H_3
in its OWN right, that structurally discharges the historical-6_2
puzzle: 6_2 is the AME-volume-matched proxy for the WHOLE-ATOM knot,
but the SDP-canonical object is the BINDING link, and that does pass.

## Braid words

| object | strands | braid word | source |
|---|---|---|---|
| ²H whole-atom (6_2)   | B_3 | `[1, -2, 1, 1, 1, -2]`  | atlas |
| **²H binding (L_H = Hopf)** | B_2 (padded to B_3) | `[1, 1]` (σ_1²) | Rolfsen / atlas §"L_H" |
| ³He whole-atom (L6a4) | B_3 | `[-1, 2, -1, 2, -1, 2]` | atlas |

We test each at H_3 via the joint_tower_sdp_solver_v2 H_3 cvxpy SDP-
feasibility entry.

## Expected outcome (and what would refute it)

Hypothesis: **Hopf-link L_H IS PSD-feasible at H_3.** If true,
this is a structural finding (Topic 3 closure for ²H modulo
uniqueness arg). If false, the binding-link path is refuted just
like the whole-atom path; back to drawing board.

Ref: docs/coordination/2026-06-02-m-p-linking-weight-and-binding-link-scope.md
Ref: content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md
Ref: docs/audits/2026-06-02-subgoal-1-sdp-canonical-knot-run.md
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import numpy as np  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q as Q_CANONICAL  # noqa: E402

# Reuse the H_3 Hoefsmit standard representation + trivial/sign reps
from joint_tower_sdp_solver_v2 import (  # noqa: E402
    sdp_feasibility_h3,
)

set_compute_dps()

# Per the recursive-atom-knot-atlas + conj-canonical-knot-id-sdp:
TESTS = [
    # (name, braid_word, classification)
    ("²H whole-atom 6_2",
     [1, -2, 1, 1, 1, -2],
     "historical AME-volume-match — PR #1698 verified NOT PSD"),
    ("²H binding L_H (Hopf, σ_1²)",
     [1, 1],
     "structural-decomposition canonical binding link"),
    ("²H binding L_H — σ_2² variant",
     [2, 2],
     "structural variant: σ_2² instead of σ_1²"),
    ("³He whole-atom L6a4",
     [-1, 2, -1, 2, -1, 2],
     "PR #1698 confirmed PSD-feasible — control"),
    # Sanity: unknot
    ("control: trivial (unknot)",
     [],
     "unknot = no crossings"),
]


def all_psd(per_block: dict) -> bool:
    """Are all three Wedderburn blocks PSD at q_0?

    sdp_feasibility_h3 returns:
      - trivial_(3) / sign_(1,1,1): 1×1 blocks, key `psd` (bool)
      - standard_(2,1): 2×2 block, key `psd_symmetric_part` (bool)
      - top-level `all_blocks_psd_or_close` (bool) — authoritative summary
    """
    if "all_blocks_psd_or_close" in per_block:
        return bool(per_block["all_blocks_psd_or_close"])
    for blk_name, blk in per_block.items():
        if not isinstance(blk, dict):
            continue
        # 1D blocks use "psd"
        if "psd" in blk and not blk["psd"]:
            return False
        # 2D blocks use "psd_symmetric_part"
        if "psd_symmetric_part" in blk and not blk["psd_symmetric_part"]:
            return False
    return True


def main() -> int:
    q_val = float(Q_CANONICAL)
    print(f"Binding-link PSD-feasibility probe @ q_0 = {Q_CANONICAL}")
    print()
    print(f"  {'object':<40s} {'PSD?':<6s}  blocks_summary")
    print("  " + "-" * 90)

    results = []
    for name, word, classification in TESTS:
        try:
            per_block = sdp_feasibility_h3(word, q_val)
            psd_all = all_psd(per_block)
            # Summarize each block (handles both 1D `psd` and 2D `psd_symmetric_part`)
            blk_summary = []
            for blk_name, blk_data in per_block.items():
                if blk_name == "all_blocks_psd_or_close":
                    continue
                if isinstance(blk_data, dict):
                    if "psd" in blk_data:
                        ok = blk_data["psd"]
                        val = blk_data.get("value", 0)
                        blk_summary.append(f"{blk_name}={val:+.3f}{'✓' if ok else '✗'}")
                    elif "psd_symmetric_part" in blk_data:
                        ok = blk_data["psd_symmetric_part"]
                        eig_min = blk_data.get("min_eigenvalue", 0)
                        blk_summary.append(f"{blk_name}_min_eig={eig_min:+.3f}{'✓' if ok else '✗'}")
            sum_str = " ".join(blk_summary)
            mark = "✓" if psd_all else "✗"
            print(f"  {name:<40s} {mark:<6s}  {sum_str}")
            results.append({
                "name": name,
                "braid_word": list(word),
                "classification": classification,
                "all_psd": psd_all,
                "per_block": {
                    # Per Gemini #1712 review: top-level non-dict entries
                    # (e.g. all_blocks_psd_or_close, a bool) used to be
                    # silently coerced to {}; and inner bools were cast to
                    # 1.0/0.0 because isinstance(True, int) is True in Python.
                    # Fix: pass non-dicts through verbatim, and exclude bool
                    # from float-coercion.
                    k: ({
                        kk: float(vv)
                        if isinstance(vv, (int, float)) and not isinstance(vv, bool)
                        else vv
                        for kk, vv in v.items()
                    } if isinstance(v, dict) else v)
                    for k, v in per_block.items()
                },
            })
        except Exception as e:
            print(f"  {name:<40s} ERR    {type(e).__name__}: {str(e)[:50]}")
            results.append({
                "name": name,
                "braid_word": list(word),
                "error": f"{type(e).__name__}: {e}",
            })

    print()
    # Headline verdict
    hopf_result = next((r for r in results if "Hopf" in r["name"] and "σ_1²" in r["name"]), None)
    six_two = next((r for r in results if "6_2" in r["name"]), None)
    if hopf_result and "all_psd" in hopf_result:
        if hopf_result["all_psd"]:
            print(f"  VERDICT: ²H Hopf-link IS PSD-feasible at H_3 ✓")
            print(f"           Structural-decomposition hypothesis SUPPORTED")
            print(f"           (vs 6_2 whole-atom: 6_2 was {'PSD' if six_two and six_two.get('all_psd') else 'NOT PSD'})")
        else:
            print(f"  VERDICT: ²H Hopf-link is NOT PSD-feasible at H_3 ✗")
            print(f"           Structural-decomposition hypothesis REFUTED for ²H")
            print(f"           — binding-link is no better than whole-atom 6_2")

    w_out = WitnessBuilder("binding-link-psd-feasibility-probe", engine="python")
    w_out.set_description(
        "Topic 3 of PR #1712: tests whether the BINDING LINK K (not the "
        "whole-atom knot) is the SDP-canonical object for the deuteron, "
        "per conj-canonical-knot-id-sdp.md structural decomposition. "
        "Tests K = L_H (Hopf) for ²H at H_3, with controls (²H 6_2 = "
        "atlas whole-atom, ³He L6a4 = PR #1698 PSD ✓, unknot = trivial)."
    )
    for r in results:
        w_out.add_data(f"result_{r['name'].replace(' ', '_')}",
                       str(r.get("all_psd", r.get("error", "?"))))
    w_out.add_assertion(
        name="hopf_link_psd_at_h3",
        computed=bool(hopf_result and hopf_result.get("all_psd")),
        expected=True,
        tolerance=0,
        source="Structural-decomposition hypothesis (Topic 3)",
    )
    out = w_out.save()
    print(f"\n  Witness: {out.name}")
    return 0 if (hopf_result and hopf_result.get("all_psd")) else 1


if __name__ == "__main__":
    sys.exit(main())
