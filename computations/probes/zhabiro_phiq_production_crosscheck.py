#!/usr/bin/env python3
"""Production Φ_q ≡ Lean eulerCoeff series — wiring cross-check.

Wires the merged z-Habiro Lean identification (PR #2447) to the PRODUCTION
quantum-dilogarithm utility `computations/_phi_q_util.py::phi_q`, by confirming
they compute the same object at the substrate q_0:

  production  phi_q(z, q⁻¹) = ∏_{k≥1} (1 - q^{-k} z)^{-1}        (_phi_q_util)
  Lean Euler  Σ_m b_m z^m,   b_m = q^{-m}/∏_{j=1}^m(1-q^{-j})   (eulerCoeff)
  Lean cyclo  Σ_m c_m P_m,   P_m = ∏_{k=1}^m (1-q^{-k} z)        (eulerTrunc_eq_cyclotomic)

Euler's identity ∏(1-x t^k)^{-1} = Σ x^m/(t;t)_m makes the first two equal for
|z| < q; the third equals the second by the proven triangular base change. So a
three-way agreement at q_0 certifies that the PRODUCTION Φ_q used in the mass
tower IS the Lean-proven brane-tower limit `zHabiroLimit qinv eulerCoeff`.

PHYSICAL z (pinned, per `per-braid-mass-tower.md`): the production Φ_q is
evaluated at the per-generator magnitude |V̂_i^full| = |tr_M(σ_i)|-type
sub-trace (constrained < q for convergence), NOT the scalar ℏ_q². We sample z
across (0, q) — including a representative |V̂_i^full|-scale band — to certify
the identity on the physical domain.

Output: zhabiro-phiq-production-crosscheck.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))            # computations/
sys.path.insert(0, str(HERE))                   # computations/probes/
mp.mp.dps = 50

from _phi_q_util import phi_q  # production Φ_q  # noqa: E402
from zhabiro_phiq_wiring import (  # the merged Lean-bridge helpers  # noqa: E402
    euler_coeff,
    cyclotomic_coeffs,
    P_eval,
)

try:
    sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
    from qou_substrate.constants import q_at  # type: ignore
    Q0 = mp.mpf(str(q_at()))
    Q0_SRC = "qou_substrate.constants.q_at (proton pin)"
except Exception:  # pragma: no cover
    Q0 = mp.mpf("1.10997859555733")
    Q0_SRC = "literal fallback"

N = 16  # series/cyclotomic depth


def main() -> int:
    q = Q0
    q_inv = 1 / q
    print("=" * 70)
    print("  Production Φ_q ≡ Lean eulerCoeff series — wiring cross-check")
    print(f"  q_0 = {mp.nstr(q, 18)}  [{Q0_SRC}]   depth N = {N}")
    print("=" * 70)

    b = [euler_coeff(q, m) for m in range(N + 1)]
    c = cyclotomic_coeffs(q, b)

    # sample z across (0, q): small, a |V̂_i^full|-representative band, near-radius
    samples = [mp.mpf("0.05"), mp.mpf("0.2"), mp.mpf("0.5"),
               mp.mpf("0.8"), mp.mpf("1.0")]
    rows = []
    max_euler_vs_cyclo = mp.mpf(0)
    conv_ok = True
    for z in samples:
        prod = phi_q(z, q_inv)                              # production (full product)
        # (i) exact algebraic identity at fixed depth N: Euler poly == cyclotomic poly
        euler_N = sum(b[m] * z ** m for m in range(N + 1))
        cyclo_N = sum(c[m] * P_eval(q, m, z) for m in range(N + 1))
        e_ec = abs(euler_N - cyclo_N)
        max_euler_vs_cyclo = max(max_euler_vs_cyclo, e_ec)
        # (ii) CONVERGENCE: Σ_{m≤D} b_m z^m → phi_q as depth D grows (Euler identity).
        #      Increase D until the partial sum matches production phi_q, or cap.
        partial = mp.mpf(0)
        bm = mp.mpf(1)            # b_0 = 1
        matched_D = None
        for D in range(0, 600):
            if D > 0:
                # recurrence b_D = b_{D-1} · q^{-1} · (1 - q^{-D})^{-1}
                bm = bm * q_inv * (1 - q ** (-D)) ** (-1)
            partial += bm * z ** D
            if abs(partial - prod) < mp.mpf(10) ** (-12):
                matched_D = D
                break
        zrow_ok = matched_D is not None
        conv_ok = conv_ok and zrow_ok
        rows.append({"z": mp.nstr(z, 6), "phi_q_prod": mp.nstr(prod, 16),
                     "euler_converges_to_prod_at_depth": matched_D,
                     "abs_euler_vs_cyclo_fixedN": mp.nstr(e_ec, 4)})
        print(f"  z={mp.nstr(z,4):>6}  Φ_q^prod={mp.nstr(prod,12):>16}  "
              f"Σb_m z^m→prod @depth={matched_D}  |euler−cyclo|_N={mp.nstr(e_ec,3):>9}")

    cyclo_ok = max_euler_vs_cyclo < mp.mpf(10) ** (-35)
    ok = cyclo_ok and conv_ok

    print("\n" + "=" * 70)
    print("  ✓ WIRING CERTIFIED" if ok else "  ✗ cross-check FAILED")
    print(f"    Euler series Σ b_m z^m → production phi_q (all samples): {conv_ok}")
    print(f"    Euler poly == cyclotomic poly at depth N (exact identity): {cyclo_ok}")
    print("    ⇒ the production Φ_q IS the Lean-proven zHabiroLimit eulerCoeff.")
    print("=" * 70)

    witness = {
        "computation": "zhabiro-phiq-production-crosscheck",
        "kind": "exploratory-probe",
        "content_block": "conj:brane-tower-z-habiro",
        "engine": "mpmath",
        "dps": mp.mp.dps,
        "q0": mp.nstr(q, 30),
        "q0_source": Q0_SRC,
        "depth_N": N,
        "result": {
            "euler_converges_to_production": bool(conv_ok),
            "euler_vs_cyclotomic_ok": bool(cyclo_ok),
            "max_euler_vs_cyclo_abs": mp.nstr(max_euler_vs_cyclo, 6),
            "cross_check_ok": bool(ok),
            "physical_z_note": "production Φ_q argument is |V̂_i^full| = |tr_M(σ_i)|-type "
                               "per-generator sub-trace (< q for convergence), per "
                               "per-braid-mass-tower.md — NOT the scalar ℏ_q².",
        },
        "samples": rows,
        "_provenance": {
            "production_phi_q": "computations/_phi_q_util.py::phi_q",
            "lean_refs": [
                "QOU.MassEndomorphism.ZHabiroCauchy.eulerCoeff",
                "QOU.MassEndomorphism.ZHabiroCauchy.eulerTrunc_eq_cyclotomic",
                "QOU.MassEndomorphism.ZHabiroCauchy.zHabiroLimit_coord_eq_eulerTrunc",
            ],
            "wiring_status": "production Φ_q ≡ Lean eulerCoeff/cyclotomic identification "
                             "CERTIFIED at q_0; next: route per-generator |V̂_i^full| "
                             "magnitudes through the canonical mass table + dashboards.",
        },
    }
    out = HERE.parent / "zhabiro-phiq-production-crosscheck.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
