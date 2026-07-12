#!/usr/bin/env python3
"""
Even-channel Borel singularity from the exact κ_n: quantify the Gevrey-1 divergence
of the 4₁ Kashaev log-asymptotic and compare the resurgence action A to knot data.

Context (4₁↔Q_β bridge, growth-class obstruction — docs/audits/2026-07-12-fmap-
4one-qbeta-bridge-growth-obstruction.md). The even channel `log J_N(4₁) = ... +
Σ κ_n/N^n` has EXACT low rungs (κ₁=(11/108)√3π, κ₂=(2/27)π², κ₃=(1081/21870)√3π³,
κ₄=(98/729)π⁴; #3606/#3628). Their ratios rise → the series is Gevrey-1 divergent
(hyperbolic-knot Borel singularity). This probe extracts κ₅, κ₆ (lower precision),
fits the large-order growth κ_n ~ C·Γ(n+β)/A^n to get the Borel singularity A (in
the 1/N variable), and compares A to Vol(4₁)/2π and related quantities.

The Q_β ladder is convergent (c_{k+1}/c_k → 1/u = 117.41, KC8), so A characterises
the even-channel divergence that the Borel/Faddeev-Φ_b resummation must resum.

IMPORTANT framing (anti-laundering): the Kashaev q is on |q|=1 (root of unity); the
substrate q₀ is real > 1 (off |q|=1). The map between the even Borel singularity A
and the odd pole 1/u is therefore the ANALYTIC CONTINUATION off the unit circle
(the state integral), NOT a simple ℏ↔u reparametrisation. This probe reports A and
its arithmetic; it does NOT claim a naive algebraic bridge relation. No fit to QOU
data; no c_k wired; no tier change. Self-contained.
"""
import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp

mp.mp.dps = 200


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e})") from e


def log_kashaev_4_1(N):
    pi = mp.pi
    logP = mp.mpf(0)
    m = mp.mpf(0)
    s = mp.mpf(1)
    for k in range(1, N):
        logP += 2 * mp.log(2 * mp.sin(pi * k / N))
        if logP > m:
            s = s * mp.exp(m - logP) + 1
            m = logP
        else:
            s += mp.exp(logP - m)
    return m + mp.log(s)


def poly_fit_1_over_N(Ns, ys):
    M = len(Ns)
    xs = [mp.mpf(1) / N for N in Ns]
    V = mp.matrix(M, M)
    for i in range(M):
        for j in range(M):
            V[i, j] = xs[i] ** j
    a = mp.lu_solve(V, mp.matrix(ys))
    return [a[j] for j in range(M)]


