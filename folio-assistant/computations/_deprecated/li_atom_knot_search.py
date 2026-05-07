#!/usr/bin/env python3
"""[DEPRECATED] Atom-knot identification for ⁶Li and ⁷Li by VOLUME MATCHING.

⚠️  DEPRECATION NOTICE (2026-04-26):

    This script is REVERSE-ENGINEERED methodology and is NOT a principled
    derivation.  It searches the SnapPy hyperbolic-knot databases for a
    knot whose volume matches the AME binding-energy target — i.e. it
    USES the answer to find the knot, rather than DERIVING the knot from
    the GB-NF source of truth.

    The principled path (see `confined-particle.md` + `mass-table-ppb`)
    is:
       GB-NF(particle)  →  T_w ∈ H_{n_0}(q_0)
                        →  Markov closure (knot/link complement)
                        →  Vol_hyp (computed from closure)
                        →  B_pred = ρ · m_e · Vol_hyp
       compared a posteriori to AME.

    Volume-match search short-circuits steps 1–3.  At an 11-crossing
    search of ~2400 knots/links, a 4-ppb residual (⁷Li at L_{11a62})
    is striking BUT cannot be distinguished from a numerical
    coincidence without an independent derivation of the braid word
    in H_21(q_0).  Likewise the ⁶Li K_{11a259} fit at 165,000 ppb
    is at the noise floor of the search.

    USE THIS SCRIPT ONLY for:
      - reproducing the historical claim (⁶Li=K11a259, ⁷Li=L11a62)
      - generating a list of CANDIDATE knots to be checked against an
        independently-derived braid NF (when that becomes available)

    DO NOT USE for:
      - claiming a particle-knot identification as principled
      - generating new mass predictions in the atlas

    See `methodology-deprecation.witness.json` for the per-particle
    methodology audit and the deprecation rationale.

Mass-table-ppb framework:
    B_pred(K) = ρ · m_e · Vol_hyp(K)
where ρ ∈ {1, 2, 3, ...} is an integer prefactor and Vol_hyp is the
hyperbolic volume of the knot/link complement.

For ⁶Li: B_AME = 31.99405 MeV, m_e = 0.51099895 MeV.
For ⁷Li: B_AME = 39.24452 MeV.

Target Vol values (B_AME / (ρ · m_e)) over ρ = 1, ..., 8:

    ⁶Li: ρ=1→62.6, ρ=2→31.3, ρ=3→20.9, ρ=4→15.7, ρ=5→12.5, ρ=6→10.4, ρ=7→8.94, ρ=8→7.82
    ⁷Li: ρ=1→76.8, ρ=2→38.4, ρ=3→25.6, ρ=4→19.2, ρ=5→15.4, ρ=6→12.8, ρ=7→11.0, ρ=8→9.59

Strategy (volume-match, NOT derivation):
  1. Enumerate hyperbolic knots & links from SnapPy's manifold tables
     up to crossing-number 11 (covers volumes 0 to ~20).
  2. For each, compute Vol_hyp.
  3. For each (ρ, target), find best-matching knot with |Vol - target|
     minimised.
  4. Report ppb residual.
"""
from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")


def _emit_deprecation_warning():
    """Emit a runtime DeprecationWarning so anyone re-running this
    script sees the methodology caveat."""
    import warnings as _w
    _w.warn(
        "li_atom_knot_search.py is DEPRECATED methodology — see "
        "methodology-deprecation.witness.json for the principled "
        "GB-NF → Markov-closure path. This script searches by "
        "volume-match, which reverse-engineers the answer.",
        DeprecationWarning,
        stacklevel=2,
    )


_emit_deprecation_warning()


# AME 2020 binding energies (MeV)
B_AME_6Li = 31.99405
B_AME_7Li = 39.24452
m_e = 0.51099895


def enumerate_hyperbolic_volumes(max_crossings=11, max_chern=5):
    """Walk SnapPy's HTLinkExteriors and OrientableCuspedCensus
    up to max_crossings; yield (name, volume, source)."""
    import snappy

    out = []
    # Knot tables (RolfsenTable up to 10 crossings, KnotExteriors via snappy)
    print(f"Enumerating knots up to {max_crossings} crossings...", file=sys.stderr)
    try:
        for c in range(3, max_crossings + 1):
            tbl = snappy.HTLinkExteriors(crossings=c)
            for i, M in enumerate(tbl):
                try:
                    M.simplify()
                    vol = float(M.volume())
                    if vol > 0.01:  # skip non-hyperbolic
                        out.append((str(M), vol, f"HT-{c}cr"))
                except Exception:
                    continue
                if i > 1500:  # cap per crossing-class to keep runtime sane
                    break
    except Exception as e:
        print(f"  HTLink iteration error: {e}", file=sys.stderr)

    # Add the orientable cusped census (small-volume manifolds m000-m999)
    print("Adding orientable cusped census manifolds (m000-m999)...", file=sys.stderr)
    try:
        for M in snappy.OrientableCuspedCensus[:1000]:
            try:
                vol = float(M.volume())
                if vol > 0.01:
                    out.append((str(M), vol, "OCC"))
            except Exception:
                continue
    except Exception as e:
        print(f"  OCC iteration error: {e}", file=sys.stderr)

    # Deduplicate by volume (knots often have multiple representations)
    seen_vols = set()
    dedup = []
    for n, v, s in out:
        v_key = round(v * 1e6) / 1e6
        if v_key in seen_vols:
            continue
        seen_vols.add(v_key)
        dedup.append((n, v, s))
    print(f"Total: {len(out)} → {len(dedup)} after volume-dedup",
          file=sys.stderr)
    return dedup


