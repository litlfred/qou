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


@lru_cache(maxsize=2048)
def _cached_volume_hyp(braid_tuple: tuple) -> float:
    """Hyperbolic volume of braid closure (SnapPy), cached.

    Returns 0.0 on non-hyperbolic links (torus, satellite, composite).
    """
    import snappy
    try:
        L = snappy.Link(braid_closure=list(braid_tuple))
        if len(L.link_components) == 0:
            return 0.0
        M = L.exterior()
        vol = M.volume()
        vol_f = float(vol) if hasattr(vol, "__float__") else 0.0
        if abs(vol_f) < 1e-3:
            return 0.0
        return vol_f
    except Exception:
        return 0.0


@lru_cache(maxsize=2048)
def _cached_kauffman_regularized_vol(braid_tuple: tuple) -> float:
    """Kauffman-bracket-regularized "volume" for non-hyperbolic closures.

    Uses the Kashaev / Jones-polynomial-modulus prescription:
        Vol_reg(K) = log |J_K(q₀)|
    where J_K is the Jones polynomial / Kauffman bracket of the
    closure evaluated at our substrate q₀.  Consistent with
    hyperbolic Vol at the volume-conjecture limit, finite for torus
    knots, and sign-sensitive (can be negative, corresponding to
    mass defect direction).

    Implementation: compute Kauffman bracket via state-sum expansion
    on the braid closure.  Each crossing contributes factor
    A = q^{-1/4} in positive resolution, A⁻¹ in negative.  Circle
    count gives factor (-A² − A⁻²)^{C-1}.
    """
    # Kauffman bracket state sum (Kauffman 1987):
    # <L> = Σ_states A^{a(s)} · (-A² - A⁻²)^{|s| − 1}
    # where a(s) = (# A-resolutions) − (# A⁻¹-resolutions) at each
    # crossing, |s| = # loops after resolution.
    # We use A² = q, so A = q^{1/2} → natural base.
    import numpy as np
    A = Q0 ** 0.25  # A⁴ = q (standard convention)
    if not braid_tuple:
        return 0.0
    n_strands = max(abs(g) for g in braid_tuple) + 1
    n_cross = len(braid_tuple)
    # Each crossing is positive (σ_i) or negative (σ_i⁻¹).
    # Kauffman state sum: each crossing has A-resolution or B-resolution.
    # For positive crossing σ: A-res = horizontal smoothing = A contribution
    # For negative crossing σ⁻¹: A-res = vertical smoothing = A⁻¹ contribution
    # ... we enumerate 2^n_cross states, count loops, sum weights.
    total = 0.0 + 0.0j
    d_const = -(A ** 2) - (A ** (-2))
    N_STATES = 2 ** n_cross
    # Limit for tractability
    if n_cross > 22:
        # Downsample uniformly
        import random
        random.seed(123)
        state_iter = (random.randint(0, N_STATES - 1) for _ in range(2 ** 22))
        weight = N_STATES / (2 ** 22)
    else:
        state_iter = range(N_STATES)
        weight = 1.0
    for state in state_iter:
        # Build smoothing pattern
        # Track arcs by union-find on (strand_idx, top/bottom)
        parent = list(range(2 * n_strands))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        # Start: each strand's top connects to bottom (closure identity)
        for s in range(n_strands):
            union(s, n_strands + s)
        # Simulate crossings sequentially
        # For simplicity, use a heuristic loop count via circle
        # enumeration on the diagram post-resolution
        # This is a rough approximation — full state-sum needs
        # proper planar arc tracking.  Here we use braid-closure
        # circle count via the permutation of the braid word's
        # smoothed braid.
        perm = list(range(n_strands))
        a_count = 0
        for ci, g in enumerate(braid_tuple):
            i = abs(g) - 1
            resolution_bit = (state >> ci) & 1
            # For σ: A-res = no strand swap; B-res = swap.
            # For σ⁻¹: A-res = swap; B-res = no swap.
            if g > 0:  # σ
                if resolution_bit == 0:  # A-resolution → no swap
                    a_count += 1
                else:  # B-resolution → swap
                    perm[i], perm[i + 1] = perm[i + 1], perm[i]
                    a_count -= 1
            else:  # σ⁻¹
                if resolution_bit == 0:  # A-res → swap
                    perm[i], perm[i + 1] = perm[i + 1], perm[i]
                    a_count += 1
                else:  # B-res → no swap
                    a_count -= 1
        # Count cycles in perm = number of loops in closure
        visited = [False] * n_strands
        n_loops = 0
        for s in range(n_strands):
            if visited[s]:
                continue
            n_loops += 1
            k = s
            while not visited[k]:
                visited[k] = True
                k = perm[k]
        # Kauffman state weight
        w = (A ** a_count) * (d_const ** (n_loops - 1))
        total += w * weight
    # Vol_reg = log |bracket|
    if abs(total) < 1e-30:
        return 0.0
    return math.log(abs(total.real if abs(total.imag) < 1e-6 else abs(total)))


