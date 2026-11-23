#!/usr/bin/env python3
"""The window transfer at A = 4, 6, 7 — where the general-word kernel cannot go.

`chi_kernel_conformance_harness` validates a candidate against the general-word
Rust kernel, and stops at A = 3 because the kernel costs **621 s at A = 4** and
did not finish A = 6 inside a 900 s budget. But A = 4, 6, 7 are exactly the sizes
`chi_window_transfer` exists for: `mass_binding_dashboard --low` needs 4He, 6Li
and 7Li. So the harness cannot check the transfer where it matters most.

**A second independent oracle covers that gap, and it is already in the corpus.**
`chi_monotone_transfer.chi_all_lambda` is fast at every size and is a genuinely
separate implementation — it sweeps one generator at a time using only the
DIAGONAL seminormal entry, where the window transfer carries an (init, cur)
level pair and full 2x2 blocks. Its restriction is that it needs a MONOTONE word,
which the `grouped` intra order supplies at any A.

So this probe checks the window transfer against it on the grouped word at
A = 4, 6, 7. That does not exercise the interleaving — the harness does that at
A <= 3 — but it does exercise **everything else at scale**: the level-retirement
rule, the trace's init == cur requirement, the box-extension loop, and the
partition bookkeeping over 77, 385 and 792 partitions.

Together the two cover the matrix: interleaving is checked at small A against the
kernel, and scale is checked at large A against the monotone transfer.

## Two measured facts worth carrying forward

**1. Per-chi agreement degrades with `n`; `tr_M` agreement does not.** Measured
5.99e-49 at n=12, 1.23e-47 at n=18, 1.09e-46 at n=21 — accumulation over more
operations, and still ~40 orders below anything the framework reads. The
`y_lambda`-weighted trace stays at ~1e-52 throughout, because the weighting is a
sum in which independent per-partition errors partly cancel. `tr_M` is what
consumers actually read, so the tolerance that matters is the stable one.

**2. On MONOTONE words the existing transfer is ~10x FASTER** (0.16 s vs 1.80 s
at A=7), because the window transfer carries the (init, cur) pair that the
monotone case does not need. That is the price of generality and it is not a
defect — but it means the right wiring is a DISPATCH (monotone -> existing
transfer, non-monotone -> window transfer), never a replacement.

Arithmetic: mpmath at the 50-dps floor. No float64.
Exit 0 iff every check passes.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_window_transfer import chi_all_lambda_window  # noqa: E402
from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

# Per-chi tolerance is loosened with n to match the measured accumulation; tr_M
# is held tight because it measurably does not accumulate. Both sit far above
# the kernel's own ~1 ulp reproducibility floor (1.00229e-50), so neither is
# testing arithmetic noise.
CHI_TOL = {12: mp.mpf("1e-45"), 18: mp.mpf("1e-44"), 21: mp.mpf("1e-43")}
TR_TOL = mp.mpf("1e-48")

CASES = [(2, 2, "4He"), (3, 3, "6Li"), (3, 4, "7Li")]


def main() -> int:
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    checks: list[tuple[str, bool]] = []

    print("  window transfer vs the INDEPENDENT monotone transfer, grouped word\n")
    for (Z, N, name) in CASES:
        n = 3 * (Z + N)
        word = atom_braid_word_3A(Z, N, intra_order="grouped")
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}

        t0 = time.time()
        got = chi_all_lambda_window(word, n, dps=50)
        t_win = time.time() - t0
        t0 = time.time()
        ref = chi_all_lambda(word, n, dps=50)
        t_mono = time.time() - t0

        keys_ok = set(got) == set(ref)
        worst = mp.mpf(0)
        for lam in set(got) | set(ref):
            worst = max(worst, abs(got.get(lam, mp.mpf(0)) - ref.get(lam, mp.mpf(0))))
        tr_g = mp.fsum(y[lam] * got.get(lam, mp.mpf(0)) for lam in y)
        tr_r = mp.fsum(y[lam] * ref.get(lam, mp.mpf(0)) for lam in y)
        d_tr = abs(tr_g - tr_r)

        print(f"  {name:4s} n={n:2d} parts={len(ref):3d}  "
              f"max|dchi|={mp.nstr(worst, 6):>12}  |dtr_M|={mp.nstr(d_tr, 6):>12}  "
              f"window {t_win:6.2f}s  monotone {t_mono:6.2f}s")

        checks.append((f"{name}: partition sets match ({len(got)} vs {len(ref)})",
                       keys_ok))
        checks.append((f"{name}: chi agrees (max|d| = {mp.nstr(worst, 6)})",
                       worst < CHI_TOL[n]))
        checks.append((f"{name}: tr_M agrees (|d| = {mp.nstr(d_tr, 6)})",
                       d_tr < TR_TOL))

    print()
    ok = sum(1 for _l, p in checks if p)
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
    print(f"\n{ok}/{len(checks)} checks passed")
    print("\n  NOTE: this checks SCALE, not interleaving — the grouped word is\n"
          "  monotone by construction. Interleaving is checked at A <= 3 against\n"
          "  the general-word kernel in chi_kernel_conformance_harness. Neither\n"
          "  probe covers both, which is why both exist.")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
