#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Ocneanu / Jones–Markov weights ω_λ(q, z) for Iwahori–Hecke H_n(q).

Symmetric convention:
    σ² = (q − q⁻¹)σ + 1     (eigenvalues  q, −q⁻¹)
    z = 1 / (q^{1/2} + q^{−1/2})   (Markov parameter)

The canonical Jones–Markov trace on H_n(q) decomposes over irreps as

    tr_M(x)  =  Σ_{λ ⊢ n}  (ω_λ(q, z) / d_λ)  ·  χ_λ(x)

where d_λ is the classical symmetric-group dimension.  The weights
ω_λ satisfy:

    (W1)  Σ_{λ ⊢ n}  ω_λ = 1                      (tr_M(1) = 1)
    (W2)  Σ_{λ ⊢ n}  (ω_λ / d_λ) · χ_λ(T_i) = z  (tr_M(T_i) = z)
    (W3)  tr_M(xT_n) = z · tr_M(x) for x ∈ H_n    (Markov II)
    (W4)  consistency across n: ω_{λ} at level n must restrict
          to ω_{λ'} at level n−1 under branching.

DERIVATION (symmetric convention, rational in q and z):

At H_2 with partitions {(2), (1,1)}:
  χ_(2)(T_0) = q,   χ_(1,1)(T_0) = −q⁻¹,   d_(2) = d_(1,1) = 1.

Solve (W1), (W2):
  ω_(2) + ω_(1,1) = 1
  ω_(2) · q − ω_(1,1) · q⁻¹ = z

⇒  ω_(2) = (z + q⁻¹) / (q + q⁻¹) = (z + q⁻¹) / [2]_q
   ω_(1,1) = (q − z) / (q + q⁻¹) = (q − z) / [2]_q

Consistency check at q = 1:  ω_(2) = ω_(1,1) = 1/2 (if z = 0; Plancherel).
At our q₀, z: both are definite positive numbers summing to 1.

GENERAL FORMULA (Wenzl 1988, adapted to symmetric convention):

  ω_λ(q, z) = Π_{(i,j) ∈ λ}  (z · q^{j−i} − q^{−(j−i)}) / (q^{h(i,j)} − q^{−h(i,j)})

where:
  (i, j) ∈ λ runs over cells,
  j − i is the content of the cell,
  h(i, j) is the hook length.

(At q = 1: reduces to d_λ²/n! = Plancherel, since each
 numerator → z and denominator → 2 h.)

This module provides the formula and verification harness matching
the prop:categorical-mass-markov explicit values table.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import math
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from partition_utils import hook_lengths_with_cells as hook_lengths  # noqa: E402


# Symbolic q and z for derivation
q = sp.Symbol('q', positive=True)
z = sp.Symbol('z', positive=True)
z_num = Q0**3 / (Q0**2 + 1)
z_sym = q**3 / (q**2 + 1)


def omega_lambda_formula_guess(shape: tuple[int, ...], *,
                                 q_val: float = None, z_val: float = None):
    """FAILED GUESS: hook-content formula Π(z q^c − q^{−c})/(q^h − q^{−h}).

    Does NOT satisfy Σ ω = 1 at q ≠ 1.  Retained for reference; see
    omega_lambda_via_inversion below for the correct approach.
    """
    if q_val is None:
        q_val = Q0
    if z_val is None:
        z_val = z_num
    num = 1.0
    den = 1.0
    for (i, j, h) in hook_lengths(shape):
        c = j - i
        num *= z_val * q_val ** c - q_val ** (-c)
        den *= q_val ** h - q_val ** (-h)
    return num / den


# ── Derivation by inversion of the Markov-axiom linear system ──
#
# For each n, enumerate p(n) reduced words in S_n (basis of H_n).
# Compute tr_M(T_w) via the canonical path (markov_trace_canonical.
# tr_M_element) and χ_λ(T_w) per partition λ.  Solve:
#
#    Σ_λ (ω_λ / d_λ) · χ_λ(T_w_k)  =  tr_M(T_w_k)    (k = 1…p(n))
#
# This is a p(n) × p(n) linear system with unique solution ω_λ.
# Works at ANY convention — no need to guess the formula.

_OMEGA_CACHE: dict[int, dict[tuple, float]] = {}
_OMEGA_DISK_DIR = Path(__file__).parent / ".cache" / "ocneanu"


def _load_omega_disk(n: int, q_val: float) -> dict | None:
    """Legacy v1 disk loader.  Deprecated — use _load_omega_disk_v2.

    Key format: comma-separated integer partition string → float.
    Returns dict keyed by tuple[int, ...] → float matching the
    in-memory _OMEGA_CACHE signature.
    """
    _OMEGA_DISK_DIR.mkdir(parents=True, exist_ok=True)
    f = _OMEGA_DISK_DIR / f"n{n}_q{q_val:.10f}.json"
    if not f.exists():
        return None
    try:
        import json as _json
        raw = _json.loads(f.read_text())
        out = {}
        for k, v in raw.items():
            if not k:
                out[()] = float(v)
            else:
                out[tuple(int(x) for x in k.split(","))] = float(v)
        return out
    except Exception:
        return None


def _save_omega_disk(n: int, q_val: float, omegas: dict):
    import json as _json
    _OMEGA_DISK_DIR.mkdir(parents=True, exist_ok=True)
    f = _OMEGA_DISK_DIR / f"n{n}_q{q_val:.10f}.json"
    payload = {",".join(str(x) for x in shape) if shape else "":
                v for shape, v in omegas.items()}
    try:
        f.write_text(_json.dumps(payload))
    except Exception:
        pass


def _load_omega_disk_v2(n: int, q_val: float):
    """Simpler json dump: keys are shape tuples stringified."""
    _OMEGA_DISK_DIR.mkdir(parents=True, exist_ok=True)
    f = _OMEGA_DISK_DIR / f"n{n}_q{q_val:.10f}_v2.json"
    if not f.exists():
        return None
    try:
        import json as _json
        raw = _json.loads(f.read_text())
        out = {}
        for key_str, v in raw.items():
            if not key_str:
                out[()] = v
            else:
                parts = key_str.split(",")
                out[tuple(int(x) for x in parts)] = v
        return out
    except Exception:
        return None


def _save_omega_disk_v2(n: int, q_val: float, omegas: dict):
    import json as _json
    _OMEGA_DISK_DIR.mkdir(parents=True, exist_ok=True)
    f = _OMEGA_DISK_DIR / f"n{n}_q{q_val:.10f}_v2.json"
    payload = {}
    for shape, v in omegas.items():
        key = ",".join(str(x) for x in shape) if shape else ""
        payload[key] = v
    try:
        f.write_text(_json.dumps(payload))
    except Exception:
        pass


def _reduced_words_for_basis(n: int) -> list[tuple[int, ...]]:
    """Choose p(n) linearly-independent reduced words in S_n.

    For small n: use the minimal-length reduced word for each
    conjugacy class (cycle-type = partition representative).
    Guaranteed linearly independent by character-orthogonality.
    """
    from hecke_characters import partitions_of
    words = []
    for shape in partitions_of(n):
        # Build a reduced word whose image in S_n has cycle type shape.
        # For shape = (n_1, n_2, ..., n_k) with n_1 ≥ n_2 ≥ …:
        # Each cycle of length n_j contributes (n_j − 1) transpositions.
        # Arrange cycles back-to-back in disjoint ranges.
        word = []
        offset = 0
        for part in shape:
            # Cycle on {offset, …, offset+part-1}: s_{offset} s_{offset+1} …
            for t in range(part - 1):
                word.append(offset + t)
            offset += part
        words.append(tuple(word))
    return words


def tr_M_via_ocneanu_word(Z: int, N: int, *,
                            include_inter: bool = True,
                            m_pp: int = 1, m_pn: int = 1,
                            m_nn: int = 1,
                            q_val: float = None,
                            z_val: float = None) -> float:
    """FAST tr_M(W_atom) via raw braid-word multiplication + ω_λ weights.

    Bypasses SymbolicHeckeElement / Hecke reduction entirely: multiplies
    the (c, d, gen) factors directly in each seminormal irrep, then
    sums Σ_λ ω_λ · χ_λ(W) / d_λ with Ocneanu weights.

    Use for atom binding calculations — 100s of times faster than the
    reduce-then-Ocneanu path since it avoids the O(N²)–O(N³) Gröbner–
    Shirshov reduction cost.
    """
    from mass_at_3A_proper import (atom_braid_word_3A,
                                     chi_lambda_of_word,
                                     _cached_seminormal, Q0_PROTON)
    from hecke_characters import partitions_of
    if q_val is None:
        q_val = Q0
    if z_val is None:
        z_val = z_num
    A = Z + N
    if A < 1:
        return 1.0
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    omegas_by_shape = omega_lambda_via_inversion(n_strands,
                                                    q_val=q_val,
                                                    z_val=z_val)
    total = 0.0
    for shape in partitions_of(n_strands):
        sigmas, dim, _syts = _cached_seminormal(shape, Q0_PROTON)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, word, n_strands - 1)
        omega = omegas_by_shape.get(shape, 0.0)
        total += omega * chi / dim
    return total


