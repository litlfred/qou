#!/usr/bin/env python3
"""
Figure-eight (4₁ = Higgs) root-of-unity saddle → Vol(4₁).  Keystone part (a).

Verifies the volume-conjecture (Kashaev–Murakami–Murakami) root-of-unity
(Φ_q / compact-q-dilog) saddle for the figure-eight knot, the QOU Higgs:

    ⟨4₁⟩_N = Σ_{k=0}^{N-1} | (q)_k |²,    q = e^{2πi/N},   (q)_k = ∏_{j=1}^k (1-q^j)
           = Σ_{k=0}^{N-1} ∏_{j=1}^k (2 - 2cos(2πj/N))     [real form]

    lim_{N→∞} (2π/N) · log ⟨4₁⟩_N  =  Vol(4₁) = 2.029883…

This is the Φ_q (root-of-unity) saddle of the AJ machinery Â_{4_1}·J_N = 0
(phi-q-aj-machinery-identification.md): the figure-eight is hyperbolic, so
the Kashaev sum grows EXPONENTIALLY and its rate is the hyperbolic volume —
unlike a torus knot (Vol_hyp = 0, polynomial growth). The asymptotic carries
a (3/2)·log N sub-leading term, so a one-term Richardson removal in (log N)/N
sharpens the estimate.

Audit-only. Establishes that the Higgs (4₁) root-of-unity saddle = Vol(4₁),
i.e. the Re-face mass scale m_μ/m_e = Vol(4₁)/ℏ_q² has a literature-anchored
saddle origin (CAL-2 reanalysis audit 2026-06-30).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
mp.mp.dps = 60

VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)  # Vol(4_1) EXACT = 2*Cl_2(pi/3) = 6*Lambda(pi/3).
# The literal that was here printed 49 digits and was correct to 20 --
#   was    2.02988321281930725001 1597804990447526446605015756
#   exact  2.02988321281930725004 2405108549040571883378615060599584
# so 29 digits were fabricated. dps is raised above, so the closed form
# is exact here and cannot be mis-transcribed at all (bean qou-ckbv).


def kashaev_4_1(N: int) -> mp.mpf:
    """⟨4₁⟩_N = Σ_{k=0}^{N-1} ∏_{j=1}^k (2 - 2cos(2πj/N)).  Real, positive."""
    total = mp.mpf(0)
    prod = mp.mpf(1)  # k=0 empty product
    total += prod
    for k in range(1, N):
        prod *= (2 - 2 * mp.cos(2 * mp.pi * k / N))
        total += prod
    return total


def main() -> int:
    mp.mp.dps = 60
    print(f"\n  FIGURE-EIGHT (4₁ = Higgs) Kashaev volume — root-of-unity (Φ_q) saddle")
    print(f"  Target Vol(4₁) = {float(VOL_4_1):.10f}\n")
    print(f"  {'N':>5}  {'(2π/N)·log⟨4₁⟩_N':>18}  {'Richardson(logN/N)':>20}  {'err vs Vol':>12}")
    print("  " + "-" * 62)

    Ns = [50, 100, 200, 300, 400, 600, 800, 1200]
    raw = {}
    prev = None
    rows = []
    for N in Ns:
        K = kashaev_4_1(N)
        est = (2 * mp.pi / N) * mp.log(K)
        raw[N] = est
        # Richardson: est(N) = Vol + c·(log N)/N + … ; eliminate using two N's
        rich = None
        if prev is not None:
            Np, ep = prev
            xp = mp.log(Np) / Np
            xn = mp.log(N) / N
            rich = (ep * xn - est * xp) / (xn - xp)  # linear extrapolation in (log N)/N → 0
        prev = (N, est)
        err = abs((rich if rich is not None else est) - VOL_4_1)
        rows.append((N, est, rich, err))
        rich_s = f"{float(rich):.8f}" if rich is not None else "—"
        print(f"  {N:>5}  {float(est):>18.8f}  {rich_s:>20}  {float(err):>12.2e}")

    best = rows[-1]
    print(f"\n  Best Richardson estimate (N={best[0]}): {float(best[2]):.8f}  "
          f"vs Vol(4₁)={float(VOL_4_1):.8f}  (err {float(best[3]):.2e})")
    converging = float(rows[-1][3]) < float(rows[2][3])  # tighter than N=200 row
    grows_exp = float(raw[Ns[-1]]) > 1.5  # nonzero rate (torus would → 0)
    print(f"  Exponential growth (rate ≫ 0, not a torus knot)? {grows_exp}")
    print(f"  Converging toward Vol(4₁) under Richardson? {converging}")
    print(f"\n  ⇒ The 4₁ (Higgs) ROOT-OF-UNITY (Φ_q) saddle reproduces Vol(4₁): "
          f"{'CONFIRMED' if (grows_exp and converging) else 'INCONCLUSIVE at these N'}.")

    witness = {
        "description": "Figure-eight (4₁=Higgs) Kashaev invariant: root-of-unity (Φ_q) saddle reproduces Vol(4₁) [volume conjecture], keystone part (a)",
        "computation": "figure_eight_kashaev_volume",
        "audit_only": True,
        "precision_dps": 60,
        "context": {
            "tests": "phi-q-aj-machinery-identification.md — Φ_q saddle of Â_{4_1} = Vol(4_1)",
            "ties_to": "CAL-2 = V(4_1): Re=Vol(4_1)->m_mu/m_e (this); Im=CS(4_1)->D_beta (next)",
            "formula": "<4_1>_N = sum_{k=0}^{N-1} prod_{j=1}^k (2 - 2 cos(2 pi j / N)); (2pi/N) log -> Vol(4_1)",
        },
        "vol_4_1_target": str(VOL_4_1),
        "estimates": {str(N): {"raw": str(e), "richardson": (str(r) if r is not None else None),
                               "err": str(err)} for (N, e, r, err) in rows},
        "best_richardson": {"N": best[0], "value": str(best[2]), "err": str(best[3])},
        "exponential_growth": grows_exp,
        "converging": converging,
        "verdict": "CONFIRMED" if (grows_exp and converging) else "INCONCLUSIVE",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "figure-eight-kashaev-volume.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
