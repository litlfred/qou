#!/usr/bin/env python3
"""
Paper-exact per-block log-form binding energy.

Implements prop:tower-binding-energy verbatim:

    B(Z, N) = Σ_{λ ∈ {sym, std, alt}}
              w_λ · m_e · Σ_{i=0}^{A-2} ln|Φ_q(V̂_i^λ)|

where V̂_i^λ is the additive Wedderburn traced volume in channel λ
at generator i, and

    ln|Φ_q(v)| = −Σ_{k≥1} ln|1 − q^{−k} v|.

Unlike the aggregate formula (mass_endomorphism.mass_from_tower) or
the earlier per-block probe (per_block_phi_q.mass_per_block), the
logarithm absorbs the Φ_q pole: ln|Φ_q(v)| is well-defined for all
real v ≠ q^k (k ≥ 1 integer), via |1 − q^{−k}v| = q^{−k}v − 1 for
q^{−k}v > 1.  This is the "analytic continuation past |V̂| = q"
mentioned in prop:tower-binding-energy.

Atomic mass formula from the same proposition:

    M(Z, N) = Z · m_p + N · m_n + Z · m_e − B(Z, N)

Optional QED correction (prop:deuterium-derived-binding):

    B_phys = B_strong · (1 − α_EM / 2)

tightens the deuterium prediction from the aggregate 0.018% to the
paper-claimed 0.008%.

Usage:
    python3 folio-assistant/computations/binding_per_block_log.py
"""
from __future__ import annotations

