#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase6_marginal_stein.py — Phase 6 of the covariance-kernel proof epic
(qou-x631), effective-Stein program, STEP 1: the marginal Stein / Berry–Esseen ingredients for the
3-cycle content-spread ω₃ (Fulman `math/0305423` did only k=2 / the transposition; this is k=3).

From Phase 5: the Plancherel-reversible down-up chain has ω₃ = Σc²−C(n,2) as an eigenfunction with
E[ω₃(λ*)|λ] = (1−τ₃)ω₃(λ), τ₃ = 3/n. Normalise W := ω₃/σ, σ² := Var_P(ω₃) = E_P[ω₃²], so E[W*|W] =
(1−τ₃)W (mean 0, var 1). Stein's exchangeable-pair Berry–Esseen bound (Fulman Thm 1.3) for such a pair
is governed by two dimensionless ingredients:
    A(n) := (1/τ₃)·√Var_P( E[(W*−W)² | λ] )        (fluctuation of the conditional variance),
    B(n) := √( E_P|W*−W|³ / τ₃ ),                   (third-moment term),
with `|P(W≤x)−Φ(x)| ≤ c₁·A(n) + c₂·B(n)` for absolute constants c₁,c₂ (Stein). This probe computes
A(n), B(n) exactly-ish (float on the exact chain) and estimates their decay rate in n — the marginal
CLT rate for the 3-cycle, the k=3 analogue of Fulman's `n^{−1/4}` for the transposition.

Consistency checks emitted: E_P[(W*−W)²] = 2τ₃ (eigenfunction identity), E_P[W]=0, Var_P(W)=1.

SCOPE.  This is the MARGINAL CLT ingredient — a stepping stone.  It does NOT bound the kernel, which
is the JOINT covariance Cov(f,ω₃); the joint/effective Berry–Esseen bound on (ln f, ω₃) is the open
core of the effective-Stein program (STEP 2+, genuine multi-session, not in the literature).
scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7).  In-sandbox (exact chain + float moments).

# Ref: [fulman2004stein] https://doi.org/10.1090/S0002-9947-04-03499-3
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

NMAX = 12


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


def corners_remove(l):
    l = list(l)
    out = []
    for i in range(len(l)):
        if (i == len(l) - 1 and l[i] >= 1) or (i < len(l) - 1 and l[i] > l[i + 1]):
            m = l[:]
            m[i] -= 1
            out.append(tuple(x for x in m if x > 0))
    return out


def boxes_add(m, n):
    m = list(m)
    out = []
    for i in range(len(m) + 1):
        cur = m[i] if i < len(m) else 0
        prev = m[i - 1] if i > 0 else 10 ** 9
        if cur < prev:
            a = m[:]
            if i < len(m):
                a[i] += 1
            else:
                a = a + [1]
            out.append(tuple(a))
    return out


def krow(a, n, dm):
    row = {}
    for mu in corners_remove(a):
        pd = Fr(dim(mu), dm[a])
        for b in boxes_add(mu, n):
            row[b] = row.get(b, Fr(0)) + pd * Fr(dm[b], n * dim(mu))
    return row


