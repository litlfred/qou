#!/usr/bin/env python3
"""binding_bring_enhancement_compare — does Bring color-tube weighting
close the 15% T vs ³He f-factor spread?

Re-runs the binding-shell-enhancement analysis at q_0 with
`pn_convention="bring_color_weighted"` and compares to
`pn_convention="strict_averaged"` (the historical baseline used by
`binding_shell_enhancement_derivation.py`). The Bring weighting uses
the substrate-pure formula

    f_pn = z - h · (1/2 - δ/4),   δ = Δm_{n-p}/M_N ≈ 1.37e-3
                                   (`_li_2_q_util.flavor_split_subleading`,
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

from _li_2_q_util import flavor_split_subleading  # noqa: E402
from closed_form_tau_M import closed_form_ratio  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


# AME2020 binding energies (MeV)
AME = {
    "D":   2.224566,
    "T":   8.481798,
    "³He": 7.718058,
    "⁴He": 28.295674,
}


def build_witness() -> dict:
    mp.mp.dps = 50
    q = mp.mpf(Q_50_DIGIT_STR)
    delta = flavor_split_subleading(q)

    # Vol(𝓑₃) = 8G (Catalan)
    vol_b3 = 8 * mp.catalan

    rows: list[dict] = []
    for label, Z, N in [("D", 1, 1), ("T", 1, 2), ("³He", 2, 1), ("⁴He", 2, 2)]:
        r_strict = closed_form_ratio(Z, N, q, pn_convention="strict_averaged")
        r_bring = closed_form_ratio(Z, N, q, pn_convention="bring_color_weighted")

        # Naive B_endo at q_0 using closed_form_ratio as a proxy for
        # |tr_M(free)| − |tr_M(atom)| ↦ ratio (rough; the actual
        # binding_canonical mass-formula path is more involved, but
        # the RELATIVE Bring-vs-strict difference is the structural
        # quantity we want here).
        b_endo_strict = float(M_E_MEV * vol_b3 * (1 - r_strict))
        b_endo_bring = float(M_E_MEV * vol_b3 * (1 - r_bring))

        b_exp = AME[label]
        f_strict = b_exp / b_endo_strict if b_endo_strict != 0 else float("nan")
        f_bring = b_exp / b_endo_bring if b_endo_bring != 0 else float("nan")

        rows.append({
            "atom": label,
            "Z": Z,
            "N": N,
            "tau_M_ratio_strict": float(r_strict),
            "tau_M_ratio_bring": float(r_bring),
            "tau_M_ratio_delta_ppm": float((r_bring - r_strict) / r_strict * 1e6),
            "B_endo_strict_MeV": b_endo_strict,
            "B_endo_bring_MeV": b_endo_bring,
            "B_AME_MeV": b_exp,
            "f_required_strict": f_strict,
            "f_required_bring": f_bring,
        })

    # T vs ³He f-spread (the open question)
    t_row = next(r for r in rows if r["atom"] == "T")
    he3_row = next(r for r in rows if r["atom"] == "³He")
    f_spread_strict = abs(t_row["f_required_strict"] - he3_row["f_required_strict"]) \
        / max(t_row["f_required_strict"], he3_row["f_required_strict"])
    f_spread_bring = abs(t_row["f_required_bring"] - he3_row["f_required_bring"]) \
        / max(t_row["f_required_bring"], he3_row["f_required_bring"])

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
            "m_e_MeV": float(M_E_MEV),
            "delta_flavor_split_subleading": float(delta),
            "vol_borromean_8G": float(vol_b3),
            "AME": AME,
        },
        "predictions": rows,
        "f_spread_summary": summary,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out",
        default="computations/binding-bring-enhancement-compare.witness.json",
    )
    ap.add_argument("--print", action="store_true")
    args = ap.parse_args()

    witness = build_witness()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"witness emitted: {out_path}")
    if args.print:
        print()
        print(f"  δ = Δm/M_N = {witness['inputs']['delta_flavor_split_subleading']:.6e}")
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
                f"  {r['atom']:>4} {comp:<10} {r['tau_M_ratio_strict']:>11.6f} "
                f"{r['tau_M_ratio_bring']:>11.6f} {r['tau_M_ratio_delta_ppm']:>9.2f} "
                f"{r['f_required_strict']:>10.4f} {r['f_required_bring']:>10.4f}"
            )
        print()
        print("  " + witness["f_spread_summary"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
