#!/usr/bin/env python3
"""dg_torsion_binding_ratio_a3_probe.py — does the canonical DG 1-loop torsion
ratio beat the volume ratio for the A=3 binding mirror pair (³H vs ³He)?

Bean qou-985x (extended-Bloch tetrahedron term), PR #4824. Audit:
`docs/audits/2026-08-08-extended-bloch-tetrahedron-scoping-trefoil-trap.md` §7.

CONTEXT.  The extended-Bloch route's appeal is that Neumann's flattening makes
the DG 1-loop invariant canonical (the shape-unit ambiguity is fixed by the
gluing/parity equations; `one_loop_ambiguity_group_probe.py`). The §2 volume
ratio Vol(8₁₁)/Vol(L6a4)=1.1308 already sits +2.9% off B(³H)/B(³He)=1.0990.
This probe asks the honest follow-up: does the *torsion* object the flattening
actually canonicalises do any better than the volume?

METHOD.  Reuse `whitehead_c_sigma_torsion.one_loop_torsion` — |det J| of the
NZ gluing-equation Jacobian on SnapPy's geometric triangulation, at high dps.
Zero free parameters: the overall constant cancels in the ratio. The A=3
binding carriers are the corpus-canonical SDP links (T→8₁₁, ³He→L6a4=Borromean;
`binding_link_volumes.py`).

CALIBRATION (non-circular).  4₁ → |det J| = √3, the classically-known adjoint
Reidemeister torsion (trace field Q(√−3)); L6a4 → 64 (corpus).

CAVEAT.  |det J| is triangulation-*representative*, not yet the fully
retriangulation-invariant flattened value (the flattening-monomial repair is
the open qou-fl4t item). Values here are on SnapPy's default geometric
triangulation.

RESULT (honest NEGATIVE, scope-a).  τ_DG(8₁₁)/τ_DG(L6a4) = 1.1347 (+3.2% vs the
binding ratio) — essentially identical to the volume ratio (+2.9%). The
canonical torsion does NOT improve the A=3 binding mirror-pair over volume.
No fit; nothing wired to production.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40

HERE = Path(__file__).resolve().parent
COMPUTE = HERE.parent  # computations/

# AME2020 binding energies (MeV) — mirror pair ³H / ³He.
B_3H = mp.mpf("8.481798")
B_3He = mp.mpf("7.718058")

# SnapPy-verified hyperbolic volumes (binding_link_volumes.py).
VOL_8_11 = mp.mpf("8.2863168178")
VOL_L6a4 = mp.mpf("7.32772475342")


def _load_one_loop_torsion():
    src = COMPUTE / "whitehead_c_sigma_torsion.py"
    spec = importlib.util.spec_from_file_location("wct_probe", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.one_loop_torsion


def main() -> None:
    olt = _load_one_loop_torsion()

    tau = {}
    for name in ("4_1", "8_11", "L6a4"):
        val, _det, _z = olt(name)
        tau[name] = val

    # Calibration checks.
    cal_41 = abs(tau["4_1"] - mp.sqrt(3)) < mp.mpf("1e-20")
    cal_L6 = abs(tau["L6a4"] - 64) < mp.mpf("1e-20")

    r_tau = tau["8_11"] / tau["L6a4"]
    r_vol = VOL_8_11 / VOL_L6a4
    r_bind = B_3H / B_3He

    result = {
        "schema": "witness/v1",
        "computation": "dg_torsion_binding_ratio_a3_probe",
        "description": (
            "Canonical DG 1-loop torsion ratio vs volume ratio vs binding "
            "ratio for the A=3 mirror pair (³H→8₁₁, ³He→L6a4). Zero-parameter."
        ),
        "dps": mp.mp.dps,
        "tau_DG": {k: mp.nstr(v, 25) for k, v in tau.items()},
        "calibration": {
            "tau_4_1_eq_sqrt3": bool(cal_41),
            "tau_L6a4_eq_64": bool(cal_L6),
        },
        "ratios": {
            "tau_8_11_over_L6a4": mp.nstr(r_tau, 15),
            "vol_8_11_over_L6a4": mp.nstr(r_vol, 15),
            "binding_3H_over_3He": mp.nstr(r_bind, 15),
        },
        "misses_pct": {
            "tau_ratio_vs_binding": mp.nstr((r_tau - r_bind) / r_bind * 100, 6),
            "vol_ratio_vs_binding": mp.nstr((r_vol - r_bind) / r_bind * 100, 6),
        },
        "verdict": (
            "honest-negative (scope-a): the canonical DG torsion ratio (+3.2%) "
            "is essentially identical to the volume ratio (+2.9%) and does not "
            "improve the A=3 binding mirror-pair. Caveat: |det J| is "
            "triangulation-representative (flattening-monomial repair = qou-fl4t)."
        ),
        "anti_fit": "zero free parameters; overall constant cancels in the ratio",
        "wired_to_production": False,
        "q0_pin": "n/a (topological invariants, q0-independent)",
    }
    print(json.dumps(result, indent=2))

    out = HERE / "dg-torsion-binding-ratio-a3.witness.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nwitness -> {out}")


if __name__ == "__main__":
    main()
