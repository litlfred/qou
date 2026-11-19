#!/usr/bin/env python3
"""A conformance harness any chi^lambda implementation must pass — the oracle
the block-monotone window transfer needs BEFORE it is written.

`chi_general_word.chi_all_lambda_any` restored the atom trace producer by
routing non-monotone words to the general-word Rust kernel. That is correct and
`d_lambda`-BOUND: A=3 costs 0.36 s, A=4 costs 621 s, A>=5 is impractical (bean
`qou-wdij`). The fix that restores `O(A)` is a transfer carrying the three-level
window state, and its failure mode is **a plausible wrong number, not an
exception** — a mis-signed Hoefsmit off-diagonal produces characters that look
entirely reasonable.

So the oracle is wired first, and this file is it. Point it at any callable with
the `chi_all_lambda_*` signature and it decides.

## What it checks, and why each one

Both intra orders are exercised at every atom, because they probe different
paths through a dispatcher: `grouped` is monotone (fast transfer), `borromean`
is not (general kernel). An implementation that silently handled only one would
pass a single-order harness.

1. **Against the general-word kernel** — the reference. Validated against the
   monotone transfer to 6.1e-50 in
   `nonmonotone_atom_trace_kernel_route_probe.py`, so it is trusted here rather
   than re-derived.
2. **Against the monotone transfer, on monotone words only** — a second,
   independent implementation. Catches an error the kernel and a new transfer
   could share.
3. **On `tr_M`, not just per-partition chi** — the y_lambda-weighted trace is
   the quantity every consumer actually reads, and (measured) it does not carry
   the kernel's ~1 ulp per-chi wobble at all: its spread over 8 runs is EXACTLY
   0.0. So the trace check can be tightened far past the per-chi one.
4. **Partition-set identity** — a transfer that drops or invents a `lambda`
   would otherwise pass a max-difference test that only walks the keys it has.
   This is the shape the `n % 3` guard was added for (bean `qou-ym48`): the
   sweep ended holding partitions of the wrong size, every lookup missed, and
   the result read as zero with no exception.

## The circularity this file used to carry is GONE — and how to tell

When this harness was written the dispatcher routed non-monotone words to
`chi_all_lambda_general`, which is *also* the oracle, so those rows reported
`max|d| = 0.0` EXACTLY: a function compared with itself, testing **routing**
rather than arithmetic. This section warned that a 35/35 on the dispatcher was
evidence about the easy case plus the wiring, not about the hard case.

That is no longer true. `chi_all_lambda_any` now routes non-monotone words to
`chi_window_transfer.chi_all_lambda_window`, an independent `d_λ`-free
implementation, so the borromean rows are a genuine two-implementation
comparison and read `1.2e-50 … 2.1e-49`.

**The diagnostic is the number itself, and it is worth keeping in mind whoever
reads this next: a borromean row reporting exactly `0.0` means the candidate IS
the oracle on that path, and the row is worth nothing.** A non-zero value at the
serialization floor is the result; an exact zero is a tautology wearing its
clothes.

## Tolerances, and why they are what they are

`CHI_TOL = 1e-45` sits five orders ABOVE the kernel's measured non-reproducibility
floor (1.00229e-50, ~1 ulp at 50 dps; bean `qou-07ts` and its extension in
`qou-wdij`). That gap is deliberate: it makes the per-chi check a test of two
implementations against each other rather than a test of the kernel's own noise.

`TR_TOL = 1e-45` applies to `tr_M`, where the wobble measurably does not reach.

Neither is a floor to be relaxed if a new implementation fails. A window transfer
that needs a looser tolerance than the kernel's own noise is not agreeing; it is
being fitted to pass, which this repository's discipline names as a fit.

Usage:
    python3 chi_kernel_conformance_harness.py            # checks the dispatcher
    from chi_kernel_conformance_harness import conformance
    conformance(my_window_transfer)                      # checks a candidate

Arithmetic: mpmath at the 50-dps floor. No float64.
Exit 0 iff every check passes.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from chi_general_word import chi_all_lambda_general, word_is_monotone  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

# See the module docstring: five orders above the kernel's measured 1-ulp
# reproducibility floor, deliberately. Do not relax these to make a candidate
# pass.
CHI_TOL = mp.mpf("1e-45")
TR_TOL = mp.mpf("1e-45")

# (1,0)/(0,1) are single nucleons — the intra word alone, where an interleaving
# bug has nowhere to hide behind a bond. (1,1) is the first word with a bond.
# (1,2)/(2,1) are the largest the oracle answers in under a second.
ATOMS = [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)]
ORDERS = ("grouped", "borromean")


def _tr(chi, y):
    return mp.fsum(y[lam] * chi.get(lam, mp.mpf(0)) for lam in y)


def conformance(chi_fn, *, name: str = "candidate", atoms=None, verbose=True):
    """Run the harness against `chi_fn(word, n, dps=..., q=...)`.

    Returns `(checks, n_passed)`; `checks` is a list of `(label, passed)`.
    """
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    checks: list[tuple[str, bool]] = []

    for (Z, N) in (atoms or ATOMS):
        n = 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}

        for order in ORDERS:
            word = atom_braid_word_3A(Z, N, intra_order=order)
            tag = f"{name} ({Z},{N}) {order}"
            mono = word_is_monotone(word)

            try:
                got = chi_fn(word, n, dps=50)
            except Exception as exc:                      # noqa: BLE001
                checks.append((f"{tag}: raised {type(exc).__name__}: {exc}", False))
                continue

            ref = chi_all_lambda_general(word, n, dps=50)

            # 4. partition-set identity, first — a max-difference over the keys
            #    the candidate happens to have would otherwise hide a drop.
            same_keys = set(got) == set(ref)
            checks.append((
                f"{tag}: partition set matches the oracle "
                f"({len(got)} vs {len(ref)})", same_keys))

            # 1. per-partition chi against the oracle
            worst = mp.mpf(0)
            for lam in set(got) | set(ref):
                worst = max(worst, abs(got.get(lam, mp.mpf(0))
                                       - ref.get(lam, mp.mpf(0))))
            checks.append((
                f"{tag}: chi == general-word kernel "
                f"(max|d| = {mp.nstr(worst, 6)})", worst < CHI_TOL))

            # 3. tr_M, where the kernel's ulp wobble measurably does not reach
            d_tr = abs(_tr(got, y) - _tr(ref, y))
            checks.append((
                f"{tag}: tr_M == oracle (|d| = {mp.nstr(d_tr, 6)})",
                d_tr < TR_TOL))

            # 2. the independent second implementation, where it applies
            if mono:
                ref2 = chi_all_lambda(word, n, dps=50)
                worst2 = mp.mpf(0)
                for lam in set(got) | set(ref2):
                    worst2 = max(worst2, abs(got.get(lam, mp.mpf(0))
                                             - ref2.get(lam, mp.mpf(0))))
                checks.append((
                    f"{tag}: chi == monotone transfer (independent) "
                    f"(max|d| = {mp.nstr(worst2, 6)})", worst2 < CHI_TOL))

    n_pass = sum(1 for _l, p in checks if p)
    if verbose:
        for label, passed in checks:
            print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        print(f"\n{n_pass}/{len(checks)} checks passed")
    return checks, n_pass


def main() -> int:
    from chi_general_word import chi_all_lambda_any

    print("Conformance: chi_general_word.chi_all_lambda_any (the live dispatcher)\n")
    checks, n_pass = conformance(chi_all_lambda_any, name="dispatcher")
    print(
        "\n  NOTE: a borromean row reading exactly max|d| = 0.0 would mean the "
        "candidate IS\n  the oracle on that path — routing tested, arithmetic "
        "not. The dispatcher used\n  to be in that position; it now routes "
        "non-monotone words to the window\n  transfer, so those rows are a "
        "genuine two-implementation comparison.")
    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
