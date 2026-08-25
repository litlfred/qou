#!/usr/bin/env python3
"""Wiring status of every atom in the mass-table sweep.

Per author direction 2026-05-24: "no census assigned/searching, only
use canonical/SDP braid words".  This script classifies every entry
in `mass_table_ppb.py`'s ATOM_ASSIGN by wiring-derivation status and
reports what's CANONICAL vs EXPLORATORY vs GAP.

## Wiring-status taxonomy

| Status | Meaning | What's needed for ✅ |
|--------|---------|---------------------|
| **canonical-sdp** | knot + ν_SDP derived from R5-full SDP solver | (none — fully wired) |
| **extrapolated** | knot framework-derived, ν_SDP extrapolated | R5-full SDP solver landing |
| **exploratory** | census-assigned knot; ν_SDP guessed | R5-full SDP solver + Rule-14 census audit |
| **alpha-cluster** | built on n × ⁴He extrapolation | ⁴He canonical first |
| **gap** | no atom→knot rule | Rule-14 atom-knot census expansion to A ∈ {5, 6, 7} |
| **unwired** | not even in ATOM_ASSIGN | atom→knot rule authoring |

## KLR positivity check

Khovanov-Lauda-Rouquier categorification gives a **positivity
property** for canonical-basis structure constants.  Predicted
binding from the framework's |tr_M| · Vol(K) formula is a **lower
bound** on observed binding (since the formula captures only the
canonical-basis projection; positive-coefficient corrections from
the full crystal-shadow live ABOVE this lower bound).

**Therefore: predicted ≤ observed.**  Over-predictions
(B_pred > B_AME) indicate the formula has a mistake — either
the wrong knot, wrong ν_SDP, or a missing structural restriction.

This script flags every over-prediction as a KLR-positivity violation
and tags it with the suspect formula component.

## Diagnostics (per canonical-watcher §Slot J)

- **GB filtration**: ℓ-dependent per atom; reported via the knot's
  braid-word length (proxy)
- **Jet order**: leading-order h^0 (bare volume); deviation magnitude
  reported in h^k units (h ≈ 0.209 at q_0, h² ≈ 0.0437, h⁴ ≈ 0.00191)
- **Bar-symmetry**: B_pred is bar-symmetric (positive volume × positive
  ν_SDP); deviations may be bar-anti-symmetric (h^odd) or bar-symmetric
  (h^even)

## Output

- Console: tabular wiring-status report
- Witness: `mass-sweep-wiring-status.witness.json` — per-atom rows
  with (status, suspect-component, error-jet-order-classification)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# Substrate q_0 at 50 dps
set_compute_dps()
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0 = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
h = q0 - 1 / q0
H_F = float(h)
H_SQ_F = float(h ** 2)
H_4_F = float(h ** 4)

AME = [
    ("2H",   1, 1, 2,   float(AME_B_DEUTERON_MEV_VALIDATION)),
    ("3H",   1, 2, 3,   float(AME_B_TRITIUM_MEV_VALIDATION)),
    ("3He",  2, 1, 3,   float(AME_B_HE3_MEV_VALIDATION)),
    ("4He",  2, 2, 4,  float(AME_B_HE4_MEV_VALIDATION)),
    ("5Li",  3, 2, 5,  26.328),
    ("6Li",  3, 3, 6,  float(AME_B_LI6_MEV_VALIDATION)),
    ("7Li",  3, 4, 7,  39.24453),
    ("8Be",  4, 4, 8,  56.49951),
    ("9Be",  4, 5, 9,  58.16500),
    ("11B",  5, 6, 11, 76.20550),
    ("12C",  6, 6, 12, 92.16175),
    ("14N",  7, 7, 14, 104.65880),
    ("16O",  8, 8, 16, 127.61929),
    ("19F",  9, 10, 19, 147.80140),
    ("20Ne", 10, 10, 20, 160.64486),
    ("24Mg", 12, 12, 24, 198.25690),
    ("40Ca", 20, 20, 40, 342.05210),
]

WIRING = {
    "2H":   ("exploratory",   "knot=6_2 census-assigned + ν_SDP=1 guess",  "Rule-14 census + R5-full SDP solver"),
    "3H":   ("exploratory",   "knot=8_11 census-assigned + ν_SDP=2 guess", "Rule-14 census + R5-full SDP solver"),
    "3He":  ("exploratory",   "link=L6a4 census-assigned + ν_SDP=2 guess", "Rule-14 census + R5-full SDP solver"),
    "4He":  ("extrapolated",  "A·8G magic rule + ν_SDP=2 extrapolated",     "R5-full SDP solver"),
    "5Li":  ("gap",           "no atom→knot rule for A=5",                  "Rule-14 census expansion to A∈{5,6,7}"),
    "6Li":  ("gap",           "no atom→knot rule for A=6",                  "Rule-14 census expansion to A∈{5,6,7}"),
    "7Li":  ("gap",           "no atom→knot rule for A=7",                  "Rule-14 census expansion to A∈{5,6,7}"),
    "8Be":  ("alpha-cluster", "2×4He + 1×c_αα recursion (built on ⁴He extrap.)", "4He canonical first"),
    "9Be":  ("gap",           "2α+n Borromean halo — composite rule needed", "α-core + valence nucleon decomposition"),
    "11B":  ("gap",           "2α+3p p-shell — composite rule needed",      "α-core + valence nucleon decomposition"),
    "12C":  ("alpha-cluster", "3×4He + 3×c_αα recursion",                   "4He canonical first"),
    "14N":  ("gap",           "3α+2p N=Z mirror — composite rule needed",   "α-core + valence nucleon decomposition"),
    "16O":  ("alpha-cluster", "4×4He + 6×c_αα recursion",                   "4He canonical first"),
    "19F":  ("gap",           "4α+3p sd-shell onset — composite rule needed","α-core + valence nucleon decomposition"),
    "20Ne": ("alpha-cluster", "5×4He + 10×c_αα recursion",                  "4He canonical first"),
    "24Mg": ("alpha-cluster", "6×4He + 15×c_αα recursion",                  "4He canonical first"),
    "40Ca": ("alpha-cluster", "10×4He + 45×c_αα recursion",                 "4He canonical first"),
}

# B_pred values from the current EXPLORATORY/extrapolated layer (per
# mass_table_ppb.py default output).  Only used to flag KLR-positivity
# violations against the EXPLORATORY layer — not to assert framework
# correctness.
B_PRED_EXPLORATORY = {
    "2H":   2.2488,
    "3H":   8.4686,
    "3He":  7.4889,
    "4He":  29.9557,
    "8Be":  62.3383,
    "12C":  97.1480,
    "16O": 134.3846,
    "20Ne": 174.0483,
    "24Mg": 216.1389,
    "40Ca": 408.7713,
}


def jet_order_classification(err_rel: float) -> str:
    """Classify |relative error| in jet-order h^k units."""
    if err_rel < H_4_F * 0.5:
        return f"<h⁴/2 (≈ {H_4_F/2:.2e})"
    if err_rel < H_4_F * 2:
        return f"≈ h⁴ (≈ {H_4_F:.2e})"
    if err_rel < H_SQ_F * 0.5:
        return f"between h⁴ and h²/2"
    if err_rel < H_SQ_F * 2:
        return f"≈ h² (≈ {H_SQ_F:.2e})"
    if err_rel < H_F * 0.5:
        return f"between h² and h/2"
    if err_rel < H_F * 2:
        return f"≈ h (≈ {H_F:.2e})"
    return f"> 2h ({err_rel:.2e}) — large, suggests structural mistake"


def main() -> int:
    print("=" * 130)
    print("MASS-SWEEP WIRING-STATUS REPORT")
    print(f"  q_0 = {float(q0):.10f}    h = q-q⁻¹ = {H_F:.10f}")
    print(f"  h² = {H_SQ_F:.6e}    h⁴ = {H_4_F:.6e}")
    print(f"  KLR positivity: predicted ≤ observed (canonical basis lower bound)")
    print("=" * 130)
    print(f"  {'atom':>5} {'A':>3}  {'B_AME':>10}  {'wiring status':>16}  "
          f"{'KLR':>4}  {'err/h^k class':>22}  suspect component")
    print("  " + "-" * 128)
    rows = []
    status_counts = {}
    klr_violations = 0
    for sym, Z, N, A, B_ame in AME:
        status, suspect, needs = WIRING[sym]
        status_counts[status] = status_counts.get(status, 0) + 1
        B_pred = B_PRED_EXPLORATORY.get(sym)
        err = B_pred - B_ame if B_pred is not None else None
        err_rel = err / B_ame if (err is not None and B_ame > 0) else None
        klr_violates = (err is not None and err > 0)
        klr_flag = "✗" if klr_violates else ("✓" if err is not None else "—")
        if klr_violates:
            klr_violations += 1
        jet_class = jet_order_classification(abs(err_rel)) if err_rel is not None else "(no B_pred)"
        sign = "+" if (err is not None and err > 0) else ("−" if err is not None else " ")
        print(f"  {sym:>5} {A:>3}  {B_ame:>10.4f}  {status:>16}  "
              f"{klr_flag:>4}  {sign}{jet_class:>21}  {suspect}")
        rows.append({
            "atom": sym, "A": A, "Z": Z, "N": N,
            "B_AME_MeV": B_ame,
            "B_pred_exploratory_MeV": B_pred,
            "err_MeV": err,
            "err_rel": err_rel,
            "wiring_status": status,
            "klr_positivity_violates": klr_violates,
            "jet_order_classification": jet_class,
            "suspect_component": suspect,
            "needs_for_canonical": needs,
        })

    print("  " + "-" * 128)
    print()
    print("STATUS SUMMARY:")
    for status, count in sorted(status_counts.items()):
        print(f"  {status:>16}:  {count} atoms")
    print()
    print(f"KLR positivity violations:  {klr_violations} / {sum(1 for r in rows if r['B_pred_exploratory_MeV'] is not None)}")
    print()
    print("WHAT THE FRAMEWORK CAN SAY CANONICALLY:")
    canonical_atoms = [r for r in rows if r["wiring_status"] == "canonical-sdp"]
    if not canonical_atoms:
        print("  (NONE)  No atom in the AME sweep is fully canonically wired.")
        print("  Every prediction in the current mass table sits at the")
        print("  EXPLORATORY or extrapolated layer.  Production-grade")
        print("  canonical wiring requires R5-full SDP solver landing.")
    else:
        for r in canonical_atoms:
            print(f"  {r['atom']:>5}: {r['B_pred_exploratory_MeV']:.4f} MeV")

    w = WitnessBuilder("mass-sweep-wiring-status", engine="python+mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Wiring-status taxonomy for every atom in mass_table_ppb.py "
        "ATOM_ASSIGN.  Per author direction 2026-05-24, classifies "
        "each entry as canonical-sdp / extrapolated / exploratory / "
        "alpha-cluster / gap / unwired.  Identifies KLR-positivity "
        "violations (predicted > observed) and the suspect formula "
        "component for each.  Reports that NO atom is fully "
        "canonically wired — every current prediction sits at "
        "EXPLORATORY/extrapolated layer, awaiting R5-full SDP."
    )
    w.add_parameter("q_0", float(q0))
    w.add_parameter("h_q0", H_F)
    w.add_parameter("h_sq_q0", H_SQ_F)
    w.add_parameter("h_4_q0", H_4_F)
    w.add_parameter(
        "klr_positivity",
        "Khovanov-Lauda-Rouquier categorical positivity: framework's "
        "|tr_M|·Vol(K) prediction is a LOWER BOUND on observed binding. "
        "Over-predictions (B_pred > B_AME) indicate the formula has a "
        "mistake — wrong knot, wrong ν_SDP, or missing restriction.",
    )
    w.add_data("per_atom_wiring_status", rows)
    w.add_data("status_summary", status_counts)
    w.add_data("klr_violations_count", klr_violations)
    w.add_data(
        "fully_canonically_wired_atoms",
        [r["atom"] for r in canonical_atoms],
    )
    w.add_assertion(
        "no_atom_fully_canonical",
        computed=len(canonical_atoms),
        expected=0,
        tolerance=0,
        unit="atoms",
        source="ATOM_ASSIGN wiring-status survey",
    )
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
