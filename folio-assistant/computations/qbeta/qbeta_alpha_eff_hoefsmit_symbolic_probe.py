#!/usr/bin/env python3
"""qbeta_alpha_eff_hoefsmit_symbolic_probe.py
================================================

**Lift the on-main N=3 α_eff to a symbolic phase and reconcile it with the
#1887/#1900 `cos(Φ(u))` ladder reframe** — a concrete contribution to the
KLR/crystal residue-A program (scope doc
`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`, on
`main`), supplying the "Symbolic α(q)" input that scope lists as open.

## Corpus-grep finding (this probe documents it)

`probe_q_beta_operator_valued_N3.py` (on `main`) already carries α_eff in
**closed symbolic form**:

    z      = 1 / (√q + 1/√q)            # bar-EVEN  (= 1/(2 cosh(η/2)))
    h      = q − 1/q                    # bar-ODD   (= 2 sinh η, Hecke param)
    alpha  = (z − 1) · h / 2            # bar-ODD   ⇒ sources the bar-odd c_3
    ℏ_q    = (q − 1)/q,   u = b·ℏ_q²    # ladder variable
    Q_β/Q_A = cos( alpha − u/2 − u²/2 − u³/2 − … )       (N=3 candidate, line 144)

So the "symbolic α(q)" is **not open** — it is `alpha = (z−1)h/2`, and its
bar-ODD parity independently confirms the #1900 kernel constraint
(`a_1 = −c_3` bar-odd).

## The precise reconciliation gap (this probe quantifies it)

The #1887 reframe wrote `Q_β/Q_A = cos(Φ(u))` with `Φ(u) = Φ₁u + Φ₂u² + …`,
`Φ₁ = √2`, **no constant term and no u¹ term** (`c_1 = 0`, ladder starts at
`k=2`). The on-main producer instead has a phase `alpha − u/2 − u²/2 − …`
with a **non-zero constant `alpha`** and a **non-zero u¹ coefficient −1/2**.
These are different parametrisations of the same observable. Writing the
ladder base so that `F(0)=1` (i.e. dividing by `cos(alpha)`),

    F(u) = cos(alpha − u/2 − u²/2 − u³/2) / cos(alpha)
         = 1 + c_1 u + c_2 u² + c_3 u³ + …

gives, by Taylor expansion, `c_1 = (1/2)·tan(alpha) ≠ 0`. So the producer's
`u = b·ℏ_q²` ladder has a non-vanishing **u¹ rung** — it is NOT the same `u`
as the #1887 reframe (whose ladder starts at u²). This probe reports the
numerical `c_1, c_2, c_3` from the producer parametrisation at both anchors,
making the gap explicit: **reconciling the two `u`'s (a rescaling / change of
ladder variable that kills the u¹ term and normalises `c_2 = −1`) is the
concrete next step** for deriving `Φ₂` symbolically from `alpha = (z−1)h/2`.

No fit; no production wiring; closure stays the KLR/SW-residue frontier.

## References
- α_eff symbolic source (on main): `probe_q_beta_operator_valued_N3.py`
- ladder reframe + kernel constraints: PR #1887, PR #1900 (merged)
- KLR residue-A program: `docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, sqrt, cos, sin, tan, taylor, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def substrate_quantities(q: mpf) -> dict[str, mpf]:
    """The on-main N=3 closed forms (probe_q_beta_operator_valued_N3.py)."""
    h = q - 1 / q                                  # bar-odd Hecke param
    z = 1 / (sqrt(q) + 1 / sqrt(q))                # bar-even
    hbar_q = (q - 1) / q
    hbar_q2 = hbar_q ** 2
    alpha = (z - 1) * h / 2                         # bar-odd single-wrap angle
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = sqrt(d1 * d2 + 1)                           # Hoefsmit normalisation
    u = b * hbar_q2                                 # ladder variable
    return {"h": h, "z": z, "alpha": alpha, "b": b, "hbar_q2": hbar_q2, "u": u}


def ladder_coeffs_from_producer_phase(alpha: mpf, order: int = 4) -> list[mpf]:
    """Taylor coeffs c_k of  F(u) = cos(alpha - Σ_{k≥1} u^k/2) / cos(alpha).

    The geometric phase tail has the closed form
    `Σ_{k≥1} u^k/2 = u / (2(1-u))`, so the coefficients through `order` are
    mathematically exact with no arbitrary truncation. Returns
    [c_0, c_1, c_2, c_3, ...]; c_0 = 1 by construction.
    """
    ca = cos(alpha)

    def F(u):
        tail = u / (2 * (1 - u))     # = Σ_{k≥1} u^k/2, closed form
        return cos(alpha - tail) / ca

    return taylor(F, mpf(0), order)


def main() -> int:
    set_compute_dps()

    rows = []
    c1_raw: list[tuple[mpf, mpf]] = []   # (c_1, tan(α)/2) per anchor, lossless
    print("=" * 84)
    print(" Q_β α_eff (on-main N=3 closed form) → ladder c_k reconciliation")
    print("=" * 84)
    print(f"  α = (z-1)·h/2,  z = 1/(√q+1/√q) [bar-even],  h = q-1/q [bar-odd] ⇒ α bar-ODD")
    print(f"  producer phase: Q_β/Q_A = cos(α - Σ u^k/2),  u = b·ℏ_q²")
    print()
    print(f"  {'anchor':<8}{'α':>16}{'u':>14}{'c_1':>14}{'c_2':>14}{'c_3':>14}")
    print(f"  {'-'*8}{'-'*16}{'-'*14}{'-'*14}{'-'*14}{'-'*14}")

    for name, qf in (("proton", q_at), ("muon", q_muon_at)):
        q = qf(mp.dps)
        s = substrate_quantities(q)
        coeffs = ladder_coeffs_from_producer_phase(s["alpha"], order=4)
        c1, c2, c3 = coeffs[1], coeffs[2], coeffs[3]
        # the analytic prediction c_1 = tan(α)/2 (the reconciliation gap)
        c1_pred = tan(s["alpha"]) / 2
        c1_raw.append((c1, c1_pred))     # keep raw mpf for the assertion
        rows.append({
            "anchor": name,
            "q": fmt(q),
            "alpha": fmt(s["alpha"]),
            "alpha_is_bar_odd": True,   # (z-1)·h/2, h bar-odd, z bar-even
            "u": fmt(s["u"]),
            "c_1_producer": fmt(c1),
            "c_1_analytic_tan_alpha_over_2": fmt(c1_pred),
            "c_1_nonzero": bool(fabs(c1) > mpf("1e-30")),
            "c_2_producer": fmt(c2),
            "c_3_producer": fmt(c3),
        })
        print(f"  {name:<8}{float(s['alpha']):>16.8f}{float(s['u']):>14.6e}"
              f"{float(c1):>14.6f}{float(c2):>14.6f}{float(c3):>14.6f}")

    print()
    print("=" * 84)
    print(" VERDICT")
    print("=" * 84)
    print("  The on-main α_eff = (z-1)·h/2 is closed-form symbolic and bar-ODD")
    print("  (h = q-1/q). The producer's u = b·ℏ_q² ladder has a NON-ZERO u¹ rung")
    print("  c_1 = tan(α)/2 ≠ 0, so it is a DIFFERENT ladder variable than the")
    print("  #1887 reframe (c_1 = 0, c_2 = -1). Reconciling the two u's — a change")
    print("  of ladder variable killing the u¹ term and normalising c_2 = -1 — is")
    print("  the concrete next step to derive Φ₂ symbolically from (z-1)·h/2.")
    verdict = "ALPHA_EFF_SYMBOLIC_ON_MAIN_LADDER_VARIABLE_RECONCILIATION_OPEN"

    wb = WitnessBuilder(
        "qbeta-alpha-eff-hoefsmit-symbolic-probe", engine="mpmath",
    )
    wb.set_description(
        "Lift the on-main N=3 α_eff (probe_q_beta_operator_valued_N3.py) to a "
        "symbolic phase and reconcile with the #1887/#1900 cos(Φ(u)) ladder "
        "reframe. Finds: α_eff = (z-1)·h/2 is ALREADY closed-form symbolic on "
        "main and bar-ODD (h=q-1/q), independently confirming the #1900 "
        "bar-odd kernel constraint. Quantifies the reconciliation gap: the "
        "producer's u=b·ℏ_q² ladder has c_1 = tan(α)/2 ≠ 0 (a non-zero u¹ "
        "rung), so it differs from the #1887 reframe (c_1=0, c_2=-1). The "
        "ladder-variable reconciliation is the concrete next step for a "
        "symbolic Φ₂. Contribution to the KLR residue-A program; no fit, "
        "nothing wired."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("anchors", rows)
    wb.add_data("verdict", verdict)
    wb.add_data("alpha_eff_symbolic", "(z-1)*h/2 ; z=1/(sqrt(q)+1/sqrt(q)) ; h=q-1/q")
    wb.add_data("interpretation", (
        "α_eff = (z-1)·h/2 is closed-form symbolic on main (not open as the "
        "KLR scope lists). It is bar-ODD, confirming #1900. The open piece is "
        "narrower than 'derive symbolic α': it is the ladder-variable "
        "reconciliation between the producer phase (c_1≠0) and the #1887 "
        "reframe (c_1=0, c_2=-1), after which Φ₂ follows from the symbolic α."
    ))
    wb.add_assertion(
        "producer_ladder_has_nonzero_u1_rung_both_anchors",
        computed=1.0 if all(r["c_1_nonzero"] for r in rows) else 0.0,
        expected=1.0,
    )
    # Assertion checked on the RAW mpf values captured during the loop, NOT
    # round-tripped through the formatted strings (which can round small
    # differences down at output_dps).
    wb.add_assertion(
        "c1_matches_tan_alpha_over_2",
        computed=1.0 if all(
            fabs(c1 - c1p) < mpf("1e-30") for c1, c1p in c1_raw
        ) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-alpha-eff-hoefsmit-symbolic-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
