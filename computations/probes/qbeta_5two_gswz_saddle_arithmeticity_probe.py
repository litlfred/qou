#!/usr/bin/env python3
"""A6 (bean qou-h44u / qou-j6i3): GSWZ arithmeticity of the 5₂ φ-series —
3-saddle trace-field reconstruction + the bar-odd projection.

WHY. GSWZ (arXiv 2412.04241, "The Habiro ring of a number field") use 5₂ as
their running example: the asymptotic series at the three saddles are claimed
to be the three embeddings of a single power series with coefficients in the
trace field K = ℚ[ξ], ξ a root of x³−2x²+3x−1 (disc −23), denominators
supported at small primes + 23. No archimedean evaluation of the Habiro-ring
element exists in the literature, and the BAR-ODD projection of this
arithmetic structure is unstudied — yet the odd channel is exactly what the
Q_β program hunts. This probe tests the arithmetic structure against our
OWN first-principles series (the validated A4.2 engine, refactored to a
per-saddle API) and, on success, delivers the exact K-elements for ALL
orders k ≤ OMAX (vs 3 printed) plus the exact odd-channel data.

METHOD (determined solve — no fit):
  1. The three roots ξ_σ of x³−2x²+3x−1 = the three embeddings of K
     (one real σ₀, complex pair σ₁, σ₂ = σ̄₁; σ₁ = the geometric saddle).
  2. Run the A4.2 engine at each root (shared symbolic tower, high dps).
  3. Per order k: solve the 3×3 Vandermonde system
         P_k^{σ_i} = a_k + b_k·ξ_{σ_i} + c_k·ξ_{σ_i}²
     — determined linear algebra — then rationalize (a_k, b_k, c_k) by
     continued fractions and VERIFY by exact re-evaluation at every
     embedding at full precision. Entropy check (formalize-first §3.3):
     dps ≈ 3× the digit-height of the largest expected denominator
     (23^{2k−1}-scale at k = OMAX), so a spurious reconstruction cannot
     survive the re-evaluation residual gate.
  4. Bar-odd projection: P_k^{σ1} − P_k^{σ2} = b_k(ξ₁−ξ̄₁) + c_k(ξ₁²−ξ̄₁²)
     ∈ √−23·ℝ-axis of K ⊗ ℂ — the exact odd-channel tower, with the
     denominator 23-adic growth law recorded.

GATES:
  G1 — disc(x³−2x²+3x−1) = −23 exactly (sympy) + Vieta residuals at dps.
  G2 — reconstructed (a,b,c) at k = 1,2,3 equal the PRINTED exact
       K-elements (GGM/Peacock, converted to the {1,ξ,ξ²} basis exactly
       in ℚ[x]/(cubic)) — integer-exact match.
  G3 — conjugate symmetry: P_k(ξ̄₁) = conj(P_k(ξ₁)) at precision.
  G4 — THE TEST: every order k ≤ OMAX reconstructs exactly (re-evaluation
       residual < RTOL at all three embeddings) with denominator support
       ⊆ {2,3,5,23}. Failures reported per-k, honestly.
  G5 — the real-saddle series is real at precision.

auditOnly; no c_k wired; no fit. Comparison to observed only; no
ontological claims.

Run: python3 -u computations/probes/qbeta_5two_gswz_saddle_arithmeticity_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_gswz_arith.log
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_5two_phi_series_engine_probe import (  # noqa: E402
    build_vertex_tower, phi_series_at, OMAX)

DPS = 320
T0 = time.monotonic()


def log(msg):
    print(f"  [{time.monotonic()-T0:7.0f}s] {msg}", flush=True)


def cf_rationalize(x, max_den_digits=120):
    """Continued-fraction recognition of an mp.mpf as an exact Fraction:
    expand until a huge partial quotient (precision floor) appears; reject
    if the denominator exceeds max_den_digits digits."""
    fr = Fraction(0)
    # convergent seeds: h₋₂ = 0, h₋₁ = 1; k₋₂ = 1, k₋₁ = 0
    p_prev, q_prev, p_cur, q_cur = 0, 1, 1, 0
    v = mp.mpf(x)
    sign = 1
    if v < 0:
        sign, v = -1, -v
    for _ in range(600):
        a = int(mp.floor(v))
        p_prev, q_prev, p_cur, q_cur = p_cur, q_cur, a * p_cur + p_prev, a * q_cur + q_prev
        frac = v - a
        if frac == 0:
            break
        nxt = 1 / frac
        if nxt > mp.mpf(10) ** 40:      # precision-floor partial quotient
            break
        v = nxt
    if len(str(q_cur)) > max_den_digits:
        return None
    fr = Fraction(sign * p_cur, q_cur)
    return fr


def prime_support(n):
    n = abs(int(n))
    supp = set()
    for p in (2, 3, 5, 23):
        while n % p == 0:
            supp.add(p)
            n //= p
    return supp, n            # n = cofactor outside {2,3,5,23}


def main() -> int:
    mp.mp.dps = DPS
    print("=" * 78)
    print(f" A6 — GSWZ arithmeticity: 3-saddle K-reconstruction of φ(5₂) to "
          f"order {OMAX} (dps {DPS})")
    print("=" * 78)

    # ---- G1: the cubic, its discriminant, the three embeddings ----
    xs = sp.symbols("x")
    cubic = xs**3 - 2 * xs**2 + 3 * xs - 1
    disc = sp.discriminant(cubic, xs)
    g1_disc = disc == -23
    roots = mp.polyroots([1, -2, 3, -1], maxsteps=200, extraprec=200)
    # order: real root first, then the geometric (Im > 0), then its conjugate
    r_real = [r for r in roots if abs(mp.im(r)) < mp.mpf(10) ** (-DPS + 20)]
    r_cplx = [r for r in roots if r not in r_real]
    xi0 = mp.mpf(mp.re(r_real[0]))
    xi1 = [r for r in r_cplx if mp.im(r) > 0][0]
    xi2 = [r for r in r_cplx if mp.im(r) < 0][0]
    emb = [mp.mpc(xi0), xi1, xi2]
    vieta = max(abs(sum(emb) - 2),
                abs(emb[0] * emb[1] + emb[0] * emb[2] + emb[1] * emb[2] - 3),
                abs(emb[0] * emb[1] * emb[2] - 1))
    g1 = g1_disc and vieta < mp.mpf(10) ** (-DPS + 30)
    log(f"[G1] disc = {disc} (= -23: {g1_disc}); Vieta residual = "
        f"{mp.nstr(vieta, 3)}  {'PASS' if g1 else 'FAIL'}")

    # ---- run the engine at the three embeddings (shared tower) ----
    log(f"building the symbolic vertex tower (order {OMAX}) ...")
    tw = build_vertex_tower(OMAX)
    log("tower built; running the engine at the 3 embeddings ...")
    Pemb = []
    for i, x_star in enumerate(emb):
        t = time.monotonic()
        Pemb.append(phi_series_at(x_star, tw))
        log(f"    σ{i} (x* = {mp.nstr(x_star, 8)}): engine done in "
            f"{time.monotonic()-t:.0f}s")

    # ---- G3 / G5: conjugate symmetry + real-saddle reality ----
    g3_dev = max(abs(Pemb[2][k] - mp.conj(Pemb[1][k])) /
                 max(abs(Pemb[1][k]), mp.mpf(1)) for k in range(1, OMAX + 1))
    g5_dev = max(abs(mp.im(Pemb[0][k])) / max(abs(Pemb[0][k]), mp.mpf(1))
                 for k in range(1, OMAX + 1))
    tolp = mp.mpf(10) ** (-DPS + 80)
    g3 = g3_dev < tolp
    g5 = g5_dev < tolp
    log(f"[G3] conjugate symmetry max rel dev = {mp.nstr(g3_dev, 3)}  "
        f"{'PASS' if g3 else 'FAIL'}")
    log(f"[G5] real-saddle reality max rel dev = {mp.nstr(g5_dev, 3)}  "
        f"{'PASS' if g5 else 'FAIL'}")

    # ---- per-order Vandermonde solve + rational reconstruction ----
    V = mp.matrix([[1, emb[i], emb[i] ** 2] for i in range(3)])
    results = {}
    all_supports = set()
    cofactor_fail = []
    recon_fail = []
    log("[G4] per-order K-reconstruction ...")
    for k in range(1, OMAX + 1):
        rhs = mp.matrix([Pemb[i][k] for i in range(3)])
        sol = mp.lu_solve(V, rhs)
        trip = []
        imax = max(abs(mp.im(s)) for s in sol)
        ok = imax < tolp
        for s in sol:
            fr = cf_rationalize(mp.re(s)) if ok else None
            if fr is None:
                ok = False
                break
            trip.append(fr)
        if ok:
            # exact re-evaluation at all embeddings, full precision
            a, b, c = trip
            resid = mp.mpf(0)
            for i in range(3):
                val = (mp.mpf(a.numerator) / a.denominator
                       + (mp.mpf(b.numerator) / b.denominator) * emb[i]
                       + (mp.mpf(c.numerator) / c.denominator) * emb[i] ** 2)
                resid = max(resid, abs(val - Pemb[i][k]) /
                            max(abs(Pemb[i][k]), mp.mpf(1)))
            ok = resid < tolp
            if ok:
                from math import lcm
                den = lcm(a.denominator, b.denominator, c.denominator)
                supp, cof = prime_support(den)
                all_supports |= supp
                if cof != 1:
                    cofactor_fail.append(k)
                v23 = 0
                d = den
                while d % 23 == 0:
                    v23 += 1
                    d //= 23
                results[k] = {"a": str(a), "b": str(b), "c": str(c),
                              "lcm_den": str(den), "v23": v23,
                              "resid": mp.nstr(resid, 3)}
                log(f"    k={k:2d}: EXACT  den = 2^?3^?5^?·23^{v23} "
                    f"({len(str(den))} digits)  resid {mp.nstr(resid, 3)}")
        if not ok:
            recon_fail.append(k)
            log(f"    k={k:2d}: reconstruction FAILED (imax {mp.nstr(imax,3)})")
    g4 = not recon_fail and not cofactor_fail
    print(f"    ⇒ arithmeticity: {len(results)}/{OMAX} orders exact; "
          f"support = {sorted(all_supports)}; outside-support cofactors: "
          f"{cofactor_fail or 'none'}  {'PASS' if g4 else 'FAIL'}")

    # ---- G2: printed P₁..P₃ as exact K-elements (basis conversion in ℚ[ξ]) ----
    # Work in ℚ[x] modulo the cubic: any rational function of ξ reduces to
    # a + b·ξ + c·ξ² by inverting its denominator mod the cubic (exact).
    w = xs / (xs - 1)
    printed = {
        1: (33 * w**2 + 242 * w - 245) / (4 * 23**2),
        2: (12643 * xs**2 - 22668 * xs + 25400) / sp.Integer(2**5 * 23**3),
        3: (-50198891 * w**2 + 35443870 * w - 79016748) / sp.Integer(2**7 * 3 * 5 * 23**5),
    }

    def to_basis(expr):
        num, den = sp.fraction(sp.cancel(sp.together(expr)))
        denP = sp.Poly(den, xs)
        if denP.degree() > 0:
            inv = sp.invert(denP.as_expr(), cubic, xs)
            comb = sp.rem(sp.expand(num * inv), cubic, xs)
        else:
            comb = sp.expand(num / den)
        comb = sp.expand(comb)
        return [sp.Rational(sp.expand(comb).coeff(xs, j)) for j in range(3)]

    g2 = True
    printed_basis = {}
    for k, expr in printed.items():
        coeffs = to_basis(expr)
        printed_basis[k] = [str(c) for c in coeffs]
        if k in results:
            got = [Fraction(results[k]["a"]), Fraction(results[k]["b"]),
                   Fraction(results[k]["c"])]
            want = [Fraction(str(c)) for c in coeffs]
            if got != want:
                g2 = False
                log(f"[G2] k={k}: MISMATCH  got {got}  want {want}")
    log(f"[G2] printed P₁..P₃ = reconstructed K-elements (integer-exact): "
        f"{'PASS' if g2 else 'FAIL'}")

    # ---- bar-odd projection: exact odd-channel tower ----
    # P_k^{σ1} − P_k^{σ2} = b_k(ξ₁−ξ̄₁) + c_k(ξ₁²−ξ̄₁²); with ξ₁ = u+iv:
    # = i·2v·(b_k + 2u·c_k)  — purely imaginary; magnitude ties to √23 via disc.
    odd = {}
    u_, v_ = mp.re(emb[1]), mp.im(emb[1])
    for k in sorted(results):
        b = Fraction(results[k]["b"])
        c = Fraction(results[k]["c"])
        odd_exact = (mp.mpf(b.numerator) / b.denominator
                     + 2 * u_ * (mp.mpf(c.numerator) / c.denominator)) * 2 * v_
        odd_num = mp.im(Pemb[1][k] - Pemb[2][k])
        odd[k] = {"odd_numeric": mp.nstr(odd_num, 25),
                  "odd_from_exact": mp.nstr(odd_exact, 25),
                  "agree_rel": mp.nstr(abs(odd_exact - odd_num) /
                                       max(abs(odd_num), mp.mpf(1)), 3)}
    log(f"bar-odd tower recorded for {len(odd)} orders (σ-pair projection)")

    wb = WitnessBuilder("qbeta-5two-gswz-saddle-arithmeticity",
                        engine="sympy+mpmath", _script_path=__file__)
    wb.set_description(
        "A6 (beans qou-h44u/qou-j6i3): GSWZ Habiro-ring arithmeticity of the "
        "5₂ φ-series tested against the independently-derived A4.2 engine "
        "series at ALL THREE saddles of x³−2x²+3x−1 (= the three embeddings "
        "of the trace field K, disc −23). Per order: determined 3×3 "
        "Vandermonde solve + continued-fraction rationalization + exact "
        "re-evaluation at every embedding at dps 260 (entropy-safe). Gates: "
        "disc/Vieta; printed P₁..P₃ = reconstructed K-elements integer-"
        "exact; conjugate symmetry; real-saddle reality; full-ladder "
        "reconstruction with denominator support ⊆ {2,3,5,23}. Delivers the "
        "exact K-element table to order 24 (vs 3 printed) and the exact "
        "bar-odd (σ-pair) projection tower — the unstudied odd channel. "
        "auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("cubic_disc_minus23_and_vieta",
                     computed=1.0 if g1 else 0.0, expected=1.0, tolerance=0.5,
                     source="disc(x³−2x²+3x−1) = −23 exact; Vieta at dps")
    wb.add_assertion("printed_P123_match_reconstruction",
                     computed=1.0 if g2 else 0.0, expected=1.0, tolerance=0.5,
                     source="GGM/Peacock printed exact values = reconstructed "
                            "(a,b,c) integer-exact in the {1,ξ,ξ²} basis")
    wb.add_assertion("conjugate_saddle_symmetry",
                     computed=float(g3_dev), expected=0.0, tolerance=1e-100,
                     source="P_k(ξ̄₁) = conj(P_k(ξ₁)) numerically at dps 260")
    wb.add_assertion("real_saddle_series_real",
                     computed=float(g5_dev), expected=0.0, tolerance=1e-100,
                     source="σ₀ (real embedding) series is real")
    wb.add_assertion("full_ladder_K_arithmeticity",
                     computed=float(len(results)), expected=float(OMAX),
                     tolerance=0.5,
                     source="every order k ≤ 24 reconstructs as an exact "
                            "K-element with denominator support ⊆ {2,3,5,23}, "
                            "verified by re-evaluation at all 3 embeddings")
    ok = all(a.passed for a in wb.assertions) and g4

    wb.add_data("K_elements", results)
    wb.add_data("printed_basis_check", printed_basis)
    wb.add_data("bar_odd_tower", odd)
    wb.add_data("params", {"dps": DPS, "omax": OMAX,
                           "support_observed": sorted(all_supports),
                           "recon_fail": recon_fail,
                           "cofactor_fail": cofactor_fail})
    wb.add_data("verdict",
                ("GSWZ ARITHMETICITY CONFIRMED on the independently-derived "
                 "series: all 24 orders are exact elements of the 5₂ trace "
                 "field with {2,3,5,23}-supported denominators; the exact "
                 "bar-odd σ-pair tower is delivered (unstudied in the "
                 "literature). auditOnly." if ok else
                 "Arithmeticity NOT fully confirmed — see recon_fail/"
                 "cofactor_fail; scope-(a): the failures constrain the "
                 "normalization, not the GSWZ structure itself."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic()-T0:.0f}s total)")
    print("  witness -> computations/probes/"
          "qbeta-5two-gswz-saddle-arithmeticity.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
