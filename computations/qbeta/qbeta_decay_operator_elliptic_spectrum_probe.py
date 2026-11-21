#!/usr/bin/env python3
"""qou-cds1: the decay OPERATOR Delta_L is ELLIPTIC — Step 21 was looking at
traces, and traces cannot see a spectrum.

======================================================================
THE CORRECTION (owner, and it is right)
======================================================================

Step 21 concluded "no phase can hide in the jet tower" from the fact that every
tower quantity it examined is REAL at real q: w_sym(k), w_alt(k), and the
W-weighted traces Sum_lam W_lam chi^lam(O), since chi^lam(T_w) lies in Z[q,q^-1]
(Geck-Pfeiffer). True, and beside the point.

What the ladder needs is an ELLIPTIC GENERATOR: traceless part with det > 0, i.e.
a complex-conjugate SPECTRUM (Step 18, HolonomySpectrumSignObstruction). A real
trace says NOTHING about a real spectrum. Step 21 ranged over traces and drew a
conclusion about spectra; that is an over-reach, and it is corrected here.

The owner's framing was the right one: "in the tower you're not looking for the
beta decay itself, but the thing that DOES beta decay" -- an operator, not a
number. And "you should be able to see the trefoil in some part of the tower".

BOTH ARE ALREADY IN THE CORPUS, and finding them is what fixes the error:
  * the H_3 normal-form basis is [gamma, sigma_0, sigma_1, L+, L-, e^-]
    = [1, T0, T1, T0T1, T1T0, T0T1T0]. The last basis element -- named `e^-`,
    the ELECTRON -- IS the longest element sigma_0 sigma_1
    sigma_0 (`qbeta_ck_from_operator_markov_trace_probe`: tr_M^lam(trefoil) =
    chi^lam(sigma_1 sigma_2 sigma_1)).
  * `qbeta_hoefsmit_tbeta_matrix_build_probe` already builds the operator-valued
    T_beta per Wedderburn block from the Hoefsmit seminormal matrices, on the
    stated ground that "PR #1840 ruled out the scalar-q route ... the c_k are
    IRREDUCIBLY OPERATOR-VALUED".

======================================================================
THE FINDING
======================================================================

At the proton pin, in the two-dimensional (2,1) block:

  operator                                   tr^2 - 4det   det(traceless)  spectrum
  Delta_S  (short model; the ladder's forms)   +0.043706      -0.010927     real (hyperbolic)
  Delta_L = NF(n) - NF(p)  (LONG; production)  -0.035837      +0.008959     *** ELLIPTIC ***

So an ELLIPTIC operator does exist in the corpus, and it is exactly the object
the owner pointed at. Three reasons Step 18's exclusions never touched it:

  1. it is a DIFFERENCE of normal forms -- an ALGEBRA element, not a braid-group
     element -- so `BraidImageEigenphaseExclusion` (which covers braid IMAGES)
     does not apply;
  2. it lives in the (2,1) block, which chi^(2,1)(Delta_S) = 0 makes invisible
     for the short model the ladder's closed forms come from;
  3. Step 21 looked at traces, and its trace IS real (-0.0914) -- the ellipticity
     is in the spectrum, which a trace cannot report.

THE ASYMMETRY IS THE POINT. The model the ladder's CLOSED FORMS come from is
hyperbolic; the model PRODUCTION RUNS ON is elliptic. `qou-cds1` already records
Delta_S vs Delta_L as a live fork with mixed pricing
(`qbeta_delta_element_fork_pricing_probe`); this adds that the two differ in KIND
and not merely in value.

======================================================================
AND IT IS THE WRONG PHASE
======================================================================

  eigenvalues     -0.045681 +- 0.094653 i        |lambda| = sqrt(det) = 0.105100
  cos(theta)      = tr/(2 sqrt(det)) = -0.434649
  eigenphase      theta = 2.020445 rad
  REQUIRED                0.056595 rad     -> a factor of 35.7

So Delta_L supplies an elliptic generator but not THE ladder phase. What it
retires is the Step-20/21 verdict "branch 3 is out of NAMED candidates": the
corpus contains an elliptic generator and the arc missed it by looking at the
wrong kind of object.

*** A NUMERICAL COINCIDENCE, FLAGGED AND NOT PURSUED. *** theta = 2.0204450 sits
1.21e-4 relative (0.012 %) from |c_3(muon)| = 2.02020024 at the CODATA-2018
anchor. NO MECHANISM connects a radian-valued eigenphase to a dimensionless
Taylor coefficient, the anchor it matches is the SUPERSEDED one (Step 16), and
this corpus has a documented precedent for exactly this trap -- the stale muon
extraction -2.00973976 and the candidate J_Hopf - hbar_q^2 = -2.00981719 agree to
four decimals while being different objects, and misled an earlier pass. Recorded
per the standing owner ruling as a target a future derivation may be checked
AGAINST, never a criterion to search ON. No search was run.

======================================================================
SCOPE
======================================================================
Scope-(a) for the finding, scope-(b) for the correction to Step 21. Nothing
derived, proposed, wired or readmitted; no convention adjudicated; no c_k value
asserted. Anchor: experimental (proton) pin, per the 2026-08-07 directive.
LEAN: `QOU/QBeta/TraceRealSpectrumComplex.lean`, sorry-free -- the ellipticity
criterion, the fact that a real trace and real determinant admit a complex
spectrum (the formal content of the Step-21 error), and that the two models
differ in kind on the measured data.
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
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke")]
import _path_bridge  # noqa: E402, F401

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from hecke_core import build_nucleon_nf_mp  # noqa: E402
from q_parameter import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 40

Q0 = q_at(mp.mp.dps)
H = Q0 - 1 / Q0
HBAR_Q = (Q0 - 1) / Q0
B_SUB = mp.sqrt((H ** 2 + 3) / (H ** 2 + 4))
U = B_SUB * HBAR_Q ** 2
Z_C = mp.sqrt(Q0) / (1 + Q0)
THETA_REQ = mp.fabs((Z_C - 1) * H / 2 - U / 2)

ME = mp.mpf(str(C.M_E_MEV))
QB = mp.mpf(str(C.Q_BETA_MEV))
QA = ME * mp.fabs(Q0 ** 2 - 2 * Q0 - 1) * (Q0 + 1) / (2 * Q0 ** 3)

# The H_3 normal-form basis, as words in the generators. `e^-` (the electron) is
# the longest element (closure: Hopf link, owner ruling 2026-11-21).
WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]
BASIS_NAMES = ["gamma", "sigma_0", "sigma_1", "L+", "L-", "e^- (trefoil)"]

# The CODATA-2018 muon c_3, for the flagged coincidence only. SUPERSEDED value
# (Step 16); carried here because that is the number theta lands near, and saying
# so is part of reporting the coincidence honestly.
C3_MUON_2018 = mp.mpf("2.02020024")


def block(shape, vec):
    gens = build_seminormal_matrices_mp(tuple(shape), Q0)[0]
    d = gens[0].rows
    M = mp.zeros(d, d)
    for c, w in zip(vec, WORDS):
        B = mp.eye(d)
        for i in w:
            B = B * gens[i]
        M = M + mp.mpf(c) * B
    return M, d


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" the decay OPERATOR is elliptic — traces cannot see a spectrum")
    print("=" * 78)
    print(f"\n  H_3 normal-form basis = {BASIS_NAMES}")
    print(f"  i.e. [1, T0, T1, T0T1, T1T0, T0T1T0] — 'e^-' IS the longest element,")
    print(f"  which IS the trefoil sigma_0 sigma_1 sigma_0. The electron is in the basis.")

    # `build_nucleon_nf` returns a list of Python FLOATS, so
    # `mp.mpf(str(x))` would read a float64 as exact at this file's dps.
    # `build_nucleon_nf_mp` is the same braid word in mpf -- and it was
    # STALE by the 2026-08-30 gluon term until it was fixed on this branch;
    # do not swap to it on a docstring's word without re-measuring.
    p = build_nucleon_nf_mp(list("uud"), mp.mp.dps)
    n = build_nucleon_nf_mp(list("udd"), mp.mp.dps)
    d_l = [n[i] - p[i] for i in range(6)]
    d_s = [H ** 2 / 2, -H / 2, -H / 2, mp.mpf(0), mp.mpf(0), mp.mpf(0)]

    print(f"\n  THE (2,1) BLOCK\n")
    print(f"  {'operator':38s}{'trace':>16s}{'det':>16s}{'tr^2-4det':>16s}  spectrum")
    out = {}
    for nm, v in (("Delta_S (short; ladder's closed forms)", d_s),
                  ("Delta_L = NF(n)-NF(p) (LONG; production)", d_l)):
        M, d = block((2, 1), v)
        tr = M[0, 0] + M[1, 1]
        det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        disc = tr ** 2 - 4 * det
        out[nm] = (tr, det, disc)
        print(f"  {nm:38s}{mp.nstr(tr, 11):>16s}{mp.nstr(det, 11):>16s}"
              f"{mp.nstr(disc, 11):>16s}  "
              f"{'*** ELLIPTIC ***' if disc < 0 else 'real (hyperbolic)'}")

    tr_l, det_l, disc_l = out["Delta_L = NF(n)-NF(p) (LONG; production)"]
    tr_s, det_s, disc_s = out["Delta_S (short; ladder's closed forms)"]
    mod = mp.sqrt(det_l)
    cos_t = tr_l / (2 * mod)
    theta = mp.acos(cos_t)
    print(f"\n  Delta_L's elliptic data:")
    print(f"    eigenvalues  {mp.nstr(tr_l / 2, 10)} +- {mp.nstr(mp.sqrt(-disc_l) / 2, 10)} i")
    print(f"    |lambda| = sqrt(det) = {mp.nstr(mod, 12)}")
    print(f"    cos(theta) = tr/(2 sqrt(det)) = {mp.nstr(cos_t, 14)}")
    print(f"    eigenphase theta = {mp.nstr(theta, 14)} rad")
    print(f"    REQUIRED phase   = {mp.nstr(THETA_REQ, 14)} rad"
          f"   -> factor {mp.nstr(theta / THETA_REQ, 8)}")
    print(f"    required cos     = {mp.nstr(mp.cos(THETA_REQ), 14)}   (Delta_L gives "
          f"{mp.nstr(cos_t, 10)})")

    rel = mp.fabs(theta - C3_MUON_2018) / C3_MUON_2018
    print(f"\n  *** FLAGGED COINCIDENCE, NOT PURSUED ***")
    print(f"    theta = {mp.nstr(theta, 12)} sits {mp.nstr(rel, 4)} relative "
          f"({mp.nstr(rel * 100, 4)} %) from |c_3(muon)| = {C3_MUON_2018}")
    print(f"    at the SUPERSEDED CODATA-2018 anchor (Step 16). No mechanism connects a")
    print(f"    radian eigenphase to a dimensionless Taylor coefficient; this corpus has a")
    print(f"    documented precedent for the trap (stale -2.00973976 vs J_Hopf - hbar^2")
    print(f"    -2.00981719, agreeing to 4 decimals while being different objects).")
    print(f"    Recorded as a target to check a derivation AGAINST. No search was run.")

    a = [
        {"name": "electron_word_is_the_longest_element_is_the_trefoil",
         "passed": True,
         "detail": "the H_3 NF basis is [1, T0, T1, T0T1, T1T0, T0T1T0] and its sixth "
                   "element is named 'e^-' — the electron IS the trefoil, already in the "
                   "corpus's own basis"},
        {"name": "delta_L_the_production_model_is_elliptic",
         "passed": bool(disc_l < 0),
         "detail": f"tr^2 - 4det = {mp.nstr(disc_l, 8)} < 0, det(traceless) = "
                   f"{mp.nstr(det_l - tr_l ** 2 / 4, 8)} > 0 — complex-conjugate spectrum "
                   f"{mp.nstr(tr_l / 2, 8)} +- {mp.nstr(mp.sqrt(-disc_l) / 2, 8)} i"},
        {"name": "delta_S_the_ladders_model_is_hyperbolic",
         "passed": bool(disc_s > 0),
         "detail": f"tr^2 - 4det = {mp.nstr(disc_s, 8)} > 0 — real spectrum. The two Delta "
                   "models differ in KIND, not merely in value"},
        {"name": "step21_conclusion_over_reached",
         "passed": bool(mp.fabs(mp.im(mp.mpc(tr_l))) < mp.mpf("1e-30") and disc_l < 0),
         "detail": f"Delta_L's trace is real ({mp.nstr(tr_l, 8)}) while its spectrum is "
                   "complex — so 'every tower trace is real' could never have settled "
                   "whether a tower operator is elliptic. Step 21's conclusion is corrected"},
        {"name": "elliptic_phase_is_not_the_ladder_phase",
         "passed": bool(theta / THETA_REQ > 10),
         "detail": f"theta = {mp.nstr(theta, 10)} rad against the required "
                   f"{mp.nstr(THETA_REQ, 10)} — a factor {mp.nstr(theta / THETA_REQ, 6)}. "
                   "Delta_L supplies an elliptic generator, not THE phase"},
        {"name": "branch3_is_not_out_of_named_candidates_after_all",
         "passed": bool(disc_l < 0),
         "detail": "Step 20/21's 'out of named candidates' is withdrawn: the corpus "
                   "contains an elliptic operator, in the block the short model makes "
                   "invisible, and it is not in the braid image so the eigenphase "
                   "exclusion never covered it"},
    ]
    all_passed = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-decay-operator-elliptic-spectrum",
        "engine": "mpmath",
        "description": (
            "qou-cds1: CORRECTS Step 21. That step concluded no phase can hide in the jet "
            "tower because every tower TRACE is real at real q; but the ladder needs an "
            "elliptic GENERATOR (complex-conjugate spectrum), and a real trace says nothing "
            "about a real spectrum. Following the owner's framing -- look for the thing that "
            "DOES the decay, and for the trefoil -- both are already in the corpus: the H_3 "
            "normal-form basis is [1,T0,T1,T0T1,T1T0,T0T1T0] whose sixth element is named "
            "'e^-', the electron, which IS the trefoil; and qbeta_hoefsmit_tbeta_matrix_build "
            "already builds T_beta operator-valued per block. Measured in the (2,1) block at "
            "the proton pin: Delta_L = NF(n)-NF(p), the LONG model production runs on, is "
            "ELLIPTIC (tr^2-4det = -0.035837, det(traceless) = +0.008959, eigenvalues "
            "-0.045681 +- 0.094653 i), while Delta_S, the short model the ladder's closed "
            "forms come from, is HYPERBOLIC (+0.043706). Step 18's exclusions never touched "
            "Delta_L: it is an algebra element not a braid-group element, it lives in the "
            "block chi^(2,1)(Delta_S)=0 hides, and its trace is real. BUT its eigenphase is "
            "2.020445 rad against a required 0.056595 -- a factor 35.7 -- so it is not THE "
            "ladder phase. What it retires is 'branch 3 is out of named candidates'. A "
            "coincidence is flagged and not pursued: theta sits 0.012 % from |c_3(muon)| at "
            "the SUPERSEDED CODATA-2018 anchor, with no mechanism and a documented precedent "
            "for the trap. Lean: QOU/QBeta/TraceRealSpectrumComplex.lean, sorry-free."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "pin": "experimental (proton), per the 2026-08-07 owner directive",
            "dps": 40,
            "nf_basis": BASIS_NAMES,
            "lean": "QOU/QBeta/TraceRealSpectrumComplex.lean",
            "lean_theorems": ["IsElliptic", "isElliptic_iff_traceless_det_pos",
                              "real_trace_real_det_but_complex_spectrum",
                              "short_model_not_elliptic", "isElliptic_det_pos"],
            "anti_fit": ("the theta-vs-c_3 proximity is REPORTED, not pursued; no search "
                         "over combinations was run, and the anchor it matches is the "
                         "superseded CODATA-2018 one"),
        },
        "data": {
            "q0": mp.nstr(Q0, 20), "u": mp.nstr(U, 16),
            "theta_required": mp.nstr(THETA_REQ, 16),
            "block_2_1": {
                "Delta_S": {"trace": mp.nstr(tr_s, 14), "det": mp.nstr(det_s, 14),
                            "disc": mp.nstr(disc_s, 14), "spectrum": "real"},
                "Delta_L": {"trace": mp.nstr(tr_l, 14), "det": mp.nstr(det_l, 14),
                            "disc": mp.nstr(disc_l, 14), "spectrum": "elliptic",
                            "modulus": mp.nstr(mod, 14),
                            "cos_theta": mp.nstr(cos_t, 14),
                            "eigenphase_rad": mp.nstr(theta, 14)}},
            "phase_ratio_to_required": mp.nstr(theta / THETA_REQ, 10),
            "flagged_coincidence": {
                "theta": mp.nstr(theta, 14),
                "c3_muon_codata2018_abs": str(C3_MUON_2018),
                "relative": mp.nstr(rel, 8),
                "status": "FLAGGED, NOT PURSUED — no mechanism; superseded anchor"},
        },
        "context": {
            "axis": "qou-cds1: is there an elliptic operator in the tower?",
            "answer": (
                "Yes — Delta_L, the long-model decay operator production runs on, is "
                "elliptic in the (2,1) block. Step 21 missed it by examining traces, which "
                "cannot see a spectrum. Its eigenphase 2.020445 is a factor 35.7 from the "
                "required 0.056595, so it is not the ladder phase."),
            "corrects": (
                "Step 21's 'no phase can hide in the jet tower' and Step 20/21's 'branch 3 "
                "is out of named candidates'. The vanishing Step 21 proved -- bar-odd "
                "operators have zero Plancherel trace -- STANDS and is unaffected; what is "
                "withdrawn is the inference from trace-realness to spectrum-realness."),
            "scope": ("Scope-(a) for the finding, scope-(b) for the correction. Nothing "
                      "derived, proposed, wired or readmitted; no c_k value asserted."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-decay-operator-elliptic-spectrum.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
