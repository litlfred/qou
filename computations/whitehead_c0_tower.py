#!/usr/bin/env python3
"""Whitehead reduced colored-Jones Kashaev tower → the asymptotic constant
c₀ (the "factor").

Part 2 of the Whitehead reconstruction.  The reduced (÷[N]¹) colored Jones
at the root q_HL = e^{2πi/N} has the refined-volume-conjecture asymptotic

    log|J_red(N)|  =  (Vol/2π)·N  +  p·log N  +  c₀  +  d/N  +  e/N² + …

For the Whitehead link Vol = 4G is FIXED (identified, Part 1b); p is the
growth exponent (≈ 3/2 for these octahedral saddles).  Fitting the tail
gives c₀.  The prior (lost) session parametrised competing structural
predictions as

    c₀(factor) = c₀_base + ½·ln(factor),   factor ∈ {1, 2, 4}
               ≈ {−0.87, −0.52, −0.17}

so the "factor" enters as √factor in the prefactor.  This tower pins the
Whitehead c₀ (and, with the SAME pipeline, the figure-eight reference) to
decide the factor.

Method (fast + validated, whitehead_fast.py): the normalized invariant
norm(q) is analytic and finite at the root; evaluate it just off the root
at several δ and extrapolate δ→0 (Neville) to the exact Kashaev value —
float64-clean, no catastrophic cancellation.  Validated against the exact
figure-eight Kashaev value J_HL(e^{2πi/N}) to rel-err ~1e-4 (N ≤ 10).

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_fast import closure_norm  # noqa: E402

VOL_4_1 = 2.029883212819307
VOL_WHITEHEAD = 3.663862376708876          # 4G
FIG8 = [1, -2, 1, -2]
WHITEHEAD = [1, -2, 1, -2, 1]


def kashaev_at_root(word, m, N, deltas=(0.024, 0.018, 0.012, 0.008, 0.004)):
    """|J_red(N)| at the exact root via Neville δ→0 extrapolation of norm(q)."""
    xs = list(deltas)
    ys = []
    for d in deltas:
        th = math.pi * (1 - d) / N
        q = complex(math.cos(th), math.sin(th))
        ys.append(closure_norm(word, m, N, q))
    n = len(xs)
    for k in range(1, n):
        for i in range(n - k):
            ys[i] = ((0 - xs[i + k]) * ys[i] - (0 - xs[i]) * ys[i + 1]) / (xs[i] - xs[i + k])
    return abs(ys[0])


def fit_c0(Ns, logs, vol, fix_p=None):
    """Least-squares fit log|J| = (vol/2π)N + p·logN + c₀ + d/N + e/N².

    vol/2π·N is subtracted (fixed); returns (p, c₀, d, e).  If fix_p given,
    p is fixed and only c₀,d,e are fit.
    """
    A = vol / (2 * math.pi)
    y = np.array([lg - A * N for lg, N in zip(logs, Ns)])
    cols = []
    if fix_p is None:
        cols.append([math.log(N) for N in Ns])       # p
    else:
        y = y - fix_p * np.array([math.log(N) for N in Ns])
    cols.append([1.0 for _ in Ns])                    # c₀
    cols.append([1.0 / N for N in Ns])                # d
    cols.append([1.0 / N**2 for N in Ns])             # e
    M = np.array(cols, dtype=float).T
    coef, *_ = np.linalg.lstsq(M, y, rcond=None)
    if fix_p is None:
        p, c0, d, e = coef
    else:
        p = fix_p
        c0, d, e = coef
    return p, c0, d, e


def run(word, m, vol, label, Ns):
    print(f"\n  {label}: reduced colored Jones at root (Vol={vol:.5f} fixed)")
    logs = []
    for N in Ns:
        val = kashaev_at_root(word, m, N)
        lg = math.log(val)
        logs.append(lg)
        print(f"    N={N:>3}  |J_red|={val:.6e}  log={lg:.6f}")
    out = {}
    for fp in (None, 1.5):
        p, c0, d, e = fit_c0(Ns, logs, vol, fix_p=fp)
        tag = "p free" if fp is None else "p=3/2 fixed"
        factor = math.exp(2 * (c0 - (-0.87)))
        print(f"    fit [{tag}]: p={p:.4f}  c₀={c0:.4f}  (⇒ factor=exp(2(c₀+0.87))={factor:.3f})")
        out[tag] = {"p": p, "c0": c0, "d": d, "e": e, "factor_rel_base": factor}
    return {"Ns": Ns, "logs": logs, "fits": out}


def main() -> int:
    Ns = [6, 8, 10, 12]        # extend with 14 if time permits
    if "--hi" in sys.argv:
        Ns = [6, 8, 10, 12, 14]
    print("Whitehead c₀ tower — factor decision")
    print("  prediction: c₀(factor) = −0.87 + ½ln(factor); factor∈{1,2,4}→{−0.87,−0.52,−0.17}")

    fig = run(FIG8, 3, VOL_4_1, "figure-eight 4₁ (reference)", Ns)
    wh = run(WHITEHEAD, 3, VOL_WHITEHEAD, "Whitehead L5a1", Ns)

    c0_w = wh["fits"]["p=3/2 fixed"]["c0"]
    factor = math.exp(2 * (c0_w - (-0.87)))
    nearest = min([1, 2, 4], key=lambda f: abs(factor - f))
    print(f"\n  ⇒ Whitehead c₀ (p=3/2) = {c0_w:.4f}  → factor ≈ {factor:.3f}  "
          f"(nearest structural prediction: factor {nearest})")

    witness = {
        "description": "Whitehead reduced colored-Jones Kashaev tower: asymptotic constant c₀ and the 'factor' (c₀=−0.87+½ln factor). Reconstruction of a lost stalled session.",
        "computation": "whitehead_c0_tower",
        "audit_only": True,
        "method": "delta->0 Neville extrapolation of norm(q)=raw/[N] to the exact root; validated vs exact figure-eight Kashaev (rel-err ~1e-4, N<=10)",
        "whitehead_braid_word": "[1,-2,1,-2,1]",
        "vol_whitehead_4G": VOL_WHITEHEAD,
        "Ns": Ns,
        "figure_eight_reference": fig,
        "whitehead": wh,
        "whitehead_c0_p32": c0_w,
        "whitehead_factor": factor,
        "nearest_factor_prediction": nearest,
        "caveat": "float64 delta-extrapolation; c0 precision limited by N range (same compute wall the prior session hit at N~10). Higher N needs mpmath or a symbolic reduced form.",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c0-tower.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
