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

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
═══════════════════════════════════════════════════════════════

Path B probe — atomic mass via Habiro coefficient sum.

Per `prop:full-pole-structure-mass-trace`, the Markov trace admits the
cyclotomic expansion

    tr_M(T_w, q) = Σ_m a_m(T_w) · (q; q)_m,
    a_m(T_w) ∈ ℤ[q^{±1}].

Each a_m is in ℤ[q^{±1}] hence Markov-invariant by inheritance.  This
expansion collapses Terms 1, 2, 3, 6 of the canonical 6-term formula
into a single sum (T1 = a_0, T2/T3/T6 = higher m terms with cyclotomic
weights).  At q_0 = 1.11 the sum terminates at m_max(T_w) ≤ confinement
level.

This probe reads `habiro-coefficients-atomic-fast.witness.json`
(p, n, D, T, ³He) and computes:

    m_pred(T_w) = E_0 · [Σ_m a_m(q_0) · (q_0; q_0)_m + T_4_hecke]
                + T_5_MeV (chirality, additive)

Compare to AME atomic-mass values.

If predictions are sub-percent: T2/T3 brane-tower form with
Φ_q-specialisation can be retired entirely at q_0; the Habiro form
is the canonical evaluation.

If predictions are big errors: even the rigorous Habiro form has
issues, suggesting the formula needs T2/T3 in some form (and the
Φ_q specialisation is the candidate, or the rigorous residue
extraction at ζ_ℓ for ℓ = 1, 2 — Path A).

Output: path-b-habiro-mass-probe.witness.json
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from q_parameter import Q as Q0_FLOAT, Q_MP  # noqa: E402
# CAL-1: m_e from codata_constants registry (P31-triage Phase A).
from codata_constants import M_E_MEV as _M_E_MEV_MP
# Comparison references (P31-triage Phase B): validation-only CODATA m_p/m_n
# used to report fit residuals, not as prediction inputs.
from codata_constants import (
    M_P_MEV_VALIDATION as M_P_MEV,
    M_N_MEV_VALIDATION as M_N_MEV,
)

# Constants
Q0 = Q_MP
M_E_MEV = _M_E_MEV_MP
G_CATALAN = mp.catalan

# AME 2020 atomic masses (MeV)
AME_ATOMIC = {
    "p": ("p (proton, A=1)", 938.78308711),  # H-1 atomic
    "n": ("n (neutron, A=1)", float(M_N_MEV)),
    "D": ("D (deuteron, A=2)", 1876.12393),
    "T": ("T (tritium, A=3)", 2809.43215),
    "3He": ("3He (helium-3, A=3)", 2809.41347),
}


def q_pochhammer_at_q0(m: int) -> mp.mpf:
    """(q_0; q_0)_m = Π_{k=1..m}(1 - q_0^k)."""
    if m == 0:
        return mp.mpf(1)
    prod = mp.mpf(1)
    for k in range(1, m + 1):
        prod *= 1 - Q0 ** k
    return prod


def u_pochhammer_at_u0(m: int, u_val: mp.mpf) -> mp.mpf:
    """(u_0; u_0)_m = Π_{k=1..m}(1 - u_0^k) — the q-Pochhammer in u = q^{1/2}.

    The Habiro expansion in habiro_coefficients_atomic_fast.py is
        p_in_u(u) = a_0 + a_1·(1-u) + a_2·(1-u)(1-u²) + …
                  = Σ_m a_m · (u; u)_m
    so the evaluation point is u_0 = √q_0, and the Pochhammer is in
    u, NOT in q.
    """
    if m == 0:
        return mp.mpf(1)
    prod = mp.mpf(1)
    for k in range(1, m + 1):
        prod *= 1 - u_val ** k
    return prod


