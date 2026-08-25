#!/usr/bin/env python3
"""qborel_confluence_pos_probe.py — Attack B on the conjecture
"binding Borel variable = loop proper time" (balanced-kernel q→1 confluence
+ the (POS) kernel-positivity hypothesis).

Bean qou-xa89 (Attack B), epic qou-q04o. AUDIT-ONLY — scope-(a), NO FIT,
nothing wired. Target: conj:schwinger-measure-computational-time read in the
BALANCED q-Borel convention N^bal_q(n) = q^{−(n−1)(n−2)/4}·[n−1]_q! (the
fibre-level refinement forced by Attack E's bar-covariance falsifier;
docs/audits/2026-07-25-borel-propertime-attack-a-e.md). Attack A reduced the
conjecture to (POS) kernel positivity + (REP) (n−1)!-moment representability
via Stieltjes determinacy of {k!} (Carleman). Attack B asks the KERNEL-level
questions: (i) does the balanced fibre kernel confluesce to the classical
e^{−s}·ds as q → 1 (rate + exact h²-coefficient), and (ii) is there a
manifestly POSITIVE fibre kernel carrying exactly the balanced moments?

Reference read directly: Ramis–Sauloy–Zhang, "Local analytic classification
of q-difference equations" (Astérisque 355; library/arxiv-0903.0853v3/0903.0853v3.pdf):
  - Def 2.3.3 (p. 23): level-1 formal q-Borel B_{q,1}f(ξ) = Σ f_n q^{−n(n−1)/2}ξⁿ
    (|q| > 1 convention).
  - §3.3.1 (p. 39): level-d q-Borel via a family t_n with t_n = q^{n−d}t_{n−d};
    natural level-1 choice t_n = q^{n(n−1)/2}; theta-built families.
  - §1.2.1 (p. 7): the Borel/Laplace kernels are NOT canonical — several
    q-exponential-kernel choices and continuous or DISCRETE (Jackson-style)
    contours.
  - eq. (1.2) (p. 9): θ(z; q) = Σ_{n∈Z} q^{−n(n−1)/2} zⁿ
    = Π_{n≥0} (1−q^{−n−1})(1+q^{−n}z)(1+q^{−n−1}/z)  [Jacobi triple product],
    with θ(qz) = qz·θ(z). For REAL q > 1 and REAL z > 0 every factor is
    manifestly positive — the (POS) factorization.
  - §1.1.3 (p. 2): RSZ explicitly does NOT treat q → 1 confluence — it defers
    to Di Vizio–Zhang, "On q-summation and confluence", Ann. Inst. Fourier
    59(1):347–392 (2009) [their ref 21]. The rigorous kernel-convergence
    theorem is therefore NOT in RSZ; it is the named remaining gap.

INDEX CONVENTION (Attack A's A2 shift, kept throughout): all kernels are
stated as FINITE (probability) measures K with Stieltjes moments
∫ s^k K(ds) = N^bal(k+1), k ≥ 0 (mass N^bal(1) = 1); the conjecture's
ds/s-moment shape ∫ s^n (K(ds)/s) = N^bal(n) is the same statement.

BLOCKS
  C1  Structural identities, exact (sympy):
      (a) the theta-measure mechanism: m·k − m(m+1)/2 = k(k−1)/2 − j(j+1)/2
          at m = j + k — an exact polynomial identity in (j, k); it makes the
          discrete measure with atoms q^m and weights ∝ q^{−m(m+1)/2}
          (= 1/θ(q^m; q) up to θ(1), by θ(qz) = qz·θ(z)) have k-th moments
          ∝ q^{k(k−1)/2} for ALL k — the RSZ level-1 weight, realized by a
          positive Jackson-style discrete kernel;
      (b) balanced = bar-geometric mean: N^bal(n)² = N_q(n)·N_{q⁻¹}(n) and
          N^bal(n) = q^{+(n−1)(n−2)/4}·[n−1]_{q⁻¹}!, exact, n = 1..8.
  C2  THE h²-COEFFICIENT TEST (decisive check), exact (sympy), n = 1..8:
      log(N^bal_{e^h}(n)/(n−1)!) = 0·h + c₂(n)·h² + O(h⁴) with
      c₂(n) = Σ_{k=1}^{n−1}(k²−1)/24 = (n−1)(n−2)(2n+3)/144, compared as
      EXACT RATIONALS against Attack E's predicted target — per moment
      order n. (Also: the h¹ coefficient vanishes and the h³ coefficient
      vanishes — bar-invariance forces even parity in h.)
  C3  Confluence ladder, numerically exact (mpmath 60 dps):
      q_k = 1 + 10^{−k}, k = 1..6. dev(n) = N^bal(n)/(n−1)! − 1:
      n = 1, 2 → exactly 0; n = 3..8 → log-log slope of dev vs h = ln q
      in [1.9, 2.1] (the O(h²) rate; the fitted EXPONENT is a diagnostic of
      an exactly-known series structure, NOT a fitted physics constant),
      and the extracted dev/h² at k = 6 matches the exact rational c₂(n)
      to 1e−6 relative.
  C4  (POS) — the manifestly positive balanced fibre kernel, at
      q ∈ {1.2, q₀ muon pin, q₀ proton pin} (60 dps, tol 1e−30):
      the balanced moments factor as N^bal(k+1) = A(k)·B(k) with
      A(k) = [k]_{q⁻¹}! (bar-side q-Gamma) and B(k) = q^{+k(k−1)/4}
      (half-weight theta/Gaussian factor). Realizations, both = Mellin
      (multiplicative) convolutions of manifestly positive factors:
        C4a Jackson q-Gamma factor (p := q⁻¹ < 1): atoms t_m = p^m/(1−p),
            masses c_m = p^m·(p^{m+1}; p)_∞ > 0 (every factor 1−p^j > 0);
            moments Σ c_m t_m^k = [k]_p! (Jackson integral of Γ_p, the
            discrete positive kernel; RSZ §1.2.1's "Jackson style" contour).
        C4b theta factor (q̃ := q^{1/2}): atoms q̃^j (j ∈ Z), masses
            ∝ q̃^{−j(j+1)/2}/Θ₀ = (θ(1;q̃)/θ(q̃^j;q̃))/Θ₀ > 0; moments
            = q^{k(k−1)/4} exactly (C1a mechanism at base q̃); positivity of
            every RSZ-(1.2) triple-product factor checked on a grid.
        C4c log-normal factor: density w.r.t. ds/s of mass 1,
            exp(−(ln s − μ̂)²/(2σ²))/√(2πσ²), σ² = (ln q)/2, μ̂ = −(ln q)/4;
            moments e^{kμ̂ + k²σ²/2} = q^{k(k−1)/4} (verified by quadrature);
            manifestly positive (Gaussian density).
        C4d assembly: A(k)·B(k) = N^bal(k+1) exactly (both realizations) —
            (POS)∧(REP-balanced) is SATISFIABLE at fibre level: an explicit
            positive kernel with exactly the balanced moments EXISTS.
        C4e fibre INDETERMINACY (the honest converse): K^at (Jackson ⊛ theta,
            purely atomic) and K^ac (Jackson ⊛ log-normal, absolutely
            continuous) are DISTINCT positive measures sharing ALL balanced
            moments ⇒ at q ≠ 1 the balanced moment problem is INDETERMINATE:
            Attack A's determinacy forcing ("moments ⇒ kernel") is an
            ARCHIMEDEAN (q → 1) special feature, not available at the fibre.
            Consistency check: the Carleman terms N^bal(k+1)^{−1/(2k)} decay
            geometrically (ratio < q^{−1/16} for k = 100..200 at q = 1.2) ⇒
            Σ converges ⇒ Carleman's sufficient condition FAILS at the fibre.
  C5  Kernel-level confluence diagnostic (float64 — LOSSY, diagnostic only,
      NOT production precision): CDF of K^ac_q at s ∈ {1/2, 1, 2} vs the
      classical 1 − e^{−s} along q = 1 + 10^{−k}, k = 1..3: deviations
      shrink monotonically down the ladder (weak-convergence trend).

VERDICT SHAPE (scope-(a) throughout): the balanced kernel-level confluence
holds at the moment level with exact vanishing h¹ and exactly the Attack-E
h² target; a manifestly positive balanced fibre kernel exists (RSZ
theta/Jackson ingredients); the remaining gap to a THEOREM is the classical
kernel-convergence step (Fréchet–Shohat moment-convergence theorem + the
Carleman determinacy of the LIMIT sequence {k!}) — neither in Mathlib, and
explicitly outside RSZ (§1.1.3; Di Vizio–Zhang 2009 is the literature
route). Nothing here proves the conjecture: the substrate's kernel being
one of these positive realizations remains the open (POS)+(REP) content,
now with the sharpening that at q ≠ 1 the moments do NOT pin the kernel.

Exit 0 iff all assertions pass. Witness:
qborel-confluence-pos.witness.json (audit-only).
Audit doc: docs/audits/2026-07-25-qborel-confluence-pos-attack.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402
import math  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, sqrt as mpsqrt, quad as mpquad, exp as mpexp  # noqa: E402
from mpmath import log as mplog, pi as mppi  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0        # sympy exact / integer comparisons
TOL_50 = 1e-30       # 60-dps kernel-identity cross-checks (floor 1e-25)
TOL_QUAD = 1e-28     # quadrature-backed identity (tanh-sinh, 60 dps)
TOL_C2_NUM = 1e-6    # numeric h²-coefficient extraction at h = 1e-6
N_MOMENTS = 8        # symbolic / moment range (n = 1..8, k = 0..8)
LADDER_K = 6         # confluence ladder q = 1 + 10^{−k}, k = 1..6
RATE_LO, RATE_HI = 1.9, 2.1   # rate-exponent bracket (diagnostic)

# q₀, both pins, 50-digit strings with provenance (muon from the canonical
# witness; proton from qou_substrate.constants Q_50_DIGIT_STR).
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28; _solve_q_proton_f64 + mpmath refine):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_q, _h = sp.symbols("q h", positive=True)
_jj, _kk, _mm = sp.symbols("j k m", integer=True)


def qint(qv, kk: int):
    """One-sided quantum integer [k]_q = 1 + q + … + q^{k−1} (corpus
    convention, QOU.Mass.QDifferenceConfluentObstruction.qint)."""
    return sum(qv ** i for i in range(kk))


def qfact(qv, m: int):
    """[m]_q! = ∏_{j=1}^{m} [j]_q; N_q(n) = qfact(q, n−1)."""
    r = sp.Integer(1)
    for j in range(1, m + 1):
        r *= qint(qv, j)
    return r


def balanced_normalizer(qv, n: int):
    """N^bal_q(n) = q^{−(n−1)(n−2)/4}·[n−1]_q! (sympy)."""
    m = n - 1
    return qv ** (-sp.Rational(m * (m - 1), 4)) * qfact(qv, m)


def c2_target(n: int):
    """Attack E's predicted h² coefficient Σ_{k=1}^{n−1}(k²−1)/24 (exact)."""
    return sp.Rational(sum(k * k - 1 for k in range(1, n)), 24)


