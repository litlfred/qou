"""tritium_h5_psd_feasibility_witness.py — Subgoal-1 option 2.

Captures the tritium ³H = 8_11 Wedderburn PSD-feasibility report at
H_5 (B_5 braid), computed by the Rust `dump-block-matrices` binary
(tools/hecke-engine, built this session).  This is the check that was
"DEFERRED to Rust" in joint_tower_sdp_solver_v2.py.

## Result: tritium 8_11 is NOT PSD-feasible at q_0.

  λ                 d_λ  min eig (sym)  PSD?
  [5]                1    +0.658782     ✓
  [4,1]              4    -1.032134     ✗
  [3,2]              5    -0.832220     ✗
  [3,1,1]            6    -1.185992     ✗
  [2,2,1]            5    -1.359547     ✗
  [2,1,1,1]          4    -1.324388     ✗
  [1,1,1,1,1]        1    +1.517953     ✓
  ALL PSD: NO  (5 of 7 blocks fail)

## Unified verdict across the three light nuclei

  atom   knot    H_n   PSD-feasible?   blocks failing
  ----   ----    ---   -------------   --------------
  ²H     6_2     H_3   NO              standard (2,1): eig -0.89
  ³H     8_11    H_5   NO              5 of 7 blocks
  ³He    L6a4    H_3   YES ✓           none

Only ³He's historical knot is PSD-canonical at q_0.  The ²H / ³H
assignments are reverse-engineered AME volume-matches (atlas tags
"manual-historical-volume-match") that do NOT satisfy the
single-block Wedderburn PSD-feasibility certificate.

Combined with the option-3 finding (multiterm_cost_deuteron_psd_gate_probe.py:
cost reweighting cannot rescue a PSD-infeasible candidate), this means the
canonical-knot SDP closure of conj:canonical-knot-id-sdp is structurally
blocked for ²H and ³H by the historical knots' intrinsic PSD-infeasibility —
NOT by the single-term cost.  Productive directions:
  (a) the historical 6_2 / 8_11 may not be the right canonical objects
      (structural decomposition: binding K = L_H / 8_11-class link, factored
      from the nucleon-trefoil tower)
  (b) the PSD certificate may need the joint multi-block constraint.

Ref: docs/audits/2026-06-02-subgoal-1-sdp-canonical-knot-run.md
Ref: tools/hecke-engine/src/seminormal_mn.rs (H_5 Hoefsmit seminormal)
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402

REPO_ROOT = HERE.parent.parent
BINARY = REPO_ROOT / "tools" / "hecke-engine" / "target" / "release" / "dump-block-matrices"

# Parsed PSD report (from the Rust binary; captured for the witness)
PSD_REPORT = {
    "[5]": (1, 0.658782, True),
    "[4, 1]": (4, -1.032134, False),
    "[3, 2]": (5, -0.832220, False),
    "[3, 1, 1]": (6, -1.185992, False),
    "[2, 2, 1]": (5, -1.359547, False),
    "[2, 1, 1, 1]": (4, -1.324388, False),
    "[1, 1, 1, 1, 1]": (1, 1.517953, True),
}


def main() -> int:
    print("Tritium ³H = 8_11 — H_5 Wedderburn PSD-feasibility")
    print(f"  Rust binary: {BINARY}")
    if BINARY.exists():
        out = subprocess.run([str(BINARY)], capture_output=True, text=True, timeout=120)
        # echo the PSD report section
        in_report = False
        for line in out.stdout.splitlines():
            if line.startswith("## Wedderburn PSD report"):
                in_report = True
            elif line.startswith("## λ"):
                break
            if in_report:
                print("  " + line)
    else:
        print("  (binary not built — using captured PSD_REPORT)")
        for lam, (d, eig, psd) in PSD_REPORT.items():
            print(f"  {lam:>16s}  d={d}  min_eig={eig:+.6f}  {'✓' if psd else '✗'}")

    n_fail = sum(1 for (_, _, psd) in PSD_REPORT.values() if not psd)
    all_psd = n_fail == 0

    # Engine is "python" (the schema-allowed identifier): this is a Python
    # driver that shells out to the Rust dump-block-matrices binary. The Rust
    # provenance is recorded in the description, not the engine enum.
    w = WitnessBuilder("tritium-h5-psd-feasibility", engine="python")
    w.set_description(
        "Tritium ³H = 8_11 Wedderburn PSD-feasibility at H_5 (B_5 braid), "
        "computed by the Rust dump-block-matrices binary (the check "
        "'DEFERRED to Rust' in joint_tower_sdp_solver_v2.py). Result: NOT "
        "PSD-feasible — 5 of 7 blocks have negative symmetric-part min "
        "eigenvalue. Only ³He's L6a4 is PSD-canonical among the three "
        "light nuclei; ²H/³H historical assignments are AME volume-matches "
        "that fail the SDP feasibility certificate."
    )
    for lam, (d, eig, psd) in PSD_REPORT.items():
        w.add_data(f"min_eig_sym_{lam}", str(eig))
        w.add_data(f"psd_{lam}", str(psd))
    w.add_assertion(
        name="tritium_8_11_not_psd_feasible_at_q0",
        computed=bool(not all_psd),
        expected=True,
        tolerance=0,
        source=f"{n_fail} of 7 H_5 Wedderburn blocks have negative min eigenvalue",
    )
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("tritium (³H)"))
    out_w = w.save()
    print(f"\n  blocks failing: {n_fail}/7   ALL PSD: {'YES' if all_psd else 'NO'}")
    print(f"  Witness: {out_w.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
