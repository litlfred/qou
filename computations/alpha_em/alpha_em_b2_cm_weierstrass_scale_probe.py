#!/usr/bin/env python3
"""alpha_em_b2_cm_weierstrass_scale_probe.py — bean qou-m117 (Option B-backup):
bypass the Braden-Northover normalization convention via CM theory /
Weierstrass models of the Bring elliptic factors.

Under the standing 2026-07-19 owner ruling (R2 / the per-loop identification
is NOT derived-proved) and the attack-options scope discipline
(docs/audits/2026-07-24-alpha-em-b2-tau-identification-attack-options.md):
no tau-functor constructed, no TauRhoHodgeLift instance registered, no fit,
nothing wired, 1/(8pi) stays phase-4. Route C's refutation (the landed
alpha_em_b2_invariant_c_probe.py) stands: NO single convention-free scalar
|c| exists; this probe attacks the residual DISCRETE structure of the
tau-scale gate, honestly.

WHAT THIS PROBE DOES (W1-W7):
  W1. CM LEG DIES IMMEDIATELY (scope-(a) narrowing, recorded honestly):
      the corpus j-invariants j(tau0) = -121945/32 and j(5*tau0) = -25/2
      (Braden-Disney-Hogg, conductor-50 class 50a) are NON-INTEGRAL
      rationals. A CM elliptic curve has j an ALGEBRAIC INTEGER (classical
      CM theory: j of a CM point generates the ring class field and is
      integral). Denominators 32 and 2 != 1 ==> NEITHER factor has CM.
      The bean's literal "CM point documented independent of B-N
      normalization" route is therefore CLOSED as stated — scope-(a): this
      kills the CM *mechanism*, not the convention-bypass goal, which
      survives via the Q-model leg below.
  W2. Q-MODEL LEG (what survives): both curves are Q-curves in the 50a
      isogeny class with Q-rational Weierstrass models. Build the standard
      j-parametrized model E_j: y^2 + xy = x^3 - 36/(j-1728) x - 1/(j-1728)
      with EXACT rational arithmetic; certify c4^3/Delta == j exactly
      (Fraction round-trip; no floats). Delta < 0 for both (rhombic
      lattice — consistent with Re tau = -1/2).
  W3. PERIODS FROM THE MODEL, INDEPENDENT OF ANY PERIOD-MATRIX INPUT:
      compute the period lattice of each Q-model by AGM (mpmath, 50 dps)
      from the Weierstrass cubic's roots, reduce the period ratio to the
      SL2(Z) fundamental domain, and self-certify by j round-trip
      (residual ~1e-58). Period RATIOS are twist-independent, so the
      choice of Q-model in the twist class is immaterial.
  W4. INDEPENDENT j-INVERSION CROSS-CHECK: invert the modular j-function
      on the boundary line Re tau = -1/2 (where real j < 0 lives) by root-
      finding on 1728*kleinj; the two routes (AGM periods vs j-inversion)
      agree to ~1e-50. Recover tau0 at 50 dps by the exact SL2(Z) word:
      tau_A^fund = gamma'(tau0) with gamma' = [[1,1],[-2,-1]], i.e.
      tau0 = -1/2 + i/(4*Im tau_A^fund). Matches the corpus literature
      value -0.5 + 0.186676i (BringEllipticFactor.lean docstring,
      Braden-Disney-Hogg) to the quoted 6 digits.
  W5. X0(5) / (1,5,5,5) GATE SELF-CERTIFIED: reduce(5*tau0_recovered)
      equals the fundamental tau of the j = -25/2 curve to ~1e-60, and
      Im(tau_B^fund) / Im(tau0_recovered) = 4*t_A*t_B = 5 EXACTLY at
      50 dps. This certifies the Braden-Northover (1,5,5,5) period-matrix
      convention INDEPENDENTLY: j-inversion + Q-model AGM periods only,
      no period-matrix input, no B-N normalization consumed.
  W6. THE HONEST TAU-SCALE FINDING (what this does and does NOT fix):
      the Q-model/Neron differential normalizes periods PER CURVE
      canonically — but the absolute Hodge scale on H^{1,0}(Bring) still
      passes through the isogeny Jac(Bring) -> E_{5tau0}^3 x E_{tau0}
      (unknown degree / pullback factor). With Neron normalization the
      REMAINING freedom is DISCRETE: an isogeny pullback phi^* scales the
      induced form by deg(phi) in Z_{>0} (natural support: powers of 5,
      given the conductor-50 / X0(5) structure). The tau-scale gate
      narrows from a continuous unknown to that discrete set.
  W7. THE deg^2 = 25 OBSERVATION (scope-(a), OPEN, owner-level, NO
      identification): the landed route-C witness records the canonical
      geometric-mean representative c_geo = 0.99470743... with
      c_geo/(1/(8pi)) = 24.9997244717 — within 1.1e-5 (relative) of
      25 = deg(5-isogeny)^2 = 5^2, exactly the square of the X0(5) degree
      certified in W5. RECORDED as a candidate discrete origin for the
      tau-scale, DOUBLE-GATED: (a) route C proved the ratio is
      normalization-carrying (it depends on the entry-[0,0]=1 convention
      of both Grams), so "25" is a candidate only if that convention is
      the natural one; (b) even then it is an observation, not a
      derivation. No tuning; the 1.1e-5 residual is reported as-is.

Scope guard: no fit; nothing wired; the tau-identification remains the
sole open categorical input; 1/(8pi) stays phase-4. Self-contained
(mpmath + fractions). mpmath dps 50 (+10 guard); no float64 in the
certification path.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-- Ref: [braden-northover-2012] SIGMA 8 (2012) 065
-- Ref: [silverman-1986] The Arithmetic of Elliptic Curves (CM j integral:
--       Thm II.6.1 in Silverman ATAEC / classical complex multiplication)
"""
import datetime
import hashlib
import itertools
import json
import os
import subprocess
import sys
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 60  # 50 target + 10 guard

