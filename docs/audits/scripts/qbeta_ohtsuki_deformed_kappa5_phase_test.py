#!/usr/bin/env python3
"""
κ̃₅ tall ladder — the PREDECLARED phase-law falsification test.

The ξ-frame phase law (merged #3819) was identified from rungs κ̃₁..κ̃₄:

    arg κ̃_n = −n·arctan(t/π)   ⟺   κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ,   ξ = u + 2πi, t = u/2.

This probe extracts the FIFTH deformed rung κ̃₅(u_sub), which played no role in
the identification, and tests the law's advance prediction

    arg κ̃₅ = −5·arctan(t/π) = −0.166002393889…   (u_sub = 2 ln q₀, proton pin)

— a genuine falsification test: the prediction is stated before the extraction
(this docstring is committed with the prediction; the witness records both).
Secondary deliverables: κ̃₅'s magnitude extends the deformed tower for the
5-rung Borel–Padé, and the lower rungs re-extracted at the taller ladder must
reproduce the #3691 witness values (consistency).

Ladder: 11 points N = 512…524288 at dps 1050 (deformed-saddle cancellation
≈ 0.0017·N digits ⇒ ≈ 891 d at the top rung; adaptive truncation guard kept).
Everything else (exact deformed Habiro sum, Murakami-theorem regime,
branch-safe Re/Im channels) inherited from the sibling probes.

Discipline: 4₁ facts at a deformed meridian; no fit (the phase is a
parameter-free prediction, the magnitude is measured); no c_k wired; no tier
change.
"""
import datetime
import hashlib
import json
import os
import sys
import time

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from qbeta_ohtsuki_deformed_meridian_rungs import (  # noqa: E402
    _head_sha, _substrate_q, fit_im_channel, fit_re_channel,
)
from qbeta_ohtsuki_deformed_kappa3_tall_ladder import (  # noqa: E402
    log_jones_deformed_progress,
)

# AFTER the imports — the sibling modules set their own dps at import time.
mp.mp.dps = 1050


