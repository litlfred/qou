#!/usr/bin/env python3
"""
DERIVE the 4₁ Ohtsuki rungs κ_n symbolically — exact saddle recursion, no PSLQ.

Upgrades the numerically-identified rungs (#3606/#3628: κ₁=(11/108)√3π,
κ₂=(2/27)π², κ₃=(1081/21870)√3π³, κ₄=(98/729)π⁴) from `numerical-exact` to
`symbolic-exact`: they are computed here from first principles (Euler–Maclaurin
+ Laplace at the x*=5/6 saddle) in exact ℚ(√3, π) arithmetic, and the derivation
emits arbitrarily many further rungs (κ₅…κ₈) exactly.

Derivation (all steps standard, no free parameters):

  log J_N(4₁) = log Σ_{k=0}^{N−1} exp(h_N(k)),  h_N(k) = 2 Σ_{j=1}^k g(j/N),
  g(x) = log(2 sin πx).

1. **Euler–Maclaurin on the inner sum** (x = k/N; all k-independent/endpoint
   terms — including the singular j→0 data — collect into the stripped
   normalisation C_N + (3/2)logN + N·Vol/2π and NEVER touch the κ_n):
     h_N(xN) = C_N + 2N·G(x) + g(x) + Σ_{m≥1} 2·B_{2m}/(2m)! · g^{(2m−1)}(x) · N^{1−2m},
   with G(x) = ∫₀ˣ g, so G^{(m)} = g^{(m−1)}.
2. **Poisson summation on the outer sum** (integrand analytic, saddle width
   √N ⇒ non-integral modes are e^{−cN}, exponentially below every κ_n):
     Σ_k → N ∫ dx.
3. **Laplace at the interior maximum x* = 5/6** (g(x*)=0, G''(x*)=g'(x*)=−√3π):
   substitute x = x* + εv, ε = 1/√N; Gaussian weight exp(−√3π v²); expand
   everything beyond the Gaussian in ε with EXACT coefficients (sympy, √3 and π
   symbolic — sin(5π/6)=1/2 and cos(5π/6)=−√3/2 are exact); average with
   Gaussian moments ⟨v^{2j}⟩ = (2j−1)!!/(2√3π)^j; take log; collect ε^{2n}.

Every input is exact: g-derivatives at x* ∈ ℚ(√3)·π^m, Bernoulli numbers ∈ ℚ,
Gaussian moments ∈ ℚ·(√3π)^{−j}. Hence κ_n ∈ ℚ(√3)·π^n *by construction* — the
parity alternation and the 3-power denominators fall out, they are not assumed.

KILL CRITERIA (hard assertions): the derived κ₁…κ₄ must equal the four
independently PSLQ-identified values (36/30/25/19 confirmed digits, #3628), and
the derived κ₅, κ₆ must match the numerical extractions 84.6421656… [14d] /
676.946679… [10d]. A derivation that "almost" matches is a FAIL.

DISCIPLINE: 4₁-Kashaev/Ohtsuki topology; NOT wired Q_β c_k; no fit; no tier
change to any Q_β rung (the κ_n tier upgrade is internal to the even channel).
"""
import datetime
import hashlib
import json
import os
import subprocess
from fractions import Fraction

