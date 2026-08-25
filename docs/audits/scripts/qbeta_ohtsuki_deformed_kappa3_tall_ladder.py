#!/usr/bin/env python3
"""
κ̃₃(u_sub): the next odd deformed Ohtsuki rung at the substrate meridian —
tall-ladder extension of `qbeta_ohtsuki_deformed_meridian_rungs.py` (PR #3691).

The 9-point ladder (N ≤ 131072, dps 300) resolved κ̃₁ to 12 digits and κ̃₂
roughly. The rung-resolution limit is ladder HEIGHT (asymptotic truncation),
not working precision — so this probe runs a single tall ladder at the proton
substrate meridian only: 11 points N = 512…524288. The deformed-saddle
cancellation costs ≈ 0.0017·N decimal digits at u_sub (measured in #3691), so
the top rung needs ≈ 900 digits — dps 980 with headroom, adaptive truncation
kept as a guard.

Everything else (exact deformed Habiro sum, Murakami-theorem regime, branch-safe
Re/Im channels) is inherited by import from the sibling probe. Same discipline:
4₁ facts at a deformed meridian; no c_k wired; no fit; no tier change.
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
    _head_sha, _substrate_q, fit_im_channel, fit_re_channel, solve_basis,
)

# AFTER the import — the sibling module sets dps=300 at import time; the tall
# ladder needs ≈900 digits of cancellation headroom at N=524288.
mp.mp.dps = 980


def log_jones_deformed_progress(N, u, report_every=131072):
    """Same streaming sum as the sibling probe, with inner progress lines for
    the multi-minute top rungs (long-compute logging discipline)."""
    xi = mp.mpc(u, 0) + 2j * mp.pi
    r = mp.exp(xi / N)
    two_cosh_u = 2 * mp.cosh(mp.mpf(u))
    Q = mp.mpc(1)
    logP = mp.mpc(0)
    ref = mp.mpc(0)
    peak = mp.mpf(0)
    s = mp.mpc(1)
    t0 = time.time()
    for j in range(1, N):
        Q *= r
        g = two_cosh_u - (Q + 1 / Q)
        logP += mp.log(g)
        re = mp.re(logP)
        if re > peak:
            peak = re
        if re > mp.re(ref):
            s = s * mp.exp(ref - logP) + 1
            ref = logP
        else:
            s += mp.exp(logP - ref)
        if j % report_every == 0:
            el = time.time() - t0
            print(f"      … j={j}/{N} ({100 * j / N:.0f}%) elapsed={el:.0f}s "
                  f"eta={el * (N - j) / j:.0f}s", flush=True)
    logJ = ref + mp.log(s)
    # NOT float() — see the sibling probe: the downcast is what puts raw
    # float64 in the witness. Keep it mpf and serialize at emission.
    loss = (peak - mp.re(logJ)) / mp.log(10)
    return logJ, loss


def main():
    pi = mp.pi
    s3 = mp.sqrt(3)
    kappa1_exact_u0 = 11 * s3 * pi / 108
    kappa3_exact_u0 = mp.mpf(1081) / 21870 * s3 * pi ** 3

    q_p, _ = _substrate_q()
    u_p = 2 * mp.log(q_p)
    t_p = mp.log(q_p)
    print(f"substrate meridian u = {mp.nstr(u_p, 20)}  (dps {mp.mp.dps})")

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
        el = time.time() - t0
        print(f"    [{i + 1}/{len(Ns)}] N={N:7d} loss={float(loss):6.1f}d "
              f"elapsed={el:7.1f}s", flush=True)
    Nk = kept

    re_l = [mp.re(x) for x in logJs]
    im_l = [mp.im(x) for x in logJs]
    fit = fit_re_channel(Nk, re_l, beta_pinned=True)
    fit_c1 = fit_re_channel(Nk[:-1], re_l[:-1], beta_pinned=True)
    fit_c2 = fit_re_channel(Nk[:-2], re_l[:-2], beta_pinned=True)
    imfit = fit_im_channel(Nk, im_l)
    imfit_c1 = fit_im_channel(Nk[:-1], im_l[:-1])

    rungs = {}
    for n in (1, 2, 3, 4):
        kn = fit["kappa_re"][n - 1]
        knc = fit_c1["kappa_re"][n - 1] if n - 1 < len(fit_c1["kappa_re"]) else None
        knc2 = fit_c2["kappa_re"][n - 1] if n - 1 < len(fit_c2["kappa_re"]) else None
        conv = abs(kn - knc) if knc is not None else mp.inf
        conf = int(-mp.log10(conv)) if 0 < conv < 1 else (40 if conv == 0 else 0)
        ki = imfit["kappa_im"][n - 1] if n - 1 < len(imfit["kappa_im"]) else None
        kic = imfit_c1["kappa_im"][n - 1] if n - 1 < len(imfit_c1["kappa_im"]) else None
        convi = abs(ki - kic) if (ki is not None and kic is not None) else mp.inf
        confi = int(-mp.log10(convi)) if 0 < convi < 1 else (40 if convi == 0 else 0)
        rungs[n] = {
            "re": mp.nstr(kn, 25), "re_conf_digits": conf,
            "re_coarse2": mp.nstr(knc2, 25) if knc2 is not None else None,
            "im": mp.nstr(ki, 25) if ki is not None else None,
            "im_conf_digits": confi,
        }
        print(f"  κ̃_{n}(u_sub) = {mp.nstr(kn, 18)} [{conf}d] "
              f"+ i·{mp.nstr(ki, 12) if ki is not None else '—'} [{confi}d]",
              flush=True)

    k1 = fit["kappa_re"][0]
    k3 = fit["kappa_re"][2]
    k3_im = imfit["kappa_im"][2]
    k1_prior = mp.mpf("0.587343387311212")   # #3691 9-point ladder value
    k1_consistent = abs(k1 - k1_prior) < mp.mpf("1e-11")

    # the bar-odd finite-b series (2πb² = i·t): odd rungs enter Im 𝔙 with
    # alternating sign — Im[(i t)^1]κ₁ = t·κ₁, Im[(i t)^3]κ₃ = −t³·κ₃ (Re parts).
    lead1 = t_p * k1
    lead3 = -(t_p ** 3) * k3
    print(f"\n  finite-b bar-odd series at u_sub (Re-channel rungs):")
    print(f"    t·Re κ̃₁            = {mp.nstr(lead1, 12)}")
    print(f"    −t³·Re κ̃₃          = {mp.nstr(lead3, 12)}")
    print(f"    partial sum (n≤3)   = {mp.nstr(lead1 + lead3, 12)}")
    print(f"  κ₃(0) exact = (1081/21870)√3π³ = {mp.nstr(kappa3_exact_u0, 15)}; "
          f"κ̃₃(u_sub) shift = {mp.nstr(k3 - kappa3_exact_u0, 10)}")

    v_k1 = bool(k1_consistent)
    v_k3 = rungs[3]["re_conf_digits"] >= 4
    assertions = [
        {"name": "kappa1_consistent_with_3691_ladder", "passed": v_k1},
        {"name": "kappa3_resolved_4_digits", "passed": bool(v_k3)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        f"Tall ladder (N≤{Nk[-1]}, dps {mp.mp.dps}, {len(Nk)} pts) at the proton "
        f"substrate meridian: κ̃₃(u_sub) = {rungs[3]['re']} [{rungs[3]['re_conf_digits']}d] "
        f"+ i·{rungs[3]['im']} [{rungs[3]['im_conf_digits']}d] vs κ₃(0) = "
        f"(1081/21870)√3π³ = {mp.nstr(kappa3_exact_u0, 12)}. κ̃₁ reproduces the "
        f"#3691 value ({k1_consistent}). Finite-b bar-odd partial sum "
        f"t·κ̃₁ − t³·κ̃₃ = {mp.nstr(lead1 + lead3, 10)}. 4₁ facts; no c_k wired; "
        f"no fit; no tier change."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-deformed-kappa3-tall-ladder",
        "description": "κ̃₃(u) at the substrate meridian via a tall deformed "
                       "Habiro ladder (extends #3691's 9-point run; rung "
                       "resolution is ladder-height-limited). Feeds the odd "
                       "finite-b series t·κ̃₁ − t³·κ̃₃ + … for the bar-odd S.",
        "audit_only": True,
        "tier": "numerical (deformed higher-rung extraction)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "u_substrate": mp.nstr(u_p, 25),
            "Ns_kept": Nk,
            "max_loss_digits": mp.nstr(max(losses), 25),
            "rungs": rungs,
            "kappa1_prior_3691": mp.nstr(k1_prior, 18),
            "kappa3_u0_exact": "(1081/21870)*sqrt(3)*pi^3",
            "finite_b_odd_series": {
                "t_kappa1": mp.nstr(lead1, 15),
                "minus_t3_kappa3": mp.nstr(lead3, 15),
                "partial_sum_n_le_3": mp.nstr(lead1 + lead3, 15),
            },
            "verdict": verdict,
        },
        "context": {
            "axis": "bar-odd S route 2: odd deformed rungs at the substrate meridian",
            "builds_on": ["#3691 κ̃₁(u) 9-pt ladder", "#3628 κ₃(0) exact"],
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-deformed-kappa3-tall-ladder.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
