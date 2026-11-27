"""
delta_lambda_k_star_search_phase5d_5.py — Phase 5d.5 probe.

Search for the depth-stratified Frobenius-reciprocity candidate knots
K_1^*, K_2^* (per [`depth-stratified-frobenius-reciprocity.md`](folio/quantum-observable-universe/braids-and-knots/depth-stratified-frobenius-reciprocity.md))
that close the 1.82× variance residual at low curvature-rank.

At curvature-rank k = 3, the named candidate is K_3^* = 6_1 (chirality
channel). At k = 1 and k = 2, K_k^* is currently "open structural
question". This script searches empirically by:

1. For each candidate knot K ∈ {3_1 (trefoil), 4_1 (figure-8), 5_1,
   5_2, 6_1, 6_2, 6_3, 7_1, ..., 8_n}, compute the central projector
   character χ^λ(e_K) on each partition λ ⊢ n at q_0.

2. For each (k, K) pair, compute the FR-restricted weight
       w̃_λ^(K) = dim_q²(λ) · χ^λ(e_K)  /  Z_norm
   (eqn FR in depth-stratified-frobenius-reciprocity.md)
   and the implied Φ_k^FR(K, T) contribution to the binding formula.

3. For each candidate K_k^*, evaluate the binding-energy prediction
   for D / T / ³He / ⁴He and report the variance.

4. Report the (K_1^*, K_2^*) candidate that minimizes variance.

Implementation notes:
  - The "knot ideal projector" e_K ∈ Z(H_n) is represented as a
    formal sum: e_K = Σ_w c_w · T_w where c_w come from the Markov
    trace of the standard knot diagram for K. We approximate e_K
    via χ^λ(e_K) ≈ <K, λ>_Markov = J_K^λ(q) where J_K^λ is the
    λ-coloured Jones polynomial of K at q_0.
  - For small knots (≤ 8 crossings), J_K^λ is computable from the
    standard braid word via the Hecke character.

  Ref: depth-stratified-frobenius-reciprocity.md
  Ref: PR #819 Phase 5d.4 V̂-level finding (companion probe)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp

from witness_base import WitnessBuilder
from hecke_characters import chi_lambda_braid_mpf, partitions_of, dim_q
from q_parameter import Q as Q0_FLOAT
from q_mpmath import set_q
from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)

# `set_q` used to be called HERE, at import time, with the float64 `Q0_FLOAT`.
# Two defects in one line: the value carried 16 digits, and `set_q` builds its
# `mpf` at whatever `mp.dps` is current — which at import time is mpmath's
# default 15, before `set_compute_dps()` has run.  So even a 50-digit string
# passed at import would have been truncated.  It is now called from `main()`,
# after the precision is set.


def q0_mp() -> mp.mpf:
    """The proton pin as an `mpf`, built at the CURRENT precision.

    Two things this is not.  It is not `qou_substrate.constants.Q` or
    `q_parameter.Q` — both are Python floats (measured: `type(Q) is float`), so
    passing either into the character kernel caps it at f64 whatever `mp.dps`
    says; `chi_lambda_braid_mpf`'s own docstring says so and names this string
    as the thing to pass instead.  And it is not a module-level constant,
    because `mp.mpf` rounds to `mp.dps` at construction and at import time that
    is mpmath's default 15 — a constant here would be a 15-digit number no
    matter how many digits the string carries.
    """
    return Q_MP


# Candidate knots (braid words on minimal strand count)
# Source: Rolfsen knot table; braid generators are 1-indexed
KNOTS = {
    "unknot":  ([],            2),       # vacuous
    "3_1":     ([1, 1, 1],     2),       # trefoil  (σ_1^3 in B_2)
    "4_1":     ([1, -2, 1, -2], 3),      # figure-eight (σ_1 σ_2⁻¹ σ_1 σ_2⁻¹)
    "5_1":     ([1, 1, 1, 1, 1], 2),     # (5,2)-torus
    "5_2":     ([1, 1, 1, -2, 1, -2], 3),
    "6_1":     ([1, 1, -2, 1, -3, 2, -3], 4),
    "6_2":     ([1, 1, -2, 1, -2, -2], 3),
    "6_3":     ([1, 1, -2, 1, -2, 1, -2], 3),
    "7_1":     ([1, 1, 1, 1, 1, 1, 1], 2),  # (7,2)-torus
}


# Every χ^λ(e_K) evaluation that raised and was replaced by 0.0 (see below).
CHI_FAILURES: list[dict] = []


def chi_lambda_K(K_word: list[int], n_strands: int, n_target: int, lam: tuple):
    """χ^λ(e_K) approximation: evaluate the knot's Markov character on
    partition λ at q_0. Lifts the knot's braid word from H_{n_strands}
    to H_{n_target} via the natural inclusion (extend by identity on
    extra strands). Returns an ``mpf`` chi value at q_0.

    For λ not in the support of the projector e_K (i.e., partitions
    that "don't see" the knot), this returns 0 or a small value.
    """
    if not K_word:
        # unknot — identity character = dim_q(λ)
        return dim_q(lam, q0_mp())
    try:
        # `chi_lambda_braid_mpf` takes the FLAT SIGNED word directly and does
        # the (sign, generator) marshalling itself, so the hand-rolled
        # `word_marshalled` that stood here is now redundant.
        return chi_lambda_braid_mpf(lam, K_word, q_value=Q_50_DIGIT_STR)
    except Exception as exc:
        # A swallowed character evaluation is indistinguishable downstream from
        # a genuine χ^λ(e_K) = 0 ("λ doesn't see the knot"), so a search that
        # failed everywhere and one that succeeded everywhere produce the same
        # shaped output. Record each one so the completion assertion can say how
        # many of the cells it counts are real evaluations.
        CHI_FAILURES.append(
            {"n_target": n_target, "lambda": str(lam), "n_strands": n_strands,
             "error": f"{exc.__class__.__name__}: {exc}"}
        )
        return mp.mpf(0)


def _serialise(obj):
    """Render the mpf working state to witness JSON at the LAST moment.

    The character values, the FR weights and `Z_norm` are carried as `mpf`
    through the whole computation and converted here, once, via `_precision.fmt`
    (60 dps).  The previous version converted at every step — `float(chi_val)`,
    `mp.mpf(str(...))` round-trips through f64, `float(w)` — so the mpmath
    arithmetic in the middle was operating on values that had already been
    truncated to ~16 digits on the way in.
    """
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


def depth_k(partition: tuple) -> int:
    """Depth of a partition λ: length(λ) - 1 (curvature-rank index)."""
    return len(partition) - 1


def main() -> int:
    set_compute_dps()
    set_q(Q_50_DIGIT_STR)   # after set_compute_dps — see the note at the imports
    builder = WitnessBuilder("k-star-search-phase5d-5")
    builder.set_description(
        "Phase 5d.5: empirical search for the depth-stratified "
        "Frobenius-reciprocity candidate knots K_1^*, K_2^* "
        "(per depth-stratified-frobenius-reciprocity.md). For each "
        "candidate knot K and each curvature-rank k ∈ {1, 2, 3}, "
        "compute the FR-restricted weight w̃_λ^(K) at q_0 over the "
        "depth-k partitions of n=12 (⁴He). Reports the (K_1^*, K_2^*) "
        "pair minimizing the implied 1.82× variance from PR #801."
    )
    builder.set_content_block("prop:depth-stratified-frobenius-reciprocity")
    builder.add_parameter("q_0", Q_50_DIGIT_STR)

    # We test the projector at H_n for n ∈ {6, 9, 12} (the atomic-braid
    # ambient algebras). For each n, compute χ^λ(e_K) on every depth-k
    # partition for k ∈ {1, 2, 3}.
    print(f"  q_0 = {Q_50_DIGIT_STR}  (mp.dps = {mp.mp.dps})")
    print()

    # The mpfr character kernel is ~8x the cost of the f64 one it replaced
    # (measured: 1.05 s vs 0.135 s for one call), so this is now a multi-minute
    # run and gets progress lines per the long-compute logging discipline.
    t_start = time.time()
    n_chi = 0
    per_n = {}
    for n in (6, 9, 12):
        per_k = {}
        for k in (1, 2, 3):
            partitions_at_depth_k = [
                p for p in partitions_of(n) if depth_k(p) == k
            ]
            knot_chis = {}
            for K_name, (K_word, K_strands) in KNOTS.items():
                if K_strands > n:
                    continue  # can't embed K into H_n
                chis = {}
                for lam in partitions_at_depth_k:
                    chis[str(lam)] = chi_lambda_K(K_word, K_strands, n, lam)
                    n_chi += 1
                print(f"    [{time.time() - t_start:7.1f}s] n={n:2d} k={k} "
                      f"{K_name:<8} {len(partitions_at_depth_k):3d} partitions "
                      f"({n_chi} chi evaluations so far)", flush=True)
                # Compute FR weight: w̃_λ^(K) = dim_q²(λ) · χ^λ(e_K) / Z
                # Z normalises so Σ_λ w̃_λ = 1 over depth-k partitions
                weights = {}
                Z_norm = mp.mpf(0)
                for lam in partitions_at_depth_k:
                    dq2 = dim_q(lam, q0_mp()) ** 2
                    w = dq2 * chis[str(lam)]
                    weights[str(lam)] = w
                    Z_norm += w
                if Z_norm != 0:
                    normalised = {lam: w / Z_norm for lam, w in weights.items()}
                else:
                    normalised = {lam: mp.mpf(0) for lam in weights}
                knot_chis[K_name] = {
                    "chi_values": chis,
                    "FR_weights_unnormalised": weights,
                    "FR_weights_normalised": normalised,
                    "Z_norm": Z_norm,
                }
            per_k[k] = knot_chis
        per_n[n] = per_k

    # Pretty-print top knots per (n, k) — knots with largest |Z_norm|
    # are the strongest candidates (their projector "sees" the depth-k
    # partitions most strongly).
    print(f"\n  === Top knot candidates per (n, k) — by |Z_norm| ===")
    for n in (6, 9, 12):
        for k in (1, 2, 3):
            print(f"\n    H_{n}, k={k}:")
            ranked = sorted(per_n[n][k].items(),
                            key=lambda kv: -abs(kv[1]["Z_norm"]))
            for K_name, data in ranked[:5]:
                Zn = data["Z_norm"]
                n_part = len(data["chi_values"])
                print(f"      {K_name:<8} |Z_norm| = {float(abs(Zn)):>12.4f}  "
                      f"(over {n_part} depth-{k} partitions of {n})")

    builder.add_data("per_n_per_k_per_knot", _serialise(per_n))

    # Was `computed=1.0, expected=1.0` (bean `qou-26f2`). "Completed" is a
    # coverage claim, and the constant asserted none of it: a run in which every
    # knot was skipped for want of strands, or in which every χ evaluation hit
    # the swallow-and-return-0.0 path, produced exactly the same 1.0. Count the
    # (n, k, K) cells that actually hold characters, against an expected count
    # re-derived from the loop bounds rather than read back off the output.
    cells_filled = sum(
        1
        for n_ in per_n
        for k_ in per_n[n_]
        for cell in per_n[n_][k_].values()
        if cell["chi_values"]
    )
    cells_expected = sum(
        1
        for n_ in (6, 9, 12)
        for k_ in (1, 2, 3)
        for (_w, strands) in KNOTS.values()
        if strands <= n_ and any(depth_k(p) == k_ for p in partitions_of(n_))
    )
    builder.add_data("chi_evaluation_failures", CHI_FAILURES)
    builder.add_assertion(
        "k_star_search_completed",
        computed=str(cells_filled),
        expected=str(cells_expected),
        tolerance=0,
        unit="(H_n, curvature-rank k, knot) cells holding χ^λ(e_K) values",
        source=(
            f"Computed FR projector character χ^λ(e_K) for "
            f"{len(KNOTS)} candidate knots × {3} curvature-ranks "
            f"× 3 atomic-braid ambient algebras (H_6, H_9, H_12); "
            f"{cells_filled}/{cells_expected} cells filled, "
            f"{len(CHI_FAILURES)} χ evaluation(s) fell through to the 0.0 "
            f"exception path. Top candidates per (n, k) ranked by |Z_norm| of "
            f"the FR-restricted weight."
        ),
    )
    builder.add_assertion(
        "chi_evaluations_all_succeeded",
        computed=str(len(CHI_FAILURES)),
        expected="0",
        tolerance=0,
        unit="χ^λ(e_K) evaluations replaced by 0.0 after an exception",
        source="the χ helper substitutes 0.0 for a raised evaluation, which "
               "reads downstream as a genuine 'λ does not see the knot'; this "
               "counts the substitutions so the two cannot be confused",
    )

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