def main():
    q_p, _ = _substrate_q()
    u_p = 2 * mp.log(q_p)
    t_p = mp.log(q_p)
    phi = mp.atan(t_p / mp.pi)
    pred_arg_k5 = -5 * phi
    print(f"substrate meridian u = {mp.nstr(u_p, 20)}  (dps {mp.mp.dps})")
    print(f"PREDECLARED prediction:  arg κ̃₅ = −5·arctan(t/π) = {mp.nstr(pred_arg_k5, 15)}")

    Ns = [512 * 2 ** j for j in range(11)]   # 512 … 524288
    logJs, losses, kept = [], [], []
    t0 = time.time()
    for i, N in enumerate(Ns):
        lj, loss = log_jones_deformed_progress(N, u_p)
        if loss > mp.mp.dps - 40:
            print(f"    N={N} loss={float(loss):.1f}d exceeds headroom — truncating",
                  flush=True)
            break
        kept.append(N)
        logJs.append(lj)
        losses.append(loss)
        print(f"    [{i + 1}/{len(Ns)}] N={N:7d} loss={float(loss):7.1f}d "
              f"elapsed={time.time() - t0:8.1f}s", flush=True)
    Nk = kept

    re_l = [mp.re(x) for x in logJs]
    im_l = [mp.im(x) for x in logJs]
    fit = fit_re_channel(Nk, re_l, beta_pinned=True)
    fit_c1 = fit_re_channel(Nk[:-1], re_l[:-1], beta_pinned=True)
    imfit = fit_im_channel(Nk, im_l)
    imfit_c1 = fit_im_channel(Nk[:-1], im_l[:-1])

    rungs = {}
    for n in range(1, 6):
        kn = fit["kappa_re"][n - 1]
        knc = fit_c1["kappa_re"][n - 1] if n - 1 < len(fit_c1["kappa_re"]) else None
        conv = abs(kn - knc) if knc is not None else mp.inf
        conf = int(-mp.log10(conv)) if 0 < conv < 1 else (40 if conv == 0 else 0)
        ki = imfit["kappa_im"][n - 1] if n - 1 < len(imfit["kappa_im"]) else None
        kic = imfit_c1["kappa_im"][n - 1] if n - 1 < len(imfit_c1["kappa_im"]) else None
        convi = abs(ki - kic) if (ki is not None and kic is not None) else mp.inf
        confi = int(-mp.log10(convi)) if 0 < convi < 1 else (40 if convi == 0 else 0)
        rungs[n] = {"re": mp.nstr(kn, 25), "re_conf": conf,
                    "im": mp.nstr(ki, 25) if ki is not None else None,
                    "im_conf": confi,
                    "val": mp.mpc(kn, ki if ki is not None else 0)}
        print(f"  κ̃_{n} = {mp.nstr(kn, 15)} [{conf}d] + i·"
              f"{mp.nstr(ki, 10) if ki is not None else '—'} [{confi}d]", flush=True)

    # ---- the falsification test ----
    k5 = rungs[5]["val"]
    arg5 = mp.arg(k5)
    resid = arg5 - pred_arg_k5
    conf5 = min(rungs[5]["re_conf"], rungs[5]["im_conf"])
    # the phase is testable to roughly the rung's attained digits
    tol = mp.mpf(10) ** (-(max(conf5 - 1, 2)))
    passed = abs(resid) < tol
    print(f"\n  FALSIFICATION TEST:")
    print(f"    measured  arg κ̃₅ = {mp.nstr(arg5, 15)}")
    print(f"    predicted arg κ̃₅ = {mp.nstr(pred_arg_k5, 15)}")
    print(f"    residual = {mp.nstr(resid, 6)}  (tolerance 10^−{max(conf5 - 1, 2)} "
          f"from κ̃₅'s {conf5} confident digits)  →  "
          f"{'LAW SURVIVES' if passed else 'LAW FALSIFIED'}")

    # lower-rung consistency vs the #3691 tall-ladder witness
    k1_prior = mp.mpf("0.5873433873112124288453212")
    k3_prior = mp.mpf("3.956290802132388210604952")
    cons = (abs(mp.re(rungs[1]["val"]) - k1_prior) < mp.mpf("1e-15") and
            abs(mp.re(rungs[3]["val"]) - k3_prior) < mp.mpf("1e-7"))
    print(f"  lower-rung consistency vs #3691 witness: {cons}")

    verdict = (
        f"Predeclared phase-law test at rung 5: measured arg κ̃₅ = "
        f"{mp.nstr(arg5, 12)} vs predicted −5·arctan(t/π) = "
        f"{mp.nstr(pred_arg_k5, 12)}; residual {mp.nstr(resid, 4)} at κ̃₅ "
        f"precision {conf5}d → {'LAW SURVIVES' if passed else 'LAW FALSIFIED'}. "
        f"κ̃₅(u_sub) = {rungs[5]['re']} [{rungs[5]['re_conf']}d] + "
        f"i·{rungs[5]['im']} [{rungs[5]['im_conf']}d] extends the deformed tower "
        f"to 5 rungs. Lower rungs reproduce #3691 ({cons}). 4₁ facts; no fit "
        f"(parameter-free prediction); no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    assertions = [
        {"name": "phase_law_prediction_survives_rung5", "passed": bool(passed)},
        {"name": "lower_rungs_reproduce_3691", "passed": bool(cons)},
        {"name": "kappa5_resolved_3_digits", "passed": bool(conf5 >= 3)},
    ]
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-deformed-kappa5-phase-test",
        "description": "Predeclared falsification test of the xi-frame phase law "
                       "(merged #3819) at the fifth deformed rung: the law, "
                       "identified from rungs 1-4, predicts arg kappa~_5 = "
                       "-5*arctan(t/pi) in advance; this tall ladder (N<=524288, "
                       "dps 1050) extracts kappa~_5 and tests it. Also extends "
                       "the deformed tower for the 5-rung Borel-Pade.",
        "audit_only": True,
        "tier": "numerical (predeclared-prediction test)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
        "result": {
            "u_substrate": mp.nstr(u_p, 25),
            "Ns_kept": Nk,
            "max_loss_digits": mp.nstr(max(losses), 25),
            "predicted_arg_kappa5": mp.nstr(pred_arg_k5, 20),
            "measured_arg_kappa5": mp.nstr(arg5, 20),
            "residual": mp.nstr(resid, 10),
            "kappa5_conf_digits_re_im": [rungs[5]["re_conf"], rungs[5]["im_conf"]],
            "rungs": {str(n): {k: v for k, v in r.items() if k != "val"}
                      for n, r in rungs.items()},
            "verdict": verdict,
        },
        "context": {
            "axis": "bar-odd S / A_omega lane: xi-frame phase law falsification",
            "law_source": "#3819 (identified from rungs 1-4 only)",
            "prediction_predeclared": True,
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-deformed-kappa5-phase-test.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
