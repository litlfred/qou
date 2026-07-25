#!/usr/bin/env python3
r"""
wlambda_covariance_epic_A1b_dpp_maya_representation.py — DPP route, deliverable 1 (qou-x631, qou-g0n2):
the Maya-diagram quadratic representation that makes the determinantal (Borodin–Okounkov–Olshanski)
tool applicable to the covariance kernel — and the depoissonization obstruction that is its real
difficulty.

MOTIVATION. Every prior route (A1/A5 dim²→dim³ threshold; A2 polynomial-positivity + 3 route-
eliminations; A3 CM refuted) converged on the same missing tool: a determinantal / generating-function
handle on ν_v = Cov_Planch(N_v, ω₃), the hook-count-vs-content-spread covariance. This probe sets up
that tool and locates precisely where its difficulty lies.

THE STRUCTURAL BRIDGE (exact, verified n ≤ 10). Encode λ by its Maya diagram: particle set
P(λ) = {λ_i − i : i ≥ 1} ⊂ ℤ (vacuum {−1,−2,…}), occupations m_a = 1_{a∈P}. Then:

  • Claim 1 (hook = particle–hole distance):  N_v = Σ_a (1 − m_a) m_{a+v}   — QUADRATIC in m.
  • Claim 2 (hook-content identity Σh²=Σc²+n²):  ω₃ = Σ_v v² N_v − n² − C(n,2)  — also QUADRATIC in m.

So Cov(N_v, ω₃) is the covariance of two quadratic statistics of the Maya occupation process. Under
the θ-poissonized Plancherel measure P_θ(λ) = e^{−θ} θ^{|λ|} (dim λ / |λ|!)², the occupations m_a form
a DETERMINANTAL point process with the discrete-Bessel kernel (Borodin–Okounkov–Olshanski 2000,
`math/9905032`). Hence Cov(N_v, N_w) admits an exact Wick / kernel-contraction reduction — the tool
the elementary character machinery lacked.

THE OBSTRUCTION (the honest finding — depoissonization is the hard step). The kernel condition that
makes A2 work is Σ_v ν_v = 0, which holds at FIXED n because Σ_v N_v = n is then a constant, so the
|λ|-comovement is projected out. At the POISSONIZED level |λ| fluctuates, and the SAME expression
Cov(N_v, Σ_□ h²) is DOMINATED by that fluctuation and comes out ALL POSITIVE (θ=4: ≈ +12.5, +10.0, …,
+0.08) — the opposite sign structure. Numerically:

  fixed-n:      ν_v = Cov(N_v, Σh²) = Cov(N_v, ω₃),  Σ_v ν_v = 0,  mixed sign  (the A2 object)
  poissonized:  Cov_θ(N_v, Σh²) > 0 for all v,       Σ_v (·) ≠ 0,  |λ|-comovement dominates

So the determinantal kernel must be DEPOISSONIZED — conditioned on |λ| = n (equivalently, the
|λ|-fluctuation contribution subtracted) — before its sign reflects the fixed-n covariance. That
conditioning, not the kernel algebra, is where the DPP route's difficulty concentrates. This scopes
the next attempt precisely: compute the |λ|=n-conditioned discrete-Bessel kernel (or the steepest-
descent depoissonization of Cov_θ(N_v, N_w) with the |λ|-mean-field subtracted).

HONESTY. Establishes the exact structural bridge + names the real obstruction. Does NOT prove the
kernel; the depoissonized-kernel sign analysis is open. scope-(a); no fit; nothing wired; no c_k;
L2 unchanged (2/7).

# Ref: [manuscript] docs/audits/2026-07-25-covariance-kernel-A1b-dpp-maya-representation.md
# Ref: [borodin-okounkov-olshanski] https://arxiv.org/abs/math/9905032
"""
from __future__ import annotations

import math
import sys
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


