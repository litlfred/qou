#!/usr/bin/env python3
"""Radial Vol·ρ binding-handle mirror test (front 1 of the C_knot attack menu).

After PR #4556 refuted a single-universal C_knot and PR #4592 refuted the (angular) eigenphase route,
the surviving compass is that the missing binding scale must be RADIAL/dimensionful. The mass formula
runs on `m = m_e·Vol(K)·ρ(K)/ℏ_q²`, but the binding formula `B = m_e·|S(K)|` carries NO such geometric
dressing — so the deficit `C_knot = B_AME/(m_e·|S(K)|)` might BE that missing `Vol·ρ/ℏ_q²` factor.

DECISIVE CHEAP TEST (0-fit, no free parameters, B_AME enters only as the fixed C_knot value from #4556):
Tritium (³H = 1p2n) and ³He (2p1n) are **mirror nuclei** (p↔n swap). If they are ALSO mirror knots —
equal hyperbolic volume `Vol(T)=Vol(³He)` — then the radial hypothesis `C_knot = Vol·ρ/ℏ_q²` forces

        C_knot(T) / C_knot(³He)  =  ρ(T) / ρ(³He)                       (Vol and ℏ_q² cancel),

with the paper-canonical per-block density `ρ(K) = tr_M(K) = Σ_λ y_λ χ^λ(β_K)` (`density_per_block`,
mass_vol_density.py). Both sides are DERIVED numbers — no fit. The probe computes them from the
committed per-partition χ witnesses and reports the ratio-of-ratios (= 1 iff the ansatz holds).

RESULT (see audit): the two ratios land on OPPOSITE sides of unity — `C_knot(T)/C_knot(³He) ≈ 1.35`
(T more bound) but `ρ(T)/ρ(³He) ≈ 0.50` (T smaller trace). So `ρ = tr_M` is ANTI-correlated with
C_knot across the mirror pair; the natural radial ansatz fails in DIRECTION, not merely magnitude.

Scope: **scope-(a)** — this specific ansatz (`ρ = tr_M`, `Vol(T)=Vol(³He)`) is refuted. It does NOT
refute the radial handle in general: the survivors are (i) a density `ρ ≠ tr_M`, or (ii) genuinely
distinct volumes `Vol(T) ≠ Vol(³He)` (the two braids differ — `tr_M(T) ≠ tr_M(³He)` — so mirror-knot
equality is an assumption, not established). Next step is `Vol(T)`, `Vol(³He)` from the actual braid
closures. No fit; nothing wired; `free_parameters = 0`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COMP = REPO / "computations"

# C_knot from PR #4556 (on main), master-formula convention, 0-fit.
C_KNOT = {"T": 4.444, "3He": 3.292}

WIT = {
    "T": COMP / "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": COMP / "chi-helium-3-h9-at-q0-50dps.witness.json",
}


def tr_M(path: Path) -> float:
    """ρ_per_block(K) = tr_M(K) = Σ_λ y_λ χ^λ (density_per_block)."""
    doc = json.load(open(path))
    bp = doc.get("by_partition") or doc.get("data", {}).get("by_partition") or []
    return sum(float(e["y_lambda"]) * float(e.get("chi_lambda", e.get("chi"))) for e in bp)


def main() -> int:
    rho = {k: tr_M(p) for k, p in WIT.items()}
    c_ratio = C_KNOT["T"] / C_KNOT["3He"]
    rho_ratio = rho["T"] / rho["3He"]
    ror = c_ratio / rho_ratio

    print("Mirror test — radial hypothesis C_knot = Vol·ρ/ℏ_q² (assuming Vol(T)=Vol(³He)):")
    print(f"  ρ(T)=tr_M(T)   = {rho['T']:+.6f}")
    print(f"  ρ(³He)=tr_M    = {rho['3He']:+.6f}")
    print(f"  C_knot(T)/C_knot(³He) = {c_ratio:.4f}   (T more bound; > 1)")
    print(f"  ρ(T)/ρ(³He)           = {rho_ratio:.4f}   (T smaller trace; < 1)")
    print(f"  ratio-of-ratios       = {ror:.4f}   (= 1 iff ansatz holds)")
    anti = (c_ratio - 1.0) * (rho_ratio - 1.0) < 0
    print(f"\n  anti-correlated across the mirror pair (opposite sides of 1): {anti}")
    print("  VERDICT: ρ=tr_M radial ansatz REFUTED in direction (scope-a). The radial handle")
    print("  survives only if ρ≠tr_M or Vol(T)≠Vol(³He). No fit; free_parameters=0.")

    out = COMP / "deltalambda" / "radial-volrho-mirror-test.witness.json"
    # Provenance stamp (bean qou-f1rs): the witness dict was built
    # INLINE at the write below, so there was nothing to stamp. It
    # is bound to a name here so this producer records which script
    # wrote it -- a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    _prov_payload = {
        "description": "Radial Vol·ρ mirror test (front 1): C_knot=Vol·ρ/ℏ_q² with ρ=tr_M and "
                       "Vol(T)=Vol(³He) is refuted in DIRECTION — C_knot ratio 1.35 (>1) vs tr_M "
                       "ratio 0.50 (<1), anti-correlated. scope-(a). Survivors: ρ≠tr_M or "
                       "Vol(T)≠Vol(³He). bean qou-0g4z / front-1.",
        "free_parameters": 0,
        "c_knot_ratio_T_over_3He": c_ratio,
        "rho_trM_ratio_T_over_3He": rho_ratio,
        "ratio_of_ratios": ror,
        "anti_correlated": anti,
        "verdict": "rho-eq-trM-radial-ansatz-refuted-in-direction",
    }
    _prov_payload.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        _prov_payload, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(_prov_payload, indent=2) + "\n")
    print(f"\nwitness -> {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
