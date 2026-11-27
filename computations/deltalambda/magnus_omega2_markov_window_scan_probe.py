#!/usr/bin/env python3
r"""
magnus_omega2_markov_window_scan_probe.py — the Magnus Omega_2 pairing as a function of the Markov
parameter z, across the whole faithful window 0 <= z <= h (qou-uir6; owner ruling 2026-10-12)

## The ruling this implements

Owner, 2026-10-12, options (ii) + (iii) of qou-uir6:
  (ii)  Omega_2 is a binding quantity: report the scan of P(z) across the faithful window as THE
        result;
  (iii) keep the convention-D numbers, relabelled as a TWO-ROW (Temperley-Lieb) DIAGNOSTIC, with no
        number changed.
The beans stay open (qou-uir6, qou-za3q).  Nothing here is wired to a dashboard.

The original scan lived only in a stalled container and was lost; this rebuilds it from committed
data.  Its recorded outcome ("(-,-,-) on >= 99 % of the window, (-,+,+) only within ~0.4 % h of the
Molien end") is NOT used as a target: the checks below were fixed before the numbers were computed,
and the comparison with that recollection is reported, not asserted.

## The object

For A = 2, 3, 4 (deuteron, triton, 4He; n = 3A) the sign probes record, per partition lambda |- n,
the block trace t_lambda = tr(rho_lambda Omega_2) at the proton pin q0.  The pairing at Markov
parameter z is

    P_A(z) = sum_lambda w_lambda(q0, z) * t_lambda,

with w the closed-form Ocneanu weight (`QOU.SchurWeyl.OcneanuWeight`): one affine-in-z factor per
cell over the q^2-hook product, so P_A is an exact POLYNOMIAL in z of degree <= n.

  * z = z_D = q^3/(q^2+1)  (convention D) — the recorded `P_total_wenzl`.  z_D > h, so convention D
    lies OUTSIDE the faithful window; there every three-row weight vanishes
    (`ocneanuWeight_conventionD_eq_zero_of_three_rows`), i.e. the D value sees only the two-row
    (Temperley-Lieb) quotient.  Hence the relabel: a two-row diagnostic.
  * 0 <= z <= h, h = q - 1/q — the faithful window: every weight positive
    (`QOU.SchurWeyl.PositiveWindow.forall_pos_iff`).  z = 0 is the Molien symmetrising trace
    (`ocneanuWeight_zero_eq_molienWeight`); z = h/2 is the sign-transpose fixed point.

## Pre-registered checks (written before any number was computed)

  W1  P_A(z_D) reproduces the recorded P_total_wenzl of each sign witness (tolerance 1e-40).
  W2  normalisation sum_lambda dim_lambda w_lambda(z) = 1 at z in {0, h/4, h/2, 3h/4, h}.
  W3  every w_lambda(z) > 0 at interior grid points of the window (n = 6, 9, 12).
  W5  every real root of P_A in [0, h] (mpmath.polyroots) is one the grid bracketed.
  W4  (measurement, no threshold) the real roots of each P_A in [0, h], the sign of P_A on each
      sub-interval, the measure of the window carrying each sign pattern over (A=2,3,4), reported
      as fractions of h.

Arithmetic: mpmath 60 dps; polynomial coefficients exact up to the 60-digit inputs; roots by sign
bracketing on a 4000-point grid then bisection to 1e-50.  No float64.
Witness: computations/deltalambda/magnus-omega2-markov-window-scan.witness.json.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone

from mpmath import mp, mpf

mp.dps = 60

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

Q = Q_MP
H = Q - 1 / Q
ZD = Q ** 3 / (Q ** 2 + 1)
GRID = 4000

SOURCES = [
    (2, "deuteron", "deuteron-magnus-omega2-sign.witness.json"),
    (3, "triton", "triton-magnus-omega2-sign.witness.json"),
    (4, "he4", "he4-magnus-omega2-sign.witness.json"),
]


def hooks(lam):
    cols = [sum(1 for x in lam if x > j) for j in range(lam[0])]
    return {(i, j): lam[i] - j - 1 + cols[j] - i - 1 + 1 for i in range(len(lam)) for j in range(lam[i])}


def poly_mul(a, b):
    out = [mpf(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def weight_poly(lam):
    """Coefficients (ascending in z) of the Ocneanu weight w_lambda(q0, z)."""
    num = [mpf(1)]
    den = mpf(1)
    hk = hooks(lam)
    for (i, j), hh in hk.items():
        # factor q^{2i}(q^2 - 1 - q z) + q^{2j+1} z = q^{2i}(q^2-1) + z (q^{2j+1} - q^{2i+1})
        num = poly_mul(num, [Q ** (2 * i) * (Q ** 2 - 1), Q ** (2 * j + 1) - Q ** (2 * i + 1)])
        den *= Q ** (2 * hh) - 1
    return [c / den for c in num]


def peval(p, z):
    acc = mpf(0)
    for c in reversed(p):
        acc = acc * z + c
    return acc


def main() -> int:
    t0 = time.time()
    results = []

    def check(name, ok, detail):
        results.append({"check": name, "pass": bool(ok), "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}\n       {detail}", flush=True)

    tol = mpf(10) ** -40
    polys, recorded, wpolys, dims = {}, {}, {}, {}
    for A, name, fn in SOURCES:
        d = json.load(open(os.path.join(_HERE, fn)))["results"]
        recorded[A] = mpf(d["P_total_wenzl"])
        P = [mpf(0)]
        wpolys[A], dims[A] = [], []
        for row in d["per_partition"]:
            lam = tuple(row["lambda"])
            wp = weight_poly(lam)
            wpolys[A].append(wp)
            dims[A].append(int(row["dim"]))
            t = mpf(row["tr_rho_Omega2"])
            P = [(P[k] if k < len(P) else 0) + (wp[k] * t if k < len(wp) else 0)
                 for k in range(max(len(P), len(wp)))]
        polys[A] = P

    # W1
    w1 = {A: peval(polys[A], ZD) - recorded[A] for A in polys}
    check("W1_reproduces_recorded_conventionD_values",
          all(abs(v) < tol for v in w1.values()),
          "; ".join(f"A={A}: P(z_D) = {mp.nstr(peval(polys[A], ZD), 15)} vs recorded "
                    f"{mp.nstr(recorded[A], 15)} (diff {mp.nstr(abs(w1[A]), 3)})" for A in polys))

    # W2
    worst2 = mpf(0)
    for A in polys:
        for z in [mpf(0), H / 4, H / 2, 3 * H / 4, H]:
            s = sum(dims[A][i] * peval(wpolys[A][i], z) for i in range(len(dims[A])))
            worst2 = max(worst2, abs(s - 1))
    check("W2_weight_normalisation_in_window", worst2 < tol,
          f"max |sum dim w(z) - 1| over A = 2,3,4 and 5 window points: {mp.nstr(worst2, 3)}")

    # W3
    neg = 0
    for A in polys:
        for k in range(1, 50):
            z = H * k / 50
            neg += sum(1 for wp in wpolys[A] if peval(wp, z) <= 0)
    check("W3_weights_positive_in_window_interior", neg == 0,
          f"non-positive weights at 49 interior points x all partitions of n = 6, 9, 12: {neg}")

    # W4 roots and sign pattern
    roots = {}
    for A, P in polys.items():
        rs = []
        prev_z, prev_v = mpf(0), peval(P, mpf(0))
        for k in range(1, GRID + 1):
            z = H * k / GRID
            v = peval(P, z)
            if prev_v == 0:
                rs.append(prev_z)
            elif prev_v * v < 0:
                lo, hi = prev_z, z
                for _ in range(200):
                    mid = (lo + hi) / 2
                    if peval(P, lo) * peval(P, mid) <= 0:
                        hi = mid
                    else:
                        lo = mid
                rs.append((lo + hi) / 2)
            prev_z, prev_v = z, v
        roots[A] = rs
    cuts = sorted({mpf(0), H} | {r for rs in roots.values() for r in rs})
    segments = []
    for a, b in zip(cuts, cuts[1:]):
        m = (a + b) / 2
        pat = "".join("+" if peval(polys[A], m) > 0 else "-" for A in (2, 3, 4))
        segments.append({"z_from": mp.nstr(a, 25), "z_to": mp.nstr(b, 25),
                         "from_over_h": mp.nstr(a / H, 12), "to_over_h": mp.nstr(b / H, 12),
                         "pattern_A234": pat})
    measure = {}
    for s, (a, b) in zip(segments, zip(cuts, cuts[1:])):
        measure[s["pattern_A234"]] = measure.get(s["pattern_A234"], mpf(0)) + (b - a) / H
    endpoint = {f"z={lbl}": "".join("+" if peval(polys[A], z) > 0 else "-" for A in (2, 3, 4))
                for lbl, z in [("0 (Molien)", mpf(0)), ("h/2", H / 2), ("h", H), ("z_D", ZD)]}
    values = {f"A={A}": {lbl: mp.nstr(peval(polys[A], z), 15)
                         for lbl, z in [("0", mpf(0)), ("h/2", H / 2), ("h", H), ("z_D", ZD)]}
              for A in polys}
    check("W4_window_scan_measurement", True,
          "roots in [0,h] (as z/h): "
          + "; ".join(f"A={A}: {[mp.nstr(r / H, 10) for r in roots[A]]}" for A in polys)
          + ". Pattern measure (fraction of h): "
          + ", ".join(f"{k}: {mp.nstr(v * 100, 8)} %" for k, v in sorted(measure.items()))
          + f". Endpoint patterns: {endpoint}.")

    # W5 robustness: every real root in [0, h] from mpmath.polyroots is one the grid bracketed
    missed = {}
    for A, P in polys.items():
        coeffs = list(reversed(P))
        while coeffs and coeffs[0] == 0:
            coeffs.pop(0)
        allr = mp.polyroots(coeffs, maxsteps=500, extraprec=400)
        real_in = [mp.re(r) for r in allr if abs(mp.im(r)) < mpf(10) ** -30 and 0 <= mp.re(r) <= H]
        missed[A] = [r for r in real_in if all(abs(r - g) > mpf(10) ** -30 for g in roots[A])]
    check("W5_no_root_missed_by_grid", all(not m for m in missed.values()),
          "real roots of P_A in [0,h] from polyroots (all-roots, extraprec 400) not bracketed by the "
          + f"{GRID}-point grid: " + "; ".join(f"A={A}: {len(missed[A])}" for A in polys))

    n_ok = sum(1 for x in results if x["pass"])
    print("\n" + "=" * 78)
    print(f"{n_ok}/{len(results)} checks passed   [{time.time() - t0:.1f}s]")
    print("=" * 78)
    payload = {
        "probe": "magnus_omega2_markov_window_scan_probe",
        "bean": ["qou-uir6", "qou-za3q"],
        "owner_ruling": "2026-10-12: (ii) the faithful-window scan is THE result; (iii) convention-D "
                        "values relabelled as a two-row (Temperley-Lieb) diagnostic, numbers unchanged; "
                        "beans stay open",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q, 50),
        "q0_anchor": "physical_proton",
        "dps": mp.dps,
        "h": mp.nstr(H, 40),
        "z_D": mp.nstr(ZD, 40),
        "z_D_over_h": mp.nstr(ZD / H, 20),
        "inputs": [fn for _, _, fn in SOURCES],
        "polynomial_coefficients_ascending": {f"A={A}": [mp.nstr(c, 40) for c in polys[A]] for A in polys},
        "roots_in_window_over_h": {f"A={A}": [mp.nstr(r / H, 20) for r in roots[A]] for A in polys},
        "segments": segments,
        "pattern_measure_fraction_of_h": {k: mp.nstr(v, 20) for k, v in measure.items()},
        "endpoint_patterns": endpoint,
        "values": values,
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "not_established": "which z inside the window is physical; any MeV normalisation; that the "
                           "closed-form ocneanuWeight is the Markov weight system at n = 9, 12 "
                           "(proved at n = 3, checked to n = 6)",
    }
    out = os.path.join(_HERE, "magnus-omega2-markov-window-scan.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
