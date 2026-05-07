#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to folio-assistant/computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""Magic-A binding formula — callable wrapper for the doubly-magic light-nucleus rule.

Exposes the magic-A shell-closure formula

    B(magic-A) = ρ_F · m_e · A · 8G

where 8G = Vol(L6a4) = Vol(Borromean rings) is the universal residue
prefactor (Catalan's constant ×8), per the canonical chain
prop:gravity-spectral-prefactor and binding-scale-catalan.

Per the watched-branch's methodology audit
(`methodology-deprecation.witness.json` `recursive-atom-knot-atlas.md`),
this rule is **only used for ⁴He at light A**; ⁸Be and heavier atoms
use `recursive-on-4He` (see alpha_cluster_recursion.py).

The reason ⁴He uses the magic-A rule rather than tr_M(T_w) is that
⁴He has no single hyperbolic knot — it is doubly magic (Z = N = 2,
both magic) and the shell-closure structure replaces the per-knot
Markov-trace evaluation.

Reference: prop:atom-knot-mass-derivation (`B(𝔥) = m_e · ρ · tr_M(T_w)`)
specialises here; see docs/b-over-a-error-budget.md Appendix C.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# CODATA 2022
M_E_MEV: float = 0.51099895069

# Catalan's constant (truncated to f64 precision; full 50-dps value not
# preserved in float arithmetic — the formula B = ρ · m_e · A · 8G is
# evaluated in plain Python float, giving ~16-digit accuracy regardless).
# Reference value: G = 0.91596559417721901505460351493238411077414937428167
CATALAN_G: float = 0.9159655941772190

# 8G = Vol(L6a4) = Vol(Borromean rings) — exact hyperbolic-geometry identity
# (= 2 ideal octahedra × 4G each).
VOL_BORROMEAN: float = 8.0 * CATALAN_G  # ≈ 7.32772475341775

# AME2020 reference values for verification
AME_BA_MEV = {
    (2, 2): 28.295674,    # ⁴He doubly magic (Z=2, N=2)
    # Other doubly-magic: (8,8)=¹⁶O 127.62; (20,20)=⁴⁰Ca 342.05; (20,28)=⁴⁸Ca; (82,126)=²⁰⁸Pb
    # These are NOT magic-A in the framework — they use recursive-on-4He.
}

# Atom-symbol map (single source of truth for Family 2 atoms; consumed
# by `b_over_a_v5_unified.py` to avoid duplicating magic strings).
ATOM_SYMBOL: dict[tuple[int, int], str] = {
    (2, 2): "⁴He",
}

MAGIC_NUMBERS = {2, 8, 20, 28, 50, 82, 126}


def is_doubly_magic(Z: int, N: int) -> bool:
    return Z in MAGIC_NUMBERS and N in MAGIC_NUMBERS


def is_magic_A_atom(Z: int, N: int) -> bool:
    """True iff the magic-A formula applies in the watched-branch's
    methodology audit.  Currently only ⁴He (Z=2, N=2)."""
    return (Z, N) == (2, 2)


def magic_A_binding(Z: int, N: int, rho_F: float = 2.0) -> dict:
    """Compute B(magic-A) = ρ_F · m_e · A · 8G.

    Args:
        Z, N: proton/neutron counts.
        rho_F: structural prefactor.  ρ_F = 2 for ⁴He per
            binding_ladder_catalog.py:63 ('2·m_e·4·Vol(L6a4)').

    Returns:
        dict with B_pred_MeV, formula description, and AME comparison
        if available.
    """
    A = Z + N
    if not is_magic_A_atom(Z, N):
        return {
            "applicable": False,
            "reason": (
                f"(Z={Z}, N={N}) is not a magic-A atom in the framework; "
                "the magic-A-formula tag in methodology-deprecation.witness.json "
                "currently lists only ⁴He (Z=N=2)."
            ),
        }
    B_pred = rho_F * M_E_MEV * A * VOL_BORROMEAN
    out = {
        "applicable": True,
        "Z": Z,
        "N": N,
        "A": A,
        "rho_F": rho_F,
        "m_e_MeV": M_E_MEV,
        "Vol_8G": VOL_BORROMEAN,
        "B_pred_MeV": B_pred,
        "formula": f"{rho_F:g}·m_e·{A}·8G",
    }
    B_AME = AME_BA_MEV.get((Z, N))
    if B_AME is not None:
        out["B_AME_MeV"] = B_AME
        out["err_MeV"] = B_pred - B_AME
        out["err_pct"] = 100.0 * (B_pred - B_AME) / B_AME
    return out


def main() -> int:
    print("MAGIC-A FORMULA — doubly-magic light-nucleus binding")
    print(f"  m_e   = {M_E_MEV:.10f} MeV (CODATA 2022)")
    print(f"  Vol_8G = 8G = {VOL_BORROMEAN:.10f}  (Borromean rings)")
    print(f"  Catalan's constant G = {CATALAN_G:.15f}")
    print()
    print(f"  {'atom':>6} {'A':>3}  {'B_pred (MeV)':>14}  {'B_AME (MeV)':>13}  {'err_MeV':>10}  {'err %':>7}")
    print("  " + "-" * 70)
    rows = []
    for (Z, N), B_AME in AME_BA_MEV.items():
        r = magic_A_binding(Z, N)
        if not r.get("applicable"):
            continue
        rows.append(r)
        sym = {(2, 2): "⁴He"}.get((Z, N), f"(Z={Z},N={N})")
        print(f"  {sym:>6} {r['A']:>3}  "
              f"{r['B_pred_MeV']:>14.6f}  "
              f"{r['B_AME_MeV']:>13.6f}  "
              f"{r['err_MeV']:>+10.4f}  "
              f"{r['err_pct']:>+6.2f}%")
    print()
    print("Canonical-chain context:")
    print("  This is the magic-A specialization of `B(𝔥) = m_e · ρ · tr_M(T_w)`.")
    print("  ⁴He has no single hyperbolic knot — the doubly-magic shell-closure")
    print("  structure replaces per-knot Markov-trace evaluation.")
    print("  Numerical handle: Vol(L6a4) = 8G is an exact hyperbolic-geometry")
    print("  identity (Borromean rings = 2 ideal octahedra each of volume 4G).")
    print()
    out_path = Path(__file__).parent / "magic-A-formula.witness.json"
    out_path.write_text(json.dumps({
        "computation": "magic-A-formula",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Magic-A doubly-magic binding formula B = ρ_F · m_e · A · 8G "
            "as a callable.  Currently applies to ⁴He only per the "
            "watched-branch's methodology audit; heavier doubly-magic "
            "atoms (¹⁶O, ⁴⁰Ca) use recursive-on-4He instead."
        ),
        "constants": {
            "m_e_MeV": M_E_MEV,
            "catalan_G": CATALAN_G,
            "Vol_8G": VOL_BORROMEAN,
            "magic_numbers": sorted(MAGIC_NUMBERS),
        },
        "rows": rows,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