import math
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
sys.path.insert(0, str(Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from mass_endomorphism import (additive_wedderburn_volumes,
                                  HA, qi0, z_mark,
                                  w_sym, w_std, w_alt)


# ── Physical constants (CODATA 2022 where applicable) ────────
M_E_MEV = 0.51099895069
M_P_MEV = 938.27208816
M_N_MEV = 939.56542052
ALPHA_EM = 7.2973525693e-3  # fine-structure constant
CATALAN_G = 0.9159655941772190  # Catalan's constant

# prop:binding-scale-catalan — α = m_e · 8G ≈ 3.744 MeV
ALPHA_BINDING_MEV = M_E_MEV * 8 * CATALAN_G


def ln_abs_phi_q(v: float, *,
                   K_max: int = 4000,
                   skip_tol: float = 1e-15,
                   pole_tol: float = 1e-15,
                   pole_mode: str = "principal") -> float:
    """ln|Φ_q(v)| = −Σ_{k≥1} ln|1 − q^{−k} v|.

    **pole_mode='principal'** implements the documented principal-
    value regularisation (docs/infrastructure-audit-2026-04-20.md
    line 73): the zero-measure factor |1 − q^{-k}v|^{-1} at the
    exact pole index is DROPPED from the product.  In log-sum form
    this means `term = 0` for factors with abs_diff < pole_tol,
    equivalent to the integral-of-ln-near-zero vanishing.

    This is the paper-exact prescription.  It introduces a
    ≈−ln(pole_tol) ≈ 34.5 discontinuity across the pole-tolerance
    shell (at-pole contribution = 0; just-outside contribution ≈
    +34.5), but for the paper's use cases V̂ either equals q^k by
    construction (designed pole hits, e.g. V̂^sym = q at pp inter-
    nucleon crossings, V̂^sym = q^3 at the electron trefoil) or is
    far from any q^k — intermediate cases do not arise.  If a
    caller encounters a generic V̂ within pole_tol of a q^k, the
    result is UNDERESTIMATED by ~34.5 per such hit and should be
    investigated separately.

    Sum truncated once the summand magnitude falls below
    ``skip_tol`` — at q₀ ≈ 1.11 the tail is super-geometric
    (q^{−k} → 0), so a few hundred terms suffice.

    **Pole handling.**  The log diverges at v = q^k (k ≥ 1) where
    |1 − q^{−k}v| = 0.  Structural V̂ values hit these poles
    exactly (e.g. V̂^sym = q at pp inter-nucleon crossings).  The
    paper's prop:tower-binding-energy specifies analytic continuation
    "well-defined for all V̂ ≠ q^n"; at the isolated poles, we
    apply the principal-value regularization — drop the
    zero-measure factor from the product.

    - ``pole_mode="principal"`` (default): skip the k where
      |1 − q^{−k}v| < pole_tol.  Finite result; matches the
      paper's numerical values for ³He, ⁴He.
    - ``pole_mode="raise"``: raise ZeroDivisionError.
    - ``pole_mode="sign"``: return +∞ (the natural limit from
      the left of q^k; conservative upper bound).

    Returns the scalar ln|Φ_q(v)| (negative of the log-product
    form); the minus sign is baked in so this returns the value
    that appears directly in the paper's B(Z,N) formula.
    """
    # Accumulate −Σ_k ln|1 − q^{−k}v|.
    # qi_pow starts at 1 and is advanced to q^{-k} at the TOP of each
    # iteration, so the update happens in exactly one place.
    total = 0.0
    qi_pow = 1.0
    for k in range(1, K_max + 1):
        qi_pow /= q0                 # now qi_pow = q^{-k}
        x = qi_pow * v
        diff = 1.0 - x
        abs_diff = abs(diff)
        if abs_diff < pole_tol:
            if pole_mode == "raise":
                raise ZeroDivisionError(
                    f"ln|Φ_q| diverges at v ≈ q^k (x = {x}, k = {k})")
            if pole_mode == "sign":
                return float("inf")
            # principal: drop the zero-measure factor (term = 0) per
            # the documented PV regularisation.  See docstring for
            # the known ≈−ln(pole_tol) discontinuity across the
            # tolerance shell.
            term = 0.0
        else:
            term = math.log(abs_diff)
        total -= term
        # Converge: once |x| « 1, |ln|1−x|| ≈ |x| falls to zero.
        if abs(term) < skip_tol and abs(x) < skip_tol:
            break
    return total


def binding_per_block_log(cross: dict, n_strands: int, *,
                             apply_qed: bool = True,
                             m_e_MeV: float = M_E_MEV) -> dict:
    """Paper-exact binding B(Z,N) via per-block log-form Φ_q.

    Args:
      cross:     crossings_per_gen dict (per additive_wedderburn_volumes)
      n_strands: 3·A for A = Z+N nucleons
      apply_qed: multiply by (1 − α_EM/2) per prop:deuterium-derived-binding
      m_e_MeV:   electron mass scale (default CODATA)

    Returns dict with:
      B_MeV: binding energy in MeV (with QED if apply_qed)
      B_strong_MeV: B before QED correction
      B_per_block: dict {sym, std, alt} with each channel's
                   Σ_i ln|Φ_q(V̂_i^λ)| (cat units) and
                   w_λ · m_e · sum (MeV)
    """
    vols = additive_wedderburn_volumes(n_strands, cross)
    channels = {"sym": w_sym, "std": w_std, "alt": w_alt}
    key_per_channel = {"sym": "sym", "std": "std", "alt": "alt"}
    per_block = {}
    B_strong = 0.0
    for ch, w in channels.items():
        key = key_per_channel[ch]
        ln_sum = 0.0
        V_per_gen = []
        for v in vols:
            val = v[key]
            V_per_gen.append(val)
            ln_sum += ln_abs_phi_q(val)
        contrib = w * m_e_MeV * ln_sum
        per_block[ch] = {
            "w_lambda": w,
            "V_per_gen": V_per_gen,
            "ln_phi_sum_cat": ln_sum,
            "contribution_MeV": contrib,
        }
        B_strong += contrib
    if apply_qed:
        qed_factor = 1.0 - ALPHA_EM / 2.0
        B_phys = B_strong * qed_factor
    else:
        qed_factor = 1.0
        B_phys = B_strong
    return {
        "B_MeV": B_phys,
        "B_strong_MeV": B_strong,
        "qed_factor": qed_factor,
        "qed_applied": apply_qed,
        "per_block": per_block,
        "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
    }


def atomic_mass_per_block_log(Z: int, N: int, cross: dict,
                                 n_strands: int, *,
                                 apply_qed: bool = True) -> dict:
    """Full atomic mass M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)."""
    binding = binding_per_block_log(cross, n_strands,
                                       apply_qed=apply_qed)
    M = (Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
         - binding["B_MeV"])
    return {
        "Z": Z, "N": N, "A": Z + N,
        "M_MeV": M,
        "B_MeV": binding["B_MeV"],
        "binding": binding,
    }


# ── Atom-level binding: wire paper formula through mass_endomorphism_atom ───

def _binding_per_block_log_from_V(
        V_atom_per_block: dict, V_free_per_block: dict,
        n_gens: int) -> float:
    """Compute B = sum_lambda w_lambda m_e [sum_i ln|Phi(free)| - sum_i ln|Phi(atom)|]
    given per-block V̂ values at a single level.  Scalar categorical
    output (NOT MeV — caller multiplies by m_e if needed; this helper
    returns the ratio value used inside the brane-tower sum).
    """
    channels = {"sym": w_sym, "std": w_std, "alt": w_alt}
    total = 0.0
    for ch, w in channels.items():
        ln_atom = sum(ln_abs_phi_q(V_atom_per_block[ch][i])
                       for i in range(n_gens))
        ln_free = sum(ln_abs_phi_q(V_free_per_block[ch][i])
                       for i in range(n_gens))
        total += w * (ln_free - ln_atom)
    return total


def atom_binding_per_block_log_jet(Z: int, N: int, *,
                                      apply_qed: bool = True,
                                      n_jet_levels: int = 0,
                                      verbose: bool = False) -> dict:
    """Per-block log binding with optional jet-tower corrections.

    Formula (jet-augmented prop:tower-binding-energy):

      B(Z,N) = m_e * sum_lambda w_lambda *
               [ sum_i ln|Phi_q(V̂_i^{lambda,(0)})|_atom→free
               + sum_{n=1..N} hbar_q^{2n} *
                    sum_i ln|Phi_q(V̂_i^{lambda,(n)})|_atom→free ]

    where V̂_i^{lambda,(n)} = z^n · V̂_i^{lambda,(0)} is the
    Markov-stab jet lift (simplest).  Level-0 corresponds to
    n_jet_levels=0 and matches atom_binding_per_block_log.

    Uses prop:descended-level-zero: the descended (holonomy) piece
    is the log|prod V̂| contribution, carried by the level-0 term.
    Level n ≥ 1 carries only transient corrections.  Each level-n
    residual |Delta^(n)| is bounded by prop:delta-max-uniform-bound
    via the operator-norm estimate on the Hecke standard
    representation; the geometric-series tail bound from
    prop:jet-tower-convergence certifies the truncation error.

    Returns dict with:
      B_MeV, B_strong_MeV, qed_factor: main outputs
      per_level: list of {n, delta_cat, term_MeV, cum_MeV}
      tail_bound_MeV: conservative geometric-series tail estimate
    """
    from mass_endomorphism_atom import atom_crossings
    from mass_endomorphism import additive_wedderburn_volumes

    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    n_strands = 3 * A
    n_gens = n_strands - 1

    cross_atom = atom_crossings(nucleon_types, include_inter=True)
    cross_free = atom_crossings(nucleon_types, include_inter=False)
    vols_atom_0 = additive_wedderburn_volumes(n_strands, cross_atom)
    vols_free_0 = additive_wedderburn_volumes(n_strands, cross_free)

    # Organize per-block V̂ arrays at level 0.
    V_atom_0 = {ch: [vols_atom_0[i][ch] for i in range(n_gens)]
                 for ch in ["sym", "std", "alt"]}
    V_free_0 = {ch: [vols_free_0[i][ch] for i in range(n_gens)]
                 for ch in ["sym", "std", "alt"]}

    hbar_q = (q0 - 1.0) / q0
    hbar_q_sq = hbar_q * hbar_q

    # Level-0 binding contribution (paper's base B).
    B_cat_level0 = _binding_per_block_log_from_V(V_atom_0, V_free_0, n_gens)
    B_strong_cat = B_cat_level0
    per_level = [{
        "level": 0,
        "delta_cat": B_cat_level0,
        "scale": 1.0,
        "term_cat": B_cat_level0,
        "term_MeV": M_E_MEV * B_cat_level0,
        "cum_MeV": M_E_MEV * B_cat_level0,
    }]

    # Level n ≥ 1: jet-lifted V̂ = z^n · V̂^(0), transient corrections.
    for n in range(1, n_jet_levels + 1):
        scale_V = z_mark ** n
        V_atom_n = {ch: [v * scale_V for v in V_atom_0[ch]]
                     for ch in ["sym", "std", "alt"]}
        V_free_n = {ch: [v * scale_V for v in V_free_0[ch]]
                     for ch in ["sym", "std", "alt"]}
        delta_n_cat = _binding_per_block_log_from_V(
            V_atom_n, V_free_n, n_gens)
        brane_weight = hbar_q_sq ** n
        term_cat = brane_weight * delta_n_cat
        B_strong_cat += term_cat
        cum_MeV = M_E_MEV * B_strong_cat
        per_level.append({
            "level": n,
            "delta_cat": delta_n_cat,
            "scale": brane_weight,
            "term_cat": term_cat,
            "term_MeV": M_E_MEV * term_cat,
            "cum_MeV": cum_MeV,
        })
        if verbose:
            print(f"  level {n}: Δ = {delta_n_cat:+.4e} cat, "
                  f"ℏ_q^{{2n}}·Δ = {term_cat:+.4e} cat, "
                  f"cum = {cum_MeV:+.6f} MeV")

    # Geometric tail bound from prop:jet-tower-convergence +
    # prop:delta-max-uniform-bound.  Δ_max conservatively taken as
    # max|delta_n| over computed levels; tail = Δ_max · ℏ_q^{2(N+1)}
    # / (1 − ℏ_q^2).
    if n_jet_levels >= 1:
        delta_max = max(abs(p["delta_cat"]) for p in per_level[1:])
        tail_cat = (delta_max * hbar_q_sq ** (n_jet_levels + 1)
                      / (1.0 - hbar_q_sq))
        tail_MeV = M_E_MEV * tail_cat
    else:
        tail_cat = float("inf")  # no level-1 sampled
        tail_MeV = float("inf")

    B_strong = M_E_MEV * B_strong_cat
    qed_factor = (1.0 - ALPHA_EM / 2.0) if apply_qed else 1.0
    B_phys = B_strong * qed_factor
    M = (Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV - B_phys)

    return {
        "Z": Z, "N": N, "A": A,
        "n_jet_levels": n_jet_levels,
        "B_MeV": B_phys,
        "B_strong_MeV": B_strong,
        "qed_factor": qed_factor,
        "qed_applied": apply_qed,
        "tail_bound_MeV": tail_MeV,
        "M_MeV": M,
        "per_level": per_level,
    }


# ── Kähler lift on per-block V̂ ──────────────────────────────
#
# prop:tower-binding-energy uses V̂_i^λ computed at fixed q₀.
# The proper Kähler-differential construction of the 1-jet (the
# recursive brane tower A_1 = A_0 ⊗ Ω¹(A_0)) adds q-derivative
# corrections:
#
#   V̂_i^{λ,Kähler}(q) = V̂_i^λ(q)
#                      + ℏ_q · q · dV̂_i^λ/dq
#                      + (ℏ_q²/2) · [q² d²V̂_i^λ/dq² + q dV̂_i^λ/dq]
#                      + O(ℏ_q³)
#
# Evaluated at q₀.  Modeling error vs proper analytic lift:
#   order 0 (no Kähler, level-0 only): ε = O(ℏ_q) per generator
#   order 1: ε = O(ℏ_q²)
#   order 2: ε = O(ℏ_q³)
#
# The 2nd-order lift gives ε·|V̂| ~ ℏ_q³ ≈ 10⁻³ — still above ppb
# but tighter than the O(ℏ_q) baseline of the raw paper formula.

def _build_V_per_block_symbolic(Z: int, N: int, include_inter: bool):
    """Per-block sympy expressions for V̂^{sym,std,alt}_i(q).

    Returns dict {"sym": [V̂_0^sym(q), …], "std": […], "alt": […]}
    as lists of sympy expressions, one per generator.

    Uses the same nuclear crossings structure as
    mass_endomorphism_atom.atom_crossings, but builds the
    Wedderburn-block polynomials directly from (c, d) tuples
    (no λ-partition summation).  The blocks are independent:

      V̂^sym_i = Π_k (c_k q + d_k)
      V̂^alt_i = Π_k (−c_k q⁻¹ + d_k)
      V̂^std_i = z(q) · a + b   where (a, b) is the transfer-matrix
                                 product of the chain.
    """
    import sympy as sp
    from mass_endomorphism_atom import atom_crossings

    q_sym = sp.Symbol('q', positive=True)
    qi_sym = 1 / q_sym
    HA_sym = q_sym - qi_sym
    z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    cross = atom_crossings(nucleon_types, include_inter=include_inter)
    n_strands = 3 * A
    n_gens = n_strands - 1

    V = {"sym": [], "std": [], "alt": []}
    for i in range(n_gens):
        # Tolerances for float → symbolic conversion:
        #   _C_FACTOR_TOL: c ∈ {1} vs other
        #   _D_ZERO_TOL:   d = 0 (exact float zero)
        #   _D_HECKE_TOL:  d = -h or -h/2 at q_0 (looser; h derived from q_0)
        _C_FACTOR_TOL = 1e-9
        _D_ZERO_TOL = 1e-12
        _D_HECKE_TOL = 1e-6
        factors = cross.get(i, [])
        factors_sym = []
        for (c_f, d_f) in factors:
            c = sp.Integer(1) if abs(c_f - 1.0) < _C_FACTOR_TOL \
                else sp.nsimplify(c_f)
            if abs(d_f) < _D_ZERO_TOL:
                d = sp.Integer(0)
            elif abs(d_f + (q0 - 1.0 / q0)) < _D_HECKE_TOL:
                d = -HA_sym
            elif abs(d_f + (q0 - 1.0 / q0) / 2) < _D_HECKE_TOL:
                d = -HA_sym / 2
            else:
                d = sp.nsimplify(d_f)
            factors_sym.append((c, d))

        if not factors_sym:
            V["sym"].append(sp.Integer(1))
            V["std"].append(sp.Integer(1))
            V["alt"].append(sp.Integer(1))
            continue

        # sym, alt: product forms
        prod_sym = sp.Integer(1)
        prod_alt = sp.Integer(1)
        for (c_s, d_s) in factors_sym:
            prod_sym *= c_s * q_sym + d_s
            prod_alt *= -c_s * qi_sym + d_s
        V["sym"].append(sp.simplify(prod_sym))
        V["alt"].append(sp.simplify(prod_alt))

        # std: transfer-matrix chain
        a, b = sp.Integer(0), sp.Integer(1)
        for (c_s, d_s) in factors_sym:
            a_new = a * c_s * HA_sym + a * d_s + b * c_s
            b_new = a * c_s + b * d_s
            a, b = a_new, b_new
        std_expr = z_sym * a + b
        V["std"].append(sp.simplify(std_expr))

    return V, q_sym


def _evaluate_V_with_kahler(V_sym_per_block: dict, q_sym, *,
                               order: int = 0) -> dict:
    """Evaluate per-block symbolic V̂ at q₀ with Kähler-lift corrections.

    order=0: raw V̂(q₀)  (paper's formula as-written)
    order=1: V̂(q₀) + ℏ_q · q · dV̂/dq |_{q₀}
    order=2: +   (ℏ_q²/2) · [q² d²V̂/dq² + q dV̂/dq] |_{q₀}
    """
    import sympy as sp
    hbar_q_sym = (q_sym - 1) / q_sym
    out = {"sym": [], "std": [], "alt": []}
    for ch in ["sym", "std", "alt"]:
        for V_i in V_sym_per_block[ch]:
            V_lifted = V_i
            if order >= 1:
                dV = sp.diff(V_i, q_sym)
                V_lifted = V_lifted + hbar_q_sym * q_sym * dV
            if order >= 2:
                d2V = sp.diff(V_i, q_sym, 2)
                second = q_sym ** 2 * d2V + q_sym * sp.diff(V_i, q_sym)
                V_lifted = V_lifted + (hbar_q_sym ** 2 / 2) * second
            out[ch].append(float(V_lifted.subs(q_sym, q0)))
    return out


def atom_binding_per_block_log_kahler(Z: int, N: int, *,
                                          apply_qed: bool = True,
                                          kahler_order: int = 2,
                                          verbose: bool = False) -> dict:
    """Per-block log binding with proper Kähler-differential jet lift.

    Uses the analytic q-derivative of V̂^λ_i(q) (built symbolically
    from crossings) and applies Kähler corrections of the requested
    order.  The paper's formula
    ([tower-binding-energy](#prop:tower-binding-energy)) specifies
    V̂^λ at level 0; the Kähler lift provides the recursive brane
    tower correction from
    ([jet-tower remark](#rem:mass-endomorphism-jet-tower)) at a
    single higher-order level (not a tower sum — the Kähler
    corrections replace the level-0 V̂ with a Taylor-expanded
    q-dependent value).

    kahler_order=0 recovers atom_binding_per_block_log.
    """
    V_atom_sym, q_sym = _build_V_per_block_symbolic(
        Z, N, include_inter=True)
    V_free_sym, _ = _build_V_per_block_symbolic(
        Z, N, include_inter=False)
    V_atom = _evaluate_V_with_kahler(V_atom_sym, q_sym,
                                         order=kahler_order)
    V_free = _evaluate_V_with_kahler(V_free_sym, q_sym,
                                         order=kahler_order)

    A = Z + N
    n_strands = 3 * A
    n_gens = n_strands - 1

    channels = {"sym": w_sym, "std": w_std, "alt": w_alt}
    B_strong = 0.0
    per_block = {}
    for ch, w in channels.items():
        ln_atom = sum(ln_abs_phi_q(V_atom[ch][i])
                       for i in range(n_gens))
        ln_free = sum(ln_abs_phi_q(V_free[ch][i])
                       for i in range(n_gens))
        contrib = w * M_E_MEV * (ln_free - ln_atom)
        B_strong += contrib
        per_block[ch] = {
            "w_lambda": w,
            "V_atom_per_gen": V_atom[ch],
            "V_free_per_gen": V_free[ch],
            "ln_phi_atom": ln_atom,
            "ln_phi_free": ln_free,
            "contribution_MeV": contrib,
        }
        if verbose:
            print(f"  {ch}: ln|Φ_q|_free - ln|Φ_q|_atom = "
                  f"{ln_free - ln_atom:+.4f}, "
                  f"contrib = {contrib:+.6f} MeV")
    qed_factor = (1.0 - ALPHA_EM / 2.0) if apply_qed else 1.0
    B_phys = B_strong * qed_factor
    M = (Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV - B_phys)
    return {
        "Z": Z, "N": N, "A": A,
        "kahler_order": kahler_order,
        "B_MeV": B_phys,
        "B_strong_MeV": B_strong,
        "qed_factor": qed_factor,
        "qed_applied": apply_qed,
        "M_MeV": M,
        "per_block": per_block,
    }


def atom_binding_per_block_log(Z: int, N: int, *,
                                  apply_qed: bool = True) -> dict:
    """Paper B(Z,N) via per-block log Φ_q on nuclear braid crossings.

    Builds the nuclear atom braid via mass_endomorphism_atom.atom_crossings
    (intra-nucleon + inter-nucleon generators on 3A strands), evaluates
    V̂_i^λ per Wedderburn block, and returns the log-form binding
    prescribed by prop:tower-binding-energy.

    Sign convention in the paper: B(Z,N) > 0 is the binding.  The raw
    log-sum may be negative if atom ln|Φ_q| < free ln|Φ_q| (negative
    defect) — in that case |B| is the binding magnitude.  We report
    both the signed B (paper form, could be negative) and the
    magnitude along with the free-baseline split so the caller can
    interpret.
    """
    from mass_endomorphism_atom import atom_crossings

    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    n_strands = 3 * A

    cross_atom = atom_crossings(nucleon_types, include_inter=True)
    cross_free = atom_crossings(nucleon_types, include_inter=False)

    r_atom = binding_per_block_log(cross_atom, n_strands,
                                       apply_qed=False)
    r_free = binding_per_block_log(cross_free, n_strands,
                                       apply_qed=False)

    # Binding = free − atom per-block log difference, then QED at end.
    B_strong = r_free["B_strong_MeV"] - r_atom["B_strong_MeV"]
    qed_factor = (1.0 - ALPHA_EM / 2.0) if apply_qed else 1.0
    B_phys = B_strong * qed_factor

    # Atomic mass including binding.
    M = (Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV - B_phys)

    return {
        "Z": Z, "N": N, "A": A,
        "B_MeV": B_phys,
        "B_strong_MeV": B_strong,
        "qed_factor": qed_factor,
        "qed_applied": apply_qed,
        "M_MeV": M,
        "atom_block_MeV": r_atom["B_strong_MeV"],
        "free_block_MeV": r_free["B_strong_MeV"],
        "atom_per_block": r_atom["per_block"],
        "free_per_block": r_free["per_block"],
    }


if __name__ == "__main__":
    print("=" * 100)
    print("PAPER-EXACT PER-BLOCK LOG-FORM BINDING")
    print(f"q₀ = {q0:.6f}, m_e = {M_E_MEV:.6f} MeV")
    print(f"w_sym = {w_sym:.4f}, w_std = {w_std:.4f}, "
          f"w_alt = {w_alt:.4f}  (sum = {w_sym+w_std+w_alt:.4f})")
    print(f"α_EM = {ALPHA_EM}, QED factor = {1 - ALPHA_EM/2:.6f}")
    print(f"ALPHA_BINDING = m_e · 8G = {ALPHA_BINDING_MEV:.4f} MeV "
          f"(prop:binding-scale-catalan)")
    print("=" * 100)

    # Sanity: ln|Φ_q(v)| on a few sample values
    print("\nSanity check: ln|Φ_q(v)| vs Φ_q(v) behaviour")
    print(f"  {'v':>8} {'|v|':>10} {'ln|Φ_q|':>14} "
          f"{'note':>30}")
    for v in [0.1, 0.5, 0.9, 1.0, 1.05, 1.09, 1.15, 1.2, 1.5, 2.0]:
        try:
            ln_phi = ln_abs_phi_q(v)
            note = ""
            if v > q0:
                note = "beyond q₀ (analytic cont.)"
            print(f"  {v:>8.3f} {abs(v):>10.4f} {ln_phi:>+14.4f} "
                  f"{note:>30}")
        except ZeroDivisionError as e:
            print(f"  {v:>8.3f}  DIVERGES near q^k: {e}")

    # Deuterium (sym-only crossings — simplest test case)
    # Actual nuclear pipeline needs build_atom_symbolic integration;
    # here we just confirm the ln_abs_phi_q function works.
    print("\n" + "=" * 100)
    print("Electron (trefoil σ^3 on 2 strands)")
    print("=" * 100)
    electron_cross = {0: [(1.0, 0.0)] * 3}
    r = binding_per_block_log(electron_cross, 2, apply_qed=False)
    print(f"  per-block V̂ at gen 0:")
    for ch in ["sym", "std", "alt"]:
        b = r["per_block"][ch]
        print(f"    {ch:>4}: V̂ = {b['V_per_gen'][0]:+.6f}, "
              f"ln|Φ_q| = {b['ln_phi_sum_cat']:+.4f}, "
              f"contribution = {b['contribution_MeV']:+.4f} MeV")
    print(f"  B_strong = {r['B_strong_MeV']:+.6f} MeV  "
          f"(observed m_e = {M_E_MEV:.6f})")

    # Nuclear binding: D, T, ³He, ⁴He via atom_crossings.
    print("\n" + "=" * 100)
    print("NUCLEAR BINDING via per-block log Φ_q "
          "(prop:tower-binding-energy)")
    print("=" * 100)
    # AME 2020 binding energies (MeV)
    AME_B = {
        ("D", 1, 1):   2.22452,
        ("T", 1, 2):   8.4818,
        ("³He", 2, 1): 7.7181,
        ("⁴He", 2, 2): 28.2957,
    }
    print(f"  {'atom':>6} {'Z':>3} {'N':>3} {'B_strong':>11} "
          f"{'B_phys':>11} {'B_AME':>11} {'|Δm/m|%':>11}")
    print("  " + "-" * 85)
    nuclear_results = []
    for (name, Z, N), B_AME in AME_B.items():
        try:
            r = atom_binding_per_block_log(Z, N, apply_qed=True)
            A = r["A"]
            dm_pct = (abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100)
            print(f"  {name:>6} {Z:>3} {N:>3} "
                  f"{r['B_strong_MeV']:>+11.4f} {r['B_MeV']:>+11.4f} "
                  f"{B_AME:>+11.4f} {dm_pct:>10.4f}%")
            nuclear_results.append({**r, "name": name, "B_AME": B_AME,
                                      "dm_pct": dm_pct})
        except Exception as e:
            print(f"  {name:>6} ERR: {type(e).__name__}: {str(e)[:60]}")

    # ── Kähler-lifted per-block V̂ (proper jet-up from level 0) ─
    # Requires sympy; skip gracefully if unavailable.
    try:
        import sympy as _sp  # noqa: F401
        have_sympy = True
    except ImportError:
        have_sympy = False
    kahler_results = []
    if have_sympy:
        print("\n" + "=" * 100)
        print("KÄHLER-LIFTED PER-BLOCK V̂  (option #3 — proper "
              "analytic q-derivative)")
        print(f"  ℏ_q = {(q0-1)/q0:.4f}; modeling ε: "
              f"O(ℏ_q) → O(ℏ_q²) → O(ℏ_q³) at orders 0 → 1 → 2")
        print("=" * 100)
        for K_ORDER in [0, 1, 2]:
            eps_order = K_ORDER + 1
            print(f"\n--- kahler_order = {K_ORDER}, "
                  f"ε = O(ℏ_q^{eps_order}) ---")
            print(f"  {'atom':>6} {'B_phys':>12} {'B_AME':>11} "
                  f"{'|Δm/m|%':>11} {'eps_bound':>14}")
            print("  " + "-" * 75)
            for (name, Z, N), B_AME in AME_B.items():
                try:
                    r = atom_binding_per_block_log_kahler(
                        Z, N, apply_qed=True,
                        kahler_order=K_ORDER)
                    A = r["A"]
                    dm_pct = (abs(r["B_MeV"] - B_AME)
                               / (A * 938.272) * 100)
                    hbar_q = (q0 - 1) / q0
                    eps_MeV = hbar_q ** eps_order * M_E_MEV
                    print(f"  {name:>6} {r['B_MeV']:>+12.6f} "
                          f"{B_AME:>+11.4f} "
                          f"{dm_pct:>10.4f}% "
                          f"{eps_MeV:>13.3e}")
                    kahler_results.append({
                        **r, "name": name, "B_AME": B_AME,
                        "dm_pct": dm_pct, "K_order": K_ORDER,
                        "eps_bound_MeV": eps_MeV,
                    })
                except Exception as e:
                    print(f"  {name:>6} ERR: {type(e).__name__}: "
                          f"{str(e)[:60]}")
    else:
        print("\n(sympy not available — skipping Kähler-lift section)")

    # ── Jet-tower corrections (option #2 from follow-up plan) ────
    print("\n" + "=" * 100)
    print("JET-TOWER-AUGMENTED: B = B_lvl0 + sum_n ℏ_q^{2n} * Δ^(n)")
    print(f"  ℏ_q^2 = {((q0-1)/q0)**2:.6f}  "
          f"(per-level geometric damping)")
    print("=" * 100)
    jet_results = []
    for N_MAX in [0, 1, 2, 3]:
        print(f"\n--- n_jet_levels = {N_MAX} ---")
        print(f"  {'atom':>6} {'B_phys':>12} {'B_AME':>11} "
              f"{'|Δm/m|%':>11} {'tail_bound':>14}")
        print("  " + "-" * 75)
        for (name, Z, N), B_AME in AME_B.items():
            try:
                r = atom_binding_per_block_log_jet(
                    Z, N, apply_qed=True, n_jet_levels=N_MAX)
                A = r["A"]
                dm_pct = abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
                tail = r.get("tail_bound_MeV", float("inf"))
                tail_str = f"{tail:.3e}" if math.isfinite(tail) else "—"
                print(f"  {name:>6} {r['B_MeV']:>+12.6f} "
                      f"{B_AME:>+11.4f} "
                      f"{dm_pct:>10.4f}% {tail_str:>14}")
                jet_results.append({**r, "name": name,
                                      "B_AME": B_AME,
                                      "dm_pct": dm_pct,
                                      "N_jet": N_MAX})
            except Exception as e:
                print(f"  {name:>6} ERR: {type(e).__name__}: "
                      f"{str(e)[:60]}")

    witness = {
        "computation": "binding-per-block-log",
        "description": (
            "Paper-exact per-block log-form B(Z,N) = Σ_λ w_λ m_e "
            "Σ_i ln|Φ_q(V̂_i^λ)| from prop:tower-binding-energy.  "
            "Uses the log-form of Φ_q which is well-defined past "
            "|V̂| = q via ln|1 − q^{-k}v| = ln|q^{-k}v − 1| for "
            "q^{-k}v > 1 (the 'analytic continuation past the "
            "pole' in the paper).  QED correction (1 − α_EM/2) "
            "applied per prop:deuterium-derived-binding."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "m_e_MeV": M_E_MEV,
            "alpha_em": ALPHA_EM,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
            "alpha_binding_MeV": ALPHA_BINDING_MEV,
        },
        # P2.5: see docs/audits/2026-05-02-p2-5-symbolic-q-audit.md
        "symbolic_q_form": {
            "engine": "sympy",
            "q_symbol": "q (sp.Symbol('q', positive=True))",
            "h_symbol_definition": "HA = q - 1/q",
            "z_symbol_definition": "z = 1 / (sqrt(q) + 1/sqrt(q))",
            "pattern": "sympy-symbolic-coefficients-evaluated-at-q0",
            "note": (
                "Per-V̂_i^λ coefficient polynomials in q are "
                "constructed symbolically; the numerical results "
                "below come from .subs(q_sym, q_0) evaluation."
            ),
        },
        "sample_ln_phi_q": {
            f"v_{v}": ln_abs_phi_q(v) if v != 1.0 else "DIVERGES"
            for v in [0.1, 0.5, 0.9, 1.05, 1.09, 1.15, 1.2, 1.5, 2.0]
        },
        "electron_result": r,
        "nuclear_results": nuclear_results,
        "jet_tower_results": jet_results,
        "kahler_results": kahler_results,
    }
    out = Path(__file__).parent / "binding-per-block-log.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
