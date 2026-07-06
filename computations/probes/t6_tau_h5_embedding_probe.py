#!/usr/bin/env python3
"""
T6 tau probe — recompute V̂_τ at H_5 (5-strand) instead of H_3.

Per PR #1127's lepton-tower H_n+1 branching conjecture
([conj:lepton-tower-h-n-plus-1-branching](
../../content/quantum-observable-universe/braids-and-knots/conj-lepton-tower-h-n-plus-1-branching.md)):
muon (m=2) closes at H_3+1 = H_4 std rep (3,1) factor [3]_q · [2]_q / [4]_q.
By analogy, tau (m=3) should close at H_4+1 = H_5 std rep (4,1) factor.

The tau braid T(2,7) = σ_1^7 lives naturally in H_2. Previous T6
attempts used H_3 3-channel Plancherel weights (analog of electron),
yielding V̂_τ = 1.119 > q_0 = 1.110 — OUTSIDE Li_2^q convergence
radius (diverges).

This probe applies per_generator_V_hat_general with n_strands=5
(H_5 5-strand embedding) to:
  1. Verify V̂_τ stays in convergence radius |V̂| < q_0
  2. Compute m_τ via canonical Li_2^q per-braid mass tower
  3. Compare to CODATA m_τ/m_e = 3477.23
  4. Test whether ξ_3 = [4]_q · [2]_q / [5]_q · (1/ℏ_q²) closes
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from per_generator_V_hat_general import (
    per_generator_V_hat_general,
    li2q_mpmath,
)


def main() -> int:
    mp.mp.dps = 50

    Vol_4_1 = mp.mpf("2.0298832128193072500424051085490405718833786150606")
    cal2_target = M_MU_OVER_M_E
    cal_tau_e = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    h = q0 - 1 / q0
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))

    print(f"=== Substrate ===")
    print(f"  q_0 = {float(q0):.10f}, h = {float(h):.6f}, z = {float(z):.6f}")
    print()

    # Test tau braid σ_1^7 at H_2, H_3, H_5
    print(f"=== V̂_τ for σ_1^7 at different H_n embeddings ===")
    print(f"{'n_strands':>10s}  {'V̂_1':>14s}  {'in convergence radius?':>25s}")
    print("-" * 60)

    results_by_n = {}
    for n_strands in [2, 3, 4, 5, 6]:
        word = [(1.0, 0.0, 0)] * 7  # σ_1^7
        V_data = per_generator_V_hat_general(n_strands, word)
        V_1 = V_data[0]["full"] if V_data else 0.0
        in_radius = abs(V_1) < float(q0)
        print(f"  {n_strands:10d}  {V_1:+14.6f}  {'YES ✓' if in_radius else 'NO ✗':>25s}")
        results_by_n[n_strands] = {"V_1": V_1, "in_radius": in_radius}
    print()

    # Compute m_τ via canonical Li_2^q tower for each H_n where V is in radius
    print(f"=== m_τ via canonical Li_2^q tower (descended-dropped) ===")
    print(f"{'n_strands':>10s}  {'V̂_1':>10s}  {'m_τ_dim':>12s}  {'ratio m_τ/m_e (computed)':>22s}")
    print("-" * 70)

    # m_e via H_3 3-channel (paper convention)
    # Per pyhecke V_HAT_ELECTRON formula:
    a3, b3 = mp.mpf(0), mp.mpf(1)
    for _ in range(3):
        a3, b3 = a3 * h + b3, a3
    two_q = q0 + 1/q0
    three_q = q0**2 + 1 + (1/q0)**2
    qfac_3 = two_q * three_q
    W_SYM_h3 = mp.mpf(1) / qfac_3
    W_STD_h3 = two_q * two_q / qfac_3
    W_ALT_h3 = mp.mpf(1) / qfac_3
    V_e_h3 = W_SYM_h3 * q0**3 + W_STD_h3 * (z * a3 + b3) + W_ALT_h3 * (-(1/q0))**3
    m_e_dim_li2q = -li2q_mpmath(-mp.fabs(V_e_h3), q0)

    print(f"  (electron V̂_e via H_3 3-channel = {float(V_e_h3):.6f}, m_e_dim = {float(m_e_dim_li2q):.6f})")
    print()

    for n_strands, data in results_by_n.items():
        if not data["in_radius"]:
            print(f"  {n_strands:10d}  {data['V_1']:+10.4f}  {'DIVERGES':>12s}  {'—':>22s}")
            continue
        m_tau_dim = -li2q_mpmath(-mp.fabs(mp.mpf(data["V_1"])), q0)
        ratio = m_tau_dim / m_e_dim_li2q
        data["m_tau_dim"] = float(m_tau_dim)
        data["ratio"] = float(ratio)
        print(f"  {n_strands:10d}  {data['V_1']:+10.6f}  {float(m_tau_dim):+12.6f}  {float(ratio):+22.4f}")
    print()

    print(f"  CODATA m_τ/m_e = {float(cal_tau_e):.4f}")
    print()

    # For H_5 (predicted optimal per conj:lepton-tower-h-n-plus-1-branching):
    # ξ_3 predicted = [4]_q · [2]_q / [5]_q · (1/ℏ_q²)
    four_q = q0**3 + q0 + 1/q0 + (1/q0)**3
    five_q_poly = q0**4 + q0**2 + 1 + (1/q0)**2 + (1/q0)**4
    xi_3_conjectural = four_q * two_q / five_q_poly / hbar_q_sq

    print(f"=== ξ_3 conjectural form check ===")
    print(f"  [4]_q · [2]_q / [5]_q = {float(four_q * two_q / five_q_poly):.6f}")
    print(f"  / ℏ_q² = {float(four_q * two_q / five_q_poly / hbar_q_sq):.6f}")
    print(f"  ξ_3 conjectural = {float(xi_3_conjectural):.4f}")
    print()

    if 5 in results_by_n and results_by_n[5]["in_radius"]:
        ratio_h5 = mp.mpf(str(results_by_n[5]["ratio"]))
        predicted_m_tau = ratio_h5 * xi_3_conjectural
        rel_err = (predicted_m_tau - cal_tau_e) / cal_tau_e * 100
        print(f"=== Tau closure check at H_5 ===")
        print(f"  m_τ predicted = (ratio_h5) · ξ_3 = {float(ratio_h5):.4f} · {float(xi_3_conjectural):.4f}")
        print(f"                = {float(predicted_m_tau):.4f}")
        print(f"  CODATA        = {float(cal_tau_e):.4f}")
        print(f"  Rel. error    = {float(rel_err):+.4f}%")
        verdict = "CLOSE (< 5%)" if abs(float(rel_err)) < 5 else "OFF"
        print(f"  Verdict       = {verdict}")
    else:
        print(f"  Cannot compute tau closure: V̂_τ at H_5 not in convergence radius")

    # Witness
    witness = {
        "description": "T6 tau probe — H_5 embedding test for V̂_τ + ξ_3 conjectural closure",
        "computation": "t6_tau_h5_embedding_probe",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "purpose": "Test PR #1127's conj:lepton-tower-h-n-plus-1-branching at m=3 (tau)",
            "method": "per_generator_V_hat_general at n_strands ∈ {2,3,4,5,6} for σ_1^7 word",
            "comparison_against": "CODATA m_τ/m_e = 3477.23",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z": str(z),
            "ℏ_q²": str(hbar_q_sq),
            "V_e_h3_3channel": str(V_e_h3),
            "m_e_dim_li2q": str(m_e_dim_li2q),
            "[4]_q · [2]_q / [5]_q": str(four_q * two_q / five_q_poly),
            "xi_3_conjectural": str(xi_3_conjectural),
            "CODATA_m_tau_e": str(cal_tau_e),
        },
        "tau_per_h_n": {
            str(n): {
                "V_1": str(d["V_1"]),
                "in_convergence_radius": d["in_radius"],
                "m_tau_dim": d.get("m_tau_dim"),
                "ratio_m_tau_over_m_e": d.get("ratio"),
            }
            for n, d in results_by_n.items()
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    here = Path(__file__).resolve().parent
    out = here / "t6-tau-h5-embedding-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