def stein_ingredients(n):
    P = list(partitions_of(n))
    dm = {p: dim(p) for p in P}
    fact = math.factorial(n)
    Ck2 = n * (n - 1) // 2
    Pw = {p: Fr(dm[p] ** 2, fact) for p in P}
    om = {p: Fr(C2(p) - Ck2) for p in P}
    # sigma^2 = Var_P(omega3) = E_P[omega3^2]  (mean 0)
    var = sum(Pw[p] * om[p] * om[p] for p in P)
    sigma = math.sqrt(float(var))
    W = {p: float(om[p]) / sigma for p in P}
    tau = 3.0 / n
    # conditional moments of Delta W under the chain
    m2_mean = 0.0
    m2_sq = 0.0
    m3_mean = 0.0
    Wmean = sum(float(Pw[p]) * W[p] for p in P)
    Wvar = sum(float(Pw[p]) * W[p] ** 2 for p in P) - Wmean ** 2
    for a in P:
        row = krow(a, n, dm)
        m2 = 0.0
        m3 = 0.0
        for b, kab in row.items():
            dW = W[b] - W[a]
            k = float(kab)
            m2 += k * dW * dW
            m3 += k * abs(dW) ** 3
        pw = float(Pw[a])
        m2_mean += pw * m2
        m2_sq += pw * m2 * m2
        m3_mean += pw * m3
    var_m2 = max(m2_sq - m2_mean ** 2, 0.0)
    A = math.sqrt(var_m2) / tau
    B = math.sqrt(m3_mean / tau)
    return dict(sigma2=float(var), Wmean=Wmean, Wvar=Wvar, tau=tau,
                m2_mean=m2_mean, two_tau=2 * tau, var_m2=var_m2, m3_mean=m3_mean, A=A, B=B)


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — Phase 6 (effective Stein) STEP 1: ω₃ marginal ===\n")
    print(" n |  Var_P(ω₃) | E[(ΔW)²]=2τ? |   A(n)     |   B(n)     | checks(W̄≈0,VarW≈1)")
    rows = []
    for n in range(3, NMAX + 1):
        d = stein_ingredients(n)
        chk = abs(d['m2_mean'] - d['two_tau']) < 1e-9 and abs(d['Wmean']) < 1e-9 and abs(d['Wvar'] - 1) < 1e-9
        rows.append((n, d))
        print(f"{n:2d} | {d['sigma2']:10.3f} | {d['m2_mean']:.4f}/{d['two_tau']:.4f} "
              f"| {d['A']:.6f} | {d['B']:.6f} | {chk}")
    # rate estimate: fit log A, log B vs log n over the tail
    import math as _m
    def slope(xs, ys):
        nk = len(xs); sx = sum(xs); sy = sum(ys)
        sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
        return (nk * sxy - sx * sy) / (nk * sxx - sx * sx)
    tail = rows[3:]
    lns = [_m.log(n) for (n, _d) in tail]
    sA = slope(lns, [_m.log(d['A']) for (_n, d) in tail])
    sB = slope(lns, [_m.log(d['B']) for (_n, d) in tail])
    print(f"\nDecay-rate estimates (tail log-log slope):  A(n) ~ n^{sA:.2f},  B(n) ~ n^{sB:.2f}")
    print(f"(Fulman's transposition marginal rate is n^-0.25; this is the k=3 / ω₃ analogue.)")
    ok = all(abs(d['m2_mean'] - d['two_tau']) < 1e-9 for (_n, d) in rows)
    print(f"\nEigenfunction identity E[(ΔW)²]=2τ₃ holds all n≤{NMAX}: {ok}")
    print("STEP 1 (marginal ω₃ Stein ingredients) done. STEP 2 (open): joint effective Berry–Esseen")
    print("on (ln f, ω₃) to bound the transfer-factor error below the negative main term — the kernel.")
    print(f"\nRESULT: marginal Stein ingredients computed + identity verified: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase6-marginal-stein", engine="python-exact+float")
        w.set_description(
            "Phase 6 (effective-Stein program) STEP 1 of the covariance-kernel epic (qou-x631): the "
            "marginal Stein/Berry–Esseen ingredients for the 3-cycle content-spread ω₃ (Fulman "
            "math/0305423 did only k=2/transposition; this is k=3). On the Plancherel-reversible "
            "down-up chain, W=ω₃/σ (σ²=Var_P(ω₃)) has E[W*|W]=(1−3/n)W; the exchangeable-pair BE bound "
            "is governed by A(n)=(1/τ₃)√Var_P(E[(ΔW)²|λ]) and B(n)=√(E_P|ΔW|³/τ₃), τ₃=3/n. Computed "
            "both across n and estimated their log-log decay rate (the k=3 analogue of Fulman's n^-1/4 "
            "transposition rate). Consistency verified: E_P[(ΔW)²]=2τ₃, E_P[W]=0, Var_P(W)=1 all n≤12. "
            "SCOPE: this is the MARGINAL CLT ingredient (stepping stone); it does NOT bound the kernel "
            "(the JOINT covariance Cov(f,ω₃)) — the joint effective Berry–Esseen on (ln f,ω₃) is the "
            "open core (STEP 2+, multi-session, not in the literature). scope-(a); no fit; nothing "
            "wired; no c_k; L2 2/7.")
        w.add_data("tau3", "3/n")
        w.add_data("W_normalized", "W = omega3 / sqrt(Var_P(omega3))")
        w.add_data("marginal_rate_A_loglog_slope", round(sA, 3))
        w.add_data("marginal_rate_B_loglog_slope", round(sB, 3))
        w.add_data("eigenfunction_identity_E_dW2_eq_2tau", bool(ok))
        w.add_data("A_B_table", [[n, round(d['A'], 6), round(d['B'], 6)] for (n, d) in rows])
        w.add_data("scope_note", "marginal only; kernel needs joint (ln f, omega3) effective BE (open)")
        w.add_assertion(
            "covariance_epic_phase6_marginal_stein_step1",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Marginal Stein ingredients A(n),B(n) for the ω₃ (3-cycle) content-spread computed "
                    "on the Plancherel down-up chain; eigenfunction identity E[(ΔW)²]=2τ₃ (τ₃=3/n) "
                    "verified n≤12. First step of the effective-Stein program; the joint (ln f,ω₃) BE "
                    "bound remains open. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