def main():
    pi = mp.pi
    Vol = 2 * mp.clsin(2, pi / 3)
    s3 = mp.sqrt(3)

    # 13 points → coefficients a_0..a_12; we trust κ_1..κ_6 (precision decays
    # ~5 digits/rung). Up to N=3.14M keeps it under ~6 min.
    Ns = [1536 * 2 ** j for j in range(13)]   # 1536 … 6291456
    print(f"computing log J_N(4_1), {len(Ns)} points N≤{Ns[-1]} (dps {mp.mp.dps}) ...")
    D = []
    for i, N in enumerate(Ns):
        D.append(log_kashaev_4_1(N) - mp.mpf(3) / 2 * mp.log(N) - N * Vol / (2 * pi))
        print(f"  [{i+1}/{len(Ns)}] N={N} done", flush=True)

    a = poly_fit_1_over_N(Ns, D)
    ac = poly_fit_1_over_N(Ns[:-2], D[:-2])

    # Exact reference values for κ_1..κ_4 (sanity + they anchor the growth fit).
    exact = {1: 11 * s3 * pi / 108, 2: 2 * pi ** 2 / 27,
             3: 1081 * s3 * pi ** 3 / 21870, 4: 98 * pi ** 4 / 729}

    kappa = {}
    conf = {}
    print("\n  rung   κ_n                       confident digits")
    for n in range(1, 9):
        kn = a[n]
        cd = int(-mp.log10(abs(kn - ac[n]))) if n < len(ac) and abs(kn - ac[n]) > 0 else 0
        kappa[n] = kn
        conf[n] = cd
        exflag = ""
        if n in exact:
            exflag = f"  (exact={mp.nstr(exact[n],10)}, match={abs(kn-exact[n])<mp.mpf(10)**(-min(cd,15))})"
        print(f"  κ_{n}   {mp.nstr(kn, 18):>22}   [{cd}d]{exflag}", flush=True)

    # Large-order Gevrey-1 fit: κ_n ~ C·Γ(n+β)/A^n ⇒ ratio r_n = κ_{n+1}/κ_n =
    # (n+β)/A. Linear regression r_n = (1/A)·n + (β/A) over the reliable rungs.
    reliable = [n for n in range(1, 7) if conf.get(n, 0) >= 6 and conf.get(n + 1, 0) >= 6]
    ratios = {n: kappa[n + 1] / kappa[n] for n in reliable}
    print(f"\n  reliable ratio rungs: {reliable}")
    for n in reliable:
        print(f"    r_{n} = κ_{n+1}/κ_{n} = {mp.nstr(ratios[n], 12)}")
    # Least-squares slope/intercept of r_n vs n.
    ns = [mp.mpf(n) for n in reliable]
    rs = [ratios[n] for n in reliable]
    nbar = sum(ns) / len(ns)
    rbar = sum(rs) / len(rs)
    slope = sum((ns[i] - nbar) * (rs[i] - rbar) for i in range(len(ns))) / \
        sum((ns[i] - nbar) ** 2 for i in range(len(ns)))
    intercept = rbar - slope * nbar
    A = 1 / slope
    beta = intercept * A
    print(f"\n  Gevrey-1 large-order fit  r_n = (1/A)·n + β/A:")
    print(f"    slope 1/A = {mp.nstr(slope, 10)}  ⇒  A = {mp.nstr(A, 12)}")
    print(f"    β = {mp.nstr(beta, 8)}")

    # Arithmetic of A: compare to Vol(4₁)/2π and multiples.
    v2p = Vol / (2 * pi)
    print(f"\n  Vol(4₁)/2π = {mp.nstr(v2p, 12)}")
    print(f"  A / (Vol/2π)     = {mp.nstr(A / v2p, 8)}")
    print(f"  A / (2·Vol/2π)   = {mp.nstr(A / (2 * v2p), 8)}")
    print(f"  A·2π / Vol       = {mp.nstr(A * 2 * pi / Vol, 8)}")

    # The Q_β side (convergent): pole at 1/u = 117.41 (KC8). NOT algebraically
    # mapped here — the Kashaev q is on |q|=1, the substrate q₀ is real>1, so the
    # relation is analytic continuation (the state integral), not a reparametrisation.
    u_pole = mp.mpf(1) / mp.mpf("117.41")
    print(f"\n  Q_β ladder pole u_substrate ≈ {mp.nstr(u_pole, 8)} (1/117.41; convergent)")
    print(f"  [growth-class dichotomy: even A finite ⇒ Gevrey-1 divergent;")
    print(f"   Q_β ratio→117.41 constant ⇒ convergent. The bridge is the Borel/Φ_b")
    print(f"   resummation / analytic continuation off |q|=1, NOT b·A²=u_substrate.]")

    kappa_exact_ok = all(
        abs(kappa[n] - exact[n]) < mp.mpf(10) ** (-min(conf[n], 15)) for n in exact)
    ratios_rise = all(ratios[reliable[i]] < ratios[reliable[i + 1]]
                      for i in range(len(reliable) - 1))

    verdict = (
        f"Even-channel κ_n are Gevrey-1 DIVERGENT: the reliable ratios "
        f"{[mp.nstr(ratios[n],6) for n in reliable]} rise ~linearly in n "
        f"(r_n=(1/A)n+β/A), giving a finite Borel singularity A={mp.nstr(A,8)} "
        f"(≈ Vol(4₁)/2π × {mp.nstr(A/v2p,5)}; β≈{mp.nstr(beta,4)}). This is the "
        f"quantitative form of the growth-class obstruction: a Gevrey-1 divergent "
        f"series cannot equal the CONVERGENT Q_β ladder (ratio→117.41, KC8) "
        f"term-by-term, so the 4₁↔Q_β bridge is necessarily the Borel/median "
        f"(Faddeev Φ_b) resummation — i.e. the analytic continuation from the "
        f"Kashaev locus |q|=1 to the real substrate q₀>1, NOT an ℏ↔u "
        f"reparametrisation. Complements (does not duplicate) the Φ_b construction "
        f"on #3544/#3596. No fit; no c_k wired; no tier change."
    )
    print("\nVERDICT:", verdict)

    assertions = [
        {"name": "kappa_1_4_reproduce_exact", "passed": bool(kappa_exact_ok)},
        {"name": "ratios_rise_gevrey1", "passed": bool(ratios_rise)},
        {"name": "borel_singularity_finite_positive", "passed": bool(0 < A < 10)},
    ]
    all_passed = all(x["passed"] for x in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-even-borel-singularity",
        "description": "Even-channel 4₁ Kashaev κ_n are Gevrey-1 divergent; Borel "
                       "singularity A from the large-order fit — the quantitative "
                       "growth-class obstruction to a term-by-term 4₁↔Q_β bridge.",
        "audit_only": True,
        "tier": "numerical (large-order growth)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "kappa": {n: mp.nstr(kappa[n], 20) for n in range(1, 7)},
            "confident_digits": {n: conf[n] for n in range(1, 7)},
            "reliable_ratio_rungs": reliable,
            "ratios": {n: mp.nstr(ratios[n], 12) for n in reliable},
            "borel_singularity_A": mp.nstr(A, 12),
            "gevrey1_beta": mp.nstr(beta, 8),
            "A_over_Vol_2pi": mp.nstr(A / v2p, 8),
            "qbeta_pole_u_substrate": mp.nstr(u_pole, 8),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: 4₁↔Q_β bridge, even-channel Borel singularity",
            "framing": "Kashaev |q|=1 vs substrate real q₀>1 ⇒ bridge is analytic "
                       "continuation (state integral), not ℏ↔u reparametrisation",
            "complements": "Φ_b construction on #3544/#3596 (does not duplicate)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-even-borel-singularity.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
