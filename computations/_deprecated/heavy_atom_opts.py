#!/usr/bin/env python3
"""
Heavy-atom optimization module (CORRECTED — no vacuum filter).

Implements user-selected optimizations:
  (2) Per-nucleon character cache
  (3) Skew-SYT precomputation
  (5) Confinement-level shortcut (non-magic uses H_A shorthand)
  (7) Magic-anchor cache (all magic and double-magic)

Plus hook for mixed-integer SDP (MISDP) on quadratic cross-term.

CORRECTION: earlier version applied a "vacuum filter" (drop χ_λ < 0
partitions). User feedback: this made |Δm/m|% worse (0.4-2.5% →
7-35%).  Reverted.  Markov trace is intrinsically SIGNED; both
positive and negative χ_λ contributions are physical and combine
to give the true trace.  Filtering biases the atom/free difference
asymmetrically.

Uses signed Markov trace throughout:
    tr_M(W) = Σ_λ w_λ(q) · χ_λ(W) / d_λ
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0 as qi, z_mark, HA as h,
    proton_cross, neutron_cross, Phi_q,
    mass_from_tower, additive_wedderburn_volumes,
)

CACHE_FILE = Path(__file__).parent / "heavy-atom-opts.witness.json"
MAGIC = {2, 8, 20, 28, 50, 82, 126}


def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {"computedAt": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q": q0},
            "opt2_nucleon_chars": {},
            "opt3_skew_syt": {},
            "opt5_shorthand_masses": {},
            "opt7_magic_anchors": {}}


def save_cache(cache):
    cache["computedAt"] = datetime.now(timezone.utc).isoformat()
    CACHE_FILE.write_text(json.dumps(cache, indent=2, default=str))


# ── OPT 2: Per-nucleon character cache ──────────────────────────────

def nucleon_h3_characters(crossings_per_gen):
    """(χ^sym, χ^std, χ^alt) for a nucleon K ∈ H_3(q)."""
    chi_sym = 1.0
    chi_alt = 1.0
    for gen in [0, 1]:
        for c, d in crossings_per_gen.get(gen, []):
            chi_sym *= c * q0 + d
            chi_alt *= -c * qi + d
    sigma_1 = np.array([[q0, 0.0], [0.0, -qi]])
    alpha = -1.0 / (q0 ** 3 + q0)
    gamma = q0 ** 3 / (q0 ** 2 + 1.0)
    off = math.sqrt(max(0.0, -1.0 - alpha * gamma))
    sigma_2 = np.array([[alpha, off], [off, gamma]])
    M = np.eye(2)
    for gen in [0, 1]:
        sig = sigma_1 if gen == 0 else sigma_2
        for c, d in crossings_per_gen.get(gen, []):
            op = c * sig + d * np.eye(2)
            M = M @ op
    return {'sym': float(chi_sym), 'std': float(np.trace(M)),
            'alt': float(chi_alt)}


def get_nucleon_chars(ntype, cache):
    if ntype in cache["opt2_nucleon_chars"]:
        return cache["opt2_nucleon_chars"][ntype]
    src = proton_cross if ntype == 'p' else neutron_cross
    chars = nucleon_h3_characters(src)
    cache["opt2_nucleon_chars"][ntype] = chars
    return chars


# ── OPT 3: Skew-SYT precomputation ──────────────────────────────────

def fits_inside(mu, lam):
    if len(mu) > len(lam):
        return False
    for i, m in enumerate(mu):
        if m > lam[i]:
            return False
    return True


@lru_cache(maxsize=8192)
def skew_syt_count(lam_tuple, mu_tuple):
    lam = list(lam_tuple)
    mu = list(mu_tuple)
    if not fits_inside(mu, lam):
        return 0
    n = sum(lam) - sum(mu)
    if n < 0:
        return 0
    L = len(lam)
    mu_p = list(mu) + [0] * (L - len(mu))
    M = [[0.0] * L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            kk = lam[i] - mu_p[j] - i + j
            if kk >= 0:
                M[i][j] = 1.0 / math.factorial(kk)
    det = float(np.linalg.det(np.array(M)))
    return int(round(math.factorial(n) * det))


def partitions_of(n):
    if n == 0:
        return [()]
    out = []
    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, cur + [p])
    rec(n, n, [])
    return out


def precompute_skew_syt(k_max, cache):
    H3 = [(3,), (2, 1), (1, 1, 1)]
    key = f"k_max_{k_max}"
    if key in cache["opt3_skew_syt"]:
        return cache["opt3_skew_syt"][key]
    for k in range(3, k_max + 1):
        for lam in partitions_of(k):
            for mu in H3:
                skew_syt_count(tuple(lam), tuple(mu))
    cache["opt3_skew_syt"][key] = {
        "cached_entries": skew_syt_count.cache_info().currsize
    }
    return cache["opt3_skew_syt"][key]


# ── OPT 5: Confinement-level shortcut ──────────────────────────────

def nucleon_shorthand_mass(Z, N, cache):
    key = f"{Z}-{N}"
    if key in cache["opt5_shorthand_masses"]:
        return cache["opt5_shorthand_masses"][key]
    p_vols = additive_wedderburn_volumes(3, proton_cross)
    n_vols = additive_wedderburn_volumes(3, neutron_cross)
    _, _, _, m_p = mass_from_tower(p_vols)
    _, _, _, m_n = mass_from_tower(n_vols)
    m_free = Z * m_p + N * m_n
    A = Z + N
    z_sq = z_mark ** 2
    V_nuc = (m_p * m_n) ** 0.5 / max(m_p, m_n)
    pair_contrib = ((A - 1) * z_sq * Phi_q(abs(V_nuc))
                    if abs(V_nuc) < q0 else 0.0)
    m_atom = m_free + pair_contrib
    result = {"m_free": m_free, "m_atom": m_atom,
              "pair_contrib": pair_contrib,
              "n_nucleon_strands": A,  # opt 5: H_A not H_{3A}
              "n_quark_strands_skipped": 3 * A - A}
    cache["opt5_shorthand_masses"][key] = result
    return result


# ── OPT 7: Magic-anchor cache (all magic and double-magic) ─────────

def is_single_magic(Z, N):
    return (Z in MAGIC) ^ (N in MAGIC)


def is_double_magic(Z, N):
    return (Z in MAGIC) and (N in MAGIC)


def magic_type(Z, N):
    if is_double_magic(Z, N):
        return "double"
    elif Z in MAGIC:
        return "Z-magic"
    elif N in MAGIC:
        return "N-magic"
    else:
        return "non-magic"


def compute_magic_anchor(Z, N, cache):
    """Exact signed Markov trace for magic configurations.

    Uses COMMON max_ln rescaling between atom and free so that the
    ratio atom/free is meaningful.
    """
    key = f"{Z}-{N}"
    if key in cache["opt7_magic_anchors"]:
        return cache["opt7_magic_anchors"][key]
    mtype = magic_type(Z, N)
    if mtype == "non-magic":
        return None
    try:
        from hecke_core import atom_character_raw, _PARTITION_TABLE
        A = Z + N
        k_cap = min(6, 3 * A)
        active = [e for e in _PARTITION_TABLE
                  if e.get('has_ysn', False) and e.get('k', 0) <= k_cap]
        # Compute both atom and free with common max_ln scaling
        atom_data = []
        free_data = []
        for entry in active:
            a_chi, a_ln, dim = atom_character_raw(Z, N, entry, include_inter=True)
            f_chi, f_ln, _ = atom_character_raw(Z, N, entry, include_inter=False)
            atom_data.append({
                'partition': entry['partition'], 'chi': a_chi, 'ln': a_ln,
                'dim': dim, 'weight': entry.get('wedderburn_weight', 0),
            })
            free_data.append({
                'partition': entry['partition'], 'chi': f_chi, 'ln': f_ln,
                'dim': dim, 'weight': entry.get('wedderburn_weight', 0),
            })
        # Common max_ln for meaningful ratio
        common_max_ln = max(
            max((d['ln'] for d in atom_data), default=0),
            max((d['ln'] for d in free_data), default=0),
        )
        atom_total = 0.0
        free_total = 0.0
        for pd in atom_data:
            chi_rescaled = pd['chi'] * math.exp(pd['ln'] - common_max_ln)
            atom_total += pd['weight'] * chi_rescaled / pd['dim']
        for fd in free_data:
            chi_rescaled = fd['chi'] * math.exp(fd['ln'] - common_max_ln)
            free_total += fd['weight'] * chi_rescaled / fd['dim']
        result = {
            "Z": Z, "N": N, "A": A,
            "magic_type": mtype,
            "atom_trM_signed": atom_total,
            "free_trM_signed": free_total,
            "common_max_ln": common_max_ln,
            "k_cap_used": k_cap,
            "n_partitions": len(active),
        }
        cache["opt7_magic_anchors"][key] = result
        return result
    except Exception as e:
        return {"Z": Z, "N": N, "error": str(e)}


MISDP_NOTES = """
Quadratic cross-term requires MISDP (mixed-integer SDP):

   Σ_{|i-j|=1} z² · Φ_q(|V̂_i V̂_j|)

