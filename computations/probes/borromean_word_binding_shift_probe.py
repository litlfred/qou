#!/usr/bin/env python3
"""What the Borromean word correction does to the binding predictions, and what
it costs to compute them.

Companion to `nonmonotone_atom_trace_kernel_route_probe.py`, which establishes
that the corrected (interleaved Borromean) atom word is non-monotone, that the
fine-Bratteli transfer therefore refuses it, and that
`pyhecke_native.chi_lambda_all_partitions_mpfr` is a validated route for it.
This probe asks the two questions that follow: **what moves**, and **what does
the route cost**.

## 1. The binding predictions move by 4-8x, in the WRONG direction

Under the production observe-early law `B = Q_beta * (|tr_free| - |tr_atom|)`:

| atom | AME (MeV) | B, grouped word | B, Borromean word | ratio |
|---|---|---|---|---|
| D   | 2.224566 | 0.43540348 | 0.11503953  | 0.264 |
| 3H  | 8.481798 | 0.69513150 | 0.088347359 | 0.127 |
| 3He | 7.718043 | 0.69855221 | 0.10137663  | 0.145 |

The grouped word already under-bound by 5-12x. The corrected word under-binds by
19-96x. **This is reported, not repaired.** The word correction is an owner
ruling on a structural error (`7db032fb48`: the grouped assembly was a different
element of `H_3(q)`, and only the interleaved one is `beta_Bor`), so the honest
reading is that the previous, better-looking number came from the wrong object.
Per this repository's anti-fit discipline a documented honest miss is a result;
reverting to the grouped word because its number was closer would be selection
against the target.

## 2. The route restores correctness and loses the O(A) scaling

The transfer is `d_lambda`-free; the general-word kernel is not. Measured on
this container, 50 dps, canonical `q0`, one word per row:

| A | n | partitions | general-word kernel |
|---|---|---|---|
| 1 |  3 |  3 | < 0.01 s |
| 2 |  6 | 11 | < 0.01 s |
| 3 |  9 | 30 |   0.36 s |
| 4 | 12 | 77 | **621.38 s** |

A ~1700x jump from `n = 9` to `n = 12`. The producer computes two words (atom
and free), so 4He is ~21 min and A >= 5 was still running when its budget
expired. For comparison the transfer did every one of these in under 0.05 s.

So the repair is fully adequate through 3H/3He, makes 4He a long compute, and
leaves A >= 5 impractical. The real fix is the block-monotone window transfer
described in `chi_general_word`'s module docstring and bean `qou-wdij`: the atom
word is non-monotone only *within* each 3-strand nucleon, so a transfer carrying
the three-level window state would compose it and keep O(A).

The A = 4 timing is quoted from a measured run and is NOT re-run here -- this
probe stays under a minute so it is cheap to re-run. Re-measure with
`--timing` if you need it fresh.

Arithmetic: mpmath at the 50-dps floor throughout. No float64.

Exit 0 iff every check passes.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_general_word import chi_all_lambda_any, word_is_monotone  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from binding_canonical import _Q_BETA_N  # noqa: E402

# AME2020 binding energies, MeV.
AME = {"D": mp.mpf("2.224566"), "3H": mp.mpf("8.481798"),
       "3He": mp.mpf("7.718043")}
ZN = {"D": (1, 1), "3H": (1, 2), "3He": (2, 1)}

# Recorded ratios from the run this probe documents; re-derived below and
# required to reproduce, so a future word change makes this probe fail rather
# than silently restate a stale table.
EXPECTED_RATIO = {"D": mp.mpf("0.2642"), "3H": mp.mpf("0.1271"),
                  "3He": mp.mpf("0.1451")}
RATIO_TOL = mp.mpf("5e-4")


def _tr(Z, N, n, y, *, order, inter):
    chi = chi_all_lambda_any(
        atom_braid_word_3A(Z, N, include_inter=inter, intra_order=order), n)
    return mp.fsum(y[lam] * chi.get(lam, mp.mpf(0)) for lam in y)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timing", action="store_true",
                    help="also re-measure the kernel cost at A=4 (~10 min)")
    args = ap.parse_args()

    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    qb = mp.mpf(str(_Q_BETA_N))
    checks: list[tuple[str, bool]] = []

    print("  atom   AME (MeV)     B grouped        B borromean      ratio   "
          "AME/B_bor")
    for name, (Z, N) in ZN.items():
        n = 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}

        w_bor = atom_braid_word_3A(Z, N, include_inter=True)
        checks.append((f"{name}: the production word is non-monotone",
                       not word_is_monotone(w_bor)))

        b = {}
        for order in ("grouped", "borromean"):
            ta = _tr(Z, N, n, y, order=order, inter=True)
            tf = _tr(Z, N, n, y, order=order, inter=False)
            b[order] = qb * (abs(tf) - abs(ta))

        ratio = b["borromean"] / b["grouped"]
        print(f"  {name:4s} {mp.nstr(AME[name], 7):>10} "
              f"{mp.nstr(b['grouped'], 8):>16} "
              f"{mp.nstr(b['borromean'], 8):>16} "
              f"{mp.nstr(ratio, 4):>8} {mp.nstr(AME[name] / b['borromean'], 4):>10}")

        checks.append((
            f"{name}: the Borromean B reproduces the recorded ratio "
            f"{mp.nstr(EXPECTED_RATIO[name], 4)}",
            abs(ratio - EXPECTED_RATIO[name]) < RATIO_TOL))
        checks.append((
            f"{name}: the corrected word moves B DOWN, away from AME",
            b["borromean"] < b["grouped"] < AME[name]))

    if args.timing:
        for (Z, N) in [(1, 1), (1, 2), (2, 2)]:
            n = 3 * (Z + N)
            t0 = time.time()
            chi_all_lambda_any(atom_braid_word_3A(Z, N), n)
            print(f"  timing: A={Z + N} n={n} kernel {time.time() - t0:.2f} s",
                  flush=True)

    print()
    ok = sum(1 for _n, p in checks if p)
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    print(f"\n{ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
