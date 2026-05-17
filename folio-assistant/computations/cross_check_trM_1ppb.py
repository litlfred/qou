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
# Third path landed via PR #681's Step 2 + this PR's combiner: the
# canonical Σ_λ y_λ(q_0) · χ^λ(β; q_0) trace built from per-irrep
# chi caches (`per_irrep_pole_atom.py` chi-{atom}-h{n} caches).
CHICACHE_PATH = HERE / "canonical-tr-m-via-chi-cache.witness.json"
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

    # Third path: canonical chi-cache combiner (PR #681 Step 2).
    # Only atoms with COMPLETE chi caches contribute to the 1ppb
    # gate; partial caches yield truncated traces and are reported
    # separately as `chi_cache_partial`.
    chicache_by_atom: dict[str, dict] = {}
    chicache_partials: dict[str, dict] = {}
    if CHICACHE_PATH.exists():
        chicache = json.loads(CHICACHE_PATH.read_text())
        for r in chicache.get("data", {}).get("results", []) or chicache.get("results", []):
            atom = r.get("atom")
            if atom is None:
                continue
            if r.get("partial_cache"):
                chicache_partials[atom] = r
            else:
                chicache_by_atom[atom] = r

    common_atoms = sorted(
        set(hoef_by_atom) & set(peel_by_atom)
    )

    print("=" * 76)
    print("Cross-check tr_M @ q_0 — Hoefsmit (mpfr 50dps) vs markov_peel")
    print("=" * 76)
    print(f"  tolerance: {TOLERANCE} (1 ppb)  |  dps: {args.dps}")
    print()
    print(f"  {'atom':<14} {'Hoefsmit':>20}  {'markov_peel':>20}  "
          f"{'chi-cache':>20}  {'|Δ_rel|max':>11}  status")
    print("  " + "─" * 95)

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

        # Third path (chi-cache combiner). Optional — only present
        # for atoms with COMPLETE chi caches (proton, neutron,
        # deuteron in the initial wave; T/³He/⁴He pending Step 2).
        chi_entry = chicache_by_atom.get(atom)
        if chi_entry is not None:
            c_val = mpmathify(chi_entry["abs_tr_M_q0"])
        else:
            c_val = None

        if h_val == 0 and p_val == 0:
            rel_hp = mpf(0)
        elif h_val == 0:
            rel_hp = fabs(p_val)
        else:
            rel_hp = fabs(p_val - h_val) / fabs(h_val)

        if c_val is not None and h_val != 0:
            rel_hc = fabs(c_val - fabs(h_val)) / fabs(h_val)
            rel_max = max(rel_hp, rel_hc)
        else:
            rel_hc = None
            rel_max = rel_hp

        ok = rel_max < TOLERANCE
        if not ok:
            any_diverge = True
        status = "OK" if ok else "DIVERGE"
        c_str = f"{str(c_val)[:20]:>20}" if c_val is not None else f"{'(partial cache)':>20}"
        print(f"  {atom:<14} {str(h_val)[:20]:>20}  "
              f"{str(p_val)[:20]:>20}  {c_str}  "
              f"{mp.nstr(rel_max, 3):>11}  {status}")

        d: dict = {
            "atom": atom,
            "hoefsmit_50dps": str(h_val),
            "markov_peel": str(p_val),
            "abs_delta_hoef_peel": str(fabs(p_val - h_val)),
            "rel_delta_hoef_peel": str(rel_hp),
            "within_1ppb": ok,
        }
        if c_val is not None:
            d["chi_cache_canonical"] = str(c_val)
            d["abs_delta_hoef_chi"] = str(fabs(c_val - fabs(h_val)))
            d["rel_delta_hoef_chi"] = str(rel_hc)
        elif atom in chicache_partials:
            d["chi_cache_partial"] = {
                "partitions_used": chicache_partials[atom]["partitions_used"],
                "partitions_total": chicache_partials[atom]["partitions_total"],
            }
        deltas.append(d)

    out = {
        "auditOnly": "docs/audits/2026-05-08-crystal-r-matrix-sublemma-2-1.md",
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
