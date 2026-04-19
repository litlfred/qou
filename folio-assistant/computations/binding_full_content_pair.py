#!/usr/bin/env python3
"""
Combined probe: production unified_lift pipeline with the SCALAR pair
term in tower_mass_level replaced by SYT-content-weighted V̂_{ij}.

Motivation (session handover):

  content_weighted_pair_probe moved T/3He toward AME under
  proton-calibrated E_0 + no Kähler.  The production pipeline
  (unified_lift.binding_unified) uses β-decay E_0, analytic Kähler
  lift, and a multi-level jet sum Σ_n ℏ_q^{2n} · Δm^{(n)} driven by
  Markov-stab iteration.  Scalar under production gives 0.018/0.06/
  0.03 % on D/T/3He at kahler_order=0 — the current ceiling.

  Does replacing the scalar pair V_i · V_j with the content-weighted
  V̂_{ij}^{content} under production (β-decay E_0 + Kähler + ℏ_q²)
  add constructively, or over-correct (like the traced-product path)?

Approach:

  The production `unified_lift.binding_unified` multi-level tower
  loop calls `tower_mass_level(V_n, pair_mode='full')` at each jet
  level n, where V_n is the Markov-stab-lifted per-generator volume
  (V_1 is the Kähler-corrected baseline; V_n = z^{n-1} · V_1 for
  n >= 2).

  Content-weighted V̂_{ij}^{content} is a LEVEL-1 object computed
  from the atom braid word via
  content_weighted_pair_probe.content_weighted_pair_term.  Its
  Markov-stab lift to level n scales as z^{2(n-1)} (two V̂ factors,
  each lifting as z^{n-1}).

  We precompute V̂_{ij}^{content} at level 1 once per atom (atom +
  free), then in the tower loop scale by z^{2(n-1)} at each level
  and use a modified tower_mass_level_content that replaces the
  scalar pair term.
"""
from __future__ import annotations

import sys
import json
import math
import time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from canonical_plus_multibrane import (HBAR_Q, HBAR_Q_SQ, z_mark,
                                          phi_q_safe, lift_V_markov,
                                          E_0_BETA_DECAY_MEV,
                                          tower_mass_level)
from kahler_lift import build_V_hat_symbolic
from unified_lift import unified_lift
from ocneanu_weights import tr_M_via_ocneanu_word
from content_weighted_pair_probe import content_weighted_pair_term


def tower_mass_level_content(V: list[float],
                               Vij: dict[tuple[int, int], float],
                               *, cap_frac: float = 0.98) -> float:
    """tower_mass_level with scalar pair replaced by content-weighted.

    Term 1 (descended): |Π V_i|  — unchanged
    Term 2 (single):    Σ_i Φ_q(|V_i|) — unchanged
    Term 3 (pair):      Σ_{i<j} z² · Φ_q(|V̂_{ij}^{content}|)  ← swapped
    """
    n = len(V)
    if n == 0:
        return 0.0
    desc = 1.0
    for v in V:
        desc *= v
    desc = abs(desc)
    single = sum(phi_q_safe(abs(v), cap_frac=cap_frac) for v in V)
    cross = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            vij = Vij.get((i, j))
            if vij is None:
                raise KeyError(f"Vij missing ({i},{j})")
            cross += z_mark ** 2 * phi_q_safe(abs(vij), cap_frac=cap_frac)
    return desc + single + cross


