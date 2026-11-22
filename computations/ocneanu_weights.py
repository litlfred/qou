#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Ocneanu / Jones–Markov weights ω_λ(q, z) for Iwahori–Hecke H_n(q).

Symmetric convention:
    σ² = (q − q⁻¹)σ + 1     (eigenvalues  q, −q⁻¹)
    z = q³ / (q² + 1)       (Markov parameter — convention D, canonical)

This line read `z = 1 / (q^{1/2} + q^{−1/2})` — convention C, excised by owner
ruling 2026-08-15 — until 2026-10-10, while the module's own bindings were
already convention D: `z_num = Q0**3 / (Q0**2 + 1)` and
`z_sym = q**3 / (q**2 + 1)` (both below). Only the LABELS were C; no binding in
this file was ever the C value, and the value audit
(`scripts/convention-c-value-audit.py`) has never reported one here. Bean
`qou-pc7l`, re-measured on the 2026-10-10 C→D re-audit (`qou-am5t`).

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
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from partition_utils import hook_lengths_with_cells as hook_lengths  # noqa: E402
from qou_substrate.precision import COMPUTE_DPS  # noqa: E402


# PRECISION (owner approval 2026-11-22, branch-cache item P9).  This module was
# float64 end to end: numpy seminormal matrices, `scipy.linalg.solve`, and a
# `float()` on every trace, with an in-memory cache keyed on `n` alone (so a
# second q in one process was served the first q's weights) and a disk cache
# keyed on `q:.10f`.  It now carries `mpmath.mpf` end to end: exact-q sparse
# seminormal matrices, the symbolic tr_M evaluated by mpmath, and
# `mp.lu_solve`.  Both caches key on the exact q (its decimal string at the
# working precision) and on that precision.  Default precision is
# `qou_substrate.precision.COMPUTE_DPS`; a caller may pass `dps=`.
#
# `Q0` and `z_num` are `mpf` at COMPUTE_DPS (they were float64).  `Q0` is the
# q_parameter anchor string, i.e. the same anchor the float `Q` named before.
with mp.workdps(COMPUTE_DPS):
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    z_num = Q0 ** 3 / (Q0 ** 2 + 1)

# Symbolic q and z for derivation
q = sp.Symbol('q', positive=True)
z = sp.Symbol('z', positive=True)
z_sym = q**3 / (q**2 + 1)


def _as_mpf(x):
    """Exact conversion of a q value to mpf at the current precision.

    str / mpf / int / Fraction / sympy Rational go through exactly.  A float
    is taken at its exact binary value (mpf(float) is exact): the float64
    rounding is then the caller's, not this module's.
    """
    if isinstance(x, mp.mpf):
        return +x
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / x.denominator
    if isinstance(x, sp.Rational):
        return mp.mpf(int(x.p)) / int(x.q)
    if isinstance(x, sp.Basic):
        return mp.mpf(str(sp.N(x, mp.dps + 10)))
    return mp.mpf(x)


def omega_lambda_formula_guess(shape: tuple[int, ...], *,
                                 q_val=None, z_val=None):
    """FAILED GUESS: hook-content formula Π(z q^c − q^{−c})/(q^h − q^{−h}).

    Does NOT satisfy Σ ω = 1 at q ≠ 1.  Retained for reference; see
    omega_lambda_via_inversion below for the correct approach.
    """
    qv = Q0 if q_val is None else _as_mpf(q_val)
    zv = z_num if z_val is None else _as_mpf(z_val)
    num = mp.mpf(1)
    den = mp.mpf(1)
    for (i, j, h) in hook_lengths(shape):
        c = j - i
        num *= zv * qv ** c - qv ** (-c)
        den *= qv ** h - qv ** (-h)
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

_OMEGA_CACHE: dict[tuple, dict[tuple, "mp.mpf"]] = {}
_OMEGA_DISK_DIR = Path(__file__).parent / ".cache" / "ocneanu"
# Bump when the computation changes in a way that moves values.
_OMEGA_DISK_VERSION = "v3-mpf"


def _q_key(qv, dps: int) -> str:
    """Exact cache tag for q at precision dps: its full decimal string."""
    return mp.nstr(qv, dps + 5, strip_zeros=False)


