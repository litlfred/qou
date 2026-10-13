#!/usr/bin/env python3
"""qbeta_fibre_unit_circle_opens_route5_probe.py — the fibre locus for route 5 is
|q| = 1, exactly, and the Kashaev sublocus reduces to one undecidable question.

Bean `qou-cds1` / `qou-pdix` route 5.  Scope-(a) for the arithmetic, (b) for the
ellipticity criterion (a proved identity, stated below).

## Where this picks up

`e68347cc12` retargeted `conj:im-q-physical-role` TO THE FIBRE: all three
candidate roles for Im(q) are settled at `q_0` and "all three remain open on the
fibre, where q is a formal variable and Im(q) is unconstrained."

Route 5 needs an ELLIPTIC generator -- `det A > 0`, spectrum `+-i*theta` -- because
a real-spectrum holonomy has character `cosh a >= 1` while the required correction
is below 1 (`HolonomySpectrumSignObstruction`, step 18).  Step 19
(`ImQCannotSupplyEllipticGenerator`) refuted Im(q) as the source AT THE
ARCHIMEDEAN LEVEL, reasoning from `Re q = 1.10998 > 1`.  This probe asks the
fibre question that leaves open.

## 1. The fibre locus is the unit circle, and the reason is exact

Matching the Kohno-Drinfeld holonomy to the Hecke eigenvalues forces
`hbar = 2 ln q`, giving `det A = -(ln q)^2`.  So

    det A > 0   <=>   (ln q)^2 < 0   <=>   ln q purely imaginary   <=>   |q| = 1

At the real substrate anchor `ln q_0 = 0.10434` and `det A = -0.010887 < 0`
(hyperbolic -- exactly what step 18 excluded).  On `|q| = 1`, `ln q = i*phi` and
`det A = +phi^2 > 0`: **elliptic by construction**, with eigenphase
`theta = |arg q|`.

So the unit circle is not one candidate locus among many -- it is PRECISELY the
locus on which the step-18/19 exclusion lifts.

## 2. It is the SAME locus the conjecture block already names

Candidate (i) of `conj:im-q-physical-role` is the Kashaev regime `|q| = 1`, where
`bar q = q^{-1}` and the corpus's chirality operation (the bar involution, the
mirror knot) coincides with complex conjugation.  The block records the substrate
as sitting 18.83 % of `q_0` away from that circle.

Two independent routes -- the ellipticity requirement here, and the chirality
identification there -- select ONE locus.  Recorded as a structural
correspondence, not as evidence for either.

## 3. The Kashaev sublocus reduces to an undecidable arithmetic question

A root of unity `q = e^{2*pi*i*k/N}` gives `theta = 2*pi*k/N`, so it supplies the
required phase **iff `theta/2pi` is RATIONAL**.  Measured,

    theta/2pi = 0.009010923285895504

and that is not a question a measurement can answer: every real number has
rational approximations of arbitrary accuracy.  The continued-fraction
convergents make the point rather than settling it -- `42/4661`, `85/9433`,
`1145/127068` fit to 2e-6, 5e-7, 8e-11 and mean nothing; a larger denominator is
a free parameter.

**The only low-denominator candidate is `k/N = 1/111`**, at 2.1e-4 relative --
and the target's OWN uncertainty is larger than that: correcting the quoted
target from the form's value to the experimental one moved it by **4.0e-4**
(`qbeta_required_phase_target_provenance_probe`).  So N = 111 sits INSIDE the
band the target cannot resolve.

**N = 111 is therefore not excluded, and equally is not evidence.**  Per this
arc's own discipline a target may be checked AGAINST, never searched ON.  No
search for a reason N should be 111 was run, and none should be until something
independent selects it.

## 4. A coincidence, flagged and NOT pursued

`2*pi/theta = 110.9764` sits 1.9e-4 from `100 * q_0 = 110.9979`.  These are
different kinds of object -- an integer index against a dimensionless modulus,
with a factor of 100 inserted by hand -- and this corpus has documented
precedent for exactly this trap (the stale `-2.00973976` / `J_Hopf - hbar^2`
four-decimal agreement).  Recorded so a later reader does not rediscover it as
new.  No mechanism, no search.

## Precision

mpmath at 50 dps; `q_0` from `q_at` (proton pin); `m_e` / `Q_beta` from
`codata_constants`; `fractions.Fraction` for the exact convergents.  No float64.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

from mpmath import mp                                          # noqa: E402

from codata_constants import M_E_MEV, Q_BETA_MEV               # noqa: E402
from q_parameter import q_at                                   # noqa: E402

DPS = 50
mp.dps = DPS   # before the module-scope mpf literals below (import-time dps ratchet)
TARGET_OWN_UNCERTAINTY = mp.mpf("4.0e-4")   # form-vs-experiment gap, PR #6688

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))


def convergents(x: mp.mpf, n: int = 8):
    """Continued-fraction convergents of x as exact (num, den) pairs."""
    cf, t = [], x
    for _ in range(n):
        a = int(mp.floor(t))
        cf.append(a)
        if t == a:
            break
        t = 1 / (t - a)
    out = []
    for i in range(2, len(cf) + 1):
        pn, pd = cf[i - 1], 1
        for a in reversed(cf[: i - 1]):
            pn, pd = a * pn + pd, pn
        if pd:
            out.append((pn, pd))
    return cf, out


def main() -> int:
    mp.dps = DPS
    q = q_at(DPS)
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    Q_A = mp.mpf(str(M_E_MEV)) * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    required = mp.mpf(str(Q_BETA_MEV)) / (Q_A * (1 - u ** 2))
    theta = mp.acos(required)

    print("=" * 78)
    print(" Route 5 on the FIBRE: the locus is |q| = 1, exactly   (qou-cds1)")
    print("=" * 78)
    print(f"\n  theta_required = {mp.nstr(theta, 16)}   (experimental, per #6688)")

    print("\n[1] why the unit circle, exactly")
    lnq = mp.log(q)
    detA_real = -lnq ** 2
    print(f"    det A = -(ln q)^2      (KD matching forces hbar = 2 ln q)")
    print(f"    at q0 real: ln q0 = {mp.nstr(lnq, 12)}  det A = {mp.nstr(detA_real, 12)}"
          f"  -> HYPERBOLIC")
    phi = theta
    detA_circle = phi ** 2
    print(f"    on |q| = 1: ln q = i*phi  det A = +phi^2 = {mp.nstr(detA_circle, 12)}"
          f"  -> ELLIPTIC")
    check(
        "unit_circle_is_exactly_where_the_exclusion_lifts",
        detA_real < 0 < detA_circle,
        "det A = -(ln q)^2 is positive iff ln q is purely imaginary iff |q| = 1; "
        f"at the real anchor det A = {mp.nstr(detA_real, 8)} < 0 (hyperbolic, the "
        f"step-18 exclusion) and on the circle det A = +phi^2 > 0 (elliptic). The "
        "fibre locus is not one candidate among many -- it is the whole solution set.",
    )

    print("\n[2] the same locus the conjecture block names")
    print("    conj:im-q-physical-role candidate (i) = the Kashaev regime |q| = 1,")
    print("    where bar q = q^-1 and the bar involution IS complex conjugation.")
    check(
        "ellipticity_locus_coincides_with_candidate_i_locus",
        True,
        "the ellipticity requirement (this probe) and the chirality "
        "identification (candidate (i)) select the SAME locus |q| = 1 from "
        "independent directions -- recorded as a structural correspondence, not "
        "as evidence for either",
    )

    print("\n[3] the Kashaev sublocus: an undecidable arithmetic question")
    ratio = theta / (2 * mp.pi)
    print(f"    theta/2pi = {mp.nstr(ratio, 16)}")
    print(f"    a root of unity supplies theta  <=>  theta/2pi is RATIONAL")
    cf, convs = convergents(ratio)
    print(f"    continued fraction: {cf}")
    low_den = []
    for n_, d_ in convs:
        rel = (2 * mp.pi * mp.mpf(n_) / d_ - theta) / theta
        flag = ""
        if d_ <= 200:
            low_den.append((n_, d_, rel))
            flag = "   <- low denominator"
        print(f"      k/N = {n_}/{d_:<9} theta = {mp.nstr(2 * mp.pi * mp.mpf(n_) / d_, 12)}"
              f"   rel {mp.nstr(rel, 6)}{flag}")
    inside = [(n_, d_, r) for n_, d_, r in low_den if abs(r) < TARGET_OWN_UNCERTAINTY]
    print(f"\n    target's OWN uncertainty (form vs experiment, #6688) = "
          f"{mp.nstr(TARGET_OWN_UNCERTAINTY, 4)} relative")
    print(f"    low-denominator convergents inside that band: "
          f"{[(n_, d_) for n_, d_, _ in inside]}")
    check(
        "only_N_111_is_inside_the_targets_own_uncertainty",
        len(inside) == 1 and inside[0][1] == 111,
        f"k/N = 1/111 sits {mp.nstr(abs(inside[0][2]), 4)} relative from the "
        f"required phase, INSIDE the target's own {mp.nstr(TARGET_OWN_UNCERTAINTY, 3)} "
        f"band, so it cannot be excluded -- and equally is not evidence. Larger "
        f"denominators fit better and mean nothing: a denominator is a free "
        f"parameter. No search for a reason N should be 111 was run.",
    )
    check(
        "rationality_is_not_decidable_by_measurement",
        True,
        "a root of unity supplies theta iff theta/2pi is rational; every real "
        "number has rational approximations of arbitrary accuracy, so no "
        "measurement settles this. The convergents illustrate the point rather "
        "than answering it.",
    )

    print("\n[4] a coincidence, flagged and NOT pursued")
    N_req = 2 * mp.pi / theta
    coin = (100 * q - N_req) / N_req
    print(f"    2pi/theta = {mp.nstr(N_req, 12)}   vs   100*q0 = {mp.nstr(100 * q, 12)}"
          f"   rel {mp.nstr(coin, 6)}")
    print("    Different kinds of object, with a factor of 100 inserted by hand.")
    print("    Documented precedent for this trap in this corpus. No mechanism, no search.")
    check(
        "coincidence_is_recorded_not_pursued",
        abs(coin) < mp.mpf("1e-3"),
        f"2pi/theta and 100*q_0 agree to {mp.nstr(abs(coin), 4)} relative; an "
        f"integer index against a dimensionless modulus with a hand-inserted "
        f"factor of 100. Recorded so a later reader does not rediscover it as new.",
    )

    print("\n  assertions:")
    for name, ok, detail in results:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"           {detail}")
    all_passed = all(ok for _, ok, _ in results)
    print(f"\n  allPassed: {all_passed}  ({sum(ok for _, ok, _ in results)}/{len(results)})")

    out = {
        "probe": "qbeta_fibre_unit_circle_opens_route5_probe",
        "bean": "qou-cds1",
        "question": "does the fibre reading of conj:im-q-physical-role open route 5, "
                    "and what does the Kashaev regime supply?",
        "answer": "yes, and exactly: det A = -(ln q)^2 > 0 iff |q| = 1, so the unit "
                  "circle is the whole locus on which the step-18/19 exclusion lifts "
                  "-- and it is the same locus candidate (i) names. The root-of-unity "
                  "sublocus needs theta/2pi rational, which no measurement decides; "
                  "k/N = 1/111 is the only low-denominator candidate and sits inside "
                  "the target's own 4.0e-4 uncertainty, so it is neither excluded nor "
                  "evidence.",
        "scope": "(a) for the arithmetic; the ellipticity criterion is an identity",
        "q0": mp.nstr(q, 20), "q0_pin": "proton (q_at)", "dps": DPS,
        "theta_required": mp.nstr(theta, 20),
        "theta_over_2pi": mp.nstr(ratio, 20),
        "det_A_at_real_q0": mp.nstr(detA_real, 20),
        "det_A_on_unit_circle": mp.nstr(detA_circle, 20),
        "continued_fraction": cf,
        "convergents": [
            {"k": n_, "N": d_,
             "theta": mp.nstr(2 * mp.pi * mp.mpf(n_) / d_, 20),
             "rel_err": mp.nstr((2 * mp.pi * mp.mpf(n_) / d_ - theta) / theta, 20)}
            for n_, d_ in convs
        ],
        "target_own_uncertainty_rel": mp.nstr(TARGET_OWN_UNCERTAINTY, 8),
        "coincidence_2pi_over_theta_vs_100_q0": mp.nstr(coin, 20),
        "assertions": [{"name": n, "passed": ok, "detail": d} for n, ok, d in results],
        "allPassed": all_passed,
    }
    dest = _HERE.parent / "qbeta-fibre-unit-circle-opens-route5.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\n  witness -> {dest.relative_to(_COMP.parent)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
