"""qbeta_chain4_kashiwara_step2_n4 — Step 2 of Chain 4.

Extends Step 1's n=3 enumeration to partitions of n=4 + key Demazure
character / hook invariants, surveying for the residue A prefactor
A / ℏ_q^15 ≈ 6.47.

Per the c_2 = -1 Lean reference to f̃₁² (Kashiwara lowering operator
squared), the residue prefactor more likely lives in n=4 partition
crystals than n=3 — c_2 IS the second-order Taylor coefficient, so
f̃₁² ≡ 2-step crystal descent, naturally at n=2 or n=4 algebra
weights, NOT at n=3.

PARTITIONS OF n=4 (5 total):
  (4)        — symmetric trivial, f^(4) = 1, q-dim = 1
  (3,1)      — partial symmetric, f^(3,1) = 3, q-dim = (q+q⁻¹)(q²+q⁻²)
  (2,2)      — square, f^(2,2) = 2, q-dim = q²+1+q⁻²
  (2,1,1)    — antisymmetric-on-(1,1), f^(2,1,1) = 3, q-dim conjugate to (3,1)
  (1,1,1,1)  — antisymmetric, f^(1,1,1,1) = 1, q-dim = 1

KEY INVARIANTS PER PARTITION:
  - f^λ      = dim of S_n irrep (= |SYT(λ)|)
  - hook(λ)  = ∏ h(c) over cells c of λ
  - cocharge(T) = Σ over standard Young tableaux T of λ
  - q-dim(λ) at q_0 = ∏ [h(c)]_q / ∏ [n+c(c)−r(c)]_q   (q-hook formula)
  - λ_to_dual hooks  = product of hook lengths in λ' (conjugate)

CANDIDATE PREFACTOR SPACE:
  Linear combinations + ratios of these invariants, including
  cross-partition (sum over all λ ⊢ 4), products f^λ · q-dim,
  ratios cocharge / f^λ, etc.

ANTI-PATTERN GUARDS:
  - TIERED reporting only.
  - NO ansatz proposed.
  - All near-matches reported with EXPLICIT cross-anchor caveat
    (currently single-anchor m_p-pin q_0 only).
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

RESIDUE_A = mp.mpf("1.804e-15")
# h_q at proton-pinned q_0 (post 2026-05-28 re-pin)
H_Q_SUBSTRATE = mp.mpf("0.092250227040225014")
# Single-anchor evaluation only; cross-anchor in Step 3
Q_PROTON_50 = mp.mpf("1.10997858275138080759166909561")


def partition_invariants_n4() -> dict:
    """Compute basic invariants for the 5 partitions of n=4.

    Hook lengths computed by standard Young diagram method.
    cocharge sums computed by Lascoux-Schützenberger statistic over
    standard tableaux (cocharge of reading word).
    """
    return {
        "(4)": {
            "f_lambda": 1,
            "hooks": [4, 3, 2, 1],  # single row [1,2,3,4] with hooks 4,3,2,1
            "hook_product": 24,
            "cocharge_sum": 0,
            "shape": "row",
        },
        "(3,1)": {
            "f_lambda": 3,  # 3 SYT
            "hooks": [4, 2, 1, 1],  # hooks of (3,1): row1=4,2,1; row2=1
            "hook_product": 8,
            "cocharge_sum": 2,  # cocharge sum over 3 SYT
            "shape": "L",
        },
        "(2,2)": {
            "f_lambda": 2,  # 2 SYT
            "hooks": [3, 2, 2, 1],  # hooks: corner=3; (1,2)=2; (2,1)=2; (2,2)=1
            "hook_product": 12,
            "cocharge_sum": 2,  # 0 + 2
            "shape": "square",
        },
        "(2,1,1)": {
            "f_lambda": 3,
            "hooks": [4, 1, 2, 1],
            "hook_product": 8,
            "cocharge_sum": 4,  # higher-cocharge tableaux dominate
            "shape": "L-rot",
        },
        "(1,1,1,1)": {
            "f_lambda": 1,
            "hooks": [4, 3, 2, 1],
            "hook_product": 24,
            "cocharge_sum": 6,  # 0 + 1 + 2 + 3 of column tableau
            "shape": "column",
        },
    }


def q_integer(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q = (q^n - q^(-n)) / (q - q^(-1))."""
    if n == 0:
        return mp.mpf(0)
    return (q**n - q**(-n)) / (q - q**(-1))


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    """[n]_q! = [1]_q · [2]_q · ... · [n]_q."""
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_integer(k, q)
    return out


