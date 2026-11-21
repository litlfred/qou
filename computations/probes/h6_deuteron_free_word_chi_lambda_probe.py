#!/usr/bin/env python3
"""H₆ deuteron FREE-word per-partition characters χ_λ — the free reference
(item-A follow-on to PR #2485).

PR #2485 produced the *bound* deuteron character vector χ_λ(W_atom) at H₆
(`h6_deuteron_chi_lambda_probe.py`, `include_inter=True`), and its witness
explicitly deferred "the free reference, the χ_λ(𝓑_n−𝓑_p) difference and the
T_beta selector" to a follow-on. This probe supplies the **free reference**:
the deuteron's free word `atom_braid_word_3A(1, 1, include_inter=False)` — the
same two nucleons with the inter-nucleon binding crossing removed — and pairs
it with the bound word so the per-partition binding difference
Δχ_λ = χ_λ(bound) − χ_λ(free) and the Markov-weighted trace difference are
both materialised at λ ⊢ 6.

The binding prediction here is the single-trace form
    B = E₀ · ( |tr_M(W_free)| − |tr_M(W_atom)| ),   tr_M = Σ_λ y_λ(q₀) χ_λ,
with y_λ the canonical Wenzl/Jones–Markov weights (`wedderburn_jones_markov`).
This reproduces the known single-trace deuteron under-prediction (0.435403 MeV
vs AME 2.225 MeV — the docstring previously said "≈ 0.47", which no run of this
probe has produced); it is an audit datum, NOT a production binding claim — the
canonical per-isotope binding lives in `binding_canonical` and the Δ_λ gate is
the open frontier (see AGENTS.md "Δ_λ gate"). Nothing here is wired.

Free word has NO p-n interface crossing, so it is convention-independent
(`bring_color_weighted` ≡ `strict_averaged` on the free word); the bound word
uses the canonical `bring_color_weighted`, matching #2485 exactly.

Run:  python3 -u computations/probes/h6_deuteron_free_word_chi_lambda_probe.py
"""
import math
import sys
import time
from pathlib import Path as _Path

# `_precision` was imported at module level while the only `sys.path` setup
# sat at line ~221, INSIDE the witness-writing function -- so the import ran
# first and died unless the caller had exported the PYTHONPATH the docstring
# above used to demand. A producer that cannot be started without out-of-band
# knowledge is a producer no gate can run, and its witness can never go stale.
# `_path_bridge` sets every path this file needs. Bean `qou/ti1n`.
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import fmt as _fmt  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)

t0 = time.time()


