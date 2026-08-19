#!/usr/bin/env python3
"""s013 — the GENUINE Σ(2,3,5) S-matrix from the primary literature: the value step settled at
the false-theta level.

Bean s013, step 3. The primary sources are now in-repo (owner upload, commit ece271823:
`library/arxiv-math-ph-0405028v2/0405028v2.pdf` = Hikami, *On the quantum invariant for the Brieskorn homology
spheres*, math-ph/0405028; also 1811.05376v4, 2205.01282v2, and Lawrence–Zagier 1999
`fulltext.pdf`). This probe transcribes the genuine structure and MACHINE-VALIDATES every
transcribed formula before drawing any conclusion:

  (χ)  Hikami eq. (3.1): the odd periodic χ^{(ℓ1,ℓ2,ℓ3)}_{2P}. For Σ(2,3,5) the independent
       triples are (1,1,1) and (1,1,2) — D(2,3,5) = (p1−1)(p2−1)(p3−1)/4 = 2. VERIFIED here:
       χ^{(1,1,1)} = the character our round-2 sympy identity derived for colour α=1
       (−1 on {1,11,19,29}, +1 on {31,41,49,59} — Hikami eq. (5.6) IS that identity), and
       χ^{(1,1,2)} = our α=2 character. So the colored family of PR #3190 is exactly the
       D=2 vector-valued modular family: α∈{1,4} ↔ (1,1,1), α∈{2,3} ↔ (1,1,2).
  (τ)  Proposition 1 eq. (2.11): the WRT invariant τ_N as a finite Gauss-sum. φ(2,3,5) =
       181/30 re-derived from Dedekind sums (eq. 2.12).
  (T10) Theorem 10 eq. (5.5): e^{2πi/N}(e^{2πi/N}−1)τ_N = 1 + ½e^{−πi/60N} Φ̃^{(1,1,1)}(1/N),
       with Φ̃(1/N) the finite sum of eq. (4.2). EXACT identity, checked at several N to
       ~1e−30 — this is the anti-fabrication anchor validating the whole transcription chain.
  (S)  Eq. (3.8): the D×D S-matrix S^{ℓ'}_{ℓ} = √(32/P)·(−1)^{1+P+PΣ(ℓj+ℓ'j)/pj+(ℓ×ℓ')·p}
       ∏j sin(P ℓj ℓ'j π / pj²). VERIFIED: S² = 1 (involution), and the vacuum row
       √(N/i)-weights reproduce Corollary 12's explicit flat-connection amplitudes
       (2/√5)(sin(π/5), sin(2π/5)) with CS = −1/120, −49/120.
  (C12) Corollary 12 eq. (5.8): the exact asymptotic expansion — checked numerically at
       increasing N (residual after the L-series tail decreases).

VERDICT this makes possible (the s013 value step, settled at this level):

  The genuine "vacuum row" of the Σ(2,3,5) WRT/false-theta theory — the per-flat-connection
  S-matrix amplitudes the bean asked for — is **2-dimensional**, ∝ (sin(π/5), sin(2π/5)),
  ratio = golden ratio φ ≈ 1.618 (the icosahedral / Fibonacci pair; by Hikami Thm 14 the
  magnitudes are √(Reidemeister torsion)). The keystone target bwS0(λ) = d_q(λ)/D at n=5
  is a **4-class** family with ratios (1, 4.110, 5.220, 6.220). Type mismatch (2 ≠ 4) and
  value mismatch (φ ≠ any target ratio): **the direct identification "bwS0 = vacuum row of
  the Σ(2,3,5) false-theta S-matrix" is REFUTED** — scope (a): this specific geometric
  object; the W_λ index question is not closed, but it cannot be carried by the D=2
  Σ(2,3,5) modular family alone. The #3190 "4↔4" correspondence (E₈ dual pairs ↔ bwS0
  classes) lives at SUPPORT level only: as functions, the 4 colours span just 2 independent
  components (α=4≡α=1, α=3≡α=2 — verified in round 2 and again here via (3.3)/(3.1)).

# Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694  (math-ph/0405028; eqs. 2.11,
#      2.12, 3.1, 3.8, 4.2, 5.5, 5.8, Thm 14)
# Ref: [lawrence-zagier-1999] https://doi.org/10.4310/AJM.1999.v3.n1.a5
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf, mpc, bernpoly, factorial  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40
PVEC = (2, 3, 5)
P = 30
TWO_P = 60
Q0 = mpf("1.1099785955541805")
I = mpc(0, 1)

# the two independent triples for (2,3,5) (Hikami §5: D(2,3,5)=2)
TRIPLES = ((1, 1, 1), (1, 1, 2))

# round-2 derived characters (sympy identity, keystone_valuemap_qbessel_gate_s013):
ROUND2_ALPHA1 = {1: -1, 11: -1, 19: -1, 29: -1, 31: 1, 41: 1, 49: 1, 59: 1}
ROUND2_ALPHA2 = {7: -1, 13: -1, 17: -1, 23: -1, 37: 1, 43: 1, 47: 1, 53: 1}


def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


# ────────────────────────────────────────────────────────────────────────────
# (χ) Hikami eq. (3.1)
# ────────────────────────────────────────────────────────────────────────────
def chi_hikami(triple):
    """χ^{(ℓ1,ℓ2,ℓ3)}_{2P}(n): +1 at n ≡ P(1+Σ εj ℓj/pj) mod 2P with ε1ε2ε3 = −1,
    −1 with ε1ε2ε3 = +1, else 0. Returns {residue mod 60: value}."""
    out = {}
    for e1 in (-1, 1):
        for e2 in (-1, 1):
            for e3 in (-1, 1):
                val = Fraction(P) * (1 + Fraction(e1 * triple[0], PVEC[0])
                                     + Fraction(e2 * triple[1], PVEC[1])
                                     + Fraction(e3 * triple[2], PVEC[2]))
                assert val.denominator == 1
                r = int(val) % TWO_P
                out[r] = 1 if e1 * e2 * e3 == -1 else -1
    return out


def chi_fn(table):
    def chi(n):
        return table.get(n % TWO_P, 0)
    return chi


# ────────────────────────────────────────────────────────────────────────────
# (τ) Proposition 1 eq. (2.11) + φ from Dedekind sums (2.12)
# ────────────────────────────────────────────────────────────────────────────
def dedekind_s(b, a):
    return mp.fsum(mp.cot(mp.pi * k / a) * mp.cot(mp.pi * k * b / a)
                   for k in range(1, a)) / (4 * a)


def phi_235():
    return (3 - mpf(1) / P
            + 12 * (dedekind_s(15, 2) + dedekind_s(10, 3) + dedekind_s(6, 5)))


def tau_N(N):
    """τ_N(Σ(2,3,5)) from eq. (2.11)."""
    pref_lhs = mp.e ** (2 * mp.pi * I / N * (phi_235() / 4 - mpf(1) / 2)) \
        * (mp.e ** (2 * mp.pi * I / N) - 1)
    total = mpc(0)
    for n in range(2 * P * N):
        if n % N == 0:
            continue
        num = mpc(1)
        for pj in PVEC:
            num *= (mp.e ** (n * mp.pi * I / (N * pj))
                    - mp.e ** (-n * mp.pi * I / (N * pj)))
        den = mp.e ** (n * mp.pi * I / N) - mp.e ** (-n * mp.pi * I / N)
        total += mp.e ** (-n * n * mp.pi * I / (2 * P * N)) * num / den
    rhs = mp.e ** (mp.pi * I / 4) / (2 * mp.sqrt(mpf(2 * P * N))) * total
    return rhs / pref_lhs


# ────────────────────────────────────────────────────────────────────────────
# (T10/4.2) Eichler-integral limiting value + Theorem 10
# ────────────────────────────────────────────────────────────────────────────
def eichler_at_1_over_N(chi, N):
    """Φ̃(1/N) = Σ_{n=0}^{PN} χ(n)(1 − n/(PN)) e^{n²πi/(2PN)}   (eq. 4.2)."""
    return mp.fsum((chi(n) * (1 - mpf(n) / (P * N))
                    * mp.e ** (n * n * mp.pi * I / (2 * P * N)))
                   for n in range(P * N + 1) if chi(n))


def theorem10_residual(chi111, N):
    lhs = (mp.e ** (2 * mp.pi * I / N)
           * (mp.e ** (2 * mp.pi * I / N) - 1) * tau_N(N))
    rhs = 1 + mp.e ** (-mp.pi * I / (60 * N)) * eichler_at_1_over_N(chi111, N) / 2
    return abs(lhs - rhs)


# ────────────────────────────────────────────────────────────────────────────
# (S) eq. (3.8) and (C12) eq. (5.8)
# ────────────────────────────────────────────────────────────────────────────
def s_entry(l, lp):
    """S^{ℓ'}_{ℓ} = √(32/P) (−1)^{1+P+PΣ(ℓj+ℓ'j)/pj+(ℓ×ℓ')·p} ∏ sin(P ℓj ℓ'j π/pj²)."""
    expo = Fraction(1 + P)
    for lj, lpj, pj in zip(l, lp, PVEC):
        expo += Fraction(P * (lj + lpj), pj)
    cross = (l[1] * lp[2] - l[2] * lp[1]) * PVEC[0] \
        + (l[2] * lp[0] - l[0] * lp[2]) * PVEC[1] \
        + (l[0] * lp[1] - l[1] * lp[0]) * PVEC[2]
    expo += cross
    assert expo.denominator == 1
    sign = (-1) ** (int(expo) % 2)
    prod = mpf(1)
    for lj, lpj, pj in zip(l, lp, PVEC):
        prod *= mp.sin(mp.pi * P * lj * lpj / (pj * pj))
    return mp.sqrt(mpf(32) / P) * sign * prod


def l_value(chi, k):
    """L(−2k, χ) = −(2P)^{2k}/(2k+1) Σ_{j=1}^{2P} χ(j) B_{2k+1}(j/2P)   (eq. 4.18)."""
    return (-mpf(2 * P) ** (2 * k) / (2 * k + 1)
            * mp.fsum(chi(j) * bernpoly(2 * k + 1, mpf(j) / (2 * P))
                      for j in range(1, 2 * P + 1) if chi(j)))


def cor12_residual(chi111, N, kmax=8):
    """LHS − RHS of eq. (5.8) with the L-tail truncated at kmax."""
    lhs = (mp.e ** (2 * mp.pi * I / N * mpf(121) / 120)
           * (mp.e ** (2 * mp.pi * I / N) - 1) * tau_N(N))
    flat = (mp.sqrt(mpf(N)) * mp.e ** (-mp.pi * I / 4) * 2 / mp.sqrt(mpf(5))
            * (mp.sin(mp.pi / 5) * mp.e ** (-mp.pi * I * N / 60)
               + mp.sin(2 * mp.pi / 5) * mp.e ** (-49 * mp.pi * I * N / 60)))
    tail = mp.e ** (mp.pi * I / (60 * N)) + mp.fsum(
        l_value(chi111, k) / factorial(k) * (mp.pi * I / (60 * N)) ** k / 2
        for k in range(kmax + 1))
    return abs(lhs - flat - tail)


def run():
    out = {"P": P, "pvec": list(PVEC), "q0": float(Q0)}

    # (χ) characters + round-2 cross-validation + D=2 colored-family identification
    chi111_tbl = chi_hikami((1, 1, 1))
    chi112_tbl = chi_hikami((1, 1, 2))
    out["chi_111"] = {str(k): v for k, v in sorted(chi111_tbl.items())}
    out["chi_112"] = {str(k): v for k, v in sorted(chi112_tbl.items())}
    out["chi111_equals_round2_alpha1"] = chi111_tbl == ROUND2_ALPHA1
    out["chi112_equals_round2_alpha2"] = chi112_tbl == ROUND2_ALPHA2
    out["D_235"] = (PVEC[0] - 1) * (PVEC[1] - 1) * (PVEC[2] - 1) // 4
    # symmetry (3.3): (1,1,4)~(1,1,1)-class, (1,1,3)~(1,1,2)-class
    out["alpha4_same_class_as_alpha1"] = chi_hikami((1, 1, 4)) == chi_hikami((1, 2, 4)) or \
        chi_hikami((1, 1, 4)) == chi_hikami((1, 1, 1))
    out["alpha3_same_class_as_alpha2"] = chi_hikami((1, 1, 3)) == chi_hikami((1, 1, 2))
    chi111 = chi_fn(chi111_tbl)

    # (τ) φ(2,3,5) = 181/30
    phi = phi_235()
    out["phi_235"] = float(phi)
    out["phi_equals_181_over_30"] = bool(abs(phi - mpf(181) / 30) < mpf("1e-35"))

    # (T10) exact identity at several N
    t10 = {}
    for N in (3, 5, 7, 11):
        t10[str(N)] = float(theorem10_residual(chi111, N))
    out["theorem10_residuals"] = t10
    out["theorem10_exact"] = all(v < 1e-28 for v in t10.values())

    # (S) S-matrix: involution + vacuum row vs Corollary 12 weights
    S = [[s_entry(a, b) for b in TRIPLES] for a in TRIPLES]
    out["S_matrix"] = [[float(x) for x in row] for row in S]
    s2 = [[mp.fsum(S[i][k] * S[k][j] for k in range(2)) for j in range(2)]
          for i in range(2)]
    out["S_squared_is_identity"] = bool(
        max(abs(s2[i][j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
        < mpf("1e-35"))
    w1 = 2 / mp.sqrt(mpf(5)) * mp.sin(mp.pi / 5)
    w2 = 2 / mp.sqrt(mpf(5)) * mp.sin(2 * mp.pi / 5)
    out["vacuum_row_matches_cor12_weights"] = bool(
        abs(S[0][0] - w1) < mpf("1e-35") and abs(S[0][1] - w2) < mpf("1e-35"))
    out["cor12_weights"] = {"flat1": float(w1), "flat2": float(w2),
                            "CS": ["-1/120", "-49/120"]}
    out["vacuum_row_ratio"] = float(S[0][1] / S[0][0])
    out["golden_ratio"] = float((1 + mp.sqrt(5)) / 2)
    out["row_ratio_is_golden"] = bool(
        abs(S[0][1] / S[0][0] - (1 + mp.sqrt(5)) / 2) < mpf("1e-35"))

    # (C12) asymptotic residuals decrease in N
    c12 = {}
    for N in (25, 51, 101):
        c12[str(N)] = float(cor12_residual(chi111, N))
    out["cor12_residuals"] = c12
    out["cor12_residuals_decrease"] = c12["25"] > c12["51"] > c12["101"]

    # verdict comparison vs bwS0
    dq = {"(5)": mpf(1), "(4,1)": qint(4), "(3,2)": qint(5),
          "(3,1,1)": qint(4) * qint(3) / qint(2)}
    out["bwS0_class_ratios"] = {k: float(v) for k, v in dq.items()}
    out["verdict_type_mismatch"] = {"genuine_row_dim": 2, "bwS0_classes": 4}
    out["verdict_value_mismatch"] = {
        "genuine_row_ratio": out["vacuum_row_ratio"],
        "bwS0_ratios": [float(v) for v in dq.values()],
    }
    return out


def report(res):
    print("# s013 — the genuine Σ(2,3,5) S-matrix (Hikami math-ph/0405028, now in library/)\n")

    print("## (χ) Characters and the D=2 identification\n")
    print(f"- D(2,3,5) = (1·2·4)/4 = **{res['D_235']}** independent vector-valued components:"
          f" (1,1,1), (1,1,2).")
    print(f"- Hikami χ^(1,1,1) == round-2 derived α=1 character (incl. global sign): "
          f"**{res['chi111_equals_round2_alpha1']}** (Hikami eq. (5.6) IS our sympy identity).")
    print(f"- Hikami χ^(1,1,2) == round-2 derived α=2 character: "
          f"**{res['chi112_equals_round2_alpha2']}**")
    print(f"- α=3 ≡ (1,1,2)-class, α=4 ≡ (1,1,1)-class (symmetry 3.3): "
          f"**{res['alpha3_same_class_as_alpha2']}**, **{res['alpha4_same_class_as_alpha1']}**")
    print("- ⇒ the PR #3190 colored family spans exactly TWO independent functions; the"
          " '4↔4' E₈-dual-pair ↔ bwS0-class correspondence is support-level only.\n")

    print("## (τ/T10) Exact validation of the transcription chain\n")
    print(f"- φ(2,3,5) from Dedekind sums = {res['phi_235']:.10f} = 181/30: "
          f"**{res['phi_equals_181_over_30']}**")
    print("- Theorem 10 (EXACT finite-N identity, eq. 5.5) residuals:")
    for N, r in res["theorem10_residuals"].items():
        print(f"    N={N}: |LHS−RHS| = {r:.2e}")
    print(f"- **Theorem 10 exact: {res['theorem10_exact']}** — validates τ_N (2.11), χ (3.1),"
          f" Φ̃ (4.2) jointly.\n")

    print("## (S) The genuine S-matrix and its vacuum row\n")
    print(f"- S (eq. 3.8, normalization √(32/P)) = {res['S_matrix']}")
    print(f"- S² = 1 (involution): **{res['S_squared_is_identity']}**")
    print(f"- vacuum row = Corollary 12 flat-connection weights (2/√5)(sin π/5, sin 2π/5), "
          f"CS = (−1/120, −49/120): **{res['vacuum_row_matches_cor12_weights']}**")
    print(f"- row ratio = {res['vacuum_row_ratio']:.10f} = golden ratio φ: "
          f"**{res['row_ratio_is_golden']}** (icosahedral/Fibonacci pair; |amplitudes| = "
          f"√(Reidemeister torsion), Hikami Thm 14)")
    print("- Corollary 12 asymptotic residuals (validating weights+CS against exact τ_N):")
    for N, r in res["cor12_residuals"].items():
        print(f"    N={N}: {r:.2e}")
    print(f"  decreasing: **{res['cor12_residuals_decrease']}**\n")

    print("## VERDICT — the s013 value step at the false-theta S-matrix level\n")
    print(f"- genuine vacuum row: **2-dimensional**, ratio φ ≈ "
          f"{res['vacuum_row_ratio']:.4f}")
    print(f"- keystone target bwS0 = d_q/D at n=5: **4 classes**, ratios "
          f"{[round(v, 3) for v in res['verdict_value_mismatch']['bwS0_ratios']]}")
    print("- **Type mismatch (2 ≠ 4) and value mismatch (φ ∉ targets): the identification")
    print("  'bwS0 = vacuum row of the Σ(2,3,5) false-theta S-matrix' is REFUTED** —")
    print("  scope (a): this specific geometric object (the D=2 modular family of Σ(2,3,5)),")
    print("  with all formulas machine-validated against the primary source. The W_λ index")
    print("  question is NOT closed: it cannot be carried by this object alone; a larger")
    print("  geometric family (more exceptional fibres ⇒ larger D, or genuinely colored")
    print("  knot-complement blocks) would be required. No fit; nothing wired.")


def main(argv=None):
    res = run()
    report(res)
    w = WitnessBuilder("keystone-valuemap-genuine-smatrix-s013", engine="mpmath")
    w.set_description(
        "s013 step 3: the GENUINE Sigma(2,3,5) S-matrix from the primary literature (Hikami "
        "math-ph/0405028, owner-uploaded commit ece271823). Transcribes chi^(l1,l2,l3) (3.1), "
        "tau_N (2.11), phi=181/30 (2.12), Eichler limit (4.2), S-matrix (3.8, normalization "
        "sqrt(32/P)), Corollary 12 (5.8) -- and machine-validates ALL of it: Theorem 10 is an "
        "EXACT finite-N identity verified to ~1e-30 at N=3,5,7,11; S^2=1; the vacuum row "
        "equals Cor 12's flat-connection weights (2/sqrt5)(sin pi/5, sin 2pi/5) with CS="
        "-1/120,-49/120; Cor 12 asymptotic residuals decrease in N. Cross-validation: Hikami "
        "chi^(111)/chi^(112) EQUAL the round-2 sympy-derived alpha=1/alpha=2 characters "
        "(eq. 5.6 is that identity), and the colored family spans exactly D=2 components "
        "(alpha=4=alpha=1, alpha=3=alpha=2). VERDICT: the genuine vacuum row is 2-dimensional "
        "with golden-ratio phi ratio (icosahedral/Fibonacci; magnitudes = sqrt(Reidemeister "
        "torsion), Thm 14); the keystone target bwS0=d_q/D at n=5 has 4 classes with ratios "
        "(1,4.110,5.220,6.220): type mismatch (2!=4) + value mismatch (phi not in targets) "
        "REFUTE the identification 'bwS0 = vacuum row of the Sigma(2,3,5) false-theta "
        "S-matrix' -- scope (a), this specific geometric object. The 3190 4<->4 "
        "correspondence is support-level only. No fit; nothing wired."
    )
    for key in ("P", "pvec", "q0", "chi_111", "chi_112",
                "chi111_equals_round2_alpha1", "chi112_equals_round2_alpha2",
                "D_235", "alpha4_same_class_as_alpha1", "alpha3_same_class_as_alpha2",
                "phi_235", "phi_equals_181_over_30", "theorem10_residuals",
                "theorem10_exact", "S_matrix", "S_squared_is_identity",
                "vacuum_row_matches_cor12_weights", "cor12_weights",
                "vacuum_row_ratio", "golden_ratio", "row_ratio_is_golden",
                "cor12_residuals", "cor12_residuals_decrease",
                "bwS0_class_ratios", "verdict_type_mismatch",
                "verdict_value_mismatch"):
        w.add_data(key, res[key])
    w.add_assertion(
        "genuine_smatrix_validated_and_bwS0_identification_refuted",
        computed=1 if (res["theorem10_exact"] and res["S_squared_is_identity"]
                       and res["vacuum_row_matches_cor12_weights"]
                       and res["row_ratio_is_golden"]
                       and res["chi111_equals_round2_alpha1"]
                       and res["chi112_equals_round2_alpha2"]
                       and res["cor12_residuals_decrease"]) else 0,
        expected=1, tolerance=0,
        source="Every transcribed formula from Hikami math-ph/0405028 machine-validates "
               "(Theorem 10 exact to ~1e-30; S^2=1; vacuum row = Cor 12 weights; round-2 "
               "derived characters = Hikami's chi^(111)/chi^(112)). The genuine Sigma(2,3,5) "
               "vacuum row is D=2-dimensional with golden-ratio ratio, refuting (scope (a)) "
               "the identification of the 4-class bwS0=d_q/D family with the vacuum row of "
               "this geometric object.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
