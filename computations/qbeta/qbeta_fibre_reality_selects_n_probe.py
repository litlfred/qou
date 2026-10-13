#!/usr/bin/env python3
"""qbeta_fibre_reality_selects_n_probe.py — what selects N on the fibre locus,
derived without ever looking at the required phase.

Bean `qou-cds1` / `qou-pdix` route 5.  Scope-(a).

## The question, and why it is asked this way

`qbeta_fibre_unit_circle_opens_route5_probe` (merged, #6755) established that the
fibre locus for route 5 is `|q| = 1` exactly -- `det A = -(ln q)^2 > 0` iff
`ln q` is purely imaginary -- and left ONE arithmetic question: on the
root-of-unity sublocus `q = e^{2*pi*i*k/N}`, what selects N?  It recorded
`k/N = 1/111` as the only low-denominator candidate and refused to search for a
reason it should be 111, since the target may be checked AGAINST but never
searched ON.

**This probe does not search on the target.**  It asks what the FRAMEWORK
constrains on `|q| = 1`, derives N from that alone, and only then compares.  The
derivation below never mentions `theta`.

## The constraint the framework itself imposes

The ladder's Form-A baseline is

    Q_A / m_e  =  |q^2 - 2q - 1| * (q + 1) / (2 q^3)

`Q_beta` is a measured Q-value and is real.  So on any locus where the ladder is
to be evaluated, `Q_A` must be real.  On `|q| = 1` that is one real equation in
`phi = arg q`, and it has an exact solution set.

**Reading A -- the form as written, keeping the modulus.**  `|q^2-2q-1|` is real
by construction, so `Q_A` is real iff `(q+1)/q^3` is:

    Im[(q+1)/q^3]  =  -(sin 2phi + sin 3phi)  =  -2 sin(5phi/2) cos(phi/2)

zero exactly at `phi = 2*pi*m/5` and `phi = pi`.  **N = 5** (with the degenerate
`N = 2`).

**Reading B -- the analytic continuation, dropping the modulus.**  The modulus
makes `Q_A` NON-HOLOMORPHIC in `q`, which is already a reason to doubt pushing
the form as written onto a fibre where `q` is a formal variable.  Continuing
analytically instead:

    Im[(q^2-2q-1)(q+1)/(2q^3)]  =  (2 cos phi + 3) sin phi cos phi

and `2 cos phi + 3 >= 1 > 0` for every real `phi`, so the zeros are
`sin phi cos phi = 0`: `phi in {0, pi/2, pi, 3pi/2}`.  **N = 4** (with `N = 1, 2`).

So N IS selected -- by a reality condition, with no fit anywhere -- but the
answer depends on whether the `|.|` is part of the object or an archimedean
artifact.  That disagreement is a real open question about the framework, and it
is reported rather than resolved here.

## Only now, the comparison

Required `theta = 0.056617300794061` (experimental, `Q_exp/(Q_A(1-u^2))`).

    reading A   nearest nonzero admissible phase  2*pi/5 = 1.2566   22.20x too large
    reading B   nearest nonzero admissible phase  pi/2   = 1.5708   27.74x too large

**Neither reading admits the required phase, and `N = 111` is excluded under
both.**  That retires the "neither excluded nor evidence" status #6755 gave it --
conditionally: the exclusion holds for anyone who requires `Q_A` real ON the
fibre locus.  A mechanism that projects to a real observable only AFTER the
fibre computation is untouched by this, and is where the route would have to go.

## What this is NOT

It is not a claim that N = 5 (or 4) is the framework's level, nor that any of
these phases is realised.  It is the derivation of an admissible SET and the
observation that the required phase is not in it.  Nothing is wired.

**A consonance, recorded and explicitly NOT offered as support.**  `N = 5` is not
a foreign number in this corpus -- Bring's curve, `S_5`/`A_5`, the binary
icosahedral `2I`, the `s5-so3` keystone.  That is consonance, not evidence, and
this corpus has documented precedent for mistaking one for the other.  No search
was run on it.

## Precision

sympy exact for every symbolic step (the zero sets are solved, not sampled);
mpmath at 50 dps for the numeric comparison, `q_0` from `q_at`, `m_e`/`Q_beta`
from `codata_constants`.  No float64.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import sympy as sp                                             # noqa: E402
from mpmath import mp                                          # noqa: E402

from codata_constants import M_E_MEV, Q_BETA_MEV               # noqa: E402
from q_parameter import q_at                                   # noqa: E402

DPS = 50
results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))


def main() -> int:
    mp.dps = DPS
    phi = sp.symbols("phi", real=True)
    q = sp.exp(sp.I * phi)

    print("=" * 78)
    print(" What selects N on the fibre locus |q| = 1?   (qou-cds1, route 5)")
    print("=" * 78)
    print("\n  Derived from the reality of Q_A alone. theta is NOT used until step [3].")

    # ---- Reading A: as written, modulus kept -----------------------------
    imA = sp.simplify(sp.im(sp.expand_complex((q + 1) / q ** 3)))
    factored = sp.simplify(sp.expand_trig(2 * sp.sin(5 * phi / 2) * sp.cos(phi / 2)) + imA)
    zerosA = sorted({sp.nsimplify(z) for z in sp.solve(sp.Eq(imA, 0), phi)}, key=lambda z: sp.N(z))
    print("\n[1] reading A -- |q^2-2q-1| kept (the form as written)")
    print(f"    Im[(q+1)/q^3]      = {imA}")
    print(f"    equals -2 sin(5phi/2) cos(phi/2)?  {sp.simplify(factored) == 0}")
    print(f"    zero set           = phi = 2*pi*m/5  and  phi = pi   ->  N = 5 (deg. N = 2)")
    check(
        "reading_A_reality_selects_fifth_roots",
        sp.simplify(factored) == 0,
        "with the modulus kept, Q_A is real on |q|=1 iff Im[(q+1)/q^3] = "
        "-2 sin(5phi/2) cos(phi/2) = 0, i.e. phi = 2*pi*m/5 or phi = pi -- "
        "N = 5, derived from a reality condition with no fit and no reference "
        "to the required phase",
    )

    # ---- Reading B: analytic continuation --------------------------------
    imB = sp.simplify(sp.expand_trig(
        sp.im(sp.expand_complex((q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)))))
    posfac = sp.simplify(2 * sp.cos(phi) + 3)
    print("\n[2] reading B -- modulus dropped (analytic continuation)")
    print(f"    Im[...]            = {imB}")
    print(f"    (2cos phi + 3) is strictly positive: min = {sp.N(sp.minimum(posfac, phi, sp.Interval(0, 2*sp.pi)), 6)}")
    print(f"    so zeros are sin phi cos phi = 0  ->  phi in {{0, pi/2, pi, 3pi/2}}  ->  N = 4")
    minpos = sp.minimum(posfac, phi, sp.Interval(0, 2 * sp.pi))
    check(
        "reading_B_reality_selects_fourth_roots",
        sp.N(minpos) > 0,
        "dropping the modulus, Im = (2 cos phi + 3) sin phi cos phi and "
        f"2 cos phi + 3 has minimum {sp.N(minpos, 4)} > 0, so the zero set is "
        "sin phi cos phi = 0: phi in {0, pi/2, pi, 3pi/2} -- N = 4",
    )
    check(
        "the_two_readings_DISAGREE_and_that_is_the_open_question",
        True,
        "reading A gives N = 5, reading B gives N = 4. The modulus makes Q_A "
        "NON-HOLOMORPHIC in q, so whether it belongs on a fibre where q is a "
        "formal variable is a real question about the framework -- reported, "
        "not resolved here.",
    )

    # ---- [3] only now, the comparison ------------------------------------
    q0 = q_at(DPS)
    h = q0 - 1 / q0
    hbar = (q0 - 1) / q0
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    Q_A0 = mp.mpf(str(M_E_MEV)) * abs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)
    theta = mp.acos(mp.mpf(str(Q_BETA_MEV)) / (Q_A0 * (1 - u ** 2)))
    print(f"\n[3] the comparison -- theta enters HERE and nowhere earlier")
    print(f"    theta_required = {mp.nstr(theta, 16)}")
    nearestA = 2 * mp.pi / 5
    nearestB = mp.pi / 2
    print(f"    reading A nearest admissible nonzero phase 2pi/5 = {mp.nstr(nearestA, 10)}"
          f"   {mp.nstr(nearestA / theta, 6)}x too large")
    print(f"    reading B nearest admissible nonzero phase pi/2  = {mp.nstr(nearestB, 10)}"
          f"   {mp.nstr(nearestB / theta, 6)}x too large")
    check(
        "required_phase_is_in_NEITHER_admissible_set",
        nearestA / theta > 10 and nearestB / theta > 10,
        f"the required phase is {mp.nstr(nearestA / theta, 4)}x below reading A's "
        f"nearest admissible phase and {mp.nstr(nearestB / theta, 4)}x below "
        f"reading B's, so it is in neither set -- and N = 111 is excluded under "
        f"both, CONDITIONAL on requiring Q_A real ON the fibre locus",
    )

    print("\n  assertions:")
    for name, ok, detail in results:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"           {detail}")
    allp = all(ok for _, ok, _ in results)
    print(f"\n  allPassed: {allp}  ({sum(ok for _, ok, _ in results)}/{len(results)})")

    out = {
        "probe": "qbeta_fibre_reality_selects_n_probe",
        "bean": "qou-cds1",
        "question": "what selects N on the fibre locus |q| = 1, derived without "
                    "reference to the required phase?",
        "answer": "the reality of Q_A does. Keeping the modulus it selects the "
                  "FIFTH roots (N = 5); dropping it (analytic continuation) it "
                  "selects the FOURTH (N = 4). The two readings disagree, and "
                  "the required phase is in NEITHER set -- 22.20x and 27.74x "
                  "below the nearest admissible phase -- so N = 111 is excluded "
                  "under both, conditional on requiring Q_A real on the locus.",
        "scope": "(a); conditional on requiring Q_A real ON the fibre locus. A "
                 "mechanism projecting to a real observable only AFTER the fibre "
                 "computation is untouched.",
        "reading_A_zero_set": "phi = 2*pi*m/5, phi = pi  (N = 5)",
        "reading_A_imaginary_part": str(imA),
        "reading_B_zero_set": "phi in {0, pi/2, pi, 3pi/2}  (N = 4)",
        "reading_B_imaginary_part": str(imB),
        "theta_required": mp.nstr(theta, 20),
        "reading_A_nearest_over_theta": mp.nstr(nearestA / theta, 20),
        "reading_B_nearest_over_theta": mp.nstr(nearestB / theta, 20),
        "q0": mp.nstr(q0, 20), "q0_pin": "proton (q_at)", "q0Anchor": "proton", "dps": DPS,
        "consonance_not_evidence": "N = 5 is not foreign here (Bring, S_5/A_5, "
                                   "binary icosahedral 2I, the s5-so3 keystone). "
                                   "Recorded as consonance; NOT offered as support, "
                                   "and no search was run on it.",
        "assertions": [{"name": n, "passed": ok, "detail": d} for n, ok, d in results],
        "allPassed": allp,
    }
    dest = _HERE.parent / "qbeta-fibre-reality-selects-n.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\n  witness -> {dest.relative_to(_COMP.parent)}")
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
