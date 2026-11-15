"""The Kerov-mode question was the wrong question; and two dominance routes die at k=18.

Epic `qou-x631`, T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cyc) <= 0. Bean `qou-igjo`
follow-up; the open item is `qou-r91v`'s "Cov_beta(C_2, ln f) <= 0 on [2,3] still
needs a genuine argument", and `qou-4hq0` names the missing tool as a
non-shifted-symmetric ln-dim expansion.

*** SELF-CORRECTION FIRST: MY OWN CLAIM IN #7051 WAS UNDER-EVIDENCED ***

I recorded that expanding ln f in the Kerov modes "will not terminate", on the
evidence that the SINGLE-CYCLE modes mu = (p,1^{k-p}) carry a share of
Var_P(ln f) that falls from 20.8% to 12.4%. That measurement is correct and the
inference does not follow from it, because {Sigma_p} generate the shifted-
symmetric algebra MULTIPLICATIVELY: Sigma_mu for multi-cycle mu is a polynomial
in the Sigma_p, so the linear span of single cycles being small says nothing
about low-DEGREE polynomials in them. Expanding in the FULL class basis and
grouping by d = number of nontrivial cycles:

    k      d=1      d=2      d=3     d<=2 cumulative
    8    24.4%    66.1%     1.9%        90.5%
   12    20.8%    56.4%    12.9%        77.2%
   16    19.4%    50.0%    13.3%        69.4%

**The mass is at d=2, which I never looked at.** The conclusion survives -- no
FIXED degree holds up, d<=2 falls 90.5% -> 69.4% and the Kerov degree needed for
90% grows roughly linearly in k -- but it survives on evidence I had not taken.

*** AND THEN THE CONCLUSION IS BESIDE THE POINT ANYWAY ***

Whether the expansion converges is irrelevant to the conjecture, because the
quantity in question is ONE coefficient of it. Sigma_3 = (k)_3/sqrt(|C_3|) * e_3
is a single basis vector, so

    Cov_P(ln f, Sigma_3)  =  (k)_3/sqrt(|C_3|) * <ln f - E ln f, e_3>

and every d >= 2 mode -- the 50-66% of the mass -- is ORTHOGONAL to e_3 and
contributes exactly nothing. "Can ln f be expanded in Kerov modes?" was the wrong
question. The right one is "can one coefficient be computed or signed?", and the
expansion's convergence has no bearing on it. Asserted below as an exact identity.

*** THE CLEANEST FORM OF THE CONJECTURE FOUND SO FAR ***

Drop the measures. Set

    G(s) := SUM_lam (f^lam)^{1+s} chi^lam(3-cyc) .

Then G(0) = 0 EXACTLY (column orthogonality: SUM_lam f^lam chi^lam(mu) = 0 for
mu != 1^k) and G(1) = T_3(k) is the conjecture. No partition function, no
tilted measure, no covariance -- the epic's E_Q / Cov_beta formulations all carry
a normaliser Z that this one does not. The tempering family of `qou-f4ye` is
s = beta - 2.

Split by the sign of the character. With W := SUM_{chi>0} f|chi| = SUM_{chi<0}
f|chi| -- that equality IS G(0) = 0, and it holds as exact integer equality --
define probability measures nu_pm(lam) ∝ f^lam |chi^lam(3)| on the two sign
classes. Then

    G(s) = W * ( E_{nu+}[f^s] - E_{nu-}[f^s] ) ,

so the conjecture is exactly E_{nu+}[f^s] <= E_{nu-}[f^s] on s in [0,1]:
**partitions whose 3-cycle character is negative carry the larger dimensions.**

*** TWO ROUTES TESTED AND ELIMINATED ***

Both are the natural sufficient conditions for that, and both are FALSE.

  1. FIRST-ORDER stochastic dominance of nu- over nu+ in f^lam. It would give
     G(s) <= 0 for every s >= 0, not just [0,1].
  2. INCREASING-CONCAVE (second-order) dominance. Strictly weaker, and exactly
     matched to the exponents that matter: x^s is increasing concave for
     s in (0,1). The k=18 failure of (1) does not touch it a priori.

Measured exactly on Fractions over 10 <= k <= 32: at every k the survival
functions do not cross at all (sign pattern [-1], nu+ uniformly below nu-) --
EXCEPT k = 18 and k = 26, where both orders fail, by 0.0161 and 0.0011. So the
structure is not a near-miss to be patched; it is false at recurring k with a
shrinking gap, and a sufficient condition that fails anywhere is not a route.
The conjecture itself continues to hold at those k.

Recorded so the two are not re-opened: they look compelling, they hold at 21 of
23 values tested, and they are dead.
"""
from __future__ import annotations

