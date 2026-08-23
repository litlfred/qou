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

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import argparse
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
import sys

sys.path.insert(0, str(HERE))
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in _Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    _Path(__file__).resolve().parent,
)
sys.path.insert(0, str(_QOU_REPO_ROOT / "tools" / "pyhecke" / "python"))

from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from murnaghan_nakayama import dim_specht  # noqa: E402
from nucleus_sdp_assembly import cost_gram_from_arrays  # noqa: E402

# ── Nucleus registry ────────────────────────────────────────────────────
# A nucleus is (Z, N); strand count n = 3·A = 3·(Z+N). The cost has two
# factors per Wedderburn block λ ⊢ n:
#   * y_λ  — the Wenzl weight d_q(λ)²/[n]_q!.  Depends ONLY on (n, q_0),
#            NOT on the nucleus → resolved generically from a Wenzl source
#            keyed by n (`wenzl-y-lambda-h{n}.witness.json` etc.).
#   * χ_λ  — the per-nucleus character χ^λ(β_K).  Nucleus-specific → comes
#            from a per-nucleus character witness.
# To add a nuclide: append (Z, N, chi_source). y_λ is automatic if a Wenzl
# source for that n exists; otherwise the run reports the missing source.
NUCLEI = {
    # A=1 nucleons (n=3, complete H_3 table). χ witnesses carry inline
    # 50-dps y_λ + χ_λ in `by_partition`, so the bar-fold solve runs with
    # zero recompute — the smallest shell of the per-nucleus census.
    "proton":   dict(Z=1, N=0, chi="chi-proton-h3-at-q0-50dps.witness.json"),
    "neutron":  dict(Z=0, N=1, chi="chi-neutron-h3-at-q0-50dps.witness.json"),
    "deuteron": dict(Z=1, N=1, chi="iterative-lp-dual-h6-deuteron.witness.json"),
    "he3":      dict(Z=2, N=1, chi="chi-helium-3-h9-at-q0-50dps.witness.json"),
    "tritium":  dict(Z=1, N=2, chi="chi-tritium-h9-at-q0-50dps.witness.json"),
    # He-4: full 77-partition table (existing infra) + Wenzl y_λ for n=12.
    "he4":      dict(Z=2, N=2, chi="chi-lambda-he4-full-partition-table.witness.json"),
}

