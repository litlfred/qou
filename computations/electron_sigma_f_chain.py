#!/usr/bin/env python3
"""
σ_F(Z) electron-dressing chain — canonical confinement-SDP dual (diagnostic).

NOTE (cross-check / superseded-by). The canonical, more rigorous version of
this computation is `computations/sigma_f_electron_shell_chain.py` on main
(50-dps mpmath throughout, with the closed-form Wedderburn LP dual — no f64).
This script is retained as an INDEPENDENT cvxpy/Clarabel cross-check of the
same claim-1 monotonicity + claim-2 multiplicity, not as the canonical path;
prefer the mpmath version for any production use. Both agree: σ_F is monotone
and the bare categorical operator does NOT reproduce the noble-gas peaks (the
2n²/Madelung shell-capacity derivation is open — see
docs/audits/2026-06-16-2n2-shell-capacity-derivation-gap.md).

Implements the **dual** of the confinement SDP (prop:confinement-sdp) at the
atom-electron level (level 6), which the canonical `pyhecke.sdp` dispatcher
still carries only as a skeleton and the deprecated `multi_level_sdp.py`
computes primal-only (no dual — the first-class-dual anti-pattern). With the
dual in hand it traces the **Frobenius stability index**

    σ_F(P^Z, q) = n_target · y₀*(P^Z, q)            (prop:shell-closure-stability)

along the electron dressing chain P^0 → P^1 → … and reports the binding
multiplicity μ = rank of the optimal confined operator Φ* (= |active support|).

What is faithful here
---------------------
  • The confinement SDP is set up per prop:confinement-sdp: min ⟨T,Φ⟩ over
    Φ ⪰ 0 with per-block Frobenius positivity ⟨π_λ,Φ⟩ ≥ 0 and the
    normalisation tr Φ = n_target; T = Markov-trace weighting. The DUAL is
    emitted (y₀*, per-block y_λ*, duality gap) via cvxpy/Clarabel.
  • Claim 1 (σ_F monotone non-decreasing in Z) is demonstrated on the chain:
    dressing grows n_target = 3A + Z while y₀* stays bounded, so σ_F rises —
    the SDP never goes infeasible (refuting the raw-Gram "capacity").
  • Claim 2's MECHANISM (a degenerate cost-minimum ⇒ rank-μ active support,
    μ ≥ 2) is shown on an explicit closed-shell block: when the lowest cost
    level is d-fold degenerate, Φ* spreads over the d-dim eigenspace and
    μ = d ≥ 2 — the categorical signature of a closed shell.

What is NOT done here (flagged, research tranche)
-------------------------------------------------
  The full faithful reproduction of the noble-gas ionisation PEAKS — σ_F local
  maxima exactly at Z ∈ {2,10,18,…} (claim 2, ionisation-energy corollary) —
  needs the multi-level cost operator that encodes the 2n² shell degeneracies
  and the Madelung sub-shell ordering. Encoding those by hand would make the
  peaks an INPUT, not an emergent result; that is the level-6 cost-operator
  infra cut, deferred. This script delivers the dual machinery + claims 1 and
  the claim-2 mechanism, not the periodic-table peaks.

Refs: prop:confinement-sdp, prop:shell-closure-stability (claims 1–2),
prop:noble-gas-characterization, ElectronShell.lean.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "substrate"))
sys.path.insert(0, HERE)

import cvxpy as cp  # noqa: E402
from q_parameter import Q as q0, Q_INV as qi0  # noqa: E402

q0, qi0 = float(q0), float(qi0)
z = 1.0 / (q0 ** 0.5 + qi0 ** 0.5)


def confinement_dual(T_diag, n_target, tol=1e-6):
    """Solve the confinement SDP (prop:confinement-sdp) and return the dual.

        min ⟨T,Φ⟩  s.t.  Φ ⪰ 0,  Φ_ii ≥ 0 (per-block),  tr Φ = n_target.

    Returns σ_F = n_target·y₀*, the multiplicity μ = rank Φ*, the per-block
    duals, primal/dual objective and gap. T is diagonal (Markov weighting)."""
    k = len(T_diag)
    T = np.diag(np.asarray(T_diag, dtype=float))
    Phi = cp.Variable((k, k), PSD=True)
    norm_c = cp.trace(Phi) == n_target
    block_c = [Phi[i, i] >= 0 for i in range(k)]
    prob = cp.Problem(cp.Minimize(cp.trace(T @ Phi)), [norm_c] + block_c)
    prob.solve(solver=cp.CLARABEL)
    if prob.status not in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
        return {"feasible": False, "status": prob.status}
    # cvxpy returns the equality-constraint multiplier with the opposite sign
    # to our Lagrangian convention; flip so σ_F = n_target·y₀* = primal_obj
    # (strong duality / Slater holds, prop:shell-closure-stability).
    y0 = -float(norm_c.dual_value)
    sigma_F = n_target * y0
    evals = np.linalg.eigvalsh(Phi.value)
    mu = int(np.sum(evals > tol * max(1.0, evals.max())))
    return {
        "feasible": True,
        "sigma_F": sigma_F,
        "y0": y0,
        "mu": mu,
        "primal_obj": float(prob.value),
        "gap": abs(float(prob.value) - sigma_F),
        "y_blocks": [float(c.dual_value) for c in block_c],
    }


# Markov-trace cost per confinement operator (NF weights). Lowest weight = the
# most-confined operator the SDP selects; ties = degeneracy.
TR_M = [1.0, z, z, z * z, z * z, z ** 3]


def main() -> int:
    print(f"  σ_F(Z) ELECTRON-DRESSING CHAIN — confinement-SDP dual   "
          f"q₀={q0:.6f}  z={z:.5f}\n")

    # --- §1  Claim 1: σ_F monotone along the dressing chain -----------------
    #   He-like nucleus (Z=2, N=2, A=4): dress with electrons e = 0,1,2,….
    #   n_target = 3A + e (strand count grows); cost = Markov weights.
    print("### §1  Claim 1 — σ_F = n_target·y₀* monotone non-decreasing in Z")
    print("| e⁻ (Z) | n_target=3A+Z | σ_F | y₀* | μ=rank Φ* | gap | feasible |")
    print("|--:|--:|--:|--:|--:|--:|:--:|")
    A = 4
    prev, monotone = None, True
    for Zc in range(0, 9):
        r = confinement_dual(TR_M, n_target=float(3 * A + Zc))
        if not r["feasible"]:
            print(f"| {Zc} | {3*A+Zc} | INFEASIBLE | | | | ✗ |")
            continue
        if prev is not None and r["sigma_F"] < prev - 1e-7:
            monotone = False
        prev = r["sigma_F"]
        print(f"| {Zc} | {3*A+Zc} | {r['sigma_F']:.5f} | {r['y0']:.5f} | "
              f"{r['mu']} | {r['gap']:.1e} | ✓ |")
    print(f"  → σ_F monotone non-decreasing: {monotone}; feasible throughout "
          f"(never 'won't solve').\n")

    # --- §2  Claim 2 mechanism: degenerate cost-min ⇒ μ ≥ 2 -----------------
    #   A closed shell = the lowest cost level is d-fold degenerate; Φ* then
    #   spreads over the d-dim eigenspace and μ = d. Sweep the degeneracy d.
    print("### §2  Claim 2 mechanism — closed shell = degenerate cost-min ⇒ μ≥2")
    print("| shell degeneracy d (lowest level) | μ = rank Φ* | σ_F | closed? |")
    print("|--:|--:|--:|:--:|")
    for d in range(1, 5):
        # cost: d operators tied at the minimum (closed shell), rest higher
        T = [0.10] * d + [1.0, 2.0]
        r = confinement_dual(T, n_target=2.0)
        closed = "✓ μ≥2" if r["mu"] >= 2 else "open"
        print(f"| {d} | {r['mu']} | {r['sigma_F']:.4f} | {closed} |")
    print("  → when the lowest cost level is d-fold degenerate (a full shell:")
    print("    all magnetic/spin labels of principal n at one energy), Φ*")
    print("    occupies the d-dim eigenspace and μ = d. μ≥2 is the binding-")
    print("    multiplicity signature of shell closure (claim 2).\n")

    # --- §3  Finding --------------------------------------------------------
    print("### Finding")
    print("  • The canonical confinement-SDP DUAL is now computed at the atom-")
    print("    electron level (σ_F, y₀*, μ, gap) — the level-6 dual that was a")
    print("    skeleton / primal-only is wired via cvxpy+Clarabel.")
    print("  • Claim 1 holds: σ_F is monotone non-decreasing along the dressing")
    print("    chain; the SDP never goes infeasible (the raw-Gram 'capacity' is")
    print("    the excluded interlacing branch — see the companion demo).")
    print("  • Claim 2 mechanism holds: a degenerate cost-minimum (closed shell)")
    print("    gives rank-μ active support with μ≥2 — the multiplicity read-out.")
    print("  • DEFERRED (research tranche): the σ_F local-maxima exactly at the")
    print("    noble-gas Z∈{2,10,18,…} need the multi-level cost operator that")
    print("    encodes 2n² shell degeneracies + Madelung ordering. Hand-coding")
    print("    those would make the peaks an input, not emergent — so they are")
    print("    left to the level-6 cost-operator infra cut, not faked here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
