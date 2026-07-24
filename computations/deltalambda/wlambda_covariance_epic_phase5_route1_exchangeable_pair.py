#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase5_route1_exchangeable_pair.py — Phase 5 of the covariance-kernel proof
epic (qou-x631): build the Fulman-analogue Stein exchangeable pair for the 3-cycle, and reformulate
the kernel as a LOCAL one-step dimension-increment correlation.

Fulman (`math/0305423`) proves a Stein-method CLT (with error) for the TRANSPOSITION character ratio
by building an exchangeable pair from the Plancherel-reversible down-up Markov chain on Young diagrams,
for which the transposition central character is an eigenfunction.  This probe carries that
construction to the 3-CYCLE — the central element our kernel needs.

THE CHAIN.  On partitions of `n`, the down-up chain
    down:  λ → μ  (remove a corner box, prob  dim μ / dim λ),
    up:    μ → λ* (add a box,          prob  dim λ* / (n · dim μ)),
is stochastic and **reversible w.r.t. the Plancherel measure** `P(λ) = (dim λ)²/n!` (verified).

EIGENFUNCTION + EXACT EIGENVALUE.  The content-power central characters `ω_j(λ) := Σ_□c(□)^j −
E_Planch[Σc^j]` are eigenfunctions of the chain for `j = 1, 2`:
    j = 1 (Σc,  transposition, Fulman's object):  τ₁ = 2/n,
    j = 2 (Σc², 3-cycle,       OUR object ω₃):    τ₃ = 3/n,        ← the direct analogue.
(`j ≥ 3` mix and are not pure eigenfunctions; we do not need them.)  So `E[ω₃(λ*) | λ] = (1−3/n)·ω₃(λ)`
— exactly the hypothesis `E_W(W*) = (1−τ)W` that Fulman's Stein bound (his Thm 1.3) requires.

LOCAL REFORMULATION OF THE KERNEL.  With `f = dim` and `Δf := f(λ*) − f(λ)`, reversibility + the
eigenfunction property give the EXACT identity (derivation, verified):
    E_P[ Δf · ω₃(λ) ] = E_P[ ω₃ · (Kf − f) ] = (1−τ₃)⟨ω₃,f⟩_P − ⟨ω₃,f⟩_P = −τ₃ · Cov_P(f, ω₃)
    = −(3/n) · cov(n)/n!.
Hence
    **kernel `cov(n) ≤ 0`  ⇔  `Cov_P(f, ω₃) ≤ 0`  ⇔  `E_P[ Δf · ω₃ ] ≥ 0`**,
i.e. the global sign is the sign of the correlation between the ONE-STEP dimension increment `Δf` and
the current content-spread `ω₃` — a local quantity.  This is the Fulman-analogue reduction; it does
**not** yet close the sign (that needs either the explicit combinatorial evaluation of `E_P[Δf·ω₃]`
with a sign, or the joint Stein CLT of `(f, ω₃)` with an effective Berry–Esseen error — genuine
further work, and NOT in the literature for the 3-cycle-with-dimension covariance).

Discipline: scope-(a) construction/reformulation; no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
The kernel remains an honest §3b conjecture.  In-sandbox (exact `Fraction`).

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

NMAX = 9


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


def contents(l):
    return [(j - i) for i, row in enumerate(l) for j in range(row)]


def pk(l, k):
    return sum(c ** k for c in contents(l))


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


def build_chain(n):
    P = list(partitions_of(n))
    idx = {p: i for i, p in enumerate(P)}
    N = len(P)
    dm = {p: dim(p) for p in P}
    fact = math.factorial(n)
    K = [[Fr(0)] * N for _ in range(N)]
    for a in P:
        for mu in corners_remove(a):
            pd = Fr(dim(mu), dm[a])
            for b in boxes_add(mu, n):
                K[idx[a]][idx[b]] += pd * Fr(dm[b], n * dim(mu))
    Pw = {p: Fr(dm[p] ** 2, fact) for p in P}
    return P, idx, N, dm, fact, K, Pw


def eigen_tau(P, N, K, Pw, k):
    """content-power central char ω_k = Σc^k − E_P[Σc^k]; return (is_eigenfunction, tau)."""
    Epk = sum(Pw[p] * pk(p, k) for p in P)
    om = [Fr(pk(p, k)) - Epk for p in P]
    Kom = [sum(K[i][j] * om[j] for j in range(N)) for i in range(N)]
    rs = set(Kom[i] / om[i] for i in range(N) if om[i] != 0)
    if len(rs) == 1:
        return True, (1 - next(iter(rs))), om
    return False, None, om


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — Phase 5: Route-1 exchangeable pair (3-cycle) ===\n")

    all_rev = all_eig3 = all_id = True
    tau1s, tau3s = [], []
    for n in range(3, NMAX + 1):
        P, idx, N, dm, fact, K, Pw = build_chain(n)
        stoch = all(sum(K[i]) == 1 for i in range(N))
        rev = all(Pw[P[i]] * K[i][j] == Pw[P[j]] * K[j][i] for i in range(N) for j in range(N))
        e1, t1, _ = eigen_tau(P, N, K, Pw, 1)
        e3, t3, om3 = eigen_tau(P, N, K, Pw, 2)  # Σc² central char = ω₃ (3-cycle)
        # exchangeable-pair identity: E_P[Δf · ω₃] = −τ₃ · cov(n)/n!
        lhs = Fr(0)
        for i, a in enumerate(P):
            inc = sum(K[i][j] * (dm[P[j]] - dm[a]) for j in range(N))
            lhs += Pw[a] * om3[i] * inc
        Ck2 = n * (n - 1) // 2
        cov = sum(dm[p] ** 3 * (pk(p, 2) - Ck2) for p in P)
        pred = -t3 * Fr(cov, fact) if e3 else None
        idok = (lhs == pred)
        all_rev &= (stoch and rev); all_eig3 &= e3; all_id &= idok
        tau1s.append(t1); tau3s.append(t3)
        print(f"n={n}: reversible={stoch and rev}  ω₃ eigenfn={e3}  τ₁(Σc)={t1}  τ₃(Σc²)={t3}  "
              f"E_P[Δf·ω₃]={lhs} = −τ₃·cov/n!={pred}  ({idok})")

    tau1_formula = all(t == Fr(2, n) for t, n in zip(tau1s, range(3, NMAX + 1)))
    tau3_formula = all(t == Fr(3, n) for t, n in zip(tau3s, range(3, NMAX + 1)))
    ok = all_rev and all_eig3 and all_id and tau1_formula and tau3_formula
    print(f"\nτ₁ = 2/n (Fulman transposition analogue) all n: {tau1_formula}")
    print(f"τ₃ = 3/n (our 3-cycle) all n: {tau3_formula}")
    print(f"reversible chain: {all_rev}; ω₃ eigenfunction: {all_eig3}; local identity holds: {all_id}")
    print(f"\nLOCAL REFORMULATION: kernel ≤ 0  ⇔  E_P[(f(λ*)−f(λ))·ω₃(λ)] ≥ 0  (τ₃ = 3/n > 0).")
    print(f"Next (open): sign E_P[Δf·ω₃] via explicit increment, or joint Stein CLT with effective error.")
    print(f"\nRESULT: Route-1 exchangeable-pair construction verified: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase5-route1-exchangeable-pair",
                           engine="python-exact")
        w.set_description(
            "Phase 5 of the covariance-kernel proof epic (qou-x631): the Fulman-analogue Stein "
            "exchangeable pair for the 3-cycle. Built the Plancherel-reversible down-up chain on "
            "partitions of n (down: remove corner, prob dim μ/dim λ; up: add box, prob dim λ*/(n dim μ)); "
            "reversibility verified. The content-power central characters ω_j=Σc^j−E_P[Σc^j] are "
            "eigenfunctions for j=1 (Σc, transposition, Fulman's object, τ₁=2/n) and j=2 (Σc²=ω₃, "
            "3-cycle, OUR object, τ₃=3/n) — the direct k=2 analogue of Fulman's k=1; j≥3 mix (not "
            "needed). So E[ω₃(λ*)|λ]=(1−3/n)ω₃(λ), the exact hypothesis of Fulman's Stein bound. "
            "Reversibility + eigenfunction give the EXACT identity E_P[Δf·ω₃]=−τ₃·Cov_P(f,ω₃)="
            "−(3/n)cov(n)/n! (Δf=f(λ*)−f(λ)), verified n≤9. Hence the kernel is reformulated LOCALLY: "
            "cov(n)≤0 ⇔ E_P[(f(λ*)−f(λ))ω₃(λ)]≥0 (correlation of the one-step dimension increment with "
            "the content-spread). Does NOT yet close the sign (needs the explicit increment evaluation "
            "or a joint Stein CLT with effective Berry–Esseen error — genuine further work, not in the "
            "literature for the 3-cycle×dimension covariance). scope-(a); no fit; nothing wired; no "
            "c_k; L2 2/7.")
        w.add_data("chain", "Plancherel-reversible down-up on partitions of n")
        w.add_data("reversible_verified_nmax", NMAX)
        w.add_data("tau1_transposition", "2/n (Fulman analogue)")
        w.add_data("tau3_three_cycle", "3/n (our omega3)")
        w.add_data("omega3_is_eigenfunction", bool(all_eig3))
        w.add_data("local_identity", "E_P[(f(lam*)-f(lam)) omega3] = -(3/n) cov(n)/n!")
        w.add_data("local_identity_verified", bool(all_id))
        w.add_data("local_reformulation", "cov(n)<=0  <=>  E_P[Df*omega3] >= 0")
        w.add_assertion(
            "covariance_epic_phase5_route1_exchangeable_pair",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Plancherel-reversible down-up chain built; ω₃=Σc²−C(n,2) is an eigenfunction with "
                    "τ₃=3/n (Fulman-analogue of the transposition τ₁=2/n); exact identity "
                    "E_P[Δf·ω₃]=−(3/n)cov/n! verified n≤9 ⇒ kernel⇔E_P[Δf·ω₃]≥0 (local reformulation). "
                    "Construction only; sign still open. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
