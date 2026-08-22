#!/usr/bin/env python3
"""Whitehead link (5²₁ = L5a1 = 2-bridge b(8,3)) colored Jones + Kashaev
root-of-unity saddle → Vol(Whitehead).

Reconstruction of a stalled-session probe whose live code was never
committed and was lost to container reclamation (branch
claude/whitehead-habiro-kashaev-lupmgo).  The lost interim result was a
Whitehead ÷[N]¹ reduced-Jones Kashaev constant c₀ trending toward the
"factor-2" prediction (c₀ ≈ −0.520) at N ≤ 9, inconclusive.

Anti-guessing discipline (AGENTS.md §Critical-distance, §anti-laundering):
NO Whitehead colored-Jones closed form is transcribed from memory here.
Instead the invariant is built from *derivable* ingredients and validated
against an *independent* target — the hyperbolic volume:

    Vol(Whitehead complement) = Vol(regular ideal octahedron)
                              = 8·Λ(π/4) = 4·G = 3.6638623767…
                              (G = Catalan's constant; SnapPy: 3.66386238)

The volume-conjecture growth rate of the Kashaev invariant is therefore a
stringent, formula-free check: if a candidate diagram's Kashaev sum grows
at rate 4G, the diagram is the Whitehead link (the only 5-crossing
2-component link with this volume; the torus link L4a1 has Vol = 0).

Structure of this file (built incrementally, each piece validated):
  Part 0  — targets + a re-validation harness on the KNOWN-GOOD
            figure-eight Kashaev sum (proves the asymptotic/Richardson
            machinery is correct before it is trusted on the Whitehead).
  Part 1  — [next commit] Whitehead Kashaev state sum, growth-rate check
            vs 4G.
  Part 2  — [next commit] reduced colored Jones tr_q/[N]¹, c₀ extraction,
            factor comparison.

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

# Precision must be raised HERE, not in main(): the 25-digit constant below is
# built at import time, and at mpmath's default 15 dps it would be frozen at
# 53 bits with 9 of its digits discarded. main() sets the same 50.
mp.mp.dps = 50

# Vol(Whitehead) = 4·Catalan = volume of the regular ideal octahedron.
VOL_WHITEHEAD = mp.mpf("3.663862376708876060218414")  # = 4·G, SnapPy 3.66386238


# ── Part 0: re-validation harness on the figure-eight (known-good) ──
def kashaev_4_1(N: int) -> mp.mpf:
    """⟨4₁⟩_N = Σ_{k=0}^{N-1} ∏_{j=1}^k (2 − 2cos(2πj/N)).  Real, positive.

    Verbatim structural copy of the committed figure_eight_kashaev_volume.py
    kernel — used ONLY as a self-test that the Richardson/asymptotic code
    below reproduces the established Vol(4₁) = 2.0298832… before that code
    is applied to the (new) Whitehead sum.
    """
    total = mp.mpf(0)
    prod = mp.mpf(1)  # k = 0 empty product
    total += prod
    for k in range(1, N):
        prod *= (2 - 2 * mp.cos(2 * mp.pi * k / N))
        total += prod
    return total


VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)  # Vol(4_1) EXACT = 2*Cl_2(pi/3) = 6*Lambda(pi/3).
# The literal that was here printed 49 digits and was correct to 20 --
#   was    2.02988321281930725001 1597804990447526446605015756
#   exact  2.02988321281930725004 2405108549040571883378615060599584
# so 29 digits were fabricated. dps is raised above, so the closed form
# is exact here and cannot be mis-transcribed at all (bean qou-ckbv).


def volume_from_kashaev(kashaev_fn, Ns):
    """(2π/N)·log⟨L⟩_N with a one-term Richardson removal in (log N)/N.

    Returns list of (N, raw_est, richardson_est).  The sub-leading term of
    log⟨L⟩_N is (3/2)·log N for these octahedral saddles, so a linear
    extrapolation in x = (log N)/N → 0 sharpens the volume estimate.
    """
    rows = []
    prev = None
    for N in Ns:
        K = kashaev_fn(N)
        est = (2 * mp.pi / N) * mp.log(abs(K))
        rich = None
        if prev is not None:
            Np, ep = prev
            xp = mp.log(Np) / Np
            xn = mp.log(N) / N
            rich = (ep * xn - est * xp) / (xn - xp)
        prev = (N, est)
        rows.append((N, est, rich))
    return rows


def main() -> int:
    mp.mp.dps = 50
    print("\n  WHITEHEAD link — colored Jones / Kashaev reconstruction")
    print(f"  Vol(Whitehead) target = 4·G = {float(VOL_WHITEHEAD):.10f}  (regular ideal octahedron)\n")

    print("  Part 0 — harness self-test on figure-eight (known-good):")
    rows = volume_from_kashaev(kashaev_4_1, [50, 100, 200, 400, 800])
    for N, est, rich in rows:
        rs = f"{float(rich):.8f}" if rich is not None else "—"
        print(f"    N={N:>4}  raw={float(est):.8f}  richardson={rs}")
    best = rows[-1][2]
    err = abs(best - VOL_4_1)
    ok = err < mp.mpf("1e-2")
    print(f"    best richardson = {float(best):.8f}  vs Vol(4₁)={float(VOL_4_1):.8f}  err={float(err):.2e}")
    print(f"    harness {'OK — asymptotic machinery validated' if ok else 'FAILED — do not trust downstream'}\n")

    print("  Part 1 (Whitehead Kashaev state sum) — pending next commit.")
    print("  Part 2 (reduced tr_q/[N]¹, c₀ factor) — pending next commit.")

    witness = {
        "description": "Whitehead link colored Jones / Kashaev reconstruction — Part 0 harness (asymptotic machinery self-test vs Vol(4₁)); Vol(Whitehead)=4G validator target",
        "computation": "whitehead_kashaev_volume",
        "audit_only": True,
        "precision_dps": 50,
        "reconstruction_of": "lost stalled session on branch claude/whitehead-habiro-kashaev-lupmgo (uncommitted, container-reclaimed)",
        "vol_whitehead_target": str(VOL_WHITEHEAD),
        "vol_4_1_target": str(VOL_4_1),
        "harness_best_richardson": str(best),
        "harness_err_vs_vol_4_1": str(err),
        "harness_ok": bool(ok),
        "status": "part-0-harness-only",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-kashaev-volume.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"  Witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
