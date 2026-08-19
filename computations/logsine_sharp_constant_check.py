#!/usr/bin/env python3
"""Does `phi_smooth_defect_sharp` state the right thing?  Measured: yes.

The Lean theorem `QOU.Knot.FigureEightVolume.phi_smooth_defect_sharp`
(`LogSineSharpConstant.lean`, sorry-free) asserts, for every 0 < h and every
n >= 1 with n*h < pi,

    | S(h, n)  -  (h/2)*(phi(n h) - phi(h)) |   <=   (h^2/2)*(phi'(h) - phi'(n h)),

    S(h, n) := sum_{i=1}^{n-1} int_{i h}^{(i+1) h} (phi((i+1) h) - phi(u)) du,
    phi(x)  := log(2 sin x) - log x,     phi'(x) := cot x - 1/x.

The COMPILER guarantees the proof.  It cannot tell me the statement is the one
van der Veen needs, nor that the bound is not vacuously loose.  This probe
checks both, against the same grid the earlier evidence probe used
(`logsine_smooth_defect_constant.py`, h = pi/N, n = N/2, so r = 1/2):

 1. the inequality holds (it must -- a violation would mean the Lean statement
    and this transcription of it disagree, i.e. I mis-stated it);
 2. the residual really is O(h^2), not O(h) -- so the identified term
    (h/2)(phi(nh) - phi(h)) is the leading behaviour and not a coincidence;
 3. the identified term agrees with the earlier probe's measured limit,
    (1/2)(phi(n h) - log 2), which is the MIDPOINT of the interval that
    `smooth_defect_squeeze` proves and provably cannot narrow.  phi(h) -> log 2
    as h -> 0, so the two descriptions coincide in the limit; the i = 0 cell
    that this theorem excludes contributes at most |phi(h) - log 2| after
    scaling by 1/h, and so drops out.

Audit-only; no wiring.  mpmath end to end (no float64 anywhere, per AGENTS.md).
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp


def phi(x):
    return mp.log(2 * mp.sin(x)) - mp.log(x)


def phi_deriv(x):
    return mp.cos(x) / mp.sin(x) - 1 / x


def interior_defect(h, n):
    """S(h, n): the interior cells i = 1 .. n-1 (the cells covering [h, nh])."""
    total = mp.mpf(0)
    for i in range(1, n):
        lo = i * h
        hi = (i + 1) * h
        total += mp.quad(lambda u: phi(hi) - phi(u), [lo, hi])
    return total


def main() -> int:
    mp.mp.dps = 30
    print(__doc__.split("\n")[0], "\n")

    rows = []
    prev_resid = None
    for N in (200, 400, 800, 1600):
        h = mp.pi / N
        n = N // 2
        S = interior_defect(h, n)
        term = h / 2 * (phi(n * h) - phi(h))
        bound = h ** 2 / 2 * (phi_deriv(h) - phi_deriv(n * h))
        resid = abs(S - term)
        holds = bool(resid <= bound)
        # ratio against the earlier probe's measured limit, (1/2)(phi(nh) - log 2)
        old_limit = (phi(n * h) - mp.log(2)) / 2
        ratio = None if prev_resid is None else prev_resid / resid
        rows.append(
            {
                "N": N,
                "h": mp.nstr(h, 10),
                "S": mp.nstr(S, 12),
                "identified_term": mp.nstr(term, 12),
                "residual": mp.nstr(resid, 8),
                "lean_bound": mp.nstr(bound, 8),
                "inequality_holds": holds,
                "scaled_term_over_h": mp.nstr(term / h, 12),
                "earlier_probe_limit": mp.nstr(old_limit, 12),
                "residual_halving_ratio": None if ratio is None else mp.nstr(ratio, 6),
            }
        )
        print(
            f"  N={N:5d}  resid={mp.nstr(resid, 4)}  bound={mp.nstr(bound, 4)}"
            f"  holds={holds}"
            + ("" if ratio is None else f"  resid ratio vs prev N={mp.nstr(ratio, 5)}")
        )
        prev_resid = resid

    all_hold = all(r["inequality_holds"] for r in rows)
    # halving h should quarter an O(h^2) residual; accept [3.4, 4.6]
    ratios = [mp.mpf(r["residual_halving_ratio"]) for r in rows if r["residual_halving_ratio"]]
    order_two = all(mp.mpf("3.4") <= t <= mp.mpf("4.6") for t in ratios)
    last = rows[-1]
    term_matches_old = abs(
        mp.mpf(last["scaled_term_over_h"]) - mp.mpf(last["earlier_probe_limit"])
    ) < mp.mpf("1e-3")

    print(
        f"\n  VERDICT: inequality holds at every N ({all_hold}); residual is"
        f" O(h^2) — it quarters when h halves ({order_two}); the identified"
        f" term matches the earlier probe's measured limit ({term_matches_old})."
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
        "scriptFile": "logsine_sharp_constant_check.py",
        "commitSha": commit_sha,
        "description": (
            "Statement-level check of QOU.Knot.FigureEightVolume."
            "phi_smooth_defect_sharp: the proved inequality holds numerically, "
            "its residual is O(h^2) so the identified Euler-Maclaurin term "
            "(h/2)(phi(nh) - phi(h)) is the leading behaviour, and that term "
            "reproduces the limit measured in logsine_smooth_defect_constant.py "
            "-- the 1/2 the antitone squeeze cannot pin (bean qou-shrp)."
        ),
        "computation": "logsine_sharp_constant_check",
        "audit_only": True,
        "precision_dps": 30,
        "rows": rows,
        "inequality_holds_everywhere": all_hold,
        "residual_is_order_h_squared": bool(order_two),
        "identified_term_matches_earlier_limit": bool(term_matches_old),
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).with_name("logsine-sharp-constant-check.witness.json")
    out.write_text(json.dumps(witness, indent=1) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if (all_hold and order_two and term_matches_old) else 1


if __name__ == "__main__":
    sys.exit(main())