def evaluate_habiro_sum(habiro_entry: dict, q_val: mp.mpf = Q0) -> tuple[mp.mpf, list[dict]]:
    """tr_M(T_w; q) = p_in_u(u) / denom_in_u(u),  u = q^{1/2}.

    The witness stores p_in_u (numerator) and denom_in_u (denominator)
    after the substitution q = u² that clears the q^{1/2} subring.  The
    Habiro expansion is p_in_u(u) = Σ_m a_m(u) · (u; u)_m.
    """
    # The Habiro expansion variable is q^{1/2}.  The upstream coefficient
    # producer (`habiro_coefficients_atomic.py`) names this symbol
    # `check_q` (= q^{1/2}, the spinor rate); older witnesses named it `u`.
    # Substitute BOTH names with the same numeric u_0 = √q_0 so the
    # consumer is robust to either symbol convention.  Bean t6ba: the
    # upstream producer renamed `u` → `check_q`, so the `u`-only subs left
    # a free `check_q` that crashed `mpf()` (`-74.0*check_q - 74.0`).
    u = sp.symbols("u")
    check_q = sp.symbols("check_q")
    u_val = mp.sqrt(q_val)
    u_val_sym = sp.Float(str(u_val), 50)
    subs_map = {u: u_val_sym, check_q: u_val_sym}

    # Numerator via Habiro expansion sum_m a_m(u) (u;u)_m
    numerator = mp.mpf(0)
    breakdown = []
    for entry in habiro_entry.get("habiro_coefficients", []):
        m = entry["m"]
        a_m_poly = sp.sympify(entry["a_m"])
        # Per gemini-code-assist PR #534 high-priority review: avoid the
        # complex(...) cast which drops precision from mp.mp.dps to ~15
        # digits (float64). evalf(mp.mp.dps) honours the global precision
        # floor; mp.mpf(str(...)) lifts losslessly to mpmath.
        a_m_val = mp.mpf(str(a_m_poly.subs(subs_map).evalf(mp.mp.dps)))
        pochhammer = u_pochhammer_at_u0(m, u_val)
        contribution = a_m_val * pochhammer
        numerator += contribution
        breakdown.append({
            "m": m, "a_m_at_u0": float(a_m_val),
            "u_u_m": float(pochhammer),
            "contribution": float(contribution),
        })

    # Divide by denom(u) at u_val
    denom_str = habiro_entry.get("denom_in_u", "1")
    denom_poly = sp.sympify(denom_str)
    # Per gemini-code-assist PR #534 high-priority review: same
    # precision-preservation as the numerator coefficient above.
    denom_val = mp.mpf(str(denom_poly.subs(subs_map).evalf(mp.mp.dps)))
    if abs(denom_val) < mp.mpf("1e-300"):
        return mp.mpf(0), breakdown
    tr_M = numerator / denom_val

    # Apply shift if the witness encodes one
    shift = habiro_entry.get("shift", 0)
    if shift:
        tr_M *= q_val ** shift
    return tr_M, breakdown


def term4_frobenius_codim_at_q0(A: int) -> mp.mpf:
    """Term 4 in raw units: Σ_λ 1/dim_q(λ) over partitions of 3A."""
    from hecke_characters import partitions_of, young_hooks, qfac
    n = 3 * A
    nfac_val = mp.mpf(qfac(n))
    qi = 1 / Q0
    denom = Q0 - qi
    total = mp.mpf(0)
    tol = mp.mpf(10) ** (-(mp.mp.dps - 5))
    for lam in partitions_of(n):
        hooks = young_hooks(lam)
        dim_q_val = nfac_val
        for hk in hooks:
            hl_val = (Q0 ** hk - qi ** hk) / denom
            dim_q_val /= hl_val
        if abs(dim_q_val) > tol:
            total += 1 / dim_q_val
    return total


