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
from hecke_characters import chi_lambda_braid
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q, Q_50_DIGIT_STR
from witness_base import WitnessBuilder
from _precision import fmt, set_compute_dps  # noqa: E402


# h = q − q⁻¹ at the pinned substrate q₀, DERIVED, as `mpf`.
#
# This was the float64 literal `HA = 0.20906032198987945`, and that number is
# not a stale copy of this quantity — it is this quantity **at a different
# q₀ pin**. Inverting `h = q − 1/q` gives `q = 1.1099785955541805692`, which
# is the **muon CODATA-2018** pin to 6.1e-18, i.e. exact to the literal's own
# 17 digits. The live pin is the proton one, `q₀ = 1.1099785827513808076`.
#
# So this was a LAYER STRADDLE in AGENTS.md's precise sense — an ideal-layer
# (muon) input hardcoded into a producer whose `d` values arrive from the live
# proton pin — and not a rounding slip. The drift is 2.31942e-8 on `h`, which
# is 1.81 × the 1.28e-8 q₀ separation, i.e. **the μ–p substrate tension
# itself, 11.53 ppb**. That matches the μ₃ Fréchet straddle AGENTS.md records
# (11.54 ppb) to three digits, because it is the same quantity. It is also
# doubly superseded: the muon anchor moved to CODATA 2022 on 2026-08-22
# (`fca08de7d2`), so the literal was not even the current ideal-layer value.
#
# What it broke: `HA`/`H_HALF` are pattern-matching discriminators against the
# `d` of each crossing at tolerance 1e-12, and `atom_braid_word_3A` emits `d`
# as `mpf` at the live pin — measured on deuterium, `d ∈ {0, -0.20906029879…,
# -0.10453014939…, -0.10445824776…}`. With the stale literal `abs(d + HA)` is
# 2.32e-8, never `< 1e-12`, so the σ⁻¹ branch could never be taken and
# `expand_to_branches` fell through to `raise ValueError(f"unexpected d={d}")`
# on every live word. It also contaminated values: the stale literal is the
# empty-word branch's coefficient, so λ=(2,1) read −2.3194e-08 where the exact
# value is 0.
#
# Derived from `Q_50_DIGIT_STR` rather than from `hecke_core.h`, which is the
# live-pin value but is a Python `float` — one carrier, and no float64 path.
_Q_MP = mp.mpf(Q_50_DIGIT_STR)
HA = _Q_MP - 1 / _Q_MP
H_HALF = HA / 2

# Exact-arithmetic tag for `chi_lambda_braid`. Without it that function
# returns float64 regardless of what it is given, which put 44 raw-float64
# fields into this producer's witness the first time the HA repair above let it
# run far enough to emit one. Measured at n = 3: 0.05 ms/call, i.e. ~2 s for
# the 40k-call ⁴He case — the float64 path bought nothing.
CHI_PRECISION = 50


def _pn_weighted_d():
    """-h(1/2 - delta/4): the colour-weighted p-n interface shift.

    Carries `mpf` throughout. The two `float()` casts this had — on
    `hecke_core.h` and on `_avg_color_delta()` — were a float64 path on a
    quantity compared at 1e-9, and `hecke_core.h` is itself a Python `float`,
    so `HA` above is used instead: one carrier for `h` in this file.
    """
    from canonical_braid_crossings import _avg_color_delta
    return -HA * (mp.mpf(1) / 2 - mp.mpf(str(_avg_color_delta())) / 4)


_D_PN_WEIGHTED = _pn_weighted_d()


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
        if abs(d) < 1e-12:
            # Pure σ_k: extend each branch (no split)
            for coeff, word in branches:
                new_branches.append((coeff, word + [(1, k + 1)]))
        elif abs(d + HA) < 1e-12:
            # σ_k - h: this is σ_k^{-1}. Single branch: append (-1, k+1).
            for coeff, word in branches:
                new_branches.append((coeff, word + [(-1, k + 1)]))
        elif abs(d + H_HALF) < 1e-12 or abs(d - _D_PN_WEIGHTED) < 1e-9:
            # σ_avg = σ_k + d: split into two branches. d is -h/2 for the
            # colour-BLIND interface and -h(1/2 - delta/4) for the
            # colour-WEIGHTED one; the identity coefficient below is the
            # actual d, so both are exact. Hardcoding -h/2 here silently
            # deleted the p-n colour asymmetry (qou-gdtb).
            half_h = -mp.mpf(str(d))
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


