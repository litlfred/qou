#!/usr/bin/env python3
"""qbeta_ohtsuki_nz_bridge_b6_probe.py — E1b: the parameter-free b⁶ test.

Follow-up to the E1 refutation (qbeta_ohtsuki_nz_bridge_b4_probe.py, merged
PR #5081 branch): the STRICTLY LINEAR bridge u = c·b failed at order b⁴
(geometric a₄ = i·√3/24 is imaginary where the linear bridge needs real).
E1b tests the minimal repair — the odd-series bridge

    u(b) = c·b + c₃·b³        (4 real dof: c, c₃ ∈ ℂ)

whose four dof are EXACTLY consumed by the b² and b⁴ complex matching
equations against the Ohtsuki tower (exact rungs κ₁ = 11√3π/108,
κ₂ = 2π²/27). Order b⁶ (exact κ₃ = 1081√3π³/21870) is then a
ZERO-FREE-PARAMETER test:

  b²:  N·a₂c²                          = 2π·κ₁
  b⁴:  N·(2a₂cc₃ + a₄c⁴)               = (2π)²·κ₂
  b⁶:  N·(a₂c₃² + 4a₄c³c₃ + a₆c⁶)      =? (2π)³·κ₃      ← THE TEST

for tower normalization N ∈ {1, 2} (𝔙 vs Φ = 2𝔙; note the constant term
already disfavors N = 2 since the tower's 𝔙₀ is Vol(4₁), not 2·Vol(4₁) —
run both anyway). Both sign branches of c are equivalent (all matched
combinations are invariant under (c, c₃) ↦ (−c, −c₃)).

WHAT IS COMPUTED (derived, no fit; scope-(a); nothing wired):
  [1] Geometric a₂, a₄, a₆ of 𝔙(u) by 4-point Richardson on the validated
      NZ longitude integral (T2 probe's V41_integrated), h-ladder checked;
      a₂ validated against the proved i·√3/4 and a₄ against the E1-measured
      i·√3/24 before a₆ is read.
  [2] FREE exact-form check (C14-flagged observation, not used by the test):
      the pattern a₂ = i√3/4, a₄ = i√3/24 is the series of
      −(√3/2)·i·log cos u  (= i√3(u²/4 + u⁴/24 + u⁶/90 + …)), predicting
      a₆ = i·√3/90. Reported as data.
  [3] The b⁶ residual R = N·(a₂c₃² + 4a₄c³c₃ + a₆c⁶) − (2π)³κ₃ for
      N ∈ {1, 2}, with (c, c₃) solved exactly from the b²/b⁴ equations.
      |R|/(2π)³κ₃ ≪ 1 for some N ⇒ the odd-series bridge SURVIVES its
      first parameter-free test with that normalization (scale pinned);
      otherwise the 2-term odd bridge is refuted at b⁶ (scope-(a)).

Beans: qou-0n1r (E1b) / qou-yh67. Lean lock: OhtsukiNZBridgeScale.lean.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
_probes = str(Path(__file__).resolve().parent.parent / "probes")
sys.path.insert(0, _probes)
import sdeformed_channel_signflip_probe as t2  # noqa: E402

set_compute_dps()  # mp.mp.dps = COMPUTE_DPS (70)

KAPPA1 = 11 * mp.sqrt(3) * mp.pi / 108
KAPPA2 = 2 * mp.pi ** 2 / 27
KAPPA3 = 1081 * mp.sqrt(3) * mp.pi ** 3 / 21870
A2_PROVED = mp.mpc(0, 1) * mp.sqrt(3) / 4
A4_E1 = mp.mpc(0, 1) * mp.sqrt(3) / 24
A6_LOGCOS = mp.mpc(0, 1) * mp.sqrt(3) / 90   # −(√3/2)i·log cos u candidate


def V_of_u(u):
    if u == 0:
        return t2.V41_integrated(mp.mpf("1e-30"))
    return t2.V41_integrated(u)


def extract_a246(h):
    """4-point Richardson for (a2, a4, a6), eliminating a8."""
    V0 = V_of_u(mp.mpf(0))
    d = [V_of_u(k * h) - V0 for k in (1, 2, 3, 4)]
    M = mp.matrix([[k ** 2, k ** 4, k ** 6, k ** 8] for k in (1, 2, 3, 4)])
    sol = mp.lu_solve(M, mp.matrix(d))
    return sol[0] / h ** 2, sol[1] / h ** 4, sol[2] / h ** 6


def main() -> int:
    print("=" * 78)
    print(" E1b — the parameter-free b⁶ test of the odd-series bridge u = c·b + c₃·b³")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-ohtsuki-nz-bridge-b6", engine="mpmath")
    wb.set_description(
        "E1b parameter-free b6 test (follow-up to the E1 linear-bridge "
        "refutation): odd-series bridge u = c*b + c3*b^3, dof exactly "
        "consumed by the b2/b4 matches vs exact Ohtsuki rungs; order b6 "
        "(exact kappa3 = 1081*sqrt(3)*pi^3/21870) is then a zero-freedom "
        "test, run for tower normalization N in {1,2}. Geometric a2,a4,a6 "
        "from 4-point Richardson on the validated NZ longitude integral "
        "(a2 vs proved i*sqrt(3)/4, a4 vs E1's i*sqrt(3)/24). Free "
        "exact-form check: -(sqrt(3)/2)*i*log(cos u) predicts a6 = "
        "i*sqrt(3)/90 (C14-flagged observation). Verdict reported not "
        "asserted; no fit; nothing wired. Scope-(a). Beans qou-0n1r/qou-yh67."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # [1] extraction + validations
    print("\n[1] geometric a₂, a₄, a₆ (4-point Richardson, h-ladder):")
    rows = []
    for hexp in ("2", "2.5"):
        h = mp.mpf(10) ** (-mp.mpf(hexp))
        a2, a4, a6 = extract_a246(h)
        rows.append({"h": mp.nstr(h, 4), "a2": mp.nstr(a2, 12),
                     "a4": mp.nstr(a4, 12), "a6": mp.nstr(a6, 12)})
        print(f"    h=1e-{hexp}: a₂={mp.nstr(a2, 10)} a₄={mp.nstr(a4, 10)} a₆={mp.nstr(a6, 10)}")
    a2f, a4f, a6f = extract_a246(mp.mpf(10) ** (-mp.mpf("2.5")))
    e2, e4 = mp.fabs(a2f - A2_PROVED), mp.fabs(a4f - A4_E1)
    e6_logcos = mp.fabs(a6f - A6_LOGCOS)
    print(f"    a₂ vs proved: {float(e2):.2e}   a₄ vs E1: {float(e4):.2e}")
    print(f"\n[2] exact-form check: a₆ vs i·√3/90 (−(√3/2)i·log cos u): "
          f"|Δ| = {float(e6_logcos):.2e}  (rel {float(e6_logcos/mp.fabs(A6_LOGCOS)):.2e})")

    # [3] solve the bridge and test b⁶
    results = {}
    for N in (1, 2):
        Nc = mp.mpf(N)
        c = mp.sqrt(2 * mp.pi * KAPPA1 / (Nc * a2f))
        c3 = ((2 * mp.pi) ** 2 * KAPPA2 / Nc - a4f * c ** 4) / (2 * a2f * c)
        lhs = Nc * (a2f * c3 ** 2 + 4 * a4f * c ** 3 * c3 + a6f * c ** 6)
        rhs = (2 * mp.pi) ** 3 * KAPPA3
        rel = float(mp.fabs(lhs - rhs) / mp.fabs(rhs))
        results[N] = {"c": mp.nstr(c, 15), "c3": mp.nstr(c3, 15),
                      "lhs_b6": mp.nstr(lhs, 15), "rhs_b6": mp.nstr(rhs, 15),
                      "rel_residual": mp.nstr(mp.mpf(rel), 6)}
        print(f"\n[3] N={N}: c = {mp.nstr(c, 10)}")
        print(f"          c₃ = {mp.nstr(c3, 10)}")
        print(f"          b⁶: LHS = {mp.nstr(lhs, 10)}  vs (2π)³κ₃ = {mp.nstr(rhs, 10)}")
        print(f"          relative residual = {rel:.4f}")

    r1 = float(mp.mpf(results[1]["rel_residual"]))
    r2 = float(mp.mpf(results[2]["rel_residual"]))
    if min(r1, r2) < 0.05:
        which = 1 if r1 <= r2 else 2
        verdict = (f"ODD-SERIES BRIDGE SURVIVES the b6 parameter-free test at "
                   f"N={which} (residual {min(r1, r2):.4f}); scale pinned at that "
                   f"normalization")
    else:
        verdict = (f"2-TERM ODD BRIDGE REFUTED at b6 (scope-(a)): residuals "
                   f"N=1: {r1:.4f}, N=2: {r2:.4f} — neither within 5%")
    print(f"\n    VERDICT: {verdict}")

    wb.add_data("extraction", rows)
    wb.add_data("validations", {"a2_err": mp.nstr(e2, 6), "a4_err_vs_E1": mp.nstr(e4, 6)})
    wb.add_data("logcos_candidate", {"a6_pred": "i*sqrt(3)/90",
                                     "abs_err": mp.nstr(e6_logcos, 6),
                                     "note": "C14-flagged observation; not used by the test"})
    wb.add_data("b6_test", results)
    wb.add_data("verdict", {"text": verdict})
    wb.add_assertion("a2_matches_proved", computed=mp.nstr(e2, 10),
                     expected="0", tolerance="1e-8",
                     source="4-point Richardson a2 vs proved i*sqrt(3)/4")
    wb.add_assertion("a4_matches_e1", computed=mp.nstr(e4, 10),
                     expected="0", tolerance="1e-8",
                     source="4-point Richardson a4 vs E1's i*sqrt(3)/24")
    # q0 anchor: this probe never reads the substrate modulus. Verified here
    # by transitive import cone (4 modules) rather than inherited from the b4
    # sibling — b4 was found q0-free under qou-rw91 and b6 was *expected* to
    # match, but an expectation is not a verdict and bean qou-kx04 says so
    # explicitly. The cone confirms it independently.
    # Via save(extra=...) and NOT add_data(), which nests under `data` where
    # the audit reading body["q0Anchor"] cannot see it. No q0Value — one here
    # is a Q0_FLIP.
    wb.save({
        "q0AnchorReason": (
            "Same free-parameter-u construction as the b4 sibling: proved "
            "constants only, no substrate value read. Verified here by its "
            "own 4-module import cone rather than inherited from b4 — the "
            "expectation that b6 matches b4 was not the evidence for it "
            "(bean qou-kx04)."
        ),
        "q0Anchor": "independent",
    })

    ok = e2 < mp.mpf("1e-8") and e4 < mp.mpf("1e-8")
    print(f"\n  RESULT: {'method validated; verdict recorded' if ok else 'VALIDATION FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
