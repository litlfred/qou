#!/usr/bin/env python3
"""W1 subleading term — extract the 1-loop (torsion) datum from the
Borromean colored-Jones asymptotics.

Follow-on to the merged volume anchor
(computations/probes/borromean_jones_volume_anchor.py, PR #4208), which
anchored the LEADING term: the Kashaev growth rate of J_{B,N}(e^{2πi/N})
recovers Vol(𝓑₃)=8G to 0.4%.  This probe extracts the NEXT term.

The Ohtsuki-type asymptotic expansion of the Kashaev invariant of a
hyperbolic link is

  log|J_{K,N}(e^{2πi/N})| = (N/2π)·Vol + p·log N + c₀ + O(1/N),

where
  • (N/2π)·Vol   is the leading volume term (anchored in #4208),
  • p            is the power-of-N prefactor (p = 3/2 for a 1-cusp
                 knot; larger for a multi-cusp link — 𝓑₃ has 3 cusps),
  • c₀           is the "1-loop" constant.  By the 1-loop conjecture
                 (Dimofte–Garoufalidis arXiv:1102.4847) exp(c₀) is
                 fixed by the ADJOINT REIDEMEISTER TORSION τ(𝓑₃) of
                 the complete hyperbolic structure (the delta-invariant
                 1/√(±τ), times explicit 2π/i factors).

We FIX Vol = 8G (known, from #4208) and least-squares fit the remaining
coefficients (p, c₀, d) from the exactly-computable Habiro tower.  The
extracted (p, c₀) are the second and third honest bridge data below the
volume — the numbers any derived index↔tr_M bridge must also reproduce
on its side.

What this does / does NOT do:
  • DOES measure p and c₀ from the Jones side, parameter-free.
  • Does NOT yet compare c₀ to an independent τ(𝓑₃): the corpus carries
    no Borromean adjoint torsion (grep 2026-07-25).  Computing τ(𝓑₃)
    from the octahedral Neumann–Zagier data is the bounded follow-up
    that turns this MEASUREMENT into a MATCH.  We report c₀ honestly as
    a measured constant, not a verified torsion match.

Discipline: audit-only; scope-(a); NO fit of any physical observable
(Vol is fixed by topology; p, c₀ are read off, not tuned to a target);
nothing wired; no c_k; L2 unchanged.  Reuses the corpus Habiro
transcription (Garoufalidis–Le arXiv:math/0508100 v6 App A).

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

V_OCT = 4 * mp.catalan       # ideal regular octahedron = 4G
VOL_BOR = 2 * V_OCT          # Borromean complement = 8G ≈ 7.327724753


def log_abs_habiro_at_root(n: int) -> mp.mpf:
    """log |J_{B,n}(e^{2πi/n})| via the corpus Habiro sum (removable-pole
    safe: evaluate at s = e^{iπ(1+δ)/n}, δ = 1e-30, 60 dps)."""
    delta = mp.mpf("1e-30")
    sval = mp.e ** (1j * mp.pi * (1 + delta) / n)

    def brk(j: int):
        return sval**j - sval ** (-j)

    total = mp.mpc(0)
    bn2 = brk(n) ** 2
    for l in range(0, n):
        num = bn2
        for j in range(1, l + 1):
            num *= (brk(n + j) * brk(n - j)) ** 3
        den = mp.mpc(1)
        for j in range(l + 1, 2 * l + 2):
            den *= brk(j) ** 2
        total += ((-1) ** l) * num / den
    return mp.log(abs(total))


def lstsq(rows_phi, ys):
    """Solve min ‖Φ c − y‖ via mpmath Gaussian elimination on the normal
    equations (no numpy in sandbox).  rows_phi[k] is the design row."""
    m = len(rows_phi[0])
    AtA = [[sum(rows_phi[k][i] * rows_phi[k][j] for k in range(len(rows_phi)))
            for j in range(m)] for i in range(m)]
    Aty = [sum(rows_phi[k][i] * ys[k] for k in range(len(rows_phi))) for i in range(m)]
    M = [AtA[i] + [Aty[i]] for i in range(m)]
    for col in range(m):
        piv = max(range(col, m), key=lambda rr: abs(M[rr][col]))
        M[col], M[piv] = M[piv], M[col]
        for rr in range(m):
            if rr != col and M[rr][col] != 0:
                f = M[rr][col] / M[col][col]
                M[rr] = [M[rr][c] - f * M[col][c] for c in range(m + 1)]
    return [M[i][m] / M[i][i] for i in range(m)]


def main() -> int:
    NMAX = 44
    print(f"Vol(𝓑₃) = 8G = {mp.nstr(VOL_BOR, 12)} (fixed from #4208)")
    Ns, logs = [], []
    for n in range(4, NMAX + 1):
        lg = log_abs_habiro_at_root(n)
        Ns.append(mp.mpf(n))
        logs.append(lg)
    # subtract the KNOWN leading volume term, fit the remainder to
    #   r(N) := log|J| − (N/2π)Vol = p·log N + c₀ + d/N.
    lead = [(N / (2 * mp.pi)) * VOL_BOR for N in Ns]
    resid = [logs[i] - lead[i] for i in range(len(Ns))]

    print(f"\n{'N':>3} {'log|J|':>16} {'r(N)=log|J|−volTerm':>22}")
    for i in range(len(Ns)):
        if int(Ns[i]) % 4 == 0 or i >= len(Ns) - 4:
            print(f"{int(Ns[i]):>3} {float(logs[i]):>16.6f} {float(resid[i]):>22.6f}")

    # tail fit (drop small N to suppress higher 1/N² contamination)
    tail_lo = 16
    idx = [i for i in range(len(Ns)) if Ns[i] >= tail_lo]

    # (A) 3-param fit r = p·logN + c₀ + d/N  (Vol fixed)
    phi3 = [[mp.log(Ns[i]), mp.mpf(1), 1 / Ns[i]] for i in idx]
    y = [resid[i] for i in idx]
    p_fit, c0_fit, d_fit = lstsq(phi3, y)

    # (B) 4-param cross-check: also free the volume slope,
    #     log|J| = a·N + p·logN + c₀ + d/N  → check a·2π ≈ 8G.
    phi4 = [[Ns[i], mp.log(Ns[i]), mp.mpf(1), 1 / Ns[i]] for i in idx]
    y4 = [logs[i] for i in idx]
    a4, p4, c04, d4 = lstsq(phi4, y4)

    print(f"\n── Vol-fixed 3-param fit  r(N)=p·logN + c₀ + d/N  (tail N≥{tail_lo}) ──")
    print(f"  power  p   = {float(p_fit):.5f}   (knot 3/2 = 1.5; 𝓑₃ has 3 cusps)")
    print(f"  1-loop c₀  = {float(c0_fit):.5f}")
    print(f"  1/N    d   = {float(d_fit):.5f}")
    print(f"\n── free-slope 4-param cross-check ──")
    print(f"  slope a    = {float(a4):.6f}  → a·2π = {float(a4*2*mp.pi):.5f}  (8G = {float(VOL_BOR):.5f})")
    print(f"  power  p   = {float(p4):.5f}")
    print(f"  1-loop c₀  = {float(c04):.5f}")

    # 1-loop delta candidate: exp(c₀) up to the standard 2π factors.
    # (Reported as raw exp(c₀); the τ comparison is the follow-up.)
    delta_expc0 = float(mp.e ** c0_fit)
    print(f"\n  exp(c₀)    = {delta_expc0:.6f}   (raw 1-loop amplitude; τ(𝓑₃) comparison = follow-up)")

    verdict_vol = abs(float(a4 * 2 * mp.pi) - float(VOL_BOR)) / float(VOL_BOR) < 0.02
    print(f"\nVERDICT: leading volume re-confirmed ({'OK' if verdict_vol else 'OFF'}); "
          f"subleading power p≈{float(p_fit):.2f} and 1-loop constant c₀≈{float(c0_fit):.3f} "
          f"MEASURED (τ(𝓑₃) match is the follow-up).")

    script_path = Path(__file__).resolve()
    src = script_path.read_text()
    try:
        commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(script_path)],
            cwd=script_path.parent, text=True).strip()
    except Exception:
        commit = ""
    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": commit,
        "scriptFile": "computations/probes/borromean_jones_1loop_torsion.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12],
        "scriptCommitSha": commit,
        "description": "Subleading (power-of-N + 1-loop constant c₀) extraction "
                       "from the Borromean colored-Jones Kashaev asymptotics, "
                       "Vol fixed = 8G. The next honest bridge data below the "
                       "volume. Audit-only; no fit; nothing wired.",
        "auditOnly": True,
        "parameters": {"NMAX": NMAX, "tail_lo": tail_lo, "root": "q=exp(2πi/N)"},
        "data": {
            "vol_borromean_8G": mp.nstr(VOL_BOR, 20),
            "fit_vol_fixed": {"power_p": float(p_fit), "c0": float(c0_fit), "d": float(d_fit)},
            "fit_free_slope": {"slope_a": float(a4), "vol_from_slope": float(a4 * 2 * mp.pi),
                                "power_p": float(p4), "c0": float(c04), "d": float(d4)},
            "exp_c0_raw_1loop_amplitude": delta_expc0,
            "verdict_leading_volume_ok": bool(verdict_vol),
            "note": "c0 is a MEASURED constant; comparison to the adjoint "
                    "Reidemeister torsion tau(B3) requires the octahedral "
                    "Neumann-Zagier 1-loop computation (follow-up).",
        },
    }
    out = script_path.with_name("borromean-jones-1loop-torsion.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