def omega_lambda_via_inversion(n: int, *,
                                 q_val: float = None,
                                 z_val: float = None,
                                 use_conjugate_symmetry: bool = True
                                 ) -> dict[tuple, float]:
    """Compute ω_λ for all λ ⊢ n by inverting the canonical tr_M system.

    Uses:
      • markov_trace_canonical.tr_M_element as ground truth for tr_M(T_w).
      • hecke_characters seminormal matrices for χ_λ(T_w).
      • scipy.linalg.solve for the linear inversion.

    When ``use_conjugate_symmetry=True`` (default), for each
    non-self-conjugate pair (λ, λ') only ONE set of Hoefsmit matrices
    is built; χ^{λ'}(T_w) is derived from χ^λ(T_w) via the Track-2
    formula χ^{λ'}(T_w) = (-1)^{ℓ(w)} · χ^λ(T_w) |_{q → q^{-1}}.
    The matrix rebuild at q^{-1} is cheap compared to repeated
    character matmul, halving the dominant cost for non-self-conj
    partitions.  At n=12: 9 self-conj + 34 pairs = 43 distinct
    matrix-builds instead of 77.

    Cached per n (disk cache is shared across symmetry modes).
    """
    import numpy as np
    from scipy.linalg import solve
    from hecke_characters import (partitions_of, build_seminormal_matrices)
    from markov_trace_canonical import tr_M_element
    from hecke_symbolic import SymbolicHeckeElement, q as q_sym_hs
    from conjugate_symmetry import (is_self_conjugate,
                                       conjugate_partition,
                                       conjugate_pair_representatives)
    from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached

    if q_val is None:
        q_val = Q0

    cache_key = n
    if cache_key in _OMEGA_CACHE:
        return _OMEGA_CACHE[cache_key]
    # Try disk cache first
    disk_omegas = _load_omega_disk_v2(n, q_val)
    if disk_omegas is not None:
        _OMEGA_CACHE[cache_key] = disk_omegas
        return disk_omegas

    shapes = list(partitions_of(n))
    shape_index = {s: j for j, s in enumerate(shapes)}
    words = _reduced_words_for_basis(n)
    assert len(shapes) == len(words), \
        f"p({n}) = {len(shapes)} partitions, {len(words)} words"

    # Decide which shapes to evaluate directly vs derive via conjugate.
    if use_conjugate_symmetry:
        self_conj, pairs = conjugate_pair_representatives(n)
        direct_shapes = list(self_conj) + [rep for rep, _ in pairs]
        derived_map = {other: rep for rep, other in pairs}
    else:
        direct_shapes = shapes
        derived_map = {}

    from scipy.sparse import issparse, eye as speye
    from conjugate_symmetry import _build_seminormal_at_q

    def _eval_chi(sigmas, dim, w):
        if dim == 0:
            return 0.0
        is_sparse = issparse(sigmas[0]) if sigmas else False
        if is_sparse:
            prod = speye(dim, format='csr')
        else:
            prod = np.eye(dim)
        for g in w:
            if 0 <= g < len(sigmas):
                prod = prod @ sigmas[g]
            else:
                return None
        if is_sparse:
            return float(prod.diagonal().sum())
        return float(np.trace(prod))

    # Build coefficient matrix M[k, λ] = χ_λ(T_w_k) / d_λ.
    # Conjugate symmetry: build each Hoefsmit matrix set at q ONCE per
    # direct shape, and (if it has a conjugate partner) also at q^{-1}
    # ONCE per representative.  For non-symmetry mode, fall back to the
    # original per-(k,shape) rebuild (matches legacy behaviour).
    M = np.zeros((len(shapes), len(shapes)))
    rhs = np.zeros(len(shapes))

    sigmas_at_q_cache: dict[tuple, tuple] = {}
    sigmas_at_qinv_cache: dict[tuple, tuple] = {}
    # Shared Hoefsmit BlockCache across all shapes — Track 1.
    # Key ρ = content distance; entry (a_ρ, a'_ρ, b_ρ).  Reused across
    # every partition at this n; eliminates the O(d_λ²) swap-partner
    # scan in legacy build_seminormal_matrices.
    from q_parameter import HA as _HA
    block_cache = BlockCache(q_val, q_val - 1.0 / q_val)
    block_cache_qinv = BlockCache(1.0 / q_val, 1.0 / q_val - q_val)
    if use_conjugate_symmetry:
        for shape in direct_shapes:
            s, d, _ = build_seminormal_matrices_cached(
                shape, cache=block_cache)
            sigmas_at_q_cache[shape] = (s, d)
        reps_needing_qinv = set(derived_map.values())
        for shape in reps_needing_qinv:
            s, d, _ = build_seminormal_matrices_cached(
                shape, cache=block_cache_qinv,
                q_val=1.0 / q_val)
            sigmas_at_qinv_cache[shape] = (s, d)

    for k, w in enumerate(words):
        elem = (SymbolicHeckeElement({w: 1}) if w
                else SymbolicHeckeElement({(): 1}))
        tr_sym = tr_M_element(elem, n)
        tr_num = float(sp.N(tr_sym.subs(q_sym_hs, q_val)))
        rhs[k] = tr_num
        for shape in direct_shapes:
            if use_conjugate_symmetry:
                sigmas, d_lam = sigmas_at_q_cache[shape]
            else:
                # Legacy path: share BlockCache but not per-shape cache.
                sigmas, d_lam, _ = build_seminormal_matrices_cached(
                    shape, cache=block_cache)
            chi = _eval_chi(sigmas, d_lam, w)
            if chi is None or d_lam == 0:
                continue
            j = shape_index[shape]
            M[k, j] = chi / d_lam
        if use_conjugate_symmetry:
            for lp, rep in derived_map.items():
                sigmas_qi, dim = sigmas_at_qinv_cache[rep]
                chi_qi = _eval_chi(sigmas_qi, dim, w)
                if chi_qi is None or dim == 0:
                    continue
                chi_lp = ((-1) ** len(w)) * chi_qi
                j = shape_index[lp]
                M[k, j] = chi_lp / dim

    # Solve M · ω = rhs
    omega = solve(M, rhs)
    omega_dict = {shape: float(omega[j])
                   for j, shape in enumerate(shapes)}
    _OMEGA_CACHE[cache_key] = omega_dict
    _save_omega_disk_v2(n, q_val, omega_dict)
    return omega_dict