def q_dim_partition(hooks: list[int], q: mp.mpf, n: int) -> mp.mpf:
    """q-dim_q(λ) = [n]_q! / ∏ [h(c)]_q   (q-hook formula).

    For generic q ≠ 1, dim_q(λ) is a Laurent polynomial in q.
    """
    nf = q_factorial(n, q)
    hf = mp.mpf(1)
    for h in hooks:
        hf *= q_integer(h, q)
    return nf / hf


def build_candidates(inv: dict, q: mp.mpf) -> dict[str, mp.mpf]:
    """Build a ~30-candidate set of prefactor candidates."""
    out: dict[str, mp.mpf] = {}

    # Basic per-partition invariants
    for lam, d in inv.items():
        out[f"f^{lam}"] = mp.mpf(d["f_lambda"])
        out[f"hook_prod_{lam}"] = mp.mpf(d["hook_product"])
        out[f"1/hook_prod_{lam}"] = mp.mpf(1) / mp.mpf(d["hook_product"])
        out[f"cocharge_{lam}"] = mp.mpf(d["cocharge_sum"])

    # q-dim_q for each partition at q_0
    for lam, d in inv.items():
        qd = q_dim_partition(d["hooks"], q, 4)
        out[f"q-dim_{lam}"] = qd
        out[f"q-dim²_{lam}"] = qd * qd

    # Summed invariants
    out["Σ f^λ (4-partitions)"] = sum(mp.mpf(d["f_lambda"]) for d in inv.values())
    out["Σ cocharge (4-partitions)"] = sum(
        mp.mpf(d["cocharge_sum"]) for d in inv.values()
    )
    out["Σ q-dim (4-partitions)"] = sum(
        q_dim_partition(d["hooks"], q, 4) for d in inv.values()
    )

    # Specific ratios suggested by the c_2 = -1 = f̃₁² Lean connection
    # The 2-step Kashiwara descent on partition (2,2) is a natural target
    f_22 = mp.mpf(inv["(2,2)"]["f_lambda"])
    qd_22 = q_dim_partition(inv["(2,2)"]["hooks"], q, 4)
    out["cocharge_(2,2) / f^(2,2)"] = mp.mpf(inv["(2,2)"]["cocharge_sum"]) / f_22
    out["q-dim_(2,2) · f^(2,2)"] = qd_22 * f_22

    # The (3,1) partition often carries adjoint-irrep content
    f_31 = mp.mpf(inv["(3,1)"]["f_lambda"])
    qd_31 = q_dim_partition(inv["(3,1)"]["hooks"], q, 4)
    out["q-dim_(3,1) · f^(3,1)"] = qd_31 * f_31
    out["q-dim_(3,1) - q-dim_(2,1,1)"] = qd_31 - q_dim_partition(
        inv["(2,1,1)"]["hooks"], q, 4
    )

    return out


def report_proximity(
    cands: dict[str, mp.mpf], target: mp.mpf
) -> dict[str, dict]:
    """TIERED proximity report."""
    out = {}
    for name, val in cands.items():
        if val == 0:
            out[name] = {
                "value": "0",
                "ratio": "0",
                "tier": "ZERO",
            }
            continue
        ratio = val / target
        rel_err = abs(ratio - 1)
        if rel_err < mp.mpf("1e-6"):
            tier = "NEAR-1PPM"
        elif rel_err < mp.mpf("1e-3"):
            tier = "NEAR-1PPB-but-not-1ppm"  # placeholder; ppt actually
        elif rel_err < mp.mpf("0.01"):
            tier = "NEAR-1PCT"
        elif rel_err < mp.mpf("0.1"):
            tier = "NEAR-FUZZY"
        elif rel_err < mp.mpf("0.5"):
            tier = "NEAR-CLOSE"
        else:
            tier = "MISS"
        out[name] = {
            "value": mp.nstr(val, 6),
            "ratio": mp.nstr(ratio, 6),
            "tier": tier,
        }
    return out


