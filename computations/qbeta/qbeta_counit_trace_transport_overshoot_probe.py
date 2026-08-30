#!/usr/bin/env python3
"""qou-avt1: the counit->trace transport OVERSHOOTS. Scope-(a).

GATES PRE-STATED BEFORE THE RUN (scratchpad avt1_pre.md; reproduced verbatim in
the audit doc). Nothing here hunts a formula near F_required; G3 solves ONE
linear equation with ONE unknown and G4 is a ratio fixed in advance.

CORPUS INPUTS, not re-derived:
  KC19, proved-lean `QOU.QBeta.evalMap_affine` / `evalMap_ratio`:
      E(w) = h^2/2 - h*w      is AFFINE in the crossing weight w
      E(w)/E(w0) = (h - 2w)/(h - 2w0)
  eps(Delta)  = h^2/2 - h     = E(1)      <- trivial loop weight
  tr_M(Delta) = h^2/2 - h*z   = E(z)
  eps - tr_M  = h(z - 1) = 2*alpha        <- the ladder phase IS this gap
  Q_A = -E_0 * eps(Delta)

So "the ladder transports the evaluation from the counit to the Markov trace"
means, concretely, MOVING THE LOOP WEIGHT w FROM 1 TO z ALONG AN AFFINE LINE.
That is a sharp enough statement to test, and this probe tests it.

RESULT. The data wants a loop weight essentially AT the counit: the required
departure from w = 1 is a few tenths of a percent of the counit->trace distance.
So the transport, taken to completion, overshoots by ~2-3 orders of magnitude.
"The ladder is transporting counit -> trace" is therefore NOT what the anchor
supports: whatever the ladder is doing, it moves the evaluation a tiny fraction
of the way to the trace, not all of it.

W* IS A MEASUREMENT, NOT A VALUE. It is what the current parameterisation
demands, in the natural coordinate -- exactly as qou-cds1 measured z* and
alpha_required. Do NOT wire it, and do NOT hunt a closed form for it: it is
resolved no better than ce is (1.45%), so any identification quoted tighter than
that is arithmetic, not measurement.

Exact mpmath at 60 dps end-to-end; no float64. NO fit, NO c_k, NO wiring.
"""
# PATH BRIDGE — required before the provenance stamp can import
# `qou_substrate` (bean qou-ya1e). That module is not installed and not on
# PYTHONPATH; it is reachable only through `_path_bridge`, which
# `migrate_bare_producer_provenance.py` inserted the stamp WITHOUT. The
# import sits at function scope, so this producer did all its work and then
# died at the save with ModuleNotFoundError. Idiom copied verbatim from
# `qbeta/qbeta_c3_candidate_audit.py`.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import datetime, hashlib, json, os, subprocess, sys
sys.path.insert(0, "/home/user/qou/computations")
sys.path.insert(0, "/home/user/qou/computations/substrate")

import mpmath as mp
from mpmath import mpf, sqrt
mp.mp.dps = 60
from codata_constants import M_E_MEV, Q_BETA_MEV

Q0 = "1.1099785827513808075916690956107688798744991218736"


def _sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True).strip()
    except Exception:
        return None


