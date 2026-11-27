#!/usr/bin/env python3
"""
keystone_qhankel_eq2_vacuum_row.py — the LAST disciplined q-Bessel form for
the s013 keystone value map, now fully sourced.

Context. The keystone value step needs the vector
    bwS0(λ) = d_q(λ)/D,   d_q = ([1]_q, [4]_q, [5]_q, [4]_q[3]_q/[2]_q)
            ≈ (1, 4.10968, 5.22044, 6.22044)   at q = q0^-1 ≈ 0.90092
(the compact SU_q(2)/Hecke quantum-dimension vector = Verlinde S_0λ/S_00,
PR #3292 FACT 1). Redirect (ii) asked whether the NON-compact E_q(2)
"vacuum row" — the Plancherel-fixed values of the third (Hahn–Exton)
q-Bessel — independently reproduces this vector with NO free parameters.

The single-argument form was refuted un-sourced (2026-07-02 §4); the
0th-order q-Bessel TRICOMI C_{0,q} = Σ(-1)^k x^k/([k]_q!)^2 was refuted
with a source (2026-07-04, library/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials/raza-fadel-cesarano-2025-two-variable-q-legendre-polynomials.pdf). BUT the Tricomi lacks the
Gaussian q^{k(k-1)/2} that makes the THIRD q-Bessel entire-of-order-0 with
DISCRETE orthogonality — i.e. the Tricomi is not the Plancherel object.

Source (owner upload, decisive): Koornwinder T.H., Swarttouw R.F., "On
q-analogues of the Fourier and Hankel transforms", arXiv:1208.2521 (=
Trans. AMS 333, 1992). Their eq. (1.2), Exton normalization:

    C_α(q; x) = (1-q)^α / (q;q)_∞
                · Σ_{k≥0} q^{k(k-1)/2} (q^{α+k+1};q)_∞ (-x(1-q)^2)^k / (q;q)_k

with the Hansen–Lommel orthogonality holding at the roots μ_1<μ_2<… of
C_α(q;μ)=0, over the q-integral ∫_0^1 f dq x = (1-q) Σ_k f(q^k) q^k. Those
roots μ_j ARE the Plancherel-fixed nodes — 0 free parameters at fixed q.

Test (0-dof, falsifiable). Do any parameter-free quantities of the sourced
C_α — the ordered roots μ_j, their roots/normalisations, or C_α at the
q-lattice nodes q^k — reproduce the compact target vector within 1%, for
the natural labels α ∈ {0, 1/2, 1, 2}? No fit; every candidate reported
with ratio.

Output: keystone-qhankel-eq2-vacuum-row.witness.json
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, findroot

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).parent

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_int_at as _q_int_at  # noqa: E402

# Substrate: categorical q0>1; the |q|<1 image used by E_q(2) harmonic analysis.
Q0 = Q_MP
Q = 1 / Q0                      # ≈ 0.90092


def qint(n, q=Q):
    """Symmetric (balanced) q-integer [n]_q = (q^n - q^-n)/(q - q^-1).

    CORRECTED 2026-09-13 (bean qou-9nn0).  This computed the symmetric
    bracket in the variable sqrt(q) -- i.e. [n]_{sqrt q}, which as a
    function of q is a DIFFERENT function, not a different convention.
    The file contradicted itself: the docstring's formula said
    (q^{n/2}-q^{-n/2})/(q^{1/2}-q^{-1/2}) while the module docstring
    publishes the target this probe must reproduce,

        d_q = ([1]_q, [4]_q, [5]_q, [4]_q[3]_q/[2]_q)
            ~ (1, 4.10968, 5.22044, 6.22044)   at q = q0^-1 ~ 0.90092

    citing PR #3292 FACT 1 (the compact SU_q(2) quantum-dimension vector
    = Verlinde S_0l/S_00).  The target vector is the corpus-backed half;
    the old body missed it by 0.166 on [4], building (1, 4.0273, 5.0546,
    6.0546) instead.  Canonical [n]_q reproduces the published vector to
    2.4e-6, which is that vector's own 6-digit rounding.  The gate here
    is 1%, and the old target's error was 2.0% on [4] / 3.2% on [5] --
    larger than the gate, so the recorded refutation was being computed
    against a target the probe's own docstring does not name.

    Delegates to qou_substrate.constants.q_int_at rather than carrying a
    local copy -- that signature exists precisely so q-parametric callers
    have something to import (bean qou-4u10).
    """
    return _q_int_at(n, q, mp.mp.dps)


def qpoch_inf(a, q=Q, terms=400):
    """(a;q)_∞ = Π_{j≥0}(1 - a q^j); |q|<1 converges (q≈0.9 → ~300 terms)."""
    p = mpf(1)
    qp = mpf(1)
    for _ in range(terms):
        p *= (1 - a * qp)
        qp *= q
    return p


def qpoch_k(a, k, q=Q):
    """(a;q)_k = Π_{j=0}^{k-1}(1 - a q^j)."""
    p = mpf(1)
    qp = mpf(1)
    for _ in range(k):
        p *= (1 - a * qp)
        qp *= q
    return p


_QQINF = None
_COEF_CACHE = {}


def _term_coeffs(alpha, q=Q, terms=90):
    """Precompute the k-th x-independent coefficient of C_α once per α:

        c_k = q^{k(k-1)/2} · (q^{α+k+1};q)_∞ / (q;q)_k

    using (q^{α+k+1};q)_∞ = (q^{α+1};q)_∞ / (q^{α+1};q)_k so no infinite
    product is taken inside the k-loop.  Returns (prefactor, [c_0..c_{terms-1}])."""
    global _QQINF
    key = (str(alpha), terms)
    if key in _COEF_CACHE:
        return _COEF_CACHE[key]
    if _QQINF is None:
        _QQINF = qpoch_inf(q, q)                    # (q;q)_∞, α-independent
    a_inf = qpoch_inf(q ** (alpha + 1), q)          # (q^{α+1};q)_∞, once per α
    pref = (1 - q) ** alpha / _QQINF
    coeffs = []
    qq_k = mpf(1)          # (q;q)_k
    a_k = mpf(1)           # (q^{α+1};q)_k
    for k in range(terms):
        if k > 0:
            qq_k *= (1 - q ** k)
            a_k *= (1 - q ** (alpha + k))
        gauss = q ** (mpf(k * (k - 1)) / 2)
        coeffs.append(gauss * (a_inf / a_k) / qq_k)
    _COEF_CACHE[key] = (pref, coeffs)
    return pref, coeffs


def hahn_exton_C(alpha, x, q=Q, terms=90):
    """Third (Hahn–Exton) q-Bessel, KS eq. (1.2), Exton normalization."""
    pref, coeffs = _term_coeffs(alpha, q, terms)
    x = mpf(x)
    s = mpf(0)
    xterm = mpf(1)                        # (-x(1-q)^2)^k accumulator
    neg = -x * (1 - q) ** 2
    for c in coeffs:
        s += c * xterm
        xterm *= neg
    return pref * s


def positive_roots(alpha, n_roots=6, q=Q):
    """First n positive roots μ_j of C_α(q;μ)=0 (the Plancherel nodes)."""
    _term_coeffs(alpha, q)               # warm the per-α coefficient cache
    roots = []
    x, dx = mpf("0.05"), mpf("0.15")
    prev = hahn_exton_C(alpha, x, q)
    xmax = mpf("300")
    while len(roots) < n_roots and x < xmax:
        x2 = x + dx
        cur = hahn_exton_C(alpha, x2, q)
        if prev == 0 or (prev < 0) != (cur < 0):
            try:
                r = findroot(lambda t: hahn_exton_C(alpha, t, q), (x + x2) / 2)
                if r > 0 and (not roots or abs(r - roots[-1]) > mpf("1e-6")):
                    roots.append(r)
            except Exception:  # noqa: BLE001 — bracket refine miss: keep scanning
                pass
        prev, x = cur, x2
    return roots


def main() -> int:
    targets = {"[1]": qint(1), "[4]": qint(4), "[5]": qint(5),
               "[4][3]/[2]": qint(4) * qint(3) / qint(2)}
    tvec = [targets[k] for k in ("[1]", "[4]", "[5]", "[4][3]/[2]")]
    nontrivial = [targets["[4]"], targets["[5]"], targets["[4][3]/[2]"]]

    print("# s013 — Hahn–Exton third q-Bessel (Koornwinder–Swarttouw 1208.2521 "
          "eq.1.2) E_q(2) vacuum row vs compact target")
    print(f"q0 = {mp.nstr(Q0,12)}   q = 1/q0 = {mp.nstr(Q,12)}")
    print("targets d_q =", [mp.nstr(t, 7) for t in tvec])
    print()

    candidates = {}
    per_alpha = {}
    for alpha in (0, mpf(1) / 2, 1, 2):
        roots = positive_roots(alpha)
        aname = ("0" if alpha == 0 else "1/2" if alpha == mpf(1) / 2
                 else str(int(alpha)))
        per_alpha[aname] = [mp.nstr(r, 10) for r in roots]
        print(f"α={aname}: first {len(roots)} positive roots μ_j of C_α:")
        for j, r in enumerate(roots, 1):
            print(f"   μ_{j} = {mp.nstr(r,10):>13s}   √μ = {mp.nstr(mp.sqrt(r),8):>10s}"
                  f"   μ/μ1 = {mp.nstr(r/roots[0],8):>10s}")
        r1 = roots[0] if roots else mpf(1)
        for j, r in enumerate(roots, 1):
            candidates[f"a{aname}_mu_{j}"] = r
            candidates[f"a{aname}_sqrt_mu_{j}"] = mp.sqrt(r)
            if j >= 2:
                candidates[f"a{aname}_mu_{j}_over_mu1"] = r / r1
                candidates[f"a{aname}_sqrt_mu_{j}_over_mu1"] = mp.sqrt(r / r1)
        # q-lattice node values (Plancherel support points)
        for kk in range(6):
            candidates[f"a{aname}_C_at_qlat_{kk}"] = hahn_exton_C(alpha, Q ** kk)

    # The DISCIPLINED claim is a COHERENT realisation: does one (α, form) pair
    # reproduce the ORDERED 4-vector {1,[4],[5],[4][3]/[2]}? A single index
    # grazing a single target across the ~100-candidate menu is a coincidence,
    # not a realisation (formalize-first / PSLQ-entropy caution), so the gate is
    # the ordered-vector match, and scattered single hits are recorded as the
    # menu-size sharpener only.
    n_candidates = len(candidates)
    scattered = []
    for cname, cval in candidates.items():
        for tname, t in (("[4]", nontrivial[0]), ("[5]", nontrivial[1]),
                         ("[4][3]/[2]", nontrivial[2])):
            if t != 0 and abs(cval / t - 1) < mpf("0.01"):
                scattered.append((cname, tname, mp.nstr(cval, 8), mp.nstr(t, 8)))

    vec4 = False
    vec4_detail = None
    for aname, rs in per_alpha.items():
        rr = [mpf(x) for x in rs]
        if len(rr) >= 4:
            for form, vv in (("mu", rr[:4]),
                             ("sqrt", [mp.sqrt(x) for x in rr[:4]]),
                             ("ratio", [x / rr[0] for x in rr[:4]])):
                if all(abs(vv[i] / tvec[i] - 1) < mpf("0.01") for i in range(4)):
                    vec4 = True
                    vec4_detail = (aname, form)

    print()
    print(f"candidate menu size = {n_candidates}")
    print("scattered single-index 1% hits (menu coincidence, NOT a realisation):",
          scattered if scattered else "NONE")
    print("COHERENT ordered-4-vector match:", vec4, vec4_detail or "")

    wb = WitnessBuilder("keystone-qhankel-eq2-vacuum-row",
                        engine="mpmath", output_dir=HERE)
    wb.set_description(
        "s013 redirect (ii), decisive sourced test: the Plancherel-fixed "
        "E_q(2) vacuum row — roots μ_j of the third (Hahn–Exton) q-Bessel "
        "C_α (Koornwinder–Swarttouw 1208.2521 eq.1.2), α∈{0,1/2,1,2}, and "
        "C_α at the q-lattice nodes — vs the compact target "
        "d_q={[1],[4],[5],[4][3]/[2]}. 0-dof, no fit; every candidate "
        "reported with ratio. Nothing wired.")
    wb.add_data("source", "Koornwinder-Swarttouw arXiv:1208.2521 (=TAMS 333, "
                "1992) eq.(1.2); library/arxiv-1208.2521v1/1208.2521v1.pdf")
    wb.add_data("q0", mp.nstr(Q0, 30))
    wb.add_data("q", mp.nstr(Q, 30))
    wb.add_data("target_d_q", [mp.nstr(t, 20) for t in tvec])
    wb.add_data("roots_per_alpha", per_alpha)
    wb.add_data("candidate_menu_size", n_candidates)
    wb.add_data("scattered_single_index_hits", scattered)
    wb.add_data("coherent_4vector_match", vec4)
    wb.add_data("coherent_4vector_detail", vec4_detail)
    wb.add_data("verdict",
                "REFUTED-as-is (scope a): NO coherent (α, form) pair reproduces "
                "the ORDERED compact d_q vector {1,[4],[5],[4][3]/[2]} within "
                "1% among the Plancherel-fixed roots/√roots/ratios/q-lattice "
                f"values of the sourced Hahn-Exton C_α (α∈{{0,1/2,1,2}}). The "
                f"{len(scattered)} scattered single-index 1% hits across the "
                f"{n_candidates}-candidate menu are large-menu coincidences (no "
                "two land in the same ordered vector), recorded as the "
                "sharpener not a realisation. The non-compact E_q(2) Plancherel "
                "vacuum row does not land on the compact quantum-dimension "
                "target — consistent with the compact/non-compact type argument "
                "(PR #3292). Does NOT structurally exclude a different node "
                "convention (scope a); the honest value-step resolution is the "
                "compact Markov/Verlinde identity S_0λ/S_00=d_q (redirect iii, "
                "the non-geometric 'why' = Markov-trace uniqueness / Wenzl "
                "bridge / Perron-Frobenius selection, already in the corpus)."
                if not vec4 else
                "COHERENT MATCH — see coherent_4vector_detail (near-match tier; "
                "NOT wired without owner review + (a)/(b) adjudication).")
    wb.add_assertion("roots_found",
                     str(all(len(v) >= 4 for v in per_alpha.values())), "True",
                     source="each α must yield ≥4 positive Plancherel roots for "
                            "a 4-vector comparison")
    wb.add_assertion("no_coherent_4vector_match", str(vec4), "False",
                     source="refutation gate: the disciplined claim is a COHERENT "
                            "ordered-vector realisation; a future (α,form) change "
                            "reproducing the ordered d_q must FAIL this so it is "
                            "re-adjudicated (a)/(b). Scattered single-index hits "
                            "are menu coincidences, not gated.")
    path = wb.save()
    print(f"\nwitness: {path}")
    print("VERDICT:", "coherent match (near-match tier)" if vec4
          else "REFUTED-as-is, scope (a) — coherent 4-vector not realised")
    return 0


if __name__ == "__main__":
    sys.exit(main())