def find_best(target_vol, knots, top_k=5):
    """Find top-k knots matching target volume, sorted by |Vol - target|."""
    return sorted(
        ((n, v, s, abs(v - target_vol)) for (n, v, s) in knots),
        key=lambda x: x[3],
    )[:top_k]


def main():
    print("=" * 78)
    print("⁶Li, ⁷Li ATOM-KNOT IDENTIFICATION via mass-table-ppb framework")
    print("=" * 78)
    print(f"  m_e = {m_e} MeV")
    print(f"  ⁶Li B_AME = {B_AME_6Li} MeV  (target Vol = B/(ρ·m_e))")
    print(f"  ⁷Li B_AME = {B_AME_7Li} MeV")
    print()

    # Enumerate hyperbolic knots
    knots = enumerate_hyperbolic_volumes(max_crossings=11)
    print()
    print(f"Searching {len(knots)} hyperbolic knot/link complements...")
    print()

    results = {"6Li": {}, "7Li": {}}

    for ame, label, bind in [(B_AME_6Li, "6Li", B_AME_6Li),
                              (B_AME_7Li, "7Li", B_AME_7Li)]:
        print(f"--- {label} (B_AME = {bind} MeV) ---")
        print(f"{'ρ':>3} {'target Vol':>12} {'best K':>30} {'Vol(K)':>10} "
              f"{'|err MeV|':>10} {'|err pct|':>10} {'|err ppb|':>14}")
        print("-" * 95)
        for rho in range(1, 9):
            target = bind / (rho * m_e)
            best = find_best(target, knots, top_k=1)
            if not best:
                continue
            n, v, s, _ = best[0]
            B_pred = rho * m_e * v
            err_mev = B_pred - bind
            err_pct = err_mev / bind * 100
            err_ppb = err_mev / bind * 1e9
            results[label][str(rho)] = {
                "target_vol": target,
                "best_knot": n,
                "vol": v,
                "source": s,
                "B_pred": B_pred,
                "err_mev": err_mev,
                "err_pct": err_pct,
                "err_ppb": err_ppb,
            }
            print(f"{rho:>3} {target:>12.4f} {n:>30} {v:>10.4f} "
                  f"{abs(err_mev):>10.4f} {abs(err_pct):>9.3f}% "
                  f"{abs(err_ppb):>14.2e}")
        print()

    # Save witness
    out = {
        "computation": "li-atom-knot-search",
        "description": (
            "⁶Li, ⁷Li atom-knot identification via mass-table-ppb framework: "
            "B_pred = ρ · m_e · Vol_hyp(K). Searches hyperbolic knots/links "
            "with crossing number ≤ 11 from SnapPy HTLinkExteriors + "
            "OrientableCuspedCensus."
        ),
        "B_AME_6Li": B_AME_6Li,
        "B_AME_7Li": B_AME_7Li,
        "m_e_MeV": m_e,
        "n_knots_searched": len(knots),
        "results": results,
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }
    out_path = Path(__file__).parent / "li-atom-knot-search.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")

    # Summary
    print()
    print("=" * 78)
    print("BEST MATCHES")
    print("=" * 78)
    for label in ["6Li", "7Li"]:
        if not results[label]:
            continue
        # Find the (ρ, knot) with smallest error percentage
        best = min(results[label].items(),
                   key=lambda kv: abs(kv[1]["err_pct"]))
        rho, info = best
        print(f"\n  {label}: ρ = {rho}, K = {info['best_knot']}")
        print(f"     Vol = {info['vol']:.6f}")
        print(f"     B_pred = {info['B_pred']:.4f} MeV  vs  B_AME = "
              f"{B_AME_6Li if label == '6Li' else B_AME_7Li:.4f} MeV")
        print(f"     err = {info['err_pct']:+.4f}% = {info['err_ppb']:+.2e} ppb")


if __name__ == "__main__":
    main()
