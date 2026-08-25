#!/usr/bin/env python3
"""rep_jackson_identification_probe.py — Attack 1 on (REP), the last
substantive hypothesis of conj:schwinger-measure-computational-time:
"the corpus's ACTUAL binding resummation is integration against a positive
kernel whose ds/s-moments are the balanced normalizer."

Bean qou-u5p0. AUDIT-ONLY — scope-(a), NO FIT, nothing wired; the target
conjecture stays a conjecture.

DETERMINATION (the key deliverable, established by corpus survey — see the
audit doc): the corpus performs NO integral resummation of the binding
OGF anywhere. The production binding numbers come from the finite algebraic
Markov-trace evaluation (computations/mass_binding_dashboard.py header:
"every binding form is evaluated from the ONE canonical Jones–Markov
transfer trace tr_m_atom_zn … α = E₀"); the binding OGF / C1 carrier
appears only FORMALLY — the keystone normalizer strip b_n = B_n/N(n)
(KeystoneBridgeC1Binding.lean), the coefficient-level (diagonal-weight)
formal q-Borel of the Route-D audit, and growth/singularity DIAGNOSTICS
(lever1_*). Hence (REP) is a claim about a canonical CHOICE of integral
representation for an operation the corpus performs formally — not a
matching to an existing corpus integral.

WHAT THIS PROBE THEREFORE CHECKS (all exact or 60-dps/1e-30):

  R1  The corpus's actual formal operation, exact (sympy integers):
      involution numbers I(n) (I(n+2) = I(n+1) + (n+1)·I(n)); periods
      B_n = I(n)/n; C1 carrier b_n = I(n)/n!; the keystone strip
      b_n = B_n/N(n) with N(n) = (n−1)! forced by n·N(n) = n!; and the
      proved depth-2 recurrence (n+2)·b_{n+2} = b_{n+1} + b_n. This IS
      the corpus operation (REP) must represent — a diagonal normalizer
      strip on coefficients, not an integral.
  R2  ATTACK-5 FALSIFIER, archimedean leg (sympy exact): the strip is
      EXACTLY integration against the unit Schwinger kernel, order by
      order: ∫₀^∞ s^n e^{−s} ds/s = (n−1)! for n = 1..8, and the
      finite-order polynomial identity
        ∫₀^∞ [Σ_{n≤N} b_n (x s)^n] e^{−s} ds/s = Σ_{n≤N} B_n x^n
      as an exact polynomial identity in x (N = 8). Any mismatch would
      kill the option; MATCH is required.
  R3  ATTACK-5 FALSIFIER, fibre leg (mpmath 60 dps, tol 1e−30, at
      q ∈ {1.2, q₀ muon pin, q₀ proton pin}): the Attack-B atomic kernel
      K^at = Jackson q-Gamma ⊛ theta (RSZ ingredients: Def 2.3.3 weight,
      eq (1.2) theta, §1.2.1 Jackson-style discrete contour) satisfies
      ∫ s^n K^at(ds)/s = N^bal(n) = q^{−(n−1)(n−2)/4}[n−1]_q!, n = 1..9,
      and the finite-order rewriting of the q-lift carrier
      (S_q(n+2) = S_q(n+1) + [n+1]_q S_q(n), b^q_n = S_q(n)/[n]_q!)
      through the kernel reproduces Σ b^q_n N^bal(n) x^n coefficient-wise
      AND at a spot value x = 0.37. Exact discrepancy vs the corpus's
      one-sided proved strip [n−1]_q! recorded: the bar-covariant weight
      q^{−(n−1)(n−2)/4} (Attack E), exact per n.
  R4  CANONICAL-CHOICE NON-UNIQUENESS (the new content; at q = 1.2):
      the u-translate family of the theta factor — atoms u·q̃^j (j ∈ ℤ,
      q̃ = √q), masses ∝ q̃^{−j(j+1)/2}u^{−j} — has u-INDEPENDENT moments
      q^{k(k−1)/4} (exact reindex identity, sympy; verified 1e−30 at
      u = 1 and u = 1.3), yet distinct support for generic u. The natural
      bar-reflection σ: s ↦ q̃^{−1}/s (the unique reflection fixing BOTH
      Attack-B B-factor realizations — theta u=1 via j ↦ −1−j, and the
      log-normal via Gaussian symmetry about μ̂ = −(ln q̃)/2, sympy exact)
      maps μ_u ↦ μ_{1/u}; the symmetrization ½(μ_u + μ_{1/u}) is
      positive, σ-INVARIANT, atomic, has the same moments for EVERY u,
      and (Jackson ⊛ ·) then yields a u-CONTINUUM of positive kernels
      with exactly the balanced moments N^bal(k+1). CONSEQUENCE:
      positivity + balanced moments + bar-reflection-invariance +
      atomicity do NOT pin the kernel at q ≠ 1 — the fibre
      indeterminacy of Attack B §3.1 sharpened from "two realizations"
      to "a continuum, even inside the symmetric atomic class". At
      q = 1 the class is a singleton (Carleman determinacy of {k!},
      Attack A — cited, not re-derived).

VERDICT SHAPE (scope-(a)): the falsifier PASSES — the corpus's formal
strip IS order-by-order integration against the Jackson/theta kernel in
the balanced convention (and against e^{−s} ds at q = 1); but because the
corpus never performs the integral, (REP) is a canonical-choice premise,
and R4 shows the choice is NOT pinned by the named structural properties
at q ≠ 1. RSZ themselves state kernel non-canonicity (§1.2.1) and give
no general explicit integral formula for their preferred ch. 5 summation
("except for some particular cases") — there is no "RSZ classification"
in which the theta kernel is the unique bar-invariant choice. Pinning
the kernel requires a derivation input beyond moments + symmetry.
Nothing here proves or refutes the conjecture.

Exit 0 iff all assertions pass. Witness:
rep-jackson-identification.witness.json (audit-only).
Audit doc: docs/audits/2026-08-01-rep-jackson-identification.md.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _bridge

import json  # noqa: E402

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, sqrt as mpsqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0        # sympy exact / integer comparisons
TOL_50 = 1e-30       # 60-dps kernel-identity cross-checks
N_ORD = 8            # finite-order falsifier truncation (n = 1..N_ORD)
N_MOM = 9            # fibre ds/s-moments n = 1..N_MOM
U_GENERIC = "1.3"    # generic translate parameter (R4)
X_SPOT = "0.37"      # spot evaluation point for the polynomial falsifier

# q₀, both pins, 50-digit strings with provenance (muon from the canonical
# witness; proton from qou_substrate.constants Q_50_DIGIT_STR).
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28; _solve_q_proton_f64 + mpmath refine):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_q, _s, _x, _u = sp.symbols("q s x u", positive=True)
_ii, _jj, _kk = sp.symbols("i j k", integer=True)


# ------------------------------------------------------------ exact helpers

def involution_numbers(n_max: int) -> list[sp.Integer]:
    """I(0..n_max): I(0) = I(1) = 1, I(n+2) = I(n+1) + (n+1)·I(n) —
    the corpus binding-period numerators (sw-classical-jet-exactness;
    QOU.Mass.BindingGevreyHalf.involutionNumber)."""
    I = [sp.Integer(1), sp.Integer(1)]
    for n in range(n_max - 1):
        I.append(I[-1] + (n + 1) * I[-2])
    return I


def qint(qv, kk: int):
    """One-sided quantum integer [k]_q (corpus convention,
    QOU.Mass.QDifferenceConfluentObstruction.qint)."""
    return sum(qv ** i for i in range(kk))


def qfact(qv, m: int):
    """[m]_q! = ∏ [j]_q; the corpus one-sided normalizer N_q(n) =
    qfact(q, n−1) (KeystoneBridgeC1Binding q-lift leg)."""
    r = qv ** 0
    for j in range(1, m + 1):
        r = r * qint(qv, j)
    return r


def mp_qint(q0: mpf, kk: int) -> mpf:
    return sum(q0 ** i for i in range(kk))


def mp_qfact(q0: mpf, m: int) -> mpf:
    r = mpf(1)
    for j in range(1, m + 1):
        r *= mp_qint(q0, j)
    return r


def mp_balanced_normalizer(q0: mpf, n: int) -> mpf:
    """N^bal_q(n) = q^{−(n−1)(n−2)/4}·[n−1]_q! (Attack E balanced
    convention)."""
    m = n - 1
    return q0 ** (-mpf(m * (m - 1)) / 4) * mp_qfact(q0, m)


# ------------------------------------------------- fibre kernels (Attack B)

def jackson_factor(q0: mpf, k_max: int, tail_dps: int = 42):
    """Jackson q-Gamma kernel at p = 1/q0 (Attack-B C4a): atoms
    t_m = p^m/(1−p), masses c_m = p^m·(p^{m+1};p)_∞ > 0; moments
    Σ c_m t_m^k = [k]_p!."""
    p = 1 / q0
    M = int(tail_dps / -mp.log10(p)) + 60
    pp = [mpf(1)]
    for j in range(1, M + 1):
        pp.append(pp[-1] * (1 - p ** j))
    pp_inf = pp[-1]
    a = 1 / (1 - p)
    atoms = [a * p ** m for m in range(M)]
    masses = [p ** m * pp_inf / pp[m] for m in range(M)]
    moments = [sum(c * t ** k for c, t in zip(masses, atoms))
               for k in range(k_max + 1)]
    return atoms, masses, moments


def theta_translate_factor(q0: mpf, uu: mpf, k_max: int,
                           tail_dps: int = 42):
    """u-translated half-weight theta kernel at q̃ = √q0: atoms u·q̃^j
    (j ∈ ℤ), masses ∝ q̃^{−j(j+1)/2}·u^{−j} (normalized). At u = 1 this
    is the Attack-B C4b theta kernel. Returns (js, atoms, masses,
    moments[0..k_max]); the R4a reindex identity makes the moments
    u-INDEPENDENT: exactly q0^{k(k−1)/4}."""
    qt = mpsqrt(q0)
    J = 10
    while float((J * (J + 1) / 2 - J * (k_max + 4)) * mp.log10(qt)) \
            < tail_dps + 10:
        J += 10
    js = list(range(-J, J + 1))
    w = [qt ** (-mpf(j * (j + 1)) / 2) * uu ** (-j) for j in js]
    Z = sum(w)
    atoms = [uu * qt ** j for j in js]
    masses = [ww / Z for ww in w]
    moments = [sum(c * t ** k for c, t in zip(masses, atoms))
               for k in range(k_max + 1)]
    return js, atoms, masses, moments


def measure_eq(atoms_a, masses_a, atoms_b, masses_b, tol,
               mass_floor=mpf("1e-38")) -> bool:
    """Compare two atomic measures given as (atoms, masses) lists —
    filter truncation dust below mass_floor, sort by atom location,
    then require the atom SETS to coincide (rel 1e−20) with masses
    agreeing within tol (relative)."""
    fa = sorted((a, m) for a, m in zip(atoms_a, masses_a) if m > mass_floor)
    fb = sorted((a, m) for a, m in zip(atoms_b, masses_b) if m > mass_floor)
    if len(fa) != len(fb):
        return False
    worst = mpf(0)
    for (aa, ma), (ab, mb) in zip(fa, fb):
        if abs(aa / ab - 1) > mpf("1e-20"):
            return False                      # atom sets differ
        worst = max(worst, abs(ma / mb - 1))
    return worst < tol


# ---------------------------------------------------------------- Block R1

def block_r1_corpus_operation(wb: WitnessBuilder) -> list[sp.Rational]:
    """R1: the corpus's actual formal operation — the keystone
    normalizer strip + the proved depth-2 recurrence, exact."""
    NN = 14
    I = involution_numbers(NN + 2)
    B = [None] + [sp.Rational(I[n], n) for n in range(1, NN + 1)]
    b = [None] + [sp.Rational(I[n], sp.factorial(n)) for n in range(1, NN + 1)]
    for n in range(1, NN + 1):
        Nn = sp.factorial(n - 1)
        assert n * Nn == sp.factorial(n), n           # n·N(n) = n!
        assert B[n] / Nn == b[n], n                   # the strip
    for n in range(1, NN - 1):
        # proved depth-2 kernel (KeystoneBridgeC1Binding, classical leg)
        assert (n + 2) * b[n + 2] == b[n + 1] + b[n], n
    wb.add_assertion(
        "corpus_formal_strip_exact", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source="n = 1..14, exact integers/rationals: the corpus binding "
               "operation is the FORMAL keystone strip b_n = B_n/N(n) with "
               "B_n = I(n)/n (involution periods, sw-classical-jet-"
               "exactness), N(n) = (n−1)! forced by n·N(n) = n! "
               "(KeystoneBridgeC1Binding.period_carrier_strip), landing on "
               "the C1 carrier b_n = I(n)/n! that satisfies the proved "
               "depth-2 kernel (n+2)·b_{n+2} = b_{n+1} + b_n — a diagonal "
               "coefficient operation; the corpus survey (audit §1) finds "
               "NO integral resummation of this series anywhere "
               "(production binding = finite Markov-trace evaluation, "
               "mass_binding_dashboard.py)")
    return b


# ---------------------------------------------------------------- Block R2

def block_r2_archimedean_falsifier(wb: WitnessBuilder,
                                   b: list[sp.Rational]) -> None:
    """R2: Attack-5 falsifier, archimedean leg — the strip IS
    integration against e^{−s} ds/s, exactly, order by order."""
    # per-order moments
    for n in range(1, N_ORD + 1):
        val = sp.integrate(_s ** n * sp.exp(-_s) / _s, (_s, 0, sp.oo))
        assert sp.simplify(val - sp.factorial(n - 1)) == 0, n
    # finite-order polynomial identity in x
    poly = sum(b[n] * (_x * _s) ** n for n in range(1, N_ORD + 1))
    lhs = sp.integrate(sp.expand(poly * sp.exp(-_s) / _s), (_s, 0, sp.oo))
    I = involution_numbers(N_ORD)
    rhs = sum(sp.Rational(I[n], n) * _x ** n for n in range(1, N_ORD + 1))
    assert sp.expand(lhs - rhs) == 0, sp.expand(lhs - rhs)
    wb.add_assertion(
        "archimedean_falsifier_match", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source=f"sympy exact, n = 1..{N_ORD}: ∫₀^∞ s^n e^(−s) ds/s = (n−1)! "
               f"per order, and the finite-order polynomial identity "
               f"∫₀^∞ [Σ b_n (xs)^n] e^(−s) ds/s = Σ B_n x^n holds exactly "
               f"in x — the corpus's normalizer strip IS order-by-order "
               f"integration against the unit Schwinger kernel at q = 1. "
               f"FALSIFIER PASSES (a mismatch would have killed the "
               f"identification)")


# ---------------------------------------------------------------- Block R3

def block_r3_fibre_falsifier(wb: WitnessBuilder, q_name: str,
                             q_str: str) -> None:
    """R3: Attack-5 falsifier, fibre leg at one q value — the balanced
    normalizer values ARE the Jackson⊛theta ds/s-moments, and the q-lift
    carrier's finite-order resummation through the kernel matches."""
    q0 = mpf(q_str)
    _, _, mom_j = jackson_factor(q0, N_MOM)
    _, _, _, mom_t = theta_translate_factor(q0, mpf(1), N_MOM)
    # ds/s-moment identity: ∫ s^n K^at(ds)/s = ∫ s^{n−1} K^at(ds)
    #                     = [n−1]_{q⁻¹}!·q^{(n−1)(n−2)/4} = N^bal(n)
    worst = mpf(0)
    one_sided_gap = {}
    for n in range(1, N_MOM + 1):
        k = n - 1
        kernel_mom = mom_j[k] * mom_t[k]          # Mellin convolution
        nbal = mp_balanced_normalizer(q0, n)
        worst = max(worst, abs(kernel_mom / nbal - 1))
        # exact discrepancy vs the corpus's PROVED one-sided strip:
        ratio = nbal / mp_qfact(q0, k)            # = q^{−k(k−1)/4}
        tgt = q0 ** (-mpf(k * (k - 1)) / 4)
        worst = max(worst, abs(ratio / tgt - 1))
        one_sided_gap[n] = mp.nstr(ratio, 12)
    assert worst < TOL_50, worst
    # finite-order rewriting of the q-lift carrier through the kernel
    S = [mpf(1), mpf(1)]
    for n in range(N_ORD + 1):
        S.append(S[-1] + mp_qint(q0, n + 1) * S[-2])
    bq = [None] + [S[n] / mp_qfact(q0, n) for n in range(1, N_ORD + 1)]
    xx = mpf(X_SPOT)
    lhs = sum(bq[n] * xx ** n * (mom_j[n - 1] * mom_t[n - 1])
              for n in range(1, N_ORD + 1))
    rhs = sum(bq[n] * xx ** n * mp_balanced_normalizer(q0, n)
              for n in range(1, N_ORD + 1))
    worst2 = abs(lhs / rhs - 1)
    assert worst2 < TOL_50, worst2
    wb.add_assertion(
        f"fibre_falsifier_match_{q_name}",
        computed=mp.nstr(max(worst, worst2), 5), expected="0",
        tolerance=TOL_50,
        source=f"q = {q_name} ({mp.nstr(q0, 12)}…), 60 dps: the Jackson "
               f"q-Gamma ⊛ theta atomic kernel (RSZ Def 2.3.3 weight + "
               f"eq (1.2) theta + §1.2.1 Jackson-style discrete contour) "
               f"has ds/s-moments ∫ s^n K(ds)/s exactly N^bal(n) = "
               f"q^(−(n−1)(n−2)/4)·[n−1]_q! for n = 1..{N_MOM} "
               f"(rel < 1e−30), the exact per-n gap to the corpus's proved "
               f"one-sided strip [n−1]_q! being the bar-covariant weight "
               f"q^(−(n−1)(n−2)/4) (Attack E); the finite-order "
               f"resummation of the q-lift C1 carrier b^q_n = S_q(n)/[n]_q! "
               f"through the kernel matches Σ b^q_n·N^bal(n)·x^n at "
               f"x = {X_SPOT} (rel < 1e−30). FALSIFIER PASSES in the "
               f"balanced convention")
    if q_name == "test":
        wb.add_data("one_sided_vs_balanced_gap", one_sided_gap)


