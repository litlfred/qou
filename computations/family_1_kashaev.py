#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to folio-assistant/computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""Family-1 binding via Kashaev law — historical knot identifications.

Implements the leading-order family-1 formula from
binding_ladder_catalog.py for atoms with explicit knot Markov closures:

    B(D)   = 1 · m_e · Vol(6_2)        (Vol = 4.40083...)
    B(T)   = 2 · m_e · Vol(8_11)       (Vol = 8.28632...)
    B(³He) = 2 · m_e · Vol(L6a4)       (Vol = 8G = 7.32772...)

This is the post-Archimedean naming of the canonical formula
B = m_e · ρ · tr_M(T_w) at q = q_0, where the volume conjecture
identifies tr_M(T_w) with Vol_hyp(closure) for hyperbolic knot/link
closures (Kashaev 1997, Murakami–Murakami 2001).

The knot identifications for D, T, ³He are `manual-historical-volume-match`
per the watched-branch's methodology audit
(`methodology-deprecation.witness.json`); the GB-NF derivation in
H_{n_0}(q_0) is pending the watched-branch's H_5+ phase 4+ runs.

Reference: prop:atom-knot-mass-derivation, recursive-atom-knot-atlas.md.
See docs/b-over-a-error-budget.md.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Import M_E_MEV + VOL_BORROMEAN (= 8G) from the canonical source to
# avoid duplicated magic values.  The L6a4 = 8G identity is exact
# hyperbolic-geometry; sharing the constant guarantees consistency.
if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))
from magic_A_formula import M_E_MEV, VOL_BORROMEAN  # noqa: E402


# Knot hyperbolic volumes (from SnapPy census; values in
# binding_ladder_catalog.py:48 + d_inter_correction_test.py:57).
# L6a4 (Borromean rings) shared with magic_A_formula via VOL_BORROMEAN.
KNOT_VOL = {
    "6_2":  4.4008325161230461,
    "8_11": 8.28631808635811,
    "L6a4": VOL_BORROMEAN,        # = 8G (Borromean rings)
}


# Per-atom knot identification + structural prefactor ρ_F (in units of m_e).
# Values from binding_ladder_catalog.py:60+.
FAMILY_1_REGISTRY: dict[tuple[int, int], dict] = {
    (1, 1): {
        "symbol": "²H",
        "knot": "6_2",
        "rho_F": 1,
        "method": "manual-historical-volume-match",
    },
    (1, 2): {
        "symbol": "³H",
        "knot": "8_11",
        "rho_F": 2,
        "method": "manual-historical-volume-match",
    },
    (2, 1): {
        "symbol": "³He",
        "knot": "L6a4",
        "rho_F": 2,
        "method": "manual-historical-volume-match",
    },
}


AME_BA_MEV = {
    (1, 1):  2.22452,
    (1, 2):  8.48181,
    (2, 1):  7.71804,
}


def is_family_1_atom(Z: int, N: int) -> bool:
    return (Z, N) in FAMILY_1_REGISTRY


def family_1_binding(Z: int, N: int) -> dict:
    """Compute B = ρ_F · m_e · Vol_hyp(K) for atom (Z, N) using the
    historical knot identification.

    Returns a dict with B_pred_MeV, knot, ρ_F, Vol_hyp, AME comparison
    if available.
    """
    if not is_family_1_atom(Z, N):
        return {
            "applicable": False,
            "reason": (
                f"(Z={Z}, N={N}) not in Family-1 registry "
                "{D, T, ³He}; use family_2 (magic-A) or family_3 (α-cluster)."
            ),
        }
    entry = FAMILY_1_REGISTRY[(Z, N)]
    knot = entry["knot"]
    rho_F = entry["rho_F"]
    Vol_K = KNOT_VOL[knot]
    B_pred = rho_F * M_E_MEV * Vol_K
    out = {
        "applicable": True,
        "Z": Z, "N": N, "A": Z + N,
        "symbol": entry["symbol"],
        "knot": knot,
        "rho_F": rho_F,
        "Vol_hyp": Vol_K,
        "m_e_MeV": M_E_MEV,
        "B_pred_MeV": B_pred,
        "formula": f"{rho_F}·m_e·Vol({knot})",
        "method": entry["method"],
    }
    B_AME = AME_BA_MEV.get((Z, N))
    if B_AME is not None:
        out["B_AME_MeV"] = B_AME
        out["err_MeV"] = B_pred - B_AME
        out["err_pct"] = 100.0 * (B_pred - B_AME) / B_AME
    return out


def main() -> int:
    print("FAMILY-1 KASHAEV LAW — D, T, ³He")
    print(f"  m_e = {M_E_MEV:.10f} MeV")
    print(f"  Knot volumes (SnapPy census):")
    for k, v in KNOT_VOL.items():
        print(f"    Vol({k}) = {v}")
    print()
    print(f"  {'atom':>5} {'knot':>5} {'ρ_F':>4}  {'Vol_hyp':>10}  "
          f"{'B_pred (MeV)':>14}  {'B_AME (MeV)':>13}  "
          f"{'err_MeV':>10}  {'err %':>8}")
    print("  " + "-" * 95)
    rows = []
    for (Z, N) in FAMILY_1_REGISTRY:
        r = family_1_binding(Z, N)
        rows.append(r)
        print(f"  {r['symbol']:>5} {r['knot']:>5} {r['rho_F']:>4}  "
              f"{r['Vol_hyp']:>10.6f}  "
              f"{r['B_pred_MeV']:>14.6f}  "
              f"{r['B_AME_MeV']:>13.6f}  "
              f"{r['err_MeV']:>+10.4f}  "
              f"{r['err_pct']:>+7.2f}%")
    print()
    out_path = Path(__file__).parent / "family-1-kashaev.witness.json"
    out_path.write_text(json.dumps({
        "computation": "family-1-kashaev",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Family-1 binding via Kashaev law B = ρ_F · m_e · Vol_hyp(K) "
            "for D, T, ³He using historical knot identifications "
            "(6_2, 8_11, L6a4).  This is the leading-order term; the "
            "remaining ~1-3% residuals are higher-order Habiro/jet "
            "corrections per binding_ladder_catalog.find_best_alpha."
        ),
        "constants": {"m_e_MeV": M_E_MEV},
        "knot_volumes": KNOT_VOL,
        "rows": rows,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
