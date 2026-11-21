#!/usr/bin/env python3
"""qou-cds1: is the cosine in `Q_N1 = Q_A * cos(alpha - u/2)` justified?

NO, on the evidence available -- and the reason is sharper than "it was
manufactured". The PHASE does real work; the COSINE does none that the data can
see. Those are different claims and the corpus had not separated them.

WHAT WAS ALREADY CLOSED, and by whom. `QOU.QBeta.BraidImageEigenphaseExclusion`
(bean qou-cds1, Lean, sorry-free) leaves three ways a transfer matrix with
spectrum {e^{+-i alpha}} could earn the cosine, and closes two: the class meant
to carry the spectral reading (`EigenphaseCarrier`) is VACUOUS; the braid-image
branch is EXCLUDED in every convention; "M arbitrary" is CIRCULAR
(`rotationOfPhase` satisfies it for any alpha). Only a holonomy of an
independently-defined connection (KZ / Kohno-Drinfeld) survives, and nothing in
the corpus supplies one. This probe adds the quantitative half that exclusion
does not reach.

THE MEASUREMENT (proton pin, 50 dps, convention C).

    1 sigma on the measured Q_beta/Q_A            7.784e-7
    cos(theta) explains ................. 95.60 % of the 0.167 % deviation
    |cos(theta) - (1 - theta^2/2)| ....... 4.274e-7   =   0.549 sigma
    residual the c_k tower must absorb ... 7.382e-5   =  94.836 sigma

So the phase is a genuine ZERO-PARAMETER success: `theta = (z-1)h/2 - u/2` with
z fixed by the convention captures 95.6 % of the deviation from Q_A, and the
`- u/2` offset is part of that (without it, 81.8 %).

And the cosine is a genuine NULL. Everything that distinguishes `cos(theta)` from
its quadratic truncation `1 - theta^2/2` amounts to HALF A STANDARD DEVIATION of
the measurement, while the residual it fails to explain is NINETY-FIVE. The data
cannot tell a cosine from a parabola here; any function agreeing to second order
fits identically well and leaves the same c_k tower. Ratio: 172.7x under C.

UNDER D IT IS WORSE ON BOTH COUNTS: the cosine explains only 59.76 %, and the
residual/signature ratio is 4039x.

FORMALISED. `QOU/QBeta/CosineParametrisationUnfalsifiable.lean`, sorry-free,
axioms [propext, Classical.choice, Quot.sound]:
  * `cos_departure_le` -- for |theta| <= 3/50 (covers both conventions),
    |cos theta - (1 - theta^2/2)| <= 7e-7, i.e. below the 7.784e-7 resolution.
  * `ck_residual_dominates_cos_departure` -- with r >= 7e-5, the cosine's whole
    signature is at most r/100.
  * `cos_parametrisation_not_injective` -- cos is even, so two distinct z give
    the SAME correction, while the exact correction is affine in z
    (`traceDelta_cross_mul`) hence injective. The parametrisation discards a
    distinction the object makes; this is the algebraic form of the "square-root
    branch point 0.062 % above q0" the corpus already met.

WHAT IS AND IS NOT WARRANTED. Warranted: the correction is `1 - theta^2/2` to
within the resolution, with `theta` the convention-fixed discrepancy phase. NOT
warranted by anything measured here: that the correction is a COSINE, that
`theta` is an angle, that there is a rotation or a unitary behind it, or that the
residual should be expanded in powers of `u` at all -- a `c_k` tower in `u` is a
second modelling choice on top of the first, and the anchor constrains only ONE
number (`7.382e-5`), so `c_2 = -1` is an assumption and `c_3` is what is left
after it. One measurement cannot determine a series.

======================================================================
CORRECTION TO STEP 16 OF THIS BEAN -- MINE, AND IT MATTERS HERE
======================================================================
Step 16 (`qbeta-decay-functional-unification-protium`, commit a949c94115)
concluded that "the two decay functionals are ONE functional in two coordinates"
and that "the c_k are the affine-vs-cosine reparametrisation residual".

THAT IS OVERSTATED. The identity `prod_k(1 + c_k u^k) = affine(z)/cos(theta(z))`
is a valid rearrangement only if BOTH sides are evaluated at the SAME z. The
corpus's ladder does not do that: it FIXES `z = z_conv` and sets
`prod = data/cos(theta(z_conv))`, while the trace route FREES z and sets
`affine(z) = data`. Concretely, at z_C the affine correction is 0.4409 -- 56 %
from the data -- whereas the ladder's product there is 0.999926. Step 16's probe
printed 0.441582 as "the ladder product at z_C"; that number is not the corpus's
ladder product and should not be read as one.

The accurate statement: the two routes are two ALLOCATIONS of the same 0.167 %
residual, with different free parameters -- a c_k tower against a free z. They
share Q_A identically and agree at z = 1, so leading-order agreement between them
is automatic and carries no information; beyond that they are different models.

WHAT SURVIVES STEP 16 UNCHANGED: the bridge `E_0*(-eps(Delta_S)) = Q_A`
(Lean-proved, and pre-existing as prop:neutron-qvalue-symbolic); both corrections
equal 1 at z = 1; the protium findings (Delta_S is an ATOMIC object, 235x
discrimination, and the protium ELEMENT refuted); and
`F_REQUIRED_TRM = (Q_beta/Q_A)/affine(z_D)` to 3.6e-9, which is a statement about
the trace route alone and stands. Step 15's withdrawal of "K off by 2.2656x"
therefore also stands.

SCOPE. Scope-(a). Does NOT show the cosine is wrong, does not propose a
replacement, does not derive alpha, and wires nothing. It shows the cosine is not
TESTED by the Q_beta anchor. Branch 3 of the eigenphase trichotomy is untouched:
a KZ/Kohno-Drinfeld derivation would justify the cosine independently of anything
measured here. Anchor: experimental (proton) pin, per the 2026-08-07 directive.
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

from q_parameter import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 50

Q0 = q_at(mp.mp.dps)
H = Q0 - 1 / Q0
HBAR = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HBAR ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
Z_D = Q0 ** 3 / (Q0 ** 2 + 1)

ME = mp.mpf(str(C.M_E_MEV))
ME_ERR = mp.mpf(str(C.M_E_MEV_ERR))
QB = mp.mpf(str(C.Q_BETA_MEV))
QB_ERR = mp.mpf(str(C.Q_BETA_MEV_ERR))
QA = ME * mp.fabs(Q0 ** 2 - 2 * Q0 - 1) * (Q0 + 1) / (2 * Q0 ** 3)

TARGET = QB / QA
# 1 sigma on the measured ratio: Q_beta and m_e are the CAL inputs it moves with.
SIGMA = TARGET * mp.sqrt((QB_ERR / QB) ** 2 + (ME_ERR / ME) ** 2)


def theta_of(z):
    """The ladder's phase, alpha - u/2 with alpha = (z-1)h/2."""
    return (z - 1) * H / 2 - U / 2


