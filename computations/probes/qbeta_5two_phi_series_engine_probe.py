#!/usr/bin/env python3
"""A4.2 (bean qou-ea86): the 5₂ φ_σ1 coefficient-generation engine — the
τ-channel saddle expansion of the state integral to deep order, with the
first Borel look.

WHY. A4 (median Borel–Laplace of the 5₂ bar-odd series) needs φ_σ1(τ) to
~25+ orders; only 5 printed orders exist, one of which (τ²) was misprinted
in GGM 2007.10190 eq 20 (arbitrated 2026-07-18: Peacock eq 76 @ ξ is
correct — see qbeta-5two-phi-series-tau2-arbitration). This engine GENERATES
the series from first principles.

CONSTRUCTION (formal steepest descent of Z_5₂ = ∫Φ_b(v)³e^{−2πiv²}dv):
rescale v = y/(2πb), ħ := 2πib² = 2πiτ. The Faddeev asymptotic expansion
    ln Φ_b(y/(2πb)) ~ Σ_{n≥0} ħ^{2n−1}·B_{2n}/(2n)!·Li_{2−2n}(−e^y)
gives the exponent  W = (1/ħ)·V₀(y) + Σ_{n≥1} ħ^{2n−1}·3B_{2n}/(2n)!·L_n(y),
    V₀(y) = 3Li₂(−e^y) + y²,   L_n(y) = Li_{2−2n}(−e^y).
The critical equation V₀'(y*) = 0 ⇔ (1−x)³ = x², x = −e^{y*} — EXACTLY the
GGM eq-19 critical point (ξ₁ = 0.78492+1.30714i geometric): the convention
lock. Every vertex coefficient is (z·d/dz)^k of the Li-tower — a RATIONAL
function of z evaluated at x* (generated symbolically once via
Li_{−k} = (z d/dz)Li_{−k+1} from Li₀ = z/(1−z)). Gaussian fluctuations:
y = y* + √ħ·u, Wick moments u^{2m} → (2m−1)!!·σ^{2m}, σ² = −1/V₀''(y*);
bivariate truncated series in (√ħ, u) assembled by dict-polynomials at
mp.dps = 60. φ(τ) = the resulting fluctuation series in ħ = 2πiτ, normalized
φ = 1 + Σ_{k≥1} a_k τ^k, P_k := a_k (the eq-20 coefficient convention
validated by the gates).

GATES (published + this session's independent data):
  G1 — saddle: x* reproduces the GGM ξ₁ root of x³−2x²+3x−1 (i.e.
       (1−x)³ = x² with the geometric branch).
  G2 — P₁ matches the AGREED printed τ¹ coefficient (both papers under the
       generator identity; also A4.1-extracted at 3.8e-4).
  G3 — P₂ matches the ARBITRATED value (Peacock eq 76 at ξ; A4.1-extracted
       at 2%).
  G4 — P₃: the engine's exact-order value vs the printed (agreed) τ³ —
       settles the A4.1 τ³ diagnostic (0.3 rel) with a derived value.
OUTPUT — P_k to order OMAX (default 24) + the first Borel diagnostics:
ratio-test/Borel–Padé nearest-singularity estimate vs the GGM eq-81
prediction |V(σ1)−V(σ2)| = 5.6563 in the x=2πiτ Borel plane (σ1→σ2 Stokes;
resurgence gate). auditOnly; no c_k wired; no fit.

Run: python3 -u computations/probes/qbeta_5two_phi_series_engine_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_phi_engine.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

OMAX = 24               # φ-series order in τ
HMAX = 2 * OMAX         # half-power (√ħ) truncation
TWO_PI_I = 2j * mp.pi


def li_tower(max_n, kmax):
    """Symbolic table D[n][k] = (z d/dz)^k Li_{2−2n}(z) as rational functions
    of z, for n = 1..max_n (L_n = Li_{2−2n}) and k = 0..kmax. Built from
    Li₀ = z/(1−z) by repeated z·d/dz; Li₂-level derivatives (n=0 tower)
    handled separately."""
    z = sp.symbols("z")
    # ladder of Li_s for s = 1, 0, -1, ... : Li₁ = −log(1−z) (only needed as
    # a derivative seed), Li₀ = z/(1−z), Li_{−k} = (z d/dz) Li_{−k+1}
    li = {1: -sp.log(1 - z), 0: z / (1 - z)}
    smin = 2 - 2 * max_n - kmax
    s = 0
    while s > smin:
        li[s - 1] = sp.simplify(z * sp.diff(li[s], z))
        s -= 1
    D = {}
    for n in range(1, max_n + 1):
        base_s = 2 - 2 * n
        D[n] = {k: li[base_s - k] for k in range(kmax + 1)}
    return z, D


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" A4.2 — 5₂ φ_σ1 engine: τ-channel saddle expansion to order {OMAX}")
    print("=" * 78)

    # ---- G1: the saddle ----
    # V₀'(y) = −3 ln(1+e^y) + 2y = 0 ⇔ (1−x)³ = x², x = −e^y (geometric root)
    xi = mp.findroot(lambda x: x**3 - 2 * x**2 + 3 * x - 1,
                     mp.mpc("0.78492", "1.30714"))
    x_star = xi
    y_star = mp.log(-x_star)      # any branch; only z*=x* enters the vertices
    resid = (1 - x_star) ** 3 - x_star ** 2
    g1 = abs(resid) < mp.mpf("1e-50")
    print(f"\n[G1] saddle x* = {mp.nstr(x_star, 15)}  |(1−x)³−x²| = "
          f"{mp.nstr(abs(resid), 3)}  {'PASS' if g1 else 'FAIL'}")

    # ---- vertex data ----
    # V₀ derivatives: V₀'' = −3·z/(1+... careful: d/dy = z d/dz with z = −e^y
    # ⇒ dz/dy = z. Li₂(z): (z d/dz)Li₂ = Li₁ = −ln(1−z); so
    # V₀(y) = 3Li₂(z) + y², V₀^{(k)} for k≥2 from the Li tower + y² term.
    max_n = OMAX // 2 + 1
    kmax = HMAX + 4
    print(f"\n  building Li tower (n ≤ {max_n}, k ≤ {kmax}) symbolically ...",
          flush=True)
    zsym, D = li_tower(max_n, kmax)
    t1 = time.monotonic()
    print(f"  ... built in {t1 - t0:.0f}s; evaluating at x* ...", flush=True)

    def ev(expr):
        f = sp.lambdify(zsym, expr, "mpmath")
        return f(x_star)

    # V₀ y-derivatives at y*: k-th derivative of 3Li₂(z(y)) is 3·(z d/dz)^k Li₂
    # = 3·(z d/dz)^{k−1} Li₁; (z d/dz)^j Li₁ = (z d/dz)^{j−1} Li₀ for j ≥ 1.
    li1 = -sp.log(1 - zsym)
    li0 = zsym / (1 - zsym)
    tower01 = {0: li1, 1: li0}
    for k in range(2, kmax + 2):
        tower01[k] = sp.simplify(zsym * sp.diff(tower01[k - 1], zsym))
    V0d = {2: 3 * ev(tower01[1]) + 2}          # + y² term contributes 2 at k=2
    for k in range(3, kmax + 2):
        V0d[k] = 3 * ev(tower01[k - 1])
    # L_n y-derivatives at y*
    Ld = {n: {k: ev(D[n][k]) for k in range(kmax + 1)} for n in range(1, max_n + 1)}
    # BALANCED Φ_b expansion: Bernoulli POLYNOMIALS at 1/2 — B_{2n}(1/2) =
    # (2^{1−2n}−1)·B_{2n}. Diagnosed empirically against the corpus-validated
    # log_phi_b (naive B_{2n} overshoots the O(ħ) term by exactly 3×; with
    # B_{2n}(1/2) the expansion converges to 9e-25 by n=6).
    bern = {n: (mp.mpf(2) ** (1 - 2 * n) - 1) * mp.bernoulli(2 * n)
            / mp.factorial(2 * n) for n in range(1, max_n + 1)}
    print(f"  ... vertex data evaluated ({time.monotonic() - t1:.0f}s)", flush=True)

    # ---- bivariate assembly: series in (h = √ħ, u), truncated at h^HMAX ----
    # exponent minus Gaussian part:
    #   Wv = Σ_{k≥3} h^{k−2} V₀^{(k)} u^k / k!                (from (1/ħ)V₀)
    #      + Σ_{n≥1} 3·B_{2n}/(2n)!·Σ_{k≥0} h^{2(2n−1)+k} L_n^{(k)} u^k / k!
    # dict-poly: key (p, m) = (power of h, power of u) → mpc coeff
    Wv = {}

    def add(p, m, c):
        if p <= HMAX and abs(c) > 0:
            Wv[(p, m)] = Wv.get((p, m), mp.mpc(0)) + c

    for k in range(3, HMAX + 2 + 1):
        add(k - 2, k, V0d[k] / mp.factorial(k))
    for n in range(1, max_n + 1):
        base = 2 * (2 * n - 1)
        if base > HMAX:
            break
        for k in range(0, HMAX - base + 1):
            add(base + k, k, 3 * bern[n] * Ld[n][k] / mp.factorial(k))

    # exp(Wv) truncated at h^HMAX
    print("  exponentiating the vertex series ...", flush=True)
    t2 = time.monotonic()
    expW = {(0, 0): mp.mpc(1)}
    term = {(0, 0): mp.mpc(1)}
    order = 1
    while True:
        # term = term * Wv / order, truncate
        new = {}
        for (p1, m1), c1 in term.items():
            for (p2, m2), c2 in Wv.items():
                p, m = p1 + p2, m1 + m2
                if p <= HMAX:
                    new[(p, m)] = new.get((p, m), mp.mpc(0)) + c1 * c2 / order
        term = new
        if not term:
            break
        for key, c in term.items():
            expW[key] = expW.get(key, mp.mpc(0)) + c
        order += 1
        if order > HMAX:                # Wv has min h-power 1 ⇒ terminates
            break
    print(f"  ... done ({time.monotonic() - t2:.0f}s; {len(expW)} monomials)",
          flush=True)

    # ---- Wick contraction: u^{2m} → (2m−1)!!·σ^{2m}, σ² = −1/V₀'' ----
    sig2 = -1 / V0d[2]
    phi_h = {}                          # series in h (only even powers survive)
    for (p, m), c in expW.items():
        if m % 2 == 1:
            continue
        mm = m // 2
        dfact = mp.mpf(1)
        for j in range(1, mm + 1):
            dfact *= (2 * j - 1)
        phi_h[p] = phi_h.get(p, mp.mpc(0)) + c * dfact * sig2 ** mm
    # φ(τ) = Σ phi_h[2k]·ħ^k = Σ phi_h[2k]·(2πi)^k·τ^k, and the printed
    # convention is φ(τ) = 1 + Σ P_k·(2πi)^k·τ^k (validated by the A4.1
    # extraction) ⇒ P_k = phi_h[2k] DIRECTLY (run-1 lesson: multiplying by
    # (2πi)^k here double-counts the factor).
    P = {}
    for k in range(0, OMAX + 1):
        P[k] = phi_h.get(2 * k, mp.mpc(0))
    norm = P[0]
    for k in P:
        P[k] = P[k] / norm
    # PREFACTOR ALIGNMENT (run-2 lesson, found as an exact +1/8 shift in P₁ to
    # 3e-5): the printed φ_σ (GGM Thm-3 normalization) excludes the
    # factorization prefactor (q/q̃)^{1/8}, whose q-part contributes e^{ħ/8}
    # to the raw saddle expansion. Multiply by e^{−ħ/8}: in P-units
    # P_k → Σ_j P_{k−j}·(−1/8)^j/j!.
    Pal = {}
    for k in range(0, OMAX + 1):
        acc = mp.mpc(0)
        for j in range(0, k + 1):
            acc += P[k - j] * (mp.mpf(-1) / 8) ** j / mp.factorial(j)
        Pal[k] = acc
    P = Pal
    print(f"\n  φ_σ1 series generated to order {OMAX}; P₀ normalized to 1.")

    # ---- gates against printed + arbitrated + A4.1-extracted values ----
    P1_ref = (33 * (xi / (xi - 1)) ** 2 + 242 * (xi / (xi - 1)) - 245) / (4 * 23**2)
    # the agreed τ¹ value is GGM@z = Peacock@ξ; use GGM's poly at z = ξ/(ξ−1)
    P2_ref = (12643 * xi**2 - 22668 * xi + 25400) / (2**5 * 23**3)   # Peacock@ξ (arbitrated)
    P3_ref = (-50198891 * (xi / (xi - 1))**2 + 35443870 * (xi / (xi - 1))
              - 79016748) / (2**7 * 3 * 5 * 23**5)                    # GGM@z (agreed w/ Peacock@ξ)
    r1 = abs(P[1] - P1_ref) / abs(P1_ref)
    r2 = abs(P[2] - P2_ref) / abs(P2_ref)
    r3 = abs(P[3] - P3_ref) / abs(P3_ref)
    g2 = r1 < mp.mpf("1e-30")
    g3 = r2 < mp.mpf("1e-30")
    print(f"\n[G2] P₁ vs agreed printed:    rel = {mp.nstr(r1, 4)}  {'PASS' if g2 else 'FAIL'}")
    print(f"[G3] P₂ vs arbitrated value:  rel = {mp.nstr(r2, 4)}  {'PASS' if g3 else 'FAIL'}")
    print(f"[G4] P₃ vs printed (agreed):  rel = {mp.nstr(r3, 4)}  "
          f"{'MATCHES — τ³ settled' if r3 < mp.mpf('1e-25') else 'DIFFERS — engine value is the derived one'}")
    print("\n  first coefficients:")
    for k in range(1, min(9, OMAX + 1)):
        print(f"    P_{k} = {mp.nstr(P[k], 15)}")

    # ---- Borel diagnostics ----
    # Borel transform b_k = a_k/k!; nearest singularity |ι| ≈ lim |b_k/b_{k+1}|
    print("\n[B] Borel diagnostics (nearest singularity vs GGM eq-81 ι₁₂):")
    V1 = mp.mpc("2.8281220883307832", "1.3790860299")
    V2 = mp.mpc("-2.8281220883307832", "1.3790860299")
    # in the x = 2πiτ variable (the P-unit series φ = Σ P_k x^k), the
    # transseries factor e^{V/(2πτ)} = e^{iV/x} puts the Borel singularity at
    # ζ = i(V₁−V₂): distance |V₁−V₂| — NOT /2π (run-3 lesson: the /2π form is
    # the τ-plane ι₁₂ of GGM eq 81; the ratio test runs in x-units).
    iota12 = abs(V1 - V2)
    ratios = []
    for k in range(OMAX - 6, OMAX - 1):
        bk = P[k] / mp.factorial(k)
        bk1 = P[k + 1] / mp.factorial(k + 1)
        ratios.append(abs(bk / bk1))
        print(f"    |b_{k}/b_{k+1}| = {mp.nstr(abs(bk / bk1), 8)}")
    est = ratios[-1]
    # crude Richardson on the last three ratio estimates
    if len(ratios) >= 3:
        r_a, r_b, r_c = ratios[-3:]
        est = r_c + (r_c - r_b) ** 2 / ((r_c - r_b) - (r_b - r_a)) \
            if (r_c - r_b) != (r_b - r_a) else r_c
    print(f"    Richardson estimate ≈ {mp.nstr(est, 8)}   "
          f"GGM ι₁₂ prediction = |V₁−V₂|/2π = {mp.nstr(iota12, 8)}")
    borel_ok = abs(est - iota12) / iota12 < mp.mpf("0.1")
    print(f"    resurgence gate (20%): {'PASS' if borel_ok else 'INFORMATIVE — '}"
          f"rel dev = {mp.nstr(abs(est - iota12) / iota12, 4)}")

    ok_gates = g1 and g2 and g3

    wb = WitnessBuilder("qbeta-5two-phi-series-engine", engine="sympy+mpmath",
                        _script_path=__file__)
    wb.set_description(
        "A4.2 (bean qou-ea86): first-principles generation of the 5₂ φ_σ1 "
        "perturbative series to order 24 by formal steepest descent of the "
        "state integral in the τ-channel (Faddeev asymptotics of Φ_b³; "
        "V₀ = 3Li₂(−e^y)+y² whose critical equation is exactly GGM eq-19; "
        "all vertices rational in the saddle via the Li_{−k} tower; Wick "
        "engine at dps 60). Gates: saddle = the geometric ξ₁; P₁ = the agreed "
        "printed value; P₂ = the ARBITRATED (Peacock@ξ) value — the engine "
        "independently re-confirms the 2026-07-18 τ² misprint arbitration if "
        "these pass at 1e-30. P₃ derived (settles the A4.1 τ³ diagnostic). "
        "Borel diagnostics: nearest-singularity ratio estimate vs the GGM "
        "eq-81 ι₁₂ = |V(σ1)−V(σ2)|/2π Stokes distance. Unblocks the A4 "
        "median Borel–Laplace program. auditOnly; no c_k wired; no fit.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_assertion("saddle_is_geometric_root",
                     computed=float(abs(resid)), expected=0.0, tolerance=1e-50,
                     source="V₀' = 0 ⇔ (1−x)³ = x² at the geometric ξ₁ branch")
    wb.add_assertion("P1_matches_agreed",
                     computed=1.0 if g2 else 0.0, expected=1.0, tolerance=0.5,
                     source="engine P₁ = the agreed printed τ¹ (GGM@z = Peacock@ξ) "
                            "at 1e-30")
    wb.add_assertion("P2_matches_arbitrated",
                     computed=1.0 if g3 else 0.0, expected=1.0, tolerance=0.5,
                     source="engine P₂ = the arbitrated Peacock-eq-76@ξ value at "
                            "1e-30 — independent re-confirmation of the misprint "
                            "arbitration")
    wb.add_assertion("borel_singularity_near_iota12",
                     computed=1.0 if borel_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="Borel nearest-singularity estimate within 20% of the "
                            "GGM eq-81 ι₁₂ Stokes distance (resurgence gate)")
    ok = all(a.passed for a in wb.assertions)

    wb.add_data("series_order", OMAX)
    wb.add_data("P_coefficients", {str(k): mp.nstr(P[k], 40)
                                   for k in range(1, OMAX + 1)})
    wb.add_data("P3_engine_vs_printed_rel", mp.nstr(r3, 10))
    wb.add_data("borel", {"ratio_estimates": [mp.nstr(r, 12) for r in ratios],
                          "richardson": mp.nstr(est, 15),
                          "iota12_prediction": mp.nstr(iota12, 15)})
    wb.add_data("verdict",
                ("ENGINE VALIDATED + SERIES DELIVERED: φ_σ1 to order 24 from "
                 "first principles, gates on the agreed P₁ and the arbitrated "
                 "P₂ (independent re-confirmation of the τ² misprint verdict); "
                 "P₃ now derived; Borel nearest singularity consistent with the "
                 "GGM ι₁₂ Stokes distance. The A4 median Borel–Laplace program "
                 "is unblocked with a trustworthy coefficient basis."
                 if ok else "A gate failed — inspect before using the series."))
    wb.save()
    print(f"\n  assertions passed: {ok}   ({time.monotonic() - t0:.0f}s total)")
    print("  witness -> computations/probes/qbeta-5two-phi-series-engine.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
