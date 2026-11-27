#!/usr/bin/env python3
r"""
wlambda_covariance_kernel_square_law_inverse.py — the covariance kernel as a coefficient of the
convolution inverse of the square law on S_n (bean qou-v8t7, epic qou-7igi / qou-x631).

THE REFORMULATION (proved on paper; this probe checks it with zero shared code).
Let  Q := (1/n!) Σ_{x∈S_n} x²  ∈ Z(ℚ[S_n]),  the law of X² for X uniform on S_n.
Every irreducible character of S_n is real (Frobenius–Schur indicator 1), so
    (1/n!) Σ_x χ^λ(x²) = 1,
and the central element Q acts on V^λ by the scalar 1/f^λ.  Hence Q is invertible in the
centre and  Q^{-1} = Σ_λ f^λ e_λ = (1/n!) Σ_g T(g)·g,  T(g) := Σ_λ (f^λ)² χ^λ(g).
At a 3-cycle σ this is the kernel:

    cov(n) ≤ 0   ⇔   T₃(n) ≤ 0   ⇔   [σ] Q^{-1} ≤ 0,

i.e. the convolution inverse of the square law puts non-positive mass on 3-cycles.
More generally, for any central F with eigenvalue F(λ),  Cov_Planch(F, ω₃) = |C₃|·[σ]F̂, so
with  φ(s) := [σ] Q^{-s}  one has  φ(1) ∝ kernel  and  φ'(0) ∝ A2 = Cov_Planch(ln f, ω₃).

CHECK A (independent, group algebra, n = 3..7).  Build Q as a class function by enumerating
all x ∈ S_n and counting x², invert it in the class algebra by solving the convolution system,
and compare the 3-cycle coefficient and the identity coefficient with T₃(n)/n! and Σ_λ(f^λ)³/n!
computed from the hook-length formula.  Nothing is shared between the two sides.

CHECK B (large-tilt sign is the sign of ω₃ at the maximum-dimension shape).  As s → ∞,
sign Cov(ω₃, f^s) = sign Σ_{f^λ = f_max} ω₃(λ).  Exact over n = 3..40: this is POSITIVE at
n = 18 (λ = (7,4,3,2,1,1) and its transpose, ω₃ = +3) and n = 26 (ω₃ = +1), zero at
n = 4, 5, 8, 14, 21, negative otherwise.  Consequence (structural, the invariant is this exact
count): no argument that would give Cov(ω₃, ψ(f)) ≤ 0 for every increasing ψ, or for every
ψ(f) = Σ_m c_m (1 − 1/f)^m with c_m ≥ 0, or for every power ψ = f^s with s ≥ 1, can exist.
The sufficient condition "a_m := [σ](e − Q)^m ≤ 0 for all m" (which would give φ(s) ≤ 0 for all
s > 0 via Q^{-s} = Σ_m C(s+m−1, m)(e − Q)^m) is therefore FALSE at n = 18.  The kernel's sign
at s = 1 needs an argument that uses s = 1 (or a bounded s-window), not monotonicity in the tilt.

CHECK C (where the tilt flips).  Brackets for the first s with Cov(ω₃, f^s) > 0 at n = 18, 26,
computed with mpmath at 60 digits (exact integer inputs; mpf only for the real power).

scope-(a) for C; B is a structural exclusion of a proof CLASS (not of the kernel), with the
exact counterexample as its invariant.  No fit; nothing wired; no measured value enters.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from math import comb, factorial

import mpmath as mp

mp.mp.dps = 60


def partitions(n: int, m: int | None = None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in partitions(n - k, k):
            yield (k,) + p


def dim_and_omega3(lam: tuple[int, ...], n: int) -> tuple[int, int]:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    hp, c2 = 1, 0
    for i, r in enumerate(lam):
        for j in range(r):
            hp *= r - j + conj[j] - i - 1
            c2 += (j - i) ** 2
    return factorial(n) // hp, c2 - comb(n, 2)


# ---------------------------------------------------------------- check A (group algebra)
def cycle_type(p: tuple[int, ...]) -> tuple[int, ...]:
    n, seen, ct = len(p), [False] * len(p), []
    for i in range(n):
        if not seen[i]:
            L, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = p[j]
                L += 1
            ct.append(L)
    return tuple(sorted(ct, reverse=True))


def compose(a, b):  # (a∘b)(i) = a(b(i))
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    inv = [0] * len(a)
    for i, ai in enumerate(a):
        inv[ai] = i
    return tuple(inv)


def solve(M, rhs):
    k = len(M)
    A = [row[:] + [rhs[i]] for i, row in enumerate(M)]
    for c in range(k):
        piv = next(r for r in range(c, k) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        for r in range(k):
            if r != c and A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [A[i][k] / A[i][i] for i in range(k)]


def check_A(n: int) -> dict:
    perms = list(itertools.permutations(range(n)))
    nf = factorial(n)
    classes = sorted({cycle_type(p) for p in perms}, reverse=True)
    idx = {c: i for i, c in enumerate(classes)}
    members = {c: [] for c in classes}
    for p in perms:
        members[cycle_type(p)].append(p)
    reps = {c: members[c][0] for c in classes}
    # Q as a class function: Q(g) = #{x : x² = g} / n!
    sq = {c: 0 for c in classes}
    for x in perms:
        sq[cycle_type(compose(x, x))] += 1
    Qval = {c: Fraction(sq[c], nf * len(members[c])) for c in classes}
    # (Q * 1_{C_j})(g_i) = Σ_{h ∈ C_j} Q(g_i h^{-1})
    M = [[sum(Qval[cycle_type(compose(reps[ci], inverse(h)))] for h in members[cj])
          for cj in classes] for ci in classes]
    e = tuple([1] * n)
    rhs = [Fraction(1) if c == e else Fraction(0) for c in classes]
    x = solve(M, rhs)
    three = tuple([3] + [1] * (n - 3))
    coeff3, coeffe = x[idx[three]], x[idx[e]]
    # hook side
    T3 = Fraction(0)
    S3 = 0
    for lam in partitions(n):
        f, w = dim_and_omega3(lam, n)
        S3 += f ** 3
        # f²χ(σ) = f³ ω₃ / |C₃|,  |C₃| = n(n-1)(n-2)/3
        T3 += Fraction(f ** 3 * w * 3, n * (n - 1) * (n - 2))
    return {"n": n, "coeff3": coeff3, "T3_over_nfact": T3 / nf,
            "coeffe": coeffe, "sumf3_over_nfact": Fraction(S3, nf),
            "ok": coeff3 == T3 / nf and coeffe == Fraction(S3, nf)}


# ---------------------------------------------------------------- check B (top shape)
def check_B(nmax: int) -> dict:
    out = {}
    for n in range(3, nmax + 1):
        data = [(lam,) + dim_and_omega3(lam, n) for lam in partitions(n)]
        fmax = max(f for _, f, _ in data)
        top = [(lam, w) for lam, f, w in data if f == fmax]
        out[n] = {"fmax": fmax, "shapes": [list(l) for l, _ in top],
                  "omega3_sum": sum(w for _, w in top)}
    return out


# ---------------------------------------------------------------- check C (flip point)
def check_C(n: int) -> tuple[float, float]:
    L = [(mp.mpf(f), w) for f, w in (dim_and_omega3(l, n) for l in partitions(n))]

    def phi(s):
        return mp.fsum(F ** (2 + s) * w for F, w in L)

    lo, hi = mp.mpf(1), mp.mpf(2)
    assert phi(lo) < 0
    while phi(hi) <= 0:
        lo, hi = hi, 2 * hi
    for _ in range(60):
        mid = (lo + hi) / 2
        if phi(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def main() -> int:
    print("A. group-algebra inverse of the square law vs hook-formula kernel")
    okA = True
    resA = []
    for n in range(3, 8):
        r = check_A(n)
        resA.append(r)
        okA &= r["ok"]
        print(f"  n={n}: [3-cycle]Q^-1 = {r['coeff3']}  T3/n! = {r['T3_over_nfact']}   "
              f"[e]Q^-1 = {r['coeffe']}  Σf³/n! = {r['sumf3_over_nfact']}   match={r['ok']}")
    print("B. sign of ω₃ summed over the maximum-dimension shapes, n=3..40")
    B = check_B(40)
    pos = [n for n, v in B.items() if v["omega3_sum"] > 0]
    zero = [n for n, v in B.items() if v["omega3_sum"] == 0]
    for n in pos:
        print(f"  n={n}: f_max={B[n]['fmax']} shapes={B[n]['shapes']} Σω₃={B[n]['omega3_sum']}  > 0")
    print(f"  positive at n={pos}; zero at n={zero}; negative elsewhere")
    okB = pos == [18, 26] and zero == [4, 5, 8, 14, 21]
    print("C. first s with Cov(ω₃, f^s) > 0")
    brackets = {}
    for n in pos:
        lo, hi = check_C(n)
        brackets[n] = mp.nstr(hi, 12)
        print(f"  n={n}: s* ∈ ({mp.nstr(lo, 12)}, {mp.nstr(hi, 12)}]")
    ok = okA and okB
    print(f"\nRESULT: reformulation verified n=3..7: {okA}; top-shape sign table as stated: {okB}")
    try:
        sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1] / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-kernel-square-law-inverse", engine="python-exact")
        w.set_description(
            "Covariance kernel as the 3-cycle coefficient of Q^{-1}, Q = (1/n!)Σ_x x² (law of X², X "
            "uniform on S_n): Q acts on V^λ by 1/f^λ (Frobenius–Schur indicator 1), so "
            "Q^{-1}=(1/n!)Σ_g T(g)g and cov(n)≤0 ⇔ [σ]Q^{-1}≤0. Verified in the class algebra with "
            "zero shared code, n=3..7. Large-tilt sign of Cov(ω₃,f^s) = sign of ω₃ at the max-dim "
            "shape: positive at n=18, 26 (n≤40), so no tilt-uniform / increasing-ψ / absolutely-"
            "monotone argument can prove the kernel. Does NOT prove the kernel. No fit; nothing wired.")
        w.add_data("checkA", [{k: str(v) for k, v in r.items()} for r in resA])
        w.add_data("maxdim_omega3_positive_n", pos)
        w.add_data("maxdim_omega3_zero_n", zero)
        w.add_data("maxdim_table", {str(n): v for n, v in B.items()})
        w.add_data("tilt_flip_s_upper_bracket", {str(k): v for k, v in brackets.items()})
        w.add_assertion("kernel_square_law_inverse", computed=str(int(ok)), expected="1",
                        tolerance=0,
                        source="[σ]Q^{-1} = T3/n! and [e]Q^{-1} = Σf³/n! exactly for n=3..7; "
                               "max-dim ω₃ > 0 exactly at n∈{18,26} for n≤40.")
        print(f"Witness: {w.save()}")
    except ImportError as e:
        print(f"(witness skipped — witness_base unavailable: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
