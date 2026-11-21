#!/usr/bin/env python3
"""The Borromean atom word is non-monotone, so the production transfer kernel
refuses it — and the general-word kernel is the route that already exists.

**The regression.** Commit `7db032fb48` (2026-09-05 07:53 UTC, on the owner
ruling recorded in bean `qou-hu1f`) changed `mass_at_3A_proper.atom_braid_word_3A`
to emit the INTERLEAVED Borromean intra-nucleon word by default
(`intra_order="borromean"`), because the previous grouped assembly was a
different element of `H_3(q)` — 82 % away at `q₀`, and only the interleaved one
is `beta_Bor`. That fix is correct and is not in question here.

What it did not account for is that interleaving `sigma_0` and `sigma_1` makes
the generator sequence NON-MONOTONE:

    grouped    (1,0)  gens [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]        monotone
    borromean  (1,0)  gens [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]    NOT monotone

and the entire fine-Bratteli transfer-matrix machinery
(`chi_monotone_transfer.chi_all_lambda` and its accelerator
`reduced_block_kernel.chi_all_lambda_reduced_block`) is valid ONLY for monotone
words. Its own module docstring states this as its "KEY FACT", derived from the
grouped word. Both refuse with `ValueError: non-monotone word`.

So `tr_m_atom_via_transfer.tr_m_atom_zn` — the canonical atom trace producer —
raises for EVERY atom on `main`, `(1,0)`, `(0,1)` and `(1,1)` alike, and
`mass_binding_dashboard.py` dies on its first call.

**The refusal is correct and must stay.** Composing a non-monotone word through
the per-generator alpha/beta reduction would give a silently wrong answer; the
guard is doing its job. What is missing is a route for the word the producer now
builds.

**The route already exists.** Bean `qou-sorn` records
`pyhecke_native.chi_lambda_all_partitions_mpfr` as "the general-word kernel",
validated byte-for-byte against `tr_m_atom_zn`. A bean is not a primary source,
so this probe RE-VALIDATES that claim here rather than citing it: it runs the
kernel and the transfer against the SAME grouped word and requires agreement at
the 50-dps floor, and only then reports the kernel's value on the Borromean
word.

## The kernel is NOT bit-reproducible, and this probe is built to survive that

`cf412d98f9` (bean `qou-07ts`, landed while this branch was in flight) measured
`compute_atom_chi_rust.py 3He` producing **four distinct outputs in eight runs**.
That producer reaches the SAME function this module dispatches to
(`chi_cd_mpfr` -> `pyhecke_native.chi_lambda_all_partitions_mpfr`), so the
finding lands squarely on the route added here, and it is checked rather than
argued.

Re-measured through THIS route, 8 runs each, sha256 over the 50-digit chi
strings:

    3He   4 distinct fingerprints in 8    (reproduces qou-07ts exactly)
    3H    2 distinct fingerprints in 8    (qou-07ts recorded T as STABLE)

so `3H` wobbles too, just more rarely — an extension of that finding on more
draws, not a contradiction of it.

**Magnitude, which is what decides whether anything here is affected:**

    max |d chi| across 8 runs   1.00229e-50   (~1 ulp at 50 dps)
    max relative                7.46451e-50
    spread in tr_M              EXACTLY 0.0

The per-partition characters wobble at the last serialized digit; the
`y_lambda`-weighted trace does not move at all. So `AGREE` below is set to
`1e-45` — five orders ABOVE the kernel's own reproducibility floor, deliberately,
so this probe tests agreement between two implementations and not the kernel's
noise. Everything this branch reports is far above it: traces at 20 digits (30
orders), binding numbers at 8 (42 orders).

Arithmetic: mpmath at the 50-dps floor throughout; the kernel returns decimal
strings loaded into `mpf`. No float64 anywhere.

Exit 0 iff every check passes.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from chi_monotone_transfer import chi_all_lambda  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

TOL = mp.mpf("1e-30")
# Agreement floor. The kernel and the transfer are independent implementations
# (Rust mpfr vs Python mpmath), so exact string equality is not the right bar;
# 1e-45 is 5 digits inside the 50-dps serialization floor.
AGREE = mp.mpf("1e-45")

# Reproducibility probe: how many draws, and the bound the per-chi wobble must
# stay under. Measured floor is 1.00229e-50 (~1 ulp at 50 dps); 1e-48 leaves
# two orders of slack so a genuine degradation still fails this.
REPRO_RUNS = 8
REPRO_ULP = mp.mpf("1e-48")


def encode(word, h):
    """`(c, d, g)` triples -> the kernel's `(sign, g+1)` with per-position
    `avg_shifts`. Same encoding as
    `probes/cyclic_triple_bond_cross_term_probe.py`, which validated it."""
    signed, shifts = [], []
    for c, d, g in word:
        cm = c if isinstance(c, mp.mpf) else mp.mpf(str(c))
        assert abs(cm - 1) < mp.mpf("1e-9"), f"c={c} != 1 unsupported"
        dm = d if isinstance(d, mp.mpf) else mp.mpf(str(d))
        g1 = int(g) + 1
        if abs(dm) < TOL:
            signed.append((1, g1))
            shifts.append("")
        elif abs(dm + h) < TOL:
            signed.append((-1, g1))
            shifts.append("")
        elif abs(dm + h / 2) < TOL:
            signed.append((0, g1))
            shifts.append("")
        else:  # colour-weighted p-n letter
            signed.append((0, g1))
            shifts.append(mp.nstr(-dm, 60))
    return signed, shifts


def chi_kernel(word, n, h):
    """`{lambda: chi^lambda(word)}` via the general-word Rust kernel."""
    import pyhecke_native as pn

    signed, shifts = encode(word, h)
    out = pn.chi_lambda_all_partitions_mpfr(n, signed, Q_50_DIGIT_STR, 50, shifts)
    return {tuple(lam): mp.mpf(s) for lam, s in out}


def tr_from_chi(chi, y):
    return sum(y[lam] * v for lam, v in chi.items() if lam in y)


def main() -> int:
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    checks: list[tuple[str, bool, str]] = []

    for (Z, N) in [(1, 0), (0, 1), (1, 1)]:
        A, n = Z + N, 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}

        w_grp = atom_braid_word_3A(Z, N, intra_order="grouped")
        w_bor = atom_braid_word_3A(Z, N, intra_order="borromean")

        gens_grp = [g for _c, _d, g in w_grp]
        gens_bor = [g for _c, _d, g in w_bor]
        mono = all(gens_grp[i] <= gens_grp[i + 1] for i in range(len(gens_grp) - 1))
        nonmono = any(gens_bor[i] > gens_bor[i + 1] for i in range(len(gens_bor) - 1))
        checks.append((f"({Z},{N}) grouped word is monotone", mono, ""))
        checks.append((f"({Z},{N}) borromean word is NOT monotone", nonmono, ""))

        # The transfer REFUSES the borromean word — the regression, asserted.
        refused = False
        try:
            chi_all_lambda(w_bor, n)
        except ValueError as e:
            refused = "non-monotone" in str(e)
        checks.append(
            (f"({Z},{N}) transfer refuses the borromean word", refused, ""))

        # THE LOAD-BEARING CHECK: kernel == transfer on the grouped word.
        chi_t = chi_all_lambda(w_grp, n)
        chi_k = chi_kernel(w_grp, n, h)
        worst = mp.mpf(0)
        for lam, v in chi_t.items():
            worst = max(worst, abs(v - chi_k.get(lam, mp.mpf(0))))
        checks.append((
            f"({Z},{N}) kernel == transfer on the grouped word "
            f"(max|d chi| = {mp.nstr(worst, 6)})",
            worst < AGREE, ""))

        tr_grp = tr_from_chi(chi_t, y)
        tr_bor = tr_from_chi(chi_kernel(w_bor, n, h), y)
        rel = abs(tr_bor - tr_grp) / abs(tr_grp) if tr_grp != 0 else mp.mpf("inf")
        checks.append((
            f"({Z},{N}) kernel computes the borromean trace "
            f"(grouped {mp.nstr(tr_grp, 20)} -> borromean {mp.nstr(tr_bor, 20)}, "
            f"rel {mp.nstr(rel, 4)})",
            tr_bor == tr_bor, ""))  # finiteness; the value is the report

    # ── the kernel's reproducibility floor, and that it does not reach tr_M ──
    # Deliberately NOT a check on the fingerprint count: the wobble is
    # stochastic (3H showed 2 distinct in 8, 3He showed 4), so asserting
    # "unstable" would itself be flaky. What IS robust, and is what this route
    # depends on, is that the wobble stays ~1 ulp and cancels out of the
    # y_lambda-weighted trace entirely.
    for (Z, N) in [(1, 2), (2, 1)]:
        n = 3 * (Z + N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
        w = atom_braid_word_3A(Z, N)
        runs = [chi_kernel(w, n, h) for _ in range(REPRO_RUNS)]
        spread = mp.mpf(0)
        for lam in runs[0]:
            vals = [r[lam] for r in runs]
            spread = max(spread, max(vals) - min(vals))
        trs = [mp.fsum(y[lam] * r.get(lam, mp.mpf(0)) for lam in y) for r in runs]
        tr_spread = max(trs) - min(trs)
        checks.append((
            f"({Z},{N}) kernel non-reproducibility stays ~1 ulp over "
            f"{REPRO_RUNS} runs (max spread = {mp.nstr(spread, 6)})",
            spread < REPRO_ULP, ""))
        checks.append((
            f"({Z},{N}) the wobble does NOT reach tr_M "
            f"(spread = {mp.nstr(tr_spread, 6)})",
            tr_spread == 0, ""))

    ok = sum(1 for _n, p, _m in checks if p)
    for name, passed, _m in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    print(f"\n{ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
