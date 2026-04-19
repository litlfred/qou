"""Gram matrix G on the H_3(q) NF basis, NF multiplication, and exact
(Fraction) variants — canonical owner.

Authoritative source for:
  Constants   NF_BASIS, NF_NAMES, TR_M, z, W_SYM, W_STD, W_ALT, G, G_INV
  Functions   hm, hm_exact, nf_tr, nf_net
  Internals   _hm_dict, _reduce_nf, _build_gram

Moved here (with inversion in M2b) from the 3425-line
folio-assistant/computations/hecke_core.py so there is a single
source of truth that downstream code can depend on. `hecke_core.py`
now imports these back for backward compatibility.

Every coefficient carries over exactly from the original definition;
values of G, G_INV, and every NF multiplication are byte-identical
to the pre-inversion implementation.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from . import _legacy  # noqa: F401  — adjusts sys.path
from . import bridge  # single source of truth for pyhecke_native

from q_parameter import Q as q0, Q_INV as qi, HA as h  # type: ignore[import-not-found]


# ══════════════════════════════════════════════════════════════
# Native acceleration (delegated to bridge — no duplicate import)
# ══════════════════════════════════════════════════════════════
# The PyO3 module is imported once, in `pyhecke.bridge`. This module
# just reads the cached handle so there is a single place where native
# availability is detected and a single place to add new native
# dispatches.

_native = bridge._NATIVE
_HAS_NATIVE = _native is not None


def has_native() -> bool:
    """True iff the pyhecke_native wheel is installed.

    Delegates to :func:`pyhecke.bridge.has_native` so the check is
    defined in exactly one place.
    """
    return bridge.has_native()


# ══════════════════════════════════════════════════════════════
# Scalar constants
# ══════════════════════════════════════════════════════════════

z = 1.0 / (q0 ** 0.5 + qi ** 0.5)

# Wedderburn-Artin weights for H_3(q)
_q2 = q0 ** 2
_denom_w = _q2 ** 2 + 4 * _q2 + 1
W_SYM = _q2 / _denom_w
W_STD = (_q2 + 1) ** 2 / _denom_w
W_ALT = _q2 / _denom_w


# ══════════════════════════════════════════════════════════════
# NF basis and Markov-trace weights
# ══════════════════════════════════════════════════════════════

NF_BASIS: list[tuple[int, ...]] = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES: list[str] = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M = np.array([1.0, z, z, z ** 2, z ** 2, z ** 3])


# Bond operators for molecular binding (per-generator crossing chains)
INV_TREFOIL_G0 = [(1, -h), (1, -h)]  # σ₀⁻¹σ₀⁻¹
INV_TREFOIL_G1 = [(1, -h)]  # σ₁⁻¹


# ══════════════════════════════════════════════════════════════
# NF multiplication in H_3(q)
# ══════════════════════════════════════════════════════════════

def _hm_tables(h_val, c, d, gen):
    """Dispatch table for the NF multiplication kernel.

    Returned list has the shape ``[(source_idx, [(target_idx, coeff), …]), …]``
    matching the pre-inversion hecke_core layout. Same structure is used
    by the float path (:func:`_hm_pure`) and the exact-rational path
    (:func:`hm_exact`); only ``h_val`` and the initial zero differ.
    """
    if gen == 0:
        return [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h_val), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h_val), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h_val), (4, c), (5, d)]),
        ]
    return [
        (0, [(2, c), (0, d)]),
        (1, [(4, c), (1, d)]),
        (2, [(2, c * h_val), (0, c), (2, d)]),
        (3, [(5, c), (3, d)]),
        (4, [(4, c * h_val), (1, c), (4, d)]),
        (5, [(5, c * h_val), (3, c), (5, d)]),
    ]


def _hm_apply(nf, tables, zero, is_zero):
    """Run the 6-row NF multiplication given a prebuilt table."""
    r = [zero] * 6
    for si, tgts in tables:
        coeff = nf[si]
        if is_zero(coeff):
            continue
        for ti, co in tgts:
            r[ti] += coeff * co
    return r


def _hm_pure(nf, c, d, gen):
    """Pure-Python float NF multiplication. Used as the fallback when
    ``pyhecke_native`` is not available."""
    return _hm_apply(nf, _hm_tables(h, c, d, gen), 0.0,
                     lambda x: abs(x) < 1e-15)


def hm(nf, c, d, gen):
    """Multiply NF element by ``(c·σ_gen + d·I)``. Returns a fresh
    6-element list.

    Dispatches to ``pyhecke_native.hm`` when the wheel is installed
    (~10× the pure-Python speed on the hot path). Falls back to
    :func:`_hm_pure` otherwise — numerics are byte-identical.

    **Round-trip caveat**: each call marshals ``nf`` from Python to
    Rust and back. For tight loops that apply many NF multiplications,
    call :func:`build_atom_nf` (which keeps the full chain inside
    Rust — one marshal per atom) instead of looping ``hm`` from Python.
    """
    if _HAS_NATIVE:
        # `list(nf)` handles both list and numpy-array inputs;
        # the native layer allocates a length-6 Vec internally.
        return list(_native.hm(list(nf), float(c), float(d), int(gen)))
    return _hm_pure(nf, c, d, gen)


def nf_tr(nf):
    """Markov trace of an NF element. Native-dispatched when available."""
    if _HAS_NATIVE:
        return _native.nf_tr(list(nf))
    return sum(nf[i] * TR_M[i] for i in range(6))


def nf_net(nf):
    """Net (sum of NF coefficients).

    Intentionally **not** native-dispatched: ``sum(nf)`` is a trivial
    Python builtin and the PyO3 marshal of the 6-element input would
    outweigh the arithmetic. Use the native call directly only if you
    already have the data on the Rust side.
    """
    return sum(nf)


# ══════════════════════════════════════════════════════════════
# Gram matrix
# ══════════════════════════════════════════════════════════════

def _hm_dict(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def _reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    i = word[p]
                    pre, suf = word[:p], word[p + 2:]
                    new[pre + (i,) + suf] = new.get(pre + (i,) + suf, 0) + coeff * h
                    new[pre + suf] = new.get(pre + suf, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def _build_gram():
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = _hm_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = _reduce_nf(prod)
            vec = np.array([nf.get(b, 0.0) for b in NF_BASIS])
            G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))
    return G


G = _build_gram()
G_INV = np.linalg.inv(G)

# Identity NF: the trivial braid [1, 0, 0, 0, 0, 0]
_ID_NF = np.array([1.0, 0, 0, 0, 0, 0])


# ══════════════════════════════════════════════════════════════
# Exact rational NF computation via Fraction arithmetic
# ══════════════════════════════════════════════════════════════
# H_3(q) at q = 111/100 is exact in ℚ. Uses Python's Fraction — no
# floating point, no overflow.

_Q_FRAC = Fraction(111, 100)
_QI_FRAC = Fraction(100, 111)
_H_FRAC = _Q_FRAC - _QI_FRAC  # h = q - 1/q (exact rational)
_Z_FRAC = Fraction(4993, 10000)  # z ≈ 1/(q^{1/2}+q^{-1/2})

_TR_M_FRAC = [Fraction(1), _Z_FRAC, _Z_FRAC,
              _Z_FRAC ** 2, _Z_FRAC ** 2, _Z_FRAC ** 3]

_SYM_EIG_FRAC = [Fraction(1), _Q_FRAC, _Q_FRAC,
                 _Q_FRAC ** 2, _Q_FRAC ** 2, _Q_FRAC ** 3]
_ALT_EIG_FRAC = [Fraction(1), -_QI_FRAC, -_QI_FRAC,
                 _QI_FRAC ** 2, _QI_FRAC ** 2, -_QI_FRAC ** 3]


def hm_exact(nf, c, d, gen):
    """Exact Fraction multiplication: NF × (c·σ_gen + d·I).

    Same logic as :func:`hm` but with Fraction arithmetic — no
    rounding, no floating-point error. Not native-dispatched: the
    PyO3 layer only exposes the f64 kernel. For exact rationals we
    run the Python loop over the shared dispatch table.
    """
    return _hm_apply(nf, _hm_tables(_H_FRAC, c, d, gen), Fraction(0),
                     lambda x: x == 0)


# ══════════════════════════════════════════════════════════════
# Public API
# ══════════════════════════════════════════════════════════════

__all__ = [
    # Scalar constants
    "z", "W_SYM", "W_STD", "W_ALT",
    # NF basis
    "NF_BASIS", "NF_NAMES", "TR_M",
    # Bond operators
    "INV_TREFOIL_G0", "INV_TREFOIL_G1",
    # NF multiplication
    "hm", "hm_exact", "nf_tr", "nf_net",
    # Gram matrix
    "G", "G_INV", "gram_matrix", "gram_inverse",
    # Native-dispatched atom kernels
    "build_atom_nf", "atom_per_generator_volumes", "has_native",
    # Exact-rational internals (rarely used externally)
    "_H_FRAC", "_Z_FRAC", "_TR_M_FRAC",
    "_SYM_EIG_FRAC", "_ALT_EIG_FRAC",
]


def gram_matrix() -> np.ndarray:
    """Return the 6x6 Gram matrix on the NF basis at q = q_0."""
    return G


def gram_inverse() -> np.ndarray:
    """Return G^{-1}."""
    return G_INV


# ══════════════════════════════════════════════════════════════
# Native-accelerated atom kernels
# ══════════════════════════════════════════════════════════════
# When the `pyhecke_native` wheel is installed, these dispatch to the
# Rust implementation (~100× on ⁴⁰Ca). Fallback is hecke_core's pure
# Python. hecke_core is imported lazily at call time to avoid
# circular-import with pyhecke.gram's own loading.
#
# The native handle `_native` is set at the top of this module (shared
# with `hm` / `nf_tr` dispatch) — no second import block here.


def build_atom_nf(Z: int, N: int):
    """Build the atom NF for (Z, N). Native-dispatched; falls back
    to hecke_core.build_atom_nf when the wheel is absent."""
    if _HAS_NATIVE:
        return _native.build_atom_nf(Z, N)
    import hecke_core  # type: ignore[import-not-found]
    return hecke_core.build_atom_nf(Z, N)


def atom_per_generator_volumes(
    Z: int,
    N: int,
    include_inter: bool = True,
    crossings_per_pair: int = 1,
    m_pp=None, m_pn=None, m_nn=None,
):
    """Per-generator Wedderburn volumes for the atom braid. Native-
    dispatched; falls back to hecke_core.atom_per_generator_volumes
    when the wheel is absent."""
    if _HAS_NATIVE:
        return _native.atom_per_generator_volumes(
            Z, N,
            include_inter=include_inter,
            crossings_per_pair=crossings_per_pair,
            m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        )
    import hecke_core  # type: ignore[import-not-found]
    return hecke_core.atom_per_generator_volumes(
        Z, N,
        include_inter=include_inter,
        crossings_per_pair=crossings_per_pair,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
    )