J_A = Fraction(-121945, 32)   # j(tau0)   — Braden-Disney-Hogg, class 50a
J_B = Fraction(-25, 2)        # j(5*tau0)
TAU0_LIT = mp.mpc("-0.5", "0.186676")  # corpus literature value (6 digits)
CERT_TOL = mp.mpf(10) ** (-45)


def frac_to_mpf(x: Fraction):
    return mp.mpf(x.numerator) / mp.mpf(x.denominator)


def ej_model(j: Fraction):
    """Standard j-parametrized Q-rational Weierstrass model for j != 0, 1728:
    E_j : y^2 + xy = x^3 - 36/(j-1728) x - 1/(j-1728). Exact arithmetic."""
    d = j - 1728
    a1, a2, a3 = Fraction(1), Fraction(0), Fraction(0)
    a4 = Fraction(-36) / d
    a6 = Fraction(-1) / d
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    Delta = (c4 ** 3 - c6 ** 2) / 1728
    return (a1, a2, a3, a4, a6), c4, c6, Delta, c4 ** 3 / Delta


def reduce_fund(tau):
    """SL2(Z) reduction to the fundamental domain, canonical boundary
    representative Re = -1/2 (both +-1/2 are equivalent via T)."""
    for _ in range(200):
        n = int(mp.floor(mp.re(tau) + mp.mpf(1) / 2))
        tau = tau - n
        if mp.fabs(tau) < 1 - mp.mpf(10) ** (-50):
            tau = -1 / tau
        else:
            break
    if mp.re(tau) > mp.mpf("0.4999"):
        tau -= 1
    return tau


def j_of(tau):
    return 1728 * mp.kleinj(tau)


def invert_j_on_line(j_target: Fraction, guess):
    """Invert j on the boundary Re = -1/2 (real j < 0 lives there)."""
    jt = frac_to_mpf(j_target)
    f = lambda t: mp.re(j_of(mp.mpc(mp.mpf(-1) / 2, t))) - jt
    t = mp.findroot(f, guess)
    return mp.mpc(mp.mpf(-1) / 2, t), abs(f(t))


