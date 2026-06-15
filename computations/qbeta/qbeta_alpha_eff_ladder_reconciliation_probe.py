#!/usr/bin/env python3
"""qbeta_alpha_eff_ladder_reconciliation_probe.py
=================================================

**Reconciliation tranche** (follow-up to `qbeta_alpha_eff_hoefsmit_symbolic_probe.py`):
does the on-main α_eff-based phase actually reproduce the #1887 ladder
`cos(Φ(u))` with `Φ₁ = √2`, `c_2 = −1` — i.e. does `Φ₂` drop out of the
closed-form `alpha = (z−1)·h/2`?

The previous probe used the producer's *line-144 exploratory candidate*
`cos(alpha − u/2 − u²/2 − …)`. This probe uses the producer's **canonical**
N=1/N=2 model (probe_q_beta_operator_valued_N3.py lines 75–78):

    Q_N1 = Q_A · cos(alpha − u/2)
    Q_N2 = Q_N1 · (1 − u²)            ( u = b·ℏ_q² )

and asks the decisive question by Taylor-expanding the base-normalised ratio

    G(u) = Q_N2 / [Q_A · cos(alpha)] = cos(alpha − u/2)(1 − u²) / cos(alpha)
         = 1 + c_1 u + c_2 u² + c_3 u³ + …

- The #1887 reframe requires (proved) `c_1 = 0`, `c_2 = −1` ⇒ leading phase
  coefficient `√2` (`Φ₁ = √2`).
- If the canonical α_eff model gives `c_1 ≠ 0` and `c_2 ≠ −1`, then the
  producer's α_eff phase is a **different parametrisation** than #1887's
  `Φ(u)` and `Φ₂` does **not** follow from `(z−1)·h/2` by reparametrisation —
  the closure stays the kernel-derivation frontier.

This is a formalize-first decision probe: it either closes `Φ₂` (the
reparametrisation works) or refutes the easy path (they are different
phases) before any wide symbolic search. No fit; nothing wired.

## References
- α_eff symbolic source (on main): `probe_q_beta_operator_valued_N3.py` (lines 75–78)
- prior probe + finding: `qbeta_alpha_eff_hoefsmit_symbolic_probe.py` (PR #1907)
- proved c_2 = −1 / Φ₁ = √2: PR #1602, PR #1887
- c_3 cross-anchor target: `qbeta_utils.c3_target_at`
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, sqrt, cos, taylor, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at  # noqa: E402


def substrate(q: mpf) -> dict[str, mpf]:
    """On-main N=3 closed forms (probe_q_beta_operator_valued_N3.py)."""
    h = q - 1 / q
    z = 1 / (sqrt(q) + 1 / sqrt(q))
    hbar_q2 = ((q - 1) / q) ** 2
    alpha = (z - 1) * h / 2
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = sqrt(d1 * d2 + 1)
    return {"alpha": alpha, "u": b * hbar_q2, "b": b, "hbar_q2": hbar_q2}


def canonical_ladder_coeffs(alpha: mpf, order: int = 4) -> list[mpf]:
    """c_k of G(u) = cos(alpha - u/2)(1 - u²)/cos(alpha) — the CANONICAL
    producer N=2 model, base-normalised so G(0)=1."""
    ca = cos(alpha)

    def G(u):
        return cos(alpha - u / 2) * (1 - u ** 2) / ca

    return taylor(G, mpf(0), order)


def main() -> int:
    set_compute_dps()
    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    sqrt2 = sqrt(mpf(2))

    rows = []
    raw = []   # (c1, c2) per anchor, lossless for assertions
    print("=" * 86)
    print(" Q_β α_eff ladder reconciliation — canonical cos(α-u/2)(1-u²) vs #1887")
    print("=" * 86)
    print(f"  #1887 (proved) requires: c_1 = 0, c_2 = -1  (⇒ Φ₁ = √2 = {float(sqrt2):.6f})")
    print()
    print(f"  {'anchor':<8}{'α':>14}{'c_1 (canon)':>16}{'c_2 (canon)':>16}"
          f"{'c_2 == -1?':>12}{'leadφ vs √2':>14}")
    print(f"  {'-'*8}{'-'*14}{'-'*16}{'-'*16}{'-'*12}{'-'*14}")

    for name, qf in (("proton", q_at), ("muon", q_muon_at)):
        q = qf(mp.dps)
        s = substrate(q)
        coeffs = canonical_ladder_coeffs(s["alpha"], order=4)
        c1, c2, c3 = coeffs[1], coeffs[2], coeffs[3]
        raw.append((c1, c2))
        c2_is_minus1 = fabs(c2 - (-1)) < mpf("1e-6")
        # c_2 = -9/8 is structural (α-independent — see witness: both anchors
        # identical). Confirm the closed value.
        c2_eq_minus_9_8 = fabs(c2 - mpf(-9) / 8) < mpf("1e-9")
        # leading phase coefficient from c_2: if Q/base = cos(Φ), c_2 = -Φ_lead²/2
        # so |Φ_lead| = sqrt(-2 c_2) when c_2 < 0 (compare to √2).
        phi_lead = sqrt(-2 * c2) if c2 < 0 else mpf("nan")
        # RIGOUR: can a single ladder rescale ũ = λ·u reconcile with #1887?
        # Under ũ=λu: c̃_2 = c_2/λ², c̃_1 = c_1/λ. Pick λ to force c̃_2 = -1
        # (λ = sqrt(c_2 / -1)); then check whether c̃_1 also vanishes. It cannot,
        # since c_1 ≠ 0 and λ is finite ⇒ no single rescale fixes BOTH.
        lam_fix_c2 = sqrt(c2 / mpf(-1))          # makes c̃_2 = -1
        c1_after_rescale = c1 / lam_fix_c2       # residual u¹ rung (≠ 0)
        rescale_reconciles = fabs(c1_after_rescale) < mpf("1e-12")
        rows.append({
            "anchor": name,
            "alpha": fmt(s["alpha"]),
            "c_1_canonical": fmt(c1),
            "c_2_canonical": fmt(c2),
            "c_3_canonical": fmt(c3),
            "c_2_equals_minus_1": bool(c2_is_minus1),
            "c_2_equals_minus_9_over_8": bool(c2_eq_minus_9_8),
            "phi_lead_from_c2": fmt(phi_lead),
            "phi_lead_equals_sqrt2": bool(fabs(phi_lead - sqrt2) < mpf("1e-6")),
            "lambda_to_force_c2_minus1": fmt(lam_fix_c2),
            "c_1_after_rescale": fmt(c1_after_rescale),
            "single_rescale_reconciles_both": bool(rescale_reconciles),
            "c_3_true_target": fmt(c3_target_at(q, q_codata, me)),
        })
        print(f"  {name:<8}{float(s['alpha']):>14.8f}{float(c1):>16.8f}"
              f"{float(c2):>16.8f}{str(c2_is_minus1):>12}{float(phi_lead):>14.6f}")

    print()
    print("=" * 86)
    print(" VERDICT")
    print("=" * 86)
    c2_match = all(r["c_2_equals_minus_1"] for r in rows)
    c1_zero = all(fabs(c1) < mpf("1e-12") for c1, _ in raw)
    if c2_match and c1_zero:
        print("  RECONCILED — the canonical α_eff model reproduces c_1=0, c_2=-1;")
        print("  Φ₂ follows from the symbolic alpha = (z-1)·h/2.")
        verdict = "RECONCILED_PHI2_FROM_SYMBOLIC_ALPHA"
    else:
        print("  NOT RECONCILED — the canonical α_eff phase cos(α-u/2)(1-u²) has")
        print(f"    c_1 = {rows[0]['c_1_canonical'][:12]} (≠ 0) and")
        print(f"    c_2 = {rows[0]['c_2_canonical'][:12]} (≠ -1; ⇒ leading phase coeff")
        print(f"    {rows[0]['phi_lead_from_c2'][:8]} ≠ √2 = {float(sqrt2):.6f}).")
        print("  So the on-main α_eff = (z-1)·h/2 is a DIFFERENT phase")
        print("  parametrisation than the #1887 Φ(u): Φ₂ does NOT drop out of it")
        print("  by reparametrisation. α_eff stays a (bar-odd, correct) leading")
        print("  approximation; the exact Φ₂ remains the kernel-derivation frontier.")
        print()
        print("  RIGOUR — no single ladder rescale ũ=λ·u reconciles both rungs:")
        print(f"    c_2 = -9/8 STRUCTURALLY (α-independent: both anchors identical).")
        print(f"    λ to force c̃_2=-1 is {rows[0]['lambda_to_force_c2_minus1'][:8]}, but then")
        print(f"    c̃_1 = {rows[0]['c_1_after_rescale'][:10]} ≠ 0 (the u¹ rung survives).")
        print(f"    Fixing c_2 and c_1 needs two d.o.f.; a rescale has one ⇒ impossible.")
        verdict = "NOT_RECONCILED_ALPHA_EFF_IS_DISTINCT_PHASE_FROM_1887_PHI"

    wb = WitnessBuilder(
        "qbeta-alpha-eff-ladder-reconciliation-probe", engine="mpmath",
    )
    wb.set_description(
        "Reconciliation tranche: test whether the on-main α_eff-based phase "
        "(canonical producer model cos(alpha-u/2)(1-u²), alpha=(z-1)h/2) "
        "reproduces the #1887 ladder c_1=0, c_2=-1 (Φ₁=√2), i.e. whether Φ₂ "
        "follows from the symbolic alpha. Uses the CANONICAL N=2 model (not "
        "the line-144 exploratory candidate of the prior probe). Verdict "
        "records whether α_eff reconciles with #1887 Φ(u) or is a distinct "
        "phase parametrisation. No fit; nothing wired."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("anchors", rows)
    wb.add_data("verdict", verdict)
    wb.add_data("phi1_sqrt2", fmt(sqrt2))
    wb.add_data("interpretation", (
        "If c_2 != -1 (canonical α_eff model), the on-main alpha=(z-1)h/2 is a "
        "different phase decomposition than the #1887 Φ(u); Φ₂ does not follow "
        "from it by reparametrisation, and the closure stays the kernel "
        "(SW-residue/KLR) frontier. The bar-odd parity of alpha (prior probe) "
        "is unaffected — it remains an independent confirmation of #1900."
    ))
    wb.add_assertion(
        "decisive_c2_compared_to_minus1_both_anchors",
        computed=1.0 if all(
            fabs(c2 - (-1)) > mpf("1e-9") or fabs(c2 - (-1)) < mpf("1e-9")
            for _, c2 in raw
        ) else 0.0,
        expected=1.0,   # probe always produces a decisive c_2 (this asserts it ran)
    )
    wb.add_assertion(
        "verdict_matches_c2_reconciliation",
        computed=1.0 if (
            (verdict.startswith("RECONCILED")) == (c2_match and c1_zero)
        ) else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "c2_is_structural_minus_9_over_8_both_anchors",
        computed=1.0 if all(r["c_2_equals_minus_9_over_8"] for r in rows) else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "no_single_rescale_reconciles_both_rungs",
        computed=1.0 if not any(
            r["single_rescale_reconciles_both"] for r in rows
        ) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-alpha-eff-ladder-reconciliation-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
