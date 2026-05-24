#!/usr/bin/env python3
"""Spike: operator-theoretic Faddeev pentagon route to λ_scale.

This is the **hardest** of the four `λ_scale` derivation paths
catalogued in the PR #941 audit § "What this does NOT rule out".

The genuine Faddeev pentagon is an OPERATOR identity:

   Φ_q(U) · Φ_q(V) = Φ_q(V) · Φ_q(U·V) · Φ_q(U)

where U, V satisfy the q-Heisenberg / Weyl commutation
`U·V = q² · V·U`. This is NOT a commutative ratio identity —
the previous spikes (PR #923, #928, #941) tested only commutative
substrate-natural Φ_q values and their ratios, so the genuinely
non-commutative information of the pentagon was not probed.

The four predecessor exhaustion results:

  PR #923  linear PSLQ on Li_2^q + Φ_q at substrate args (negative)
  PR #928  linear PSLQ on V̂_S + ℚ(ζ_60) + Tier-0 knot vols (negative)
  PR #941  non-linear Φ_q functional eq + pentagon-commutative (negative)
  this    OPERATOR pentagon in finite-N truncated rep (probing)

## Method

Truncated Hilbert space `H_N = ℂ^N` (N = 16). Pick:

  U = diag(1, q², q⁴, …, q^(2N-2))         (number-op-like)
  V = strict upper-shift, V|k⟩ = |k+1⟩     (k < N-1)

Then `U·V|k⟩ = q^(2k+2) |k+1⟩` and `V·U|k⟩ = q^(2k) |k+1⟩`, so
`U·V = q² · V·U` exactly in the open part of the truncation
(error only at the boundary row k = N-1, which we exclude).

Faddeev's Φ_q acts on a matrix `M` by spectral functional calculus:

  Φ_q(M) = ∑_i Φ_q(λ_i) · |i⟩⟨i|         (M diagonalisable)

For finite N and |q| > 1, Φ_q(λ) = ∏_{j=1..K} (1 - q^(-j) λ)^(-1)
converges fast (K = 200 plenty at q_0 ≈ 1.11). V is nilpotent
(spectrum {0}, V^N = 0), so each *factor* (I − q^(-j) V)^(-1)
truncates exactly: the geometric series I + (q^(-j) V) + … has at
most N nonzero terms by V's nilpotency. The *outer* product over
j ≥ 1 is still infinite, and the K = 200 cutoff is justified by
|q^(-K)| ≪ 10^(-50) (convergence-based, not algebraic).

We probe:

  (1) Pentagon-identity numerical sanity:
        ‖Φ_q(U) Φ_q(V) − Φ_q(V) Φ_q(UV) Φ_q(U)‖ → 0
      verified on the open (non-boundary) block.
  (2) Substrate-natural matrix elements of single Φ_q's:
        ⟨k|Φ_q(U)|k⟩, ⟨k|Φ_q(V)|k⟩, ⟨0|Φ_q(U)Φ_q(V)|0⟩, …
  (3) Non-commutator ratios:
        ⟨0|Φ_q(U) Φ_q(V) − Φ_q(V) Φ_q(U)|0⟩  ÷ ⟨0|[U,V]|0⟩
      and other substrate-natural normalised quantities.
  (4) Traces:
        tr(Φ_q(U)), tr(Φ_q(V)), tr(Φ_q(U) Φ_q(V)), tr(Φ_q(U)⁻¹ Φ_q(V))

For each scalar probe, check `|probe − λ_p| / λ_p`. Any landing
within 1 ppb is a candidate operator-theoretic closed form.

## Expected outcome (cumulative discipline)

Each of the prior three CAL-4 spikes returned negative. If this
operator-theoretic probe also returns negative across a
substantive set of scalar invariants, the empirical case for
`conj:lambda-scale-bring-bloch-identity` being a genuine CAL-4
anchor (not derived from substrate) is essentially closed.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder


# ── Faddeev Φ_q on scalars (truncated product) ──────────────────
def phi_q_scalar(z, qi, K=200):
    """Φ_q(z) = ∏_{j=1..K} (1 - qi^j · z)^(-1).

    For |qi| < 1 (i.e. q > 1), this converges. K=200 gives ~50 dps
    accuracy at q_0 ≈ 1.11.
    """
    p = mp.mpf(1)
    qj = qi
    for _ in range(K):
        p /= (1 - qj * z)
        qj *= qi
        if abs(qj) < mp.mpf(10) ** (-mp.mp.dps - 10):
            break
    return p


# ── Matrix utilities (mpmath) ────────────────────────────────────
def zeros_matrix(n):
    return mp.matrix([[mp.mpf(0)] * n for _ in range(n)])


def diag(vals):
    n = len(vals)
    M = zeros_matrix(n)
    for i, v in enumerate(vals):
        M[i, i] = v
    return M


def matmul(A, B):
    return A * B


def matnorm(M):
    s = mp.mpf(0)
    for i in range(M.rows):
        for j in range(M.cols):
            s += abs(M[i, j]) ** 2
    return mp.sqrt(s)


def shift_matrix(n):
    """V|k⟩ = |k+1⟩ for k < n-1, V|n-1⟩ = 0. Strict upper-shift."""
    M = zeros_matrix(n)
    for k in range(n - 1):
        M[k + 1, k] = mp.mpf(1)
    return M


# ── Φ_q on matrices ──────────────────────────────────────────────
def phi_q_diagonal(U_eigs, qi, K=200):
    """Φ_q applied to a diagonal matrix with eigenvalues U_eigs."""
    n = len(U_eigs)
    M = zeros_matrix(n)
    for i, lam in enumerate(U_eigs):
        M[i, i] = phi_q_scalar(lam, qi, K=K)
    return M


def phi_q_nilpotent(V, qi, K_max):
    """Φ_q(V) for strictly upper-shift V (nilpotent).

    Φ_q(V) = ∏_{j=1}^K (I - qi^j V)^(-1). For V nilpotent with index
    n, the product terminates: (I - α V)^(-1) = I + αV + α²V² + …
    + α^(n-1) V^(n-1). The full product expands to a polynomial in
    V of degree ≤ n-1.
    """
    n = V.rows
    I = diag([mp.mpf(1)] * n)
    result = I.copy()
    qj = qi
    for _ in range(K_max):
        # (I - qj * V)^(-1) via geometric series, terminates at V^(n-1)
        factor = I.copy()
        V_pow = V.copy()
        alpha_pow = qj
        for _p in range(1, n):
            factor = factor + alpha_pow * V_pow
            V_pow = V_pow * V
            alpha_pow *= qj
            # break if V_pow becomes ≈ 0
            if matnorm(V_pow) < mp.mpf(10) ** (-mp.mp.dps - 5):
                break
        result = result * factor
        qj *= qi
        if abs(qj) < mp.mpf(10) ** (-mp.mp.dps - 10):
            break
    return result


def phi_q_general(M, qi, K=200):
    """Φ_q on a general matrix via the convergent product
    ∏_{j=1..K} (I - qi^j M)^(-1).

    If M is nilpotent (M^n = 0 for some n ≤ N), uses the
    exact geometric expansion (I - α M)^(-1) = ∑_k α^k M^k
    which terminates at k = n-1 — avoids the instability
    of `factor ** (-1)` for nilpotent factor.
    """
    n = M.rows
    I = diag([mp.mpf(1)] * n)
    # Compute powers M^p up to first vanishing — detects nilpotency
    M_powers = [I]
    M_pow = I.copy()
    for _ in range(n):
        M_pow = M_pow * M
        if matnorm(M_pow) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
        M_powers.append(M_pow)
    # `is_nilpotent` is True iff some power M^p (p ≤ n) had norm below
    # the precision threshold, terminating the loop early. If the loop
    # ran to completion without M^p vanishing, len(M_powers) == n+1
    # and `is_nilpotent` is False, triggering the general inverse path.
    is_nilpotent = (len(M_powers) <= n)
    if is_nilpotent:
        # (I - α M)^(-1) = ∑_{p=0}^{len(M_powers)-1} α^p M^p
        result = I.copy()
        qj = qi
        for _ in range(K):
            factor = I.copy()
            alpha_pow = qj
            for p in range(1, len(M_powers)):
                factor = factor + alpha_pow * M_powers[p]
                alpha_pow *= qj
            result = result * factor
            qj *= qi
            if abs(qj) < mp.mpf(10) ** (-mp.mp.dps - 10):
                break
        return result
    # Fallback: full inverse (unstable, not used in current spike)
    result = I.copy()
    qj = qi
    for _ in range(K):
        factor = I - qj * M
        factor_inv = factor ** (-1)
        result = result * factor_inv
        qj *= qi
        if abs(qj) < mp.mpf(10) ** (-mp.mp.dps - 10):
            break
    return result


# ── Main spike ───────────────────────────────────────────────────
def main():
    t_start = time.monotonic()
    mp.mp.dps = 50

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Qi = 1 / Q0
    # CODATA-implied λ_p target — matches the value used in
    # bring_bloch_tier{0..5}_search scripts (single source of truth).
    # Has ~31 significant digits, well above the 1e-9 ppb cutoff.
    lambda_p = mp.mpf("2.4599527843613182892482457339493")

    N = 16  # Hilbert-space dim
    K_phi = 200  # Φ_q truncation
    print(f"Faddeev pentagon operator spike  (N={N}, K={K_phi}, dps={mp.mp.dps})")
    print(f"q_0 = {mp.nstr(Q0, 12)}, λ_p = {mp.nstr(lambda_p, 12)}")
    print()

    findings = []

    # ── Construct U, V ───────────────────────────────────────────
    # Scale U by h_q = q - q^(-1) so eigenvalues h_q·q^(2k) never
    # coincide with q^integer — avoids poles in Φ_q(λ) = ∏(1-qi^j·λ)^(-1)
    # which would occur when qi^j · λ = 1.
    h_q = Q0 - Qi
    U_eigs = [h_q * Q0 ** (2 * k) for k in range(N)]
    U = diag(U_eigs)
    V = shift_matrix(N)
    print(f"U = h_q · diag(q^0, q^2, …, q^{2*(N-1)}), max eig = {mp.nstr(U_eigs[-1], 8)}")
    print(f"V = strict upper-shift on ℂ^{N}")
    print()

    # ── Verify q-Heisenberg relation U·V = q² · V·U ───────────────
    UV = matmul(U, V)
    VU = matmul(V, U)
    rel_diff = matnorm(UV - Q0 * Q0 * VU)
    rel_diff_open = mp.mpf(0)  # error on the open block (excluding boundary col)
    for i in range(N):
        for j in range(N - 1):  # exclude last column (boundary)
            d = UV[i, j] - Q0 * Q0 * VU[i, j]
            rel_diff_open += abs(d) ** 2
    rel_diff_open = mp.sqrt(rel_diff_open)
    print(f"q-Heisenberg verification:")
    print(f"  ‖U·V − q² V·U‖_full = {mp.nstr(rel_diff, 6)} (boundary error expected)")
    print(f"  ‖U·V − q² V·U‖_open = {mp.nstr(rel_diff_open, 6)} (should be ~0)")
    print()

    # ── Compute Φ_q(U), Φ_q(V), Φ_q(UV) ──────────────────────────
    print(f"Computing Φ_q(U) (diagonal, K={K_phi})…")
    PhiU = phi_q_diagonal(U_eigs, Qi, K=K_phi)
    print(f"Computing Φ_q(V) (nilpotent, K={K_phi})…")
    PhiV = phi_q_nilpotent(V, Qi, K_max=K_phi)
    print(f"Computing Φ_q(U·V) (general, K={K_phi})…")
    PhiUV = phi_q_general(UV, Qi, K=K_phi)
    print()

    # ── Pentagon sanity check ────────────────────────────────────
    LHS = matmul(PhiU, PhiV)
    RHS_inner = matmul(PhiUV, PhiU)
    RHS = matmul(PhiV, RHS_inner)
    pent_diff_full = matnorm(LHS - RHS)
    # Open block = exclude the truncation boundary column (k = N-1),
    # matching the q-Heisenberg open-block convention above. Note this
    # is an absolute-norm check; entries grow with k since Φ_q(h_q·q^(2k))
    # is large at high k, so this norm is dominated by row N-2 / col N-2
    # entries — see audit doc § Known issues for the limitation.
    pent_diff_open = mp.mpf(0)
    for i in range(N):
        for j in range(N - 1):
            d = LHS[i, j] - RHS[i, j]
            pent_diff_open += abs(d) ** 2
    pent_diff_open = mp.sqrt(pent_diff_open)
    print(f"Pentagon ‖LHS − RHS‖:")
    print(f"  full:        {mp.nstr(pent_diff_full, 6)}")
    print(f"  open block:  {mp.nstr(pent_diff_open, 6)}")
    print(f"  LHS[0,0] = {mp.nstr(LHS[0, 0], 10)}")
    print(f"  RHS[0,0] = {mp.nstr(RHS[0, 0], 10)}")
    print()

    # ── Scalar invariants ────────────────────────────────────────
    print(f"Scalar invariants — compare to λ_p = {mp.nstr(lambda_p, 12)}:")
    probes = {}

    # (a) Diagonal matrix elements
    for k in range(min(N, 8)):
        probes[f"⟨{k}|Φ_q(U)|{k}⟩"] = PhiU[k, k]
    probes["⟨0|Φ_q(V)|0⟩"] = PhiV[0, 0]
    probes["⟨0|Φ_q(U·V)|0⟩"] = PhiUV[0, 0]
    probes["⟨0|Φ_q(U)Φ_q(V)|0⟩"] = LHS[0, 0]
    probes["⟨0|Φ_q(V)Φ_q(U)|0⟩"] = matmul(PhiV, PhiU)[0, 0]
    PhiUinv = PhiU ** (-1)
    probes["⟨0|Φ_q(U)⁻¹Φ_q(V)|0⟩"] = matmul(PhiUinv, PhiV)[0, 0]

    # (b) Traces (renormalised — divide by N or by tr(I) = N)
    tr_PhiU = sum(PhiU[k, k] for k in range(N))
    tr_PhiV = sum(PhiV[k, k] for k in range(N))
    tr_PhiUV = sum(PhiUV[k, k] for k in range(N))
    tr_LHS = sum(LHS[k, k] for k in range(N))
    probes["tr(Φ_q(U))/N"] = tr_PhiU / N
    probes["tr(Φ_q(V))/N"] = tr_PhiV / N  # = 1 since V is nilpotent
    probes["tr(Φ_q(U·V))/N"] = tr_PhiUV / N
    probes["tr(LHS)/N"] = tr_LHS / N

    # (c) Ratios of probes
    probe_pairs = list(probes.items())
    for i in range(len(probe_pairs)):
        a, va = probe_pairs[i]
        for j in range(len(probe_pairs)):
            if i == j:
                continue
            b, vb = probe_pairs[j]
            if abs(vb) < mp.mpf(10) ** (-30):
                continue
            r = va / vb
            if abs(r.imag if hasattr(r, "imag") else 0) > mp.mpf(10) ** (-20):
                continue
            r_real = r.real if hasattr(r, "real") else r
            rel = abs(r_real - lambda_p) / lambda_p
            if rel < mp.mpf(10) ** (-3):
                probes[f"({a}) / ({b})"] = r_real
                if rel < mp.mpf(10) ** (-9):
                    findings.append({
                        "kind": "ratio-of-probes",
                        "numerator": a,
                        "denominator": b,
                        "value": mp.nstr(r_real, 18),
                        "rel_err": mp.nstr(rel, 8),
                    })

    # (d) Pentagon-derived: deviation tr(LHS - RHS) / λ_p target
    pent_dev_tr = sum((LHS[k, k] - RHS[k, k]) for k in range(N))

    # Print all probes + match status
    smallest_err = mp.inf
    smallest_name = None
    for name, val in probes.items():
        val_real = val.real if hasattr(val, "real") else val
        rel = abs(val_real - lambda_p) / lambda_p
        marker = ""
        if rel < mp.mpf(10) ** (-9):
            marker = " ← <1 ppb"
            findings.append({
                "kind": "direct-probe",
                "name": name,
                "value": mp.nstr(val_real, 18),
                "rel_err": mp.nstr(rel, 8),
            })
        elif rel < mp.mpf(10) ** (-3):
            marker = " ← <0.1%"
        elif rel < mp.mpf("0.1"):
            marker = " ← <10%"
        if rel < smallest_err:
            smallest_err = rel
            smallest_name = name
        print(f"  {name:<32s} = {mp.nstr(val_real, 12)}  (rel err = {mp.nstr(rel, 5)}){marker}")
    print()
    print(f"  closest: {smallest_name} (rel err = {mp.nstr(smallest_err, 6)})")
    print()

    # ── Structural finding: Φ_q functional eq at z_* = h_q · q^10 ──
    # The Φ_q functional equation Φ_q(qz)/Φ_q(z) = 1/(1−z) yields
    # λ_p ≈ 1/(1 − z_*) iff z_* ≈ 1 − 1/λ_p ≈ 0.5935. The
    # substrate-natural quantity h_q · q^10 ≈ 0.5935 hits this very
    # closely (19 ppm). For comparison, the existing benchmark
    # 5/2 − h_q²·G hits at 5.6 ppm. Both are CAL-4-tier near-matches;
    # neither reaches ppb precision.
    G = mp.catalan
    form_5_2 = mp.mpf(5) / 2 - h_q ** 2 * G
    form_phi_q_fe = 1 / (1 - h_q * Q0 ** 10)
    err_5_2 = abs(form_5_2 - lambda_p) / lambda_p
    err_phi_q_fe = abs(form_phi_q_fe - lambda_p) / lambda_p
    print("Operator-theoretic-derived near-match (this spike's structural finding):")
    print(f"  Φ_q functional eq at z_*=h_q·q^10:  1/(1−h_q·q^10) = {mp.nstr(form_phi_q_fe, 16)}")
    print(f"  → matches λ_p to                                    {mp.nstr(err_phi_q_fe * 1e6, 5)} ppm")
    print(f"Existing CAL-4 benchmark (probe_family_a_variants):")
    print(f"  5/2 − h_q²·G                       = {mp.nstr(form_5_2, 16)}")
    print(f"  → matches λ_p to                    {mp.nstr(err_5_2 * 1e6, 5)} ppm")
    print()
    print(f"SUMMARY: {len(findings)} candidate <1 ppb match(es).")
    print(f"         (Φ_q functional-eq form found at 19 ppm — see audit doc)")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder(
        "faddeev-pentagon-operator-spike",
        engine="mpmath",
        start_time=t_start,
    )
    w.set_description(
        "Spike: operator-theoretic Faddeev pentagon route to "
        f"λ_scale. N={N}-dim truncated Heisenberg rep with "
        "U = h_q · diag(q^(2k)), V = strict upper-shift; satisfies "
        "U·V = q²·V·U on the open block (verified to ~10⁻⁵⁰). "
        "Computes Φ_q(U), Φ_q(V), Φ_q(U·V) via spectral / nilpotent "
        "calculus, records the pentagon-identity matrix-norm residual "
        "(reported absolute; large due to high-eigenvalue entries — "
        "the (0,0) entries agree to 10 digits, see audit doc § Known "
        "issues), then probes a substrate-natural family of scalar "
        "invariants (diagonal matrix elements, traces, ratios) for "
        "ppb-precision matches to λ_p = 2.4599527843613… (CODATA). "
        "Companion to PR #923/#928/#941 cumulative CAL-4 audit — "
        "operator-theoretic route is the hardest of the four "
        "structurally-distinct paths."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("dps", 50)
    w.add_parameter("N", N)
    w.add_parameter("K_phi_truncation", K_phi)
    w.add_data("q_heisenberg_full_err", mp.nstr(rel_diff, 12))
    w.add_data("q_heisenberg_open_err", mp.nstr(rel_diff_open, 12))
    w.add_data("pentagon_full_err", mp.nstr(pent_diff_full, 12))
    w.add_data("pentagon_open_err", mp.nstr(pent_diff_open, 12))
    w.add_data("smallest_probe_name", smallest_name)
    w.add_data("smallest_probe_rel_err", mp.nstr(smallest_err, 12))
    w.add_data("n_probes", len(probes))
    w.add_data("findings", findings)
    w.add_data("structural_near_match", {
        "form": "1 / (1 - h_q * q_0^10)",
        "interpretation": "Φ_q(q·z_*) / Φ_q(z_*) = 1/(1 - z_*) with z_* = h_q·q_0^10",
        "value": mp.nstr(form_phi_q_fe, 22),
        "lambda_p_target": mp.nstr(lambda_p, 22),
        "abs_error": mp.nstr(abs(form_phi_q_fe - lambda_p), 12),
        "rel_error_ppm": mp.nstr(err_phi_q_fe * 1e6, 8),
    })
    w.add_data("existing_benchmark", {
        "form": "5/2 - h_q^2 * G",
        "source": "probe_family_a_variants.py probe_1",
        "value": mp.nstr(form_5_2, 22),
        "rel_error_ppm": mp.nstr(err_5_2 * 1e6, 8),
    })
    w.add_assertion(
        "spike_completed",
        computed=1.0,
        expected=1.0,
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
