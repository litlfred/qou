#!/usr/bin/env python3
"""Cross-check tr_M(β_atom) at 1ppb between two independent paths.

Compares the canonical Markov trace tr_M @ q_0 from:
  - Hoefsmit / mpfr 50-dps brute-force
    (`atomic-tr-m-mpfr-50dps.witness.json`)
  - Markov-axiom recursive ascent (`markov_peel.tr_M_atomic`)
    (`markov-peel-atomic-tr-m.witness.json` — production witness
    landed in PR #520 / #508)

Both witnesses store the trace at high precision; we parse via
mpmath and report the relative delta. Flags any atom that diverges
by more than 1 part per billion (1e-9).

Output: `cross-check-trM-1ppb.witness.json`

CI gate: invoke with `--strict` to exit non-zero on any divergence.

Usage:
    python3 folio-assistant/computations/cross_check_trM_1ppb.py
    python3 folio-assistant/computations/cross_check_trM_1ppb.py --strict
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpf, fabs, mpmathify

HERE = Path(__file__).parent
HOEF_PATH = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
PEEL_PATH = HERE / "markov-peel-atomic-tr-m.witness.json"
OUT_PATH = HERE / "cross-check-trM-1ppb.witness.json"

TOLERANCE = mpf("1e-9")  # 1 ppb relative

# Map from peel-witness (Z, N) tuples to atom-name strings used by
# the Hoefsmit witness for its `atom` field. Keep the atom names in
# the literal lookup table so the cross-check can be read by humans.
_ZN_TO_ATOM = {
    (1, 0): "proton",
    (0, 1): "neutron",
    (1, 1): "deuteron",
    (1, 2): "tritium",
    (2, 1): "helium-3",
    (2, 2): "helium-4",
    (3, 2): "lithium-5",
    (3, 3): "lithium-6",
    (3, 4): "lithium-7",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="Exit non-zero on any > 1ppb divergence")
    ap.add_argument("--dps", type=int, default=50,
                    help="mpmath working precision (default 50)")
    args = ap.parse_args()
    mp.dps = args.dps

    hoef = json.loads(HOEF_PATH.read_text())
    peel = json.loads(PEEL_PATH.read_text())

    # Hoefsmit results: list of dicts, atom name in 'atom'
    hoef_by_atom = {r["atom"]: r for r in hoef["results"]}
    # Markov-peel results: list of dicts keyed on (Z, N) — production
    # witness format from `markov_peel_atomic_witness.py`.
    peel_by_atom = {}
    for r in peel.get("data", {}).get("results", []):
        atom = _ZN_TO_ATOM.get((r["Z"], r["N"]))
        if atom is None:
            continue
        peel_by_atom[atom] = r

    common_atoms = sorted(
        set(hoef_by_atom) & set(peel_by_atom)
    )

    print("=" * 76)
    print("Cross-check tr_M @ q_0 — Hoefsmit (mpfr 50dps) vs markov_peel")
    print("=" * 76)
    print(f"  tolerance: {TOLERANCE} (1 ppb)  |  dps: {args.dps}")
    print()
    print(f"  {'atom':<14} {'Hoefsmit':>20}  {'markov_peel':>20}  "
          f"{'|Δ_rel|':>13}  status")
    print("  " + "─" * 74)

    deltas: list[dict] = []
    any_diverge = False

    for atom in common_atoms:
        h = hoef_by_atom[atom]
        p = peel_by_atom[atom]
        if h.get("tr_M_at_q0_50dps") is None:
            continue
        # Production witness key is `tr_M_at_q0` (not _str / _50dps).
        peel_str = p.get("tr_M_at_q0") or p.get("tr_M_at_q0_str")
        if peel_str is None:
            continue
        if "error" in p:
            continue

        h_val = mpmathify(h["tr_M_at_q0_50dps"])
        p_val = mpmathify(peel_str)
        if h_val == 0 and p_val == 0:
            rel = mpf(0)
        elif h_val == 0:
            rel = fabs(p_val)
        else:
            rel = fabs(p_val - h_val) / fabs(h_val)

        ok = rel < TOLERANCE
        if not ok:
            any_diverge = True
        status = "OK" if ok else "DIVERGE"
        print(f"  {atom:<14} {str(h_val)[:20]:>20}  "
              f"{str(p_val)[:20]:>20}  {mp.nstr(rel, 3):>13}  {status}")

        deltas.append({
            "atom": atom,
            "hoefsmit_50dps": str(h_val),
            "markov_peel": str(p_val),
            "abs_delta": str(fabs(p_val - h_val)),
            "rel_delta": str(rel),
            "within_1ppb": ok,
        })

    out = {
        "computation": "cross-check-trM-1ppb",
        "description": (
            "Pairwise comparison of tr_M(β_atom) @ q_0 between the "
            "Hoefsmit/mpfr 50-dps brute-force path and the Markov-"
            "axiom recursive ascent (markov_peel, production "
            "witness from PR #520). Tolerance is 1 ppb (1e-9 "
            "relative)."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "tolerance_relative": str(TOLERANCE),
        "working_precision_dps": args.dps,
        "atoms_compared": len(deltas),
        "any_diverge": any_diverge,
        "deltas": deltas,
    }
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print()
    print(f"  Witness: {OUT_PATH.name}")
    print(f"  atoms compared: {len(deltas)}, divergent: "
          f"{sum(1 for d in deltas if not d['within_1ppb'])}")

    if args.strict and any_diverge:
        print()
        print("  STRICT mode: divergence above 1ppb — exiting 1")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
