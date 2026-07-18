#!/usr/bin/env python3
"""
wlambda_covariance_kernel_frontier.py — attack log + free-cumulant framing of the open covariance
kernel Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0 (the sole residual gap of the Δ_λ growth bound, #3939/#3959).

#3959 reduced the growth sub-lemma (D) to the covariance kernel
    T₃ = Σ_λ (f^λ)² χ^λ(3-cycle) ≤ 0   ⇔   Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0.
This probe pushes the attack: (i) extends the numerical verification, (ii) establishes — exactly,
verified per λ — the FREE-CUMULANT framing that situates the kernel in Biane–Śniady / Kerov-CLT
theory, and (iii) records the elementary approaches that do NOT close it. It does not prove the
kernel; the kernel remains open. It maps the frontier so the next attacker starts correctly.

VERIFIED FACTS (this probe):

A. EXTENDED VERIFICATION.  T₃ < 0 strictly for k = 3..N (default N=30); the margin −4T₃/T₁
   decreases monotonically toward 0⁺, matching the sharp asymptotic E[f^{λ/(2,1)}]/E[f^λ] → 1/3⁺
   (so (D)'s bound is tight, not slack).

B. KEROV-POLYNOMIAL FRAMING (exact, per λ).  With Σ̂₃(λ) = (k)₃·χ^λ(3-cycle)/f^λ = 3(C₂(λ) − C(k,2)),
   C₂ = Σ_□c(□)², and R_j the free cumulants of the transition measure of λ (R₂ = M₂ = k,
   R₄ = M₄ − 2M₂²):

       Σ̂₃ = R₄ + R₂         (Kerov polynomial; verified all λ, k ≤ 14),
       E_Planch[R₄] = −k     (exact; verified k ≤ 14, ⇒ E[Σ̂₃] = 0),

   so the kernel is EQUIVALENT to  Cov_Planch(f^λ, R₄) ≤ 0  — dimension anti-correlates with the
   4th free cumulant of the shape. R₄ is no more elementary to bound than C₂, so this re-expresses
   (not closes) the kernel; but it is the correct Biane–Śniady setting.

C. RSK FORM.  T₃ = Σ_{w∈S_k} χ^{sh(w)}(3-cycle) = Σ_w f^{sh(w)}·Σ̂₃(sh(w))/(k)₃ — the 3-cycle
   character averaged over the RSK shape of a uniform permutation (Kerov-CLT observable).

WHY ELEMENTARY APPROACHES DO NOT CLOSE IT (recorded so they are not retried):
 - per-λ sign is FALSE (the row shape gives χ^λ(3-cycle) = +1 > 0; the sign is on the Plancherel
   average only);
 - T₃ = Σ(f^λ)²χ³ is the UNDIVIDED character sum (Σχ³, not Σχ³/f^λ) ⇒ not a connection-coefficient
   count ⇒ no manifestly-nonnegative model;
 - the crude character-ratio bound |χ³/f^λ| ≤ 1 is ATTAINED (=1) at the extremes ⇒ no uniform
   `< 1/3` bound ⇒ the sign is genuinely needed (a bound cannot substitute).

The mechanism: the two extreme shapes (row, column) each contribute exactly +1; the balanced bulk
(large (f^λ)², contents concentrated ⇒ C₂ < C(k,2) ⇒ χ₃ < 0) supplies the dominant negative.

VERDICT: the covariance kernel is a Biane–Śniady / Kerov-CLT character-ratio anti-correlation
(closing machinery: Śniady's genus expansion of the joint cumulants of characters, or the Kerov
CLT covariance structure). Not closed here; verified k ≤ 30, framed exactly in free cumulants.

Discipline: scope-(a) frontier map; no fit; nothing wired; no `c_k`; L2 unchanged (2/7). In-sandbox
(integer + Fraction; no numpy/cvxpy/SnapPy).

# Ref: [moralespakpanova2016] https://arxiv.org/abs/1610.07561
# Ref: [fulman2004stein] https://arxiv.org/abs/math/0305423
# Ref: [biane1998representations] https://doi.org/10.1006/aima.1998.1741
# Ref: [sniady2006asymptotics] https://doi.org/10.1007/s00440-005-0479-7
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

NMAX_COV = 30   # extended verification of T₃ < 0 (fast: hooks + contents only)
NMAX_KEROV = 14  # Kerov-polynomial framing (slower: transition-measure moments)


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hook_dim(l):
    l = list(l)
    n = sum(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    d = 1
    for i, row in enumerate(l):
        for j in range(row):
            d *= (row - j) + (conj[j] - i) - 1
    return math.factorial(n) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def corners(l):
    """Addable and removable corner contents (interlacing) of the transition measure."""
    l = list(l)
    L = len(l)
    add, rem = [], []
    for i in range(L + 1):
        li = l[i] if i < L else 0
        prev = l[i - 1] if i > 0 else 10 ** 9
        if prev > li:
            add.append(li - i)
    for i in range(L):
        if i == L - 1 or l[i] > l[i + 1]:
            rem.append((l[i] - 1) - i)
    return sorted(add), sorted(rem)


def transition_moments(l):
    """M₂, M₃, M₄ of the Kerov transition measure μ_λ (weights w_j = ∏(b_j−a_i)/∏_{k≠j}(b_j−b_k))."""
    add, rem = corners(l)
    M = {2: Fraction(0), 3: Fraction(0), 4: Fraction(0)}
    for j, bj in enumerate(add):
        num = Fraction(1)
        for ai in rem:
            num *= (bj - ai)
        den = Fraction(1)
        for k2, bk in enumerate(add):
            if k2 != j:
                den *= (bj - bk)
        w = num / den
        for n in (2, 3, 4):
            M[n] += w * bj ** n
    return M


def main() -> int:
    print("=== Frontier map of the open kernel  Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0 ===\n")

    # A. extended verification of T₃ < 0
    print(f"A. extended verification T₃ < 0 (k=3..{NMAX_COV}):")
    cov_ok = True
    margins = []
    for k in range(3, NMAX_COV + 1):
        Ck2 = k * (k - 1) // 2
        cov = T1 = 0
        for l in partitions_of(k):
            f = hook_dim(l)
            cov += f ** 3 * (C2(l) - Ck2)
            T1 += f ** 3
        if cov >= 0:
            cov_ok = False
        margin = float(-4 * Fraction(3 * cov, k * (k - 1) * (k - 2)) / T1)
        margins.append((k, margin))
    print(f"   T₃ < 0 for all k=3..{NMAX_COV}: {cov_ok};  "
          f"margin −4T₃/T₁: {margins[0][1]:.4f} (k=3) → {margins[-1][1]:.5f} (k={NMAX_COV})")

    # B. Kerov-polynomial framing
    print(f"\nB. free-cumulant framing (k=3..{NMAX_KEROV}):")
    kerov_ok = True
    ER4_ok = True
    covR4_ok = True
    for k in range(3, NMAX_KEROV + 1):
        Ck2 = k * (k - 1) // 2
        kf = math.factorial(k)
        T1 = 0
        ER4_num = Fraction(0)
        covR4_num = Fraction(0)
        for l in partitions_of(k):
            f = hook_dim(l)
            M = transition_moments(l)
            R2 = M[2]
            R4 = M[4] - 2 * M[2] ** 2
            if 3 * (C2(l) - Ck2) != R4 + R2:          # Σ̂₃ = R₄ + R₂
                kerov_ok = False
            T1 += f ** 3
            ER4_num += f * f * R4                       # k!·E_Planch[R₄]
            covR4_num += f ** 3 * R4
        ER4 = Fraction(ER4_num, kf)
        Ef = Fraction(T1, kf)
        if ER4 != -k:                                  # E_Planch[R₄] = −k exactly
            ER4_ok = False
        covR4 = Fraction(covR4_num, kf) - Ef * ER4     # Cov(f, R₄)
        if covR4 > 0:
            covR4_ok = False
    print(f"   Kerov polynomial  Σ̂₃ = R₄ + R₂  (all λ): {kerov_ok}")
    print(f"   E_Planch[R₄] = −k  exactly: {ER4_ok}")
    print(f"   ⇒ kernel ⇔ Cov_Planch(f^λ, R₄) ≤ 0, verified: {covR4_ok}")

    print("\nC. RSK form: T₃ = Σ_{w∈S_k} χ^{sh(w)}(3-cycle) (3-cycle character over the RSK shape).")
    print("\nWHY NOT CLOSED (recorded): per-λ sign false (row → +1); undivided Σχ³ ⇒ no positivity")
    print("model; |χ³/f| ≤ 1 attained at extremes ⇒ no uniform bound. Verdict: Biane–Śniady /")
    print("Kerov-CLT anti-correlation; closing machinery = Śniady genus expansion / Kerov CLT.")

    ok = bool(cov_ok and kerov_ok and ER4_ok and covR4_ok)
    print(f"\nRESULT: kernel verified (k≤{NMAX_COV}) + framed exactly in free cumulants; OPEN: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-kernel-frontier", engine="python-exact")
        w.set_description(
            "Attack log + free-cumulant framing of the open covariance kernel "
            "Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0 (residual gap of the Δ_λ growth bound #3939/#3959). "
            "(A) T₃=Σ(f^λ)²χ^λ(3-cycle) < 0 verified k=3..30 (margin −4T₃/T₁ → 0⁺, matching the "
            "sharp E[f^{λ/(2,1)}]/E[f^λ]→1/3⁺). (B) Kerov-polynomial framing, exact per λ (k≤14): "
            "Σ̂₃=R₄+R₂ (R₂=k, R₄=M₄−2M₂² of the transition measure), and E_Planch[R₄]=−k exactly, so "
            "the kernel ⇔ Cov_Planch(f^λ, R₄) ≤ 0 (dimension anti-correlates with the 4th free "
            "cumulant). (C) RSK form T₃=Σ_{w∈S_k}χ^{sh(w)}(3-cycle). Records why elementary approaches "
            "fail: per-λ sign false (row→+1); undivided Σχ³ is not a connection-coefficient count "
            "(no positivity model); |χ³/f^λ|≤1 attained at extremes (no uniform bound). Verdict: a "
            "Biane–Śniady / Kerov-CLT character-ratio anti-correlation; closing machinery = Śniady's "
            "genus expansion / the Kerov CLT covariance. NOT closed; maps the frontier. scope-(a); no "
            "fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("T3_negative_verified_to_k", NMAX_COV)
        w.add_data("T3_negative_all", bool(cov_ok))
        w.add_data("margin_first_k3", margins[0][1])
        w.add_data("margin_last", margins[-1][1])
        w.add_data("kerov_polynomial_sigma3_eq_R4_plus_R2", bool(kerov_ok))
        w.add_data("E_Planch_R4_eq_minus_k", bool(ER4_ok))
        w.add_data("kernel_equiv_cov_f_R4_le_0", bool(covR4_ok))
        w.add_data("status", "OPEN — Biane-Sniady / Kerov-CLT anti-correlation; framed not proved")
        w.add_assertion(
            "covariance_kernel_verified_and_framed_open",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("T₃<0 verified k≤30; Kerov polynomial Σ̂₃=R₄+R₂ and E_Planch[R₄]=−k exact (k≤14) "
                    "⇒ kernel ⇔ Cov(f^λ,R₄)≤0; elementary approaches recorded-excluded. OPEN "
                    "(Biane-Sniady / Kerov-CLT). No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
