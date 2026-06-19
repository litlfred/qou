#!/usr/bin/env python3
"""H₆ deuteron per-partition characters χ_λ — first live datum (item A, PR #2485).

The binding tower-convergence gate needs χ_λ(𝓑_n − 𝓑_p) at n = 6, 9, 12; only
H₃ existed live (the H₆ work was deprecated). `atom_braid_word_3A` is already
general-A (3 strands × A nucleons), so the deuteron (Z=1, N=1, A=2) gives a
6-strand word in H₆. This probe builds the Hoefsmit seminormal reps for every
λ ⊢ 6 and evaluates χ_λ on the deuteron word — the per-partition characters
that the tower-convergence test consumes.

Scope: this produces the *characters* only (the missing data). The full
tower-convergence test (T_beta selector, χ_λ(𝓑_n − 𝓑_p) difference) is the
follow-on per docs/audits/2026-06-17-jacobi-anger-physical-weight-n3.md.

Run:  PYTHONPATH=...:tools/pyhecke/python python3 -u probes/h6_deuteron_chi_lambda_probe.py
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


def main():
    from pyhecke.gram import h as gram_h
    h = float(gram_h)
    q0 = (h + math.sqrt(h * h + 4.0)) / 2.0  # h = q − 1/q ⇒ q = (h+√(h²+4))/2
    log(f"canonical substrate: h = {h:.12f}, q0 = {q0:.12f}")

    from pyhecke.syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word

    # Deuteron: Z=1, N=1 ⇒ A=2 ⇒ 3A = 6 strands ⇒ 5 generators σ_0..σ_4.
    word = atom_braid_word_3A(1, 1)
    n_gens = 5
    log(f"deuteron word: {len(word)} crossings on {n_gens} generators (H_6)")

    cache = BlockCache(q0, h)
    lambdas = partitions_of(6)
    log(f"{len(lambdas)} partitions of 6")

    results = {}
    for i, lam in enumerate(lambdas, 1):
        data = build_seminormal_matrices_cached(lam, cache=cache)
        # data convention matches the n=3 path: (sigmas, dim, ...)
        sigmas, dim = data[0], data[1]
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens)
        results[lam] = (dim, float(chi))
        log(f"  λ={lam!s:12s} dim={dim:3d}  χ_λ(deuteron)={float(chi): .9e}")

    log("=== H_6 deuteron character vector (λ ⊢ 6) ===")
    for lam, (dim, chi) in results.items():
        print(f"  {lam!s:14s} dim={dim:3d}  chi={chi: .12e}", flush=True)

    sum_dim_sq = sum(d * d for d, _ in results.values())
    log(f"Σ dim² = {sum_dim_sq} (expect 6! = 720: {'OK' if sum_dim_sq == 720 else 'MISMATCH'})")

    _emit_witness(results, q0, h, word, sum_dim_sq)
    log(f"done in {time.time() - t0:.1f}s")
    return results


def _emit_witness(results, q0, h, word, sum_dim_sq):
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
        "name": "h6-deuteron-chi-lambda",
        "description": "First live H_6 per-partition characters χ_λ of the "
                       "deuteron bound braid word (atom_braid_word_3A(1,1), "
                       "6 strands). Probe datum for the binding tower-convergence "
                       "gate; the free reference, the χ_λ(𝓑_n−𝓑_p) difference and "
                       "the T_beta selector are the follow-on (item A, PR #2485).",
        "auditOnly": True,
        "probe": True,
        "substrate": {"q0": q0, "h": h, "q0_pin": "proton (canonical)"},
        "word": {"isotope": "deuteron", "Z": 1, "N": 1, "A": 2,
                 "strands": 6, "generators": 5, "n_crossings": len(word)},
        "validation": {"sum_dim_squared": sum_dim_sq, "expected_factorial_6": 720,
                       "ok": sum_dim_sq == 720},
        "characters": [
            {"partition": list(lam), "dim": dim, "chi": chi}
            for lam, (dim, chi) in results.items()
        ],
        "witness": {"scriptCommitSha": sha, "scriptHash": script_hash,
                    "producer": "computations/probes/h6_deuteron_chi_lambda_probe.py"},
    }
    dest = os.path.join(here, "..", "h6-deuteron-chi-lambda.witness.json")
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
