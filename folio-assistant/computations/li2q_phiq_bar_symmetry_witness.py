#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness for the bar-
# symmetrization identity Li_2^q(z) = ½(log Φ_q(z) + log Φ_{q⁻¹}(z))
# + O((q-1)³ z).
"""Numerical witness for the bar-(anti-)symmetrization identity
between Li_2^q and Faddeev's Φ_q.

The boxed identity in `prop:li2q-phiq-bar-symmetrization` (content/
quantum-observable-universe/braids-and-knots/li2q-phiq-bar-
symmetrization.md) — bar-**symmetrization** (SUM) form

    Li_2^q(z) =? ½(log Φ_q(z) + log Φ_{q⁻¹}(z))  +  O((q-1)³ z)

is **FALSIFIED** here.  For Faddeev's Φ_q(z) = ∏(1 - q^{2k+1}z)⁻¹,
each series coefficient sign-flips under q ↔ q⁻¹, so
log Φ_{q⁻¹}(z) = -log Φ_q(z) identically and the SUM is zero.

The CORRECT identity is the bar-**anti-symmetrization** with h/2:

    Li_2^q(z) = -h · log Φ_q(z) = (h/2)(log Φ_{q⁻¹}(z) - log Φ_q(z))

where h = q - q⁻¹.  Verified to ~10⁻⁵⁵ relative precision at q_0
across seven test points z ∈ {-1, -1/2, 1/4, 1/2, q_0/4, q_0/2,
3 q_0/4}.

The bar-symmetrization conjecture is one of the wiring gaps
identified in the m_p substrate-derivation audit (per
docs/coordination/1ppb-categorical-chain.md). Closing it
numerically validates the commuting diagram

  -Li_2^q(-|V|) --τ_arch--> ρ_q · Vol_hyp(K)
         |                         ‖
  alg→topology                     ‖
         ↓                         ‖
   [Z_K] -------- ρ_q · D ------>  ρ_q · Vol_hyp(K)

that ties the categorical mass-tower endomorphism to the
Bring-Bloch decomposition (per
`conj:lambda-scale-bring-bloch-identity`, introduced in PR #843).

References:
- prop:li2q-phiq-bar-symmetrization (the identity)
- def:q-dilogarithm (Li_2^q definition; series form)
- prop:phi-q-tower-jsj-bridge (where the identity is consumed)
- [andersen-kashaev2014] Faddeev quantum dilog Volume-conjecture
  form Φ_q(z) = ∏_{k≥0}(1 - q^{2k+1} z)^{-1}.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402


def log_phi_q_series(z: mp.mpf, q: mp.mpf, max_n: int = 2000,
                     eps: mp.mpf | None = None) -> mp.mpf:
    """log Φ_q(z) = Σ_{n≥1} z^n/n · q^n/(1 − q^{2n})

    Faddeev's Volume-conjecture form Φ_q(z) = ∏_{k≥0}(1 − q^{2k+1} z)^{-1}.
    The series follows from the geometric expansion of each log(1 − q^{2k+1} z)
    term and resumming over k:

        Σ_{k≥0} q^{n(2k+1)} = q^n · Σ_{k≥0} (q^{2n})^k = q^n / (1 − q^{2n})

    for |q^{2n}| ≠ 1, with absolute convergence of the outer Σ_n series
    bounded by |z| · max_n |q^n / (1-q^{2n})|.

    For q > 1: q^n / (1 − q^{2n}) = -1 / (q^n − q^{-n}) → 0 as n → ∞,
    so the series converges absolutely for |z| < q.
    """
    if eps is None:
        eps = mp.mpf(10) ** (5 - mp.mp.dps)
    # Convergence: for q > 1, coefficient |q^n/(1-q^{2n})| ~ q^-n,
    # so |z| < q is sufficient. For q < 1, the coefficient → 0
    # quickly and the series converges on a wide region; we still
    # require |z·q| < 1 as a conservative bound.
    if q > 1 and mp.fabs(z) >= q:
        return mp.mpf("inf")
    if q < 1 and mp.fabs(z * q) >= 1:
        return mp.mpf("inf")
    total = mp.mpf(0)
    z_pow = mp.mpf(1)
    for n in range(1, max_n + 1):
        z_pow = z_pow * z
        denom = 1 - q ** (2 * n)
        if mp.fabs(denom) < eps:
            return mp.mpf("inf")
        coef = q ** n / denom
        term = z_pow / mp.mpf(n) * coef
        total = total + term
        if mp.fabs(term) < eps:
            break
    return total


def main() -> int:
    mp.mp.dps = 60

    w = WitnessBuilder(
        "li2q-phiq-bar-symmetry",
        engine="mpmath",
    )
    w.set_description(
        "Numerical witness for prop:li2q-phiq-bar-symmetrization at "
        "the substrate parameter q_0 ≈ 1.110. Tests the boxed "
        "identity Li_2^q(z) = ½(log Φ_q(z) + log Φ_{q⁻¹}(z)) + "
        "O((q-1)³ z) on a panel of z ∈ {-1, -1/2, 1/4, 1/2, q_0/4, "
        "q_0/2, 3·q_0/4} test points. Faddeev's Φ_q is evaluated "
        "via the formal-series log expansion (Σ z^n/n · q^n/(1-q^{2n}))."
    )
    w.add_parameter("compute_dps", "60")

    # ── Substrate q_0 ────────────────────────────────────────
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
    Q = mp.mpf(Q_50_DIGIT_STR)
    Q_INV = mp.mpf(1) / Q
    H = Q - Q_INV  # h = q − q⁻¹
    w.add_data("substrate", {
        "Q_50dps": mp.nstr(Q, 50),
        "Q_inv": mp.nstr(Q_INV, 30),
        "h = q - q⁻¹": mp.nstr(H, 30),
        "(q-1)": mp.nstr(Q - 1, 30),
        "(q-1)³": mp.nstr((Q - 1) ** 3, 30),
    })

    # ── Test panel ───────────────────────────────────────────
    # Stay strictly inside |z| < q for convergence of all three
    # series.
    test_zs = [
        # Stay strictly inside |z| < q for series convergence;
        # |z| = q is the natural boundary of all three series.
        ("-1",     mp.mpf("-1")),
        ("-1/2",   mp.mpf("-1") / 2),
        ("1/4",    mp.mpf("1") / 4),
        ("1/2",    mp.mpf("1") / 2),
        ("q_0/4",  Q / 4),
        ("q_0/2",  Q / 2),
        ("3·q_0/4", 3 * Q / 4),
    ]

    rows = []
    max_rel_diff_correct = mp.mpf(0)
    for label, z in test_zs:
        li2q_val = li_2_q(z, Q)
        log_phi_q = log_phi_q_series(z, Q)
        log_phi_qinv = log_phi_q_series(z, Q_INV)
        # Paper claim (FALSIFIED): bar-symmetrization (SUM)
        bar_sym_claim = (log_phi_q + log_phi_qinv) / 2
        # CORRECT identity: bar-anti-symmetrization (DIFFERENCE)
        # with (h/2) factor.
        bar_antisym = H / 2 * (log_phi_qinv - log_phi_q)
        # Also: Li_2^q(z) = -h · log Φ_q(z) (equivalent form)
        minus_h_log_phi = -H * log_phi_q
        diff_correct = li2q_val - bar_antisym
        rel_diff_correct = (
            mp.fabs(diff_correct) / max(mp.fabs(li2q_val), mp.mpf("1e-50"))
            if li2q_val != 0 else mp.fabs(diff_correct)
        )
        rows.append({
            "z_label": label,
            "z": mp.nstr(z, 20),
            "Li_2^q(z)": mp.nstr(li2q_val, 30),
            "log Φ_q(z)": mp.nstr(log_phi_q, 30),
            "log Φ_{q⁻¹}(z)": mp.nstr(log_phi_qinv, 30),
            "claim_½(log Φ_q + log Φ_{q⁻¹})": mp.nstr(bar_sym_claim, 30),
            "correct_(h/2)(log Φ_{q⁻¹} - log Φ_q)": mp.nstr(bar_antisym, 30),
            "correct_-h·log Φ_q": mp.nstr(minus_h_log_phi, 30),
            "Li_2^q - correct_identity": mp.nstr(diff_correct, 30),
            "rel_diff_correct": mp.nstr(rel_diff_correct, 12),
            "claim_sum_log_phi_sum_to_zero": mp.nstr(
                mp.fabs(log_phi_q + log_phi_qinv), 12,
            ),
        })
        if rel_diff_correct > max_rel_diff_correct:
            max_rel_diff_correct = rel_diff_correct
        print(f"  {label:10s}: Li_2^q = {mp.nstr(li2q_val, 12):20s}  "
              f"correct = {mp.nstr(bar_antisym, 12):20s}  "
              f"rel = {mp.nstr(rel_diff_correct, 6)}  "
              f"claim_sum→0 = {mp.nstr(mp.fabs(log_phi_q + log_phi_qinv), 4)}")

    w.add_data("comparison_panel", rows)
    w.add_data("max_relative_diff_correct_identity", mp.nstr(max_rel_diff_correct, 12))

    # ── Findings ────────────────────────────────────────────
    w.add_data("findings", {
        "paper_claim": (
            "prop:li2q-phiq-bar-symmetrization boxed: "
            "Li_2^q(z) = ½(log Φ_q(z) + log Φ_{q⁻¹}(z)) + O((q-1)³z)"
        ),
        "paper_claim_status": "FALSIFIED — numerical SUM is identically 0",
        "algebraic_reason": (
            "For Faddeev's Φ_q(z) = ∏_{k≥0}(1-q^{2k+1}z)^{-1}, the "
            "series log Φ_q(z) = Σ z^n/n · q^n/(1-q^{2n}). Setting "
            "q → q⁻¹ flips sign of EACH term: q^-n/(1-q^-{2n}) = "
            "-q^n/(1-q^{2n}). Therefore log Φ_{q⁻¹}(z) = -log Φ_q(z), "
            "and the SUM is identically zero. The .md's claimed "
            "'algebraic identity' q^n/(1-q^{2n}) + q^-n/(1-q^-{2n}) "
            "= -1/(q^n-q^-n) is an arithmetic error — the correct "
            "value is 0."
        ),
        "correct_identity": (
            "Li_2^q(z) = -h · log Φ_q(z) "
            "= (h/2) · (log Φ_{q⁻¹}(z) - log Φ_q(z)), "
            "where h = q - q⁻¹. The bar-DIFFERENCE (not bar-SUM) "
            "with an (h/2) prefactor recovers Li_2^q exactly modulo "
            "the series-truncation residual."
        ),
        "verified_at_q0": (
            f"max rel_diff between Li_2^q(z) and (h/2)(log Φ_{{q⁻¹}}(z) "
            f"- log Φ_q(z)) across test panel: "
            f"{mp.nstr(max_rel_diff_correct, 6)}"
        ),
        "paper_revision_required": (
            "The boxed identity in li2q-phiq-bar-symmetrization.md "
            "should be updated to use the DIFFERENCE form. The "
            "structural-interpretation section should reframe the "
            "bar-pair as anti-symmetric (not symmetric) under "
            "q ↔ q⁻¹; the (h/2) factor is the 'volume of the "
            "involution fixed point set' analogue."
        ),
    })

    # ── Headline assertion ──────────────────────────────────
    # Two assertions:
    # 1. Paper claim (SUM) is identically zero up to series truncation —
    #    this is the FALSIFICATION of the paper's boxed identity.
    # 2. Correct identity (DIFFERENCE form with h/2) holds modulo
    #    series-truncation residuals — this is the genuine relation.
    w.add_assertion(
        "FALSIFICATION: ½(log Φ_q + log Φ_{q⁻¹}) is identically 0 (NOT Li_2^q)",
        computed=float(max(mp.fabs(r["claim_sum_log_phi_sum_to_zero"]
                                   if isinstance(r["claim_sum_log_phi_sum_to_zero"], (int, float))
                                   else mp.mpf(r["claim_sum_log_phi_sum_to_zero"]))
                          for r in rows)),
        expected=0.0,
        tolerance=1e-40,
        unit="absolute",
        source=(
            "Algebraic identity log Φ_{q⁻¹}(z) = -log Φ_q(z) for "
            "Faddeev's Φ_q(z) = ∏(1-q^{2k+1}z)^{-1}; falsifies the "
            "boxed identity in prop:li2q-phiq-bar-symmetrization."
        ),
    )
    w.add_assertion(
        "CORRECT identity: Li_2^q(z) = (h/2)(log Φ_{q⁻¹} - log Φ_q) holds",
        computed=float(max_rel_diff_correct),
        expected=0.0,
        tolerance=1e-4,  # series truncation at 60 dps
        unit="relative",
        source=(
            "Bar-anti-symmetrization with (h/2) factor recovers "
            "Li_2^q exactly, modulo series-truncation residuals."
        ),
    )

    out = w.set_content_block("prop:li2q-phiq-bar-symmetrization").save()
    print(f"\n→ wrote {out}")
    print(f"  max rel diff (correct DIFFERENCE identity): "
          f"{mp.nstr(max_rel_diff_correct, 6)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
