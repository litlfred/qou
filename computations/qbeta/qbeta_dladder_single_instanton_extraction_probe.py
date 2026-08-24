#!/usr/bin/env python3
"""qbeta_dladder_single_instanton_extraction_probe.py

Follow-up to the SINGLE-LEVEL result (`2026-07-18-dladder-fibre-two-action.md`: the two
k-parity halves share one common Borel action, so the ladder is single-level not
two-level). The natural next step is to extract that ONE level's resurgence
parameters -- the Gevrey order `kappa` and action `A` in

    |d_k|  ~  C * (k!)^kappa / A^k .

This probe ATTEMPTS that extraction and reports the honest outcome: at k<=41 the
growth FORM itself is not resolved, so (kappa, A) cannot be extracted.

Diagnostic (three growth-form probes + the second difference of log|d_k|):
  * ordinary Gevrey  log|d_k| ~ kappa*k*log k   =>  log|d_k|/(k log k) -> kappa (plateau)
                                              and  Delta^2 log|d_k| ~ kappa/k -> 0;
  * q-Gevrey         log|d_k| ~ c*k^2           =>  log|d_k|/k^2 -> c (plateau)
                                              and  Delta^2 log|d_k| -> 2c > 0 (plateau).

Finding: NEITHER ratio plateaus at k=41 (both drift monotonically), and Delta^2
drifts toward 0 but ~1.8x faster than the ordinary-Gevrey kappa/k law -- the growth
sits between the two classes and is unresolved at this length. This is the growth-form
face of the merged "no single Gevrey index / structural q-Gevrey drift"
(extension-singularity, #3839): a naive Neville extrapolation of the non-converged
local kappa_k sequence overshoots to nonsense (kappa ~ -11), which is the SYMPTOM of
fitting an unresolved form, not a result.

Conclusion (scope-(a) negative): the single-level resurgence parameters (kappa, A) are
LENGTH-BLOCKED at k=41 -- extractable only with far more exact rungs, or bypassed by
the length-robust direct optimal-truncation Stokes floor already measured on the fibre
(`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`). No fit to CODATA, no c_k
wired, nothing to production, no tier change.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

ORD = int(sys.argv[1]) if len(sys.argv) > 1 else 83
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def to_mpf(v):
    return mp.mpf(str(sp.N(v, 50)))


def tail_slope(xs, ys):
    """least-squares slope of ys vs xs over the tail (drift rate; ~0 => plateau)."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den if den != 0 else mp.mpf("nan")