# --------------------------------------------------------- mpmath kernels

def mp_balanced_ratio(q0: mpf, n: int) -> mpf:
    """N^bal_q(n)/(n−1)! at 60 dps (exact product formula)."""
    m = n - 1
    r = mpf(1)
    for j in range(1, m + 1):
        r *= (q0 ** j - 1) / (q0 - 1)
    r *= q0 ** (-mpf(m * (m - 1)) / 4)
    for j in range(2, m + 1):
        r /= j
    return r


def jackson_factor(q0: mpf, k_max: int, tail_dps: int = 42):
    """Jackson q-Gamma kernel at p = 1/q0: atoms t_m = p^m/(1−p), masses
    c_m = p^m·(p^{m+1};p)_∞ = p^m·(p;p)_∞/(p;p)_m > 0. Returns
    (atoms, masses, moments[0..k_max]). Truncation: p^M < 10^{−tail_dps}."""
    p = 1 / q0
    M = int(tail_dps / -mp.log10(p)) + 60
    pp = [mpf(1)]
    for j in range(1, M + 1):
        pp.append(pp[-1] * (1 - p ** j))
    pp_inf = pp[-1]
    a = 1 / (1 - p)
    atoms = [a * p ** m for m in range(M)]
    masses = [p ** m * pp_inf / pp[m] for m in range(M)]
    moments = []
    for k in range(k_max + 1):
        moments.append(sum(c * t ** k for c, t in zip(masses, atoms)))
    return atoms, masses, moments