def binding_unified_content(Z: int, N: int, *,
                               pair_mode: str = "full",
                               kahler_order: int = 0,
                               E_0: float = E_0_BETA_DECAY_MEV,
                               jet_cap: int = 60,
                               target_ppm: float = 1.0,
                               verbose: bool = False) -> dict:
    """Production unified_lift binding with content-weighted pair.

    Clone of unified_lift.binding_unified with the pair term swapped.
    """
    A = Z + N
    n_strands = 3 * A
    n_gens = n_strands - 1

    # Canonical term (unchanged).
    t_canon = time.time()
    tr_atom = tr_M_via_ocneanu_word(Z, N, include_inter=True)
    tr_free = tr_M_via_ocneanu_word(Z, N, include_inter=False)
    canonical_MeV = E_0 * (abs(tr_free) - abs(tr_atom))
    canon_dt = time.time() - t_canon

    # Kähler-lifted V_i baseline (same as unified_lift.binding_unified).
    t_kahler = time.time()
    V_atom_sym = build_V_hat_symbolic(Z, N, include_inter=True)
    V_free_sym = build_V_hat_symbolic(Z, N, include_inter=False)
    a_lift = unified_lift(V_atom_sym, order=kahler_order)
    f_lift = unified_lift(V_free_sym, order=kahler_order)
    key = "V_markov" if kahler_order == 0 else f"V{kahler_order}"
    V_a_1 = a_lift[key]
    V_f_1 = f_lift[key]
    kahler_dt = time.time() - t_kahler

    # Content-weighted V̂_{ij} at level 1 (atom + free).
    t_content = time.time()
    Vij_atom: dict[tuple[int, int], float] = {}
    Vij_free: dict[tuple[int, int], float] = {}
    for i in range(n_gens):
        for j in range(i + 1, n_gens):
            Vij_atom[(i, j)] = content_weighted_pair_term(
                Z, N, (i, j), include_inter=True)
            Vij_free[(i, j)] = content_weighted_pair_term(
                Z, N, (i, j), include_inter=False)
    content_dt = time.time() - t_content
    if verbose:
        print(f"  content-pair precompute {len(Vij_atom)} pairs in "
              f"{content_dt:.1f}s")

    # Multi-level jet tower loop (matches unified_lift.binding_unified).
    n_strands_mev = n_strands * 938.272
    target_term_cat = (target_ppm * 1e-6 * n_strands_mev) / max(E_0, 1e-12)
    tower_term_cat = 0.0
    delta_1 = None
    jet_log = []
    n = 0
    V_a_n = list(V_a_1)
    V_f_n = list(V_f_1)
    Vij_a_n = dict(Vij_atom)
    Vij_f_n = dict(Vij_free)
    while n < jet_cap:
        n += 1
        if n > 1:
            V_a_n = lift_V_markov(V_a_1, n - 1)
            V_f_n = lift_V_markov(V_f_1, n - 1)
            # Pair scales as z^{2(n-1)} — two V̂ factors, each z^{n-1}.
            scale = z_mark ** (2 * (n - 1))
            Vij_a_n = {k: v * scale for k, v in Vij_atom.items()}
            Vij_f_n = {k: v * scale for k, v in Vij_free.items()}
        m_a_n = tower_mass_level_content(V_a_n, Vij_a_n)
        m_f_n = tower_mass_level_content(V_f_n, Vij_f_n)
        delta_n = m_f_n - m_a_n
        if delta_1 is None:
            delta_1 = delta_n
        term_n_cat = (HBAR_Q_SQ ** n) * delta_n
        tower_term_cat += term_n_cat
        jet_log.append({"level": n, "delta_n": delta_n,
                          "term_cat": term_n_cat,
                          "cumulative_cat": tower_term_cat})
        if abs(term_n_cat) < target_term_cat:
            break
    tower_MeV = E_0 * tower_term_cat

    eps_order = 3 + kahler_order
    eps_MeV = (HBAR_Q ** eps_order) * abs(delta_1) * E_0

    return {
        "Z": Z, "N": N, "A": A, "pair_form": "content-weighted",
        "kahler_order": kahler_order, "E_0_MeV": E_0,
        "canonical_MeV": canonical_MeV,
        "tower_delta_1_cat": delta_1,
        "tower_MeV": tower_MeV,
        "B_MeV": canonical_MeV + tower_MeV,
        "jet_levels_used": n,
        "jet_log": jet_log,
        "eps_MeV": eps_MeV,
        "eps_order": f"O(ℏ_q^{eps_order})",
        "canonical_time_sec": canon_dt,
        "kahler_time_sec": kahler_dt,
        "content_time_sec": content_dt,
    }


