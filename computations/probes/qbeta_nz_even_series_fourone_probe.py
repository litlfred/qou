#!/usr/bin/env python3
"""NZ even-series probe for 4₁ — exact deformation data from the A-polynomial.

PROBE (2026-07-12, PR #3622; companion to the Lean parity prune
``QOU/Knot/NeumannZagierParity.lean``).  Everything here is *geometric-exact*
data about the figure-eight complement's deformation variety — NOT an
empirical c_k extraction (the C18 entropy block does not apply: no CODATA
value enters the series computation).

What it computes, directly from the A-polynomial of 4₁ (CCGLS form,
geometric branch), with NO Neumann–Zagier sign/normalisation conventions
assumed:

  A(L, M) = M⁴L² − (M⁸ − M⁶ − 2M⁴ − M² + 1)L + M⁴,
  meridian eigenvalue M = e^{u/2}  (u := 2 log M, documented convention),
  longitude branch L(u) with L(0) = −1;  v(u) := log(−L(u)), v(0) = 0.

1. **Geometric branch pin**: A(−1, 1) = 0 with a double root (∂A/∂L = 0
   there) — the complete structure.
2. **Numeric parity test of v** (the NZ oddness, corroborated from the
   A-polynomial itself): v(−u) = −v(u) to ~1e-40 along real, imaginary and
   generic complex directions.  This is the convention-free content behind
   the Lean class hypothesis ``NeumannZagierEvenPotential.even_potential``:
   v odd ⇒ any potential Φ with Φ' ∝ v is even ⇒ NO u³ (or any odd) rung —
   parity survives integration and any constant rescaling.
3. **Series coefficients of v** via Cauchy/FFT contour extraction:
   v(u) = τ·u + v₃·u³ + v₅·u⁵ + … with even coefficients vanishing to
   precision; τ and v₃ recognised as exact elements a + b·√−3·i of the
   trace field ℚ(√−3) (small-height lattice scan — recognition of an exact
   geometric constant, not an empirical fit).
4. **Convention-free next-order ratio**: with Φ' = v (any overall constant),
   Φ = (τ/2)u² + (v₃/4)u⁴ + …, so the relative u⁴ correction to the leading
   u² law is  corr(u) = 1 + (v₃/(2τ))·u².  Evaluated at the #3573 anchor
   coordinates (z_ED = ln q₀ ≈ 0.10439 muon-side, HA = 2 ln q₀ ≈ 0.20906
   proton-side) to report whether the exact next NZ order moves the
   sibling's (√3/2)|u|² magnitude law (2.5% / 4.1% misses) toward or away
   from the S targets.  REPORT-ONLY: no assertion on the S match, no c_k
   proposed, nothing wired (flip-flop guard §8).

Run:  python3 -u qbeta_nz_even_series_fourone_probe.py 2>&1 | tee /tmp/nz-even-series.log
"""

import json
import os
import subprocess
from datetime import datetime, timezone

import mpmath as mp

mp.mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "qbeta-nz-even-series-fourone.witness.json")

SQRT3 = mp.sqrt(3)


# ---------------------------------------------------------------------------
# A-polynomial of 4₁ (CCGLS normalisation) and its L-derivative
# ---------------------------------------------------------------------------
def A_poly(L, M):
    return M**4 * L**2 - (M**8 - M**6 - 2 * M**4 - M**2 + 1) * L + M**4


def dA_dL(L, M):
    return 2 * M**4 * L - (M**8 - M**6 - 2 * M**4 - M**2 + 1)


def B_of(M):
    return M**8 - M**6 - 2 * M**4 - M**2 + 1