def theta_factor(q0: mpf, k_max: int, tail_dps: int = 42):
    """Half-weight theta kernel at q̃ = √q0: atoms q̃^j (j ∈ Z), masses
    q̃^{−j(j+1)/2}/Θ₀ > 0 (= (θ(1;q̃)/θ(q̃^j;q̃))/Θ₀ by θ(q̃z) = q̃z·θ(z)).
    Returns (js, atoms, masses, moments[0..k_max]); moment target is
    q0^{k(k−1)/4}."""
    qt = mpsqrt(q0)
    # |j| ≤ J with q̃^{−J(J+1)/2}·q̃^{J·k_max} < 10^{−tail_dps}
    J = 10
    while float((J * (J + 1) / 2 - J * k_max) * mp.log10(qt)) < tail_dps + 10:
        J += 10
    js = list(range(-J, J + 1))
    w = [qt ** (-mpf(j * (j + 1)) / 2) for j in js]
    Theta0 = sum(w)
    atoms = [qt ** j for j in js]
    masses = [x / Theta0 for x in w]
    moments = []
    for k in range(k_max + 1):
        moments.append(sum(c * t ** k for c, t in zip(masses, atoms)))
    return js, atoms, masses, moments


def rsz_theta_triple_product(z: mpf, qt: mpf, tail_dps: int = 42) -> mpf:
    """RSZ eq. (1.2): θ(z;q̃) = Π_{n≥0}(1−q̃^{−n−1})(1+q̃^{−n}z)(1+q̃^{−n−1}/z)
    for |q̃| > 1 — every factor manifestly positive for real q̃ > 1, z > 0."""
    N = int(tail_dps / float(mp.log10(qt))) + 40
    r = mpf(1)
    for n in range(N):
        r *= (1 - qt ** (-n - 1)) * (1 + qt ** (-n) * z) \
            * (1 + qt ** (-n - 1) / z)
    return r


