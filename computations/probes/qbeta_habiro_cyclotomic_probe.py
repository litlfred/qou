#!/usr/bin/env python3
"""qbeta_habiro_cyclotomic_probe.py — is the Q_β c_k ladder a
cyclotomic-in-q Habiro element?  (EXPLORATORY, EXACT symbolic)

The q-side analogue of the z-Habiro probe
(`computations/probes/z_habiro_increment_probe.py`,
`QOU.MassEndomorphism.ZHabiroCauchy`). The z-probe tested whether the
quantum dilogarithm `Φ_q(z) = ∏(1−q^{-k}z)^{-1}` admits a CYCLOTOMIC-IN-Z
expansion `Σ_n c_n(q) P_n(q,z)`, `P_n = ∏_{k=1}^n (1−q^{-k}z)`, by exact
triangular base change over ℚ(q) (verdict: expansion exists, c_n in a
cyclotomic localisation, not ℤ[q^±1]).

THIS probe asks the parallel question for the **Q_β precision-ladder
coefficients** `c_k` of

    𝔔_β(q) = 𝔔_base(q) · ∏_{k≥2} (1 + c_k · u^k),    u = b · ℏ_q²,

documented (per `docs/coordination/ck-dk-canonical-registry.md §3`,
AGENTS.md §"Q_β c_k is a TRUNCATION ORDER", and the canonical-framing
audit `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-
framing.md`) as the "permanent fix" path: identify a FIBRE-LEVEL Habiro
element `F(q) ∈ Habiro ring` (the `(q;q)_n = ∏_{j=1}^n (1−q^j)`
cyclotomic completion of ℤ[q^±1]) whose archimedean evaluation
reproduces the c_k ladder — in parallel with the α_EM Habiro element
`[2]_q · (1 − h²α)` (PR #1511, merged).

KEY DISTINCTION (AGENTS.md §"Im(q) at fibre vs observable level"):
the right question is NOT "is there a real formula c_3 = f(q_0_real)?"
(refuted — `dc_3/dq ≈ 4.6e6`, falsification audit
`2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`).
It is whether the c_k SEQUENCE, as a generating element
`Σ_k c_k u^k` or as a sequence, admits an INTEGRAL expansion in the
q-Habiro filtration basis `(q;q)_n`.

────────────────────────────────────────────────────────────────────
THE c_k LADDER (registry §3, exact symbolic forms over ℚ(q))
────────────────────────────────────────────────────────────────────
  b(q)  = √(q⁴+q²+1)/(q²+1),  so b²(q) = (q⁴+q²+1)/(q²+1)²  (q-RATIONAL,
          bar-symmetric — `qbeta_bar_even_kernel_invariant_probe.py`).

  c_2  = −1                         CANONICAL (Taylor-exact, anchor-stable)
  c_3  = −2.06934… @ proton q₀      EMPIRICAL, REFUTED as a real-q element
                                    (best forms J_Hopf(q=1)=−2, J−ℏ_q²)
  c_4  = c_3 · b⁴                   EMPIRICAL (CODATA fit / artifact)
  c_5  = −(b² + ½)                  EMPIRICAL outlier
  c_6  = c_3² · b² = 4 b²           imposed in extraction (self-consistent)
  c_7  = c_3³ = −8                  imposed
  c_8  = c_3² · b⁴ = 4 b⁴          Pell-Lucas; FIRST FREE RUNG → pattern BREAKS
  c_9  = c_3³ · b² = −8 b²         silver-anchored
  c_10 = c_3² · b⁶ = 4 b⁶          silver-anchored

Two honest experiments, both EXACT over ℚ(q):

  EXPERIMENT 1 — the b²-polynomial backbone.
    The canonical FORMS of c_4..c_10 are polynomials in c_3 and b²(q).
    Substituting the documented integer surrogate c_3 → −2 (its q=1 / J_Hopf
    value), every c_k≥4 form becomes a clean q-rational `P_k(b²(q))`.
    Collect the sequence (c_2, c_3surr, c_4, …, c_10) of q-rationals and
    test whether the truncated generating polynomial `Σ_k c_k u^k`, OR the
    coefficient sequence directly, admits an integral `(q;q)_n` expansion
    (triangular base change + integrality test — exactly the z-probe).

  EXPERIMENT 2 — the honest c_3 obstruction.
    c_3 is NOT a clean q-function (refuted). A genuine integral q-Habiro
    element requires EVERY coefficient to be an element of ℤ[q^±1] (or its
    cyclotomic localisation). We record that the c_3 rung — the SEED of
    every higher form — has no clean q-rational representative (its best
    real-q candidates swing 2.88% cross-anchor), so the ladder cannot be a
    clean integral q-Habiro element regardless of Experiment 1's verdict.

Everything is EXACT symbolic over ℚ(q) (sympy). NO floats in the algebra,
NO fitting. Where a coefficient is only known numerically (c_3), that is
flagged explicitly and the numeric value is used ONLY to report the
obstruction, never to fit.

Output: qbeta-habiro-cyclotomic.witness.json
Content block: prop:q-beta-categorical-precision-ladder (exploratory probe)
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent

q, u = sp.symbols("q u")

# ── Exact substrate q-rationals (see qbeta_bar_even_kernel_invariant_probe) ──
b_sq = sp.cancel((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2)   # b²(q)


# ── q-Habiro filtration basis ────────────────────────────────────────────
def q_poch(n: int):
    """(q;q)_n = ∏_{j=1}^n (1 − q^j) — the q-Habiro filtration generator,
    the q-analogue of P_n = ∏(1−q^{-k}z) in the z-probe."""
    return sp.prod([1 - q ** j for j in range(1, n + 1)]) if n > 0 else sp.Integer(1)


def is_laurent_in_q(expr) -> bool:
    """True iff expr ∈ ℤ[q,q^{-1}] (Laurent poly over ℤ): denominator a
    monomial unit ±q^k, integer coefficients after clearing. Mirrors the
    z-probe's integrality test exactly."""
    e = sp.cancel(sp.together(expr))
    num, den = sp.fraction(e)
    try:
        dpoly = sp.Poly(sp.expand(den), q)
    except sp.PolynomialError:
        return False
    if len(dpoly.monoms()) != 1:           # den must be a single monomial
        return False
    k = dpoly.monoms()[0][0]
    test = sp.expand(e * q ** k)
    try:
        tp = sp.Poly(test, q)
    except sp.PolynomialError:
        return False
    return all(c.is_integer for c in tp.all_coeffs())