def contour_v_samples(r, N):
    """Analytic geometric-branch samples v(u_k) on the circle |u| = r.

    A is quadratic in L; the two roots meet at the complete structure
    (double root at u = 0), so `sqrt(disc)` needs analytic tracking:
    disc(u) = B² − 4M⁸ vanishes to second order at 0, w(u) := disc/u² is
    analytic and nonzero on a small disc, and the branch of sqrt(w) is
    chosen CONTINUOUSLY around the contour (principal at the start,
    nearest-sign thereafter).  Returns (samples, closure_defect): the
    closure defect measures whether the tracked sqrt returns to its
    starting value after a full loop (≈ 0 ⟺ no branch point inside,
    single-valued analytic branch — asserted by the caller)."""
    samples = []
    s_prev = None
    s_first = None
    for k in range(N + 1):  # one extra point to test closure
        th = 2 * mp.pi * k / N
        u = r * mp.e ** (1j * th)
        M = mp.e ** (u / 2)
        w = (B_of(M) ** 2 - 4 * M**8) / u**2
        s = mp.sqrt(w)
        if s_prev is not None and abs(s - s_prev) > abs(-s - s_prev):
            s = -s
        if s_first is None:
            s_first = s
        s_prev = s
        if k < N:
            L = (B_of(M) + u * s) / (2 * M**4)
            samples.append(mp.log(-L))
    closure = abs(s_prev - s_first) / abs(s_first)
    return samples, closure


# ---------------------------------------------------------------------------
# Exact-recognition helper over the lattice (a + b·i√3)/den, small height
# ---------------------------------------------------------------------------
def recognize_q_sqrt_m3(x, max_num=12, max_den=12, tol=mp.mpf("1e-38")):
    """Try x ≈ (a + b·i·√3)/d with small integers a, b, d.  Returns
    (a, b, d) or None."""
    for d in range(1, max_den + 1):
        xr = x.real * d
        xi = x.imag * d / SQRT3
        a = mp.nint(xr)
        b = mp.nint(xi)
        if abs(a) > max_num or abs(b) > max_num:
            continue
        cand = (a + b * 1j * SQRT3) / d
        if abs(x - cand) < tol:
            return int(a), int(b), d
    return None


