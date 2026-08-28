#!/usr/bin/env python3
"""Whitehead link VC sub-leading constant c_σ — HIGH-PRECISION mpmath
extrapolation, to decide whether c_σ admits a closed form.

Route (formalize-first, structural claim stated BEFORE the search):

    STRUCTURAL CLAIM (tested, not assumed):  c_σ = 2^{-3/4}.

Motivation: the refined Volume-Conjecture / Ohtsuki 1-loop prefactor of a
hyperbolic link is  c_σ ∝ (2π)^{power} · (± τ_adjoint)^{-1/2}, τ = adjoint
Reidemeister torsion of the complement at the geometric flat connection.  For
the Whitehead complement = regular ideal octahedron (shapes with |z| = √2,
trace field ℚ(i)), the natural algebraic scale is a pure power of 2.  The
float64 tower (whitehead_c_sigma.py) extrapolates c_σ ≈ 0.5946027, and
2^{-3/4} = 0.5946035575 — a 6-digit, π-free, parameter-free match.  This script
pins c_σ to many more digits (mpmath, van der Veen exact formula at large N +
Neville/Richardson extrapolation in 1/N) so the match can be confirmed or
refuted well beyond coincidence.

|J_N| is van der Veen's positive-sum formula (Lemma 1, arXiv:math/0611181),
the same transcription validated three ways in whitehead_van_der_veen.py.  The
sum is phase-stable (no root-of-unity cancellation catastrophe), so mpmath at
dps≈60 gives log|J_N| to full precision.  Audit-only; NO wiring.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def log_JN(N: int) -> mp.mpf:
    """log|J_N(Whitehead W_{0,1,1,0})(e^{2πi/N})| — van der Veen Lemma 1, mpmath.

    Mirrors whitehead_c_sigma.log_JN exactly but in mpf/mpc:
      inner[n] = Σ_{k=0}^{N-1-n} ∏_{j=1}^n [2 sin²((k+j)π/N)] / ∏_{j=1}^n sin(jπ/N)
      J_N      = Σ_{n=0}^{N-1} (2n+1) · exp(-i n(n+1-N)π/(2N)) · inner[n]
    """
    piN = mp.pi / N
    # f[m] = 2 sin²(mπ/N), m = 0 .. 2N+1
    f = [2 * mp.sin(m * piN) ** 2 for m in range(2 * N + 2)]
    g = [mp.sin(j * piN) for j in range(1, N + 1)]           # g[j-1] = sin(jπ/N)
    inner = [mp.mpf(0)] * N
    P = [mp.mpf(1)] * (N + 2)                                # P[k] = ∏_{j≤n} f[k+j]
    inner[0] = mp.mpf(N)
    gprod = mp.mpf(1)
    for n in range(1, N):
        for k in range(N):
            P[k] *= f[n + k]
        gprod *= g[n - 1]
        s = mp.mpf(0)
        for k in range(N - n):
            s += P[k]
        inner[n] = s / gprod
    tot = mp.mpc(0)
    for n in range(N):
        phase = mp.e ** (mp.mpc(0, 1) * (-(mp.mpf(n) * (n + 1 - N)) / (2 * N)) * mp.pi)
        tot += (2 * n + 1) * phase * inner[n]
    return mp.log(abs(tot))


def c_sigma(N: int, p, A) -> mp.mpf:
    return mp.e ** (log_JN(N) - p * mp.log(N) - A * N)


def neville_1overN(Ns, vals):
    """Neville/Richardson extrapolation to 1/N → 0 (polynomial in h = 1/N)."""
    xs = [mp.mpf(1) / N for N in Ns]
    ys = list(vals)
    m = len(ys)
    T = [list(ys)]
    for k in range(1, m):
        row = []
        for i in range(m - k):
            xi, xik = xs[i], xs[i + k]
            row.append((T[k - 1][i + 1] * (0 - xi) - T[k - 1][i] * (0 - xik)) / (xik - xi))
        T.append(row)
    return T[m - 1][0], T   # top-level value + table for convergence inspection


if __name__ == "__main__":
    mp.mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    VOL = 4 * mp.catalan
    A = VOL / (2 * mp.pi)
    p = mp.mpf(3) / 2   # geometric-connection exponent (settled 3/2, witness p=1.4999992)

    # large-N tower; O(N²) mpf, phase-stable.  Keep runtime bounded.
    Ns = [int(x) for x in (sys.argv[2].split(",")
                           if len(sys.argv) > 2 else
                           "300,400,500,700,900,1100,1400".split(","))]
    print(f"Whitehead c_σ high-precision — mpmath dps={mp.mp.dps}")
    print(f"  VOL=4G = {mp.nstr(VOL, 25)},  A=Vol/2π = {mp.nstr(A, 25)}\n")

    cs = {}
    t0 = time.time()
    for N in Ns:
        ts = time.time()
        cs[N] = c_sigma(N, p, A)
        el = time.time() - ts
        print(f"  N={N:5d}: c_σ(N) = {mp.nstr(cs[N], 22)}   ({el:5.1f}s, "
              f"tot {time.time()-t0:6.1f}s)", flush=True)

    c_inf, T = neville_1overN(Ns, [cs[N] for N in Ns])
    print(f"\n  Neville 1/N → 0 extrapolation:  c_σ(∞) = {mp.nstr(c_inf, 22)}")

    # candidate closed forms (parameter-free, structural)
    cands = {
        "2^{-3/4}": mp.power(2, mp.mpf(-3) / 4),
        "1/(2·2^{1/4})=2^{-5/4}": mp.power(2, mp.mpf(-5) / 4),
        "2^{-1/2}=1/√2": mp.power(2, mp.mpf(-1) / 2),
        "1/√(2π)·√π= ...": mp.mpf(0),  # placeholder, skip if 0
        "3^{-1/4}(fig8 torsion)": mp.power(3, mp.mpf(-1) / 4),
        "1/√e·...": mp.mpf(0),
    }
    print("\n  candidate comparison (|c_σ(∞) − cand| and relative):")
    best = None
    for name, val in cands.items():
        if val == 0:
            continue
        d = abs(c_inf - val)
        rel = d / abs(c_inf)
        digits = int(-mp.log10(rel)) if rel > 0 else 999
        print(f"    {name:28s} = {mp.nstr(val, 20)}   Δ={mp.nstr(d, 6)}  "
              f"rel={mp.nstr(rel, 4)}  (~{digits} digits)")
        if best is None or rel < best[1]:
            best = (name, rel, digits)
    print(f"\n  best match: {best[0]}  to ~{best[2]} digits (rel {mp.nstr(best[1],4)})")

    wit = {
        "description": "Whitehead link VC sub-leading constant c_σ pinned to high precision (mpmath, van der Veen exact colored Jones + Neville 1/N extrapolation) and compared to parameter-free closed forms. Tests the structural claim c_σ = 2^{-3/4}.",
        "computation": "whitehead_c_sigma_hiprec", "audit_only": True,
        "reference": "van der Veen arXiv:math/0611181 Lemma 1; GGMW/Ohtsuki 1-loop asymptotic",
        "dps": mp.mp.dps,
        "vol_4G": mp.nstr(VOL, 30),
        "p_exponent_used": "3/2",
        "Ns": Ns,
        "c_sigma_tower": {str(N): mp.nstr(cs[N], 25) for N in Ns},
        "c_sigma_extrapolated": mp.nstr(c_inf, 25),
        "candidate_2_pow_minus_3_4": mp.nstr(cands["2^{-3/4}"], 25),
        "best_match": best[0],
        "best_match_digits": best[2],
        "note": "Structural claim c_σ=2^{-3/4} TESTED numerically here; DERIVATION from adjoint Reidemeister torsion is a separate step (see whitehead_torsion_1loop.py). NOT wired.",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-c-sigma-hiprec.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    wit.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        wit, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(wit, indent=2))
    print(f"\n  Witness: {out}")
