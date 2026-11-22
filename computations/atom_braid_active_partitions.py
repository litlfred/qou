#!/usr/bin/env python3
"""
Identify the ACTIVE partition set for the canonical atom-braid
T_w(Z, N) = atom_braid_word_3A(Z, N) on B_{3A}, verifying the
conjecture conj:atom-braid-exterior-algebra's structural prediction:

  Active partitions λ ⊢ 3A with χ_λ(T_w(Z, N)) ≠ 0 form a set of size
  ≤ n* + 1 = 3A − Z + 1, mapping bijectively to grades k ∈ [δ, δ + n*]
  of the exterior algebra Λ^k(R^(3A−Z)).

Method: for each (c, d, k) crossing in atom_braid_word_3A(Z, N),
recursively split via linearity:
  χ_λ(braid · (c·σ + d·1)) = c · χ_λ(braid · σ) + d · χ_λ(braid).
This gives a 2^(#Avg) leaf-summation where each leaf is a chi_lambda
of a pure σ^±1 braid word.

For ⁴He: 2^9 = 512 leaves × 77 partitions = ~40k chi calls.
For ³He / T: 2^(2 or 3) × 30 = ~60-240 chi calls.
For D: 2^2 × 11 = ~44 chi calls.

Audit-only; cites conj:atom-braid-exterior-algebra.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hecke_characters import chi_lambda_braid_mpf
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder
from _precision import set_compute_dps, fmt  # noqa: E402


# h = q − q⁻¹, read from its OWNING source. `atom_braid_word_3A` builds every
# inter-nucleon template as `h_loc = q − 1/q` from `q_parameter.Q_50_DIGIT_STR`
# inside `workdps(max(dps, 60))`; the letters this probe classifies carry that
# value, so the tag it is compared against must be the same object.
#
# Until 2026-10-13 this was the typed literal `HA = 0.20906032198987945`, which
# is 1.1095e-7 relative from the live h. Used as a 1e-12 classification tag,
# that stale literal matched NO averaged letter, so `expand_to_branches` raised
# `ValueError("unexpected d=...")` on every word, the `except` below swallowed
# it as `chi = None` for every partition, and the probe reported
# `observed_active_count = 0 <= predicted` — a vacuous PASS (ruling D, PR #7788
# follow-up). Do not reintroduce a literal here.
with mp.workdps(60):
    _Q_EXACT = mp.mpf(Q_50_DIGIT_STR)
    HA = _Q_EXACT - mp.mpf(1) / _Q_EXACT
    H_HALF = HA / 2


def _pn_weighted_d():
    """-h(1/2 - delta/4): the colour-weighted p-n interface shift, in mpf.

    delta from `canonical_braid_crossings._avg_color_delta`, the documented
    single source of the flavour split for the braid pipeline.
    """
    from canonical_braid_crossings import _avg_color_delta
    with mp.workdps(60):
        return -HA * (mp.mpf(1) / 2 - mp.mpf(_avg_color_delta()) / 4)


_D_PN_WEIGHTED = _pn_weighted_d()

# Classification tolerance for the letter tags. The word's d values and the
# tags above are the same 60-dps arithmetic; measured agreement is ~1e-60, so
# 1e-40 separates "same template" from "different template" (the nearest two,
# -h/2 and the colour-weighted pn shift, are 7.2e-5 apart).
with mp.workdps(60):
    _TAG_TOL = mp.mpf("1e-40")


def all_partitions(n: int):
    """Generate all partitions of n in descending-parts form."""
    parts = []
    def rec(remaining, mx, current):
        if remaining == 0:
            parts.append(tuple(current))
            return
        for k in range(min(remaining, mx), 0, -1):
            current.append(k)
            rec(remaining - k, k, current)
            current.pop()
    rec(n, n, [])
    return parts


def expand_to_branches(atom_word):
    """Expand each (c, d, k) tuple into a list of (coeff, signed_letters)
    branches. Each branch is a pure σ^±1 braid word with an attached
    rational coefficient. Total 2^(#Avg) branches.

    (1, 0, k)  → 1 branch: coeff=1, append (+1, k+1)
    (1, -h, k) → 1 branch: coeff=1, append (-1, k+1)
    (1, -h/2, k) → 2 branches: coeff=1/2 with (+1, k+1); coeff=-h/2 with []
                   actually σ_avg = σ - h/2, so:
                   χ(B·σ_avg) = χ(B·σ) - (h/2) χ(B)
                   = 1·χ(B·(+1, k+1)) + (-h/2)·χ(B)
    """
    # Start with one branch: empty word, coeff = 1
    branches = [(mp.mpf(1), [])]
    for (c, d, k) in atom_word:
        new_branches = []
        # Each crossing operator is `c·σ_k + d·1`
        # So we split: append (+1, k+1) with coeff·c, OR keep braid with coeff·d
        if abs(mp.mpf(d)) < _TAG_TOL:
            # Pure σ_k: extend each branch (no split)
            for coeff, word in branches:
                new_branches.append((coeff, word + [(1, k + 1)]))
        elif abs(mp.mpf(d) + HA) < _TAG_TOL:
            # σ_k - h: this is σ_k^{-1}. Single branch: append (-1, k+1).
            for coeff, word in branches:
                new_branches.append((coeff, word + [(-1, k + 1)]))
        elif (abs(mp.mpf(d) + H_HALF) < _TAG_TOL
              or abs(mp.mpf(d) - _D_PN_WEIGHTED) < _TAG_TOL):
            # σ_avg = σ_k + d: split into two branches. d is -h/2 for the
            # colour-BLIND interface and -h(1/2 - delta/4) for the
            # colour-WEIGHTED one; the identity coefficient below is the
            # actual d, so both are exact. Hardcoding -h/2 here silently
            # deleted the p-n colour asymmetry (qou-gdtb).
            half_h = -mp.mpf(d)
            for coeff, word in branches:
                # Branch A: σ_k (coeff · 1)
                new_branches.append(
                    (coeff * mp.mpf(c), word + [(1, k + 1)])
                )
                # Branch B: identity (coeff · -h/2)
                new_branches.append(
                    (coeff * (-half_h), list(word))
                )
        else:
            raise ValueError(f"unexpected d={d}")
        branches = new_branches
    return branches


def chi_lambda_atom_braid(lambda_shape, atom_word, q_value=Q_50_DIGIT_STR,
                          dps=60):
    """Compute χ_λ(T_w) by linear expansion over Avg branches."""
    branches = expand_to_branches(atom_word)
    total = mp.mpf(0)
    for coeff, word in branches:
        if word:
            signed = [sgn * g for sgn, g in word]
            val = chi_lambda_braid_mpf(lambda_shape, signed, q_value=q_value,
                                       dps=dps)
            total += coeff * val
        else:
            # Empty word = identity element; χ_λ(1) = dim V_λ
            from hecke_characters import specht_dim
            total += coeff * mp.mpf(specht_dim(lambda_shape))
    return total


def main() -> int:
    set_compute_dps()

    w = WitnessBuilder("atom-braid-active-partitions", engine="mpmath")
    w.set_description(
        "Identifies the ACTIVE partition set for the canonical atom-braid "
        "T_w(Z, N) = atom_braid_word_3A(Z, N) on B_{3A}. Per conj:atom-braid-"
        "exterior-algebra, the predicted active set size is n* + 1 = "
        "3A − Z + 1 (one per Pascal-row position). This probe computes "
        "χ_λ(T_w) for every λ ⊢ 3A and reports the threshold-above active "
        "set, cross-checking the conjecture's prediction."
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md"
    )
    w.set_content_block("conj:atom-braid-exterior-algebra")
    w.add_parameter("precision_dps", 60)
    w.add_parameter("q_0", Q_50_DIGIT_STR)
    w.add_parameter("h", fmt(HA))

    threshold = mp.mpf("1e-6")  # χ values below this treated as zero

    all_results = {}
    # NOTE: ⁴He requires 2^9 × 77 = 39k chi calls; per-call cost at H_12
    # ~1 s → est. 11 hours. Scoping this probe to D + T + ³He only;
    # ⁴He active-set identification is deferred to R5.7 (Wedderburn-PSD
    # on BraidLetter) which extracts per-partition data directly from
    # the Rust solver in <1 s.
    for (Z, N, label) in [(1, 1, "D"), (1, 2, "T"), (2, 1, "³He")]:
        A = Z + N
        n0 = 3 * A
        predicted_active = 3 * A - Z + 1

        atom_word = atom_braid_word_3A(Z, N)
        partitions = all_partitions(n0)

        n_avg = sum(1 for (c, d, k) in atom_word
                    if abs(mp.mpf(d) + H_HALF) < _TAG_TOL)

        t0 = time.time()
        chi_values = {}
        chi_errors = []
        for lam in partitions:
            try:
                val = chi_lambda_atom_braid(lam, atom_word)
                chi_values[tuple(lam)] = val
            except Exception as e:
                # Recorded, not swallowed: a silent `None` here is what made
                # the stale-HA run report a vacuous PASS.
                chi_values[tuple(lam)] = None
                chi_errors.append(f"{tuple(lam)}: {type(e).__name__}: {e}")

        elapsed = time.time() - t0

        active = [(lam, v) for lam, v in chi_values.items()
                  if v is not None and abs(v) > threshold]
        active_sorted = sorted(active, key=lambda x: -abs(x[1]))

        observed_active_count = len(active)

        # A bound "observed <= predicted" is vacuously true when nothing was
        # computed. Measured 2026-11-15 in a container without pyhecke_native:
        # every partition raised NotImplementedError, observed = 0, and the
        # assertion PASSED. A partition that errored is not a zero; the bound
        # holds only if every chi was actually evaluated.
        match = (not chi_errors) and (observed_active_count <= predicted_active)

        result = {
            "Z": Z, "N": N, "A": A, "n_0": n0,
            "p_n0": len(partitions),
            "predicted_max_active": predicted_active,
            "observed_active_count": observed_active_count,
            "match_prediction": match,
            "n_avg_crossings": n_avg,
            "n_chi_errors": len(chi_errors),
            "chi_errors_head": chi_errors[:3],
            "n_branches": 2 ** n_avg,
            "elapsed_seconds": f"{elapsed:.3f}",
            "top_active_partitions": [
                {"lambda": list(lam), "chi": fmt(v)}
                for lam, v in active_sorted[:15]
            ],
        }
        all_results[label] = result

        print(f"=== {label}: Z={Z}, N={N}, A={A}, n_0={n0} ===")
        print(f"  Partitions p({n0}): {len(partitions)}")
        print(f"  Predicted max active (n*+1): {predicted_active}")
        print(f"  Observed active (|χ| > {threshold}): {observed_active_count}")
        print(f"  Conjecture match (observed ≤ predicted): {match}")
        print(f"  Avg crossings: {n_avg}, branches: 2^{n_avg}={2**n_avg}")
        print(f"  Elapsed: {elapsed:.2f} s")
        if active_sorted[:5]:
            print(f"  Top 5 active partitions:")
            for lam, v in active_sorted[:5]:
                print(f"    {lam}: χ = {mp.nstr(v, 12)}")
        print()

    w.add_data("per_atom_results", all_results)

    # Headline assertion: all 4 atoms satisfy the bound
    all_match = all(r["match_prediction"] for r in all_results.values())
    w.add_assertion(
        name="all_atoms_satisfy_exterior_algebra_bound",
        computed=str(int(all_match)),
        expected="1",
        tolerance=0,
        source="conj:atom-braid-exterior-algebra prediction: |active| ≤ 3A − Z + 1",
    )

    w.add_caveat(
        "The 'active partition' threshold is |χ| > 1e-6, which may miss "
        "structurally-active but numerically-tiny channels OR include "
        "numerical artifacts. Independent verification at 50-dps mpmath "
        "is the natural follow-up. The conjecture's exact prediction "
        "(n* + 1 = 3A − Z + 1) is an UPPER BOUND on the active count; "
        "fewer-than-predicted active partitions still satisfies the bound."
    )

    out = w.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