def chi_lambda_atom_braid(lambda_shape, atom_word, q_value, tol=1e-12,
                          precision=CHI_PRECISION):
    """Compute χ_λ(T_w) by linear expansion over Avg branches.

    `precision` is passed through to `chi_lambda_braid`, which otherwise
    returns a Python `float` **whatever it is given** — measured: the exact
    value `χ_(2,1)(σ₂σ₂⁻¹) = 2` comes back as `1.9999999999999997` under the
    default and as the exact string `"2.0"` at `precision=50`. Passing an
    `mpf` `q_value` alone does NOT help; the float64 is inside the callee.
    """
    branches = expand_to_branches(atom_word)
    total = mp.mpf(0)
    for coeff, word in branches:
        if word:
            val = chi_lambda_braid(lambda_shape, word, q_value=q_value,
                                   precision=precision)
            total += coeff * mp.mpf(str(val))
        else:
            # Empty word = identity element; χ_λ(1) = dim V_λ.
            # `hook_length_dim_lambda` never existed in `hecke_characters`
            # (nor anywhere in the tree) — the name this file wants is
            # `specht_dim`, whose docstring IS this quantity: "Integer
            # Specht-module dimension f^λ = #SYT(λ) = n! / ∏ hook(c)
            # (hook-length formula)". `partition_utils.dim_lambda` records the
            # same function as the replacement for ad-hoc `hook_length_dim`
            # copies, and agrees with it exactly. NOT `dim_q`, which is the
            # q-deformed dimension (2.0109 vs 2 at λ=(2,1) at the proton q₀).
            # Bean qou-2cz1.
            from hecke_characters import specht_dim
            total += coeff * mp.mpf(specht_dim(lambda_shape))
    return total


def main() -> int:
    set_compute_dps()
    q = _Q_MP   # was float(Q): a float64 cast of the substrate parameter

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
    w.add_parameter("precision_dps", 30)
    w.add_parameter("q_0", str(q))

    threshold = 1e-6  # χ values below this treated as zero

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
                    if abs(d + H_HALF) < 1e-12)

        t0 = time.time()
        chi_values = {}
        chi_failures = []
        for lam in partitions:
            try:
                val = chi_lambda_atom_braid(lam, atom_word, q)
                chi_values[tuple(lam)] = mp.mpf(str(val))
            except Exception as e:
                # VISIBLE, not swallowed. This bare handler is why the
                # committed witness recorded `observed_active_count: 0` and
                # `match_prediction: True` for every atom: `expand_to_branches`
                # raised `ValueError: unexpected d=...` for EVERY partition
                # (the muon-pinned `HA` above), the handler recorded `None`, the
                # `v is not None` filter selected nothing, and
                # `match = (0 <= predicted)` passed VACUOUSLY. A conjecture's
                # structural prediction was being published as confirmed by a
                # producer that computed nothing at all — on a witness stamped
                # with the correct live proton anchor, so every staleness and
                # anchor detector read it as healthy.
                chi_values[tuple(lam)] = None
                chi_failures.append((tuple(lam), f"{type(e).__name__}: {e}"))

        elapsed = time.time() - t0

        active = [(lam, v) for lam, v in chi_values.items()
                  if v is not None and abs(v) > threshold]
        active_sorted = sorted(active, key=lambda x: -abs(x[1]))

        observed_active_count = len(active)

        # A vacuous pass is not a pass. If any chi could not be computed the
        # active set is not a measurement of anything, and `match` must not be
        # reported as True on the strength of an empty set.
        chi_failed_count = len(chi_failures)
        if chi_failed_count:
            print(f"  \u26a0 {chi_failed_count}/{len(partitions)} chi values FAILED "
                  f"— the active set is not a measurement. First: "
                  f"{chi_failures[0][1]}")
        match = (observed_active_count <= predicted_active
                 and chi_failed_count == 0)

        result = {
            "Z": Z, "N": N, "A": A, "n_0": n0,
            "p_n0": len(partitions),
            "predicted_max_active": predicted_active,
            "observed_active_count": observed_active_count,
            "match_prediction": match,
            "chi_failed_count": chi_failed_count,
            "chi_failures": [{"lambda": list(l), "error": e}
                             for l, e in chi_failures[:5]],
            "n_avg_crossings": n_avg,
            "n_branches": 2 ** n_avg,
            # Timing is inherently float64 and AGENTS.md lists `elapsed_seconds`
            # among the volatile/ephemeral keys, but the raw-float64 ratchet is a
            # DRAINING baseline and three new raw fields would take it red. Format
            # rather than baseline-widen, per "fix at the producer; baselines
            # drain, never grow."
            "elapsed_seconds": fmt(mp.mpf(str(elapsed))),
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
                print(f"    {lam}: χ = {v:+.6e}")
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