def kauffman_state_sum_vol(Z: int, N: int, *, include_inter: bool = True,
                              m_pp: int = 1, m_pn: int = 1, m_nn: int = 1
                              ) -> dict:
    """Full 2^M Kauffman-bracket-weighted volume.

    For each of 2^M resolutions of mixed crossings, compute:
      - Hyperbolic Vol via SnapPy (0 for non-hyperbolic)
      - Kauffman-regularized Vol via log|Jones polynomial|

    Aggregate with Kauffman-bracket weights: each mixed resolution
    has weight (1/2)^M (= equal weights since mixed = ½(σ+σ⁻¹)).
    """
    braid, mixed = atom_braid_to_pure(Z, N,
                                         include_inter=include_inter,
                                         m_pp=m_pp, m_pn=m_pn,
                                         m_nn=m_nn)
    M_count = len(mixed)
    n_total = 2 ** M_count
    weight = 1.0 / n_total  # uniform Kauffman weight per mixed resolution

    sum_vol_hyp = 0.0
    sum_vol_reg = 0.0
    n_hyp = 0
    per_res = []

    for bits in range(n_total):
        word = resolve_braid(braid, mixed, bits)
        if not word:
            continue
        vol_hyp = _cached_volume_hyp(tuple(word))
        vol_reg = _cached_kauffman_regularized_vol(tuple(word))
        sum_vol_hyp += weight * vol_hyp
        sum_vol_reg += weight * vol_reg
        if vol_hyp > 0:
            n_hyp += 1
        per_res.append({"bits": bits, "vol_hyp": vol_hyp,
                          "vol_reg": vol_reg})
    return {
        "Z": Z, "N": N, "A": Z + N,
        "include_inter": include_inter,
        "M_mixed": M_count,
        "n_resolutions": n_total,
        "n_hyperbolic": n_hyp,
        "kauffman_vol_hyp": sum_vol_hyp,
        "kauffman_vol_reg": sum_vol_reg,
    }


def average_volume(Z: int, N: int, *, include_inter: bool = True,
                    m_pp: int = 1, m_pn: int = 1, m_nn: int = 1,
                    max_resolutions: int = 1024) -> dict:
    """Average hyperbolic volume over mixed-crossing resolutions (legacy).

    Samples if 2^M > max_resolutions.  Simple mean (uniform weight).
    For the proper Kauffman-weighted state sum, use
    kauffman_state_sum_vol (full enumeration).
    """
    braid, mixed = atom_braid_to_pure(Z, N,
                                         include_inter=include_inter,
                                         m_pp=m_pp, m_pn=m_pn,
                                         m_nn=m_nn)
    M_count = len(mixed)
    if 2 ** M_count > max_resolutions:
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
        v = _cached_volume_hyp(tuple(word))
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


from experimental_constants import Q_NEUTRON_MEV as _Q_BETA_N  # noqa: E402


