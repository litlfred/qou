#!/usr/bin/env python3
"""
Atom → knot derivation (Phase 3 of 1-ppb path).

Replaces the SnapPy census search in `jsj_verification.py` with a
direct derivation: build the 3A-strand braid word for atom (Z, N) via
`atom_braid_word_3A`, translate each Hecke factor back to a signed
braid generator, close the braid, and extract the exterior's
hyperbolic volume.

Hecke factor → braid generator dictionary
-----------------------------------------

Each factor is ``(c, d, g)`` representing ``c·T_g + d·1`` in H_{3A}(q).
By the Hecke relation ``T² = h·T + 1`` (with ``h = q − q⁻¹``):

  * ``T`` is the image of the positive braid generator ``σ_g``;
  * ``T⁻¹ = T − h`` is the image of ``σ_g⁻¹``.

So the translation is:

  * ``(1, 0, g)      → +(g+1)``   (σ_g)
  * ``(1, -h, g)     → -(g+1)``   (σ_g⁻¹)
  * ``(1, -h/2, g)   → +(g+1)``   (mixed; average of σ and σ⁻¹ —
                                   we pick σ as the canonical rep;
                                   see `MIXED_CROSSING_RULE`)

Mixed crossings (proton-neutron) correspond to the Hecke element
``(T + T⁻¹)/2`` and do NOT lift to a single braid generator.  We
approximate by picking ``+σ_g``; the other choices (``-σ_g``, or
splitting into two terms) can be explored by setting
``MIXED_CROSSING_RULE``.

Output
------

For each atom: float volume, 50-digit high-precision volume, and
comparison to B_AME/ρ for ρ ∈ {m_e, 2 m_e}.  Writes a witness JSON
and a text summary.
"""
from __future__ import annotations

import sys
import json
import math
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import HA as H_VAL  # h = q - q⁻¹ at q₀
from mass_at_3A_proper import atom_braid_word_3A

try:
    import snappy as _snappy
    _SNAPPY_AVAILABLE = True
except ImportError:
    _snappy = None
    _SNAPPY_AVAILABLE = False

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G
M_E_MEV = 0.51099895

MIXED_CROSSING_RULE = "positive"  # "positive" | "negative" | "alternating"

# Interleaving policy for the (σ_0^a σ_1^b) chain inside one nucleon.
# "block"       → σ_0^a · σ_1^b   (Hecke-algebra equivalent but braid-group
#                                  collapses: closure is non-hyperbolic).
# "interleaved" → (σ_0 σ_1)^gcd(a,b) ... honest braid-group lift of the
#                 confinement chain (σ_0 σ_1⁻¹)^3.  Gives Borromean rings
#                 for a single nucleon at q₀.
BRAID_INTERLEAVE = "block"  # "block" | "interleaved"

ATOMS = [
    ("D",   1, 1,   2.22452),
    ("T",   1, 2,   8.481821),
    ("3He", 2, 1,   7.718043),
    ("4He", 2, 2,  28.295674),
]


def _classify_factor(c: float, d: float) -> str:
    """Map ``(c, d)`` to 'pos', 'neg', or 'mixed'."""
    if abs(c - 1.0) > 1e-6:
        raise ValueError(f"unsupported c={c} (expected 1)")
    # Single tolerance for all classifications.
    TOL = 1e-7
    if abs(d) < TOL:
        return "pos"
    if abs(d + H_VAL) < TOL:
        return "neg"
    if abs(d + H_VAL / 2) < TOL:
        return "mixed"
    raise ValueError(f"unsupported d={d} (not 0, -h, -h/2)")


