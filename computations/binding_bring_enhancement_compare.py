#!/usr/bin/env python3
"""binding_bring_enhancement_compare — does Bring color-tube weighting
close the 15% T vs ³He f-factor spread?

Re-runs the binding-shell-enhancement analysis at q_0 with
`pn_convention="bring_color_weighted"` and compares to
`pn_convention="strict_averaged"` (the historical baseline used by
`binding_shell_enhancement_derivation.py`). The Bring weighting uses
the substrate-pure formula

    f_pn = z - h · (1/2 - δ/4),   δ = Δm_{n-p}/M_N ≈ 1.37e-3
                                   (`_li_2_q_util.flavor_split_leading`,
                                    PROVED PR #690/#942)

per `closed_form_tau_M.py::closed_form_ratio` and the categorical
content of `conj:inter-nucleon-channel-color-tube`
(`brings-surface/inter-nucleon-channel-color-tube.md`).

Honest framing: this is the Bring-weighted re-run requested in the
audit `docs/audits/2026-05-31-binding-magic-A-wireup.md` § "What
remains open" item 2. The question is **structural**: does the
substrate-pure δ at q_0 (180.9 ppm uniform correction across
single-pn-arc atoms) move the f-factor spread between T and ³He?

Outputs `binding-bring-enhancement-compare.witness.json`.

Run from repo root: `python3 computations/binding_bring_enhancement_compare.py --print`
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# `set_compute_dps()` must run BEFORE `codata_constants` is imported. That
# module builds its AME constants inside `mp.workdps(max(50, mp.mp.dps))` at
# import time, and importing `_precision` does not itself set `mp.dps` (its
# own docstring: "IMPORTING THIS MODULE DOES NOT SET mp.dps"). Left at
# mpmath's default 15 the guard clamps them to 50 digits, and `fmt` then
# serializes 60 digits of a 50-digit value: `2.2245662` came out as
# "2.2245661999999999999999999999999999999999999999999" + "9734095406"
# — a binary tail reading as measured. Ordering the import is the fix.
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from _li_2_q_util import flavor_split_leading  # noqa: E402
from closed_form_tau_M import closed_form_ratio  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# AME2020 binding energies (MeV)
AME = {
    "D":   AME_B_DEUTERON_MEV_VALIDATION,
    "T":   AME_B_TRITIUM_MEV_VALIDATION,
    "³He": AME_B_HE3_MEV_VALIDATION,
    "⁴He": AME_B_HE4_MEV_VALIDATION,
}


def build_witness() -> dict:
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    delta = flavor_split_leading(q)

    # Vol(𝓑₃) = 8G (Catalan)
    vol_b3 = 8 * mp.catalan

    rows: list[dict] = []
    raw: dict[str, dict] = {}
    for label, Z, N in [("D", 1, 1), ("T", 1, 2), ("³He", 2, 1), ("⁴He", 2, 2)]:
        r_strict = closed_form_ratio(Z, N, q, pn_convention="strict_averaged")
        r_bring = closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted")

        # Naive B_endo at q_0 using closed_form_ratio as a proxy for
        # |tr_M(free)| − |tr_M(atom)| ↦ ratio (rough; the actual
        # binding_canonical mass-formula path is more involved, but
        # the RELATIVE Bring-vs-strict difference is the structural
        # quantity we want here).
        # Kept in mpf. These were float() -- which capped f_required at 53
        # bits while it was still serialized at 60 digits, so the tail was
        # binary64 expansion reading as measured (NO-FLOAT64).
        b_endo_strict = M_E_MEV * vol_b3 * (1 - r_strict)
        b_endo_bring = M_E_MEV * vol_b3 * (1 - r_bring)

        b_exp = AME[label]
        f_strict = b_exp / b_endo_strict if b_endo_strict != 0 else mp.nan
        f_bring = b_exp / b_endo_bring if b_endo_bring != 0 else mp.nan

        raw[label] = {"f_strict": f_strict, "f_bring": f_bring}
        rows.append({
            "atom": label,
            "Z": Z,
            "N": N,
            "tau_M_ratio_strict": fmt(r_strict),
            "tau_M_ratio_bring": fmt(r_bring),
            "tau_M_ratio_delta_ppm": fmt(
                (r_bring - r_strict) / r_strict * mp.mpf("1e6")),
            "B_endo_strict_MeV": fmt(b_endo_strict),
            "B_endo_bring_MeV": fmt(b_endo_bring),
            "B_AME_MeV": fmt(b_exp),
            "f_required_strict": fmt(f_strict),
            "f_required_bring": fmt(f_bring),
        })

    # T vs ³He f-spread (the open question). Read from `raw`, not from
    # `rows`: the latter now holds the serialized strings.
    t_row = raw["T"]
    he3_row = raw["³He"]
    f_spread_strict = abs(t_row["f_strict"] - he3_row["f_strict"]) \
        / max(t_row["f_strict"], he3_row["f_strict"])
    f_spread_bring = abs(t_row["f_bring"] - he3_row["f_bring"]) \
        / max(t_row["f_bring"], he3_row["f_bring"])

    summary = (
        f"T vs ³He f-factor spread (single-magic A=3 p/n asymmetry): "
        f"strict_averaged = {f_spread_strict * 100:.2f}%, "
        f"bring_color_weighted = {f_spread_bring * 100:.2f}%. "
    )
    if abs(f_spread_strict - f_spread_bring) / f_spread_strict < 0.01:
        summary += (
            "The Bring weighting at q_0 produces a substantially identical "
            "f-spread — the 180.9 ppm uniform correction cancels out of the "
            "T vs ³He ratio because both have exactly one pn arc. "
            "The 15%+ T vs ³He spread is at the arc-COMPOSITION layer "
            "(T = pn+nn vs ³He = pp+pn, distinct factors f_nn ≠ f_pp), "
            "NOT at the pn-arc weighting layer; Bring weighting cannot "
            "close it. The actual closure path is the operator-valued "
            "Wenzl branching with full per-arc operator extracts "
            "(canonical_tr_m_via_branching.py + A_operator_extract_at_level.py), "
            "not a scalar pn-weighting refinement."
        )
    else:
        summary += "The Bring weighting moves the f-spread non-trivially; revisit interpretation."

    return {
        "name": "binding-bring-enhancement-compare",
        "description": (
            "Re-runs the T vs ³He f-factor comparison with "
            "pn_convention='bring_color_weighted' to test whether the "
            "substrate-pure δ = Δm/M_N at q_0 closes the 15% "
            "single-magic A=3 p/n asymmetry. Per the audit "
            "docs/audits/2026-05-31-binding-magic-A-wireup.md."
        ),
        "computation": (
            "closed_form_ratio(Z, N, q_0, pn_convention) compared across "
            "'strict_averaged' and 'bring_color_weighted'; f required to "
            "close B_endo to B_AME under each."
        ),
        "generator": "computations/binding_bring_enhancement_compare.py",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "q_0_50dps": Q_50_DIGIT_STR,
            "m_e_MeV": fmt(M_E_MEV),
            "delta_flavor_split_leading": fmt(delta),
            "vol_borromean_8G": fmt(vol_b3),
            "AME": {k: fmt(v) for k, v in AME.items()},
        },
        "predictions": rows,
        "f_spread_summary": summary,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out",
        # Script-relative via the HERE this file already defines: the old
        # cwd-relative default wrote to computations/computations/… when run
        # from inside computations/.
        default=str(HERE / "binding-bring-enhancement-compare.witness.json"),
    )
    ap.add_argument("--print", action="store_true")
    args = ap.parse_args()

    witness = build_witness()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out_path.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"witness emitted: {out_path}")
    if args.print:
        print()
        # float() below is display-only; see the note on the witness fields.
        _d = float(mp.mpf(witness["inputs"]["delta_flavor_split_leading"]))
        print(f"  δ = Δm/M_N = {_d:.6e}")
        print()
        hdr = f"  {'atom':>4} {'arc-comp':<10} {'τ_M strict':>11} {'τ_M Bring':>11} {'Δ (ppm)':>9} {'f strict':>10} {'f Bring':>10}"
        print(hdr)
        for r in witness["predictions"]:
            comp = "pn" if r["Z"] == r["N"] == 1 else (
                "pn,nn" if r["atom"] == "T" else
                "pp,pn" if r["atom"] == "³He" else
                "pp,pn,nn"
            )
            print(
                f"  {r['atom']:>4} {comp:<10} "
                f"{float(mp.mpf(r['tau_M_ratio_strict'])):>11.6f} "
                f"{float(mp.mpf(r['tau_M_ratio_bring'])):>11.6f} "
                f"{float(mp.mpf(r['tau_M_ratio_delta_ppm'])):>9.2f} "
                f"{float(mp.mpf(r['f_required_strict'])):>10.4f} "f"{float(mp.mpf(r['f_required_bring'])):>10.4f}"
            )
        print()
        print("  " + witness["f_spread_summary"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
