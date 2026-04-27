#!/usr/bin/env python3
"""Audit canonical compute scripts for alignment with calibration-inputs.md.

Per content/quantum-observable-universe/braids-and-knots/calibration-inputs.md
the canonical 3-input scheme is:

  1. m_μ/m_e = 206.768   → fixes q_0 (substrate)
  2. m_e = 0.511 MeV     → leptonic mass scale
  3. Q_β(n) = 0.7823 MeV → hadronic energy scale E_0

  m_n = m_p + Q_β        (Hecke engine)
  m_p: derived via Skein pair formula (Skein resolution of Borromean
       braid is OPEN; currently calibrated)
  μ_u, μ_d: derived from Skein resolution tree (currently
       back-solved from m_p, m_n)

Anything that uses BOTH m_p AND m_n from CODATA over-counts the
hadronic input. Anything using μ_d − μ_u from CODATA splitting
implicitly uses BOTH.

Audit each Python script under folio-assistant/computations/ and
classify by which inputs it uses. Emits canonical-script-input-audit
witness with per-script row.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder

HERE = Path(__file__).parent

# Markers we look for in each script
MARKERS = {
    "M_E_MEV":     re.compile(r"\bM_E_MEV\b"),
    "M_P_MEV":     re.compile(r"\bM_P_MEV\b"),
    "M_N_MEV":     re.compile(r"\bM_N_MEV\b"),
    "Q_NEUTRON":   re.compile(r"\bQ_NEUTRON_MEV\b|\bQ_BETA\b|\bQ_beta\b"),
    "Q_TRITIUM":   re.compile(r"\bQ_TRITIUM_MEV\b"),
    "Q_C14":       re.compile(r"\bQ_C14_MEV\b"),
    "Vol_hyp":     re.compile(r"\bVol\(.*\)|\bvol_hyp\b|\bVOL_BORROMEAN\b|\bVOL_FIGURE_EIGHT\b|\bVOL_THREE_TWIST\b"),
    "q_parameter": re.compile(r"from q_parameter import|from\s+q_parameter\s+import"),
    "experimental_constants": re.compile(r"from experimental_constants import|from\s+experimental_constants\s+import"),
    "MASS_RATIO_MU_E": re.compile(r"\bMASS_RATIO_MU_E\b|\bMU_OVER_E\b"),
    "calibration_skein_pair": re.compile(r"skein.pair|S_uu|S_ud|S_dd|μ_u|μ_d|mu_u|mu_d"),
}


def classify_script(path: Path) -> dict:
    """Read script and tally which canonical inputs it uses."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if "import" not in text and "def " not in text:
        return None  # data file, skip
    found = {key: bool(rx.search(text)) for key, rx in MARKERS.items()}
    # Determine alignment status
    uses_m_p = found["M_P_MEV"]
    uses_m_n = found["M_N_MEV"]
    uses_q_beta = found["Q_NEUTRON"]
    uses_vol_hyp = found["Vol_hyp"]
    uses_canonical_q0 = found["q_parameter"]
    uses_canonical_consts = found["experimental_constants"]
    if uses_m_p and uses_m_n:
        # Two hadronic inputs — over-count if Q_β not also used
        scheme = "4-input-mp-and-mn (over-counts hadronic if Q_β implicit)"
    elif uses_m_p and uses_q_beta:
        scheme = "3-input-canonical (m_p + Q_β; per calibration-inputs.md)"
    elif uses_m_n and uses_q_beta:
        scheme = "3-input-alt (m_n + Q_β)"
    elif uses_m_p and not uses_m_n:
        scheme = "m_p-only (no Q_β; m_n derivation TBD)"
    elif uses_m_n and not uses_m_p:
        scheme = "m_n-only (no Q_β; m_p derivation TBD)"
    elif uses_q_beta:
        scheme = "Q_β-only-hadronic"
    elif uses_vol_hyp:
        scheme = "vol-hyp-fitted (uses hyperbolic volume; FITTED under option B)"
    else:
        scheme = "no-hadronic-input (substrate-only or pure dimensionless)"
    return {
        "script":     path.name,
        "found":      found,
        "scheme":     scheme,
        "uses_canonical_q0_source":     uses_canonical_q0,
        "uses_canonical_consts_source": uses_canonical_consts,
    }


def main():
    rows = []
    for py in sorted(HERE.glob("*.py")):
        if py.name.startswith("_"):
            continue
        result = classify_script(py)
        if result is None:
            continue
        rows.append(result)

    # Bucket by scheme
    buckets = {}
    for r in rows:
        buckets.setdefault(r["scheme"], []).append(r["script"])

    # Print summary
    print("=" * 80)
    print(f"Canonical-compute input audit  ({len(rows)} scripts)")
    print("=" * 80)
    for scheme, scripts in sorted(buckets.items(), key=lambda x: -len(x[1])):
        print(f"\n  {scheme}  ({len(scripts)} scripts)")
        for s in scripts[:8]:
            print(f"    {s}")
        if len(scripts) > 8:
            print(f"    … and {len(scripts) - 8} more")
    print()

    # Build summary statistics
    total = len(rows)
    by_scheme = {scheme: len(scripts) for scheme, scripts in buckets.items()}
    canonical_3input = sum(
        n for s, n in by_scheme.items()
        if "3-input-canonical" in s
        or "3-input-alt" in s
        or "Q_β-only-hadronic" in s
    )
    over_counts = sum(
        n for s, n in by_scheme.items() if "over-counts" in s
    )
    fitted = sum(
        n for s, n in by_scheme.items() if "FITTED" in s or "vol-hyp" in s.lower()
    )

    print(f"Summary:")
    print(f"  Aligned with calibration-inputs.md (3-input canonical): {canonical_3input} / {total} ({100*canonical_3input/total:.1f}%)")
    print(f"  Uses both m_p AND m_n (over-count hadronic):           {over_counts} / {total} ({100*over_counts/total:.1f}%)")
    print(f"  Uses Vol_hyp (fitted under option B):                  {fitted} / {total} ({100*fitted/total:.1f}%)")
    print(f"  Other (no-hadronic / substrate-only):                  {total - canonical_3input - over_counts - fitted} / {total}")

    # Build witness
    w = (
        WitnessBuilder("canonical-script-input-audit", engine="python")
        .set_description(
            "Audit of every Python computation script under "
            "folio-assistant/computations/ for alignment with the "
            "paper's 3-input canonical scheme (calibration-inputs.md): "
            "q_0 from m_μ/m_e, m_e, and Q_β(n). Flags scripts that "
            "use both m_p AND m_n from CODATA (over-counts hadronic "
            "input), use Vol_hyp (fitted under option B), or omit "
            "canonical input modules entirely."
        )
        .set_content_block("calibration-inputs.md")
        .add_parameter("total_scripts_audited", total)
        .add_data("by_scheme", by_scheme)
        .add_data("rows", rows)
        .add_data("canonical_3input_count", canonical_3input)
        .add_data("over_count_count", over_counts)
        .add_data("vol_hyp_fitted_count", fitted)
        .add_caveat(
            "Heuristic detection by import + regex. False positives possible "
            "for scripts that comment out CODATA constants or use them only "
            "for comparison rather than derivation."
        )
        .add_caveat(
            "Per calibration-inputs.md: m_n = m_p + Q_β (Hecke engine). "
            "Scripts using both m_p and m_n from CODATA are using 4 "
            "hadronic inputs where 3 suffice."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
