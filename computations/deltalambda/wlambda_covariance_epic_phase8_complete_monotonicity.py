#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase8_complete_monotonicity.py — attack A3 refinement (qou-x631):
the mixed-cumulant Taylor coefficients of the tilted mean exhibit a clean (−1)^m alternation for
n ≥ 8, signalling that −g'(θ) is COMPLETELY MONOTONE — a Bernstein-representation target that would
close the kernel AND the whole β ≥ 2 family.

Setup.  g(θ) := E_{β=2+θ}[ω₃] = Σ_λ f^{2+θ}ω₃ / Σ_λ f^{2+θ}  (ω₃ = Σc² − C(n,2)); it is the
exponentially-(dimension-)tilted mean of ω₃.  g(0)=0, g(1)=kernel (∝cov(n)), g'(0)=Cov_Planch(ln f,ω₃).
Its Taylor coefficients a_m := g^{(m)}(0)/m! are the mixed Plancherel cumulants κ_{m+1}(ln f;…;ω₃)/m!.

FINDING.  The signs of a_m follow `sign(a_m) = (−1)^m` EXACTLY for n = 8..17, verified to order m = 10
(60-dps `mpmath.taylor`).  Equivalently the Taylor coefficients of `−g'(θ)` are all ≥ 0 alternating —
the **complete-monotonicity signature**.  For n ≤ 7 the low orders still alternate but high orders
(m ≳ 5) deviate — a small-n boundary effect (those n are covered by exact enumeration k ≤ 40 anyway).
Also `Σ_{m≥2}|a_m| < |a_1|` for all n (absolute domination — stronger than the Phase-7 |R|<|g'(0)|).

WHY IT MATTERS.  If `−g'(θ)` is completely monotone on `θ ∈ [0,∞)` (Bernstein's theorem:
`−g'(θ) = ∫_0^∞ e^{−θs} dμ(s)` for a positive measure μ), then `g'(θ) ≤ 0` for ALL θ ≥ 0, hence
`g(1) = ∫_0^1 g'(θ)dθ ≤ 0` (the KERNEL) and more generally `E_β[ω₃] ≤ 0` for all β ≥ 2 (the whole
family), in one stroke.  This unifies attack A2 (the θ=0 endpoint `g'(0)≤0`) and A3 (the interval /
all-θ statement), and names a concrete proof tool: a Hausdorff/Bernstein moment representation of the
dimension-tilted content-spread covariance.

HONESTY.  The (−1)^m pattern is verified via the SIGNS of Taylor coefficients to order 10 for n=8..17
— strong evidence, NOT a proof that −g' is exactly completely monotone (a finite exponential-sum ratio
is analytic; exact CM is an all-orders statement).  The target for a rigorous attack: prove −g'(θ) is
CM (or its Taylor coefficients alternate to all orders) for n ≥ n₀, via the tilted-mean / MLR / moment
structure of `⟨ω₃ e^{θ ln f}⟩/⟨e^{θ ln f}⟩`.  scope-(a); no fit; nothing wired; no `c_k`; L2 2/7.

# Ref: [manuscript] docs/audits/2026-07-24-covariance-kernel-route1-exchangeable-pair.md
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from mpmath import mp, mpf, power, fsum, taylor  # noqa: E402

mp.dps = 60
NMAX = 17
NORD = 10
N0 = 8  # empirical onset of the clean (-1)^m pattern


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
    if not l:
        return []
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(l) for j in range(row)]


