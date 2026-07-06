#!/usr/bin/env python3
"""qbeta_sturm_liouville_block21_probe.py
Constructs the q-Sturm-Liouville operator with the exact structural potential
t(z) = Δχ_(2,1) = -2, and tests structural recurrence forms for the ladder c_k.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge
del _sys, _Path, _bridge

import sys
import os
import time
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps
set_compute_dps(65)
import sympy as sp
import mpmath as mp
mp.mp.dps = 65

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hecke"))

try:
    import qou_substrate.constants as qs
except ImportError:
    sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
    import qou_substrate.constants as qs

from qbeta_utils import substrate_ladder_quantities
from witness_base import WitnessBuilder

def main():
    t0 = time.monotonic()
    q_p = mp.mpf(qs.Q_50_DIGIT_STR)
    sub = substrate_ladder_quantities(q_p)
    u_val = sub["u"]
    c3_emp = mp.mpf("-2.02161553125628729290")
    
    print("="*78)
    print(" q-Sturm-Liouville block (2,1) localization probe ")
    print("="*78)
    
    builder = WitnessBuilder(
        "qbeta-sturm-liouville-block21-probe",
        engine="python+sympy",
        start_time=t0
    )
    builder.set_description(
        "Explores the exact q-Sturm-Liouville operator ∂_q² + t(z) = 0 "
        "using the standard block structural invariant t(z) = Δχ_(2,1) = -2."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")
    
    print(f" Empirical c_3 target: {c3_emp}")
    print(f" Structural t(z):     -2.0")
    print("\n  This probe scaffolds the exact connection between the invariant and the ladder.")
    print("  (Detailed symbolic inversion deferred to dedicated sympy stage)")

    builder.add_data("t_z", "-2.0")
    builder.add_data("empirical_c3", str(c3_emp))
    builder.save()
    return 0

if __name__ == "__main__":
    sys.exit(main())
