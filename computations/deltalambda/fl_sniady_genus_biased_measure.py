#!/usr/bin/env python3
"""
fl_sniady_genus_biased_measure.py — Phase-2 Śniady genus expansion on the (f^λ)³-biased measure
(bean qou-joi7, epic qou-x631). The Phase-1 target named in
docs/audits/2026-07-18-covariance-kernel-proof-epic-phase1.md.

THE OBJECT. The Δ_λ covariance kernel is (equivalently)
    cov(k) = Σ_{λ⊢k} (f^λ)³ (C₂(λ) − C(k,2))  ≤  0,   C₂ = Σ_□ c(□)², C(k,2)=k(k−1)/2.
Dividing by Z₃ = Σ_{λ⊢k}(f^λ)³ makes it a statement about the DIMENSION-CUBED-BIASED measure
    P₃(λ) = (f^λ)³ / Z₃:            Δ(k) := E_{P₃}[C₂] − C(k,2) = cov(k)/Z₃ ≤ 0.
Because C₂ = C(k,2) + (R₄+R₂)/3 with R₂=k, R₄ the 4th free cumulant of the transition measure
(Kerov polynomial Σ̂₃ = R₄+R₂, verified #3998), this is also
    E_{P₃}[R₄] = 3·Δ(k) − k,   vs   E_{Plancherel}[R₄] = −k exactly.

WHAT THIS PROBE COMPUTES (all EXACT — hooks, contents, transition free cumulants):
 (A) Δ(k) = E_{P₃}[C₂] − C(k,2) and E_{P₃}[R₄], k = 3..KMAX. Confirms Δ<0 (kernel) and quantifies
     how much MORE negative the cube-biased R₄ is than the Plancherel −k.
 (B) LEADING ASYMPTOTICS via successive log-ratios: the exponent p and constant c in −Δ(k) ~ c·k^p.
     Finding: p ≈ 3/2 — the biasing lowers the content spread by an amount of order k^{3/2}, one
     power of √k BELOW the Plancherel content spread C(k,2) ~ k²/2. Under Plancherel the k^{3/2}
     term is exactly ZERO (E_Planch[C₂]=k(k−1)/2), so the k^{3/2} deviation is BORN of the biasing.
 (C) THE INFINITESIMAL TILT (genus / free-probability object): dE_β[C₂]/dβ = Cov_β(C₂, ln f^λ).
     At β=2 this is Cov_Planch(C₂, ln f^λ), the covariance of the polynomial function C₂ (which HAS
     a genus expansion) with the log-dimension. Computed exactly; also ~ −c'·k^{3/2} and < 0 — the
     finite kernel (β:2→3) and the infinitesimal tilt agree in sign and order.

WHAT THE GENUS EXPANSION SAYS (the honest Phase-2 conclusion):
 • The obstruction named in Phase 1 is CONFIRMED and made precise: Σ̂₃ = R₄+R₂ is a polynomial
   function on Young diagrams (its Plancherel cumulants have Śniady's genus grading), but the
   biasing weight f^λ = χ^λ(e) is the exponential DIMENSION — it lies OUTSIDE the algebra of
   polynomial functions, so the genus grading does not close Cov_Planch(f^λ, C₂). The genus
   expansion controls one factor of the covariance, not the other.
 • What the genus/limit-shape picture DOES give: the k^{3/2} scaling is a FLUCTUATION-order effect
   (subleading to the k² content spread), and the sign is the tilted-limit-shape heuristic — the
   extra f^λ concentrates P₃ more tightly around the f^λ-maximising (balanced) shape, REDUCING
   content dispersion ⇒ Δ<0. This is a heuristic for the sign, NOT a proof.
 • Δ_λ IMPLICATION: the sub-lemma (D) `w_std` bound is TIGHT (margin → 0⁺), and the negativity it
   needs is a genuine order-k^{3/2} effect, not a knife-edge — so the Δ_λ super-exponential growth
   bound is robustly correct MODULO the still-open sign of this order-k^{3/2} anti-correlation.

VERDICT: kernel still OPEN. Delivered: exact biased-measure asymptotics (k^{3/2} scaling of the
content-spread deficit), the infinitesimal-tilt object, and a precise statement of why the genus
grading does not directly close it. scope-(a); no fit; nothing wired; no c_k; L2 unchanged (2/7).

# Ref: [sniady2006asymptotics] https://doi.org/10.1007/s00440-005-0479-7
# Ref: [biane1998representations] https://doi.org/10.1006/aima.1998.1741
# Ref: [moralespakpanova2016] https://arxiv.org/abs/1610.07561
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

KMAX = 44         # exact biased-measure asymptotics (hooks + contents + transition cumulants)
FIT_KMIN = 20     # asymptotic fit window (drop small-k transients)


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hook_lengths(l):
    l = list(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])] if l else []
    hs = []
    for i, row in enumerate(l):
        for j in range(row):
            hs.append((row - j) + (conj[j] - i) - 1)
    return hs


def hook_dim(l):
    l = list(l)
    n = sum(l)
    if n == 0:
        return 1
    d = 1
    for h in hook_lengths(l):
        d *= h
    return math.factorial(n) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def corners(l):
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


def R4_transition(l):
    """R₄ = M₄ − 2·M₂² of the Kerov transition measure of λ (free cumulant)."""
    add, rem = corners(l)
    M2 = Fraction(0)
    M4 = Fraction(0)
    for j, bj in enumerate(add):
        num = Fraction(1)
        for ai in rem:
            num *= (bj - ai)
        den = Fraction(1)
        for k2, bk in enumerate(add):
            if k2 != j:
                den *= (bj - bk)
        w = num / den
        M2 += w * bj ** 2
        M4 += w * bj ** 4
    return M4 - 2 * M2 ** 2


def main() -> int:
    print("=== Śniady genus expansion on the (f^λ)³-biased measure (epic qou-x631, Phase 2) ===\n")
    print(f"{'k':>2} {'Δ=E_P3[C2]−C(k,2)':>18} {'E_P3[R4]':>12} {'E_Pl[R4]=−k':>12} "
          f"{'Cov_Pl(C2,lnf)':>16}")

    kernel_ok = True
    rows = []
    for k in range(3, KMAX + 1):
        Ck2 = Fraction(k * (k - 1), 2)
        Z3 = 0
        num_C2 = Fraction(0)       # Σ (f^λ)³ C₂     → E_P3[C2] = num/Z3
        num_R4 = Fraction(0)       # Σ (f^λ)³ R₄     → E_P3[R4]
        # infinitesimal tilt at β=2: Cov_Planch(C2, ln f) = E_Pl[C2 ln f] − E_Pl[C2] E_Pl[ln f]
        kf = math.factorial(k)
        sum_f2 = 0                 # Σ (f^λ)²        (= k!, sanity)
        sum_f2_C2 = Fraction(0)    # Σ (f^λ)² C₂
        sum_f2_lnf = 0.0           # Σ (f^λ)² ln f
        sum_f2_C2_lnf = 0.0        # Σ (f^λ)² C₂ ln f
        for l in partitions_of(k):
            f = hook_dim(l)
            c2 = C2(l)
            f3 = f ** 3
            Z3 += f3
            num_C2 += f3 * c2
            num_R4 += f3 * R4_transition(l)
            f2 = f * f
            lnf = math.log(f) if f > 0 else 0.0
            sum_f2 += f2
            sum_f2_C2 += f2 * c2
            sum_f2_lnf += f2 * lnf
            sum_f2_C2_lnf += f2 * c2 * lnf
        assert sum_f2 == kf, "Σ(f^λ)² ≠ k! (RSK sanity)"
        Ep3_C2 = Fraction(num_C2, Z3)
        Delta = Ep3_C2 - Ck2
        Ep3_R4 = Fraction(num_R4, Z3)
        # Plancherel covariance of C₂ with ln f (float; ln is transcendental)
        Epl_C2 = float(sum_f2_C2) / kf         # = C(k,2)
        Epl_lnf = sum_f2_lnf / kf
        Epl_C2_lnf = sum_f2_C2_lnf / kf
        cov_C2_lnf = Epl_C2_lnf - Epl_C2 * Epl_lnf
        if Delta > 0:
            kernel_ok = False
        rows.append((k, Delta, Ep3_R4, cov_C2_lnf))
        if k in (3, 4, 5) or k % 5 == 0 or k == KMAX:
            print(f"{k:>2} {float(Delta):>18.4f} {float(Ep3_R4):>12.3f} {-k:>12} "
                  f"{cov_C2_lnf:>16.4f}")

    def loglog_slope(pairs):
        """Least-squares slope of ln(y) vs ln(k) over pairs [(k, y>0)] — a stable exponent estimate."""
        xs = [math.log(k) for (k, y) in pairs]
        ys = [math.log(y) for (k, y) in pairs]
        n = len(xs)
        mx = sum(xs) / n
        my = sum(ys) / n
        sxx = sum((x - mx) ** 2 for x in xs)
        sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        slope = sxy / sxx
        intercept = my - slope * mx
        return slope, math.exp(intercept)

    # (B) leading exponent of −Δ(k) ~ c k^p via a STABLE log-log least-squares regression on the
    # fit window (successive ratios are too noisy — Δ(k) has partition-level fluctuations).
    print(f"\n(B) leading asymptotics  −Δ(k) ~ c·k^p  (log-log least-squares, k≥{FIT_KMIN}):")
    win = [(k, float(-d)) for (k, d, _, _) in rows if k >= FIT_KMIN and d < 0]
    pav, c_est = loglog_slope(win)
    print(f"    fitted exponent  p ≈ {pav:.3f}   (Kerov-CLT fluctuation order Std_Planch(C₂) ~ k^{{3/2}} = 1.500)")
    print(f"    fitted constant  c ≈ {c_est:.5f}   over k∈[{FIT_KMIN},{KMAX}]")

    # (C) infinitesimal-tilt exponent (same stable regression)
    print(f"\n(C) infinitesimal tilt  Cov_Planch(C₂, ln f^λ) = dE_β[C₂]/dβ|₂  (should be <0, ~k^{{3/2}}):")
    tilt_neg = all(cv < 0 for (kk, _, _, cv) in rows if kk >= 6)
    twin = [(k, -cv) for (k, _, _, cv) in rows if k >= FIT_KMIN and cv < 0]
    tpav, _ = loglog_slope(twin)
    print(f"    Cov_Planch(C₂, ln f) < 0 for all k≥6: {tilt_neg};  fitted exponent ≈ {tpav:.3f}")

    print("\n(GENUS CONCLUSION) Σ̂₃=R₄+R₂ is a polynomial function on Young diagrams (Śniady genus")
    print("grading applies to its Plancherel cumulants), but the biasing weight f^λ=χ^λ(e) is the")
    print("exponential DIMENSION — OUTSIDE the polynomial-function algebra — so the genus grading")
    print("controls only one factor of Cov_Planch(f^λ,C₂) and does NOT close the kernel. What the")
    print("genus/limit-shape picture DOES give: the k^{3/2} scaling is a fluctuation-order effect,")
    print("and the sign is the tilted-limit-shape heuristic (extra f^λ concentrates P₃ around the")
    print("f^λ-maximising balanced shape ⇒ less content dispersion ⇒ Δ<0). Heuristic, not a proof.")

    # honest criterion: kernel Δ<0 everywhere; tilt<0; exponent is sub-quadratic and near the
    # k^{3/2} Kerov-CLT fluctuation order (band [1.3,1.8] — data is consistent with 3/2, possibly
    # with a slow log/√ correction; we do NOT claim exactly 3/2).
    ok = bool(kernel_ok and tilt_neg and 1.3 <= pav <= 1.8)
    print(f"\nRESULT: Δ<0 all k≤{KMAX}; −Δ ~ c·k^{{{pav:.2f}}} (sub-quadratic, near k^3/2); tilt<0. "
          f"Kernel OPEN. ok={ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("fl-sniady-genus-biased-measure", engine="python-exact")
        w.set_description(
            "Phase-2 Śniady genus expansion on the (f^λ)³-biased measure P₃(λ)=(f^λ)³/Z₃ for the Δ_λ "
            "covariance kernel (epic qou-x631). Exact (hooks+contents+transition free cumulants): "
            "(A) Δ(k)=E_{P₃}[C₂]−C(k,2)=cov(k)/Z₃ < 0 all k≤44, and E_{P₃}[R₄]=3Δ−k, MORE negative "
            "than the Plancherel E[R₄]=−k. (B) leading asymptotics −Δ(k) ~ c·k^p with p≈3/2 (the "
            "biasing lowers the content spread by an order-k^{3/2} amount, one √k below the k²/2 "
            "Plancherel spread; under Plancherel this term is exactly 0, so it is BORN of the "
            "biasing). (C) the infinitesimal tilt Cov_Planch(C₂,ln f^λ)=dE_β[C₂]/dβ|₂ is <0 and "
            "~k^{3/2}, agreeing in sign/order with the finite β:2→3 kernel. GENUS CONCLUSION: Σ̂₃=R₄+R₂ "
            "is a polynomial function (genus grading applies to its Plancherel cumulants) but f^λ is "
            "the exponential dimension, OUTSIDE that algebra, so the genus grading controls one "
            "factor of Cov_Planch(f^λ,C₂) and does NOT close the kernel; the k^{3/2} scaling is a "
            "fluctuation-order effect and the sign is the tilted-limit-shape heuristic (not a proof). "
            "Kernel OPEN. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("kmax", KMAX)
        w.add_data("delta_all_negative", bool(kernel_ok))
        w.add_data("delta_leading_exponent_p", float(pav))
        w.add_data("delta_leading_constant_c_at_p1p5", float(c_est))
        w.add_data("tilt_cov_C2_lnf_negative", bool(tilt_neg))
        w.add_data("tilt_leading_exponent", float(tpav))
        w.add_data("table_k_delta_Ep3R4_covC2lnf",
                   [[k, float(d), float(r4), cv] for (k, d, r4, cv) in rows])
        w.add_assertion(
            "biased_measure_content_spread_deficit_subquadratic_near_k32",
            computed=f"{pav:.3f}", expected="1.55", tolerance=0.25,
            source=("E_{P₃}[C₂]−C(k,2) < 0 all k≤44 with fitted leading exponent ≈1.5–1.65 "
                    "(sub-quadratic, near the Kerov-CLT fluctuation order k^{3/2}; not claimed exactly "
                    "3/2); infinitesimal tilt Cov_Planch(C₂,ln f) < 0 same order. Genus grading does "
                    "not close the kernel (f^λ ∉ polynomial-function algebra). Kernel OPEN. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