# ---------------------------------------------------------------- Block C1

def block_c1_structural(wb: WitnessBuilder) -> None:
    """C1: theta-measure mechanism (exact polynomial identity) + balanced
    = bar-geometric-mean identities."""
    # (a) reindex m = j + k: m·k − m(m+1)/2 == k(k−1)/2 − j(j+1)/2
    lhs = _mm * _kk - sp.Rational(1, 2) * _mm * (_mm + 1)
    rhs = sp.Rational(1, 2) * _kk * (_kk - 1) \
        - sp.Rational(1, 2) * _jj * (_jj + 1)
    d = sp.expand(lhs.subs(_mm, _jj + _kk) - rhs)
    assert d == 0, d
    wb.add_assertion(
        "theta_measure_mechanism", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source="exact polynomial identity m·k − m(m+1)/2 = k(k−1)/2 − "
               "j(j+1)/2 at m = j+k: the discrete measure with atoms q^m "
               "and weights ∝ q^{−m(m+1)/2} (equivalently 1/θ(q^m;q) up to "
               "θ(1), via RSZ eq (1.2) functional equation θ(qz) = qz·θ(z)) "
               "has k-th moments ∝ q^{k(k−1)/2} for ALL k — the RSZ "
               "Def-2.3.3 level-1 q-Borel weight is realized by a POSITIVE "
               "Jackson-style discrete kernel (RSZ §1.2.1 discrete-contour "
               "menu)")
    # (b) balanced = geometric mean of the bar pair; and the bar-side form
    for n in range(1, N_MOMENTS + 1):
        m = n - 1
        Nb = balanced_normalizer(_q, n)
        d1 = sp.simplify(Nb ** 2 - qfact(_q, m) * qfact(1 / _q, m))
        assert d1 == 0, n
        d2 = sp.simplify(
            Nb - _q ** (sp.Rational(m * (m - 1), 4)) * qfact(1 / _q, m))
        assert d2 == 0, n
    wb.add_assertion(
        "balanced_geometric_mean", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source="N^bal(n)² = N_q(n)·N_{q⁻¹}(n) and N^bal(n) = "
               "q^{+(n−1)(n−2)/4}·[n−1]_{q⁻¹}! exactly (n = 1..8): the "
               "balanced normalizer is the geometric mean of the bar pair — "
               "the bar-symmetrized q-Borel weight, and the split used by "
               "the positive kernel construction (C4)")


# ---------------------------------------------------------------- Block C2

def block_c2_h2_exact(wb: WitnessBuilder) -> dict:
    """C2: THE decisive check — exact h² coefficient per n vs Attack E's
    target Σ(k²−1)/24, as exact rationals."""
    rows = {}
    for n in range(1, N_MOMENTS + 1):
        m = n - 1
        expr = sp.log(
            (balanced_normalizer(_q, n) / sp.factorial(m)).subs(
                _q, sp.exp(_h)))
        ser = sp.series(expr, _h, 0, 4).removeO()
        c1 = sp.expand(ser).coeff(_h, 1)
        c2 = sp.expand(ser).coeff(_h, 2)
        c3 = sp.expand(ser).coeff(_h, 3)
        pred = c2_target(n)
        closed = sp.Rational((n - 1) * (n - 2) * (2 * n + 3), 144)
        assert c1 == 0, (n, c1)                       # balanced: no h¹
        assert c3 == 0, (n, c3)                       # bar-parity: no h³
        assert sp.simplify(c2 - pred) == 0, (n, c2, pred)   # THE test
        assert pred == closed, (n, pred, closed)      # closed form
        rows[n] = str(pred)
    # closed form symbolically: Σ_{k=1}^{n−1}(k²−1)/24 = (n−1)(n−2)(2n+3)/144
    nsym = sp.symbols("n", positive=True, integer=True)
    S = sp.summation((_kk ** 2 - 1) / 24, (_kk, 1, nsym - 1))
    d = sp.simplify(S - (nsym - 1) * (nsym - 2) * (2 * nsym + 3) / 144)
    assert d == 0, d
    wb.add_assertion(
        "h2_coefficient_exact_match", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source="log(N^bal_{e^h}(n)/(n−1)!) = c₂(n)·h² + O(h⁴) with h¹ AND "
               "h³ coefficients exactly 0 (bar-invariance ⇒ even in h) and "
               "c₂(n) EXACTLY equal (as rationals, n = 1..8) to Attack E's "
               "next-order falsifier target Σ_{k=1}^{n−1}(k²−1)/24 "
               "= (n−1)(n−2)(2n+3)/144 (closed form proved symbolically): "
               "the balanced confluence structure is verified through "
               "second order — MATCH (support, not proof)")
    wb.add_data("h2_exact_coefficients", rows)
    return rows


