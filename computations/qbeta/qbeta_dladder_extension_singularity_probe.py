#!/usr/bin/env python3
"""qbeta_dladder_extension_singularity_probe.py

The "more terms" arm of the D-ladder q-Borel program (the follow-up explicitly
flagged in `qbeta_dladder_qborel_leroy_resummation_probe.py`): extend the exact
ℚ(√3) D-ladder past k=21 and re-measure the Borel–Leroy structure, to decide
whether the k=21 singularity-estimator inconsistency (dlog-Padé vs root-test)
is a finite-k shadow (shrinks with more terms) or structural q-Gevrey drift
(persists).

Measurements (scope-(a): measurement, NOT identification; no instanton action
claimed unless the two estimators agree at the extended k):
  1. exact d_k to the largest KMAX the ORD-extension affords (target k≈31);
  2. the divergence-class fit log|d_k| = A + Bk + C·k·log k on the extended
     range — does C stabilise or keep drifting (q-Gevrey signature)?
  3. the Borel–Leroy order scan s* (slope-zero crossing) at extended k vs the
     k=21 value ≈0.20;
  4. dlog-Padé singularity ρ(s*) vs root-test radius at extended k — the
     consistency gap vs its k=21 value.

No c_k wired; no fit to QOU observables; no tier change. Self-asserted
witness; exact rational core reused from the merged 07-13 probes.
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

ORD = 63          # was 43 (k≤21); 63 targets k≈31
core.ORD = ORD
# The generating-function module reads its ORD from sys.argv at import time
# (`int(sys.argv[1]) if len(sys.argv) > 1 else 43`) — pass it through argv so
# every internal series length is built consistently at the extended order.
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


def class_fit(d, kmax, klo=6):
    """Fit log|d_k| = A + B·k + C·k·log k over klo..kmax; return (A,B,C)."""
    rows, ys = [], []
    for k in range(klo, kmax + 1):
        rows.append([mp.mpf(1), mp.mpf(k), mp.mpf(k) * mp.log(k)])
        ys.append(mp.log(abs(d[k])))
    A = mp.matrix(rows)
    sol = mp.qr_solve(A, mp.matrix(ys))[0]
    return sol[0], sol[1], sol[2]


def root_slope(b, kmax, klo=8):
    xs = list(range(klo, kmax + 1))
    ys = [abs(b[k]) ** (mp.mpf(1) / k) for k in xs]
    n = len(xs)
    sx = mp.fsum(xs); sy = mp.fsum(ys)
    sxx = mp.fsum(x * x for x in xs); sxy = mp.fsum(x * y for x, y in zip(xs, ys))
    return (n * sxy - sx * sy) / (n * sxx - sx * sx)


def s_star(d, kmax):
    lo, hi = mp.mpf(0), mp.mpf(1)
    for _ in range(40):
        mid = (lo + hi) / 2
        b = [mp.mpf(0)] + [d[k] / mp.factorial(k) ** mid for k in range(1, kmax + 1)]
        if root_slope(b, kmax) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def dlog_pade_sing(b, kmax):
    """Nearest positive-real singularity of Σ b_k ζ^k via dlog-Padé (diagonal)."""
    c = [b[k] for k in range(1, kmax + 1)]
    # dlog series: f'/f coefficients
    n = len(c)
    dl = [c[1] / c[0] if n > 1 else mp.mpf(0)]
    # build power series of d/dζ log(Σ c_k ζ^{k-1}) numerically via ratio recursion
    f = c
    g = [mp.mpf(0)] * n
    for m in range(n - 1):
        acc = (m + 1) * f[m + 1] if m + 1 < n else mp.mpf(0)
        for j in range(m):
            acc -= g[j] * f[m - j]
        g[m] = acc / f[0]
    M = (n - 2) // 2
    if M < 2:
        return None
    A = mp.matrix(M, M)
    rhs = mp.matrix(M, 1)
    for i in range(M):
        for j in range(M):
            A[i, j] = g[M + i - 1 - j]
        rhs[i] = -g[M + i]
    try:
        qc = mp.lu_solve(A, rhs)
    except Exception:
        return None
    poly = [mp.mpf(1)] + [qc[j] for j in range(M)]
    roots = mp.polyroots(poly[::-1], maxsteps=200, extraprec=80, error=False)
    best = None
    for r in roots:
        if abs(mp.im(r)) < 1e-6 and mp.re(r) > 0:
            if best is None or mp.re(r) < best:
                best = mp.re(r)
    return best


def main():
    print(f"building exact D-ladder at ORD={ORD} ...", flush=True)
    d, KMAX = d_coeffs()
    print(f"  KMAX = {KMAX} (was 21)", flush=True)

    A_, B_, C_full = class_fit(d, KMAX)
    _, _, C_21 = class_fit(d, min(21, KMAX))
    print(f"  class fit C (k≤21) = {mp.nstr(C_21, 6)};  C (k≤{KMAX}) = {mp.nstr(C_full, 6)}")

    ss_21 = s_star(d, min(21, KMAX))
    ss_full = s_star(d, KMAX)
    print(f"  Borel–Leroy s* (k≤21) = {mp.nstr(ss_21, 6)};  s* (k≤{KMAX}) = {mp.nstr(ss_full, 6)}")

    b_full = [mp.mpf(0)] + [d[k] / mp.factorial(k) ** ss_full for k in range(1, KMAX + 1)]
    rho = dlog_pade_sing(b_full, KMAX)
    slope_at_s = root_slope(b_full, KMAX)
    # root-test implied radius at s*: |b_k|^{1/k} → 1/ρ_rt
    tail = [abs(b_full[k]) ** (mp.mpf(1) / k) for k in range(KMAX - 4, KMAX + 1)]
    rho_rt = 1 / (mp.fsum(tail) / len(tail))
    gap = (abs(rho / rho_rt - 1) if rho else None)
    print(f"  dlog-Padé ρ(s*) = {mp.nstr(rho, 8) if rho else 'none'};  "
          f"root-test ρ ≈ {mp.nstr(rho_rt, 8)};  gap = {mp.nstr(gap, 4) if gap else 'n/a'}")

    drift = abs(ss_full - ss_21)
    consistent = bool(gap is not None and gap < mp.mpf("0.15"))
    verdict = (
        f"D-ladder extended exactly to k={KMAX}. Divergence-class C: {mp.nstr(C_21, 4)}→"
        f"{mp.nstr(C_full, 4)}; Borel–Leroy s*: {mp.nstr(ss_21, 4)}→{mp.nstr(ss_full, 4)} "
        f"(drift {mp.nstr(drift, 3)}). "
        + (f"The dlog-Padé and root-test singularity estimates now AGREE to "
           f"{mp.nstr(gap, 3)} — the k=21 inconsistency was a finite-k shadow; the "
           f"resolved Borel-plane singularity is ρ ≈ {mp.nstr(rho, 8)} (measurement, "
           "not an identification; no instanton action claimed without a second method)."
           if consistent else
           f"The estimator inconsistency PERSISTS at k={KMAX} (gap "
           f"{mp.nstr(gap, 3) if gap else 'n/a'}) — consistent with structural q-Gevrey "
           "drift (no single Gevrey index), reinforcing that the honest resummation is "
           "the genuine Écalle acceleration / Φ_b state integral, not any fixed-order "
           "Borel–Leroy. Scope-(a) measurement.")
        + " No c_k wired; no fit; no tier change."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder(
        computation="qbeta-dladder-extension-singularity",
        description="Extend the exact D-ladder past k=21 (ORD=63) and re-measure "
                    "divergence class, Borel–Leroy order, and singularity-estimator "
                    "consistency — decides finite-k shadow vs structural q-Gevrey drift.",
        script_file=__file__,
    )
    wb.add_assertion("extended_past_21", KMAX > 21)
    wb.add_assertion("class_C_positive", bool(C_full > 0))
    wb.add_assertion("sstar_positive", bool(ss_full > 0))
    wb.set_result({
        "KMAX": KMAX,
        "C_k21": mp.nstr(C_21, 8), "C_full": mp.nstr(C_full, 8),
        "sstar_k21": mp.nstr(ss_21, 8), "sstar_full": mp.nstr(ss_full, 8),
        "sstar_drift": mp.nstr(drift, 6),
        "rho_dlog_pade": (mp.nstr(rho, 12) if rho else None),
        "rho_root_test": mp.nstr(rho_rt, 12),
        "estimator_gap": (mp.nstr(gap, 6) if gap else None),
        "estimators_consistent": consistent,
        "verdict": verdict,
    })
    wb.save(output_dir=str(Path(__file__).resolve().parent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