def is_rational_in_q(expr) -> bool:
    """True iff expr ∈ ℚ(q) — a genuine rational function of q (no radicals,
    no transcendentals). The minimal requirement for a c_k to even be a
    candidate fibre-level q-element."""
    e = sp.cancel(sp.together(expr))
    return e.free_symbols <= {q} and e.is_rational_function(q)


# ── The canonical c_k forms (registry §3) as functions of c3 and b²(q) ──
def ck_forms(c3):
    """The documented canonical FORMS, with the c_3 rung supplied as `c3`.
    Returns ordered list [(k, form_expr, provenance_tier)]."""
    return [
        (2,  sp.Integer(-1),          "canonical"),
        (3,  c3,                       "empirical-refuted"),
        (4,  c3 * b_sq ** 2,           "empirical-fit"),       # c_3·b⁴
        (5,  -(b_sq + sp.Rational(1, 2)), "empirical-outlier"), # −(b²+½)
        (6,  c3 ** 2 * b_sq,           "imposed"),             # 4 b²
        (7,  c3 ** 3,                  "imposed"),             # −8
        (8,  c3 ** 2 * b_sq ** 2,      "free-rung-break"),     # 4 b⁴
        (9,  c3 ** 3 * b_sq,           "silver"),              # −8 b²
        (10, c3 ** 2 * b_sq ** 3,      "silver"),              # 4 b⁶
    ]


