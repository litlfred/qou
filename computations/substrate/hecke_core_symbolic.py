"""Symbolic-in-q companion to ``hecke_core``.

Background (audit §3·E in
``docs/audits/2026-05-01-math-framework-deep-audit.md``):
    "all Markov / V should be in ℤ[q^{±1}] (sympy or CRT
    reconstruction), with q_0-substitution **only at the final step**.
    Currently the proton/neutron/atom paths substitute q_0 early."

``hecke_core.py`` imports ``Q``, ``Q_INV``, ``HA`` from
``q_parameter`` as **floats**.  Every downstream construction
(``z``, ``W_SYM``, ``W_STD``, ``W_ALT``, ``hm``, ``hm_exact``,
``vertex_volume``, ``atom_V_full``, ``_chain_V_full``,
``_vertex_channels``, ``_phi1_from_ordering``, ``q_int(n)``, …) is
therefore numerical from the very first multiplication.  Even
``hm_exact`` only escapes f64 by **pinning q to the rational
``111/100``** — not a symbolic q.

This module recreates the same API but with ``q`` carried as a
sympy ``Symbol``.  Substitution into ``q = q_0`` (the
``Vol(4_1)/(m_μ/m_e)`` value from ``q_parameter``) happens **only at
the final step** through :func:`evalf_at_q0`, which uses mpmath at
50 dps for the Q-value emission.

Public surface (mirrors ``hecke_core``):

    Symbolic constants
        q, q_inv, h, z, two_q, w_sym, w_std, w_alt, q_int(n)

    NF basis multiplication
        hm_sym(nf, c, d, gen)
        nf_tr_sym(nf), nf_net_sym(nf)

    Atom braid (symbolic)
        build_atom_nf_sym(Z, N)
        atom_gen_chains_sym(Z, N)
        atom_V_full_sym(Z, N) -> (V0, V1) sympy
        vertex_volume_sym(chain), _chain_V_full_sym(chain),
        _vertex_channels_sym(chain) -> (lam_sym, V_std, lam_alt)

    Φ_1 (mass-tower log)
        compute_phi1_full_sym(Z, N) -> sympy expression
        _phi1_from_ordering_sym(ordering) -> sympy expression

    Final-step substitution (mpmath, 50 dps)
        evalf_at_q0(expr, dps=50) -> mpmath.mpf
        as_polynomial_in_q(expr) -> sympy.Poly (when possible)

The module is **strictly additive**: it does not modify
``hecke_core.py``.  Numerical results computed by ``hecke_core``
(early-q_0) and ``hecke_core_symbolic`` (late-q_0) should agree
within the floating-point precision of the former; the symbolic
path additionally exposes the closed form polynomial in q.

Limits / what's still open:
  * The α_EM / Chern-Simons block in ``hecke_core`` lines 86-117
    mixes ``π²`` (transcendental) with q-integer arithmetic.  We
    *could* keep π symbolic too, but the Gram-determinant ratio is
    non-polynomial — it lives in ``ℚ(q, π²)``.  We therefore offer
    a symbolic helper ``alpha_em_inv_sym()`` returning an
    expression in (q, π).
  * ``z = q³/(q²+1)`` (**convention D**) is a rational function of q,
    so nothing here leaves ``ℚ(q)`` on account of z.  Under the excised
    convention C, ``z = 1/(q^{1/2} + q^{-1/2})`` introduced ``√q`` and the
    expression lived in ``ℤ[q^{±1/2}]`` after rationalisation; that branch
    is gone.
  * Fractions in ``hm`` arise from ``-h/2`` for mixed
    quark/inter-nucleon crossings.  Sympy handles ``Rational(1, 2)``
    natively, so coefficients land in ``ℚ[q^{±1}]``.

Reference: prop:mass-endomorphism-tower, thm:wedderburn-mass-formula
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from typing import Iterable, Sequence

import sympy as sp
import mpmath as mp

from q_parameter import q_at  # final-step substitution only


# ══════════════════════════════════════════════════════════════
# Symbolic primitives — q is a sympy.Symbol throughout
# ══════════════════════════════════════════════════════════════

q = sp.Symbol("q", positive=True)
q_inv = 1 / q

# h = q - q⁻¹  (symbolic)
h = q - q_inv

# z = q³/(q²+1) — **convention D** (owner ruling 2026-08-15, reaffirmed
# 2026-08-23).  Was convention C, z = 1/(√q + 1/√q) = √q/(q+1), excised.
#
# This module is the symbolic mirror of pyhecke.gram / hecke_core, and
# `pyhecke/gram.py` has carried convention D since 2026-08-15 — its own banner
# records that the change moves z by +22.70% and is NOT value-preserving.  The
# mirror was left on C, so its `TR_M_SYM` Markov-trace weights disagreed with
# the module they mirror by +22.70% at length 1, +50.6% at length 2 and +84.7%
# at length 3.  That is a frame straddle, not a convention preference.
#
# Under D, z is rational in q, so the ℚ[q^{±1/2}] half-power branch that C
# forced does not arise here at all.  The module-level `sqrt_q = sp.sqrt(q)`
# is DELETED rather than kept: z was its only consumer in this file, it is not
# part of the public surface listed in the module docstring, and no importer
# reads it.  Leaving it would advertise a half-power branch that no longer
# exists.
z = q ** 3 / (q ** 2 + 1)

# [2]_q, [n]_q
two_q = q + q_inv

ONE = sp.Integer(1)
HALF = sp.Rational(1, 2)


def q_int_sym(n: int) -> sp.Expr:
    """Symbolic quantum integer [n]_q = (q^n - q^{-n})/(q - q^{-1}).

    Returns a polynomial in (q, q⁻¹).  ``simplify`` is intentionally
    skipped to keep the expression cheap; downstream callers may
    invoke ``sp.together`` or ``sp.cancel`` if a normal form is
    needed before substitution.
    """
    return (q**n - q**(-n)) / h


# Wedderburn-Artin weights for H_3(q): w_λ = dim_q(λ)² / [3]_q!
# Closed form (matches pyhecke.gram lines 37-41):
#   w_sym = q² / (q⁴ + 4q² + 1)
#   w_std = (q² + 1)² / (q⁴ + 4q² + 1)
#   w_alt = q² / (q⁴ + 4q² + 1)
_q2 = q**2
_denom_w = _q2**2 + 4 * _q2 + 1
w_sym = _q2 / _denom_w
w_std = (_q2 + 1) ** 2 / _denom_w
w_alt = _q2 / _denom_w


# ══════════════════════════════════════════════════════════════
# NF basis (same as pyhecke.gram), Markov trace weights symbolic
# ══════════════════════════════════════════════════════════════

NF_BASIS: list[tuple[int, ...]] = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES: list[str] = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]

# TR_M weights — symbolic via z.  Word lengths 0,1,1,2,2,3.
TR_M_SYM: list[sp.Expr] = [ONE, z, z, z**2, z**2, z**3]

INV_TREFOIL_G0_SYM = [(ONE, -h), (ONE, -h)]  # σ₀⁻¹σ₀⁻¹
INV_TREFOIL_G1_SYM = [(ONE, -h)]              # σ₁⁻¹


# ══════════════════════════════════════════════════════════════
# NF multiplication — symbolic mirror of pyhecke.gram.hm
# ══════════════════════════════════════════════════════════════

def hm_sym(nf: Sequence[sp.Expr], c: sp.Expr, d: sp.Expr, gen: int) -> list[sp.Expr]:
    """Multiply NF element by (c·σ_gen + d·I) symbolically.

    Mirrors ``pyhecke.gram.hm`` line-for-line, but every coefficient
    stays in ``ℚ[q^{±1}]``.  (The tables below use only ``h``, ``c`` and
    ``d`` — z does not enter this function in either convention.)
    Returns a 6-element list of sympy expressions.
    """
    r = [sp.Integer(0)] * 6
    if gen == 0:
        tables = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * h), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * h), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * h), (4, c), (5, d)]),
        ]
    else:
        tables = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * h), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * h), (1, c), (4, d)]),
            (5, [(5, c * h), (3, c), (5, d)]),
        ]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] = r[ti] + nf[si] * co
    return r


def nf_tr_sym(nf: Sequence[sp.Expr]) -> sp.Expr:
    """Markov trace of a symbolic NF vector."""
    return sum(nf[i] * TR_M_SYM[i] for i in range(6))


def nf_net_sym(nf: Sequence[sp.Expr]) -> sp.Expr:
    """Net (sum of NF coefficients) — symbolic."""
    return sum(nf)


# ══════════════════════════════════════════════════════════════
# Per-generator chains — pure structural ports of hecke_core
# ══════════════════════════════════════════════════════════════

def _proton_chains_sym() -> tuple[list[tuple[sp.Expr, sp.Expr]], list[tuple[sp.Expr, sp.Expr]]]:
    """Per-generator (g0, g1) chains for one proton.  Coefficients
    are sympy expressions in q."""
    g0: list[tuple[sp.Expr, sp.Expr]] = [(ONE, sp.Integer(0))] * 3
    g1: list[tuple[sp.Expr, sp.Expr]] = [(ONE, -h)] * 3
    # Quark crossings: (0,1)=uu→σ₀, (0,2)=ud→mixed, (1,2)=ud→mixed
    g0.append((ONE, sp.Integer(0)))    # uu
    g0.append((ONE, -h * HALF))        # ud mixed on gen 0
    g1.append((ONE, -h * HALF))        # ud mixed on gen 1
    # Gluon self-coupling: 2 σ₀
    g0.append((ONE, sp.Integer(0)))
    g0.append((ONE, sp.Integer(0)))
    return g0, g1


def _neutron_chains_sym() -> tuple[list[tuple[sp.Expr, sp.Expr]], list[tuple[sp.Expr, sp.Expr]]]:
    """Per-generator (g0, g1) chains for one neutron."""
    g0: list[tuple[sp.Expr, sp.Expr]] = [(ONE, sp.Integer(0))] * 3
    g1: list[tuple[sp.Expr, sp.Expr]] = [(ONE, -h)] * 3
    # Quark crossings: (0,1)=ud→mixed, (0,2)=ud→mixed, (1,2)=dd→σ⁻¹
    g0.append((ONE, -h * HALF))
    g0.append((ONE, -h * HALF))
    g1.append((ONE, -h))
    # Gluon self-coupling
    g0.append((ONE, sp.Integer(0)))
    g0.append((ONE, sp.Integer(0)))
    return g0, g1


_PROTON_G0_SYM, _PROTON_G1_SYM = _proton_chains_sym()
_NEUTRON_G0_SYM, _NEUTRON_G1_SYM = _neutron_chains_sym()


def _ground_state_ordering(Z: int, N: int) -> list[str]:
    """Match hecke_core.build_atom_nf — interleaved p/n ordering."""
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append("p"); pc += 1
        else:
            ordering.append("n"); nc += 1
    return ordering


def atom_gen_chains_sym(Z: int, N: int):
    """Per-generator chains for atom (Z, N), symbolic.

    Mirrors ``hecke_core.atom_gen_chains`` exactly: nucleon
    chains in ground-state order, inter-nucleon σ₀ on gen 0, then
    Z electrons each contributing (1, -h) to gen 1.
    """
    g0: list[tuple[sp.Expr, sp.Expr]] = []
    g1: list[tuple[sp.Expr, sp.Expr]] = []
    ordering = _ground_state_ordering(Z, N)

    for k, kind in enumerate(ordering):
        if kind == "p":
            g0.extend(_PROTON_G0_SYM)
            g1.extend(_PROTON_G1_SYM)
        else:
            g0.extend(_NEUTRON_G0_SYM)
            g1.extend(_NEUTRON_G1_SYM)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                g0.append((ONE, sp.Integer(0)))
            elif ti == "n" and tj == "n":
                g0.append((ONE, -h))
            else:
                g0.append((ONE, -h * HALF))

    for _ in range(Z):
        g1.append((ONE, -h))

    return g0, g1


# ══════════════════════════════════════════════════════════════
# Symbolic Wedderburn channel evaluators
# ══════════════════════════════════════════════════════════════

def _vertex_channels_sym(chain: Iterable[tuple[sp.Expr, sp.Expr]]):
    """Return (λ_sym, V_std, λ_alt) symbolically for a crossing chain.

    Mirrors ``hecke_core._vertex_channels`` — but nothing is f64.
    The transfer matrix runs in ``ℚ(q)`` — including where z appears,
    since convention D's ``z = q³/(q²+1)`` is rational in q.  Under the
    excised convention C this dropped to the field of fractions of
    ``ℤ[q^{±1/2}]``.
    """
    a = sp.Integer(0)
    b = sp.Integer(1)
    sp_chan = sp.Integer(1)   # symmetric channel running product
    ap_chan = sp.Integer(1)   # alternating channel running product
    for c, d in chain:
        a, b = a * c * h + a * d + b * c, a * c + b * d
        sp_chan = sp_chan * (c * q + d)
        ap_chan = ap_chan * (-c * q_inv + d)
    V_std = z * a + b
    return sp_chan, V_std, ap_chan


def _chain_V_full_sym(chain: Iterable[tuple[sp.Expr, sp.Expr]]) -> sp.Expr:
    """Wedderburn-weighted traced volume of a crossing chain.

    Mirror of ``hecke_core._chain_V_full`` with sympy arithmetic.
    """
    s, v, a = _vertex_channels_sym(chain)
    return w_sym * s + w_std * v + w_alt * a


def vertex_volume_sym(chain: Iterable[tuple[sp.Expr, sp.Expr]]) -> sp.Expr:
    """Public alias preserving the API of ``hecke_core.vertex_volume``."""
    return _chain_V_full_sym(chain)


def atom_V_full_sym(Z: int, N: int) -> tuple[sp.Expr, sp.Expr]:
    """Symbolic per-generator V̂_i^full for atom (Z, N).

    Returns (V0, V1) as sympy expressions.  Substitute via
    :func:`evalf_at_q0` only when emitting the witness number.
    """
    g0, g1 = atom_gen_chains_sym(Z, N)
    return _chain_V_full_sym(g0), _chain_V_full_sym(g1)


# ══════════════════════════════════════════════════════════════
# build_atom_nf — symbolic NF coefficients
# ══════════════════════════════════════════════════════════════

def build_atom_nf_sym(Z: int, N: int) -> list[sp.Expr]:
    """Symbolic mirror of ``hecke_core.build_atom_nf``.

    Returns a 6-element NF vector with coefficients in
    ``ℚ(q, √q)``.  Use ``evalf_at_q0`` per-component to obtain
    f64/mpmath numerical values at the end.
    """
    A = Z + N
    if A == 0:
        return [ONE, sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0)]

    ordering = _ground_state_ordering(Z, N)
    nf: list[sp.Expr] = [ONE, sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.Integer(0)]

    for k in range(A):
        kind = ordering[k]
        if kind == "p":
            for _ in range(3):
                nf = hm_sym(nf, ONE, sp.Integer(0), 0)   # σ₀
                nf = hm_sym(nf, ONE, -h, 1)              # σ₁⁻¹
            nf = hm_sym(nf, ONE, sp.Integer(0), 0)       # uu
            nf = hm_sym(nf, ONE, -h * HALF, 0)           # ud mixed
            nf = hm_sym(nf, ONE, -h * HALF, 1)           # ud mixed
            nf = hm_sym(nf, ONE, sp.Integer(0), 0)       # gluon 1
            nf = hm_sym(nf, ONE, sp.Integer(0), 0)       # gluon 2
        else:
            for _ in range(3):
                nf = hm_sym(nf, ONE, sp.Integer(0), 0)
                nf = hm_sym(nf, ONE, -h, 1)
            nf = hm_sym(nf, ONE, -h * HALF, 0)
            nf = hm_sym(nf, ONE, -h * HALF, 0)
            nf = hm_sym(nf, ONE, -h, 1)
            nf = hm_sym(nf, ONE, sp.Integer(0), 0)
            nf = hm_sym(nf, ONE, sp.Integer(0), 0)

        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == "p" and tj == "p":
                nf = hm_sym(nf, ONE, sp.Integer(0), 0)
            elif ti == "n" and tj == "n":
                nf = hm_sym(nf, ONE, -h, 0)
            else:
                nf = hm_sym(nf, ONE, -h * HALF, 0)

    for _ in range(Z):
        nf = hm_sym(nf, ONE, -h, 1)

    return nf


# ══════════════════════════════════════════════════════════════
# Φ₁ from a strand ordering — kept structurally faithful but
# symbolic until the final |·| / log step.
# ══════════════════════════════════════════════════════════════

def _crossing_coeff_sym(ti: str, tj: str):
    """Mirror of ``hecke_core._crossing_coeff`` returning sympy d."""
    if ti == "p" and tj == "p":
        return sp.Integer(0)
    if ti == "n" and tj == "n":
        return -h
    if (ti, tj) in (("p", "n"), ("n", "p")):
        return -h * HALF
    if (ti, tj) in (("p", "e"), ("e", "p")):
        return -h
    if ti == "e" and tj == "e":
        return sp.Integer(0)
    return None


def _phi1_from_ordering_sym(ordering: Sequence[str], dps: int = 50) -> mp.mpf:
    """Symbolic V̂_i computation, mpmath log at the very end.

    Mirrors ``hecke_core._phi1_from_ordering`` step-for-step except
    that the transfer matrix is built symbolically and only
    substituted at the |V̂_i| step.  This avoids the early-q_0
    cancellation noise on the standard-rep determinant.
    """
    n = len(ordering)
    if n <= 1:
        return mp.mpf(0)

    phi = mp.mpf(0)
    for i in range(n - 1):
        M00, M01, M10, M11 = ONE, sp.Integer(0), sp.Integer(0), ONE
        for j in range(i + 1, n):
            d = _crossing_coeff_sym(ordering[i], ordering[j])
            if d is None:
                continue
            t00, t01, t10, t11 = h + d, ONE, ONE, d
            n00 = M00 * t00 + M01 * t10
            n01 = M00 * t01 + M01 * t11
            n10 = M10 * t00 + M11 * t10
            n11 = M10 * t01 + M11 * t11
            M00, M01, M10, M11 = n00, n01, n10, n11
        V_sym = z * M10 + M11
        V_num = evalf_at_q0(V_sym, dps=dps)
        if abs(V_num) > mp.mpf(f"1e-{dps - 5}"):
            phi += mp.log(abs(V_num))
    return phi


def _alternating_ordering_sym(Z: int, N: int) -> list[str]:
    """Mirror of ``hecke_core._alternating_ordering``."""
    ordering = []
    pi, ni = 0, 0
    for k in range(Z + N):
        if pi < Z and (ni >= N or k % 2 == 0):
            ordering.append("p"); pi += 1
        else:
            ordering.append("n"); ni += 1
    return ordering


def compute_phi1_full_sym(Z: int, N: int, dps: int = 50) -> mp.mpf:
    """Symbolic mirror of ``hecke_core.compute_phi1_full`` (no Rust path).

    A==2 dedicated formula (``B(D) = α × V̂_e``) is reproduced with
    α = M_E_MEV × 8·G  (where G is Catalan).  The trefoil's V̂_e
    stays symbolic until the final magnitude.
    """
    A = Z + N
    if A <= 1 and Z == 0:
        return mp.mpf(0)

    if A == 2:
        # Trefoil σ_1^3 on 2 strands → 3 crossings (c=1,d=0) on gen 0.
        chain = [(ONE, sp.Integer(0))] * 3
        # V_e = w_sym q^3 + w_std (z·M00+M10) + w_alt (-q^{-1})^3
        # but we route through _chain_V_full_sym for the std block.
        V_e_sym = _chain_V_full_sym(chain)
        # Catalan + Borromean scale (numerical at the end). Both M_E_MEV
        # and CATALAN imported from experimental_constants per Gemini review
        # on PR #515 (centralized-constants rule).
        from experimental_constants import M_E_MEV, CATALAN  # type: ignore
        alpha = mp.mpf(M_E_MEV) * 8 * mp.mpf(CATALAN)
        V_num = evalf_at_q0(V_e_sym, dps=dps)
        return alpha * abs(V_num)

    ordering = _alternating_ordering_sym(Z, N) + ["e"] * Z
    return _phi1_from_ordering_sym(ordering, dps=dps)


# ══════════════════════════════════════════════════════════════
# Final-step substitution helpers
# ══════════════════════════════════════════════════════════════

def evalf_at_q0(expr: sp.Expr, dps: int = 50) -> mp.mpf:
    """Substitute q ← q_0 (CODATA-anchored) and evaluate at ``dps``
    mpmath digits.  This is the **only** place a numerical q value
    enters the symbolic pipeline.

    Returns ``mpmath.mpf``; complex outputs raise ``ValueError``.
    """
    if isinstance(expr, (int, float, sp.Integer, sp.Float, sp.Rational)):
        return mp.mpf(sp.Float(expr, dps))
    with mp.workdps(dps + 5):
        q0_mp = q_at(dps + 5)
        # sympy → mpmath at the requested precision.  Use
        # expr.evalf(dps, subs={...}) — fused substitution + evaluation
        # avoids materialising the full symbolic tree under .subs() first
        # (per Gemini review on PR #511).
        out = expr.evalf(dps + 5, subs={q: sp.Float(q0_mp, dps + 5)})
        if not out.is_real:
            raise ValueError(f"evalf_at_q0: expected real, got {out}")
        return mp.mpf(str(out))


def evalf_vector_at_q0(vec: Sequence[sp.Expr], dps: int = 50) -> list[mp.mpf]:
    """Apply :func:`evalf_at_q0` componentwise (e.g. NF vectors)."""
    return [evalf_at_q0(c, dps=dps) for c in vec]


def as_polynomial_in_q(expr: sp.Expr) -> sp.Expr:
    """Best-effort: rationalise (clear ``√q``, common denominators) and
    return the resulting Laurent polynomial in q.

    Returns a sympy expression; downstream tooling can call
    ``sp.Poly(result, q)`` if a Poly object is needed.
    """
    return sp.together(sp.expand(expr.rewrite(sp.Pow)))


# ══════════════════════════════════════════════════════════════
# α_EM — symbolic CS-corrected expression (still has π², kept
# transparent rather than being substituted away).
# ══════════════════════════════════════════════════════════════

def alpha_em_inv_sym(pi_sym: sp.Symbol | None = None) -> sp.Expr:
    """Symbolic CS-corrected 1/α_EM.

    Mirrors ``hecke_core`` lines 75-117: ``bare × (1 + c1 + c1²·κ)``
    where ``κ`` is the Gram-determinant ratio from the J²(Bring's
    surface) pairing.  ``π`` is a sympy symbol (default
    ``sp.pi``) so the closed form lives in ``ℚ(q, π)``.
    """
    pi = pi_sym if pi_sym is not None else sp.pi
    bare_inv = q * q_int_sym(9) * q_int_sym(10)
    CS_T29 = pi**2 * sp.Rational(10, 9)
    CS_T35 = pi**2 * sp.Rational(16, 15)
    hbar_q2 = (1 - q_inv) ** 2
    n2 = q_int_sym(2)
    c1 = (CS_T29 + CS_T35) * (n2 / 2) * hbar_q2 / bare_inv

    # Classical Gram (uses literal m,n integers; no q involved → cancels)
    sl = sp.Integer(8)
    linking = sp.Integer(17)
    G_cl_11 = CS_T29 + pi**2 * sl**2 / sp.Integer(18) ** 2
    G_cl_22 = CS_T35 + pi**2 * sl**2 / sp.Integer(15) ** 2
    G_cl_12 = pi**2 * linking**2 / (sp.Integer(18) * sp.Integer(15))
    det_G_cl = G_cl_11 * G_cl_22 - G_cl_12**2

    # q-deformed Gram (replace m,n → [m]_q, [n]_q)
    qi9 = q_int_sym(9)
    qi5 = q_int_sym(5)
    qi3 = q_int_sym(3)
    linking_q = sp.Abs(n2 * qi5 - qi3 * qi9)
    CS_q_29 = pi**2 * (n2**2 - 1) * (qi9**2 - 1) / (12 * n2 * qi9)
    CS_q_35 = pi**2 * (qi3**2 - 1) * (qi5**2 - 1) / (12 * qi3 * qi5)
    sl_q_29 = (n2 - 1) * (qi9 - 1)
    sl_q_35 = (qi3 - 1) * (qi5 - 1)
    G_q_11 = CS_q_29 + pi**2 * sl_q_29**2 / (n2 * qi9) ** 2
    G_q_22 = CS_q_35 + pi**2 * sl_q_35**2 / (qi3 * qi5) ** 2
    G_q_12 = pi**2 * linking_q**2 / (n2 * qi9 * qi3 * qi5)
    det_G_q = G_q_11 * G_q_22 - G_q_12**2

    kappa = det_G_cl / det_G_q
    return bare_inv * (1 + c1 + c1**2 * kappa)


def alpha_em_inv_sym_exact(pi_sym: sp.Symbol | None = None) -> sp.Expr:
    """Symbolic 1/α_EM with the CS tower summed EXACTLY (all orders).

    `alpha_em_inv_sym` above truncates the correction tower at order 2
    (``1 + c1 + c1²κ``). That tower is geometric —

        1 + Σ_{j≥1} c₁^j κ^{j−1}  =  1 + c₁/(1 − c₁κ)

    — so it admits a closed form with no order parameter at all. Expanding
    the closed form in ``c₁`` reproduces ``1 + c₁ + c₁²κ + c₁³κ² + …``, so
    the truncated version is its 3-term Taylor polynomial.

    At the substrate anchor ``c₁·κ ≈ 2.7e-3``, so the truncation costs
    ≈ 11.06 ppb. Prefer this function wherever the result feeds a ppb- or
    ppq-level claim. Lives in ℚ(q, π) exactly as the truncated form does.
    """
    pi = pi_sym if pi_sym is not None else sp.pi
    bare_inv = q * q_int_sym(9) * q_int_sym(10)
    CS_T29 = pi**2 * sp.Rational(10, 9)
    CS_T35 = pi**2 * sp.Rational(16, 15)
    hbar_q2 = (1 - q_inv) ** 2
    n2 = q_int_sym(2)
    c1 = (CS_T29 + CS_T35) * (n2 / 2) * hbar_q2 / bare_inv

    sl = sp.Integer(8)
    linking = sp.Integer(17)
    G_cl_11 = CS_T29 + pi**2 * sl**2 / sp.Integer(18) ** 2
    G_cl_22 = CS_T35 + pi**2 * sl**2 / sp.Integer(15) ** 2
    G_cl_12 = pi**2 * linking**2 / (sp.Integer(18) * sp.Integer(15))
    det_G_cl = G_cl_11 * G_cl_22 - G_cl_12**2

    qi9, qi5, qi3 = q_int_sym(9), q_int_sym(5), q_int_sym(3)
    linking_q = sp.Abs(n2 * qi5 - qi3 * qi9)
    CS_q_29 = pi**2 * (n2**2 - 1) * (qi9**2 - 1) / (12 * n2 * qi9)
    CS_q_35 = pi**2 * (qi3**2 - 1) * (qi5**2 - 1) / (12 * qi3 * qi5)
    sl_q_29 = (n2 - 1) * (qi9 - 1)
    sl_q_35 = (qi3 - 1) * (qi5 - 1)
    G_q_11 = CS_q_29 + pi**2 * sl_q_29**2 / (n2 * qi9) ** 2
    G_q_22 = CS_q_35 + pi**2 * sl_q_35**2 / (qi3 * qi5) ** 2
    G_q_12 = pi**2 * linking_q**2 / (n2 * qi9 * qi3 * qi5)
    det_G_q = G_q_11 * G_q_22 - G_q_12**2

    kappa = det_G_cl / det_G_q
    return bare_inv * (1 + c1 / (1 - c1 * kappa))


# ══════════════════════════════════════════════════════════════
# Module self-test
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":  # pragma: no cover
    print("hecke_core_symbolic — quick self-test")
    print("  q          =", q)
    print("  h = q-q⁻¹  =", h)
    print("  z          =", z)
    print("  w_sym      =", sp.simplify(w_sym))
    print("  w_std      =", sp.simplify(w_std))
    print("  w_alt      =", sp.simplify(w_alt))
    print("  [3]_q      =", sp.expand(q_int_sym(3)))

    nf_p = build_atom_nf_sym(1, 0)
    print("  NF(p)      =", [sp.simplify(c) for c in nf_p])

    V0, V1 = atom_V_full_sym(1, 0)
    print("  V_full(p)0 =", evalf_at_q0(V0, dps=50))
    print("  V_full(p)1 =", evalf_at_q0(V1, dps=50))
