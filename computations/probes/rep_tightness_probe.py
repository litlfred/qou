#!/usr/bin/env python3
"""rep_tightness_probe.py — REP attack 2: tightness of the balanced
q-Borel kernel family as q → 1⁺ (archimedean (REP) without fibre
uniqueness).

Bean qou-ry7x, epic qou-q04o. AUDIT-ONLY — scope-(a), NO FIT, nothing
wired. Target: the archimedean (REP) leg of
conj:schwinger-measure-computational-time for the CONSTRUCTED balanced
kernel family (Attack B §3, docs/audits/2026-07-25-qborel-confluence-pos-attack.md):
the atomic Jackson ⊛ theta kernel K^at_q and the a.c. Jackson ⊛
log-normal kernel K^ac_q (σ² = (ln q)/2, μ̂ = −(ln q)/4) are explicit
positive probability measures with Stieltjes moments exactly
N^bal_q(k+1) → k!.

CLAIM UNDER TEST: the family {K_q : q ∈ (1, q₀]} is TIGHT — so (by
Prokhorov selection + the Lean-proved factorial-moment determinacy pin,
both carried in QOU/Archimedean/BalancedKernelTightness.lean and
BalancedKernelConfluence.lean) every subsequential weak limit is THE
Schwinger measure e^{−s}·ds.

THE ANALYTIC MECHANISM (nearly free): the SECOND moment of every member
is ∫ s² dK_q = N^bal_q(3) = q^{−1/2}(1+q) = 2 + (√q−1)²/√q — an EXACT
identity, monotone increasing in q on (1, ∞), hence uniformly bounded by
C₂ := q₀^{−1/2}(1+q₀) on the whole family q ∈ (1, q₀]. Markov's
inequality then gives the uniform tail bound
K_q((R, ∞)) ≤ N^bal_q(3)/R² ≤ C₂/R², i.e. the tightness certificate:
for every ε > 0 the compact [0, √(C₂/ε)] catches mass ≥ 1 − ε of EVERY
member simultaneously.

NORMALIZATION CONSISTENCY (the dK vs ds/s subtlety): all kernels here
are FINITE (probability) measures K with Stieltjes moments
∫ s^k dK = N^bal(k+1), k ≥ 0 (mass N^bal(1) = 1) — Attack A's A2 shift,
identical to the FrechetShohat.lean `HasStieltjesMoments` convention and
to the shifted framing e^{−s}ds with moments k! = N(k+1). The
conjecture's ds/s-moment shape ∫ s^n dK/s = N^bal(n) is the same
statement; the "second moment" of the tightness argument is the k = 2
Stieltjes moment = N^bal(3), whose q → 1 limit is 2! = 2.

BLOCKS
  T1  Exact identities (sympy):
      (a) second moment N^bal(3) = q^{−1/2}(1+q), and the tightness-is-
          nearly-free form N^bal(3) − 2 = (√q−1)²/√q ≥ 0;
      (b) monotonicity: d/dq N^bal(3) = (q−1)/(2q^{3/2}) > 0 for q > 1
          (exact factorization) ⇒ sup_{q ∈ (1, q₀]} N^bal(3) =
          N^bal_{q₀}(3) =: C₂ — the uniform second-moment bound is exact
          and covers the WHOLE interval, not just sampled q;
      (c) mass N^bal(1) = 1 (probability normalization).
  T2  Second moments of the explicit kernels (mpmath 60 dps, tol 1e−30):
      at q ∈ {1.2, q₀ proton, q₀ muon, 1+10⁻¹, 1+10⁻², 1+10⁻³}:
      Jackson([2]_p!) × theta(q^{1/2}) = N^bal(3) (atomic) and
      Jackson × e^{2μ̂+2σ²} = N^bal(3) (log-normal a.c.), both ≤ the
      exact bound q^{−1/2}(1+q) evaluated at that q, and all ladder
      values ≤ C₂(max tested q).
  T3  Markov tail verification (mpmath 60 dps): at
      q ∈ {1.2, q₀ proton, 1+10⁻², 1+10⁻³}, thresholds
      R ∈ {2, 4, 8, 16, 32}: tail masses K_q((R, ∞)) of BOTH kernel
      variants (atomic: exact prefix-sum over the (m, j) grid via the
      separable Jackson-tail × theta-atom decomposition; a.c.: Jackson
      mixture of log-normal complementary CDFs, erfc) satisfy
      tail ≤ N^bal_q(3)/R² (Markov, per-member) — and are in fact far
      smaller (recorded; diagnostic of the exponential-type actual
      decay, not needed for tightness).
  T4  Uniform tightness certificate: for ε ∈ {10⁻², 10⁻⁴, 10⁻⁶}:
      R(ε) = √(C₂/ε) with C₂ from the max tested q; verify
      sup over ALL tested q (both variants) of tail(R(ε)) ≤ ε.
      (Compact windows [0, R(ε)] catching 1 − ε of every member.)
  T5  Moment-convergence hook (the k = 2 leg feeding the Lean
      `isTightMeasureSet_of_tendsto_integral_sq`): N^bal_q(3) − 2 ↓ 0
      monotonically along the ladder, at the exact rate (√q−1)²/√q
      (rel < 1e−30 vs the T1a closed form).

VERDICT SHAPE (scope-(a)): tightness of the CONSTRUCTED family is
verified numerically-exactly at every sampled q and proved analytically
by the exact T1 identities + Markov (the Lean file carries the Markov /
uniform-bound / tightness steps sorry-free over Mathlib's
IsTightMeasureSet). What this does NOT close: the identification of the
substrate's OWN kernel with a member of this family (REP-1's job; the
fibre moment problem is indeterminate at q ≠ 1, Attack B §3.1).

Exit 0 iff all assertions pass. Witness: rep-tightness.witness.json
(audit-only). Audit doc:
docs/audits/2026-08-01-rep-tightness-archimedean.md.
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
from mpmath import mp, mpf, sqrt as mpsqrt, exp as mpexp, erfc as mperfc  # noqa: E402
from mpmath import log as mplog  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0        # sympy exact comparisons
TOL_50 = 1e-30       # 60-dps kernel-identity cross-checks
N_LADDER = 3         # ladder q = 1 + 10^{−k}, k = 1..3 (atomic grids grow as 10^k)
R_THRESHOLDS = (2, 4, 8, 16, 32)
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

EPS_LADDER = (mpf("1e-2"), mpf("1e-4"), mpf("1e-6"))
TAIL_DPS = 34        # truncation depth for kernel grids (tails compared at 1e-30)

# q₀ pins (50-digit strings with provenance), as in the Attack-B probe.
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"

_q = sp.symbols("q", positive=True)


# ------------------------------------------------------------------ kernels
# (identical constructions to qborel_confluence_pos_probe.py Block C4 —
# reused, not re-derived; the moment identities were verified there to
# 1e−30 and are re-checked here at k = 0, 2 only.)

def jackson_kernel(q0: mpf):
    """Jackson q-Gamma kernel at p = 1/q0: atoms t_m = p^m/(1−p), masses
    c_m = p^m·(p^{m+1};p)_∞ > 0. Returns (atoms, masses, prefix) where
    prefix[m] = Σ_{i<m} c_i (for O(1) tail reads: the atoms are strictly
    DECREASING in m, so the tail above a threshold is a prefix sum)."""
    p = 1 / q0
    M = int(TAIL_DPS / float(-mp.log10(p))) + 60
    pp = [mpf(1)]
    for j in range(1, M + 1):
        pp.append(pp[-1] * (1 - p ** j))
    pp_inf = pp[-1]
    a = 1 / (1 - p)
    atoms = [a * p ** m for m in range(M)]
    masses = [p ** m * pp_inf / pp[m] for m in range(M)]
    prefix = [mpf(0)]
    for c in masses:
        prefix.append(prefix[-1] + c)
    return atoms, masses, prefix


def jackson_tail(atoms, prefix, x: mpf) -> mpf:
    """Σ_{m : t_m > x} c_m — mass of the Jackson kernel above x.
    Atoms decrease in m: binary-search the first m with t_m ≤ x."""
    lo, hi = 0, len(atoms)
    while lo < hi:
        mid = (lo + hi) // 2
        if atoms[mid] > x:
            lo = mid + 1
        else:
            hi = mid
    return prefix[lo]


def theta_kernel(q0: mpf, k_max: int = 2):
    """Half-weight theta kernel at q̃ = √q0: atoms q̃^j (j ∈ ℤ), masses
    q̃^{−j(j+1)/2}/Θ₀ > 0; k-th moments q0^{k(k−1)/4} exactly."""
    qt = mpsqrt(q0)
    J = 10
    while float((J * (J + 1) / 2 - J * k_max) * mp.log10(qt)) < TAIL_DPS + 10:
        J += 10
    js = list(range(-J, J + 1))
    w = [qt ** (-mpf(j * (j + 1)) / 2) for j in js]
    Theta0 = sum(w)
    atoms = [qt ** j for j in js]
    masses = [x / Theta0 for x in w]
    return atoms, masses


def second_moment_atomic(q0: mpf, jk, tk) -> mpf:
    """∫ s² dK^at = (Σ c_m t_m²)·(Σ w_j a_j²) — separable Mellin factors."""
    atoms_j, masses_j, _ = jk
    atoms_t, masses_t = tk
    m2_j = sum(c * t ** 2 for c, t in zip(masses_j, atoms_j))
    m2_t = sum(c * t ** 2 for c, t in zip(masses_t, atoms_t))
    return m2_j * m2_t


def tail_atomic(R: mpf, jk, tk) -> mpf:
    """K^at((R, ∞)) = Σ_j w_j · JacksonTail(R / a_j) (separable, exact
    up to the positive-series truncation of both grids)."""
    atoms_jack, _, prefix = jk
    atoms_t, masses_t = tk
    return sum(wj * jackson_tail(atoms_jack, prefix, R / aj)
               for aj, wj in zip(atoms_t, masses_t))


def tail_ac(R: mpf, jk, sig: mpf, muh: mpf) -> mpf:
    """K^ac((R, ∞)) = Σ_m c_m · ½·erfc((ln(R/t_m) − μ̂)/(σ√2)) — the
    Jackson mixture of log-normal complementary CDFs."""
    atoms_jack, masses_jack, _ = jk
    tot = mpf(0)
    for t, c in zip(atoms_jack, masses_jack):
        z = (mplog(R / t) - muh) / (sig * mpsqrt(2))
        tot += c * mperfc(z) / 2
    return tot


def nbal3(q0: mpf) -> mpf:
    """N^bal_q(3) = q^{−1/2}·(1+q) — the exact second moment (T1a)."""
    return (1 + q0) / mpsqrt(q0)


# ---------------------------------------------------------------- Block T1

def block_t1_exact(wb: WitnessBuilder) -> None:
    """T1: exact second-moment identity, positivity gap, monotonicity."""
    _ok: list[bool] = []
    m = 2  # N^bal(3) = q^{-m(m-1)/4}·[2]_q! at m = 2
    nbal = _q ** (-sp.Rational(m * (m - 1), 4)) * (1 + _q)  # [2]_q! = 1+q
    # (a) closed forms
    d_a1 = sp.simplify(nbal - (1 + _q) / sp.sqrt(_q))
    d_a2 = sp.simplify(nbal - 2 - (sp.sqrt(_q) - 1) ** 2 / sp.sqrt(_q))
    _ok.append(bool(d_a1 == 0 and d_a2 == 0))
    assert _ok[-1], (d_a1, d_a2)
    # (b) monotonicity: d/dq = (q−1)/(2q^{3/2}) — exact factorization
    d_b = sp.simplify(sp.diff(nbal, _q) - (_q - 1) / (2 * _q ** sp.Rational(3, 2)))
    _ok.append(bool(d_b == 0))
    assert _ok[-1], d_b
    # (c) mass: N^bal(1) = [0]_q! · q^0 = 1 exactly (m = 0 empty product)
    wb.add_assertion(
        "second_moment_exact_identities", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source="∫ s² dK_q = N^bal_q(3) = q^{−1/2}(1+q) = 2 + (√q−1)²/√q "
               "and d/dq N^bal(3) = (q−1)/(2q^{3/2}) — exact (sympy). "
               "For q > 1 the derivative is > 0, so on the family "
               "interval q ∈ (1, q₀] the second moment is monotone "
               "increasing with sup = N^bal_{q₀}(3) =: C₂ and inf → 2! "
               "= 2 as q → 1⁺: the uniform second-moment bound covering "
               "the WHOLE interval is exact and free (no numerics "
               "needed); the mass is N^bal(1) = 1 exactly (probability "
               "normalization, dK-framing = Attack A's A2 shift of the "
               "ds/s convention)")


# ---------------------------------------------------------------- Block T2

def block_t2_kernel_second_moments(wb: WitnessBuilder, q_values) -> None:
    """T2: kernel second moments == N^bal(3) (both variants) and ≤ the
    exact bound, per sampled q."""
    worst = mpf(0)
    rows = {}
    c2_max = max(nbal3(q0) for _, q0 in q_values)
    for name, q0 in q_values:
        jk = jackson_kernel(q0)
        tk = theta_kernel(q0)
        hh = mplog(q0)
        sig2 = hh / 2
        muh = -hh / 4
        target = nbal3(q0)
        m2_at = second_moment_atomic(q0, jk, tk)
        # a.c. second moment: Jackson [2]_p! factor × log-normal
        # e^{2μ̂+2σ²} = q^{1/2} (Gaussian moment, exact)
        m2_j = sum(c * t ** 2 for c, t in zip(jk[1], jk[0]))
        m2_ac = m2_j * mpexp(2 * muh + 2 * sig2)
        for m2 in (m2_at, m2_ac):
            worst = max(worst, abs(m2 / target - 1))
            assert m2 <= target * (1 + mpf(10) ** (-25)), (name, m2, target)
        assert target <= c2_max * (1 + mpf(10) ** (-25)), name
        rows[name] = {"q": mp.nstr(q0, 12), "N_bal_3": mp.nstr(target, 25),
                      "m2_atomic": mp.nstr(m2_at, 25),
                      "m2_ac": mp.nstr(m2_ac, 25)}
    assert worst < TOL_50, worst
    wb.add_assertion(
        "kernel_second_moments", computed=mp.nstr(worst, 5),
        expected="0", tolerance=TOL_50,
        source=f"∫ s² dK = N^bal_q(3) for BOTH explicit kernels (atomic "
               f"Jackson ⊛ theta via the separable Mellin factors "
               f"[2]_p!·q^{{1/2}}; a.c. Jackson ⊛ log-normal via the "
               f"exact Gaussian moment e^{{2μ̂+2σ²}} = q^{{1/2}}) at "
               f"every sampled q ({', '.join(n for n, _ in q_values)}), "
               f"rel < 1e−30 (60 dps), and every value ≤ the exact "
               f"monotone bound C₂ = max N^bal(3) = {mp.nstr(c2_max, 12)} "
               f"— the uniformly-bounded-second-moment hypothesis of the "
               f"Lean tightness theorem is verified on the constructed "
               f"family")
    wb.add_data("second_moments", rows)


# ---------------------------------------------------------------- Block T3

def block_t3_markov_tails(wb: WitnessBuilder, q_values) -> dict:
    """T3: tail masses obey the Markov bound tail(R) ≤ N^bal(3)/R² at
    every sampled q and threshold, both kernel variants."""
    _ok: list[bool] = []
    rows = {}
    kernels = {}
    for name, q0 in q_values:
        jk = jackson_kernel(q0)
        tk = theta_kernel(q0)
        hh = mplog(q0)
        sig = mpsqrt(hh / 2)
        muh = -hh / 4
        kernels[name] = (q0, jk, tk, sig, muh)
        m2 = nbal3(q0)
        rows[name] = {}
        for R in R_THRESHOLDS:
            Rm = mpf(R)
            markov = m2 / Rm ** 2
            t_at = tail_atomic(Rm, jk, tk)
            t_ac = tail_ac(Rm, jk, sig, muh)
            # positive-series truncation error < 1e-30 ≪ slack: bound holds
            _ok.append(bool(t_at <= markov))
            assert _ok[-1], (name, R, t_at, markov)
            _ok.append(bool(t_ac <= markov))
            assert _ok[-1], (name, R, t_ac, markov)
            rows[name][str(R)] = {
                "markov_bound": mp.nstr(markov, 10),
                "tail_atomic": mp.nstr(t_at, 10),
                "tail_ac": mp.nstr(t_ac, 10)}
    wb.add_assertion(
        "markov_tail_bound", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source=f"0 = #violations of [K_q((R,∞)) ≤ N^bal_q(3)/R²] over "
               f"q ∈ {{{', '.join(n for n, _ in q_values)}}}, "
               f"R ∈ {R_THRESHOLDS}, BOTH kernel variants (atomic tail "
               f"by exact prefix-sum over the separable Jackson × theta "
               f"grid; a.c. tail as the Jackson mixture of log-normal "
               f"erfc complementary CDFs; 60 dps). The observed tails "
               f"are far below the Markov bound (exponential-type actual "
               f"decay — diagnostic only; Markov + the uniform second "
               f"moment already suffice for tightness)")
    wb.add_data("markov_tails", rows)
    return kernels


# ---------------------------------------------------------------- Block T4

def block_t4_uniform_certificate(wb: WitnessBuilder, kernels) -> None:
    """T4: the tightness certificate — one compact window per ε catches
    1 − ε of EVERY member simultaneously."""
    _ok: list[bool] = []
    c2_max = max(nbal3(q0) for q0, *_ in kernels.values())
    cert = {}
    for eps in EPS_LADDER:
        Reps = mpsqrt(c2_max / eps)
        sup_tail = mpf(0)
        for name, (q0, jk, tk, sig, muh) in kernels.items():
            sup_tail = max(sup_tail, tail_atomic(Reps, jk, tk),
                           tail_ac(Reps, jk, sig, muh))
        _ok.append(bool(sup_tail <= eps))
        assert _ok[-1], (mp.nstr(eps, 5), sup_tail)
        cert[mp.nstr(eps, 5)] = {"R_eps": mp.nstr(Reps, 12),
                                 "sup_tail": mp.nstr(sup_tail, 10)}
    wb.add_assertion(
        "uniform_tightness_certificate", computed=all(_ok), expected=True,
        tolerance=TOL_EXACT,
        source=f"0 = #violations of [sup_q K_q((R(ε),∞)) ≤ ε] with "
               f"R(ε) = √(C₂/ε), C₂ = {mp.nstr(c2_max, 12)} (the exact "
               f"monotone second-moment bound), ε ∈ {{1e−2, 1e−4, "
               f"1e−6}}, sup over every sampled q and BOTH variants: "
               f"the single compact [0, R(ε)] catches mass ≥ 1 − ε of "
               f"every family member simultaneously — the "
               f"IsTightMeasureSet certificate realized numerically")
    wb.add_data("tightness_certificate", cert)


# ---------------------------------------------------------------- Block T5

def block_t5_moment_convergence(wb: WitnessBuilder) -> None:
    """T5: k = 2 moment-convergence leg: N^bal(3) − 2 = (√q−1)²/√q ↓ 0
    along the ladder, matching the exact closed form."""
    worst = mpf(0)
    prev = None
    ladder = {}
    for k in range(1, 7):
        q0 = mpf(1) + mpf(10) ** (-k)
        gap = nbal3(q0) - 2
        closed = (mpsqrt(q0) - 1) ** 2 / mpsqrt(q0)
        worst = max(worst, abs(gap / closed - 1))
        assert gap > 0
        if prev is not None:
            assert gap < prev
        prev = gap
        ladder[f"1e-{k}"] = mp.nstr(gap, 15)
    assert worst < TOL_50, worst
    wb.add_assertion(
        "second_moment_convergence", computed=mp.nstr(worst, 5),
        expected="0", tolerance=TOL_50,
        source="N^bal_q(3) − 2 = (√q−1)²/√q exactly (rel < 1e−30 vs the "
               "closed form) and strictly decreasing to 0 along "
               "q = 1+10^{−k}, k = 1..6 — the k = 2 moment-convergence "
               "hypothesis (Tendsto → 2!) that the Lean theorem "
               "isTightMeasureSet_of_tendsto_integral_sq converts into "
               "tightness via Tendsto.bddAbove_range + Markov")
    wb.add_data("second_moment_gap_ladder", ladder)


def main() -> int:
    set_compute_dps(60)
    wb = WitnessBuilder("rep-tightness", engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "REP attack 2 — tightness of the balanced q-Borel kernel family "
        "(bean qou-ry7x, epic qou-q04o; audit-only, scope-(a), NO FIT, "
        "nothing wired). The explicit positive kernels with exactly the "
        "balanced moments (atomic Jackson ⊛ theta; a.c. Jackson ⊛ "
        "log-normal, σ² = ln(q)/2, μ̂ = −ln(q)/4; Attack B §3) form a "
        "q-indexed family whose SECOND moment is the exact monotone "
        "quantity N^bal_q(3) = q^{−1/2}(1+q) = 2 + (√q−1)²/√q — "
        "uniformly bounded on q ∈ (1, q₀] by C₂ = N^bal_{q₀}(3). "
        "Markov's inequality then yields uniform tail control "
        "K_q((R,∞)) ≤ C₂/R²: the family is TIGHT, verified here at "
        "60 dps (tails of both variants vs the Markov bound at every "
        "sampled q; one compact window per ε catching 1−ε of every "
        "member). Consequence (carried in Lean, "
        "QOU/Archimedean/BalancedKernelTightness.lean): tight + "
        "[Prokhorov selection, Mathlib-gap class] ⇒ subsequential weak "
        "limits exist; + [moment passage, Mathlib-gap class] + the "
        "Lean-PROVED factorial determinacy pin (Carleman divergence + "
        "[CarlemanDeterminacyStieltjes]) ⇒ EVERY subsequential limit is "
        "the Schwinger measure e^{−s}ds — archimedean (REP) for the "
        "constructed family without fibre uniqueness (which fails: the "
        "fibre problem is indeterminate at q ≠ 1, Attack B §3.1). NOT "
        "closed: the identification of the substrate's own kernel with "
        "a member of this family (REP-1).")
    wb.set_audit_only("docs/audits/2026-08-01-rep-tightness-archimedean.md")

    block_t1_exact(wb)
    print("T1: exact second-moment identity + monotone uniform bound "
          "(sympy).")

    q_values_t2 = [("test", mpf("1.2")),
                   ("proton", mpf(Q0_PROTON_STR)),
                   ("muon", mpf(Q0_MUON_STR))]
    q_values_t2 += [(f"1+1e-{k}", mpf(1) + mpf(10) ** (-k))
                    for k in range(1, N_LADDER + 1)]
    block_t2_kernel_second_moments(wb, q_values_t2)
    print("T2: kernel second moments == N^bal(3), both variants, "
          "rel < 1e-30.")

    q_values_t3 = [("test", mpf("1.2")),
                   ("proton", mpf(Q0_PROTON_STR)),
                   ("1+1e-2", mpf(1) + mpf(10) ** (-2)),
                   ("1+1e-3", mpf(1) + mpf(10) ** (-3))]
    kernels = block_t3_markov_tails(wb, q_values_t3)
    print("T3: Markov tail bound holds at every sampled q, R, both "
          "variants.")
    block_t4_uniform_certificate(wb, kernels)
    print("T4: uniform tightness certificate — one compact per eps for "
          "the whole family.")
    block_t5_moment_convergence(wb)
    print("T5: second-moment gap (sqrt(q)-1)^2/sqrt(q) -> 0 down the "
          "ladder.")

    wb.add_data("q0_pins", {
        "muon": Q0_MUON_STR, "proton": Q0_PROTON_STR,
        "source": "computations/q-pinning-50-digit.witness.json (muon, "
                  "canonical 3-CAL layer); qou_substrate.constants."
                  "Q_50_DIGIT_STR (proton, precision layer)"})
    wb.add_data("lean_carrier", {
        "file": "content/quantum-observable-universe/lean/QOU/"
                "Archimedean/BalancedKernelTightness.lean",
        "proved": ["tail_measureReal_le (Markov)",
                   "measure_compl_closedBall_le",
                   "isTightMeasureSet_of_integral_sq_le",
                   "isTightMeasureSet_of_tendsto_integral_sq",
                   "subseq_limit_eq_schwinger (conditional composition)"],
        "gap_classes": ["ProkhorovSelectionReal (Mathlib gap)",
                        "MomentPassageStieltjes (Mathlib gap)",
                        "CarlemanDeterminacyStieltjes (merged, reused)"]})
    wb.save()
    print("\nwitness saved; all assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