def verify_sum(n: int, *, q_val: float = None, z_val: float = None) -> dict:
    """Verify Σ_λ ω_λ = 1 at H_n."""
    if q_val is None:
        q_val = Q0
    if z_val is None:
        z_val = z_num
    total = 0.0
    entries = []
    from hecke_characters import partitions_of
    omegas = omega_lambda_via_inversion(n, q_val=q_val, z_val=z_val)
    for shape in partitions_of(n):
        omega = omegas.get(shape, 0.0)
        total += omega
        entries.append({"shape": shape, "omega": omega})
    return {"n": n, "total": total,
             "deviation_from_1": abs(total - 1.0),
             "entries": entries}


def verify_trace_of_T0(n: int, *, q_val: float = None,
                        z_val: float = None) -> dict:
    """Verify Σ_λ (ω_λ / d_λ) · χ_λ(T_0) = z at H_n.

    χ_λ(T_0) = (# cells in row 1 that contain entry 2 is first next
    to entry 1) · q - (# cells in col 1 same) · q⁻¹ ...
    More precisely: χ_λ(T_0) counts same-row and same-col SYTs:
    χ_λ(T_0) = m_+(λ, 0) · q + m_-(λ, 0) · (−q⁻¹)
    where m_+(λ, 0) and m_-(λ, 0) are computed via
    canonical_tower.eigen_multiplicities.
    """
    from canonical_tower import eigen_multiplicities
    from hecke_characters import partitions_of
    if q_val is None:
        q_val = Q0
    if z_val is None:
        z_val = z_num
    qi = 1.0 / q_val
    total = 0.0
    entries = []
    omegas = omega_lambda_via_inversion(n, q_val=q_val, z_val=z_val)
    for shape in partitions_of(n):
        omega = omegas.get(shape, 0.0)
        mp, mm = eigen_multiplicities(shape, 0)
        d_lam = mp + mm
        if d_lam == 0:
            continue
        chi = mp * q_val + mm * (-qi)
        contrib = omega * chi / d_lam
        total += contrib
        entries.append({"shape": shape, "omega": omega, "chi": chi,
                          "d_lam": d_lam, "contrib": contrib})
    return {"n": n, "total_tr": total, "expected_z": z_val,
             "deviation": abs(total - z_val), "entries": entries}


