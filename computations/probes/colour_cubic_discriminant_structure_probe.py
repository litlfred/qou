#!/usr/bin/env python3
"""
Structure of the colour-tube cubic's discriminant locus — the Bring-side
"divergent points", and whether they meet the Borel-side singularity.

Owner question (2026-09-06): *"Where are the divergent points? Are they related
to saddle points on Brings?"* Bean `qou-3qla`; audit
`docs/audits/2026-09-06-resurgence-arc-convention-d-reanalysis.md`.

`docs/picard-lefschetz-plan.md` gives the colour-tube cubic

    c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0

with discriminant `Δ(z) = -(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)`, and
records one fact about its roots: that they are all complex and the pair nearest
`z₀ = 0.104` is `z_c ≈ 0.106 ± 0.937i`. This probe measures four further
structural facts that document does not state, and tests the one identification
the resurgence arc would need.

WHAT IS NEW HERE (measured, exact where claimed exact)

1. **The sextic is PALINDROMIC** — `(16, 24, 35, 50, 35, 24, 16)` reads the same
   backwards. Its roots therefore come in reciprocal pairs `z, 1/z`, verified:
   `|z_small| · |z_large| = 1` to the printed precision.

2. **One conjugate pair lies EXACTLY on the unit circle**, `|z| − 1 = 0`. Those
   roots are a pure phase `e^{±iθ}`, `θ = 2.9166887082513073529`,
   `θ/π = 0.92841085075702107917`.

3. **That phase is NOT a root of unity** at any of the orders a Bring /
   cyclotomic reading would want — for `n ∈ {5, 7, 10, 12, 20, 24}` the index
   `θn/2π` is `2.32, 3.25, 4.64, 5.57, 9.28, 11.14`, none integral. So the
   unit-circle point is a phase but sits at no cyclotomic evaluation point;
   a Habiro-ring reading does not pick it up for free.

4. **The palindromic reduction `w = z + 1/z` gives an honest cubic**,
   `16w³ + 24w² − 13w + 2`, whose **integer discriminant is exactly −80000 =
   −2⁷·5⁴**, with no rational root (checked over `p|2, q|16`). The `5⁴` is
   arithmetically suggestive next to Bring's quintic / icosahedral setting —
   **recorded as an observation, NOT derived, and not used for anything.**

THE NEGATIVE, which is the point of the exercise

Resurgence would have the Borel-plane singularity be a saddle's action. The
corpus's Borel-side datum is the level-1/2 singularity at `ξ = 1/√2` at `q = 1`
(binding kernel Gevrey-1/2, `QOU.Mass.BindingGevreyHalf`). Tested directly
against the simple invariants of `z_c`:

    |z_c|      / (1/√2) = 1.3337
    |z_c|²     / (1/√2) = 1.2578
    Im z_c     / (1/√2) = 1.3253
    Re z_c     / (1/√2) = 0.1497
    |w_cplx|   / (1/√2) = 0.3581

**None is a clean ratio.** Scope-(a): the simple identifications tested do not
hold. This does NOT exclude a connection — the honest test is whether
`ξ = 1/√2` is the *action* `∫λ_SW` along a Picard–Lefschetz thimble from `z_c`,
which needs a definite `λ_SW` and is not computed here. What it does exclude is
the cheap version of the identification, which is what an unasked question
usually dies of.

No float64: every number is `mpmath.mpf` / `mpc`, and the discriminant is exact
integer arithmetic.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

#: Δ(z) = −(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16), docs/picard-lefschetz-plan.md
SEXTIC = [16, 24, 35, 50, 35, 24, 16]

#: Borel-side datum: level-1/2 singularity at q = 1 (Gevrey-1/2 binding kernel).
XI = "1/sqrt(2)"


def main() -> int:
    checks: list[dict] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    # 1. palindromic
    check("palindromic", SEXTIC == SEXTIC[::-1],
          f"coefficients {SEXTIC} read the same backwards")

    roots = mp.polyroots([mp.mpf(c) for c in SEXTIC], maxsteps=300, extraprec=300)
    check("root_count", len(roots) == 6, f"{len(roots)} roots")

    # 2. reciprocal pairing
    by_mod = sorted(roots, key=lambda z: abs(z))
    prod = abs(by_mod[0]) * abs(by_mod[-1])
    check("reciprocal_pairing", abs(prod - 1) < mp.mpf("1e-40"),
          f"|z_min|*|z_max| = {mp.nstr(prod, 25)}")

    # 3. exactly one conjugate pair on the unit circle
    on_circle = [r for r in roots if abs(abs(r) - 1) < mp.mpf("1e-40")]
    check("unit_circle_pair", len(on_circle) == 2,
          f"{len(on_circle)} roots with |z| = 1 (max deviation "
          f"{mp.nstr(max(abs(abs(r))-1 for r in on_circle), 6) if on_circle else 'n/a'})")

    uc = [r for r in on_circle if mp.im(r) > 0][0]
    theta = mp.atan2(mp.im(uc), mp.re(uc))

    # 4. the phase is NOT a root of unity at the orders a Bring reading wants
    orders = (5, 7, 10, 12, 20, 24)
    idx = {n: theta * n / (2 * mp.pi) for n in orders}
    non_integral = all(
        abs(v - mp.nint(v)) > mp.mpf("1e-6") for v in idx.values()
    )
    check("phase_not_root_of_unity", non_integral,
          "theta*n/2pi = " + ", ".join(f"{n}:{mp.nstr(v, 6)}" for n, v in idx.items()))

    # 5. palindromic reduction and its EXACT integer discriminant
    a, b, c, d = 16, 24, -13, 2
    disc = (18 * a * b * c * d - 4 * b ** 3 * d + b ** 2 * c ** 2
            - 4 * a * c ** 3 - 27 * a ** 2 * d ** 2)
    check("reduced_cubic_discriminant", disc == -80000,
          f"disc(16w^3+24w^2-13w+2) = {disc} = -2^7 * 5^4 (exact integer arithmetic)")

    w_real = 2 * mp.cos(theta)
    resid = 16 * w_real ** 3 + 24 * w_real ** 2 - 13 * w_real + 2
    check("reduction_consistent", abs(resid) < mp.mpf("1e-40"),
          f"w = 2cos(theta) = {mp.nstr(w_real, 20)} solves the reduced cubic, "
          f"residual {mp.nstr(abs(resid), 6)}")

    rational = [(p, q) for p in (1, -1, 2, -2) for q in (1, 2, 4, 8, 16)
                if abs(16 * mp.mpf(p) ** 3 / q ** 3 + 24 * mp.mpf(p) ** 2 / q ** 2
                       - 13 * mp.mpf(p) / q + 2) < mp.mpf("1e-40")]
    check("reduced_cubic_irrational", not rational,
          f"no rational root over p|2, q|16 (found {rational})")

    # 6. THE NEGATIVE: xi = 1/sqrt(2) against the simple invariants of z_c
    zc = [r for r in roots if mp.im(r) > 0 and abs(r) < 1][0]
    xi = 1 / mp.sqrt(2)
    wc = [w for w in mp.polyroots([mp.mpf(x) for x in (16, 24, -13, 2)],
                                  maxsteps=300, extraprec=300) if mp.im(w) > 0][0]
    ratios = {
        "abs_zc": abs(zc) / xi,
        "abs_zc_sq": abs(zc) ** 2 / xi,
        "im_zc": mp.im(zc) / xi,
        "re_zc": mp.re(zc) / xi,
        "abs_w_complex": abs(wc) / xi,
    }
    clean = [k for k, v in ratios.items()
             if abs(v - mp.nint(v)) < mp.mpf("1e-8") or abs(1 / v - mp.nint(1 / v)) < mp.mpf("1e-8")]
    check("xi_not_simply_related", not clean,
          "ratios to 1/sqrt(2): "
          + ", ".join(f"{k}={mp.nstr(v, 8)}" for k, v in ratios.items())
          + f" -- clean hits: {clean}")

    n_pass = sum(1 for c in checks if c["pass"])
    for c in checks:
        print(f"[{'PASS' if c['pass'] else 'FAIL'}] {c['check']}: {c['detail']}")
    print(f"\n{n_pass}/{len(checks)} checks pass")

    wb = WitnessBuilder("colour-cubic-discriminant-structure", _script_path=__file__)
    wb.save({
        "description": (
            "Structure of the colour-tube cubic's discriminant locus (the "
            "Bring-side divergent points) and a direct test of the "
            "identification resurgence would need. NEW: the sextic is "
            "palindromic, its roots pair reciprocally, one conjugate pair lies "
            "exactly on the unit circle as a pure phase that is NOT a root of "
            "unity at n in {5,7,10,12,20,24}, and the palindromic reduction "
            "16w^3+24w^2-13w+2 has exact integer discriminant -80000 = -2^7*5^4. "
            "NEGATIVE: xi = 1/sqrt(2), the Borel-side level-1/2 singularity, is "
            "not simply related to any tested invariant of z_c. Scope-(a): the "
            "cheap identification fails; the action integral along a "
            "Picard-Lefschetz thimble was NOT computed and is the honest test."
        ),
        "checks": checks,
        "checks_passed": n_pass,
        "checks_total": len(checks),
        "sextic": SEXTIC,
        "theta": mp.nstr(theta, 30),
        "theta_over_pi": mp.nstr(theta / mp.pi, 30),
        "reduced_cubic": [16, 24, -13, 2],
        "reduced_cubic_discriminant": disc,
        "reduced_cubic_discriminant_factored": "-2^7 * 5^4",
        "z_c": {"re": mp.nstr(mp.re(zc), 30), "im": mp.nstr(mp.im(zc), 30)},
        "xi_borel": XI,
        "xi_ratios": {k: mp.nstr(v, 20) for k, v in ratios.items()},
        "not_computed": (
            "the action integral int lambda_SW along a Picard-Lefschetz thimble "
            "from z_c -- the honest test of whether xi = 1/sqrt(2) is that saddle's action"
        ),
    })
    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