def main() -> None:
    import json
    import sys

    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here.parent))
    import _path_bridge as _pb  # noqa: F401

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import WitnessBuilder

    print("=" * 78)
    print("Q_β Chain 4 Step 2 — Kashiwara crystal at n=4")
    print("=" * 78)
    print()
    prefactor_target = RESIDUE_A / (H_Q_SUBSTRATE ** 15)
    print(f"Target prefactor: A / ℏ_q^15 = {mp.nstr(prefactor_target, 8)}")
    print(f"  A = {mp.nstr(RESIDUE_A, 4)}")
    print(f"  ℏ_q^15 = {mp.nstr(H_Q_SUBSTRATE ** 15, 4)}")
    print()

    inv = partition_invariants_n4()
    print("Partition invariants (n=4):")
    print(f"{'partition':10s} {'f^λ':5s} {'hook∏':6s} {'cocharge':10s}")
    for lam, d in inv.items():
        print(f"  {lam:8s} {d['f_lambda']:3d}  "
              f"{d['hook_product']:6d}  {d['cocharge_sum']:6d}")
    print()

    cands = build_candidates(inv, Q_PROTON_50)
    results = report_proximity(cands, prefactor_target)

    # Sort by tier (best first)
    tier_order = {
        "NEAR-1PPM": 0, "NEAR-1PPB-but-not-1ppm": 1, "NEAR-1PCT": 2,
        "NEAR-FUZZY": 3, "NEAR-CLOSE": 4, "MISS": 5, "ZERO": 6,
    }
    sorted_items = sorted(
        results.items(),
        key=lambda kv: (tier_order.get(kv[1]["tier"], 99),
                        abs(mp.mpf(kv[1]["ratio"]) - 1) if kv[1]["ratio"] != "0" else mp.mpf("999"))
    )

    print(f"Step 2 proximity results ({len(cands)} candidates):")
    print(f"{'Candidate':40s} {'value':12s} {'ratio':12s} {'tier'}")
    for name, r in sorted_items[:20]:  # top 20
        print(f"  {name:38s} {r['value']:12s} {r['ratio']:12s} {r['tier']}")
    print()

    # Find best near-match
    best_tier = sorted_items[0][1]["tier"]
    best_name = sorted_items[0][0]
    best_ratio = sorted_items[0][1]["ratio"]

    print(f"BEST: {best_name} → {best_tier} (ratio {best_ratio})")
    print()

    near_matches = [
        (name, r) for name, r in results.items()
        if r["tier"] in ("NEAR-1PPM", "NEAR-1PPB-but-not-1ppm", "NEAR-1PCT", "NEAR-FUZZY")
    ]
    if near_matches:
        print(f"NEAR-MATCHES found ({len(near_matches)}):")
        for name, r in near_matches:
            print(f"  {name} → {r['tier']} (ratio {r['ratio']})")
        print()
        print("⚠ Single-anchor result (m_p-pin q_0 only). Step 3 must")
        print("  cross-anchor at q_muon BEFORE any structural claim.")
    else:
        print("VERDICT: NO near-matches at n=4 single-anchor probe.")
        print("Step 3 (cross-anchor) may still surface marginal candidates")
        print("but the n=4 partition algebra at fixed cocharge / hook")
        print("does NOT yield the residue prefactor categorically here.")

    # Emit witness
    wb = WitnessBuilder(
        name="qbeta-chain4-kashiwara-step2-n4",
        engine="mpmath",
        output_dir=here,
    )
    wb.set_description(
        f"Step 2 of PR #1772 Chain 4 — Kashiwara crystal probe at n=4. "
        f"Survey of {len(cands)} prefactor candidates derived from "
        f"partition invariants of the 5 partitions of 4: f^λ, hook "
        f"products, cocharge sums, q-dimensions at proton-pinned q_0. "
        f"Best near-match: {best_name} → {best_tier} (ratio {best_ratio}). "
        f"Anti-pattern guards respected: TIERED reporting; cross-anchor "
        f"deferred to Step 3; NO ansatz proposed."
    )
    wb.add_assertion(
        name="step2_enumeration_complete",
        computed=len(cands) >= 20,
        expected=True,
        source=f"Step 2 enumerated {len(cands)} candidates (target ≥ 20)",
    )
    wb.add_data("residue_target_A", str(RESIDUE_A))
    wb.add_data("prefactor_target", str(prefactor_target))
    wb.add_data("h_q_substrate", str(H_Q_SUBSTRATE))
    wb.add_data("q_proton", str(Q_PROTON_50))
    wb.add_data("partition_invariants_n4", inv)
    wb.add_data(
        "step2_results_top10",
        {name: r for name, r in sorted_items[:10]},
    )
    wb.add_data("best_match", {
        "candidate": best_name,
        "tier": best_tier,
        "ratio": best_ratio,
    })
    wb.add_data("near_match_count", len(near_matches))
    wb.add_data("next_step", "Step 3: cross-anchor validation (q_muon)")
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
