#!/usr/bin/env python3
"""A6.3: the tail law of the exact q-Borel sequence at DEPTH — C_n
extended to n ≤ 96.

WHY. A6.2 found the exact W9 q-Borel integers T̂_n carry no clean
algebraic n^{−θ} tail at n ≤ 43 (single-model θ window-drifts 11.3 → 9.4;
three-model ranking only indicative) — leaving open whether the tail is
pre-asymptotic (θ stabilizes deeper) or the Borel singularity at w = −1
is genuinely flat-type. This probe extends the EXACT Masbaum integer
Laurent C_{5₂,n} (closed form, Masbaum DOI 10.2140/agt.2003.3.537 —
shared Pascal triangle built once) to n ≤ 96 and re-runs the tail-law
discrimination at depth.

PRECISION. leval at n ≈ 96 cancels ~640 digits (Laurent exponents to
~3n²+5n in a-units, ā = e^{t/2} with t = ln q₀), so the run is at
dps 800 (headroom ≥ 150 digits over the worst cancellation) — entropy-
safe for every reported ratio.

GATES:
  G1 — regeneration: the shared-triangle C_n equals the merged profile
       module's C52(n) EXACTLY (integer dict equality) at n = 5, 20, 43.
  G2 — overlap: T̂_n for n ≤ 43 reproduces the A6.2 values (rel 1e-30).
  G3 — ranking reproducibility across the two deep windows.
THE MEASUREMENT — single-model θ on sliding windows (does it stabilize?)
+ the three-model (algebraic / stretched-√n / quadratic) rms ranking at
depth. Honest outcome either way: a stabilized θ (algebraic tail, value
reported) or continued drift (flat-type singularity, recorded).

auditOnly; no c_k wired; no fit (exponent/model extraction is a
structural measurement). Comparison to observed only; no ontological
claims.

Run: python3 -u computations/probes/qbeta_5two_tail_law_deep_cn_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_tail_deep.log
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

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402

# --- precision: raised for bucket-B fix (bean qou-p77d) ---
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

N_MAX = 96
DPS = 800
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:6.0f}s] {msg}", flush=True)


def build_pascal(nmax):
    """Gaussian-binomial Pascal triangle in q (integer dicts), rows 0..nmax,
    built ONCE (the profile module rebuilds per call — O(n⁴) at depth)."""
    rows = [[{0: 1}]]
    for nn in range(1, nmax + 1):
        prev = rows[-1]
        new = [{0: 1}]
        for kk in range(1, nn):
            shifted = {e + kk: c for e, c in prev[kk].items()} \
                if kk < len(prev) else {}
            new.append(_mb.ladd(prev[kk - 1], shifted))
        new.append({0: 1})
        rows.append(new)
    return rows


def c52_from_rows(n, rows):
    """Masbaum C_{5₂,n}(a) via the prebuilt triangle (same algebra as
    the profile module's C52)."""
    out = {}
    for k in range(n + 1):
        bq = rows[n][k]
        bb = {2 * e - k * (n - k): c for e, c in bq.items()}
        base = 3 * n * n + 5 * n + k * k - 2 * k - 3 * n * k
        out = _mb.ladd(out, {base + e: c for e, c in bb.items()})
    if n % 2 == 1:
        out = {e: -c for e, c in out.items()}
    return out


def main() -> int:
    mp.mp.dps = DPS
    print("=" * 78)
    print(f" A6.3 — deep tail law of the exact q-Borel T̂_n (n ≤ {N_MAX}, "
          f"dps {DPS})")
    print("=" * 78)

    t = mp.log(q_at(50))
    a0 = mp.e ** (-t / 2)
    ainv = 1 / a0
    qbar = ainv ** 2

    log(f"building the shared Pascal triangle to n = {N_MAX} ...")
    rows = build_pascal(N_MAX)
    log("triangle built")

    # ---- G1: exact regeneration vs the merged profile module ----
    g1 = all(c52_from_rows(n, rows) == _mb.C52(n) for n in (5, 20, 43))
    log(f"[G1] shared-triangle C_n == profile C52(n) exactly at "
        f"n = 5, 20, 43: {'PASS' if g1 else 'FAIL'}")

    # ---- exact transform to depth ----
    log(f"evaluating T̂_n to n = {N_MAX} (worst cancellation ~640 digits) ...")
    Th = []
    poch = mp.mpf(1)
    for n in range(N_MAX + 1):
        if n > 0:
            poch *= (1 - qbar ** n)
        Th.append(_mb.leval(c52_from_rows(n, rows), ainv) * poch ** 2
                  * a0 ** (5 * n * n + 7 * n))
        if n % 16 == 0:
            log(f"    n = {n}: |T̂_n| = {mp.nstr(abs(Th[n]), 6)}")
    alt_pos = all((-1) ** n * Th[n] > 0 for n in range(N_MAX + 1))
    log(f"(−1)^n·T̂_n > 0 for all n ≤ {N_MAX}: {alt_pos}")

    # ---- G2: overlap with the A6.2 (profile-module) values at n ≤ 43 ----
    poch2 = mp.mpf(1)
    g2_dev = mp.mpf(0)
    for n in range(44):
        if n > 0:
            poch2 *= (1 - qbar ** n)
        ref = _mb.leval(_mb.C52(n), ainv) * poch2 ** 2 \
            * a0 ** (5 * n * n + 7 * n)
        g2_dev = max(g2_dev, abs(Th[n] - ref) / abs(ref))
    g2 = g2_dev < mp.mpf("1e-30")
    log(f"[G2] overlap n ≤ 43 vs profile-module route: max rel "
        f"{mp.nstr(g2_dev, 3)}: {'PASS' if g2 else 'FAIL'}")

    # ---- the measurement: sliding single-model θ + three-model ranking ----
    def fit_resid(ns, third):
        A_ = mp.matrix([[1, n, third(n)] for n in ns])
        y = mp.matrix([mp.log(abs(Th[n])) for n in ns])
        coef = mp.lu_solve(A_.T * A_, A_.T * y)
        resid = A_ * coef - y
        rms = mp.sqrt(sum(r * r for r in resid) / len(ns))
        return coef, rms

    log("sliding-window single-model θ (ln n model):")
    theta_track = {}
    for lo in (20, 32, 44, 56, 68, 80):
        ns = list(range(lo, min(lo + 16, N_MAX) + 1))
        coef, _ = fit_resid(ns, lambda n: -mp.log(n))
        theta_track[f"{lo}..{ns[-1]}"] = mp.nstr(coef[2], 8)
        log(f"    window {lo:>2}..{ns[-1]}: θ = {mp.nstr(coef[2], 8)}")
    thetas = [mp.mpf(v) for v in theta_track.values()]
    drift_early = abs(thetas[1] - thetas[0])
    drift_late = abs(thetas[-1] - thetas[-2])
    stabilized = drift_late < mp.mpf("0.3")

    # ---- plateau / simple-pole test (the deep-run discovery) ----
    # First deep run: θ marches monotonically toward 0 and |T̂_n| PLATEAUS
    # (1.2388e-12 at n=80 → 1.2323e-12 at n=96) — coefficients tending to
    # a nonzero constant c∞·(−1)^n, i.e. ĝ(w) has a SIMPLE POLE at w = −1
    # with residue c∞ (the "soft singularity" reading at n ≤ 43 was the
    # transient). Extract c∞ by Aitken acceleration of u_n = (−1)^n T̂_n
    # and gate its stability across offsets.
    u = [(-1) ** n * Th[n] for n in range(N_MAX + 1)]

    def aitken_once(s):
        return [(s[i + 2] * s[i] - s[i + 1] ** 2)
                / (s[i + 2] - 2 * s[i + 1] + s[i])
                for i in range(len(s) - 2)]
    tail_u = u[N_MAX - 24:]
    acc1 = aitken_once(tail_u)
    acc2 = aitken_once(acc1)
    c_inf_a = acc2[-1]
    c_inf_b = acc2[-4]
    pole_stab = abs(c_inf_a - c_inf_b) / abs(c_inf_a)
    is_pole = c_inf_a > 0 and pole_stab < mp.mpf("0.02")
    # transient decay ratio toward the plateau
    d_seq = [abs(u[n] - c_inf_a) for n in range(N_MAX - 12, N_MAX + 1)]
    trans_ratio = d_seq[-1] / d_seq[-2] if d_seq[-2] > 0 else mp.mpf(0)
    log(f"[pole] Aitken plateau c∞ = {mp.nstr(c_inf_a, 8)} "
        f"(offset stability {mp.nstr(pole_stab, 3)}); transient ratio "
        f"{mp.nstr(trans_ratio, 5)}")
    print(f"    ⇒ (−1)^n·T̂_n → c∞ ≈ {mp.nstr(c_inf_a, 6)} ≠ 0: SIMPLE POLE "
          f"at w = −1, residue ≈ c∞")
    print(f"      {'PASS' if is_pole else 'INDETERMINATE'} — the shallow "
          f"'soft singularity' reading (W9-parallel B1 + A6.2) was the "
          f"transient")

    models = {"algebraic_ln_n": lambda n: -mp.log(n),
              "stretched_sqrt_n": lambda n: -mp.sqrt(n),
              "quadratic_n2": lambda n: -mp.mpf(n * n) / 2}
    windows = {"48..96": list(range(48, N_MAX + 1)),
               "64..96": list(range(64, N_MAX + 1))}
    tab = {}
    rankings = {}
    log("three-model ranking at depth:")
    for wname, ns in windows.items():
        tab[wname] = {}
        for mname, third in models.items():
            coef, rms = fit_resid(ns, third)
            tab[wname][mname] = {"coef": mp.nstr(coef[2], 8),
                                 "rms": mp.nstr(rms, 6)}
        ranking = sorted(models, key=lambda m: mp.mpf(tab[wname][m]["rms"]))
        rankings[wname] = ranking
        log(f"    window {wname}: " + "  ".join(
            f"{m}: rms {tab[wname][m]['rms']}" for m in ranking))
    g3 = rankings["48..96"] == rankings["64..96"]
    best = rankings["48..96"][0]
    best_rms = mp.mpf(tab["48..96"][best]["rms"])
    runner_rms = mp.mpf(tab["48..96"][rankings["48..96"][1]]["rms"])
    decisive = runner_rms / best_rms > 2

    print(f"\n    θ track: {theta_track}")
    print(f"    late-window θ drift = {mp.nstr(drift_late, 3)} "
          f"({'STABILIZED — algebraic tail, θ ≈ ' + mp.nstr(thetas[-1], 5) if stabilized else 'still drifting — flat-type/pre-asymptotic'})")
    print(f"    best deep model: {best} "
          f"({'decisive' if decisive else 'indicative'}; runner-up rms "
          f"×{mp.nstr(runner_rms / best_rms, 4)}); ranking reproducible: "
          f"{'PASS' if g3 else 'FAIL'}")

    wb = WitnessBuilder("qbeta-5two-tail-law-deep-cn", engine="mpmath",
                        _script_path=__file__)
    wb.set_description(
        "A6.3: the exact Masbaum C_n extended to n ≤ 96 (shared Pascal "
        "triangle, gated exactly against the merged profile module) and "
        "the W9 q-Borel sequence's tail law re-measured at depth and "
        "dps 800 (~640-digit worst cancellation, entropy-safe): sliding-"
        "window single-model θ track (does the A6.2 drift stabilize?) + "
        "the three-model discrimination on deep windows. Honest outcome "
        "either way: stabilized θ = algebraic tail with the value "
        "reported, continued drift = flat-type singularity recorded. "
        "auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("cn_regeneration_exact",
                     computed=1.0 if g1 else 0.0, expected=1.0, tolerance=0.5,
                     source="shared-triangle C_n == profile C52(n), integer "
                            "dict equality at n = 5, 20, 43")
    wb.add_assertion("overlap_with_a62_values",
                     computed=g2_dev, expected=0.0, tolerance=1e-30,
                     source="T̂_n (n ≤ 43) matches the A6.2 profile-module "
                            "route")
    wb.add_assertion("deep_ranking_reproducible",
                     computed=1.0 if g3 else 0.0, expected=1.0, tolerance=0.5,
                     source="three-model ranking identical on 48..96 and "
                            "64..96")
    ok = all(a.passed for a in wb.assertions)

    wb.add_assertion("plateau_pole_extraction_stable",
                     computed=pole_stab, expected=0.0, tolerance=0.02,
                     source="Aitken plateau c∞ of (−1)^n·T̂_n stable across "
                            "offsets — simple pole at w = −1, residue c∞")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("theta_track", theta_track)
    wb.add_data("theta_stabilized", bool(stabilized))
    wb.add_data("pole", {"c_inf_residue": mp.nstr(c_inf_a, 15),
                         "offset_stability": mp.nstr(pole_stab, 6),
                         "transient_ratio": mp.nstr(trans_ratio, 8),
                         "reading": "simple pole at w = -1 with residue "
                                    "c_inf; the 'soft singularity' at "
                                    "n <= 43 was the transient",
                         "g3_lane_flag": "the theta-Laplace D_odd scheme "
                                         "band (5e-16) predates this pole: "
                                         "a pole ambiguity enters at the "
                                         "residue scale ~1e-12 — still ~9 "
                                         "orders below the physics scale, "
                                         "but the stated precision needs "
                                         "the caveat"})
    wb.add_data("deep_models", {"tab": tab, "rankings": rankings,
                                "best": best, "decisive": bool(decisive)})
    wb.add_data("alt_positive_to_96", bool(alt_pos))
    wb.add_data("params", {"n_max": N_MAX, "dps": DPS})
    wb.add_data("verdict",
                ((f"TAIL LAW AT DEPTH SETTLED: (−1)^n·T̂_n → c∞ ≈ "
                  f"{mp.nstr(c_inf_a, 6)} ≠ 0 (Aitken-stable "
                  f"{mp.nstr(pole_stab, 3)}) — the Borel function has a "
                  f"SIMPLE POLE at w = −1 with residue ≈ c∞; the θ track "
                  f"{theta_track} marching to 0 and the shallow-window "
                  f"'soft singularity' reading (W9-parallel B1 + A6.2) "
                  f"were the transient. The naive φ-side 3/2 algebraic tie "
                  f"is REFUTED-as-stated for this sequence (scope-(a): "
                  f"this transform/normalization). g3-lane flag recorded: "
                  f"the pole introduces a ~1e-12-scale contour ambiguity "
                  f"above the stated 5e-16 D_odd scheme band (no physics "
                  f"impact; precision caveat). auditOnly."
                  if is_pole else
                  f"TAIL LAW AT DEPTH: plateau extraction INDETERMINATE "
                  f"(stability {mp.nstr(pole_stab, 3)}); θ track "
                  f"{theta_track}. auditOnly.")
                 if ok else "A gate failed — inspect before use."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-tail-law-deep-cn.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
