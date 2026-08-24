#!/usr/bin/env python3
"""Whitehead c₀ — mpmath EXACT-ROOT only (no float64).

Per owner directive: the c₀ / factor determination uses ONLY high-precision
mpmath exact-root values.  The float64 δ-extrapolation (whitehead_c0_tower*.py)
is dropped from the number — it drifts ~1% at N≥8 (the 5-crossing magnitude
worsens the near-root cancellation), which biased the earlier c₀.

Inputs (all mpmath / exact):
  • Whitehead reduced |J_red(N)| at the exact root, from the mpmath R-matrix
    (dps=40), harvested from whitehead-c0-tower-hi.witness.json (N=6,8,10) and
    optionally extended to N=12 here.
  • Figure-eight REFERENCE c₀ computed EXACTLY from the finite Habiro–Le
    polynomial J_N(4₁) at the exact root e^{2πi/N} (no R-matrix, no float64);
    must recover the known −¼ln3 = −0.2747, validating the fit.

Fit: log|J_red| = (Vol/2π)N + p·logN + c₀ + d/N (+ e/N²), p = 3/2 fixed.

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_colored_jones import (  # noqa: E402
    r_check_braiding, closure_invariant_fast, qint, colored_jones_4_1_exact,
)

mp.mp.dps = 60
# Both of these have closed forms and neither needs a literal. dps is
# raised above, so these evaluate exactly (bean qou-ckbv).
#   VOL_WHITEHEAD: the old literal said "# 4G" in a comment while
#     writing 25 digits by hand -- correct, but transcribed.
#   VOL_4_1: the old literal printed 31 digits and was correct to 20:
#       was    2.02988321281930725001 1597804990
#       exact  2.02988321281930725004 2405108549040571883378615...
VOL_WHITEHEAD = 4 * mp.catalan            # = 8*Lambda(pi/4), one ideal octahedron
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)      # = 2*Cl_2(pi/3) = 6*Lambda(pi/3)
WHITEHEAD = [1, -2, 1, -2, 1]
EXTEND_N12 = "--n12" in sys.argv


def whitehead_exact(N, delta=mp.mpf("1e-45")):
    """mpmath exact-root |J_red(N)| for the Whitehead link (fast O(N⁸) path).

    δ=1e-45 with dps=60 preserves ~15 digits through the near-root tiny/tiny
    division (raw,[N] ~ 1e-45; abs error ~1e-60 → ~15 digits in the ratio).
    """
    th = mp.pi * (1 - delta) / N
    q = mp.exp(mp.mpc(0, 1) * th)
    Rc, Rci = r_check_braiding(N, q)
    raw = closure_invariant_fast(WHITEHEAD, N, q, Rc, Rci, mu_power=1)
    return abs(raw / qint(N, q))


def fig8_exact_logJ(N):
    """EXACT log|J_N(4₁)| at the exact root e^{2πi/N} — finite polynomial, no float64."""
    qHL = mp.exp(2j * mp.pi / N)          # Habiro–Le convention (= q_mine²)
    return mp.log(abs(colored_jones_4_1_exact(N, qHL)))


def fit_c0(Ns, logs, vol, p=mp.mpf("1.5"), nterms=1):
    """log|J| = (vol/2π)N + p logN + c₀ + Σ_{j=1}^{nterms} a_j/N^j.  mpmath lstsq via normal eqns."""
    A = vol / (2 * mp.pi)
    y = [lg - A * N - p * mp.log(N) for lg, N in zip(logs, Ns)]
    # design columns: [1, 1/N, 1/N², …]
    cols = [[mp.mpf(1) for _ in Ns]] + [[1 / mp.mpf(N)**j for N in Ns] for j in range(1, nterms + 1)]
    M = mp.matrix(len(Ns), nterms + 1)
    for i in range(len(Ns)):
        for j in range(nterms + 1):
            M[i, j] = cols[j][i]
    yv = mp.matrix(y)
    # normal equations (MᵀM)x = Mᵀy
    MT = M.T
    coef = mp.lu_solve(MT * M, MT * yv)
    return coef[0]


def main() -> int:
    t0 = time.monotonic()
    print("Whitehead c₀ — mpmath EXACT-ROOT ONLY (no float64)")
    print(f"  Vol=4G fixed, p=3/2; factor prediction 2 → c₀=−0.52\n")

    # figure-eight reference c₀ (EXACT, fast) — validates the fit
    print("  figure-eight reference (exact Habiro–Le at root; target c₀=−¼ln3=−0.2747):")
    Nf = [6, 8, 10, 12, 14]
    logf = [fig8_exact_logJ(N) for N in Nf]
    for N, lg in zip(Nf, logf):
        print(f"    N={N:>3}  log|J|={float(lg):.6f}")
    for nt in (1, 2):
        c0f = fit_c0(Nf, logf, VOL_4_1, nterms=nt)
        print(f"    fit c₀ [{nt}-term] = {float(c0f):+.4f}  (−¼ln3 = {float(-mp.log(3)/4):+.4f})")

    # Whitehead exact anchors: harvest from hi-tower witness, else compute
    wit = Path(__file__).resolve().parent / "whitehead-c0-tower-hi.witness.json"
    vals = {}
    if wit.exists():
        d = json.loads(wit.read_text())
        for k, v in d.get("mpmath_exact_values", {}).items():
            vals[int(k)] = mp.mpf(str(v))
    for N in (6, 8, 10):
        if N not in vals:
            print(f"    computing Whitehead mpmath N={N} …", flush=True)
            vals[N] = whitehead_exact(N)
    if EXTEND_N12:
        print(f"    computing Whitehead mpmath N=12 (long) …", flush=True)
        vals[12] = whitehead_exact(12)

    Nw = sorted(vals)
    logw = [mp.log(vals[N]) for N in Nw]
    print(f"\n  Whitehead exact anchors (mpmath):")
    for N in Nw:
        print(f"    N={N:>3}  |J_red|={float(vals[N]):.8e}  log={float(mp.log(vals[N])):.6f}")

    print("\n  Whitehead c₀ fits (p=3/2, mpmath-only):")
    c0s = []
    for nt in (1, 2):
        if len(Nw) >= nt + 1:
            c0 = fit_c0(Nw, logw, VOL_WHITEHEAD, nterms=nt)
            c0s.append(float(c0))
            factor = mp.e ** (2 * (c0 + mp.mpf("0.87")))
            print(f"    [{nt}-term, N={Nw}]  c₀={float(c0):+.4f}  factor={float(factor):.2f}")
    # window: drop lowest N
    if len(Nw) >= 3:
        c0hi = fit_c0(Nw[1:], logw[1:], VOL_WHITEHEAD, nterms=1)
        c0s.append(float(c0hi))
        print(f"    [1-term, N={Nw[1:]}]  c₀={float(c0hi):+.4f}  factor={float(mp.e**(2*(c0hi+mp.mpf('0.87')))):.2f}")

    c0_mean = sum(c0s) / len(c0s)
    c0_spread = (max(c0s) - min(c0s)) / 2
    factor = float(mp.e ** (2 * (mp.mpf(str(c0_mean)) + mp.mpf("0.87"))))
    nearest = min([1, 2, 4], key=lambda f: abs(factor - f))
    excl = abs(c0_mean + 0.87) > 3 * c0_spread and abs(c0_mean + 0.17) > 3 * c0_spread
    print(f"\n  ⇒ Whitehead c₀ = {c0_mean:+.3f} ± {c0_spread:.3f} (mpmath-only)  →  factor = {factor:.2f}")
    print(f"    nearest prediction: FACTOR {nearest}; excludes factor 1 & 4: {'YES' if excl else 'marginal'}")

    witness = {
        "description": "Whitehead c₀ / factor from mpmath EXACT-ROOT values only (float64 dropped per owner directive). Reconstruction of a lost session.",
        "computation": "whitehead_c0_mpmath",
        "audit_only": True,
        "precision": "mpmath dps=40, exact-root evaluation (no float64 in the c0 determination)",
        "whitehead_braid_word": "[1,-2,1,-2,1]",
        "vol_4G": str(VOL_WHITEHEAD),
        "p_fixed": 1.5,
        "figure_eight_reference_c0_2term": float(fit_c0(Nf, logf, VOL_4_1, nterms=2)),
        "figure_eight_target_minus_quarter_ln3": float(-mp.log(3) / 4),
        "whitehead_exact_values": {str(N): float(vals[N]) for N in Nw},
        "whitehead_c0_mean": c0_mean,
        "whitehead_c0_spread": c0_spread,
        "factor": factor,
        "nearest_factor": nearest,
        "excludes_factor_1_and_4": bool(excl),
        "verdict": f"FACTOR {nearest}: c0={c0_mean:.3f}±{c0_spread:.3f} (mpmath-only)",
        "wall_seconds": f"{time.monotonic() - t0:.3f}",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c0-mpmath.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}  ({time.monotonic()-t0:.0f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