# ── CLI ─────────────────────────────────────────────────────

if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
    ]
    # Kähler order 0 is optimal on T/3He (see session P2.3 finding).
    ORDERS = [0]
    # For D, also include order=2 since it's stable there.
    ORDERS_D = [0, 2]

    print("=" * 110)
    print("PROBE: production unified_lift + CONTENT-WEIGHTED pair")
    print(f"q₀ = {Q0}, ℏ_q² = {HBAR_Q_SQ:.6f}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    from unified_lift import binding_unified

    results = []
    for ko in [0, 2]:
        print(f"\n{'=' * 80}")
        print(f"SCALAR (production unified_lift) — Kähler order {ko}")
        print("=" * 80)
        scalar_ref = {}
        for name, Z, N, B_AME in ATOMS:
            if ko == 2 and name in ("T", "3He"):
                continue  # order 2 diverges on T/3He (session P2.3)
            A = Z + N
            t0 = time.time()
            r = binding_unified(Z, N, pair_mode="full", kahler_order=ko)
            dt = time.time() - t0
            dm = abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
            scalar_ref[name] = {"B": r["B_MeV"], "err": dm, "t": dt,
                                  "canonical_MeV": r["canonical_MeV"],
                                  "tower_MeV": r["tower_MeV"]}
            print(f"  {name:>6} A={A} B_AME={B_AME:>8.3f} "
                  f"B_pred={r['B_MeV']:+10.4f} canon={r['canonical_MeV']:+.4f} "
                  f"tower={r['tower_MeV']:+.4f} err={dm:.4f}% ({dt:.1f}s)")

        print(f"\n{'=' * 80}")
        print(f"CONTENT-WEIGHTED pair — Kähler order {ko}")
        print("=" * 80)
        print(f"  {'Atom':>6} {'B_AME':>8} {'B_scalar':>10} "
              f"{'B_content':>10} {'err_s%':>9} {'err_c%':>9} "
              f"{'Δerr%':>10} {'time':>7}")
        print("  " + "-" * 86)
        for name, Z, N, B_AME in ATOMS:
            if ko == 2 and name in ("T", "3He"):
                continue
            A = Z + N
            t0 = time.time()
            try:
                r = binding_unified_content(Z, N, kahler_order=ko,
                                                verbose=False)
                dt = time.time() - t0
                dm_c = abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
                ref = scalar_ref[name]
                d_err = dm_c - ref["err"]
                print(f"  {name:>6} {B_AME:>8.3f} "
                      f"{ref['B']:>+10.4f} {r['B_MeV']:>+10.4f} "
                      f"{ref['err']:>8.4f}% {dm_c:>8.4f}% "
                      f"{d_err:>+9.4f}% {dt:>6.1f}s")
                results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                                 "err_content_pct": dm_c,
                                 "err_scalar_ref_pct": ref["err"],
                                 "delta_err_pct": d_err,
                                 "time_sec": dt})
            except Exception as e:
                print(f"  {name:>6} ERR: {type(e).__name__}: "
                      f"{str(e)[:80]}")

    witness = {
        "computation": "binding-full-content-pair-v2",
        "description": (
            "Production unified_lift.binding_unified with the scalar "
            "pair term swapped for content-weighted V̂_{ij}^{content} "
            "in every jet level.  Single-gen V_i remains Kähler-lifted "
            "per unified_lift; β-decay E_0 and ℏ_q² multi-level scaling "
            "unchanged.  Tests whether content-pair + Kähler is "
            "constructive or over-corrects."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "hbar_q_sq": HBAR_Q_SQ,
                        "E_0_MeV": E_0_BETA_DECAY_MEV,
                        "kahler_orders_tested": [0, 2]},
        "results": results,
    }
    out = Path(__file__).parent / "binding-full-content-pair.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