# ---------------------------------------------------------------- Block R4

def block_r4_nonuniqueness(wb: WitnessBuilder) -> None:
    """R4: canonical-choice non-uniqueness at the fibre — the
    u-translate/reflection/symmetrization construction (q = 1.2)."""
    # R4a — exact reindex identity behind u-independence (sympy):
    # with j = i + k:  jk − j(j+1)/2 = k(k−1)/2 − i(i+1)/2, so
    # Σ_j q̃^{jk−j(j+1)/2} u^{−j} = q̃^{k(k−1)/2}·u^{−k}·Σ_i q̃^{−i(i+1)/2}u^{−i}
    # and the atom factor u^k cancels the u^{−k}: moments u-independent.
    lhs = _jj * _kk - sp.Rational(1, 2) * _jj * (_jj + 1)
    rhs = sp.Rational(1, 2) * _kk * (_kk - 1) \
        - sp.Rational(1, 2) * _ii * (_ii + 1)
    d = sp.expand(lhs.subs(_jj, _ii + _kk) - rhs)
    assert d == 0, d
    # u-power bookkeeping: u^{−j} = u^{−i}·u^{−k} at j = i + k (trivial
    # but stated): exact.
    du = sp.simplify(_u ** (-(_ii + _kk)) - _u ** (-_ii) * _u ** (-_kk))
    assert du == 0, du
    # log-normal reflection symmetry about μ̂ (sympy exact): the density
    # exp(−(t−μ̂)²/(2σ²)) is invariant under t ↦ 2μ̂ − t.
    t, mu, sg = sp.symbols("t mu sigma", real=True, positive=True)
    dens = sp.exp(-(t - mu) ** 2 / (2 * sg ** 2))
    assert sp.simplify(dens.subs(t, 2 * mu - t) - dens) == 0

    # numeric layer at q = 1.2
    q0 = mpf("1.2")
    qt = mpsqrt(q0)
    uu = mpf(U_GENERIC)
    _, _, mom_j = jackson_factor(q0, N_MOM)

    # R4b — u-independent moments, distinct support
    js1, at1, ms1, mom1 = theta_translate_factor(q0, mpf(1), N_MOM)
    jsu, atu, msu, momu = theta_translate_factor(q0, uu, N_MOM)
    worst = mpf(0)
    for k in range(N_MOM + 1):
        tgt = q0 ** (mpf(k * (k - 1)) / 4)
        worst = max(worst, abs(mom1[k] / tgt - 1), abs(momu[k] / tgt - 1))
    assert worst < TOL_50, worst
    # support distinctness: fractional part of ln u / ln q̃ away from ℤ
    frac = mp.frac(mp.log(uu) / mp.log(qt))
    dist = min(frac, 1 - frac)
    assert dist > mpf("0.05"), dist

    # R4c — the bar-reflection σ: s ↦ q̃^{−1}/s.
    # theta u = 1: σ-invariant via the exact index map j ↦ −1−j
    # (σ(q̃^j) = q̃^{−1−j}; masses q̃^{−j(j+1)/2} equal at j and −1−j).
    for j in range(-6, 7):
        e1 = -sp.Rational(j * (j + 1), 2)
        e2 = -sp.Rational((-1 - j) * (-j), 2)
        assert e1 == e2, j
    # pushforward σμ_u equals μ_{1/u} as a measure (numeric, 1e−30)
    at_ref = [qt ** (-1) / a for a in atu]
    _, at_inv, ms_inv, _ = theta_translate_factor(q0, 1 / uu, N_MOM)
    assert measure_eq(at_ref, msu, at_inv, ms_inv, mpf(TOL_50) * 100)
    # and μ_{1/u} ≠ μ_u for generic u (support distance: u vs 1/u grids
    # differ iff 2·ln u / ln q̃ ∉ ℤ):
    frac2 = mp.frac(2 * mp.log(uu) / mp.log(qt))
    dist2 = min(frac2, 1 - frac2)
    assert dist2 > mpf("0.05"), dist2

    # R4d — symmetrization: μ^sym_u = ½(μ_u + μ_{1/u}) is positive,
    # σ-invariant by construction, atomic, and has the SAME moments;
    # Jackson ⊛ μ^sym_u has exactly the balanced moments.
    _, at_i, ms_i, mom_i = theta_translate_factor(q0, 1 / uu, N_MOM)
    worst_s = mpf(0)
    for k in range(N_MOM + 1):
        m_sym = (momu[k] + mom_i[k]) / 2
        tgt = q0 ** (mpf(k * (k - 1)) / 4)
        worst_s = max(worst_s, abs(m_sym / tgt - 1))
        full = mom_j[k] * m_sym
        nbal = mp_balanced_normalizer(q0, k + 1)
        worst_s = max(worst_s, abs(full / nbal - 1))
    assert worst_s < TOL_50, worst_s
    # σ-invariance of the symmetrized measure (pushforward = itself):
    at_sym = atu + at_i
    ms_sym = [m / 2 for m in msu] + [m / 2 for m in ms_i]
    at_sym_ref = [qt ** (-1) / a for a in at_sym]
    assert measure_eq(at_sym_ref, ms_sym, at_sym, ms_sym,
                      mpf(TOL_50) * 100)
    # distinct from the canonical u = 1 kernel (its support contains the
    # u-grid, disjoint from q̃^ℤ by dist > 0.05 above): recorded.

    wb.add_assertion(
        "fibre_canonical_choice_not_pinned", computed="0", expected="0",
        tolerance=TOL_EXACT,
        source=f"q = 1.2, 60 dps + sympy-exact reindex/symmetry "
               f"identities: the u-translated theta factor (atoms u·q̃^j, "
               f"masses ∝ q̃^(−j(j+1)/2)·u^(−j)) has u-INDEPENDENT moments "
               f"q^(k(k−1)/4) (rel < 1e−30 at u = 1 and u = {U_GENERIC}; "
               f"exact mechanism jk − j(j+1)/2 = k(k−1)/2 − i(i+1)/2), "
               f"with support distinct from the u = 1 grid (grid offset "
               f"{mp.nstr(dist, 5)} of a q̃-step). The bar-reflection "
               f"σ: s ↦ q̃^(−1)/s — the unique reflection fixing both "
               f"Attack-B B-factor realizations (theta u = 1 via "
               f"j ↦ −1−j exact; log-normal via Gaussian symmetry, sympy) "
               f"— maps μ_u ↦ μ_(1/u) (measure equality < 1e−28), and the "
               f"symmetrization ½(μ_u + μ_(1/u)) is positive, σ-invariant, "
               f"atomic, same moments, giving after Jackson-convolution a "
               f"u-CONTINUUM of positive kernels with exactly the balanced "
               f"moments N^bal(k+1) (rel < 1e−30). CONSEQUENCE: "
               f"positivity + balanced moments + bar-reflection-invariance "
               f"+ atomicity do NOT pin the fibre kernel — (REP)'s "
               f"canonical choice needs a derivation input beyond "
               f"moments + symmetry (RSZ §1.2.1 kernel non-canonicity; "
               f"at q = 1 the class IS a singleton by Carleman, Attack A)")
    wb.add_data("translate_support_offsets",
                {"u": U_GENERIC, "dist_u_grid": mp.nstr(dist, 8),
                 "dist_u_vs_inv_u": mp.nstr(dist2, 8)})


