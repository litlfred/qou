#!/usr/bin/env python3
"""borel_propertime_moment_attack_probe.py — Attacks A + E on the conjecture
"binding Borel variable = loop proper time".

Beans qou-7gu9 (Attack A, moment-determinacy) + qou-zfl0 (Attack E,
falsifier-first), epic qou-q04o. AUDIT-ONLY — scope-(a), NO FIT, nothing
wired. The target conjecture (being authored as a content block by a sibling
agent) identifies the Borel-plane variable of the binding OGF resummation —
the C1 carrier of QOU/Mass/KeystoneBridgeC1Binding.lean, whose normalizer
N(n) = (n−1)! is PROVED forced by n·N(n) = n! — with the Schwinger proper
time s of the ζ-regularized photon determinant ∫₀^∞ (ds/s)·Tr e^{−sΔ} on
Jac(Bring) (the a₀ = 1/(4π) leg; SchwingerMeasureShape.lean). Source lead:
docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md §d′/§5.

ATTACK A — moment-determinacy reduction (formalize-first narrowing):
  A1  Moment identity, exact: ∫₀^∞ sⁿ e^{−s} ds/s = Γ(n) = (n−1)!,
      n = 1..8 (sympy). The keystone-forced normalizer IS the n-th moment
      of the unit (c = 1) Schwinger kernel.
  A2  Honesty at n = 0: ∫₀^∞ e^{−s} ds/s = ∞ — the kernel e^{−s}·ds/s is
      an INFINITE measure at s = 0. Determinacy therefore lives on the
      index-shifted FINITE measure e^{−s}·ds with Stieltjes moments
      m_k = ∫ s^k e^{−s} ds = k! = N(k+1), k ≥ 0.
  A3  Carleman verdict, exact: the Stieltjes problem for {k!} is
      DETERMINATE. Stirling: lim (k!)^{1/(2k)}/√k = e^{−1/2} (sympy exact
      limit), so the Carleman terms (k!)^{−1/(2k)} ~ √(e/k); the exact
      inequality k! ≤ k^{2k} (k ≥ 1) gives (k!)^{−1/(2k)} ≥ 1/k, and
      Σ 1/k = ∞ ⇒ Σ (k!)^{−1/(2k)} = ∞: Carleman's condition holds, so
      e^{−s}·ds is the UNIQUE positive measure on (0,∞) with these
      moments [Ref: Berg / Simon, classical Stieltjes moment theory].
  A4  Stieltjes consistency, exact: Hankel determinants det[(i+j)!] > 0
      and det[(i+j+1)!] > 0, sizes 1..6 (integers) — {k!} satisfies the
      positive-definiteness the determinate representation requires.
  A5  Unit forcing distinguisher (r2core B5 refined): with kernel
      c·e^{−s}·ds/s the moments are c·(n−1)!; the PROVED bridge identity
      n·N(n) = n! forces c = 1 exactly; c = ½ fails for every n.
  A6  Binding-side positivity STATUS (corpus facts, computed exactly):
      (i) I(n) > 0 (Lean-proved involutionNumber_pos; recomputed to
      n = 40); (ii) the normalized C1 carrier b_n = I(n)/n! is NOT
      log-convex (b_2² = 1 > b_1·b_3 = 2/3) — so {b_n} is NOT itself a
      Stieltjes moment sequence; the positive-measure hypothesis of the
      reduction is about the RESUMMATION KERNEL, not the carrier
      coefficients; (iii) the RAW binding periods B_n = I(n)/n ARE
      log-convex for 2 ≤ n ≤ 39 (necessary Stieltjes condition passes —
      recorded as status, NOT a representability proof).

  REDUCTION (the deliverable of Attack A): since {N(k+1)} = {k!} is a
  DETERMINATE Stieltjes sequence (A3), the conjecture reduces to exactly
  two open hypotheses: (i) POSITIVITY — the binding Borel resummation
  kernel K_b(s)·ds (the weight realizing B_n = b_n·∫ sⁿ K_b(s) ds/s) is a
  positive measure on (0,∞); (ii) REPRESENTABILITY — its ds/s-moments are
  the keystone-forced (n−1)!. Given (i)+(ii), determinacy forces
  K_b(s)·ds = e^{−s}·ds — the binding Borel variable and the loop proper
  time then carry THE SAME kernel, which is the identification up to the
  variable naming. Neither hypothesis is proved; both are named in the
  conditional Lean class (BorelProperTimeMoment.lean, no instance).

ATTACK E — falsifier-first (one computable consequence beyond the shared
Γ(n) moments; exact, both q₀ pins):
  E1  Bar-involution falsifier. Loop proper time s is REAL ⇒ bar-invariant
      (bar: q ↦ q⁻¹ acts trivially on s). The binding side's q-Borel
      normalizer N_q(n) = [n−1]_q! (one-sided [k]_q = 1+q+…+q^{k−1}, the
      corpus convention of KeystoneBridgeC1Binding) transforms with an
      exact nontrivial weight:
          [k]_{q⁻¹} = q^{1−k}·[k]_q   ⇒   N_{q⁻¹}(n) = q^{−(n−1)(n−2)/2}·N_q(n).
      Verified symbolically n = 1..8. VERDICT: FAIL for the identification
      as stated with the one-sided normalizer at q ≠ 1 — the binding Borel
      variable is bar-COVARIANT (weight q^{−(n−1)(n−2)/2} ≠ 1 for n ≥ 3),
      the loop proper time bar-INVARIANT. Scope-(a): refutes the stated
      unbalanced-kernel identification only, at q ≠ 1; at q = 1 (the
      archimedean/classical shadow, where the loop lives) the weight is 1
      and nothing is refuted.
  E2  The exact repair (the bar-projection caveat, constructive): the
      BALANCED normalizer N_q^bal(n) = q^{−(n−1)(n−2)/4}·[n−1]_q!
      (equivalently ∏[k]^bal with [k]^bal = (q^{k/2}−q^{−k/2})/(q^{1/2}−q^{−1/2}),
      the corpus's BalancedQuantumTwist convention) is EXACTLY
      bar-invariant (verified symbolically n = 1..8) — the identification
      survives iff the conjecture's kernel is read in the balanced
      convention.
  E3  Subleading (q → 1) structure falsifier. Per-moment relative
      corrections, exact series:
        unbalanced:  N_q(n)/(n−1)! = 1 + (q−1)·(n−1)(n−2)/4 + O((q−1)²)
                     — QUADRATIC in n;
        balanced:    N_q^bal(n)/(n−1)! = 1 + 0·(q−1) + O((q−1)²); at
                     q = e^h the h² coefficient is Σ_{k=1}^{n−1}(k²−1)/24
                     (exact) — NO first-order q-correction;
        loop side:   a heat-kernel a₁-correction gives moments
                     (n−1)!·(1 + (a₁/A)·n + …) — LINEAR in n (exact:
                     ∫ s^{n+1}e^{−s}ds/s = n·(n−1)!).
      VERDICT: the unbalanced first-order pattern (quadratic in n) matches
      NEITHER the loop side's q-independence at fixed geometry (0) NOR any
      a₁-type curvature correction (linear in n) — same FAIL as E1, now at
      the moment level with the exact discrepancy (n−1)(n−2)/4·(q−1). The
      balanced kernel's vanishing first-order correction matches the loop
      side's q-independence — PASS (still unproved) with the bar-projection
      caveat. The surviving q²-order coefficient Σ(k²−1)/24 is recorded as
      the next-order falsifier target (would have to be matched by a
      2nd-order structure on the loop side if the q-direction maps to any
      loop deformation at all).
  E4  Pin numerics (both q₀ pins, 50 dps): the actual size of the
      unbalanced defect at q₀ — e.g. n = 6: (q₀−1)·5 ≈ 0.55 relative, an
      O(1) discrepancy, NOT a small correction — and the pin-shift of the
      weights (~1e-8 relative, matching the known pin separation; recorded,
      not scored).

Exit 0 iff all assertions pass. Witness:
borel-propertime-moment-attack.witness.json (audit-only).
Audit doc: docs/audits/2026-07-25-borel-propertime-attack-a-e.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402
from fractions import Fraction  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0             # sympy exact / integer comparisons
N_MOMENTS = 8             # A1/E1/E2 symbolic range
N_HANKEL = 6              # A4 Hankel sizes
N_LOGCONVEX = 40          # A6 raw-period log-convexity range

# q₀, both pins, 50-digit strings with provenance (muon from the canonical
# witness; proton from qou_substrate.constants Q_50_DIGIT_STR).
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28; _solve_q_proton_f64 + mpmath refine):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_s, _q, _a = sp.symbols("s q a", positive=True)
_k = sp.symbols("k", positive=True, integer=True)
_eps, _h = sp.symbols("eps h")


def qint(qv, kk: int):
    """One-sided quantum integer [k]_q = 1 + q + … + q^{k−1} — the corpus
    convention (QOU.Mass.QDifferenceConfluentObstruction.qint)."""
    return sum(qv ** i for i in range(kk))


def qfact(qv, m: int):
    """[m]_q! = ∏_{j=1}^{m} [j]_q (qfact); N_q(n) = qfact(q, n−1)."""
    r = sp.Integer(1)
    for j in range(1, m + 1):
        r *= qint(qv, j)
    return r


def involution_numbers(n_max: int) -> list[int]:
    """I(0..n_max) via I(m) = I(m−1) + (m−1)·I(m−2) — exact integers
    (Lean: BindingGevreyHalf.involutionNumber)."""
    I = [1, 1]
    for m in range(2, n_max + 1):
        I.append(I[-1] + (m - 1) * I[-2])
    return I


# ---------------------------------------------------------------- Attack A

def block_a1_moment_identity(wb: WitnessBuilder) -> None:
    """A1: ∫₀^∞ sⁿ e^{−s} ds/s = Γ(n) = (n−1)!, n = 1..N_MOMENTS, exact."""
    _ok: list[bool] = []
    for n in range(1, N_MOMENTS + 1):
        val = sp.integrate(_s ** n * sp.exp(-_s) / _s, (_s, 0, sp.oo))
        _ok.append(bool(val == sp.factorial(n - 1)))
        assert _ok[-1], (n, val)
    wb.add_assertion(
        "moment_identity_gamma", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source=f"∫₀^∞ sⁿ e^(−s) ds/s − (n−1)! = 0 exactly (sympy), "
               f"n = 1..{N_MOMENTS}: the keystone-forced normalizer "
               f"N(n) = (n−1)! (KeystoneBridgeC1Binding, proved "
               f"n·N(n) = n!) IS the n-th moment of the unit (c = 1) "
               f"Schwinger kernel e^(−s)·ds/s")


def block_a2_n0_divergence(wb: WitnessBuilder) -> None:
    """A2: the kernel e^{−s}·ds/s has infinite mass at s = 0 — determinacy
    must be stated for the shifted finite measure e^{−s}·ds."""
    _ok: list[bool] = []
    v0 = sp.integrate(sp.exp(-_s) / _s, (_s, 0, sp.oo))
    _ok.append(bool(v0 == sp.oo))
    assert _ok[-1], v0
    # shifted moments: m_k = ∫ s^k e^{−s} ds = k! (finite measure, m_0 = 1)
    for kk in range(0, N_MOMENTS):
        mk = sp.integrate(_s ** kk * sp.exp(-_s), (_s, 0, sp.oo))
        _ok.append(bool(mk == sp.factorial(kk)))
        assert _ok[-1], (kk, mk)
    wb.add_assertion(
        "n0_divergence_and_shift", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="∫₀^∞ e^(−s) ds/s = ∞ (the ds/s kernel is an infinite "
               "measure at s = 0); the determinacy statement lives on the "
               "index-shifted FINITE measure e^(−s)·ds with Stieltjes "
               "moments m_k = k! = N(k+1) (verified exactly k = 0..7)")


def block_a3_carleman(wb: WitnessBuilder) -> None:
    """A3: Carleman's condition for {k!} — exact Stirling limit + exact
    harmonic comparison. Verdict: DETERMINATE."""
    _ok: list[bool] = []
    # Stirling asymptotics of the Carleman term, exact sympy limit:
    L = sp.limit(sp.factorial(_k) ** (sp.Rational(1, 2) / _k) / sp.sqrt(_k),
                 _k, sp.oo)
    _ok.append(bool(L == sp.exp(sp.Rational(-1, 2))))
    assert _ok[-1], L
    # exact comparison inequality: k! ≤ k^(2k) ⇒ (k!)^(−1/(2k)) ≥ 1/k
    for kk in range(1, 201):
        _ok.append(bool(sp.factorial(kk) <= sp.Integer(kk) ** (2 * kk)))
        assert _ok[-1], kk
    # partial sums of the harmonic minorant exceed ln N (divergence marker)
    H = sum(Fraction(1, kk) for kk in range(1, 201))
    _ok.append(bool(H > sp.log(200)))
    assert _ok[-1], H
    wb.add_assertion(
        "carleman_determinate", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="Carleman for the Stieltjes problem of {k!}: exact Stirling "
               "limit lim (k!)^(1/(2k))/√k = e^(−1/2) (sympy), so terms "
               "(k!)^(−1/(2k)) ~ √(e/k); exact minorant k! ≤ k^(2k) "
               "(verified k = 1..200) gives (k!)^(−1/(2k)) ≥ 1/k and "
               "Σ 1/k = ∞ ⇒ Σ (k!)^(−1/(2k)) = ∞: Carleman holds, the "
               "moment problem is DETERMINATE — e^(−s)·ds is the UNIQUE "
               "positive measure on (0,∞) with moments {k!}")


def block_a4_hankel(wb: WitnessBuilder) -> None:
    """A4: Hankel positive-definiteness of {k!} (Stieltjes consistency)."""
    _ok: list[bool] = []
    for n in range(1, N_HANKEL + 1):
        H0 = sp.Matrix(n, n, lambda i, j: sp.factorial(i + j))
        H1 = sp.Matrix(n, n, lambda i, j: sp.factorial(i + j + 1))
        _ok.append(bool(H0.det() > 0))
        assert _ok[-1], n
        _ok.append(bool(H1.det() > 0))
        assert _ok[-1], n
    wb.add_assertion(
        "hankel_positive", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source=f"det[(i+j)!] > 0 and det[(i+j+1)!] > 0 for sizes "
               f"1..{N_HANKEL} (exact integers): {{k!}} satisfies the "
               f"Stieltjes positive-definiteness consistent with the "
               f"unique representing measure e^(−s)·ds")


def block_a5_unit_forcing(wb: WitnessBuilder) -> None:
    """A5: kernel c·e^{−s}·ds/s has moments c·(n−1)!; the proved bridge
    identity n·N(n) = n! forces c = 1; c = ½ fails for every n."""
    _ok: list[bool] = []
    c = sp.symbols("c", positive=True)
    for n in range(1, N_MOMENTS + 1):
        # n·(c·(n−1)!) = n!  ⟺  c = 1
        sol = sp.solve(sp.Eq(n * (c * sp.factorial(n - 1)),
                             sp.factorial(n)), c)
        _ok.append(bool(sol == [1]))
        assert _ok[-1], (n, sol)
        _ok.append(bool(n * (sp.Rational(1, 2) * sp.factorial(n - 1)) != sp.factorial(n)))
        assert _ok[-1], n
    wb.add_assertion(
        "unit_forced_c_eq_1", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="with kernel c·e^(−s)·ds/s the moments are c·(n−1)!; the "
               "PROVED KeystoneBridgeC1Binding identity n·N(n) = n! forces "
               "c = 1 exactly (unique sympy solution, n = 1..8); c = 1/2 "
               "fails for every n — conditional on the identification, the "
               "Schwinger unit is pinned (r2core §5 distinguisher, "
               "re-verified)")


def block_a6_positivity_status(wb: WitnessBuilder) -> None:
    """A6: binding-side positivity status — what is proved vs open."""
    _ok: list[bool] = []
    I = involution_numbers(N_LOGCONVEX + 1)
    _ok.append(bool(all((x > 0 for x in I))))
    assert _ok[-1]
    b = [Fraction(I[m], sp.factorial(m)) for m in range(len(I))]
    # (ii) the C1 carrier is NOT log-convex: b_2² > b_1·b_3
    _ok.append(bool(b[2] ** 2 > b[1] * b[3]))
    assert _ok[-1], (b[2] ** 2, b[1] * b[3])
    carrier_violations = [m for m in range(1, 20)
                          if b[m] ** 2 > b[m - 1] * b[m + 1]]
    _ok.append(bool(2 in carrier_violations))
    assert _ok[-1]
    # (iii) the RAW periods B_n = I(n)/n pass log-convexity 2..39
    B = [None] + [Fraction(I[m], m) for m in range(1, len(I))]
    raw_violations = [m for m in range(2, N_LOGCONVEX)
                      if B[m] ** 2 > B[m - 1] * B[m + 1]]
    _ok.append(bool(raw_violations == []))
    assert _ok[-1], raw_violations
    wb.add_assertion(
        "binding_positivity_status", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="binding-side status: (i) I(n) > 0 exact to n = 41 "
               "(Lean-proved involutionNumber_pos); (ii) the normalized C1 "
               "carrier b_n = I(n)/n! is NOT log-convex (b_2² = 1 > "
               "b_1·b_3 = 2/3; violations at m = 2..6,…) — {b_n} is NOT "
               "itself a Stieltjes moment sequence, so the reduction's "
               "positive-measure hypothesis concerns the RESUMMATION "
               "KERNEL, not the carrier coefficients; (iii) the raw "
               "periods B_n = I(n)/n ARE log-convex for 2 ≤ n ≤ 39 — the "
               "necessary Stieltjes condition PASSES for the raw series "
               "(status datum, NOT a representability proof)")
    wb.add_data("binding_positivity", {
        "carrier_logconvex_violations_m_lt_20": carrier_violations,
        "raw_period_logconvex_violations_2_39": raw_violations,
        "note": "corpus grep found NO prior Stieltjes/positive-measure "
                "representability statement for the binding OGF — "
                "positivity+representability are genuinely open; the "
                "Frobenius-positivity SDP constraints (confinement-sdp) "
                "constrain Wedderburn-block pairings ⟨π_λ, Φ⟩ ≥ 0, a "
                "different object from the Borel kernel; no transfer "
                "established",
    })


# ---------------------------------------------------------------- Attack E

def block_e1_bar_falsifier(wb: WitnessBuilder) -> None:
    """E1: bar-transform of the one-sided q-Borel normalizer — exact
    covariance weight q^{−(n−1)(n−2)/2} ≠ 1 for n ≥ 3."""
    _ok: list[bool] = []
    for kk in range(1, N_MOMENTS + 1):
        d = sp.simplify(qint(1 / _q, kk) - _q ** (1 - kk) * qint(_q, kk))
        _ok.append(bool(d == 0))
        assert _ok[-1], kk
    nontrivial = 0
    for n in range(1, N_MOMENTS + 1):
        m = n - 1
        w = sp.simplify(qfact(1 / _q, m) / qfact(_q, m))
        target = _q ** (-sp.Rational(m * (m - 1), 2))
        _ok.append(bool(sp.simplify(w - target) == 0))
        assert _ok[-1], (n, w)
        if m * (m - 1) != 0:
            nontrivial += 1
    _ok.append(bool(nontrivial == N_MOMENTS - 2))
    assert _ok[-1]
    wb.add_assertion(
        "bar_covariance_weight", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="[k]_{q⁻¹} = q^(1−k)·[k]_q exactly (k = 1..8) ⇒ "
               "N_{q⁻¹}(n) = q^(−(n−1)(n−2)/2)·N_q(n) exactly (n = 1..8; "
               "weight nontrivial for every n ≥ 3): the one-sided q-Borel "
               "normalizer is bar-COVARIANT while loop proper time (s real) "
               "is bar-INVARIANT — FALSIFIER FIRES for the identification "
               "with the unbalanced kernel at q ≠ 1 (scope-(a): the stated "
               "unbalanced form only; trivial at q = 1)")


def block_e2_balanced_repair(wb: WitnessBuilder) -> None:
    """E2: the balanced normalizer is exactly bar-invariant — the
    constructive bar-projection caveat."""
    _ok: list[bool] = []
    for n in range(1, N_MOMENTS + 1):
        m = n - 1
        Nb = _q ** (-sp.Rational(m * (m - 1), 4)) * qfact(_q, m)
        d = sp.simplify(Nb.subs(_q, 1 / _q) - Nb)
        _ok.append(bool(d == 0))
        assert _ok[-1], n
    wb.add_assertion(
        "balanced_bar_invariant", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="N_q^bal(n) = q^(−(n−1)(n−2)/4)·[n−1]_q! satisfies "
               "N^bal_{q⁻¹} = N^bal_q exactly (n = 1..8) — the balanced "
               "(BalancedQuantumTwist) convention restores bar-invariance; "
               "the identification survives iff the conjecture's kernel is "
               "read balanced (the exact bar-projection caveat)")


def block_e3_subleading(wb: WitnessBuilder) -> None:
    """E3: exact first-order q-corrections — quadratic (unbalanced) vs 0
    (balanced) vs linear (loop a₁) — and the balanced h² coefficient."""
    _ok: list[bool] = []
    for n in range(3, N_MOMENTS):
        m = n - 1
        # unbalanced: coefficient of (q−1) is (n−1)(n−2)/4
        ser = sp.series((qfact(_q, m) / sp.factorial(m)).subs(_q, 1 + _eps),
                        _eps, 0, 2).removeO()
        c1 = sp.expand(ser).coeff(_eps, 1)
        _ok.append(bool(c1 == sp.Rational(m * (m - 1), 4)))
        assert _ok[-1], (n, c1)
        # balanced: first order vanishes; h² coefficient of log is
        # Σ_{k=1}^{n−1}(k²−1)/24
        Nb = _q ** (-sp.Rational(m * (m - 1), 4)) * qfact(_q, m)
        bser = sp.series((Nb / sp.factorial(m)).subs(_q, 1 + _eps),
                         _eps, 0, 2).removeO()
        _ok.append(bool(sp.expand(bser).coeff(_eps, 1) == 0))
        assert _ok[-1], n
        lg = sp.series(sp.log((Nb / sp.factorial(m)).subs(_q, sp.exp(_h))),
                       _h, 0, 3).removeO()
        c2 = sp.expand(lg).coeff(_h, 2)
        pred = sp.Rational(sum(kk * kk - 1 for kk in range(1, m + 1)), 24)
        _ok.append(bool(sp.simplify(c2 - pred) == 0))
        assert _ok[-1], (n, c2, pred)
    # loop side: an a₁ heat-kernel correction is LINEAR in n per moment
    for n in range(1, N_MOMENTS - 1):
        val = sp.integrate(_s ** n * sp.exp(-_s) * (1 + _a * _s) / _s,
                           (_s, 0, sp.oo))
        _ok.append(bool(sp.simplify(val - sp.factorial(n - 1) * (1 + _a * n)) == 0))
        assert _ok[-1], n
    wb.add_assertion(
        "subleading_pattern_mismatch", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="exact per-moment corrections: unbalanced q-Borel "
               "1 + (q−1)(n−1)(n−2)/4 + O² (QUADRATIC in n); balanced "
               "1 + 0·(q−1) + O², with h²-coefficient Σ(k²−1)/24 at "
               "q = e^h; loop heat-kernel a₁-correction (n−1)!(1 + a₁n/A) "
               "(LINEAR in n). Unbalanced matches neither loop "
               "q-independence (0) nor curvature (linear) — E1's FAIL "
               "reproduced at moment level with exact discrepancy; "
               "balanced first-order 0 matches loop q-independence — PASS "
               "(unproved); the balanced q²-order Σ(k²−1)/24 is the "
               "next-order falsifier target")


def block_e4_pin_numerics(wb: WitnessBuilder) -> None:
    """E4: sizes at the two q₀ pins, 50 dps — recorded, not scored."""
    out = {}
    for name, q0s in (("muon", Q0_MUON_STR), ("proton", Q0_PROTON_STR)):
        q0 = mpf(q0s)
        n = 6
        m = n - 1
        # unbalanced first-order defect estimate and exact weight at q₀
        defect1 = (q0 - 1) * m * (m - 1) / 4
        w_bar = q0 ** (-mpf(m * (m - 1)) / 2)
        ratio_unbal = mpf(1)
        for j in range(1, m + 1):
            ratio_unbal *= sum(q0 ** i for i in range(j))
        ratio_unbal /= mpf(int(sp.factorial(m)))
        ratio_bal = ratio_unbal * q0 ** (-mpf(m * (m - 1)) / 4)
        out[name] = {
            "n": n,
            "first_order_defect_estimate": mp.nstr(defect1, 20),
            "bar_weight_q0^{-(n-1)(n-2)/2}": mp.nstr(w_bar, 20),
            "Nq_over_factorial_unbalanced": mp.nstr(ratio_unbal, 30),
            "Nq_over_factorial_balanced": mp.nstr(ratio_bal, 30),
        }
    # pin shift of the balanced ratio (recorded; expected ~1e-8 relative)
    rb_mu = mpf(out["muon"]["Nq_over_factorial_balanced"])
    rb_pr = mpf(out["proton"]["Nq_over_factorial_balanced"])
    out["balanced_ratio_pin_shift_rel"] = mp.nstr(
        abs(rb_mu - rb_pr) / rb_pr, 8)
    out["note"] = ("O(1) unbalanced defect at q₀ (≈0.55 at n = 6): the "
                   "E1/E3 discrepancy is NOT a small correction at the "
                   "substrate value — the unbalanced identification fails "
                   "grossly away from q = 1; recorded, not scored (the "
                   "falsifier verdicts are the exact symbolic E1/E3)")
    wb.add_data("pin_numerics", out)


def main() -> int:
    set_compute_dps(50)
    wb = WitnessBuilder("borel-propertime-moment-attack",
                        engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "Attacks A + E on the conjecture 'binding Borel variable = loop "
        "proper time' (beans qou-7gu9 + qou-zfl0, epic qou-q04o; "
        "audit-only, scope-(a), NO FIT, nothing wired). ATTACK A "
        "(moment-determinacy reduction): the keystone-forced normalizer "
        "N(n) = (n−1)! is exactly the n-th ds/s-moment of the unit "
        "Schwinger kernel e^(−s)·ds/s (A1); the kernel is an infinite "
        "measure at s = 0, so determinacy lives on the shifted finite "
        "measure e^(−s)·ds with moments {k!} (A2); Carleman's condition "
        "holds exactly for {k!} (Stirling limit e^(−1/2); minorant "
        "k! ≤ k^(2k) ⇒ terms ≥ 1/k; harmonic divergence) so the Stieltjes "
        "problem is DETERMINATE (A3), Hankel-consistent (A4); with kernel "
        "c·e^(−s)·ds/s the proved n·N(n) = n! forces c = 1 (A5). "
        "REDUCTION: the conjecture reduces to two named open hypotheses — "
        "positivity + (n−1)!-representability of the binding resummation "
        "kernel; determinacy then forces the kernel to BE e^(−s)·ds. "
        "Binding-side status (A6): coefficient positivity Lean-proved; "
        "the C1 carrier is NOT a moment sequence (log-convexity fails at "
        "m = 2); the raw periods I(n)/n pass log-convexity to n = 39 "
        "(necessary condition only); kernel positivity/representability "
        "OPEN. ATTACK E (falsifier): the one-sided q-Borel normalizer is "
        "bar-COVARIANT with exact weight q^(−(n−1)(n−2)/2) while loop "
        "proper time is bar-invariant — the unbalanced identification "
        "FAILS at q ≠ 1 (E1), reproduced at moment level by the exact "
        "first-order pattern mismatch quadratic-vs-{0, linear} (E3); the "
        "balanced normalizer q^(−(n−1)(n−2)/4)·[n−1]_q! is exactly "
        "bar-invariant with vanishing first-order correction — the "
        "identification SURVIVES with the balanced-kernel (bar-projection) "
        "caveat (E2), next falsifier at q²-order Σ(k²−1)/24. Pin numerics "
        "recorded at both q₀ pins (E4).")
    wb.set_audit_only(
        "docs/audits/2026-07-25-borel-propertime-attack-a-e.md")

    block_a1_moment_identity(wb)
    print("A1: N(n) = (n−1)! = unit-Schwinger ds/s-moment, exact n=1..8.")
    block_a2_n0_divergence(wb)
    print("A2: ds/s kernel infinite at s=0; shifted finite moments k!.")
    block_a3_carleman(wb)
    print("A3: Carleman holds exactly — {k!} Stieltjes-DETERMINATE.")
    block_a4_hankel(wb)
    print("A4: Hankel determinants positive (sizes 1..6, exact).")
    block_a5_unit_forcing(wb)
    print("A5: c = 1 forced by proved n·N(n) = n!; c = ½ fails.")
    block_a6_positivity_status(wb)
    print("A6: carrier NOT a moment sequence; raw periods log-convex to "
          "n = 39; kernel positivity OPEN.")
    block_e1_bar_falsifier(wb)
    print("E1: bar weight q^(−(n−1)(n−2)/2) exact — unbalanced "
          "identification FAILS at q ≠ 1.")
    block_e2_balanced_repair(wb)
    print("E2: balanced normalizer exactly bar-invariant — repair exists.")
    block_e3_subleading(wb)
    print("E3: first-order patterns quadratic/0/linear — mismatch exact; "
          "balanced passes.")
    block_e4_pin_numerics(wb)
    print("E4: pin numerics recorded (both pins, 50 dps).")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
