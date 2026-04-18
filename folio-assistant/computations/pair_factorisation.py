#!/usr/bin/env python3
"""
Pair-factorisation probe: traced V̂_{ij} vs scalar V̂_i · V̂_j.

The current tower formula uses Φ_q(|V̂_i V̂_j|) where V̂_i V̂_j is a
SCALAR product of two already-traced numbers.  This implicitly
assumes
    tr_M(ρ^λ(σ_i σ_j)) = tr_M(ρ^λ(σ_i)) · tr_M(ρ^λ(σ_j))
which holds only for 1-dim irreps.  For non-1-dim λ (which dominate
at n ≥ 6) the character does not factor, and the missing correlation

    Δ_{ij}^λ = tr_M(ρ^λ(σ_i σ_j)) − tr_M(ρ^λ(σ_i)) · tr_M(ρ^λ(σ_j))

contributes to mass error.  Hypothesis: T/³He divergence at Kähler
order ≥ 1 is driven by Δ_{ij}^λ accumulating when the lift amplifies
V̂_i V̂_j.

This module computes V̂_{ij} via per-irrep matrix products in the
seminormal basis and provides a probe sweep against the scalar-
factorisation default.
"""
from __future__ import annotations

import sys
import math
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from mass_endomorphism import z_mark
from hecke_characters import (build_seminormal_matrices, partitions_of,
                                dim_q, qfac, standard_young_tableaux)
from mass_at_3A_proper import atom_braid_word_3A, phi_q_safe
from canonical_plus_multibrane import (HBAR_Q, HBAR_Q_SQ,
                                          E_0_BETA_DECAY_MEV,
                                          per_gen_V_hat_aggregated,
                                          lift_V_markov)
from markov_trace_canonical import tr_M_element
from binding_canonical import build_atom_symbolic
from hecke_symbolic import SymbolicHeckeDivision, q as q_sym
import sympy as sp


def per_irrep_M_position(shape: tuple[int, ...], i: int,
                            factors: list[tuple[float, float]],
                            sigmas: list[np.ndarray],
                            dim: int) -> np.ndarray:
    """M_i^λ = Π_k (c_k σ_i^λ + d_k I) as d_λ × d_λ matrix.

    factors: list of (c_k, d_k) at generator position i.
    sigmas:  list of σ_j^λ matrices, indexed σ_1, σ_2, ...
    """
    if not factors:
        return np.eye(dim)
    sig_i = sigmas[i]
    if hasattr(sig_i, "toarray"):
        sig_i = sig_i.toarray()
    M = np.eye(dim)
    for (c, d) in factors:
        block = c * sig_i + d * np.eye(dim)
        M = M @ block
    return M


