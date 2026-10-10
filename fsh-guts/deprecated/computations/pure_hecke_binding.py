#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
Pure-Hecke binding formula from knot-factor-frobenius-pairing.md.

  B_bulk(Z, N) = E_0 · (|tr_M(W_free)| − |tr_M(W_atom)|)

where:
  W_free = disconnected-tensor baseline (no inter-nucleon crossings)
  W_atom = full atomic braid (with pp/pn/nn crossings)
  tr_M(W) = Σ_λ w_λ · χ_λ(W)/d_λ   (Plancherel-weighted trace,
                                      which equals Markov in the
                                      paper's convention at q₀)
  E_0 = 0.782 MeV (neutron β-decay Q-value, single calibration)

Paper's asserted verification (knot-factor-frobenius-pairing.md):
  A = 2 (D):   a = tr_M(W_atom)/tr_M(W_free) = 1 + h  (satellite chiral)
  A = 3 (T):   a = 1 − h² ≈ 0.956
  A = 3 (³He): a = 1 − h²
  A = 4 (⁴He): a = (1 − h²)²

This script:
  1. Builds W_free and W_atom character sums for each isotope
  2. Computes the Markov-trace ratio and difference
  3. Applies B = E_0 · (|tr_free| − |tr_atom|) as binding prediction
  4. Compares to CODATA binding energies
"""
from __future__ import annotations

import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 40

from hecke_core import atom_character_raw, _partition_table, _ensure_ysn_attached
from hecke_characters import partitions_of, dim_q, young_hooks, qfac
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

_ensure_ysn_attached()
_PT = _partition_table()

def _entries_for_k(k: int):
    return [e for e in _PT if e['k'] == k]

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
h = Q0 - QI           # Hecke deformation H_A
me = mp.mpf(str(M_E_MEV))
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
E0 = mp.mpf(str(Q_NEUTRON_MEV))  # 0.78233341 MeV (CODATA-derived)


def classical_dim(shape) -> int:
    n = sum(shape); hooks = young_hooks(shape)
    f = 1
    for k in range(2, n + 1): f *= k
    hp = 1
    for h_ in hooks: hp *= h_
    return f // hp


def _a_k_numerator_denominator(Z: int, N: int, include_inter: bool) -> tuple:
    """Paper formula (knot-factor-frobenius-pairing.md + jet-filtered-knot-factor.md):
        a_k(β) = [Σ_λ w_λ · χ_λ(β)] / [Σ_λ w_λ · d_λ]
    where w_λ = d_q(λ)²/[n]_q! (Plancherel) and d_λ is CLASSICAL
    (since Res^{H_k}_{H_3}(V_λ) has dim = d_λ as a vector space).

    Returns (numerator_mp, denominator_mp, n_partitions_used).
    """
    n_strands = 3 * (Z + N)
    if n_strands < 2:
        return mp.mpf(0), mp.mpf(1), 0
    nfac = mp.mpf(1)
    for k in range(2, n_strands + 1):
        nfac *= (Q0**k - QI**k) / (Q0 - QI)
    numerator = mp.mpc(0)
    denominator = mp.mpf(0)
    n_terms = 0
    entries = _entries_for_k(n_strands)
    for entry in entries:
        shape = entry['partition']
        try:
            dq = mp.mpf(str(float(dim_q(shape))))
        except Exception:
            continue
        if dq == 0:
            continue
        d_cl = mp.mpf(classical_dim(shape))
        w = dq * dq / nfac
        try:
            chi_q, log_norm, dim_cl_entry = atom_character_raw(Z, N, entry,
                                                          include_inter=include_inter)
        except Exception:
            continue
        chi_actual = mp.mpc(str(float(chi_q))) * mp.exp(mp.mpf(str(float(log_norm))))
        numerator   += w * chi_actual
        denominator += w * d_cl
        n_terms += 1
    return numerator, denominator, n_terms


def markov_trace(Z: int, N: int, include_inter: bool) -> tuple:
    """Compute raw Plancherel sum Σ w_λ·χ_λ/d_q (old — kept for compat)."""
    return _a_k_numerator_denominator(Z, N, include_inter)[:2]


def main() -> int:
    print("=" * 100)
    print("PURE-HECKE BINDING via knot-factor-Frobenius-pairing formula")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  E_0 (single calibration, neutron β-decay Q) = {float(E0)} MeV")
    print(f"  h = q − q⁻¹ = {float(h):.6f}")
    print()

    CODATA = {
        "D":    (1, 1, 2, 2.22456612),
        "T":    (1, 2, 3, 8.481798),
        "3He":  (2, 1, 3, 7.718058),
        "4He":  (2, 2, 4, 28.29566),
    }
    PAPER_A = {
        2: mp.mpf(1) + h,              # 1 + h for A=2 (chiral satellite)
        3: mp.mpf(1) - h*h,            # 1 − h² for A=3 (amphi 4_1)
        4: (mp.mpf(1) - h*h) ** 2,     # (1 − h²)² for A=4 (Borromean)
    }

    print(f"  {'iso':<5} {'Z':>2} {'N':>2} {'A':>2} "
          f"{'tr_M_free':>15} {'tr_M_atom':>15} {'a_ratio':>12} "
          f"{'a_paper':>12} {'B_pred':>10} {'B_AME':>10} {'err%':>8}")
    rows = []
    for iso, (Z, N, A, B_ame) in CODATA.items():
        tr_free, n_free = markov_trace(Z, N, include_inter=False)
        tr_atom, n_atom = markov_trace(Z, N, include_inter=True)
        abs_free = mp.fabs(tr_free)
        abs_atom = mp.fabs(tr_atom)
        B_pred = E0 * (abs_free - abs_atom)
        ratio_mp = abs_atom / abs_free if abs_free > 0 else mp.mpf(0)
        ratio = float(mp.re(ratio_mp))
        a_paper = PAPER_A.get(A, mp.mpf(1))
        B_pred_re = float(mp.re(B_pred))
        err = (B_pred_re - B_ame) / B_ame * 100
        print(f"  {iso:<5} {Z:>2} {N:>2} {A:>2} "
              f"{float(mp.re(abs_free)):>15.8f} {float(mp.re(abs_atom)):>15.8f} "
              f"{ratio:>12.8f} {float(a_paper):>12.8f} "
              f"{B_pred_re:>10.4f} {B_ame:>10.4f} {err:>+7.3f}%")
        rows.append({
            "isotope": iso, "Z": Z, "N": N, "A": A,
            "tr_free_abs": float(mp.re(abs_free)),
            "tr_atom_abs": float(mp.re(abs_atom)),
            "a_ratio": ratio,
            "a_paper": float(a_paper),
            "B_pred_MeV": B_pred_re,
            "B_AME_MeV": B_ame,
            "err_pct": err,
        })

    print()
    print("  Comparison: paper's asserted a(ρ) vs our computed ratio")
    print(f"  {'iso':<5} {'our ratio':>12} {'paper ratio':>12} {'diff':>10}")
    for r in rows:
        diff = float(r["a_ratio"]) - float(r["a_paper"])
        print(f"  {r['isotope']:<5} {float(r['a_ratio']):>12.8f} "
              f"{float(r['a_paper']):>12.8f} {diff:>+10.3e}")

    witness = {
        "computation": "pure-hecke-binding",
        "description": (
            "Pure-Hecke binding via paper's knot-factor-Frobenius-"
            "pairing formula: B = E_0·(|tr_M(W_free)|−|tr_M(W_atom)|), "
            "single calibration E_0 = 0.782 MeV.  Compares tr_M ratio "
            "a(N) to paper's asserted values 1+h (A=2), 1-h² (A=3), "
            "(1-h²)² (A=4).  No BW scaffolding."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
        "E_0_MeV": float(E0),
        "rows": rows,
    }
    out = Path(__file__).parent / "pure-hecke-binding.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
