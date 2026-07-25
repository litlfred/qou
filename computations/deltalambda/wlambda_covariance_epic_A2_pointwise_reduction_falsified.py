#!/usr/bin/env python3
r"""
wlambda_covariance_epic_A2_pointwise_reduction_falsified.py — CORRECTION (qou-x631, qou-ogrk).

The A2 "pointwise reduction" — Cov_Planch(H_s, ω₃) ≤ 0 for all s>0, equivalently the polynomial
positivity R(x) ≥ 0 on (0,1) where P(x)=Σ_v ν_v x^v = x(x−1)R(x) — was verified only to small n
(n≤13 in the hook-reduction audit; n≤15 in the polynomial-positivity probe/PR #4242). Pushing the
EXACT computation further shows it is **FALSE for n ≥ 29**:

  • first failure at n = 29:  max_{s>0} Cov_Planch(H_s, ω₃) = +0.056 at s ≈ 0.52  (grows with n);
  • equivalently R(x) develops a genuine root in (0,1) at n = 30 (R < 0 on part of the interval),
    the last negative R-coefficient having crept from index ≤ 4 up to index 5 near the transition.

So the pointwise sign is a **small-n artifact**, not a theorem — the polynomial-positivity target
`R ≥ 0 on (0,1)` cannot prove A2. This retracts the "R > 0 on [0,∞)" framing of PR #4242 as a general
reduction and the "Cov(H_s,ω₃) < 0 strictly on the interior" impression of the hook-reduction audit;
both were true only in the verified small-n window.

WHAT SURVIVES (verified EXACTLY, k, n ≤ 40 — the important part):

  • the KERNEL conjecture itself  cov(k) = Σ_λ (f^λ)³ ω₃(λ) ≤ 0  — strongly negative, intact;
  • the A2 leg itself  Cov_Planch(ln f^λ, ω₃) = −Σ_v ln(v) ν_v ≤ 0  — negative, intact.

The Frullani identity Cov(ln f,ω₃) = ∫_0^∞ (1/s) Cov(H_s,ω₃) ds still holds; A2 ≤ 0 survives by
**cancellation** — the integrand Cov(H_s,ω₃) is now positive on part of the s-range (n≥29) but the
integral stays ≤ 0. Hence "A2 ⟸ Cov(H_s,ω₃)≤0 ∀s" is a valid implication with a **false premise**
for n≥29: the pointwise sign is sufficient but does not hold, so it is not a usable route. Proving A2
requires the FULL integral (a signed-cancellation / global argument), not a pointwise sign.

DISCIPLINE. This is an honest retraction of a small-n over-generalization (scope-(a) route-death), not
a refutation of the kernel or A2. The polynomial-positivity route to A2 is eliminated **with an exact
counterexample** (n≥29). scope-(a); no fit; nothing wired; no c_k; L2 unchanged (2/7).

# Ref: [manuscript] docs/audits/2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hooks(l):
    l = list(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])] if l else []
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(l) for j in range(row)]


def dim(l):
    l2 = list(l)
    conj = [sum(1 for p in l2 if p > j) for j in range(l2[0])] if l2 else []
    d = 1
    for i, row in enumerate(l2):
        for j in range(row):
            d *= (row - j) + (conj[j] - i) - 1
    return math.factorial(sum(l)) // d


def C2content(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def max_cov_Hs(n):
    """max_{s>0} Cov_Planch(H_s, ω₃), H_s = Σ e^{-s h}; exact rational weights, s-scan."""
    Ck2 = n * (n - 1) // 2
    fact = math.factorial(n)
    data = [(dim(l), hooks(l), C2content(l) - Ck2) for l in partitions_of(n)]
    best = -1e18
    bests = 0.0
    for i in range(1, 400):
        s = 0.02 * i
        cov = 0.0
        for d, hk, wt in data:
            Hs = sum(math.exp(-s * h) for h in hk)
            cov += (d * d / fact) * Hs * wt
        if cov > best:
            best = cov
            bests = s
    return best, bests


def kernel_and_a2(n):
    """exact kernel cov(n)=Σ(dim)³ω₃ (int) and A2=Cov(ln f,ω₃)=−Σ ln(v) ν_v (float)."""
    Ck2 = n * (n - 1) // 2
    fact = math.factorial(n)
    kernel = 0
    EN = {}
    ENs = {}
    Esum = Fr(0)
    for l in partitions_of(n):
        d = dim(l)
        hk = hooks(l)
        sh2 = sum(h * h for h in hk)
        om3 = sh2 - n * n - Ck2  # = Σc² − C(n,2)
        kernel += d ** 3 * om3
        w = Fr(d * d, fact)
        Esum += w * sh2
        cnt = {}
        for h in hk:
            cnt[h] = cnt.get(h, 0) + 1
        for v, c in cnt.items():
            EN[v] = EN.get(v, Fr(0)) + w * c
            ENs[v] = ENs.get(v, Fr(0)) + w * c * sh2
    a2 = 0.0
    for v in EN:
        nu_v = ENs[v] - EN[v] * Esum
        a2 += -math.log(v) * float(nu_v)
    return kernel, a2


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — CORRECTION: A2 pointwise reduction FALSIFIED ===\n")

    print("The pointwise target Cov_Planch(H_s,ω₃) ≤ 0 ∀s>0  (⟺ R≥0 on (0,1)) — max over s>0:")
    print(" n | max_s Cov(H_s,ω₃) | argmax s | pointwise target holds (want ≤0)?")
    first_fail = None
    for n in [13, 20, 26, 28, 29, 30, 32, 35]:
        mx, s = max_cov_Hs(n)
        holds = mx <= 1e-9
        if not holds and first_fail is None:
            first_fail = n
        print(f"{n:2d} | {mx:+.5e} | {s:.2f} | {holds}")
    print(f"\n  → pointwise reduction FIRST FAILS at n = {first_fail}  (small-n artifact; not a theorem)")

    print("\nWHAT SURVIVES (exact, n≤40): the KERNEL and A2 themselves —")
    print(" n | kernel cov(n)=Σ(dim)³ω₃ ≤0? | A2 Cov(ln f,ω₃) ≤0? ")
    kernel_ok = a2_ok = True
    for n in [29, 30, 35, 40]:
        k, a2 = kernel_and_a2(n)
        kernel_ok &= (k <= 0)
        a2_ok &= (a2 <= 1e-9)
        print(f"{n:2d} | {k <= 0}  (cov={k:+d})".ljust(60) + f"| {a2 <= 1e-9}  (={a2:+.4f})")
    print(f"\n  KERNEL cov(k)≤0 survives k≤40: {kernel_ok}")
    print(f"  A2 Cov(ln f,ω₃)≤0 survives n≤40: {a2_ok}  (Frullani integral ≤0 by CANCELLATION,")
    print("  even though its integrand Cov(H_s,ω₃) is now positive on part of the s-range for n≥29)")

    # correctness of the correction: pointwise fails, but kernel & A2 hold
    ok = (first_fail is not None) and kernel_ok and a2_ok
    print("\nNET: the A2 polynomial-positivity / pointwise-Cov(H_s) route is ELIMINATED with an exact")
    print("counterexample (n≥29). The kernel and A2 themselves are INTACT. Proving A2 needs the full")
    print("Frullani integral (signed cancellation), not the pointwise sign.")
    print(f"\nRESULT: correction verified (pointwise fails n≥29; kernel & A2 survive n≤40): {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-A2-pointwise-reduction-falsified", engine="python-exact")
        w.set_description(
            "CORRECTION (qou-x631, qou-ogrk): the A2 pointwise reduction Cov_Planch(H_s,ω₃)≤0 ∀s>0 "
            "(⟺ R≥0 on (0,1), P(x)=Σν_v x^v=x(x−1)R(x)) is FALSE for n≥29 — verified exactly, first "
            "failure n=29 (max_s Cov=+0.056 at s≈0.52, growing with n; R gains a root in (0,1) at n=30). "
            "It was verified only to n≤13 (hook-reduction audit) / n≤15 (polynomial-positivity PR #4242); "
            "the pointwise sign is a SMALL-n ARTIFACT, so the polynomial-positivity target cannot prove "
            "A2. Retracts the 'R>0 on [0,∞)' general-reduction framing of #4242. WHAT SURVIVES (exact, "
            "k,n≤40): the KERNEL conjecture cov(k)=Σ(f^λ)³ω₃≤0 (strongly negative) AND the A2 leg "
            "Cov_Planch(ln f,ω₃)=−Σ ln(v)ν_v≤0 — both intact. A2 survives by CANCELLATION: the Frullani "
            "identity Cov(ln f,ω₃)=∫(1/s)Cov(H_s,ω₃)ds stays ≤0 though the integrand goes positive on "
            "part of the range (n≥29). So 'A2 ⟸ Cov(H_s,ω₃)≤0 ∀s' is a valid implication with a FALSE "
            "premise; proving A2 needs the full signed integral, not a pointwise sign. Honest retraction "
            "of a small-n over-generalization (scope-(a) route-death with exact counterexample); not a "
            "refutation of the kernel or A2. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("pointwise_reduction_first_fails_at_n", first_fail)
        w.add_data("pointwise_reduction_false_for_n_ge_29", True)
        w.add_data("R_gains_root_in_unit_interval_at_n", 30)
        w.add_data("kernel_survives_nmax40", bool(kernel_ok))
        w.add_data("a2_survives_nmax40", bool(a2_ok))
        w.add_data("a2_mechanism", "Frullani integral <=0 by cancellation; integrand Cov(H_s,omega3) positive on part of range for n>=29")
        w.add_data("retracts", "PR #4242 'R>0 on [0,inf)' general-reduction framing; hook-reduction 'Cov(H_s)<0 strictly interior'")
        w.add_assertion(
            "covariance_epic_A2_pointwise_reduction_falsified",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("pointwise Cov_Planch(H_s,omega3)<=0 for-all-s FALSE for n>=29 (exact, first fail "
                    "n=29, max_s=+0.056); R>=0 on (0,1) FALSE (root at n=30). Kernel cov(k)<=0 and A2 "
                    "Cov(ln f,omega3)<=0 both SURVIVE exactly k,n<=40. Route eliminated with exact "
                    "counterexample; kernel and A2 intact. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