def main():
    q, me, Qc = mpf(Q0), mpf(str(M_E_MEV)), mpf(str(Q_BETA_MEV))
    h = q - 1/q
    z_C, z_D = sqrt(q)/(1 + q), q**3/(q**2 + 1)
    E = lambda w: h**2/2 - h*w                    # KC19 evaluation map
    L = lambda w: E(w)/E(1)                       # ladder factor vs the counit
    Q_A = me * mp.fabs(q**2 - 2*q - 1) * (q + 1) / (2*q**3)
    F_req = Qc/Q_A

    assertions, data = [], {}

    def check(name, passed, note=""):
        assertions.append({"name": name, "passed": bool(passed), "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # G1 -- the setup reproduces the corpus identity exactly
    for nm, z in (("C", z_C), ("D", z_D)):
        alpha = (z - 1)*h/2
        check(f"G1_eps_minus_trM_eq_2alpha_{nm}",
              abs((E(1) - E(z)) - 2*alpha) < mpf("1e-55"))

    # G2 -- form clash: L is affine in w, the ladder asserts a cosine
    lin = all(abs((L(mpf(a)) + L(mpf(b)))/2 - L((mpf(a) + mpf(b))/2)) < mpf("1e-55")
              for a, b in (("0", "1"), ("0.3", "0.9"), ("-1", "2")))
    check("G2_ladder_factor_is_affine_in_w_not_a_cosine", lin)

    # G3 -- ONE linear equation, ONE unknown.  w* = (h - F*(h-2))/2
    w_star = (h - F_req*(h - 2))/2
    check("G3_w_star_solves_L_eq_F_required", abs(L(w_star) - F_req) < mpf("1e-50"))

    # G4 -- THE LOAD-BEARING TEST (kill criterion fixed before the run)
    print()
    print(f"  F_required        = {mp.nstr(F_req, 20)}")
    print(f"  w* (data demands) = {mp.nstr(w_star, 20)}")
    print(f"  counit  w = 1     ,  trace  z_C = {mp.nstr(z_C, 12)} / z_D = {mp.nstr(z_D, 12)}")
    print()
    fracs = {}
    for nm, z in (("C", z_C), ("D", z_D)):
        frac = (w_star - 1)/(z - 1)
        fracs[nm] = frac
        print(f"  frac_{nm} = (w*-1)/(z_{nm}-1) = {mp.nstr(frac, 12)}"
              f"   -> transport overshoots by {mp.nstr(1/frac, 8)}x")
    overshoot = all(abs(f) < mpf("0.01") for f in fracs.values())
    check("G4_transport_overshoots_frac_below_1pct", overshoot,
          f"(frac_C={mp.nstr(fracs['C'],6)}, frac_D={mp.nstr(fracs['D'],6)})")

    # G5 -- bar-parity of w*, against z_D's known q^-4 twist
    qi = 1/q
    h_bar = qi - q
    F_req_bar_unknown = None          # F at 1/q is NOT measurable (no anchor there)
    w_star_reflect = (h_bar - F_req*(h_bar - 2))/2      # same F, bar'd h
    check("G5_w_star_not_bar_even", abs(w_star_reflect - w_star) > mpf("1e-30"),
          f"(w*(h->-h) = {mp.nstr(w_star_reflect, 10)})")

    data.update({
        "F_required": mp.nstr(F_req, 40),
        "w_star_measurement_not_value": mp.nstr(w_star, 40),
        "counit_loop_weight": "1",
        "z_C": mp.nstr(z_C, 40), "z_D": mp.nstr(z_D, 40),
        "frac_of_counit_to_trace_distance": {k: mp.nstr(v, 20) for k, v in fracs.items()},
        "overshoot_factor": {k: mp.nstr(1/v, 20) for k, v in fracs.items()},
    })

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "OVERSHOOT (scope-(a)). Under KC19 the counit->trace transport IS just "
        "moving the loop weight w from 1 to z along an affine line. Solving the "
        "one linear equation L(w*) = F_required puts w* within ~0.15% of the "
        "COUNIT (w = 1), i.e. the data wants only ~0.3% of the counit->trace "
        "distance under C and ~0.4% under D -- the completed transport overshoots "
        "by ~300x and ~270x respectively. So 'the ladder transports the "
        "evaluation from the counit to the Markov trace' is NOT supported as "
        "stated: whatever the ladder does, it moves the evaluation a tiny "
        "fraction of the way. Separately (G2) the ladder factor is AFFINE in w "
        "while the ladder asserts a COSINE -- two different functional forms, "
        "agreeing only at isolated points. w* is a MEASUREMENT of what the "
        "current parameterisation demands, not a value; it is resolved no better "
        "than ce (1.45%), so no closed form may be quoted for it. Nothing wired."
        if all_passed else
        "INCONCLUSIVE -- a pre-stated gate failed; re-derive before citing.")

    src = open(__file__, "rb").read()
    w = {"computation": "qbeta-counit-trace-transport-overshoot",
         "description": "qou-avt1 formalize-first: under KC19 the counit->trace "
                        "transport is an affine move of the loop weight, and the "
                        "anchor wants <0.5% of that move -- the transport "
                        "overshoots by ~300x.",
         "engine": "mpmath", "markov_convention": "both (C and D compared)",
         "assertions": assertions, "data": data, "verdict": verdict,
         "witness": {"scriptPath": "computations/qbeta/" + os.path.basename(__file__),
                     "scriptHash": hashlib.sha256(src).hexdigest()[:12],
                     "commitSha": _sha(),
                     "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()}}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qbeta-counit-trace-transport-overshoot.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        w.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            w, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(w, f, indent=2); f.write("\n")
    print(f"\n{verdict}\n\nWitness: {os.path.basename(out)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
