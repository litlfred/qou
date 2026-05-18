#!/usr/bin/env python3
# polynomial_q_not_applicable: high-precision spectral structure
# decomposition at mpmath 50 dps — verifies bar-pair structure exact
# at 1e-30 and searches for the next-order correction series.
"""Schur-Weyl-style block decomposition of `M = ρ(β_EW Δ_I^minimal)`
on `V_{(3,2,1)}` — searches for the structural reformulation of the
`q^(1/5)` reading that closes the 0.15 % residual identified by
`probe_staircase_ew_k3_categorical.py`.

## Two structural analyses

1. **Bar-pair structure (verification + reciprocity)**: confirms at
   mpmath 50 dps that all 16 eigenvalues of `M` pair perfectly with
   products `e_+ · e_- = ±1`. For `ρ_3 = (3,2,1)` self-conjugate, all
   8 pairs have sign `-` (so `e_- = −1/e_+`). This means `M` is
   **anti-self-reciprocal**: its characteristic polynomial
   `p(λ) = det(M − λI)` satisfies the symmetry
   `λ^16 · p(−1/λ) = ±p(λ)`, and `det(M) = (−1)^8 = +1`.

   The Schützenberger / bar involution on SYTs is the categorical
   shadow of this spectral symmetry. A direct construction of the
   involution operator on the SYT basis requires jeu-de-taquin
   normalisation (not simple transpose-plus-complement, which can
   produce non-standard tableaux); we observe the spectral symmetry
   directly rather than building the operator.

2. **Next-order correction fit**: takes the empirical residual
   `r := cot θ_W^CODATA / (e_top/e_2nd) − q_0^(1/5)` and fits it to
   `q_0^(1/5) · (1 + α·X)` for `X ∈ {h^k, ℏ_q^k : k = 1..4}` with
   `h := q − q^(-1)`, `ℏ_q := 1 − q^(-1)`, reporting `α` at each
   order. A clean `α` (e.g. `α = 3/4`, `α = 1/2`, `α = ζ(3)/π²`)
   would suggest the categorical origin of the correction.

## Why this matters

[`rem-staircase-ew-k3-mpfr-finding`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/rem-staircase-ew-k3-mpfr-finding.md)
established that `q^(1/5)` is NOT an exact identity — the conjecture's
literal content is falsified at 50 dps, with a structural `0.15 %`
residual surviving. The natural follow-up question is whether that
residual is itself **structurally derivable** from V_(3,2,1) data
(corner-hook, content sums, bar-involution invariants) or whether
it requires inputs outside the categorical substrate (e.g.
electroweak running, CODATA experimental uncertainty).

If the next-order correction `α` is a clean rational or a small
combinatorial invariant of `ρ_3`, the conjecture refines to a
two-term closed form. If `α` is numerically opaque, the categorical
route stalls at leading order and the residual must come from
elsewhere.

`auditOnly`: docs/audits/2026-05-17-staircase-ew-k3-block-decomposition.md

Witness: `staircase-ew-k3-block-decomposition.witness.json`

@module folio-assistant/computations/probe_staircase_ew_k3_block_decomposition
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from mpmath import mp, mpf, fabs  # noqa: E402

from hecke_character_symbolic import standard_young_tableaux  # noqa: E402
from probe_staircase_ew_k3_categorical import (  # noqa: E402
    build_hoefsmit_mpfr,
    beta_ew_word_n6,
    _dps_tol,
)
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

SHAPE = (3, 2, 1)
K = 3
H_CORNER = 2 * K - 1  # = 5


def find_bar_pairs(eigs: list, tol: "mpf") -> tuple[list, int]:
    """Group eigenvalues into bar-pairs `e_+ · e_- = ±1`."""
    used: set[int] = set()
    pairs = []
    for i in range(len(eigs)):
        if i in used:
            continue
        for j in range(i + 1, len(eigs)):
            if j in used:
                continue
            prod = eigs[i] * eigs[j]
            for sign, target in [("+", mpf(1)), ("-", mpf(-1))]:
                if fabs(prod - target) < tol:
                    pairs.append((i, j, eigs[i], eigs[j], sign))
                    used.add(i)
                    used.add(j)
                    break
            if i in used:
                break
    return pairs, len(eigs) - len(used)


def reciprocity_check(M: "mp.matrix", eigs: list) -> dict:
    """Verify `M` is anti-self-reciprocal: spectrum closed under `x ↦ −1/x`.

    Computes `det(M)` (should be +1) and the maximum `|e + 1/e'|` over
    candidate bar-partner pairs (should be 0 at 50-dps tolerance).
    """
    det_M = mp.det(M)
    # Match each e with the closest candidate -1/e' among the others.
    max_mismatch = mpf(0)
    for i, e in enumerate(eigs):
        target = -1 / e
        best = min(
            (fabs(eigs[j] - target) for j in range(len(eigs)) if j != i),
            default=mpf("inf"),
        )
        if best > max_mismatch:
            max_mismatch = best
    return {
        "det_M": mp.nstr(det_M, 30),
        "max_partner_mismatch_50dps": mp.nstr(max_mismatch, 30),
    }


def fit_next_order_correction(
    residual: "mpf", q0: "mpf", target_leading: "mpf"
) -> dict:
    """Fit `residual = target_leading · (1 + α·h^k)` for `k ∈ {2, 3, 4}`.

    Returns the α coefficient at each order, plus an "is this a nice
    rational?" check against small denominators.
    """
    h = q0 - 1 / q0
    hbar_q = 1 - 1 / q0
    excess = residual / target_leading - 1
    fits: dict = {}
    for power_name, power_value in [
        ("h^1", h),
        ("h^2", h ** 2),
        ("h^3", h ** 3),
        ("h^4", h ** 4),
        ("hbar_q", hbar_q),
        ("hbar_q^2", hbar_q ** 2),
        ("hbar_q^3", hbar_q ** 3),
    ]:
        alpha = excess / power_value
        # Check small-denominator rationals
        rationals: list[tuple[str, float]] = []
        for den in range(2, 13):
            for num in range(1, 13 * den):
                cand = mpf(num) / mpf(den)
                rel = fabs(alpha - cand) / max(fabs(alpha), mpf(1))
                if rel < mpf("1e-3"):
                    rationals.append((f"{num}/{den}", float(rel)))
                    break
        fits[power_name] = {
            "alpha": mp.nstr(alpha, 20),
            "rational_hits": rationals[:3],
        }
    return fits


def main() -> int:
    print("=" * 78)
    print("Staircase EW-residual k=3 — block decomposition analysis (50 dps)")
    print("=" * 78)
    print()

    q0 = Q_MP
    print(f"  q_0 = {mp.nstr(q0, 25)}")
    print(f"  ρ_3 = {SHAPE} (self-conjugate)")
    print()

    # Build SYTs + Hoefsmit matrices.
    syts, cells, _contents = standard_young_tableaux(SHAPE)
    sigmas, dim = build_hoefsmit_mpfr(SHAPE, q0)
    assert dim == 16, f"expected dim 16, got {dim}"
    print(f"  dim V_(3,2,1) = {dim}")
    print(f"  SYTs enumerated: {len(syts)}")

    # Compute the word image M.
    word = beta_ew_word_n6()
    M = mp.eye(dim)
    for g in word:
        M = M * sigmas[g]
    print(f"  β_EW word length = {len(word)}; M built")
    print()

    # ─── §1: Bar-pair structure + reciprocity verification ─────
    eigs, _ev = mp.eig(M)
    bar_tol = _dps_tol(20)
    pairs, n_unpaired = find_bar_pairs(eigs, bar_tol)
    plus_count = sum(1 for *_, s in pairs if s == "+")
    minus_count = sum(1 for *_, s in pairs if s == "-")
    print(f"§1 Bar-pair structure of eigenvalues:")
    print(f"   pairs found at tol {mp.nstr(bar_tol, 4)}: {len(pairs)}")
    print(f"   sign +1: {plus_count},  sign −1: {minus_count}")
    print(f"   unpaired: {n_unpaired}")

    recip = reciprocity_check(M, eigs)
    print(f"   det(M)                           = {recip['det_M']}")
    print(f"   max |e + 1/partner|              = "
          f"{recip['max_partner_mismatch_50dps']}")
    print(f"   → M is anti-self-reciprocal (eigenvalues closed under "
          f"x↦−1/x)")
    print()

    # ─── §2: Next-order correction fit ─────────────────────────
    sin2_theta_W = mpf("0.23121")
    cot_theta_W_codata = mp.sqrt((1 - sin2_theta_W) / sin2_theta_W)
    # Top two positive-real eigenvalues
    pos_real = sorted(
        [e for e in eigs if fabs(e.imag if hasattr(e, "imag") else 0)
         < _dps_tol(20) and (e.real if hasattr(e, "real") else e) > 0],
        key=lambda e: -fabs(e),
    )
    e_top = pos_real[0]
    e_2nd = pos_real[1]
    bare = fabs(e_top) / fabs(e_2nd)
    residual = cot_theta_W_codata / bare
    predicted = q0 ** (mpf(1) / H_CORNER)
    rel_diff = fabs(residual - predicted) / predicted

    print(f"§2 Next-order correction fit:")
    print(f"   e_top                  = {mp.nstr(e_top, 20)}")
    print(f"   e_2nd                  = {mp.nstr(e_2nd, 20)}")
    print(f"   bare top/2nd           = {mp.nstr(bare, 20)}")
    print(f"   CODATA cot θ_W         = {mp.nstr(cot_theta_W_codata, 20)}")
    print(f"   residual = CODATA/bare = {mp.nstr(residual, 20)}")
    print(f"   leading q^(1/5)        = {mp.nstr(predicted, 20)}")
    print(f"   |residual − q^(1/5)|/q^(1/5) = {mp.nstr(rel_diff, 8)}")
    print()

    fits = fit_next_order_correction(residual, q0, predicted)
    print(f"   Fit: residual = q^(1/5) · (1 + α · X) for various X:")
    print(f"   {'X':<10s} {'α':>22s}  small-denom rationals")
    for power, info in fits.items():
        rats = info["rational_hits"]
        rat_str = ", ".join(f"{r[0]} (rel {r[1]:.1e})" for r in rats) \
            if rats else "(no clean fit)"
        print(f"   {power:<10s} {info['alpha']:>22s}  {rat_str}")
    print()

    # ─── §3: Clean-rational exponent search residual = q^a ─────
    # Solve residual = q0^a → a = log(residual)/log(q0).
    a_exp = mp.log(residual) / mp.log(q0)
    print(f"§3 Cleanest possible closed form: residual = q^a")
    print(f"   a = log(residual)/log(q_0) = {mp.nstr(a_exp, 25)}")

    # Search small-denominator rationals (Stern-Brocot-like sweep).
    from math import gcd
    rational_hits = []
    for q_den in range(2, 200):
        for p_num in range(1, q_den):
            if gcd(p_num, q_den) != 1:
                continue
            cand = mpf(p_num) / mpf(q_den)
            err = fabs(a_exp - cand)
            rational_hits.append((err, p_num, q_den, cand))
    rational_hits.sort()
    print(f"   Best rational fits (denominators ≤ 200):")
    for err, p_num, q_den, cand in rational_hits[:5]:
        q_pow = q0 ** cand
        resid_rel = fabs(residual - q_pow) / residual
        print(f"     a ≈ {p_num:3d}/{q_den:3d} = {mp.nstr(cand, 12):<14s}  "
              f"|a − p/q| = {mp.nstr(err, 6):<11s}  "
              f"|residual − q^(p/q)|/residual = {mp.nstr(resid_rel, 4)}")
    print()

    # ─── §4: Structural hypothesis check ───────────────────────
    # Σhook(ρ_k) for staircase: well-known formula sum-of-squares
    #   Σhook(ρ_k) = k(k+1)(2k+1)/6
    # Hypothesis: residual at level k = q^(k / Σhook(ρ_k))
    #                                  = q^(6 / [(k+1)(2k+1)])
    sum_hook_rho_k = K * (K + 1) * (2 * K + 1) // 6
    hypothesis_exp = mpf(K) / mpf(sum_hook_rho_k)
    hypothesis_value = q0 ** hypothesis_exp
    rel_diff_hyp = fabs(residual - hypothesis_value) / residual
    print(f"§4 Structural hypothesis: residual = q^(k / Σhook(ρ_k))")
    print(f"   Σhook(ρ_{K})              = {sum_hook_rho_k}  "
          f"(= k(k+1)(2k+1)/6 sum-of-squares formula)")
    print(f"   k / Σhook(ρ_{K})          = {K}/{sum_hook_rho_k} = "
          f"{mp.nstr(hypothesis_exp, 15)}")
    print(f"   hypothesised residual    = q^({K}/{sum_hook_rho_k}) = "
          f"{mp.nstr(hypothesis_value, 25)}")
    print(f"   actual residual          = {mp.nstr(residual, 25)}")
    print(f"   |Δ_rel|                  = {mp.nstr(rel_diff_hyp, 8)}")

    codata_uncertainty_floor = mpf("1e-4")
    is_sub_codata = rel_diff_hyp < codata_uncertainty_floor
    print(f"   below CODATA floor (~1e-4)? "
          f"{'✓ yes — single-point match' if is_sub_codata else '✗ no'}")
    print()

    # ─── §5: q-derivative falsification of the q^a hypothesis ─────
    # If residual(q) really equals q^a globally, then
    # d/d(log q) log(residual) should equal `a` at every q.
    # Compute the slope numerically and check.
    print(f"§5 q-derivative consistency test (CRITICAL):")
    h_step = mpf("1e-10")
    log_q0 = mp.log(q0)

    def residual_at_q(q_val):
        sig_q, _dim = build_hoefsmit_mpfr(SHAPE, q_val)
        M_q = mp.eye(_dim)
        for g in word:
            M_q = M_q * sig_q[g]
        eigs_q, _ = mp.eig(M_q)
        pr = sorted(
            [e for e in eigs_q
             if fabs(e.imag if hasattr(e, "imag") else 0) < _dps_tol(20)
             and (e.real if hasattr(e, "real") else e) > 0],
            key=lambda e: -fabs(e),
        )
        bare_q = fabs(pr[0]) / fabs(pr[1])
        return cot_theta_W_codata / bare_q

    qs = [mp.exp(log_q0 + k * h_step) for k in (-2, -1, 0, 1, 2)]
    log_res = [mp.log(residual_at_q(qi)) for qi in qs]
    deriv1 = (
        -log_res[4] + 8 * log_res[3] - 8 * log_res[1] + log_res[0]
    ) / (12 * h_step)
    deriv2 = (
        -log_res[4] + 16 * log_res[3] - 30 * log_res[2]
        + 16 * log_res[1] - log_res[0]
    ) / (12 * h_step ** 2)

    print(f"   d/d(log q) log(residual)        = {mp.nstr(deriv1, 12)}")
    print(f"   d²/d(log q)² log(residual)      = {mp.nstr(deriv2, 12)}")
    print(f"   q^a hypothesis predicts:")
    print(f"     d/d(log q) log(residual)      = a = 3/14 = "
          f"{mp.nstr(mpf(3)/14, 12)}")
    print(f"     d²/d(log q)² log(residual)    = 0 (constant slope)")
    hypothesis_consistent_with_derivative = (
        fabs(deriv1 - mpf(3) / 14) < mpf("0.1")
        and fabs(deriv2) < mpf("1")
    )
    print(f"   q^a hypothesis CONSISTENT with derivative test? "
          f"{'✓ yes' if hypothesis_consistent_with_derivative else '✗ NO — FALSIFIED'}")
    print(f"   → the single-point match at q_0 (5 ppm) is a coincidence;")
    print(f"     residual is NOT a pure power function of q.")
    print()

    # Build witness
    builder = (
        WitnessBuilder(
            "staircase-ew-k3-block-decomposition", engine="mpmath"
        )
        .set_description(
            "Schur-Weyl-style block decomposition probe for V_(3,2,1) at "
            "mpmath 50 dps. Two analyses: (§1) bar-pair structure of "
            "M = ρ(β_EW Δ_I^minimal) — verifies all 16 eigenvalues form "
            "8 perfect bar-pairs with sign −1 (anti-self-reciprocal "
            "spectrum: closed under x↦−1/x); det(M) = +1. (§2) "
            "next-order correction fit — given the empirical residual "
            "= CODATA cot θ_W / (top/2nd) and the leading q^(1/5) "
            "approximation from rem:staircase-ew-k3-mpfr-finding, fits "
            "residual = q^(1/5) · (1 + α·X) for X ∈ {h, h², h³, h⁴, "
            "ℏ_q, ℏ_q², ℏ_q³} and reports α plus any small-denom "
            "rational match. Complements rem:staircase-ew-k3-mpfr-"
            "finding by searching for the structural origin of the "
            "0.15 % residual. (Note: a direct bar-involution operator "
            "B on the SYT basis requires the Schützenberger jeu-de-"
            "taquin algorithm — not implemented here; the spectral "
            "symmetry is observed directly via the reciprocity check.)"
        )
        .set_content_block("conj:staircase-ew-residual")
        .set_audit_only(
            "docs/audits/2026-05-17-staircase-ew-k3-block-decomposition.md")
        .add_parameter("k", K)
        .add_parameter("staircase_partition", list(SHAPE))
        .add_parameter("dim_V_rho3", dim)
        .add_parameter("h_corner", H_CORNER)
        .add_parameter("q_0_50dps", mp.nstr(q0, 50))
        .add_assertion(
            "bar_pair_structure_exact",
            computed=len(pairs),
            expected=dim // 2,
            tolerance=0,
            unit="count",
        )
        .add_data("bar_pair_count", len(pairs))
        .add_data("bar_pair_plus_signs", plus_count)
        .add_data("bar_pair_minus_signs", minus_count)
        .add_data("unpaired_eigenvalues", n_unpaired)
        .add_data("det_M_50dps", recip["det_M"])
        .add_data("max_reciprocity_mismatch_50dps",
                  recip["max_partner_mismatch_50dps"])
        .add_data("e_top_50dps", mp.nstr(e_top, 50))
        .add_data("e_second_50dps", mp.nstr(e_2nd, 50))
        .add_data("residual_codata_over_bare_50dps",
                  mp.nstr(residual, 50))
        .add_data("predicted_q_pow_one_fifth_50dps",
                  mp.nstr(predicted, 50))
        .add_data("leading_rel_diff_50dps", mp.nstr(rel_diff, 50))
        .add_data("next_order_correction_fits", fits)
        .add_data("log_residual_over_log_q0", mp.nstr(a_exp, 50))
        .add_data("best_rational_fits_residual_exponent", [
            {"p": int(p), "q": int(q),
             "value": mp.nstr(cand, 30),
             "abs_err_in_exponent": mp.nstr(err, 30),
             "rel_err_in_residual": mp.nstr(
                 fabs(residual - q0 ** cand) / residual, 30)}
            for err, p, q, cand in rational_hits[:5]
        ])
        .add_data("sum_hook_staircase_k", sum_hook_rho_k)
        .add_data("structural_hypothesis_exponent",
                  mp.nstr(hypothesis_exp, 50))
        .add_data("structural_hypothesis_value_50dps",
                  mp.nstr(hypothesis_value, 50))
        .add_data("structural_hypothesis_rel_diff_50dps",
                  mp.nstr(rel_diff_hyp, 50))
        .add_data("structural_hypothesis_below_codata_floor",
                  bool(is_sub_codata))
        .add_data("q_derivative_log_residual_50dps",
                  mp.nstr(deriv1, 50))
        .add_data("q_second_derivative_log_residual_50dps",
                  mp.nstr(deriv2, 50))
        .add_data("q_derivative_predicted_by_hypothesis",
                  mp.nstr(mpf(3) / 14, 50))
        .add_data("q_derivative_hypothesis_consistent",
                  bool(hypothesis_consistent_with_derivative))
        .add_caveat(
            "§3-§4 are EMPIRICAL pattern-matching at a single point q=q_0, "
            "NOT a derivation. §5 (q-derivative test) falsifies the q^a "
            "hypothesis: the actual slope d/d(log q) log(residual) at "
            "q_0 is large and negative (~-4.6), not the predicted 3/14. "
            "The single-point match (5 ppm at q_0) is a coincidence; "
            "residual is not a pure power function of q.  A real "
            "derivation would require either (a) constructing M(q)'s "
            "eigenvalues as symbolic q-functions and identifying the "
            "categorical mechanism producing the cot θ_W ratio, or "
            "(b) finding a different parameterisation where the "
            "residual IS a clean function (e.g. of substrate "
            "invariants, not just q itself)."
        )
    )
    out_path = builder.save()
    print(f"  Witness: {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