def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("rep-jackson-identification", engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "Attack 1 on (REP) — the last substantive hypothesis of "
        "conj:schwinger-measure-computational-time (bean qou-u5p0; "
        "audit-only, scope-(a), NO FIT, nothing wired). DETERMINATION "
        "(audit §1, corpus survey): the corpus performs NO integral "
        "resummation of the binding OGF — production binding is the "
        "finite Markov-trace evaluation (mass_binding_dashboard.py, "
        "canonical_mass.py); the OGF appears only formally (keystone "
        "strip, coefficient-level q-Borel, growth diagnostics). Hence "
        "(REP) is a canonical-CHOICE claim, not a matching to an "
        "existing corpus integral. R1: the corpus formal operation "
        "(involution periods B_n = I(n)/n, strip N(n) = (n−1)! forced "
        "by n·N(n) = n!, depth-2 recurrence) verified exact. R2 "
        "(falsifier, archimedean): the strip IS order-by-order "
        "integration against e^(−s)·ds/s — per-order moments AND the "
        "finite-order polynomial identity exact (sympy) — MATCH. R3 "
        "(falsifier, fibre; q = 1.2 + both q₀ pins): the Jackson⊛theta "
        "atomic kernel's ds/s-moments equal N^bal(n) = "
        "q^(−(n−1)(n−2)/4)[n−1]_q! (rel < 1e−30) and the q-lift C1 "
        "carrier resums through the kernel correctly at finite order; "
        "the exact gap to the corpus's proved one-sided strip is the "
        "Attack-E bar-covariant weight — MATCH in the balanced "
        "convention. R4 (the new content): the u-translate/reflection/"
        "symmetrization construction exhibits a u-CONTINUUM of "
        "positive, bar-reflection-invariant, ATOMIC kernels sharing "
        "all balanced moments (exact reindex mechanism; 60 dps "
        "cross-checks) — positivity + moments + bar-symmetry + "
        "atomicity do NOT pin the kernel at q ≠ 1 (sharpens Attack B "
        "§3.1 from 'two realizations' to 'a continuum inside the "
        "symmetric atomic class'); at q = 1 the class is a singleton "
        "(Carleman, Attack A, cited). RSZ (Astérisque 355) §1.2.1 "
        "states kernel non-canonicity and gives no general explicit "
        "integral formula for its ch. 5 summation — no 'RSZ "
        "classification' pins the theta kernel as the unique "
        "bar-invariant choice. Nothing here proves or refutes the "
        "conjecture.")
    wb.set_audit_only(
        "docs/audits/2026-08-01-rep-jackson-identification.md")

    b = block_r1_corpus_operation(wb)
    print("R1: corpus formal operation (strip + depth-2 recurrence) exact.")
    block_r2_archimedean_falsifier(wb, b)
    print("R2: archimedean falsifier — strip = ∫ e^(-s) ds/s, exact MATCH.")
    for name, qs in (("test", "1.2"), ("muon", Q0_MUON_STR),
                     ("proton", Q0_PROTON_STR)):
        block_r3_fibre_falsifier(wb, name, qs)
        print(f"R3[{name}]: fibre falsifier — Jackson⊛theta ds/s-moments "
              f"= N^bal, MATCH (rel < 1e-30).")
    block_r4_nonuniqueness(wb)
    print("R4: canonical choice NOT pinned at q ≠ 1 — u-continuum of "
          "positive symmetric atomic kernels with the balanced moments.")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.add_data("determination", {
        "verdict": "formal-only — no integral resummation of the binding "
                   "OGF exists in the corpus",
        "production_binding": "computations/mass_binding_dashboard.py "
                              "(Markov trace tr_m_atom_zn at α = E₀; "
                              "closed-form B_sym chain), "
                              "computations/canonical_mass.py facade",
        "formal_appearances": [
            "content/quantum-observable-universe/lean/QOU/Mass/"
            "KeystoneBridgeC1Binding.lean (normalizer strip, recurrence)",
            "docs/audits/2026-07-20-qlift-routeD-qborel-transform.md "
            "(coefficient-level FORMAL q-Borel — diagonal weight)",
            "computations/lever1_borel_half_singularity_probe.py + "
            "lever1_gevrey_order_pin.py (growth/singularity DIAGNOSTICS, "
            "exploratory, no resummed value produced or consumed)",
        ],
        "nearest_actual_resummations": [
            "computations/qbeta/qbeta_dladder_jackson_qborel_"
            "acceleration_probe.py (Q_β D-ladder — different series; "
            "fixed-base Jackson q-Borel refuted as mis-classed)",
            "computations/qbeta/qbeta_dladder_ecalle_phib_resummation.py "
            "(Q_β; Écalle/Φ_b state integral, measurement-only)",
            "computations/probes/qbeta_g3_5two_qborel_theta_laplace.py "
            "(Q_β Habiro bar-side; θ-kernel bilateral Laplace)",
        ]})
    wb.add_data("rsz_citations", {
        "paper": "library/arxiv-0903.0853v3/0903.0853v3.pdf — Ramis–Sauloy–Zhang, "
                 "Astérisque 355",
        "def_2_3_3": "level-1 formal q-Borel, weight q^{−n(n−1)/2} (p. 23)",
        "eq_1_2": "θ(z;q) triple product — manifest positivity (p. 9)",
        "sec_1_2_1": "kernel NON-canonicity: 'several choices for Borel "
                     "and Laplace kernels … and several choices of the "
                     "integration contours (continuous or discrete in "
                     "Jackson style)'; and for RSZ's own ch. 5 summation "
                     "'we did not obtain explicit integral formulae … "
                     "except for some particular cases' (pp. 7-8) — there "
                     "is NO RSZ classification in which the theta kernel "
                     "is the unique bar-invariant choice",
    })
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