def affine(z):
    """The EXACT correction: tr_M^z(Delta_S)/eps(Delta_S), affine in z."""
    return (2 * Q0 * z - Q0 ** 2 + 1) / (2 * Q0 - Q0 ** 2 + 1)


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" qou-cds1: is the cosine parametrisation justified?")
    print("=" * 78)
    dev = 1 - TARGET
    print(f"\n  measured Q_beta/Q_A = {mp.nstr(TARGET, 16)}")
    print(f"  deviation from Q_A  = {mp.nstr(dev, 10)}   (the 0.167 %)")
    print(f"  1 sigma on it       = {mp.nstr(SIGMA, 8)}   (Q_beta 0.78 ppm + m_e)")
    print(f"  u = {mp.nstr(U, 12)}    h = {mp.nstr(H, 12)}")

    rows = {}
    for nm, z in (("C", Z_C), ("D", Z_D)):
        th = theta_of(z)
        cosv = mp.cos(th)
        quad = 1 - th ** 2 / 2
        signature = mp.fabs(cosv - quad)
        residual = mp.fabs(TARGET / cosv - 1)
        rows[nm] = {
            "z": z, "theta": th, "cos": cosv, "quad": quad,
            "explains_pct": (1 - cosv) / dev * 100,
            "explains_no_offset_pct": (1 - mp.cos((z - 1) * H / 2)) / dev * 100,
            "signature": signature, "signature_sigma": signature / SIGMA,
            "residual": residual, "residual_sigma": residual / SIGMA,
            "ratio": residual / signature,
            "affine": affine(z),
        }
        r = rows[nm]
        print(f"\n  --- convention {nm}:  z = {mp.nstr(z, 12)}   "
              f"theta = {mp.nstr(th, 12)}")
        print(f"    cos(theta) = {mp.nstr(cosv, 14)}  -> explains "
              f"{mp.nstr(r['explains_pct'], 6)} % of the deviation, ZERO parameters")
        print(f"      (without the -u/2 offset: {mp.nstr(r['explains_no_offset_pct'], 6)} %)")
        print(f"    THE COSINE'S OWN SIGNATURE |cos - (1 - theta^2/2)|")
        print(f"      = {mp.nstr(signature, 8)}   = {mp.nstr(r['signature_sigma'], 5)} sigma"
              f"   <- statistically invisible")
        print(f"    THE RESIDUAL THE c_k TOWER MUST ABSORB")
        print(f"      = {mp.nstr(residual, 8)}   = {mp.nstr(r['residual_sigma'], 6)} sigma")
        print(f"    ratio residual/signature = {mp.nstr(r['ratio'], 8)}x")

    print(f"\n  READING. The PHASE does real work — 95.6 % of the deviation under C")
    print(f"  with no free parameter. The COSINE does none the data can see: its")
    print(f"  entire content beyond a parabola is {mp.nstr(rows['C']['signature_sigma'], 4)} sigma, while what it")
    print(f"  fails to explain is {mp.nstr(rows['C']['residual_sigma'], 5)} sigma. Any function agreeing to")
    print(f"  second order fits identically and leaves the same c_k tower.")

    # --- the 2-to-1 defect, numerically (Lean: cos_parametrisation_not_injective)
    th0 = theta_of(Z_C)
    z_mirror = 1 + 2 * (U / 2 - th0) / H
    print(f"\n  2-to-1: z = {mp.nstr(Z_C, 12)} and z' = {mp.nstr(z_mirror, 12)} give")
    print(f"    the SAME cos = {mp.nstr(mp.cos(theta_of(Z_C)), 14)} / "
          f"{mp.nstr(mp.cos(theta_of(z_mirror)), 14)}")
    print(f"    but DIFFERENT exact corrections: {mp.nstr(affine(Z_C), 12)} vs "
          f"{mp.nstr(affine(z_mirror), 12)}")

    # --- the Step 16 correction, shown rather than asserted -------------
    print(f"\n  STEP 16 CORRECTION (mine). The ladder and the trace route do NOT")
    print(f"  evaluate at the same z, so they are two ALLOCATIONS, not one functional:")
    print(f"    at z_C:  affine(z_C)          = {mp.nstr(affine(Z_C), 12)}   "
          f"({mp.nstr(mp.fabs(affine(Z_C) / TARGET - 1) * 100, 4)} % from the data)")
    print(f"             corpus ladder product = {mp.nstr(TARGET / mp.cos(theta_of(Z_C)), 12)}")
    print(f"    Step 16's probe printed {mp.nstr(affine(Z_C) / mp.cos(theta_of(Z_C)), 12)} as 'the ladder")
    print(f"    product at z_C'; that is affine/cos, which the corpus's ladder is not.")

    c = rows["C"]
    d = rows["D"]
    a = [
        {"name": "phase_does_real_work_zero_parameters",
         "passed": bool(c["explains_pct"] > 90 and c["explains_no_offset_pct"] > 75),
         "detail": f"cos(theta) at z_C explains {mp.nstr(c['explains_pct'], 5)} % of the "
                   f"deviation with no free parameter ({mp.nstr(c['explains_no_offset_pct'], 5)} % "
                   "without the -u/2 offset) — the phase is not the problem"},
        {"name": "cosine_signature_is_below_experimental_resolution",
         "passed": bool(c["signature_sigma"] < 1 and d["signature_sigma"] < 1),
         "detail": f"|cos - (1 - theta^2/2)| = {mp.nstr(c['signature'], 6)} = "
                   f"{mp.nstr(c['signature_sigma'], 4)} sigma (C), "
                   f"{mp.nstr(d['signature_sigma'], 4)} sigma (D) — the data cannot tell a "
                   "cosine from a parabola here"},
        {"name": "ck_residual_dominates_the_cosine_signature",
         "passed": bool(c["ratio"] > 100 and d["ratio"] > 100),
         "detail": f"residual/signature = {mp.nstr(c['ratio'], 6)}x (C), "
                   f"{mp.nstr(d['ratio'], 6)}x (D). The c_k tower is correcting a "
                   "quadratic, and would be the same tower for any function agreeing "
                   "to second order"},
        {"name": "residual_itself_is_highly_significant",
         "passed": bool(c["residual_sigma"] > 10),
         "detail": f"{mp.nstr(c['residual_sigma'], 6)} sigma — so the thing the ladder "
                   "exists to explain IS real; what is unsupported is explaining it with "
                   "a cosine rather than with anything else quadratic"},
        {"name": "convention_D_is_worse_on_both_counts",
         "passed": bool(d["explains_pct"] < c["explains_pct"] and d["ratio"] > c["ratio"]),
         "detail": f"D explains {mp.nstr(d['explains_pct'], 5)} % against C's "
                   f"{mp.nstr(c['explains_pct'], 5)} %, and its residual/signature ratio is "
                   f"{mp.nstr(d['ratio'], 5)}x against {mp.nstr(c['ratio'], 5)}x"},
        {"name": "cosine_is_two_to_one_where_the_exact_form_is_injective",
         "passed": bool(mp.fabs(mp.cos(theta_of(Z_C)) - mp.cos(theta_of(z_mirror)))
                        < mp.mpf("1e-40")
                        and mp.fabs(affine(Z_C) - affine(z_mirror)) > mp.mpf("0.1")),
         "detail": f"z = {mp.nstr(Z_C, 10)} and z' = {mp.nstr(z_mirror, 10)} share a cos but "
                   f"have exact corrections {mp.nstr(affine(Z_C), 8)} vs "
                   f"{mp.nstr(affine(z_mirror), 8)} — Lean cos_parametrisation_not_injective"},
        {"name": "step16_unification_claim_is_corrected_here",
         "passed": bool(mp.fabs(affine(Z_C) / TARGET - 1) > mp.mpf("0.5")),
         "detail": f"affine(z_C) = {mp.nstr(affine(Z_C), 10)} is "
                   f"{mp.nstr(mp.fabs(affine(Z_C) / TARGET - 1) * 100, 4)} % from the data, so "
                   "the ladder and the trace route are NOT evaluated at the same z and are "
                   "two allocations rather than one functional. Step 16 overstated it"},
    ]
    all_passed = all(x["passed"] for x in a)
    print("\n  assertions:")
    for x in a:
        print(f"    [{'PASS' if x['passed'] else 'FAIL'}] {x['name']}")
        print(f"           {x['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for x in a if x['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-cosine-parametrisation-justification",
        "engine": "mpmath",
        "description": (
            "qou-cds1: the cosine in Q_N1 = Q_A*cos(alpha - u/2) is NOT justified by the "
            "Q_beta anchor, but the PHASE is. cos(theta) with theta fixed by the convention "
            "explains 95.60 % of the 0.167 % deviation from Q_A with zero free parameters "
            "(81.76 % without the -u/2 offset), so the phase does real work. But the "
            "cosine's entire content beyond its quadratic truncation is 4.274e-7 = 0.549 "
            "sigma of the measured Q_beta/Q_A, while the residual the c_k tower must absorb "
            "is 7.382e-5 = 94.8 sigma -- a ratio of 172.7x under C and 4039x under D. The "
            "data cannot distinguish cos(theta) from 1 - theta^2/2; any function agreeing to "
            "second order fits identically and leaves the same tower. Complements "
            "BraidImageEigenphaseExclusion, which closes the braid-image and arbitrary-M "
            "branches and leaves only a KZ/Kohno-Drinfeld holonomy. Also CORRECTS Step 16's "
            "'the two functionals are one functional': the ladder fixes z by convention "
            "while the trace route frees it, so they are two allocations of one residual. "
            "Lean: QOU/QBeta/CosineParametrisationUnfalsifiable.lean, 3 theorems, sorry-free."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "dps": 50,
            "lean": "QOU/QBeta/CosineParametrisationUnfalsifiable.lean",
            "lean_theorems": ["cos_departure_le", "ck_residual_dominates_cos_departure",
                              "cos_parametrisation_not_injective"],
            "companion_lean": "QOU/QBeta/BraidImageEigenphaseExclusion.lean",
        },
        "data": {
            "q0": mp.nstr(Q0, 20), "h": mp.nstr(H, 16), "u": mp.nstr(U, 16),
            "Q_A_MeV": mp.nstr(QA, 16),
            "measured_ratio": mp.nstr(TARGET, 16),
            "deviation_from_QA": mp.nstr(dev, 12),
            "one_sigma_on_ratio": mp.nstr(SIGMA, 10),
            "by_convention": {
                nm: {k: mp.nstr(v, 12) for k, v in r.items()} for nm, r in rows.items()},
            "mirror_z_same_cos": mp.nstr(z_mirror, 16),
            "affine_at_z_C": mp.nstr(affine(Z_C), 12),
            "corpus_ladder_product_at_z_C": mp.nstr(TARGET / mp.cos(theta_of(Z_C)), 12),
            "step16_printed_affine_over_cos": mp.nstr(
                affine(Z_C) / mp.cos(theta_of(Z_C)), 12),
        },
        "context": {
            "axis": "qou-cds1: is the cosine parametrisation justified at all?",
            "answer": (
                "The PHASE is; the COSINE is not. theta = (z-1)h/2 - u/2 captures 95.6 % of "
                "the deviation with no free parameter. But everything distinguishing cos "
                "from 1 - theta^2/2 is 0.549 sigma, against a 94.8-sigma residual -- so the "
                "cosine is not tested by this anchor, and the c_k tower is correcting a "
                "parabola. Warranted: correction = 1 - theta^2/2 within resolution. NOT "
                "warranted: that it is a cosine, that theta is an angle, that a rotation or "
                "unitary is behind it, or that the residual should be expanded in powers of "
                "u -- the anchor constrains ONE number, so c_2 = -1 is an assumption and "
                "c_3 is what is left after it."),
            "corrects": (
                "Step 16 of this bean (commit a949c94115): 'the two decay functionals are "
                "one functional in two coordinates' is OVERSTATED. The identity "
                "prod = affine(z)/cos(theta(z)) needs both sides at the SAME z; the corpus's "
                "ladder fixes z = z_conv and the trace route frees z. At z_C the affine "
                "correction is 0.4409, 55.8 % from the data, while the ladder's product is "
                "0.999926. Two allocations of one residual, with different free parameters. "
                "What survives: the E_0*(-eps) = Q_A bridge, agreement at z = 1, the protium "
                "findings, and F_REQUIRED_TRM = (Q_beta/Q_A)/affine(z_D)."),
            "scope": (
                "Scope-(a). Does not show the cosine is wrong, propose a replacement, derive "
                "alpha, or wire anything. Branch 3 of the eigenphase trichotomy "
                "(KZ / Kohno-Drinfeld holonomy) is untouched and would justify the cosine "
                "independently of anything measured here."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out = HERE / "qbeta-cosine-parametrisation-justification.witness.json"
    with open(out, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
