#!/usr/bin/env python3
"""
Pure-Hecke binding via prefix-word per-level product.

Formula (knot-factor-frobenius-pairing.md + jet-filtered-knot-factor.md):

  a(Z,N) = Π_{k=3}^{3A} a_k(β_k)

with per-level ratio:

  a_k(β_k) = [Σ_{λ ⊢ k} w_λ^(k) · χ_λ(β_k)] / [Σ_{λ ⊢ k} w_λ^(k) · d_λ]

and final binding:

  B = E_0 · (1 − a(Z,N))  · ???   (need to match the paper's specific form)
   or
  B = E_0 · (|tr_free| − |tr_atom|)

where β_k is the PREFIX braid word at jet level k.

Three prefix interpretations tested:
  1. strand-cumulative  — use only generators σ_0..σ_{k-2}
  2. nucleon-cumulative — full atom at A' = k/3 (only k multiple of 3)
  3. order-of-generation — nucleon-by-nucleon as built in atom_gen_chains

SDP-based "best" prefix: deferred; treat this as exploratory.
"""
from __future__ import annotations

import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40

from hecke_core import (_partition_table, _ensure_ysn_attached,
                           atom_character_raw,)
from hecke_characters import dim_q, young_hooks, partitions_of
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
h = Q0 - QI
me = mp.mpf(str(M_E_MEV))
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
E0 = mp.mpf(str(Q_NEUTRON_MEV))  # 0.78233341 MeV (CODATA-derived)

_ensure_ysn_attached()
_PT = _partition_table()


def classical_dim(shape) -> int:
    n = sum(shape); hooks = young_hooks(shape)
    f = 1
    for k in range(2, n + 1): f *= k
    hp = 1
    for x in hooks: hp *= x
    return f // hp


def q_fact(n):
    out = mp.mpf(1)
    for k in range(2, n + 1):
        out *= (Q0**k - QI**k) / (Q0 - QI)
    return out


def a_k_ratio(Z: int, N: int, n_strands_override: int = None,
                include_inter: bool = True) -> tuple:
    """Compute a_k at level k = n_strands_override (or 3(Z+N)).

    Uses partition-table entries for that k and atom_character_raw
    with the given (Z, N), include_inter.
    """
    n_strands = n_strands_override if n_strands_override else 3 * (Z + N)
    if n_strands < 2:
        return mp.mpf(1), 0
    nfac = q_fact(n_strands)
    entries = [e for e in _PT if e['k'] == n_strands]
    if not entries:
        return None, 0
    num = mp.mpc(0)
    den = mp.mpf(0)
    nT = 0
    for entry in entries:
        shape = entry['partition']
        dq = mp.mpf(str(float(dim_q(shape))))
        if dq == 0: continue
        d_cl = mp.mpf(classical_dim(shape))
        w = dq * dq / nfac
        try:
            chi_q, log_norm, _ = atom_character_raw(Z, N, entry,
                                                    include_inter=include_inter)
        except Exception:
            continue
        chi_actual = mp.mpc(str(float(chi_q))) * mp.exp(mp.mpf(str(float(log_norm))))
        num += w * chi_actual
        den += w * d_cl
        nT += 1
    if den == 0:
        return None, nT
    return num / den, nT


def nucleon_cumulative_ak_product(Z: int, N: int) -> dict:
    """Nucleon-cumulative prefix: a_k at k=3, 6, 9, ... product.

    At k=3: proton or first nucleon alone (we use Z=1, N=0 for proton,
    Z=0, N=1 for first-neutron atoms; for mixed, take first ordered).
    At k=6: A=2 atom (first two nucleons).
    At k=9: A=3 atom.
    At k=3A: full atom.
    """
    A = Z + N
    # Order of nucleons per atom_gen_chains convention: protons first,
    # then neutrons.
    ordering = ['p'] * Z + ['n'] * N

    a_levels = []
    for level, k in enumerate([3 * (j + 1) for j in range(A)]):
        j = level + 1  # build up j-th nucleon
        zj = sum(1 for t in ordering[:j] if t == 'p')
        nj = j - zj
        a_k_atom, nT_a = a_k_ratio(zj, nj, n_strands_override=k,
                                      include_inter=True)
        a_k_free, nT_f = a_k_ratio(zj, nj, n_strands_override=k,
                                      include_inter=False)
        if a_k_atom is None or a_k_free is None:
            a_levels.append({"k": k, "a_atom": None, "a_free": None,
                              "ratio": None, "n_partitions": nT_a})
        else:
            ratio = a_k_atom / a_k_free if a_k_free != 0 else mp.mpc(0)
            a_levels.append({
                "k": k, "Zj": zj, "Nj": nj,
                "a_atom_re": float(mp.re(a_k_atom)),
                "a_free_re": float(mp.re(a_k_free)),
                "ratio_re": float(mp.re(ratio)),
                "n_partitions": nT_a,
            })
    # Product of per-level ratios (atom/free):
    prod = mp.mpc(1)
    n_levels_used = 0
    for entry in a_levels:
        if entry.get("ratio_re") is not None:
            prod *= mp.mpc(entry["ratio_re"])
            n_levels_used += 1
    return {
        "levels": a_levels,
        "product_abs": float(mp.fabs(prod)),
        "product_re": float(mp.re(prod)),
        "n_levels_used": n_levels_used,
    }


def main() -> int:
    print("=" * 100)
    print("PURE-HECKE BINDING via PER-LEVEL PREFIX WORD PRODUCT")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT},  h = {float(h):.6f}")
    print(f"  E_0 = {float(E0)} MeV (single calibration)")
    print()

    CODATA = {
        "D":    (1, 1, 2, 2.22456612),
        "T":    (1, 2, 3, 8.481798),
        "3He":  (2, 1, 3, 7.718058),
    }

    print("Nucleon-cumulative prefix (option 2):")
    print(f"  {'iso':<5} {'A':>2}  per-level ratios (atom/free) → product")
    for iso, (Z, N, A, B_ame) in CODATA.items():
        res = nucleon_cumulative_ak_product(Z, N)
        levels_str = " · ".join(
            f"a_{e['k']}={e.get('ratio_re', 'n/a'):.4f}" if isinstance(e.get('ratio_re'), float)
            else f"a_{e['k']}=n/a"
            for e in res['levels']
        )
        B_pred = E0 * (1 - res['product_abs'])
        err = float((B_pred - B_ame) / B_ame * 100)
        print(f"  {iso:<5} {A:>2}  {levels_str}  →  Π = {res['product_abs']:.6f}  "
              f"B_pred(E_0·(1-Π)) = {float(B_pred):.4f} MeV  "
              f"vs {B_ame:.4f} (err {err:+.2f}%)")

    witness = {
        "computation": "pure-hecke-binding-prefix",
        "description": (
            "Pure-Hecke binding via per-level prefix-word product, "
            "nucleon-cumulative interpretation: a_k(β_k) at k = 3, 6, ... "
            "where β_k is the atom braid for the first k/3 nucleons.  "
            "Final knot factor a(Z,N) = Π_k a_k; binding B = E_0·(1−a)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0_FLOAT,
    }
    out = Path(__file__).parent / "pure-hecke-binding-prefix.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
