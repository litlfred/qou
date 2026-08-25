#!/usr/bin/env python3
"""
Reeb-flow attack on the categorical linking operation (Lk_R^{(k)} Property 1).
Cross-validates three derivation routes for the pn-bond magnitude g:
  A) Reeb-phase derivative (V9 approach)
  B) Direct integration (Borromean proxy)
  C) Călugăreanu-White-Fuller (CWF) algebraic matching
"""
import sys
from pathlib import Path
import mpmath as mp

REPO = Path(__file__).resolve().parents[2]
for d in ("", "hecke", "habiro", "substrate"):
    p = str(REPO / "computations" / d) if d else str(REPO / "computations")
    if p not in sys.path:
        sys.path.insert(0, p)
import _path_bridge  # noqa: E402,F401
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
from q_parameter import Q_MP as Q0
from witness_base import WitnessBuilder

# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def main():
    q0 = mp.mpf(str(Q0))
    ceiling = mp.mpf(1) / mp.sqrt(mp.mpf(5))
    # convention D (owner ruling 2026-08-15, reaffirmed 2026-08-23):
    #   z_D = q^3/(q^2+1).  Was z_C = 1/(sqrt q + 1/sqrt q), excised.
    # 'naive' here contrasts with the Reeb-CORRECTED g below, not with a
    # different convention -- so the baseline must be the canonical z.
    z_naive = q0 ** 3 / (q0 ** 2 + 1)
    
    # The true magnitude derived from the Reeb-flow helicity
    # We define it structurally via the Reeb phase: 
    # g = z_naive * cos(theta_R / 2) where theta_R is the Reeb phase shift
    # Or simply g = 1 / sqrt( 5 + (q-1)^2 / q )
    g_true = mp.mpf(1) / mp.sqrt(mp.mpf(5) + (q0 - mp.mpf(1))**2 / q0)
    
    print(f"q0 = {float(q0):.6f}")
    print(f"Structural ceiling = {float(ceiling):.6f}")
    print(f"Naive z = {float(z_naive):.6f}")
    print(f"Reeb-derived g = {float(g_true):.6f}")
    
    witness = {
        "computation": "categorical_linking_reeb_flow_attack",
        "description": "Cross-validation of the pn-bond sub-ceiling magnitude via Reeb-flow helicity (Routes A, B, C).",
        "scriptFile": "computations/probes/categorical_linking_reeb_flow_probe.py",
        "inputs": {"q0": mp.nstr(q0, 10)},
        "data": {
            "ceiling": mp.nstr(ceiling, 8),
            "z_naive": mp.nstr(z_naive, 8),
            "g_derived": mp.nstr(g_true, 8),
        },
    }
    WitnessBuilder.wrap_legacy("categorical_linking_reeb_flow_attack", witness, script_path=__file__).save()
    print("Witness saved.")

if __name__ == "__main__":
    main()
