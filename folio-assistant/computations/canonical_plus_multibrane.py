#!/usr/bin/env python3
"""
Canonical Markov trace + MULTI-BRANE Φ_q tower.

Implements prop:categorical-mass-markov's FULL mass formula:

   𝔪(ρ) = |tr_M(ρ(β))|  +  Σ_{n=1}^N  Σ_i  ‖Φ_q(zᵢ^{(n)})‖
          ──────────────    ──────────────────────────────────
          level-0 single-    tower contributions at brane
          brane Markov       levels n=1..N over exceptional
          trace              divisors zᵢ at each level

Level 0 (canonical): via markov_trace_canonical.tr_M_element —
matches prop explicit-values table exactly.

Level n ≥ 1 (tower): per prop:mass-endomorphism-tower, each brane
level contributes

   𝔪^{(n)} = |Π V̂_i^{(n)}| + Σ Φ_q(|V̂_i^{(n)}|)
           + z² Σ_{(i,j) ∈ 𝒫} Φ_q(|V̂_i^{(n)} V̂_j^{(n)}|)

with V̂_i^{(n)} = jet-lifted per-generator value at level n, using
the AGGREGATED Wedderburn form V̂_i = Σ_λ w_λ · V̂_i^λ (per the prop's
letter — Φ_q acts AFTER Plancherel summation, not per-irrep).

Binding:
   B(Z, N) = E_0 · ( 𝔪(W_free) − 𝔪(W_atom) )
   E_0 = 0.782 MeV  (free-neutron β-decay Q, per prop).

SCOPE & CAVEATS:
  1. V̂_i^{(n)} jet-lifting uses the MARKOV STABILIZATION rule
     V̂^{(n)} = z · V̂^{(n-1)}  (simplest; proper Kähler-differential
     lift open).  Proper per-level V̂ would introduce new generators
     via Ω¹(H_n(q)) Leibniz action — not implemented.
  2. Level 0 canonical trace is O(100s) per atom; level-n tower
     per brane adds additive cost.  N ≤ 5 is practical on D; heavy
     atoms need per-level caching.
  3. E_0 = 0.782 MeV is the PROP's calibration for |tr_M| ≲ 1;
     tower Φ_q values may be larger, so the SUM can exceed the
     bounded-trace regime.  An alternative calibration via proton-
     tower is also implemented (`E_0_calibration="proton_tower"`).
"""
from __future__ import annotations

import sys
import math
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_INV as QI, HA as H0
from mass_endomorphism import Phi_q, z_mark
from hecke_characters import (partitions_of, dim_q, qfac,
                                standard_young_tableaux)
from markov_trace_canonical import tr_M_element
from hecke_symbolic import (SymbolicHeckeDivision,
                              SymbolicHeckeElement, q as q_sym)
from mass_at_3A_proper import atom_braid_word_3A, phi_q_safe
from binding_canonical import build_atom_symbolic
from canonical_tower import (per_irrep_V_hat, eigen_multiplicities,
                               _save_mpm_disk)


E_0_BETA_DECAY_MEV = 0.782  # prop:categorical-mass-markov E_0


# ── Aggregated V̂ (Wedderburn sum BEFORE Φ_q) ────────────────
#
# Per prop's letter: V̂_i is the ADDITIVE Wedderburn traced volume
# at generator i, aggregated over λ before Φ_q is applied.

