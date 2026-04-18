#!/usr/bin/env python3
"""
Non-perturbative exceptional-divisor tower via SnapPy hyperbolic volume.

Per prop:categorical-mass-markov §Scope line 112:
  "the full tower sum... evaluates to Vol(K)/ℏ_q² in the archimedean
   realisation"

and the identity Vol(4_1)/ℏ_q² = m_μ/m_e = 206.77 confirming ℏ_q² is
the natural mass-ratio normalization.

This module computes the mass tower contribution **non-perturbatively**
as Vol(atom braid closure) / ℏ_q², bypassing the asymptotic ℏ_q-Taylor
expansion that diverges for heavier atoms.

Mixed-crossing resolution:
  Atom braids contain "mixed" (c=1, d=-h/2) crossings = ½(σ + σ⁻¹).
  These aren't single topological braid moves.  Each mixed crossing
  has TWO resolutions: σ (positive) and σ⁻¹ (negative).  For a
  braid word with M mixed crossings, we enumerate all 2^M resolutions
  and average their hyperbolic volumes weighted 1/2^M.

Caveats:
  • Some resolutions give non-hyperbolic links (torus, satellite) —
    SnapPy returns ~0 volume in those cases.
  • For small atoms M can be large (D has 5 mixed crossings → 32
    resolutions; T has 7 → 128).  Scales as 2^M — feasible for
    A ≤ 4 atoms with intra+inter = ~5-10 mixed crossings.
  • Trace closure vs plat closure: we use standard braid closure
    (trace closure of the braid group on 3A strands).
"""
from __future__ import annotations

import sys
import math
from pathlib import Path
from functools import lru_cache

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, HA as HA_VAL
from mass_at_3A_proper import atom_braid_word_3A

H0 = HA_VAL  # h at q₀
HBAR_Q = (Q0 - 1.0) / Q0  # ℏ_q
HBAR_Q_SQ = HBAR_Q * HBAR_Q


def atom_braid_to_pure(Z: int, N: int, *, include_inter: bool = True,
                         m_pp: int = 1, m_pn: int = 1, m_nn: int = 1
                         ) -> tuple[list, list[int]]:
    """Convert atom Hecke word to a pure-braid skeleton + list of mixed
    crossing positions.

    Returns (braid_template, mixed_positions) where:
      braid_template: list of elements, each either
        + int  (positive generator σ_i → 1-based index i+1 for SnapPy)
        − int  (negative generator σ_i⁻¹ → -(i+1))
        ("mixed", i+1)  (mixed crossing at gen i, pending resolution)
        None  (identity, skip in closure)
      mixed_positions: list of indices into braid_template where mixed
        crossings appear.
    """
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    braid = []
    mixed = []
    for (c, d, g) in word:
        gen_1based = g + 1
        if abs(c) < 1e-12 and abs(d - 1.0) < 1e-12:
            # identity — skip
            continue
        if abs(c - 1.0) < 1e-12 and abs(d) < 1e-12:
            braid.append(gen_1based)        # σ
        elif abs(c - 1.0) < 1e-12 and abs(d + H0) < 1e-6:
            braid.append(-gen_1based)       # σ⁻¹
        elif abs(c - 1.0) < 1e-12 and abs(d + H0 / 2) < 1e-6:
            idx = len(braid)
            braid.append(("mixed", gen_1based))
            mixed.append(idx)
        else:
            raise ValueError(f"unknown (c, d) = ({c}, {d})")
    return braid, mixed


def resolve_braid(braid_template: list, mixed_positions: list[int],
                    resolution_bits: int) -> list[int]:
    """Given 2^M-bit selector, produce a concrete braid word.

    Each bit 0 → σ (positive), 1 → σ⁻¹ (negative) at that mixed
    crossing.
    """
    out = []
    for idx, elem in enumerate(braid_template):
        if idx in mixed_positions:
            bit_idx = mixed_positions.index(idx)
            bit = (resolution_bits >> bit_idx) & 1
            sign = +1 if bit == 0 else -1
            out.append(sign * elem[1])
        else:
            out.append(elem)
    return out


@lru_cache(maxsize=1024)
def _cached_volume(braid_tuple: tuple) -> float:
    """Hyperbolic volume of braid closure, cached.  Returns 0 on
    non-hyperbolic (degenerate numerical signal, typically < 1e-3).
    """
    import snappy
    try:
        L = snappy.Link(braid_closure=list(braid_tuple))
        if len(L.link_components) == 0:
            return 0.0
        M = L.exterior()
        # Try a few tetrahedralizations to get hyperbolic one
        vol = M.volume()
        # SnapPy can return float or a complex interval; coerce
        vol_f = float(vol) if hasattr(vol, "__float__") else 0.0
        # Clamp tiny numerical noise to 0 (non-hyperbolic signature)
        if abs(vol_f) < 1e-3:
            return 0.0
        return vol_f
    except Exception:
        return 0.0