def hooks_mult(l):
    l = list(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])] if l else []
    cnt = {}
    for i, row in enumerate(l):
        for j in range(row):
            h = (row - j) + (conj[j] - i) - 1
            cnt[h] = cnt.get(h, 0) + 1
    return cnt


def hooks(l):
    l = list(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])] if l else []
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(l) for j in range(row)]


def dim(l):
    d = 1
    for h in hooks(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2content(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def particles(l, W):
    l = list(l)
    ell = len(l)
    P = set()
    i = 1
    while True:
        lam = l[i - 1] if i - 1 < ell else 0
        p = lam - i
        if p < -W:
            break
        P.add(p)
        i += 1
        if i > W + ell + 5:
            break
    return P


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — DPP route: Maya representation + depoissonization ===\n")

    # ---- Claim 1 & 2: exact Maya quadratic representation ----
    W = 40
    print("Structural bridge (exact): Maya diagram m_a = 1_{a ∈ {λ_i−i}}.")
    ok1 = ok2 = True
    for n in range(1, 11):
        for l in partitions_of(n):
            P = particles(l, W)
            m = {a: (1 if a in P else 0) for a in range(-W, W + 1)}
            hc = hooks_mult(l)
            # Claim 1: N_v = Σ_a (1-m_a) m_{a+v}
            for v in range(1, n + 1):
                maya = sum((1 - (m.get(a, 1 if a < -W else 0))) * m.get(a + v, 0)
                           for a in range(-W, W + 1))
                if maya != hc.get(v, 0):
                    ok1 = False
            # Claim 2: ω₃ = Σ v² N_v − n² − C(n,2)  ⟺  Σh² = Σc² + n²
            sh2 = sum(v * v * c for v, c in hc.items())
            if sh2 - n * n != C2content(l):
                ok2 = False
    print(f"  Claim 1: N_v = Σ_a (1−m_a) m_(a+v)  (hook = particle–hole distance)   exact n≤10: {ok1}")
    print(f"  Claim 2: ω₃ = Σ_v v² N_v − n² − C(n,2)  (Σh²=Σc²+n², QUADRATIC in m)   exact n≤10: {ok2}")
    bridge_ok = ok1 and ok2

    # ---- poissonized Plancherel: determinantal, and the depoissonization obstruction ----
    THETA = 4.0
    NTRUNC = 22
    print(f"\nθ-poissonized Plancherel (θ={THETA}, |λ|≤{NTRUNC}): occupations are DETERMINANTAL")
    print("  (Borodin–Okounkov–Olshanski, discrete-Bessel kernel). Compute Cov_θ(N_v, Σh²):")
    allL = [l for nn in range(0, NTRUNC + 1) for l in partitions_of(nn)]
    wt = [math.exp(-THETA) * THETA ** sum(l) * (dim(l) / math.factorial(sum(l))) ** 2 for l in allL]
    wtot = sum(wt)
    hookcounts = [hooks_mult(l) for l in allL]
    vmax = 10

    def EN(v):
        return sum(w * hc.get(v, 0) for w, hc in zip(wt, hookcounts)) / wtot

    def Esh2_N(v):
        return sum(w * hc.get(v, 0) * sum(k * k * c for k, c in hc.items())
                   for w, hc in zip(wt, hookcounts)) / wtot

    Esh2 = sum(w * sum(k * k * c for k, c in hc.items()) for w, hc in zip(wt, hookcounts)) / wtot
    ENv = {v: EN(v) for v in range(1, vmax + 1)}
    cov_theta = [Esh2_N(v) - ENv[v] * Esh2 for v in range(1, vmax + 1)]
    all_pos = all(x > 0 for x in cov_theta)
    print(f"  total weight = {wtot:.6f} (→1, truncation complete)")
    print("  Cov_θ(N_v, Σh²), v=1..10:  " + ' '.join(f'{x:+.3f}' for x in cov_theta))
    print(f"  ALL POSITIVE at poissonized level: {all_pos}   ← |λ|-comovement dominates")
    print("  (contrast fixed-n: Cov(N_v,Σh²)=ν_v, Σ_v ν_v=0, mixed sign — the |λ|-comovement is")
    print("   projected out because Σ_v N_v = n is then CONSTANT. Depoissonization is required.)")

    ok = bridge_ok and all_pos
    print("\nNET: DPP tool applies (Maya quadratic rep exact; occupations determinantal by BOO). The")
    print("route's real difficulty is DEPOISSONIZATION: the poissonized covariance is dominated by")
    print("|λ|-fluctuations (wrong sign); the fixed-n statement needs conditioning on |λ|=n.")
    print(f"\nRESULT: Maya bridge exact + depoissonization obstruction demonstrated: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-A1b-dpp-maya-representation", engine="python-exact")
        w.set_description(
            "DPP route deliverable 1 (qou-x631, qou-g0n2): the Maya-diagram quadratic representation "
            "that makes the Borodin–Okounkov–Olshanski determinantal tool applicable to the covariance "
            "kernel, plus the depoissonization obstruction that is its real difficulty. Encode λ by its "
            "Maya diagram m_a=1_{a∈{λ_i−i}}. EXACT (n≤10): N_v=Σ_a(1−m_a)m_{a+v} (hook=particle-hole "
            "distance, quadratic in m) and ω₃=Σ_v v²N_v−n²−C(n,2) (via Σh²=Σc²+n², quadratic in m). So "
            "Cov(N_v,ω₃) is a covariance of two quadratic statistics; under θ-poissonized Plancherel the "
            "occupations are a DETERMINANTAL point process (discrete-Bessel kernel, BOO math/9905032), "
            "giving a Wick/kernel reduction of Cov(N_v,N_w). OBSTRUCTION (honest finding): the kernel "
            "condition Σ_v ν_v=0 holds at FIXED n because Σ_v N_v=n is constant (|λ|-comovement projected "
            "out); at POISSONIZED level |λ| fluctuates and dominates, so Cov_θ(N_v,Σh²) comes out ALL "
            "POSITIVE (θ=4: +12.5,…,+0.08) — opposite sign. Hence the DPP kernel must be DEPOISSONIZED "
            "(conditioned on |λ|=n) before its sign reflects the fixed-n covariance; that conditioning, "
            "not the kernel algebra, is where the route's difficulty concentrates. Scopes the next "
            "attempt: the |λ|=n-conditioned discrete-Bessel kernel / steepest-descent depoissonization "
            "with |λ|-mean-field subtraction. Establishes the exact bridge + names the obstruction; does "
            "NOT prove the kernel. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("maya_claim1_hook_particle_hole", "N_v = sum_a (1-m_a) m_{a+v}  (exact n<=10)")
        w.add_data("maya_claim2_omega3_quadratic", "omega3 = sum_v v^2 N_v - n^2 - C(n,2)  (exact n<=10)")
        w.add_data("occupations_determinantal", "BOO discrete-Bessel kernel (math/9905032)")
        w.add_data("poissonized_cov_all_positive", bool(all_pos))
        w.add_data("obstruction", "depoissonization: fixed-n Sigma nu=0 (|lambda| const) vs poissonized |lambda|-comovement dominates")
        w.add_data("next_step", "compute |lambda|=n-conditioned discrete-Bessel kernel / depoissonize with |lambda|-mean-field subtraction")
        w.add_assertion(
            "covariance_epic_A1b_dpp_maya_bridge_and_obstruction",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Maya quadratic rep exact (N_v=sum(1-m_a)m_{a+v}, omega3=sum v^2 N_v-n^2-C(n,2), "
                    "n<=10); occupations determinantal (BOO); poissonized Cov_theta(N_v,Sum h^2) all "
                    "positive (|lambda|-comovement dominates) ⇒ depoissonization is the real obstruction. "
                    "Structural bridge + obstruction, not a proof. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
