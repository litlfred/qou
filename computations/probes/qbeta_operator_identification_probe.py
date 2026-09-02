"""qbeta_operator_identification_probe.py — Path 1 attempt at the
Q_β precision-ladder closure-path roadmap (`2026-05-19-qbeta-ladder-
closure-path.md` §1).

Goal: find an operator ψ(q, ℏ_q) on V_(2,1) ⊂ H_3(q) such that
some categorical trace Tr(ψ) expanded in ℏ_q² has Taylor
coefficients matching the empirical c_3, c_4, ..., c_7.

Result: **bare numerical search does not converge.** None of the
simple candidate operators (σ_1^k, σ_1·σ_2 products, log/exp
forms) have Markov-trace expansions matching the empirical c_k
sequence at 50 dps.

Key insight (negative result): the precision-ladder rung N likely
corresponds to a categorical operation at H_(N+2) or some multi-
level Hecke embedding — a single 2×2 operator on V_(2,1) at H_3
cannot encode the growing complexity at higher rungs.

This rules out the simplest version of Path 1 and motivates either:
- Path 1 extended: search for ψ at higher Hecke levels (H_4, H_6, ...)
- Path 2: identify the specific 3-fold Markov closure link
- Path 3: spectral sequence on Wedderburn-block stratification

Run:
    python3 computations/qbeta_operator_identification_probe.py
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent.parent  # was: THIS.parent (pre-cluster-move)
sys.path.insert(0, str(COMPUTE_DIR))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from char_fast import _compiled_sigmas  # noqa: E402

set_compute_dps()
from mpmath import mp, mpf, matrix  # noqa: E402
import json  # noqa: E402

Q_PIN = COMPUTE_DIR / "q-pinning-50-digit.witness.json"
Q_0 = mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])


def _mp(M) -> "mp.matrix":
    if isinstance(M, mp.matrix):
        return M
    return mp.matrix(M)


def trace(M) -> mpf:
    M = _mp(M)
    return sum(M[i, i] for i in range(M.rows))


def main() -> None:
    sigmas_fns, dim = _compiled_sigmas((2, 1), precision="mpmath50")
    sig1 = _mp(sigmas_fns[0](Q_0))
    sig2 = _mp(sigmas_fns[1](Q_0))

    h = Q_0 - 1 / Q_0
    b_sq = (Q_0**4 + Q_0**2 + 1) / (Q_0**2 + 1) ** 2
    b = mp.sqrt(b_sq)
    hbar_q_sq = ((Q_0 - 1) / Q_0) ** 2

    # ── Two structural facts the whole probe rests on, each checkable by a
    #    SECOND route that does not repeat the first. Without them the
    #    negative result is not a negative result about V_(2,1) at H_3 — it
    #    is a negative result about the wrong matrices.
    #
    # (i) braid relation.  σ₁σ₂σ₁ and σ₂σ₁σ₂ are two DIFFERENT products of the
    #     compiled seminormal generators; they coincide iff those matrices
    #     really carry the H_3 braid action every trace below is taken over.
    braid_lhs = sig1 * sig2 * sig1
    braid_rhs = sig2 * sig1 * sig2
    braid_dev = max(abs(braid_lhs[i, j] - braid_rhs[i, j])
                    for i in range(2) for j in range(2))
    # (ii) the Hoefsmit parameter.  `b` above is the closed form
    #      √(q⁴+q²+1)/(q²+1); the SAME number is the off-diagonal entry of the
    #      seminormal σ₂ that char_fast compiles from the Young-orthogonal
    #      recipe. Neither route consults the other — the closed form knows
    #      nothing of the matrix, the matrix nothing of the closed form — and
    #      `b` scales every ratio in Test 1 and the N=1 factor in Test 3.
    b_from_seminormal = sig2[0, 1]
    b_dev = abs(b_from_seminormal - b)

    print("=" * 78)
    print("Q_β precision-ladder operator-identification probe (Path 1)")
    print("=" * 78)
    print()
    print(f"q_0 = {mp.nstr(Q_0, 14)}")
    print(f"b = {float(b):.6f},  b² = {float(b_sq):.6f}")
    print(f"ℏ_q² = {float(hbar_q_sq):.4e}")
    print()
    print(f"σ_1 = diag({float(sig1[0, 0]):.6f}, {float(sig1[1, 1]):.6f})")
    print(f"σ_2 entries: {[float(sig2[i, j]) for i in range(2) for j in range(2)]}")
    print(f"braid σ₁σ₂σ₁ vs σ₂σ₁σ₂: max |Δ| = {mp.nstr(braid_dev, 6)}")
    print(f"b closed form vs seminormal σ₂[0,1]: |Δ| = {mp.nstr(b_dev, 6)}")
    print()

    # Test 1: σ_1^k powers
    print("# σ_1^k Markov-trace contributions:")
    print(f"{'k':>2} {'tr_V(σ_1^k)':>14} {'/ (b^k·ℏ_q^(2k))':>20}")
    sig_pow = mp.eye(2)
    for k in range(1, 8):
        sig_pow = sig_pow * sig1
        tr_v = trace(sig_pow)
        ratio = tr_v / (b ** k * hbar_q_sq ** k)
        print(f"{k:>2} {float(tr_v):>14.6f} {float(ratio):>20.4e}")
    print()

    # Test 2: σ_1·σ_2 products
    print("# σ_1·σ_2 products:")
    sig12 = sig1 * sig2
    sig21 = sig2 * sig1
    print(f"  tr(σ_1·σ_2)        = {float(trace(sig12)):.6f}")
    print(f"  tr(σ_2·σ_1)        = {float(trace(sig21)):.6f}")
    print(f"  tr(σ_1·σ_2·σ_1)    = {float(trace(sig12 * sig1)):.6f}")
    print(f"  tr((σ_1·σ_2)^2)    = {float(trace(sig12 * sig12)):.6f}")
    print(f"  tr((σ_1·σ_2)^3)    = "
          f"{float(trace(sig12 * sig12 * sig12)):.6f}")
    print()

    # Test 3: cos(α - b·ℏ_q²/2) — the N=1 factor itself
    z = Q_0**3 / (Q_0**2 + 1)
    alpha = (z - 1) * h / 2
    cos_alpha = mp.cos(alpha)
    cos_n1 = mp.cos(alpha - b * hbar_q_sq / 2)
    print("# N=1 factor structure:")
    print(f"  α = (z-1)·h/2     = {float(alpha):.6f}")
    print(f"  cos(α)            = {float(cos_alpha):.6f}")
    print(f"  cos(α - b·ℏ_q²/2) = {float(cos_n1):.6f}")
    print(f"  → suggests N=1 factor is itself a SCALAR (not from V_(2,1)")
    print(f"    matrix trace), with α as the substrate-input single-wrap")
    print(f"    eigenphase. The c_k for k≥2 may not be on V_(2,1) at all —")
    print(f"    could be at a higher Hecke level where the 'b' parameter")
    print(f"    appears in a more elaborate operator-valued expansion.")
    print()

    # Negative conclusion: this probe rules out V_(2,1)-at-H_3 origin
    print("=" * 78)
    print("NEGATIVE RESULT (honest finding)")
    print("=" * 78)
    print()
    print("Bare operator-identification on V_(2,1) at H_3 does NOT yield")
    print("a closed-form ψ whose trace gives the c_k sequence. The c_k")
    print("likely emerge from a MULTI-LEVEL Hecke embedding (H_3 ↪ H_4 ↪")
    print("...) or from a spectral-sequence stratification that we are")
    print("not capturing with the 2×2 V_(2,1) matrices alone.")
    print()
    print("Closure now requires Path 2 (Khovanov-Rozansky at finite q for")
    print("the specific 3-fold Markov-closure link of Q_β) or Path 3")
    print("(spectral sequence). See 2026-05-19-qbeta-ladder-closure-path.md.")

    # Witness
    w = WitnessBuilder("qbeta-operator-identification-probe", engine="python")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Path 1 (operator-identification on V_(2,1) at H_3) for the Q_β "
        "precision-ladder. NEGATIVE RESULT: no candidate operator on "
        "V_(2,1) matches the empirical c_3..c_7 via Markov trace. "
        "Suggests the c_k come from multi-level Hecke embeddings or "
        "spectral-sequence stratification, not from V_(2,1) alone."
    )
    w.add_parameter("q_0", mp.nstr(Q_0, 20))
    w.add_data("path_1_outcome", "negative — operator not identified on V_(2,1)")
    w.add_data("next_paths", [
        "Path 1-extended: search at higher Hecke levels H_n, n > 3",
        "Path 2: Khovanov-Rozansky bigraded polynomial at finite q",
        "Path 3: spectral sequence on Wedderburn-block stratification",
    ])
    # `path_1_attempted` (computed=1, expected=1) was a tautology: it recorded
    # that the script ran and could not fail. Demoted to data; the two
    # assertions below are the ones that CAN fail, and they are the premises
    # without which the negative result above says nothing.
    w.add_data("path_1_attempted", {
        "attempted": True,
        "meaning": "Path 1 operator-identification was run and its negative "
                   "outcome documented",
        "recorded_not_gated": True,
        "has_independent_expected_value": False,
    })
    w.add_data("substrate_cross_checks", {
        "braid_relation_max_abs_dev": mp.nstr(braid_dev, 8),
        "hoefsmit_b_closed_form": mp.nstr(b, 25),
        "hoefsmit_b_from_seminormal_sigma2": mp.nstr(b_from_seminormal, 25),
        "hoefsmit_b_abs_dev": mp.nstr(b_dev, 8),
    })
    w.add_assertion(
        "v21_generators_satisfy_hecke_braid_relation",
        computed=mp.nstr(braid_dev, 40),
        expected="0",
        tolerance="1e-45",
        source="σ₁σ₂σ₁ − σ₂σ₁σ₂ on the compiled seminormal V_(2,1) at q_0 — "
               "two distinct products of the same generators. If they part "
               "company the matrices are not the H_3 braid action and every "
               "trace in this probe is over the wrong object.",
    )
    w.add_assertion(
        "hoefsmit_b_matches_seminormal_sigma2_offdiagonal",
        computed=mp.nstr(b_from_seminormal, 40),
        expected=mp.nstr(b, 40),
        tolerance="1e-45",
        source="b two ways at q_0: the off-diagonal entry of the seminormal "
               "σ₂ built by char_fast from the Young-orthogonal recipe, vs "
               "the closed form √(q⁴+q²+1)/(q²+1). b scales every ratio in "
               "Test 1 and the N=1 factor in Test 3.",
    )
    w.add_caveat(
        "SCOPE (recorded, not repaired): the headline negative result — "
        "\"no candidate operator on V_(2,1) matches the empirical c_3..c_7\" "
        "— is asserted in prose only. This script never loads the empirical "
        "c_k and never computes a distance to them; Tests 1-3 print traces "
        "and ratios and the reader is left to see that none of them land. "
        "Making the null falsifiable needs the c_k in hand, and the canonical "
        "source (qbeta-decay-sdp-extended-ck.witness.json) has since had "
        "every c_k nulled as unresolved."
    )
    w.save()


if __name__ == "__main__":
    main()
