#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output.
"""
Nucleus real-SDP with bar-fold symmetry reduction — generalizes the
deuteron Phase B (PR #1582) to higher A via the §7b bar-involution.

The deuteron finding (`deuteron_real_sdp.py`): at q_0 the Frobenius Gram
diag(tr_M(P_λ)) is indefinite, and every negative-norm block is the
conjugate λ↦λ' of a positive block with the q-trace sign flipped — the
bar-involution (q↦q⁻¹) / Type-B-folding signature.  That symmetry is the
key to pushing the (3A)! compute wall higher: instead of carrying all
p(3A) blocks, fold conjugate pairs and solve the bounded operator-
selection program on the positive-norm representative subspace.

This script generalizes that to ANY nucleus for which a per-partition
character witness exists, keyed by `--atom`:

  deuteron : iterative-lp-dual-h6-deuteron.witness.json   (H_6,  11 blocks)
  he3      : chi-helium-3-h9-at-q0-50dps.witness.json      (H_9,  30 blocks)
  he4      : chi-helium-4-h12-at-q0-50dps.witness.json     (H_12, partial)

For each it:
  1. Assembles cost t_λ = y_λ·χ^λ and Frobenius diag g_λ = tr_M(P_λ)=y_λ·dim.
  2. Runs the bar-fold symmetry analysis (conjugate pairing + sign flips).
  3. Solves the bounded operator-selection LP on the positive-norm
     subspace (the fold representatives) via the canonical pyhecke dual
     entry point — primal + dual + strong-duality gap.
  4. Reports the reduction ratio  |positive-norm blocks| / |all blocks|.

Output: nucleus-real-sdp-<atom>.witness.json
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
import sys

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke" / "python"))

from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from murnaghan_nakayama import dim_specht  # noqa: E402

# atom → (witness file, loader-kind).  loader-kind selects how to read the
# per-partition cost out of that witness's particular schema.
ATOMS = {
    "deuteron": ("iterative-lp-dual-h6-deuteron.witness.json", "deuteron"),
    "he3": ("chi-helium-3-h9-at-q0-50dps.witness.json", "chi_by_partition"),
    "he4": ("chi-helium-4-h12-at-q0-50dps.witness.json", "chi_by_partition"),
}


def conjugate_partition(part: tuple[int, ...]) -> tuple[int, ...]:
    if not part:
        return ()
    return tuple(sum(1 for r in part if r > j) for j in range(part[0]))


def sanitize_nan(val):
    if isinstance(val, dict):
        return {k: sanitize_nan(v) for k, v in val.items()}
    if isinstance(val, list):
        return [sanitize_nan(x) for x in val]
    if isinstance(val, float) and not math.isfinite(val):
        return None
    return val


def load_cost(atom: str):
    """Return (parts, y, chi, dims, meta) for the atom's character witness."""
    fname, kind = ATOMS[atom]
    raw = json.loads((HERE / fname).read_text())
    data = raw.get("data", raw)

    if kind == "deuteron":
        ydict = data["y_lambda_at_q0"]
        chidict = data["chi_lambda_beta_D_at_q0"]
        keys = list(ydict.keys())
        parts = [tuple(int(p) for p in k.strip("()").rstrip(",").split(",") if p.strip())
                 for k in keys]
        y = np.array([float(ydict[k]) for k in keys])
        chi = np.array([float(chidict[k]) for k in keys])
        meta = {"n_strands": 6, "partial": False}
    elif kind == "chi_by_partition":
        bp = data["by_partition"]
        parts = [tuple(e["partition"]) for e in bp]
        y = np.array([float(e["y_lambda"]) for e in bp])
        chi = np.array([float(e["chi_lambda"]) for e in bp])
        meta = {
            "n_strands": data["n_strands"],
            "partial": bool(data.get("partial")) or
            (data.get("n_partitions_total") is not None and
             data["n_partitions"] != data["n_partitions_total"]),
            "tr_M_at_q0": float(data["tr_M_at_q0"]),
        }
    else:  # pragma: no cover
        raise ValueError(kind)

    dims = [dim_specht(p) for p in parts]
    return parts, y, chi, dims, meta


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atom", choices=sorted(ATOMS), default="he3")
    args = ap.parse_args()
    atom = args.atom

    parts, y, chi, dims, meta = load_cost(atom)
    keys = [str(tuple(p)) for p in parts]
    n_blocks = len(parts)

    t = y * chi                       # cost t_λ = tr_M(P_λ · β)
    frob_diag = y * np.array(dims)    # g_λ = tr_M(P_λ) = y_λ · dim S^λ
    tr_M = float(t.sum())

    # ── bar-fold symmetry analysis ──────────────────────────────────────
    idx_of = {p: i for i, p in enumerate(parts)}
    trM_of = {p: float(frob_diag[i]) for i, p in enumerate(parts)}
    self_conj, sign_flip_pairs, conj_pairs = [], [], 0
    seen = set()
    for p in parts:
        c = conjugate_partition(p)
        if c == p:
            self_conj.append(str(p))
        if c in trM_of and frozenset((p, c)) not in seen and p != c:
            seen.add(frozenset((p, c)))
            conj_pairs += 1
            if (trM_of[p] < 0) != (trM_of[c] < 0):
                sign_flip_pairs.append([str(p), str(c)])
    conjugates_present = all(conjugate_partition(p) in idx_of for p in parts)

    # ── bounded solve on the positive-norm (fold representative) subspace ─
    pos = [i for i, g in enumerate(frob_diag) if g > 0.0]
    pos_keys = [keys[i] for i in pos]
    t_pos = t[pos]
    G_pos = np.diag(frob_diag[pos])
    n_target_pos = float(t_pos.sum())
    lp = solve_operator_selection_lp(t_pos, G_pos, n_target_pos)
    lp_d = lp.to_dict()
    _gap = lp_d.get("duality_gap")
    bounded = (_gap is not None and abs(float(_gap)) < 1e-6
               and bool(lp_d.get("feasible", True)))
    active = [pos_keys[i] for i in lp_d.get("active_set", []) if i < len(pos_keys)]

    reduction = len(pos) / n_blocks if n_blocks else float("nan")

    witness = {
        "engine": "nucleus_real_sdp_barfold",
        "engineVersion": "0.1.0",
        "computation": (
            f"{atom} real-SDP with bar-fold symmetry reduction — bounded "
            "positive-norm-subspace operator-selection. operator-selection-lp / lp-dual."
        ),
        "scriptFile": "nucleus_real_sdp.py",
        "lean_uniqueness_ref": f"qou:QOU.BraidKnot.{atom}_uniqueness_closed",
        "data": {
            "atom": atom,
            "n_strands": meta["n_strands"],
            "n_blocks": n_blocks,
            "partial_character_table": meta["partial"],
            "conjugates_all_present": conjugates_present,
            "tr_M": tr_M,
            # bar-fold symmetry
            "negative_norm_blocks": [keys[i] for i, g in enumerate(frob_diag) if g < 0],
            "self_conjugate_blocks": self_conj,
            "conjugate_pairs": conj_pairs,
            "sign_flip_conjugate_pairs": sign_flip_pairs,
            "barfold_reduction_ratio": reduction,
            "barfold_representatives": pos_keys,
            # bounded subspace solve (primal + dual)
            "positive_norm_subspace_solve": {
                "n_target": n_target_pos,
                "bounded": bounded,
                "strong_duality_holds": bounded,
                "active_blocks": active,
                "y0_star": lp_d.get("y0_star"),
                "y_star": lp_d.get("y_star"),
                "active_set": lp_d.get("active_set"),
                "primal_obj": lp_d.get("primal_obj"),
                "dual_obj": lp_d.get("dual_obj"),
                "duality_gap": lp_d.get("duality_gap"),
            },
            "note": (
                "Full real SDP needs Phase B color-flavor constraints (LR "
                "branching H_{3A} ⊃ (H_3)^Z×(H_3)^N); this is the bar-fold "
                "symmetry-reduced bounded baseline. Partial character tables "
                "cannot close the fold (conjugates absent) — see "
                "conjugates_all_present."
            ),
        },
    }
    out = HERE / f"nucleus-real-sdp-{atom}.witness.json"
    out.write_text(json.dumps(sanitize_nan(witness), indent=2) + "\n")

    print(f"{atom}: {n_blocks} blocks @ H_{meta['n_strands']}  "
          f"(partial table: {meta['partial']}, conjugates present: {conjugates_present})")
    print(f"  tr_M = {tr_M:.10f}")
    print(f"  bar-fold: {len(self_conj)} self-conj, {conj_pairs} conj-pairs, "
          f"{len(sign_flip_pairs)} sign-flipping")
    print(f"  reduction: {len(pos)}/{n_blocks} = {reduction:.3f} (positive-norm representatives)")
    print(f"  subspace solve — bounded: {bounded}  active: {len(active)} blocks")
    print(f"  wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
