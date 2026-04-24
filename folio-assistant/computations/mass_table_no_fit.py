#!/usr/bin/env python3
"""
STRICTLY-derivation mass table — no AME-informed inputs of any kind.

Columns (zero fitting, zero AME-driven choices):

  Paper  −αΦ₁    : B_pred = −(m_e · 8G) · Φ_1(β_atom)
                   Φ_1 = Σ log|V̂_i^full(q_0)| (atom − free)
                   Wedderburn-weighted per-generator algebraic volume.

  tr_M (closed) : B_pred = (m_e · 8G) · |tr_M^Plancherel(β_atom)|
                   Plancherel-weighted sum of χ_λ(β_atom) over all
                   partitions λ ⊢ 3A.  Closed form via Hoefsmit
                   seminormal matrices (PR #401 std_matrix_trace_closed_form).
                   Only D / T / ³He computable inside the 45s time
                   budget; ⁴He requires n=12 (77 partitions).

  χ_sym·χ_alt   : structural scalar −(1 + H_A²/4)^(2A+1) — does not
                   directly predict B but tracks the 1-dim block
                   contribution as an independent check.

  ⁴He magic     : B_pred = 2·m_e · 4·8G  (framework A·8G magic rule,
                   derived from 4 Borromean rings — the ONLY Kashaev
                   entry with a pure-framework justification; included
                   as the single derivation-based knot prediction.)

REMOVED (because they were AME-informed):
  - D ↔ 6_2, T ↔ 8_11, ³He ↔ L6a4  (census-picked by Vol ≈ B_AME/ρ)
  - α-cluster c_αα = m_e · Vol(7²_1)  (c_αα fitted to ¹²C AME binding)

Output: mass-table-no-fit.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import atom_per_generator_volumes, h as H_A_VAL
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder


CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN  # paper's binding scale, derivation-only

AME_TABLE = [
    ("2H",   1,  1,  2.22456612),
    ("3H",   1,  2,  8.4817984),
    ("3He",  2,  1,  7.7180375),
    ("4He",  2,  2, 28.2956912),
    ("6Li",  3,  3, 31.99405),
    ("7Li",  3,  4, 39.24453),
    ("8Be",  4,  4, 56.49951),
    ("9Be",  4,  5, 58.16498),
    ("11B",  5,  6, 76.20548),
    ("12C",  6,  6, 92.16175),
    ("14N",  7,  7, 104.65877),
    ("16O",  8,  8, 127.61929),
    ("19F",  9, 10, 147.80137),
    ("20Ne", 10, 10, 160.64486),
    ("24Mg", 12, 12, 198.25690),
    ("40Ca", 20, 20, 342.05212),
]


def phi_1(Z: int, N: int) -> float:
    v_atom = atom_per_generator_volumes(Z, N, include_inter=True)
    v_free = atom_per_generator_volumes(Z, N, include_inter=False)

    def sum_ln(vols):
        total = 0.0
        for v in vols:
            f = v["full"]
            if abs(f) < 1e-30:
                return float("-inf")
            total += math.log(abs(f))
        return total

    return sum_ln(v_atom) - sum_ln(v_free)


def b_paper(Z: int, N: int) -> dict:
    try:
        p1 = phi_1(Z, N)
    except Exception:
        return {"B": None, "phi_1": None}
    return {"B": -ALPHA_MEV * p1, "phi_1": p1}


def tr_M_from_witness():
    """Pull |tr_M| values already computed by std_matrix_trace_closed_form.

    If the witness file is missing (e.g. fresh clone without running
    the prerequisite script), automatically invoke
    std_matrix_trace_closed_form.py to generate it.  Returns {} only
    if the re-generation itself fails.
    """
    import json
    import os
    import subprocess
    # Allow the auto-generation timeout to be overridden via env var.
    # Default 300s is plenty for D/T/3He but 4He (n=12, 77 partitions)
    # can exceed it on slower hardware.
    timeout_s = int(os.environ.get("TR_M_WITNESS_TIMEOUT_S", "300"))
    p = Path(__file__).parent / "std-matrix-trace-closed-form.witness.json"
    if not p.exists():
        script = Path(__file__).parent / "std_matrix_trace_closed_form.py"
        if script.exists():
            try:
                subprocess.run([sys.executable, str(script)],
                               check=True, cwd=script.parent,
                               capture_output=True, timeout=timeout_s)
            except Exception as e:
                print(f"  [warn] could not auto-generate tr_M witness: {e}")
                return {}
        else:
            print("  [warn] tr_M witness missing and generator script not "
                  "found; the α·|tr_M| column will be empty")
            return {}
    try:
        d = json.loads(p.read_text())
    except Exception:
        return {}
    out = {}
    for r in d.get("atoms", []):
        key = (r["Z"], r["N"])
        out[key] = {
            "abs_tr_M": r["abs_tr_M"],
            "n_partitions_computed": r["n_partitions_computed"],
            "n_partitions_total": r["n_partitions_total"],
        }
    return out


def b_trm(Z: int, N: int, trm_cache) -> dict:
    data = trm_cache.get((Z, N))
    if not data:
        return {"B": None, "abs_tr_M": None, "coverage": None}
    B = ALPHA_MEV * data["abs_tr_M"]
    cov = f"{data['n_partitions_computed']}/{data['n_partitions_total']}"
    return {"B": B, "abs_tr_M": data["abs_tr_M"], "coverage": cov}


def b_magic_4he(Z: int, N: int) -> dict | None:
    if (Z, N) == (2, 2):
        return {"B": 2 * M_E_MEV * 4 * VOL_BORROMEAN,
                "formula": "2·m_e · 4·8G  [framework: A·8G magic rule]"}
    return None


def chi_sym_alt_closed(Z: int, N: int) -> float:
    A = Z + N
    return -((1.0 + float(H_A_VAL) ** 2 / 4.0) ** (2 * A + 1))


def main():
    w = WitnessBuilder("mass-table-no-fit", engine="closed-form+matrix-trace")
    w.set_description(
        "STRICTLY derivation-only mass table: removes census-picked "
        "(D/T/³He) and α-cluster-fitted c_αα entries.  Only ⁴He carries a "
        "framework-derived Kashaev prediction.  Paper −αΦ₁ and Plancherel-"
        "weighted |tr_M(β)| columns are zero-parameter predictions from the "
        "Wedderburn / Hecke structure alone."
    )
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("m_e_MeV", M_E_MEV)
    w.add_parameter("alpha_mev_paper", ALPHA_MEV)
    w.add_caveat(
        "tr_M column covers only D, T, ³He (n=6, n=9 partitions feasible "
        "in seconds).  ⁴He tr_M needs n=12 (77 partitions) — skipped."
    )

    trm_cache = tr_M_from_witness()

    print("=" * 140)
    print("MASS TABLE — strictly derivation only (no AME-informed knot assignments)")
    print(f"  α = m_e · 8G = {ALPHA_MEV:.6f} MeV   H_A = {float(H_A_VAL):.6f}")
    print("=" * 140)
    print(f"{'atom':<6}{'A':>3}{'B_AME':>11}"
          f"   {'Paper −αΦ₁':>12}{'err%':>8}  "
          f"{'α·|tr_M|':>10}{'err%':>8}  "
          f"{'⁴He magic':>11}{'err%':>8}  "
          f"{'χ_s·χ_a':>10}  notes")
    print("-" * 140)

    rows = []
    for sym, Z, N, B_ame in AME_TABLE:
        A = Z + N
        paper = b_paper(Z, N)
        trm = b_trm(Z, N, trm_cache)
        magic = b_magic_4he(Z, N)
        chi = chi_sym_alt_closed(Z, N)

        def fmt_err(pred):
            if pred is None:
                return f"{'—':>12}", f"{'—':>8}"
            e = (pred - B_ame) / B_ame * 100
            return f"{pred:>+12.4f}", f"{e:>+7.2f}%"

        p_str, p_err = fmt_err(paper["B"]) if paper["B"] is not None else (f"{'—':>12}", f"{'—':>8}")
        t_str = f"{trm['B']:>+10.4f}" if trm["B"] is not None else f"{'—':>10}"
        t_err = (f"{(trm['B']-B_ame)/B_ame*100:>+7.2f}%" if trm["B"] is not None
                 else f"{'—':>8}")
        m_str = f"{magic['B']:>+11.4f}" if magic else f"{'—':>11}"
        m_err = (f"{(magic['B']-B_ame)/B_ame*100:>+7.2f}%" if magic
                 else f"{'—':>8}")
        notes = ""
        if trm.get("coverage"):
            notes = f"tr_M from {trm['coverage']} partitions"

        print(f"{sym:<6}{A:>3}{B_ame:>11.4f}   "
              f"{p_str}{p_err}  {t_str}{t_err}  "
              f"{m_str}{m_err}  {chi:>+10.4f}  {notes}")

        rows.append({
            "atom": sym, "Z": Z, "N": N, "A": A,
            "B_AME": B_ame,
            "paper": paper,
            "tr_M": trm,
            "magic_4he": magic,
            "chi_sym_alt_closed": chi,
        })

    # Mean |err| on atoms with Paper predictions (all 16)
    paper_atoms = [r for r in rows if r["paper"]["B"] is not None]
    mean_err_paper = (sum(abs((r["paper"]["B"] - r["B_AME"]) / r["B_AME"] * 100)
                          for r in paper_atoms) / len(paper_atoms))
    trm_atoms = [r for r in rows if r["tr_M"]["B"] is not None]
    mean_err_trm = (sum(abs((r["tr_M"]["B"] - r["B_AME"]) / r["B_AME"] * 100)
                        for r in trm_atoms) / len(trm_atoms)) if trm_atoms else None

    print("-" * 140)
    print(f"  mean |err|  Paper −αΦ₁ (n={len(paper_atoms)}): {mean_err_paper:.2f}%")
    if mean_err_trm is not None:
        print(f"  mean |err|  α·|tr_M|   (n={len(trm_atoms)}): {mean_err_trm:.2f}%")

    print()
    print("REMOVED (were AME-informed):")
    print("  • D ↔ 6_2, T ↔ 8_11, ³He ↔ L6a4   (census-matched to B_AME/ρ)")
    print("  • α-cluster c_αα = m_e · Vol(7²_1) (c_αα fitted to ¹²C)")
    print("RETAINED (framework-derived):")
    print("  • ⁴He: 2·m_e · 4·8G (A·8G rule from 4 Borromean α-closure)")
    print("  • Paper B = −α·Φ_1 (Wedderburn per-gen algebraic volume)")
    print("  • α·|tr_M| (Plancherel-weighted Hoefsmit char sum)")

    w.add_data("rows", rows)
    w.add_data("mean_err_pct", {"paper": mean_err_paper, "tr_M": mean_err_trm})
    w.save()


if __name__ == "__main__":
    main()