def periods_from_model(c4: Fraction, c6: Fraction, j_target: Fraction):
    """Lattice shape of the Q-model via AGM on the Weierstrass cubic roots;
    self-certified by j round-trip over all basis candidates. Returns
    (tau_fund, j_residual). Twist-independent (period RATIO only)."""
    g2 = frac_to_mpf(c4) / 12
    g3 = frac_to_mpf(c6) / 216
    roots = mp.polyroots([4, 0, -g2, -g3], maxsteps=200, extraprec=200)
    jt = frac_to_mpf(j_target)
    best = None
    for e1, e2, e3 in itertools.permutations(roots):
        try:
            s13 = mp.sqrt(e1 - e3)
            s12 = mp.sqrt(e1 - e2)
            s23 = mp.sqrt(e2 - e3)
            w1 = mp.pi / mp.agm(s13, s12)
            w2 = mp.pi / mp.agm(s13, s23)
        except Exception:
            continue
        for mult in (1, mp.mpc(0, 1), -1, mp.mpc(0, -1)):
            for num, den in ((w2, w1), (w1, w2)):
                tau = mult * num / den
                if mp.im(tau) <= 0:
                    continue
                t = reduce_fund(tau)
                err = abs(j_of(t) - jt)
                if best is None or err < best[1]:
                    best = (t, err)
    return best


