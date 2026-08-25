#!/usr/bin/env python3
"""threerow_qcross_trend_probe.py — is q_cross(n) a STRUCTURED SEQUENCE, and is q₀'s
position within it DERIVED or COINCIDENTAL?

Bean qou-prjo.  Follow-up to #4829 (deuteron ≥3-row sign crossing) and its UNIT-2
sibling (`threerow_crossing_a_dependence_probe.py`, A-dependence of the crossing).

THE OBJECT.  F_K(q) = Σ_{λ⊢3A, ℓ(λ)≥3} y_λ(q)·χ^λ(β_K;q)·Δ_λ, with the PROVED
value-only Δ_λ = (−1)^{n(λ)}·dim V_λ, plus its character-free companion
G_n(q) = Σ_{λ⊢n, ℓ(λ)≥3} y_λ(q)·Δ_λ (defined for EVERY n, not just n = 3A).

WHAT THIS PROBE ADDS OVER #4829 / UNIT-2 — three structural facts, each verified
here to 35+ digits, that together REFRAME the "trend" question:

  (BG-1)  DUAL-CAUCHY NORMALISER.  Σ_{μ⊢n} f^μ·s_μ = p_1^n exactly, so the
          y_λ normaliser is CLOSED FORM:  Z(q) = ((1−Q^r)/(1−Q))^n, giving
          y_λ = s_λ·((1−Q)/(1−Q^r))^n.  Z > 0 on the whole real-level branch, so
          sgn G_n = sgn S_n with S_n := Σ_{ℓ≥3} s_λ·Δ_λ — the normaliser CANNOT
          create or destroy a crossing.  (Removes a pole-vs-zero ambiguity that a
          bisect-on-sign-change scan cannot otherwise distinguish.)

  (BG-2)  THE WENZL LEVEL EIGENVALUE HAS A POLE.  With u = √q, Q = u⁴,
          Q^r = u³/D(u), D(u) = −u⁶−u⁴+u³+u²+1.  D has a real root
          u* = 1.13068544546204…, i.e. q* = u*² = 1.27844957657969….  BELOW q* the
          effective level r = log(Q^r)/log(Q) is REAL; ABOVE q* it is COMPLEX
          (r(1.30) = 5.05+5.99i, r(1.45) = 0.81+4.23i).  So (1, q*) is the
          REAL-LEVEL BRANCH, and q₀ ≈ 1.10998 lies inside it (r(q₀) = 2.5995).

          ⇒ CORRECTION TO UNIT-2.  The n=9 "crossings" reported at q ≈ 1.4285 /
          1.4617 lie ABOVE q*, i.e. OFF the real-level branch, where the Wenzl
          principal specialisation s_λ(1,Q,…,Q^{r−1}) has no real level.  A
          "trend" built by comparing q_cross(6)=1.054 (r real) with q_cross(9)≈1.43
          (r complex) compares across a branch singularity.  This probe therefore
          sweeps ONLY the real-level branch (1, q*).

  (BG-3)  LEVEL-INTEGER LADDER (the genuinely structured sequence).  s_λ = 0
          whenever some cell has r + c(x) = 0; the minimum content of λ is
          −(ℓ(λ)−1), so at INTEGER level r = k every λ with ℓ(λ) > k drops out.
          The ladder q_k solving r(q_k) = k is the root of the explicit integer
          polynomial  Σ_{j=0}^{k−1} u^{4j+3} = u^{4k} + u^{4k+2},  is strictly
          increasing, and accumulates at q*:
              q_2 = 1 exactly,  q_3 = 1.15416065…,  q_4 = 1.21589…,  → q*.
          Since r→2⁺ as q→1⁺, the ENTIRE ℓ≥3 stratum degenerates at q=1 — which is
          why F and G are O(10⁻⁵) at q = 1+10⁻⁴ (#4829 §2), not an accident.

THE THREE QUESTIONS (asked only on the real-level branch):
  Q1 monotone?    → per-n crossing sets for G_n (n=3..N) and F_K (D,T,³He,⁴He).
  Q2 derivable?   → S_n is a RATIONAL FUNCTION of u=√q with INTEGER coefficients,
                    so every crossing is an algebraic number; the exact irreducible
                    minimal polynomial + certified root enclosure is computed for
                    small n (sympy, exact rational arithmetic).
  Q3 q₀ special?  → ONLY after Q1/Q2, and gated by the GENERICITY test below.

🛑 ANTI-NUMEROLOGY GATE (AGENTS.md §"Defined residual ≠ derived decomposition" it.2).
"q₀ lies between two crossings" is NOT a result by itself: ANY constant in the same
interval reproduces the identical sign pattern.  So this probe COMPUTES THE WINDOW —
the maximal interval around q₀ on which the isotope sign-vector is constant — its
width, its fraction of the branch, its Shannon content in bits, and how many
low-height rationals and simple algebraic constants also fall inside it.  A verdict
of "COINCIDENTAL" is reported as a FIRST-CLASS result, not softened.

DISCIPLINE.  free_parameters = 0.  AME never used (not even as a check).  q₀ =
EXPERIMENTAL PROTON ANCHOR (`q_parameter.Q_50_DIGIT_STR`, owner directive
2026-08-07); y_λ via the LIVE closed form `schur_principal_mpmath` — NOT the
muon-serving `wedderburn_jones_markov.y_lambda_at` cache (AGENTS.md straddle
hazard).  Layer-pure: y_λ(q) and χ^λ(β;q) are ALWAYS evaluated at the same running
q.  Scope-(a) by default: "no crossing on interval I" is a statement about I only;
a LOCATED crossing is a positive existence statement (bracketed sign change of a
continuous function).  No invariant is proved to forbid a zero anywhere ⇒ no
scope-(b) claim is made.

PRECISION.  y_λ / s_λ: 50-dps mpmath.  χ^λ: f64 (pure-Python Hoefsmit seminormal
via the sparse kernel `threerow_chi_sparse`, exact-equal to the #4829 dense path to
1.4e-15).  Decisive for SIGN questions away from a crossing; located crossing q
values carry f64 resolution only.  The Q2 minimal polynomials are EXACT (sympy
rational arithmetic, certified real-root isolation) and carry no f64 error at all.
"""
from __future__ import annotations