def per_irrep_V_pair(Z: int, N: int, shape: tuple[int, ...], *,
                       include_inter: bool = True,
                       m_pp: int = 1, m_pn: int = 1,
                       m_nn: int = 1) -> tuple[list[float], dict]:
    """Per-irrep V̂_i^λ AND V̂_{ij}^λ via full matrix products.

    Returns (V_lin, V_pair) where:
      V_lin[i]      = tr_λ(M_i^λ) / d_λ          (matches per_irrep_V_hat)
      V_pair[(i,j)] = tr_λ(M_i^λ M_j^λ) / d_λ    (NEW — true pair trace)
    """
    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    n_gens = n_strands - 1

    word_by_gen: list[list[tuple[float, float]]] = [[]
                                                      for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((c, d))

    syts, _cells, _contents = standard_young_tableaux(shape)
    d_cl = len(syts)
    if d_cl == 0:
        return [0.0] * n_gens, {}

    sigmas, dim, _syts = build_seminormal_matrices(shape, sparse=False)
    if dim == 0 or len(sigmas) < n_gens:
        return [0.0] * n_gens, {}

    # Per-position matrices M_i^λ (kept in memory, d_λ × d_λ each)
    M_per_pos: list[np.ndarray] = []
    V_lin = [0.0] * n_gens
    for i in range(n_gens):
        if word_by_gen[i]:
            M_i = per_irrep_M_position(shape, i, word_by_gen[i],
                                          sigmas, dim)
        else:
            M_i = np.eye(dim)
        M_per_pos.append(M_i)
        V_lin[i] = float(np.trace(M_i)) / d_cl

    # Pair traces: tr(M_i M_j) / d_λ for i < j
    V_pair: dict[tuple[int, int], float] = {}
    for i in range(n_gens):
        Mi = M_per_pos[i]
        for j in range(i + 1, n_gens):
            Mj = M_per_pos[j]
            V_pair[(i, j)] = float(np.trace(Mi @ Mj)) / d_cl
    return V_lin, V_pair


def per_pair_V_hat_aggregated(Z: int, N: int, *,
                                 include_inter: bool = True,
                                 m_pp: int = 1, m_pn: int = 1,
                                 m_nn: int = 1
                                 ) -> tuple[list[float], dict]:
    """Plancherel-summed V̂_i AND V̂_{ij} across all λ ⊢ n_strands.

    Returns (V_lin, V_pair) where each is the Σ_λ w_λ · (·) aggregate.
    """
    A = Z + N
    if A < 1:
        return [], {}
    n_strands = 3 * A
    n_gens = n_strands - 1
    nfac = qfac(n_strands)
    V_lin = [0.0] * n_gens
    V_pair: dict[tuple[int, int], float] = {}
    for shape in partitions_of(n_strands):
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_lam = (dq * dq) / nfac
        V_l, V_p = per_irrep_V_pair(Z, N, shape,
                                       include_inter=include_inter,
                                       m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
        for i in range(n_gens):
            V_lin[i] += w_lam * V_l[i]
        for key, val in V_p.items():
            V_pair[key] = V_pair.get(key, 0.0) + w_lam * val
    return V_lin, V_pair


def tower_mass_level_traced(V_lin: list[float],
                              V_pair: dict[tuple[int, int], float],
                              *, pair_mode: str = "full",
                              cap_frac: float = 0.98) -> float:
    """Mass per jet level using TRUE pair traces (no scalar factorisation).

    Same formula as canonical_plus_multibrane.tower_mass_level, but
    Φ_q's argument is the actual Plancherel-summed tr_M(σ_i σ_j) per
    pair rather than the product of single traces.
    """
    n = len(V_lin)
    if n == 0:
        return 0.0
    desc = 1.0
    for v in V_lin:
        desc *= v
    desc = abs(desc)
    single = sum(phi_q_safe(abs(v), cap_frac=cap_frac) for v in V_lin)
    cross = 0.0
    if pair_mode == "adjacent":
        for i in range(n - 1):
            v_ij = V_pair.get((i, i + 1), 0.0)
            cross += z_mark ** 2 * phi_q_safe(abs(v_ij),
                                                 cap_frac=cap_frac)
    elif pair_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                v_ij = V_pair.get((i, j), 0.0)
                cross += z_mark ** 2 * phi_q_safe(abs(v_ij),
                                                    cap_frac=cap_frac)
    return desc + single + cross


def lift_V_pair_markov(V_pair: dict[tuple[int, int], float],
                          level: int) -> dict[tuple[int, int], float]:
    """Markov-stab lift on pair traces: V̂_{ij}^{(n)} = z^{2n} V̂_{ij}^{(0)}.

    Two factors of z per level (one per generator position in the
    pair), matching the per-V̂ Markov-stab rule V̂_i^{(n)} = z^n V̂_i^{(0)}
    when applied to the operator product M_i M_j.
    """
    if level == 0:
        return dict(V_pair)
    factor = z_mark ** (2 * level)
    return {k: v * factor for k, v in V_pair.items()}


def binding_pair_traced(Z: int, N: int, *,
                          mode: str = "traced",
                          pair_mode: str = "full",
                          E_0: float = E_0_BETA_DECAY_MEV,
                          include_canonical: bool = False,
                          verbose: bool = False) -> dict:
    """Tower-only binding (default) with optional traced-product pair term.

    mode ∈ {"scalar", "traced"}:
      "scalar" — Φ_q(|V̂_i V̂_j|) using V̂_i = single traces (default
                  matches canonical_plus_multibrane).
      "traced" — Φ_q(|V̂_{ij}|) using V̂_{ij} = Plancherel-summed
                  tr(ρ^λ(σ_i σ_j)).

    The canonical term is the SAME under both modes (only the tower
    cross-term differs).  By default we omit it — the scalar-vs-traced
    delta is what the probe needs.  Pass include_canonical=True for a
    full B_pred number (slow at n ≥ 9).
    """
    A = Z + N
    if A < 1:
        return {"status": "trivial"}
    n_strands = 3 * A

    canonical_MeV = 0.0
    if include_canonical:
        div = SymbolicHeckeDivision()
        ae = build_atom_symbolic(Z, N, include_inter=True)
        fe = build_atom_symbolic(Z, N, include_inter=False)
        ae, _ = div.reduce(ae)
        fe, _ = div.reduce(fe)
        ta = complex(sp.N(tr_M_element(ae, n_strands).subs(q_sym, Q0)))
        tf = complex(sp.N(tr_M_element(fe, n_strands).subs(q_sym, Q0)))
        if abs(ta.imag) < 1e-9:
            ta = ta.real
        if abs(tf.imag) < 1e-9:
            tf = tf.real
        canonical_term = abs(tf) - abs(ta)
        canonical_MeV = E_0 * canonical_term

    # ── Tower at level 1 with chosen pair-term mode ────────
    if mode == "traced":
        V_a_lin, V_a_pair = per_pair_V_hat_aggregated(
            Z, N, include_inter=True)
        V_f_lin, V_f_pair = per_pair_V_hat_aggregated(
            Z, N, include_inter=False)
        # Markov-stab lift level 1
        V_a_lin_1 = [v * z_mark for v in V_a_lin]
        V_f_lin_1 = [v * z_mark for v in V_f_lin]
        V_a_pair_1 = lift_V_pair_markov(V_a_pair, 1)
        V_f_pair_1 = lift_V_pair_markov(V_f_pair, 1)
        m_a = tower_mass_level_traced(V_a_lin_1, V_a_pair_1,
                                          pair_mode=pair_mode)
        m_f = tower_mass_level_traced(V_f_lin_1, V_f_pair_1,
                                          pair_mode=pair_mode)
    else:
        # Scalar (current default) — reuse canonical_plus_multibrane path
        from canonical_plus_multibrane import tower_mass_level
        V_a_0 = per_gen_V_hat_aggregated(Z, N, include_inter=True)
        V_f_0 = per_gen_V_hat_aggregated(Z, N, include_inter=False)
        V_a_1 = lift_V_markov(V_a_0, 1)
        V_f_1 = lift_V_markov(V_f_0, 1)
        m_a = tower_mass_level(V_a_1, pair_mode=pair_mode)
        m_f = tower_mass_level(V_f_1, pair_mode=pair_mode)

    delta_1 = m_f - m_a
    tower_MeV = E_0 * HBAR_Q_SQ * delta_1
    B = canonical_MeV + tower_MeV

    return {
        "Z": Z, "N": N, "A": A, "mode": mode, "pair_mode": pair_mode,
        "E_0_MeV": E_0,
        "canonical_MeV": canonical_MeV,
        "tower_delta_1_cat": delta_1,
        "tower_MeV": tower_MeV,
        "B_MeV": B,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1, 2.22452),
        ("T",   1, 2, 8.481821),
        ("3He", 2, 1, 7.71804),
    ]
    # Pre-cached canonical contribution per (Z,N) from
    # unified-lift.witness.json — same number under scalar AND traced
    # modes (only the tower term differs), so we can skip the slow
    # Hecke-reduced canonical evaluation here.
    CANONICAL_MEV = {(1, 1): 0.4655, (1, 2): 0.6287, (2, 1): 0.6578}
    print("=" * 100)
    print("PAIR-FACTORISATION PROBE")
    print(f"q₀ = {Q0}, ℏ_q = {HBAR_Q:.4f}, "
          f"E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("Compares scalar V̂_i V̂_j vs traced V̂_{ij} = "
          "Σ_λ w_λ tr(ρ^λ(σ_i σ_j)) / d_λ")
    print("Canonical Markov term is the SAME under both modes "
          "(cached from unified-lift.witness)")
    print("=" * 100)

    results = []
    for mode in ["scalar", "traced"]:
        print(f"\n--- mode = {mode}, pair_mode = full ---")
        print(f"  {'Atom':>4} {'A':>3} {'B_AME':>9} "
              f"{'B_canon':>10} {'B_tower':>10} {'B_total':>10} "
              f"{'|Δm/m|%':>9} {'time':>7}")
        print("  " + "-" * 80)
        for name, Z, N, B_AME in ATOMS:
            A = Z + N
            try:
                t0 = time.time()
                r = binding_pair_traced(Z, N, mode=mode,
                                           pair_mode="full",
                                           include_canonical=False)
                dt = time.time() - t0
                # Inject cached canonical
                canon = CANONICAL_MEV.get((Z, N), 0.0)
                B_total = canon + r["tower_MeV"]
                r = {**r, "canonical_MeV": canon, "B_MeV": B_total}
                dm = (abs(B_total - B_AME) / (A * 938.272) * 100
                       if math.isfinite(B_total)
                       else float("nan"))
                print(f"  {name:>4} {A:>3} {B_AME:>9.4f} "
                      f"{canon:>+10.4f} "
                      f"{r['tower_MeV']:>+10.4f} "
                      f"{B_total:>+10.4f} "
                      f"{dm:>8.4f}% "
                      f"{dt:>6.1f}s")
                results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                                 "delta_m_over_m_pct": dm,
                                 "time_sec": dt})
            except Exception as e:
                print(f"  {name:>4}: ERR {type(e).__name__}: "
                      f"{str(e)[:80]}")

    # Summary: scalar-vs-traced delta on tower contribution
    print(f"\n{'=' * 80}")
    print("DELTA: traced − scalar (tower only)")
    print("=" * 80)
    print(f"  {'Atom':>4} {'tower_scalar':>14} {'tower_traced':>14} "
          f"{'Δ_MeV':>10} {'Δ_keV':>10}")
    by_atom: dict = {}
    for r in results:
        by_atom.setdefault(r["atom"], {})[r["mode"]] = r["tower_MeV"]
    for atom, modes in by_atom.items():
        s = modes.get("scalar", 0)
        t = modes.get("traced", 0)
        d = t - s
        print(f"  {atom:>4} {s:>+14.4f} {t:>+14.4f} {d:>+10.4f} "
              f"{d*1000:>+10.2f}")

    witness = {
        "computation": "pair-factorisation-probe",
        "description": (
            "Pair-factorisation probe.  Compares scalar V̂_i · V̂_j "
            "(default in tower_mass_level) against traced V̂_{ij} = "
            "Σ_λ w_λ tr(ρ^λ(σ_i σ_j))/d_λ via per-irrep seminormal "
            "matrix products.  If traced reduces T/³He error ≥ 5×, "
            "the residual at Kähler order 1+ is scalar-factorisation "
            "and the all-pairs cross-term should be migrated to the "
            "traced form.  Single brane level (n=1), pair_mode=full."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                        "n_brane_levels": 1,
                        "pair_mode": "full"},
        "results": results,
    }
    out = Path(__file__).parent / "pair-factorisation-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