Approach:
  1. Continuous SDP relaxation (cvxpy / sdp_cross_channel.py) on V̂_i ∈ R^+.
  2. Round to integer grid.
  3. Branch-and-cut with continuous SDP as relaxation at each node.
  4. Pick minimum |tr_M| feasible integer point.

The continuous SDP in sdp_cross_channel.py has 2×2 PSD blocks per
adjacent pair — this is the relaxation.  Integer extension via B&C.
"""


def warm_all_caches(atoms):
    cache = load_cache()
    get_nucleon_chars('p', cache)
    get_nucleon_chars('n', cache)
    precompute_skew_syt(k_max=6, cache=cache)
    for atom, Z, N in atoms:
        nucleon_shorthand_mass(Z, N, cache)
    for atom, Z, N in atoms:
        if magic_type(Z, N) != "non-magic":
            compute_magic_anchor(Z, N, cache)
    save_cache(cache)
    return cache


if __name__ == "__main__":
    print("HEAVY-ATOM OPTIMIZATIONS 2,3,5,7 (NO VACUUM FILTER)")
    print("=" * 84)
    print(f"Cache file: {CACHE_FILE}")
    print(f"q₀ = {q0}")
    print()

    ATOMS = [
        ("D",    1,  1),    # single magic (N=1, not in MAGIC actually)
        ("T",    1,  2),    # N=2 magic
        ("3He",  2,  1),    # Z=2 magic
        ("4He",  2,  2),    # double magic
        ("6Li",  3,  3),    # non-magic
        ("12C",  6,  6),    # non-magic
        ("14C",  6,  8),    # N=8 magic
        ("16O",  8,  8),    # double magic
        ("20Ne", 10, 10),   # non-magic
        ("40Ca", 20, 20),   # double magic
    ]

    cache = warm_all_caches(ATOMS)

    # Opt 2 summary
    print("OPT 2: per-nucleon characters")
    for ntype in ['p', 'n']:
        c = cache["opt2_nucleon_chars"][ntype]
        print(f"  {ntype}: sym={c['sym']:+.4f}, std={c['std']:+.4f}, "
              f"alt={c['alt']:+.4f}")
    print()

    # Opt 3 summary
    print("OPT 3: skew-SYT cache")
    for key, val in cache["opt3_skew_syt"].items():
        print(f"  {key}: {val['cached_entries']} entries")
    print()

    # Opt 5 summary
    print("OPT 5: nucleon-shorthand (H_A vs H_{3A}, non-magic shortcut)")
    print(f"  {'Atom':>6} {'A':>3} {'magic':>10} {'m_free':>12} "
          f"{'m_atom':>12} {'strands saved':>14}")
    for atom, Z, N in ATOMS:
        key = f"{Z}-{N}"
        if key in cache["opt5_shorthand_masses"]:
            d = cache["opt5_shorthand_masses"][key]
            mt = magic_type(Z, N)
            print(f"  {atom:>6} {Z+N:>3d} {mt:>10} "
                  f"{d['m_free']:>12.4e} {d['m_atom']:>12.4e} "
                  f"{d['n_quark_strands_skipped']:>14d}")
    print()

    # Opt 7 summary — SIGNED tr_M
    print("OPT 7: magic-anchor signed Markov traces (NO filter)")
    print(f"  {'Atom':>6} {'A':>3} {'type':>12} {'n_part':>7} "
          f"{'atom_tr_M':>14} {'free_tr_M':>14}")
    for atom, Z, N in ATOMS:
        key = f"{Z}-{N}"
        if key in cache["opt7_magic_anchors"]:
            d = cache["opt7_magic_anchors"][key]
            if "error" in d:
                print(f"  {atom:>6} {Z+N:>3d}  ERROR: {d['error']}")
            else:
                print(f"  {atom:>6} {Z+N:>3d} {d['magic_type']:>12} "
                      f"{d['n_partitions']:>7d} "
                      f"{d['atom_trM_signed']:>14.4e} "
                      f"{d['free_trM_signed']:>14.4e}")
    print()
    print("MISDP NOTE:")
    print(MISDP_NOTES)