import json
import math  # float64-ok: only the ln f decomposition shares, which are reported to 3 dp; every dominance verdict is decided on exact Fractions
import subprocess
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
from _mn_characters import partitions, border_strips, chi, hook_dim  # noqa: E402

EXPAND_K = (8, 10, 12, 14, 16)
DOM_K = tuple(range(10, 33))
G_K = tuple(range(4, 23))


def csize(mu: tuple, k: int) -> int:
    den = 1
    for part, m in Counter(mu).items():
        den *= (part ** m) * math.factorial(m)
    return math.factorial(k) // den


def sgn(mu: tuple) -> int:
    return (-1) ** sum(p - 1 for p in mu)


def chi3(lam: tuple, nfm: int) -> int:
    return sum((-1) ** ht * hook_dim(nu, nfm) for nu, ht in border_strips(lam, 3))


def sign_split(k: int):
    """(pos, neg, W) with entries (f^lam, |chi^lam(3-cyc)|)."""
    nf, nfm = math.factorial(k), math.factorial(k - 3)
    pos, neg = [], []
    for lam in partitions(k):
        c = chi3(lam, nfm)
        if c == 0:
            continue
        f = hook_dim(lam, nf)
        (pos if c > 0 else neg).append((f, abs(c)))
    return pos, neg, sum(f * c for f, c in pos), sum(f * c for f, c in neg)


