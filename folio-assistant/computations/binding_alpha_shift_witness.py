#!/usr/bin/env python3
"""Binding α_shift candidate cross-check — light nuclei A ∈ {2, 3, 4}.

Numerical cross-check of the Lean instance
[`lightNucleiForceCarrierKnot`](../../content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean#L251)
against experimental binding energies. The §3b-cond instance is
sorry-free at the structural level; this script reports whether the
candidate `(p_A, k_A)` identifications, combined with the deuteron-
pinned dimensionless coupling ρ_0, reproduce experimental B(A) for
A ∈ {3, 4}.

Formula
-------

    B(A) = m_e · ρ_0 · α_shift(T(p_A, k_A))

where:
  m_e        = 0.5109989461 MeV  (CODATA 2018)
  ρ_0        = B(D) / (m_e · α_shift(T(2,3)))   (dimensionless, deuteron-pinned)
  α_shift(T(p, k)) = k · (p - 1)                 (Lean: `bindingAlphaShift`)

Reference:
  - [audit] docs/audits/2026-05-31-binding-alpha-shift-a4-status.md
  - [audit] docs/audits/2026-05-28-binding-endomorphism-analogy.md
  - Lean: content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean

Honest framing: the current candidate identifications were noted in
the file as "agent-survey hypothesis (2026-05-30) suggests p ∈ {2, 3}
with k ≥ 5 for A ≥ 3"; the Phase-3 substrate-uniqueness derivation
remains open. This script's role is to report the numerical gap
truthfully so the next research step is grounded.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


# CODATA 2018
M_E_MEV = 0.5109989461

# Experimental binding energies, AME 2020 / NIST (MeV)
B_EXP_MEV: dict[str, float] = {
    "D":   2.224566,
    "T":   8.481798,
    "³He": 7.718058,
    "⁴He": 28.295674,
}


@dataclass(frozen=True)
class Candidate:
    """A light-nucleus binding force-carrier candidate (mirrors Lean)."""
    A: int
    nucleus: str
    p: int
    k: int

    @property
    def alpha_shift(self) -> int:
        """α_shift(T(p, k)) = k · (p - 1) — `bindingAlphaShift` in Lean."""
        return self.k * (self.p - 1)


# Mirrors `lightNucleusP` / `lightNucleusK` in
# content/quantum-observable-universe/mass-theory/binding-alpha-shift-extension.lean
LIGHT_NUCLEI: list[Candidate] = [
    Candidate(A=2, nucleus="D",   p=2, k=3),
    Candidate(A=3, nucleus="T",   p=2, k=5),
    Candidate(A=3, nucleus="³He", p=2, k=5),
    Candidate(A=4, nucleus="⁴He", p=3, k=4),
]


def pin_rho_0_from_deuteron() -> float:
    """Deuteron-pinned dimensionless ρ_0 := B(D) / (m_e · α_shift(T(2,3)))."""
    d = next(c for c in LIGHT_NUCLEI if c.nucleus == "D")
    return B_EXP_MEV[d.nucleus] / (M_E_MEV * d.alpha_shift)


def predict_binding(c: Candidate, rho_0: float) -> float:
    """B_pred(A) = m_e · ρ_0 · α_shift(T(p_A, k_A))."""
    return M_E_MEV * rho_0 * c.alpha_shift


def build_witness() -> dict:
    rho_0 = pin_rho_0_from_deuteron()
    rows: list[dict] = []
    for c in LIGHT_NUCLEI:
        b_pred = predict_binding(c, rho_0)
        b_exp = B_EXP_MEV[c.nucleus]
        ratio = b_pred / b_exp if b_exp != 0 else float("nan")
        rel_err = (b_pred - b_exp) / b_exp if b_exp != 0 else float("nan")
        rows.append({
            "A": c.A,
            "nucleus": c.nucleus,
            "torus_knot": f"T({c.p},{c.k})",
            "p": c.p,
            "k": c.k,
            "alpha_shift": c.alpha_shift,
            "B_predicted_MeV": round(b_pred, 6),
            "B_experimental_MeV": round(b_exp, 6),
            "ratio_pred_over_exp": round(ratio, 4),
            "relative_error": round(rel_err, 4),
        })
    return {
        "name": "binding-alpha-shift-witness",
        "description": (
            "Numerical cross-check of the light-nuclei "
            "BindingForceCarrierKnot candidates against experimental "
            "B(A). Honest gap report; the candidate identifications "
            "are agent-survey hypotheses, not derived uniqueness "
            "theorems (Phase 3 open math)."
        ),
        "computation": "B(A) = m_e · ρ_0 · α_shift(T(p_A, k_A))",
        "generator": "folio-assistant/computations/binding_alpha_shift_witness.py",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "m_e_MeV": M_E_MEV,
            "m_e_source": "CODATA 2018",
            "B_experimental_source": "AME 2020 / NIST",
            "rho_0_dimensionless": round(rho_0, 6),
            "rho_0_pinned_by": "deuteron (D) at α_shift(T(2,3)) = 3",
        },
        "lean_reference": (
            "content/quantum-observable-universe/mass-theory/"
            "binding-alpha-shift-extension.lean::lightNucleiForceCarrierKnot"
        ),
        "predictions": rows,
        "honest_gap_report": _gap_summary(rows),
    }


def _gap_summary(rows: list[dict]) -> str:
    """One-paragraph honest framing of the gap, computed from the rows."""
    nontrivial = [r for r in rows if r["nucleus"] != "D"]
    if not nontrivial:
        return "Deuteron is the calibration; no out-of-sample comparison."
    worst = max(nontrivial, key=lambda r: abs(r["relative_error"]))
    worst_ratio_pct = 100 * (worst["ratio_pred_over_exp"] - 1)
    summary = (
        f"Deuteron-pinned ρ_0 reproduces B(D) by construction. "
        f"For heavier nuclei the simple proportionality miss is "
        f"substantial: worst case {worst['nucleus']} at "
        f"α_shift = {worst['alpha_shift']} predicts "
        f"{worst['B_predicted_MeV']:.3f} MeV vs experimental "
        f"{worst['B_experimental_MeV']:.3f} MeV "
        f"({worst_ratio_pct:+.0f}% from 1×). "
        f"Consistent with the file's narrative that ρ may not be "
        f"substrate-universal; per-A scaling (or a richer "
        f"force-carrier identification) is needed for A ≥ 3. "
        f"Phase-3 substrate-uniqueness derivation remains open."
    )
    return summary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--out",
        default="folio-assistant/computations/binding-alpha-shift-witness.witness.json",
        help="Witness output path (default: alongside the script).",
    )
    ap.add_argument(
        "--print",
        action="store_true",
        help="Print the predictions table to stdout in addition to writing the witness.",
    )
    args = ap.parse_args()

    witness = build_witness()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"witness emitted: {out_path}")

    if args.print:
        print()
        print(f"  ρ_0 = {witness['inputs']['rho_0_dimensionless']} (deuteron-pinned)")
        print()
        print(f"  {'A':>2} {'nucleus':<5} {'T(p,k)':<8} {'α_shift':>7} "
              f"{'B_pred':>10} {'B_exp':>10} {'pred/exp':>9}")
        for row in witness["predictions"]:
            print(
                f"  {row['A']:>2} {row['nucleus']:<5} {row['torus_knot']:<8} "
                f"{row['alpha_shift']:>7} {row['B_predicted_MeV']:>10.4f} "
                f"{row['B_experimental_MeV']:>10.4f} {row['ratio_pred_over_exp']:>9.4f}"
            )
        print()
        print(f"  {witness['honest_gap_report']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
