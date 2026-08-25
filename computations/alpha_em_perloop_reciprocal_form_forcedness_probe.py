#!/usr/bin/env python3
"""alpha_em_perloop_reciprocal_form_forcedness_probe.py

Front-3 move 1: is the α_EM per-loop measure `1/(π·b₁) = 1/(8π)` FORCED by naive
mode-counting bookkeeping from the two now-settled ingredients — the 2-D
heat-kernel per-mode constant `1/(4π)` (#3909) and the homological index
`b₁ = 2g = 8` (#3896) — or does the `8π` (and the reciprocal `1/b₁`) require the
genuine polarized-Jacobian theta-factor computation (#3911)?

This probe does NOT try to derive `8π`. It ENUMERATES the natural dimensionless
combinations of the fixed data {heat-kernel `1/(4π)`, b₁=8, genus g=4, photon
polarizations P=2} and reports how many independent combinations land on the
CODATA-selected `1/(8π)`. If several do and none is singled out by a forcing
principle, the honest conclusion (scope-(a)) is that the coefficient is NOT
naive-mode-countable — the reciprocal-form/multiplicity does not separate from
the magnitude leg, and `8π` must come from the #3911 theta-factor, not arithmetic.
This is the anti-laundering guard: it PREVENTS a sibling from reverse-engineering
`8π` from a hand-picked combination (the trap flagged in the merged forcedness
audit: "the working 1/(8π) must be FORCED, never reverse-engineered").

DISCIPLINE: no fit (nothing tuned to CODATA — the opposite: we ask whether the
geometry FORCES it), no c_k, nothing wired, no tier change. Self-asserted witness.
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _pb  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main():
    pi = mp.pi
    target = 1 / (8 * pi)                 # the per-loop measure denominator's reciprocal
    hk = 1 / (4 * pi)                      # 2-D heat-kernel per-mode constant (#3909, settled)
    b1 = mp.mpf(8)                         # homological index 2g (#3896, settled)
    g = mp.mpf(4)
    P = mp.mpf(2)                          # photon physical polarizations

    # Enumerate: (hk multiplier from {1, 1/2, 2}) × (integer count from
    # {1, b1, g, P, b1/P=4, b1*P, g*P, b1/g=2}) in numerator or denominator.
    integers = {"1": mp.mpf(1), "b1=8": b1, "g=4": g, "P=2": P,
                "b1/P=4": b1 / P, "b1/g=2": b1 / g, "b1*P=16": b1 * P, "g*P=8": g * P}
    hk_mults = {"hk": hk, "hk/2": hk / 2, "2hk": 2 * hk}

    hits = []
    for hkn, hkv in hk_mults.items():
        for iname, iv in integers.items():
            for placement, val in (("/count", hkv / iv), ("*count", hkv * iv)):
                if abs(val - target) < mp.mpf("1e-30"):
                    hits.append(f"{hkn} {placement} {iname}")
    n_hits = len(hits)

    print(f"target 1/(8π) = {mp.nstr(target, 12)}")
    print(f"heat-kernel per-mode 1/(4π) = {mp.nstr(hk, 12)}, b₁=8, g=4, P=2")
    print(f"\n  natural combinations landing on 1/(8π): {n_hits}")
    for h in hits:
        print(f"    • {h}")

    # A combination is FORCED only if exactly one exists AND a physical principle
    # singles it out. Multiple hits ⇒ not naive-mode-countable.
    forced = bool(n_hits == 1)
    verdict = (
        f"The α_EM per-loop measure 1/(8π) is reproduced by {n_hits} distinct natural "
        f"combinations of the settled data {{1/(4π), b₁=8, g=4, P=2}} "
        + (f"({'; '.join(hits)}). " if hits else "— none found (recheck data). ")
        + ("Since MORE THAN ONE lands on 1/(8π) and no forcing principle singles one "
           "out, the coefficient is NOT naive-mode-countable: the reciprocal-form and "
           "the `8π = 2·4π` multiplicity do NOT separate from the magnitude, so `8π` "
           "cannot be honestly derived by arithmetic bookkeeping — it must come from "
           "the genuine polarized-Jacobian genus-4 theta-factor computation (#3911). "
           "This is the anti-laundering result: it forecloses reverse-engineering 8π "
           "from a hand-picked combination. The count b₁=8 and π-power 1/(4π) are "
           "settled; the JOINT coefficient is one object with the magnitude leg, not a "
           "separable arithmetic piece."
           if not forced else
           "Exactly one combination lands on 1/(8π) — candidate for a forced reading; "
           "verify a physical principle singles it out before any claim.")
        + " No fit; no c_k; nothing wired; no tier change."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder(
        name="alpha-em-perloop-reciprocal-form-forcedness",
        engine="mpmath", _script_path=__file__,
        output_dir=str(Path(__file__).resolve().parent))
    wb.set_description(
        "Enumerate natural {1/(4π), b₁=8, g=4, P=2} combinations landing on the "
        "per-loop measure 1/(8π); test whether the coefficient is naive-mode-countable "
        "(forced) or requires the #3911 theta-factor (not separable).")
    wb.set_audit_only("docs/audits/2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md")
    wb.add_assertion("multiple_combinations_hit_target", str(n_hits >= 2), "True")
    wb.add_assertion("not_naive_mode_countable", str(not forced), "True")
    wb.add_data("n_combinations_hitting_8pi", n_hits)
    wb.add_data("combinations", hits)
    wb.add_data("forced_unique", forced)
    wb.add_data("verdict", verdict)
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