def main() -> int:
    t0 = time.monotonic()
    a: list[dict] = []
    ok = True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    # ------------------------------------------------------------------ 1
    print("=" * 78)
    print("1. FULL class-basis expansion of ln f -- the mass is at d=2, not d=1")
    print("=" * 78)
    shares: dict[int, dict[int, float]] = {}
    bad_parseval, bad_odd = [], []
    for k in EXPAND_K:
        nf = math.factorial(k)
        lams = list(partitions(k))
        fs = {l: hook_dim(l, nf) for l in lams}
        lg = {l: math.log(fs[l]) for l in lams}
        w = {l: (fs[l] * fs[l]) / nf for l in lams}
        el = sum(w[l] * lg[l] for l in lams)
        var = sum(w[l] * (lg[l] - el) ** 2 for l in lams)
        ident = tuple([1] * k)
        by_d: dict[int, float] = defaultdict(float)
        tot, odd = 0.0, 0.0
        for mu in partitions(k):
            if mu == ident:
                continue
            s = sum(fs[l] * chi(l, mu) * lg[l] for l in lams)
            b = math.sqrt(csize(mu, k)) * s / nf
            tot += b * b
            if sgn(mu) == -1:
                odd += b * b
            by_d[sum(1 for p in mu if p > 1)] += b * b
        if abs(tot / var - 1.0) > 1e-9:
            bad_parseval.append(k)
        if odd / var > 1e-20:
            bad_odd.append(k)
        shares[k] = {d: by_d[d] / var for d in sorted(by_d)}
        c2 = shares[k].get(1, 0) + shares[k].get(2, 0)
        print(f"    k={k:>3}  d=1 {shares[k].get(1,0):6.1%}   d=2 {shares[k].get(2,0):6.1%}"
              f"   d=3 {shares[k].get(3,0):6.1%}   d<=2 {c2:6.1%}"
              f"   Parseval {tot/var:.9f}")

    ok &= chk("parseval_exact_over_full_class_basis", bad_parseval, [],
              note="SUM_{mu != 1^k} b_mu^2 = Var_P(ln f) to 1e-9 at every k -- the "
                   "expansion is complete, which is the check that the coefficients "
                   "are right")
    ok &= chk("ln_f_is_supported_on_even_classes", bad_odd, [],
              note="ln f is omega-even, so its odd-class mass is 0; measured ~1e-30 "
                   "relative, i.e. numerically exact")
    ok &= chk("mass_is_at_degree_two_not_degree_one",
              bool(all(shares[k][2] > 2 * shares[k][1] for k in EXPAND_K)), True,
              note=f"d=2 carries {shares[16][2]:.1%} against d=1's {shares[16][1]:.1%} at "
                   "k=16. SELF-CORRECTION: #7051 argued ln f has no terminating Kerov "
                   "expansion from the d=1 share alone, which does not follow -- the "
                   "Sigma_p generate the algebra MULTIPLICATIVELY, and the mass is at d=2")
    ok &= chk("no_fixed_degree_suffices",
              bool(shares[16][1] + shares[16][2] < shares[8][1] + shares[8][2]), True,
              note=f"d<=2 cumulative falls {shares[8][1]+shares[8][2]:.1%} (k=8) -> "
                   f"{shares[16][1]+shares[16][2]:.1%} (k=16). The #7051 conclusion "
                   "survives, now on evidence that supports it")

    # ------------------------------------------------------------------ 2
    print()
    print("=" * 78)
    print("2. THE COVARIANCE IS ONE COEFFICIENT -- convergence is irrelevant")
    print("=" * 78)
    bad_one = []
    for k in range(5, 13):
        nf = math.factorial(k)
        lams = list(partitions(k))
        mu3 = tuple([3] + [1] * (k - 3))
        c3 = csize(mu3, k)
        # Sigma_3 = (k)_3/sqrt(|C_3|) e_3  <=>  (k)_3 = |C_3| * 3 ... check the
        # exact algebraic identity (k)_3 = 3|C_3| that makes it one coefficient.
        f3 = k * (k - 1) * (k - 2)
        if f3 != 3 * c3:
            bad_one.append(k)
    ok &= chk("sigma3_is_a_single_basis_vector", bad_one, [],
              note="|C_{(3,1^{k-3})}| = (k)_3/3, so Sigma_3 = (k)_3/sqrt(|C_3|) * e_3 is "
                   "ONE orthonormal basis vector. Hence Cov_P(ln f, Sigma_3) is one "
                   "Fourier coefficient of ln f, and every d>=2 mode -- the 50-66% of "
                   "the mass measured above -- is orthogonal to it and contributes "
                   "nothing. Whether the expansion terminates has no bearing on the "
                   "conjecture")

    # ------------------------------------------------------------------ 3
    print()
    print("=" * 78)
    print("3. G(s) = SUM (f)^{1+s} chi(3): G(0)=0 exactly, G(1)=T_3, no normaliser")
    print("=" * 78)
    bad_g0, bad_gneg = [], []
    for k in G_K:
        pos, neg, wp, wn = sign_split(k)
        if wp != wn:
            bad_g0.append(k)
        for s in (0.25, 0.5, 0.75, 1.0):
            ep = sum(f * c * (f ** s) for f, c in pos) / wp
            en = sum(f * c * (f ** s) for f, c in neg) / wn
            if ep - en >= 0:
                bad_gneg.append((k, s))
    ok &= chk("G_of_zero_vanishes_as_exact_integers", bad_g0, [],
              note="W+ = W- as EXACT integers for 4 <= k <= 22. This is G(0) = 0, i.e. "
                   "column orthogonality, and it is what makes the sign-split a pair of "
                   "probability measures with equal total mass")
    ok &= chk("G_is_negative_on_the_open_interval", bad_gneg, [],
              note="E_{nu+}[f^s] < E_{nu-}[f^s] at s = .25,.5,.75,1 for every k tested: "
                   "partitions whose 3-cycle character is NEGATIVE carry the larger "
                   "dimensions. s=1 is the conjecture itself")

    # ------------------------------------------------------------------ 4
    print()
    print("=" * 78)
    print("4. BOTH DOMINANCE ROUTES ARE FALSE -- k = 18 and k = 26")
    print("=" * 78)
    fsd_fail, icv_fail, gaps = [], [], {}
    for k in DOM_K:
        pos, neg, wp, wn = sign_split(k)
        ts = sorted({f for f, _ in pos} | {f for f, _ in neg})

        def suffix(items):
            d: dict[int, int] = defaultdict(int)
            for f, c in items:
                d[f] += f * c
            S, A, s, acc = {}, {}, 0, 0
            for t in reversed(ts):
                S[t], A[t] = s, acc
                s += d[t]
                acc += d[t] * t
            return S, A

        sp, ap = suffix(pos)
        sn, an = suffix(neg)
        worst = Fraction(0)
        f_bad = i_bad = 0
        for t in ts:
            d1 = Fraction(sp[t], wp) - Fraction(sn[t], wn)
            if d1 > 0:
                f_bad += 1
                worst = max(worst, d1)
            if Fraction(ap[t] - t * sp[t], wp) > Fraction(an[t] - t * sn[t], wn):
                i_bad += 1
        if f_bad:
            fsd_fail.append(k)
            gaps[k] = float(worst)  # float64-ok: reporting only -- `worst` is an exact Fraction and the FSD verdict `f_bad` is decided by the exact comparison `d1 > 0` above, never by this float
        if i_bad:
            icv_fail.append(k)
        print(f"    k={k:>3}  FSD viol {f_bad:>2}   ICV viol {i_bad:>2}"
              + (f"   worst gap {float(worst):.4f}" if f_bad else ""))  # float64-ok: console display of an exact Fraction; no assertion reads it

    ok &= chk("first_order_dominance_is_FALSE", fsd_fail, [18, 26],
              note=f"nu- does NOT stochastically dominate nu+ in f^lam. Exact on "
                   f"Fractions: fails at k=18 (gap {gaps.get(18,0):.4f}) and k=26 (gap "
                   f"{gaps.get(26,0):.4f}), holds at the other 21 values in 10..32. It "
                   "would have given G(s) <= 0 for ALL s >= 0. ELIMINATED")
    ok &= chk("increasing_concave_dominance_is_FALSE", icv_fail, [18, 26],
              note="Second-order (increasing-concave) dominance is strictly WEAKER and "
                   "exactly matched to the exponents that matter -- x^s is increasing "
                   "concave for s in (0,1) -- so the FSD failure did not settle it. It "
                   "fails at the SAME two k. ELIMINATED")
    # Does the CONJECTURE survive at the two k where the dominance orders die?
    # (An always-true expression stood here in the first draft. It asserted
    # nothing and would have printed PASS regardless -- the exact failure the
    # rest of this file is about.)
    still_holds = []
    for k in (18, 26):
        pos, neg, wp, wn = sign_split(k)
        ep = Fraction(sum(f * c * f for f, c in pos), wp)
        en = Fraction(sum(f * c * f for f, c in neg), wn)
        still_holds.append((k, ep <= en))
    ok &= chk("conjecture_still_holds_at_the_failing_k",
              [t for _, t in still_holds], [True, True],
              note="Decided on exact Fractions: E_{nu+}[f] <= E_{nu-}[f] -- i.e. "
                   "G(1) = T_3(k) <= 0 -- holds at BOTH k=18 and k=26. So those k break "
                   "the dominance STRUCTURE, not the conjecture, which is what makes the "
                   "two orders strictly stronger than needed and strictly false")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-kerov-mode.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-kerov-mode",
        "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631", "bean": "qou-igjo",
                       "claim": "the Kerov-expansion question is orthogonal to the "
                                "conjecture (one coefficient); FSD and ICV on the "
                                "sign-split both fail at k=18 and k=26"},
        "data": {
            # Decimal strings, not floats: AGENTS.md "none may enter a witness".
            # These are float64-grade (log of an exact integer) and are reported
            # to 4 dp, well inside what they support; every dominance verdict
            # above is decided on exact Fractions, not on these.
            "_grade": "decimal strings, float64-grade, 4 dp",
            "ln_f_share_by_degree": {str(k): {str(d): f"{v:.4f}" for d, v in row.items()}
                                     for k, row in shares.items()},
            "fsd_failing_k": fsd_fail,
            "icv_failing_k": icv_fail,
            "fsd_worst_gap": {str(k): f"{v:.6f}" for k, v in gaps.items()},
        },
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_kerov_mode_probe.py",
                       "elapsed_s": f"{time.monotonic() - t0:.3f}"},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