# Wenzl y_λ sources keyed by strand count n (existing infra, q_0-pinned).
# Generic: any nucleus at strand count n reuses the same y_λ table.
YLAMBDA_SOURCES = {
    12: "wenzl-y-lambda-h12.witness.json",
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


def _norm(part) -> tuple[int, ...]:
    """Normalize a partition (list or '(a, b)' string) to a tuple."""
    if isinstance(part, str):
        return tuple(int(p) for p in part.strip("()[]").split(",") if p.strip())
    return tuple(int(x) for x in part)


def extract_chi(data: dict) -> dict[tuple, float]:
    """Pull {partition: χ^λ} from any of the per-nucleus witness schemas.

    Handles: deuteron's `chi_lambda_beta_D_at_q0` dict, the
    `by_partition` list (he3/he4-partial), and the full-table
    `per_partition_chi_lambda` list (he4-full).  Schema-agnostic so new
    nuclei drop in without a per-atom loader branch.
    """
    if "chi_lambda_beta_D_at_q0" in data:
        return {_norm(k): float(v) for k, v in data["chi_lambda_beta_D_at_q0"].items()}
    for container in ("by_partition", "per_partition_chi_lambda", "per_partition"):
        if container in data and isinstance(data[container], list):
            out = {}
            for e in data[container]:
                p = _norm(e["partition"])
                # chi field name varies across schemas
                for ck in ("chi_lambda", "chi_lambda_he4", "chi", "chi_lambda_at_q0"):
                    if ck in e:
                        out[p] = float(e[ck])
                        break
            if out:
                return out
    raise KeyError("no recognized χ container in witness")


def resolve_y_lambda(parts: list[tuple], n: int, chi_data: dict) -> dict[tuple, float]:
    """y_λ for every block, generic in (n, q_0) — NOT nucleus-specific.

    Order of resolution:
      1. inline in the χ witness (deuteron `y_lambda_at_q0`, or a
         `by_partition` list carrying `y_lambda`), else
      2. the Wenzl source for strand count n (`YLAMBDA_SOURCES[n]`).
    Raises if neither covers all blocks — the run then reports exactly
    which y_λ source is missing for that n.
    """
    # (1) inline
    if "y_lambda_at_q0" in chi_data:
        ydict = {_norm(k): float(v) for k, v in chi_data["y_lambda_at_q0"].items()}
        if all(p in ydict for p in parts):
            return ydict
    for container in ("by_partition", "per_partition"):
        if container in chi_data and isinstance(chi_data[container], list) \
                and all("y_lambda" in e for e in chi_data[container]):
            ydict = {_norm(e["partition"]): float(e["y_lambda"])
                     for e in chi_data[container]}
            if all(p in ydict for p in parts):
                return ydict
    # (2) Wenzl source by n
    src = YLAMBDA_SOURCES.get(n)
    if src and (HERE / src).exists():
        wdata = json.loads((HERE / src).read_text())
        wdata = wdata.get("data", wdata)
        wlist = wdata.get("per_partition", [])
        ydict = {_norm(e["partition"]): float(e["y_lambda"]) for e in wlist}
        if all(p in ydict for p in parts):
            return ydict
    raise KeyError(
        f"no y_λ source covers all {len(parts)} blocks at n={n}; "
        f"add a Wenzl source to YLAMBDA_SOURCES[{n}]"
    )


def load_cost(atom: str):
    """Return (parts, y, chi, dims, meta) for the nucleus — generic resolver."""
    spec = NUCLEI[atom]
    Z, N = spec["Z"], spec["N"]
    n = 3 * (Z + N)
    raw = json.loads((HERE / spec["chi"]).read_text())
    data = raw.get("data", raw)

    chi_map = extract_chi(data)
    parts = sorted(chi_map.keys(), key=lambda p: (-sum(p), p))
    y_map = resolve_y_lambda(parts, n, data)

    chi = np.array([chi_map[p] for p in parts])
    y = np.array([y_map[p] for p in parts])
    dims = [dim_specht(p) for p in parts]

    # full table = all p(n) partitions present?  (completeness, not the old
    # "partial" flag that just meant the upstream witness was truncated)
    n_partitions_total = num_partitions(n)
    complete = (len(parts) == n_partitions_total)
    meta = {
        "n_strands": n, "Z": Z, "N": N, "A": Z + N,
        "partial": not complete,
        "n_partitions": len(parts),
        "n_partitions_total": n_partitions_total,
    }
    return parts, y, chi, dims, meta


def num_partitions(n: int) -> int:
    """p(n) via Euler's pentagonal recurrence (no sympy dependency)."""
    p = [1] + [0] * n
    for i in range(1, n + 1):
        k, total = 1, 0
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > i and g2 > i:
                break
            sign = -1 if k % 2 == 0 else 1
            if g1 <= i:
                total += sign * p[i - g1]
            if g2 <= i:
                total += sign * p[i - g2]
            k += 1
        p[i] = total
    return p[n]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atom", choices=sorted(NUCLEI), default="he3")
    args = ap.parse_args()
    atom = args.atom

    parts, y, chi, dims, meta = load_cost(atom)
    keys = [str(tuple(p)) for p in parts]
    n_blocks = len(parts)

    # cost t_λ = y_λ·χ^λ + Frobenius Gram g_λ = y_λ·dim via the shared core.
    _cg = cost_gram_from_arrays(keys, parts, dims, y, chi)
    t, frob_diag, tr_M = _cg.t, _cg.frob_diag, _cg.tr_M

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
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` — and a witness without one cannot be
    # compared against its producer, so it drops OUT of the self-staleness
    # audit and reads as "not stale" forever. Regenerating it then looks
    # like progress while removing it from the count: a false drain.
    # Full rationale and the detector: computations/witness_drain_audit.py.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched, so consumers
    # of legacy `assertions` records (which key on `label`, not `name`) do
    # not have to change. `engine` is passed back from the payload because
    # the helper overwrites it, and a descriptive engine string is worth
    # keeping.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", 'numpy'))
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
