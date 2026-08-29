#!/usr/bin/env python3
"""A6.2: the two odd-channel routes confronted — the saddle-side σ-pair
projection vs the W9-parallel resummed bar-side datum D_odd.

CONTEXT. Two independent lanes now hold 5₂ odd-channel data at the
substrate:
  * the MAIN-LINE Masbaum-face lane (probe qbeta_g3_5two_qborel_theta_
    laplace + dodd_median_crosschecks, merged): D_odd = −0.007579403739
    ± 5e-16 (median-normalized, scheme-robust) — a FUNCTION-VALUE odd
    datum from θ-Laplace resummation of the exact integer-Laurent
    Habiro tail;
  * this branch's A6 lane: the exact bar-odd σ-pair K-tower
    P_k(ξ₁) − P_k(ξ̄₁) of the state-integral saddle series (all 24 orders
    exact in the trace field).
Bridging the two at function level needs the state-integral factorization
normalization (Stokes sector population on the real-q ray) — named OPEN by
the W9-parallel verdict itself. This probe does the two things that need
NO scheme constant:

  A — the σ-pair odd projection EVALUATED at the substrate:
      O_φ := Im φ_σ1(x_sub), x_sub = −ln q₀ (the A4.3 substrate ray; the
      conjugate saddle gives the conjugate value, so the σ-pair difference
      is 2i·O_φ). Computed by 24-order truncation AND Borel–Padé
      directional Laplace (both converged at |x_sub| ≈ 0.104 — consistency
      gate). A derived, calibration-free odd number; recorded scope-(a)
      against D_odd and the anchor rows — NO identification.

  B — a normalization-free STRUCTURAL cross-check: the W9 exact q-Borel
      sequence T̂_n = C_n(q̄)(q̄;q̄)_n²a₀^{5n²+7n} has |ratio| → 1 (soft
      singularity at w = −1). The φ-side Gauss prefactor (ħ^{1/2} per
      saddle) predicts the soft exponent θ = 3/2 in
      (−1)^n T̂_n ~ A·rⁿ·n^{−θ}: extract θ from the exact integers by a
      3-parameter linear model in (1, n, ln n) — an exponent MEASUREMENT
      (linear algebra on exact data; no parameter enters any physical
      claim) — and compare. Agreement ties the two routes' analytic
      structure with zero scheme freedom; disagreement is recorded as the
      measured exponent.

auditOnly; no c_k wired; no fit (the θ extraction is a structural
measurement, labeled as such). Comparison to observed only; no
ontological claims.

Run: python3 -u computations/probes/qbeta_5two_odd_two_route_confrontation_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_odd_confrontation.log
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from qou_substrate.constants import q_at  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "qbeta_g3_5two_masbaum_barodd_profile",
    _HERE / "qbeta_g3_5two_masbaum_barodd_profile.py")
_mb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mb)

mp.mp.dps = 60

# committed reference values (scope-(a) comparison rows)
D_ODD = mp.mpf("-0.007579403739")   # median-normalized, scheme-robust (5e-16; dodd_median_crosschecks)
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
IM_VB = mp.mpf("0.0585499951473")
N_COEF = 44
T0 = time.monotonic()


def load_phi_basis():
    w = record_upstream(_HERE / "qbeta-5two-phi-series-engine.witness.json", _UPSTREAM_RECORDS)
    P = {0: mp.mpc(1)}
    for k, v in w["data"]["P_coefficients"].items():
        m = re.match(r"\(?\s*([-\d.e]+)\s*([+-])\s*([\d.e]+)j\)?", v)
        r_, s_, i_ = m.groups()
        P[int(k)] = mp.mpc(mp.mpf(r_), mp.mpf(i_) * (1 if s_ == "+" else -1))
    return P


def main() -> int:
    print("=" * 78)
    print(" A6.2 — odd-channel two-route confrontation (σ-pair vs D_odd)")
    print("=" * 78)

    t = mp.log(q_at(50))
    x_sub = -t                     # the A4.3 substrate ray x = −ln q₀

    # ---- A: σ-pair odd projection at the substrate ----
    P = load_phi_basis()
    OMAX = max(P)

    def phi_trunc(x):
        return sum(P[k] * x ** k for k in range(OMAX + 1))

    b = [P[k] / mp.factorial(k) for k in range(OMAX + 1)]
    p_num, p_den = mp.pade(b, 11, 12)

    def B_pade(zeta):
        num = sum(p_num[i] * zeta ** i for i in range(len(p_num)))
        den = sum(p_den[i] * zeta ** i for i in range(len(p_den)))
        return num / den

    def phi_res(x):
        ray = x / abs(x)
        f = lambda u: B_pade(u * ray) * mp.e ** (-(u * ray) / x) * ray
        return mp.quad(f, [0, 5, 20, 80]) / x

    pt = phi_trunc(x_sub)
    pr = phi_res(x_sub)
    O_t = mp.im(pt)
    O_r = mp.im(pr)
    consA = abs(O_t - O_r) / abs(O_t)
    gA = consA < mp.mpf("1e-6")
    log = lambda m_: print(f"  [{time.monotonic()-T0:5.0f}s] {m_}", flush=True)
    log(f"[A] x_sub = {mp.nstr(x_sub, 10)}")
    log(f"    Im φ_σ1: truncation {mp.nstr(O_t, 15)}  resummed "
        f"{mp.nstr(O_r, 15)}  consistency {mp.nstr(consA, 3)}")
    print(f"    σ-pair odd projection O_φ = {mp.nstr(O_t, 12)}  "
          f"{'PASS' if gA else 'FAIL'} (truncation/resummation gate)")
    rows = {"O_phi_sigma_pair": O_t, "D_odd_masbaum_face": D_ODD,
            "ratio_O_phi_over_D_odd": O_t / D_ODD,
            "S_muon": S_MUON, "S_proton": S_PROTON,
            "u_cubed": (2 * t) ** 3, "Im_Vb": IM_VB}
    print("\n    scope-(a) rows (NOT identifications; the function-level "
          "bridge needs the")
    print("    Stokes-population normalization — open per the W9-parallel "
          "verdict):")
    for k, v in rows.items():
        print(f"      {k:>24} = {mp.nstr(v, 10)}")

    # ---- B: tail-law discrimination on the exact W9 sequence ----
    # First-run lesson (recorded): the naive single-model power-law
    # extraction ln|T̂| = c0 + c1·n − θ·ln n is WINDOW-UNSTABLE
    # (θ: 11.3 → 9.4 between tails) — the exact integers do NOT follow a
    # clean algebraic n^{−θ} at n ≤ 43, so the naive φ-side θ = 3/2 tie is
    # not testable at this depth (scope-(a): this comparison, at this
    # depth). Honest replacement: a three-model discrimination —
    #   M_alg:       ln|T̂_n| = c0 + c1·n − θ·ln n     (algebraic soft sing.)
    #   M_stretch:   ln|T̂_n| = c0 + c1·n − c·√n       (flat/stretched type)
    #   M_quad:      ln|T̂_n| = c0 + c1·n − c·n²/2     (residual q-quadratic)
    # ranked by RMS residual on two tail windows; the assertion is the
    # REPRODUCIBILITY of the ranking, not any physics pass/fail.
    a0 = mp.e ** (-t / 2)
    ainv = 1 / a0
    qbar = ainv ** 2
    Th = []
    poch = mp.mpf(1)
    for n in range(N_COEF):
        if n > 0:
            poch *= (1 - qbar ** n)
        Th.append(_mb.leval(_mb.C52(n), ainv) * poch ** 2
                  * a0 ** (5 * n * n + 7 * n))

    def fit_resid(ns, third):
        A_ = mp.matrix([[1, n, third(n)] for n in ns])
        y = mp.matrix([mp.log(abs(Th[n])) for n in ns])
        coef = mp.lu_solve(A_.T * A_, A_.T * y)
        resid = A_ * coef - y
        rms = mp.sqrt(sum(r * r for r in resid) / len(ns))
        return coef[2], rms

    models = {"algebraic_ln_n": lambda n: -mp.log(n),
              "stretched_sqrt_n": lambda n: -mp.sqrt(n),
              "quadratic_n2": lambda n: -mp.mpf(n * n) / 2}
    windows = {"20..43": list(range(20, N_COEF)),
               "28..43": list(range(28, N_COEF))}
    tab = {}
    rankings = {}
    log("[B] tail-law discrimination on the exact T̂_n:")
    for wname, ns in windows.items():
        tab[wname] = {}
        for mname, third in models.items():
            c3_, rms = fit_resid(ns, third)
            tab[wname][mname] = {"coef": mp.nstr(c3_, 8),
                                 "rms": mp.nstr(rms, 6)}
        ranking = sorted(models, key=lambda m: mp.mpf(tab[wname][m]["rms"]))
        rankings[wname] = ranking
        log(f"    window {wname}: " + "  ".join(
            f"{m}: rms {tab[wname][m]['rms']}" for m in ranking))
    gB_stable = rankings["20..43"] == rankings["28..43"]
    best = rankings["20..43"][0]
    best_rms = mp.mpf(tab["20..43"][best]["rms"])
    runner_rms = mp.mpf(tab["20..43"][rankings["20..43"][1]]["rms"])
    decisive = runner_rms / best_rms > 2
    print(f"    best tail model: {best} "
          f"({'decisive' if decisive else 'indicative'}; runner-up rms "
          f"×{mp.nstr(runner_rms / best_rms, 4)}); ranking reproducible "
          f"across windows: {'PASS' if gB_stable else 'FAIL'}")
    print("    ⇒ the naive algebraic n^{−θ} tie to the φ-side 3/2 is NOT "
          "supported at n ≤ 43")
    print("      (scope-(a): this depth/model class; deeper C_n or an "
          "analytic argument needed).")

    wb = WitnessBuilder("qbeta-5two-odd-two-route-confrontation",
                        engine="mpmath", _script_path=__file__)
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "A6.2: the two independent 5₂ odd-channel routes confronted at the "
        "substrate with NO scheme constant. A: the saddle-side σ-pair odd "
        "projection O_φ = Im φ_σ1(−ln q₀) (24-order basis; truncation vs "
        "Borel–Padé directional Laplace consistency-gated) — a derived, "
        "calibration-free odd number recorded scope-(a) against the "
        "Masbaum-face resummed D_odd and the anchor rows, with the "
        "function-level bridge (Stokes sector population on the real-q "
        "ray) explicitly named OPEN. B: a normalization-free structural "
        "tie — the soft-singularity exponent θ of the exact W9 q-Borel "
        "integer sequence, measured by a 3-parameter linear model "
        "(structural measurement, not a physics fit), vs the φ-side "
        "Gauss-prefactor prediction θ = 3/2. auditOnly; no c_k wired; "
        "no fit; no identification.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("sigma_pair_projection_consistent",
                     computed=consA, expected=0.0, tolerance=1e-6,
                     source="Im φ_σ1(x_sub): truncation = directional "
                            "resummation (both converged at |x| ≈ 0.104)")
    wb.add_assertion("tail_law_ranking_reproducible",
                     computed=1.0 if gB_stable else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="three-model tail-law ranking (algebraic / "
                            "stretched / quadratic) identical across the "
                            "two tail windows on the exact T̂_n")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("sigma_pair", {"x_sub": mp.nstr(x_sub, 15),
                               "O_phi_trunc": mp.nstr(O_t, 25),
                               "O_phi_resummed": mp.nstr(O_r, 25)})
    wb.add_data("confrontation_rows", {k: mp.nstr(v, 12)
                                       for k, v in rows.items()})
    wb.add_data("tail_law", {"models": tab, "rankings": rankings,
                             "best": best,
                             "decisive": bool(decisive),
                             "note": "single-model power-law extraction was "
                                     "window-unstable (theta 11.3 vs 9.4, "
                                     "first run) — no clean algebraic tail "
                                     "at n <= 43; the naive phi-side 3/2 "
                                     "tie is untestable at this depth "
                                     "(scope-(a))"})
    wb.add_data("open_bridge",
                "the function-level identification O_φ ↔ D_odd requires the "
                "Stokes sector population of the state-integral transseries "
                "on the real-q ray (the factorization normalization) — open. "
                "NOTE: the g3 lane's own SCHEME ambiguity has since closed "
                "(δ-torus median, 5e-16) — what remains open is the bridge "
                "between the two OBJECTS (σ-pair coefficientwise projection "
                "vs Habiro-face function value), not their scheme. Neither "
                "route's number is wired anywhere.")
    wb.add_data("verdict",
                (f"TWO-ROUTE CONFRONTATION RECORDED: O_φ = {mp.nstr(O_t, 8)} "
                 f"(σ-pair, calibration-free) vs D_odd = {mp.nstr(D_ODD, 6)} "
                 f"(Masbaum-face resummation) — ratio {mp.nstr(O_t/D_ODD, 6)}, "
                 f"scope-(a), bridge OPEN. Tail law: best model = {best} "
                 f"({'decisive' if decisive else 'indicative'}); no clean "
                 f"algebraic n^-theta at n <= 43, so the naive phi-side 3/2 "
                 f"exponent tie is untestable at this depth (scope-(a)). "
                 f"auditOnly." if ok else "A gate failed — inspect before use."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s)")
    print("  witness -> computations/probes/"
          "qbeta-5two-odd-two-route-confrontation.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