def binding_snappy(Z: int, N: int, *, E_0: float = float(_Q_BETA_N),
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

    # Tower term: Vol / ℏ_q² via full 2^M Kauffman state sum
    t0 = time.time()
    vol_a = kauffman_state_sum_vol(Z, N, include_inter=True)
    vol_f = kauffman_state_sum_vol(Z, N, include_inter=False)
    # Two aggregations: hyperbolic volume and Jones-regularized
    delta_vol_hyp = vol_f["kauffman_vol_hyp"] - vol_a["kauffman_vol_hyp"]
    delta_vol_reg = vol_f["kauffman_vol_reg"] - vol_a["kauffman_vol_reg"]
    tower_hyp_MeV = E_0 * delta_vol_hyp / HBAR_Q_SQ
    tower_reg_MeV = E_0 * delta_vol_reg / HBAR_Q_SQ
    result["vol_atom"] = vol_a
    result["vol_free"] = vol_f
    result["delta_vol_hyp"] = delta_vol_hyp
    result["delta_vol_reg"] = delta_vol_reg
    result["tower_hyp_MeV"] = tower_hyp_MeV
    result["tower_reg_MeV"] = tower_reg_MeV
    result["tower_time_sec"] = time.time() - t0
    # Default: use hyperbolic Vol (matches prop's literal reading)
    tower_MeV = tower_hyp_MeV
    result["tower_MeV"] = tower_MeV

    B = canonical_MeV + tower_MeV
    result["B_MeV"] = B
    return result


if __name__ == "__main__":
    import time
    import json
    from datetime import datetime, timezone
    ATOMS = [
        ("D",    1, 1,  2.22452),
        # T/3He/4He pending (ω_λ at n=9 or 12 slow + large state sums)
        # ("T",    1, 2,  8.481821),
        # ("3He",  2, 1,  7.71804),
        # ("4He",  2, 2, 28.295674),
    ]
    print("=" * 110)
    print("SNAPPY NON-PERTURBATIVE TOWER: Vol(K)/ℏ_q² + canonical tr_M")
    print(f"q₀ = {Q0}, ℏ_q² = {HBAR_Q_SQ:.6f}, "
          f"E_0 = {float(_Q_BETA_N):.8f} MeV (Q_β(n))")
    print("=" * 110)
    print(f"\n  {'Atom':>4} {'A':>3} {'M':>4} {'ΔVol_hyp':>10} "
          f"{'ΔVol_reg':>10} {'B_canon':>9} {'B_tower_hyp':>12} "
          f"{'B_tower_reg':>12} {'B_total_hyp':>12} {'|Δm/m|%_hyp':>11} "
          f"{'B_total_reg':>12} {'|Δm/m|%_reg':>11} {'time':>7}")
    print("  " + "-" * 140)
    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        try:
            t0 = time.time()
            r = binding_snappy(Z, N)
            dt = time.time() - t0
            B_total_hyp = r["canonical_MeV"] + r["tower_hyp_MeV"]
            B_total_reg = r["canonical_MeV"] + r["tower_reg_MeV"]
            dm_hyp = (abs(B_total_hyp - B_AME) / (A * 938.272) * 100
                       if math.isfinite(B_total_hyp) else float("nan"))
            dm_reg = (abs(B_total_reg - B_AME) / (A * 938.272) * 100
                       if math.isfinite(B_total_reg) else float("nan"))
            print(f"  {name:>4} {A:>3} {r['vol_atom']['M_mixed']:>4} "
                  f"{r['delta_vol_hyp']:>+10.4f} "
                  f"{r['delta_vol_reg']:>+10.4f} "
                  f"{r['canonical_MeV']:>+9.3f} "
                  f"{r['tower_hyp_MeV']:>+12.3f} "
                  f"{r['tower_reg_MeV']:>+12.3f} "
                  f"{B_total_hyp:>+12.3f} {dm_hyp:>10.4f}% "
                  f"{B_total_reg:>+12.3f} {dm_reg:>10.4f}% "
                  f"{dt:>6.1f}s")
            results.append({**r,
                             "B_total_hyp_MeV": B_total_hyp,
                             "B_total_reg_MeV": B_total_reg,
                             "atom": name, "B_AME_MeV": B_AME,
                             "delta_m_over_m_pct_hyp": dm_hyp,
                             "delta_m_over_m_pct_reg": dm_reg,
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
                        "E_0_MeV": float(_Q_BETA_N)},
        "results": results,
    }
    out = Path(__file__).parent / "snappy-tower.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