def atom_to_braid_word(Z: int, N: int,
                         mixed_rule: str = MIXED_CROSSING_RULE,
                         interleave: str = BRAID_INTERLEAVE,
                         ) -> tuple[list[int], dict]:
    """Return (signed-int braid word, stats dict).

    interleave="block"       → literal order from atom_braid_word_3A
    interleave="interleaved" → for each nucleon, interleave its g_0 chain
                               with its g_1 chain to restore braid-group
                               faithfulness (σ_0 σ_1)-style alternation.
    """
    triples = atom_braid_word_3A(Z, N)
    counts = {"pos": 0, "neg": 0, "mixed": 0}
    n_mixed_pos = 0

    def _sign(kind: str) -> int:
        nonlocal n_mixed_pos
        if kind == "pos":
            return +1
        if kind == "neg":
            return -1
        if mixed_rule == "positive":
            return +1
        if mixed_rule == "negative":
            return -1
        if mixed_rule == "alternating":
            s = +1 if (n_mixed_pos % 2 == 0) else -1
            n_mixed_pos += 1
            return s
        raise ValueError(f"unknown mixed_rule: {mixed_rule}")

    word: list[int] = []
    if interleave == "block":
        for c, d, g in triples:
            kind = _classify_factor(c, d)
            counts[kind] += 1
            word.append(_sign(kind) * (g + 1))
    elif interleave == "interleaved":
        # Split triples into per-nucleon chunks.  Each nucleon k
        # contributes a g0 chain (at gen 3k), a g1 chain (at gen 3k+1),
        # and an optional inter-nucleon block at gen 3k+2.  Interleave
        # g0 and g1 chains by zip-padding.
        by_nucleon: list[dict] = []
        current: dict = {"g0": [], "g1": [], "inter": []}
        triples_with_kind = [(c, d, g, _classify_factor(c, d))
                               for (c, d, g) in triples]
        # assume triples come in order: nucleon 0 g0 chain, g1 chain,
        # then inter, nucleon 1 g0 chain, g1 chain, inter, ...
        for (c, d, g, kind) in triples_with_kind:
            k = g // 3
            sub = g % 3   # 0 → g0, 1 → g1, 2 → inter
            while len(by_nucleon) <= k:
                by_nucleon.append({"g0": [], "g1": [], "inter": []})
            target = ("g0", "g1", "inter")[sub]
            by_nucleon[k][target].append((g, kind))
        for k, block in enumerate(by_nucleon):
            g0c, g1c, ic = block["g0"], block["g1"], block["inter"]
            # interleave g0 and g1 by zipping with padding
            lim = max(len(g0c), len(g1c))
            for i in range(lim):
                if i < len(g0c):
                    g, kind = g0c[i]
                    counts[kind] += 1
                    word.append(_sign(kind) * (g + 1))
                if i < len(g1c):
                    g, kind = g1c[i]
                    counts[kind] += 1
                    word.append(_sign(kind) * (g + 1))
            # inter-nucleon crossings kept as a trailing block
            for g, kind in ic:
                counts[kind] += 1
                word.append(_sign(kind) * (g + 1))
    else:
        raise ValueError(f"unknown interleave policy: {interleave}")

    stats = {
        "n_factors": len(triples),
        "counts": counts,
        "mixed_rule": mixed_rule,
        "interleave": interleave,
        "n_strands": 3 * (Z + N),
        "max_generator": max((abs(x) for x in word), default=0),
    }
    return word, stats


def volume_of_closure(word: list[int], digits: int = 50) -> dict:
    """Close braid, compute Vol of exterior (float + HP)."""
    if not _SNAPPY_AVAILABLE:
        return {"status": "snappy_missing"}
    try:
        L = _snappy.Link(braid_closure=word)
        E = L.exterior()
    except Exception as e:
        return {"status": "construction_error", "error": str(e)}
    try:
        v_raw = E.volume()
        v_float = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
    except Exception as e:
        return {"status": "volume_error", "error": str(e)}
    # Report non-hyperbolic (Vol < 0.5 is a safe threshold for torus/satellite)
    is_hyperbolic = v_float > 0.5
    from hp_volume import hp_volume_of_manifold
    hp_str: str | None = (
        hp_volume_of_manifold(E, digits=digits) if is_hyperbolic else None
    )
    result = {
        "status": "ok",
        "components": len(L.link_components),
        "crossings": len(word),
        "volume_float": v_float,
        "volume_50digit": hp_str,
        "is_hyperbolic": is_hyperbolic,
    }
    return result


