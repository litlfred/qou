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
This reproduces the known single-trace deuteron under-prediction (≈ 0.47 MeV vs
AME 2.225 MeV); it is an audit datum, NOT a production binding claim — the
canonical per-isotope binding lives in `binding_canonical` and the Δ_λ gate is
the open frontier (see CLAUDE.md "Δ_λ gate"). Nothing here is wired.

Free word has NO p-n interface crossing, so it is convention-independent
(`bring_color_weighted` ≡ `strict_averaged` on the free word); the bound word
uses the canonical `bring_color_weighted`, matching #2485 exactly.

Run:  PYTHONPATH=computations:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate \
        python3 -u computations/probes/h6_deuteron_free_word_chi_lambda_probe.py
"""
import math
import sys
import time

t0 = time.time()


def log(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def partitions_of(n):
    """All partitions of n as weakly-decreasing tuples."""
    if n == 0:
        return [()]
    out = []

    def rec(remaining, maxpart, prefix):
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for p in range(min(remaining, maxpart), 0, -1):
            rec(remaining - p, p, prefix + [p])

    rec(n, n, [])
    return out


# β-decay Q-value calibration E₀ (free-neutron), per prop:categorical-mass-markov.
E_0_MEV = 0.78233341
B_D_AME_MEV = 2.224573  # AME2020 deuteron binding (audit comparison only)


def main():
    from pyhecke.gram import h as gram_h
    h = float(gram_h)
    q0 = (h + math.sqrt(h * h + 4.0)) / 2.0  # h = q − 1/q ⇒ q = (h+√(h²+4))/2
    log(f"canonical substrate: h = {h:.12f}, q0 = {q0:.12f}")

    from pyhecke.syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word
    from wedderburn_jones_markov import y_lambda_at

    # Deuteron: Z=1, N=1 ⇒ A=2 ⇒ 3A = 6 strands ⇒ generators σ_0..σ_4.
    word_bound = atom_braid_word_3A(1, 1, include_inter=True)
    word_free = atom_braid_word_3A(1, 1, include_inter=False)
    n_gens = 5
    log(f"bound word: {len(word_bound)} crossings; free word: {len(word_free)} "
        f"crossings on {n_gens} generators (H_6)")

    cache = BlockCache(q0, h)
    lambdas = partitions_of(6)
    y6 = {tuple(k): float(v) for k, v in y_lambda_at(6, q0).items()}
    log(f"{len(lambdas)} partitions of 6; canonical Wenzl y_λ loaded")

    results = []
    trM_bound = 0.0
    trM_free = 0.0
    for lam in lambdas:
        data = build_seminormal_matrices_cached(lam, cache=cache)
        sigmas, dim = data[0], data[1]
        chi_b = chi_lambda_of_word(sigmas, dim, word_bound, n_gens)
        chi_f = chi_lambda_of_word(sigmas, dim, word_free, n_gens)
        y_lam = y6.get(lam, 0.0)
        trM_bound += y_lam * chi_b
        trM_free += y_lam * chi_f
        results.append((lam, dim, float(chi_b), float(chi_f), y_lam))
        log(f"  λ={lam!s:14s} dim={dim:3d}  χ_bound={chi_b: .8e}  "
            f"χ_free={chi_f: .8e}  Δχ={chi_b - chi_f: .6e}")

    sum_dim_sq = sum(d * d for _, d, _, _, _ in results)
    log(f"Σ dim² = {sum_dim_sq} (expect 6! = 720: "
        f"{'OK' if sum_dim_sq == 720 else 'MISMATCH'})")

    b_pred = E_0_MEV * (abs(trM_free) - abs(trM_bound))
    log(f"tr_M(bound) = {trM_bound:.8f}   tr_M(free) = {trM_free:.8f}")
    log(f"B_pred (single-trace) = E₀·(|tr_M_free|−|tr_M_atom|) = {b_pred:.6f} MeV "
        f"(AME B_D = {B_D_AME_MEV} MeV — single-trace under-predicts, audit only)")

    _emit_witness(results, q0, h, word_bound, word_free, sum_dim_sq,
                  trM_bound, trM_free, b_pred)
    log(f"done in {time.time() - t0:.1f}s")
    return results


def _emit_witness(results, q0, h, word_bound, word_free, sum_dim_sq,
                  trM_bound, trM_free, b_pred):
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
        "substrate": {"q0": q0, "h": h, "q0_pin": "proton (canonical)"},
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
            "tr_M_bound": trM_bound,
            "tr_M_free": trM_free,
            "delta_tr_M_free_minus_bound": trM_free - trM_bound,
            "B_pred_single_trace_MeV": b_pred,
            "note": "single-trace B under-predicts AME; audit only, not wired",
        },
        "characters": [
            {"partition": list(lam), "dim": dim,
             "chi_bound": chi_b, "chi_free": chi_f,
             "delta_chi_bound_minus_free": chi_b - chi_f, "y_lambda": y_lam}
            for (lam, dim, chi_b, chi_f, y_lam) in results
        ],
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/h6_deuteron_free_word_chi_lambda_probe.py"},
    }
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
