#!/usr/bin/env python3
"""
Decomposition-based census search for odd-A / non-α atoms.

Rather than matching the full binding B to a single census link, we
decompose per cluster-model intuition:

    B(atom) ≈ B(α-chain base) + B(residual bond)

where the α-chain base uses the established 2m_e · (4·8G)·n_α + C(n_α,2)·c_αα
formula, and the residual bond is an extra knot / link we search for.

Candidates per atom:
  ⁶Li  = α + D        → residual = B(⁶Li) - B(⁴He) - B(²H)
  ⁷Li  = α + T        → residual = B(⁷Li) - B(⁴He) - B(³H)
  ⁹Be  = 2α + n       → residual = B(⁹Be) - 2·B(⁴He) - c_αα - B(n)
  ¹⁰B  = 2α + D       → residual = B(¹⁰B) - 2·B(⁴He) - c_αα - B(²H)
  ¹⁰Be = 2α + 2n      → residual = B(¹⁰Be) - 2·B(⁴He) - c_αα
  ¹¹B  = 2α + T       → residual = B(¹¹B) - 2·B(⁴He) - c_αα - B(³H)

Search SnapPy census for links with Vol matching residual / ρ for
ρ ∈ {m_e, 2m_e}.  Residuals are small (MeV scale), so targets are
small volumes in reach of the census.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0

try:
    import snappy
except ImportError:
    print("SnapPy not installed; abort.", file=sys.stderr)
    sys.exit(1)

# ── Constants ────────────────────────────────────────────────────
M_E_MEV       = 0.51099895
CATALAN_G     = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G
VOL_7_2_1     = 4.7495
B_4HE         = 28.295674
B_D           = 2.22458
B_T           = 8.4818
B_3HE         = 7.7180
c_aa          = M_E_MEV * VOL_7_2_1   # α-α coupling ≈ 2.427 MeV

# ── Decompositions ───────────────────────────────────────────────
# base = sum of known clusters; residual = B_AME - base
DECOMP = [
    # (atom, Z, N, B_AME, base_description, base_MeV, ρ_for_residual)
    # ρ_for_residual = "me" or "2me" — heuristic: two-body bonds use m_e
    ("6Li",  3, 3, 31.9941, "α + D",            B_4HE + B_D,                "me"),
    ("7Li",  3, 4, 39.2446, "α + T",            B_4HE + B_T,                "me"),
    ("9Be",  4, 5, 58.1651, "2α + n (bound)",   2*B_4HE + c_aa,             "me"),
    ("10B",  5, 5, 64.7512, "2α + D",           2*B_4HE + c_aa + B_D,       "me"),
    ("10Be", 4, 6, 64.9775, "2α + 2n",          2*B_4HE + c_aa,             "me"),
    ("11B",  5, 6, 76.2054, "2α + T",           2*B_4HE + c_aa + B_T,       "me"),
]


def search_near(target_vol: float, max_crossings: int = 11,
                window: float = 0.5) -> list[dict]:
    # Hyperbolic volumes are non-negative; a negative target means the
    # base decomposition over-predicts binding and no census knot can
    # close the gap.  Skip the scan and signal the anomaly to caller.
    if target_vol <= 0:
        return []
    candidates = []
    for n_cross in range(3, max_crossings + 1):
        try:
            it = snappy.LinkExteriors(crossings=n_cross)
        except Exception:
            continue
        for M in it:
            try:
                v_raw = M.volume()
                v = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
            except Exception:
                continue
            if abs(v - target_vol) <= window:
                try:
                    sol = str(M.solution_type())
                except Exception:
                    sol = "unknown"
                candidates.append({
                    "name": M.name(),
                    "crossings": n_cross,
                    "cusps": M.num_cusps(),
                    "volume": v,
                    "target": target_vol,
                    "err_pct": 100.0 * (v - target_vol) / target_vol,
                    "err_abs": v - target_vol,
                    "solution_type": sol,
                })
    candidates.sort(key=lambda c: abs(c["err_abs"]))
    return candidates[:8]


def main() -> int:
    print(f"\n  Decomposition search — odd-A atoms as α-chain + residual bond")
    print(f"  m_e = {M_E_MEV:.6f} MeV, Vol(B_3) = 8G = {VOL_BORROMEAN:.4f}")
    print(f"  c_αα = m_e · Vol(7²_1) = {c_aa:.4f} MeV\n")

    header = (f"  {'atom':>6} {'base':>14} {'base_MeV':>10} "
              f"{'res_MeV':>9} {'ρ':>4} {'tgt_V':>8}   best match")
    print(header)
    print("  " + "-" * (len(header) - 2))

    witness_rows = []
    for atom, Z, N, B_ame, desc, base_mev, rho in DECOMP:
        residual = B_ame - base_mev
        if rho == "me":
            target_vol = residual / M_E_MEV
        else:
            target_vol = residual / (2 * M_E_MEV)
        matches = search_near(target_vol, max_crossings=11, window=0.5)
        if matches:
            best = matches[0]
            best_str = (f"{best['name']} (Vol={best['volume']:.4f}, "
                        f"err={best['err_pct']:+.2f}%)")
        else:
            best_str = "— no match in window —"
        print(f"  {atom:>6} {desc:>14} {base_mev:>10.3f} "
              f"{residual:>+9.3f} {rho:>4} {target_vol:>8.3f}   {best_str}")
        witness_rows.append({
            "atom": atom,
            "Z": Z,
            "N": N,
            "A": Z + N,
            "B_AME_MeV": B_ame,
            "base_description": desc,
            "base_MeV": base_mev,
            "residual_MeV": residual,
            "density_used": rho,
            "target_vol": target_vol,
            "matches": matches,
        })

    witness = {
        "name": "odd-a-decomposition-search",
        "description": (
            "Decomposition-based census search for odd-A and non-α "
            "atoms.  Splits B(atom) = B(α-chain base) + B(residual "
            "bond) per cluster-model intuition, then searches SnapPy "
            "for a hyperbolic link matching the residual at either "
            "m_e or 2m_e density.  Gives candidate knots/links for "
            "the extra bond holding the α-chain to the odd nucleons."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0,
            "M_E_MEV": M_E_MEV,
            "CATALAN_G": CATALAN_G,
            "VOL_BORROMEAN": VOL_BORROMEAN,
            "c_alpha_alpha_MEV": c_aa,
            "B_4HE_MEV": B_4HE,
            "B_D_MEV": B_D,
            "B_T_MEV": B_T,
        },
        "rows": witness_rows,
    }
    out = Path(__file__).parent / "odd-a-decomposition-search.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