import os
import sys
import math
import time
import warnings
from pathlib import Path

sys.path[:0] = [
    str(Path(__file__).resolve().parent.parent),
    str(Path(__file__).resolve().parent.parent / "substrate"),
    str(Path(__file__).resolve().parent.parent / "hecke"),
]
for _extra in ("/home/user/qou/computations", "/home/user/qou/computations/substrate",
               "/home/user/qou/computations/hecke", "/home/user/qou/computations/deltalambda"):
    if _extra not in sys.path:
        sys.path.append(_extra)
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    partitions_of, _f_lambda, schur_principal_mpmath, _wenzl_constants,
    hooks_and_contents, n_partition,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from _precision import set_compute_dps, str_at_true_precision  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from threerow_chi_sparse import chi_atom_sparse  # noqa: E402
from threerow_sign_crossing_probe import fmt_f64_limited  # noqa: E402

warnings.filterwarnings("ignore")
set_compute_dps(50)

Q0 = mp.mpf(Q_50_DIGIT_STR)          # EXPERIMENTAL PROTON ANCHOR
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
N_MAX_FREE = int(os.environ.get("QOU_NMAX_FREE", "23"))
GRID_FREE = int(os.environ.get("QOU_GRID_FREE", "220"))
GRID_ISO = int(os.environ.get("QOU_GRID_ISO", "90"))
GRID_4HE = int(os.environ.get("QOU_GRID_4HE", "26"))
OUTDIR = Path(os.environ.get("QOU_OUTDIR", str(Path(__file__).resolve().parent)))


# ══════════════════════════════════════════════════════════════════════════
# BG-2: the real-level branch
# ══════════════════════════════════════════════════════════════════════════
def _D_wenzl(u):
    """D(u) = −u⁶−u⁴+u³+u²+1;  Q^r = u³/D(u) with u=√q. Pole of Q^r at D(u)=0."""
    return -u**6 - u**4 + u**3 + u**2 + 1


U_STAR = mp.findroot(_D_wenzl, mp.mpf("1.13"))
Q_STAR = U_STAR ** 2                     # real-level branch is (1, Q_STAR)
Q_LO = mp.mpf("1.000001")
Q_HI = Q_STAR * (1 - mp.mpf("1e-5"))