# ---------------------------------------------------------------- Block C3

def block_c3_ladder(wb: WitnessBuilder) -> None:
    """C3: confluence ladder q = 1 + 10^{−k}, k = 1..6 — rate exponent and
    numeric h²-coefficient extraction (numerically exact values; the fitted
    EXPONENT is a diagnostic, not a fitted physics constant)."""
    ladder = [mpf(1) + mpf(10) ** (-k) for k in range(1, LADDER_K + 1)]
    # n = 1, 2: deviation exactly 0 ([0]! and [1]^bal = 1 exactly)
    for q0 in ladder:
        for n in (1, 2):
            assert mp_balanced_ratio(q0, n) - 1 == 0, (n, q0)
    slopes, extract = {}, {}
    for n in range(3, N_MOMENTS + 1):
        xs, ys = [], []
        for q0 in ladder:
            hh = mplog(q0)
            dev = mp_balanced_ratio(q0, n) - 1
            assert dev > 0
            xs.append(mplog(hh))
            ys.append(mplog(dev))
        N = len(xs)
        xbar = sum(xs) / N
        ybar = sum(ys) / N
        slope = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) \
            / sum((x - xbar) ** 2 for x in xs)
        slopes[n] = float(slope)
        assert RATE_LO < slope < RATE_HI, (n, slope)
        # numeric h² extraction at the smallest rung vs exact rational
        q0 = ladder[-1]
        hh = mplog(q0)
        c2_num = (mp_balanced_ratio(q0, n) - 1) / hh ** 2
        c2_ex = mpf(c2_target(n).p) / mpf(c2_target(n).q)
        rel = abs(c2_num / c2_ex - 1)
        assert rel < TOL_C2_NUM, (n, rel)
        extract[n] = {"slope": float(slope),
                      "c2_numeric_at_k6": mp.nstr(c2_num, 20),
                      "c2_exact": str(c2_target(n)),
                      "rel_err": mp.nstr(rel, 5)}
    wb.add_assertion(
        "confluence_rate_h2",
        computed=float(max(abs(s - 2) for s in slopes.values())),
        expected="0", tolerance=0.1,
        source=f"max |slope − 2| over n = 3..{N_MOMENTS} (slopes "
               f"{min(slopes.values()):.4f}..{max(slopes.values()):.4f}): "
               f"log-log fit of |N^bal_q(n)/(n−1)! − 1| vs h = ln q over "
               f"q = 1+10^(−k), k = 1..{LADDER_K} (60 dps, exact product "
               f"formula): slope in [{RATE_LO}, {RATE_HI}] for every "
               f"n = 3..{N_MOMENTS}, and the extracted dev/h² at k = 6 "
               f"matches the exact rational c₂(n) to < {TOL_C2_NUM} rel — "
               f"the balanced moments converge to (n−1)! at rate O((ln q)²) "
               f"with zero first order; n = 1, 2 deviations are exactly 0. "
               f"The fitted exponent is a DIAGNOSTIC of the exactly-proved "
               f"C2 series structure, not a fitted physics constant")
    wb.add_data("confluence_ladder", extract)


# ---------------------------------------------------------------- Block C4

