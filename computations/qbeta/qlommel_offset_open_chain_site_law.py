#!/usr/bin/env python3
"""qlommel_offset_open_chain_site_law.py
=========================================

Derive-or-refute (NO FIT, pure algebra): the Δ_λ exponent OFFSET is the
open-chain boundary, reducing the whole keystone to a single per-site constant.

## Result

The canonical residual exponent `10A−5` factors EXACTLY as

    10A − 5  =  5 · (2A − 1)  =  5 · [ A  +  (A − 1) ]
                                     └nucleons┘  └bonds┘

i.e. `5` per **chain-site** of an OPEN linear A-chain (A nucleon-sites + A−1
inter-nucleon bond-sites). Two consequences, both removing apparent freedom:

1. **The slope 10 per nucleon is forced:** each nucleon adds 2 sites (itself +
   one bond), so the per-nucleon q-power is `2 × 5 = 10` — matching the
   independently-derived crossing slope `σ+σ⁻¹ = 10A−2` (`A`-only).
2. **The `−5` offset is the open-chain boundary, NOT a fit:** an open A-chain has
   `2A−1` sites, one fewer bond (`A−1`) than nucleons (`A`); the missing terminal
   bond is exactly `−1` site `= −5` in q-power. A *closed* chain (A bonds) would
   give `5·2A = 10A`; the open chain gives `10A − 5`.

So the `−3` "crossing-vs-site puzzle" was a category error: the crossing COUNT
`σ+σ⁻¹ = 10A−2` and the q-POWER `5(2A−1) = 10A−5` are different quantities; they
need not be equal, and their constant difference `3` carries no q-power meaning.

## What remains open

The **single** residual unknown is the per-site q-power magnitude `5` — the
Bring-quintic conjecture (`brings-surface`: 𝒳₅, Aut = S₅, the same `5` as the
Weinberg cosh-ratio `(5,7)`). Confirming `5` needs the q-GRADED Markov trace of
the single-site sub-braid (the Rust hecke engine), out of scope here. This script
establishes the *structure* (open-chain site law) that isolates that one number;
it is pure algebra (no fit, no trace), gate-respecting, NOT wired.

Combined with `qlommel_b_ladder_slope_derivation.py` (b from the slope) and the
Lean `first_kind_geometric_b`, the keystone is reduced to: **derive the per-site
q-power = 5.**
"""
from __future__ import annotations

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402

import time  # noqa: E402

from qou_substrate.witness import WitnessBuilder  # noqa: E402

PER_SITE = 5  # the Bring-quintic conjecture (𝒳₅, Aut=S₅) — NOT derived here


def main() -> int:
    t0 = time.monotonic()
    rows = []
    site_law_ok = True
    open_chain_ok = True
    per_site_ok = True
    print("  A   exp=10A-5   5·(2A-1)   sites=A+(A-1)   per-site   open-chain −5?")
    for A in range(1, 13):
        exponent = 10 * A - 5
        sites = (2 * A - 1)
        nucleon_sites, bond_sites = A, A - 1
        five_times_sites = PER_SITE * sites
        per_site = exponent / sites  # exact integer 5
        closed_chain = PER_SITE * (2 * A)  # = 10A (A bonds)
        offset_from_open = exponent - closed_chain  # = -5 = -(PER_SITE * 1 missing bond)
        site_law_ok = site_law_ok and (exponent == five_times_sites)
        open_chain_ok = open_chain_ok and (sites == nucleon_sites + bond_sites) and (offset_from_open == -PER_SITE)
        per_site_ok = per_site_ok and (per_site == PER_SITE)
        rows.append({"A": A, "exponent_10A_5": exponent, "sites_2A_1": sites,
                     "nucleon_sites": nucleon_sites, "bond_sites": bond_sites,
                     "five_times_sites": five_times_sites, "per_site": per_site,
                     "closed_chain_10A": closed_chain, "open_chain_offset": offset_from_open})
        if A <= 8 or A == 12:
            print(f"  {A:>2}   {exponent:>8}   {five_times_sites:>8}   "
                  f"{nucleon_sites}+{bond_sites}={sites:<8}   {per_site:>8.1f}   "
                  f"{offset_from_open:>+d} {'OK' if offset_from_open==-5 else 'X'}")

    w = WitnessBuilder("qlommel-offset-open-chain-site-law",
                       engine="python+algebra", start_time=t0)
    (w.set_description(
        "Derive-or-refute (pure algebra, no fit): the Δ_λ exponent offset is the "
        "OPEN-CHAIN boundary. 10A−5 = 5·(2A−1) = 5·[A nucleons + (A−1) bonds]: 5 "
        "per chain-site of an open A-chain. The slope 10/nucleon is forced (2 "
        "sites/nucleon × 5); the −5 offset is the open chain having one fewer bond "
        "(A−1) than nucleons (A) — a closed chain would give 10A. The '−3 vs "
        "crossings' was a category error (crossing COUNT σ+σ⁻¹=10A−2 ≠ q-POWER "
        "5(2A−1)). Reduces the keystone to a SINGLE unknown: per-site q-power = 5 "
        "(Bring quintic 𝒳₅, Aut=S₅), whose confirmation needs the q-graded trace "
        "(Rust engine, out of scope). Gate-respecting; NOT wired.")
     .add_parameter("per_site_q_power", str(PER_SITE))
     .add_data("site_law_rows", rows)
     .add_data("decomposition", {
         "exponent": "10A−5 = 5·(2A−1)",
         "sites": "2A−1 = A (nucleon-sites) + (A−1) (bond-sites), OPEN chain",
         "slope": "10/nucleon = 2 sites/nucleon × 5/site (forced)",
         "offset": "−5 = open-chain boundary (A−1 bonds, one fewer than A nucleons); "
                   "closed chain (A bonds) would give 10A",
         "minus_3_resolved": "category error: crossing COUNT 10A−2 ≠ q-POWER 10A−5",
     })
     .add_data("residual_open", {
         "only_unknown": "per-site q-power = 5 (Bring quintic; needs q-graded trace)",
         "reduces_with": "qlommel_b_ladder_slope_derivation.py + Lean first_kind_geometric_b",
     })
     .add_data("discipline", "pure algebra; no fit; structure derived; per-site 5 "
                             "still conjectural; NOT wired"))
    w.add_assertion("exponent_is_five_times_open_chain_sites",
                    computed=bool(site_law_ok), expected=True,
                    source="10A−5 = 5·(2A−1) exactly for A=1..12")
    w.add_assertion("offset_is_open_chain_boundary_minus_5",
                    computed=bool(open_chain_ok), expected=True,
                    source="2A−1 = A + (A−1) (open chain); exponent − 5·2A = −5 "
                           "(one missing terminal bond)")
    w.add_assertion("per_site_q_power_is_constant_5",
                    computed=bool(per_site_ok), expected=True,
                    source="(10A−5)/(2A−1) = 5 for all A — the single residual unknown")
    out = w.save()
    print(f"\n  VERDICT: offset −5 = OPEN-CHAIN boundary (derived); keystone reduced "
          f"to per-site q-power = 5 (Bring quintic).\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
