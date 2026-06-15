#!/usr/bin/env python3
# polynomial_q_not_applicable: structural-constraint probe imposing
#   joint multi-atom consistency on Δ_λ. Not a fit ansatz — Δ_λ
#   per-partition is global (atom-independent) by canonical framework
#   assumption; the multi-atom equations test that assumption.
"""
Probe-2: Joint multi-atom Δ_λ LP for closure on the D + T + ³He chain.

Per `docs/audits/2026-05-24-delta-lambda-closure-synthesis-next-step.md`
§3.2 — the second single-session diagnostic probe. Tests whether Δ_λ
is consistent across the small-atom family when treated as a GLOBAL
per-partition quantity:

    For all atoms K, B(K) = m_e · Σ_λ y_λ(q_0) · χ^λ(β_K) · Δ_λ

The same Δ_λ value applies in every atom's equation — D's partitions
⊢ 6 contribute to D's equation; T and ³He's partitions ⊢ 9 contribute
to T and ³He (sharing variables because partitions of 9 don't depend
on the atom). NOT a fit-based ansatz: the global-Δ_λ assumption is
the canonical framework's structural claim; joint multi-atom is the
test of consistency.

# Ref: prop:operator-selection-lp (LP dual infrastructure)
# Ref: docs/audits/2026-05-24-delta-lambda-closure-synthesis-next-step.md §3.2

## Setup

For atoms ∈ {D, T, ³He}:

    target(K) = -B(K) / m_e = Σ_λ c_λ(K) · Δ_λ

where c_λ(K) = y_λ(q_0) · χ^λ(β_K).

Variable structure (after deduplication):

    D's partitions: λ ⊢ 6,  11 distinct shapes
    T's partitions: λ ⊢ 9,  30 distinct shapes (T and ³He SHARE these)

Total: 11 + 30 = 41 unknowns, 3 target equations.

Two LP variants (joint min-||·||_2):

  **Variant A (joint, no bar-invariance)**: 41 unknowns, 3 eqs,
  38 free dimensions, min-||Δ||_2.

  **Variant B (joint + bar-invariance per n)**: Δ_λ = Δ_{λ^T} within
  each n. For n=6: 11 → 6 effective ν (5 pairs + 1 self). For n=9:
  30 → 16 effective ν (14 pairs + 2 self). Total: 22 effective ν,
  3 eqs, 19 free dims.

Diagnostic:

- If variant B's joint solution gives smaller max |Δ_λ| than probe-1's
  D-only result (15.69), the multi-atom consistency tightens the
  closure — Δ_λ has structural cross-atom signal.
- If variant B's joint solution gives LARGER max |Δ_λ|, the global-
  Δ_λ assumption is INCONSISTENT (T or ³He's target conflicts with
  D's at the bar-invariance level).
- The cross-atom residual (sum of squared deviations per atom) is the
  KEY metric.

## Caveats

- D and T/³He have DISJOINT partition sets (different n), so the
  variable space is the direct sum. The "consistency" tested is
  whether a joint min-norm exists, not whether variables overlap.
- Probe assumes χ^λ × y_λ contributions are correctly tabulated in
  the existing chi witnesses. No new χ computation here.
- 19+ free dimensions remain in variant B. Probe-2 is NOT closure;
  it's a diagnostic of cross-atom consistency.
- ⁴He at H_12 is NOT included — only 24 of 77 partitions are in its
  chi witness, so the truncation makes the LP ill-defined. A future
  probe-2-extended will add ⁴He once chi witness covers all 77.

## Result framing

If variant B succeeds with small ||Δ||, the next single-session
probes (probe-2-extended with ⁴He, probe-4 atom-family linearity)
become productive. If variant B requires large ||Δ||, the next
research direction must address atom-dependent Δ_λ (i.e. the global
assumption is wrong and Δ_λ should be Δ_λ(K) — which goes back to
Path B in `2026-05-18-delta-lambda-gating-context.md`).
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


def partition_transpose(p: Partition) -> Partition:
    if not p:
        return ()
    n_rows = p[0]
    return tuple(sum(1 for x in p if x > i) for i in range(n_rows))


def load_chi_witness(path: Path) -> dict[Partition, mpmath.mpf]:
    """Load χ × y per partition from a chi-<atom>-h<n>-at-q0 witness."""
    d = json.loads(path.read_text())
    rows = d.get("by_partition") or d.get("data", {}).get("by_partition", [])
    return {tuple(r["partition"]): mp.mpf(r["contribution"]) for r in rows}


def main() -> int:
    emp = json.loads(
        (HERE / "delta-lambda-empirical-tabulation.witness.json").read_text()
    )
    pa = emp.get("data", {}).get("per_atom") or emp.get("per_atom", {})
    target = {
        "D": mp.mpf(pa["D"]["target_signed"]),
        "T": mp.mpf(pa["T"]["target_signed"]),
        "He3": mp.mpf(pa["3He"]["target_signed"]),
    }
    print("Empirical targets (m_e units):")
    for k, v in target.items():
        print(f"  target_{k} = {mp.nstr(v, 15)}")
    print()

    c_D = load_chi_witness(HERE / "chi-deuteron-h6-at-q0-50dps.witness.json")
    c_T = load_chi_witness(HERE / "chi-tritium-h9-at-q0-50dps.witness.json")
    c_He3 = load_chi_witness(HERE / "chi-helium-3-h9-at-q0-50dps.witness.json")

    parts_n6 = sorted(c_D.keys(), key=lambda p: (-len(p), p))
    parts_n9 = sorted(set(c_T.keys()) | set(c_He3.keys()), key=lambda p: (-len(p), p))

    print(f"Variable space:")
    print(f"  n=6 (D only):     {len(parts_n6)} partitions")
    print(f"  n=9 (T + ³He):    {len(parts_n9)} partitions (shared)")
    print(f"  Total unknowns:   {len(parts_n6) + len(parts_n9)}")
    print(f"  Target equations: 3")
    print()

    # ── Build numeric LP using mpmath matrices (substrate precision) ──
    # Variant A: joint min-||Δ||_2 (no bar-invariance)
    print("─── Variant A: joint multi-atom, no bar-invariance ───")
    all_vars = parts_n6 + parts_n9
    n_vars = len(all_vars)
    var_idx = {p: i for i, p in enumerate(all_vars)}

    A = matrix(3, n_vars)  # zero-initialised mpmath matrix
    b = matrix(3, 1)
    for j, lam in enumerate(parts_n6):
        A[0, j] = c_D[lam]
    for j, lam in enumerate(parts_n9):
        idx = var_idx[lam]
        A[1, idx] = c_T.get(lam, mp.mpf(0))
        A[2, idx] = c_He3.get(lam, mp.mpf(0))
    b[0, 0] = target["D"]
    b[1, 0] = target["T"]
    b[2, 0] = target["He3"]

    # Min-||Δ||_2 over A · Δ = b: Δ = A^T (A A^T)^{-1} b
    # AAT is 3×3 (cheap); LU-solve gives (AAT)^{-1} b at substrate dps
    AAT = A * A.T
    y = lu_solve(AAT, b)  # AAT · y = b, so y = AAT^{-1} b
    delta_A_mat = A.T * y
    delta_A_list = [delta_A_mat[i, 0] for i in range(n_vars)]
    max_abs_A = max(abs(d) for d in delta_A_list)
    norm_A = mp.sqrt(sum(d * d for d in delta_A_list))
    # Residual: ||A · Δ - b||_2
    resid_mat = A * delta_A_mat - b
    resid_norm = mp.sqrt(sum(resid_mat[i, 0] ** 2 for i in range(3)))
    b_norm = mp.sqrt(sum(b[i, 0] ** 2 for i in range(3)))
    rel_err_A = resid_norm / b_norm
    print(f"  max |Δ_λ| = {mp.nstr(max_abs_A, 12)}")
    print(f"  ||Δ||_2   = {mp.nstr(norm_A, 12)}")
    print(f"  rel_err   = {mp.nstr(rel_err_A, 6)}")
    print()

    # Show top-magnitude entries
    top_A = sorted(
        zip(all_vars, delta_A_list), key=lambda kv: -abs(kv[1])
    )[:8]
    print(f"  Top 8 |Δ_λ| (variant A):")
    for lam, val in top_A:
        n = sum(lam)
        sign = "+" if val >= 0 else ""
        print(f"    Δ_{lam!s:18s} (n={n}) = {sign}{mp.nstr(val, 12)}")
    print()

    # ── Variant B: joint + bar-invariance per n ──────────────────
    print("─── Variant B: joint + bar-invariance per n ───")

    def build_pair_basis(parts: list[Partition]) -> tuple[
        list[tuple[Partition, Partition | None]], list[list[Partition]]
    ]:
        """Pair partitions under transpose. Return (pair_map, members)."""
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

    pair_n6, members_n6 = build_pair_basis(parts_n6)
    pair_n9, members_n9 = build_pair_basis(parts_n9)
    print(f"  n=6: {len(pair_n6)} ν (pairs+self) = {len(parts_n6)} Δ_λ")
    print(f"  n=9: {len(pair_n9)} ν (pairs+self) = {len(parts_n9)} Δ_λ")
    print(f"  Total effective ν: {len(pair_n6) + len(pair_n9)}")
    print()

    # ν-space LP: each ν_i represents Δ_λ for all λ in members[i]
    # (each member shares the same Δ value under bar-invariance).
    nu_n6_count = len(pair_n6)
    nu_n9_count = len(pair_n9)
    nu_total = nu_n6_count + nu_n9_count

    AB = matrix(3, nu_total)
    # Row 0: D target — n=6 ν coefficients are SUM of c_λ over the pair
    for i, ms in enumerate(members_n6):
        AB[0, i] = sum((c_D[lam] for lam in ms), start=mp.mpf(0))
    # Row 1: T target — n=9 ν coefficients
    for i, ms in enumerate(members_n9):
        AB[1, nu_n6_count + i] = sum(
            (c_T.get(lam, mp.mpf(0)) for lam in ms), start=mp.mpf(0)
        )
    # Row 2: ³He target — n=9 ν coefficients
    for i, ms in enumerate(members_n9):
        AB[2, nu_n6_count + i] = sum(
            (c_He3.get(lam, mp.mpf(0)) for lam in ms), start=mp.mpf(0)
        )

    # Min ||ν||_2 over AB · ν = b
    ABAT = AB * AB.T
    y_B = lu_solve(ABAT, b)
    nu_sol_mat = AB.T * y_B
    nu_sol = [nu_sol_mat[i, 0] for i in range(nu_total)]
    # Reconstruct full Δ_λ from ν
    delta_B: dict[Partition, mpmath.mpf] = {}
    for i, ms in enumerate(members_n6):
        for lam in ms:
            delta_B[lam] = nu_sol[i]
    for i, ms in enumerate(members_n9):
        for lam in ms:
            delta_B[lam] = nu_sol[nu_n6_count + i]

    max_abs_B = max(abs(v) for v in delta_B.values())
    nu_norm_B = mp.sqrt(sum(n * n for n in nu_sol))
    resid_B_mat = AB * nu_sol_mat - b
    resid_B_norm = mp.sqrt(sum(resid_B_mat[i, 0] ** 2 for i in range(3)))
    rel_err_B = resid_B_norm / b_norm
    print(f"  max |Δ_λ| = {mp.nstr(max_abs_B, 12)}")
    print(f"  ||ν||_2   = {mp.nstr(nu_norm_B, 12)}")
    print(f"  rel_err   = {mp.nstr(rel_err_B, 6)}")
    print()

    # Show top-magnitude entries
    top_B = sorted(
        delta_B.items(), key=lambda kv: -abs(kv[1])
    )[:8]
    print(f"  Top 8 |Δ_λ| (variant B):")
    for lam, val in top_B:
        n = sum(lam)
        sign = "+" if val >= 0 else ""
        print(f"    Δ_{lam!s:18s} (n={n}) = {sign}{mp.nstr(val, 12)}")
    print()

    # ── Comparison vs probe-1 ──────────────────────────────────────
    print("=" * 60)
    print("Scale comparison vs probe-1 + probe-3 + prior ansätze:")
    print("=" * 60)
    print(f"  probe-1 (D bar-invariance min-||ν||_2):     15.694866")
    print(f"  probe-3 variant A (D pin alone):            28.946476")
    print(f"  probe-3 variant B (D pin + bar):            29.457375")
    print(f"  probe-2 variant A (joint multi, no bar):   {mp.nstr(max_abs_A, 10)}")
    print(f"  probe-2 variant B (joint multi + bar):     {mp.nstr(max_abs_B, 10)}")
    print(f"  a_single_block (prior):                     22.959")
    print(f"  b_padded_staircase (prior):                301.521")
    print()

    if max_abs_B < mp.mpf("15.694866"):
        diagnostic = (
            f"joint multi-atom + bar-invariance gives SMALLER max |Δ_λ| "
            f"({mp.nstr(max_abs_B, 6)}) than probe-1 alone (15.695) — "
            f"global-Δ_λ assumption SUPPORTED; multi-atom consistency "
            f"tightens the closure"
        )
        cross_atom_signal = "supports_global_delta"
    elif max_abs_B < mp.mpf("25"):
        diagnostic = (
            f"joint multi-atom + bar-invariance gives ||Δ_λ|| "
            f"({mp.nstr(max_abs_B, 6)}) comparable to probe-1 — global-Δ_λ "
            f"assumption NEUTRAL; no strong cross-atom signal"
        )
        cross_atom_signal = "neutral"
    else:
        diagnostic = (
            f"joint multi-atom + bar-invariance gives LARGER max |Δ_λ| "
            f"({mp.nstr(max_abs_B, 6)}) than probe-1 alone — global-Δ_λ "
            f"assumption WEAKENED; T or ³He may require atom-dependent "
            f"Δ_λ(K) component"
        )
        cross_atom_signal = "weakens_global_delta"

    print(f"Diagnostic: {diagnostic}")
    print(f"Cross-atom signal: {cross_atom_signal}")

    # ── Witness emission ──────────────────────────────────────────
    w = WitnessBuilder(
        "delta-lambda-multi-atom-probe",
        engine="python+mpmath+numpy",
    )
    w.add_parameter("partition_count_n6", len(parts_n6))
    w.add_parameter("partition_count_n9", len(parts_n9))
    w.add_parameter("total_unknowns", n_vars)
    w.add_parameter("target_equations", 3)
    w.add_parameter("atoms", ["D", "T", "3He"])
    w.add_data("targets", {
        "D": mp.nstr(target["D"], 30),
        "T": mp.nstr(target["T"], 30),
        "He3": mp.nstr(target["He3"], 30),
    })
    w.add_data("variant_a_joint_no_bar", {
        "max_abs_delta": mp.nstr(max_abs_A, 30),
        "norm_2": mp.nstr(norm_A, 30),
        "rel_err": mp.nstr(rel_err_A, 30),
        "free_dims": n_vars - 3,
        "top_8": [
            {"partition": list(lam), "n": sum(lam), "delta": mp.nstr(v, 30)}
            for lam, v in top_A
        ],
    })
    w.add_data("variant_b_joint_plus_bar", {
        "max_abs_delta": mp.nstr(max_abs_B, 30),
        "nu_norm_2": mp.nstr(nu_norm_B, 30),
        "rel_err": mp.nstr(rel_err_B, 30),
        "effective_nu_count": nu_total,
        "free_dims": nu_total - 3,
        "top_8": [
            {"partition": list(lam), "n": sum(lam), "delta": mp.nstr(v, 30)}
            for lam, v in top_B
        ],
    })
    w.add_data("scale_comparison_summary", {
        "probe_1_bar_only": "15.694866",
        "probe_2_variant_a": mp.nstr(max_abs_A, 12),
        "probe_2_variant_b": mp.nstr(max_abs_B, 12),
        "probe_3_variant_a": "28.946476",
        "probe_3_variant_b": "29.457375",
        "diagnostic": diagnostic,
        "cross_atom_signal": cross_atom_signal,
    })
    # _tol_display = display-context tolerance for WitnessBuilder API
    _tol_display = 1e-25
    assert rel_err_A < _tol_display, (
        f"variant A rel_err {mp.nstr(rel_err_A, 12)} too large"
    )
    assert rel_err_B < _tol_display, (
        f"variant B rel_err {mp.nstr(rel_err_B, 12)} too large"
    )
    w.add_assertion(
        "variant A (joint, no bar-invariance) satisfies all 3 target equations",
        computed=mp.nstr(rel_err_A, 30),
        expected="0",
        tolerance=_tol_display,
    )
    w.add_assertion(
        "variant B (joint + bar-invariance) satisfies all 3 target equations",
        computed=mp.nstr(rel_err_B, 30),
        expected="0",
        tolerance=_tol_display,
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