def block_c4_pos_kernel(wb: WitnessBuilder, q_name: str, q_str: str) -> None:
    """C4: the manifestly positive balanced kernel at one q value —
    Jackson (C4a), theta (C4b), log-normal (C4c) factors; assembly (C4d);
    fibre-indeterminacy witness (C4e runs only for q_name == 'test')."""
    q0 = mpf(q_str)
    hh = mplog(q0)
    qt = mpsqrt(q0)

    # C4a — Jackson q-Gamma factor at p = 1/q
    atoms_j, masses_j, mom_j = jackson_factor(q0, N_MOMENTS)
    assert min(masses_j) > 0
    p = 1 / q0
    worst_a = mpf(0)
    for k in range(N_MOMENTS + 1):
        tgt = mpf(1)
        for j in range(1, k + 1):
            tgt *= (1 - p ** j) / (1 - p)         # [k]_p!
        worst_a = max(worst_a, abs(mom_j[k] / tgt - 1))
    assert worst_a < TOL_50, worst_a

    # C4b — theta factor at q̃ = √q; masses = RSZ 1/θ values on the grid
    js, atoms_t, masses_t, mom_t = theta_factor(q0, N_MOMENTS)
    assert min(masses_t) > 0
    worst_b = mpf(0)
    for k in range(N_MOMENTS + 1):
        tgt = q0 ** (mpf(k * (k - 1)) / 4)
        worst_b = max(worst_b, abs(mom_t[k] / tgt - 1))
    assert worst_b < TOL_50, worst_b
    # cross-check masses against the RSZ eq-(1.2) triple product:
    # q̃^{−j(j+1)/2} = θ(1;q̃)/θ(q̃^j;q̃), and every triple-product factor > 0
    th1 = rsz_theta_triple_product(mpf(1), qt)
    worst_th = mpf(0)
    for j in (-3, -2, -1, 0, 1, 2, 3):
        thj = rsz_theta_triple_product(qt ** j, qt)
        worst_th = max(worst_th,
                       abs((th1 / thj) / qt ** (-mpf(j * (j + 1)) / 2) - 1))
    assert worst_th < TOL_QUAD, worst_th
    # positivity grid of the factorization itself
    for j in range(-8, 9):
        z = qt ** j
        for nfac in range(0, 120):
            assert (1 - qt ** (-nfac - 1)) > 0
            assert (1 + qt ** (-nfac) * z) > 0
            assert (1 + qt ** (-nfac - 1) / z) > 0

    # C4c — log-normal factor: σ² = h/2, μ̂ = −h/4, mass 1
    sig2 = hh / 2
    muh = -hh / 4
    worst_c = mpf(0)
    for k in range(N_MOMENTS + 1):
        val = mpquad(
            lambda u, k=k: mpexp(k * u - (u - muh) ** 2 / (2 * sig2))
            / mpsqrt(2 * mppi * sig2), [-mp.inf, mp.inf])
        tgt = q0 ** (mpf(k * (k - 1)) / 4)
        worst_c = max(worst_c, abs(val / tgt - 1))
    assert worst_c < TOL_QUAD, worst_c
    # density positivity grid (manifest — Gaussian)
    for u10 in range(-30, 31):
        u = mpf(u10) / 10
        assert mpexp(-(u - muh) ** 2 / (2 * sig2)) > 0

    # C4d — assembly: A(k)·B(k) == N^bal(k+1), both realizations
    worst_d = mpf(0)
    for k in range(N_MOMENTS + 1):
        nbal = mp_balanced_ratio(q0, k + 1)
        for j in range(2, k + 1):
            nbal *= j                              # back to N^bal(k+1)
        for mom_B in (mom_t[k], q0 ** (mpf(k * (k - 1)) / 4)):
            got = mom_j[k] * mom_B
            worst_d = max(worst_d, abs(got / nbal - 1))
    assert worst_d < TOL_50, worst_d

    wb.add_assertion(
        f"pos_kernel_{q_name}", computed=mp.nstr(
            max(worst_a, worst_b, worst_d), 5),
        expected="0", tolerance=TOL_50,
        source=f"q = {q_name} ({mp.nstr(q0, 12)}…): the balanced moments "
               f"factor exactly as N^bal(k+1) = [k]_{{q⁻¹}}!·q^{{k(k−1)/4}} "
               f"(k = 0..{N_MOMENTS}, rel < 1e−30) and BOTH factors are "
               f"moments of manifestly positive measures — Jackson q-Gamma "
               f"kernel at p = q⁻¹ (atoms p^m/(1−p), masses "
               f"p^m·(p^{{m+1}};p)_∞ > 0) and the half-weight theta kernel "
               f"at q̃ = √q (atoms q̃^j, masses ∝ 1/θ(q̃^j;q̃) > 0 by the RSZ "
               f"eq-(1.2) triple product, every factor positive on the "
               f"grid; log-normal continuous variant verified by "
               f"quadrature, rel < 1e−28). Mellin convolution ⇒ an "
               f"EXPLICIT positive kernel with exactly the balanced "
               f"moments exists: (POS)∧(REP-balanced) is satisfiable at "
               f"the fibre")
    if q_name == "test":
        # C4e — fibre indeterminacy + Carleman failure (q-independent
        # structure; run once at the test value)
        # atom of K^at at s = 1 (j = 0 theta atom × Jackson atoms): the
        # atomic realization has strictly positive point masses while the
        # log-normal realization is absolutely continuous — two DISTINCT
        # positive measures, ALL moments equal (exact identities above).
        atom_mass = masses_t[js.index(0)] * masses_j[0]
        assert atom_mass > 0
        terms = []
        for k in range(1, 201):
            nb = mp_balanced_ratio(q0, k + 1)
            for j in range(2, k + 1):
                nb *= j
            terms.append(nb ** (-1 / mpf(2 * k)))
        ratios = [terms[k] / terms[k - 1] for k in range(100, 200)]
        bound = q0 ** (-mpf(1) / 16)
        assert max(ratios) < bound, (max(ratios), bound)
        wb.add_assertion(
            "fibre_indeterminacy", computed="0", expected="0",
            tolerance=TOL_EXACT,
            source="0 = #violations of [Carleman-term ratio "
                   f"N^bal(k+1)^(−1/(2k)) step < q^(−1/16) = "
                   f"{mp.nstr(bound, 8)}], observed max ratio "
                   f"{mp.nstr(max(ratios), 8)} (k = 100..200). "
                   "At q = 1.2: (i) the atomic realization K^at = Jackson ⊛ "
                   "theta has strictly positive point masses (e.g. mass "
                   f"{mp.nstr(atom_mass, 8)} against the s = t₀ atom "
                   "product) while K^ac = Jackson ⊛ log-normal is "
                   "absolutely continuous — two DISTINCT positive measures "
                   "with ALL balanced moments equal (exact factor "
                   "identities): the balanced moment problem at q ≠ 1 is "
                   "INDETERMINATE; (ii) consistently, the Carleman terms "
                   "N^bal(k+1)^{−1/(2k)} decay geometrically (ratio < "
                   "q^{−1/16} for k = 100..200) so Σ converges — Carleman's "
                   "sufficient condition fails at the fibre. Determinacy "
                   "('moments ⇒ kernel', Attack A) is an ARCHIMEDEAN q → 1 "
                   "feature only")