def log(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


# β-decay Q-value calibration E₀ (free-neutron), per prop:categorical-mass-markov.
E_0_MEV = 0.78233341
B_D_AME_MEV = float(AME_B_DEUTERON_MEV_VALIDATION)  # AME2020 deuteron binding (audit comparison only)


def main():
    # NO FLOAT64 (AGENTS.md "PROBES ARE NOT EXEMPT", bean qou-stqr).
    # Was:  h = float(pyhecke.gram.h); q0 = (h + math.sqrt(h*h + 4))/2
    # Two leaks in two lines — `gram.h` is the float64 module constant (5.0e-17
    # off exact), and q0 was then recovered from it by inverting h = q − 1/q
    # through a float64 math.sqrt. The inversion is also backwards: q0 is the
    # primitive the corpus publishes at 50 digits, h is the derived quantity.
    # Now taken in the canonical direction, exactly.
    from q_parameter import Q_50_DIGIT_STR as _Q50
    # Built at >= 60 dps regardless of ambient precision: an mpf keeps the
    # precision it was CREATED at, so mpf(str(q0)) under mpmath's default
    # (dps=15) bakes in a 15-digit q0 (3.0e-17 error) which _precision.fmt
    # then PADS to 60 digits — a float64-padding artifact, and strictly worse
    # than the honest float it replaced. Same trap mass_at_3A_proper.py
    # documents at its own workdps(60).
    with mp.workdps(max(mp.mp.dps, 60)):
        q0 = +mp.mpf(str(_Q50))
        h = +(q0 - 1 / q0)
    log(f"canonical substrate: h = {mp.nstr(h, 14)}, q0 = {mp.nstr(q0, 14)}")

    from pyhecke.syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from hoefsmit_mpmath import (BlockCacheMP, chi_lambda_of_word_mp,
                                 seminormal_matrices_mp)
    from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word
    from wedderburn_jones_markov import y_lambda_at
    # Canonical shared partition enumerator (centralized; per Gemini review on
    # #2496 — no duplicated local helper). mass_at_3A_proper above triggers
    # _path_bridge, putting computations/hecke on the path.
    from hecke_characters import partitions_of  # noqa: E402

    # Deuteron: Z=1, N=1 ⇒ A=2 ⇒ 3A = 6 strands ⇒ generators σ_0..σ_4.
    word_bound = atom_braid_word_3A(1, 1, include_inter=True)
    word_free = atom_braid_word_3A(1, 1, include_inter=False)
    n_gens = 5
    log(f"bound word: {len(word_bound)} crossings; free word: {len(word_free)} "
        f"crossings on {n_gens} generators (H_6)")

    # NO FLOAT64 (AGENTS.md "PROBES ARE NOT EXEMPT").  The characters used to
    # come from `build_seminormal_matrices_cached` + `chi_lambda_of_word`,
    # which are float64 BY CONSTRUCTION — `BlockCache` uses `math.sqrt` against
    # a fixed 1e-15 degeneracy threshold, and the character routine accumulates
    # the word into a numpy matrix and returns `float(np.trace(...))`.  Handing
    # those an mpf q0 does not make them exact; numpy coerces on contact.  The
    # earlier fix on this file corrected only the q0/h ENTRY POINT, so the
    # witness serialised a 50-digit substrate next to a float64 payload —
    # advertising a precision the numbers did not have.
    #
    # The payload is now `hoefsmit_mpmath`, the same Hoefsmit construction
    # carried end to end in mpmath.  The float64 path is still run, but only as
    # a measured cross-check: the relative gap it reports IS the float64 floor
    # (~1e-15), not a disagreement about the mathematics.
    cache = BlockCache(float(q0), float(h))      # f64 cross-check path only
    cache_mp = BlockCacheMP(q0, h)               # the payload
    lambdas = list(partitions_of(6))
    y6 = {tuple(k): v for k, v in y_lambda_at(6, q0).items()}   # mpf, unrounded
    log(f"{len(lambdas)} partitions of 6; canonical Wenzl y_λ loaded (mpf)")

    results = []
    trM_bound = mp.mpf(0)
    trM_free = mp.mpf(0)
    f64_gaps = []
    for lam in lambdas:
        sigmas, dim, _ = seminormal_matrices_mp(lam, cache=cache_mp)
        chi_b = chi_lambda_of_word_mp(sigmas, dim, word_bound, n_gens)
        chi_f = chi_lambda_of_word_mp(sigmas, dim, word_free, n_gens)

        sig64, dim64 = build_seminormal_matrices_cached(lam, cache=cache)[:2]
        chi_b64 = chi_lambda_of_word(sig64, dim64, word_bound, n_gens)
        if chi_b != 0:
            f64_gaps.append(abs((mp.mpf(chi_b64) - chi_b) / chi_b))

        y_lam = y6.get(lam, mp.mpf(0))
        trM_bound += y_lam * chi_b
        trM_free += y_lam * chi_f
        results.append((lam, dim, chi_b, chi_f, y_lam))
        log(f"  λ={lam!s:14s} dim={dim:3d}  χ_bound={mp.nstr(chi_b, 12)}  "
            f"χ_free={mp.nstr(chi_f, 12)}  Δχ={mp.nstr(chi_b - chi_f, 8)}")

    log(f"float64 cross-check: max relative gap on χ_bound = "
        f"{mp.nstr(max(f64_gaps), 3)} — the float64 floor, not a disagreement")

    sum_dim_sq = sum(d * d for _, d, _, _, _ in results)
    log(f"Σ dim² = {sum_dim_sq} (expect 6! = 720: "
        f"{'OK' if sum_dim_sq == 720 else 'MISMATCH'})")

    b_pred = mp.mpf(E_0_MEV) * (abs(trM_free) - abs(trM_bound))
    log(f"tr_M(bound) = {mp.nstr(trM_bound, 14)}   "
        f"tr_M(free) = {mp.nstr(trM_free, 14)}")
    log(f"B_pred (single-trace) = E₀·(|tr_M_free|−|tr_M_atom|) = "
        f"{mp.nstr(b_pred, 10)} MeV (AME B_D = {B_D_AME_MEV} MeV — "
        f"single-trace under-predicts, audit only)")

    _emit_witness(results, q0, h, word_bound, word_free, sum_dim_sq,
                  trM_bound, trM_free, b_pred, f64_gaps)
    log(f"done in {time.time() - t0:.1f}s")
    return results


def _emit_witness(results, q0, h, word_bound, word_free, sum_dim_sq,
                  trM_bound, trM_free, b_pred, f64_gaps):
    import hashlib
    import json
    import os
    import subprocess

    here = os.path.dirname(os.path.abspath(__file__))
    script = os.path.abspath(__file__)
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", script],
            cwd=here, text=True).strip()
    except Exception:
        sha = None
    with open(script, "rb") as f:
        script_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    out = {
        "name": "h6-deuteron-free-word-chi-lambda",
        "description": "First live H_6 FREE-word per-partition characters χ_λ of "
                       "the deuteron (atom_braid_word_3A(1,1, include_inter=False), "
                       "6 strands) — the free reference deferred by the #2485 bound "
                       "probe. Pairs bound/free χ_λ, the per-partition binding "
                       "difference Δχ_λ, and the Wenzl-weighted single-trace tr_M "
                       "difference. Audit datum; the single-trace B under-predicts "
                       "(Δ_λ gate is the open frontier). Nothing wired.",
        "auditOnly": True,
        "probe": True,
        # mpf -> output-precision strings via the canonical serializer
        # (AGENTS.md: "carry the value as mpmath.mpf from its source and
        # serialize with _precision.fmt"). Previously these were float64.
        "substrate": {"q0": _fmt(q0), "h": _fmt(h),
                      "q0_pin": "proton (canonical)"},
        "word": {"isotope": "deuteron", "Z": 1, "N": 1, "A": 2,
                 "strands": 6, "generators": 5,
                 "n_crossings_bound": len(word_bound),
                 "n_crossings_free": len(word_free),
                 "pn_convention_bound": "bring_color_weighted",
                 "free_word_convention_independent": True},
        "validation": {"sum_dim_squared": sum_dim_sq,
                       "expected_factorial_6": 720,
                       "ok": sum_dim_sq == 720},
        "calibration": {"E_0_MeV": E_0_MEV, "B_D_AME_MeV": B_D_AME_MEV},
        "markov_trace": {
            "tr_M_bound": _fmt(trM_bound),
            "tr_M_free": _fmt(trM_free),
            "delta_tr_M_free_minus_bound": _fmt(trM_free - trM_bound),
            "B_pred_single_trace_MeV": _fmt(b_pred),
            "note": "single-trace B under-predicts AME; audit only, not wired",
        },
        "arithmetic": {
            "characters": "mpmath (hoefsmit_mpmath), not float64",
            "why": "the canonical fast path (BlockCache + chi_lambda_of_word) is "
                   "float64 by construction — math.sqrt against a 1e-15 threshold, "
                   "and float(np.trace(...)). Passing it an mpf q0 does not make it "
                   "exact. Per AGENTS.md 'PROBES ARE NOT EXEMPT'.",
            "f64_max_relative_gap_on_chi_bound": _fmt(max(f64_gaps)),
            "f64_gap_reading": "this IS the float64 floor, not a disagreement about "
                               "the mathematics",
        },
        "characters": [
            {"partition": list(lam), "dim": dim,
             "chi_bound": _fmt(chi_b), "chi_free": _fmt(chi_f),
             "delta_chi_bound_minus_free": _fmt(chi_b - chi_f),
             "y_lambda": _fmt(y_lam)}
            for (lam, dim, chi_b, chi_f, y_lam) in results
        ],
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/h6_deuteron_free_word_chi_lambda_probe.py"},
    }
    import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _sys.path.insert(0, os.path.join(here, "..", "substrate"))
    from _precision import fmt as _fmt_unused  # noqa: E402,F401
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    dest = os.path.join(here, "..", "h6-deuteron-free-word-chi-lambda.witness.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"[witness] wrote {os.path.normpath(dest)}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)
