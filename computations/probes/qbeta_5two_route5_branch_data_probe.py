#!/usr/bin/env python3
"""Route 5 of the 5₂ saddle sum rule: does the integral route actually close,
and what IS the branch data ``b = (-1, +1, +1)``?

Context
-------
Bean ``qou-0yqu``.  The 5₂ saddle sum rule is

    Σⱼ Re(Vⱼ) = -3π²/2,    Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼ·πi)²

with ``yⱼ`` the roots of ``y³ - 2y² + 3y - 1`` and ``b = (-1, +1, +1)``.  It is
verified to 80 dps and **unproved**.

Route 5 rewrites ``Σⱼ Li₂(yⱼ)`` as a single *real* convergent integral, because
``∏ⱼ(1 - yⱼz) = 1 - 2z + 3z² - z³`` is a real polynomial positive on ``[0,1]``.
Four Lean bricks of that landed 2026-08-07 (``prod_one_sub_mul_eq``,
``abs_log_recipCubic_le``, ``intervalIntegrable_log_recipCubic_div``,
``LiTwo_eq_integral_unit``).

This probe tests the two claims that the Lean work leaves open, and one claim
this agent wrote into bean ``qou-0yqu`` that has **not** been checked.

Gates
-----
G1  Σⱼ Log(1 - yⱼz) == log P(z) on (0,1] with NO 2πik correction.
    (The conjugate pair's arguments cancel and the real root contributes a
    positive real, so every principal branch should already be right.)

G2  Σⱼ Li₂(yⱼ) == -∫₀¹ log P(z)/z dz, with Li₂ the principal-branch
    polylogarithm.  This is the identity the Lean spine is aimed at; it needs
    the complex Li₂ at |y₁| = 1.52, which is exactly what Lean cannot yet do.

G3  RETRACTION TEST for a claim this agent wrote into bean qou-0yqu on
    2026-08-07: "the branch data b = (-1,+1,+1) is exactly the 2πik correction
    in log ∏ = Σ log".  G1 decides it.  If G1 shows zero correction, the claim
    is WRONG and must be struck from the bean.

G4  ALTERNATIVE identification of b.  Each root satisfies y² = (1-y)³, so
    2·Log y - 3·Log(1-y) = 2πi·kⱼ for an integer kⱼ.  Is b that k?

G5  Does the sum rule itself reproduce, at working precision, from the
    integral?  Reported as a cross-check, not as a proof.

No fitting: every quantity is parameter-free.  All near-misses are reported.

-- Ref: [manuscript] beans qou-0yqu, qou-gkco; docs/coordination/1ppq-qbeta.md
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 60

TWO_PI_I = 2j * mp.pi
B_CORPUS = (-1, +1, +1)


def roots():
    """Roots of y³ - 2y² + 3y - 1, ordered (y₁ upper-half, y₂ = conj, y₃ real)."""
    rs = mp.polyroots([1, -2, 3, -1], maxsteps=200, extraprec=200)
    real = [r for r in rs if abs(mp.im(r)) < mp.mpf(10) ** -40]
    cplx = [r for r in rs if abs(mp.im(r)) >= mp.mpf(10) ** -40]
    cplx.sort(key=lambda r: -mp.im(r))
    return cplx[0], cplx[1], mp.mpf(mp.re(real[0]))


def recip_cubic(z):
    return 1 - 2 * z + 3 * z**2 - z**3


def gate1_log_additivity(y1, y2, y3):
    """Σⱼ Log(1 - yⱼz) vs log P(z): is there a 2πik correction, or none?"""
    worst = mp.mpf(0)
    worst_z = None
    ks = set()
    for i in range(1, 41):
        z = mp.mpf(i) / 40
        lhs = sum(mp.log(1 - y * z) for y in (y1, y2, y3))
        rhs = mp.log(recip_cubic(z))
        d = lhs - rhs
        k = d / TWO_PI_I
        ks.add(int(mp.nint(mp.re(k))))
        err = abs(d)
        if err > worst:
            worst, worst_z = err, z
    return {
        "gate": "G1",
        "claim": "sum of principal Logs equals log P with NO 2pi i correction",
        "worst_abs_deviation": mp.nstr(worst, 8),
        "worst_at_z": mp.nstr(worst_z, 6) if worst_z is not None else None,
        "integer_corrections_seen": sorted(ks),
        "pass": bool(worst < mp.mpf(10) ** -45),
    }


def gate2_integral_equals_sum(y1, y2, y3):
    """Σⱼ Li₂(yⱼ) vs -∫₀¹ log P(z)/z dz."""
    lhs = sum(mp.polylog(2, y) for y in (y1, y2, y3))
    rhs = -mp.quad(lambda z: mp.log(recip_cubic(z)) / z, [0, 1])
    return {
        "gate": "G2",
        "claim": "sum_j Li2(y_j) == -int_0^1 log P(z)/z dz",
        "lhs_re": mp.nstr(mp.re(lhs), 25),
        "lhs_im": mp.nstr(mp.im(lhs), 8),
        "rhs": mp.nstr(rhs, 25),
        "abs_difference": mp.nstr(abs(lhs - rhs), 8),
        "pass": bool(abs(lhs - rhs) < mp.mpf(10) ** -20),
    }


def gate4_branch_defect(y1, y2, y3):
    """y² = (1-y)³ forces 2 Log y - 3 Log(1-y) = 2πi k. Is k the corpus b?"""
    out = []
    for name, y in (("y1", y1), ("y2", y2), ("y3", mp.mpc(y3))):
        d = 2 * mp.log(y) - 3 * mp.log(1 - y)
        k = d / TWO_PI_I
        out.append(
            {
                "root": name,
                "k_re": mp.nstr(mp.re(k), 12),
                "k_im": mp.nstr(mp.im(k), 8),
                "k_is_integer": bool(abs(k - mp.nint(mp.re(k))) < mp.mpf(10) ** -40),
                "k_rounded": int(mp.nint(mp.re(k))),
            }
        )
    ks = tuple(o["k_rounded"] for o in out)
    return {
        "gate": "G4",
        "claim": "b == k, the branch defect of 2 Log y = 3 Log(1-y)",
        "per_root": out,
        "k_tuple": list(ks),
        "b_corpus": list(B_CORPUS),
        "matches_b": bool(ks == B_CORPUS),
        "matches_b_up_to_sign": bool(tuple(-x for x in ks) == B_CORPUS),
    }


def gate5_sum_rule_cross_check(y1, y2, y3):
    """Reproduce Σⱼ Re Vⱼ = -3π²/2 from the corpus b. Cross-check only."""
    total = mp.mpf(0)
    per = []
    for y, b in zip((y1, y2, mp.mpc(y3)), B_CORPUS):
        V = 3 * mp.polylog(2, y) + (mp.log(y) + b * mp.pi * 1j) ** 2
        per.append(mp.nstr(mp.re(V), 20))
        total += mp.re(V)
    target = -3 * mp.pi**2 / 2
    return {
        "gate": "G5",
        "claim": "sum_j Re(V_j) == -3 pi^2 / 2 (verified, UNPROVED)",
        "per_root_re_V": per,
        "total": mp.nstr(total, 30),
        "target": mp.nstr(target, 30),
        "abs_difference": mp.nstr(abs(total - target), 8),
        "pass": bool(abs(total - target) < mp.mpf(10) ** -30),
    }


def main() -> None:
    y1, y2, y3 = roots()
    g1 = gate1_log_additivity(y1, y2, y3)
    g2 = gate2_integral_equals_sum(y1, y2, y3)
    g4 = gate4_branch_defect(y1, y2, y3)
    g5 = gate5_sum_rule_cross_check(y1, y2, y3)

    # G3 is a verdict on a prior claim, decided by G1.
    g3 = {
        "gate": "G3",
        "prior_claim_under_test": (
            "bean qou-0yqu, 2026-08-07, written by this agent: 'the branch data "
            "b = (-1,+1,+1) is exactly the 2 pi i k correction in log prod = sum log'"
        ),
        "verdict": "REFUTED" if g1["pass"] else "NOT REFUTED",
        "reason": (
            "G1 finds no 2 pi i correction at all in the integrand identity: the "
            "conjugate pair's arguments cancel and the real root contributes a "
            "positive real, so every principal branch is already correct. b "
            "therefore cannot be that correction."
            if g1["pass"]
            else "G1 found a nonzero correction; the claim survives this test."
        ),
        "action_required": (
            "strike the claim from bean qou-0yqu" if g1["pass"] else "none"
        ),
    }

    result = {
        "probe": "qbeta_5two_route5_branch_data_probe",
        "dps": mp.mp.dps,
        "roots": {
            "y1": [mp.nstr(mp.re(y1), 20), mp.nstr(mp.im(y1), 20)],
            "y3": mp.nstr(y3, 20),
            "abs_y1": mp.nstr(abs(y1), 20),
        },
        "gates": [g1, g2, g3, g4, g5],
        "scope": (
            "Numerical verification only. Nothing here proves the sum rule, which "
            "remains verified-to-80-dps and unproved. Scope-(a) throughout: no "
            "ingredient is structurally excluded by any gate below."
        ),
    }
    print(json.dumps(result, indent=2))
    out = Path(__file__).resolve().parents[1] / "qbeta-5two-route5-branch-data.witness.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
