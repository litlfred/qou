"""
path4_rho_K_at_h3A.py — Path 4 investigation: ρ_K from H_{3A} dim_q

Per owner's Path 4 (recommended): test the paper's proposed
structural refinement at `atomic-mass-gb-nf.md` line 131-142:

  "The conjecture must be evaluated at the ATOMIC strand count
   n_0 = 3·A, embedding the braid into H_{3·A}(q_0) through the
   binding operator K(𝔥)."

Hypothesis: ρ_K = dim_q(λ*) at H_{3A}, where λ* is the dominant
Wedderburn block of the binding operator K(𝔥) ⊆ H_{3A}.

Test: for each atom, compute MAX dim_q(λ) over partitions λ ⊢ 3A
at q_0 = 1.1097859... and compare to the empirical ρ_K_CODATA
from `atomic-mass-gb-nf.md` line 60-67:

  proton  A=1  ρ_K_CODATA = 1723.6
  neutron A=1  ρ_K_CODATA = 1991.6
  D       A=2  ρ_K_CODATA = 9453.0
  T       A=3  ρ_K_CODATA = 52828.5
  ³He     A=3  ρ_K_CODATA = 26609.2

If MAX dim_q(λ ⊢ 3A) at H_{3A} ≈ ρ_K_CODATA per atom, the paper's
Path 4 hypothesis is confirmed.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path
from mpmath import mp, mpf
from q_parameter import Q_MP  # noqa: E402 — experimental/proton pin, 50 dps

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

# q_0 pinning — experimental/proton per the 2026-08-07 owner directive.  This
# script compares against proton/neutron rho_K_CODATA, i.e. it is an
# experimental-layer computation, and its manifest entry is physical_proton.
# It previously read q-pinning-50-digit.witness.json directly; that witness is
# MUON-anchored, so the script computed at the ideal pin while declaring the
# experimental one.  Q_MP is the proton pin at the same 50 dps.
q = Q_MP
q_inv = mpf(1) / q
h_q = q - q_inv

# CODATA-fit ρ_K values per atom (from atomic-mass-gb-nf.md table)
RHO_K_CODATA = {
    "proton":  (1, 1723.6),
    "neutron": (1, 1991.6),
    "D":       (2, 9453.0),
    "T":       (3, 52828.5),
    "³He":     (3, 26609.2),
}


def q_int(n: int) -> mpf:
    """Symmetric q-integer [n]_q = (q^n - q^{-n})/(q - q^{-1})."""
    if n == 0:
        return mpf(0)
    return (q**n - q_inv**n) / h_q


def q_fact(n: int) -> mpf:
    """q-factorial [n]_q! = Π_{k=1}^n [k]_q."""
    if n == 0:
        return mpf(1)
    out = mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k)
    return out


def partitions(n: int) -> list[tuple[int, ...]]:
    """All partitions of n as tuples (decreasing parts)."""
    if n == 0:
        return [()]
    res: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, acc: list[int]) -> None:
        if remaining == 0:
            res.append(tuple(acc))
            return
        for p in range(min(remaining, max_part), 0, -1):
            rec(remaining - p, p, acc + [p])

    rec(n, n, [])
    return res


def hook_lengths(shape: tuple[int, ...]) -> list[int]:
    """Hook length per cell of a partition shape."""
    hooks: list[int] = []
    cols = [0] * (shape[0] if shape else 0)
    rows = list(shape)
    for i, row_len in enumerate(rows):
        for j in range(row_len):
            arm = row_len - j - 1
            leg = sum(1 for k in range(i + 1, len(rows)) if rows[k] > j)
            hooks.append(1 + arm + leg)
    return hooks


def dim_q_partition(shape: tuple[int, ...]) -> mpf:
    """q-deformed dimension dim_q(λ) = [n]_q! / Π_{x ∈ λ} [h_x(λ)]_q."""
    n = sum(shape)
    num = q_fact(n)
    den = mpf(1)
    for h in hook_lengths(shape):
        den *= q_int(h)
    return num / den


def main() -> int:
    print("=" * 80)
    print("  Path 4 — ρ_K = dim_q(λ*) at H_{3A}?")
    print("  per atomic-mass-gb-nf.md line 131-142 hypothesis")
    print("=" * 80)
    print(f"  q_0 = {mp.nstr(q, 20)}")
    print()
    print(f"  {'atom':6} {'A':>2} {'n_0=3A':>6} "
          f"{'max dim_q(λ⊢n_0)':>18} {'ρ_K_CODATA':>14} {'ratio':>10}")
    print("  " + "-" * 75)
    results = []
    for atom, (A, rho_k_codata) in RHO_K_CODATA.items():
        n0 = 3 * A
        parts = partitions(n0)
        dims = [(p, dim_q_partition(p)) for p in parts]
        # Sort by magnitude
        dims.sort(key=lambda x: mp.fabs(x[1]), reverse=True)
        max_p, max_d = dims[0]
        ratio = float(rho_k_codata / max_d) if max_d != 0 else float("inf")
        results.append({
            "atom": atom, "A": A, "n_0": n0,
            "max_dim_q_partition": list(max_p),
            "max_dim_q_value": str(max_d),
            "rho_K_CODATA": rho_k_codata,
            "ratio": str(ratio),
        })
        print(f"  {atom:6} {A:>2} {n0:>6} "
              f"{mp.nstr(max_d, 12):>18} {rho_k_codata:>14.1f} {ratio:>10.4f}")

    print()
    print("  Top-5 partitions of n_0 by dim_q for each atom (diagnostic):")
    for atom, (A, _) in RHO_K_CODATA.items():
        n0 = 3 * A
        parts = partitions(n0)
        dims = [(p, dim_q_partition(p)) for p in parts]
        dims.sort(key=lambda x: mp.fabs(x[1]), reverse=True)
        print(f"\n    {atom} (n_0 = {n0}):")
        for p, d in dims[:5]:
            print(f"      λ = {p}, dim_q = {mp.nstr(d, 10)}")

    # Cumulative sum
    print()
    print("  ALTERNATIVE — Σ_λ dim_q(λ)² / [n_0]_q!  (Plancherel-like):")
    for atom, (A, rho_k_codata) in RHO_K_CODATA.items():
        n0 = 3 * A
        parts = partitions(n0)
        sum_dim_sq = sum(dim_q_partition(p) ** 2 for p in parts)
        n0fac = q_fact(n0)
        plancherel_sum = sum_dim_sq / n0fac
        print(f"    {atom:6} A={A}: Σ dim_q² / [n_0]_q! = {mp.nstr(plancherel_sum, 10)}, "
              f"ρ_K_CODATA = {rho_k_codata}")

    print()
    print("  ALTERNATIVE — Σ_λ dim_q(λ)² (unnormalised, just sum of squares):")
    for atom, (A, rho_k_codata) in RHO_K_CODATA.items():
        n0 = 3 * A
        parts = partitions(n0)
        sum_dim_sq = sum(dim_q_partition(p) ** 2 for p in parts)
        ratio = float(rho_k_codata / sum_dim_sq) if sum_dim_sq != 0 else float("inf")
        print(f"    {atom:6} A={A}: Σ dim_q² = {mp.nstr(sum_dim_sq, 12):>18}, "
              f"ρ_K_CODATA = {rho_k_codata:>10.1f}, ratio = {ratio:.4f}")

    # Witness emission
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("path4-rho-K-at-h3A", engine="python+mpmath")
         .set_description("Path 4 hypothesis test: ρ_K = dim_q(λ*) at H_{3A}"))
    w.add_data("q_pinned", str(q))
    w.add_data("hypothesis_max_dim_q", results)
    w.add_data("paper_reference",
               "atomic-mass-gb-nf.md line 131-142 (binding operator K in H_{3A})")

    # Assertion: does the simple max_dim_q rule close ρ_K?
    closes_for_any = any(abs(float(r["ratio"]) - 1.0) < 0.1 for r in results)
    w.add_assertion("max_dim_q_closes_rho_K_for_any_atom",
                    computed=1.0 if closes_for_any else 0.0,
                    expected=0.0)  # we EXPECT it to fail per our analysis
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