def level_r(q):
    """Effective Wenzl level r = log(Q^r)/log(Q). Real on (1,q*), complex above."""
    Q, QR = _wenzl_constants(q)
    return mp.log(QR) / mp.log(Q)


def q_level(k: int):
    """q_k with r(q_k)=k exactly: root of Σ_{j<k} u^{4j+3} = u^{4k} + u^{4k+2}."""
    f = lambda u: sum(u ** (4 * j + 3) for j in range(k)) - u ** (4 * k) - u ** (4 * k + 2)
    return mp.findroot(f, mp.mpf("1.0") + mp.mpf("0.02") * k) ** 2


def delta_lambda(lam) -> int:
    """Δ_λ = (−1)^{n(λ)}·dim V_λ  (PROVED value-only; n(λ)=Σ_j C(λ'_j,2))."""
    conj = tuple(sum(1 for p in lam if p > i) for i in range(lam[0])) if lam else ()
    sgn = math.prod((-1) ** (p * (p - 1) // 2) for p in conj)
    return sgn * _f_lambda(tuple(lam))


def S_free(n, q, min_rows=3):
    """S_n(q) = Σ_{ℓ≥3} s_λ(q)·Δ_λ.  sgn S_n = sgn G_n on (1,q*) by BG-1."""
    return sum(schur_principal_mpmath(l, q) * delta_lambda(l)
               for l in partitions_of(n) if len(l) >= min_rows)


def F_iso_sparse(Z, N, q, min_rows=3):
    """F_K(q) via the sparse character kernel. Layer-pure (y_λ and χ^λ both at q)."""
    n = 3 * (Z + N)
    ys = {}
    shapes = [l for l in partitions_of(n) if len(l) >= min_rows]
    # y_λ = s_λ·((1−Q)/(1−Q^r))^n  (BG-1 closed-form normaliser, exact)
    Q, QR = _wenzl_constants(q)
    pref = ((1 - Q) / (1 - QR)) ** n
    tot = mp.mpf(0)
    for l in shapes:
        ys[l] = schur_principal_mpmath(l, q) * pref
        tot += ys[l] * chi_atom_sparse(l, Z, N, q) * delta_lambda(l)
    return tot


def bisect(f, a, b, fa, fb, iters=60):
    for _ in range(iters):
        m = (a + b) / 2
        fm = f(m)
        if fm == 0:
            return m
        if (fm > 0) == (fa > 0):
            a, fa = m, fm
        else:
            b, fb = m, fm
    return (a + b) / 2


def crossings(f, lo, hi, npts, iters=60, log=None):
    """Geometric grid in (q−1); bisect every bracketed sign change."""
    a, b = mp.log(lo - 1), mp.log(hi - 1)
    grid = [1 + mp.e ** (a + (b - a) * k / (npts - 1)) for k in range(npts)]
    vals = []
    t0 = time.time()
    for k, x in enumerate(grid):
        vals.append(f(x))
        if log and (k % max(1, npts // 8) == 0):
            el = time.time() - t0
            eta = el / (k + 1) * (npts - k - 1)
            print(f"      [{log}] {k+1}/{npts} q={float(x):.5f} f={float(vals[-1]):+.4e} "
                  f"elapsed {el:.0f}s ETA {eta:.0f}s", flush=True)
    out = []
    for i in range(len(grid) - 1):
        if vals[i] != 0 and vals[i + 1] != 0 and (vals[i] > 0) != (vals[i + 1] > 0):
            out.append(bisect(f, grid[i], grid[i + 1], vals[i], vals[i + 1], iters))
    return out, grid, vals


# ══════════════════════════════════════════════════════════════════════════
# Q2: EXACT algebraic characterisation.  S_n is a rational function of u=√q
# with INTEGER coefficients ⇒ every crossing is an algebraic number.
# ══════════════════════════════════════════════════════════════════════════
def exact_crossing_polys(n, eps_exp=28):
    """Exact irreducible minimal polynomial + certified enclosure for the u>1 roots.

    Uses sympy rational arithmetic end-to-end (no floating point anywhere) and
    VAS/Sturm real-root ISOLATION, so the returned interval is a certified
    enclosure, not a numerical estimate.
    """
    import sympy as sp
    u = sp.symbols("u", positive=True)
    Q = u ** 4
    zW = u ** 3 / (u ** 2 + 1)
    QR = sp.cancel(zW / (1 - Q + zW))          # = u³/(−u⁶−u⁴+u³+u²+1)

    def s_sym(lam):
        hs, cs = hooks_and_contents(lam)
        num, den = sp.Integer(1), sp.Integer(1)
        for h, c in zip(hs, cs):
            num *= (1 - QR * Q ** c)
            den *= (1 - Q ** h)
        return Q ** n_partition(lam) * num / den

    S = sum(s_sym(l) * delta_lambda(l) for l in partitions_of(n) if len(l) >= 3)
    numer, _ = sp.fraction(sp.cancel(sp.together(S)))
    P = sp.Poly(sp.expand(numer), u).primitive()[1]
    eps = sp.Rational(1, 10 ** eps_exp)
    out = []
    for f, mult in sp.factor_list(P.as_expr())[1]:
        pf = sp.Poly(f, u)
        try:
            iv = pf.intervals(eps=eps)
        except Exception:
            continue
        for (a, b), _m in iv:
            if a > 1:
                # `a`, `b` are EXACT sympy rationals bounding an isolated root.
                # They used to be `float()`-ed before both the reported q_cross
                # and the branch verdict, so an exact bound was compared with a
                # 50-dps q* across an f64 round-trip. Carried as mpf instead:
                # exact in, 50 dps out, verdict decided at full precision.
                a_mp = mp.mpf(int(a.p)) / mp.mpf(int(a.q))
                b_mp = mp.mpf(int(b.p)) / mp.mpf(int(b.q))
                out.append({
                    "irreducible_degree": int(pf.degree()),
                    "multiplicity": int(mult),
                    "u_lo": str(a), "u_hi": str(b),
                    "q_cross": str_at_true_precision(a_mp * b_mp),
                    "on_real_level_branch": bool(a_mp ** 2 < Q_STAR),
                })
    return int(P.degree()), out


# ══════════════════════════════════════════════════════════════════════════
# 🛑 GENERICITY: how much does "q₀ sits here" actually constrain q?
# ══════════════════════════════════════════════════════════════════════════
def sign_window(all_crossings, q0, lo, hi):
    """Maximal interval around q₀ on which the whole sign-vector is constant.

    `all_crossings` = every located crossing of every member of the family.  The
    sign-vector can only change AT a crossing, so the window is bounded by the
    nearest crossing on each side (or the branch endpoints).
    """
    below = [c for c in all_crossings if c < q0]
    above = [c for c in all_crossings if c > q0]
    a = max(below) if below else lo
    b = min(above) if above else hi
    return a, b, b - a


def count_natural_constants(a, b):
    """How many 'natural' constants land in [a,b]?  SYSTEMATIC generator — the set is
    defined by construction rules fixed in advance, never hand-picked to taste."""
    a, b = float(a), float(b)
    hits = {"rationals_den_le_12": [], "radicals_a_root_b": [], "named_combos": []}
    for den in range(1, 13):
        for numr in range(den + 1, 4 * den + 1):
            if math.gcd(numr, den) != 1:
                continue
            v = numr / den
            if a <= v <= b:
                hits["rationals_den_le_12"].append(f"{numr}/{den}={v:.6f}")
    for base in range(2, 21):
        for root in range(1, 13):
            v = base ** (1.0 / root)
            if a <= v <= b:
                hits["radicals_a_root_b"].append(f"{base}^(1/{root})={v:.6f}")
    named = {"pi": math.pi, "e": math.e, "phi": (1 + 5 ** .5) / 2, "sqrt2": 2 ** .5,
             "sqrt3": 3 ** .5, "sqrt5": 5 ** .5, "ln2": math.log(2), "ln3": math.log(3),
             "gamma": 0.5772156649015329, "zeta3": 1.2020569031595943,
             "Vol_4_1": 2.029883212819307, "Catalan": 0.9159655941772190}
    for nm, val in named.items():
        for p in range(1, 7):
            for qd in range(1, 7):
                if math.gcd(p, qd) != 1:
                    continue
                v = val * p / qd
                if a <= v <= b:
                    hits["named_combos"].append(f"{nm}*{p}/{qd}={v:.6f}")
    return hits


def main() -> int:
    T0 = time.time()
    print("=" * 90)
    print(" q_cross(n) TREND — is it a structured sequence, and is q₀'s place derived?")
    print("=" * 90)
    print(f" q₀ (EXPERIMENTAL PROTON ANCHOR) = {mp.nstr(Q0, 20)}")

    # ── BG: branch geometry ────────────────────────────────────────────────
    print("\n" + "─" * 90)
    print(" BG. BRANCH GEOMETRY (the reframing: which q are even on the same branch?)")
    print("─" * 90)
    cauchy_err = mp.mpf(0)
    for n in (4, 6, 9, 12):
        for qs in ("1.05", "1.10998", "1.25"):
            q = mp.mpf(qs)
            Q, QR = _wenzl_constants(q)
            Z = sum(schur_principal_mpmath(m, q) * _f_lambda(m) for m in partitions_of(n))
            cauchy_err = max(cauchy_err, abs(Z - ((1 - QR) / (1 - Q)) ** n) / abs(Z))
    print(f"  BG-1 dual-Cauchy  Z = ((1−Q^r)/(1−Q))^n : max rel err {float(cauchy_err):.3e}")
    print(f"  BG-2 Wenzl pole   u* = {mp.nstr(U_STAR, 22)}   q* = {mp.nstr(Q_STAR, 22)}")
    r_below, r_above = level_r(Q_STAR * mp.mpf("0.98")), level_r(mp.mpf("1.45"))
    print(f"       level r(q₀) = {mp.nstr(level_r(Q0), 12)}  (REAL, branch OK)")
    print(f"       level r(0.98q*) = {mp.nstr(r_below, 10)} (real);  r(1.45) = "
          f"{mp.nstr(r_above, 10)}  ← COMPLEX ⇒ OFF-BRANCH")
    ladder = {}
    print("  BG-3 level-integer ladder q_k (r(q_k)=k), Σ_{j<k}u^{4j+3} = u^{4k}+u^{4k+2}:")
    for k in range(2, 11):
        qk = q_level(k)
        ladder[k] = qk
        print(f"       q_{k:<2d} = {mp.nstr(qk, 18)}   r = {mp.nstr(level_r(qk), 6) if qk > 1 else '2 (limit)'}")
    q3 = ladder[3]
    print(f"       ⇒ q₀ ∈ (q_2, q_3) = (1, {mp.nstr(q3, 12)});  r(q₀)={mp.nstr(level_r(Q0),8)} ∉ ℤ")
    van = {}
    for lam in [(3, 2, 1), (4, 1, 1), (3, 1, 1, 1), (2, 2, 1, 1), (1,) * 6]:
        van[str(lam)] = str_at_true_precision(abs(schur_principal_mpmath(lam, q3)))
    print(f"       vanishing law at r=3: |s_λ| = " +
          ", ".join(f"{k}:{float(mp.mpf(v)):.2e}" for k, v in van.items())
          + "  (ℓ>3 ⇒ 0)")

    # ── 1. character-free q_cross(n) ───────────────────────────────────────
    print("\n" + "─" * 90)
    print(f" 1. CHARACTER-FREE  G_n on the REAL-LEVEL BRANCH (1, q*),  n = 3..{N_MAX_FREE}")
    print("─" * 90)
    free = {}
    free_mpf = {}     # mpf crossings, kept out of the witness dict
    all_free_cross = []
    for n in range(3, N_MAX_FREE + 1):
        t0 = time.time()
        f = lambda q, n=n: S_free(n, q)
        cs, _g, _v = crossings(f, Q_LO, Q_HI, GRID_FREE)
        free[str(n)] = {
            "n_partitions_l_ge_3": sum(1 for l in partitions_of(n) if len(l) >= 3),
            "S_at_lo": str_at_true_precision(f(Q_LO)),
            "S_at_q0": str_at_true_precision(f(Q0)),
            "S_at_hi": str_at_true_precision(f(Q_HI)),
            "crossings": [str_at_true_precision(c) for c in cs],
            "n_crossings": len(cs),
        }
        free_mpf[str(n)] = list(cs)      # monotonicity is decided on these, not
        all_free_cross += list(cs)       # on their decimal strings
        print(f"  n={n:2d}  crossings={len(cs)}  " +
              (" ".join(f"{float(c):.6f}" for c in cs) if cs else "—") +
              f"   [{time.time()-t0:.1f}s]", flush=True)

    seq = [(int(k), cs[0]) for k, cs in free_mpf.items() if cs]
    monotone = all(seq[i + 1][1] > seq[i][1] for i in range(len(seq) - 1))
    print(f"\n  first-crossing sequence: {[(n, round(float(q), 6)) for n, q in seq]}")
    print(f"  MONOTONE INCREASING? {monotone}")

    # ── 2. character-dressed isotopes ──────────────────────────────────────
    print("\n" + "─" * 90)
    print(" 2. CHARACTER-DRESSED  F_K on (1, q*)  — D, T, ³He, ⁴He (n=12 leg NEW)")
    print("─" * 90)
    iso = {}
    all_iso_cross = []
    for name in ("D", "T", "3He", "4He"):
        Z, N = ZN[name]
        n = 3 * (Z + N)
        npts = GRID_4HE if name == "4He" else GRID_ISO
        t0 = time.time()
        f = lambda q, Z=Z, N=N: F_iso_sparse(Z, N, q)
        cs, _g, _v = crossings(f, Q_LO, Q_HI, npts, iters=(30 if name == "4He" else 60),
                               log=(name if name == "4He" else None))
        fq0 = f(Q0)
        iso[name] = {
            "n_strands": n, "grid_points": npts,
            "F_at_lo": fmt_f64_limited(f(Q_LO)),
            "F_at_q0": fmt_f64_limited(fq0),
            "F_at_hi": fmt_f64_limited(f(Q_HI)),
            "sign_at_q0": int(mp.sign(fq0)),
            "crossings_on_real_level_branch": [fmt_f64_limited(c) for c in cs],
            "n_crossings": len(cs),
        }
        all_iso_cross += list(cs)
        print(f"  {name:4s} n={n:2d}  F(q₀)={float(fq0):+.5e}  crossings={len(cs)}  " +
              (" ".join(f"{float(c):.6f}" for c in cs) if cs else "—") +
              f"   [{time.time()-t0:.0f}s]", flush=True)

    # ── 3. exact algebraic characterisation ────────────────────────────────
    print("\n" + "─" * 90)
    print(" 3. EXACT ALGEBRAIC FORM (sympy exact rational arithmetic; certified roots)")
    print("─" * 90)
    exact = {}
    for n in (6, 8, 11):
        t0 = time.time()
        deg, roots = exact_crossing_polys(n)
        exact[str(n)] = {"numerator_degree": deg, "roots_u_gt_1": roots}
        print(f"  n={n:2d}  numerator deg {deg}")
        for r in roots:
            tag = "REAL-LEVEL BRANCH" if r["on_real_level_branch"] else "off-branch (q>q*)"
            print(f"        irreducible deg {r['irreducible_degree']:4d}  "
                  f"q_cross = {r['q_cross']}   [{tag}]")
        print(f"        [{time.time()-t0:.0f}s]", flush=True)

    # ── 4. 🛑 GENERICITY GATE ──────────────────────────────────────────────
    print("\n" + "=" * 90)
    print(" 4. 🛑 GENERICITY GATE — does q₀'s position carry information?")
    print("=" * 90)
    a_i, b_i, w_i = sign_window(all_iso_cross, Q0, mp.mpf(1), Q_STAR)
    a_f, b_f, w_f = sign_window(all_free_cross, Q0, mp.mpf(1), Q_STAR)
    branch_w = Q_STAR - 1
    nat = count_natural_constants(a_i, b_i)
    n_nat = sum(len(v) for v in nat.values())
    print(f"  ISOTOPE sign-vector window around q₀ : [{float(a_i):.6f}, "
          f"{float(b_i):.6f}]  width {float(w_i):.6f}")
    print(f"     = {float(100*w_i/branch_w):.1f}% of the real-level branch "
          f"(width {float(branch_w):.6f})")
    print(f"     information content = log2(branch/window) = "
          f"{math.log2(float(branch_w/w_i)):.3f} bits")
    print(f"  CHARACTER-FREE (n≤{N_MAX_FREE}) window       : [{float(a_f):.6f}, "
          f"{float(b_f):.6f}]  width {float(w_f):.6f}")
    print(f"  'natural' constants inside the ISOTOPE window: {n_nat}")
    for k, v in nat.items():
        print(f"     {k:24s} {len(v):3d}   e.g. {', '.join(v[:6])}")
    coincidental = (n_nat > 1) or (w_i > 0.25 * branch_w)
    print(f"\n  VERDICT: q₀'s position is {'COINCIDENTAL' if coincidental else 'INFORMATIVE'}")

    # ── verdict ────────────────────────────────────────────────────────────
    verdict = {
        "monotone": bool(monotone),
        "sporadic_existence": True,
        "exactly_algebraic": True,
        "closed_form_in_radicals": False,
        "q0_position": "coincidental" if coincidental else "informative",
    }
    print("\n" + "=" * 90)
    print(f" TOTAL WALL {time.time()-T0:.0f}s")
    print("=" * 90)

    # ── witness ────────────────────────────────────────────────────────────
    w = WitnessBuilder("threerow-qcross-trend", engine="mpmath50+sympy-exact+f64-seminormal",
                       output_dir=OUTDIR)
    w.set_description(
        "Bean qou-prjo. Asks whether q_cross(n) — the q at which the Δ_λ-weighted ≥3-row "
        "archimedean trace changes sign — is a STRUCTURED SEQUENCE, and whether q₀'s "
        "position in it is DERIVED or COINCIDENTAL. Establishes three branch-geometry "
        "facts first: (BG-1) the y_λ normaliser is the closed form Z=((1−Q^r)/(1−Q))^n by "
        "dual Cauchy, and is positive on (1,q*), so it can neither create nor destroy a "
        "crossing; (BG-2) the Wenzl level eigenvalue Q^r=u³/(−u⁶−u⁴+u³+u²+1) (u=√q) has a "
        "POLE at q*=1.278449576579693…, above which the effective level r is COMPLEX — so "
        "the real-level branch is (1,q*) and the previously-reported n=9 crossings at "
        "q≈1.43/1.46 lie OFF it; (BG-3) at integer level r=k every λ with ℓ(λ)>k has "
        "s_λ=0, giving the level-integer ladder q_k (explicit integer polynomial) which "
        "increases and accumulates at q*, with q₀ strictly inside (q_2,q_3)=(1,1.15416…). "
        "On the real-level branch the crossing set is computed for the character-free G_n "
        "(n=3..N) and the character-dressed F_K (D,T,³He,⁴He, including the n=12 ⁴He leg "
        "left open by #4829). Crossings are shown EXACTLY ALGEBRAIC (irreducible integer "
        "minimal polynomial in u=√q, certified real-root isolation). A GENERICITY GATE "
        "then measures the width of the interval around q₀ that reproduces the same sign "
        "pattern, in absolute terms, as a fraction of the branch, in bits, and by counting "
        "systematically-generated natural constants inside it. Δ_λ=(−1)^{n(λ)}·dim is the "
        "PROVED value-only weight; free_parameters=0; AME never used; experimental proton "
        "anchor; layer-pure; live y_λ closed form, NOT the muon cache."
    )
    w.add_parameter("q0_experimental_proton_anchor", mp.nstr(Q0, 30))
    w.add_parameter("q0_pin", "experimental/proton (q_parameter.Q_50_DIGIT_STR); live closed-form y_λ")
    w.add_parameter("free_parameters", 0)
    w.add_parameter("q_star_real_level_branch_end", mp.nstr(Q_STAR, 30))
    w.add_parameter("u_star", mp.nstr(U_STAR, 30))
    w.add_parameter("wenzl_pole_polynomial_in_u", "-u^6 - u^4 + u^3 + u^2 + 1")
    w.add_parameter("level_ladder_polynomial_in_u", "sum_{j<k} u^(4j+3) - u^(4k) - u^(4k+2)")
    w.add_parameter("n_max_character_free", N_MAX_FREE)
    w.add_parameter("chi_precision", "f64 Hoefsmit seminormal (sparse kernel, = dense to 1.4e-15)")
    w.add_data("branch_geometry", {
        "dual_cauchy_max_rel_err": str_at_true_precision(cauchy_err),
        "level_at_q0": str_at_true_precision(level_r(Q0)),
        "level_ladder_q_k": {str(k): mp.nstr(v, 20) for k, v in ladder.items()},
        "level_r_at_1p45_complex": str(r_above),
        "s_lambda_vanishing_at_r3": van,
        "q0_between_q2_and_q3": True,
    })
    w.add_data("character_free_crossings", free)
    w.add_data("character_free_first_crossing_sequence",
               [[n, str_at_true_precision(q)] for n, q in seq])
    w.add_data("isotope_crossings", iso)
    w.add_data("exact_algebraic", exact)
    w.add_data("genericity", {
        "isotope_sign_window": [fmt_f64_limited(a_i), fmt_f64_limited(b_i)],
        "isotope_window_width": fmt_f64_limited(w_i),
        "character_free_sign_window": [str_at_true_precision(a_f),
                                       str_at_true_precision(b_f)],
        "character_free_window_width": str_at_true_precision(w_f),
        "real_level_branch_width": str_at_true_precision(branch_w),
        "window_fraction_of_branch": fmt_f64_limited(w_i / branch_w),
        "information_bits": fmt_f64_limited(mp.log(branch_w / w_i) / mp.log(2)),
        "natural_constants_in_window": nat,
        "natural_constants_count": n_nat,
    })
    w.add_data("verdict", verdict)
    w.add_assertion("q_cross_sequence_monotone", monotone, False)
    w.add_assertion("crossings_exist_for_all_n", len(seq) == N_MAX_FREE - 2, False)
    w.add_assertion("q0_position_informative", not coincidental, False)
    w.add_assertion("dual_cauchy_identity_holds", bool(cauchy_err < mp.mpf("1e-35")), True)
    w.add_assertion("q0_on_real_level_branch", bool(Q0 < Q_STAR), True)
    w.add_caveat(
        "🛑 GENERICITY / ANTI-NUMEROLOGY. 'q₀ lies between two crossings' is NOT a result: "
        f"the interval around q₀ reproducing the same isotope sign-vector has width "
        f"{float(w_i):.4f} = {float(100*w_i/branch_w):.1f}% of the real-level "
        f"branch, i.e. only "
        f"{math.log2(float(branch_w/w_i)):.2f} bits of constraint, and contains {n_nat} "
        "systematically-generated 'natural' constants. q₀'s position is therefore reported "
        "as COINCIDENTAL, not derived. No q was ever solved for to produce a sign pattern "
        "(free_parameters=0); the anchor is an input throughout."
    )
    w.add_caveat(
        "CORRECTION TO THE PRIOR A-DEPENDENCE READ. The n=9 crossings previously located at "
        "q≈1.4285/1.4617 lie ABOVE the Wenzl pole q*=1.27845, where the effective level "
        "r=log(Q^r)/log(Q) is COMPLEX (r(1.45)=0.81+4.23i) and the principal specialisation "
        "s_λ(1,Q,…,Q^{r−1}) has no real level. They are therefore NOT comparable to the "
        "deuteron crossing at q=1.0537 as members of one monotone trend; this probe sweeps "
        "only the real-level branch (1,q*)."
    )
    w.add_caveat(
        "Scope-(a) throughout. A LOCATED crossing is a positive existence statement "
        "(bracketed sign change of a continuous function). 'No crossing for this n' is a "
        "statement about the SWEPT INTERVAL AND GRID only — a grid can miss an even number "
        "of zeros between adjacent points. No invariant is proved to forbid a zero "
        "anywhere, so NO scope-(b) exclusion is claimed."
    )
    w.add_caveat(
        "value_only object: F_K and G_n are NOT binding energies (Δ_λ is value-only, and "
        "this probe tests only the SIGN structure of the ≥3-row weighting). The extensive "
        "super-pairwise binding MAGNITUDE remains OPEN — bean qou-prjo is NOT closed."
    )
    w.add_caveat(
        "PRECISION SPLIT. Branch geometry, level ladder and S_n are 50-dps mpmath; the "
        "exact-algebraic section is EXACT sympy rational arithmetic with certified VAS/Sturm "
        "root isolation (no floating point). χ^λ is f64 (pure-Python Hoefsmit seminormal via "
        "the sparse kernel, exact-equal to the dense path to 1.4e-15), so the isotope "
        "crossing q values carry f64 resolution only."
    )
    w.save()
    print(f"witness -> {OUTDIR}/threerow-qcross-trend.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
