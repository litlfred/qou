#!/usr/bin/env python3
"""qbeta_c3_pole_sign_complexification_probe.py

Does the Φ_q pole's OWN sign supply the missing phase? — NO (computed exclusion).

Context. The pole→cusp route (`conj:algebraic-geometric-dilog-equivalence`)
needs a COMPLEX phase to move the Newton flow off the real axis: the literal
real seed flows to the golden branch, Vol = 0, no CS
(`qbeta_c3_barodd_pole_seed_newton_probe.py`, finding A), and the seeding is
anchor-blind (`qbeta_c3_phib_pole_seed_sensitivity_probe.py`). Both prior
probes seeded with the pole MAGNITUDE `q₀^{-(2k+1)}` — but the actual pole of
the compact `Φ_q(x) = ∏(1+q^{2n+1}x)^{-1}` sits at

    x_k = −q₀^{-(2k+1)}          (zero of 1 + q^{2k+1}x — NEGATIVE real),

i.e. it carries the phase π. This probe asks the one derived question the sign
opens: does the principal-branch complexification of the pole itself,

    m² := x_k   ⇒   u_k = log x_k = iπ − (2k+1)·log q₀,

pass the diagonal-crossing gate (`signflip_requires_diagonal_cross`,
`qbeta_udeform_map_constraint_probe.py`: (Re²u−Im²u) must be +ve at muon,
−ve at proton)?

FINDINGS (computed; scope-(a); C14 anti-fit; no c_k wired; m(q₀) NOT fitted):
  A. For every fixed k (0..19), sign[Re²u_k − Im²u_k] is IDENTICAL at the two
     anchors — the family is anchor-blind at the 1e-8 anchor separation, so NO
     fixed-k member can reproduce the measured sign flip
     S(muon) = +0.00968 > 0 > S(proton) = −0.03946. Family excluded, scope-(a).
  B. The leading-form sign boundary is (2k+1) = π/log q₀ ≈ 30.113 at both
     anchors; no odd integer falls between the two anchor values, so no k
     flips between anchors (checked, not assumed).
  C. NUMEROLOGICAL TRAP (flagged, not used): near k = 15 (2k+1 = 31) the
     magnitude κ|Re²u−Im²u| dips to O(S); any per-anchor choice of k to match
     sign or magnitude would be a FIT (two anchors, one integer each = two
     tuned parameters) and is NOT performed.
  D. Reality invariance (the structural upgrade, Lean-proved): a Newton
     iteration on the real-coefficient gluing polynomial started at ANY real
     seed — positive or negative — has all-real iterates, and a convergent
     all-real sequence has a real limit, so it can NEVER reach the cusp shape
     e^{iπ/3} (Im = √3/2 ≠ 0). The prior probes' finding A is thereby a
     scope-(b) exclusion for the whole REAL-seed class (invariant: conjugation
     equivariance + closedness of ℝ), Lean
     `QOU.QBeta.NewtonRealityInvariance` (sorry-free).

VERDICT: the pole's own −1 does not supply the phase. Sharpening of the open
link: the required phase is strictly interior (0 < |arg m²| < π with the
diagonal-crossing anchor asymmetry) — neither the real axis (either sign) nor
the principal branch of the pole's log reaches it. `u(q₀)` stays OPEN.

Lean: QOU/QBeta/NewtonRealityInvariance.lean (this PR).
Companion audits: docs/audits/2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md,
docs/audits/2026-07-26-sdeformed-channel-signflip.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from qou_substrate.precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()  # mp.mp.dps = COMPUTE_DPS (70) — matches witness metadata
KAPPA = mp.sqrt(3) / 4          # |a₂|, cusp modulus τ = −i√3 (A-polynomial)
S_MUON = mp.mpf("0.00968298")   # measured targets (anchor-blind witness)
S_PROTON = mp.mpf("-0.03945936")
K_RANGE = 20


def u_principal(q, k):
    """Principal-branch log of the k-th Φ_q pole x_k = −q^{-(2k+1)}."""
    return mp.mpc(0, mp.pi) - (2 * k + 1) * mp.log(q)


def leading_im_V(u):
    """Corrected NZ leading form Im 𝔙 = (√3/4)(Re²u − Im²u)."""
    return KAPPA * (mp.re(u) ** 2 - mp.im(u) ** 2)


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — does the Φ_q pole's SIGN supply the phase?  (answer: no)")
    print("=" * 78)

    qp, qm = q_at(60), q_muon_at(60)

    wb = WitnessBuilder("qbeta-c3-pole-sign-complexification", engine="mpmath")
    wb.set_description(
        "Tests the one derived candidate the Φ_q pole's own sign opens: prior "
        "pole-seed probes used the pole MAGNITUDE q0^-(2k+1), but the actual "
        "pole of Φ_q is x_k = −q0^-(2k+1) (phase π). Principal-branch "
        "complexification m² := x_k ⇒ u_k = iπ − (2k+1)·log q0 is tested "
        "against the diagonal-crossing gate (corrected NZ leading form "
        "Im 𝔙 = (√3/4)(Re²u−Im²u)). RESULT: for every fixed k the sign is "
        "identical at both anchors (anchor-blind; boundary (2k+1)=π/log q0"
        "≈30.113 crossed by no odd integer between the anchors) ⇒ family "
        "excluded scope-(a); the near-k=15 magnitude dip is flagged as a "
        "numerological trap and NOT used (C14). Reality invariance (Lean "
        "NewtonRealityInvariance, sorry-free) upgrades the real-seed "
        "exclusion to scope-(b): real seeds of EITHER sign have all-real "
        "Newton iterates and cannot reach the cusp e^{iπ/3}. u(q0) stays "
        "OPEN; no c_k wired; nothing fitted."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # [0] the pole location really is negative (definition check, not folklore)
    k0_res = 1 + qm ** (2 * 0 + 1) * (-(qm ** -(2 * 0 + 1)))
    print(f"\n[0] pole definition check: 1 + q^(2k+1)·x_k = {mp.nstr(k0_res, 5)} (k=0)")

    # [1] fixed-k family vs the gate: sign at both anchors, every k
    print("\n[1] principal-branch u_k = iπ − (2k+1)log q₀ vs the diagonal gate:")
    rows, all_same_sign = [], True
    for k in range(K_RANGE):
        lm, lp = leading_im_V(u_principal(qm, k)), leading_im_V(u_principal(qp, k))
        same = (lm > 0) == (lp > 0)
        all_same_sign &= same
        if k in (0, 1, 14, 15, 16, K_RANGE - 1):
            print(f"    k={k:2d}: ImV_lead(muon)={mp.nstr(lm, 6):>14}  "
                  f"(proton)={mp.nstr(lp, 6):>14}  same_sign={same}")
        rows.append({"k": k, "ImV_lead_muon": mp.nstr(lm, 12),
                     "ImV_lead_proton": mp.nstr(lp, 12), "same_sign": bool(same)})

    # [2] boundary check: does any odd integer separate the two anchor values?
    bm, bp = mp.pi / mp.log(qm), mp.pi / mp.log(qp)
    lo, hi = min(bm, bp), max(bm, bp)
    n_lo = int(mp.floor(lo))
    crossing_odd = next((n for n in range(n_lo, n_lo + 3)
                         if n % 2 == 1 and lo < n < hi), None)
    print(f"\n[2] sign boundary (2k+1) = π/log q₀: muon {mp.nstr(bm, 12)}, "
          f"proton {mp.nstr(bp, 12)}")
    print(f"    odd integer strictly between them: {crossing_odd}  (None ⇒ no k flips)")

    # [3] the trap, flagged
    print("\n[3] TRAP (flagged, NOT used): near k=15 the magnitude dips to O(S);")
    print("    choosing k per anchor to chase sign/magnitude would be a fit (C14).")

    # [4] verdict
    flip_measured = S_MUON > 0 > S_PROTON
    excluded = all_same_sign and crossing_odd is None and flip_measured
    print("\n[4] VERDICT: pole sign (phase π, principal branch) does NOT supply the")
    print("    flip — family anchor-blind, excluded scope-(a). Real seeds of either")
    print("    sign are excluded scope-(b) by Lean NewtonRealityInvariance. u(q₀) OPEN.")

    wb.add_data("anchors", {"q_muon": mp.nstr(qm, 30), "q_proton": mp.nstr(qp, 30),
                            "S_muon": mp.nstr(S_MUON, 10), "S_proton": mp.nstr(S_PROTON, 10)})
    wb.add_data("fixed_k_family", rows)
    wb.add_data("sign_boundary", {
        "pi_over_logq_muon": mp.nstr(bm, 20), "pi_over_logq_proton": mp.nstr(bp, 20),
        "odd_integer_between_anchors": crossing_odd})
    wb.add_data("scope", {
        "family_exclusion": "scope-(a): every fixed-k principal-branch member is "
                            "anchor-blind (same sign both anchors); no k flips",
        "real_seed_exclusion": "scope-(b): Lean QOU.QBeta.NewtonRealityInvariance — "
                               "real seeds (either sign) have all-real Newton "
                               "iterates; limit real; cusp Im=√3/2 unreachable",
        "open": "u(q0) — required phase strictly interior, 0 < |arg m²| < π"})
    wb.add_assertion("pole_is_negative_of_magnitude",
                     computed=fmt(mp.fabs(k0_res)), expected=0.0, tolerance=1e-45,
                     source="1 + q^{2k+1}·x_k = 0 at x_k = −q^{-(2k+1)} (Φ_q pole)")
    wb.add_assertion("fixed_k_family_anchor_blind",
                     computed=float(0 if all_same_sign else 1), expected=0.0,
                     tolerance=0.5,
                     source="sign[ImV_lead] identical at both anchors for all k in 0..19")
    wb.add_assertion("no_odd_integer_crosses_boundary",
                     computed=float(0 if crossing_odd is None else 1), expected=0.0,
                     tolerance=0.5,
                     source="no odd (2k+1) strictly between π/log q at the two anchors")
    wb.add_assertion("measured_flip_present",
                     computed=float(1 if flip_measured else 0), expected=1.0,
                     tolerance=0.5,
                     source="S(muon) > 0 > S(proton), the anchor-blind witness targets")
    wb.save()

    print(f"\n  RESULT: {'EXCLUDED (all checks pass)' if excluded else 'CHECK FAILED'}")
    return 0 if excluded else 1


if __name__ == "__main__":
    raise SystemExit(main())