def dim(l):
    d = 1
    for h in hooks(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def taylor_coeffs(n):
    Ck2 = n * (n - 1) // 2
    S = [(mpf(dim(l)), mpf(C2(l) - Ck2)) for l in partitions_of(n)]

    def g(theta):
        b = mpf(2) + theta
        return fsum(power(f, b) * w for f, w in S) / fsum(power(f, b) for f, w in S)

    return taylor(g, mpf(0), NORD)


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — attack A3 refinement: complete monotonicity ===\n")
    print(" n | signs a_1..a_10 | (-1)^m pattern | Σ|a_{m≥2}|/|a_1|")
    cm_from_n0 = True
    absdom_all = True
    tol = mpf('1e-40')
    for n in range(4, NMAX + 1):
        a = taylor_coeffs(n)
        signs = []
        cm = True
        for m in range(1, NORD + 1):
            s = 1 if a[m] > tol else (-1 if a[m] < -tol else 0)
            signs.append('+' if s > 0 else ('-' if s < 0 else '0'))
            if s != 0 and s != (-1) ** m:
                cm = False
        absR = fsum(abs(a[m]) for m in range(2, NORD + 1))
        absdom = absR < abs(a[1])
        absdom_all &= absdom
        if n >= N0:
            cm_from_n0 &= cm
        print(f"{n:2d} | {''.join(signs)}      | {cm}          | {float(absR / abs(a[1])):.4f}")

    ok = cm_from_n0 and absdom_all
    print(f"\n(−1)^m complete-monotonicity signature holds for all n≥{N0} (to order {NORD}): {cm_from_n0}")
    print(f"absolute domination Σ_{{m≥2}}|a_m| < |a_1| all n: {absdom_all}")
    print(f"n≤7: low orders alternate, high orders deviate (small-n boundary; covered by exact k≤40).")
    print(f"\nTARGET: prove −g'(θ) is completely monotone on [0,∞) for n≥n₀ (Bernstein: −g'=∫e^{{−θs}}dμ)")
    print(f"⇒ g'≤0 on [0,∞) ⇒ kernel cov(k)≤0 AND E_β[ω₃]≤0 ∀β≥2 (whole family). Unifies A2 (θ=0) + A3.")
    print(f"\nRESULT: complete-monotonicity signature (n≥{N0}) + absolute domination verified: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase8-complete-monotonicity", engine="python-mpmath")
        w.set_description(
            "Attack A3 refinement (qou-x631): the mixed-cumulant Taylor coefficients a_m=g^{(m)}(0)/m! "
            "of the dimension-tilted mean g(θ)=E_{2+θ}[ω₃] follow sign(a_m)=(−1)^m EXACTLY for n=8..17, "
            "verified to order m=10 (60-dps). This is the COMPLETE-MONOTONICITY signature of −g'(θ): if "
            "−g' is completely monotone on [0,∞) (Bernstein: −g'(θ)=∫e^{−θs}dμ(s), μ≥0), then g'(θ)≤0 "
            "for all θ≥0, hence g(1)=∫_0^1 g'≤0 (the KERNEL) and E_β[ω₃]≤0 ∀β≥2 (the whole family), in "
            "one stroke — unifying attack A2 (θ=0 endpoint g'(0)≤0) and A3 (interval/all-θ). Also "
            "Σ_{m≥2}|a_m|<|a_1| for all n (absolute domination, stronger than Phase-7 |R|<|g'(0)|). "
            "For n≤7 low orders alternate but high orders (m≳5) deviate — a small-n boundary effect "
            "(covered by exact k≤40). HONEST: verified via SIGNS to order 10, not proved to all orders; "
            "the rigorous target is CM of −g' for n≥n₀ via the tilted-mean/MLR/moment structure of "
            "⟨ω₃ e^{θ ln f}⟩/⟨e^{θ ln f}⟩. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("target_conjecture", "-g'(θ) = -d/dβ E_β[ω₃] completely monotone on β∈[2,∞) (n≥n0)")
        w.add_data("cm_signature_holds_from_n", N0)
        w.add_data("cm_verified_to_order", NORD)
        w.add_data("cm_verified_up_to_n", NMAX)
        w.add_data("absolute_domination_all_n", bool(absdom_all))
        w.add_data("small_n_boundary_note", "n<=7 deviate at high order; covered by exact k<=40")
        w.add_data("implication", "CM(-g') => g'<=0 on [0,inf) => kernel AND whole beta>=2 family")
        w.add_data("proof_tool", "Bernstein/Hausdorff moment representation of the tilted covariance")
        w.add_assertion(
            "covariance_epic_phase8_complete_monotonicity_signature",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Taylor coeffs of g(θ)=E_{2+θ}[ω₃] follow sign=(−1)^m for n≥8 to order 10 (60dps) "
                    "⇒ −g' completely-monotone signature; plus Σ_{m≥2}|a_m|<|a_1| all n. If −g' is CM "
                    "(Bernstein) then g'≤0 on [0,∞) ⇒ kernel + whole β≥2 family. Signs to order 10, "
                    "not all-orders proof. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
