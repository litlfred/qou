#!/usr/bin/env python3
"""
Census search for failing odd-A / non-α atoms.

The partial-shell linear-interp strategy fails on ⁶Li (+36%), ⁷Li (+31%),
⁹Be (+16%), ¹⁰B (+17%).  We search SnapPy's LinkExteriors census for
hyperbolic links whose volume matches B(atom) / ρ for ρ ∈ {m_e, 2m_e}.

For each atom:
  target_m = B / m_e,  target_2m = B / (2 m_e)
  search manifolds with Vol close (within ±0.5) to either target
  rank by absolute volume difference, emit top 10 candidates

Output: odd-a-census-search.witness.json

Usage:
    python3 computations/odd_a_census_search.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0

try:
    import snappy
except ImportError:
    print("SnapPy not installed; abort.", file=sys.stderr)
    sys.exit(1)

M_E_MEV = 0.51099895

# Failing atoms from the partial-shell sweep
TARGETS = [
    # (label, Z, N, B_AME_MeV)
    ("6Li",  3, 3, 31.9941),
    ("7Li",  3, 4, 39.2446),
    ("9Be",  4, 5, 58.1651),
    ("10B",  5, 5, 64.7512),
    # bonus: even-A non-magic for comparison
    ("10Be", 4, 6, 64.9775),
    ("11B",  5, 6, 76.2054),
]

MAX_CROSSINGS = 11      # census available up to ~13 crossings
VOL_WINDOW   = 0.5      # ± window in hyperbolic units around target


def search_for_target(target_vol: float, max_crossings: int,
                      window: float) -> list[dict]:
    candidates = []
    for n_cross in range(3, max_crossings + 1):
        try:
            it = snappy.LinkExteriors(crossings=n_cross)
        except Exception as e:
            print(f"  Warning: could not open LinkExteriors(crossings={n_cross}): {e}",
                  file=sys.stderr)
            continue
        for M in it:
            try:
                v_raw = M.volume()
                v = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
            except Exception as e:
                try:
                    mname = M.name()
                except Exception:
                    mname = "<unknown>"
                print(f"  Warning: could not get volume for {mname}: {e}",
                      file=sys.stderr)
                continue
            if abs(v - target_vol) <= window:
                try:
                    sol = str(M.solution_type())
                except Exception:
                    sol = "unknown"
                try:
                    cusps = M.num_cusps()
                except Exception:
                    cusps = -1
                candidates.append({
                    "name": M.name(),
                    "crossings": n_cross,
                    "cusps": cusps,
                    "volume": v,
                    "target_vol": target_vol,
                    "err_pct": 100.0 * (v - target_vol) / target_vol,
                    "err_abs": v - target_vol,
                    "solution_type": sol,
                })
    candidates.sort(key=lambda c: abs(c["err_abs"]))
    return candidates


def main() -> int:
    print(f"\n  Substrate q_0 = {Q0:.6f}")
    print(f"  m_e = {M_E_MEV:.6f} MeV, searching links with crossings ≤ {MAX_CROSSINGS}")
    print(f"  Volume window ± {VOL_WINDOW:.2f} around B/ρ targets\n")

    witness_rows = []
    for label, Z, N, B_ame in TARGETS:
        print(f"  ── {label} (Z={Z}, N={N}, B={B_ame:.4f} MeV) ──────────")
        t_me = B_ame / M_E_MEV
        t_2me = B_ame / (2 * M_E_MEV)
        print(f"    target Vol under ρ=m_e   : {t_me:.4f}")
        print(f"    target Vol under ρ=2m_e  : {t_2me:.4f}")

        me_candidates = search_for_target(t_me, MAX_CROSSINGS, VOL_WINDOW)
        tme_candidates = search_for_target(t_2me, MAX_CROSSINGS, VOL_WINDOW)

        print(f"    ρ = m_e top 5 matches:")
        for c in me_candidates[:5]:
            print(f"      {c['name']:>16}  n={c['crossings']}  "
                  f"cusps={c['cusps']}  Vol={c['volume']:8.4f}  "
                  f"err={c['err_pct']:+.3f}%  sol={c['solution_type']}")
        print(f"    ρ = 2m_e top 5 matches:")
        for c in tme_candidates[:5]:
            print(f"      {c['name']:>16}  n={c['crossings']}  "
                  f"cusps={c['cusps']}  Vol={c['volume']:8.4f}  "
                  f"err={c['err_pct']:+.3f}%  sol={c['solution_type']}")

        witness_rows.append({
            "atom": label,
            "Z": Z,
            "N": N,
            "A": Z + N,
            "B_AME_MeV": B_ame,
            "target_vol_me": t_me,
            "target_vol_2me": t_2me,
            "matches_me": me_candidates[:10],
            "matches_2me": tme_candidates[:10],
        })
        print()

    witness = {
        "name": "odd-a-census-search",
        "description": (
            "SnapPy LinkExteriors census search for atomic links "
            "matching B/ρ for ρ ∈ {m_e, 2m_e}.  Targets are the "
            "odd-A and non-α atoms where the partial-shell "
            "interpolation fails (⁶Li, ⁷Li, ⁹Be, ¹⁰B) plus "
            "even-A non-magic (¹⁰Be, ¹¹B) for comparison."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": Q0,
            "M_E_MEV": M_E_MEV,
            "max_crossings": MAX_CROSSINGS,
            "vol_window": VOL_WINDOW,
        },
        "rows": witness_rows,
    }
    out = Path(__file__).parent / "odd-a-census-search.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"  Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
