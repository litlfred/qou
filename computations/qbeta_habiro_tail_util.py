#!/usr/bin/env python3
"""Canonical compute path for the 5₂ Habiro-tail q-Borel coefficients —
the (★) identity, EXACT-verified and cancellation-free.

THE IDENTITY (derived on PR #4195/#4226, A6.4). With q̄ = a², q̃ = a⁻²:

    C_n(a)·(q̄;q̄)_n²·a^{−(5n²+7n)}
        = (−1)ⁿ·(q̃;q̃)_n²·Σ_{k=0}^n q̃^{k(n+1)}·[n,k]_{q̃}       (★)

where C_n is the exact Masbaum integer-Laurent coefficient of 5₂
(DOI 10.2140/agt.2003.3.537) and [n,k] the Gaussian binomial. The LHS is
the W9-lane q-Borel transform T̂_n·(−1)ⁿ evaluated literally — a
~640-digit cancellation at n ≈ 96 needing dps ≈ 800. The RHS is
POSITIVE-TERM (cancellation-free): dps 60 suffices at any depth.

Status of (★): a finite integer-Laurent identity per n, verified
MACHINE-EXACTLY here (integer dict equality, no numerics — the
`verify_star_exact` gate) and numerically at 1e-497 on PR #4195. The
general-n Lean pin is bean qou-rk84.

WIRING SCOPE (STRICT): this module wires the *identity* as compute
infrastructure — faster, stabler evaluation of the same exact object.
It does NOT wire any physical claim: D_odd, O_φ, and the pole-ladder
physics remain scope-(a)/auditOnly; nothing here feeds a production
physics dashboard.

Public API:
    t_hat_exact(n, qt, poch=None) — (−1)ⁿT̂_n via the RHS of (★)
    qpoch_list(qt, nmax)          — (q̃;q̃)_n table
    residue_c_inf(qt)             — c∞ = (q̃;q̃)_∞² (pole residue at w=−1)
    c52_laurent(n)                — exact Masbaum C_n integer Laurent dict
    verify_star_exact(n)          — machine-exact check of (★) at order n

Self-test (run as a script): exact (★) for n ≤ 32, C_n cross-check vs
the profile module, numeric spot-equivalence, witness emission.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

# ----------------------------- exact Laurent helpers -----------------------


def ladd(A, B):
    C = dict(A)
    for e, c in B.items():
        C[e] = C.get(e, 0) + c
    return {e: c for e, c in C.items() if c != 0}


def lmul(A, B):
    C = {}
    for ea, ca in A.items():
        for eb, cb in B.items():
            e = ea + eb
            C[e] = C.get(e, 0) + ca * cb
    return {e: c for e, c in C.items() if c != 0}


def lscale(A, s):
    return {e: s * c for e, c in A.items()}


def lshift(A, d):
    return {e + d: c for e, c in A.items()}


def gauss_binom_rows(nmax):
    """Pascal triangle of Gaussian binomials [n,k]_q as integer dicts over
    q-exponents, rows 0..nmax."""
    rows = [[{0: 1}]]
    for nn in range(1, nmax + 1):
        prev = rows[-1]
        new = [{0: 1}]
        for kk in range(1, nn):
            shifted = {e + kk: c for e, c in prev[kk].items()} \
                if kk < len(prev) else {}
            new.append(ladd(prev[kk - 1], shifted))
        new.append({0: 1})
        rows.append(new)
    return rows


def c52_laurent(n, rows=None):
    """Exact Masbaum C_{5₂,n}(a) as an integer Laurent dict over
    a-exponents (same algebra as the merged profile module)."""
    if rows is None:
        rows = gauss_binom_rows(n)
    out = {}
    for k in range(n + 1):
        bq = rows[n][k]
        bb = {2 * e - k * (n - k): c for e, c in bq.items()}
        base = 3 * n * n + 5 * n + k * k - 2 * k - 3 * n * k
        out = ladd(out, {base + e: c for e, c in bb.items()})
    if n % 2 == 1:
        out = {e: -c for e, c in out.items()}
    return out


def verify_star_exact(n, rows=None):
    """Machine-exact check of (★) at order n: both sides expanded as
    integer Laurent dicts in a; returns True iff identical. No numerics."""
    if rows is None:
        rows = gauss_binom_rows(n)
    # LHS: C_n(a)·(q̄;q̄)_n²·a^{−(5n²+7n)}, q̄ = a²
    poch_bar = {0: 1}
    for j in range(1, n + 1):
        poch_bar = lmul(poch_bar, ladd({0: 1}, {2 * j: -1}))
    lhs = lshift(lmul(c52_laurent(n, rows), lmul(poch_bar, poch_bar)),
                 -(5 * n * n + 7 * n))
    # RHS: (−1)ⁿ·(q̃;q̃)_n²·Σ_k q̃^{k(n+1)}[n,k]_{q̃}, q̃ = a⁻²
    poch_til = {0: 1}
    for j in range(1, n + 1):
        poch_til = lmul(poch_til, ladd({0: 1}, {-2 * j: -1}))
    ssum = {}
    for k in range(n + 1):
        bink = {-2 * e: c for e, c in rows[n][k].items()}   # [n,k]_{q̃}
        ssum = ladd(ssum, lshift(bink, -2 * k * (n + 1)))
    rhs = lscale(lmul(lmul(poch_til, poch_til), ssum), (-1) ** n)
    return lhs == rhs


# ----------------------------- numeric API ---------------------------------


def qpoch_list(qt, nmax):
    """(q̃;q̃)_n for n = 0..nmax at the current mp precision."""
    out = [mp.mpf(1)]
    for j in range(1, nmax + 1):
        out.append(out[-1] * (1 - qt ** j))
    return out


def t_hat_exact(n, qt, poch=None):
    """(−1)ⁿ·T̂_n via the cancellation-free RHS of (★). All terms
    positive: full accuracy at the working precision (no dps blowup)."""
    if poch is None:
        poch = qpoch_list(qt, n)
    s = mp.mpf(0)
    for k in range(n + 1):
        term = qt ** (k * (n + 1)) * poch[n] / (poch[k] * poch[n - k])
        s += term
        if term < mp.mpf("1e-80") * s:
            break
    return poch[n] ** 2 * s


def residue_c_inf(qt, tol_exp=70):
    """c∞ = (q̃;q̃)_∞² — the residue of the simple pole of the Borel
    function ĝ(w) at w = −1 (derived, PR #4226)."""
    p = mp.mpf(1)
    j = 1
    while True:
        f = 1 - qt ** j
        p *= f
        if abs(1 - f) < mp.mpf(10) ** (-tol_exp):
            break
        j += 1
    return p ** 2


# ----------------------------- self-test -----------------------------------


def main() -> int:
    import importlib.util
    import time
    import _path_bridge as _bridge  # noqa: F401  (wires witness_base et al.)
    from witness_base import WitnessBuilder
    from qou_substrate.constants import q_at

    t0 = time.time()
    print("=" * 78)
    print(" qbeta_habiro_tail_util — (★) canonical path self-test")
    print("=" * 78)
    N_EXACT = 32

    # G1: machine-exact (★) for n ≤ N_EXACT
    rows = gauss_binom_rows(N_EXACT)
    g1 = all(verify_star_exact(n, rows) for n in range(N_EXACT + 1))
    print(f"\n[G1] (★) integer-Laurent EXACT for n ≤ {N_EXACT}: "
          f"{'PASS' if g1 else 'FAIL'}")

    # G2: C_n cross-check vs the merged profile module
    _spec = importlib.util.spec_from_file_location(
        "qbeta_g3_5two_masbaum_barodd_profile",
        _HERE / "probes" / "qbeta_g3_5two_masbaum_barodd_profile.py")
    _mb = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mb)
    g2 = all(c52_laurent(n, rows) == _mb.C52(n) for n in (3, 11, 24, 32))
    print(f"[G2] c52_laurent == profile C52 exactly at n = 3, 11, 24, 32: "
          f"{'PASS' if g2 else 'FAIL'}")

    # G3: numeric spot-equivalence at the substrate (dps 60 vs the identity)
    mp.mp.dps = 60
    t = mp.log(q_at(50))
    qt = mp.e ** (-t)
    poch = qpoch_list(qt, 100)
    v96 = t_hat_exact(96, qt, poch)
    c_inf = residue_c_inf(qt)
    # transient bound at n = 96: |u_n/c∞ − 1| ≲ q̃^{n+1}/(1−q̃)² (k=1 term
    # + poch-tail, both O(q̃^{n+1}) with O(1/(1−q̃)) amplitudes)
    bound3 = qt ** 97 / (1 - qt) ** 2
    dev3 = abs(v96 - c_inf) / c_inf
    g3 = dev3 < bound3
    print(f"[G3] t_hat_exact(96) = {mp.nstr(v96, 12)}  →  c∞ = "
          f"{mp.nstr(c_inf, 12)} (rel {mp.nstr(dev3, 3)} < derived bound "
          f"{mp.nstr(bound3, 3)}): {'PASS' if g3 else 'FAIL'}")

    wb = WitnessBuilder("qbeta-habiro-tail-util", engine="sympy-free exact + mpmath",
                        _script_path=__file__)
    wb.set_description(
        "Canonical compute path for the 5₂ Habiro-tail q-Borel "
        "coefficients: the (★) identity (derived PR #4195/#4226) verified "
        "MACHINE-EXACTLY as integer-Laurent dict equality for n ≤ 32 (no "
        "numerics), C_n cross-checked against the merged profile module, "
        "and the cancellation-free numeric path spot-gated at the "
        "substrate (dps 60 replaces the direct route's dps 800). WIRING "
        "SCOPE: compute infrastructure only — D_odd/O_φ/pole-ladder "
        "physics remain scope-(a)/auditOnly; no physical claim is wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_assertion("star_exact_to_32",
                     computed=1.0 if g1 else 0.0, expected=1.0, tolerance=0.5,
                     source="(★) as integer-Laurent dict equality, n ≤ 32 — "
                            "machine-exact, no numerics")
    wb.add_assertion("c52_matches_profile_module",
                     computed=1.0 if g2 else 0.0, expected=1.0, tolerance=0.5,
                     source="c52_laurent == the merged profile module's C52")
    wb.add_assertion("numeric_path_reaches_residue",
                     computed=dev3 / bound3, expected=0.0, tolerance=1.0,
                     source="t_hat_exact(96) → (q̃;q̃)_∞² within the DERIVED "
                            "transient bound q̃⁹⁷/(1−q̃)² at dps 60")
    ok = all(a.passed for a in wb.assertions)
    wb.add_data("identity",
                "C_n(a)(qbar;qbar)_n^2 a^-(5n^2+7n) = (-1)^n (qt;qt)_n^2 "
                "sum_k qt^{k(n+1)} [n,k]_qt")
    wb.add_data("wiring_scope",
                "compute-infra only; no physics wired; consumers adopt on "
                "next touch (W9-family probes)")
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.time()-t0:.0f}s)")
    print("  witness -> computations/qbeta-habiro-tail-util.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