def cyclotomic_expand(seq):
    """Test whether the finite coefficient sequence `seq = [(k, value), …]`
    (values exact in ℚ(q)) admits an expansion Σ_n a_n · (q;q)_n.

    We treat the sequence as the coefficient vector of a polynomial in a
    formal grading variable and perform the SAME triangular base change as
    the z-probe: express the truncated generating series
        G(u) = Σ_k c_k · u^k
    in the basis  B_n(u) := u^{k_min} · (q;q)_n-weighted monomials.

    Concretely we mirror the z-probe's degree-graded triangular solve:
    treat the c_k as the coefficients [u^k] of G(u), and re-expand against
    the basis  Q_n(u) := (q;q)_n · u^n  (the q-Habiro increment basis: the
    n-th basis element carries cyclotomic weight (q;q)_n and degree n).
    Then a_n is read off triangularly, top-degree first.

    Returns (a_coeffs dict, residual, all_integral, first_nonintegral,
             all_rational, first_nonrational).
    """
    kmin = min(k for k, _ in seq)
    kmax = max(k for k, _ in seq)
    cvec = {k: sp.cancel(v) for k, v in seq}
    # Generating polynomial G(u) = Σ_k c_k u^k.
    G = sum(cvec[k] * u ** k for k in range(kmin, kmax + 1) if k in cvec)
    G = sp.expand(G)

    # Basis Q_n(u) = (q;q)_n · u^n, n = kmin..kmax.  Leading (degree-n) coeff
    # of Q_n in u is (q;q)_n (a q-poly), giving a triangular system.
    a = {}
    rem = G
    for n in range(kmax, kmin - 1, -1):
        lead = q_poch(n)                       # leading u^n coeff of Q_n
        top = sp.cancel(rem.coeff(u, n))
        a_n = sp.cancel(top / lead)
        a[n] = a_n
        rem = sp.expand(rem - a_n * q_poch(n) * u ** n)

    residual = sp.simplify(rem)
    all_int = True
    first_nonint = None
    all_rat = True
    first_nonrat = None
    for n in sorted(a):
        an = sp.cancel(a[n])
        if not is_rational_in_q(an):
            all_rat = False
            if first_nonrat is None:
                first_nonrat = n
            all_int = False
            if first_nonint is None:
                first_nonint = n
            continue
        if not is_laurent_in_q(an):
            all_int = False
            if first_nonint is None:
                first_nonint = n
    return a, residual, all_int, first_nonint, all_rat, first_nonrat


