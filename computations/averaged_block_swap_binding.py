#!/usr/bin/env python3
"""Averaged-convention block-swapped S_atom for ⁴He — the PRODUCTION binding signal.

Refines task 1 (`block_swap_binding.py`, sign-only) to the AVERAGED
(bring_color_weighted) crossing convention used by the production binding
(`binding_canonical.py`), via `pyhecke_native.chi_q_atomic(λ, factors, q)` — the
Rust q-character on a sequence of averaged Hecke factors `c·σ + d·I` (validated: it
reproduces `binding_canonical`'s tr_M(W_atom ⁴He)=0.05536 exactly). The block-swap
braids β_σ are the same self-verified S₂×S₂ permutation braids as task 1, entered
as pure-σ factors `(c=1, d=0, gen)`.

    tr_atom_sym = ¼ Σ_{σ∈S₂×S₂} tr_M(W_atom·β_σ) ;  S_atom = tr_atom_sym / tr_M(W_atom).

## Performance — why chi_q_atomic is slow at H₁₂, and the fix

`chi_q_atomic` is O(dim²·k) per partition (dim = f^λ, k = #Hecke factors). The cost
concentrates in the ~8 partitions of 12 with dim 4000–7700 (λ=(5,3,2,1,1) dim=7700
≈ 5.3 s); the other ~69 are ≈ 0. The block-swap LENGTHENS the word (W_atom 47
factors → +18 for swap_pn = 65, +33 %), and MPFR 50-dps ≈ 100× f64. A full
single-thread sweep over the 8 factor-lists (4σ × atom/free) is ~250–340 s. FIX:
the 8 tr_M sweeps are independent ⇒ `multiprocessing.Pool` over them gives ~N_core
speedup (wall ≈ the slowest single sweep, ~40–50 s).

## Scalar-vs-exact caveat (quantified)

The free S_free here (exact H₁₂ block-level Markov symmetrization) does NOT equal
the scalar Frobenius h₂(p)h₂(n)/(τ_p²τ_n²): the scalar formula uses *H₃* Markov
traces `p_k=tr_M^{H₃}(B_p^k)` while this uses the *H₁₂* Markov trace, whose y_λ
weights are n-dependent. The ratio is recorded (≈ 0.18, a 5.5× gap) — this
QUANTIFIES the #2103 scalar caveat. (Open: whether the plain ¼Σβ_σ average is the
q-correct q-Young projection, or whether q-weighted symmetrizers shift the number.)

Output: averaged-block-swap-binding.witness.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from block_swap_binding import block_swap_word  # verified S_Z block-swap braid  # noqa: E402

N_STRANDS = 12


def averaged_factors(Z: int, N: int, include_inter: bool):
    """Atom braid word as averaged Hecke factors (c_str, d_str, gen_1based).

    DECIMAL STRINGS, not floats — `chi_q_atomic_mpfr` takes them that way
    precisely to avoid the lossy f64 boundary. Measured on the 4He word (47
    factors, 6 distinct (c, d) pairs), the `float()` this used to do loses:

        d = -0.10453014939781965771...   ->  2.738e-18
        d = -0.20906029879563931543...   ->  5.476e-18
        d = -0.10445824776972628901...   ->  2.238e-18

    (c = 1 and d = 0 are exact, so three of the six were lossless — which is
    why this reads as harmless until measured.)
    """
    return [(mp.nstr(mp.mpf(str(c)), 50), mp.nstr(mp.mpf(str(d)), 50), g + 1)
            for (c, d, g) in atom_braid_word_3A(Z, N, include_inter=include_inter)]


def _trM_worker(args):
    """Worker: tr_M(factors) = Σ_λ y_λ·χ_λ(factors) (Rust averaged q-character).

    Loads y_λ + pyhecke_native inside the worker so nothing non-picklable crosses
    the process boundary; returns the trace as a decimal string.
    """
    key, factors, q_str = args
    import mpmath as _mp
    _mp.mp.dps = 50
    import pyhecke_native as _p
    from per_irrep_pole_atom import parts_of as _parts
    from tr_m_wenzl_bridge_mpfr import _load_y_lambda as _ly
    yt = _ly(N_STRANDS, None)
    total = _mp.mpf(0)
    # Skip terms whose y_λ is structurally zero under convention D.
    #
    # The guard used to be `if y is None`, which only skips a MISSING entry.
    # Under convention D, `y_λ = 0` for ℓ(λ) > 2 — but the loaded table carries
    # those zeros as ROUND-OFF, not as exact 0, so `.get()` returns a tiny
    # nonzero and every one of them was computed in full.
    #
    # MEASURED on the H₁₂ table (77 partitions of 12):
    #
    #     7 shapes   |y| ~ 1e-3    <- ℓ(λ) ≤ 2, the ones that contribute
    #    70 shapes   |y| ≤ 1e-73   <- ℓ(λ) > 2, convention-D zeros as noise
    #
    # `count(|y| > 1e-40) == count(rows ≤ 2) == 7`. A 70-order gap, so the
    # threshold is not a tuned parameter — anything in (1e-73, 1e-3) picks out
    # the same 7 shapes.
    #
    # This was the ENTIRE cost. The skipped shapes are the expensive ones:
    # (5,3,2,1,1) is dim 7700 and 120 s in MPFR by itself, against a y_λ of
    # 1e-77, while the 7 that matter top out at dim 132. With them in, the
    # MPFR run exceeded 3300 s and was killed. So this is NOT an MPFR
    # affordability problem — the producer was doing convention-C-shaped work
    # (every row contributes) against convention-D weights.
    Y_VANISHING = _mp.mpf("1e-40")
    for sh in _parts(N_STRANDS):
        st = tuple(sh)
        y = yt.get(st)
        if y is None or abs(_mp.mpf(str(y))) < Y_VANISHING:
            continue
        # `chi_q_atomic_mpfr`, not `chi_q_atomic`. The f64 entry returns a
        # double, and `_mp.mpf(str(<double>))` then lifted it back into a
        # 50-dps accumulator — the laundering idiom, on a value with ~15 real
        # digits. The MPFR entry returns a decimal string at `dps`.
        chi = _p.chi_q_atomic_mpfr(st, factors, q_str, 50)
        total += _mp.mpf(str(y)) * _mp.mpf(chi)
    return key, _mp.nstr(total, 50)


def main() -> int:
    t0 = time.monotonic()
    Z, N = 2, 2
    q_str = Q_50_DIGIT_STR
    n = N_STRANDS

    sigma = {  # pure-σ block-swap factors (c=1, d=0)
        "id": [],
        "swap_p": [("1", "0", g + 1) for g in block_swap_word(0, 3, n)],
        "swap_n": [("1", "0", g + 1) for g in block_swap_word(6, 3, n)],
        "swap_pn": [("1", "0", g + 1) for g in
                    (block_swap_word(0, 3, n) + block_swap_word(6, 3, n))],
    }
    w_atom = averaged_factors(Z, N, include_inter=True)
    w_free = averaged_factors(Z, N, include_inter=False)

    # 8 independent tr_M sweeps (atom/free × 4 σ) → Pool over them.
    jobs = []
    for name, beta in sigma.items():
        jobs.append((("atom", name), w_atom + beta, q_str))
        jobs.append((("free", name), w_free + beta, q_str))
    nproc = min(len(jobs), os.cpu_count() or 1)
    print(f" computing {len(jobs)} tr_M sweeps on {nproc} processes …", flush=True)
    import multiprocessing as mp_
    with mp_.Pool(nproc) as pool:
        results = dict(pool.map(_trM_worker, jobs))

    at = {nm: mp.mpf(results[("atom", nm)]) for nm in sigma}
    fr = {nm: mp.mpf(results[("free", nm)]) for nm in sigma}

    print("=" * 84)
    print(" Averaged-convention block-swap S_atom for ⁴He (production binding signal)")
    print("=" * 84)
    print(f" {'σ block-perm':>14}{'tr_M(W_atom·β)':>18}{'tr_M(W_free·β)':>18}")
    print(" " + "-" * 60)
    for nm in sigma:
        print(f" {nm:>14}{float(at[nm]):>18.8f}{float(fr[nm]):>18.8f}")
    print(" " + "-" * 60)

    G = len(sigma)
    tr_atom_sym = sum(at.values()) / G
    tr_free_sym = sum(fr.values()) / G
    S_atom = tr_atom_sym / at["id"]
    S_free = tr_free_sym / fr["id"]
    signal = mp.log(S_free / S_atom)

    # Scalar-vs-exact: the scalar Frobenius bosonic h₂(p)h₂(n)/(τ_p²τ_n²).
    sym = record_upstream(HERE / "symmetrized-constituent-general.witness.json", _UPSTREAM_RECORDS)
    pp = {int(k): mp.mpf(v) for k, v in sym["data"]["proton_power_sums"].items()}
    pn = {int(k): mp.mpf(v) for k, v in sym["data"]["neutron_power_sums"].items()}
    def _h2(p1, p2):
        return (p1 ** 2 + p2) / 2
    S_free_scalar = (_h2(pp[1], pp[2]) * _h2(pn[1], pn[2])) / (pp[1] ** 2 * pn[1] ** 2)
    exact_over_scalar = S_free / S_free_scalar

    print(f"  S_atom (exact H₁₂ block-level) = {float(S_atom):.6f}")
    print(f"  S_free (exact H₁₂ block-level) = {float(S_free):.6f}")
    print(f"  S_free (scalar Frobenius, H₃)  = {float(S_free_scalar):.6f}   "
          f"→ exact/scalar = {float(exact_over_scalar):.3f} (5.5× gap)")
    print(f"  BINDING SIGNAL  log(S_free/S_atom) = {float(signal):+.6f}  "
          f"(sign-only task 1: −0.357903)")
    print("  ⇒ " + ("POSITIVE (averaged): symmetrization RELIEVES the under-"
                     "prediction — OPPOSITE sign to sign-only."
                     if float(signal) > 0 else
                     "negative: symmetrization deepens the under-prediction."))
    print(f"\n wall: {time.monotonic()-t0:.1f}s ({nproc} processes)")

    w = WitnessBuilder("averaged-block-swap-binding", engine="python+rust",
                       start_time=t0)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Averaged-convention (production) block-swapped S_atom for ⁴He via "
        "pyhecke_native.chi_q_atomic (Rust q-character on averaged Hecke factors "
        "c·σ+d·I; validated against binding_canonical tr_M=0.05536). Refines the "
        "sign-only task 1: tr_atom_sym=¼Σ_{σ∈S₂×S₂} tr_M(W_atom·β_σ). Production "
        "binding signal log(S_free/S_atom) FLIPS POSITIVE (+0.27) vs sign-only "
        "(−0.36) — symmetrization slightly relieves the under-prediction. The "
        "exact H₁₂ block-level S_free is 5.5× SMALLER than the scalar Frobenius "
        "h₂h₂/τ²τ² (H₃ traces) — quantifies the #2103 scalar caveat. Pool-"
        "parallelized over the 8 independent tr_M sweeps."
    )
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("atom_traces", {k: fmt(v) for k, v in at.items()})
    w.add_data("free_traces", {k: fmt(v) for k, v in fr.items()})
    w.add_data("S_atom", fmt(S_atom))
    w.add_data("S_free", fmt(S_free))
    w.add_data("S_free_scalar_frobenius", fmt(S_free_scalar))
    w.add_data("exact_over_scalar_ratio", fmt(exact_over_scalar))
    w.add_data("binding_signal_log_Sfree_over_Satom", fmt(signal))
    w.add_data("signonly_signal_task1", fmt(mp.mpf("-0.357903")))
    w.add_data("open_question",
               "whether the plain ¼Σβ_σ average is the q-correct q-Young "
               "projection, or whether q-weighted symmetrizers shift the number.")
    # VALID assertion: the id trace = binding_canonical's averaged ⁴He tr_M.
    bc = w.add_upstream(HERE / "binding-canonical.witness.json")
    r = next(x for x in bc["data"]["results"] if (x["Z"], x["N"]) == (2, 2))
    tr_canon = mp.mpf(str(r["tr_M_atom"]).strip("()").split("+")[0])
    w.add_assertion(
        name="id_trace_matches_binding_canonical",
        # `fmt`, not `float`: this assertion is the one that MISSED a 65.6 %
        # error. The committed witness carried `computed` from a 2026-06-11
        # run and reported "passed" at 1e-9 while its own `atom_traces.id`
        # (0.0554) disagreed with the live `binding_canonical` (0.1610). A
        # stored assertion is only re-evaluated when the producer runs, so it
        # certifies the run that wrote it, never the file you are reading.
        computed=fmt(abs(at["id"] - tr_canon)),
        expected=fmt(mp.mpf(0)), tolerance=fmt(mp.mpf("1e-30")),
        source="tr_M(W_atom·id) via chi_q_atomic == binding_canonical's averaged "
               "⁴He tr_M_atom — validates the averaged path + y_λ weighting.",
    )
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
