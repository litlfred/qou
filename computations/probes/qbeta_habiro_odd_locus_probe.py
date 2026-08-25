#!/usr/bin/env python3
"""qbeta_habiro_odd_locus_probe.py — the odd-channel Habiro datum lives in the
bar-asymmetry of the cyclotomic coefficient C_{K,n}(q).

CONTEXT (b3ix continuation; #3966). The 4₁ Habiro tail is bar-even (#3970,
Lean-proved) — no odd datum. The general Kashaev/Habiro tail is
  S_K(q) = Σ_n C_{K,n}(q) · f_n(q),   f_n(q) = ∏_{j=1}^n (1-q^j)(1-q^{-j}),
and f_n is bar-even (each factor is q↔q⁻¹ invariant). Hence the entire bar-odd
(q↔q⁻¹ antisymmetric) content of the tail is carried by the coefficient:
  C_n(q)·f_n(q) − C_n(q⁻¹)·f_n(q⁻¹) = (C_n(q) − C_n(q⁻¹))·f_n(q).
So the Q_β odd-channel resurgence is located precisely in the bar-asymmetry of
C_{K,n}. For 4₁, C_n=1 (bar-symmetric) ⇒ zero odd datum; for a chiral knot,
C_{K,n}(q)≠C_{K,n}(q⁻¹) supplies it. This probe verifies the identity numerically
and demonstrates: (i) 4₁ (C=1) is bar-even; (ii) a bar-ASYMMETRIC coefficient
produces a nonzero bar-odd tail proportional to its asymmetry.

The Lean proofs are in QOU/QBeta/HabiroCyclotomicOddLocus (lean-direct exit 0,
sorry-free): habiroTerm_bar_odd_eq_coeff_asymmetry,
habiroTerm_bar_even_of_coeff_symmetric, fourOne_habiroTerm_bar_even.

HONEST SCOPE. This LOCATES the odd datum; it does not compute the 5₂ odd action —
that needs the explicit 5₂ cyclotomic coefficient C_{5_2,n} (Masbaum's twist-knot
formula), which must be derived from that reference, not invented. scope-(b)
(a proved q↔q⁻¹ symmetry identity). No c_k; no fit.

Run: python3 -u computations/probes/qbeta_habiro_odd_locus_probe.py \\
       2>&1 | tee /tmp/qbeta_odd_locus.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


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


def factor(q, j):
    p = mp.mpf(1)
    for k in range(1, j + 1):
        p *= (1 - q ** k) * (1 - q ** -k)
    return p


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" Habiro odd-locus: the odd datum is the cyclotomic-coefficient asymmetry")
    print("=" * 78)

    q = mp.mpf("1.11")

    # (1) the identity  C(q)f(q) − C(q⁻¹)f(q⁻¹) = (C(q) − C(q⁻¹))·f(q)
    print("\n  identity  C(q)f(q) − C(q⁻¹)f(q⁻¹) = (C(q)−C(q⁻¹))·f(q):")
    max_err = mp.mpf(0)
    for (Cq, Cqi) in ((mp.mpf("1.7"), mp.mpf("-0.4")),
                      (mp.mpf("0.3"), mp.mpf("0.3")),
                      (mp.mpf("-2.1"), mp.mpf("1.6"))):
        for j in (1, 3, 5, 8):
            lhs = Cq * factor(q, j) - Cqi * factor(1 / q, j)
            rhs = (Cq - Cqi) * factor(q, j)
            max_err = max(max_err, abs(lhs - rhs))
    print(f"    max |LHS − RHS| over samples = {mp.nstr(max_err, 4)}")
    check("odd_locus_identity", max_err < mp.mpf(10) ** (-30),
          source="C(q)f(q)−C(q⁻¹)f(q⁻¹)=(C(q)−C(q⁻¹))·f(q) exactly, since the "
                 "factor f is bar-even — the odd datum is the coefficient's "
                 "bar-asymmetry (Lean: habiroTerm_bar_odd_eq_coeff_asymmetry)")

    # (2) 4₁ (C ≡ 1, bar-symmetric): zero bar-odd datum
    odd_41 = max(abs(mp.mpf(1) * factor(q, j) - mp.mpf(1) * factor(1 / q, j))
                 for j in (1, 3, 5, 8))
    print(f"\n  4₁ (C=1): max bar-odd part = {mp.nstr(odd_41, 4)} (expect 0)")
    check("fourone_bar_even_zero_odd", odd_41 < mp.mpf(10) ** (-30),
          source="C_n=1 is bar-symmetric ⇒ zero bar-odd Habiro datum (bar-even "
                 "tail; the #3970 π²/5 action is entirely bar-even)")

    # (3) a bar-ASYMMETRIC coefficient produces a nonzero bar-odd tail ∝ asymmetry
    #     (toy chiral C_n(q) = q^{-n}; NOT the 5₂ coefficient — mechanism demo)
    def Ctoy(qq, n):
        return qq ** (-n)
    print("\n  toy chiral C_n(q)=q^{-n} (bar-asymmetric): bar-odd tail nonzero:")
    nonzero = True
    for n in (1, 3, 5):
        odd = Ctoy(q, n) * factor(q, n) - Ctoy(1 / q, n) * factor(1 / q, n)
        pred = (Ctoy(q, n) - Ctoy(1 / q, n)) * factor(q, n)
        ok = abs(odd - pred) < mp.mpf(10) ** (-30) and abs(odd) > mp.mpf("1e-6")
        nonzero = nonzero and ok
        print(f"    n={n}: bar-odd term = {mp.nstr(odd, 6)} = "
              f"(C(q)−C(q⁻¹))·f  ({'ok' if ok else 'FAIL'})")
    check("chiral_coeff_gives_nonzero_odd_datum", nonzero,
          source="a bar-asymmetric cyclotomic coefficient produces a nonzero "
                 "bar-odd Habiro datum equal to (C_n(q)−C_n(q⁻¹))·f_n(q) — the "
                 "odd channel is located in the coefficient asymmetry (demo with "
                 "a toy C_n; the 5₂ coefficient is Masbaum's, to be derived)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("LOCATED: the bar-odd (q↔q⁻¹ antisymmetric) content of any Kashaev/Habiro "
         "tail S_K(q)=Σ_n C_{K,n}(q)·f_n(q) is carried ENTIRELY by the "
         "cyclotomic coefficient's bar-asymmetry — C_n(q)f_n(q)−C_n(q⁻¹)f_n(q⁻¹) "
         "= (C_n(q)−C_n(q⁻¹))·f_n(q), since f_n is bar-even (Lean-proved). 4₁ has "
         "C_n=1 (bar-symmetric) ⇒ zero odd datum (bar-even tail, the π²/5 action "
         "all-even); a chiral knot's bar-asymmetric C_{K,n} supplies the odd "
         "datum. So the Q_β odd-channel resurgence (b3ix) lives in the "
         "cyclotomic-coefficient asymmetry — for 5₂ this is the Masbaum "
         "twist-knot coefficient C_{5_2,n}, the concrete next input (to be "
         "derived from that reference, not invented). "
         if all_passed else
         "PARTIAL: a check failed — see the per-check table. ")
        + "scope-(b): a proved q↔q⁻¹ symmetry identity (Lean: "
        "HabiroCyclotomicOddLocus). NO fit; NO c_k wired."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-habiro-odd-locus",
        "description": "The odd-channel Habiro datum is located in the "
                       "bar-asymmetry of the cyclotomic coefficient C_{K,n}: "
                       "C_n(q)f−C_n(q⁻¹)f = (C_n(q)−C_n(q⁻¹))f (f bar-even). 4₁ "
                       "C_n=1 ⇒ zero odd datum; chiral C_n supplies it. 5₂ needs "
                       "Masbaum's C_{5_2,n}. Lean: HabiroCyclotomicOddLocus. "
                       "scope-(b).",
        "audit_only": True,
        "tier": "symbolic-exact (bar-parity locator)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"identity_max_err": mp.nstr(max_err, 6),
                   "fourone_odd": mp.nstr(odd_41, 6), "verdict": verdict},
        "context": {
            "axis": "b3ix odd-locus (continuation of #3970)",
            "lean": "QOU.QBeta.HabiroCyclotomicOddLocus "
                    "(habiroTerm_bar_odd_eq_coeff_asymmetry, sorry-free)",
            "next_input": "5₂ cyclotomic coefficient C_{5_2,n} (Masbaum "
                          "twist-knot formula) — to be derived, not invented",
            "supports": "#3966 b3ix",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-habiro-odd-locus.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
