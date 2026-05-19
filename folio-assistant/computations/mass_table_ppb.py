#!/usr/bin/env python3
"""
Mass table: AME vs ZERO-FREE-PARAMETER predictions, with error in ppb
and %.

No fitting.  Nothing calibrated from AME values.  Every B_pred is a
function of q₀ and a specified atom→knot assignment only.

Prediction rules (all zero-parameter from q₀):
  • Kashaev volume law      B = ρ_F · Vol_hyp(K)    with ρ_F ∈ {m_e, 2m_e}
  • Atom → knot assignment  one of:
      D    ↔ 6_2            (handover hypothesis, not derived)
      T    ↔ 8_11           (handover hypothesis, not derived)
      3He  ↔ Borromean L6a4 (handover hypothesis, not derived)
      4He  ↔ 4·Borromean    (magic-atom A·8G rule)
      A≥8  ↔ α-cluster with c_αα = m_e · Vol(7²_1)  (derived from knot 7²_1)

The atom→knot assignments for D, T, ³He were obtained by census
search in jsj_verification.py — that IS a form of AME-driven
fitting (we picked the knot whose volume is closest to B_AME/ρ).
Flagged here as "hyp: by-census" so the reader can distinguish.

Truly derived pieces: (1) the density rule ρ_F ∈ {m_e, 2m_e} —
pending formal justification; (2) the α-coupling
c_αα = m_e · Vol(7²_1) — derived from the topology of two linked
Borromean rings.  No AME input.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder  # noqa: E402
from knot_volumes import VOL_BORROMEAN, VOL_7_SQ_1  # noqa: E402

# Knot volumes now imported from `knot_volumes` (canonical mpmath
# 50dps source). Catalan G + Vol(L6a4) = 8G + Vol(7²_1) literature
# values. Pre-refactor these were f64-hardcoded literals; post-
# refactor they live in the centralised module so a `--precision
# mpfr` lift only needs to update one place. See I14 audit and the
# coordination ledger entry "knot-vol _precision propagation".

# Atomic-pair α-α coupling knot: 7²_1 (Whitehead-like linked pair).
# DERIVED: c_αα = m_e · Vol(7²_1). No AME fit.
C_ALPHA_DERIVED = M_E_MEV * VOL_7_SQ_1         # ≈ 2.4270 MeV

# Hyperbolic volumes from SnapPy (50-digit HP, independent of AME).
KNOT_VOL = {
    "6_2":       4.4008325161230461014412038656409280339834854185165,
    "8_11":      8.2863168178065925881,
    "L6a4":      VOL_BORROMEAN,
}

# AME2020 light-atom table (B in MeV; positive = binding).
AME_TABLE = [
    ("2H",     1,  1,   2.22456612),
    ("3H",     1,  2,   8.4817984),
    ("3He",    2,  1,   7.7180375),
    ("4He",    2,  2,  28.2956912),
    ("6Li",    3,  3,  31.99405),
    ("7Li",    3,  4,  39.24453),
    ("8Be",    4,  4,  56.49951),
    ("9Be",    4,  5,  58.16498),
    ("11B",    5,  6,  76.20548),
    ("12C",    6,  6,  92.16175),
    ("14N",    7,  7, 104.65877),
    ("16O",    8,  8, 127.61929),
    ("19F",    9, 10, 147.80137),
    ("20Ne",  10, 10, 160.64486),
    ("24Mg",  12, 12, 198.25690),
    ("40Ca",  20, 20, 342.05212),
]

# Atom → (knot, density, source-label) hypothesis table.
# ZERO-PARAMETER = the pairing is stated in the framework; the
# predicted binding follows mechanically from Vol and ρ.  We mark
# WHERE the pairing comes from (derived-from-framework vs census-
# assigned-from-B_AME).
ATOM_ASSIGN = {
    "2H":   {"rule": "kashaev",  "knot": "6_2",  "rho_factor": 1,
             "origin": "hyp: census-assigned"},
    "3H":   {"rule": "kashaev",  "knot": "8_11", "rho_factor": 2,
             "origin": "hyp: census-assigned"},
    "3He":  {"rule": "kashaev",  "knot": "L6a4", "rho_factor": 2,
             "origin": "hyp: census-assigned"},
    # 4He = A·8G magic-atom rule, density 2m_e, A=4.
    "4He":  {"rule": "magic",    "A_units": 4, "rho_factor": 2,
             "origin": "framework: A·8G magic rule"},
    # 6Li: no standard assignment — leave as no-prediction for now.
    # 7Li: same.
    # 8Be: α-cluster (n_α=2, n_pairs=1)
    "8Be":  {"rule": "alpha",    "n_alpha": 2, "n_pairs": 1,
             "origin": "framework: α-cluster n_α=2"},
    # 12C: α-cluster (n_α=3, n_pairs=3)
    "12C":  {"rule": "alpha",    "n_alpha": 3, "n_pairs": 3,
             "origin": "framework: α-cluster n_α=3"},
    # 16O: α-cluster (n_α=4, n_pairs=6)
    "16O":  {"rule": "alpha",    "n_alpha": 4, "n_pairs": 6,
             "origin": "framework: α-cluster n_α=4"},
    # 20Ne, 24Mg, 40Ca: α-cluster with (n_α, n_pairs) from C(n,2).
    "20Ne": {"rule": "alpha",    "n_alpha": 5, "n_pairs": 10,
             "origin": "framework: α-cluster n_α=5"},
    "24Mg": {"rule": "alpha",    "n_alpha": 6, "n_pairs": 15,
             "origin": "framework: α-cluster n_α=6"},
    "40Ca": {"rule": "alpha",    "n_alpha": 10, "n_pairs": 45,
             "origin": "framework: α-cluster n_α=10"},
}


def predict(sym: str) -> dict | None:
    """Return {B_pred, formula, origin, notes} or None if no rule."""
    info = ATOM_ASSIGN.get(sym)
    if not info:
        return None

    if info["rule"] == "kashaev":
        knot, rho_f = info["knot"], info["rho_factor"]
        vol = KNOT_VOL[knot]
        B = rho_f * M_E_MEV * vol
        return {
            "B_pred": B,
            "formula": f"{rho_f}·m_e · Vol({knot})",
            "origin": info["origin"],
            "inputs": {"knot": knot, "Vol": vol, "rho_factor": rho_f},
        }

    if info["rule"] == "magic":
        A, rho_f = info["A_units"], info["rho_factor"]
        # B = ρ · A · 8G (A independent Borromean nucleons)
        B = rho_f * M_E_MEV * A * VOL_BORROMEAN
        return {
            "B_pred": B,
            "formula": f"{rho_f}·m_e · {A}·8G",
            "origin": info["origin"],
            "inputs": {"A": A, "8G": VOL_BORROMEAN, "rho_factor": rho_f},
        }

    if info["rule"] == "alpha":
        # α-cluster: B = n_α · B(⁴He_derived) + n_pairs · c_αα
        # Use 4He_derived from magic rule = 2m_e · 4 · 8G = 29.9555 MeV
        B_4He_derived = 2 * M_E_MEV * 4 * VOL_BORROMEAN
        B = info["n_alpha"] * B_4He_derived + info["n_pairs"] * C_ALPHA_DERIVED
        return {
            "B_pred": B,
            "formula": (f"{info['n_alpha']}·B(⁴He_derived) "
                          f"+ {info['n_pairs']}·c_αα"),
            "origin": info["origin"],
            "inputs": {
                "n_alpha": info["n_alpha"],
                "n_pairs": info["n_pairs"],
                "B_4He_derived": B_4He_derived,
                "c_alpha": C_ALPHA_DERIVED,
            },
        }
    return None


def fmt_ppb(err_abs: float, b_ame: float) -> str:
    if b_ame <= 0:
        return "—"
    ppb = abs(err_abs) / b_ame * 1e9
    if ppb > 1e9:
        return f"{ppb/1e9:+.3g}×10⁹"
    if ppb > 1e6:
        return f"{ppb/1e6:+.3f}×10⁶"
    if ppb > 1e3:
        return f"{ppb/1e3:+.3f}×10³"
    return f"{ppb:+.3f}"


def main() -> int:
    print("=" * 130)
    print("MASS TABLE — AME2020 vs ZERO-FREE-PARAMETER predictions")
    print(f"  q₀ = {Q0:.10f}   m_e = {M_E_MEV} MeV")
    print(f"  8G = {VOL_BORROMEAN:.10f}   Vol(7²_1) = {VOL_7_SQ_1:.10f}")
    print(f"  c_αα (derived = m_e · Vol(7²_1)) = {C_ALPHA_DERIVED:.6f} MeV")
    print(f"  B(⁴He_derived) = 2m_e · 4·8G = "
          f"{2*M_E_MEV*4*VOL_BORROMEAN:.6f} MeV   "
          f"(AME 4He: {28.2957} MeV)")
    print(f"  NO AME VALUES USED AS INPUTS.")
    print("=" * 130)
    print(f"  {'atom':>5} {'Z':>3} {'N':>3} {'A':>3}  "
          f"{'B_AME':>10}  {'B_pred':>11}  {'err (MeV)':>11}  "
          f"{'err %':>9}  {'err ppb':>12}  formula")
    print("  " + "-" * 128)
    rows = []
    no_assign = []
    for (sym, Z, N, B_ame) in AME_TABLE:
        A = Z + N
        pred = predict(sym)
        if pred is None:
            no_assign.append((sym, Z, N, A, B_ame))
            print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
                  f"{B_ame:>10.4f}   "
                  f"[no zero-parameter rule assigned]")
            continue
        B_pred = pred["B_pred"]
        err = B_pred - B_ame
        pct = err / B_ame * 100 if B_ame else 0.0
        ppb = err / B_ame * 1e9 if B_ame else 0.0
        print(f"  {sym:>5} {Z:>3} {N:>3} {A:>3}  "
              f"{B_ame:>10.4f}  {B_pred:>+11.4f}  {err:>+11.6f}  "
              f"{pct:>+8.3f}%  {fmt_ppb(err, B_ame):>12}  "
              f"{pred['formula']}  [{pred['origin']}]")
        rows.append({
            "sym": sym, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": B_pred,
            "err_MeV": err,
            "err_pct": pct,
            "err_ppb": ppb,
            "formula": pred["formula"],
            "origin": pred["origin"],
            "inputs": pred["inputs"],
        })

    # Summary
    print()
    print("  Summary:")
    ok = rows
    within = {1: 0, 1e3: 0, 1e6: 0, 1e9: 0}
    for r in ok:
        for th in within:
            if abs(r["err_ppb"]) <= th:
                within[th] += 1
    print(f"    n = {len(ok)} atoms with zero-parameter prediction")
    print(f"    n = {len(no_assign)} atoms without rule "
          f"({', '.join(a[0] for a in no_assign)})")
    print(f"    within 1    ppb  (1e-9):    {within[1]}")
    print(f"    within 1e3  ppb  (1 ppm):   {within[1e3]}")
    print(f"    within 1e6  ppb  (0.1%):    {within[1e6]}")
    print(f"    within 1e9  ppb  (100%):    {within[1e9]}")

    mean_pct = sum(abs(r["err_pct"]) for r in ok) / len(ok) if ok else 0.0
    mean_ppb = sum(abs(r["err_ppb"]) for r in ok) / len(ok) if ok else 0.0
    print(f"    mean |err|:   {mean_pct:.4f}%  =  {mean_ppb:.3e} ppb")

    builder = (
        WitnessBuilder("mass-table-ppb", engine="python+snappy")
        .set_description(
            "AME2020 light-atom binding vs strictly zero-free-parameter "
            "predictions: Kashaev law B = ρ_F · Vol_hyp(K) with ρ_F ∈ "
            "{m_e, 2m_e}; atom→knot assignments from framework rules "
            "(magic A·8G, α-cluster with c_αα = m_e·Vol(7²_1)) or "
            "census search (flagged 'hyp: census-assigned'). "
            "NO AME-derived calibrations or fits."
        )
        .set_audit_only("docs/audits/2026-05-03-next-session-plan-to-1ppb.md")
        .add_parameter("q_0", Q0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("vol_borromean_8G", VOL_BORROMEAN)
        .add_parameter("vol_7_sq_1", VOL_7_SQ_1)
        .add_parameter("c_alpha_derived_MeV", C_ALPHA_DERIVED)
        .add_data("rows", rows)
        .add_data("atoms_no_assignment", no_assign)
        .add_data("within", {str(k): v for k, v in within.items()})
        .add_data("mean_abs_pct", mean_pct)
        .add_data("mean_abs_ppb", mean_ppb)
    )
    out = builder.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
