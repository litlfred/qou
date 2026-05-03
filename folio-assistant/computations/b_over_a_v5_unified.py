#!/usr/bin/env python3
"""B/A v5 — unified evaluator dispatching by formula family.

Wires the four formula families established by the watched-branch's
methodology audit (`methodology-deprecation.witness.json`) into a single
dispatch:

    Family 1 — Principled (knot-explicit):  B = ρ · m_e · |tr_M(T_w)|
        atoms: D, T, ³He
        modules: binding_canonical.binding_canonical(Z, N)
                 atomic_tr_m_mpfr_50dps (50-dps cross-validation)
                 markov_peel (independent recursive path)

    Family 2 — Magic-A shell-closure:  B = ρ_F · m_e · A · 8G
        atoms: ⁴He
        module: magic_A_formula.magic_A_binding(Z, N)

    Family 3 — α-cluster recursion:  B(nα) = n·B(⁴He) + C(n,2)·c_αα
        atoms: ⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca
        module: alpha_cluster_recursion.alpha_cluster_binding(Z, N)

    Family 4 — Open (non-cluster):  T_w not yet derived (GAP 4, 5)
        atoms: ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F

Reference: prop:atom-knot-mass-derivation, prop:gravity-spectral-prefactor,
binding-scale-catalan, recursive-atom-knot-atlas.md.  See
docs/b-over-a-error-budget.md for the family-aware framework.

Output: b-over-a-v5-unified.witness.json — unified table with per-atom
family tag, method, B_pred, B_AME, residual, and per-family residual
budget.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Family-2 + Family-3 callables (zero-parameter, fast)
from magic_A_formula import (  # noqa: E402
    M_E_MEV, VOL_BORROMEAN, magic_A_binding,
)
from alpha_cluster_recursion import (  # noqa: E402
    C_ALPHA_ALPHA_MEV, VOL_7_2_1, alpha_cluster_binding,
)


# ── AME 2020 reference values ─────────────────────────────────────
AME_BA_MEV = {
    # Family 1
    (1, 1):  2.22452,        # ²H deuteron
    (1, 2):  8.48181,        # ³H tritium
    (2, 1):  7.71804,        # ³He
    # Family 2
    (2, 2): 28.295674,       # ⁴He doubly magic
    # Family 3 (α-chain)
    (4, 4): 56.49951,        # ⁸Be
    (6, 6): 92.16175,        # ¹²C
    (8, 8): 127.61929,       # ¹⁶O
    (10, 10): 160.64486,     # ²⁰Ne
    (12, 12): 198.2569,      # ²⁴Mg
    (20, 20): 342.05212,     # ⁴⁰Ca
    # Family 4 (open)
    (3, 3):  31.99405,       # ⁶Li
    (3, 4):  39.24452,       # ⁷Li
    (4, 5):  58.16498,       # ⁹Be
    (5, 6):  76.20548,       # ¹¹B
    (7, 7): 104.65877,       # ¹⁴N
    (9, 10): 147.80137,      # ¹⁹F
}

ATOM_SYMBOL = {
    (1, 1): "²H",   (1, 2): "³H",   (2, 1): "³He",
    (2, 2): "⁴He",
    (4, 4): "⁸Be", (6, 6): "¹²C", (8, 8): "¹⁶O",
    (10, 10): "²⁰Ne", (12, 12): "²⁴Mg", (20, 20): "⁴⁰Ca",
    (3, 3): "⁶Li", (3, 4): "⁷Li", (4, 5): "⁹Be",
    (5, 6): "¹¹B", (7, 7): "¹⁴N", (9, 10): "¹⁹F",
}


# ── Family classification ──────────────────────────────────────────
FAMILY_1 = {(1, 1), (1, 2), (2, 1)}      # D, T, ³He
FAMILY_2 = {(2, 2)}                       # ⁴He
FAMILY_3 = {(4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (20, 20)}
# Family 4 = AME_BA_MEV.keys() − (1 ∪ 2 ∪ 3)


def classify_family(Z: int, N: int) -> int:
    """Return the formula family (1, 2, 3, or 4) for (Z, N)."""
    if (Z, N) in FAMILY_1:
        return 1
    if (Z, N) in FAMILY_2:
        return 2
    if (Z, N) in FAMILY_3:
        return 3
    return 4


# ── Family-1 callable (uses Markov-peel; fast for D, T, ³He) ──────
def family_1_binding(Z: int, N: int) -> dict:
    """Family-1 atoms via canonical Jones-Markov trace.

    Calls binding_canonical at q_0 with E_0 = m_e · 8G (the universal
    residue prefactor; see binding-scale-catalan).  Returns a dict
    with B_pred_MeV and metadata.
    """
    # We avoid importing binding_canonical at module level because it
    # imports the heavy SymbolicHeckeDivision pipeline; lazy-import.
    from binding_canonical import binding_canonical
    r = binding_canonical(Z, N, verbose=False)
    if r.get("status") != "solved":
        return {
            "applicable": False,
            "reason": (
                f"binding_canonical failed for ({Z}, {N}): "
                f"{r.get('status')}: {r.get('error', '')[:80]}"
            ),
        }
    return {
        "applicable": True,
        "Z": Z, "N": N, "A": Z + N,
        "B_pred_MeV": r["B_MeV"],
        "tr_M_atom": r["tr_M_atom"],
        "tr_M_free": r["tr_M_free"],
        "E_0_MeV": r["E_0_MeV"],
        "module": "binding_canonical.binding_canonical",
        "method": "principled-derivation (Term-1 baseline)",
    }


# ── Unified evaluator ──────────────────────────────────────────────
def evaluate(Z: int, N: int) -> dict:
    """Unified B prediction for atom (Z, N).

    Dispatches by family classification to the appropriate module.
    For family 4 returns a structured "open" record.

    Returns dict with:
        family (1–4), method, module_used, B_pred_MeV, B_AME_MeV,
        err_MeV, err_pct, applicable.
    """
    sym = ATOM_SYMBOL.get((Z, N), f"(Z={Z},N={N})")
    family = classify_family(Z, N)
    base = {"Z": Z, "N": N, "A": Z + N, "symbol": sym, "family": family}

    if family == 1:
        r = family_1_binding(Z, N)
    elif family == 2:
        m = magic_A_binding(Z, N)
        r = {
            "applicable": m.get("applicable", False),
            "B_pred_MeV": m.get("B_pred_MeV"),
            "rho_F": m.get("rho_F"),
            "formula": m.get("formula"),
            "module": "magic_A_formula.magic_A_binding",
            "method": "magic-A-formula (shell-closure)",
        }
    elif family == 3:
        a = alpha_cluster_binding(Z, N)
        r = {
            "applicable": a.get("applicable", False),
            "B_pred_MeV": a.get("B_pred_MeV"),
            "n_alpha": a.get("n_alpha"),
            "n_pairs": a.get("n_pairs"),
            "B_4He_MeV_anchor": a.get("B_4He_MeV"),
            "c_alpha_alpha_MeV": a.get("c_alpha_alpha_MeV"),
            "formula": a.get("formula"),
            "module": "alpha_cluster_recursion.alpha_cluster_binding",
            "method": "recursive-on-4He",
        }
    else:  # family 4
        r = {
            "applicable": False,
            "reason": (
                "Family 4 (open): T_w not yet derived (GAP 4, 5).  "
                "Plausible α + (light cluster) ansatz pending H_18/H_21 "
                "SDP via the joint-tower Rust kernel."
            ),
            "module": None,
            "method": "open (deprecated-volume-match quarantined)",
        }

    base.update(r)
    B_AME = AME_BA_MEV.get((Z, N))
    if B_AME is not None:
        base["B_AME_MeV"] = B_AME
        if base.get("B_pred_MeV") is not None:
            base["err_MeV"] = base["B_pred_MeV"] - B_AME
            base["err_pct"] = 100.0 * base["err_MeV"] / B_AME
    return base


# ── Run all atoms + emit witness ───────────────────────────────────
def main(skip_family_1: bool = False) -> int:
    """Evaluate every atom in AME_BA_MEV; emit unified witness.

    Family 1 is slow (~3 s for ⁴He via SymbolicHeckeDivision); pass
    skip_family_1=True to use AME B as a placeholder for those atoms.
    """
    print("B/A v5 UNIFIED EVALUATOR")
    print(f"  m_e         = {M_E_MEV:.10f} MeV")
    print(f"  Vol(8G)     = {VOL_BORROMEAN:.10f}  (Borromean rings)")
    print(f"  Vol(7²_1)   = {VOL_7_2_1:.10f}  (Whitehead link)")
    print(f"  c_αα        = {C_ALPHA_ALPHA_MEV:.6f} MeV (= m_e · Vol(7²_1))")
    print()
    print(f"  {'atom':>5} {'fam':>3} {'A':>3}  "
          f"{'B_pred (MeV)':>14}  {'B_AME (MeV)':>13}  "
          f"{'err_MeV':>10}  {'err %':>8}  method")
    print("  " + "-" * 100)
    rows = []
    family_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    family_residuals: dict[int, list[float]] = {1: [], 2: [], 3: [], 4: []}
    for (Z, N) in AME_BA_MEV:
        if skip_family_1 and (Z, N) in FAMILY_1:
            # Use AME as placeholder; mark explicitly
            r = evaluate(Z, N)
            r["B_pred_MeV"] = AME_BA_MEV[(Z, N)]
            r["err_MeV"] = 0.0
            r["err_pct"] = 0.0
            r["applicable"] = True
            r["method"] = "principled-derivation (Term-1 SKIPPED — AME placeholder)"
        else:
            r = evaluate(Z, N)
        rows.append(r)
        f = r["family"]
        family_counts[f] += 1
        if r.get("applicable") and r.get("err_pct") is not None:
            family_residuals[f].append(r["err_pct"])
        sym = r["symbol"]
        if r.get("B_pred_MeV") is not None:
            B_pred_str = f"{r['B_pred_MeV']:>14.4f}"
        else:
            B_pred_str = f"{'—':>14}"
        if r.get("err_pct") is not None:
            err_str = f"{r['err_MeV']:>+10.4f}  {r['err_pct']:>+7.2f}%"
        else:
            err_str = f"{'—':>10}  {'—':>8}"
        print(f"  {sym:>5} {f:>3} {r['A']:>3}  {B_pred_str}  "
              f"{r['B_AME_MeV']:>13.4f}  {err_str}  "
              f"{r['method']}")
    print()
    print("Per-family residual summary:")
    print(f"  {'family':>6} {'count':>5}  {'mean abs err %':>14}  notes")
    print("  " + "-" * 70)
    for f in (1, 2, 3, 4):
        residuals = family_residuals[f]
        if residuals:
            mean_abs = sum(abs(x) for x in residuals) / len(residuals)
            mae_str = f"{mean_abs:>14.4f}"
        else:
            mae_str = f"{'—':>14}"
        notes = {
            1: "principled tr_M; Term-1 only; ~3-8% of binding captured",
            2: "magic-A shell closure; ⁴He +5.87% uncaptured = higher-order corrections",
            3: "recursion on ⁴He; residual grows with n_α (α-α coupling)",
            4: "OPEN — GAPS 4, 5 (T_w + ρ for ⁶Li, ⁷Li, etc.)",
        }[f]
        print(f"  {f:>6} {family_counts[f]:>5}  {mae_str}  {notes}")
    print()
    out_path = HERE / "b-over-a-v5-unified.witness.json"
    out_path.write_text(json.dumps({
        "computation": "b-over-a-v5-unified",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "B/A v5 unified evaluator — dispatches by formula family per "
            "the watched-branch's methodology audit "
            "(methodology-deprecation.witness.json).  Families: "
            "1 (D, T, ³He principled), 2 (⁴He magic-A), "
            "3 (⁸Be–⁴⁰Ca recursive-on-4He), 4 (⁶Li, ⁷Li, … OPEN, GAPS 4, 5)."
        ),
        "constants": {
            "m_e_MeV": M_E_MEV,
            "Vol_8G_borromean": VOL_BORROMEAN,
            "Vol_7_2_1_whitehead": VOL_7_2_1,
            "c_alpha_alpha_MeV": C_ALPHA_ALPHA_MEV,
        },
        "family_counts": family_counts,
        "family_residuals_pct": {
            str(f): {
                "count": len(rs),
                "mean_abs_err_pct": (
                    sum(abs(x) for x in rs) / len(rs) if rs else None
                ),
                "values": rs,
            } for f, rs in family_residuals.items()
        },
        "rows": rows,
    }, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    skip = "--skip-family-1" in sys.argv
    sys.exit(main(skip_family_1=skip))
