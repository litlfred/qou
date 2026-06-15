#!/usr/bin/env python3
"""
Phase 3 — atom-knot search by SDP-style integer enumeration.

Adapts the atom_sdp_gluon_search framework to target link-closure
volume instead of Markov trace.  For each per-nucleon gluon
combination × mixed-crossing lift rule × braid-interleave policy,
we build a literal braid word, close it via SnapPy, and compute
Vol_hyp of the exterior.  Rank by |Vol - B_AME/ρ_F| to find the
atom-knot whose complement's volume matches the Kashaev target.

If the best match has Vol matching B_AME/ρ_F at ppb-precision,
Phase 3 is solved for that atom.  If not, the best hit tells us
how close the braid-word space can approach the target.

Default: deuterium (Z=1, N=1, ρ_F=m_e, target Vol = B_AME(D)/m_e).
"""
from __future__ import annotations

import sys
import json
import math
import time
import warnings
import itertools
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import HA as H_VAL
from atom_sdp_gluon_search import (
    atom_word_with_gluons, CANDIDATES_DUAL, CANDIDATES_EXTENDED,
)
from experimental_constants import M_E_MEV

try:
    import snappy as _snappy
    _SNAPPY_AVAILABLE = True
except ImportError:
    _snappy = None
    _SNAPPY_AVAILABLE = False


# Target volume: B_AME/ρ_F.  For D at ρ_F=m_e: 2.22456612 / 0.51099895
B_D_AME = 2.22456612
B_T_AME = 8.4817984
B_3HE_AME = 7.7180375

TARGETS = {
    "D":   {"Z": 1, "N": 1, "B_AME": B_D_AME,   "rho_factor": 1},
    "T":   {"Z": 1, "N": 2, "B_AME": B_T_AME,   "rho_factor": 2},
    "3He": {"Z": 2, "N": 1, "B_AME": B_3HE_AME, "rho_factor": 2},
}


def classify_hecke_factor(c: float, d: float) -> str:
    """Return 'pos', 'neg', or 'mixed' for the Hecke factor c·T + d."""
    if abs(c - 1.0) > 1e-6:
        raise ValueError(f"c={c} not supported")
    if abs(d) < 1e-9:
        return "pos"
    if abs(d + H_VAL) < 1e-6:
        return "neg"
    if abs(d + H_VAL / 2) < 1e-6:
        return "mixed"
    raise ValueError(f"unsupported d={d}")


def lift_to_braid(triples, mixed_rule: str,
                    interleave: str = "interleaved",
                    A: int = 2) -> list[int]:
    """Translate Hecke factors (c, d, g) into signed braid generator ints.

    mixed_rule ∈ {'pos', 'neg', 'both', 'alternating'}.  For 'both'
    we emit σ_g THEN σ_g⁻¹ (Markov-stabilization-like pair), so the
    mixed crossing splits across two braid positions.
    """
    # Split triples into per-nucleon chunks (g in [3k, 3k+2])
    by_nucleon = [{"g0": [], "g1": [], "inter": []} for _ in range(A)]
    for (c, d, g) in triples:
        kind = classify_hecke_factor(c, d)
        k = g // 3
        sub = g % 3
        if k >= A:
            continue  # safety
        target = ("g0", "g1", "inter")[sub]
        by_nucleon[k][target].append((g, kind))

    word: list[int] = []
    n_alt = 0

    def emit(g: int, kind: str):
        nonlocal n_alt
        if kind == "pos":
            word.append(+(g + 1))
        elif kind == "neg":
            word.append(-(g + 1))
        elif kind == "mixed":
            if mixed_rule == "pos":
                word.append(+(g + 1))
            elif mixed_rule == "neg":
                word.append(-(g + 1))
            elif mixed_rule == "both":
                word.append(+(g + 1))
                word.append(-(g + 1))
            elif mixed_rule == "alternating":
                sign = +1 if (n_alt % 2 == 0) else -1
                word.append(sign * (g + 1))
                n_alt += 1
            else:
                raise ValueError(f"mixed_rule {mixed_rule!r}")

    for k, block in enumerate(by_nucleon):
        g0c, g1c, ic = block["g0"], block["g1"], block["inter"]
        if interleave == "block":
            for g, kind in g0c:
                emit(g, kind)
            for g, kind in g1c:
                emit(g, kind)
        elif interleave == "interleaved":
            lim = max(len(g0c), len(g1c))
            for i in range(lim):
                if i < len(g0c):
                    g, kind = g0c[i]
                    emit(g, kind)
                if i < len(g1c):
                    g, kind = g1c[i]
                    emit(g, kind)
        else:
            raise ValueError(f"interleave {interleave!r}")
        for g, kind in ic:
            emit(g, kind)
    return word


def vol_of_closure(word: list[int], digits: int = 50):
    """Return (v_float, v_hp_str_or_None, err) from SnapPy."""
    if not _SNAPPY_AVAILABLE:
        return None, None, "snappy_missing"
    try:
        L = _snappy.Link(braid_closure=word)
        E = L.exterior()
        v_raw = E.volume()
        v = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
    except Exception as e:
        return None, None, str(e)
    from hp_volume import hp_volume_of_manifold
    hp_str = hp_volume_of_manifold(E, digits=digits) if v > 0.5 else None
    return v, hp_str, None


