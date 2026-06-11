#!/usr/bin/env python3
"""Averaged-convention block-swapped S_atom for ⁴He — the PRODUCTION binding signal.

Refines task 1 (`block_swap_binding.py`, sign-only) to the AVERAGED
(bring_color_weighted) crossing convention used by the production binding
(`binding_canonical.py`). The sign-only run gave S_atom=0.535 > S_free=0.374
(negative binding signal), but the averaged free symmetrization is much larger
(S_free ≈ 2.47, the bosonic h₂h₂/τ²τ² of #2103), so the averaged signal can FLIP
SIGN — this settles whether the identical-nucleon symmetrization deepens or
relieves the binding under-prediction.

Uses `pyhecke_native.chi_q_atomic(λ, factors, q)` — the Rust q-character on a
sequence of averaged Hecke factors `c·σ + d·I` (validated: it reproduces
`binding_canonical`'s tr_M(W_atom ⁴He)=0.05536 exactly). The block-swap braids
β_σ are the same self-verified S₂×S₂ permutation braids as task 1, here entered
as pure-σ factors `(c=1, d=0, gen)`.

tr_atom_sym = ¼ Σ_{σ∈S₂×S₂} tr_M(W_atom·β_σ) ;  S_atom = tr_atom_sym / tr_M(W_atom).
Cross-check: the FREE S_free must equal the Frobenius bosonic h₂(p)h₂(n)/(τ_p²τ_n²).

Output: averaged-block-swap-binding.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

mp.mp.dps = 50

import pyhecke_native as _pn  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from tr_m_wenzl_bridge_mpfr import _load_y_lambda  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from block_swap_binding import block_swap_word  # verified S_Z block-swap braid  # noqa: E402


def averaged_factors(Z: int, N: int, include_inter: bool):
    """Atom braid word as averaged Hecke factors (c, d, gen_1based)."""
    return [(float(c), float(d), g + 1)
            for (c, d, g) in atom_braid_word_3A(Z, N, include_inter=include_inter)]


def tr_M(factors, n: int, y_table, q_f: float) -> mp.mpf:
    """tr_M = Σ_λ y_λ · χ_λ(factors) via the Rust averaged q-character."""
    total = mp.mpf(0)
    for shape in parts_of(n):
        st = tuple(shape)
        y = y_table.get(st)
        if y is None:
            continue
        total += mp.mpf(str(y)) * mp.mpf(str(_pn.chi_q_atomic(st, factors, q_f)))
    return total


def main() -> int:
    t0 = time.monotonic()
    Z, N = 2, 2
    n = 3 * (Z + N)
    q_f = float(mp.mpf(Q_50_DIGIT_STR))
    y_table = _load_y_lambda(n, None)

    sigma = {  # pure-σ block-swap factors (c=1, d=0)
        "id": [],
        "swap_p": [(1.0, 0.0, g + 1) for g in block_swap_word(0, 3, n)],
        "swap_n": [(1.0, 0.0, g + 1) for g in block_swap_word(6, 3, n)],
        "swap_pn": [(1.0, 0.0, g + 1) for g in
                    (block_swap_word(0, 3, n) + block_swap_word(6, 3, n))],
    }
    w_atom = averaged_factors(Z, N, include_inter=True)
    w_free = averaged_factors(Z, N, include_inter=False)

    print("=" * 84)
    print(" Averaged-convention block-swap S_atom for ⁴He (production binding signal)")
    print("=" * 84)
    print(f" {'σ block-perm':>14}{'tr_M(W_atom·β)':>18}{'tr_M(W_free·β)':>18}")
    print(" " + "-" * 60)
    at, fr = {}, {}
    for name in sigma:
        ta = tr_M(w_atom + sigma[name], n, y_table, q_f)
        tf = tr_M(w_free + sigma[name], n, y_table, q_f)
        at[name], fr[name] = ta, tf
        print(f" {name:>14}{float(ta):>18.8f}{float(tf):>18.8f}")
    print(" " + "-" * 60)

    G = len(sigma)
    tr_atom_sym = sum(at.values()) / G
    tr_free_sym = sum(fr.values()) / G
    S_atom = tr_atom_sym / at["id"]
    S_free = tr_free_sym / fr["id"]
    signal = mp.log(S_free / S_atom)

    # Cross-check: free S_free vs the Frobenius bosonic h₂(p)h₂(n)/(τ_p²τ_n²).
    sym = json.loads(
        (HERE / "symmetrized-constituent-general.witness.json").read_text(encoding="utf-8"))
    pp = {int(k): mp.mpf(v) for k, v in sym["data"]["proton_power_sums"].items()}
    pn = {int(k): mp.mpf(v) for k, v in sym["data"]["neutron_power_sums"].items()}
    h2 = lambda p1, p2: (p1 ** 2 + p2) / 2
    S_free_frobenius = (h2(pp[1], pp[2]) * h2(pn[1], pn[2])) / (pp[1] ** 2 * pn[1] ** 2)

    print(f"  S_atom (averaged)  = {float(S_atom):.6f}")
    print(f"  S_free (averaged)  = {float(S_free):.6f}   "
          f"[Frobenius h₂h₂/τ²τ² = {float(S_free_frobenius):.6f}]")
    print(f"  BINDING SIGNAL  log(S_free/S_atom) = {float(signal):+.6f}")
    print(f"  (sign-only task 1 gave −0.357903)")
    if float(signal) > 0:
        print("  ⇒ POSITIVE in the averaged convention: symmetrization RELIEVES the "
              "under-prediction (opposite sign to sign-only).")
    else:
        print("  ⇒ negative: symmetrization deepens the under-prediction.")

    w = WitnessBuilder("averaged-block-swap-binding", engine="python+rust",
                       start_time=t0)
    w.set_description(
        "Averaged-convention (production) block-swapped S_atom for ⁴He via "
        "pyhecke_native.chi_q_atomic (Rust q-character on averaged Hecke factors "
        "c·σ+d·I; validated against binding_canonical's tr_M=0.05536). Refines the "
        "sign-only task 1: tr_atom_sym=¼Σ_{σ∈S₂×S₂} tr_M(W_atom·β_σ). Reports the "
        "production binding signal log(S_free/S_atom) and whether it flips sign vs "
        "sign-only. Free S_free cross-checked against the Frobenius h₂h₂/τ²τ²."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("atom_traces", {k: float(v) for k, v in at.items()})
    w.add_data("free_traces", {k: float(v) for k, v in fr.items()})
    w.add_data("S_atom", float(S_atom))
    w.add_data("S_free", float(S_free))
    w.add_data("S_free_frobenius_crosscheck", float(S_free_frobenius))
    w.add_data("binding_signal_log_Sfree_over_Satom", float(signal))
    w.add_data("signonly_signal_task1", -0.357903)
    w.add_assertion(
        name="free_S_free_matches_frobenius_h2h2",
        computed=float(abs(S_free - S_free_frobenius)), expected=0.0, tolerance=1e-9,
        source="block-swap free S_free == Frobenius bosonic h₂(p)h₂(n)/(τ_p²τ_n²) — "
               "the disjoint free symmetrization reproduces the cycle-product "
               "constituent (a cross-check that the block-swap braids + averaged "
               "chi_q_atomic are correct).",
    )
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
