#!/usr/bin/env python3
"""A6.4: the W9 Borel function DERIVED — exact resummed formula, the
pole ladder at w = −q₀ᵏ, and the pole-split regularized D_odd.

THE DERIVATION (this session; replaces the A6.2/A6.3 measurements with
a closed form). With a = e^{t/2}, q̄ = a² = q₀, q̃ = q̄⁻¹, the balanced-
binomial inversion [n,k]_{q̄} = q̄^{k(n−k)}·[n,k]_{q̃} collapses the W9
transform T̂_n = C_n(q̄)(q̄;q̄)_n²a₀^{5n²+7n}: the quadratic AND linear
exponents cancel identically, leaving the exact, cancellation-free

    (−1)ⁿ·T̂_n = (q̃;q̃)_n² · Σ_{k=0}^n q̃^{k(n+1)}·[n,k]_{q̃}.       (★)

Consequences (each gated below):
  * c∞ = lim (−1)ⁿT̂_n = (q̃;q̃)_∞²  — the A6.3 Aitken plateau
    1.230766e-12 is DERIVED (k = 0 term; all other k → 0);
  * the transient ratio is exactly q̃ = 1/q₀ (A6.3 measured 0.90086 —
    the k = 1 term q̃^{n+1}·[n,1]_{q̃});
  * ĝ(w) = Σ T̂_n wⁿ has a POLE LADDER: the k-th term of (★) sums to a
    geometric-type family with pole at w = −q̃^{−k} = −q₀ᵏ — the w = −1
    "singularity" is the k = 0 rung (simple pole, residue → c∞), and the
    A6.3 "radius-q₀ next singularity" is the k = 1 rung at w = −q₀.

PIPELINE:
  G1 — identity (★) vs the direct A6.3 route (shared Pascal triangle,
       dps 500, n ≤ 64): the two must agree to the cancellation floor.
  G2 — c∞ = (q̃;q̃)_∞² vs the A6.3 committed Aitken plateau (the
       residual transient at n = 96 is O(q̃⁹⁷) ≈ 4e-5 — gate there).
  G3 — transient ratio → q̃ (1e-3, with the 1/n-correction window).
  G4 — pole ladder: Borel–Padé of the EXACT-pole-subtracted regular
       part locates w = −q₀ (the k = 1 rung).
  G5 — the θ-Laplace re-run with the exact pole split
       ĝ = c∞/(1+w) + ĝ_reg: regularized s(F̄) and D_odd_reg, with the
       kernel/Padé spread of the NEW pipeline reported against the
       g3 lane's median D_odd = −0.007579403739 (5e-16) — does the
       band survive the pole handled exactly? Honest either way.

auditOnly; no c_k wired; no fit (every constant above is derived).
Comparison to observed only; no ontological claims.

Run: python3 -u computations/probes/qbeta_5two_gbar_pole_ladder_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_pole_ladder.log
"""
from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402 — dps must rise before module constants

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qbeta_5two_tail_law_deep_cn_probe import (  # noqa: E402
    build_pascal, c52_from_rows)

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

N_FORMULA = 96          # (★) side — cancellation-free, cheap
N_DIRECT = 64           # direct-route gate depth (dps 500 cancellation)
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

D_ODD_MEDIAN = mp.mpf("-0.007579403739")   # g3 lane, median-normalized
C_INF_A63 = mp.mpf("1.230766e-12")         # A6.3 Aitken plateau (committed)
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def qpoch_list(qt, nmax):
    """(q̃;q̃)_n for n = 0..nmax."""
    out = [mp.mpf(1)]
    for j in range(1, nmax + 1):
        out.append(out[-1] * (1 - qt ** j))
    return out


def gauss_binom_num(n, k, qt, poch):
    """[n,k]_{q̃} numerically (positive, stable)."""
    return poch[n] / (poch[k] * poch[n - k])


def t_hat_formula(n, qt, poch):
    """(★): (−1)ⁿT̂_n = (q̃;q̃)_n²·Σ_k q̃^{k(n+1)}[n,k]_{q̃}."""
    s = mp.mpf(0)
    for k in range(n + 1):
        term = qt ** (k * (n + 1)) * gauss_binom_num(n, k, qt, poch)
        s += term
        if term < mp.mpf("1e-80") * s:
            break
    return poch[n] ** 2 * s