def search_atom(atom_key: str,
                 mixed_rules: tuple = ("pos", "neg", "both", "alternating"),
                 interleaves: tuple = ("interleaved", "block"),
                 m_pp_range=(1,), m_pn_range=(1, 2),
                 m_nn_range=(1,),
                 gluon_set=None,
                 top_n: int = 10):
    """Search the (gluon × mixed_rule × interleave × multiplicity) grid
    for the braid word whose closure has Vol closest to B_AME/ρ."""
    t0 = time.time()
    info = TARGETS[atom_key]
    Z, N = info["Z"], info["N"]
    A = Z + N
    rho_f = info["rho_factor"]
    target_vol = info["B_AME"] / (rho_f * M_E_MEV)
    B_AME = info["B_AME"]

    print(f"  Target: Vol = B_AME({atom_key})/(ρ_F·m_e) = {target_vol:.10f}")
    print(f"          (ρ_F = {rho_f}·m_e)")

    if gluon_set is None:
        gluon_set = list(CANDIDATES_DUAL.keys())  # K=5: ∅,σ0,σ1,L+,L−
    gluon_combos = list(itertools.product(gluon_set, repeat=A))
    total = (len(gluon_combos) * len(mixed_rules) * len(interleaves)
             * len(m_pp_range) * len(m_pn_range) * len(m_nn_range))
    print(f"  Enumerating {total} combinations…")

    all_results = []
    for gluons in gluon_combos:
        for mr in mixed_rules:
            for il in interleaves:
                for m_pp in m_pp_range:
                    for m_pn in m_pn_range:
                        for m_nn in m_nn_range:
                            try:
                                triples = atom_word_with_gluons(
                                    Z, N, gluons,
                                    include_inter=True,
                                    m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                )
                                word = lift_to_braid(
                                    triples, mixed_rule=mr,
                                    interleave=il, A=A,
                                )
                            except Exception:
                                continue
                            v, _hp, err = vol_of_closure(word, digits=15)
                            if v is None or v <= 0.01:
                                continue
                            d_vol = v - target_vol
                            rel = d_vol / target_vol if target_vol else 0
                            all_results.append({
                                "gluons": list(gluons),
                                "mixed_rule": mr,
                                "interleave": il,
                                "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
                                "word_len": len(word),
                                "vol_float": v,
                                "delta_vol": d_vol,
                                "rel_err": rel,
                            })
    # Sort by |rel_err|
    all_results.sort(key=lambda r: abs(r["rel_err"]))

    # Recompute HP Vol for top-N
    for r in all_results[:top_n]:
        triples = atom_word_with_gluons(
            Z, N, tuple(r["gluons"]),
            include_inter=True,
            m_pp=r["m_pp"], m_pn=r["m_pn"], m_nn=r["m_nn"],
        )
        word = lift_to_braid(
            triples, mixed_rule=r["mixed_rule"],
            interleave=r["interleave"], A=A,
        )
        v, hp, _err = vol_of_closure(word, digits=50)
        r["vol_50digit"] = hp

    elapsed = time.time() - t0
    return {
        "atom": atom_key, "Z": Z, "N": N, "A": A,
        "target_vol": target_vol,
        "B_AME_MeV": B_AME,
        "rho_factor": rho_f,
        "n_enumerated": len(all_results),
        "elapsed_sec": elapsed,
        "top": all_results[:top_n],
    }


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(
        description="Phase 3 — atom-knot SDP-style enumeration")
    ap.add_argument("--atom", default="D", choices=list(TARGETS.keys()))
    ap.add_argument("--top", type=int, default=10)
    args = ap.parse_args()

    print("=" * 110)
    print(f"PHASE 3 — atom-knot search for {args.atom}")
    print("=" * 110)
    res = search_atom(args.atom, top_n=args.top)

    print(f"\n  Enumerated {res['n_enumerated']} valid closures "
          f"in {res['elapsed_sec']:.1f}s")
    print(f"  Target Vol = {res['target_vol']:.10f}   "
          f"(B_AME / (ρ_F·m_e))")
    print()
    print(f"  {'rank':>4}  {'vol_float':>18}  {'|rel_err|':>12}  "
          f"{'interleave':>11}  {'mixed':>11}  {'m_pn':>4}  {'gluons':<25}")
    print("  " + "-" * 100)
    for i, r in enumerate(res["top"]):
        print(f"  {i+1:>4}  {r['vol_float']:>18.10f}  "
              f"{abs(r['rel_err']):>12.3e}  "
              f"{r['interleave']:>11}  {r['mixed_rule']:>11}  "
              f"{r['m_pn']:>4}  {','.join(r['gluons']):<25}")
        if r.get("vol_50digit"):
            print(f"         HP = {r['vol_50digit']}")

    witness = {
        "computation": "atom-knot-search",
        "description": (
            "Phase 3: search per-nucleon gluon × mixed-crossing-lift "
            "× braid-interleave × inter-multiplicity grid for braid "
            "words whose Markov closure has Vol_hyp matching "
            "B_AME/(ρ_F · m_e) at high precision.  An SDP-style "
            "integer enumeration adapted from atom_sdp_gluon_search.py "
            "— but targets link-closure volume instead of Markov "
            "trace."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "atom": args.atom,
            "m_e_MeV": M_E_MEV,
            "h_value": H_VAL,
        },
        "result": res,
    }
    out = Path(__file__).parent / f"atom-knot-search-{args.atom}.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
