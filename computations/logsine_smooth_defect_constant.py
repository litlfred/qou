#!/usr/bin/env python3
"""Does the antitone squeeze pin vdV's 1/2 constant?  NO — it is a factor-2 gap.

Evidence for the correction recorded in
`docs/audits/2026-08-11-l41-sharp-constant-still-open.md` (bean qou-shrp).

Context.  L4-1c(ii) (`LogSineSmoothPart.lean`, PR #5003) proves sorry-free

    h*(phi_ext(n) - log 2)  <=  sum_{i<n} int_cell (phi(x_{i+1}) - phi(u)) du  <=  0

for phi(x) = log(2 sin x / x), using only antitonicity of phi.  The PR
described L4-1's ingredient list as complete.  That was an over-claim: van der
Veen's Lemma 3 reads

    S~_N ~ exp( (4N/pi) Lambda(pi/4) - (1/2) log 2N ),

whose explicit -(1/2) log 2N is the N^{-1/2} prefactor feeding Lemma 4's
N^{(c+d+3)/2}.  Getting that 1/2 requires the LIMIT of the scaled smooth
defect, not two-sided bounds on it.

This probe measures the gap directly: it computes the scaled defect

    D(N) := (1/h) * sum_{j<=n} int_{x_{j-1}}^{x_j} (phi(x_j) - phi(u)) du,
    h = pi/N,  n = N/2  (so x_n = pi/2, r = 1/2)

and compares it against (a) the proved squeeze interval [phi(x_n) - log 2, 0]
and (b) the Riemann-refinement prediction (1/2)(phi(x_n) - log 2).

Result: D(N) -> the HALF value, which sits at the midpoint of the proved
interval.  So the squeeze brackets the truth but leaves a factor-2 gap; the
derivative / mean-value refinement is still required.

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402


def phi(x):
    """phi(x) = log(2 sin x / x), written as the difference used in Lean."""
    return mp.log(2 * mp.sin(x)) - mp.log(x)


def scaled_defect(N: int) -> mp.mpf:
    """(1/h) * sum_j int_{cell_j} (phi(x_j) - phi(u)) du, at n = N/2."""
    h = mp.pi / N
    n = N // 2
    total = mp.mpf(0)
    for j in range(1, n + 1):
        xj = j * h
        lo = xj - h
        # the first cell starts at 0, where phi has an integrable log
        # singularity; nudge the endpoint (the integrand is integrable).
        if lo <= 0:
            lo = mp.mpf("1e-30")
        total += mp.quad(lambda u: phi(xj) - phi(u), [lo, xj])
    return total / h


def main() -> int:
    set_compute_dps()
    print(__doc__.split("\n")[0], "\n")

    rows = []
    for N in (200, 800, 3200):
        h = mp.pi / N
        n = N // 2
        D = scaled_defect(N)
        lo = phi(n * h) - mp.log(2)      # proved lower envelope (scaled)
        hi = mp.mpf(0)                    # proved upper envelope
        half = lo / 2                     # Riemann-refinement prediction
        rows.append(
            {
                "N": N,
                "scaled_defect": mp.nstr(D, 12),
                "proved_lower": mp.nstr(lo, 12),
                "proved_upper": "0",
                "half_prediction": mp.nstr(half, 12),
                "err_vs_half": mp.nstr(abs(D - half), 6),
                "interval_width": mp.nstr(hi - lo, 6),
            }
        )
        print(
            f"  N={N:5d}  D={mp.nstr(D, 8)}   squeeze=[{mp.nstr(lo, 6)}, 0]"
            f"   half={mp.nstr(half, 8)}   |D-half|={mp.nstr(abs(D - half), 3)}"
        )

    # the gap is real and does not close: |D - lower| stays ~ |lower|/2
    last = rows[-1]
    converges_to_half = mp.mpf(last["err_vs_half"]) < mp.mpf("1e-4")
    gap_is_factor_two = mp.mpf(last["interval_width"]) > mp.mpf("0.4")
    verdict = bool(converges_to_half and gap_is_factor_two)

    print(
        f"\n  VERDICT: the scaled defect converges to the HALF value "
        f"({'confirmed' if converges_to_half else 'NOT confirmed'}), which is the "
        f"midpoint of the proved interval of width "
        f"{last['interval_width']} — the antitone squeeze does NOT pin the 1/2."
    )

    try:
        commit_sha = subprocess.run(
            ["git", "log", "-1", "--format=%H"],
            capture_output=True, text=True, cwd=Path(__file__).parent, check=True,
        ).stdout.strip()
    except Exception:
        commit_sha = "unknown"

    witness = {
        "engine": "mpmath",
        "scriptFile": "logsine_smooth_defect_constant.py",
        "commitSha": commit_sha,
        "description": (
            "L4-1 correction evidence: the antitone squeeze of "
            "LogSineSmoothPart.smooth_defect_squeeze brackets the scaled smooth "
            "defect but does NOT pin van der Veen's 1/2 constant — the true "
            "limit is the midpoint of the proved interval. Lemma 3's explicit "
            "-(1/2) log 2N therefore still needs the Riemann/mean-value "
            "refinement (bean qou-shrp)."
        ),
        "computation": "logsine_smooth_defect_constant",
        "audit_only": True,
        "precision_dps": 30,
        "rows": rows,
        "squeeze_pins_the_half": False,
        "verdict_gap_is_factor_two": verdict,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).with_name("logsine-smooth-defect-constant.witness.json")
    out.write_text(json.dumps(witness, indent=1) + "\n")
    print(f"  witness -> {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