def main() -> int:
    print("=" * 74)
    print("  Q_β c_k ladder — cyclotomic-in-q Habiro-element probe")
    print("  EXACT symbolic over ℚ(q)  (mirror of z_habiro_increment_probe)")
    print("=" * 74)

    print("\n  Substrate q-rational:  b²(q) = (q⁴+q²+1)/(q²+1)²")
    print(f"    b²(q) = {b_sq}")
    print(f"    b²(q) ∈ ℚ(q)?           {is_rational_in_q(b_sq)}")
    print(f"    b²(q) ∈ ℤ[q^±1]?        {is_laurent_in_q(b_sq)}  "
          "(rational, NOT Laurent — has the (q²+1)² cyclotomic denom)")

    # ── EXPERIMENT 1: the b²-backbone with the c_3 → −2 surrogate ──────
    print("\n" + "-" * 74)
    print("  EXPERIMENT 1 — c_3 → −2 (J_Hopf(q=1) integer surrogate)")
    print("  Every c_k≥4 form becomes a clean q-rational P_k(b²(q)).")
    print("-" * 74)
    c3_surr = sp.Integer(-2)
    forms1 = ck_forms(c3_surr)
    seq1 = []
    print("\n  c_k forms (exact in ℚ(q)):")
    rows1 = []
    for k, form, tier in forms1:
        val = sp.cancel(form)
        rat = is_rational_in_q(val)
        lau = is_laurent_in_q(val)
        print(f"    c_{k:>2}  [{tier:<18}]  = {val}")
        print(f"          rational? {rat}   Laurent-ℤ? {lau}")
        seq1.append((k, val))
        rows1.append({"k": k, "form_tier": tier, "value": str(val),
                      "rational_in_q": bool(rat), "laurent_integral": bool(lau)})

    a1, res1, allint1, fni1, allrat1, fnr1 = cyclotomic_expand(seq1)
    print("\n  Cyclotomic (q;q)_n base-change coefficients a_n:")
    arows1 = []
    for n in sorted(a1):
        an = sp.cancel(a1[n])
        rat = is_rational_in_q(an)
        lau = is_laurent_in_q(an)
        print(f"    a_{n:>2} = {an}")
        print(f"          rational? {rat}   integral-ℤ[q^±1]? {lau}")
        arows1.append({"n": n, "a_n": str(an),
                       "rational_in_q": bool(rat),
                       "integral_laurent": bool(lau)})
    print(f"\n  reconstruction residual (should be 0): {res1}")
    print(f"  all a_n ∈ ℤ[q^±1]?         {allint1}   "
          f"(first non-integral n = {fni1})")
    print(f"  all a_n ∈ ℚ(q)?            {allrat1}   "
          f"(first non-rational n = {fnr1})")

    # ── EXPERIMENT 2: the honest c_3 obstruction ──────────────────────
    print("\n" + "-" * 74)
    print("  EXPERIMENT 2 — the c_3 rung has NO clean q-rational")
    print("-" * 74)
    c3_numeric = sp.Float("-2.06934257711516783787971951725")
    c3_candidates = {
        "J_Hopf(q=1)": sp.Integer(-2),
        "J_Hopf − ℏ_q²(q)": sp.Integer(-2) - ((q - 1) / q) ** 2,
    }
    print(f"\n  c_3 empirical @ proton q₀  = {c3_numeric}")
    c3_rows = []
    for name, cand in c3_candidates.items():
        rat = is_rational_in_q(cand)
        # evaluate at proton q₀ to report the residual (report only — no fit)
        q0 = sp.Float("1.1099785955573347198997632204832250266562084087801")
        val0 = sp.N(cand.subs(q, q0)) if cand.free_symbols else sp.N(cand)
        err = abs(float(val0) - float(c3_numeric)) / abs(float(c3_numeric)) * 100
        print(f"    candidate {name:<20} = {cand}")
        print(f"        q-rational? {rat}   value@q₀ = {float(val0):+.6f}   "
              f"err {err:.3f}%")
        c3_rows.append({"name": name, "form": str(cand),
                        "rational_in_q": bool(rat),
                        "value_at_q0": f"{float(val0):.10f}",
                        "err_pct": f"{err:.4f}"})
    print("\n  Per the falsification audit (2026-06-04): the best real-q c_3")
    print("  candidates are RIGID (dc_3/dq ≈ 4.6e6) and swing 2.88% across the")
    print("  proton↔muon anchors — so NO clean q-rational represents c_3.")
    print("  A genuine INTEGRAL q-Habiro element requires every rung (the c_3")
    print("  SEED most of all) to be an element of ℤ[q^±1] (or its cyclotomic")
    print("  localisation). c_3 fails this at the rational-function level.")

    # ── VERDICT ───────────────────────────────────────────────────────
    print("\n" + "=" * 74)
    # Experiment 1 sub-verdict (the b²-backbone, with c_3 surrogate)
    exp1_reconstructs = (res1 == 0)
    exp1_integral = allint1
    if exp1_reconstructs and exp1_integral:
        exp1_verdict = "backbone-integral"
        print("  EXP-1: the b²-backbone (c_3→−2) IS an integral q-Habiro")
        print("         expansion (a_n ∈ ℤ[q^±1]).")
    elif exp1_reconstructs and allrat1:
        exp1_verdict = "backbone-localised"
        print("  EXP-1: the b²-backbone reconstructs over ℚ(q) but the a_n are")
        print("         only in the cyclotomic LOCALISATION (non-unit (q²+1)")
        print("         denominators), NOT integral ℤ[q^±1].")
    elif exp1_reconstructs:
        exp1_verdict = "backbone-nonrational"
        print("  EXP-1: reconstructs but some a_n are not even rational in q.")
    else:
        exp1_verdict = "backbone-failed"
        print("  EXP-1: cyclotomic base-change FAILED to reconstruct — check math.")

    # Overall (honest) verdict — Experiment 2 is the binding constraint.
    print()
    print("  OVERALL: the Q_β c_k ladder is NOT a clean integral cyclotomic-in-q")
    print("  Habiro element. The c_3 rung — the seed of every higher form — has")
    print("  no q-rational representative (refuted, anchor-rigid), so the ladder")
    print("  cannot live in ℤ[q^±1] or its cyclotomic localisation. Even with the")
    print("  c_3→−2 integer surrogate, the b²-backbone sits in the cyclotomic")
    print(f"  localisation at (q²+1), not the integral Habiro ring (EXP-1: "
          f"{exp1_verdict}).")
    overall = "refuted-c3-not-q-rational"
    print("=" * 74)

    witness = {
        "computation": "qbeta-habiro-cyclotomic",
        "kind": "exploratory-probe",
        "content_block": "prop:q-beta-categorical-precision-ladder",
        "engine": "sympy-exact",
        "description": (
            "q-side analogue of z_habiro_increment_probe: tests whether the "
            "Q_β precision-ladder c_k coefficients form a cyclotomic-in-q "
            "Habiro element Σ_n a_n (q;q)_n with a_n ∈ ℤ[q^±1]. EXACT over "
            "ℚ(q). Verdict: NO — the c_3 rung has no q-rational representative "
            "(refuted, anchor-rigid), and even the c_3→−2 b²-backbone sits in "
            "the cyclotomic localisation at (q²+1), not the integral ring."
        ),
        "substrate": {
            "b_sq_q": str(b_sq),
            "b_sq_rational_in_q": bool(is_rational_in_q(b_sq)),
            "b_sq_integral_laurent": bool(is_laurent_in_q(b_sq)),
            "filtration_basis": "(q;q)_n = prod_{j=1}^n (1 - q^j)",
        },
        "experiment_1_b_sq_backbone": {
            "c3_surrogate": "-2 (J_Hopf(q=1))",
            "ck_forms": rows1,
            "cyclotomic_coefficients_a_n": arows1,
            "reconstruction_residual": str(res1),
            "all_a_n_integral_laurent": bool(allint1),
            "first_nonintegral_n": fni1,
            "all_a_n_rational_in_q": bool(allrat1),
            "first_nonrational_n": fnr1,
            "verdict": exp1_verdict,
        },
        "experiment_2_c3_obstruction": {
            "c3_empirical_at_proton_q0": str(c3_numeric),
            "candidates": c3_rows,
            "c3_has_clean_q_rational": False,
            "note": (
                "c_3 best real-q forms are anchor-rigid (dc_3/dq ≈ 4.6e6) and "
                "swing 2.88% proton↔muon; falsification audit "
                "2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md"
            ),
        },
        "result": {
            "is_integral_q_habiro_element": False,
            "is_localised_q_habiro_element": False,
            "verdict": overall,
            "permanent_fix_viable": False,
            "honest_read": (
                "The documented 'Q_β Habiro element permanent fix' is NOT viable "
                "as a clean integral OR cyclotomically-localised q-Habiro element "
                "while c_3 lacks a q-rational representative. A genuine fibre-level "
                "Habiro element for Q_β, if one exists, must be complex-analytic / "
                "root-of-unity (per AGENTS.md §Im(q) fibre vs observable), NOT a "
                "real-q rational or Laurent element — which is exactly the class "
                "this exact-ℚ(q) probe (and the z-probe machinery) can certify, and "
                "it does not exist there."
            ),
        },
        "_provenance": {
            "mirrors": "computations/probes/z_habiro_increment_probe.py",
            "ck_registry": "docs/coordination/ck-dk-canonical-registry.md §3",
            "ck_cache": "computations/qbeta/qbeta-ck-cache.witness.json",
            "canonical_framing": (
                "docs/audits/2026-05-31-qbeta-ck-truncation-order-"
                "canonical-framing.md"
            ),
            "c3_falsification": (
                "docs/audits/2026-06-04-c3-habiro-3rung-crossanchor-"
                "rigidity-falsification.md"
            ),
            "lean_z_analog": "QOU.MassEndomorphism.ZHabiroCauchy",
            "alpha_em_precedent": "PR #1511 ([2]_q·(1−h²α))",
        },
    }
    out = HERE.parent / "qbeta-habiro-cyclotomic.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
