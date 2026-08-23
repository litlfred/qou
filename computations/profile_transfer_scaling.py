#!/usr/bin/env python3
"""profile_transfer_scaling — map wall-time of the monotone-word transfer χ
and canonical tr_M up the nuclide ladder, to the feasibility ceiling.

Climbs A = 6, 7, 8, … computing the canonical atom χ^λ(β_atom) (fine-
Bratteli transfer) and tr_M = Σ y_λ χ^λ at q₀, 50 dps, reporting per-A
wall split (χ transfer vs y_λ vs assembly) and the partition count p(3A).
Stops when a step exceeds the wall cap, marking the empirical bottleneck.

Progress is flushed per A (long-compute logging discipline). Run as:
    python3 -u profile_transfer_scaling.py [cap_sec] 2>&1 | tee /tmp/profile_transfer_scaling.log

NO float64 (owner ruling 2026-06-09): mpmath at the 50-dps floor.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from host_info import host_info, summary_line  # noqa: E402
from _precision import set_compute_dps  # noqa: E402


def representative_zn(A: int) -> tuple[int, int]:
    """Half protons / half neutrons (timing is ~A-driven, split is immaterial)."""
    Z = A // 2
    return Z, A - Z


def main() -> int:
    set_compute_dps()
    cap = float(sys.argv[1]) if len(sys.argv) > 1 else 600.0
    print(f"host: {summary_line()}", flush=True)
    A_list = [6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 24]
    rows = []
    bottleneck = None
    t_start = time.time()
    for A in A_list:
        n = 3 * A
        Z, N = representative_zn(A)
        word = atom_braid_word_3A(Z, N, include_inter=True)
        t0 = time.time()
        chi = chi_all_lambda(word, n)
        t_chi = time.time() - t0
        t1 = time.time()
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
        t_y = time.time() - t1
        t2 = time.time()
        trM = mp.fsum(y[lam] * chi.get(lam, mp.mpf(0)) for lam in y)
        t_asm = time.time() - t2
        elapsed = time.time() - t_start
        rows.append({"A": A, "n": n, "p_n": len(chi),
                     "t_chi_sec": round(t_chi, 3), "t_y_sec": round(t_y, 3),
                     "t_asm_sec": round(t_asm, 3), "tr_M_atom": mp.nstr(trM, 12)})
        print(f"A={A:<3} n={n:<3} p(n)={len(chi):<7} "
              f"t_chi={t_chi:8.2f}s  t_y={t_y:8.2f}s  t_asm={t_asm:6.2f}s  "
              f"tr_M={mp.nstr(trM, 8):>13}  [elapsed {elapsed:.0f}s]", flush=True)
        if max(t_chi, t_y) > cap:
            bottleneck = {"A": A, "n": n, "limiting": "chi" if t_chi >= t_y else "y_lambda",
                          "t_chi_sec": round(t_chi, 2), "t_y_sec": round(t_y, 2)}
            print(f"  >>> BOTTLENECK at A={A} (n={n}): "
                  f"{'χ transfer' if t_chi >= t_y else 'y_λ'} exceeded cap {cap}s",
                  flush=True)
            break

    w = WitnessBuilder("transfer-scaling-profile", engine="python")
    w.set_description(
        "Wall-time scaling of the monotone-word fine-Bratteli transfer χ and "
        "canonical tr_M (Σ y_λ χ^λ) up the nuclide ladder at q₀, 50 dps. "
        "Per-A split: χ transfer vs y_λ (Jones-Markov weights) vs assembly. "
        "Maps the empirical feasibility ceiling beyond ⁷Li."
    )
    w.add_data("rows", rows)
    w.add_data("wall_cap_sec", cap)
    w.add_data("host", host_info())
    if bottleneck:
        w.add_data("bottleneck", bottleneck)
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
