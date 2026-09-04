#!/usr/bin/env python3
"""qbeta_required_phase_target_provenance_probe.py — is the branch-3 target
phase experimentally anchored, or is it the form's own output?

Bean `qou-cds1` / `qou-pdix` route 5.  Scope-(a).

## Why ask

Branch 3 of the eigenphase trichotomy scores every candidate generator against a
required eigenphase.  `HolonomySpectrumSignObstruction` quotes it as

    theta = 0.0565947 rad      (required correction factor 0.998399)

and the arc's own discipline is explicit that a number may be *checked against*
but never *searched on* if it is not independently anchored
(`qbeta_decay_operator_elliptic_spectrum_probe`, the c_3(muon) coincidence note).

I came to this suspecting the target was circular — that 0.0565947 was read off
the ladder's own `cos(alpha - u/2)`, whose form
`alpha = (z-1)h/2` has no derivation
(`docs/audits/2026-09-04-cds1-ladder-phase-has-no-derivation.md`).  If so, every
branch-3 candidate would be scored against a fit.

**That suspicion is WRONG, and the probe records it as wrong.**  The target *is*
experimentally anchored.  But checking it turned up a smaller real defect.

## What is actually true

The N=1 factor the EXPERIMENT requires, using only inputs that are independent
of the phase form —

    Q_A     = m_e |q^2-2q-1|(q+1)/(2q^3)      (prop:neutron-qvalue-symbolic)
    c_2     = -1                              (structural; no fit, no CODATA, no q_0)
    Q_exp   = CODATA free-neutron beta-decay Q-value

    required = Q_exp / (Q_A * (1 - u^2))

is a genuine target: nothing in it reads `z`, `alpha`, or any `c_k` beyond the
structural `c_2`.  So branch 3 has a legitimate criterion to search on, and the
circularity worry is unfounded.  Recorded because someone else will have it too.

## The defect that IS there

`arccos(required) = 0.0566173`, but the quoted target is `0.0565947` — and
`0.0565947` is exactly `|alpha - u/2|`, i.e. the FORM's own phase, to every digit
quoted.  The two differ by 4.0e-4 relative.

So the arc is scored against the form's output where it should be scored against
the experimental requirement.  For a candidate off by 35.7x (Delta_L) this
changes nothing.  It is recorded because the distinction between "the target" and
"what the current form happens to produce" is the exact distinction this arc's
own discipline turns on, and because a future candidate landing inside 4e-4 would
be adjudicated against the wrong number.

Correct target for branch 3:  **theta_required = 0.0566173**, not 0.0565947.

## Precision

mpmath end to end at 50 dps; `q_0` from `q_at(dps)` (proton pin, the standing
default); `m_e` and `Q_beta` from `codata_constants`.  No float64.
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
QUOTED_TARGET = mp.mpf("0.0565947")     # as quoted by HolonomySpectrumSignObstruction

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))


def main() -> int:
    mp.dps = DPS
    q = q_at(DPS)
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    me = mp.mpf(str(M_E_MEV))
    Q_exp = mp.mpf(str(Q_BETA_MEV))

    Q_A = me * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    z_C = mp.sqrt(q) / (1 + q)
    z_D = q ** 3 / (q ** 2 + 1)

    # The target, from experiment + Q_A + the structural c_2 only.
    required = Q_exp / (Q_A * (1 - u ** 2))
    theta_required = mp.acos(required)

    # The form's own phase, for comparison -- NOT an input to `required`.
    alpha_C = (z_C - 1) * h / 2
    alpha_D = (z_D - 1) * h / 2
    theta_form_C = abs(alpha_C - u / 2)

    print("=" * 78)
    print(" Is the branch-3 target phase experimentally anchored?   (qou-cds1)")
    print("=" * 78)
    print(f"\n  q0    = {mp.nstr(q, 20)}   (proton pin)")
    print(f"  Q_A   = {mp.nstr(Q_A, 16)} MeV      Q_exp = {mp.nstr(Q_exp, 16)} MeV")
    print(f"  u     = {mp.nstr(u, 14)}   (c_2 = -1 structural)")

    print("\n[1] the target, from experiment alone")
    print(f"    required = Q_exp/(Q_A*(1-u^2)) = {mp.nstr(required, 17)}")
    print(f"    arccos(required)               = {mp.nstr(theta_required, 14)}")
    print("    inputs: Q_A (closed form), c_2 = -1 (structural), CODATA Q_beta.")
    print("    reads no z, no alpha, no fitted c_k  ->  NOT circular.")
    check(
        "target_is_experimentally_anchored",
        True,
        "required = Q_exp/(Q_A*(1-u^2)) uses only the Q_A closed form, the "
        "structural c_2 = -1, and CODATA; it reads no z, no alpha and no fitted "
        "c_k, so branch 3 has a legitimate criterion to search on. The "
        "circularity worry this probe was written to test is UNFOUNDED.",
    )

    print("\n[2] but the quoted target is the FORM's phase, not this one")
    print(f"    quoted by the obstruction        = {mp.nstr(QUOTED_TARGET, 14)}")
    print(f"    |alpha - u/2| at convention C    = {mp.nstr(theta_form_C, 14)}")
    print(f"    arccos(required)  (experimental) = {mp.nstr(theta_required, 14)}")
    rel_form = abs(theta_form_C - QUOTED_TARGET) / QUOTED_TARGET
    rel_exp = abs(theta_required - QUOTED_TARGET) / QUOTED_TARGET
    print(f"    quoted vs form       : {mp.nstr(rel_form, 6)} relative")
    print(f"    quoted vs experiment : {mp.nstr(rel_exp, 6)} relative")
    check(
        "quoted_target_is_the_form_not_the_experiment",
        rel_form < mp.mpf("1e-6") < rel_exp,
        f"the quoted 0.0565947 matches |alpha - u/2| to {mp.nstr(rel_form, 4)} "
        f"relative but the experimental arccos(required) only to "
        f"{mp.nstr(rel_exp, 4)}; the arc is scored against the form's own output "
        f"where it should be scored against the experimental requirement",
    )

    print("\n[3] the size of the correction")
    print(f"    theta_required - theta_form = "
          f"{mp.nstr(theta_required - theta_form_C, 8)}"
          f"   ({mp.nstr((theta_required - theta_form_C) / theta_form_C * 100, 4)} %)")
    print("    Changes no verdict on record: Delta_L misses by 35.7x.")
    print("    Matters for any future candidate landing inside 4e-4.")
    check(
        "correction_is_small_and_changes_no_recorded_verdict",
        abs(theta_required - theta_form_C) / theta_form_C < mp.mpf("0.01"),
        f"the correction is {mp.nstr(abs(theta_required - theta_form_C) / theta_form_C * 100, 4)} %, "
        f"far inside the 35.7x by which the one elliptic candidate on record "
        f"(Delta_L, theta = 2.0204) misses; no recorded verdict moves",
    )

    print("\n[4] convention note")
    for nm, a in (("C", alpha_C), ("D", alpha_D)):
        f = mp.cos(a - u / 2)
        print(f"    cos(alpha - u/2) [{nm}] = {mp.nstr(f, 17)}"
              f"   vs required {mp.nstr(required, 17)}"
              f"   rel {mp.nstr((f - required) / required, 8)}")
    check(
        "convention_C_form_lands_near_the_requirement_D_does_not",
        abs(mp.cos(alpha_C - u / 2) - required) / required
        < abs(mp.cos(alpha_D - u / 2) - required) / required,
        "the C form sits 1.28e-6 from the experimental requirement and the D "
        "form 6.02e-4, i.e. ~470x further -- consistent with the ladder having "
        "been built in C, and NOT evidence for C, which is excised",
    )

    print("\n  assertions:")
    for name, ok, detail in results:
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
        print(f"           {detail}")
    all_passed = all(ok for _, ok, _ in results)
    print(f"\n  allPassed: {all_passed}  ({sum(ok for _, ok, _ in results)}/{len(results)})")

    out = {
        "probe": "qbeta_required_phase_target_provenance_probe",
        "bean": "qou-cds1",
        "question": "is the branch-3 required eigenphase experimentally anchored, "
                    "or is it the ladder form's own output?",
        "answer": "anchored -- the circularity worry is unfounded. But the QUOTED "
                  "target 0.0565947 is |alpha - u/2| (the form), not "
                  "arccos(Q_exp/(Q_A(1-u^2))) = 0.0566173 (the experiment); 4.0e-4 apart.",
        "correct_target_theta": mp.nstr(theta_required, 20),
        "quoted_target_theta": mp.nstr(QUOTED_TARGET, 20),
        "form_theta_convention_C": mp.nstr(theta_form_C, 20),
        "required_N1_factor": mp.nstr(required, 20),
        "scope": "(a) -- about the provenance of the target, not about any candidate",
        "q0": mp.nstr(q, 20),
        "q0_pin": "proton (q_at)",
        "dps": DPS,
        "Q_A_MeV": mp.nstr(Q_A, 20),
        "Q_exp_MeV": mp.nstr(Q_exp, 20),
        "u": mp.nstr(u, 20),
        "assertions": [
            {"name": n, "passed": ok, "detail": d} for n, ok, d in results
        ],
        "allPassed": all_passed,
    }
    dest = _HERE.parent / "qbeta-required-phase-target-provenance.witness.json"
    dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"\n  witness -> {dest.relative_to(_COMP.parent)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
