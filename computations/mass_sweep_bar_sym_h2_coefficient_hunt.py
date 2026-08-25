#!/usr/bin/env python3
"""Bug-hunt: derive the bar-symmetric h² correction coefficient per atom.

Per author direction 2026-05-24: "utilize error findings and paper/
lean results to isolate and squash compute bugs".

## Method

Each KLR-violating atom in the mass table has its error sitting at
the **bar-symmetric h² scale** (verified by `mass_sweep_wiring_status.py`,
PR #1214) or close to it.  The just-merged Lean proofs:

  - `Q_borromean(h) = 0` (PR #1211, commit 5329eb054):
      trM_borromean(h) is bar-symmetric → no bar-anti-symmetric
      component, so the framework's bar-anti-symmetric residue
      must come from operator-valued ⋈_K, NOT bare Borromean.

  - `⋈_K is bar-symmetric` (commit 68e51f80e, today):
      Proved symbolically in (2,1) of H_3(q).  The operator-valued
      bowtie's Q-channel projection vanishes structurally.

  → CONSEQUENCE: any KLR-violating bar-symmetric h² correction
    must come from a SHARED structural factor across atoms, not
    from per-atom operator-valued bowtie contributions (which
    cancel) and not from bar-Borromean structure (also cancels).

## Hypothesis to test

The framework's magic A·8G rule formula

  B(atom) = ν_SDP · m_e · A · 8G            (production)

is missing a bar-symmetric h² correction:

  B(atom) = ν_SDP · m_e · A · 8G · (1 - c·h²)

If the single coefficient `c` reproduces AME for ALL KLR-violating
atoms, it's a **canonical h² correction at the formula-structure
level** — the bug is missing this term in the magic A·8G rule.

If `c` varies per atom, the α-cluster recursion is wrong (each
atom has different bar-symmetric structure) — bigger structural
bug.

## Compute

For each KLR-violating atom with magic / α-cluster production rule,
solve

  c_atom = (1 - B_AME / B_prod) / h²

and tabulate.

## Output

- Console: per-atom `c_atom` table + variance/consistency analysis
- Witness: `mass-sweep-bar-sym-h2-coefficient.witness.json` with
  conclusion: single coefficient or per-atom variance?
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
from codata_constants import AME_B_HE4_MEV_VALIDATION  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0 = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
h = q0 - 1 / q0
h2 = h ** 2
h4 = h ** 4

# Constants (canonical, from knot_volumes.py + experimental_constants.py)
M_E_MEV = mp.mpf("0.51099895")  # noqa: P31 — CAL-1 m_e; exploratory sweep, value preserved
VOL_BORROMEAN = 8 * mp.catalan  # = 8G, Thurston 1979
VOL_7_SQ_1 = mp.mpf("4.7494999818964") # Vol(7^2_1) from SnapPy
C_ALPHA_DERIVED = M_E_MEV * VOL_7_SQ_1  # = m_e · Vol(7^2_1)

# KLR-violating atoms with production formula (magic/α-cluster).
# Each row: (sym, A, n_alpha, n_pairs, rule, B_AME_MeV)
ATOMS = [
    ("4He",    4,  1,   0, "magic",          AME_B_HE4_MEV_VALIDATION),
    ("8Be",    8,  2,   1, "alpha",          mp.mpf("56.49951")),
    ("12C",   12,  3,   3, "alpha",          mp.mpf("92.16175")),
    ("16O",   16,  4,   6, "alpha",          mp.mpf("127.61929")),
    ("20Ne",  20,  5,  10, "alpha",          mp.mpf("160.64486")),
    ("24Mg",  24,  6,  15, "alpha",          mp.mpf("198.25690")),
    ("40Ca",  40, 10,  45, "alpha",          mp.mpf("342.05210")),
]


def b_prod_magic(A: int) -> mp.mpf:
    """B_pred from magic A·8G rule with ν_SDP=2."""
    return 2 * M_E_MEV * A * VOL_BORROMEAN


def b_prod_alpha(n_alpha: int, n_pairs: int) -> mp.mpf:
    """B_pred from α-cluster recursion built on 4He magic."""
    B_4He = b_prod_magic(4)
    return n_alpha * B_4He + n_pairs * C_ALPHA_DERIVED


def main() -> int:
    print("=" * 110)
    print("BAR-SYMMETRIC h² COEFFICIENT HUNT — isolate compute bug")
    print(f"  h = q-q⁻¹ at q_0 = {float(h):.10f}    h² = {float(h2):.10f}")
    print(f"  m_e = {float(M_E_MEV):.6f} MeV    8G = {float(VOL_BORROMEAN):.6f}")
    print("=" * 110)
    print(f"  {'atom':>5} {'A':>3} {'rule':>8}  {'B_AME':>10}  {'B_prod':>11}  "
          f"{'B_prod-B_AME':>13}  {'c_atom (h² coef)':>20}  {'c·h² (frac)':>13}")
    print("  " + "-" * 108)

    rows = []
    c_values = []
    for sym, A, n_a, n_p, rule, B_ame in ATOMS:
        if rule == "magic":
            B_prod = b_prod_magic(A)
        elif rule == "alpha":
            B_prod = b_prod_alpha(n_a, n_p)
        else:
            continue
        # Solve B_AME = B_prod · (1 - c · h²):  c = (1 - B_AME/B_prod) / h²
        ratio = B_ame / B_prod
        c_atom = (1 - ratio) / h2
        c_h2 = c_atom * h2
        c_values.append((sym, c_atom))
        diff = B_prod - B_ame
        print(f"  {sym:>5} {A:>3} {rule:>8}  {float(B_ame):>10.4f}  "
              f"{float(B_prod):>11.4f}  {float(diff):>+13.6f}  "
              f"{mp.nstr(c_atom, 8):>20}  {mp.nstr(c_h2, 5):>13}")
        rows.append({
            "atom": sym, "A": A, "rule": rule,
            "B_AME_MeV": float(B_ame),
            "B_prod_MeV": float(B_prod),
            "diff_MeV": float(diff),
            "c_h2_coefficient": float(c_atom),
            "c_times_h2_fraction": float(c_h2),
        })
    print("  " + "-" * 108)

    # Consistency analysis: is there a single c reproducing all?
    c_4he = c_values[0][1]
    print()
    print(f"REFERENCE: c(⁴He) = {mp.nstr(c_4he, 10)}")
    print(f"  Equivalent canonical ν: ν_canonical = 2·(1 - c·h²) = {mp.nstr(2*(1 - c_4he*h2), 10)}")
    print()
    print("PER-ATOM c_atom / c(⁴He) ratio:")
    for sym, c in c_values:
        ratio_to_4he = c / c_4he
        print(f"  {sym:>5}: c_atom/c(⁴He) = {mp.nstr(ratio_to_4he, 8):>12}    "
              f"deviation from 1.0: {mp.nstr(ratio_to_4he - 1, 8)}")
    print()

    max_dev = max(abs(c / c_4he - 1) for _, c in c_values)
    print(f"Max deviation from c(⁴He): {mp.nstr(max_dev, 8)}")
    if max_dev < mp.mpf("1e-3"):
        verdict = "SINGLE COEFFICIENT — bug is missing bar-symmetric h² term in magic A·8G rule"
    elif max_dev < mp.mpf("0.05"):
        verdict = "NEAR-SINGLE COEFFICIENT — possible single c + α-cluster recursion adjustment"
    else:
        verdict = "VARYING — α-cluster recursion is structurally wrong; each atom needs different bar-symmetric h² correction"
    print(f"Verdict: {verdict}")
    print()

    # Cross-check: try common closed forms for c(⁴He)
    print("CLOSED-FORM CANDIDATES for c(⁴He):")
    candidates = {
        "5/2": mp.mpf("5") / 2,
        "5/2 · (1 - h²/2)": mp.mpf("5") / 2 * (1 - h2 / 2),
        "1/h": 1 / h,           # h^-1 — unphysical but check
        "A/2 (= 2)": mp.mpf("2"),
        "A (= 4)": mp.mpf("4"),
        "(A+1)/2 (= 5/2)": mp.mpf("5") / 2,
        "ln(2)/h²": mp.log(2) / h2,
        "π²/24": mp.pi**2 / 24,
    }
    for name, cand in candidates.items():
        rel = (c_4he - cand) / c_4he if cand != 0 else mp.inf
        print(f"  {name:>20} = {mp.nstr(cand, 10):>16}    rel diff to c(⁴He): "
              f"{mp.nstr(rel, 6)}")
    print()

    w = WitnessBuilder("mass-sweep-bar-sym-h2-coefficient", engine="python+mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Bug-hunt: derive the bar-symmetric h² correction coefficient "
        "per KLR-violating atom in the mass-table sweep. Tests whether "
        "a SINGLE c (canonical structural correction) reproduces AME "
        "for all atoms, or whether c varies (α-cluster recursion wrong). "
        "Uses paper-side identity Q_borromean(h)=0 (PR #1211) + ⋈_K "
        "bar-symmetric (commit 68e51f80e) to argue any h² correction "
        "must be a single canonical factor."
    )
    w.add_parameter("q_0", float(q0))
    w.add_parameter("h", float(h))
    w.add_parameter("h_squared", float(h2))
    w.add_parameter("verdict", verdict)
    w.add_parameter("c_4He", float(c_4he))
    w.add_parameter("nu_canonical_4He", float(2*(1 - c_4he*h2)))
    w.add_parameter("max_deviation_from_c_4He", float(max_dev))
    w.add_data("per_atom_c_values", rows)
    w.add_data("ratios_to_4He", [
        {"atom": sym, "c_atom_over_c_4He": float(c / c_4he)}
        for sym, c in c_values
    ])
    closed_form_data = []
    for name, cand in candidates.items():
        rel = float((c_4he - cand) / c_4he) if cand != 0 else None
        closed_form_data.append({
            "candidate": name,
            "value": float(cand),
            "rel_diff_to_c_4He": rel,
        })
    w.add_data("closed_form_candidates_for_c_4He", closed_form_data)
    w.add_assertion(
        "single_coefficient_hypothesis",
        computed=float(max_dev),
        expected=0.0,
        tolerance=0.05,  # 5% tolerance — if all c values within 5%, single c
        unit="dimensionless",
        source="(1 - B_AME/B_prod) / h² uniformity check",
    )
    out = w.save()
    print(f"Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
