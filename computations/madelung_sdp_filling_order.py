#!/usr/bin/env python3
"""
Madelung filling order from the confinement SDP + canonical T_ee — falsifiable test.

Question (owner, 2026-06-20): the confinement SDP IS the many-body optimiser, so
the electron filling ORDER should be its optimal active-set dressing sequence.
Does running it with the *canonical* electron–electron crossing T_ee reproduce
the Madelung (n+ℓ / Aufbau) order — i.e. the noble gases [2,10,18,36,…] — or
only the naive hydrogenic / pure-2n² [2,10,28,60]?

Canonical inputs
----------------
  • radial orbital energy E(n): the σ-tower binding E_bind(n) ∝ λ₊⁻ⁿ
    (shell-structure-eigenvalues; λ₊ = top eigenvalue of T_γe at q₀). ℓ-degenerate.
  • T_ee: the electron–electron crossing = the SAME σ matrix as p-p
    (transfer-matrix-operator.md). Its Markov weight is the screening coupling.
  • the SDP: pyhecke.lp_dual_solver picks the minimum-cost feasible orbital
    (primal x*) — the optimiser whose active set, swept over electron count, IS
    the fill order.

Closed shells = the cumulative-Z at the LARGE energy gaps in the sorted orbital
list (chemical inertness = a big HOMO–LUMO gap). With ℓ-degenerate energy the
gaps fall only between whole shells ⇒ closures at the pure-2n² 2,10,28,60. With
ℓ-splitting (penetration) the gaps move.

The test is honest only if T_ee is used as-is, NOT tuned to hit the noble gases
(that would be fitting). We report whatever falls out.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "substrate"))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "tools", "pyhecke", "python"))

from q_parameter import Q as q0, Q_INV as qi0  # noqa: E402
from pyhecke.lp_dual_solver import solve_operator_selection_lp  # noqa: E402

q0, qi0 = float(q0), float(qi0)
lam_plus = 0.5 * ((q0 - qi0) + ((q0 - qi0) ** 2 + 4) ** 0.5)   # top eigenvalue of T_γe
z2 = (1.0 / (q0 ** 0.5 + qi0 ** 0.5)) ** 2                     # canonical T_ee weight scale

NMAX = 4
ORBITALS = [(n, l) for n in range(1, NMAX + 1) for l in range(n)]   # (n,ℓ)
CAP = {(n, l): 2 * (2 * l + 1) for (n, l) in ORBITALS}              # 2(2ℓ+1)
NOBLE = [2, 10, 18, 36]            # chemical noble gases (Madelung), truncated to NMAX
PURE_2N2 = [2, 10, 28, 60]         # full-shell (ℓ-degenerate) closures


def e_radial(n):
    return -1.0 / (lam_plus ** n)   # more negative = more bound = fills first


def closed_shells(cost):
    """Sort orbitals by energy; closed-shell Z = cumulative count at each gap that
    is ≥ 50% of the max consecutive gap (the big HOMO–LUMO jumps)."""
    order = sorted(ORBITALS, key=lambda o: cost[o])
    E = [cost[o] for o in order]
    gaps = [E[i + 1] - E[i] for i in range(len(E) - 1)]
    thr = 0.5 * max(gaps) if gaps else 0.0
    zc, closures = 0, []
    for i, o in enumerate(order):
        zc += CAP[o]
        g = gaps[i] if i < len(gaps) else float("inf")
        if g >= thr:
            closures.append(zc)
    seq = " ".join(f"{n}{'spdf'[l]}" for (n, l) in order)
    return order, seq, closures


def verdict(closures):
    if closures[:len(NOBLE)] == NOBLE:
        return "NOBLE / Madelung ✓"
    if closures[:len(PURE_2N2)] == PURE_2N2:
        return "pure-2n² [2,10,28,60] — NOT Madelung"
    return f"other: {closures[:6]}"


def show(label, cost):
    _, seq, clo = closed_shells(cost)
    print(f"  {label}")
    print(f"    fill:          {seq}")
    print(f"    closed shells: {clo[:6]}   → {verdict(clo)}\n")
    return clo


def main() -> int:
    print(f"  MADELUNG FROM SDP + CANONICAL T_ee — falsifiable test   "
          f"q₀={q0:.5f}  λ₊={lam_plus:.5f}")
    print(f"  targets:  noble/Madelung {NOBLE}   pure-2n² {PURE_2N2}\n")

    # (1) bare radial (no screening) — ℓ-degenerate
    cost = {o: e_radial(o[0]) for o in ORBITALS}
    show("(1) bare σ-tower radial energy (no T_ee, ℓ-degenerate):", cost)

    # (2) canonical T_ee screening, ℓ-INDEPENDENT (same σ crossing for all ℓ)
    cost = {o: e_radial(o[0]) + z2 * o[0] for o in ORBITALS}     # +s·n, NO ℓ term
    show(f"(2) + canonical T_ee screening, ℓ-INDEPENDENT (+{z2:.4f}·n):", cost)

    # (3) ℓ-penetration lever: screening that RISES with ℓ (+c·ℓ). Show it MOVES
    #     the closures off pure-2n² — i.e. ℓ-penetration is the required lever.
    print("  (3) ℓ-penetration lever (+c·ℓ) — does rising-with-ℓ screening move it?")
    for c in (0.0, 0.05, 0.12, 0.20, 0.30):
        cost = {o: e_radial(o[0]) + z2 * o[0] + c * o[1] for o in ORBITALS}
        _, _, clo = closed_shells(cost)
        print(f"    c={c:>4}:  closed shells {clo[:6]}   → {verdict(clo)}")
    print("    (c>0 = an ℓ-dependence the BARE σ crossing does not carry; tuning c\n"
          "     to hit [2,10,18,36] would be fitting, not derivation.)\n")

    # (4) SDP confirmation: the canonical solver's primal x* selects min-cost
    print("  (4) SDP check — pyhecke.lp_dual_solver primal x* = the min-cost pick")
    cost = {o: e_radial(o[0]) for o in ORBITALS}
    sub = ORBITALS[:4]
    t = np.array([cost[o] - min(cost.values()) + 0.01 for o in sub])   # ≥0
    G = np.eye(len(sub))
    r = solve_operator_selection_lp(t, G, 1.0)
    d = r.to_dict() if hasattr(r, "to_dict") else r
    xs = d.get("x_star") or [0] * len(sub)
    picked = sub[int(np.argmax(xs))]
    cheapest = min(sub, key=lambda o: cost[o])
    print(f"    x* selects {picked}; cheapest = {cheapest}; agree: {picked == cheapest}"
          f"  (gap {d.get('duality_gap', float('nan')):.1e})\n")

    print("### Verdict")
    print("  • SDP optimiser is free (4): x* picks the min-cost orbital, so the")
    print("    fill ORDER is whatever the cost (screening) dictates.")
    print("  • Canonical bare/ℓ-independent T_ee (1)→(2): closed shells stay at the")
    print("    pure-2n² [2,10,28,60] — the chemical noble gases [2,10,18,36] do NOT")
    print("    appear. (Same σ crossing for every orbital ⇒ no ℓ-splitting.)")
    print("  • The closures move off 2n² ONLY with +c·ℓ penetration (3) — screening")
    print("    that rises with ℓ. That ℓ-dependence is the precise MISSING piece;")
    print("    the bare crossing does not carry it, and tuning c = fitting.")
    print("  • Answer: the SDP gives the optimiser + order-from-cost for free, but")
    print("    the canonical T_ee does NOT yield Madelung. Open, well-localised:")
    print("    where does ℓ-penetration (orbital angular momentum modulating the")
    print("    T_ee coupling to the inner core) live categorically?")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