import mpmath as mp
import sympy as sp


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
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e})") from e
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def derive_kappas(M):
    """Return {n: exact sympy κ_n} for n = 1..M via the symbolic saddle recursion."""
    x = sp.Symbol('x')
    v = sp.Symbol('v')
    eps = sp.Symbol('epsilon')          # ε = 1/√N
    ORD = 2 * M + 1                     # work modulo ε^(2M+1)

    g = sp.log(2 * sp.sin(sp.pi * x))
    xstar = sp.Rational(5, 6)

    # g^{(m)}(x*) exact, m = 0..(2M+2): enough for the ε^{2M} truncation.
    max_der = 2 * M + 3
    gders = [sp.simplify(sp.diff(g, x, m).subs(x, xstar)) for m in range(max_der + 1)]
    assert gders[0] == 0, "g(x*) must vanish (2 sin(5π/6) = 1)"
    assert sp.simplify(gders[1] + sp.sqrt(3) * sp.pi) == 0, "g'(x*) must be −√3π"

    # R(v, ε) = everything in the exponent beyond the Gaussian, at x = x* + εv:
    #   (a) 2N·G tail:  2 Σ_{m≥3} G_m (εv)^m / m! · N = 2 Σ_{m≥3} g^{(m−1)}(x*) v^m ε^{m−2}/m!
    #   (b) prefactor:  g(x* + εv) = Σ_{m≥1} g^{(m)}(x*) (εv)^m / m!
    #   (c) EM tail:    Σ_{m≥1} 2 B_{2m}/(2m)! g^{(2m−1)}(x* + εv) ε^{2(2m−1)}
    R = sp.Integer(0)
    for m in range(3, 2 * M + 3):                       # (a): ε^{m−2} ≤ ε^{2M}
        R += 2 * gders[m - 1] * v**m * eps**(m - 2) / sp.factorial(m)
    for m in range(1, 2 * M + 1):                       # (b): ε^m ≤ ε^{2M}
        R += gders[m] * v**m * eps**m / sp.factorial(m)
    for em in range(1, M + 1):                          # (c): base ε^{2(2em−1)}
        base_pow = 2 * (2 * em - 1)
        if base_pow > 2 * M:
            break
        coeff = 2 * sp.bernoulli(2 * em) / sp.factorial(2 * em)
        # g^{(2em−1)}(x* + εv) expanded to the residual ε order
        rem = 2 * M - base_pow
        expand = sum(gders[2 * em - 1 + j] * (eps * v)**j / sp.factorial(j)
                     for j in range(rem + 1))
        R += coeff * expand * eps**base_pow
    R = sp.expand(R)

    def trunc(p):
        return sp.expand(p + sp.O(eps**ORD, eps)).removeO()

    R = trunc(R)

    # exp(R) modulo ε^{2M+1}: R = O(ε), so k ≤ 2M terms suffice.
    expR = sp.Integer(1)
    term = sp.Integer(1)
    for k in range(1, 2 * M + 1):
        term = trunc(sp.expand(term * R / k))
        if term == 0:
            break
        expR += term
    expR = trunc(expR)

    # Gaussian average over v with weight exp(−√3π v²), a = √3π:
    # ⟨v^{2j}⟩ = (2j−1)!! / (2a)^j;  odd moments vanish.
    a = sp.sqrt(3) * sp.pi
    poly = sp.Poly(expR, v)
    F = sp.Integer(0)
    for monom, coeff in zip(poly.monoms(), poly.coeffs()):
        p = monom[0]
        if p % 2 == 1:
            continue
        j = p // 2
        F += coeff * sp.factorial2(2 * j - 1) / (2 * a)**j
    F = trunc(sp.expand(F))

    # D-series = log F  (the stripped normalisation eats the Gaussian norm etc.)
    logF = sp.Integer(0)
    Fm1 = trunc(sp.expand(F - 1))
    term = sp.Integer(1)
    # log(1+w) = Σ (−1)^{k+1} w^k / k, w = F−1 = O(ε²) ⇒ k ≤ M terms.
    w = Fm1
    poww = sp.Integer(1)
    for k in range(1, M + 1):
        poww = trunc(sp.expand(poww * w)) if k > 1 else w
        logF += sp.Integer((-1)**(k + 1)) * poww / k
    logF = trunc(sp.expand(logF))

    kappas = {}
    for n in range(1, M + 1):
        # radsimp+cancel keep the exact ℚ(√3)·π^n form; do NOT use nsimplify
        # (its heuristic search can mangle large exact rationals into bogus
        # radicals — observed on κ₈).
        kappas[n] = sp.radsimp(sp.cancel(sp.together(logF.coeff(eps, 2 * n))))
    return kappas