def _omega_disk_path(n: int, q_key: str, dps: int) -> Path:
    h = hashlib.sha256(f"{_OMEGA_DISK_VERSION}|{n}|{dps}|{q_key}".encode()
                       ).hexdigest()[:20]
    return _OMEGA_DISK_DIR / f"n{n}_dps{dps}_{h}.json"


def _load_omega_disk(n: int, q_key: str, dps: int):
    f = _omega_disk_path(n, q_key, dps)
    if not f.exists():
        return None
    try:
        raw = json.loads(f.read_text())
        if raw.get("q") != q_key or raw.get("dps") != dps \
                or raw.get("version") != _OMEGA_DISK_VERSION:
            return None
        out = {}
        for key_str, v in raw["omega"].items():
            shape = tuple(int(x) for x in key_str.split(",")) if key_str else ()
            out[shape] = mp.mpf(v)
        return out
    except Exception:
        return None


def _save_omega_disk(n: int, q_key: str, dps: int, omegas: dict):
    try:
        _OMEGA_DISK_DIR.mkdir(parents=True, exist_ok=True)
        payload = {
            "version": _OMEGA_DISK_VERSION, "n": n, "dps": dps, "q": q_key,
            "omega": {",".join(str(x) for x in s): mp.nstr(v, dps + 5,
                                                           strip_zeros=False)
                      for s, v in omegas.items()},
        }
        _omega_disk_path(n, q_key, dps).write_text(json.dumps(payload))
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
        word = []
        offset = 0
        for part in shape:
            for t in range(part - 1):
                word.append(offset + t)
            offset += part
        words.append(tuple(word))
    return words


# ── Exact sparse seminormal representation (mpf) ──
#
# Same entries as `hecke_characters.build_seminormal_matrices_mp` (a, a', b
# with a = h/(1 − q^{−2ρ}), a' = h/(1 − q^{2ρ}), b = sqrt|a a' + 1|), stored
# row-sparse ({row: {col: value}}) so that n beyond ~8 does not need O(d²)
# dense mp matrices.  `_check_sparse_matches_dense` cross-checks the two.

def _sparse_seminormal_mp(shape, qv):
    from hecke_characters import standard_young_tableaux
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0
    exact_one = (qv == 1)
    h_local = None if exact_one else qv - 1 / qv
    syt_index = {tuple(sorted(t.items())): idx for idx, t in enumerate(syts)}
    sigmas = []
    for k in range(1, n):
        rows: dict[int, dict[int, "mp.mpf"]] = {}
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            if exact_one:
                a = mp.mpf(1) / rho
                a_prime = -a
            else:
                a = h_local / (1 - qv ** (-2 * rho))
                a_prime = h_local / (1 - qv ** (2 * rho))
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = syt_index.get(tuple(sorted(swap_map.items())))
            if j == i:
                j = None
            if j is None:
                rows[i] = {i: a}
                processed.add(i)
            else:
                b = mp.sqrt(abs(a * a_prime + 1))
                rows[i] = {i: a, j: b}
                rows[j] = {j: a_prime, i: b}
                processed.add(i)
                processed.add(j)
        sigmas.append(rows)
    return sigmas, dim


def _trace_factors(sigmas, dim, factors):
    """tr Π_k (c_k σ_{g_k} + d_k I) in a sparse mp irrep.

    ``factors`` is a sequence of (c, d, g).  Returns None if some g is out of
    range for this irrep (matches the old dense helpers' convention).
    """
    if dim == 0:
        return mp.mpf(0)
    total = mp.mpf(0)
    # Row-by-row: row i of the product, then its diagonal entry.
    for g in (f[2] for f in factors):
        if not (0 <= g < len(sigmas)):
            return None
    for i in range(dim):
        row = {i: mp.mpf(1)}
        for (c, d, g) in factors:
            sg = sigmas[g]
            new: dict[int, "mp.mpf"] = {}
            for kk, v in row.items():
                if d != 0:
                    new[kk] = new.get(kk, 0) + v * d
                if c != 0:
                    for jj, s in sg[kk].items():
                        new[jj] = new.get(jj, 0) + v * c * s
            row = new
        total += row.get(i, 0)
    return total


