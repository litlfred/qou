import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
#!/usr/bin/env python3
"""qou-pdix route 5 / qou-cds1 branch 3: Im(q) is NOT the source of the elliptic
generator — and what "retire the tower" means, in numbers.

PART 1 — Im(q) REFUTED as the elliptic source.

`HolonomySpectrumSignObstruction` showed a REAL-spectrum holonomy has character
cosh(a) >= 1 while the measured correction is strictly below 1, so route 5 needs
an ELLIPTIC generator and the imaginarity must come from somewhere.
`conj:im-q-physical-role` is the corpus's name for that somewhere: "a substrate
moduli parameter NOT CONSTRAINED by current QOU observables, with three candidate
roles (chirality / phase coordinate / non-Hermitian deformation)". Two of the
three bear on this; both fail.

  ROUTE A -- Im(q) as a PHASE COORDINATE. The Kohno-Drinfeld generator
  eigenvalues are +-ln q, purely imaginary only if |q| = 1. But Re q = 1.10998 > 1,
  so |q|^2 = x^2 + y^2 > 1 for EVERY y: a purely elliptic generator is impossible
  outright. The only remaining move is to allow a complex character and keep its
  real part -- and that costs more than it buys. Forcing Re[character] onto the
  required 0.998399 needs

      Im(q) = +- 0.139956   (12.61 % of Re q)

  and leaves Im[character] = 0.014069, which is 8.40x the entire deviation being
  explained and 18074 sigma on the measurement. Q_beta is real, so that imaginary
  part must vanish -- and it vanishes only at y = 0, i.e. q real, which returns
  the character to >= 1.

  ROUTE B -- a NON-HERMITIAN deformation. An elliptic generator has spectrum
  +-i*lambda, so the braiding eigenvalues exp(+-i*hbar*lambda/2) lie on the UNIT
  CIRCLE. But Kohno-Drinfeld fixes hbar = 2 ln q precisely by matching the Hecke
  pair {q, -1/q} = {1.10998, -0.90092}, and neither has modulus 1. Route B does
  not fail on the data -- it fails by dissolving the scale-fixing the whole route
  depends on.

This does NOT refute conj:im-q-physical-role. Its chirality role is untouched and
Im(q) may be physical for other reasons. What is settled is that Im(q) is not the
source of the elliptic generator.

PART 2 — what "retire the cosine and state the correction as 1 - theta^2/2 with
NO TOWER" actually means.

THE TOWER is the infinite sequence c_2, c_3, c_4, ... in powers of u = b*hbar_q^2:
`Q_beta = Q_A * cos(theta) * (1 + c_2 u^2)(1 + c_3 u^3)...`. It is what `c_2 = -1`,
`c_3 ~ -2 = J_Hopf(1)`, the Habiro-element search and the rung program are all
about.

Retiring it does NOT mean dropping the correction. Measured:

    correction needed                    0.998325
    1 - theta^2/2  (no cosine, no tower) 0.998399
    residual delta left over            -7.3394e-5   =  94.29 sigma   <- REAL
    what c_2 = -1 predicts, -u^2        -7.2543e-5   =  98.84 % of delta
    left for c_3 and everything above   -8.5042e-7   =   1.09 sigma

So the residual is real and large, and `c_2 = -1` consumes nearly all of it. What
is left to determine `c_3` and every coefficient above it is ONE MARGINAL NUMBER
of about 1 sigma. The absolute bar on `c_3` is `sigma/u^3 = 1.2604`, reproducing
Step 15's independently-propagated 1.2619.

AND THE CENTRAL VALUE IS PARAMETRISATION-DEPENDENT, which is sharper than being
imprecise: extracting `c_3` through `cos` reproduces the corpus's proton value
-2.069343 (against the committed -2.06934258 -- the extraction is validated by
that agreement), while extracting it through `1 - theta^2/2` instead gives
-1.376381. A 33.49 % shift, produced by a choice the data resolves at only
0.549 sigma (Step 17). So `c_3`'s central value is an artefact of the
parametrisation, not merely poorly measured.

"NO TOWER" therefore means: write

    Q_beta = Q_A * (1 - theta^2/2) * (1 + delta),   delta = -7.3394e-5 measured

keeping `delta` as ONE number the anchor determines, instead of asserting
`delta = c_2 u^2 + c_3 u^3 + ...` with `c_2 = -1` exact and `c_3` extracted from
what is left. One measurement determines one number; it cannot determine a series.

SCOPE. Scope-(b) for part 1 (structural exclusions citing proved inequalities),
scope-(a) for part 2 (a measurement). Nothing derived, proposed, wired or
readmitted; no convention adjudicated; conj:im-q-physical-role is NOT refuted.
LEAN: `QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean`, 4 theorems, sorry-free,
axioms [propext, Classical.choice, Quot.sound]. Anchor: experimental (proton) pin.
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
HBAR_Q = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HBAR_Q ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
THETA = (Z_C - 1) * H / 2 - U / 2

ME = mp.mpf(str(C.M_E_MEV))
QB = mp.mpf(str(C.Q_BETA_MEV))
QB_ERR = mp.mpf(str(C.Q_BETA_MEV_ERR))
QA = ME * mp.fabs(Q0 ** 2 - 2 * Q0 - 1) * (Q0 + 1) / (2 * Q0 ** 3)

TARGET = QB / QA
SIGMA = TARGET * QB_ERR / QB
COS_C = mp.cos(THETA)


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" Im(q) is not the elliptic source; and what 'no tower' means")
    print("=" * 78)

    # ---- PART 1: Im(q) ------------------------------------------------
    x = Q0
    print(f"\n[1] ROUTE A — Im(q) as a phase coordinate")
    print(f"    generator eigenvalues are +- ln q; purely imaginary <=> |q| = 1")
    print(f"    Re q = {mp.nstr(x, 12)} > 1  =>  |q|^2 = x^2 + y^2 >= "
          f"{mp.nstr(x ** 2, 12)} > 1 for EVERY y")
    print(f"    => a purely elliptic generator is IMPOSSIBLE outright.")

    # threshold for Re[character] < 1 at all, and the exact solve
    thr_sq = x / (2 - x) - x ** 2
    thr = mp.sqrt(thr_sq)
    s = 1 / (2 * COS_C / x - 1)          # |q|^2 forcing Re[character] = COS_C
    y = mp.sqrt(s - x ** 2)
    qc = mp.mpc(x, y)
    char = (qc + 1 / qc) / 2             # independent complex cross-check
    print(f"\n    Re[(q+1/q)/2] < 1 at all requires |Im q| > {mp.nstr(thr, 10)}"
          f"  ({mp.nstr(thr / x * 100, 5)} % of Re q)")
    print(f"    forcing Re[(q+1/q)/2] = {mp.nstr(COS_C, 12)} requires")
    print(f"      |q|^2 = {mp.nstr(s, 12)}    Im(q) = +- {mp.nstr(y, 12)}"
          f"   ({mp.nstr(y / x * 100, 6)} % of Re q)")
    print(f"    cross-check by complex arithmetic: (q+1/q)/2 = "
          f"{mp.nstr(char.real, 12)} + {mp.nstr(char.imag, 10)} i")
    print(f"    BUT Im[character] = {mp.nstr(char.imag, 10)}")
    print(f"      = {mp.nstr(char.imag / (1 - TARGET), 6)}x the deviation being explained")
    print(f"      = {mp.nstr(char.imag / SIGMA, 7)} sigma. Q_beta is REAL, so it must vanish —")
    print(f"      and it vanishes only at y = 0 (Lean character_im_zero_iff), i.e. q real,")
    print(f"      which returns the character to >= 1.")

    print(f"\n[2] ROUTE B — a non-Hermitian deformation")
    print(f"    elliptic generator => braiding eigenvalues on the UNIT CIRCLE")
    print(f"    Kohno-Drinfeld fixes hbar = 2 ln q by matching the Hecke pair")
    print(f"      {{q, -1/q}} = {{{mp.nstr(Q0, 12)}, {mp.nstr(-1 / Q0, 12)}}}"
          f"   moduli {mp.nstr(Q0, 10)}, {mp.nstr(1 / Q0, 10)}")
    print(f"    neither is 1, so a unit-modulus spectrum cannot match.")
    print(f"    => route B buys ellipticity by DISSOLVING the scale-fixing.")

    # ---- PART 2: the tower --------------------------------------------
    quad = 1 - THETA ** 2 / 2
    delta = TARGET / quad - 1
    c2_pred = -U ** 2
    leftover = delta - c2_pred
    print(f"\n[3] WHAT 'NO TOWER' MEANS")
    print(f"    correction needed                     {mp.nstr(TARGET, 14)}")
    print(f"    1 - theta^2/2 (no cosine, no tower)   {mp.nstr(quad, 14)}")
    print(f"    residual delta                        {mp.nstr(delta, 10)}"
          f"   = {mp.nstr(mp.fabs(delta) / SIGMA, 6)} sigma   <- REAL, not droppable")
    print(f"    what c_2 = -1 predicts, -u^2          {mp.nstr(c2_pred, 10)}"
          f"   = {mp.nstr(c2_pred / delta * 100, 6)} % of delta")
    print(f"    left for c_3 and ALL above            {mp.nstr(leftover, 10)}"
          f"   = {mp.nstr(mp.fabs(leftover) / SIGMA, 5)} sigma")
    c3_quad = leftover / U ** 3
    # the corpus's own extraction, for comparison: cos, then the c_2 = -1 rung
    c3_corpus = (TARGET / (COS_C * (1 - U ** 2)) - 1) / U ** 3
    dc3 = SIGMA / U ** 3                       # same either way: sigma/u^3
    print(f"    => c_3 is extracted from a {mp.nstr(mp.fabs(leftover) / SIGMA, 4)}-sigma residue.")
    print(f"       absolute 1-sigma on c_3 = sigma/u^3 = {mp.nstr(dc3, 6)}"
          f"   (Step 15 measured 1.2619 independently — agrees)")
    print(f"    AND THE CENTRAL VALUE IS PARAMETRISATION-DEPENDENT:")
    print(f"       c_3 via cos + the c_2 rung (the corpus's) = {mp.nstr(c3_corpus, 10)}")
    print(f"       c_3 via 1 - theta^2/2 instead of cos      = {mp.nstr(c3_quad, 10)}")
    print(f"       shift = {mp.nstr(mp.fabs(c3_corpus - c3_quad), 8)}"
          f"  = {mp.nstr(mp.fabs(c3_corpus - c3_quad) / mp.fabs(c3_corpus) * 100, 5)} % of the value,")
    print(f"       produced by a choice the data resolves at only 0.549 sigma (Step 17).")
    print(f"    'no tower' = keep delta = {mp.nstr(delta, 8)} as ONE measured number,")
    print(f"    not delta = c_2 u^2 + c_3 u^3 + ... with c_2 = -1 exact.")

    a = [
        {"name": "purely_elliptic_generator_impossible_for_any_im_q",
         "passed": bool(x > 1 and x ** 2 > 1),
         "detail": f"Re q = {mp.nstr(x, 10)} > 1 forces |q|^2 >= {mp.nstr(x ** 2, 10)} > 1 for "
                   "every Im q, so ln q is never purely imaginary (Lean abs_sq_gt_one)"},
        {"name": "forcing_the_real_part_needs_a_large_im_q",
         "passed": bool(y / x > mp.mpf("0.1")),
         "detail": f"Im q = +-{mp.nstr(y, 10)} = {mp.nstr(y / x * 100, 5)} % of Re q, and the "
                   f"bare threshold for Re[character] < 1 is already "
                   f"{mp.nstr(thr / x * 100, 5)} % — not a perturbation"},
        {"name": "complex_character_leaves_an_imaginary_part_dwarfing_the_effect",
         "passed": bool(char.imag / (1 - TARGET) > 5
                        and mp.fabs(char.real - COS_C) < mp.mpf("1e-30")),
         "detail": f"Im[character] = {mp.nstr(char.imag, 8)} is "
                   f"{mp.nstr(char.imag / (1 - TARGET), 5)}x the deviation and "
                   f"{mp.nstr(char.imag / SIGMA, 6)} sigma; real part verified against the "
                   "closed form to 1e-30"},
        {"name": "hecke_pair_has_no_unit_modulus_member",
         "passed": bool(mp.fabs(Q0 - 1) > mp.mpf("0.01")
                        and mp.fabs(1 / Q0 - 1) > mp.mpf("0.01")),
         "detail": f"{{q, -1/q}} moduli are {mp.nstr(Q0, 10)} and {mp.nstr(1 / Q0, 10)}; an "
                   "elliptic generator forces unit modulus, so route B dissolves the "
                   "Kohno-Drinfeld scale-fixing (Lean hecke_eigenvalues_not_unit_modulus)"},
        {"name": "the_residual_is_real_and_large",
         "passed": bool(mp.fabs(delta) / SIGMA > 10),
         "detail": f"delta = {mp.nstr(delta, 8)} = {mp.nstr(mp.fabs(delta) / SIGMA, 6)} sigma — "
                   "retiring the tower does NOT mean dropping the correction"},
        {"name": "c2_consumes_almost_all_of_the_residual",
         "passed": bool(c2_pred / delta > mp.mpf("0.95")),
         "detail": f"-u^2 = {mp.nstr(c2_pred, 8)} is {mp.nstr(c2_pred / delta * 100, 5)} % of "
                   "delta, which is why c_2 = -1 looks good (and is 1.6 sigma consistent, "
                   "Step 15)"},
        {"name": "c3_and_above_rest_on_a_one_sigma_residue",
         "passed": bool(mp.fabs(leftover) / SIGMA < 3
                        and mp.fabs(dc3 - mp.mpf("1.2619")) < mp.mpf("0.01")),
         "detail": f"what is left for c_3 and every coefficient above is "
                   f"{mp.nstr(leftover, 8)} = {mp.nstr(mp.fabs(leftover) / SIGMA, 4)} sigma; the "
                   f"absolute bar sigma/u^3 = {mp.nstr(dc3, 6)} reproduces Step 15's "
                   "independently-propagated 1.2619"},
        {"name": "c3_central_value_is_parametrisation_dependent",
         "passed": bool(mp.fabs(c3_corpus - c3_quad) / mp.fabs(c3_corpus) > mp.mpf("0.2")),
         "detail": f"c_3 = {mp.nstr(c3_corpus, 8)} via cos, {mp.nstr(c3_quad, 8)} via "
                   f"1 - theta^2/2 — a "
                   f"{mp.nstr(mp.fabs(c3_corpus - c3_quad) / mp.fabs(c3_corpus) * 100, 4)} % shift "
                   "from a choice the data resolves at 0.549 sigma. c_3 is not merely "
                   "imprecise; its central value is an artefact of the parametrisation"},
    ]
    all_passed = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-imq-elliptic-generator-refutation",
        "engine": "mpmath",
        "description": (
            "qou-pdix route 5 / qou-cds1 branch 3. Im(q) is NOT the source of the elliptic "
            "generator route 5 needs. A purely elliptic Kohno-Drinfeld generator needs "
            "|q| = 1, impossible since Re q = 1.10998 > 1 forces |q| > 1 for every Im q. "
            "Allowing a complex character and keeping its real part needs "
            "Im q = +-0.139956 (12.61 % of Re q) and leaves Im[character] = 0.014069 -- "
            "8.40x the deviation being explained and 18074 sigma -- which must vanish since "
            "Q_beta is real, and vanishes only at Im q = 0. The non-Hermitian route gives "
            "ellipticity but forces unit-modulus braiding eigenvalues, which cannot match "
            "the Hecke pair {1.10998, -0.90092}, dissolving the scale-fixing. Does NOT "
            "refute conj:im-q-physical-role (its chirality role is untouched). Also "
            "quantifies 'retire the tower': the residual after 1 - theta^2/2 is "
            "-7.3394e-5 = 94.3 sigma (real, not droppable), c_2 = -1 consumes 98.84 % of "
            "it, and c_3 plus every coefficient above rests on a 1.09-sigma leftover (absolute "
            "bar sigma/u^3 = 1.2598, reproducing Step 15's 1.2619). And c_3's CENTRAL "
            "VALUE shifts 33.49 % -- -2.069343 via cos, -1.376381 via the parabola -- on "
            "a choice the data resolves at 0.549 sigma. Lean: "
            "QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean, 4 theorems, sorry-free."),
        "contentBlock": "conj:im-q-physical-role",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "dps": 50,
            "lean": "QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean",
            "lean_theorems": ["abs_sq_gt_one", "character_im_zero_iff",
                              "no_complex_q_gives_real_subunit_character",
                              "hecke_eigenvalues_not_unit_modulus"],
            "companion_lean": "QOU/QBeta/HolonomySpectrumSignObstruction.lean",
        },
        "data": {
            "q0": mp.nstr(Q0, 20), "u": mp.nstr(U, 16), "theta_C": mp.nstr(THETA, 16),
            "target": mp.nstr(TARGET, 16), "one_sigma": mp.nstr(SIGMA, 10),
            "cos_theta_C": mp.nstr(COS_C, 16),
            "route_A": {
                "im_q_threshold_for_re_below_one": mp.nstr(thr, 12),
                "im_q_required": mp.nstr(y, 14),
                "im_q_pct_of_re": mp.nstr(y / x * 100, 8),
                "abs_q_required": mp.nstr(mp.sqrt(s), 14),
                "im_character": mp.nstr(char.imag, 12),
                "im_character_over_deviation": mp.nstr(char.imag / (1 - TARGET), 8),
                "im_character_sigma": mp.nstr(char.imag / SIGMA, 10)},
            "route_B": {
                "hecke_eigenvalues": [mp.nstr(Q0, 14), mp.nstr(-1 / Q0, 14)],
                "moduli": [mp.nstr(Q0, 14), mp.nstr(1 / Q0, 14)]},
            "tower": {
                "quadratic_only": mp.nstr(quad, 14),
                "delta": mp.nstr(delta, 12),
                "delta_sigma": mp.nstr(mp.fabs(delta) / SIGMA, 8),
                "minus_u_squared": mp.nstr(c2_pred, 12),
                "c2_share_pct": mp.nstr(c2_pred / delta * 100, 8),
                "leftover_for_c3_and_above": mp.nstr(leftover, 12),
                "leftover_sigma": mp.nstr(mp.fabs(leftover) / SIGMA, 6),
                "c3_via_quadratic": mp.nstr(c3_quad, 10),
                "c3_via_cosine_corpus": mp.nstr(c3_corpus, 10),
                "c3_absolute_sigma": mp.nstr(dc3, 10),
                "c3_central_shift_pct": mp.nstr(
                    mp.fabs(c3_corpus - c3_quad) / mp.fabs(c3_corpus) * 100, 6)},
        },
        "context": {
            "axis": "qou-cds1 branch 3: is Im(q) the elliptic source? and what is 'no tower'?",
            "answer": (
                "Im(q) is not the source. Purely elliptic needs |q| = 1, impossible at "
                "Re q > 1; the complex-character workaround needs Im q = 12.61 % of Re q and "
                "leaves an imaginary part 8.40x the effect, which must vanish and does so "
                "only for real q. The non-Hermitian route dissolves the Kohno-Drinfeld "
                "scale-fixing. 'No tower' means keeping delta = -7.3394e-5 as one measured "
                "number rather than a series: c_2 = -1 consumes 98.84 % of it and c_3 and "
                "above rest on 1.09 sigma."),
            "does_not_refute": (
                "conj:im-q-physical-role. Its chirality role is untouched and Im(q) may be "
                "physical for other reasons; what is settled is that it cannot supply the "
                "elliptic generator."),
            "scope": (
                "Scope-(b) for the exclusions, scope-(a) for the tower measurement. Nothing "
                "derived, proposed, wired or readmitted; no convention adjudicated."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out = HERE / "qbeta-imq-elliptic-generator-refutation.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
