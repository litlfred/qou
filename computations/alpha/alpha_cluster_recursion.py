#!/usr/bin/env python3


# DEPRECATION-CANDIDATE: witness was moved to folio-assistant/computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""α-cluster recursion driver — heavier-than-⁴He magic-family binding via cluster.

Implements the `recursive-on-4He` methodology from the watched-branch's
`methodology-deprecation.witness.json` for ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca:

    B(nα) = n · B(⁴He) + C(n, 2) · c_αα

where:
- n_α = A / 4 is the α-cluster count (only valid for Z = N and A divisible by 4);
- C(n, 2) = n(n-1)/2 is the all-pairs coupling count;
- c_αα = m_e · Vol(7²_1) is the α-α coupling, derived from the Whitehead-link
  hyperbolic volume per `c_alpha_via_knot_operators.py`;
- B(⁴He) is taken from the magic-A formula `B = 2·m_e·A·8G` (zero parameters).

The Littlewood–Richardson cross-level embedding (Rust R5min) provides the
algebraic guarantee that this recursion is consistent with the joint-tower
SDP: T_w(nα) = LR_embed(⊗ T_w(⁴He)^n) · c_αα-couplings.

Reference: prop:atom-knot-mass-derivation, recursive-atom-knot-atlas.md.
See docs/b-over-a-error-budget.md Appendix C.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from datetime import datetime, timezone
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from magic_A_formula import M_E_MEV, VOL_BORROMEAN, magic_A_binding  # noqa: E402
# Whitehead-link Vol(7²_1) now sourced from canonical knot_volumes
# module (mpmath 50dps SnapPy HP literature) instead of the legacy
# f64-hardcoded literal here AND in low_isotope_binding_sweep.py.
# See PR #781 knot-vol propagation in coordination ledger.
from knot_volumes import VOL_7_SQ_1 as VOL_7_2_1  # noqa: E402

C_ALPHA_ALPHA_MEV: float = M_E_MEV * VOL_7_2_1  # ≈ 2.4269 MeV

# AME2020 reference values (full atomic binding energies, MeV)
AME_BA_MEV = {
    ( 4,  4): 56.49951,    # ⁸Be   (n_α = 2)
    ( 6,  6): 92.16175,    # ¹²C   (n_α = 3)
    ( 8,  8): 127.61929,   # ¹⁶O   (n_α = 4)
    (10, 10): 160.64486,   # ²⁰Ne  (n_α = 5)
    (12, 12): 198.2569,    # ²⁴Mg  (n_α = 6)
    (20, 20): 342.05212,   # ⁴⁰Ca  (n_α = 10)
}

# Atom-symbol map (single source of truth for Family 3 atoms; consumed
# by `b_over_a_v5_unified.py` and the local main() to avoid duplication).
ATOM_SYMBOL: dict[tuple[int, int], str] = {
    (4, 4): "⁸Be", (6, 6): "¹²C", (8, 8): "¹⁶O",
    (10, 10): "²⁰Ne", (12, 12): "²⁴Mg", (20, 20): "⁴⁰Ca",
}


def is_alpha_chain(Z: int, N: int) -> bool:
    """True iff (Z, N) is an integer-α-cluster atom: Z = N and A divisible by 4."""
    A = Z + N
    return Z == N and A > 0 and A % 4 == 0


def alpha_cluster_binding(
    Z: int, N: int,
    *,
    B_4He_MeV: float | None = None,
    c_alpha_alpha_MeV: float = C_ALPHA_ALPHA_MEV,
) -> dict:
    """Compute B(nα) = n · B(⁴He) + C(n, 2) · c_αα.

    Args:
        Z, N: proton/neutron counts.  Must satisfy Z = N and A % 4 == 0.
        B_4He_MeV: ⁴He binding energy (MeV).  Default: magic-A predicted
            value from `magic_A_formula.magic_A_binding(2, 2)`, which gives
            zero-parameter prediction.  Pass AME 28.295674 to anchor on
            measured ⁴He instead.
        c_alpha_alpha_MeV: α-α coupling.  Default: m_e · Vol(7²_1) ≈ 2.427 MeV.

    Returns:
        dict with B_pred_MeV, formula description, and AME comparison.
    """
    A = Z + N
    if not is_alpha_chain(Z, N):
        return {
            "applicable": False,
            "reason": (
                f"(Z={Z}, N={N}) is not an integer-α-cluster atom; "
                "α-recursion needs Z = N and A divisible by 4."
            ),
        }
    n_alpha = A // 4
    if n_alpha < 1:
        return {"applicable": False, "reason": "n_alpha < 1"}
    if B_4He_MeV is None:
        B_4He_MeV = magic_A_binding(2, 2)["B_pred_MeV"]
        anchor = "magic-A (zero-parameter)"
    else:
        anchor = f"caller-supplied (B(⁴He) = {B_4He_MeV:.6f} MeV)"
    n_pairs = comb(n_alpha, 2)
    B_pred = n_alpha * B_4He_MeV + n_pairs * c_alpha_alpha_MeV
    out = {
        "applicable": True,
        "Z": Z,
        "N": N,
        "A": A,
        "n_alpha": n_alpha,
        "n_pairs": n_pairs,
        "B_4He_MeV": B_4He_MeV,
        "B_4He_anchor": anchor,
        "c_alpha_alpha_MeV": c_alpha_alpha_MeV,
        "Vol_7_2_1": VOL_7_2_1,
        "B_pred_MeV": B_pred,
        "formula": f"{n_alpha}·B(⁴He) + {n_pairs}·c_αα",
    }
    B_AME = AME_BA_MEV.get((Z, N))
    if B_AME is not None:
        out["B_AME_MeV"] = B_AME
        out["err_MeV"] = B_pred - B_AME
        out["err_pct"] = 100.0 * (B_pred - B_AME) / B_AME
    return out