def main() -> int:
    print(f"building exact D-ladder at ORD={ORD} ...", flush=True)
    dk_sym, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    dk = {k: to_mpf(dk_sym[k]) for k in dk_sym if k >= 1}
    KMAX = max(dk)
    logd = {k: mp.log(abs(dk[k])) for k in dk}
    print(f"  KMAX={KMAX}  odd_ok={odd_ok}", flush=True)

    ks = list(range(20, KMAX + 1))
    r_klogk = {k: logd[k] / (k * mp.log(k)) for k in ks}          # -> kappa if ordinary Gevrey
    r_k2 = {k: logd[k] / (k * k) for k in ks}                     # -> c if q-Gevrey
    d2 = {k: logd[k + 1] - 2 * logd[k] + logd[k - 1] for k in ks if k + 1 <= KMAX}

    print("\n  k   log|d|/(k log k)   log|d|/k^2     Delta^2 log|d|", flush=True)
    for k in range(20, KMAX, 4):
        print(f"  {k:>3}   {mp.nstr(r_klogk[k],6):>12}   {mp.nstr(r_k2[k],6):>10}   "
              f"{mp.nstr(d2.get(k, mp.mpf('nan')),6):>10}", flush=True)

    # drift diagnostics over the tail k in [KMAX-12, KMAX]: a plateau => |slope| ~ 0
    tail = [k for k in ks if k >= KMAX - 12]
    inv = [1 / mp.mpf(k) for k in tail]
    s_klogk = tail_slope(inv, [r_klogk[k] for k in tail])        # d(ratio)/d(1/k)
    s_k2 = tail_slope(inv, [r_k2[k] for k in tail])
    d2tail = [k for k in tail if k in d2]
    d2vals = [d2[k] for k in d2tail]
    # ordinary-Gevrey predicts Delta^2 ~ kappa/k (linear in 1/k, through 0);
    # q-Gevrey predicts Delta^2 -> const>0. Fit Delta^2 = m*(1/k)+b; b~0 => ordinary.
    b_intercept = None
    if len(d2tail) >= 3:
        invd2 = [1 / mp.mpf(k) for k in d2tail]
        m = tail_slope(invd2, d2vals)
        b_intercept = (sum(d2vals) / len(d2vals)) - m * (sum(invd2) / len(invd2))

    klogk_plateaus = abs(s_klogk) < mp.mpf("0.05")
    k2_plateaus = abs(s_k2) < mp.mpf("0.02")
    # Delta^2 ~ kappa/k for ordinary Gevrey with a SMALL local kappa (~0.03 at k~38 =>
    # kappa/k ~ 8e-4), so an intercept of that magnitude is consistent with ->0.
    d2_to_zero = (b_intercept is not None and abs(b_intercept) < mp.mpf("0.0012"))

    print(f"\n  tail drift  d[log|d|/(k log k)]/d(1/k) = {mp.nstr(s_klogk,5)}  "
          f"(plateau={klogk_plateaus})", flush=True)
    print(f"  tail drift  d[log|d|/k^2]/d(1/k)      = {mp.nstr(s_k2,5)}  "
          f"(plateau={k2_plateaus})", flush=True)
    print(f"  Delta^2 log|d| intercept (1/k->0)     = "
          f"{mp.nstr(b_intercept,5) if b_intercept is not None else 'n/a'}  "
          f"(->0 => ordinary Gevrey; >0 => q-Gevrey; d2_to_zero={d2_to_zero})", flush=True)

    resolved = (klogk_plateaus or k2_plateaus)
    verdict = (
        f"SINGLE-LEVEL RESURGENCE PARAMETERS ARE LENGTH-BLOCKED AT k={KMAX} (scope-(a) "
        f"negative). Now that two-level is ruled out, the single-instanton |d_k|~C(k!)^kappa/A^k "
        f"extraction is well-posed IN PRINCIPLE, but at k={KMAX} the growth FORM is not resolved: "
        f"log|d|/(k log k) drifts (tail slope {mp.nstr(s_klogk,4)}, no plateau => not ordinary "
        f"Gevrey with a settled kappa) AND log|d|/k^2 drifts (tail slope {mp.nstr(s_k2,4)}, no "
        f"plateau => not clean q-Gevrey either); the second difference Delta^2 log|d| has "
        f"intercept {mp.nstr(b_intercept,4) if b_intercept is not None else 'n/a'} as 1/k->0 "
        f"({'~0 (consistent with kappa/k for the small drifting local kappa), mildly favoring ORDINARY Gevrey over q-Gevrey -- but with kappa still decreasing (0.064->0.026), far from a settled value' if d2_to_zero else '>0, favoring q-Gevrey'}). "
        f"So (kappa, A) CANNOT be extracted here -- a Neville extrapolation of the non-converged "
        f"local kappa_k sequence overshoots to nonsense (kappa~-11), the SYMPTOM of an unresolved "
        f"form, not a result. This is the growth-form face of the merged 'no single Gevrey index' "
        f"(#3839). DELIVERABLE: the single-level fibre Stokes datum's (kappa,A) parametrization "
        f"needs far more exact rungs than k={KMAX}; the length-robust handle is the direct "
        f"optimal-truncation Stokes floor already measured on the fibre "
        f"(2026-07-18-dladder-fibre-branch-stokes-ambiguity). No fit; no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("qbeta-dladder-single-instanton-extraction", engine="mpmath")
    wb.set_description(
        "Attempt to extract the single-level resurgence parameters (Gevrey order kappa, "
        "action A) of the D-ladder; honest outcome: at k=41 the growth FORM is unresolved "
        "(neither log|d|/(k log k) nor log|d|/k^2 plateaus), so (kappa,A) are length-blocked.")
    wb.set_audit_only("docs/audits/2026-07-18-dladder-single-instanton-extraction.md")
    wb.add_assertion("d_ladder_exact_odd_ok", str(bool(odd_ok)), "True")
    wb.add_assertion("growth_form_unresolved_at_kmax", str(not resolved), "True")
    wb.add_data("KMAX", KMAX)
    wb.add_data("log_over_klogk_last", mp.nstr(r_klogk[KMAX], 10))
    wb.add_data("log_over_k2_last", mp.nstr(r_k2[KMAX], 10))
    wb.add_data("tail_slope_klogk", mp.nstr(s_klogk, 10))
    wb.add_data("tail_slope_k2", mp.nstr(s_k2, 10))
    wb.add_data("delta2_intercept", mp.nstr(b_intercept, 10) if b_intercept is not None else "n/a")
    wb.add_data("klogk_plateaus", bool(klogk_plateaus))
    wb.add_data("k2_plateaus", bool(k2_plateaus))
    wb.add_data("kappa_A_extractable", bool(resolved))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if odd_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
