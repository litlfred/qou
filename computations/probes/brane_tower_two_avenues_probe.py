#!/usr/bin/env python3
"""
T2/T3 brane-tower — explore two avenues for restoring isospin invariance.

Per-channel Φ_q probe (`brane_tower_per_channel_phi_q.py`) was a
NEGATIVE result — it flips the sign of the isospin violation but
doesn't resolve it.  Two structural avenues remain (gist:
https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4):

AVENUE 1: Kähler-derivative on global tr_M(β).
  Use kahler_lift's recursive sp.diff to compute ∂/∂q tr_M(β) on
  the full atomic braid (not per-generator).  Test whether the
  Kähler derivative restores trace-invariance and whether
  d/dq tr_M(T) = d/dq tr_M(³He) under isospin.

AVENUE 2: Frobenius-antipode global symmetrization.
  Define
      T2_sym(β) := ½ (T2_legacy(β) + T2_legacy(S(β)))
  where S sends σ ↔ σ⁻¹ (the Frobenius antipode on Hecke).  For
  the production atom_per_generator_volumes construction, the
  per-strand (c, d) tables encode quark content via:
      uu pair → σ = (1, 0)
      dd pair → σ⁻¹ = (1, -h)
      ud pair → mixed = (1, -h/2)  [S-self-dual]
  Under the convention "u ↔ d under S", p (uud) ↔ n (udd) under S
  globally — so braid(T = 1p+2n) ↔ braid(³He = 2p+1n) under S.
  Therefore T2_sym(T) = T2_sym(³He) BY CONSTRUCTION; the
  symmetrization recovers isospin for mirror nuclei.  Question:
  does this give physically reasonable predictions for non-mirror
  cases (proton, neutron, deuteron, ⁴He)?

Output: brane-tower-two-avenues-probe.witness.json
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

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP  # noqa: E402
from hecke_core import (  # noqa: E402
    h as h_val, z as z_mark, W_SYM, W_STD, W_ALT,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from mass_endomorphism import Phi_q  # noqa: E402

Q0 = Q_MP
QI = Q_INV_MP
H_VAL = mp.mpf(str(float(h_val)))
Z_MARK = mp.mpf(str(float(z_mark)))


# ── Frobenius antipode S in (c, d) form ──
def apply_S(c: float, d: float) -> tuple[float, float]:
    """S: σ ↔ σ⁻¹.  In (c, d) form this maps:
        (1, 0)        ↔ (1, -h)
        (1, -h/2)     ↔ (1, -h/2)   (self-dual)
    Generic: c·σ + d ↦ c·(σ - h) + d = c·σ + (d - c·h).
    """
    h_f = float(H_VAL)
    return (float(c), float(d) - float(c) * h_f)


def per_gen_chain_volume_full(chain: list[tuple[float, float]]) -> mp.mpf:
    """|V̂_full| = |W_SYM·sp + W_STD·V_std + W_ALT·ap|."""
    a, b = mp.mpf(0), mp.mpf(1)
    sp, ap = mp.mpf(1), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a * cm * H_VAL + a * dm + b * cm, a * cm + b * dm
        sp = sp * (cm * Q0 + dm)
        ap = ap * (-cm * QI + dm)
    V_std = Z_MARK * a + b
    V_full = mp.mpf(str(W_SYM)) * sp + mp.mpf(str(W_STD)) * V_std + mp.mpf(str(W_ALT)) * ap
    return abs(V_full)


def atom_per_gen_chains(Z: int, N: int, include_inter: bool = True):
    A = Z + N
    if A < 1:
        return []
    ordering = ['p'] * Z + ['n'] * N
    n_gens_total = (3 * A - 1) if include_inter else (2 * A)
    chains = [[] for _ in range(n_gens_total)]
    for k, nuc in enumerate(ordering):
        intra_g0 = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        if include_inter:
            base_g0 = 3 * k
            base_g1 = 3 * k + 1
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        chains[base_g0].extend([(float(c), float(d)) for c, d in intra_g0])
        chains[base_g1].extend([(float(c), float(d)) for c, d in intra_g1])
    if include_inter:
        for k in range(A - 1):
            inter_pos = 3 * k + 2
            pair = (ordering[k], ordering[k + 1])
            if pair == ('p', 'p'):
                chains[inter_pos].append((1.0, 0.0))
            elif pair == ('n', 'n'):
                chains[inter_pos].append((1.0, -float(H_VAL)))
            else:
                chains[inter_pos].append((1.0, -float(H_VAL) / 2))
    return chains


def S_apply_to_chains(chains):
    """Apply Frobenius S to every (c, d) in every per-generator chain."""
    return [[apply_S(c, d) for c, d in ch] for ch in chains]


# ── T2 in three forms ──
def T2_legacy(chains) -> mp.mpf:
    total = mp.mpf(0)
    for ch in chains:
        if not ch:
            continue
        v = per_gen_chain_volume_full(ch)
        try:
            phi = Phi_q(v)
            if not mp.isinf(phi) and not mp.isnan(phi):
                total += phi
        except Exception:
            pass
    return total


def T2_S_symmetrized(chains) -> mp.mpf:
    """Avenue 2: T2_sym(β) := ½ (T2(β) + T2(S(β)))."""
    return (T2_legacy(chains) + T2_legacy(S_apply_to_chains(chains))) / 2


# ── Avenue 1: Kähler-derivative scaffold ──
def tr_M_global_at_q(chains, q_val: mp.mpf) -> mp.mpf:
    """Global Markov trace tr_M(β) = Π V̂_full_i over all generators i.

    This is the descended-trace "T1-style" form.  It IS Markov-invariant
    (per the canonical bridge witness; see PR #524 for the regression
    audit).  Used here as the base trace whose Kähler derivative is
    Avenue 1.
    """
    prod = mp.mpf(1)
    qi_val = 1 / q_val
    h_q = q_val - qi_val
    z_q = 1 / (mp.sqrt(q_val) + 1 / mp.sqrt(q_val))
    for ch in chains:
        if not ch:
            continue
        a, b = mp.mpf(0), mp.mpf(1)
        sp, ap = mp.mpf(1), mp.mpf(1)
        for c, d_in_chain in ch:
            cm = mp.mpf(c)
            dm = mp.mpf(d_in_chain)
            a, b = a * cm * h_q + a * dm + b * cm, a * cm + b * dm
            sp = sp * (cm * q_val + dm)
            ap = ap * (-cm * qi_val + dm)
        V_std = z_q * a + b
        V_full = mp.mpf(str(W_SYM)) * sp + mp.mpf(str(W_STD)) * V_std + mp.mpf(str(W_ALT)) * ap
        prod *= V_full
    return abs(prod)


def kahler_derivative_tr_M(chains, eps: mp.mpf = mp.mpf("1e-25")) -> mp.mpf:
    """∂/∂q tr_M(β) via central finite difference at q_0.

    Avenue 1's simplest reading: replace Φ_q-of-a-volume with the
    Kähler derivative of the global Markov trace.  Each derivative
    of a Markov-invariant trace is itself Markov-invariant.
    """
    f_plus = tr_M_global_at_q(chains, Q0 + eps)
    f_minus = tr_M_global_at_q(chains, Q0 - eps)
    return (f_plus - f_minus) / (2 * eps)


def kahler_2nd_derivative_tr_M(chains, eps: mp.mpf = mp.mpf("1e-15")) -> mp.mpf:
    f_plus = tr_M_global_at_q(chains, Q0 + eps)
    f_zero = tr_M_global_at_q(chains, Q0)
    f_minus = tr_M_global_at_q(chains, Q0 - eps)
    return (f_plus - 2 * f_zero + f_minus) / (eps ** 2)


# ── Sweep ──
def main() -> int:
    print("=" * 95)
    print("  T2/T3 brane-tower — exploring two avenues for trace-form restoration")
    print(f"  q_0 = {float(Q0):.10f}")
    print("=" * 95)

    atoms = [
        ("p", 1, 0, False),
        ("n", 0, 1, False),
        ("D", 1, 1, True),
        ("T", 1, 2, True),
        ("3He", 2, 1, True),
        ("4He", 2, 2, True),
    ]

    rows = []
    print("\n  AVENUE 2 — Frobenius-antipode global symmetrization of T2:")
    print(f"  {'iso':<6} {'A':>3}  {'T2_legacy':>14}  {'T2(S(β))':>14}  "
          f"{'T2_sym':>14}")
    print("  " + "-" * 65)
    for iso, Z, N, inter in atoms:
        chains = atom_per_gen_chains(Z, N, include_inter=inter)
        T2_orig = T2_legacy(chains)
        T2_S = T2_legacy(S_apply_to_chains(chains))
        T2_sym = (T2_orig + T2_S) / 2
        print(f"  {iso:<6} {Z + N:>3}  {float(T2_orig):>+14.4e}  "
              f"{float(T2_S):>+14.4e}  {float(T2_sym):>+14.4e}")
        rows.append({
            "iso": iso, "Z": Z, "N": N, "A": Z + N,
            "T2_legacy": float(T2_orig),
            "T2_S_image": float(T2_S),
            "T2_S_symmetrized": float(T2_sym),
        })

    # Avenue 2 isospin check: is T2_sym(T) == T2_sym(³He)?
    rT = next(r for r in rows if r["iso"] == "T")
    r3 = next(r for r in rows if r["iso"] == "3He")
    print("\n  Avenue 2 isospin check (T vs ³He):")
    print(f"    T2_legacy          T={rT['T2_legacy']:.4e}  ³He={r3['T2_legacy']:.4e}  Δ={r3['T2_legacy']-rT['T2_legacy']:+.4e}")
    print(f"    T2_S_image         T={rT['T2_S_image']:.4e}  ³He={r3['T2_S_image']:.4e}  Δ={r3['T2_S_image']-rT['T2_S_image']:+.4e}")
    print(f"    T2_S_symmetrized   T={rT['T2_S_symmetrized']:.4e}  ³He={r3['T2_S_symmetrized']:.4e}  Δ={r3['T2_S_symmetrized']-rT['T2_S_symmetrized']:+.4e}")
    delta_sym = r3["T2_S_symmetrized"] - rT["T2_S_symmetrized"]
    delta_legacy = r3["T2_legacy"] - rT["T2_legacy"]
    E_0 = 7.95e-4
    print(f"    Legacy ΔT2 × E_0 = {delta_legacy * E_0:+.4f} MeV")
    print(f"    Symmetrized ΔT2 × E_0 = {delta_sym * E_0:+.4f} MeV")
    print(f"    CODATA T - ³He = +0.019 MeV")

    # Verify the "S maps p↔n globally" claim
    print("\n  Verification: does S(braid(T)) = braid(³He)?")
    chains_T = atom_per_gen_chains(1, 2, include_inter=True)
    chains_3He = atom_per_gen_chains(2, 1, include_inter=True)
    chains_T_S = S_apply_to_chains(chains_T)
    T2_T_S = T2_legacy(chains_T_S)
    T2_3He = T2_legacy(chains_3He)
    print(f"    T2(S(T))  = {float(T2_T_S):.6e}")
    print(f"    T2(³He)   = {float(T2_3He):.6e}")
    print(f"    ratio     = {float(T2_T_S / T2_3He) if T2_3He else 'n/a':.6f}")
    if abs(float(T2_T_S / T2_3He) - 1) < 0.01:
        print(f"    ✓ S maps T's atomic braid onto ³He's (within 1%)")
    else:
        print(f"    ✗ S does NOT map T to ³He at the atomic-braid level")

    # AVENUE 1 — Kähler derivative of global tr_M
    print("\n" + "=" * 95)
    print("  AVENUE 1 — Kähler-derivative ∂/∂q [tr_M(β)] (finite-difference probe)")
    print("=" * 95)
    print(f"\n  {'iso':<6} {'A':>3}  {'tr_M(q_0)':>14}  {'∂/∂q tr_M':>14}  "
          f"{'∂²/∂q² tr_M':>14}")
    print("  " + "-" * 65)
    kahler_rows = []
    for iso, Z, N, inter in atoms:
        chains = atom_per_gen_chains(Z, N, include_inter=inter)
        if not chains:
            continue
        try:
            t_start = time.time()
            tr_q0 = tr_M_global_at_q(chains, Q0)
            d1 = kahler_derivative_tr_M(chains)
            d2 = kahler_2nd_derivative_tr_M(chains)
            dt = time.time() - t_start
            print(f"  {iso:<6} {Z + N:>3}  {float(tr_q0):>+14.4e}  "
                  f"{float(d1):>+14.4e}  {float(d2):>+14.4e}  ({dt:.2f}s)")
            kahler_rows.append({
                "iso": iso, "Z": Z, "N": N, "A": Z + N,
                "tr_M_global_at_q0": float(tr_q0),
                "d_dq_tr_M": float(d1),
                "d2_dq2_tr_M": float(d2),
            })
        except Exception as e:
            print(f"  {iso:<6}: ERROR {type(e).__name__}: {e}")

    # Avenue 1 isospin check: is d/dq tr_M(T) = d/dq tr_M(³He)?
    if any(r["iso"] == "T" for r in kahler_rows) and any(r["iso"] == "3He" for r in kahler_rows):
        rT_k = next(r for r in kahler_rows if r["iso"] == "T")
        r3_k = next(r for r in kahler_rows if r["iso"] == "3He")
        print("\n  Avenue 1 isospin check (T vs ³He):")
        print(f"    tr_M(T)              = {rT_k['tr_M_global_at_q0']:.6e}")
        print(f"    tr_M(³He)            = {r3_k['tr_M_global_at_q0']:.6e}")
        print(f"    ∂/∂q tr_M(T)         = {rT_k['d_dq_tr_M']:+.4e}")
        print(f"    ∂/∂q tr_M(³He)       = {r3_k['d_dq_tr_M']:+.4e}")
        print(f"    ∂²/∂q² tr_M(T)       = {rT_k['d2_dq2_tr_M']:+.4e}")
        print(f"    ∂²/∂q² tr_M(³He)     = {r3_k['d2_dq2_tr_M']:+.4e}")

    # Verdict
    print("\n" + "=" * 95)
    print("  VERDICT")
    print("=" * 95)
    print("\n  Avenue 2 (Frobenius-antipode T2 symmetrization):")
    print(f"    Legacy T2 isospin violation:    {delta_legacy * E_0:+.2f} MeV (T - ³He)")
    print(f"    Symmetrized T2 isospin violation: {-delta_sym * E_0:+.2f} MeV (T - ³He)")
    if abs(delta_sym) < abs(delta_legacy) / 10:
        print(f"    ✓ Symmetrization reduces violation by ~10× or more")
    elif abs(delta_sym) < abs(delta_legacy) / 2:
        print(f"    ◇ Symmetrization improves but doesn't fully resolve")
    else:
        print(f"    ✗ Symmetrization doesn't help materially")

    print("\n  Avenue 1 (Kähler-derivative on global tr_M):")
    print("    Diagnostic probe — full integration into 6-term formula")
    print("    requires re-deriving how Φ_q ↔ ∂/∂q tr_M maps onto T2 + T3.")
    print("    Key observation: tr_M(β) IS Markov-invariant, so any derivative")
    print("    or integral expression in tr_M is also trace-invariant.")

    witness = {
        "computation": "brane-tower-two-avenues-probe",
        "description": (
            "Concrete numerical exploration of two avenues for restoring "
            "Markov-invariance to T2/T3.  Avenue 2 (Frobenius-antipode "
            "T2_sym = (T2(beta) + T2(S(beta)))/2) and Avenue 1 (Kahler "
            "derivative of global tr_M(beta))."
        ),
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "avenue_2_T2_sym": rows,
        "avenue_2_isospin_T_minus_3He_legacy_MeV": -delta_legacy * E_0,
        "avenue_2_isospin_T_minus_3He_sym_MeV": -delta_sym * E_0,
        "avenue_1_kahler_derivatives": kahler_rows,
        "codata_T_minus_3He_MeV": 0.019,
    }
    out = HERE / "brane-tower-two-avenues-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