def canonical_markov_trace_via_ocneanu(elem, n: int, *,
                                         q_val: float = None,
                                         z_val: float = None) -> float:
    """tr_M(elem) via ω_λ weights + seminormal characters.

    FAST alternative to markov_trace_canonical.tr_M_element (via
    Hecke reduction): uses seminormal matrices from hecke_characters
    directly with Ocneanu weights (derived by inversion).

    elem: SymbolicHeckeElement OR a dict word → coefficient.
    """
    from hecke_characters import (build_seminormal_matrices,
                                    partitions_of)
    import numpy as np
    if q_val is None:
        q_val = Q0
    if z_val is None:
        z_val = z_num
    if hasattr(elem, "terms"):
        terms = elem.terms
    else:
        terms = elem
    # Precompute ω_λ for this n (cached)
    omegas_by_shape = omega_lambda_via_inversion(n, q_val=q_val,
                                                    z_val=z_val)
    total = 0.0
    for shape in partitions_of(n):
        sigmas, dim, _syts = build_seminormal_matrices(shape)
        if dim == 0:
            continue
        omega = omegas_by_shape.get(shape, 0.0)
        # Compute χ_λ(elem) = Σ_{word, coeff} coeff · tr(word in λ)
        chi_lam = 0.0
        for word, coeff in terms.items():
            # Build M_word in irrep λ
            try:
                from scipy.sparse import issparse, eye as speye
                is_sparse = issparse(sigmas[0]) if sigmas else False
            except ImportError:
                is_sparse = False
            if is_sparse:
                from scipy.sparse import eye as speye
                prod = speye(dim, format='csr')
            else:
                prod = np.eye(dim)
            for g in word:
                if 0 <= g < len(sigmas):
                    prod = prod @ sigmas[g]
                elif g < 0:
                    pass  # formal variable; skip
                else:
                    # gen out of range — element has generators beyond H_n
                    prod = None
                    break
            if prod is None:
                continue
            if is_sparse:
                tr_w = float(prod.diagonal().sum())
            else:
                tr_w = float(np.trace(prod))
            # Handle sympy coefficients: substitute q and evaluate
            if hasattr(coeff, "subs"):
                coeff_num = float(sp.N(
                    coeff.subs(sp.Symbol('q', positive=True), q_val)))
            else:
                coeff_num = float(coeff)
            chi_lam += coeff_num * tr_w
        total += omega * chi_lam / dim
    return total