# ---------------------------------------------------------------- Block C5

def block_c5_cdf_confluence(wb: WitnessBuilder) -> None:
    """C5: kernel-level (CDF) confluence diagnostic — float64, LOSSY,
    diagnostic only (per compute-author §1.1 the f64 path is cross-check
    grade; the production-precision claims live in C2/C3/C4)."""
    s_points = [0.5, 1.0, 2.0]
    devs = {s: [] for s in s_points}
    for kk in range(1, 4):
        q0 = 1.0 + 10.0 ** (-kk)
        p = 1.0 / q0
        hh = math.log(q0)
        sig = math.sqrt(hh / 2)
        muh = -hh / 4
        M = int(18 / -math.log10(p)) + 50
        # Jackson masses (float): c_m = p^m (p;p)_inf/(p;p)_m
        logpp = [0.0]
        for j in range(1, M + 1):
            logpp.append(logpp[-1] + math.log1p(-p ** j))
        logpp_inf = logpp[-1]
        a = 1 / (1 - p)
        for s in s_points:
            F = 0.0
            for m in range(M):
                cm = math.exp(m * math.log(p) + logpp_inf - logpp[m])
                tm = a * p ** m
                z = (math.log(s / tm) - muh) / sig
                F += cm * 0.5 * (1 + math.erf(z / math.sqrt(2)))
            devs[s].append(abs(F - (1 - math.exp(-s))))
    shrink = []
    for s in s_points:
        assert devs[s][0] > devs[s][1] > devs[s][2], (s, devs[s])
        assert devs[s][2] < 1e-6, (s, devs[s])
        shrink += [devs[s][0] / devs[s][1], devs[s][1] / devs[s][2]]
        # per-decade shrink ≈ ×100 ⇒ the CDF converges at ~O(h²) too
        assert 50 < devs[s][0] / devs[s][1] < 200, (s, devs[s])
        assert 50 < devs[s][1] / devs[s][2] < 200, (s, devs[s])
    wb.add_assertion(
        "cdf_confluence_diagnostic", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source="0 = #violations of [CDF deviation monotone ↓, < 1e−6 at "
               "q = 1.001, per-decade shrink in (50, 200)]; observed max "
               f"dev at k = 3: {max(d[2] for d in devs.values()):.2e}, "
               f"shrink factors {min(shrink):.1f}..{max(shrink):.1f}. "
               "CDF of the a.c. balanced kernel K^ac_q (Jackson ⊛ "
               "log-normal) at s ∈ {1/2, 1, 2} vs the classical "
               "1 − e^{−s}: deviations shrink ×~100 per ladder decade — "
               "the kernel-level (CDF) confluence toward e^{−s}·ds is "
               "empirically O(h²) as well, matching the balanced moment "
               "rate (float64 LOSSY diagnostic only; the precise "
               "confluence statements are the exact/60-dps moment results "
               "C2-C4; the rigorous kernel-convergence theorem is the "
               "named remaining gap — Fréchet–Shohat + Carleman, outside "
               "RSZ per §1.1.3, literature route Di Vizio–Zhang 2009)")
    wb.add_data("cdf_ladder_float64_diagnostic",
                {str(s): [f"{d:.6e}" for d in devs[s]] for s in s_points})