def main() -> int:
    print("=" * 78)
    print(" B2 tau-scale, bean qou-m117: CM refuted -> Q-model/Weierstrass leg;")
    print(" (1,5,5,5) gate self-certified independent of Braden-Northover")
    print("=" * 78)

    assertions = []

    def check(name, passed, detail="", computed=None, expected=None,
              tolerance=None):
        entry = {"name": name, "passed": bool(passed), "detail": detail}
        if computed is not None:
            entry["computed"] = computed
        if expected is not None:
            entry["expected"] = expected
        if tolerance is not None:
            entry["tolerance"] = tolerance
        assertions.append(entry)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # ---- W1: the CM leg dies — j non-integral => no CM --------------------
    denA, denB = J_A.denominator, J_B.denominator
    no_cm = denA != 1 and denB != 1
    check(
        "W1_no_cm_j_nonintegral", no_cm,
        f"j(tau0) = {J_A} (denominator {denA}), j(5tau0) = {J_B} (denominator "
        f"{denB}): both NON-integral rationals. CM j-invariants are algebraic "
        f"integers (classical CM theory), so NEITHER Bring elliptic factor has "
        f"CM. The bean's literal CM route is CLOSED — scope-(a): kills the CM "
        f"mechanism only; the Q-model leg below carries the convention-bypass",
        computed=[denA, denB], expected="denominators != 1")

    # ---- W2: exact Q-models -----------------------------------------------
    _, c4A, c6A, DA, jrA = ej_model(J_A)
    _, c4B, c6B, DB, jrB = ej_model(J_B)
    model_ok = (jrA == J_A) and (jrB == J_B) and DA < 0 and DB < 0
    check(
        "W2_weierstrass_q_models_exact", model_ok,
        f"E_j models (exact Fractions): A: c4={c4A}, Delta sign neg; "
        f"B: c4={c4B}, Delta sign neg; c4^3/Delta == j round-trips EXACTLY "
        f"for both. Delta<0 = rhombic lattice, consistent with Re tau = -1/2",
        computed="exact Fraction round-trip", expected="c4^3/Delta == j")

    # ---- W4a: j-inversion (independent route) ------------------------------
    tauA_inv, resA = invert_j_on_line(J_A, mp.mpf("1.34"))
    tauB_inv, resB = invert_j_on_line(J_B, mp.mpf("0.933"))
    tA = mp.im(tauA_inv)
    tB = mp.im(tauB_inv)
    inv_ok = resA < CERT_TOL and resB < CERT_TOL
    check(
        "W4a_j_inversion_50dps", inv_ok,
        f"j-inversion on Re=-1/2: tau_A^fund = -1/2 + {mp.nstr(tA, 30)}i "
        f"(resid {mp.nstr(resA, 3)}), tau_B^fund = -1/2 + {mp.nstr(tB, 30)}i "
        f"(resid {mp.nstr(resB, 3)})",
        computed=[float(resA), float(resB)], expected=0.0,
        tolerance="1e-45")

    # ---- W3: AGM periods from the Q-models (no period-matrix input) --------
    tauA_agm, errA = periods_from_model(c4A, c6A, J_A)
    tauB_agm, errB = periods_from_model(c4B, c6B, J_B)
    agm_ok = (errA < CERT_TOL and errB < CERT_TOL
              and abs(tauA_agm - tauA_inv) < CERT_TOL
              and abs(tauB_agm - tauB_inv) < CERT_TOL)
    check(
        "W3_agm_periods_match_j_inversion", agm_ok,
        f"AGM lattice shape of the Q-models certifies against j-inversion: "
        f"|tau_A^AGM - tau_A^inv| = {mp.nstr(abs(tauA_agm - tauA_inv), 3)}, "
        f"|tau_B^AGM - tau_B^inv| = {mp.nstr(abs(tauB_agm - tauB_inv), 3)} "
        f"(j round-trip residuals {mp.nstr(errA, 3)}, {mp.nstr(errB, 3)}). "
        f"Twist-independent; NO Braden-Northover period matrix consumed",
        computed=[float(abs(tauA_agm - tauA_inv)),
                  float(abs(tauB_agm - tauB_inv))],
        expected=0.0, tolerance="1e-45")

    # ---- W4b: recover tau0 at 50 dps via the exact SL2(Z) word -------------
    # Reduction word of the literature tau0: gamma' = [[1,1],[-2,-1]] maps
    # tau0 -> tau_A^fund, so tau0 = gamma'^{-1}(tau_A^fund) = -1/2 + i/(4 t_A).
    tau0_rec = mp.mpc(mp.mpf(-1) / 2, 1 / (4 * tA))
    word_ok = abs(reduce_fund(tau0_rec) - tauA_inv) < CERT_TOL
    lit_ok = abs(tau0_rec - TAU0_LIT) < mp.mpf("2e-6")
    check(
        "W4b_tau0_recovered_matches_corpus", word_ok and lit_ok,
        f"tau0 = gamma'^(-1)(tau_A^fund) = -1/2 + i/(4 t_A) = "
        f"-0.5 + {mp.nstr(mp.im(tau0_rec), 30)}i; reduce(tau0)==tau_A^fund "
        f"({mp.nstr(abs(reduce_fund(tau0_rec) - tauA_inv), 3)}); matches the "
        f"corpus literature -0.5+0.186676i to the quoted 6 digits "
        f"(|diff| = {mp.nstr(abs(tau0_rec - TAU0_LIT), 3)}); Re(tau0) = -1/2 "
        f"exactly by the SL2(Z) word structure",
        computed=abs(tau0_rec - TAU0_LIT), expected=0.0,
        tolerance="2e-6")

    # ---- W5: X0(5) + the (1,5,5,5) gate, self-certified ---------------------
    five_iso = abs(reduce_fund(5 * tau0_rec) - tauB_inv)
    gate = 4 * tA * tB          # = Im(tau_B^fund)/Im(tau0_rec) = 5 exactly
    gate_dev = abs(gate - 5)
    x05_ok = five_iso < CERT_TOL and gate_dev < CERT_TOL
    check(
        "W5_x05_gate_1555_certified", x05_ok,
        f"reduce(5*tau0_rec) == tau_B^fund to {mp.nstr(five_iso, 3)} (the "
        f"X0(5) 5-isogeny, j-labelling j(tau0)={J_A}, j(5tau0)={J_B} "
        f"CONFIRMED); Im ratio Im(tau_B^fund)/Im(tau0_rec) = 4*t_A*t_B = "
        f"{mp.nstr(gate, 30)} — the (1,5,5,5) gate's ratio-5 certified at "
        f"50 dps INDEPENDENTLY of the Braden-Northover normalization",
        computed=gate_dev, expected=0.0, tolerance="1e-45")

    # ---- W6/W7: the honest tau-scale finding + the deg^2=25 observation ----
    here = os.path.dirname(os.path.abspath(__file__))
    routec_path = os.path.join(here, "..",
                               "alpha-em-b2-invariant-c.witness.json")
    with open(routec_path) as f:
        routec = json.load(f)
    c_geo = mp.mpf(routec["data"]["geometric_mean_c"]["value"])
    inv8pi = 1 / (8 * mp.pi)
    ratio = c_geo / inv8pi
    ratio_recorded = mp.mpf(
        routec["data"]["geometric_mean_c"]["ratio_to_inv8pi"])
    rel_dev_25 = abs(ratio / 25 - 1)
    obs_ok = (abs(ratio - ratio_recorded) < mp.mpf("1e-9")
              and rel_dev_25 < mp.mpf("5e-5"))
    check(
        "W7_deg25_scale_observation_recorded", obs_ok,
        f"route-C canonical representative c_geo = {mp.nstr(c_geo, 20)}; "
        f"c_geo/(1/(8pi)) = {mp.nstr(ratio, 15)} — within "
        f"{mp.nstr(rel_dev_25, 3)} (relative) of 25 = deg(5-isogeny)^2 = 5^2, "
        f"the square of the X0(5) degree certified in W5. RECORDED as a "
        f"candidate discrete origin for the tau-scale — OPEN, owner-level, "
        f"NO identification, DOUBLE-GATED: (a) the ratio is normalization-"
        f"carrying per route C's own refutation (entry-[0,0]=1 convention); "
        f"(b) observation, not derivation. Residual 1.1e-5 reported as-is, "
        f"not tuned",
        computed=rel_dev_25, expected=0.0, tolerance="5e-5")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "BEAN qou-m117 EXECUTED HONESTLY (scope-(a); no fit; nothing wired): "
        "(1) the literal CM leg is DEAD on arrival — both 50a j-invariants "
        "are non-integral rationals, and CM j-invariants are algebraic "
        "integers; recorded as a scope-(a) narrowing, not papered over. "
        "(2) The surviving Q-model leg WORKS: exact Q-rational Weierstrass "
        "models from j alone (Fraction round-trip exact), AGM periods from "
        "the models, and independent j-inversion agree to ~1e-50 and "
        "re-derive tau0 = -1/2 + i/(4 t_A) = -0.5+0.18667646...i (corpus "
        "6-digit match) plus the X0(5) 5-isogeny and the (1,5,5,5) gate's "
        "Im-ratio = 5 EXACTLY — the Braden-Northover convention is now "
        "certified independently, with zero period-matrix input. (3) What "
        "this does NOT fix, precisely: the Neron/Q-model normalization is "
        "per-CURVE; the absolute Hodge scale on H^{1,0}(Bring) still passes "
        "through the isogeny Jac(Bring) -> E_{5tau0}^3 x E_{tau0} with "
        "unknown pullback degree — but that freedom is now DISCRETE "
        "(isogeny degrees, natural support powers of 5). (4) Against that "
        "discrete set, the route-C gate ratio 24.9997244717 sits within "
        "1.1e-5 of 25 = deg(5-isogeny)^2 — recorded as a candidate discrete "
        "origin for the tau-scale, OPEN, owner-level, double-gated "
        "(normalization-carrying + observation-only). The tau-identification "
        "remains the sole open categorical input; 1/(8pi) stays phase-4."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                      cwd=here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "alpha-em-b2-cm-weierstrass-scale",
        "description": "Bean qou-m117: CM/Weierstrass tau-scale route. CM leg "
                       "refuted honestly (both 50a j-invariants non-integral "
                       "=> no CM); Q-model leg executed: exact Q-rational "
                       "Weierstrass models from j alone, AGM periods + "
                       "independent j-inversion recover tau0 = -1/2+i/(4 t_A) "
                       "(corpus match) and certify the X0(5) 5-isogeny + the "
                       "(1,5,5,5) gate Im-ratio = 5 exactly, independent of "
                       "the Braden-Northover normalization. Tau-scale gate "
                       "narrowed to a DISCRETE set (isogeny-degree pullbacks); "
                       "the route-C ratio 24.9997 vs 25 = deg(5-isogeny)^2 "
                       "recorded as a candidate discrete origin — OPEN, "
                       "owner-level, double-gated, no identification. "
                       "Nothing wired; 1/(8pi) stays phase-4.",
        "auditOnly": "docs/audits/2026-07-25-alpha-em-b2-cm-weierstrass-scale.md",
        "tier": "numerical-certified (50 dps, self-certifying j round-trips); "
                "the deg^2=25 row is an OBSERVATION (scope-(a), open)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "mpmath", "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "precisionMetadata": {"compute_dps": 60, "target_dps": 50,
                              "guard_digits": 10,
                              "certification_tolerance": "1e-45"},
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "j_tau0": str(J_A), "j_5tau0": str(J_B),
            "cm_status": "NO CM on either factor (non-integral j); CM leg "
                         "closed scope-(a)",
            "q_model_A": {"c4": str(c4A), "c6": str(c6A),
                          "Delta": str(DA), "j_roundtrip_exact": True},
            "q_model_B": {"c4": str(c4B), "c6": str(c6B),
                          "Delta": str(DB), "j_roundtrip_exact": True},
            "tau_A_fund": f"-1/2 + {mp.nstr(tA, 50)}i",
            "tau_B_fund": f"-1/2 + {mp.nstr(tB, 50)}i",
            "tau0_recovered": f"-1/2 + {mp.nstr(mp.im(tau0_rec), 50)}i "
                              f"(= -1/2 + i/(4 t_A), exact SL2(Z) word "
                              f"gamma' = [[1,1],[-2,-1]])",
            "tau0_literature": "-0.5 + 0.186676i (Braden-Disney-Hogg via "
                               "BringEllipticFactor.lean docstring)",
            "x05_isogeny_residual": mp.nstr(five_iso, 5),
            "gate_1555_im_ratio": mp.nstr(gate, 40),
            "gate_1555_im_ratio_deviation_from_5": mp.nstr(gate_dev, 5),
            "routec_c_geo": mp.nstr(c_geo, 25),
            "routec_ratio_to_inv8pi": mp.nstr(ratio, 15),
            "deg25_relative_deviation": mp.nstr(rel_dev_25, 5),
            "deg25_status": "candidate discrete origin (25 = deg(5-isogeny)^2)"
                            " — OPEN, owner-level, double-gated: "
                            "normalization-carrying + observation-only; "
                            "NO identification, NO tuning",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-m117 (parent qou-k42c)",
            "route_c_witness": "computations/alpha-em-b2-invariant-c.witness"
                               ".json (consumed read-only)",
            "ruling": "2026-07-19: the per-loop identification is not "
                      "derived-proved — respected; nothing asserted",
            "scope_guard": "no fit; no TauRhoHodgeLift instance; nothing "
                           "wired; 1/(8pi) phase-4",
        },
    }
    out = os.path.join(here, "alpha-em-b2-cm-weierstrass-scale.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        # `default=str` is what lets an mpf reach the file at full precision;
        # without it this hand-rolled dump raises "Object of type mpf is not
        # JSON serializable" and the producer is forced to float() its results
        # at the assertion, throwing the digits away. This is the same
        # serialization the canonical WitnessBuilder path uses
        # (qou_substrate/witness.py).
        json.dump(witness, f, indent=2, default=str)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
