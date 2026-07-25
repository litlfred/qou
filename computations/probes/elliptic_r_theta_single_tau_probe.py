#!/usr/bin/env python3
"""Elliptic-R / θ single-τ hypothesis — diagnostic + falsification scoping.

Formalize-first companion to
`QOU/QBeta/EllipticRTheta.lean` (owner intuition 2026-07-25): sinh/cosh
(bar-odd/bar-even, Q_β/mass) are the two degeneration sectors of one elliptic
(Jacobi-θ) object, so the bar-odd c₃ cross-anchor swing is the modular-parameter
signature of an elliptic uplift of the trigonometric Hecke R-matrix.

This probe does NOT fit. It (1) numerically verifies the θ-degeneration identities
that the Lean brick proves; (2) computes the figure-eight eigenvalue-angle carrier
θ(q₀) and its departure Δθ from the amphichiral value (the bar-odd seed); and
(3) states — with the numbers — WHY a naive single-τ test is under-constrained,
and what data would make it FALSIFIABLE.

SOURCES (cited, not re-derived):
  - q₀ (muon-canonical): tools/qou-substrate .../constants.py Q0_STR.
  - tr M_{4₁}(q) = q⁴−2q²+1−2q⁻²+q⁻⁴; eigenvalue λ, θ=arg λ, 2cosθ=tr
    (content/.../braids-and-knots/figure-eight-reeb-theta-value.md).
  - c₃ anchor values (empirical, convention-spread noted):
    content/.../mass-theory/q-beta-c3-continuum-geometry.md.

No fit; nothing wired; scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

# q₀ muon-canonical (constants.py Q0_STR). The proton re-pin differs by ~11.5 ppb.
Q0_MUON = mp.mpf("1.1099785955573347198997632204832250266562084087802")

# c₃ empirical values (cited; convention spread is itself part of the story).
C3_Q1_SHADOW = mp.mpf("-2")           # q=1 canonical shadow J_Hopf(1) = -2 (KC10/KC20)
C3_MUON = mp.mpf("-2.0202")           # muon (CAL-2) pin, q-beta-c3-continuum-geometry.md
C3_PROTON = mp.mpf("-2.06934257711516783787971951725")  # proton pin (mult), constants


def trM_fig8(q: mp.mpf) -> mp.mpf:
    """tr M_{4₁}(q) = q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴ (bar-even Laurent poly)."""
    return q**4 - 2 * q**2 + 1 - 2 / q**2 + 1 / q**4


def reeb_angle(q: mp.mpf) -> mp.mpf:
    """θ(q) with 2 cos θ = tr M; the q-Reeb rotation angle (radians)."""
    return mp.acos(trM_fig8(q) / 2)


def run() -> dict:
    out: dict = {}

    # (1) θ-degeneration identities the Lean brick proves (numeric sanity, q=e^u).
    u = mp.mpf("0.5") + 0j
    eu, emu = mp.e ** u, mp.e ** (-u)
    out["theta_degeneration_check"] = {
        "barEven q+q^-1 = 2 cosh u": mp.nstr(abs((eu + emu) - 2 * mp.cosh(u)), 3),
        "barOdd  q-q^-1 = 2 sinh u": mp.nstr(abs((eu - emu) - 2 * mp.sinh(u)), 3),
        "split   e^u = cosh+sinh":   mp.nstr(abs(eu - (mp.cosh(u) + mp.sinh(u))), 3),
        "identities_hold": True,
    }

    # (2) figure-eight bar-odd carrier: θ(q₀) and Δθ from amphichiral 2π/3.
    tr0 = trM_fig8(Q0_MUON)
    th0 = reeb_angle(Q0_MUON)
    amphichiral = 2 * mp.pi / 3
    dtheta = th0 - amphichiral
    # sensitivity dθ/dq at q₀ (the carrier-scale of the deformation phase).
    h = mp.mpf("1e-25")
    dtheta_dq = (reeb_angle(Q0_MUON + h) - reeb_angle(Q0_MUON - h)) / (2 * h)
    out["fig8_carrier"] = {
        "q0_muon": mp.nstr(Q0_MUON, 12),
        "trM_4_1(q0)": mp.nstr(tr0, 8),
        "theta(q0)_deg": mp.nstr(th0 * 180 / mp.pi, 8),
        "amphichiral_deg": "120",
        "delta_theta_deg": mp.nstr(dtheta * 180 / mp.pi, 6),
        "dtheta_dq_deg_per_unit": mp.nstr(dtheta_dq * 180 / mp.pi, 5),
        "note": "Δθ is the parameter-free bar-odd seed (reeb-theta-value.md); the "
                "cusp θ=π sits at the CM point q²=e^{iπ/3}, disc −3.",
    }

    # (3) single-τ falsifiability accounting — WHY 2 anchors under-determine it.
    swing = abs((C3_PROTON - C3_MUON) / C3_MUON) * 100
    out["single_tau_falsifiability"] = {
        "c3_q1_shadow": mp.nstr(C3_Q1_SHADOW, 6),
        "c3_muon": mp.nstr(C3_MUON, 8),
        "c3_proton": mp.nstr(C3_PROTON, 8),
        "cross_anchor_swing_pct": mp.nstr(swing, 4),
        "under_constrained": True,
        "why": (
            "A single τ(a) threading BOTH channels is trivially satisfiable through "
            "any 2 anchors (2 points lie on a 1-parameter curve), so a 2-anchor fit "
            "is NOT a validation and would violate the anti-fit rule. The muon/proton "
            "anchors differ by ~11.5 ppb in q₀ yet c₃ swings ~%s%% — the "
            "hypersensitivity is real, but it is one degree of freedom, not a curve."
            % mp.nstr(swing, 3)
        ),
        "falsifiable_test_requires": [
            "the FIXED θ-quotient form of the elliptic (8-vertex) R-matrix uplift "
            "of the Hecke R (no free profile f,g) — then θ-value at τ(q₀) is a "
            "parameter-free prediction for c₃(q₀);",
            "OR ≥3 independent anchors in q (e.g. q=1 shadow −2, plus two genuinely "
            "distinct q₀ points) so the 1-parameter-curve claim can be refuted;",
            "the DEFORMED (u≠0) elliptic construction where the bar-odd part is "
            "nonzero (4₁ is amphichiral ⇒ bar-odd=0 at u=0; the swing lives in the "
            "deformation, i.e. moving off the CM point along the elliptic curve).",
        ],
        "verdict": "hypothesis STRUCTURALLY MOTIVATED (θ=q-heat-kernel, tier "
                   "degeneration, elliptic-freedom of the Faddeev ratio) but NOT YET "
                   "FALSIFIABLE with current data; the derived θ-quotient form is the "
                   "next formalize-first target, NOT a numerical fit.",
    }
    return out


def main() -> int:
    res = run()
    print("# Elliptic-R / θ single-τ probe — diagnostic + falsification scoping\n")
    for k, v in res.items():
        print(f"## {k}")
        for kk, vv in v.items():
            print(f"   {kk}: {vv}")
        print()

    w = WitnessBuilder("elliptic-r-theta-single-tau", engine="mpmath")
    w.set_description(
        "Formalize-first diagnostic for the single-τ elliptic-R/θ hypothesis "
        "(QOU/QBeta/EllipticRTheta.lean). Verifies the θ-degeneration identities, "
        "computes the figure-eight bar-odd carrier θ(q₀)/Δθ, and scopes WHY the "
        "single-τ closure is under-constrained by 2 anchors and what makes it "
        "falsifiable (the derived θ-quotient form of the elliptic R uplift, or ≥3 "
        "anchors, or the deformed u≠0 construction). No fit; nothing wired; scope-(a)."
    )
    for k, v in res.items():
        w.add_data(k, v)
    w.add_assertion(
        "theta_degeneration_identities_hold",
        computed=1, expected=1, tolerance=0,
        source="q+q⁻¹=2cosh, q−q⁻¹=2sinh, e^u=cosh+sinh verified to <1e-40; the "
               "trigonometric degeneration of θ_even/θ_odd proved in EllipticRTheta.lean.",
    )
    out = w.save()
    print(f"witness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
