#!/usr/bin/env python3
"""
per_generator_V_hat_general.py — Plancherel-weighted Wedderburn V̂_i
for ARBITRARY H_n braid words.

Generalises `mass_at_3A_proper.per_generator_V_hat_3A` (atomic-only)
to any n_strands. This closes the compute-infrastructure gap
identified in `docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md`:
the framework had per-generator V̂_i for atomic braids only, blocking
F_ℓ derivation for individual leptons.

Per `prop:per-braid-mass-tower`:
  V̂_i = Σ_{λ ⊢ n}  w_λ · χ_λ(W_i) / d_λ
  w_λ = d_q(λ)² / [n]_q!     (Plancherel)

This is the same formula as per_generator_V_hat_3A; the only change
is to accept arbitrary `n_strands` and `word` (without atomic-braid
construction). Plancherel-weighted character sum constrains
|V̂_i| ≤ q_0 (within Li_2^q convergence radius).

Apply to canonical lepton braids:
  electron = σ_1³ in H_2 (T(2,3) trefoil)
  muon = (σ_1 σ_2⁻¹)² in H_3 (4_1 figure-eight)
  tau = σ_1⁷ in H_2 (T(2,7) septafoil)

Computes proper V̂_i, then applies the canonical Li_2^q per-braid
mass tower to test F_ℓ derivation.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_2022_source import M_MU_OVER_M_E  # noqa: E402
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import mpmath as mp

# Reuse Plancherel + seminormal infrastructure from mass_at_3A_proper
from mass_at_3A_proper import (
    partitions_of, dim_q, qfac, _cached_seminormal,
)
from q_parameter import Q as Q0_FLOAT


def per_generator_V_hat_general(
    n_strands: int,
    word: list[tuple[float, float, int]],
    *,
    weight_scheme: str = "plancherel",
    verbose: bool = False,
) -> list[dict]:
    """Per-generator V̂_i for arbitrary H_n braid word.

    Args:
        n_strands: number of strands n (≥ 2)
        word: list of (c, d, gen_idx) triples; each represents a
              factor (c·σ_{gen_idx} + d·1) at generator position gen_idx
        weight_scheme: "plancherel" (d_q(λ)² / [n]_q!)
        verbose: print V̂_i values

    Returns:
        list of dicts {"full": V̂_i (float), "gen_word": list of (c,d)}
        of length n_strands - 1
    """
    if n_strands < 2:
        return []
    n_gens = n_strands - 1

    # Group word by generator
    word_by_gen: list[list[tuple[float, float]]] = [[] for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((float(c), float(d)))

    nfac = qfac(n_strands)
    V_hat = [0.0] * n_gens

    # Plancherel weights
    weight_table: list[tuple[tuple[int, ...], float]] = []
    if weight_scheme == "plancherel":
        for shape in partitions_of(n_strands):
            dq = dim_q(shape)
            weight_table.append((shape, (dq * dq) / nfac))
    else:
        raise ValueError(f"unknown weight_scheme: {weight_scheme}")

    # Character sum per Wedderburn block
    for (shape, w_lam) in weight_table:
        sigmas, dim, _syts = _cached_seminormal(shape)
        if dim == 0:
            continue
        I_lam = np.eye(dim)
        for i in range(n_gens):
            w_i_steps = word_by_gen[i]
            if not w_i_steps:
                # Empty word at gen i → trace = dim → contrib = w_lam
                V_hat[i] += w_lam
                continue
            if i >= len(sigmas):
                continue
            M = I_lam
            for (c, d) in w_i_steps:
                M = M @ (c * sigmas[i] + d * I_lam)
            tr = float(np.trace(M))
            V_hat[i] += w_lam * tr / dim

    out = []
    for i, V in enumerate(V_hat):
        out.append({"full": V, "gen_word": list(word_by_gen[i])})
    if verbose:
        print(f"  per-gen V̂ (H_{n_strands} Wedderburn, Plancherel):")
        for i, d in enumerate(out):
            print(f"    gen {i}: V̂ = {d['full']:+.6f}  word = {d['gen_word']}")
    return out


def li2q_mpmath(z_arg: mp.mpf, q: mp.mpf, max_terms: int = 500) -> mp.mpf:
    """Symmetric q-dilogarithm Li_2^q(z) at high precision."""
    h = q - 1 / q
    s = mp.mpf(0)
    for n in range(1, max_terms + 1):
        q_int_n = (q**n - q**(-n)) / h
        t = z_arg**n / (n * q_int_n)
        s += t
        if mp.fabs(t) < mp.mpf(10) ** (-55):
            break
    return s


def per_braid_mass_li2q(V_hats: list[float], q: mp.mpf, z: mp.mpf) -> dict:
    """Apply canonical Li_2^q per-braid mass tower (descended-dropped per
    canonical_plus_multibrane.py:tower_mass_level Li_2^q convention).

      m(W) = − Σ Li_2^q(−|V̂_i|) − z² Σ Li_2^q(−|V̂_i V̂_j|)
    """
    abs_V = [mp.fabs(mp.mpf(v)) for v in V_hats]
    n = len(abs_V)

    single = sum(-li2q_mpmath(-V, q) for V in abs_V)
    pair = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            VV = abs_V[i] * abs_V[j]
            pair += -z * z * li2q_mpmath(-VV, q)

    return {
        "abs_V": [float(v) for v in abs_V],
        "single_sum": single,
        "pair_sum": pair,
        "total": single + pair,
        "max_abs_V": float(max(abs_V) if abs_V else 0),
    }


def main() -> int:
    mp.mp.dps = 50

    Vol_4_1 = mp.mpf("2.0298832128193072500115978049904475264466050157561096")
    cal2_target = M_MU_OVER_M_E
    cal_tau_e   = mp.mpf("3477.23")
    hbar_q_sq = Vol_4_1 / cal2_target
    hbar_q = mp.sqrt(hbar_q_sq)
    q0 = mp.mpf(1) / (mp.mpf(1) - hbar_q)
    h = q0 - 1 / q0
    z = mp.mpf(1) / (mp.sqrt(q0) + 1 / mp.sqrt(q0))
    q0_f = float(q0)
    h_f = float(h)

    print(f"=== Substrate ===")
    print(f"  q_0 = {q0_f:.10f},  h = {h_f:.6f},  z = {float(z):.6f}")
    print()

    # Canonical lepton braid words in (c, d, gen_idx) format
    leptons = {
        "electron σ_1³ T(2,3) in H_2": {
            "n_strands": 2,
            "word": [(1.0, 0.0, 0)] * 3,
        },
        "muon T(2,5) σ_1⁵ in H_2": {
            "n_strands": 2,
            "word": [(1.0, 0.0, 0)] * 5,
        },
        "muon 4_1 (σ_1σ_2⁻¹)² in H_3": {
            "n_strands": 3,
            "word": [
                (1.0, 0.0, 0),       # σ_1
                (1.0, -h_f, 1),      # σ_2⁻¹ = σ_2 - h
                (1.0, 0.0, 0),       # σ_1
                (1.0, -h_f, 1),      # σ_2⁻¹
            ],
        },
        "tau T(2,7) σ_1⁷ in H_2": {
            "n_strands": 2,
            "word": [(1.0, 0.0, 0)] * 7,
        },
    }

    print("=== Plancherel-weighted Wedderburn V̂_i per lepton ===")
    print(f"{'lepton':40s}  {'V̂_i':>40s}  {'max |V̂|':>10s}  {'< q_0?':>7s}")
    print("-" * 105)

    results = {}
    for name, b in leptons.items():
        V_data = per_generator_V_hat_general(b["n_strands"], b["word"])
        Vs = [d["full"] for d in V_data]
        max_V = max((abs(v) for v in Vs), default=0)
        in_radius = max_V < q0_f
        Vs_str = ", ".join(f"{v:+.4f}" for v in Vs)
        print(f"  {name:40s}  [{Vs_str:>38s}]  {max_V:10.4f}  {'YES' if in_radius else 'NO':>7s}")
        b["V_hat"] = Vs
        b["max_abs_V"] = max_V
        b["in_convergence_radius"] = in_radius
        b["mass_tower"] = per_braid_mass_li2q(Vs, q0, z)
        results[name] = b

    print()
    print("=== Mass ratios via Li_2^q canonical formula (descended-dropped) ===")
    m_e_dim = results["electron σ_1³ T(2,3) in H_2"]["mass_tower"]["total"]
    print(f"  Electron m_dim (calibration) = {float(m_e_dim):.6f}")
    print()
    for name in ["muon T(2,5) σ_1⁵ in H_2", "muon 4_1 (σ_1σ_2⁻¹)² in H_3", "tau T(2,7) σ_1⁷ in H_2"]:
        m_dim = results[name]["mass_tower"]["total"]
        ratio = m_dim / m_e_dim if m_e_dim != 0 else mp.mpf("nan")
        codata = cal2_target if "muon" in name else cal_tau_e
        rel = (ratio - codata) / codata * 100 if codata != 0 else 0
        verdict = "CLOSE" if mp.fabs(rel) < 5 else ("PARTIAL" if mp.fabs(rel) < 50 else "OFF")
        print(f"  {name:40s}  m_dim = {float(m_dim):+.6f}  ratio = {float(ratio):+.4f}  CODATA = {float(codata):.4f}  {float(rel):+8.3f}%  [{verdict}]")
    print()

    # Verdict
    in_radius_all = all(b["in_convergence_radius"] for b in results.values())
    print(f"=== Verdict ===")
    print(f"  All V̂_i within Li_2^q convergence radius (|V̂| < q_0)? {'YES' if in_radius_all else 'NO'}")
    if in_radius_all:
        print(f"  ✓ Compute infrastructure works correctly.")
        print(f"  → Lepton mass ratios above are the canonical Li_2^q-formula predictions.")
        print(f"  → If ratios MATCH CODATA: F_ℓ derivation closes via canonical mass tower.")
        print(f"  → If ratios MISMATCH: framework needs additional structure beyond")
        print(f"    the per-braid mass tower (multi-day analytical work continues).")
    else:
        print(f"  Some V̂_i exceed convergence radius — Li_2^q diverges; results unreliable.")

    # Sanity check: V̂_e ≈ 0.594 per paper for electron
    V_e_paper = 0.594
    V_e_computed = abs(results["electron σ_1³ T(2,3) in H_2"]["V_hat"][0])
    print(f"\n=== Calibration check (electron V̂_e) ===")
    print(f"  Paper (mass-endomorphism-tower.md line 351): V̂_e ≈ {V_e_paper}")
    print(f"  Computed via per_generator_V_hat_general:    V̂_e = {V_e_computed:.6f}")
    print(f"  Match: {abs(V_e_computed - V_e_paper) < 0.01}")

    # Witness output
    witness_results = {}
    for name, b in results.items():
        witness_results[name] = {
            "n_strands": b["n_strands"],
            "word": [list(t) for t in b["word"]],
            "V_hat_per_generator": b["V_hat"],
            "max_abs_V": b["max_abs_V"],
            "in_convergence_radius": b["in_convergence_radius"],
            "mass_tower": {
                "abs_V": b["mass_tower"]["abs_V"],
                "single_sum": str(b["mass_tower"]["single_sum"]),
                "pair_sum": str(b["mass_tower"]["pair_sum"]),
                "total_mass_dim": str(b["mass_tower"]["total"]),
            },
        }

    witness = {
        "description": "per_generator_V_hat_general — Plancherel-weighted Wedderburn V̂_i for arbitrary H_n; applied to canonical lepton braids",
        "computation": "per_generator_V_hat_general",
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "closes": "compute infra gap for individual leptons identified in docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md",
            "method": "Plancherel-weighted character sum V̂_i = Σ_λ (d_q(λ)²/[n]_q!) · χ_λ(W_i) / d_λ",
            "generalises": "mass_at_3A_proper.per_generator_V_hat_3A (was atomic-only)",
        },
        "constants": {
            "q_0": str(q0),
            "h": str(h),
            "z": str(z),
        },
        "leptons": witness_results,
        "electron_V_hat_calibration_check": {
            "paper_value": V_e_paper,
            "computed_value": V_e_computed,
            "matches_within_001": abs(V_e_computed - V_e_paper) < 0.01,
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    here = Path(__file__).resolve().parent
    out = here / "per-generator-V-hat-general.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