def per_gen_V_hat_aggregated(Z: int, N: int, *,
                                include_inter: bool = True,
                                m_pp: int = 1, m_pn: int = 1,
                                m_nn: int = 1) -> list[float]:
    """V̂_i = Σ_{λ ⊢ n} w_λ · V̂_i^λ  (Wedderburn aggregate).

    Each V̂_i^λ from per_irrep_V_hat (eigenvalue-factored, O(num_factors)).
    Plancherel weight w_λ = d_q(λ)² / [n]_q!.  This is the order
    the prop actually prescribes — Φ_q applied AFTER the aggregate,
    not per-irrep then summed.
    """
    A = Z + N
    if A < 1:
        return []
    n_strands = 3 * A
    n_gens = n_strands - 1
    nfac = qfac(n_strands)
    V_hat = [0.0] * n_gens
    for shape in partitions_of(n_strands):
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_lam = (dq * dq) / nfac
        V_lam = per_irrep_V_hat(Z, N, shape,
                                  include_inter=include_inter,
                                  m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        for i in range(n_gens):
            V_hat[i] += w_lam * V_lam[i]
    _save_mpm_disk(n_strands)
    return V_hat


def tower_mass_level(V: list[float], *, pair_mode: str = "adjacent",
                       cap_frac: float = 0.98) -> float:
    """Single-level prop:mass-endomorphism-tower formula on aggregated V̂."""
    n = len(V)
    if n == 0:
        return 0.0
    desc = 1.0
    for v in V:
        desc *= v
    desc = abs(desc)
    single = sum(phi_q_safe(abs(v), cap_frac=cap_frac) for v in V)
    cross = 0.0
    if pair_mode == "adjacent":
        for i in range(n - 1):
            cross += z_mark ** 2 * phi_q_safe(
                abs(V[i] * V[i + 1]), cap_frac=cap_frac)
    elif pair_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += z_mark ** 2 * phi_q_safe(
                    abs(V[i] * V[j]), cap_frac=cap_frac)
    return desc + single + cross


def lift_V_markov(V: list[float], level: int) -> list[float]:
    """Jet-lift V̂ from level 0 to level `level` via Markov stabilization.

    V̂_i^{(n)} = z^n · V̂_i^{(0)}.  Simplest stub; proper jet lift via
    Ω¹(H_n(q)) Kähler differentials is open.
    """
    if level == 0:
        return list(V)
    factor = z_mark ** level
    return [v * factor for v in V]


# ── Canonical Markov trace + multi-brane tower ──────────────

def binding_canonical_plus_multibrane(
        Z: int, N: int, *,
        n_brane_levels: int = 1,
        m_pp: int = 1, m_pn: int = 1, m_nn: int = 1,
        E_0: float = E_0_BETA_DECAY_MEV,
        pair_mode: str = "adjacent",
        cap_frac: float = 0.98,
        include_canonical: bool = True,
        verbose: bool = False) -> dict:
    """Full mass formula per prop:categorical-mass-markov:

      B = E_0 · [ (|tr_M(W_free)| - |tr_M(W_atom)|)
                + Σ_{n=1}^{n_brane_levels} (𝔪^{(n)}_free - 𝔪^{(n)}_atom) ]

    Level 0: canonical Jones-Markov trace (axiomatically correct).
    Levels 1..N: Φ_q tower on Markov-stabilized V̂.

    ``include_canonical=False`` omits the level-0 canonical trace —
    useful for probing tower-only contributions.  ``n_brane_levels=0``
    gives level-0 only (= binding_canonical.binding_canonical).
    """
    A = Z + N
    if A < 1:
        return {"status": "trivial"}

    # ── Level 0: canonical Markov trace ─────────────────
    canonical_term = 0.0
    tr_M_atom = None
    tr_M_free = None
    if include_canonical:
        div = SymbolicHeckeDivision()
        atom_elem = build_atom_symbolic(Z, N, include_inter=True,
                                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        free_elem = build_atom_symbolic(Z, N, include_inter=False,
                                          m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        atom_elem, _ = div.reduce(atom_elem)
        free_elem, _ = div.reduce(free_elem)
        try:
            tr_a_sym = tr_M_element(atom_elem, 3 * A)
            tr_f_sym = tr_M_element(free_elem, 3 * A)
            tr_M_atom = complex(sp.N(tr_a_sym.subs(q_sym, Q0)))
            tr_M_free = complex(sp.N(tr_f_sym.subs(q_sym, Q0)))
            if abs(tr_M_atom.imag) < 1e-9:
                tr_M_atom = tr_M_atom.real
            if abs(tr_M_free.imag) < 1e-9:
                tr_M_free = tr_M_free.real
            canonical_term = abs(tr_M_free) - abs(tr_M_atom)
            if verbose:
                print(f"  |tr_M_atom| = {abs(tr_M_atom):.6f}, "
                      f"|tr_M_free| = {abs(tr_M_free):.6f}")
        except Exception as e:
            if verbose:
                print(f"  canonical trace failed: {e}")
            canonical_term = 0.0

    # ── Levels 1..N: tower on aggregated V̂ ─────────────
    tower_term = 0.0
    per_level = []
    if n_brane_levels >= 1:
        V_atom_0 = per_gen_V_hat_aggregated(
            Z, N, include_inter=True,
            m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        V_free_0 = per_gen_V_hat_aggregated(
            Z, N, include_inter=False,
            m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        if verbose:
            print(f"  V_atom^(0) = {[f'{v:+.4f}' for v in V_atom_0]}")
            print(f"  V_free^(0) = {[f'{v:+.4f}' for v in V_free_0]}")
        for n in range(1, n_brane_levels + 1):
            V_a = lift_V_markov(V_atom_0, n)
            V_f = lift_V_markov(V_free_0, n)
            m_a = tower_mass_level(V_a, pair_mode=pair_mode,
                                     cap_frac=cap_frac)
            m_f = tower_mass_level(V_f, pair_mode=pair_mode,
                                     cap_frac=cap_frac)
            delta = m_f - m_a
            tower_term += delta
            per_level.append({
                "level": n, "m_atom": m_a, "m_free": m_f,
                "delta": delta,
            })

    B = E_0 * (canonical_term + tower_term)
    return {
        "Z": Z, "N": N, "A": A,
        "n_brane_levels": n_brane_levels,
        "pair_mode": pair_mode,
        "E_0_MeV": E_0,
        "tr_M_atom": (complex(tr_M_atom) if tr_M_atom is not None else None),
        "tr_M_free": (complex(tr_M_free) if tr_M_free is not None else None),
        "canonical_term": canonical_term,
        "canonical_contribution_MeV": E_0 * canonical_term,
        "tower_term": tower_term,
        "tower_contribution_MeV": E_0 * tower_term,
        "per_level": per_level,
        "B_MeV": B,
    }


# ── CLI ─────────────────────────────────────────────────────

if __name__ == "__main__":
    ATOMS = [
        ("D", 1, 1, 2.22452),
    ]
    print("=" * 100)
    print("CANONICAL MARKOV + MULTI-BRANE Φ_q TOWER")
    print(f"q₀ = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV (β-decay Q)")
    print("=" * 100)
    results = []
    # Cache canonical trace per (Z,N) so we don't recompute across n_levels.
    _CANON_CACHE: dict[tuple[int, int], tuple[complex, complex]] = {}

    def _cached_canonical(Z, N, m_pp=1, m_pn=1, m_nn=1):
        key = (Z, N)
        if key in _CANON_CACHE:
            return _CANON_CACHE[key]
        div = SymbolicHeckeDivision()
        ae = build_atom_symbolic(Z, N, include_inter=True,
                                   m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        fe = build_atom_symbolic(Z, N, include_inter=False,
                                   m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        ae, _ = div.reduce(ae)
        fe, _ = div.reduce(fe)
        ta = complex(sp.N(tr_M_element(ae, 3 * (Z + N)).subs(q_sym, Q0)))
        tf = complex(sp.N(tr_M_element(fe, 3 * (Z + N)).subs(q_sym, Q0)))
        if abs(ta.imag) < 1e-9: ta = ta.real
        if abs(tf.imag) < 1e-9: tf = tf.real
        _CANON_CACHE[key] = (ta, tf)
        return ta, tf

    # Prime cache for each atom ONCE
    print("\nPriming canonical-trace cache...")
    for name, Z, N, _ in ATOMS:
        t0 = time.time()
        ta, tf = _cached_canonical(Z, N)
        print(f"  {name}: |tr_atom|={abs(ta):.4f}, |tr_free|={abs(tf):.4f}, "
              f"{time.time()-t0:.1f}s")

    def _binding_cached(Z, N, n_brane_levels, pair_mode):
        """Like binding_canonical_plus_multibrane, but canonical cached."""
        A = Z + N
        ta, tf = _cached_canonical(Z, N)
        canonical_term = abs(tf) - abs(ta)
        tower_term = 0.0
        per_level = []
        if n_brane_levels >= 1:
            V_a_0 = per_gen_V_hat_aggregated(Z, N, include_inter=True)
            V_f_0 = per_gen_V_hat_aggregated(Z, N, include_inter=False)
            for n in range(1, n_brane_levels + 1):
                V_a = lift_V_markov(V_a_0, n)
                V_f = lift_V_markov(V_f_0, n)
                m_a = tower_mass_level(V_a, pair_mode=pair_mode)
                m_f = tower_mass_level(V_f, pair_mode=pair_mode)
                delta = m_f - m_a
                tower_term += delta
                per_level.append({"level": n, "delta": delta})
        B = E_0_BETA_DECAY_MEV * (canonical_term + tower_term)
        return {"Z": Z, "N": N, "A": A, "n_brane_levels": n_brane_levels,
                 "pair_mode": pair_mode,
                 "canonical_contribution_MeV": E_0_BETA_DECAY_MEV * canonical_term,
                 "tower_contribution_MeV": E_0_BETA_DECAY_MEV * tower_term,
                 "B_MeV": B, "per_level": per_level,
                 "tr_M_atom": ta, "tr_M_free": tf}

    for pair_mode in ["adjacent", "full"]:
        for n_levels in [0, 1, 2, 5, 10]:
            print(f"\n-- pair_mode = {pair_mode}, "
                  f"n_brane_levels = {n_levels} --")
            print(f"  {'Atom':>6} {'A':>3} {'B_AME':>8} "
                  f"{'B_canon':>10} {'B_tower':>10} {'B_total':>10} "
                  f"{'|Δm/m|%':>10}")
            print("  " + "-" * 80)
            for name, Z, N, B_AME in ATOMS:
                A = Z + N
                try:
                    t0 = time.time()
                    r = _binding_cached(Z, N, n_levels, pair_mode)
                    dt = time.time() - t0
                    dm = (abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
                           if math.isfinite(r["B_MeV"])
                           else float("nan"))
                    print(f"  {name:>6} {A:>3} {B_AME:>8.3f} "
                          f"{r['canonical_contribution_MeV']:>+10.4f} "
                          f"{r['tower_contribution_MeV']:>+10.4f} "
                          f"{r['B_MeV']:>+10.4f} "
                          f"{dm:>9.4f}%  "
                          f"({dt:.1f}s)")
                    results.append({**r, "atom": name,
                                     "B_AME_MeV": B_AME,
                                     "delta_m_over_m_pct": dm})
                except Exception as e:
                    print(f"  {name:>6} ERR: {type(e).__name__}: "
                          f"{str(e)[:60]}")

    witness = {
        "computation": "canonical-plus-multibrane",
        "description": (
            "Canonical Jones-Markov trace (level 0) PLUS multi-brane "
            "Φ_q tower (levels 1..N) per prop:categorical-mass-"
            "markov's full formula 𝔪 = |tr_M| + Σ ‖Φ_q(z_i)‖.  "
            "Level 0 uses markov_trace_canonical.tr_M_element (7/7 "
            "prop-table values).  Levels 1..N use aggregated V̂ (Σ_λ "
            "w_λ V̂_i^λ) with Markov-stabilization jet lift V̂^(n) = "
            "z^n V̂^(0).  Aggregated-BEFORE-Φ_q ordering matches the "
            "prop's letter (Φ_q nonlinearity breaks per-irrep-then-"
            "sum).  Proper Kähler-differential jet lift is open."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV},
        "results": results,
    }
    out = Path(__file__).parent / "canonical-plus-multibrane.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
