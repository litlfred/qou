"""Confirm the operator-selection LP solves on the MPFR backend, not float64.

Moved verbatim out of the `Confirm CI solves at 50 dps, not float64` heredoc
in `.github/workflows/lp-dual-gate.yml` (TOOLS T7, bean `qou-4dj1`) so the
compute-QA runner can call it by name. The code is unchanged; only its home
moved.
"""
import numpy as np
from pyhecke import gram
from pyhecke.lp_dual_solver import solve_operator_selection_lp
t = np.array(gram.TR_M, dtype=float)
G = np.array(gram.gram_matrix(), dtype=float)
d = solve_operator_selection_lp(t, G, 1.0).to_dict()
print(f"backend={d.get('backend')!r} precision_bits={d.get('precision_bits')}")
print(f"primal_obj={d['primal_obj']:.4e}")
assert d.get("backend") == "clarabel-mpfr", (
    f"CI solved with {d.get('backend')!r} — the MPFR binary did not "
    "take effect, so every witness this job could produce would be f64")
assert "y0_star_str" in d, "no full-precision companions in the result"
