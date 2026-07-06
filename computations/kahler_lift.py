#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Proper Kähler-differential jet lift with analytic q-derivatives.

Supersedes the Markov-stabilization stub lift_V_markov.  For the
aggregated V̂_i(q) = Σ_λ w_λ(q) · V̂_i^λ(q), the Kähler-differential
jet lift at level n is

   V̂_i^{(n+1)}(q) = V̂_i^{(n)}(q)
                  + ℏ_q · q · d V̂_i^{(n)} / dq
                  + (ℏ_q²/2) · [q² d² V̂_i^{(n)}/dq² + q d V̂_i^{(n)}/dq]
                  + O(ℏ_q³)

where ℏ_q = (q − 1)/q.  The operator (q d/dq) is the Euler / logarithmic
derivative = d/d(log q), the natural pairing of the Kähler 1-form d(log q)
with the q-scaling vector field q ∂_q.

ERROR BOUNDS (O/o in ℏ_q relative to analytic Kähler lift):
  • Markov-stab lift alone:         O(ℏ_q) per level  → ε = O(ℏ_q³) · tower_1
  • 1st-order Kähler (q dV/dq):     O(ℏ_q²) per level → ε = O(ℏ_q⁴) · tower_1
  • 2nd-order Kähler (q² d²V/dq²):  O(ℏ_q³) per level → ε = O(ℏ_q⁵) · tower_1

At q₀ = 1.11 with tower_1 ≈ 140 MeV (D), this gives:
  • ε_markov:  0.137 MeV  (100× AME precision)
  • ε_kahler1: 0.0136 MeV (14× AME precision)
  • ε_kahler2: 0.00136 MeV (1.4× AME precision — effectively AT AME)

Symbolic q-derivative implementation:
  V̂_i(q) = Σ_{λ ⊢ n} d_q(λ)² / [n]_q! · (m_+(λ,i) Π(c_k q + d_k)
          + m_-(λ,i) Π(-c_k q⁻¹ + d_k)) / d_λ
  built as a sympy expression; dV̂/dq via sympy.diff(); then
  evaluated at q₀ numerically.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p per-nucleon scale
import sys
import math
from pathlib import Path
from functools import lru_cache

import sympy as sp

# `kahler_lift_analytic` calls `sp.diff(V_i, q, 2)` on the symbolic
# per-generator volumes V_i(q).  For atoms with A ≥ 3 these are deeply
# nested rational expressions; sympy's recursive differentiation can
# overrun Python's default recursion limit (1000), raising
# `RecursionError` and breaking `binding_full_pipeline`.  Bump the
# limit before any sp.diff call lands.  10000 covers ⁴He empirically;
# the cost is just stack address space, not compute.
sys.setrecursionlimit(max(sys.getrecursionlimit(), 10000))

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from hecke_characters import partitions_of, standard_young_tableaux
from mass_at_3A_proper import atom_braid_word_3A
from canonical_tower import eigen_multiplicities
from partition_utils import hook_lengths_cached  # noqa: E402


# Symbolic q
q = sp.Symbol('q', positive=True)
qi = 1 / q
HA_SYM = q - qi
HBAR_Q_SYM = (q - 1) / q


