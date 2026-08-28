#!/usr/bin/env python3
"""The Whitehead diagonal q-difference recurrence hunt — now with the fast,
exact weight-block tower (no external formula; the engine is Masbaum- +
full-engine-validated).

This is the payoff of the whole #2 chain: fast exact tower (weight-block) →
the mod-p nullspace certificate (proven end-to-end on 4₁, recovering
r2W4-inhomog / r3W4-homog) → the Whitehead diagonal recurrence, whose
fundamental solution's top row at q=1 is GGMW's c_{σ_geom} (the "factor").

Audit-only; no wiring.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from whitehead_weightblock_engine import colored_jones_weightblock  # noqa: E402
from whitehead_diagonal_recurrence_hunt import PRIMES, BASES        # noqa: E402
from takata_fig8_recurrence_hunt import hunt_on_tower               # noqa: E402

WH = [1, -2, 1, -2, 1]


def main() -> int:
    Nmax = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 28
    samples = [(p, t) for p in PRIMES[:2] for t in BASES[:2]]
    print(f"Whitehead diagonal recurrence hunt (weight-block tower, Nmax={Nmax})\n")

    t0 = time.time()
    towers = {}
    for (p, t) in samples:
        tt = time.time()
        towers[(p, t)] = {N: colored_jones_weightblock(WH, N, t, p) for N in range(1, Nmax + 1)}
        print(f"  tower (p={p},t={t}) built in {time.time()-tt:.0f}s")
    print(f"  all towers: {time.time()-t0:.0f}s\n  hunt grid (H/I = homog/inhomog):")

    # windows that FIT the weight-block ceiling (Nmax≈30): unknowns must be
    # < Nmax−r−checks. Small, but a positive here is a real recurrence; a
    # negative is an honest ceiling statement (fig-8 needed r2W4 ⇒ Nmax≳44).
    grid = [(1, 2, True), (2, 2, True), (2, 3, False), (1, 4, True),
            (2, 2, False), (1, 3, True), (3, 1, True), (2, 3, True)]
    res = {}
    for (r, W, inh) in grid:
        out = hunt_on_tower(towers, Nmax, r, W, inhomog=inh)
        key = f"r{r}_W{W}_{'I' if inh else 'H'}"
        res[key] = out["status"]
        print(f"    r={r} W={W} {'I' if inh else 'H'}: {out['status']}")

    hits = [k for k, v in res.items() if v == "CERTIFIED"]
    minwin = hits[0] if hits else None
    print(f"\n  ⇒ Whitehead diagonal recurrence recovered? "
          f"{'YES at ' + minwin if hits else 'NO — raise Nmax / widen grid'}")

    wit = {
        "description": "Whitehead diagonal q-difference recurrence hunt via the fast weight-block exact tower + the (4₁-validated) mod-p nullspace certificate. Toward J_red -> c_sigma.",
        "computation": "whitehead_recurrence_hunt_fast", "audit_only": True,
        "whitehead_braid_word": "[1,-2,1,-2,1]", "Nmax": Nmax,
        "tower": "weight-block engine (validated vs full colored_jones_modp N=2..6)",
        "grid_results": res, "certified_windows": hits, "min_window": minwin,
        "wall_seconds": f"{time.time() - t0:.3f}",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out = Path(__file__).resolve().parent / "whitehead-recurrence-hunt-fast.witness.json"
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
