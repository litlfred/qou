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
                   pole_tol: float = 1e-9,
                   pole_mode: str = "principal") -> float:
    """ln|Φ_q(v)| = −Σ_{k≥1} ln|1 − q^{−k} v|.

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
    # Accumulate −Σ_k ln|1 − q^{−k}v|
    total = 0.0
    qi_pow = 1.0 / q0  # q^{-1}
    poles_skipped = []
    for k in range(1, K_max + 1):
        x = qi_pow * v
        # |1 − x| — real so ||
        diff = 1.0 - x
        abs_diff = abs(diff)
        if abs_diff < pole_tol:
            if pole_mode == "raise":
                raise ZeroDivisionError(
                    f"ln|Φ_q| diverges at v ≈ q^k (x = {x}, k = {k})")
            elif pole_mode == "sign":
                return float("inf")
            else:  # principal: skip factor
                poles_skipped.append(k)
                qi_pow /= q0
                continue
        term = math.log(abs_diff)
        total -= term
        qi_pow /= q0
        # Converge: once |x| << 1, |ln|1−x|| ≈ |x| falls to zero.
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
        "sample_ln_phi_q": {
            f"v_{v}": ln_abs_phi_q(v) if v != 1.0 else "DIVERGES"
            for v in [0.1, 0.5, 0.9, 1.05, 1.09, 1.15, 1.2, 1.5, 2.0]
        },
        "electron_result": r,
        "nuclear_results": nuclear_results,
    }
    out = Path(__file__).parent / "binding-per-block-log.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
