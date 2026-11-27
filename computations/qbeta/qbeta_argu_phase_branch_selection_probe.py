#!/usr/bin/env python3
"""arg(u) phase branch-selection — the LAST seat of the c₃ bar-odd anchor-swing
is a WALL, numerically confirmed at both committed anchors.

Branch: claude/qbeta-argu-phase-branch-selection-2026-07-25, PR #4293.

The exclusion chain (all PROVED, sorry-free Lean):
  #4282 (C1): bar-odd datum = ι-odd antisym off-diagonal, anchor-smooth (4.56 ppm).
  #4288: boost-hyperbola bound ⇒ the S∝|u|² MAGNITUDE channel is anchor-smooth
         (5.5 orders too far from the compact locus; measured swing 0.221 ppm).
localized the residual to the non-perturbative PHASE arg(u) — the branch-selection
of conj:algebraic-geometric-dilog-equivalence.

This probe confirms numerically what QOU/QBeta/ArgUPhaseBranchSelection.lean proves:

  The substrate meridian coordinate is u = 2·log q₀. For the physical q₀ ≥ 1 it is a
  NONNEGATIVE REAL, so arg(u) = 0 at EVERY anchor ⇒ Δ(arg u) = 0. The leading NZ
  imaginary complex-volume S = (√3/2)|u|²·sin(2·arg u) is then IDENTICALLY 0 on the
  real ray (recovering the #3654 amphichirality Im 𝔙(real)=0), and its anchor-swing
  through the phase is EXACTLY 0 — regardless of the (nonzero, unbounded-by-#4288)
  phase-sensitivity ∂S/∂φ|₀ = √3·|u|². The real substrate never MOVES the phase.

  This is the WALL: the phase is a live, maximal-leverage, independent DOF, but it is
  FROZEN at the observable (real-q₀) level. Combined with #4282 + #4288, every
  categorical/geometric DOF at real q₀ supplies zero-or-negligible anchor-swing, so
  c₃'s anchor-dependence is genuinely non-categorical (fibre-level ε=Im(q) / 1/u³
  ladder representation, #3636/#3654).

Consumes committed values only: muon q₀ from the q-pinning witness, proton q₀ from
the qou-substrate constant. auditOnly; no c_k wired; nothing inverts Q_β/CODATA.

Gates (all must pass):
  A  u = 2·log q₀ is real (Im=0) and arg(u)=0 at BOTH anchors  ⇒  Δ(arg u)=0.
  B  S = (√3/2)|u|²·sin(2·arg u) = 0 on the real ray at both anchors (amphichirality).
  C  the phase is maximal-leverage: S at φ=π/4 equals the full (√3/2)|u|².
  D  the phase-channel anchor-swing is EXACTLY 0, while the c₃ target swing is 3.47%.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from mpmath import mp, mpf, log, sqrt, sin, pi, atan2

mp.dps = 60

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WITNESS = HERE / "qbeta-argu-phase-branch-selection.witness.json"

# c₃ committed anchor swing (SETTLED #1580; the target this channel must explain).
C3_SWING_FRAC = mpf("0.0347")  # 3.47 %


def _git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(Path(__file__))],
            cwd=str(ROOT), text=True,
        ).strip()
    except Exception:
        return "unknown"


def _read_muon_q0() -> mpf:
    w = json.loads((ROOT / "computations" / "q-pinning-50-digit.witness.json").read_text())

    def find_q(o):
        if isinstance(o, dict):
            if "q" in o and isinstance(o["q"], str):
                return o["q"]
            for v in o.values():
                r = find_q(v)
                if r:
                    return r
        return None

    return mpf(find_q(w))


def _read_proton_q0() -> mpf:
    sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP
    return Q_MP


def bar_odd(q: mpf) -> mpf:
    return q - 1 / q


def meridian_u(q0: mpf) -> mpf:
    """The substrate meridian NZ coordinate u = 2·log q₀ (real for real q₀)."""
    return 2 * log(q0)


def arg_of_real(x: mpf) -> mpf:
    """arg of the real x embedded in ℂ: atan2(0, x). 0 for x>0, π for x<0."""
    return atan2(mpf(0), x)


def nz_im_volume(r: mpf, phi: mpf) -> mpf:
    """Leading Neumann–Zagier Im 𝔙 = (√3/2)·r²·sin(2φ), r=|u|, φ=arg u."""
    return (sqrt(3) / 2) * r ** 2 * sin(2 * phi)


def main() -> int:
    q_mu = _read_muon_q0()
    q_p = _read_proton_q0()

    results = {}
    for name, q0 in (("muon", q_mu), ("proton", q_p)):
        u = meridian_u(q0)                 # 2 log q0, real
        r = abs(bar_odd(q0))               # |barOdd q0| = |u| lead (#4288 object)
        phi = arg_of_real(u)               # arg(u) — pinned to 0 on the real ray
        results[name] = {
            "q0": mp.nstr(q0, 30),
            "u_2logq0": mp.nstr(u, 30),
            "u_is_real": True,             # real by construction (q0 real)
            "arg_u": mp.nstr(phi, 6),
            "r_barOdd": mp.nstr(r, 12),
            "S_real_ray": mp.nstr(nz_im_volume(r, phi), 6),           # φ=arg u=0 ⇒ 0
            "S_quarter_turn": mp.nstr(nz_im_volume(r, pi / 4), 12),   # φ=π/4 ⇒ full CS
            "S_full_CS_amp": mp.nstr((sqrt(3) / 2) * r ** 2, 12),
            "phase_sensitivity_dSdphi_at0": mp.nstr(sqrt(3) * r ** 2, 12),
        }

    # --- Gate A: arg(u)=0 at both, Δ(arg u)=0 -------------------------------
    d_arg = arg_of_real(meridian_u(q_p)) - arg_of_real(meridian_u(q_mu))
    gate_A = (results["muon"]["arg_u"] == mp.nstr(mpf(0), 6)
              and results["proton"]["arg_u"] == mp.nstr(mpf(0), 6)
              and abs(d_arg) < mpf("1e-50"))

    # --- Gate B: S=0 on the real ray at both (amphichirality) ---------------
    S_mu = nz_im_volume(abs(bar_odd(q_mu)), arg_of_real(meridian_u(q_mu)))
    S_p = nz_im_volume(abs(bar_odd(q_p)), arg_of_real(meridian_u(q_p)))
    gate_B = abs(S_mu) < mpf("1e-50") and abs(S_p) < mpf("1e-50")

    # --- Gate C: phase is maximal-leverage (φ=π/4 ⇒ full CS amplitude) ------
    r_mu = abs(bar_odd(q_mu))
    gate_C = abs(nz_im_volume(r_mu, pi / 4) - (sqrt(3) / 2) * r_mu ** 2) < mpf("1e-50")

    # --- Gate D: phase-channel anchor-swing EXACTLY 0 vs 3.47% target -------
    phase_channel_swing = abs(S_p - S_mu)   # both 0 ⇒ exactly 0
    gate_D = phase_channel_swing < mpf("1e-50")

    # Cross-context: the phase-SENSITIVITY is nonzero & unbounded by #4288, yet
    # multiplied by Δ(arg u)=0. Report it to make the "independent DOF" explicit.
    sens = sqrt(3) * r_mu ** 2

    gates = {"A_arg_zero_both": bool(gate_A),
             "B_S_zero_real_ray": bool(gate_B),
             "C_phase_maximal_leverage": bool(gate_C),
             "D_phase_swing_exactly_zero": bool(gate_D)}
    all_pass = all(gates.values())

    witness = {
        "schema": "qou-probe/v1",
        "id": "qbeta-argu-phase-branch-selection",
        "description": (
            "arg(u) phase branch-selection is FROZEN on the real substrate ray — the "
            "last seat of the c₃ bar-odd anchor-swing is a WALL. u=2·log q₀ is real for "
            "q₀≥1 ⇒ arg(u)=0 at both anchors ⇒ Δ(arg u)=0; the leading NZ Im 𝔙 = "
            "(√3/2)|u|²·sin(2·arg u) is identically 0 on the real ray (amphichirality, "
            "#3654) and its phase-channel anchor-swing is EXACTLY 0, despite a nonzero "
            "unbounded-by-#4288 phase-sensitivity √3|u|². Confirms "
            "QOU/QBeta/ArgUPhaseBranchSelection.lean. auditOnly; no c_k wired."),
        "scriptCommitSha": _git_sha(),
        "verdict": "WALL — phase channel supplies exactly zero anchor-swing at real q₀ "
                   "(scope-(a)); c₃ anchor-dependence is non-categorical (#3636/#3654)",
        "anchors": results,
        "delta_arg_u": mp.nstr(d_arg, 6),
        "phase_channel_anchor_swing": mp.nstr(phase_channel_swing, 6),
        "phase_sensitivity_nonzero": mp.nstr(sens, 12),
        "phase_sensitivity_note": (
            "∂S/∂φ|₀ = √3·|u|² ≠ 0 — the phase is a maximal-leverage independent DOF, "
            "NOT bounded by #4288's boost-hyperbola magnitude ratio. It is a WALL not "
            "because it is bounded, but because Δ(arg u)=0: the real substrate never "
            "moves it."),
        "c3_target_swing_frac": mp.nstr(C3_SWING_FRAC, 6),
        "magnitude_channel_swing_ppm_ref_4288": "0.221",
        "gates": gates,
        "all_pass": all_pass,
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    WITNESS.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")

    print(f"muon   q₀ = {results['muon']['q0']}  u=2logq₀={results['muon']['u_2logq0']} "
          f"arg(u)={results['muon']['arg_u']}  S(real ray)={results['muon']['S_real_ray']}")
    print(f"proton q₀ = {results['proton']['q0']}  u=2logq₀={results['proton']['u_2logq0']} "
          f"arg(u)={results['proton']['arg_u']}  S(real ray)={results['proton']['S_real_ray']}")
    print(f"Δ(arg u) = {mp.nstr(d_arg, 6)}   phase-channel anchor-swing = "
          f"{mp.nstr(phase_channel_swing, 6)}  (target c₃ swing = 3.47%)")
    print(f"phase-sensitivity ∂S/∂φ|₀ = √3|u|² = {mp.nstr(sens, 12)} ≠ 0 "
          f"(independent DOF, unbounded by #4288) — yet ×Δ(arg u)=0")
    print(f"gates: {gates}  all_pass={all_pass}")
    print(f"witness → {WITNESS.relative_to(ROOT)}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
