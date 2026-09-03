#!/usr/bin/env python3
"""r2core_schwinger_measure_explore_probe.py — R2-core exploration: what would
DERIVE the Schwinger proper-time measure normalization from the framework's
own structures?

Bean qou-lecl. EXPLORATION TIER — scope-(a), audit-only, NO FIT, nothing
wired. The α_EM R2 owner ruling stands (2026-07-19: R2 is NOT Lean/derived-
proved; 1/(8π) stays a phase-4 identification) — this probe runs the CHEAP
EXACT FALSIFIER CHECKS for the candidate table of
docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md. It derives
nothing; it prunes and locates.

OWNER PREMISES used (recorded verbatim in the audit doc; tiered as
owner-supplied framework premises, NOT derived):
  P1 (2026-07-25): "substrate has a preferred scale q₀" is FALSE — q₀ is
      just our LOCAL value; the substrate itself is scale-free.
  P2 (2026-07-25): "proper-time is really only computational time."

THE EXACT TARGET (Task 1). The dt/t measure whose unit is open lives in the
ζ-regularized 1-loop photon determinant on the Bring Jacobian:
    log det'Δ = − ∫₀^∞ (ds/s) [Tr e^{−sΔ} − dim ker Δ],
whose small-s heat coefficient supplies a₀ = (4πs)^{−d/2}|_{d=2} = 1/(4π)
(#3909, derived), entering the α_EM tower as the one-loop insertion weight
½·a₀·α in [2]_q(1 − h²α) (#1511). The Lean shell
QOU/Archimedean/SchwingerMeasureShape.lean proves: SHAPE c·ds/s is the
unique scale-invariant density (scale_invariant_density_unique); one e-fold
carries measure c (one_nat_per_efold); s ~ E⁻² makes one energy e-fold two
proper-time e-folds (efold_jacobian_two); c = 1 with the ½ split gives
1/(8π) (unit_total_gives_eighth). OPEN: the unit c = 1 and the
½-adjudication.

CHECK BLOCKS (all pre-stated; exact sympy where possible, mpmath ≥ 30 dps
with tolerance 1e-25 otherwise; the two q₀ pins compared at 50 dps):

  B1  Linear-unit invisibility (kills candidate (c) as a unit CARRIER):
      ∫_{a/T}^{b/T} dt/t = ∫_a^b dt/t for any linear unit T > 0 (Reeb
      period t_P = q₀/(q₀−1), Planck step) — symbolically exact. A linear
      time unit cannot carry the multiplicative unit c.
  B2  Bar-fold identity (the ½ candidate (b′) made precise): for a
      bar-even integrand f(t) = f(1/t), ∫₀^∞ f dt/t = 2·∫₁^∞ f dt/t —
      the half-domain/quotient carries EXACTLY ½ of the bar-doubled
      measure; a bar-ODD integrand integrates to 0 (not ½) — the
      falsifier "the ½ appears only in bar-even channels".
  B3  The raw heat trace is NOT bar-even: Θ_{Z⁸}(1/s) = s⁴·Θ_{Z⁸}(s)
      (weight-4 Poisson reflection, unimodular b₁ = 8 lattice), NOT
      Θ(1/s) = Θ(s). The naive bar-symmetrization of the raw trace fails;
      the ½'s bar-even home must be per-channel (post-split), not the
      trace.
  B4  q-rung chart cancellation (owner premise P2, consequence (ii)):
      ∫_{q^n}^{q^{n+1}} dt/t = ln q exactly per rung; a per-step unit u
      gives c_eff = u/ln q₀. For every candidate intrinsic u ∈
      {1 nat, η_q = (2q−1)/q³, ℏ_q = 1−1/q, 𝔅 = qη_q/(q−1)²} the
      resulting c_eff is PIN-DEPENDENT (muon-q₀ vs proton-q₀ differ
      ~2.5e-9 relative; c_eff inherits > 1e-10 relative shift) — killed
      by the pin-invariance of the derived skeleton (#1511 exact rational
      coefficients; R2c rational·a₀ squeeze). The unique pin-stable
      per-step weight is u = ln q₀ (the step's own e-fold width) — the
      Haar/nat unit restated in the local chart: the ln q₀ conversion
      MUST cancel, and does only for the tautological choice.
      Plus: c_pair/c_rung = ½ exactly, q-independently — the bar-pair
      halving is scale-free even in the discrete chart.
  B5  Tower-level / keystone moment (candidate (d)): the forced q-Borel
      normalizer of KeystoneBridgeC1Binding, N(n) = (n−1)!, equals the
      n-th moment of the UNIT (c = 1) Schwinger measure with e^{−s}
      damping: ∫₀^∞ sⁿ e^{−s} ds/s = Γ(n) = (n−1)!. With measure
      c·ds/s the moments are c·(n−1)! and the PROVED bridge identity
      n·N(n) = n! forces c = 1 exactly; c = ½ would give n·N(n) = n!/2 ≠
      n!. CONDITIONAL on the unproved identification "binding Borel
      variable = loop proper time" (the keystone's geometric leg).
  B6  Chart disagreement of the two discrete step units: ln q − ℏ_q =
      (q−1)²/2 + O((q−1)³) — the q-rung and Reeb-circuit step units agree
      only in the classical limit (at q₀ they differ by ~5.3%), so "one
      per step" is chart-dependent; only the chart-free nat survives.

NO-4TH-CALIBRATION prune (third owner steer): any resolution of the ½
requiring a data-pinned constant would be a hidden CAL-4 — discipline-
excluded. Every candidate above is checked to add ZERO calibration DOF.

Exit 0 iff all assertions pass. Witness:
r2core-schwinger-measure-explore.witness.json (audit-only).
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
from mpmath import mp, mpf, quad, exp as mexp, log as mlog  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

TOL_EXACT = 0        # sympy exact comparisons
# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

TOL_NUM = mpf("1e-25")   # mpmath numeric identity checks (30 dps compute)
PIN_SHIFT_MIN = mpf("1e-10")  # pre-stated: a per-step unit is "pin-dependent"
                              # iff its c_eff shifts > 1e-10 relative between pins

# q₀, both pins, 50-digit strings with provenance (read muon from the
# canonical witness; proton from qou_substrate.constants Q_50_DIGIT_STR).
_MUON_WITNESS = _Path(__file__).resolve().parent.parent / \
    "q-pinning-50-digit.witness.json"
Q0_MUON_STR = record_upstream(_MUON_WITNESS, _UPSTREAM_RECORDS)["q0Value"]
# tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR
# (proton re-pin 2026-05-28; _solve_q_proton_f64 + mpmath refine):
Q0_PROTON_STR = "1.1099785827513808075916690956107688798744991218736"


def block1_linear_unit_invisibility():
    """B1: ∫_{a/T}^{b/T} dt/t = ∫_a^b dt/t symbolically — any linear time
    unit (Reeb period, Planck step) is invisible to the multiplicative
    measure."""
    a, b, T = sp.symbols("a b T", positive=True)
    t = sp.symbols("t", positive=True)
    lhs = sp.integrate(1 / t, (t, a / T, b / T))
    rhs = sp.integrate(1 / t, (t, a, b))
    diff = sp.simplify(lhs - rhs)
    assert diff == 0, f"linear-unit invisibility failed: {diff}"
    # Returned so the caller can record the COMPUTED difference. The witness
    # assertion used to read `computed="0", expected="0"` — a constant that
    # would pass with this whole function deleted (bean `qou-26f2`).
    # Reeb period at q₀ (recorded value only — it drops out above).
    q = sp.Rational(0)  # placeholder to avoid unused warnings
    del q
    return diff
    return diff


def block2_bar_fold(wb: WitnessBuilder):
    """B2: bar-even fold ∫₀^∞ f dt/t = 2∫₁^∞ f dt/t; bar-odd → 0."""
    # Bar-even test integrand f(t) = exp(−(t + 1/t)) (f(1/t) = f(t)).
    f = lambda t: mexp(-(t + 1 / t))  # noqa: E731
    I_full = quad(lambda t: f(t) / t, [0, 1, mp.inf])
    I_half = quad(lambda t: f(t) / t, [1, mp.inf])
    err_even = abs(I_full - 2 * I_half)
    assert err_even < TOL_NUM, f"bar-even fold: |I_full − 2·I_half| = {err_even}"
    wb.add_assertion(
        "bar_even_fold_half", computed=err_even, expected=0.0,
        tolerance=float(TOL_NUM),
        source="∫₀^∞ f dt/t − 2·∫₁^∞ f dt/t for bar-even f(t)=exp(−(t+1/t)) "
               "(exact by t↦1/t substitution; verified 30 dps): the bar "
               "quotient carries EXACTLY ½ of the bar-doubled Haar measure — "
               "candidate (b′)'s ½, located as a domain-quotient factor")
    # Bar-odd control g(t) = (t − 1/t)·exp(−(t+1/t)): integral is 0, not ½.
    g = lambda t: (t - 1 / t) * mexp(-(t + 1 / t))  # noqa: E731
    I_odd = quad(lambda t: g(t) / t, [0, 1, mp.inf])
    assert abs(I_odd) < TOL_NUM, f"bar-odd control not zero: {I_odd}"
    wb.add_assertion(
        "bar_odd_channel_zero", computed=abs(I_odd), expected=0.0,
        tolerance=float(TOL_NUM),
        source="∫₀^∞ (t−1/t)e^{−(t+1/t)} dt/t = 0 (bar-odd): the "
               "falsifier — bar-symmetrization gives ½ ONLY in bar-even "
               "channels; a bar-odd channel gets 0, never ½")


def block3_theta_not_bar_even(wb: WitnessBuilder):
    """B3: Θ_{Z⁸}(1/s) = s⁴ Θ_{Z⁸}(s) (weight-4), not Θ(1/s) = Θ(s)."""
    def theta1d(s):
        # θ(s) = Σ_{n∈Z} e^{−π s n²}, truncated far below 1e-30.
        n_max = int(mp.ceil(mp.sqrt(80 / s))) + 2
        return 1 + 2 * sum(mexp(-mp.pi * s * n * n)
                           for n in range(1, n_max))
    worst_refl = mpf(0)
    min_uneven = mp.inf
    for s in (mpf("0.7"), mpf("1.37")):
        T8_s = theta1d(s) ** 8
        T8_inv = theta1d(1 / s) ** 8
        refl = abs(T8_inv - s ** 4 * T8_s)      # Poisson, dim 8 unimodular
        uneven = abs(T8_inv - T8_s)             # naive bar-evenness
        worst_refl = max(worst_refl, refl)
        min_uneven = min(min_uneven, uneven)
    assert worst_refl < TOL_NUM, f"weight-4 reflection failed: {worst_refl}"
    assert min_uneven > mpf("0.1"), \
        f"trace unexpectedly bar-even: {min_uneven}"
    wb.add_assertion(
        "theta8_weight4_reflection", computed=worst_refl,
        expected=0.0, tolerance=float(TOL_NUM),
        source="Θ_{Z⁸}(1/s) − s⁴·Θ_{Z⁸}(s) at s ∈ {0.7, 1.37} (Jacobi "
               "θ³-type Poisson, b₁ = 8 unimodular lattice): the raw heat "
               "trace reflects with WEIGHT 4, it is NOT bar-even "
               "(|Θ(1/s) − Θ(s)| > 0.1 at the same points) — the naive "
               "bar-symmetrization of the raw trace FAILS; the ½'s "
               "bar-even home must be per-channel, post-split")


def block4_rung_chart(wb: WitnessBuilder):
    """B4: rung exactness + pin-dependence kill of intrinsic per-step units."""
    # Exact per-rung measure (symbolic): ∫_{q^n}^{q^{n+1}} dt/t = ln q.
    q, n = sp.symbols("q n", positive=True)
    t = sp.symbols("t", positive=True)
    rung = sp.simplify(sp.integrate(1 / t, (t, q ** n, q ** (n + 1))))
    assert sp.simplify(rung - sp.log(q)) == 0, f"rung measure: {rung}"
    wb.add_assertion(
        "rung_measure_exact_ln_q", computed=str(rung), expected="log(q)",
        tolerance=TOL_EXACT,
        source="∫_{q^n}^{q^{n+1}} dt/t = ln q exactly (sympy): the q-ladder "
               "rung is an exact e-fold lattice of width ln q₀ — the "
               "discretization commutes with the Haar measure")
    # Pair/single ratio is ½ exactly, q-independently (symbolic).
    L = sp.symbols("L", positive=True)
    ratio = sp.simplify((1 / (2 * L)) / (1 / L))
    assert ratio == sp.Rational(1, 2)
    wb.add_assertion(
        "pair_unit_half_scale_free", computed=str(ratio), expected="1/2",
        tolerance=TOL_EXACT,
        source="c_pair/c_rung = (1/(2L))/(1/L) = ½ for every rung width L "
               "= ln q₀: one-unit-per-bar-pair vs one-unit-per-rung differ "
               "by EXACTLY ½ independently of the local q₀ — the bar-pair "
               "halving is scale-free even in the discrete chart (the ½ is "
               "not a q-discretization artifact)")
    # Pin-dependence of intrinsic per-step units, 50 dps.
    set_compute_dps(50)
    shifts = {}
    pin_dependent = {}
    for name, ufun in [
        ("one_nat_per_step", lambda qv: mpf(1)),
        ("eta_q_per_step", lambda qv: (2 * qv - 1) / qv ** 3),
        ("hbar_q_per_step", lambda qv: 1 - 1 / qv),
        ("bandwidth_B_per_step",
         lambda qv: qv * ((2 * qv - 1) / qv ** 3) / (qv - 1) ** 2),
    ]:
        c_mu = ufun(mpf(Q0_MUON_STR)) / mlog(mpf(Q0_MUON_STR))
        c_pr = ufun(mpf(Q0_PROTON_STR)) / mlog(mpf(Q0_PROTON_STR))
        rel = abs(c_mu - c_pr) / c_mu
        shifts[name] = {"c_eff_muon": mp.nstr(c_mu, 20),
                        "c_eff_proton": mp.nstr(c_pr, 20),
                        "pin_rel_shift": mp.nstr(rel, 8)}
        pin_dependent[name] = bool(rel > PIN_SHIFT_MIN)
        assert rel > PIN_SHIFT_MIN, \
            f"{name}: expected pin-dependence, got rel shift {rel}"
    # The tautological unit u = ln q₀ gives c_eff = 1 at BOTH pins exactly.
    c_taut_mu = mlog(mpf(Q0_MUON_STR)) / mlog(mpf(Q0_MUON_STR))
    c_taut_pr = mlog(mpf(Q0_PROTON_STR)) / mlog(mpf(Q0_PROTON_STR))
    assert c_taut_mu == 1 and c_taut_pr == 1
    # `computed=True` was a constant; the measured verdict is carried now, so
    # the witness records the finding rather than restating the intent.
    wb.add_assertion(
        "intrinsic_step_units_pin_dependent",
        computed=all(pin_dependent.values()) and c_taut_mu == 1
        and c_taut_pr == 1,
        expected=True,
        tolerance=TOL_EXACT,
        source="every intrinsic per-step unit u ∈ {1 nat, η_q, ℏ_q, 𝔅} "
               "yields c_eff = u/ln q₀ with pin-relative shift > 1e-10 "
               "(muon vs proton q₀; 50 dps) — incompatible with the "
               "pin-invariant derived skeleton (#1511 exact rational "
               "coefficients; R2c rational·a₀ squeeze). The unique "
               "pin-stable per-step weight is the tautological u = ln q₀ "
               "(c_eff = 1 at both pins): the ln q₀ conversion cancels "
               "ONLY for the Haar/nat unit restated in the local chart")
    wb.add_data("per_step_unit_pin_shifts", shifts)
    # Recorded, not scored: none of the c_eff values is near a small
    # rational; η_q/ln q₀ ≈ 8.55 is NOT b₁ = 8 (6.9% off — recorded to
    # pre-empt a numerological re-pitch).
    eta_over = (2 * mpf(Q0_MUON_STR) - 1) / mpf(Q0_MUON_STR) ** 3 / \
        mlog(mpf(Q0_MUON_STR))
    wb.add_data("eta_q_over_ln_q0_not_b1",
                {"value": mp.nstr(eta_over, 12), "b1": 8,
                 "rel_miss": mp.nstr(abs(eta_over - 8) / 8, 4)})


def block5_keystone_moment(wb: WitnessBuilder):
    """B5: N(n) = (n−1)! is the c = 1 Schwinger moment; c = ½ breaks n·N=n!."""
    s, n = sp.symbols("s n", positive=True)
    # The real check was a bare `assert` in the loop below: it crashes the
    # script on failure but leaves NOTHING in the witness, and the witness
    # assertion then recorded `computed=True, expected=True` — a tautology that
    # would pass even if the loop were deleted (bean `qou-26f2`). The result is
    # now carried into the assertion, so the witness records the fact rather
    # than a constant, and the assertion can fail.
    moments_are_factorials = all(
        sp.integrate(s ** k * sp.exp(-s) / s, (s, 0, sp.oo))
        == sp.factorial(k - 1)
        for k in range(1, 7)
    )
    wb.add_assertion(
        "keystone_normalizer_is_unit_schwinger_moment",
        computed=moments_are_factorials,
        expected=True, tolerance=TOL_EXACT,
        source="∫₀^∞ sⁿ e^{−s} ds/s = (n−1)! for n = 1..6 (sympy exact) — "
               "the KeystoneBridgeC1Binding FORCED q-Borel normalizer "
               "N(n) = (n−1)! is precisely the n-th moment of the UNIT "
               "(c = 1) Schwinger measure. CONDITIONAL on the unproved "
               "identification (binding Borel variable = loop proper "
               "time): the proved bridge identity n·N(n) = n! then forces "
               "c = 1 — the binding sector and the loop measure share ONE "
               "unit, and the binding side's is forced")
    # The arithmetic distinguisher: c = ½ ⇒ n·N(n) = n!/2 ≠ n! (n ≥ 1... n!>0).
    # Same treatment — the bare `assert` proved it and the witness recorded a
    # constant.
    half_unit_differs = all(
        sp.factorial(k) / 2 != sp.factorial(k) for k in range(1, 7)
    )
    wb.add_assertion(
        "half_unit_breaks_bridge_identity",
        computed=half_unit_differs, expected=True,
        tolerance=TOL_EXACT,
        source="with c = ½ the moments are ½(n−1)! and n·N(n) = n!/2 ≠ n! "
               "for every n — the E-Jacobian reading of the ½ (c_s = ½ on "
               "the proper-time side) is arithmetically DISTINGUISHED "
               "from the ρ-split reading (c_s = 1 + channel ½) by the "
               "proved keystone identity, conditional on the same named "
               "identification (which remains UNPROVED)")


def block6_chart_disagreement(wb: WitnessBuilder):
    """B6: ln q − ℏ_q = (q−1)²/2 + O((q−1)³) — step units are chart-dependent."""
    q = sp.symbols("q", positive=True)
    expr = sp.log(q) - (1 - 1 / q)
    ser = sp.series(expr, q, 1, 4).removeO()
    lead = sp.simplify(ser.coeff((q - 1) ** 2))
    assert lead == sp.Rational(1, 2), f"leading coeff: {lead}"
    # Numeric ratio at q₀ (recorded): ln q₀ / ℏ_q(q₀) ≈ 1.053.
    set_compute_dps(50)
    q0 = mpf(Q0_MUON_STR)
    ratio = mlog(q0) / (1 - 1 / q0)
    wb.add_assertion(
        "step_charts_agree_only_classically", computed=str(lead),
        expected="1/2", tolerance=TOL_EXACT,
        source="ln q − ℏ_q = (q−1)²/2 + O((q−1)³) (sympy series): the two "
               "discrete step units (q-rung width ln q vs Reeb angle "
               f"ℏ_q = 1−1/q) agree only at q → 1; at q₀ their ratio is "
               f"≈ {mp.nstr(ratio, 6)} — 'one per step' is chart-"
               "dependent, a further consideration for the chart-free nat")


def main() -> int:
    set_compute_dps(50)
    wb = WitnessBuilder("r2core-schwinger-measure-explore",
                        engine="sympy+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "R2-core Schwinger proper-time measure exploration (bean qou-lecl; "
        "EXPLORATION TIER, audit-only, NO FIT, nothing wired; owner ruling "
        "2026-07-19 stands: R2 not derived-proved, 1/(8π) phase-4). Cheap "
        "exact falsifier checks for the candidate table: B1 linear units "
        "(Reeb period, Planck step) are invisible to the multiplicative "
        "measure (exact); B2 the bar quotient carries exactly ½ for "
        "bar-even integrands and 0 for bar-odd (the ½-only-in-bar-even "
        "falsifier); B3 the raw Z⁸ heat trace reflects with weight 4, not "
        "bar-evenly — the ½'s bar-even home is per-channel; B4 the q-rung "
        "is an exact ln q₀ e-fold lattice; every intrinsic per-step unit "
        "(1 nat, η_q, ℏ_q, 𝔅) is pin-dependent and thereby excluded — the "
        "unique pin-stable per-step weight is the step's own e-fold width "
        "(Haar restated); the bar-pair ½ is scale-free in the chart; B5 "
        "the keystone-forced N(n) = (n−1)! equals the c = 1 Schwinger "
        "moment — conditional on the (unproved) Borel-variable = "
        "proper-time identification, n·N(n) = n! forces c = 1 and "
        "distinguishes the ρ-split reading from the E-Jacobian reading; "
        "B6 the q-rung and Reeb step charts agree only classically. "
        "Owner premises P1 (substrate scale-free; q₀ local) and P2 "
        "(proper time = computational time) recorded and tiered in the "
        "audit doc. No-4th-calibration prune applied: every candidate "
        "adds zero calibration DOF; any data-pinned ½ is discipline-"
        "excluded.")
    wb.set_audit_only(
        "docs/audits/2026-07-25-r2core-schwinger-measure-exploration.md")

    b1_diff = block1_linear_unit_invisibility()
    print("B1: linear-unit invisibility exact (Reeb/Planck units cannot "
          "carry c).")
    wb.add_assertion(
        "linear_unit_invisibility", computed=str(b1_diff), expected="0",
        tolerance=TOL_EXACT,
        source="∫_{a/T}^{b/T} dt/t − ∫_a^b dt/t = 0 symbolically for any "
               "T > 0: candidate (c) (Reeb-period unit t_P = q₀/(q₀−1) "
               "≈ 10.08) cannot carry the multiplicative unit c — a "
               "linear time unit is invisible to the Haar measure")

    block2_bar_fold(wb)
    print("B2: bar-even fold = ½ exact; bar-odd channel = 0.")
    block3_theta_not_bar_even(wb)
    print("B3: Θ_{Z⁸} weight-4 reflection exact; raw trace NOT bar-even.")
    block4_rung_chart(wb)
    print("B4: rung = ln q exact; intrinsic per-step units pin-dependent "
          "(killed); pair/rung = ½ scale-free.")
    block5_keystone_moment(wb)
    print("B5: N(n) = (n−1)! = unit-Schwinger moment; c = ½ breaks "
          "n·N(n) = n! (conditional distinguisher).")
    block6_chart_disagreement(wb)
    print("B6: ln q − ℏ_q = (q−1)²/2 + O³ — step charts disagree away "
          "from q = 1.")

    wb.add_data("owner_premises", {
        "P1_scale_free_substrate":
            "\"substrate has a preferred scale q0\" is FALSE — q0 is just "
            "our LOCAL value. The substrate itself is scale-free; q0 is "
            "the locally realized value of the modulus, not a structural "
            "scale of the substrate. (owner, 2026-07-25)",
        "P2_computational_time":
            "proper-time is really only computational time. (owner, "
            "2026-07-25)",
        "tier": "owner-supplied framework premises — NOT derived; all "
                "conclusions conditional on them are so labelled",
    })
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