def derive_atom(Z: int, N: int, B_ame: float,
                 mixed_rule: str = MIXED_CROSSING_RULE,
                 interleave: str = BRAID_INTERLEAVE) -> dict:
    word, stats = atom_to_braid_word(Z, N, mixed_rule=mixed_rule,
                                         interleave=interleave)
    vol = volume_of_closure(word)
    record = {
        "atom": f"Z{Z}N{N}",
        "Z": Z, "N": N, "A": Z + N,
        "B_AME_MeV": B_ame,
        "braid_stats": stats,
        "braid_word_len": len(word),
        "volume": vol,
    }
    if vol.get("status") == "ok":
        v = vol["volume_float"]
        if v > 0:
            record["target_me_err_pct"] = (v - B_ame / M_E_MEV) / \
                (B_ame / M_E_MEV) * 100
            record["target_2me_err_pct"] = (v - B_ame / (2 * M_E_MEV)) / \
                (B_ame / (2 * M_E_MEV)) * 100
    return record


if __name__ == "__main__":
    print("=" * 100)
    print("Phase 3: Atom → Knot derivation via braid closure")
    print(f"  h = q - q⁻¹ = {H_VAL:.10f}  (from q_parameter.HA)")
    print(f"  Mixed-crossing rule: {MIXED_CROSSING_RULE!r}")
    print("=" * 100)

    results = []
    for interleave in ["block", "interleaved"]:
        print(f"\n{'#' * 100}")
        print(f"INTERLEAVE MODE: {interleave!r}")
        print(f"{'#' * 100}")
        for name, Z, N, B_ame in ATOMS:
            r = derive_atom(Z, N, B_ame, interleave=interleave)
            r["atom_label"] = name
            results.append(r)

            print(f"\n[{name}]  Z={Z}, N={N}, 3A={3*(Z+N)}  B_AME={B_ame:.4f} MeV")
            print(f"  braid factors: pos={r['braid_stats']['counts']['pos']}, "
                  f"neg={r['braid_stats']['counts']['neg']}, "
                  f"mixed={r['braid_stats']['counts']['mixed']}  "
                  f"(max σ-index {r['braid_stats']['max_generator']})")
            v = r["volume"]
            if v["status"] != "ok":
                print(f"  volume: {v['status']}  {v.get('error', '')}")
                continue
            hyp = "hyperbolic" if v["is_hyperbolic"] else "NON-hyperbolic"
            print(f"  closure: {v['components']} components, "
                  f"{v['crossings']} crossings — {hyp}")
            print(f"  Vol (float):      {v['volume_float']:.10f}")
            if v.get("volume_50digit"):
                print(f"  Vol (50-digit):   {v['volume_50digit']}")
            tgt_me = B_ame / M_E_MEV
            tgt_2me = B_ame / (2 * M_E_MEV)
            A = Z + N
            print(f"  target B/m_e   = {tgt_me:.6f}    "
                  f"err = {r.get('target_me_err_pct', float('nan')):+.3f}%")
            print(f"  target B/2m_e  = {tgt_2me:.6f}    "
                  f"err = {r.get('target_2me_err_pct', float('nan')):+.3f}%")
            print(f"  A·8G (Borromean) = {A * VOL_BORROMEAN:.6f}    "
                  f"err = {(v['volume_float'] - A*VOL_BORROMEAN)/(A*VOL_BORROMEAN)*100:+.3f}%")

    witness = {
        "computation": "atom-link-derivation",
        "description": (
            "Phase 3 prototype: derive an atom's knot/link class by "
            "closing its 3A-strand braid word (from atom_braid_word_3A). "
            "Each Hecke factor (c·T_g + d·1) is mapped back to a signed "
            "braid generator via the Hecke dictionary (T=σ, T⁻¹=σ⁻¹). "
            "Mixed proton-neutron crossings do NOT lift uniquely to a "
            "braid generator; the MIXED_CROSSING_RULE selects a lift. "
            "Exterior volume is computed via SnapPy (float + 50-digit "
            "verified via ManifoldHP)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "m_e_MeV": M_E_MEV,
            "h_value": H_VAL,
            "mixed_rule": MIXED_CROSSING_RULE,
        },
        "results": results,
    }
    out = Path(__file__).parent / "atom-link-derivation.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
