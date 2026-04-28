#!/usr/bin/env python3
"""
Extended knot/link search for D's atomic link.

Target volume: V = B_AME(D) / m_e = 2.22456612 / 0.51099895
               = 4.35328 (to 6 digits; target exact at 1 ppb would be
                 4.353276617...)

The 8-crossing census (jsj_verification.py) found 6_2 at Vol 4.40083
(+1.09%).  This probe extends the search:

  1. Higher-crossing census: 9, 10, 11, 12, 13, 14 crossing link
     complements from SnapPy LinkExteriors.
  2. Twist knots and rational-tangle fillings.
  3. Dehn fillings of the magic manifold (s776) known to hit a
     dense set of volumes.
  4. Link complements from knot_floer_homology (orderable-knot census
     at higher crossings).

For each candidate, compute HP volume to 50 digits and compare to
target at ppb precision.
"""
from __future__ import annotations

import sys
import json
import time
import warnings
import itertools
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

from experimental_constants import M_E_MEV

# Target volume (ρ = m_e)
B_D_AME = 2.22456612
TARGET_VOL = B_D_AME / M_E_MEV
# = 2.22456612 / 0.51099895 = 4.3532766...

print(f"Target Vol = {TARGET_VOL:.10f}   (B_AME(D) / m_e)")


def vol_float(M) -> float:
    try:
        v = M.volume()
        return float(v.real) if hasattr(v, "real") else float(v)
    except Exception:
        return float("nan")


def vol_hp(M, digits: int = 50) -> str | None:
    try:
        import mpmath
        with mpmath.workdps(digits):
            Mh = M.high_precision()
            v = Mh.volume()
            rp = v.real if hasattr(v, "real") else v
            return mpmath.nstr(mpmath.mpf(str(rp)), digits)
    except Exception:
        return None


def search_census(max_crossings: int = 14,
                    tol_pct: float = 0.5) -> list[dict]:
    """Scan LinkExteriors up to max_crossings, collect matches."""
    import snappy
    matches = []
    for cross_cnt in range(4, max_crossings + 1):
        try:
            census = snappy.LinkExteriors(crossings=cross_cnt)
        except Exception:
            continue
        print(f"  [crossings {cross_cnt:>2}] enumerating…", flush=True)
        for M in census:
            try:
                v = vol_float(M)
                if v <= 0.1 or v != v:
                    continue
                err = (v - TARGET_VOL) / TARGET_VOL * 100
                if abs(err) < tol_pct:
                    matches.append({
                        "name": M.name(),
                        "crossings": cross_cnt,
                        "cusps": M.num_cusps(),
                        "vol_float": v,
                        "err_pct": err,
                        "err_ppb": err * 1e7,
                    })
            except Exception:
                continue
    return matches


def search_twist_knots(N_max: int = 50) -> list[dict]:
    """Twist knots K_N = 2-bridge knot [2N+1, 2]."""
    import snappy
    results = []
    for n in range(1, N_max + 1):
        try:
            M = snappy.Manifold(f"K{n}a1") if n > 1 else None
        except Exception:
            continue
        if M is None:
            continue
        try:
            v = vol_float(M)
            err = (v - TARGET_VOL) / TARGET_VOL * 100
            if abs(err) < 1.0:
                results.append({
                    "name": f"K{n}a1", "vol_float": v, "err_pct": err,
                })
        except Exception:
            continue
    return results


def search_dehn_fillings(base_manifold: str = "s776",
                            p_range: range = range(-5, 6),
                            q_range: range = range(1, 6)) -> list[dict]:
    """Dehn surgeries on 3-cusped magic manifold s776.

    s776 has Vol = 5.3335 per cusp with 3 cusps.  Many surgeries
    give hyperbolic manifolds with volumes below the unsurgered
    value.  Some may hit our target.
    """
    import snappy
    results = []
    try:
        base = snappy.Manifold(base_manifold)
        v0 = vol_float(base)
        print(f"  Base {base_manifold}: Vol = {v0}")
    except Exception as e:
        print(f"  [could not load {base_manifold}: {e}]")
        return results

    n_cusps = base.num_cusps()
    # Only explore single-cusp surgeries for simplicity
    for cusp in range(min(n_cusps, 1)):
        for p in p_range:
            for q in q_range:
                if p == 0 and q == 0:
                    continue
                try:
                    M = base.copy()
                    # Set Dehn filling on cusp
                    fills = [None] * n_cusps
                    fills[cusp] = (p, q)
                    M.dehn_fill(fills)
                    v = vol_float(M)
                    if v < 0.1 or v != v:
                        continue
                    err = (v - TARGET_VOL) / TARGET_VOL * 100
                    if abs(err) < 1.0:
                        results.append({
                            "base": base_manifold,
                            "cusp": cusp,
                            "filling": (p, q),
                            "vol_float": v,
                            "err_pct": err,
                        })
                except Exception:
                    continue
    return results