def _check_sparse_matches_dense(shape, qv) -> "mp.mpf":
    """Max |sparse − dense| entry against build_seminormal_matrices_mp."""
    from hecke_characters import build_seminormal_matrices_mp
    dense, ddim, _ = build_seminormal_matrices_mp(shape, qv)
    sparse, sdim = _sparse_seminormal_mp(shape, qv)
    assert ddim == sdim
    worst = mp.mpf(0)
    for M, rows in zip(dense, sparse):
        for i in range(ddim):
            for j in range(ddim):
                worst = max(worst, abs(M[i, j] - rows.get(i, {}).get(j, 0)))
    return worst


def tr_M_via_ocneanu_word(Z: int, N: int, *,
                            include_inter: bool = True,
                            m_pp: int = 1, m_pn: int = 1,
                            m_nn: int = 1,
                            q_val=None,
                            z_val=None,
                            dps: int | None = None):
    """tr_M(W_atom) via braid-word multiplication + ω_λ weights, in mpf.

    Multiplies the (c, d, gen) factors directly in each exact sparse
    seminormal irrep at q, then sums Σ_λ ω_λ · χ_λ(W) / d_λ with Ocneanu
    weights.  Bypasses Gröbner–Shirshov reduction.

    Until 2026-11-22 the characters came from the float64 kernel
    `mass_at_3A_proper.chi_lambda_of_word` built at the PROTON pin regardless
    of ``q_val``; they are now built at ``q_val`` (default `Q0`).
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_characters import partitions_of
    dps = COMPUTE_DPS if dps is None else int(dps)
    A = Z + N
    if A < 1:
        return mp.mpf(1)
    with mp.workdps(dps):
        qv = Q0 if q_val is None else _as_mpf(q_val)
        n_strands = 3 * A
        word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                    include_inter=include_inter)
        factors = [(_as_mpf(c), _as_mpf(d), g) for (c, d, g) in word]
        omegas_by_shape = omega_lambda_via_inversion(n_strands, q_val=qv,
                                                     dps=dps)
        total = mp.mpf(0)
        for shape in partitions_of(n_strands):
            sigmas, dim = _sparse_seminormal_mp(shape, qv)
            if dim == 0:
                continue
            chi = _trace_factors(sigmas, dim, factors)
            if chi is None:
                continue
            total += omegas_by_shape.get(shape, 0) * chi / dim
        return +total


def omega_lambda_via_inversion(n: int, *,
                                 q_val=None,
                                 z_val=None,
                                 use_conjugate_symmetry: bool = True,
                                 dps: int | None = None
                                 ) -> dict[tuple, "mp.mpf"]:
    """Compute ω_λ for all λ ⊢ n by inverting the canonical tr_M system, in mpf.

    Uses:
      • markov_trace_canonical.tr_M_element as ground truth for tr_M(T_w),
        a rational function of q evaluated by mpmath at the exact q;
      • exact sparse seminormal matrices at q for χ_λ(T_w);
      • `mp.lu_solve` for the p(n) × p(n) inversion, with the solve's
        residual checked.

    ``q_val`` may be an mpf, a decimal string, an int, a Fraction or a sympy
    Rational (all exact); a float is taken at its exact binary value.
    ``z_val`` is accepted for signature compatibility and is NOT used: z is
    fixed by convention D inside `tr_M_element` (it always was).
    ``use_conjugate_symmetry`` is accepted and ignored: every irrep is now
    built directly at q (the q→q⁻¹ derivation was a float64-cost shortcut).
    ``dps`` defaults to `qou_substrate.precision.COMPUTE_DPS`.

    Returns {shape: mpf}.  Cached in memory and on disk, keyed on
    (n, dps, exact q string).
    """
    from hecke_characters import partitions_of
    from markov_trace_canonical import tr_M_element
    from hecke_symbolic import SymbolicHeckeElement, q as q_sym_hs

    dps = COMPUTE_DPS if dps is None else int(dps)
    with mp.workdps(dps):
        qv = Q0 if q_val is None else _as_mpf(q_val)
        q_key = _q_key(qv, dps)
        cache_key = (n, dps, q_key)
        if cache_key in _OMEGA_CACHE:
            return _OMEGA_CACHE[cache_key]
        disk = _load_omega_disk(n, q_key, dps)
        if disk is not None:
            _OMEGA_CACHE[cache_key] = disk
            return disk

        shapes = list(partitions_of(n))
        words = _reduced_words_for_basis(n)
        assert len(shapes) == len(words), \
            f"p({n}) = {len(shapes)} partitions, {len(words)} words"

        reps = {s: _sparse_seminormal_mp(s, qv) for s in shapes}
        P = len(shapes)
        M = mp.zeros(P, P)
        rhs = mp.zeros(P, 1)
        for k, w in enumerate(words):
            elem = (SymbolicHeckeElement({w: 1}) if w
                    else SymbolicHeckeElement({(): 1}))
            tr_sym = sp.sympify(tr_M_element(elem, n))
            f = sp.lambdify(q_sym_hs, tr_sym, "mpmath")
            rhs[k] = mp.mpf(f(qv)) if tr_sym.free_symbols else _as_mpf(tr_sym)
            factors = [(1, 0, g) for g in w]
            for j, shape in enumerate(shapes):
                sigmas, d_lam = reps[shape]
                if d_lam == 0:
                    continue
                chi = _trace_factors(sigmas, d_lam, factors)
                if chi is None:
                    continue
                M[k, j] = chi / d_lam

        omega = mp.lu_solve(M, rhs)
        resid = mp.norm(M * omega - rhs, mp.inf)
        scale = max(mp.norm(rhs, mp.inf), mp.mpf(1))
        if resid > scale * mp.mpf(10) ** (-(dps - 10)):
            raise ArithmeticError(
                f"omega_lambda_via_inversion(n={n}): solve residual "
                f"{mp.nstr(resid, 5)} exceeds 10^-{dps - 10}; system "
                f"ill-conditioned at this precision")
        omega_dict = {shape: +omega[j] for j, shape in enumerate(shapes)}
    _OMEGA_CACHE[cache_key] = omega_dict
    _save_omega_disk(n, q_key, dps, omega_dict)
    return omega_dict


def verify_sum(n: int, *, q_val=None, z_val=None) -> dict:
    """Verify Σ_λ ω_λ = 1 at H_n (mpf)."""
    from hecke_characters import partitions_of
    omegas = omega_lambda_via_inversion(n, q_val=q_val)
    total = mp.mpf(0)
    entries = []
    for shape in partitions_of(n):
        omega = omegas.get(shape, mp.mpf(0))
        total += omega
        entries.append({"shape": shape, "omega": omega})
    return {"n": n, "total": total,
             "deviation_from_1": abs(total - 1),
             "entries": entries}


def verify_trace_of_T0(n: int, *, q_val=None, z_val=None) -> dict:
    """Verify Σ_λ (ω_λ / d_λ) · χ_λ(T_0) = z at H_n (mpf).

    χ_λ(T_0) = m_+(λ, 0) · q + m_-(λ, 0) · (−q⁻¹), with the multiplicities
    from canonical_tower.eigen_multiplicities (integers).
    """
    from canonical_tower import eigen_multiplicities
    from hecke_characters import partitions_of
    with mp.workdps(COMPUTE_DPS):
        qv = Q0 if q_val is None else _as_mpf(q_val)
        zv = qv ** 3 / (qv ** 2 + 1) if z_val is None else _as_mpf(z_val)
        qi = 1 / qv
        total = mp.mpf(0)
        entries = []
        omegas = omega_lambda_via_inversion(n, q_val=qv)
        for shape in partitions_of(n):
            omega = omegas.get(shape, mp.mpf(0))
            mpl, mmi = eigen_multiplicities(shape, 0)
            d_lam = mpl + mmi
            if d_lam == 0:
                continue
            chi = mpl * qv + mmi * (-qi)
            contrib = omega * chi / d_lam
            total += contrib
            entries.append({"shape": shape, "omega": omega, "chi": chi,
                              "d_lam": d_lam, "contrib": contrib})
        return {"n": n, "total_tr": total, "expected_z": zv,
                 "deviation": abs(total - zv), "entries": entries}


def canonical_markov_trace_via_ocneanu(elem, n: int, *, q_val=None,
                                         z_val=None, dps: int | None = None):
    """tr_M(elem) via ω_λ weights + exact seminormal characters (mpf).

    FAST alternative to markov_trace_canonical.tr_M_element (via
    Hecke reduction).  elem: SymbolicHeckeElement OR a dict word → coeff.
    Sympy coefficients are evaluated at q by mpmath; negative generator
    indices (formal variables) are skipped; a word with a generator beyond
    H_n is dropped (both as before).  Returns an mpf.
    """
    from hecke_characters import partitions_of
    dps = COMPUTE_DPS if dps is None else int(dps)
    terms = elem.terms if hasattr(elem, "terms") else elem
    with mp.workdps(dps):
        qv = Q0 if q_val is None else _as_mpf(q_val)
        omegas_by_shape = omega_lambda_via_inversion(n, q_val=qv, dps=dps)
        q_s = sp.Symbol('q', positive=True)
        coeffs = {}
        for word, coeff in terms.items():
            if isinstance(coeff, sp.Basic) and coeff.free_symbols:
                coeffs[word] = mp.mpf(sp.lambdify(q_s, coeff, "mpmath")(qv))
            else:
                coeffs[word] = _as_mpf(coeff) if isinstance(
                    coeff, (sp.Basic, Fraction, int, str)) else mp.mpf(coeff)
        total = mp.mpf(0)
        for shape in partitions_of(n):
            sigmas, dim = _sparse_seminormal_mp(shape, qv)
            if dim == 0:
                continue
            chi_lam = mp.mpf(0)
            for word, c in coeffs.items():
                factors = [(1, 0, g) for g in word if g >= 0]
                tr_w = _trace_factors(sigmas, dim, factors)
                if tr_w is None:
                    continue
                chi_lam += c * tr_w
            total += omegas_by_shape.get(shape, 0) * chi_lam / dim
        return +total


if __name__ == "__main__":
    import time as _time
    from hecke_characters import partitions_of
    mp.dps = COMPUTE_DPS
    print("=" * 80)
    print("OCNEANU WEIGHTS ω_λ(q, z) — symmetric Hecke convention (mpf)")
    # Convention-D banner (bean qou-pc7l): z_num has always been q³/(q²+1).
    print(f"q₀ = {mp.nstr(Q0, 16)},  z = q³/(q²+1) = {mp.nstr(z_num, 16)},"
          f"  dps = {COMPUTE_DPS}")
    print("=" * 80)

    print("\nSparse vs dense mp seminormal entries (max |Δ|):")
    for s in [(2, 1), (3, 2), (2, 2, 1), (3, 2, 1)]:
        print(f"  {s}: {mp.nstr(_check_sparse_matches_dense(s, Q0), 3)}")

    print("\nHand derivation at H_2 (from (W1),(W2) linear system):")
    qi = 1 / Q0
    two_q = Q0 + qi
    w_2 = (z_num + qi) / two_q
    w_11 = (Q0 - z_num) / two_q
    print(f"  ω_(2)    = (z + q⁻¹) / [2]_q = {mp.nstr(w_2, 30)}")
    print(f"  ω_(1,1)  = (q − z)   / [2]_q = {mp.nstr(w_11, 30)}")

    print("\nBy inversion of Markov axiom system:")
    print(f"  {'n':>3} {'p(n)':>6} {'|Σω − 1|':>12}")
    for n in [2, 3, 4, 5, 6]:
        t0 = _time.time()
        omegas = omega_lambda_via_inversion(n)
        dt = _time.time() - t0
        total = sum(omegas.values())
        print(f"  {n:>3} {len(omegas):>6} {mp.nstr(abs(total - 1), 3):>12}"
              f"  ({dt:.1f}s)")
        if n == 2:
            for s, o in omegas.items():
                print(f"    ω_{s} = {mp.nstr(o, 30)}")
            print(f"    |ω_(2) − hand| = {mp.nstr(abs(omegas[(2,)] - w_2), 3)}")

    print("\nVerify Ocneanu-weights-based tr_M against prop's explicit table:")
    h_num = Q0 - 1 / Q0
    TESTS = [
        ("𝟏 (photon)",            (),          mp.mpf(1)),
        ("σ_0 (polarization)",    (0,),        z_num),
        ("σ_0σ_1 (gluon)",        (0, 1),      z_num ** 2),
        ("σ_0σ_1σ_0 (electron)",  (0, 1, 0),   h_num * z_num ** 2 + z_num),
        ("σ_1σ_0σ_1 (braid)",     (1, 0, 1),   h_num * z_num ** 2 + z_num),
    ]
    for name, word, expected in TESTS:
        n = max(word) + 2 if word else 1
        via = (mp.mpf(1) if n == 1 else
               canonical_markov_trace_via_ocneanu({word: 1}, n))
        print(f"  {name:>24} {mp.nstr(via, 20):>26} |Δ| = "
              f"{mp.nstr(abs(via - expected), 3)}")
