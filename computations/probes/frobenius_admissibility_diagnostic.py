#!/usr/bin/env python3
"""Frobenius-admissibility failure diagnostic for the knot-assignment SDP.

Bean qou-vd7j. `all_nuclides_sdp_admissibility.py` reports 0/3558 nuclei feasible
under the Frobenius per-nucleus test (vs 2221/3558 for the weak scalar LP). This
diagnostic reports WHY, per nucleus, turning "0/3558" into a structural cause.

The Frobenius LP (pyhecke.lp_dual_solver.solve_frobenius_dual_lp) is:
    min t·x   s.t.  1ᵀx = A  (net)   AND   G x = nf  (Frobenius demand)
i.e. **7 equality constraints (1 net + 6 Frobenius) on 6 unknowns** — over-
determined by one. Since G (the H_3 NF Gram) is invertible (rank 6, though
indefinite: 1 neg-norm block), `G x = nf` already fixes x = G⁻¹nf uniquely, so
its implied net is `1ᵀG⁻¹nf`. Feasibility therefore requires the *consistency*
`1ᵀG⁻¹nf = A` — which FAILS for every nucleus (the categorical-NF implied net is
O(1), not the mass number A). That inconsistency, not any deep obstruction, is
the 0/3558.

FINDING (honest, scope-limited): the Frobenius admissibility test as posed is
over-determined by an inconsistent net row. For light nuclei nf ∈ range(G)
(residual ~1e-15) ⇒ dropping/reconciling the net constraint would make the
Frobenius demand feasible. Heavy nuclei (A≳50) instead hit the known f64
`build_atom_nf` overflow (needs mpfr). This does NOT by itself derive ν_SDP — it
reframes the 0/3558 as a test-formulation artifact and points the fix at the net
normalization, not at the Gram/knot machinery.

Requires: pyhecke (+ deps numpy). Run with PYTHONPATH including tools/pyhecke/python.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

_ROOT = Path(__file__).resolve().parents[2]
# `computations/substrate` was missing from this list, so the module-level
# `pyhecke` import below succeeded and anything reaching for `q_parameter`
# then died with `No module named 'q_parameter'` -- a path gap that reads as
# a missing dependency. Bean `qou/ti1n`.
for p in ("tools/pyhecke/python", "tools/qou-substrate/python",
          "computations/substrate"):
    sys.path.insert(0, str(_ROOT / p))

from pyhecke import gram, atom  # noqa: E402

SAMPLE = [(1, 0, "p"), (0, 1, "n"), (1, 1, "2H"), (1, 2, "3H"),
          (2, 1, "3He"), (2, 2, "4He"), (6, 6, "12C"), (26, 30, "56Fe")]


def main() -> int:
    G = np.asarray(gram.gram_matrix(), dtype=float)
    t = np.asarray(gram.TR_M, dtype=float)
    w = np.linalg.eigvalsh(G)
    print("NF basis:", list(gram.NF_NAMES))
    print(f"Gram eigenvalues: {np.round(w, 5)}  rank {np.linalg.matrix_rank(G)}"
          f"  #neg-norm blocks {int((w < -1e-9).sum())}")
    print(f"\n{'nucleus':8}{'A':>3}  {'nf∈range(G) resid':>18}  "
          f"{'1ᵀG⁻¹nf':>10}  {'net gap (−A)':>12}  reason")
    for Z, N, lab in SAMPLE:
        A = Z + N
        try:
            nf = np.asarray(atom.build_atom_nf(Z, N), dtype=float)
        except Exception as e:  # noqa: BLE001
            print(f"{lab:8}{A:>3}  build fail: {e}"); continue
        if not np.all(np.isfinite(nf)):
            print(f"{lab:8}{A:>3}  {'—':>18}  {'—':>10}  {'—':>12}  "
                  f"f64 build_atom_nf OVERFLOW (needs mpfr)")
            continue
        x, _, _, _ = np.linalg.lstsq(G, nf, rcond=None)
        rG = float(np.linalg.norm(G @ x - nf))
        net = float(np.ones(len(t)) @ x)
        gap = net - A
        if rG > 1e-6:
            reason = "nf OUTSIDE range(G)"
        elif abs(gap) > 1e-6:
            reason = "OVERDETERMINED (net 1ᵀx=A vs Gx=nf inconsistent)"
        else:
            reason = "FEASIBLE"
        print(f"{lab:8}{A:>3}  {rG:>18.2e}  {net:>10.4f}  {gap:>12.4f}  {reason}")
    print("\nCause: 7 equalities (1 net + 6 Frobenius) on 6 unknowns; Gx=nf fixes "
          "x, its implied net 1ᵀG⁻¹nf (O(1)) != mass number A. The 0/3558 is this "
          "over-determination, not a Gram/knot obstruction. Fix targets the net "
          "normalization. Does NOT derive ν_SDP.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