def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("qborel-confluence-pos", engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "Attack B on the conjecture 'binding Borel variable = loop proper "
        "time' — balanced-kernel q→1 confluence + the (POS) hypothesis "
        "(bean qou-xa89, epic qou-q04o; audit-only, scope-(a), NO FIT, "
        "nothing wired). C1: the RSZ level-1 q-Borel theta weight "
        "q^{−m(m+1)/2} (Def 2.3.3 + eq (1.2), Astérisque 355) is realized "
        "by a positive Jackson-style discrete kernel (exact reindex "
        "identity); the balanced normalizer is the bar-geometric mean "
        "√(N_q·N_{q⁻¹}), exact. C2 (decisive): the h² coefficient of "
        "log(N^bal_{e^h}(n)/(n−1)!) EXACTLY equals Attack E's target "
        "Σ_{k=1}^{n−1}(k²−1)/24 = (n−1)(n−2)(2n+3)/144 for n = 1..8, with "
        "h¹ and h³ coefficients exactly 0 — MATCH: balanced confluence "
        "verified through second order. C3: ladder q = 1+10^{−k}, k = 1..6 "
        "confirms the O((ln q)²) rate (log-log slope in [1.9, 2.1], "
        "diagnostic exponent) and the numeric c₂ extraction matches the "
        "exact rationals to 1e−6. C4: (POS) at the fibre — the balanced "
        "moments factor exactly as [k]_{q⁻¹}!·q^{k(k−1)/4}, and BOTH "
        "factors are moments of manifestly positive kernels (Jackson "
        "q-Gamma at p = q⁻¹; the RSZ theta kernel at q̃ = √q, positive via "
        "the eq-(1.2) triple product; log-normal continuous variant): an "
        "explicit positive kernel with exactly the balanced moments EXISTS "
        "(verified at q = 1.2 and both q₀ pins, rel 1e−30). HONEST "
        "CONVERSE (C4e): atomic and a.c. realizations share ALL moments ⇒ "
        "the balanced moment problem at q ≠ 1 is INDETERMINATE (Carleman "
        "terms decay geometrically) — determinacy is an archimedean-only "
        "feature; at the fibre, moments do NOT pin the kernel. C5: CDF "
        "confluence trend toward e^{−s}·ds (float64 diagnostic). Remaining "
        "named gap: the rigorous kernel-convergence theorem (Fréchet–"
        "Shohat moment-convergence + Carleman determinacy of {k!}; "
        "explicitly outside RSZ per §1.1.3 — literature route Di "
        "Vizio–Zhang, Ann. Inst. Fourier 59 (2009) 347–392) plus the open "
        "(POS)+(REP) identification of the SUBSTRATE's kernel with one of "
        "the positive realizations. Nothing here proves the conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-07-25-qborel-confluence-pos-attack.md")

    block_c1_structural(wb)
    print("C1: theta-measure mechanism + balanced = bar-geometric mean, "
          "exact.")
    block_c2_h2_exact(wb)
    print("C2: h² coefficient == Σ(k²−1)/24 EXACT per n = 1..8; h¹ = h³ = 0 "
          "— MATCH.")
    block_c3_ladder(wb)
    print("C3: ladder rate O(h²) confirmed (slopes ≈ 2), numeric c₂ matches "
          "exact rationals.")
    for name, qs in (("test", "1.2"), ("muon", Q0_MUON_STR),
                     ("proton", Q0_PROTON_STR)):
        block_c4_pos_kernel(wb, name, qs)
        print(f"C4[{name}]: positive balanced kernel verified "
              f"(Jackson × theta/log-normal), rel < 1e-30.")
    block_c5_cdf_confluence(wb)
    print("C5: CDF confluence trend toward e^(−s)·ds (float diagnostic).")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.add_data("rsz_citations", {
        "paper": "library/arxiv-0903.0853v3/0903.0853v3.pdf — Ramis–Sauloy–Zhang, Astérisque "
                 "355",
        "def_2_3_3": "level-1 formal q-Borel, weight q^{−n(n−1)/2} (p. 23)",
        "sec_3_3_1": "level-d q-Borel families t_n = q^{n−d}t_{n−d}; "
                     "theta-built (p. 39)",
        "eq_1_2": "θ(z;q) = Σ q^{−n(n−1)/2}zⁿ = Π(1−q^{−n−1})(1+q^{−n}z)"
                  "(1+q^{−n−1}/z), θ(qz) = qz·θ(z) (p. 9) — the manifest "
                  "positivity factorization for real q > 1, z > 0",
        "sec_1_2_1": "kernel non-canonicity; continuous or discrete "
                     "Jackson-style contours (p. 7)",
        "sec_1_1_3": "confluence q → 1 explicitly NOT treated in RSZ; "
                     "deferred to Di Vizio–Zhang, Ann. Inst. Fourier 59 "
                     "(2009) 347–392 (p. 2) — the named remaining gap",
    })
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
