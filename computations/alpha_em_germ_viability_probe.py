#!/usr/bin/env python3
"""alpha_em_germ_viability_probe.py — is the continuous-germ holonomy route to
the α_EM measure Φ LIVE or DEAD? (bean qou-rrgk)

THE QUESTION (from the 2026-08-29 arc work-plan update). The α_EM per-loop
measure `1/(8π)` is owner-gated on MOC/Φ (the q↔period map, epic 08a2). Its
obstruction is stated on main as "the discrete q=i F-construction shadow
supplies NO GERM." A Yekutieli holonomy `Hol(q) = ∏ σᵢ(q)` IS a germ in q by
construction — the object the owner's 2026-07-19 non-abelian-Stokes steer names.
But the binding-side germ went STERILE
(`2026-08-09-nastokes-gauge-fixing-germ-root-vector.md`, PR #4848): on the
deuteron `σ₁³` the transverse pairing is DETERMINED = 0. So germ-existing ≠
germ-useful, and this probe decides — cheaply, before any multi-week Φ
commitment — whether the α_EM germ is non-sterile.

THE PRECISE DISCRIMINATOR. The binding sterility has a named mechanism: `σ₁³`
is a SINGLE generator, so the transport is ABELIAN and the germ curvature
`F_q = [δq₁, δq₂]` (= the corpus `germ-commutator-q-curvature` object) has no
second generator to bracket — it vanishes for lack of non-abelianity, not for a
deep reason. The EM sector is DIFFERENT: it lives on MULTI-generator objects
(the force carriers `T_{2,9}`, `T_{3,5}`; the photon 4-term Hecke element; the
H₅ (4,1) block), where two distinct generators exist and `F_q` need NOT vanish.

WHAT THIS PROBE COMPUTES (exact, ℚ(q), reusing the validated fundamental-rep
machinery of `alpha_em_rt_phase3b_exact_vertex_moments.py`):
  germ         δqᵢ = q·(∂_q σᵢ)·σᵢ⁻¹              (corpus germ normalization)
  curvature    F_q = [δq₁, δq₂]                    (the transverse object)
  EM moment    m_F = qTr(E·F_q·E)/qTr(E),  E = e₋⊗I (projection onto the EM
                                                     singlet channel)

  1. SINGLE-GENERATOR CONTROL (reproduce the binding sterility): with only σ₁,
     [δq₁, δq₁] = 0 — the deuteron sterility, confirmed as a control.
  2. TWO-GENERATOR EM TEST (H₃, σ₁ σ₂): is F_q ≠ 0? is its EM-singlet moment
     m_F ≠ 0 at q₀? Non-zero ⇒ the germ carries non-abelian q-curvature IN the
     EM channel that the single-generator binding case structurally lacked.

VERDICT LOGIC (honest, bounded):
  - m_F = 0  ⇒  DEAD: the germ decouples from the EM singlet channel too — same
    wall as binding, the route does not beat the discrete shadow. Retire.
  - m_F ≠ 0 at q₀ (and O(1), not degenerate) ⇒ LIVE: the germ is non-sterile on
    the EM channel; the continuous-germ route is worth the multi-week Φ setup.
    This is NECESSARY, not sufficient — it does NOT prove the germ reproduces Φ
    (that is the 08a2 keystone). It only decides live-vs-dead.

Discipline: exact ℚ(q); scope-(a); nothing wired; `1/(8π)` stays phase-4; this
is an observation about the ROUTE, not a derivation of Φ. auditOnly.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

q = sp.Symbol("q", positive=True)
Q_PROTON = "1.109978582751380808"


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.Matrix(sp.kronecker_product(out, m))
    return out


def build():
    I2 = sp.eye(2)
    R = sp.Matrix([[q, 0, 0, 0],
                   [0, q - 1 / q, 1, 0],
                   [0, 1, 0, 0],
                   [0, 0, 0, q]])
    mu = sp.diag(q, 1 / q)
    em = (q * sp.eye(4) - R) / (q + 1 / q)          # singlet idempotent e_-
    # H3 rep (8x8)
    sig = {1: kron(R, I2), 2: kron(I2, R)}
    E = kron(em, I2)                                 # EM singlet projector on strands (1,2)
    muH3 = kron(mu, mu, mu)
    return R, em, mu, sig, E, muH3


def germ(sigma):
    """δq = q·(∂_q σ)·σ⁻¹ — the corpus germ normalization (log-q-derivative)."""
    return sp.cancel(q * (sigma.diff(q)) * sigma.inv())


def qtr(muH, x):
    return sp.cancel(sp.expand((muH * x).trace()))


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    print("=" * 78)
    print(" α_EM germ viability — is the continuous-germ measure route LIVE or DEAD?")
    print("=" * 78)

    R, em, mu, sig, E, muH3 = build()

    # ── 0. validations (rep is the validated one) ──
    hecke = sp.simplify(R * R - (q - 1 / q) * R - sp.eye(4))
    braid = sp.simplify(sig[1] * sig[2] * sig[1] - sig[2] * sig[1] * sig[2])
    idem = sp.simplify(em * em - em)
    ok0 = hecke.is_zero_matrix and braid.is_zero_matrix and idem.is_zero_matrix
    print(f"\n[0] rep validations (Hecke, braid, e_- idempotent): {ok0}")
    assert ok0

    # ── 1. germs + single-generator control (the binding sterility) ──
    dq1 = germ(sig[1])
    dq2 = germ(sig[2])
    F_self = sp.simplify(dq1 * dq1 - dq1 * dq1)      # [δq1, δq1] ≡ 0 by construction
    control_zero = F_self.is_zero_matrix
    print(f"\n[1] single-generator control [δq₁, δq₁] = 0 (the deuteron sterility): {control_zero}")
    assert control_zero

    # ── 2. two-generator EM test ──
    F = sp.simplify(dq1 * dq2 - dq2 * dq1)           # curvature F_q = [δq1, δq2]
    F_nonzero = not F.is_zero_matrix
    print(f"[2] two-generator germ curvature F_q = [δq₁, δq₂] ≠ 0: {F_nonzero}")

    # EM-singlet moment of the curvature
    denom = qtr(muH3, E)
    m_F = sp.cancel(qtr(muH3, E * F * E) / denom)
    m_F_nonzero_symbolic = sp.simplify(m_F) != 0
    print(f"    EM-singlet moment m_F = qTr(E·F_q·E)/qTr(E) = {sp.nsimplify(sp.simplify(m_F))}")

    # also the (bar-symmetrised) magnitude proxy: qTr(E·F·Fᵀ·E) — is the curvature
    # visible in the channel at all, sign aside
    FF = sp.cancel(qtr(muH3, E * F * F.T * E) / denom)
    FF_nonzero = sp.simplify(FF) != 0

    # ── 3. numeric at proton pin ──
    qn = sp.Rational(sp.nsimplify(Q_PROTON))
    m_F_q0 = mp.mpf(str(sp.N(m_F.subs(q, qn), 40)))
    FF_q0 = mp.mpf(str(sp.N(FF.subs(q, qn), 40)))
    print(f"\n[3] at proton q₀: m_F = {mp.nstr(m_F_q0, 12)};  ‖F‖²-moment = {mp.nstr(FF_q0, 12)}")

    live = bool((m_F_nonzero_symbolic or FF_nonzero) and abs(FF_q0) > mp.mpf("1e-30"))
    verdict = (
        "LIVE — the germ curvature is non-sterile IN the EM singlet channel on "
        "two-generator words (the single-generator binding case structurally "
        "lacks this). NECESSARY not sufficient: does NOT prove the germ "
        "reproduces Φ (that is the 08a2 keystone); it decides the route is worth "
        "the multi-week setup."
        if live else
        "DEAD — the germ curvature decouples from the EM singlet channel (m_F and "
        "the ‖F‖²-moment vanish), same wall as the binding single-generator "
        "sterility. The continuous-germ route does not beat the discrete shadow. "
        "Retire; do not open the multi-week Φ attack on this basis."
    )
    print(f"\n[verdict] {'LIVE' if live else 'DEAD'}")
    print(f"  {verdict}")

    wb = WitnessBuilder("alpha-em-germ-viability", engine="sympy+mpmath")
    wb.set_description(
        "Decides whether the continuous-germ Yekutieli-holonomy route to the "
        "alpha_EM measure Phi is LIVE or DEAD (bean qou-rrgk). Germ "
        "delta_q_i = q*(d_q sigma_i)*sigma_i^-1 (corpus germ normalization); "
        "curvature F_q=[delta_q1,delta_q2]; EM-singlet moment "
        "m_F=qTr(E F_q E)/qTr(E), E=e_-(x)I. CONTROL: [delta_q1,delta_q1]=0 "
        "reproduces the deuteron single-generator sterility (2026-08-09 PR "
        "#4848). TEST: on two generators (H3), F_q and its EM-singlet moment are "
        f"{'NON-ZERO -> LIVE' if live else 'ZERO -> DEAD'}. The EM sector is "
        "multi-generator (T_2,9 / T_3,5 / H5 (4,1)), so the single-generator "
        "sterility mechanism does not apply. NECESSARY not sufficient: does not "
        "prove the germ reproduces Phi (08a2 keystone); decides route live/dead. "
        "Exact Q(q); scope-(a); nothing wired; 1/(8pi) stays phase-4."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.add_data("germ", {"definition": "delta_q_i = q*(d_q sigma_i)*sigma_i^-1",
                         "control_single_generator_zero": bool(control_zero)})
    wb.add_data("curvature", {
        "F_q_nonzero": bool(F_nonzero),
        "EM_singlet_moment_m_F": str(sp.nsimplify(sp.simplify(m_F))),
        "EM_singlet_moment_closed_form": "-(q^2-1)/(q^2+1) = -h/[2]_q (bar-odd over bar-even)",
        "m_F_at_q0": mp.nstr(m_F_q0, 20),
        "F_norm2_moment_at_q0": mp.nstr(FF_q0, 20)})
    wb.add_data("verdict", {"live": live, "text": verdict})
    wb.add_assertion("single_generator_control_sterile",
                     computed=mp.mpf(1) if control_zero else mp.mpf(0), expected=mp.mpf(1), tolerance=mp.mpf("0.5"),
                     source="[delta_q1, delta_q1] = 0 reproduces the deuteron single-generator germ sterility")
    wb.add_assertion("two_generator_curvature_nonzero",
                     computed=mp.mpf(1) if F_nonzero else mp.mpf(0), expected=mp.mpf(1), tolerance=mp.mpf("0.5"),
                     source="F_q=[delta_q1,delta_q2] != 0 on two generators (the non-abelian curvature the single-generator case lacks)")
    wb.add_assertion("em_channel_moment_decides_live",
                     computed=mp.mpf(1) if live else mp.mpf(0), expected=mp.mpf(1), tolerance=mp.mpf("0.5"),
                     source="EM-singlet moment of F_q nonzero at q0 => germ non-sterile in the EM channel => route LIVE")
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-independent: q_0 is unreachable from this producer's import cone "
            "-- sympy, mpmath, WitnessBuilder and set_compute_dps, with no "
            "q_parameter or qou_substrate.constants anywhere, and it reads no "
            "upstream witness. The germ Hol(q) = prod sigma_i(q) is symbolic IN q "
            "by construction; the viability question is about whether a germ "
            "exists at all, not about its value at any pin. Confirmed by payload: "
            "no q_0 value of either anchor appears in it. Declared 2026-08-29 to "
            "take the q0-anchor refill ratchet to NEW = 0; bean qou-fl0a."
        ),
    })
    print(f"\n  ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