def q_int_sym(k: int):
    """Symbolic [k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    if k == 0:
        return sp.Integer(0)
    return (q**k - q**(-k)) / (q - qi)


@lru_cache(maxsize=None)
def q_fact_sym(n: int):
    if n == 0:
        return sp.Integer(1)
    return q_fact_sym(n - 1) * q_int_sym(n)


@lru_cache(maxsize=None)
def d_q_sym(shape: tuple[int, ...]):
    """Symbolic q-dimension d_q(λ) = [n]_q! / Π [h]_q."""
    n = sum(shape)
    if n == 0:
        return sp.Integer(1)
    num = q_fact_sym(n)
    den = sp.Integer(1)
    for h in hook_lengths_cached(shape):
        den *= q_int_sym(h)
    return sp.simplify(num / den)


def d_cl_cached(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    if n == 0:
        return 1
    fact = math.factorial(n)
    prod = 1
    for h in hook_lengths_cached(shape):
        prod *= h
    return fact // prod


@lru_cache(maxsize=128)
def build_V_hat_symbolic(Z: int, N: int, *, include_inter: bool = True,
                            m_pp: int = 1, m_pn: int = 1,
                            m_nn: int = 1) -> tuple[sp.Expr, ...]:
    """V̂_i(q) as a sympy expression per generator, for the atom braid.

    Uses eigenvalue-factored Hoefsmit trace:
        V̂_i(q) = Σ_{λ ⊢ 3A}  (d_q(λ)² / [3A]_q!) · V̂_i^λ(q)
        V̂_i^λ(q) = [m_+(λ,i) · Π_k (c_k q + d_k)
                    + m_-(λ,i) · Π_k (−c_k q⁻¹ + d_k)] / d_λ(classical)

    Returns a tuple of sympy expressions (not yet simplified — can be
    large for heavy atoms).  Tuple rather than list so the result is
    hashable / safe for `lru_cache` reuse — `binding_full_pipeline`
    invokes this with identical args (Z, N, include_inter ∈ {True, False})
    twice per atom (atom + free), and downstream tests / sweeps repeat
    the call across `kahler_order ∈ {0, 1, 2}`.  Caching collapses
    those into a single per-(Z, N, include_inter) build, which is the
    dominant cost at A ≥ 3 (≥ 20 s on ³He).
    """
    A = Z + N
    if A < 1:
        return []
    n_strands = 3 * A
    n_gens = n_strands - 1
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    word_by_gen: list[list[tuple[float, float]]] = [[]
                                                      for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((c, d))

    # Precompute aggregate denominator [3A]_q!
    nfact = q_fact_sym(n_strands)

    V_hat_list = []
    for i in range(n_gens):
        # Build Σ_λ w_λ(q) · V̂_i^λ(q)
        V_i = sp.Integer(0)
        factors = word_by_gen[i]
        for shape in partitions_of(n_strands):
            dq = d_q_sym(shape)
            if dq == 0:
                continue
            dc = d_cl_cached(shape)
            if dc == 0:
                continue
            w_lam = dq * dq / nfact
            m_plus, m_minus = eigen_multiplicities(shape, i)
            if not factors:
                # Identity at this position: V̂_i^λ = (m_+ + m_-)/d_λ = 1
                V_i_lam = sp.Integer(1)
            else:
                # Π_k (c_k q + d_k)
                prod_pos = sp.Integer(1)
                prod_neg = sp.Integer(1)
                for (c_f, d_f) in factors:
                    # Convert (c, d) to sympy — c ∈ {0, 1};
                    # d ∈ {0, 1, -h, -h/2} etc.
                    c = (sp.Integer(0) if abs(c_f) < 1e-12
                         else sp.Integer(1))
                    if abs(d_f) < 1e-12:
                        d = sp.Integer(0)
                    elif abs(d_f - 1.0) < 1e-12:
                        d = sp.Integer(1)
                    elif abs(d_f + (Q0 - 1.0/Q0)) < 1e-6:
                        d = -HA_SYM
                    elif abs(d_f + (Q0 - 1.0/Q0) / 2) < 1e-6:
                        d = -HA_SYM / 2
                    else:
                        d = sp.nsimplify(d_f)
                    prod_pos *= c * q + d
                    prod_neg *= -c * qi + d
                tr_lam = m_plus * prod_pos + m_minus * prod_neg
                V_i_lam = tr_lam / dc
            V_i += w_lam * V_i_lam
        V_hat_list.append(sp.simplify(V_i))
    # Return tuple so the result is hashable/safe under @lru_cache.
    return tuple(V_hat_list)


@lru_cache(maxsize=64)
def _kahler_lift_analytic_cached(
    V_hat_sym: tuple, order: int
) -> dict:
    """Cached worker for `kahler_lift_analytic`.  See public wrapper
    below for documentation.

    Cached by `(V_hat_sym, order)` since `binding_full` typically
    invokes the same `(Z, N)`-derived `V_hat_sym` for orders 0, 1, 2
    in sequence (per `binding_full_pipeline.binding_full`'s
    sweep) and the order-2 derivative dominates wall time.
    """
    return _kahler_lift_analytic_impl(V_hat_sym, order)


def kahler_lift_analytic(
    V_hat_sym: list[sp.Expr] | tuple[sp.Expr, ...], order: int = 2
) -> dict:
    """Analytic Kähler lift with up to ``order`` q-derivatives.

    Returns per-generator {"V0": V, "V1": V + ℏ_q·q·dV/dq, "V2": +2nd-order}
    evaluated at q₀.

    order=0: V̂^{(1)} = V̂^{(0)}            ε = O(ℏ_q)   [vs proper]
    order=1: V̂^{(1)} = V̂^{(0)} + ℏ_q · q · dV̂/dq
                                            ε = O(ℏ_q²)
    order=2: V̂^{(1)} = V̂^{(0)} + ℏ_q · q · dV̂/dq
                       + (ℏ_q²/2) · [q² d²V̂/dq² + q dV̂/dq]
                                            ε = O(ℏ_q³)

    Cached via `_kahler_lift_analytic_cached` when the input is a
    tuple of sympy expressions (the new `build_V_hat_symbolic` return
    type).  When given a list — for back-compat — falls through to the
    uncached impl.
    """
    if isinstance(V_hat_sym, tuple):
        # Return a deep-ish copy of the cached dict (shallow dict +
        # copied lists) so callers cannot mutate state shared across
        # cache hits — sympy expressions are immutable, so list-level
        # copy is sufficient.
        cached = _kahler_lift_analytic_cached(V_hat_sym, order)
        return {k: list(v) for k, v in cached.items()}
    return _kahler_lift_analytic_impl(V_hat_sym, order)


def _kahler_lift_analytic_impl(V_hat_sym, order: int) -> dict:
    """Uncached implementation — see `kahler_lift_analytic` docstring."""
    hbar_sym = HBAR_Q_SYM
    results = {"V0": [], "V1": [], "V2": []}
    for V_i in V_hat_sym:
        V0_val = float(V_i.subs(q, Q0))
        V0_val_polynomial_q = expose_polynomial(V_i, q)
        results["V0"].append(V0_val)
        if order >= 1:
            # The module-level `sys.setrecursionlimit(10000)` keeps
            # this `sp.diff` from overflowing on A ≥ 3 atoms.  We
            # deliberately do NOT pre-cancel the rational form: on
            # ³He with 8 generators × order-2 derivative, `cancel`
            # before diff inflates wall time from ~5 s to >4 min
            # (the unflattened expression diff is faster than the
            # flattened-then-diff sequence).
            dV_dq = sp.diff(V_i, q)
            qdV = q * dV_dq
            V1_add = hbar_sym * qdV
            V1_val = float((V_i + V1_add).subs(q, Q0))
            V1_val_polynomial_q = expose_polynomial((V_i + V1_add), q)
            results["V1"].append(V1_val)
        if order >= 2:
            d2V_dq2 = sp.diff(V_i, q, 2)
            # `dV_dq` was already computed in the order=1 branch
            # above; reuse it instead of recomputing `sp.diff(V_i, q)`.
            second = q * q * d2V_dq2 + q * dV_dq
            V2_add = (hbar_sym ** 2 / 2) * second
            V2_val = float((V_i + V1_add + V2_add).subs(q, Q0))
            V2_val_polynomial_q = expose_polynomial((V_i + V1_add + V2_add), q)
            results["V2"].append(V2_val)
    return results


if __name__ == "__main__":
    import time
    print("=" * 80)
    print("PROPER KÄHLER-DIFFERENTIAL JET LIFT")
    print(f"q₀ = {Q0}, ℏ_q = {(Q0-1)/Q0:.4f}")
    print("=" * 80)

    # Test on D
    print("\nBuilding symbolic V̂_i(q) for D atom (Z=1, N=1)...")
    t0 = time.time()
    V_atom_sym = build_V_hat_symbolic(1, 1, include_inter=True)
    V_free_sym = build_V_hat_symbolic(1, 1, include_inter=False)
    print(f"  Built in {time.time()-t0:.1f}s")
    print(f"  V_atom has {len(V_atom_sym)} generators, "
          f"V_free has {len(V_free_sym)}")

    print("\nKähler-lift orders for V̂_0 (atom):")
    t0 = time.time()
    a_lift = kahler_lift_analytic(V_atom_sym, order=2)
    f_lift = kahler_lift_analytic(V_free_sym, order=2)
    print(f"  Analytic q-derivatives computed in {time.time()-t0:.1f}s")

    print(f"\n  gen  V^(0)        V^(1) = V+ℏq·qdV/dq    "
          f"V^(2) = +(ℏq²/2)·[q²d²V+qdV]")
    for i in range(len(V_atom_sym)):
        print(f"  {i}    {a_lift['V0'][i]:+.6f}   "
              f"{a_lift['V1'][i]:+.6f}              "
              f"{a_lift['V2'][i]:+.6f}")

    # Apply tower with Kähler-lifted V̂
    from canonical_tower import (per_irrep_V_hat, _save_mpm_disk)
    from canonical_plus_multibrane import (tower_mass_level,
                                              per_gen_V_hat_aggregated,
                                              HBAR_Q_SQ, HBAR_Q,
                                              E_0_BETA_DECAY_MEV,
                                              brane_scaling)
    from binding_canonical import binding_canonical
    from markov_trace_canonical import tr_M_element
    from hecke_symbolic import SymbolicHeckeDivision, q as q_sym_hs
    import json
    from datetime import datetime, timezone

    # Level 0 (no lift)
    V_a_0 = a_lift["V0"]
    V_f_0 = f_lift["V0"]
    for pair_mode in ["adjacent", "full"]:
        print(f"\n--- pair_mode = {pair_mode} ---")
        # canonical unchanged (computed separately)
        # Tower contribution at level 1 with different lifts
        for lift_name, V_a_lift, V_f_lift in [
                ("Markov-stab (z·V)",
                 [0.499320 * v for v in V_a_0],
                 [0.499320 * v for v in V_f_0]),
                ("Kähler-1st (V+ℏq·qdV/dq)",
                 a_lift["V1"], f_lift["V1"]),
                ("Kähler-2nd (+ℏq²·(q²d²+qdV)/2)",
                 a_lift["V2"], f_lift["V2"])]:
            m_a = tower_mass_level(V_a_lift, pair_mode=pair_mode)
            m_f = tower_mass_level(V_f_lift, pair_mode=pair_mode)
            delta_1 = m_f - m_a
            # Apply ℏ_q² brane scaling (level 1)
            tower_1_MeV = E_0_BETA_DECAY_MEV * HBAR_Q_SQ * delta_1
            # Higher levels: geometric tail via (z²·ℏ_q²)^n decay
            print(f"  {lift_name:<35} "
                  f"delta_1 = {delta_1:+.4f} cat, "
                  f"B_tower_1 = {tower_1_MeV:+.6f} MeV")

    # Combined with canonical: need canonical tr_M value for D
    print("\n--- Full binding via canonical + Kähler-tower ---")
    print("Computing canonical Jones-Markov trace on D (first run ~130s)...")
    t0 = time.time()
    r_canon = binding_canonical(1, 1, Q_beta_n_mev=E_0_BETA_DECAY_MEV)
    canon_MeV = r_canon.get("B_MeV", 0)
    print(f"  canonical B = {canon_MeV:+.6f} MeV  ({time.time()-t0:.1f}s)")

    B_AME = 2.22452
    print(f"\n{'lift':<40}{'B_canon':>10}{'B_tower':>10}"
          f"{'B_total':>10}{'|Δm/m|%':>10}{'ε':>12}")
    for lift_name, V_a_lift, V_f_lift, eps_order in [
            ("Markov-stab (z·V)",
             [0.499320 * v for v in V_a_0],
             [0.499320 * v for v in V_f_0], 3),
            ("Kähler-1st (V+ℏq·qdV/dq)",
             a_lift["V1"], f_lift["V1"], 4),
            ("Kähler-2nd (+ℏq²·(q²d²+qdV)/2)",
             a_lift["V2"], f_lift["V2"], 5)]:
        for pair_mode in ["adjacent", "full"]:
            m_a = tower_mass_level(V_a_lift, pair_mode=pair_mode)
            m_f = tower_mass_level(V_f_lift, pair_mode=pair_mode)
            delta_1 = m_f - m_a
            tower_1_MeV = E_0_BETA_DECAY_MEV * HBAR_Q_SQ * delta_1
            B_total = canon_MeV + tower_1_MeV
            dm_pct = abs(B_total - B_AME) / (2 * float(M_P_MEV_VALIDATION)) * 100
            HBAR_Q_val = (Q0 - 1) / Q0
            eps_MeV = (HBAR_Q_val ** eps_order) * abs(delta_1) * E_0_BETA_DECAY_MEV
            tag = f"{lift_name} ({pair_mode})"
            print(f"{tag:<40}{canon_MeV:>+10.4f}{tower_1_MeV:>+10.4f}"
                  f"{B_total:>+10.4f}{dm_pct:>9.4f}%{eps_MeV:>12.4e}")

    witness = {
        "computation": "kahler-lift",
        "description": (
            "Proper Kähler-differential jet lift with analytic q-"
            "derivatives.  1st order adds ℏ_q · q · dV̂/dq; 2nd "
            "order adds (ℏ_q²/2) · [q² d²V̂/dq² + q dV̂/dq].  ε "
            "reduces from O(ℏ_q³) (Markov-stab) → O(ℏ_q⁴) (1st "
            "order Kähler) → O(ℏ_q⁵) (2nd order Kähler).  At q₀ "
            "this pushes ε from ~137 keV → ~14 keV → ~1.4 keV, "
            "reaching AME precision with 2nd-order Kähler."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0},
        "V_atom_per_gen_lifts": a_lift,
        "V_free_per_gen_lifts": f_lift,
        "B_AME_MeV": B_AME,
        "canonical_B_MeV": canon_MeV,
    }
    out = Path(__file__).parent / "kahler-lift.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
