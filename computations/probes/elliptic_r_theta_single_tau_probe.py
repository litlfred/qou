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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# q₀ muon-canonical (constants.py Q0_STR). The proton re-pin differs by ~11.5 ppb.
# q0 read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). It was the
# literal 1.1099785955573... -- the RETIRED self-certified muon pin A,
# superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. There is
# no comparison leg here, so the 2026-08-30 owner ruling puts this producer
# on the PROTON default; the pin moves 11.54 ppb. `q_parameter`, not
# `qou_substrate.constants`, so the witness resolves its anchor stamp.
# The NAME Q0_MUON is kept so its call sites stay legible; it now holds the
# proton pin, which is what this producer computes at.
Q0_MUON = Q_MP

# c₃ empirical values (cited; convention spread is itself part of the story).
C3_Q1_SHADOW = mp.mpf("-2")           # q=1 canonical shadow J_Hopf(1) = -2 (KC10/KC20)
C3_MUON = mp.mpf("-2.0202")           # muon (CAL-2) pin, q-beta-c3-continuum-geometry.md
C3_PROTON = mp.mpf("-2.06934257711516783787971951725")  # proton pin (mult), constants


# The bound the θ-degeneration source string has always quoted ("verified to
# <1e-40"). Named here so the printed table, the witness assertion and the
# prose all read the same number instead of restating it.
THETA_RESIDUAL_TOL = mp.mpf("1e-40")


def trM_fig8(q: mp.mpf) -> mp.mpf:
    """tr M_{4₁}(q) = q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴ (bar-even Laurent poly)."""
    return q**4 - 2 * q**2 + 1 - 2 / q**2 + 1 / q**4


def reeb_angle(q: mp.mpf) -> mp.mpf:
    """θ(q) with 2 cos θ = tr M; the q-Reeb rotation angle (radians)."""
    return mp.acos(trM_fig8(q) / 2)


def run() -> dict:
    out: dict = {}

    # (1) θ-degeneration identities the Lean brick proves (numeric sanity, q=e^u).
    # The three residuals are named rather than inlined so `main()` can assert
    # the WORST of them. Previously they were computed, rounded to 3 figures
    # into the strings below, and then thrown away: `identities_hold` was the
    # literal `True`, and the witness assertion was `computed=1, expected=1`.
    # Nothing downstream could see a broken identity — the residuals were
    # narration, not a check.
    u = mp.mpf("0.5") + 0j
    eu, emu = mp.e ** u, mp.e ** (-u)
    r_even = abs((eu + emu) - 2 * mp.cosh(u))
    r_odd = abs((eu - emu) - 2 * mp.sinh(u))
    r_split = abs(eu - (mp.cosh(u) + mp.sinh(u)))
    r_max = max(r_even, r_odd, r_split)
    out["theta_degeneration_check"] = {
        "barEven q+q^-1 = 2 cosh u": mp.nstr(r_even, 3),
        "barOdd  q-q^-1 = 2 sinh u": mp.nstr(r_odd, 3),
        "split   e^u = cosh+sinh":   mp.nstr(r_split, 3),
        # Full-width worst residual: the number the witness assertion reads.
        # 3-figure strings above are for the printed table only.
        "max_abs_residual": mp.nstr(r_max, 12),
        "residual_tolerance": mp.nstr(THETA_RESIDUAL_TOL, 3),
        "identities_hold": bool(r_max < THETA_RESIDUAL_TOL),
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

    # (2b) QUANTITATIVE CHECK — the Faddeev-period-lattice nome is too small (scope-a).
    # τ = 1/b² is the modular parameter of the Faddeev freedom lattice ⟨ib, i/b⟩
    # (faddeev_modular_parameter). Faddeev convention q = e^{iπb²} ⇒ b² = ln q₀/(iπ)
    # at real q₀ > 1, so τ = 1/b² = iπ/ln q₀ is far up the imaginary axis and the
    # lattice sits DEEP in the τ→i∞ (trigonometric) degeneration.
    lnq = mp.log(Q0_MUON)
    b2 = lnq / (1j * mp.pi)
    tau = 1 / b2
    nome = abs(mp.e ** (2j * mp.pi * tau))
    dual_nome = abs(mp.e ** (1j * mp.pi * tau))
    out["faddeev_lattice_nome_check"] = {
        "tau_eq_1_over_b2": mp.nstr(tau, 6),
        "nome_e^{2πiτ}": mp.nstr(nome, 4),
        "dual_nome_e^{iπτ}": mp.nstr(dual_nome, 4),
        "c3_swing": "2.43e-2",
        "verdict_scope_a": (
            "REFUTED (scope-a): the c₃ swing is NOT the elliptic correction of the "
            "Faddeev uniqueness-ratio period lattice ⟨ib, i/b⟩. Its nome at the "
            "substrate is ~1e-42 to ~1e-83 — 40+ orders of magnitude below the "
            "2.4e-2 swing. This is WHY sinh/cosh (the trigonometric degeneration) "
            "already works so well: at real q₀ the Faddeev lattice IS at τ→i∞."
        ),
        "redirect": (
            "If the swing is elliptic at all, the relevant elliptic structure is the "
            "GEOMETRIC one — the figure-eight A-polynomial / holonomy curve at the CM "
            "point q²=e^{iπ/3} (disc −3, j=0), whose modular parameter is O(1), NOT "
            "the Faddeev period lattice. The elliptic-freedom result (PR #4155) is a "
            "different (uniqueness) elliptic structure and does not carry the swing."
        ),
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
    # Was `computed=1, expected=1` — a pass for any state of the identities,
    # including all three failing. The source string already named the real
    # check ("verified to <1e-40"), so run it: the assertion now carries the
    # worst of the three residuals against zero at exactly that bound. Break
    # any of q+q⁻¹=2cosh u, q−q⁻¹=2sinh u, e^u=cosh u+sinh u and the residual
    # jumps to O(1) and the witness goes red.
    w.add_assertion(
        "theta_degeneration_identities_hold",
        computed=res["theta_degeneration_check"]["max_abs_residual"],
        expected="0",
        tolerance=mp.nstr(THETA_RESIDUAL_TOL, 3),
        source="max |residual| over q+q⁻¹−2cosh u, q−q⁻¹−2sinh u, "
               "e^u−(cosh u+sinh u) at u=1/2, computed at the module dps; the "
               "trigonometric degeneration of θ_even/θ_odd proved in EllipticRTheta.lean.",
    )
    out = w.save()
    print(f"witness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
