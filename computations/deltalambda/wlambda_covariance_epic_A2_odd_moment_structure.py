#!/usr/bin/env python3
r"""
wlambda_covariance_epic_A2_odd_moment_structure.py — structure of the ODD hook-power moments
(qou-x631, qou-ogrk), the companion to the proved even-moment positivity.

The moment skeleton observed `M_k = Σ_v v^k ν_v = Cov_Planch(Σ_□ h^k, Σ_□ h²) > 0` empirically. For
EVEN `k` both weights are shifted-symmetric, so `M_{2j}` is an exact polynomial in `n` and positivity
is PROVED (see `…A2_even_moment_positivity_proved.py`, Lean `YoungDiagramKernel.{threeM4_pos,M6_pos}`).
For ODD `k` the weight `Σ_□ h^{2j+1}` is NOT shifted-symmetric, so `M_{2j+1}` is non-polynomial and no
such closed form exists. This probe characterizes the odd-`k` structure exactly (exact `Fraction`,
n = 3..NMAX) and records what does — and does NOT — give a positivity handle:

  (1) NON-POLYNOMIAL: a degree-`d` Lagrange interpolation of `M_1, M_3, M_5` from small `n`
      MISPREDICTS at larger `n` (an exact polynomial would not).
  (2) LOG-CONVEX / NOT A HAMBURGER SEQUENCE: the moment sequence satisfies `M_{k+1}² > M_k·M_{k+2}`
      uniformly — equivalently every 2×2 Hankel minor `M_i M_{i+2} − M_{i+1}²` is NEGATIVE. A positive
      measure's moments obey the reverse Cauchy–Schwarz inequality, so {M_k} is NOT the moment
      sequence of any positive measure. This KILLS the "write M_k = ∫ v^k dν with ν ≥ 0 and read off
      positivity from the measure" route.
  (3) TRANSPOSE IDENTITY (exact): `M_1(n) = 2·Cov_Planch(n_λ, Σ_□ c(□)²)`, where `n_λ = Σ_i i·λ_i`.
      From `Σ_□ h = n_λ + n_λ' + n` and Plancherel transpose-invariance. Reduces the first odd moment
      to a row-content / content-spread covariance — structurally the SAME difficulty class as the open
      kernel `Cov_Planch(f^λ, Σc²) ≤ 0`, not an easier object.
  (4) SIGNS: `M_1, M_3, M_5, M_7 > 0` for all tested `n` — but log-convexity + the proved even
      positivity does NOT bootstrap the odd signs (log-convexity relates the SQUARES `M_{k+1}²`, giving
      no sign information on `M_{k+1}`). So odd-moment positivity remains genuinely OPEN.

HONESTY. A structural characterization (what routes are and are not available for the odd moments), not
a proof of odd positivity, A2, or the kernel. scope-(a); no fit; nothing wired; no `c_k`;
L2 unchanged (2/7).

# Ref: [manuscript] docs/audits/2026-07-25-covariance-kernel-A2-odd-moment-structure.md
# Ref: [ivanov-olshanski] https://arxiv.org/abs/math/0304010
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

NMAX = 14


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def conj_of(l):
    return [sum(1 for p in l if p > j) for j in range(l[0])] if l else []


def hooks_mult(l):
    l = list(l)
    conj = conj_of(l)
    cnt = {}
    for i, row in enumerate(l):
        for j in range(row):
            h = (row - j) + (conj[j] - i) - 1
            cnt[h] = cnt.get(h, 0) + 1
    return cnt


def dim(l):
    l2 = list(l)
    conj = conj_of(l2)
    d = 1
    for i, row in enumerate(l2):
        for j in range(row):
            d *= (row - j) + (conj[j] - i) - 1
    return math.factorial(sum(l)) // d


def moments_and_transpose(n, kmax=7):
    """Return (M[1..kmax], covN) with M_k = Cov_Planch(Σh^k, Σh²) and
    covN = Cov_Planch(n_λ, Σc²), all exact."""
    fact = math.factorial(n)
    Es2 = Fr(0)
    Ehk = [Fr(0)] * (kmax + 1)
    Ehkh = [Fr(0)] * (kmax + 1)
    Enl = Fr(0)
    Ecs = Fr(0)
    Enlcs = Fr(0)
    for l in partitions_of(n):
        d = dim(l)
        w = Fr(d * d, fact)
        hc = hooks_mult(l)
        s2 = sum(v * v * c for v, c in hc.items())
        Es2 += w * s2
        for k in range(1, kmax + 1):
            sk = sum((v ** k) * c for v, c in hc.items())
            Ehk[k] += w * sk
            Ehkh[k] += w * sk * s2
        nl = sum(i * row for i, row in enumerate(l))                       # n_λ = Σ_i i·λ_i
        cs = sum(((jj - ii) ** 2) for ii, row in enumerate(l) for jj in range(row))  # Σc²
        Enl += w * nl
        Ecs += w * cs
        Enlcs += w * nl * cs
    M = {k: Ehkh[k] - Ehk[k] * Es2 for k in range(1, kmax + 1)}
    covN = Enlcs - Enl * Ecs
    return M, covN


def interp(points):
    xs = [Fr(p[0]) for p in points]
    ys = [p[1] for p in points]
    N = len(xs)
    coeffs = [Fr(0)] * N
    for i in range(N):
        num = [Fr(1)]
        den = Fr(1)
        for j in range(N):
            if j == i:
                continue
            new = [Fr(0)] * (len(num) + 1)
            for t, c in enumerate(num):
                new[t] += -xs[j] * c
                new[t + 1] += c
            num = new
            den *= (xs[i] - xs[j])
        for t, c in enumerate(num):
            coeffs[t] += ys[i] * c / den
    return coeffs


def polyval(C, x):
    return sum(c * (x ** t) for t, c in enumerate(C))


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — ODD hook-power moment structure ===\n")
    data = {n: moments_and_transpose(n) for n in range(3, NMAX + 1)}

    # (1) non-polynomiality
    nonpoly = {}
    for k in [1, 3, 5]:
        found = False
        for deg in range(k // 2 + 3, k + 4):
            pts = [(n, data[n][0][k]) for n in range(3, 3 + deg + 1) if n <= NMAX]
            if len(pts) < deg + 1:
                break
            C = interp(pts)
            ntest = 3 + deg + 1
            if ntest <= NMAX:
                if polyval(C, Fr(ntest)) != data[ntest][0][k]:
                    nonpoly[k] = True
                    found = True
                    break
        nonpoly.setdefault(k, not found and None)
    print(f"(1) non-polynomial (interp mispredicts): "
          f"{ {k: bool(v) for k, v in nonpoly.items()} }")

    # (2) Hankel minors negative ⇔ log-convex ⇔ NOT a Hamburger moment sequence
    all_neg = True
    sample = {}
    for n in [6, 10, NMAX]:
        M = data[n][0]
        minors = [M[i] * M[i + 2] - M[i + 1] ** 2 for i in range(1, 6) if i + 2 in M]
        neg = all(v < 0 for v in minors)
        all_neg &= neg
        sample[n] = neg
    print(f"(2) all 2×2 Hankel minors negative (⇒ log-convex, NOT Hamburger): {sample} → {all_neg}")

    # (3) transpose identity  M_1 = 2·Cov(n_λ, Σc²)
    transpose_ok = all(data[n][0][1] == 2 * data[n][1] for n in range(3, NMAX + 1))
    print(f"(3) transpose identity  M_1 = 2·Cov(n_λ,Σc²)  for n=3..{NMAX}: {transpose_ok}")

    # (4) odd-moment signs
    odd_pos = all(data[n][0][k] > 0 for n in range(3, NMAX + 1) for k in [1, 3, 5, 7])
    print(f"(4) M_1,M_3,M_5,M_7 > 0 for n=3..{NMAX}: {odd_pos}")

    ok = all(nonpoly.get(k) for k in [1, 3, 5]) and all_neg and transpose_ok and odd_pos
    print(f"\nRESULT: odd-moment structure characterized "
          f"(non-polynomial + log-convex/non-Hamburger + transpose identity + empirically positive): {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-A2-odd-moment-structure", engine="python-exact")
        w.set_description(
            "Structure of the ODD hook-power moments M_k=Cov_Planch(Σ_□ h^k,Σ_□ h²) of the covariance "
            "measure (qou-x631, qou-ogrk), companion to the proved even-moment positivity. Exact "
            "Fraction, n=3..14. Findings: (1) ODD moments are NON-POLYNOMIAL (Σh^{2j+1} not "
            "shifted-symmetric; degree-d interpolation of M_1,M_3,M_5 mispredicts). (2) The moment "
            "sequence is strictly LOG-CONVEX (M_{k+1}²>M_k·M_{k+2}, i.e. every 2×2 Hankel minor "
            "M_i M_{i+2}−M_{i+1}²<0) ⇒ NOT the moment sequence of any positive measure (reverse "
            "Cauchy–Schwarz fails) — kills the ∫v^k dν, ν≥0 positivity route. (3) EXACT transpose "
            "identity M_1(n)=2·Cov_Planch(n_λ,Σc²) with n_λ=Σ_i i·λ_i (from Σh=n_λ+n_λ'+n and "
            "Plancherel transpose-invariance) — reduces the first odd moment to a covariance of the "
            "SAME difficulty class as the open kernel. (4) M_1,M_3,M_5,M_7>0 for all n tested, but "
            "log-convexity+even positivity does NOT bootstrap odd signs (relates the squares) — odd "
            "positivity stays OPEN. Structural characterization, not a proof of odd positivity/A2/kernel. "
            "scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("odd_moments_nonpolynomial", bool(all(nonpoly.get(k) for k in [1, 3, 5])))
        w.add_data("moment_sequence_log_convex_not_hamburger", bool(all_neg))
        w.add_data("transpose_identity_M1_eq_2CovNlambda_ContentSq", bool(transpose_ok))
        w.add_data("odd_moments_empirically_positive_n_le_14", bool(odd_pos))
        w.add_data("odd_positivity_status", "OPEN (log-convexity relates squares; no sign bootstrap)")
        w.add_assertion(
            "covariance_epic_A2_odd_moment_structure",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Odd hook-power moments characterized exactly (n<=14): non-polynomial; strictly "
                    "log-convex hence not a positive-measure moment sequence; exact transpose identity "
                    "M_1=2·Cov(n_λ,Σc²); empirically positive but positivity OPEN. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
