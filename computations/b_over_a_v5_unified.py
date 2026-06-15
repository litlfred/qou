#!/usr/bin/env python3
"""B/A v5 — unified evaluator dispatching by formula family.

Wires the four formula families established by the watched-branch's
methodology audit (`methodology-deprecation.witness.json`) into a single
dispatch:

    Family 1 — Principled (knot-explicit):  B = ρ_F · m_e · Vol_hyp(K)
        atoms: D, T, ³He
        module: family_1_kashaev.family_1_binding (Kashaev law on
                historical knot ID).  Cross-validates against
                atomic_tr_m_mpfr_50dps and markov_peel where present.

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

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Family-1, Family-2, Family-3 callables (all zero-parameter, fast).
# AME values + family registries imported from the modules to avoid
# duplicating magic constants here.
from family_1_kashaev import (  # noqa: E402
    family_1_binding as _family_1_kashaev_binding,
    FAMILY_1_REGISTRY,
    AME_BA_MEV as _FAMILY_1_AME,
)
from magic_A_formula import (  # noqa: E402
    M_E_MEV, VOL_BORROMEAN, magic_A_binding,
    AME_BA_MEV as _FAMILY_2_AME,
    ATOM_SYMBOL as _FAMILY_2_SYMBOL,
    is_magic_A_atom,
)
from alpha_cluster_recursion import (  # noqa: E402
    C_ALPHA_ALPHA_MEV, VOL_7_2_1, alpha_cluster_binding,
    AME_BA_MEV as _FAMILY_3_AME,
    ATOM_SYMBOL as _FAMILY_3_SYMBOL,
    is_alpha_chain,
)

# Family-1 symbols sourced from FAMILY_1_REGISTRY (single source of truth).
_FAMILY_1_SYMBOL: dict[tuple[int, int], str] = {
    k: v["symbol"] for k, v in FAMILY_1_REGISTRY.items()
}


# ── Plan-H δρ diagnostic (PR #512) ────────────────────────────────
# Empirical "true_ρ" = B_AME / (m_e · Vol_hyp(K)) per atom — the ρ that
# would have to apply for `B = ρ · m_e · Vol_hyp(K)` to match AME exactly.
# Plan H's universal-formula hypothesis was FALSIFIED (signs and
# magnitudes don't fit a single closed-form ρ_F(q)); these per-atom
# values document the structural gap for closure of GAP-A in the
# 1-ppb workplan (docs/audits/2026-05-03-next-session-plan-to-1ppb.md).
def _witness_results(witness: dict) -> list:
    """Yield the result rows from a witness, supporting both the legacy
    `rows` schema and the modern `data.results` schema (per repo guideline:
    older files may use legacy schemas — verify per-file)."""
    rows = witness.get("rows")
    if isinstance(rows, list):
        return rows
    nested = witness.get("data", {})
    if isinstance(nested, dict):
        return nested.get("results", []) or []
    return []


_PLAN_H_DELTA_RHO: dict[tuple[int, int], dict] = {}
_ph_path = _pb.witness_path("rho-census-wedderburn-experiment.witness.json", HERE)
if _ph_path.exists():
    try:
        _ph_data = json.loads(_ph_path.read_text())
    except (json.JSONDecodeError, OSError):
        _ph_data = {}
    for _r in _witness_results(_ph_data):
        if "Z" not in _r or "N" not in _r:
            continue
        _PLAN_H_DELTA_RHO[(_r["Z"], _r["N"])] = {
            "true_rho": _r.get("true_rho"),
            "delta_rho": _r.get("delta_rho"),
            "rho_handpick": _r.get("rho_handpick"),
            "M_err_ppm_predicted": _r.get("M_err_ppm_predicted"),
        }


# ── Markov-peel tr_M cross-validation (PR #520) ──────────────────
# Loads pre-computed tr_M(T_w) at q_0 from markov-peel-atomic-tr-m.witness.json.
# Available for: p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li (as of #520).
# These are the canonical-input values; B_pred closure for Family 4
# still needs the ρ_F + Vol_hyp(K) derivation (GAP 4, 5).
_MARKOV_PEEL_TR_M: dict[tuple[int, int], str] = {}
_peel_path = _pb.witness_path("markov-peel-atomic-tr-m.witness.json", HERE)
if _peel_path.exists():
    try:
        _peel_data = json.loads(_peel_path.read_text())
    except (json.JSONDecodeError, OSError):
        _peel_data = {}
    for _r in _witness_results(_peel_data):
        if "Z" not in _r or "N" not in _r or "tr_M_at_q0" not in _r:
            continue
        _MARKOV_PEEL_TR_M[(_r["Z"], _r["N"])] = _r["tr_M_at_q0"]


# ── AME 2020 reference values ─────────────────────────────────────
# Families 1, 2, 3 imported from their module's AME_BA_MEV; only
# Family 4 (open atoms with no callable yet) defined locally.
_FAMILY_4_AME = {
    (3, 3):  31.99405,       # ⁶Li
    (3, 4):  39.24452,       # ⁷Li
    (4, 5):  58.16498,       # ⁹Be
    (5, 6):  76.20548,       # ¹¹B
    (7, 7): 104.65877,       # ¹⁴N
    (9, 10): 147.80137,      # ¹⁹F
}
AME_BA_MEV = {
    **_FAMILY_1_AME,
    **_FAMILY_2_AME,
    **_FAMILY_3_AME,
    **_FAMILY_4_AME,
}

# Atom symbols sourced from each family module's ATOM_SYMBOL (single
# source of truth); only Family 4 (open atoms with no callable yet) is
# defined locally.  Adding an atom to a module's ATOM_SYMBOL auto-wires
# its display name through the unified evaluator.
_FAMILY_4_SYMBOL: dict[tuple[int, int], str] = {
    (3, 3): "⁶Li", (3, 4): "⁷Li", (4, 5): "⁹Be",
    (5, 6): "¹¹B", (7, 7): "¹⁴N", (9, 10): "¹⁹F",
}
ATOM_SYMBOL = {
    **_FAMILY_1_SYMBOL,
    **_FAMILY_2_SYMBOL,
    **_FAMILY_3_SYMBOL,
    **_FAMILY_4_SYMBOL,
}


# ── Family classification (derived from module registries) ────────
# Membership is sourced from each family module's authoritative
# registry/predicate so adding an atom to a module auto-updates the
# dispatcher.
def classify_family(Z: int, N: int) -> int:
    """Return the formula family (1, 2, 3, or 4) for (Z, N)."""
    if (Z, N) in FAMILY_1_REGISTRY:
        return 1
    if is_magic_A_atom(Z, N):
        return 2
    if is_alpha_chain(Z, N) and (Z, N) in _FAMILY_3_AME:
        return 3
    return 4


# Family-1 dispatch is inlined in `evaluate` for symmetry with family
# 2/3 (matches the pattern Gemini flagged in review — no wrapper).


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
        f1 = _family_1_kashaev_binding(Z, N)
        r = {
            "applicable": f1.get("applicable", False),
            "reason": f1.get("reason"),
            "B_pred_MeV": f1.get("B_pred_MeV"),
            "knot": f1.get("knot"),
            "rho_F": f1.get("rho_F"),
            "Vol_hyp": f1.get("Vol_hyp"),
            "formula": f1.get("formula"),
            "module": "family_1_kashaev.family_1_binding",
            "method": "principled-derivation (Kashaev law via historical knot ID)",
        }
    elif family == 2:
        m = magic_A_binding(Z, N)
        r = {
            "applicable": m.get("applicable", False),
            "reason": m.get("reason"),
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
            "reason": a.get("reason"),
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
    # Canonical-input tr_M cross-validation from PR #520's markov_peel
    # production runs — independent path to the Family-1 Hoefsmit-bridge.
    if (Z, N) in _MARKOV_PEEL_TR_M:
        base["tr_M_at_q0_markov_peel"] = _MARKOV_PEEL_TR_M[(Z, N)]
        # Categorical-mass-identity diagnostic for atoms with both AME
        # and tr_M:  if  B = m_e · ρ_t · tr_M(T_w)  is the unifying
        # closed form (post-Archimedean naming of the Family-1 Kashaev
        # law via the volume conjecture), the implied ρ_t = B / (m_e ·
        # tr_M) is a research input for closing GAP 4, 5.  Not a
        # closed-form correction; published as an open observation per
        # the 1-ppb workplan W-1 / GAP-A discussion.
        if B_AME is not None:
            try:
                tr_M_float = float(_MARKOV_PEEL_TR_M[(Z, N)])
                if tr_M_float > 0:
                    base["rho_t_implied"] = B_AME / (M_E_MEV * tr_M_float)
            except (TypeError, ValueError):
                pass
    # Plan-H δρ diagnostic: per-atom empirical "true_ρ" exposing GAP-A.
    # NOT a closed-form correction (universal hypothesis falsified) —
    # documents the structural gap for the 1-ppb workplan W-1.
    if (Z, N) in _PLAN_H_DELTA_RHO:
        base["plan_h_diagnostic"] = _PLAN_H_DELTA_RHO[(Z, N)]
    return base


# ── Run all atoms + emit witness ───────────────────────────────────
def main() -> int:
    """Evaluate every atom in AME_BA_MEV; emit unified witness."""
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
            1: "Kashaev law B = ρ_F · m_e · Vol_hyp(K); historical knot IDs (6_2, 8_11, L6a4)",
            2: "magic-A shell closure; ⁴He +5.87% uncaptured = higher-order corrections",
            3: "recursion on ⁴He; residual grows with n_α (α-α coupling)",
            4: "OPEN — GAPS 4, 5 (T_w + ρ for ⁶Li, ⁷Li, etc.)",
        }[f]
        print(f"  {f:>6} {family_counts[f]:>5}  {mae_str}  {notes}")
    print()
    # Plan-H δρ diagnostic — what ρ_F would need to be for Family-1 closure
    plan_h_rows = [r for r in rows if r.get("plan_h_diagnostic")]
    if plan_h_rows:
        print("Plan-H δρ diagnostic (W-1 from 1-ppb workplan; per-atom empirical):")
        print(f"  {'atom':>5} {'ρ_handpick':>12} {'true_ρ':>10} {'δρ':>10} {'err_ppm':>10}")
        print("  " + "-" * 55)
        for r in plan_h_rows:
            ph = r["plan_h_diagnostic"]
            print(f"  {r['symbol']:>5} {ph['rho_handpick']:>12.3f} "
                  f"{ph['true_rho']:>10.6f} "
                  f"{ph['delta_rho']:>+10.6f} "
                  f"{ph['M_err_ppm_predicted']:>+10.4f}")
        print(f"  Hypothesis: universal δρ(q) — FALSIFIED (PR #512 commit 57a9ea9fd)")
        print(f"  Closure of W-1 (³He from -2.97% to ≤0.5%) requires per-atom ρ_F derivation")
        print(f"  (NOT yet available; circular if applied as a fitted correction).")
        print()
    rho_t_rows = [r for r in rows if r.get("rho_t_implied") is not None]
    if rho_t_rows:
        print("Categorical-mass-identity diagnostic (ρ_t = B / (m_e · tr_M(T_w))):")
        print(f"  {'atom':>5} {'A':>2} {'tr_M(q_0)':>14} {'ρ_t (implied)':>16}  notes")
        print("  " + "-" * 70)
        for r in rho_t_rows:
            sym = r["symbol"]
            A = r["A"]
            try:
                tr_str = f"{float(r['tr_M_at_q0_markov_peel']):>14.6e}"
            except (KeyError, TypeError, ValueError):
                tr_str = f"{'?':>14}"
            note = "" if r["family"] == 4 else "(family 1/2/3 anchor)"
            print(f"  {sym:>5} {A:>2} {tr_str} {r['rho_t_implied']:>16.4f}  {note}")
        print(f"  No closed-form ρ_t(Z, N) yet — research input for Family-4 closure (GAP 4, 5).")
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
    sys.exit(main())