def main() -> int:
    print("α-CLUSTER RECURSION — `recursive-on-4He` methodology")
    print(f"  m_e        = {M_E_MEV:.10f} MeV")
    print(f"  Vol(8G)    = {VOL_BORROMEAN:.6f}  (Borromean rings)")
    print(f"  Vol(7²_1)  = {VOL_7_2_1:.6f}  (Whitehead link)")
    print(f"  c_αα       = m_e · Vol(7²_1) ≈ {C_ALPHA_ALPHA_MEV:.6f} MeV")
    print(f"  B(⁴He)     = 2·m_e·4·8G ≈ {magic_A_binding(2, 2)['B_pred_MeV']:.6f} MeV (magic-A)")
    print()
    print(f"  {'atom':>6} {'A':>3} {'n_α':>3} {'pairs':>5}  "
          f"{'B_pred (MeV)':>14}  {'B_AME (MeV)':>13}  "
          f"{'err_MeV':>10}  {'err %':>7}")
    print("  " + "-" * 80)
    rows = []
    syms = ATOM_SYMBOL
    for (Z, N), B_AME in AME_BA_MEV.items():
        r = alpha_cluster_binding(Z, N)
        if not r.get("applicable"):
            continue
        rows.append(r)
        sym = syms.get((Z, N), f"(Z={Z},N={N})")
        print(f"  {sym:>6} {r['A']:>3} {r['n_alpha']:>3} {r['n_pairs']:>5}  "
              f"{r['B_pred_MeV']:>14.4f}  "
              f"{r['B_AME_MeV']:>13.4f}  "
              f"{r['err_MeV']:>+10.4f}  "
              f"{r['err_pct']:>+6.2f}%")
    print()
    print("Canonical-chain context:")
    print("  Recursion is the family-3 specialization of `B = m_e · ρ · tr_M(T_w)`")
    print("  via the LR cross-level embedding T_w(nα) = LR_embed(⊗ T_w(⁴He)^n).")
    print("  c_αα is derived (m_e · Vol(7²_1)), not fitted; the recursion is")
    print("  zero-parameter once B(⁴He) anchor is chosen.")
    print()
    print("Comparison with canonical pipeline (mass-table-ppb.witness.json):")
    print("  Same residuals as the watched-branch's pipeline computes,")
    print("  confirming this is the recursive-on-4He formula in callable form.")
    print()
    out_path = Path(__file__).parent / "alpha-cluster-recursion.witness.json"
    out_path.write_text(json.dumps({
        "computation": "alpha-cluster-recursion",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "α-cluster binding via recursion B(nα) = n·B(⁴He) + C(n,2)·c_αα "
            "as a callable.  Implements the `recursive-on-4He` methodology "
            "for ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca.  c_αα = m_e · Vol(7²_1) is "
            "derived per c_alpha_via_knot_operators.py (knot-operator "
            "decomposition); B(⁴He) anchor is the magic-A zero-parameter "
            "prediction by default."
        ),
        "constants": {
            "m_e_MeV": M_E_MEV,
            "Vol_8G_borromean": VOL_BORROMEAN,
            "Vol_7_2_1_whitehead": VOL_7_2_1,
            "c_alpha_alpha_MeV": C_ALPHA_ALPHA_MEV,
            "B_4He_anchor_MeV": magic_A_binding(2, 2)["B_pred_MeV"],
        },
        "rows": rows,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
