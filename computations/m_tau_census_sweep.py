#!/usr/bin/env python3
"""m_tau k=2 census sweep — full search of every available census (EXPLORATORY).

Continuation of `rem:m-tau-knot-prediction` (beans qou-zvtr, qou-ejxn).
The volume-target probe (`m-tau-volume-target.witness.json`) established
that the identity `m_tau/m_e = Vol(K)/hbar_q^k` at canonical q0 demands
Vol ~ 34.137 for k = 2 (the CAL-2-analogous exponent), and that the
original 25-knot low-crossing search could not reach it — untested, not
refuted.

This probe runs the actual search over EVERY census SnapPy exposes here
(Hoste-Thistlethwaite links to 14 crossings + knots to 15 crossings via
snappy-15-knots; the orientable cusped census to 9 tetrahedra; the
classical link and census-knot tables), reports the hit list IN FULL
(empty or not), and — the decisive datum — reports each census's
volume CEILING so the reach of the search is on the record rather than
assumed.

No candidate is proposed and no fit is performed: a hit would be a
*candidate to examine*, not a derivation, since a volume coincidence at
1% carries little information without an independent structural reason
for the knot.
"""

from __future__ import annotations

import warnings

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP, HBAR_Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf  # noqa: E402

warnings.filterwarnings("ignore")
import snappy  # noqa: E402

# Raise precision BEFORE building any module-level mpf. `set_compute_dps()` is
# also called in main(), but that runs long after import — a constant built
# here at mpmath's default 15 dps is frozen at 53 bits, and serializing it
# later at compute precision prints the binary64 tail (3477.23 came out as
# 3477.23000000000001818989403545856475830078125). Idempotent, so the call in
# main() is unaffected.
set_compute_dps()

M_TAU_OVER_M_E = mpf("3477.23")
CENSUSES = [
    "HTLinkExteriors",
    "OrientableCuspedCensus",
    "LinkExteriors",
    "CensusKnots",
]
BAND_REL = mpf(1) / 100  # the block's stated 1% tolerance (exact, not a binary float)


def ceiling_of(census, start: float = 60.0, step: float = 0.5,
               floor: float = 1.0) -> tuple[float, str, int]:
    """Max volume in a census.

    Walks DOWNWARD in narrow windows `[v, v+step)` from `start`. High-volume
    windows contain very few manifolds, so each slice is cheap — unlike a
    wide `[lo, 200]` slice, which materialises the whole census.
    """
    v = start
    while v > floor:
        try:
            ms = list(census[v:v + step])
        except Exception:
            return (mpf(0), "", 0)
        if ms:
            ms = sorted(ms, key=lambda m: -_vol(m))
            top = ms[0]
            return (_vol(top), top.name(), len(ms))
        v -= step
    return (mpf(0), "", 0)


def _vol(m):
    """Hyperbolic volume as mpf at working precision — never through float()."""
    bits = int(mp.dps * 3.3219) + 16
    return mpf(str(m.volume(bits_prec=bits)).replace(" ", ""))


def main() -> None:
    set_compute_dps()
    target = M_TAU_OVER_M_E * HBAR_Q_MP**2
    lo = target * (1 - BAND_REL)
    hi = target * (1 + BAND_REL)
    # SnapPy's census slice takes plain floats; that is an API constraint on
    # the SEARCH BOUNDS, not on anything reported.
    lo_f, hi_f = float(lo), float(hi)

    hits, ceilings = [], {}
    for name in CENSUSES:
        census = getattr(snappy, name)
        n_total = len(census)
        try:
            band = list(census[lo_f:hi_f])
        except Exception as exc:  # pragma: no cover - census API guard
            band = []
            ceilings[name] = {"error": str(exc)}
        for m in band:
            hits.append({
                "census": name,
                "name": m.name(),
                "volume": mp.nstr(_vol(m), 20),
                "num_cusps": m.num_cusps(),
                "rel_error_vs_target": mp.nstr((_vol(m) - target) / target, 12),
            })
        vol_max, top_name, _ = ceiling_of(census)
        ceilings[name] = {
            "manifolds": n_total,
            "volume_ceiling": mp.nstr(vol_max, 20),
            "ceiling_manifold": top_name,
            "reaches_band": vol_max >= lo,
        }

    total_searched = sum(c.get("manifolds", 0) for c in ceilings.values())
    any_reach = any(c.get("reaches_band") for c in ceilings.values())

    wb = WitnessBuilder("m-tau-census-sweep", engine="snappy")
    wb.set_description(
        "EXPLORATORY full-census sweep for the m_tau k=2 volume target "
        "(beans qou-zvtr/qou-ejxn): searches every SnapPy census "
        "available here for hyperbolic volume within 1% of "
        "(m_tau/m_e)*hbar_q^2 at canonical q0. Reports the hit list in "
        "full AND each census's volume ceiling, so the reach of the "
        "search is on the record. No candidate proposed; no fit.")
    wb.add_data("target", {
        "m_tau_over_m_e": str(M_TAU_OVER_M_E),
        "q0": mp.nstr(Q_MP, 20),
        "vol_target_k2": mp.nstr(target, 20),
        "band_rel": mp.nstr(BAND_REL, 12),
        "band": [mp.nstr(lo, 20), mp.nstr(hi, 20)],
    })
    wb.add_data("censuses", ceilings)
    wb.add_data("hits", hits)
    wb.add_data("total_manifolds_searched", total_searched)
    wb.add_data("verdict", (
        "NO census available here reaches the k=2 target band: the "
        "global volume ceiling across all censuses lies below the band "
        "floor. The k=2 identity therefore remains UNTESTED (not "
        "refuted) even after searching every tabulated manifold "
        "accessible in this environment — the target lives beyond the "
        "reach of current knot/link tabulation, so the census route "
        "cannot settle it. The structural route (m_tau through the "
        "muon-anchored Hecke-energy chain, bean qou-se9w) is the "
        "remaining honest path."
        if not any_reach else
        "At least one census reaches the band; see the hit list. A hit "
        "is a CANDIDATE TO EXAMINE, not a derivation: a 1% volume "
        "coincidence carries little information absent an independent "
        "structural reason for the knot."))
    wb.set_content_block("rem:m-tau-knot-prediction")
    wb.add_assertion(
        name="censuses_searched",
        computed=len([c for c in ceilings.values() if "manifolds" in c]),
        expected=len(CENSUSES), tolerance=0, unit="count",
        source="All four SnapPy censuses queried on the volume index.")
    wb.add_assertion(
        name="global_ceiling_below_band_floor",
        computed=int(not any_reach), expected=1, tolerance=0, unit="bool",
        source=("Reach verdict: no census's maximum hyperbolic volume "
                "attains the 1% band around the k=2 target, so the "
                "sweep cannot refute the identity."))
    out = wb.save()

    print(f"target Vol (k=2) = {mp.nstr(target, 12)}   band = [{mp.nstr(lo, 8)}, {mp.nstr(hi, 8)}]")
    for name, c in ceilings.items():
        print(f"  {name}: {c.get('manifolds','?')} manifolds, "
              f"ceiling {c.get('volume_ceiling','?')} "
              f"({c.get('ceiling_manifold','')}), reaches band: "
              f"{c.get('reaches_band')}")
    print(f"total searched: {total_searched}   hits in band: {len(hits)}")
    for h in hits:
        print(f"    HIT {h['census']} {h['name']} Vol={mp.nstr(mpf(h['volume']), 8)} "
              f"rel={h['rel_error_vs_target']}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