def main() -> int:
    mp.mp.dps = 60
    print("=" * 78)
    print(" A6.4 — the W9 Borel function derived: (★), the pole ladder, "
          "regularized D_odd")
    print("=" * 78)

    t = mp.log(q_at(50))
    a0 = mp.e ** (-t / 2)
    qt = a0 ** 2                    # q̃ = 1/q₀
    q0 = 1 / qt
    poch = qpoch_list(qt, N_FORMULA + 2)

    # (★) values, cancellation-free
    u = [t_hat_formula(n, qt, poch) for n in range(N_FORMULA + 1)]
    Th = [(-1) ** n * u[n] for n in range(N_FORMULA + 1)]

    # ---- G1: identity (★) vs the direct A6.3 route ----
    log(f"[G1] (★) vs direct route (n ≤ {N_DIRECT}, dps 500) ...")
    with mp.workdps(500):
        t5 = mp.log(q_at(50))
        a05 = mp.e ** (-t5 / 2)
        ainv5 = 1 / a05
        qbar5 = ainv5 ** 2
        rows = build_pascal(N_DIRECT)
        dev1 = mp.mpf(0)
        pochbar = mp.mpf(1)
        for n in range(N_DIRECT + 1):
            if n > 0:
                pochbar *= (1 - qbar5 ** n)
            direct = _mb.leval(c52_from_rows(n, rows), ainv5) \
                * pochbar ** 2 * a05 ** (5 * n * n + 7 * n)
            qt5 = a05 ** 2
            poch5 = qpoch_list(qt5, n)
            formula = (-1) ** n * poch5[n] ** 2 * mp.fsum(
                [qt5 ** (k * (n + 1)) * poch5[n]
                 / (poch5[k] * poch5[n - k]) for k in range(n + 1)])
            dev1 = max(dev1, abs(direct - formula) / abs(direct))
    g1 = dev1 < mp.mpf("1e-300")
    log(f"    max rel deviation = {mp.nstr(dev1, 3)}  "
        f"{'PASS' if g1 else 'FAIL'} — (★) is EXACT")

    # ---- G2: c∞ = (q̃;q̃)_∞² ----
    poch_inf = poch[N_FORMULA]
    for j in range(N_FORMULA + 1, N_FORMULA + 4000):
        f = 1 - qt ** j
        poch_inf *= f
        if abs(1 - f) < mp.mpf("1e-70"):
            break
    c_inf = poch_inf ** 2
    dev2 = abs(c_inf - C_INF_A63) / c_inf
    g2 = dev2 < mp.mpf("1e-3")
    log(f"[G2] c∞ = (q̃;q̃)_∞² = {mp.nstr(c_inf, 12)}  vs A6.3 Aitken "
        f"plateau {mp.nstr(C_INF_A63, 8)}: rel {mp.nstr(dev2, 3)}  "
        f"{'PASS' if g2 else 'FAIL'}")

    # ---- G3: transient ratio → q̃ ----
    ratios = [(u[n] - c_inf) / (u[n - 1] - c_inf)
              for n in range(N_FORMULA - 6, N_FORMULA + 1)]
    dev3 = abs(ratios[-1] - qt) / qt
    g3 = dev3 < mp.mpf("1e-3")
    log(f"[G3] transient ratio (u_n−c∞)/(u_{{n−1}}−c∞) = "
        f"{mp.nstr(ratios[-1], 10)}  vs q̃ = {mp.nstr(qt, 10)}: rel "
        f"{mp.nstr(dev3, 3)}  {'PASS' if g3 else 'FAIL'}")

    # ---- G4: the pole ladder — Padé of the pole-subtracted regular part ----
    # ĝ(w) = Σ T̂_n wⁿ; subtract the EXACT k = 0 pole c∞/(1+w)
    # (coefficients c∞·(−1)ⁿ) and Padé the regular part: the k = 1 rung
    # must appear at w = −q₀.
    reg = [Th[n] - c_inf * (-1) ** n for n in range(N_FORMULA + 1)]
    npade = 40
    p_num, p_den = mp.pade([mp.mpf(c) for c in reg[:npade]],
                           npade // 2, npade // 2 - 1)
    poles = mp.polyroots([p_den[i] for i in range(len(p_den) - 1, -1, -1)],
                         maxsteps=200, extraprec=100)
    target = -q0
    best = min(poles, key=lambda p: abs(p - target))
    dev4 = abs(best - target) / abs(target)
    g4 = dev4 < mp.mpf("0.05")
    log(f"[G4] regular-part Padé pole nearest −q₀: {mp.nstr(best, 10)} "
        f"(target {mp.nstr(target, 8)}; rel {mp.nstr(dev4, 3)})  "
        f"{'PASS' if g4 else 'FAIL'} — the k = 1 rung")
    ladder2 = min(poles, key=lambda p: abs(p - (-q0 ** 2)))
    log(f"    k = 2 rung diagnostic: nearest pole to −q₀² = "
        f"{mp.nstr(ladder2, 8)} (rel {mp.nstr(abs(ladder2 + q0**2)/q0**2, 3)})")

    # ---- G5: θ-Laplace with the exact pole split ----
    Qt = a0 ** 10
    t_targ = a0 ** -7

    def theta_Q(Q, w, M=60):
        return mp.fsum([Q ** (mp.mpf(m * m) / 2) * w ** m
                        for m in range(-M, M + 1)])

    def make_g_split(npade_):
        pn, pd = mp.pade([mp.mpf(c) for c in reg[:npade_]],
                         npade_ // 2, npade_ // 2 - 1)

        def g(w):
            pole = c_inf / (1 + w)
            if abs(w) <= mp.mpf("0.85"):
                # regular part by its (now geometrically convergent) series
                regv = mp.fsum([reg[n] * w ** n for n in range(N_FORMULA + 1)])
            else:
                regv = mp.polyval(pn[::-1], w) / mp.polyval(pd[::-1], w)
            return pole + regv
        return g

    def theta_laplace(gfun, Qb, s0, w0, M=14):
        acc = mp.mpf(0)
        for m in range(-M, M + 1):
            acc += Qb ** (mp.mpf(m * m) / 2) * w0 ** m * gfun(s0 * Qb ** m)
        return acc / theta_Q(Qb, w0)

    log("[G5] θ-Laplace with the exact pole split:")
    vals = []
    for npade_ in (28, 36, 44):
        for s0f in ("0.5", "0.8", "1.2"):
            g = make_g_split(npade_)
            s0 = mp.mpf(s0f)
            v = theta_laplace(g, Qt, s0, s0 / t_targ, M=14)
            vals.append(mp.re(v))
    v_mid = sorted(vals)[len(vals) // 2]
    band = max(vals) - min(vals)
    log(f"    s(F̄)_split median = {mp.nstr(v_mid, 15)}   band = "
        f"{mp.nstr(band, 3)} ({mp.nstr(band/abs(v_mid), 3)} rel)")

    # convergent side (as in the W9 probe)
    poch_c = mp.mpf(1)
    F_conv = mp.mpf(0)
    for n in range(40):
        if n > 0:
            poch_c *= (1 - qt ** n)
        term = _mb.leval(_mb.C52(n), a0) * poch_c ** 2
        F_conv += term
        if abs(term) < mp.mpf("1e-42") and n > 6:
            break
    D_odd_reg = (v_mid - F_conv) / 2
    dev5 = abs(D_odd_reg - D_ODD_MEDIAN)
    g5 = dev5 < mp.mpf("1e-9")
    log(f"    D_odd_reg = {mp.nstr(D_odd_reg, 15)}  vs median "
        f"{mp.nstr(D_ODD_MEDIAN, 12)}: |Δ| = {mp.nstr(dev5, 3)}  "
        f"{'PASS' if g5 else 'FAIL (shift recorded)'}")
    print(f"    ⇒ pole handled EXACTLY; new-pipeline band "
          f"{mp.nstr(band/2, 3)} on D_odd "
          f"({'the g3 5e-16-class robustness survives the pole' if band/2 < mp.mpf('1e-11') else 'band above 1e-11 — the pole-induced spread is the honest floor'})")

    wb = WitnessBuilder("qbeta-5two-gbar-pole-ladder", engine="mpmath",
                        _script_path=__file__)
    wb.set_description(
        "A6.4: the W9 q-Borel function DERIVED. The balanced-binomial "
        "inversion collapses the transform to the exact cancellation-free "
        "formula (−1)ⁿT̂_n = (q̃;q̃)_n²·Σ_k q̃^{k(n+1)}[n,k]_{q̃} (gated vs "
        "the direct route at dps 500), giving: the pole residue "
        "c∞ = (q̃;q̃)_∞² in closed form (the A6.3 Aitken plateau derived); "
        "the transient ratio exactly q̃ = 1/q₀ (the A6.3 0.90086 "
        "observation derived); and the POLE LADDER ĝ ~ poles at "
        "w = −q₀ᵏ (k = 1 rung located by Padé after exact pole "
        "subtraction). θ-Laplace re-run with the exact pole split: "
        "regularized D_odd vs the g3 median value, with the new "
        "pipeline's honest band. auditOnly; no c_k wired; no fit — every "
        "constant is derived.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("star_identity_exact",
                     computed=dev1, expected=0.0, tolerance=1e-300,
                     source="(★) = the direct C_n·poch²·a₀-power route, "
                            "n ≤ 64 at dps 500")
    wb.add_assertion("residue_closed_form",
                     computed=dev2, expected=0.0, tolerance=1e-3,
                     source="c∞ = (q̃;q̃)_∞² vs the A6.3 Aitken plateau "
                            "(residual transient O(q̃⁹⁷) ≈ 4e-5)")
    wb.add_assertion("transient_ratio_is_qtilde",
                     computed=dev3, expected=0.0, tolerance=1e-3,
                     source="(u_n−c∞)/(u_{n−1}−c∞) → q̃ = 1/q₀ exactly")
    wb.add_assertion("pole_ladder_k1_located",
                     computed=dev4, expected=0.0, tolerance=0.05,
                     source="Padé of the exact-pole-subtracted regular part "
                            "has its nearest pole at w = −q₀ (k = 1 rung)")
    wb.add_assertion("regularized_dodd_consistent",
                     computed=dev5, expected=0.0, tolerance=1e-9,
                     source="θ-Laplace with the exact pole split reproduces "
                            "the g3 median D_odd")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("derivation", {
        "star": "(-1)^n T_n = (qt;qt)_n^2 * sum_k qt^{k(n+1)} [n,k]_qt",
        "c_inf_closed_form": "(qt;qt)_inf^2",
        "c_inf_value": mp.nstr(c_inf, 20),
        "transient_ratio": "qt = 1/q0 exactly",
        "pole_ladder": "poles at w = -q0^k, k = 0,1,2,..."})
    wb.add_data("pole_ladder_pade", {"k1_found": mp.nstr(best, 15),
                                     "k1_rel": mp.nstr(dev4, 6),
                                     "k2_nearest": mp.nstr(ladder2, 12)})
    wb.add_data("regularized_dodd", {"s_Fbar_split": mp.nstr(v_mid, 20),
                                     "band_rel": mp.nstr(band / abs(v_mid), 6),
                                     "D_odd_reg": mp.nstr(D_odd_reg, 18),
                                     "vs_median": mp.nstr(dev5, 6)})
    wb.add_data("verdict",
                (f"THE W9 BOREL FUNCTION IS DERIVED: exact formula (★) "
                 f"(gate {mp.nstr(dev1, 2)}), residue c∞ = (q̃;q̃)_∞² = "
                 f"{mp.nstr(c_inf, 10)}, transient ratio q̃, pole ladder at "
                 f"w = −q₀ᵏ (k=1 located, rel {mp.nstr(dev4, 2)}). The "
                 f"regularized D_odd = {mp.nstr(D_odd_reg, 12)} agrees with "
                 f"the g3 median ({mp.nstr(dev5, 2)}); the A6.3 precision "
                 f"caveat resolves — the pole term is now explicit, and the "
                 f"scheme band on the regular part is {mp.nstr(band/2, 2)}. "
                 f"auditOnly." if ok else
                 "A gate failed — inspect before any claim."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-gbar-pole-ladder.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