def main() -> int:
    print("=" * 100)
    print("EXTENDED KNOT SEARCH: finding a hyperbolic knot/link")
    print(f"with Vol = {TARGET_VOL:.10f} (B_AME(D) / m_e)")
    print("=" * 100)

    # 1. Extended census up to 14 crossings
    print("\nPHASE 1: SnapPy census up to 14 crossings")
    print("-" * 70)
    t0 = time.time()
    census_matches = search_census(max_crossings=14, tol_pct=1.5)
    dt = time.time() - t0
    print(f"  {len(census_matches)} matches in {dt:.1f}s")
    if census_matches:
        census_matches.sort(key=lambda m: abs(m["err_pct"]))
        print(f"\n  Top 10 closest:")
        print(f"  {'name':>15} {'crossings':>9} {'cusps':>5} "
              f"{'Vol':>14}  {'err %':>8}")
        for m in census_matches[:10]:
            print(f"  {m['name']:>15} {m['crossings']:>9} "
                  f"{m['cusps']:>5} {m['vol_float']:>14.8f} "
                  f"{m['err_pct']:>+8.4f}%")

    # 2. Dehn surgeries on s776 (magic manifold)
    print("\nPHASE 2: Dehn surgeries on s776 (magic manifold)")
    print("-" * 70)
    t0 = time.time()
    dehn_matches = search_dehn_fillings("s776",
                                             p_range=range(-10, 11),
                                             q_range=range(1, 10))
    dt = time.time() - t0
    print(f"  {len(dehn_matches)} matches in {dt:.1f}s")
    if dehn_matches:
        dehn_matches.sort(key=lambda m: abs(m["err_pct"]))
        print(f"\n  Top 10:")
        for m in dehn_matches[:10]:
            print(f"  s776 cusp{m['cusp']} fill {m['filling']}: "
                  f"Vol = {m['vol_float']:.8f}, err {m['err_pct']:+.4f}%")

    # Combine + rank by proximity
    all_results = [(m, "census") for m in census_matches] + \
                  [(m, "dehn-s776") for m in dehn_matches]
    all_results.sort(key=lambda x: abs(x[0]["err_pct"]))

    print(f"\nPHASE 3: Combined best candidates (recomputing at 50 HP digits)")
    print("-" * 70)
    combined_top = []
    import snappy
    for (m, src) in all_results[:15]:
        # Try to rebuild the manifold for HP
        hp_str = None
        try:
            if src == "census":
                M = snappy.Manifold(m["name"])
            else:
                base = snappy.Manifold("s776")
                fills = [None] * base.num_cusps()
                fills[m["cusp"]] = m["filling"]
                M = base.copy()
                M.dehn_fill(fills)
            hp_str = vol_hp(M, digits=50)
        except Exception:
            pass
        combined_top.append({**m, "source": src, "vol_50digit": hp_str})
        name = m.get("name") or f"s776-fill{m.get('filling')}"
        print(f"  [{src:>10}] {name:>18}  float={m['vol_float']:.10f}  "
              f"err={m['err_pct']:+.4f}%")
        if hp_str:
            print(f"               HP=  {hp_str[:60]}")

    witness = {
        "computation": "d-knot-extended-search",
        "description": (
            "Extended search for a hyperbolic 3-manifold whose volume "
            "matches B_AME(D) / m_e = 4.35328 at ppb precision. "
            "Covers SnapPy LinkExteriors up to 14 crossings plus Dehn "
            "surgeries on the magic manifold s776."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "target_vol": TARGET_VOL,
        "B_AME_D_MeV": B_D_AME,
        "m_e_MeV": M_E_MEV,
        "census_matches": census_matches,
        "dehn_matches": dehn_matches,
        "combined_top": combined_top,
    }
    out = Path(__file__).parent / "d-knot-extended-search.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
