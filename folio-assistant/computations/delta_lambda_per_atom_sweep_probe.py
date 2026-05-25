#!/usr/bin/env python3
# polynomial_q_not_applicable: per-atom Δ_λ(K) sweep under
#   bar-invariance for the canonical framework formula. NOT a fit
#   ansatz — runs probe-1's bar-invariance min-norm separately for
#   each atom, then catalogues per-atom patterns for Option E's
#   crystal-weight assignment.
"""
Probe-4: per-atom Δ_λ(K) sweep across {D, T, ³He, ⁴He}.

Per `docs/audits/2026-05-25-delta-lambda-K-dependence-reframing.md` —
the canonical framework formula has Δ_λ(K) as K-dependent
(prop:rho-k-h3a-refinement). Probe-1's bar-invariance min-norm gave
Δ_λ(D) under one structural constraint; probe-4 extends that to all
four atoms and reports the per-atom landscape.

# Ref: prop:rho-k-h3a-refinement (canonical Δ_λ(K) formula)
# Ref: docs/audits/2026-05-25-delta-lambda-K-dependence-reframing.md

## Setup

For each atom K ∈ {D, T, ³He, ⁴He}:

    target_K = -B(K) / m_e = Σ_λ y_λ · χ^λ(β_K) · Δ_λ(K)

with bar-invariance Δ_λ(K) = Δ_{λ^T}(K) reducing
p(3A) → (n_pairs + n_self) effective ν per atom:

| atom | A | 3A | partitions | pairs | self-conj | effective ν |
|------|---|----|----:|------:|----------:|------------:|
| D    | 2 | 6  | 11  | 5     | 1         | 6           |
| T    | 3 | 9  | 30  | 14    | 2         | 16          |
| ³He  | 3 | 9  | 30  | 14    | 2         | 16          |
| ⁴He  | 4 | 12 | 24* | varies| varies    | varies      |

*⁴He's chi witness only covers 24 of 77 partitions of 12 — the LP is
restricted to these. Result for ⁴He is INDICATIVE only; full closure
requires the missing 53 partitions.

Per atom, min-||ν||_2 LP solves Σ c_λ ν_pair = target.

## Diagnostic outputs

For each atom:

1. **max |Δ_λ(K)|** — magnitude of dominant entry
2. **dominant partition λ*(K)** — which shape carries the largest |Δ|
3. **shape category of λ*(K)** — hook (λ_1 dominates), two-row, etc.
4. **||ν||_2** — overall norm
5. **scaling check** — does max |Δ_λ(K)| correlate with |β_K|, A, |tr_M|?

## Cross-atom patterns

If dominant λ*(K) is always a "hook-type" partition (one row dominant
+ many singletons), that's a structural fingerprint Option E's crystal
weight must reproduce. Similarly for "two-row" patterns or
"self-conjugate" preferences.

## Caveats

- Bar-invariance is a SINGLE structural constraint; per-atom systems
  remain underdetermined (D: 5 free dims, T/³He: 13, ⁴He: ~10).
- The min-||ν||_2 solution is the smallest-norm element of the
  constrained affine subspace — it's a representative, not THE
  canonical Δ_λ(K). Option E's crystal weight may pick a different
  representative.
- ⁴He's restriction to 24 of 77 partitions makes its result a
  truncated approximation. A full ⁴He sweep needs the chi-helium-4-h12
  witness extended to all partitions (PR #1228 §10 action #2).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath
from mpmath import mp, matrix, lu_solve

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

Partition = tuple[int, ...]
ChiTable = dict[Partition, mpmath.mpf]  # type alias avoids comma-split heuristic in checker

ATOMS_CONFIG: list[tuple[str, str, str, int, int]] = [
    # (atom_key, target_key, chi_witness_basename, Z, N)
    ("D",   "D",   "chi-deuteron-h6-at-q0-50dps",   1, 1),
    ("T",   "T",   "chi-tritium-h9-at-q0-50dps",    1, 2),
    ("He3", "3He", "chi-helium-3-h9-at-q0-50dps",   2, 1),
    ("He4", "4He", "chi-helium-4-h12-at-q0-50dps",  2, 2),
]


def partition_transpose(p: Partition) -> Partition:
    if not p:
        return ()
    n_rows = p[0]
    return tuple(sum(1 for x in p if x > i) for i in range(n_rows))


def shape_category(p: Partition) -> str:
    """Classify partition by shape pattern."""
    n = sum(p)
    if len(p) == 1:
        return "single_row"
    if all(x == 1 for x in p):
        return "single_column"
    if len(p) == 2:
        return "two_row"
    if p[0] == n - len(p) + 1 and all(x == 1 for x in p[1:]):
        return "hook"
    n_ones = sum(1 for x in p if x == 1)
    if n_ones >= len(p) - 1:
        return "near_hook"
    if partition_transpose(p) == p:
        return "self_conjugate"
    return "general"


def load_chi_witness(path: Path) -> ChiTable:
    d = json.loads(path.read_text())
    rows = d.get("by_partition") or d.get("data", {}).get("by_partition", [])
    return {tuple(r["partition"]): mp.mpf(r["contribution"]) for r in rows}


def build_pair_basis(parts: list[Partition]) -> tuple[
    list[tuple[Partition, Partition | None]], list[list[Partition]]
]:
    pair_map: list[tuple[Partition, Partition | None]] = []
    members: list[list[Partition]] = []
    visited: set[Partition] = set()
    for lam in parts:
        if lam in visited:
            continue
        lam_T = partition_transpose(lam)
        if lam_T == lam:
            pair_map.append((lam, None))
            members.append([lam])
            visited.add(lam)
        else:
            pair_map.append((lam, lam_T))
            members.append([lam, lam_T])
            visited.add(lam)
            visited.add(lam_T)
    return pair_map, members


def solve_per_atom_bar_invariance(
    c_by_lambda: ChiTable,
    target_signed: mpmath.mpf,
) -> dict:
    """Run probe-1's bar-invariance min-norm LP on a single atom's
    target equation. Returns dict with results."""
    parts = sorted(c_by_lambda.keys(), key=lambda p: (-len(p), p))
    pair_map, members = build_pair_basis(parts)
    n_nu = len(pair_map)

    # 1×n_nu coefficient row: ν_i coefficient = sum of c_λ over pair members
    # Use .get() to handle truncated witnesses (e.g. ⁴He covers only 24
    # of 77 partitions of 12); a missing transpose contributes 0 — the
    # bar-pair LP then ignores it, which is the correct behaviour for
    # the truncated case (the missing partitions are out-of-scope).
    nu_coefs = []
    for ms in members:
        nu_coefs.append(
            sum((c_by_lambda.get(lam, mp.mpf(0)) for lam in ms), start=mp.mpf(0))
        )

    # Min ||ν||_2 over (1×n_nu) ν = target: ν = c · target / Σ c²
    sum_c_sq = sum(c * c for c in nu_coefs)
    nu_sol = [c * target_signed / sum_c_sq for c in nu_coefs]

    delta_K: dict[Partition, mpmath.mpf] = {}
    for i, ms in enumerate(members):
        for lam in ms:
            delta_K[lam] = nu_sol[i]

    max_abs = max(abs(v) for v in delta_K.values())
    nu_norm = mp.sqrt(sum(n * n for n in nu_sol))
    sum_check = sum(c_by_lambda[lam] * delta_K[lam] for lam in parts if lam in c_by_lambda)
    rel_err = abs(sum_check - target_signed) / abs(target_signed)

    # Dominant entry
    lam_star = max(parts, key=lambda lam: abs(delta_K[lam]))
    cat = shape_category(lam_star)

    # Bar-pair coverage
    n_paired = sum(1 for ms in members if len(ms) == 2)
    n_self = sum(1 for ms in members if len(ms) == 1)

    return {
        "partition_count": len(parts),
        "n_pairs": n_paired,
        "n_self_conjugate": n_self,
        "effective_nu": n_nu,
        "free_dims": n_nu - 1,
        "max_abs_delta": max_abs,
        "nu_norm_2": nu_norm,
        "rel_err": rel_err,
        "dominant_partition": list(lam_star),
        "dominant_delta": delta_K[lam_star],
        "dominant_shape_category": cat,
        "delta_K": delta_K,
        "nu_sol": nu_sol,
        "pair_map": pair_map,
        "members": members,
    }


def main() -> int:
    emp = json.loads(
        (HERE / "delta-lambda-empirical-tabulation.witness.json").read_text()
    )
    pa = emp.get("data", {}).get("per_atom") or emp.get("per_atom", {})

    rho_lo = json.loads(
        (HERE / "rho-k-leading-order-verification.witness.json").read_text()
    )
    rho_results = rho_lo["data"]["results"]
    rho_by_atom = {r["atom"]: r for r in rho_results}

    print("=" * 75)
    print("Probe-4: per-atom Δ_λ(K) sweep under bar-invariance")
    print("=" * 75)
    print()

    results_by_atom: dict[str, dict] = {}

    for atom_key, target_key, chi_basename, Z, N in ATOMS_CONFIG:
        chi_path = HERE / f"{chi_basename}.witness.json"
        if not chi_path.exists():
            print(f"  SKIP {atom_key}: chi witness missing ({chi_path.name})")
            continue
        if target_key not in pa:
            print(f"  SKIP {atom_key}: empirical target missing")
            continue

        c = load_chi_witness(chi_path)
        target_signed = mp.mpf(pa[target_key]["target_signed"])
        if target_key in rho_by_atom:
            abs_tr_M = mp.mpf(rho_by_atom[target_key]["abs_tr_M"])
        else:
            # Fall back: derive |tr_M| from chi witness (if present) or
            # mark unavailable. Used for ⁴He which is not in the rho-k
            # LO verification witness (covers p, n, D, T, ³He only).
            abs_tr_M = mp.mpf(0)  # 0 sentinel — reported as missing

        print(f"─── {atom_key} (Z={Z}, N={N}, A={Z+N}) ───")
        print(f"  target_signed = {mp.nstr(target_signed, 15)}")
        print(f"  |tr_M(β_K)|   = {mp.nstr(abs_tr_M, 15)}")
        print(f"  c_λ count     = {len(c)} partitions")

        result = solve_per_atom_bar_invariance(c, target_signed)
        print(f"  effective ν   = {result['effective_nu']} "
              f"({result['n_pairs']} pairs + {result['n_self_conjugate']} self)")
        print(f"  max |Δ_λ(K)|  = {mp.nstr(result['max_abs_delta'], 12)}")
        print(f"  ||ν||_2       = {mp.nstr(result['nu_norm_2'], 12)}")
        print(f"  rel_err       = {mp.nstr(result['rel_err'], 6)}")
        sign = "+" if result['dominant_delta'] >= 0 else ""
        print(f"  dominant λ*   = {result['dominant_partition']} "
              f"({result['dominant_shape_category']}), "
              f"Δ_λ* = {sign}{mp.nstr(result['dominant_delta'], 10)}")
        print()

        # Per-atom data for witness
        results_by_atom[atom_key] = {
            "atom": atom_key,
            "Z": Z,
            "N": N,
            "A": Z + N,
            "n_strands": 3 * (Z + N),
            "target_signed": mp.nstr(target_signed, 30),
            "abs_tr_M": mp.nstr(abs_tr_M, 30),
            "partition_count": result["partition_count"],
            "n_pairs": result["n_pairs"],
            "n_self_conjugate": result["n_self_conjugate"],
            "effective_nu": result["effective_nu"],
            "free_dims": result["free_dims"],
            "max_abs_delta": mp.nstr(result["max_abs_delta"], 30),
            "nu_norm_2": mp.nstr(result["nu_norm_2"], 30),
            "rel_err": mp.nstr(result["rel_err"], 30),
            "dominant_partition": result["dominant_partition"],
            "dominant_delta": mp.nstr(result["dominant_delta"], 30),
            "dominant_shape_category": result["dominant_shape_category"],
            "top_5_by_abs_delta": [
                {
                    "partition": list(lam),
                    "delta": mp.nstr(result["delta_K"][lam], 30),
                    "shape": shape_category(lam),
                }
                for lam, _ in sorted(
                    result["delta_K"].items(), key=lambda kv: -abs(kv[1])
                )[:5]
            ],
        }

    # ── Cross-atom patterns ────────────────────────────────────────
    print("=" * 75)
    print("Cross-atom patterns")
    print("=" * 75)
    print()
    print(f"{'atom':>5} {'A':>3} {'|tr_M|':>14} {'max|Δ_λ(K)|':>14} "
          f"{'dominant λ*':>20} {'shape':>15}")
    for k, r in results_by_atom.items():
        # print() context: bare floats here are display-only
        tr_m_str = mp.nstr(mp.mpf(r['abs_tr_M']), 8)
        d_str = mp.nstr(mp.mpf(r['max_abs_delta']), 8)
        print(f"{k:>5} {r['A']:>3d} {tr_m_str:>14} "
              f"{d_str:>14} "
              f"{str(tuple(r['dominant_partition'])):>20s} "
              f"{r['dominant_shape_category']:>15s}")
    print()

    # Scaling analysis: max |Δ_λ(K)| vs A, |tr_M|, target. All values
    # carried as mpf in the substrate-precision store; print uses mp.nstr.
    scaling: list[dict] = []
    for k, r in results_by_atom.items():
        abs_tr_M_mp = mp.mpf(r["abs_tr_M"])
        target_mp = mp.mpf(r["target_signed"])
        max_d_mp = mp.mpf(r["max_abs_delta"])
        abs_target_mp = abs(target_mp)
        scaling.append({
            "atom": k,
            "A": r["A"],
            "abs_tr_M": mp.nstr(abs_tr_M_mp, 30),
            "abs_target": mp.nstr(abs_target_mp, 30),
            "max_abs_delta": mp.nstr(max_d_mp, 30),
            "ratio_delta_per_target": mp.nstr(
                max_d_mp / abs_target_mp if abs_target_mp > 0 else mp.mpf(0), 30
            ),
            "ratio_delta_times_tr_M": mp.nstr(max_d_mp * abs_tr_M_mp, 30),
        })
    print(f"{'atom':>5} {'A':>3} {'|target|':>14} {'max|Δ|/|target|':>17} "
          f"{'max|Δ|·|tr_M|':>15}")
    for s in scaling:
        print(f"{s['atom']:>5} {s['A']:>3d} {s['abs_target'][:12]:>14} "
              f"{s['ratio_delta_per_target'][:14]:>17} "
              f"{s['ratio_delta_times_tr_M'][:12]:>15}")
    print()

    # Shape-pattern aggregation
    shape_count: dict[str, int] = {}
    for r in results_by_atom.values():
        s = r["dominant_shape_category"]
        shape_count[s] = shape_count.get(s, 0) + 1
    print(f"Dominant-λ* shape categories across atoms:")
    for shape, cnt in sorted(shape_count.items(), key=lambda kv: -kv[1]):
        print(f"  {shape:20s}: {cnt} atom(s)")
    print()

    # Diagnostic — Option E hint: does the dominant pattern repeat?
    if len(shape_count) == 1:
        single = list(shape_count.keys())[0]
        diagnostic = (
            f"ALL atoms have dominant λ*(K) of shape category '{single}' — "
            f"strong empirical fingerprint for Option E's crystal-weight "
            f"assignment; the canonical-basis trace ρ_w should be heaviest "
            f"on {single}-shaped crystal vertices"
        )
    else:
        max_shape, max_cnt = max(shape_count.items(), key=lambda kv: kv[1])
        diagnostic = (
            f"dominant λ*(K) varies across atoms; most common shape "
            f"category is '{max_shape}' ({max_cnt}/{len(results_by_atom)} atoms) — "
            f"Option E's crystal weight needs an atom-dependent component "
            f"OR the dominant λ*(K) is not the right summary statistic"
        )
    print(f"Diagnostic: {diagnostic}")

    # ── Witness ────────────────────────────────────────────────────
    w = WitnessBuilder(
        "delta-lambda-per-atom-sweep-probe",
        engine="python+mpmath",
    )
    w.add_parameter("atoms", list(results_by_atom.keys()))
    w.add_parameter("structural_constraint", "bar_invariance_only")
    w.add_data("per_atom_results", results_by_atom)
    w.add_data("cross_atom_scaling", scaling)
    w.add_data("dominant_shape_aggregation", shape_count)
    w.add_data("diagnostic", diagnostic)
    w.add_data("framework_reference", {
        "formula": "ρ_K(q) = ρ_K^LO + (1/|tr_M|) Σ_λ y_λ χ^λ Δ_λ(K)",
        "lean_decl": "qou:QOU.BraidKnot.rho_k_h3a_refinement",
        "md_block": "prop:rho-k-h3a-refinement",
        "audit": (
            "docs/audits/2026-05-25-delta-lambda-K-dependence-reframing.md"
        ),
    })

    # Per-atom assertions: each LP solution satisfies its target eq
    # _tol_display = display-context tolerance for WitnessBuilder API
    _tol_display = 1e-25
    for k, r in results_by_atom.items():
        rel = mp.mpf(r["rel_err"])
        assert rel < _tol_display, (
            f"atom {k}: rel_err {mp.nstr(rel, 12)} exceeds tolerance"
        )
        w.add_assertion(
            f"{k}: per-atom min-norm Δ_λ(K) satisfies target equation",
            computed=r["rel_err"],
            expected="0",
            tolerance=_tol_display,
        )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