def main():
    M = 8
    print(f"symbolic saddle recursion to κ_{M} (exact ℚ(√3,π) arithmetic) ...")
    kappas = derive_kappas(M)

    s3, pi = sp.sqrt(3), sp.pi
    known = {
        1: sp.Rational(11, 108) * s3 * pi,
        2: sp.Rational(2, 27) * pi**2,
        3: sp.Rational(1081, 21870) * s3 * pi**3,
        4: sp.Rational(98, 729) * pi**4,
    }
    numeric_checks = {5: ("84.6421656050384435", 13), 6: ("676.946678964105031", 9)}

    rows = {}
    all_ok = True
    for n in range(1, M + 1):
        kn = kappas[n]
        # express as r·√3·π^n (odd) or r·π^n (even) if possible
        gen = s3 * pi**n if n % 2 == 1 else pi**n
        r = sp.cancel(sp.radsimp(kn / gen))
        is_rat = r.is_rational
        rows[n] = {"kappa_exact": str(kn), "rational_over_generator": str(r),
                   "generator": ("sqrt3*pi^%d" % n if n % 2 == 1 else "pi^%d" % n),
                   "parity_clean": bool(is_rat)}
        tag = f"= ({r})·{'√3π^%d' % n if n % 2 == 1 else 'π^%d' % n}" if is_rat \
            else f"= {kn}  (NOT a clean parity multiple)"
        print(f"  κ_{n} {tag}")
        if not is_rat:
            all_ok = False

    # KILL CRITERIA
    assertions = []
    for n, val in known.items():
        ok = sp.simplify(kappas[n] - val) == 0
        assertions.append({"name": f"kappa{n}_matches_pslq_identified", "passed": bool(ok)})
        print(f"  kill κ_{n} == PSLQ value: {ok}")
    for n, (num_str, digs) in numeric_checks.items():
        dv = mp.mpf(str(sp.N(kappas[n], 30)))
        ok = abs(dv - mp.mpf(num_str)) < mp.mpf(10) ** (-digs + 1)
        assertions.append({"name": f"kappa{n}_matches_numerical_{digs}d", "passed": bool(ok)})
        print(f"  kill κ_{n} ≈ numerical [{digs}d]: {ok}  (derived {mp.nstr(dv, 18)})")
    assertions.append({"name": "all_rungs_parity_clean", "passed": bool(all_ok)})
    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        f"DERIVED (symbolic-exact). The 4₁ Ohtsuki rungs κ_1..κ_{M} are computed "
        "from first principles (Euler–Maclaurin inner sum + Poisson outer sum + "
        "Laplace at x*=5/6) in exact ℚ(√3,π) arithmetic with no numerical input and "
        "no PSLQ. κ₁..κ₄ REPRODUCE the independently PSLQ-identified values "
        "(11/108·√3π, 2/27·π², 1081/21870·√3π³, 98/729·π⁴) — upgrading them from "
        "numerical-exact to symbolic-exact — and κ₅, κ₆ match the numerical "
        "extractions to their attained digits, with κ₅..κ₈ now EXACT (beyond any "
        "extraction precision). The √3-parity alternation and 3-power denominators "
        "are consequences of the derivation (cot(5π/6)=−√3 Taylor data + rational "
        "Bernoulli/moment arithmetic), not assumptions. Scope: 4₁-Kashaev/Ohtsuki "
        "topology; NOT wired Q_β c_k; the 4₁↔Q_β bridge (Borel/Φ_b continuation) "
        "remains open. No fit; no c_k value; no tier change on any Q_β rung."
        if all_passed else
        "DERIVATION MISMATCH — at least one kill criterion failed; do NOT trust "
        "the emitted rungs; debug the EM/Laplace bookkeeping before any use."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-symbolic-saddle",
        "description": "First-principles symbolic derivation (EM + Poisson + Laplace, "
                       "exact ℚ(√3,π)) of the 4₁ Ohtsuki rungs κ_1..κ_8; kill-checked "
                       "against the PSLQ-identified κ₁..κ₄ and numerical κ₅/κ₆.",
        "audit_only": True,
        "tier": "symbolic-exact (derivation)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy+mpmath",
        "engineVersion": f"sympy {sp.__version__}, mpmath {mp.__version__}",
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"rungs": rows, "verdict": verdict},
        "context": {
            "axis": "z->c_k f-map keystone: even channel, symbolic saddle recursion",
            "upgrades": "kappa_1..4 numerical-exact -> symbolic-exact (even-channel internal)",
            "new_exact": "kappa_5..kappa_8",
            "bridge_status": "open (Borel/Phi_b continuation; growth-class obstruction #3628)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-symbolic-saddle.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
