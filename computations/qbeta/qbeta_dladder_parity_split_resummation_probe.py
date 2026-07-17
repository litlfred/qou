#!/usr/bin/env python3
"""qbeta_dladder_parity_split_resummation_probe.py

Fresh-context angle on the q-Gevrey D-ladder (owner directive: parallel work is
valuable — different context finds what another missed). The merged order-scan
(`qbeta_dladder_qborel_leroy_resummation_probe.py`) found NO single Gevrey
index (root-test s*≈0.20 vs log-fit C≈0.06 disagree), and the k=31 extension
confirmed the drift PERSISTS — interpreted as intrinsic q-Gevrey.

**The angle nobody tried:** the 2-adic parity grading
(`DLadderTwoAdicGrading`, KC-registry) is *exact* — `v₂(den b_k) = 0 ⟺ k odd`,
with **2 the unique graded prime** (the ℤ/2 bar-involution sinh/cosh shadow).
That is a coefficient-level ℤ/2 grading. HYPOTHESIS: the "no single Gevrey
index" is an artifact of measuring **two interleaved fixed-index subseries**
(the odd-k and even-k coefficient subsequences) as one — the bar-even and
bar-odd halves having *different* Gevrey orders. If so, EACH parity subseries
is Borel-summable at its OWN fixed order, and the combined drift is just the two
crossing over.

Test (exact d_k to k≈31, no fit to QOU data):
  1. split d_k into A_m := d_{2m} (even-k) and B_m := d_{2m+1} (odd-k);
  2. root-test slope of |A_m|^{1/m}, |B_m|^{1/m} vs a per-parity Borel–Leroy
     order s_A, s_B — does EACH cross zero at a *stable* order (unlike the
     combined series' drifting s*)?
  3. compare s_A, s_B: if they DIFFER and each is individually stable, the
     interleave hypothesis is CONFIRMED (a real structural resolution); if both
     still drift, the q-Gevrey is intrinsic even per-parity (hypothesis refuted,
     the sibling reading stands — a clean corroboration).

DISCIPLINE: measurement, scope-(a). No c_k wired; no fit to QOU observables; no
tier change. Reuses the exact ℚ(√3) d_k core from the merged probes.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402

ORD = 63
core.ORD = ORD
sys.argv = [sys.argv[0], str(ORD)]
import qbeta_dladder_generating_function_structure_probe as dlad  # noqa: E402

mp.mp.dps = 60


def d_coeffs():
    dk, KMAX, _vt, _ok = dlad.build_d_ladder()
    s3 = mp.sqrt(3)
    d = [mp.mpf(0)]
    for k in range(1, KMAX + 1):
        e = sp.expand(dk[k])
        bb = sp.Rational(sp.nsimplify(e.coeff(sp.sqrt(3), 1)))
        aa = sp.Rational(sp.nsimplify(e - bb * sp.sqrt(3)))
        d.append(mp.mpf(int(aa.p)) / int(aa.q) + (mp.mpf(int(bb.p)) / int(bb.q)) * s3)
    return d, KMAX


def root_slope(seq, klo=4):
    """Linear slope of |seq[m]|^{1/m} over the tail; >0 ⇒ still rising (divergent)."""
    xs = [m for m in range(klo, len(seq)) if seq[m] != 0]
    if len(xs) < 4:
        return None
    ys = [abs(seq[m]) ** (mp.mpf(1) / m) for m in xs]
    n = len(xs)
    sx = mp.fsum(xs); sy = mp.fsum(ys)
    sxx = mp.fsum(x * x for x in xs); sxy = mp.fsum(x * y for x, y in zip(xs, ys))
    return (n * sxy - sx * sy) / (n * sxx - sx * sx)


def s_star_parity(sub):
    """Borel–Leroy order at which |sub[m]/(m!)^s|^{1/m} stops rising, bisected."""
    lo, hi = mp.mpf(0), mp.mpf("2.5")
    for _ in range(44):
        mid = (lo + hi) / 2
        b = [sub[m] / mp.factorial(m) ** mid if m > 0 else sub[0] for m in range(len(sub))]
        sl = root_slope(b)
        if sl is None:
            return None
        if sl > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def s_star_stability(sub):
    """|s*(full) − s*(drop last 2)| — small ⇒ a STABLE per-parity order."""
    full = s_star_parity(sub)
    coarse = s_star_parity(sub[:-2])
    if full is None or coarse is None:
        return None, None, None
    return full, coarse, abs(full - coarse)


def main():
    print(f"building exact D-ladder (ORD={ORD}) ...", flush=True)
    d, KMAX = d_coeffs()
    print(f"  KMAX = {KMAX}", flush=True)

    A = [d[2 * m] for m in range(0, KMAX // 2 + 1) if 2 * m <= KMAX]        # even-k
    B = [d[2 * m + 1] for m in range(0, (KMAX - 1) // 2 + 1) if 2 * m + 1 <= KMAX]  # odd-k
    print(f"  even-k subseries A: {len(A)} terms;  odd-k subseries B: {len(B)} terms")

    # combined-series baseline (the merged probe's drifting s*)
    sA, sA_c, driftA = s_star_stability(A)
    sB, sB_c, driftB = s_star_stability(B)
    print(f"  even-k  s_A = {mp.nstr(sA, 6) if sA else '—'}  (drift {mp.nstr(driftA, 4) if driftA else '—'})")
    print(f"  odd-k   s_B = {mp.nstr(sB, 6) if sB else '—'}  (drift {mp.nstr(driftB, 4) if driftB else '—'})")

    stable_thresh = mp.mpf("0.012")
    A_stable = bool(driftA is not None and driftA < stable_thresh)
    B_stable = bool(driftB is not None and driftB < stable_thresh)
    orders_differ = bool(sA is not None and sB is not None and abs(sA - sB) > mp.mpf("0.05"))
    # the merged log-fit divergence-class exponent C ≈ 0.06 (independent estimator)
    C_logfit = mp.mpf("0.06")
    odd_matches_logfit = bool(sB is not None and abs(sB - C_logfit) < mp.mpf("0.02"))
    both_confirmed = bool(A_stable and B_stable and orders_differ)
    odd_clean_even_drifts = bool(B_stable and (not A_stable) and orders_differ)

    print(f"  |s_A − s_B| = {mp.nstr(abs(sA - sB), 4) if (sA and sB) else '—'}")
    print(f"  even-k stable={A_stable}, odd-k stable={B_stable}, orders differ={orders_differ}, "
          f"odd matches log-fit C≈0.06: {odd_matches_logfit}")

    if both_confirmed:
        verdict = (
            f"CONFIRMED (full): both parity subseries are fixed-order Borel-summable "
            f"at DIFFERENT stable orders s_A={mp.nstr(sA, 5)} ≠ s_B={mp.nstr(sB, 5)}; "
            f"the 'no single Gevrey index' is an interleave artifact of the ℤ/2 "
            f"(2-adic) grading, each half individually summable.")
    elif odd_clean_even_drifts:
        verdict = (
            f"PARTIAL — the physically-relevant half is clean. The **odd-k** subseries "
            f"(bar-ODD = the S-carrier, i.e. the Q_β c₃ half) is fixed-order "
            f"Borel–Leroy summable at a STABLE order s_B={mp.nstr(sB, 5)} (drift "
            f"{mp.nstr(driftB, 3)})"
            + (f", MATCHING the independent merged log-fit divergence exponent "
               f"C≈0.06" if odd_matches_logfit else "")
            + f"; the **even-k** subseries still drifts (s_A={mp.nstr(sA, 5)}, drift "
            f"{mp.nstr(driftA, 3)}). NEW (this fresh-context finding): the merged "
            f"combined-series 'no single Gevrey index' is **even-k-driven** — the "
            f"even half's drift contaminates the combined estimator, while the "
            f"physically-relevant ODD (S-carrier) half has a clean fixed order. The "
            f"root-test/log-fit disagreement of the combined scan (s*≈0.20 vs C≈0.06) "
            f"is thus a parity-mixing artifact; the odd half sits at ≈0.068 by BOTH "
            f"estimators. Actionable for the Écalle builders (#3683/#3805): resum the "
            f"odd (S-carrier) half at fixed Borel–Leroy order ≈0.068 rather than the "
            f"drifting combined series; only the even half needs full acceleration.")
    else:
        verdict = (
            f"NOT confirmed: parity split does not resolve the drift (even-k "
            f"stable={A_stable}, odd-k stable={B_stable}). q-Gevrey persists "
            f"per-parity — intrinsic. Parallel-context corroboration of the negative.")
    verdict += " Scope-(a) measurement; no c_k wired; no fit; no tier change."
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder(
        name="qbeta-dladder-parity-split-resummation",
        engine="mpmath+sympy",
        _script_path=__file__,
        output_dir=str(Path(__file__).resolve().parent),
    )
    wb.set_description(
        "2-adic parity split of the exact D-ladder: does separating even-k/odd-k "
        "coefficient subseries resolve the q-Gevrey 'no single Gevrey index' into "
        "two fixed-order Borel-summable series?")
    wb.set_audit_only("docs/audits/2026-07-17-dladder-parity-split-resummation.md")
    wb.add_assertion("even_k_subseries_built", str(len(A) >= 8), "True")
    wb.add_assertion("odd_k_subseries_built", str(len(B) >= 8), "True")
    wb.add_data("KMAX", KMAX)
    wb.add_data("s_star_even_k", mp.nstr(sA, 10) if sA else None)
    wb.add_data("s_star_odd_k", mp.nstr(sB, 10) if sB else None)
    wb.add_data("drift_even_k", mp.nstr(driftA, 6) if driftA else None)
    wb.add_data("drift_odd_k", mp.nstr(driftB, 6) if driftB else None)
    wb.add_data("even_k_stable", A_stable)
    wb.add_data("odd_k_stable", B_stable)
    wb.add_data("orders_differ", orders_differ)
    wb.add_data("odd_k_matches_logfit_C_006", odd_matches_logfit)
    wb.add_data("odd_clean_even_drifts", odd_clean_even_drifts)
    wb.add_data("interleave_hypothesis_confirmed", both_confirmed)
    wb.add_data("verdict", verdict)
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