def average_volume(Z: int, N: int, *, include_inter: bool = True,
                    m_pp: int = 1, m_pn: int = 1, m_nn: int = 1,
                    max_resolutions: int = 1024) -> dict:
    """Average hyperbolic volume over 2^M mixed-crossing resolutions.

    Returns dict with avg_volume, n_resolutions, n_hyperbolic,
    per_resolution volumes.
    """
    braid, mixed = atom_braid_to_pure(Z, N,
                                         include_inter=include_inter,
                                         m_pp=m_pp, m_pn=m_pn,
                                         m_nn=m_nn)
    M_count = len(mixed)
    if 2 ** M_count > max_resolutions:
        # Sample instead of enumerate all
        import random
        random.seed(42)
        sample = [random.randint(0, 2 ** M_count - 1)
                   for _ in range(max_resolutions)]
    else:
        sample = list(range(2 ** M_count))
    vols = []
    n_hyp = 0
    for bits in sample:
        word = resolve_braid(braid, mixed, bits)
        if not word:
            vols.append(0.0)
            continue
        v = _cached_volume(tuple(word))
        vols.append(v)
        if v > 0:
            n_hyp += 1
    avg_vol = sum(vols) / len(vols) if vols else 0.0
    return {
        "Z": Z, "N": N, "A": Z + N,
        "include_inter": include_inter,
        "M_mixed": M_count,
        "n_resolutions": len(sample),
        "n_hyperbolic": n_hyp,
        "avg_volume": avg_vol,
        "max_volume": max(vols) if vols else 0.0,
        "min_nonzero_volume": min((v for v in vols if v > 0), default=0.0),
    }


def binding_snappy(Z: int, N: int, *, E_0: float = 0.782,
                     include_canonical: bool = True,
                     max_resolutions: int = 1024) -> dict:
    """Binding via SnapPy hyperbolic-volume non-perturbative tower.

    B = E_0 · [(|tr_M(W_free)| - |tr_M(W_atom)|)
              + (Vol(K_free) - Vol(K_atom)) / ℏ_q²]

    include_canonical=False: tower-only contribution (Vol/ℏ_q²).
    """
    import time
    result = {"Z": Z, "N": N, "A": Z + N, "E_0_MeV": E_0,
               "include_canonical": include_canonical}

    # Canonical term (fast via Ocneanu)
    canonical_MeV = 0.0
    if include_canonical:
        from ocneanu_weights import tr_M_via_ocneanu_word
        t0 = time.time()
        tr_a = tr_M_via_ocneanu_word(Z, N, include_inter=True)
        tr_f = tr_M_via_ocneanu_word(Z, N, include_inter=False)
        canonical_MeV = E_0 * (abs(tr_f) - abs(tr_a))
        result["tr_M_atom"] = abs(tr_a)
        result["tr_M_free"] = abs(tr_f)
        result["canonical_MeV"] = canonical_MeV
        result["canonical_time_sec"] = time.time() - t0

    # Tower term: Vol / ℏ_q²
    t0 = time.time()
    vol_a = average_volume(Z, N, include_inter=True,
                             max_resolutions=max_resolutions)
    vol_f = average_volume(Z, N, include_inter=False,
                             max_resolutions=max_resolutions)
    delta_vol = vol_f["avg_volume"] - vol_a["avg_volume"]
    tower_MeV = E_0 * delta_vol / HBAR_Q_SQ
    result["vol_atom"] = vol_a
    result["vol_free"] = vol_f
    result["delta_vol"] = delta_vol
    result["tower_MeV"] = tower_MeV
    result["tower_time_sec"] = time.time() - t0

    B = canonical_MeV + tower_MeV
    result["B_MeV"] = B
    return result


if __name__ == "__main__":
    import time
    import json
    from datetime import datetime, timezone
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
    ]
    print("=" * 110)
    print("SNAPPY NON-PERTURBATIVE TOWER: Vol(K)/ℏ_q² + canonical tr_M")
    print(f"q₀ = {Q0}, ℏ_q² = {HBAR_Q_SQ:.6f}, E_0 = 0.782 MeV")
    print("=" * 110)
    print(f"\n  {'Atom':>4} {'A':>3} {'M_mix':>6} {'Vol(atom)':>10} "
          f"{'Vol(free)':>10} {'ΔVol':>9} {'B_canon':>10} {'B_tower':>12} "
          f"{'B_total':>10} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 110)
    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        try:
            t0 = time.time()
            r = binding_snappy(Z, N, max_resolutions=128)
            dt = time.time() - t0
            dm = (abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
                   if math.isfinite(r["B_MeV"]) else float("nan"))
            print(f"  {name:>4} {A:>3} {r['vol_atom']['M_mixed']:>6} "
                  f"{r['vol_atom']['avg_volume']:>10.4f} "
                  f"{r['vol_free']['avg_volume']:>10.4f} "
                  f"{r['delta_vol']:>+9.4f} "
                  f"{r['canonical_MeV']:>+10.4f} "
                  f"{r['tower_MeV']:>+12.4f} "
                  f"{r['B_MeV']:>+10.4f} "
                  f"{dm:>8.4f}% "
                  f"{dt:>7.1f}s")
            results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                             "delta_m_over_m_pct": dm,
                             "time_sec": dt})
        except Exception as e:
            print(f"  {name:>4} ERR {type(e).__name__}: {str(e)[:60]}")

    witness = {
        "computation": "snappy-tower",
        "description": (
            "Non-perturbative mass tower: Vol(atom braid closure)/ℏ_q² "
            "via SnapPy hyperbolic volume, averaged over 2^M "
            "resolutions of mixed Hecke crossings (pn pairs = "
            "½(σ+σ⁻¹)).  Direct implementation of prop:categorical-"
            "mass-markov scope note ('full tower evaluates to "
            "Vol(K)/ℏ_q² in archimedean realisation').  Bypasses the "
            "ℏ_q-Taylor expansion (asymptotic for n ≥ 9).  Combined "
            "with canonical Ocneanu tr_M for single-brane defect."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "hbar_q_sq": HBAR_Q_SQ,
                        "E_0_MeV": 0.782},
        "results": results,
    }
    out = Path(__file__).parent / "snappy-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
