#!/usr/bin/env python3
"""tau_dictionary_fricke_spin_probe.py — cusp factorization of the nome dictionary,
bar ↔ Fricke candidate class, and the A6 spin/sign leg (W8b + A6).

Follow-up to computations/probes/tau_dictionary_hauptmodul_validator.py (W8),
which found the corpus's only concrete q₀ ↦ τ dictionary — the exact nome map
τ = i·|ln q₀|/(2π) — FAILs the Bring gate t₅(τ₀) = −10 with a cusp-adjacent
image t₅ ≈ 1.7e−31. The owner asked (i) "is there a zero we can factor out?"
and (ii) "is there geometric intuition to exploit?". This probe answers both
at theorem level, scope-(a), audit-only, NO FIT, nothing wired.

TASK 1 — CUSP FACTORIZATION (exact). The observed 1.7e−31 is the cusp-0 zero
of t₅, factored exactly through the Fricke involution W₅: τ ↦ −1/(5τ). From
η(−1/τ) = √(−iτ)·η(τ) one gets the EXACT identity

    t₅(τ) = t₅(−1/(5τ')) = 5³·(η(5τ')/η(τ'))⁶      at τ' = W₅(τ),

so on the imaginary axis τ = iy (τ' = i/(5y), q̃ = e^{2πiτ'} = e^{−2π/(5y)}):

    t₅(iy) = 125·q̃·∏_{n≥1} (1−q̃^{5n})⁶/(1−q̃ⁿ)⁶
           = 125·q̃·(1 + 6q̃ + 27q̃² + 98q̃³ + 315q̃⁴ + 912q̃⁵ + 2456q̃⁶ + …),

with INTEGER coefficients c_k (the 6-coloured-partition series corrected at
levels 5ℕ; computed here by exact integer series arithmetic). At the nome
dictionary y = |ln q₀|/(2π) this gives q̃ = exp(−4π²/(5·ln q₀)) ≈ 1.37e−33 and
t₅ = 125·q̃·(1 + O(q̃)) ≈ 1.7097e−31 — verified to ≥ 60 significant digits at
BOTH q₀ pins. The nome dictionary is exponentially cusp-suppressed as a
THEOREM-LEVEL statement, not a numeric accident: the nome map is a chart at
the cusp 0 of X₀(5), while the Bring class t₅ = −10 is interior.

TASK 2 — BAR ↔ FRICKE CANDIDATE CLASS (falsifier-first; structure-enumerated,
zero free parameters, NO TUNING). The corpus bar involution q ↦ q⁻¹ sends
ln q₀ ↦ −ln q₀; the Fricke involution is W₅: τ ↦ −1/(5τ). Natural candidates:

  N1   τ = i/√5 — the W₅ fixed point (the bar⊗Fricke symmetrization of the
       imaginary-axis nome family: y ⊗ 1/(5y) → geometric mean 1/√5).
       EXACT: t₅(i/√5) = +5√5 (Fricke fixed ⇒ t₅² = 125, positive branch).
  N2   τ(q₀) = e^{i(π/2 − ln q₀)}/√5 on the W₅-fixed circle |τ| = 1/√5, nome
       rate as phase. EXACTLY intertwines bar with Fricke:
       τ(q₀⁻¹) = W₅(τ(q₀)). Interior image (not cusp-adjacent). BUT the whole
       circle is excluded by a PROVED invariant: on |τ| = 1/√5, W₅ acts as
       τ ↦ −τ̄, and t₅(−τ̄) = conj t₅(τ) (real q-coefficients), so
       t₅·t̄₅ = 125 ⇒ |t₅| ≡ 5√5 ≈ 11.18 ≠ 10 = |−10|. Structural
       exclusion with cited invariant (AGENTS.md §refuted (b)): no
       parametrization of the W₅-fixed circle can pass the gate.
  N2b  the bar partner e^{i(π/2 + ln q₀)}/√5 (= W₅ ∘ N2; conjugate t₅).
  N3   τ = i·sinh(ln q₀) (bar-ODD part of the nome data).
  N4   τ = i·cosh(ln q₀) (bar-EVEN part; = i·[2]_{q₀}/2).
  Nh   half-period-shifted variants Re τ = −1/2 of N1, N2, N3, N4, and of the
       committed nome dictionary C1 (N5h: τ = −1/2 + i·ln q₀/(2π), whose
       modular nome is EXACTLY q̂ = −1/q₀ — the bar image with the sign twist).

TASK 3 — A6 SIGN LEG (BN12 sigma12-065.pdf; BDH22 2208.13692v1.pdf). Exact
re-verification, from the PRINTED data, of the discrete spin datum:

  • BN12 §5.3: the order-5 symplectic action M on H₁(Bring, ℤ) (printed 8×8
    integer matrix): M⁵ = Id, M ∈ Sp(8,ℤ), and Smith normal form
    M − Id = U·Diag(1,1,1,1,1,1,5,5)·V — all re-derived here exactly.
  • BN12 Thm 3 = BDH22 Prop 5.13 (verbatim agreement across the two papers):
    K_Q = (1/10)(3,2,−2,−3) + Im(τ₀)·(1,−2,−2,1)·i in the RR92 basis,
    τ_B = τ₀·M_RR, M_RR = [[4,1,−1,1],[1,4,1,−1],[−1,1,4,1],[1,−1,1,4]]
    (det 125, spectrum {5,5,5,1}; 5·M_RR⁻¹ integral — BDH22 Prop 4.4 shape).
  • 2N-torsion (BN12 Lemma 1, N = 5 ⇒ 10-torsion) verified exactly AND
    SHARPENED: (1,−2,−2,1) is a 5-eigenvector of M_RR, so
    5·K_Q = (4,−4,−6,1) + τ_B·(1,−2,−2,1) ∈ ℤ⁴ + τ_B ℤ⁴ symbolically in
    Im(τ₀) — K_Q is EXACTLY 5-torsion (k·K_Q ∉ Λ for k = 1..4).
  • BN12's intermediate 2K_Q = (1/5)(−12,−3,3,−3) + τ₀·(−6,−6,3,0) (p.19) is
    lattice-equivalent to 2×Thm 3 with explicit integer vectors
    n = (−4,1,3,−1), m = (−1,−1,2,−1) — internal consistency check.
  • The unique S₅(=Aut)-invariant theta characteristic is ∆ = 3a + b − c
    (BDH22 Ex 5.3 + Thm 5.11), it is EVEN (not odd — correcting the briefing's
    "odd characteristic" framing), equals the Szegő divisor ∆_S with
    K_a = A_a(∆_S) (Prop 5.13, verified there to 1e−118), i.e. the invariant
    spin structure is the ORIGIN of the θ-frame based at a. Orbit counts:
    odd 120 = 20+20+20+60 (Cor 5.7), even 136 = 1+5+5+5+10+10+10+30+30+30
    (Thm 5.9) — the "1" is the unique S₅ fixed point (Thm 4 forcing).

SIGN INVARIANT (the formalize-first necessary condition). For real modular
nome q̂ = e^{2πiτ} ∈ (−1,0)∪(0,1):

    t₅(τ) = q̂⁻¹·∏_{n≥1} (1−q̂ⁿ)⁶/(1−q̂^{5n})⁶,   every factor > 0,

hence sign t₅ = sign q̂. So t₅ = −10 < 0 REQUIRES the odd-nome chart
q̂ < 0, i.e. Re τ ≡ 1/2 (mod 1) — a half-period twist of the θ/nome frame
(the discrete datum the A6 characteristic normalizes; identifying the
worldline-spin twist with the Bring spin structure remains a framework
hypothesis, NOT established here). Consequences, verified below:
every purely-imaginary (bar-symmetric-|·|) dictionary has t₅ > 0 and is
excluded by the proved sign invariant; every half-shifted variant acquires
t₅ < 0 (sign necessary condition met) but none lands on −10 — in particular
the spin-twisted nome dictionary N5h moves from +1.7e−31 to −7.6e−7:
sign fixed, still cusp-suppressed, still FAIL.

HONEST OUTCOME: 11/11 evaluable candidates FAIL (or are exactly excluded);
no PASS was found; nothing is proposed. Closest miss (recorded, not
interpreted): N3h = −1/2 + i·sinh(ln q₀) with t₅ ≈ −4.697 (|t₅+10| ≈ 5.30).

Audit doc: docs/audits/2026-07-24-tau-dictionary-fricke-cusp-spin.md
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sympy as sp  # noqa: E402
from mpmath import mp, mpc, mpf, exp, log, pi, sqrt, cosh, sinh  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Reuse the committed validator's machinery (η-product, t₅, gate + ladder).
from tau_dictionary_hauptmodul_validator import (  # noqa: E402
    Q0_MUON, Q0_PROTON, T5_TARGET, gate, t5,
)

# ── Task 1 exact expansion coefficients (integer series arithmetic) ────────
CUSP_COEFFS_EXPECTED = [1, 6, 27, 98, 315, 912, 2456, 6210, 14937]


def cusp_series_coeffs(n_coeffs: int) -> list[int]:
    """Exact integer coefficients c_k of
    ∏_{n≥1}(1−q^{5n})⁶ / ∏_{n≥1}(1−qⁿ)⁶  =  Σ_k c_k q^k  (mod q^n_coeffs),
    via exact integer polynomial arithmetic (no floats anywhere)."""
    N = n_coeffs

    def mul(a, b):
        r = [0] * N
        for i, ai in enumerate(a):
            if ai:
                for j in range(min(N - i, len(b))):
                    if b[j]:
                        r[i + j] += ai * b[j]
        return r

    den = [1] + [0] * (N - 1)
    for n in range(1, N):
        f = [0] * N
        f[0] = 1
        f[n] = -1
        for _ in range(6):
            den = mul(den, f)
    num = [1] + [0] * (N - 1)
    for n in range(1, (N - 1) // 5 + 1):
        f = [0] * N
        f[0] = 1
        f[5 * n] = -1
        for _ in range(6):
            num = mul(num, f)
    inv = [0] * N
    inv[0] = 1  # den[0] == 1
    for k in range(1, N):
        inv[k] = -sum(den[j] * inv[k - j] for j in range(1, k + 1))
    return mul(num, inv)


def t5_cusp_form(y, n_terms: int):
    """125·q̃·Σ_{k<n_terms} c_k q̃^k at τ = iy, q̃ = e^{−2π/(5y)} — the exact
    Fricke-chart (cusp-0) evaluation of t₅(iy)."""
    qt = exp(-2 * pi / (5 * y))
    coeffs = cusp_series_coeffs(n_terms)
    acc = mpf(0)
    for k in range(n_terms - 1, -1, -1):
        acc = acc * qt + coeffs[k]
    return 125 * qt * acc, qt


def main():
    set_compute_dps()
    wb = WitnessBuilder("tau-dictionary-fricke-spin-probe", engine="mpmath+sympy")
    q0_mu = mpf(Q0_MUON)
    q0_p = mpf(Q0_PROTON)

    # ══════════════════════════════════════════════════════════════════════
    # TASK 1 — cusp-factorization identity
    # ══════════════════════════════════════════════════════════════════════
    print("TASK 1 — cusp factorization t5(iy) = 125·q̃·(1 + Σ c_k q̃^k)")

    # (1a) exact integer coefficients
    coeffs = cusp_series_coeffs(9)
    assert coeffs == CUSP_COEFFS_EXPECTED, f"cusp coefficients drifted: {coeffs}"
    print(f"  c_0..c_8 (exact integers) = {coeffs}")

    # (1b) the exact Fricke bridge t5(τ)·t5(−1/(5τ)) = 125 at a generic
    # imaginary point (this is the η-functional-equation content that turns
    # the η-product definition into the cusp chart).
    tau_gen = mpc(0, mpf("0.37"))
    fricke_prod_dev = abs(t5(tau_gen) * t5(-1 / (5 * tau_gen)) - 125)
    assert fricke_prod_dev < mpf("1e-40"), f"Fricke product dev {fricke_prod_dev}"
    print(f"  |t5(iy)·t5(W5(iy)) − 125| at y=0.37: {mp.nstr(fricke_prod_dev, 4)}")

    # (1c) numeric cross-check of the cusp-chart series at moderate q̃.
    # Peel c_0..c_5 individually (each resolved to within its known tail
    # 2·(c_{k+1}+1)·q̃), then assert the c_6..c_8 block jointly with the
    # exact next-coefficient bound (c_9 = 34390 from the same integer
    # arithmetic). The coefficients themselves are EXACT by the integer
    # series construction; this leg certifies the analytic identity.
    mp.dps = 60
    c9 = cusp_series_coeffs(10)[9]
    for y_str in ("0.5", "0.3"):
        y_mod = mpf(y_str)
        qt_mod = exp(-2 * pi / (5 * y_mod))
        resid = t5(mpc(0, y_mod)) / (125 * qt_mod)
        for k in range(0, 6):
            dev_k = abs(resid - coeffs[k])
            assert dev_k < 2 * (coeffs[k + 1] + 1) * qt_mod, (
                f"y={y_str}: coefficient c_{k} numeric mismatch: {mp.nstr(resid, 12)}")
            resid = (resid - coeffs[k]) / qt_mod
        block = coeffs[6] + coeffs[7] * qt_mod + coeffs[8] * qt_mod ** 2
        block_dev = abs(resid - block)
        assert block_dev < 2 * c9 * qt_mod ** 3, (
            f"y={y_str}: c_6..c_8 block dev {mp.nstr(block_dev, 6)}")
        print(f"  numeric peel at y={y_str} (q̃ = {mp.nstr(qt_mod, 6)}): c_0..c_5 resolved; "
              f"c_6..c_8 block dev = {mp.nstr(block_dev, 4)} < 2·c_9·q̃³")

    # (1d) both q₀ pins at high precision: direct η-product vs cusp form.
    mp.dps = 120
    pin_results = {}
    for pin, q0 in (("muon", q0_mu), ("proton", q0_p)):
        y = log(q0) / (2 * pi)
        t5_direct = t5(mpc(0, y))
        t5_cusp, qt = t5_cusp_form(y, 9)
        rel = abs(t5_direct - t5_cusp) / abs(t5_direct)
        lead_rel = abs(t5_direct - 125 * qt) / abs(t5_direct)
        assert abs(mp.im(t5_direct)) < mpf("1e-80"), "t5(iy) must be real"
        assert rel < mpf("1e-60"), f"{pin}: cusp form disagrees, rel {rel}"
        # leading-order: relative defect is 6q̃ + O(q̃²)
        assert abs(lead_rel - 6 * qt) < 100 * qt ** 2, "leading defect is not 6q̃"
        pin_results[pin] = {
            "y_nome": mp.nstr(y, 40),
            "q_tilde = exp(-4pi^2/(5 ln q0))": mp.nstr(qt, 40),
            "t5_direct_eta_product": mp.nstr(mp.re(t5_direct), 40),
            "t5_cusp_form_125_qt_series": mp.nstr(mp.re(t5_cusp), 40),
            "rel_agreement": mp.nstr(rel, 6),
        }
        print(f"  [{pin:6s}] q̃ = {mp.nstr(qt, 25)}")
        print(f"           t5(iy) = {mp.nstr(mp.re(t5_direct), 35)}   (rel dev vs cusp form: {mp.nstr(rel, 4)})")
    mp.dps = 50

    # ══════════════════════════════════════════════════════════════════════
    # TASK 2 — bar ↔ Fricke candidate class (structure-enumerated, no tuning)
    # ══════════════════════════════════════════════════════════════════════
    print("\nTASK 2 — bar ↔ Fricke candidates (falsifier-first)")

    # (2a) exact value at the Fricke fixed point: t5(i/√5) = 5√5.
    t5_fix = t5(mpc(0, 1 / sqrt(5)))
    fix_dev = abs(t5_fix - 5 * sqrt(5))
    assert fix_dev < mpf("1e-40"), f"t5(i/sqrt5) != 5*sqrt5: dev {fix_dev}"
    print(f"  t5(i/√5) = 5√5 exactly: dev = {mp.nstr(fix_dev, 4)}")

    # (2b) N2 intertwines bar with Fricke EXACTLY: τ(q0⁻¹) = W5(τ(q0)).
    def n2_map(q0):
        return exp(mpc(0, 1) * (pi / 2 - log(q0))) / sqrt(5)

    for q0 in (q0_mu, q0_p):
        equiv_dev = abs(n2_map(1 / q0) - (-1 / (5 * n2_map(q0))))
        assert equiv_dev < mpf("1e-45"), f"N2 equivariance broken: {equiv_dev}"
    print("  N2 bar↔Fricke equivariance τ(q0⁻¹) = W5(τ(q0)): exact (dev < 1e-45)")

    # (2c) the W5-fixed-circle invariant |t5| = 5√5 (proved: W5 acts as
    # τ ↦ −τ̄ on |τ| = 1/√5; t5(−τ̄) = conj t5(τ); so t5·t̄5 = 125).
    circle_devs = []
    for q0 in (q0_mu, q0_p):
        v_t5 = t5(n2_map(q0))
        circle_devs.append(abs(abs(v_t5) ** 2 - 125))
        # reflection identity: t5 at the bar partner is the conjugate
        refl_dev = abs(t5(n2_map(1 / q0)) - mp.conj(v_t5))
        assert refl_dev < mpf("1e-40"), f"reflection identity broken: {refl_dev}"
    circle_dev = max(circle_devs)
    assert circle_dev < mpf("1e-40"), f"|t5|^2 != 125 on the circle: {circle_dev}"
    print(f"  W5-fixed circle: |t5|² = 125 (dev {mp.nstr(mpf(circle_dev), 4)}) ⇒ |t5| = 5√5 ≠ 10 — family excluded")

    # (2d) candidate table (zero free parameters; enumerated from bar/Fricke/
    # half-period structure ONLY; the -1/2 shifts are the sign-twist leg).
    half = mpf("-0.5")

    def L(q0):
        return log(q0)

    candidates = {
        "N1-fricke-fixed": ("tau = i/sqrt5 (W5 fixed point; q0-independent)",
                            lambda q0: mpc(0, 1 / sqrt(5))),
        "N1h-fricke-fixed-twist": ("tau = -1/2 + i/sqrt5",
                                   lambda q0: mpc(half, 1 / sqrt(5))),
        "N2-fricke-circle": ("tau = e^{i(pi/2 - ln q0)}/sqrt5 (bar↔Fricke equivariant)",
                             n2_map),
        "N2b-fricke-circle-bar": ("tau = e^{i(pi/2 + ln q0)}/sqrt5 (bar partner)",
                                  lambda q0: n2_map(1 / q0)),
        "N2h-fricke-circle-twist": ("tau = -1/2 + e^{i(pi/2 - ln q0)}/sqrt5",
                                    lambda q0: half + n2_map(q0)),
        "N3-bar-odd": ("tau = i sinh(ln q0) (bar-odd split)",
                       lambda q0: mpc(0, sinh(L(q0)))),
        "N3h-bar-odd-twist": ("tau = -1/2 + i sinh(ln q0)",
                              lambda q0: mpc(half, sinh(L(q0)))),
        "N4-bar-even": ("tau = i cosh(ln q0) (bar-even split, [2]_q/2)",
                        lambda q0: mpc(0, cosh(L(q0)))),
        "N4h-bar-even-twist": ("tau = -1/2 + i cosh(ln q0)",
                               lambda q0: mpc(half, cosh(L(q0)))),
        "N5h-nome-twist": ("tau = -1/2 + i ln(q0)/(2pi) (spin-twisted C1; nome = -1/q0)",
                           lambda q0: mpc(half, L(q0) / (2 * pi))),
    }

    results = {}
    for key, (formula, fmap) in candidates.items():
        res = {"muon-pin": gate(fmap(q0_mu)), "proton-pin": gate(fmap(q0_p))}
        verdicts = {r["verdict"] for r in res.values()}
        assert len(verdicts) == 1, f"{key}: verdict flips across pins: {verdicts}"
        results[key] = {"formula": formula, "results": res}
        r = res["muon-pin"]
        print(f"  {key:26s} {r['verdict']:6s} t5 = {r['t5']:38s} |t5+10| = {r['abs_residual_t5_plus_10']}")

    # observed verdicts, pinned (recorded from computation — regression lock)
    expected_verdicts = {k: "FAIL" for k in candidates}
    for key, exp_v in expected_verdicts.items():
        got = {r["verdict"] for r in results[key]["results"].values()}
        assert got == {exp_v}, f"{key}: expected {exp_v}, got {got}"

    # (2e) SIGN INVARIANT checks. Purely-imaginary candidates: t5 real > 0.
    # Half-shifted candidates: t5 real < 0. (Real nome ⇒ sign t5 = sign q̂.)
    for key, (formula, fmap) in candidates.items():
        if key.startswith("N2"):
            continue  # circle-family points have non-real nome; handled by the |t5| invariant above
        v_t5 = t5(fmap(q0_mu))
        assert abs(mp.im(v_t5)) < mpf("1e-40"), f"{key}: t5 should be real"
        if key.endswith("twist") or key == "N5h-nome-twist":
            assert mp.re(v_t5) < 0, f"{key}: half-period twist must give t5 < 0"
        else:
            assert mp.re(v_t5) > 0, f"{key}: purely-imaginary tau must give t5 > 0"
    print("  sign invariant: pure-imaginary ⇒ t5 > 0; Re τ = −1/2 ⇒ t5 < 0  ✓")

    # spot-check the sign lemma on a real-nome grid (both signs of q̂)
    for qhat_s in ("-0.9", "-0.5", "-0.1", "0.1", "0.5", "0.9"):
        qhat = mpf(qhat_s)
        tau = mpc(half if qhat < 0 else 0, -log(abs(qhat)) / (2 * pi))
        v_t5 = t5(tau)
        assert abs(mp.im(v_t5)) < mpf("1e-40")
        assert (mp.re(v_t5) > 0) == (qhat > 0), f"sign lemma fails at qhat={qhat_s}"
    print("  sign lemma grid (q̂ = ±0.1, ±0.5, ±0.9): sign t5 = sign q̂  ✓")

    # (2f) the spin-twisted nome dictionary N5h has modular nome exactly −1/q₀
    for q0 in (q0_mu, q0_p):
        tau5h = mpc(half, log(q0) / (2 * pi))
        nome_dev = abs(exp(2j * pi * tau5h) + 1 / q0)
        assert nome_dev < mpf("1e-45"), f"N5h nome identity broken: {nome_dev}"
    n5h_t5 = mpf(mp.re(t5(mpc(half, log(q0_mu) / (2 * pi)))))
    print(f"  N5h nome = −1/q0 exactly; t5 = {mp.nstr(n5h_t5, 8)} (sign fixed, magnitude still cusp-suppressed)")

    # ══════════════════════════════════════════════════════════════════════
    # TASK 3 — A6 sign leg: exact checks on the printed BN12/BDH22 data
    # ══════════════════════════════════════════════════════════════════════
    print("\nTASK 3 — BN12/BDH22 spin data (exact sympy on printed integers)")

    # (3a) the printed order-5 symplectic action on H1(Bring, Z) (BN12 §5.3)
    M = sp.Matrix([
        [0, 0, 0, 1, 0, 0, 0, 0],
        [-1, 0, 0, -1, 0, 0, 0, 0],
        [0, -1, 0, 1, 0, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 1, -1, 1],
        [0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0],
    ])
    assert M ** 5 == sp.eye(8), "printed M is not order 5"
    J = sp.zeros(8, 8)
    for i in range(4):
        J[i, i + 4] = 1
        J[i + 4, i] = -1
    assert M * J * M.T == J and M.T * J * M == J, "printed M is not symplectic"
    from sympy.matrices.normalforms import smith_normal_form
    snf = smith_normal_form(M - sp.eye(8), domain=sp.ZZ)
    snf_diag = [snf[i, i] for i in range(8)]
    assert snf_diag == [1, 1, 1, 1, 1, 1, 5, 5], f"SNF drifted: {snf_diag}"
    print(f"  M⁵ = Id, M ∈ Sp(8,ℤ), SNF(M − Id) = Diag{tuple(snf_diag)}  ✓ (BN12 §5.3)")

    # (3b) RR92 Gram (BN12 (1.1) / BDH22): det 125, spectrum {5,5,5,1},
    # 5·M_RR⁻¹ integral, and v = (1,−2,−2,1) a 5-eigenvector.
    MRR = sp.Matrix([[4, 1, -1, 1], [1, 4, 1, -1], [-1, 1, 4, 1], [1, -1, 1, 4]])
    assert MRR.det() == 125
    assert MRR.eigenvals() == {sp.Integer(5): 3, sp.Integer(1): 1}
    Mprime = 5 * MRR.inv()
    assert all(x.is_Integer for x in Mprime), "5·M_RR⁻¹ not integral"
    v = sp.Matrix([1, -2, -2, 1])
    assert MRR * v == 5 * v, "(1,−2,−2,1) is not a 5-eigenvector of M_RR"
    print("  M_RR: det 125, spec {5,5,5,1}, 5·M_RR⁻¹ ∈ M₄(ℤ), M_RR·(1,−2,−2,1) = 5·(1,−2,−2,1)  ✓")

    # (3c) K_Q = (1/10)(3,2,−2,−3) + Im(τ0)(1,−2,−2,1)i (BN12 Thm 3 = BDH22
    # Prop 5.13) is EXACTLY 5-torsion in Jac = C⁴/(ℤ⁴ + τ_B ℤ⁴), τ_B = τ0·M_RR,
    # symbolically in y0 = Im(τ0) — sharper than BN12 Lemma 1's 2N = 10 bound.
    y0 = sp.symbols("y0", positive=True)
    tau0_sym = sp.Rational(-1, 2) + sp.I * y0
    K = sp.Rational(1, 10) * sp.Matrix([3, 2, -2, -3]) + sp.I * y0 * v
    n_vec = sp.expand(5 * K - tau0_sym * (MRR * v))
    assert list(n_vec) == [4, -4, -6, 1], f"5K_Q lattice part drifted: {list(n_vec)}"
    for k in range(1, 5):
        mk = k * MRR.inv() * v  # unique solution of M_RR m = k·v
        assert not all(sp.Rational(x).q == 1 for x in mk), f"K_Q order divides {k}?"
    print("  5·K_Q = (4,−4,−6,1) + τ_B·(1,−2,−2,1) exactly (symbolic in Im τ0) ⇒ K_Q is EXACTLY 5-torsion  ✓")

    # (3d) BN12's intermediate 2K_Q (p.19) ≡ 2×Thm 3 mod the lattice, with
    # explicit integer vectors — internal consistency of the printed data.
    twoK_int = sp.Rational(1, 5) * sp.Matrix([-12, -3, 3, -3]) + tau0_sym * sp.Matrix([-6, -6, 3, 0])
    diff = sp.expand(twoK_int - 2 * K)
    m_c = MRR.solve(sp.Matrix([-8, -2, 7, -2]))
    assert all(sp.Rational(x).q == 1 for x in m_c), "consistency m not integral"
    n_c = sp.expand(diff - tau0_sym * (MRR * m_c))
    assert all(x.is_Integer for x in n_c), f"consistency n not integral: {list(n_c)}"
    assert list(m_c) == [-1, -1, 2, -1] and list(n_c) == [-4, 1, 3, -1]
    print("  intermediate 2K_Q ≡ 2·K_Q(Thm 3) mod Λ with n = (−4,1,3,−1), m = (−1,−1,2,−1)  ✓")

    # (3e) the two published τ0 prints: BDH22's corrected value passes the
    # gate; BN12's own 6-d.p. print (0.185576) does NOT (recorded — the
    # BDH22 correction is load-bearing for any Im(τ0)-dependent datum).
    t5_bn12 = t5(mpc(mpf("-0.5"), mpf("0.185576")))
    t5_bdh22 = t5(mpc(mpf("-0.5"), mpf("0.186676")))
    bn12_resid = abs(t5_bn12 - T5_TARGET)
    bdh22_resid = abs(t5_bdh22 - T5_TARGET)
    assert bdh22_resid < mpf("1e-3") < bn12_resid, "tau0-print discrimination failed"
    print(f"  τ0 prints: BDH22 |t5+10| = {mp.nstr(mpf(bdh22_resid), 3)} (PASS); "
          f"BN12 print |t5+10| = {mp.nstr(mpf(bn12_resid), 3)} (off-gate; BDH22 correction load-bearing)")

    # ── witness ────────────────────────────────────────────────────────────
    wb.set_description(
        "W8b+A6 follow-up to the tau-dictionary hauptmodul validator. "
        "TASK 1: the nome dictionary's t5 ~ 1.7e-31 is factored EXACTLY "
        "through the Fricke chart: t5(iy) = 125*qt*(1 + 6qt + 27qt^2 + "
        "98qt^3 + ...), qt = exp(-2pi/(5y)) = exp(-4pi^2/(5 ln q0)) at the "
        "nome dictionary — integer coefficients from exact series "
        "arithmetic, verified to >= 60 digits at both q0 pins: the map is a "
        "cusp-0 chart, exponentially cusp-suppressed (theorem-level, not a "
        "numeric accident). TASK 2: natural bar<->Fricke candidates "
        "(falsifier-first, zero free parameters): the W5-fixed point has "
        "t5 = +5*sqrt(5) exactly; the bar<->Fricke-equivariant circle "
        "family tau(q0) = e^{i(pi/2 - ln q0)}/sqrt5 satisfies "
        "tau(1/q0) = W5(tau(q0)) exactly but the PROVED invariant "
        "|t5| = 5*sqrt(5) != 10 on the whole W5-fixed circle excludes the "
        "family; sign invariant: real nome => sign t5 = sign(nome), so "
        "t5 = -10 requires the odd-nome half-period chart Re tau = 1/2 mod "
        "1 — every purely-imaginary dictionary is excluded, every "
        "half-shifted variant acquires t5 < 0 but none lands on -10 "
        "(spin-twisted nome: t5 = -7.6e-7). 10/10 gated candidates FAIL, "
        "verdicts pin-stable; no proposal. TASK 3: BN12/BDH22 printed spin "
        "data re-verified exactly (M order 5 symplectic, SNF diag "
        "(1,...,1,5,5), K_Q 2N-torsion SHARPENED to exactly 5-torsion via "
        "the 5-eigenvector (1,-2,-2,1); unique invariant characteristic "
        "Delta = 3a+b-c is EVEN (= Szego divisor, the theta-frame origin); "
        "the briefing's 'odd characteristic' framing corrected). Audit-only; "
        "NO FIT; nothing wired."
    )
    wb.set_audit_only("docs/audits/2026-07-24-tau-dictionary-fricke-cusp-spin.md")
    wb.add_data("task1_cusp_factorization", {
        "identity": "t5(iy) = 125*qt*prod((1-qt^{5n})/(1-qt^n))^6, qt = exp(-2pi/(5y)) "
                    "(exact, via eta(-1/tau) = sqrt(-i tau) eta(tau))",
        "coefficients_c0_c8": CUSP_COEFFS_EXPECTED,
        "per_pin": pin_results,
    })
    wb.add_data("task2_candidates", results)
    wb.add_data("task2_exact_structure", {
        "fricke_fixed_point_value": "t5(i/sqrt5) = 5*sqrt5 = 11.180339887... (exact; "
                                    "Fricke-fixed => t5^2 = 125, positive branch)",
        "w5_circle_invariant": "|t5|^2 = 125 on |tau| = 1/sqrt5 (W5 acts as tau -> "
                               "-conj(tau) there; t5 has real q-coefficients) => "
                               "|t5| = 5*sqrt5 != 10: the whole circle family is "
                               "excluded by a proved invariant",
        "bar_fricke_equivariance": "tau(q0^{-1}) = W5(tau(q0)) exact for the circle "
                                   "family tau(q0) = e^{i(pi/2 - ln q0)}/sqrt5",
        "sign_invariant": "real nome qhat: t5 = qhat^{-1} prod((1-qhat^n)/(1-qhat^{5n}))^6 "
                          "with every factor > 0 => sign t5 = sign qhat; t5 = -10 "
                          "requires qhat < 0 i.e. Re tau = 1/2 mod 1 (half-period twist)",
        "n5h_nome_identity": "the spin-twisted nome dictionary tau = -1/2 + i ln(q0)/(2pi) "
                             "has modular nome exactly -1/q0",
    })
    wb.add_data("task3_spin_data", {
        "source_papers": {
            "BN12": "library/sigma12-065/sigma12-065.pdf (Braden-Northover, SIGMA 8 (2012) 065)",
            "BDH22": "library/arxiv-2208.13692v1/2208.13692v1.pdf (Braden-Disney-Hogg)",
        },
        "K_Q": "(1/10)(3,2,-2,-3) + Im(tau0)*(1,-2,-2,1)*i (BN12 Thm 3 = BDH22 "
               "Prop 5.13, verbatim cross-paper agreement; RR92 homology basis)",
        "torsion": "BN12 Lemma 1 gives 2N = 10-torsion (N = 5); sharpened here: "
                   "(1,-2,-2,1) is a 5-eigenvector of M_RR, so 5*K_Q = (4,-4,-6,1) "
                   "+ tau_B*(1,-2,-2,1) — K_Q is EXACTLY 5-torsion (symbolic in Im tau0)",
        "snf": "SNF(M - Id) = Diag(1,1,1,1,1,1,5,5) re-derived from the printed 8x8 M",
        "invariant_characteristic": "Delta = 3a + b - c (BDH22 Ex 5.3), EVEN, unique "
                                    "Aut(=S5)-invariant (BDH22 Thm 5.11; BN12 Thm 4 "
                                    "existence); = Szego divisor Delta_S with "
                                    "K_a = A_a(Delta_S) (BDH22 Prop 5.13, 1e-118): "
                                    "the invariant spin structure is the ORIGIN of "
                                    "the theta-frame based at a",
        "orbit_counts": "odd 120 = 20+20+20+60 (BDH22 Cor 5.7); even 136 = "
                        "1+5+5+5+10+10+10+30+30+30 (BDH22 Thm 5.9); the '1' is the "
                        "unique S5 fixed point",
        "briefing_correction": "the parent briefing said 'odd theta-characteristic / "
                               "spin twist'; the unique invariant characteristic is "
                               "EVEN. The sign-of-t5 twist is a half-period shift of "
                               "the nome frame (Re tau = -1/2), a distinct discrete "
                               "datum; identifying it with the invariant spin "
                               "structure is a framework hypothesis (A6 risk note), "
                               "not established here",
        "tau0_prints": "BDH22 tau0 = -0.5+0.186676i passes the gate; BN12's own "
                       "6-d.p. print 0.185576 does not (BDH22 correction "
                       "load-bearing for Im(tau0)-dependent data)",
    })
    wb.add_data("q0_pins", {"muon": Q0_MUON, "proton": Q0_PROTON})
    wb.add_caveat(
        "Scope-(a) throughout: every FAIL refutes the stated map only, never an "
        "ingredient. The two (b)-type exclusions (pure-imaginary dictionaries; "
        "the W5-fixed-circle family) cite proved invariants (sign positivity of "
        "the real-nome eta-product; |t5| = 5*sqrt5 on the Fricke-fixed circle) "
        "per AGENTS.md 'Before declaring refuted'. Candidates were enumerated "
        "from bar/Fricke/half-period structure only, never adjusted toward "
        "-10. The worldline-spin <-> Bring-spin-structure identification "
        "remains a framework hypothesis; the tau-functor (B2) remains open."
    )
    wb.add_assertion(
        "cusp_coefficients_exact",
        computed=",".join(str(c) for c in coeffs),
        expected=",".join(str(c) for c in CUSP_COEFFS_EXPECTED),
        tolerance=None,
        source="Exact integer series: prod(1-q^{5n})^6/prod(1-q^n)^6 c_0..c_8.",
    )
    wb.add_assertion(
        "cusp_form_matches_eta_product_both_pins",
        computed=float(max(mpf(pin_results[p]["rel_agreement"]) for p in pin_results)),
        expected=0.0,
        tolerance=1e-60,
        source="t5(i|ln q0|/(2pi)) direct eta-product vs 125*qt*sum(c_k qt^k) at "
               "dps 120, both q0 pins — the nome dictionary is exponentially "
               "cusp-suppressed at theorem level.",
    )
    wb.add_assertion(
        "fricke_fixed_point_exact_value",
        computed=float(fix_dev),
        expected=0.0,
        tolerance=1e-40,
        source="|t5(i/sqrt5) - 5*sqrt5| (Fricke-fixed => t5^2 = 125).",
    )
    wb.add_assertion(
        "w5_circle_family_excluded",
        computed=float(circle_dev),
        expected=0.0,
        tolerance=1e-40,
        source="||t5|^2 - 125| on the bar<->Fricke-equivariant circle family "
               "(both pins) — |t5| = 5*sqrt5 != 10 excludes every "
               "parametrization of the W5-fixed circle (proved invariant).",
    )
    wb.add_assertion(
        "all_candidates_fail_gate",
        computed="+".join(sorted({r["verdict"] for res in results.values()
                                  for r in res["results"].values()})),
        expected="FAIL",
        tolerance=None,
        source="10 structure-enumerated candidates x 2 pins: every verdict FAIL "
               "(honest outcome; no PASS found; nothing proposed).",
    )
    wb.add_assertion(
        "kq_exactly_5_torsion",
        computed="5K = (4,-4,-6,1) + tau_B*(1,-2,-2,1); k=1..4 non-lattice",
        expected="5K = (4,-4,-6,1) + tau_B*(1,-2,-2,1); k=1..4 non-lattice",
        tolerance=None,
        source="Exact sympy, symbolic in Im(tau0): K_Q (BN12 Thm 3) is exactly "
               "5-torsion, sharpening Lemma 1's 2N = 10 bound; SNF(M-Id) = "
               "Diag(1,...,1,5,5) re-derived from printed M (order 5, Sp(8,Z)).",
    )
    wb.save()
    print("\nwitness saved; all assertions passed.")


if __name__ == "__main__":
    main()
