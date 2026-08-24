#!/usr/bin/env python3
"""
Catalan-G binding probe — literal paper formula.

Tests the binding formula from prop:binding-scale-catalan +
thm:wedderburn-mass-formula (paper, verbatim):

    α = m_e · 8G                            ≈ 3.7445 MeV
    M(Z, N) = Z·m_p + N·m_n + Z·m_e + α · Σ_i ln|V̂_i^{full}|
    B(Z, N) = -α · Σ_i ln|V̂_i^{full}|    (for bound atom, Φ < 0)

where V̂_i^{full} is the Plancherel-weighted Wedderburn combination
at generator i:

    V̂_i^{full} = w_sym · V̂_i^{sym} + w_std · V̂_i^{std} + w_alt · V̂_i^{alt}

and G = Σ(-1)^k/(2k+1)² ≈ 0.91597 is Catalan's constant (geometric
invariant = Vol(𝓑_3)/8, the Borromean hyperbolic volume divided by
its two ideal octahedra).

Also tests the tower-binding variant (prop:tower-binding-energy):

    B = Σ_{λ ∈ {sym, std, alt}} w_λ · m_e · Σ_i ln|Φ_q(V̂_i^λ)|

(per-block Φ_q with log outside, summed over three Wedderburn channels).

Compares both formulas against AME on D, T, ³He, ⁴He.  No fitting; α
is fixed.  If either formula reproduces AME to <0.1%, the "density ×
hyperbolic volume" picture is validated at the atomic binding scale.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from _precision import set_compute_dps  # noqa: E402 — raise dps before any mpmath value
import sys
import json
import math
from pathlib import Path
from mpmath import mp
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0
from hecke_core import atom_per_generator_volumes, w_sym, w_std, w_alt, Phi_q
from codata_constants import (
    M_E_MEV as _M_E_MEV,
    M_P_MEV_VALIDATION as _M_P_MEV,
    M_N_MEV_VALIDATION as _M_N_MEV,
)

HBAR_Q = (q0 - 1.0) / q0
HBAR_Q_SQ = HBAR_Q * HBAR_Q

# Catalan's constant G ≈ 0.91597 — Dirichlet L(2, χ_{-4})
CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G    # 7.32772475...

# CODATA inputs — sourced from `codata_constants` (P31 audit: no
# hardcoded literals). float() cast for legacy compatibility with the
# downstream f64-based arithmetic in this script.
M_E_MEV = float(_M_E_MEV)
M_P_MEV = float(_M_P_MEV)
M_N_MEV = float(_M_N_MEV)

# Binding scale from paper
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN  # = 3.74447... MeV


# This producer USED to run at mpmath's default 15 dps, which is why the
# padding / raw-float64 / import-time gates all passed it: what it emitted
# was honestly float64, with no fake precision to detect. It raises working
# precision on the next line now. NOTE the M_E/M_P/M_N above are still cast
# down deliberately (see their comment) and CATALAN_G is a 30-digit literal
# a float64 cannot hold -- the downstream arithmetic here remains f64.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def phi_atom_wedderburn(Z: int, N: int, include_inter: bool = True) -> float:
    """Σ_i ln|V̂_i^{full}| for the atom's braid (paper: wedderburn formula).

    V̂_i^{full} = w_sym·V_i^sym + w_std·V_i^std + w_alt·V_i^alt, aggregated.
    ln|V̂| < 0 for small V̂ (bound state); ln|V̂| > 0 for large V̂.
    """
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    total = 0.0
    for v in vols:
        Vf = v["full"]
        if abs(Vf) < 1e-30:
            return float("-inf")
        total += mp.log(abs(Vf))
    return total


def phi_atom_tower_per_block(Z: int, N: int,
                                include_inter: bool = True
                                ) -> dict:
    """Σ_λ w_λ · Σ_i ln|Φ_q(V̂_i^λ)| split per Wedderburn block."""
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)

    def _log_phi(v):
        a = abs(v)
        if a >= q0 * 0.995:
            a = q0 * 0.995
        try:
            p = Phi_q(a)
            if p <= 0 or not math.isfinite(p):
                return 0.0
            return mp.log(p)
        except Exception:
            return 0.0
    sym_sum = sum(_log_phi(v["sym"]) for v in vols)
    std_sum = sum(_log_phi(v["std"]) for v in vols)
    alt_sum = sum(_log_phi(v["alt"]) for v in vols)
    return {
        "sym": w_sym * sym_sum,
        "std": w_std * std_sum,
        "alt": w_alt * alt_sum,
        "total": w_sym * sym_sum + w_std * std_sum + w_alt * alt_sum,
    }


if __name__ == "__main__":
    import time
    start_time = time.monotonic()
    print("=" * 100)
    print("CATALAN-G BINDING PROBE — paper's ρ·Vol formula, no fitting")
    print("=" * 100)
    print(f"  Catalan G      = {CATALAN_G:.15f}")
    print(f"  Vol(𝓑_3) = 8G = {VOL_BORROMEAN:.10f}  (geometric invariant)")
    print(f"  m_e           = {M_E_MEV} MeV  (density = lepton scale)")
    print(f"  α = m_e · 8G  = {ALPHA_MEV:.6f} MeV  (binding scale)")
    print(f"  q₀, ℏ_q²      = {q0:.4f}, {HBAR_Q_SQ:.4e}")
    print("=" * 100)

    # AME binding energies from the CANONICAL accessor, not hand-typed.
    # These were six literals, and every one of them disagreed with the
    # vendored AME2020 table:
    #     6Li   32.0       vs 31.9939872    -> 0.006013 MeV  (1.9e-4 rel)
    #     D      2.22452   vs  2.2245662    -> 4.62e-5 MeV
    #     T      8.481821  vs  8.4817962    -> 2.48e-5 MeV
    #     4He   28.295674  vs 28.2956624    -> 1.16e-5 MeV
    #     12C   92.161728  vs 92.1617352    -> 7.2e-6 MeV
    #     3He    7.71804   vs  7.71804132   -> 1.32e-6 MeV
    # `6Li = 32.0` is a rounded placeholder, off by 200x the next worst.
    # This is the exact failure `codata_constants.ame_binding_mev`'s docstring
    # warns about -- consumers over a TABLE of nuclides hand-typing what the
    # accessor provides -- and worse than the mass_table_ppb.py case it cites
    # (up to 1.6e-5). B_AME and err_pct in this witness MOVE as a result;
    # they were wrong before.
    from codata_constants import ame_binding_mev as _ame_b  # noqa: E402
    ATOMS = [
        (name, Z, N, _ame_b(Z, Z + N))
        for (name, Z, N) in (("D", 1, 1), ("T", 1, 2), ("3He", 2, 1),
                             ("4He", 2, 2), ("6Li", 3, 3), ("12C", 6, 6))
    ]

    # ── Formula 1: Wedderburn-aggregated log form ──────────
    print("\n" + "=" * 80)
    print("FORMULA 1: B = -α · Σ_i ln|V̂_i^full(atom)|")
    print("  (wedderburn-mass-formula; V̂_i^full = aggregated via w_λ)")
    print("=" * 80)
    print(f"  {'atom':>6} {'B_AME':>10} {'Φ_atom':>14} {'Φ_free':>14} "
          f"{'ΔΦ':>12} {'B_pred':>10} {'err_%':>10}")
    results_f1 = []
    for name, Z, N, B_AME in ATOMS:
        try:
            phi_atom = phi_atom_wedderburn(Z, N, include_inter=True)
            phi_free = phi_atom_wedderburn(Z, N, include_inter=False)
            delta_phi = phi_atom - phi_free
            # B = -α · (ln difference).  Sign: bound atoms have smaller |V̂|
            # → ln|V̂| more negative → Φ_atom < Φ_free → ΔΦ < 0 → -α·ΔΦ > 0.
            B_pred = -ALPHA_MEV * delta_phi
            err = ((B_pred - B_AME) / B_AME * 100
                    if B_AME else float("nan"))
            print(f"  {name:>6} {B_AME:>10.4f} {phi_atom:>+14.4f} "
                  f"{phi_free:>+14.4f} {delta_phi:>+12.4f} "
                  f"{B_pred:>+10.4f} {err:>+9.3f}%")
            results_f1.append({"atom": name, "Z": Z, "N": N,
                                 "A": Z + N, "B_AME": B_AME,
                                 "phi_atom": phi_atom,
                                 "phi_free": phi_free,
                                 "delta_phi": delta_phi,
                                 "B_pred_MeV": B_pred,
                                 "err_pct": err})
        except Exception as e:
            print(f"  {name:>6}: ERR {type(e).__name__}: {str(e)[:60]}")

    # ── Formula 2b: per-block Φ_q log on ATOM braid only (no free subtraction)
    print("\n" + "=" * 80)
    print("FORMULA 2b: B = Σ_λ w_λ · m_e · Σ_i ln|Φ_q(V̂_i^{atom,λ})|")
    print("  (tower-binding-energy as written; atom-only, no free subtraction)")
    print("=" * 80)
    print(f"  {'atom':>6} {'B_AME':>10} {'sym':>12} {'std':>12} "
          f"{'alt':>12} {'total':>12} {'B_pred':>10} {'err_%':>10}")
    results_f2b = []
    for name, Z, N, B_AME in ATOMS:
        try:
            pa = phi_atom_tower_per_block(Z, N, include_inter=True)
            B_pred = M_E_MEV * pa["total"]
            err = float(((B_pred - B_AME) / B_AME * 100)
                    if B_AME else float("nan"))
            print(f"  {name:>6} {B_AME:>10.4f} "
                  f"{float(pa['sym']):>+12.4f} {float(pa['std']):>+12.4f} "
                  f"{float(pa['alt']):>+12.4f} {float(pa['total']):>+12.4f} "
                  f"{float(B_pred):>+10.4f} {err:>+9.3f}%")
            results_f2b.append({"atom": name, "Z": Z, "N": N,
                                  "A": Z + N, "B_AME": B_AME,
                                  "phi_atom_total": float(pa["total"]),
                                  "B_pred_MeV": float(B_pred),
                                  "err_pct": err})
        except Exception as e:
            print(f"  {name:>6}: ERR {type(e).__name__}: {str(e)[:60]}")

    # ── Formula 2: per-block Φ_q log (tower-binding-energy) ─
    print("\n" + "=" * 80)
    print("FORMULA 2: B = Σ_λ w_λ · m_e · Σ_i [ln|Φ_q(V̂_i^λ)|_atom - ln|..|_free]")
    print("  (tower-binding-energy; per-Wedderburn-block Φ_q inside log)")
    print("=" * 80)
    print(f"  {'atom':>6} {'B_AME':>10} {'sym':>12} {'std':>12} "
          f"{'alt':>12} {'total':>12} {'B_pred':>10} {'err_%':>10}")
    results_f2 = []
    for name, Z, N, B_AME in ATOMS:
        try:
            pa = phi_atom_tower_per_block(Z, N, include_inter=True)
            pf = phi_atom_tower_per_block(Z, N, include_inter=False)
            d = {k: pa[k] - pf[k] for k in pa}
            B_pred = M_E_MEV * d["total"]
            err = ((B_pred - B_AME) / B_AME * 100
                    if B_AME else float("nan"))
            print(f"  {name:>6} {B_AME:>10.4f} "
                  f"{d['sym']:>+12.4f} {d['std']:>+12.4f} "
                  f"{d['alt']:>+12.4f} {d['total']:>+12.4f} "
                  f"{B_pred:>+10.4f} {err:>+9.3f}%")
            results_f2.append({"atom": name, "Z": Z, "N": N,
                                 "A": Z + N, "B_AME": B_AME,
                                 "delta_block_sym": d["sym"],
                                 "delta_block_std": d["std"],
                                 "delta_block_alt": d["alt"],
                                 "delta_total": d["total"],
                                 "B_pred_MeV": B_pred,
                                 "err_pct": err})
        except Exception as e:
            print(f"  {name:>6}: ERR {type(e).__name__}: {str(e)[:60]}")

    witness = {
        "computation": "catalan-binding",
        "description": (
            "Paper's literal binding formula using Catalan's constant G "
            "(= Vol(𝓑_3)/8, Borromean hyperbolic volume invariant).  "
            "Two formulas tested: (1) Wedderburn-aggregated log form "
            "B = -α·ΣΔln|V̂^full| with α = m_e·8G ≈ 3.7445 MeV; (2) "
            "per-block Φ_q tower form B = m_e·Σ_λ w_λ·ΣΔln|Φ_q(V̂^λ)|.  "
            "Neither formula has any free parameters — α is fixed by "
            "Catalan's constant (no fitting).  Validates the 'density "
            "(m_e) × volume (8G)' interpretation if numerically accurate."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "Catalan_G": CATALAN_G,
            "Vol_Borromean": VOL_BORROMEAN,
            "m_e_MeV": M_E_MEV,
            "m_p_MeV": M_P_MEV,
            "m_n_MeV": M_N_MEV,
            "alpha_MeV": ALPHA_MEV,
            "q0": q0, "hbar_q_sq": HBAR_Q_SQ,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
        },
        "formula_1_wedderburn_log": results_f1,
        "formula_2_tower_per_block": results_f2,
        "formula_2b_tower_atom_only": results_f2b,
    }
    # Wrap legacy payload via WitnessBuilder.wrap_legacy for provenance
    sys.path.insert(0, str(Path(__file__).parent))
    from witness_base import WitnessBuilder  # noqa: E402
    (WitnessBuilder
        .wrap_legacy("catalan-binding", witness,
                     script_path=__file__, engine="python",
                     start_time=start_time)
        .save())
    out = Path(__file__).parent / "catalan-binding.witness.json"
    print(f"\n  Witness: {out}")