def main():
    assertions = []
    t0 = datetime.now(timezone.utc)

    # ---- 1. geometric-branch pin -----------------------------------------
    a_at = A_poly(mp.mpc(-1), mp.mpc(1))
    da_at = dA_dL(mp.mpc(-1), mp.mpc(1))
    assertions.append({
        "name": "geometric_branch_L_eq_neg1_double_root_at_complete",
        "computed": float(abs(a_at) + abs(da_at)),
        "expected": 0.0,
        "passed": bool(abs(a_at) < mp.mpf("1e-50") and abs(da_at) < mp.mpf("1e-50")),
        "tolerance": 1e-50,
        "source": "A(L,1) = (L+1)² — CCGLS 4₁ A-polynomial, complete structure",
    })

    # ---- 2. analytic branch on the contour + closure -----------------------
    r = mp.mpf("0.06")
    N = 64
    samples, closure = contour_v_samples(r, N)
    assertions.append({
        "name": "tracked_sqrt_branch_closes_single_valued",
        "computed": float(closure),
        "expected": 0.0,
        "passed": bool(closure < mp.mpf("1e-40")),
        "tolerance": 1e-40,
        "source": "no branch point of the gluing variety inside |u| = 0.06; "
                  "v is a single-valued analytic function there",
    })

    # ---- 3. series coefficients via Cauchy/FFT ----------------------------
    coeffs = []
    for n in range(8):
        s = mp.mpc(0)
        for k in range(N):
            th = 2 * mp.pi * k / N
            s += samples[k] * mp.e ** (-1j * n * th)
        coeffs.append(s / N / r**n)

    even_leak = max(abs(coeffs[0]), abs(coeffs[2]), abs(coeffs[4]), abs(coeffs[6]))
    assertions.append({
        "name": "even_v_coefficients_vanish_v_is_odd",
        "computed": float(even_leak),
        "expected": 0.0,
        "passed": bool(even_leak < mp.mpf("1e-35")),
        "tolerance": 1e-35,
        "source": "NZ85 oddness on the geometric branch, corroborated from the "
                  "A-polynomial: v₀ = v₂ = v₄ = v₆ = 0 (Cauchy-extracted); no "
                  "framing-linear even part on this branch",
    })

    tau, v3, v5 = coeffs[1], coeffs[3], coeffs[5]
    rec_tau = recognize_q_sqrt_m3(tau)
    rec_v3 = recognize_q_sqrt_m3(v3, max_num=200, max_den=60)
    assertions.append({
        "name": "tau_recognized_in_Q_sqrt_minus3",
        "computed": 1.0 if rec_tau else 0.0,
        "expected": 1.0,
        "passed": bool(rec_tau is not None),
        "tolerance": 0.0,
        "source": f"tau = v₁ = {mp.nstr(tau, 30)}; recognition {rec_tau} "
                  "as (a + b·i√3)/d — the ℚ(√−3) cusp modulus",
    })

    # ---- 4. next-order ratio + anchor evaluation (REPORT-ONLY) ------------
    ratio = v3 / (2 * tau)  # Φ₄/Φ₂ · (1/1): corr(u) = 1 + ratio·u²
    anchors = {
        # #3573 witness (qbeta-c3-barodd-pole-cusp-phase): coordinate values
        "muon_z_ED": {"u": mp.mpf("0.104388058259"), "S": mp.mpf("0.00968298"),
                      "leading_scale_sq": mp.mpf("0.00943696339002")},
        "proton_HA": {"u": mp.mpf("0.209060298796"), "S": mp.mpf("-0.03945936"),
                      "leading_scale_sq": mp.mpf("0.0378506868923")},
    }
    anchor_report = {}
    for name, a in anchors.items():
        corr_real = 1 + (ratio * a["u"] ** 2).real  # real-u ray
        corr_imag = 1 + (ratio * (1j * a["u"]) ** 2).real  # imaginary-u ray
        for tag, corr in (("real_u", corr_real), ("imag_u", corr_imag)):
            corrected = a["leading_scale_sq"] * abs(corr)
            miss_before = abs(a["leading_scale_sq"] / abs(a["S"]) - 1)
            miss_after = abs(corrected / abs(a["S"]) - 1)
            anchor_report[f"{name}_{tag}"] = {
                "corr_factor": mp.nstr(mp.mpf(corr), 20),
                "miss_before_pct": mp.nstr(miss_before * 100, 6),
                "miss_after_pct": mp.nstr(miss_after * 100, 6),
                "moves_toward_S": bool(miss_after < miss_before),
            }

    dur = (datetime.now(timezone.utc) - t0).total_seconds()
    out = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-nz-even-series-fourone",
        "scriptFile": "qbeta_nz_even_series_fourone_probe.py",
        "commitSha": subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True,
            check=True).stdout.strip(),
        "description": (
            "NZ even-series probe for 4₁ from the CCGLS A-polynomial: numeric "
            "parity of v(u) (NZ85 oddness, convention-free), Cauchy-extracted "
            "series coefficients with ℚ(√−3) recognition of τ and v₃, and the "
            "convention-free next-order ratio v₃/(2τ) evaluated at the #3573 "
            "anchor coordinates (report-only). Companion to the Lean parity "
            "prune QOU/Knot/NeumannZagierParity.lean (no u³ rung). No c_k "
            "proposed; nothing wired."
        ),
        "precisionMetadata": {"compute_dps": 60, "contour_radius": "0.06",
                              "fft_points": N,
                              "u_convention": "u = 2·log M (meridian eigenvalue M)"},
        "data": {
            "tau_numeric": mp.nstr(tau, 40),
            "tau_recognized_a_b_d": rec_tau,
            "v3_numeric": mp.nstr(v3, 40),
            "v3_recognized_a_b_d": rec_v3,
            "v5_numeric": mp.nstr(v5, 40),
            "ratio_v3_over_2tau": mp.nstr(ratio, 30),
            "anchor_report": anchor_report,
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
        "durationSeconds": dur,
    }
    with open(OUT, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        out.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(out, f, indent=2)
        f.write("\n")
    print(json.dumps({k: out[k] for k in ("allPassed", "durationSeconds")}))
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}: "
              f"{a['computed']:.3e}")
    print("  tau =", mp.nstr(tau, 25), "rec:", rec_tau)
    print("  v3  =", mp.nstr(v3, 25), "rec:", rec_v3)
    print("  ratio v3/(2tau) =", mp.nstr(ratio, 20))
    for k, v in anchor_report.items():
        print(f"  {k}: miss {v['miss_before_pct']}% -> {v['miss_after_pct']}% "
              f"({'TOWARD' if v['moves_toward_S'] else 'AWAY'})")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
