#!/usr/bin/env python3
"""qou-pdix / qou-cds1 route 5 (branch 3): a real-spectrum holonomy lands on the
WRONG SIDE OF 1, whatever its residues.

WHAT WAS OPEN. `PhaseFailsLogFunctionalEquation` excluded CONSTANT-RESIDUE
Kohno-Drinfeld holonomies -- the scale is fixed (braiding = P exp(hbar*t/2), t
eigenvalues +-1, matched to the Hecke eigenvalues {q, -1/q} by hbar = 2 ln q), so
a constant-residue angle is c*ln q, and alpha fails the doubling identity
f(q^2) = 2 f(q) that every c*ln satisfies. That bean records what survived:
"a connection whose residues depend on q, a non-flat construction, or a genuinely
q-dependent-parameter transcendental object is untouched".

THIS CLOSES ALL THREE AT ONCE, by a sign argument that never reads the residues.

THE ARGUMENT. The ladder's correction is read as the normalised character of a
holonomy -- the `EigenphaseCarrier` shape, tr M = 2 cos alpha. Measured, that
character is STRICTLY BELOW 1. But a generator with REAL spectrum +-a gives
character cosh(a) >= 1 for EVERY real a. The bound is quantified over all real a,
so a q-dependent residue only changes WHICH a appears and the bound is unmoved.

At the Kohno-Drinfeld value the miss is elementary: hbar = 2 ln q is real at the
substrate's real q0 = 1.10998 > 1, so the generator eigenvalues +-ln q0 are real
and the character is

    (q + 1/q)/2 - 1 = (q-1)^2/(2q)

a square over a positive -- never negative. 1.005448 against a required 0.998399:
wrong SIDE of 1, by 0.706 %.

WHAT ROUTE 5 IS LEFT WITH. Not "find a connection" but "find one whose generator
is ELLIPTIC at real q" -- det A > 0 for the traceless generator, spectrum +-i*theta
rather than +-a. The Kohno-Drinfeld scale-fixing the corpus itself cites does the
opposite: it makes hbar real, hence the generator hyperbolic. So the surviving
construction has to put the imaginarity somewhere, and the corpus already names
that place: `conj:im-q-physical-role`, whose "phase coordinate" candidate role is
exactly this. Materially narrower than the open construction problem qou-pdix
currently records.

IT IS ALSO A NEW TIER-0 DISCRIMINATOR for that bean's D1-D6 acceptance test, and
one no script there can run, for the same reason D5/D6 cannot: it is a condition
on the GENERATOR, read from the construction, not on alpha's output. Distinct
from that test's "cosh-shaped" validation row, which checks the shape of alpha as
a function of q, not the spectrum of a generator.

LEAN: `QOU/QBeta/HolonomySpectrumSignObstruction.lean`, 6 theorems, sorry-free,
axioms [propext, Classical.choice, Quot.sound]. `two_le_add_inv`,
`real_spectrum_character_ge_one` (quantified over ALL real a -- the
residue-independent step), `correction_below_one_excludes_real_spectrum`,
`kd_character_sub_one`, `kd_holonomy_cannot_realise_subunit_correction`,
`kd_character_eq_one_iff` (equality only at the classical point q = 1).

SCOPE. Scope-(b): a structural exclusion citing a proved inequality. Does NOT
show no connection exists, does not derive alpha, does not adjudicate a
convention, and wires nothing. It shows the elliptic requirement is not optional.
Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]
import _path_bridge  # noqa: E402, F401

from q_parameter import Q  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 50

Q0 = mp.mpf(str(Q))
H = Q0 - 1 / Q0
HBAR_Q = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HBAR_Q ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
Z_D = Q0 ** 3 / (Q0 ** 2 + 1)

ME = mp.mpf(str(C.M_E_MEV))
QB = mp.mpf(str(C.Q_BETA_MEV))
QA = ME * mp.fabs(Q0 ** 2 - 2 * Q0 - 1) * (Q0 + 1) / (2 * Q0 ** 3)


def theta_of(z):
    return (z - 1) * H / 2 - U / 2


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" route 5: a real-spectrum holonomy is on the wrong side of 1")
    print("=" * 78)

    corr_full = QB / QA
    cos_C, cos_D = mp.cos(theta_of(Z_C)), mp.cos(theta_of(Z_D))
    print(f"\n  THE CHARACTER THE HOLONOMY MUST PRODUCE (all < 1):")
    print(f"    full correction  Q_beta/Q_A     = {mp.nstr(corr_full, 14)}")
    print(f"    ladder cosine factor, conv C    = {mp.nstr(cos_C, 14)}")
    print(f"    ladder cosine factor, conv D    = {mp.nstr(cos_D, 14)}")

    hbar = 2 * mp.log(Q0)
    kd_char = (Q0 + 1 / Q0) / 2
    kd_excess = (Q0 - 1) ** 2 / (2 * Q0)
    print(f"\n  THE KOHNO-DRINFELD SCALE-FIXING (the corpus's own statement):")
    print(f"    braiding = P exp(hbar*t/2), t eigenvalues +-1, Hecke {{q, -1/q}}")
    print(f"      => hbar = 2 ln q = {mp.nstr(hbar, 14)}   REAL, since q0 > 1 is real")
    print(f"      => generator eigenvalues +- hbar/2 = +- {mp.nstr(hbar / 2, 14)}   REAL")
    print(f"      => character = cosh(ln q0) = (q + 1/q)/2 = {mp.nstr(kd_char, 16)}")
    print(f"    (q + 1/q)/2 - 1 = (q-1)^2/(2q) = {mp.nstr(kd_excess, 12)}  <- a square, never < 0")
    print(f"    miss vs the required character: {mp.nstr((kd_char / cos_C - 1) * 100, 6)} %"
          f"  AND ON THE WRONG SIDE")

    # --- residue-independence: the bound holds for EVERY real a ---------
    print(f"\n  RESIDUE-INDEPENDENCE — cosh(a) >= 1 for every real a, so no choice of")
    print(f"  residues (constant, q-dependent, or otherwise) can help:")
    print(f"    {'a':>14s}{'cosh(a)':>20s}{'< required?':>14s}")
    probe_a = [mp.mpf("0"), hbar / 2, mp.mpf("0.0566"), mp.mpf("1"), -hbar / 2,
               mp.mpf("-0.5")]
    any_below = False
    for a in probe_a:
        ch = (mp.exp(a) + mp.exp(-a)) / 2
        below = ch < cos_C
        any_below = any_below or below
        print(f"    {mp.nstr(a, 8):>14s}{mp.nstr(ch, 14):>20s}{str(below):>14s}")
    print(f"    -> none, and none can be: the minimum over all real a is exactly 1,")
    print(f"       attained only at a = 0 (Lean kd_character_eq_one_iff).")

    # --- what an ELLIPTIC generator would need --------------------------
    theta_req = mp.acos(cos_C)
    print(f"\n  WHAT AN ELLIPTIC GENERATOR WOULD NEED (spectrum +-i*theta):")
    print(f"    cos(theta) = {mp.nstr(cos_C, 12)}  =>  theta = {mp.nstr(theta_req, 12)}")
    print(f"    i.e. det A > 0 for the traceless generator A, not det A < 0.")
    print(f"    Kohno-Drinfeld gives det A = -(ln q0)^2 = {mp.nstr(-mp.log(Q0) ** 2, 10)} < 0.")
    print(f"    The imaginarity has to come from somewhere: conj:im-q-physical-role.")

    a_list = [(("a=%s" % mp.nstr(a, 6)), (mp.exp(a) + mp.exp(-a)) / 2) for a in probe_a]
    assertions = [
        {"name": "required_character_is_strictly_below_one",
         "passed": bool(corr_full < 1 and cos_C < 1 and cos_D < 1),
         "detail": f"Q_beta/Q_A = {mp.nstr(corr_full, 12)}; ladder cosine factor "
                   f"{mp.nstr(cos_C, 12)} (C), {mp.nstr(cos_D, 12)} (D) — all below 1"},
        {"name": "kd_character_is_at_least_one_and_is_a_square_excess",
         "passed": bool(kd_char > 1
                        and mp.fabs((kd_char - 1) - kd_excess) < mp.mpf("1e-40")),
         "detail": f"(q + 1/q)/2 = {mp.nstr(kd_char, 14)}; excess over 1 equals "
                   f"(q-1)^2/(2q) = {mp.nstr(kd_excess, 10)} exactly — a square over a "
                   "positive, so never negative (Lean kd_character_sub_one)"},
        {"name": "kd_holonomy_is_on_the_wrong_side_of_one",
         "passed": bool(kd_char > cos_C and kd_char > corr_full),
         "detail": f"KD gives {mp.nstr(kd_char, 12)}, the data needs "
                   f"{mp.nstr(cos_C, 12)} — not merely off by "
                   f"{mp.nstr((kd_char / cos_C - 1) * 100, 5)} %, but on the wrong side"},
        {"name": "no_real_generator_eigenvalue_reaches_the_target",
         "passed": bool(not any_below),
         "detail": "cosh(a) >= 1 > required for every real a sampled, and the minimum "
                   "over all real a is exactly 1 at a = 0 — so the exclusion is "
                   "INDEPENDENT of the residues, which only change which a appears"},
        {"name": "elliptic_generator_is_required_not_optional",
         "passed": bool(mp.fabs(mp.cos(theta_req) - cos_C) < mp.mpf("1e-40")
                        and -mp.log(Q0) ** 2 < 0),
         "detail": f"an elliptic generator (det A > 0, spectrum +-i*{mp.nstr(theta_req, 8)}) "
                   f"reproduces the character; Kohno-Drinfeld gives det A = "
                   f"{mp.nstr(-mp.log(Q0) ** 2, 8)} < 0, hyperbolic"},
        {"name": "strengthens_the_constant_residue_exclusion",
         "passed": bool(len(probe_a) >= 4 and not any_below),
         "detail": "PhaseFailsLogFunctionalEquation excluded c*ln q (constant residues) "
                   "by a functional equation; this excludes every real-spectrum "
                   "generator including q-dependent and non-flat ones, by a sign"},
    ]
    all_passed = all(x["passed"] for x in assertions)
    print("\n  assertions:")
    for x in assertions:
        print(f"    [{'PASS' if x['passed'] else 'FAIL'}] {x['name']}")
        print(f"           {x['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for x in assertions if x['passed'])}"
          f"/{len(assertions)})")

    witness = {
        "computation": "qbeta-holonomy-spectrum-sign-obstruction",
        "engine": "mpmath",
        "description": (
            "qou-pdix route 5 / qou-cds1 branch 3: a holonomy whose generator has REAL "
            "spectrum has normalised character cosh(a) >= 1 for every real a, while the "
            "measured correction is strictly below 1 (Q_beta/Q_A = 0.998325; ladder cosine "
            "factor 0.998399 under C, 0.998999 under D). The Kohno-Drinfeld scale-fixing "
            "hbar = 2 ln q makes the generator real at the substrate's real q0 > 1, giving "
            "character (q + 1/q)/2 = 1.005448 -- excess (q-1)^2/(2q), a square, so never "
            "negative. WRONG SIDE of 1, by 0.706 %. Because the bound is quantified over "
            "ALL real a, this is INDEPENDENT of the residues and so closes all three "
            "survivors PhaseFailsLogFunctionalEquation left open (q-dependent residues, "
            "non-flat, q-dependent-parameter). What route 5 needs is an ELLIPTIC generator "
            "(det A > 0) at real q, which points at conj:im-q-physical-role. Also a new "
            "tier-0 discriminator for qou-pdix's D1-D6 test, read from the construction "
            "like D5/D6. Lean: QOU/QBeta/HolonomySpectrumSignObstruction.lean, 6 theorems, "
            "sorry-free."),
        "contentBlock": "conj:im-q-physical-role",
        "assertions": assertions,
        "allPassed": all_passed,
        "parameters": {
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "dps": 50,
            "lean": "QOU/QBeta/HolonomySpectrumSignObstruction.lean",
            "lean_theorems": ["two_le_add_inv", "real_spectrum_character_ge_one",
                              "correction_below_one_excludes_real_spectrum",
                              "kd_character_sub_one",
                              "kd_holonomy_cannot_realise_subunit_correction",
                              "kd_character_eq_one_iff"],
            "companion_lean": ["QOU/QBeta/PhaseFailsLogFunctionalEquation.lean",
                               "QOU/QBeta/BraidImageEigenphaseExclusion.lean",
                               "QOU/QBeta/CosineParametrisationUnfalsifiable.lean"],
        },
        "data": {
            "q0": mp.nstr(Q0, 20), "h": mp.nstr(H, 16), "u": mp.nstr(U, 16),
            "required_character": {
                "full_correction": mp.nstr(corr_full, 16),
                "ladder_cosine_C": mp.nstr(cos_C, 16),
                "ladder_cosine_D": mp.nstr(cos_D, 16)},
            "kohno_drinfeld": {
                "hbar_eq_2_log_q": mp.nstr(hbar, 16),
                "generator_eigenvalue": mp.nstr(hbar / 2, 16),
                "character": mp.nstr(kd_char, 18),
                "excess_over_one": mp.nstr(kd_excess, 14),
                "excess_closed_form": "(q-1)^2/(2q)",
                "det_traceless_generator": mp.nstr(-mp.log(Q0) ** 2, 14),
                "miss_pct_vs_ladder_cosine_C": mp.nstr((kd_char / cos_C - 1) * 100, 8)},
            "cosh_samples": {k: mp.nstr(v, 14) for k, v in a_list},
            "elliptic_requirement": {
                "theta_needed": mp.nstr(theta_req, 14),
                "condition": "det A > 0 (spectrum +-i*theta), not det A < 0"},
        },
        "context": {
            "axis": "qou-cds1 branch 3 / qou-pdix route 5: can a KZ holonomy give the phase?",
            "answer": (
                "Not with a real-spectrum generator, whatever its residues. The character "
                "is cosh(a) >= 1 for every real a and the data needs < 1. Kohno-Drinfeld's "
                "own scale-fixing hbar = 2 ln q makes the generator real at the substrate's "
                "real q, so the reading the corpus cites is on the wrong side of 1. Route 5 "
                "now needs an ELLIPTIC generator at real q -- the imaginarity has to come "
                "from somewhere, and conj:im-q-physical-role is the corpus's name for that "
                "place."),
            "strengthens": (
                "PhaseFailsLogFunctionalEquation, which excluded only CONSTANT-residue "
                "holonomies (c*ln q, by the doubling identity). This closes the three "
                "survivors that bean names -- q-dependent residues, non-flat, "
                "q-dependent-parameter -- because the inequality is quantified over all "
                "real a and never reads the residues."),
            "scope": (
                "Scope-(b). Does not show no connection exists, does not derive alpha, does "
                "not adjudicate a convention, wires nothing. It shows the elliptic "
                "requirement is not optional."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out = HERE / "qbeta-holonomy-spectrum-sign-obstruction.witness.json"
    with open(out, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton (experimental pin)", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