if __name__ == "__main__":
    from hecke_characters import partitions_of
    print("=" * 80)
    print("OCNEANU WEIGHTS ω_λ(q, z) — symmetric Hecke convention")
    print(f"q₀ = {Q0:.6f},  z = 1/(q^½+q^{{-½}}) = {z_num:.6f}")
    print("=" * 80)

    # Hand-derived at H_2 (closed form from Markov-axiom system)
    print("\nHand derivation at H_2 (from (W1),(W2) linear system):")
    qi = 1.0 / Q0
    two_q = Q0 + qi
    ω_2 = (z_num + qi) / two_q
    ω_11 = (Q0 - z_num) / two_q
    print(f"  ω_(2)    = (z + q⁻¹) / [2]_q = {ω_2:.8f}")
    print(f"  ω_(1,1)  = (q − z)   / [2]_q = {ω_11:.8f}")
    print(f"  Σ = {ω_2 + ω_11:.8f}  (should be 1)")

    # Inversion-based derivation, verified against tr_M_element
    print("\nBy inversion of Markov axiom system:")
    print(f"  {'n':>3} {'p(n)':>6} {'Σω':>12} {'dev 1':>12}")
    for n in [2, 3, 4, 5]:
        import time as _time
        t0 = _time.time()
        omegas = omega_lambda_via_inversion(n)
        dt = _time.time() - t0
        total = sum(omegas.values())
        print(f"  {n:>3} {len(omegas):>6} {total:>12.8f} "
              f"{abs(total - 1):>12.3e}  ({dt:.1f}s)")
        if n == 2:
            for s, o in omegas.items():
                print(f"    ω_{s} = {o:.8f}")

    # Test: compare Ocneanu-derived ω-based trace vs canonical on prop table
    print("\nVerify Ocneanu-weights-based tr_M against prop's explicit table:")
    from hecke_symbolic import SymbolicHeckeElement
    h_num = Q0 - 1.0/Q0
    TESTS = [
        ("𝟏 (photon)",           (),                1.0),
        ("σ_0 (polarization)",    (0,),              z_num),
        ("σ_0σ_1 (gluon)",         (0, 1),           z_num ** 2),
        ("σ_0σ_1σ_0 (electron)",  (0, 1, 0),        h_num * z_num ** 2 + z_num),
        ("σ_1σ_0σ_1 (braid)",     (1, 0, 1),        h_num * z_num ** 2 + z_num),
    ]
    # Use inversion-derived ω (correct); adapt to n = max(word) + 2
    print(f"\n  {'Word':>24} {'Via ω (inversion)':>20} "
          f"{'Expected':>14} {'match':>6}")
    print("  " + "-" * 68)
    for name, word, expected in TESTS:
        n = max(word) + 2 if word else 1
        if n == 1:
            via = 1.0
        else:
            omegas = omega_lambda_via_inversion(n)
            from hecke_characters import (build_seminormal_matrices,
                                            partitions_of)
            import numpy as np
            total = 0.0
            for shape in partitions_of(n):
                sigmas, d_lam, _ = build_seminormal_matrices(shape)
                if d_lam == 0:
                    continue
                try:
                    from scipy.sparse import issparse, eye as speye
                    is_sparse = issparse(sigmas[0]) if sigmas else False
                except ImportError:
                    is_sparse = False
                if is_sparse:
                    from scipy.sparse import eye as speye
                    prod = speye(d_lam, format='csr')
                else:
                    prod = np.eye(d_lam)
                for g in word:
                    prod = prod @ sigmas[g]
                chi = (float(prod.diagonal().sum()) if is_sparse
                        else float(np.trace(prod)))
                total += omegas[shape] * chi / d_lam
            via = total
        match = "✓" if abs(via - expected) < 1e-6 else "✗"
        print(f"  {name:>24} {via:>+20.10f} {expected:>+14.8f} {match:>6}")