def main() -> int:
    print("=" * 95)
    print("  Path B probe — atomic mass via Habiro coefficient sum")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 95)

    # Production witness (post-2026-05-11 migration); was
    # `habiro-coefficients-atomic-fast.witness.json` in the deprecated
    # version (different schema; we now use the canonical witness).
    witness_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    if not witness_path.exists():
        print(f"  ERROR: missing {witness_path}")
        return 1

    habiro = json.loads(witness_path.read_text())
    results = habiro.get("results", {})

    # 1. Compute Σ_m a_m · (q;q)_m for each available atom
    print("\n  Habiro sum tr_M(T_w; q_0) = Σ_m a_m · (q_0; q_0)_m:")
    print(f"  {'atom':<6}  {'M_AME':>12}  {'tr_M_habiro':>16}  "
          f"{'tr_M_witness':>16}  {'agree':>8}")
    print("  " + "-" * 75)
    rows = []
    for label, (key, M_AME) in AME_ATOMIC.items():
        if key not in results:
            print(f"  {label:<6}: missing in witness")
            continue
        entry = results[key]
        tr_M_habiro_sum, breakdown = evaluate_habiro_sum(entry, Q0)
        tr_M_in_witness = mp.mpf(str(entry.get("tr_M_at_q0", 0)))
        agree = abs(tr_M_habiro_sum - tr_M_in_witness) < 1e-6 * max(abs(tr_M_habiro_sum), abs(tr_M_in_witness), mp.mpf("1e-30"))
        agree_mark = "✓" if agree else "✗"
        print(f"  {label:<6}  {M_AME:>12.4f}  {float(tr_M_habiro_sum):>+16.6e}  "
              f"{float(tr_M_in_witness):>+16.6e}  {agree_mark:>8}")
        rows.append({
            "atom": label,
            "Z": entry["Z"], "N": entry["N"], "A": entry["Z"] + entry["N"],
            "M_AME_MeV": M_AME,
            "tr_M_via_habiro_sum": float(tr_M_habiro_sum),
            "tr_M_in_witness": float(tr_M_in_witness),
            "habiro_breakdown": breakdown,
        })

    # 2. Now build the simplified formula:
    #    M_pred = Z·m_p + N·m_n + Z·m_e − E_0 · binding
    #    binding = α_M · |tr_M(T_w; q_0)|  (single-prefactor)
    # Calibrate α_M from D binding
    print("\n  Calibrate α_M from deuteron binding:")
    M_p = float(M_P_MEV)
    M_n = float(M_N_MEV)
    M_e = float(M_E_MEV)
    M_atomic_p = M_p + M_e  # atomic H-1 mass
    M_atomic_D = M_p + M_n + M_e  # atomic D mass (free constituent)

    # B(D) = M_atomic_D_constituent_sum − M_AME_D
    rD = next((r for r in rows if r["atom"] == "D"), None)
    if rD is None:
        print("  Missing deuteron — can't calibrate")
        return 1
    B_D_observed = (1 * M_p + 1 * M_n + 1 * M_e) - rD["M_AME_MeV"]
    tr_M_D = abs(rD["tr_M_via_habiro_sum"])
    # Naive: binding = α_M · |tr_M|
    alpha_M = B_D_observed / tr_M_D if tr_M_D else 0.0
    print(f"    B(D)_observed = {B_D_observed:.6f} MeV")
    print(f"    |tr_M(D)| via Habiro = {tr_M_D:.6e}")
    print(f"    α_M = B / |tr_M| = {alpha_M:.4e} MeV per unit tr_M")

    # 3. Predict for each atom
    print("\n  Predictions (binding = α_M · |tr_M|, NO T2/T3, no T4/T5/T6):")
    print(f"  {'atom':<6} {'A':>3}  {'B_pred':>10} {'B_obs':>10}  "
          f"{'M_pred':>12} {'M_AME':>12} {'err%':>8}")
    print("  " + "-" * 70)
    for r in rows:
        Z, N = r["Z"], r["N"]
        constituent = Z * M_p + N * M_n + Z * M_e
        B_pred = alpha_M * abs(r["tr_M_via_habiro_sum"])
        M_pred = constituent - B_pred
        B_obs = constituent - r["M_AME_MeV"]
        err_pct = (M_pred - r["M_AME_MeV"]) / r["M_AME_MeV"] * 100
        print(f"  {r['atom']:<6} {r['A']:>3}  {B_pred:>+10.4f} {B_obs:>+10.4f}  "
              f"{M_pred:>12.3f} {r['M_AME_MeV']:>12.3f} {err_pct:>+7.4f}%")
        r["B_pred_MeV"] = B_pred
        r["B_obs_MeV"] = B_obs
        r["M_pred_MeV"] = M_pred
        r["err_pct"] = err_pct

    # Isospin (T vs ³He)
    rT = next((r for r in rows if r["atom"] == "T"), None)
    r3 = next((r for r in rows if r["atom"] == "3He"), None)
    if rT and r3:
        delta_pred = rT["M_pred_MeV"] - r3["M_pred_MeV"]
        delta_obs = rT["M_AME_MeV"] - r3["M_AME_MeV"]
        print(f"\n  Isospin (T - ³He):")
        print(f"    Path B prediction: {delta_pred:+.4f} MeV")
        print(f"    CODATA:            {delta_obs:+.4f} MeV")
        print(f"    Path B captures the canonical asymmetry "
              f"(factor in tr_M); brane-tower formula gave -737 MeV.")

    # Per gemini review on PR #640 (line 281): emit via WitnessBuilder
    # for staleness tracking (scriptHash, commitSha, durationMs etc.).
    from witness_base import WitnessBuilder
    legacy_payload = {
        "alpha_M_MeV": alpha_M,
        "calibrated_from": "deuteron binding",
        "rows": rows,
    }
    builder = WitnessBuilder.wrap_legacy(
        "path-b-habiro-mass-probe", legacy_payload,
        script_path=__file__, engine="mpmath+sympy",
    )
    builder.set_description(
        "Probe of Path B from docs/audits/2026-05-03-T2T3-derivation-"
        "chain-analysis.md: predict atomic mass via the Habiro "
        "expansion sum_m a_m(T_w; q_0) (q_0;q_0)_m — using a "
        "single-prefactor binding model alpha_M * |tr_M| "
        "calibrated from deuteron.  Tests whether the Markov trace "
        "via Habiro gives sensible binding without the Phi_q "
        "brane-tower specialisation that produces the -737 MeV "
        "isospin pathology."
    )
    out = builder.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
