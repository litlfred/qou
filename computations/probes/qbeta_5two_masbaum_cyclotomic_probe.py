#!/usr/bin/env python3
"""qbeta_5two_masbaum_cyclotomic_probe.py — AUTHORITATIVE 5₂ cyclotomic
coefficients C_{5_2,n}(q) from Masbaum's twist-knot formula (masbaum2003),
replacing the self-calibrating (V_{5_2}-1)/(V_{4_1}-1) heuristic with the cited
source, and CROSS-CHECKING that the heuristic was in fact correct.

CONTEXT (b3ix odd-locus; #3966, #3993). The odd-channel Habiro datum of the
Q_β resurgence is located in the bar-asymmetry of the cyclotomic coefficient
C_{K,n} (Lean: HabiroCyclotomicOddLocus). For the chiral knot 5₂ = K_2 (twist
knot, 2 full twists) the leading coefficient was first extracted by a
self-calibrating ratio; the owner flagged that heuristic ("colored jones gate
maybe from erroneous probes. be critical"). This probe answers the challenge
with the AUTHORITATIVE reference: G. Masbaum, "Skein-theoretical derivation of
some formulas of Habiro", Algebr. Geom. Topol. 3 (2003) 537–556
[masbaum2003, DOI 10.2140/agt.2003.3.537], now on main (library/agt-v3-n1-p17-p/agt-v3-n1-p17-p.pdf).

MASBAUM Theorem 4.5 (Habiro [H3]) + Theorem 5.1 + Remark 5.2, specialised p=2:
  c'_{n,2}   = (-1)^n a^{(5n²+7n)/2} Σ_{k=0}^n a^{k²-2k-3nk} [n,k]_a   (a-binomial)
  f_{K2,n}   = a^{n(n+3)/2} c'_{n,2}                       (Thm 5.1)
  f̃_{K2,n}  = (-1)^n q^{-n(n+1)/2} f_{K2,n},  q = a²        (Remark 5.2)
so J'_{5_2}(N) = Σ_n f̃_{K2,n} (q^{1-N})_n (q^{1+N})_n.

BASIS BRIDGE (derived, verified on 4₁). The framework's Kashaev-tail basis is
f_n(q) = (q;q)_n (q^{-1};q^{-1})_n (bar-even), NOT Masbaum's color-dependent
(q^{1-N})_n(q^{1+N})_n → (q;q)_n² at the Kashaev point q^N=1. Since
(q^{-1};q^{-1})_n / (q;q)_n = ∏(1-q^{-j})/(1-q^j) = (-1)^n q^{-n(n+1)/2}, the two
bases give the SAME tail with
  C_{K,n}(q) = (-1)^n q^{n(n+1)/2} · f̃_{K,n}(q).
Check: for 4₁ = K_{-1}, f̃_{4_1,n} = (-1)^n q^{-n(n+1)/2} ⇒ C_n = 1 (Kashaev's
figure-eight, C_n=1) — the bridge is validated exactly on the amphichiral knot.

CRITICAL CROSS-CHECKS (all must pass):
  1. Masbaum's coefficients reproduce the STANDARD Jones polynomial V_{5_2}(t)
     at N=2 (KnotInfo value), fixing the variable convention t = q^{-1}.
  2. The bridge gives C_n=1 for 4₁ at every n (Kashaev consistency).
  3. The self-calibrating shortcut C_{5_2,1} = -(t^{-2}+t^{-4}) at t=q^{-1}
     EQUALS the Masbaum-derived C_{5_2,1}(q) = -(q⁴+q²) — the heuristic survives.
  4. C_{5_2,n} is bar-ASYMMETRIC for n≥1 (chirality) — nonzero odd datum.

AUTHORITATIVE RESULT (this replaces the heuristic as the source of record):
  C_{5_2,0}(q) = 1
  C_{5_2,1}(q) = -(q⁴+q²)
  C_{5_2,2}(q) = q¹¹+q⁸+q⁷+q⁵
  C_{5_2,3}(q) = -(q²¹+q¹⁷+q¹⁶+q¹⁵+q¹³+q¹²+q¹¹+q⁹)

scope-(b): exact Laurent-polynomial identities from a cited published formula,
cross-checked against the standard Jones polynomial. NO fit; NO c_k wired.

Run: python3 -u computations/probes/qbeta_5two_masbaum_cyclotomic_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_masbaum.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

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
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


a = sp.symbols("a")            # a = A²  (Masbaum)
q = a ** 2                     # q = a² = A⁴  (Masbaum Remark 5.2)


def qint(m):
    return (a ** m - a ** (-m)) / (a - a ** (-1))


def qfact(m):
    r = sp.Integer(1)
    for i in range(1, m + 1):
        r *= qint(i)
    return r


def qbinom(n, k):              # Gaussian binomial in a
    if k < 0 or k > n:
        return sp.Integer(0)
    return sp.simplify(qfact(n) / (qfact(k) * qfact(n - k)))


def c_prime_n2(n):             # Masbaum (46), p=2 example
    s = sp.Integer(0)
    for k in range(0, n + 1):
        s += a ** (k ** 2 - 2 * k - 3 * n * k) * qbinom(n, k)
    return sp.simplify((-1) ** n * a ** sp.Rational(5 * n ** 2 + 7 * n, 2) * s)


def ftilde_K2(n):              # f̃_{K2,n} = (-1)^n q^{-n(n+1)/2} a^{n(n+3)/2} c'
    fK = a ** sp.Rational(n * (n + 3), 2) * c_prime_n2(n)
    return sp.simplify((-1) ** n * q ** sp.Rational(-n * (n + 1), 2) * fK)


def C_framework(n, ftil):      # bridge: C_{K,n} = (-1)^n q^{n(n+1)/2} f̃_{K,n}
    return sp.expand(sp.simplify((-1) ** n * q ** sp.Rational(n * (n + 1), 2) * ftil))


def qpoch(x, n):
    r = sp.Integer(1)
    for j in range(n):
        r *= (1 - x * q ** j)
    return r


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" AUTHORITATIVE 5₂ cyclotomic coefficients from Masbaum (masbaum2003)")
    print("=" * 78)

    ftil = {n: ftilde_K2(n) for n in range(0, 4)}
    Cfw = {n: C_framework(n, ftil[n]) for n in range(0, 4)}
    print("\n  Masbaum f̃_{K2,n} and framework C_{5_2,n}(q):")
    for n in range(0, 4):
        print(f"    n={n}: f̃={ftil[n]}   →   C_(5_2,{n})={Cfw[n]}")

    # (1) Masbaum reproduces the standard Jones V_{5_2} at N=2 (t = q^{-1})
    t = sp.symbols("t")
    V52 = t**(-1) - t**(-2) + 2*t**(-3) - t**(-4) + t**(-5) - t**(-6)   # KnotInfo
    J52_N2 = sp.simplify(
        ftil[0]*qpoch(q**(1-2), 0)*qpoch(q**(1+2), 0)
        + ftil[1]*qpoch(q**(1-2), 1)*qpoch(q**(1+2), 1))
    match_N2 = sp.simplify(J52_N2 - V52.subs(t, 1/q)) == 0
    print(f"\n  (1) J'_5₂(N=2) − V_5₂(t=q⁻¹) = "
          f"{sp.simplify(J52_N2 - V52.subs(t, 1/q))}")
    check("masbaum_reproduces_jones_5two_at_N2", match_N2,
          source="Masbaum Thm 5.1/Rem 5.2 for K_2 reproduces the standard "
                 "KnotInfo Jones polynomial V_{5_2}(t) at N=2 under t=q⁻¹ — "
                 "validates the cyclotomic coefficients against an independent "
                 "authoritative value (masbaum2003, DOI 10.2140/agt.2003.3.537)")

    # (2) bridge gives C_n=1 for 4₁ at every n (Kashaev consistency)
    c41_ok = True
    for n in range(0, 4):
        f41 = sp.simplify((-1)**n * q**sp.Rational(-n*(n+1), 2))       # Masbaum 4₁
        C41 = C_framework(n, f41)
        c41_ok = c41_ok and (sp.simplify(C41 - 1) == 0)
    print(f"  (2) 4₁ bridge C_n = 1 for n=0..3: {c41_ok}")
    check("bridge_gives_C_n_one_for_fourone", c41_ok,
          source="the derived basis bridge C_{K,n}=(-1)^n q^{n(n+1)/2}·f̃_{K,n} "
                 "maps Masbaum's f̃_{4_1,n}=(-1)^n q^{-n(n+1)/2} to C_n=1, "
                 "matching Kashaev's figure-eight tail — the bridge is exact")

    # (3) the self-calibrating shortcut matches Masbaum (the critical test)
    shortcut_q = sp.expand((-(t**(-2) + t**(-4))).subs(t, 1/q))
    shortcut_ok = sp.simplify(shortcut_q - Cfw[1]) == 0
    print(f"  (3) shortcut C_(5_2,1)@t=q⁻¹ = {shortcut_q}  vs Masbaum "
          f"{Cfw[1]}  →  match={shortcut_ok}")
    check("selfcalibrating_shortcut_matches_masbaum", shortcut_ok,
          source="the earlier self-calibrating (V_{5_2}-1)/(V_{4_1}-1) heuristic "
                 "gave C_{5_2,1}=-(t⁻²+t⁻⁴); at t=q⁻¹ this equals the "
                 "authoritative Masbaum-derived C_{5_2,1}(q)=-(q⁴+q²) EXACTLY — "
                 "the flagged 'colored-jones gate' heuristic is validated, not "
                 "erroneous")

    # (4) bar-asymmetry (chirality) for n≥1
    bar_asym = True
    for n in (1, 2, 3):
        asym = sp.simplify(Cfw[n] - Cfw[n].subs(a, 1/a))
        bar_asym = bar_asym and (asym != 0)
    print(f"  (4) C_(5_2,n) bar-asymmetric for n=1,2,3: {bar_asym}")
    check("cyclotomic_coeff_bar_asymmetric", bar_asym,
          source="C_{5_2,n}(q) ≠ C_{5_2,n}(q⁻¹) for n≥1 — 5₂ is chiral, so its "
                 "cyclotomic coefficients supply a nonzero bar-odd Habiro datum "
                 "(the odd-locus, Lean HabiroCyclotomicOddLocus)")

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        ("VALIDATED + AUTHORITATIVE. Masbaum's twist-knot formula (masbaum2003) "
         "gives the exact 5₂ = K_2 cyclotomic coefficients; they reproduce the "
         "standard Jones polynomial V_{5_2} at N=2. The derived basis bridge "
         "C_{K,n}=(-1)^n q^{n(n+1)/2}·f̃_{K,n} is exact (C_n=1 on 4₁). The earlier "
         "self-calibrating (V_{5_2}-1)/(V_{4_1}-1) heuristic — flagged by the "
         "owner as a possibly-erroneous probe — MATCHES the authoritative "
         "C_{5_2,1}(q)=-(q⁴+q²) exactly, so it stands. Authoritative higher "
         "coefficients: C_{5_2,2}=q¹¹+q⁸+q⁷+q⁵, "
         "C_{5_2,3}=-(q²¹+q¹⁷+q¹⁶+q¹⁵+q¹³+q¹²+q¹¹+q⁹). All bar-asymmetric — the "
         "5₂ bar-odd Habiro datum for the Q_β odd channel. "
         if all_passed else
         "PARTIAL: a cross-check failed — see the per-check table; do NOT treat "
         "the coefficients as authoritative until resolved. ")
        + "scope-(b): exact Laurent-polynomial identities from a cited published "
        "formula. NO fit; NO c_k wired."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-5two-masbaum-cyclotomic",
        "description": "Authoritative 5₂=K_2 cyclotomic coefficients C_{5_2,n}(q) "
                       "from Masbaum's twist-knot formula (masbaum2003), via the "
                       "derived Kashaev-tail basis bridge C_{K,n}=(-1)^n "
                       "q^{n(n+1)/2} f̃_{K,n}. Reproduces V_{5_2} at N=2; the "
                       "self-calibrating heuristic matches exactly. scope-(b).",
        "audit_only": True,
        "tier": "symbolic-exact (cited authoritative formula)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "C_5two": {str(n): str(sp.expand(Cfw[n])) for n in range(0, 4)},
            "ftilde_K2": {str(n): str(ftil[n]) for n in range(0, 4)},
            "basis_bridge": "C_{K,n}(q) = (-1)^n q^{n(n+1)/2} f~_{K,n}(q)",
            "verdict": verdict,
        },
        "context": {
            "axis": "b3ix odd-locus — authoritative 5₂ coefficient (continuation "
                    "of #3970/#3993; answers 'be critical' colored-jones gate)",
            "reference": "masbaum2003 (DOI 10.2140/agt.2003.3.537); "
                         "library/agt-v3-n1-p17-p/agt-v3-n1-p17-p.pdf",
            "lean": "QOU.QBeta.HabiroCyclotomicOddLocus (c52_1/c52_2/c52_3, "
                    "sorry-free)",
            "supports": "#3966 b3ix",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-5two-masbaum-cyclotomic.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
