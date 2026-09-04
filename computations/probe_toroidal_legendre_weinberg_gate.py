# Status: EXPLORATORY (gate probe; per local/production-vs-exploratory-discipline).
"""Toroidal-Legendre Weinberg gate (bean c4uz) — derive-first GATE probe.

Question (Gate 1 of docs/audits/2026-07-06-toroidal-legendre-gates.md):
does the Weinberg cosh-vs-cos +1.1% gap — the deviation of the categorical
torus-knot trace ratio

    P_W / P_Z = cosh(5 eta_0) / cosh(7 eta_0)          (eta_0 = ln q_0)

from the SM value cos theta_W = m_W / m_Z — reduce to a toroidal-Legendre
identity, i.e. does the torus-saddle steepest-descent evaluation of the
T(2,k) trace ratio produce, AS A DERIVED CORRECTION, a ratio of toroidal
Legendre functions

    Q_{nu-1/2}(cosh eta_0),
    Q_{n-1/2}(cosh eta)
      = int_0^pi cos(n psi) dpsi / sqrt(2 (cosh eta - cos psi))     (Heine)

in place of the bare cosh ratio?

DERIVE-FIRST DISCIPLINE (compute-author §3.3 formalize-first): this script
evaluates ONLY what the derivation prescribes. No index/argument scanning.

Derivation result (full write-up in the audit doc §Gate 1):

(A) EXACTNESS INVARIANT. The trace polynomial P_m(h) = tr_M(sigma_1^{2m})
    is an EXACT identity in H_2(q) (corpus: PR #1125, sympy-exact m=1..6;
    re-verified symbolically below for m=2,3):

        P_m(h) = sum_{j=0}^{m} C(m+j, 2j)/2 * h^{2j}
               = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q),   h = q - q^{-1}.

    A steepest-descent "correction" presupposes an asymptotic approximation
    of an integral/sum with a large parameter. The N=2 Markov-trace ratio
    P_W/P_Z has neither: it is a finite exact Laurent-rational function of
    q evaluated at q_0. There is no residual series in which Q_{nu-1/2}
    could appear as a derived correction term. The Askey two-saddle table
    (torus saddle <-> Rogers q-ultraspherical; content block
    self-dual-higgs-real-volume.md) lives at the COLORED / large-N level
    (colored-Jones asymptotics), one level above the N=2 trace used in the
    W/Z identity — its saddle corrections correct J_N asymptotics, not the
    exact H_2 trace.

(B) MONOTONICITY PRUNE (structural exclusion of the same-index bare
    replacement, invariant cited per AGENTS.md §Before declaring refuted,
    scope (b)). For x > 1 the Laplace/Heine representation (DLMF 14.12.4)

        Q_nu(x) = int_0^inf dt / (x + sqrt(x^2-1) cosh t)^{nu+1},  nu > -1,

    has integrand base x + sqrt(x^2-1) cosh t >= x + sqrt(x^2-1) > 1 for
    all t >= 0, so the integrand is strictly decreasing in nu pointwise;
    hence Q_nu(x) is STRICTLY DECREASING in the degree nu. Therefore

        Q_{5-1/2}(cosh eta_0) / Q_{7-1/2}(cosh eta_0) > 1   for every eta_0 > 0,

    while both targets — the categorical cosh ratio (~0.8908) and the SM
    cos theta_W (~0.8815) — are < 1. The same-index bare-replacement
    sub-class is structurally excluded. (Scope-limited: this does NOT
    exclude toroidal-Legendre objects appearing elsewhere, e.g. at the
    colored/large-N saddle where the Askey table actually operates.)

VERDICT: no-reduction found (gate closed for now) — an honest stop, NOT a
refutation of toroidal-Legendre machinery generally.

Item 3 (observation tier): the one legitimate unconditional evaluation —
the bare ratio Q_{5-1/2}(cosh eta_0) / Q_{7-1/2}(cosh eta_0), single
prescribed evaluation at 50 dps, reported with its deviation vs both the
categorical 0.8908 and the SM 0.8815. One number each, no variants.

Cross-checks (all at 50-dps floor, tolerance 1e-40 << the 1e-25 minimum):
  * mpmath.legenq(nu, 0, x, type=3) vs the Heine/Fourier integral rep
    vs the Laplace integral rep — three independent routes per nu.
  * sympy-exact closed-form verification of P_m for m=2 (W) and m=3 (Z).

Runtime: ~5 s. Witness: probe-toroidal-legendre-weinberg-gate.witness.json
(audit-only; report = docs/audits/2026-07-06-toroidal-legendre-gates.md).
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge for substrate/ modules

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# SM mass measurements (PDG 2022) — same literals as the corpus precedent
# rt_route_cross_particle_ratio_quantum_dim.py (exploratory tier; PDG values
# are not in codata_constants / experimental_constants as of this probe).
M_W_GEV = mp.mpf("80.379")
M_Z_GEV = mp.mpf("91.1876")

TOL_XCHECK = 1e-40  # 50-dps floor demands <= 1e-25; we hold 1e-40


# ── Symbolic layer: exact trace closed form (derivation anchor A) ────────


def trace_poly_binomial(m: int, h: sp.Symbol) -> sp.Expr:
    """P_m(h) = sum_{j=0}^m C(m+j,2j)/2 * h^{2j}  (PR #1125 binomial pattern)."""
    return sum(sp.binomial(m + j, 2 * j) * sp.Rational(1, 2) * h ** (2 * j)
               for j in range(m + 1))


def trace_poly_closed(m: int, q: sp.Symbol) -> sp.Expr:
    """P_m = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q),  [2]_q = q + q^{-1}."""
    return (q ** (2 * m + 1) + q ** (-(2 * m + 1))) / (2 * (q + 1 / q))


def verify_closed_form(m: int) -> bool:
    """sympy-exact: binomial form at h = q - q^{-1} equals the closed form."""
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q
    diff = sp.simplify(trace_poly_binomial(m, h) - trace_poly_closed(m, q))
    return diff == 0


def verify_bracket_cancellation() -> bool:
    """sympy-exact: P_2/P_3 = (q^5 + q^-5)/(q^7 + q^-7) — the [2]_q cancels."""
    q = sp.Symbol("q", positive=True)
    ratio = sp.simplify(
        trace_poly_closed(2, q) / trace_poly_closed(3, q)
        - (q ** 5 + q ** -5) / (q ** 7 + q ** -7)
    )
    return ratio == 0


# ── Numeric layer: toroidal Legendre Q_{nu-1/2} at 50 dps ────────────────


def q_toroidal_legenq(nu, x):
    """Q_nu(x) via mpmath.legenq type=3 (real-valued on (1, inf))."""
    val = mp.legenq(nu, 0, x, type=3)
    assert abs(mp.im(val)) < mp.mpf(10) ** (-(mp.mp.dps - 5)), \
        f"legenq type=3 returned non-real value at nu={nu}"
    return mp.re(val)


def q_toroidal_heine(n: int, x):
    """Heine/Fourier rep: Q_{n-1/2}(x) = int_0^pi cos(n psi)/sqrt(2(x - cos psi)) dpsi."""
    return mp.quad(lambda psi: mp.cos(n * psi) / mp.sqrt(2 * (x - mp.cos(psi))),
                   [0, mp.pi])


def q_toroidal_laplace(nu, x):
    """Laplace rep (DLMF 14.12.4): Q_nu(x) = int_0^inf (x + sqrt(x^2-1) cosh t)^{-nu-1} dt."""
    s = mp.sqrt(x * x - 1)
    return mp.quad(lambda t: (x + s * mp.cosh(t)) ** (-(nu + 1)), [0, mp.inf])


def main() -> int:
    t0 = time.monotonic()
    w = (
        WitnessBuilder("probe-toroidal-legendre-weinberg-gate", engine="mpmath")
        .set_description(
            "Gate 1 (bean c4uz): does the Weinberg cosh-vs-cos +1.1% gap reduce "
            "to a toroidal-Legendre Q_{nu-1/2} torus-saddle identity? Derive-first "
            "gate — verdict: no-reduction found (gate closed for now). The N=2 "
            "trace ratio is EXACT (no saddle-correction series exists), and the "
            "same-index replacement Q_{9/2}/Q_{13/2} is structurally excluded by "
            "degree-monotonicity of Q_nu (Laplace rep, DLMF 14.12.4): the Q-ratio "
            "is > 1 for every eta_0 > 0 while both targets are < 1. Includes the "
            "one prescribed observation-tier evaluation (item 3)."
        )
        .set_audit_only("docs/audits/2026-07-06-toroidal-legendre-gates.md")
    )

    # ── Derivation anchor A: exact closed form (symbolic, no floats) ──
    ok_m2 = verify_closed_form(2)  # W = T(2,4): 2m+1 = 5
    ok_m3 = verify_closed_form(3)  # Z = T(2,6): 2m+1 = 7
    ok_cancel = verify_bracket_cancellation()
    w.add_assertion(
        "closed_form_P2_sympy_exact (W = T(2,4))",
        computed=str(ok_m2), expected="True",
        source="PR #1125 binomial pattern, re-verified: sum C(2+j,2j)/2 h^{2j} = (q^5+q^-5)/(2[2]_q)",
    )
    w.add_assertion(
        "closed_form_P3_sympy_exact (Z = T(2,6))",
        computed=str(ok_m3), expected="True",
        source="PR #1125 binomial pattern, re-verified: sum C(3+j,2j)/2 h^{2j} = (q^7+q^-7)/(2[2]_q)",
    )
    w.add_assertion(
        "bracket_cancellation_P2_over_P3",
        computed=str(ok_cancel), expected="True",
        source="sympy-exact: P_2/P_3 = (q^5+q^-5)/(q^7+q^-7); [2]_q cancels",
    )

    # ── Substrate evaluation ──
    q0 = mp.mpf(Q_50_DIGIT_STR)
    eta0 = mp.log(q0)
    x0 = mp.cosh(eta0)

    cosh_ratio = mp.cosh(5 * eta0) / mp.cosh(7 * eta0)  # categorical P_W/P_Z
    sm_ratio = M_W_GEV / M_Z_GEV                        # cos theta_W = m_W/m_Z

    # trace-polynomial ratio at q_0 must equal the cosh ratio exactly
    p2_at_q0 = (q0 ** 5 + q0 ** -5) / (2 * (q0 + 1 / q0))
    p3_at_q0 = (q0 ** 7 + q0 ** -7) / (2 * (q0 + 1 / q0))
    w.add_assertion(
        "trace_ratio_equals_cosh_ratio_at_q0",
        computed=mp.nstr(p2_at_q0 / p3_at_q0, 45),
        expected=mp.nstr(cosh_ratio, 45),
        tolerance=TOL_XCHECK,
        source="P_2/P_3 at q_0 vs cosh(5 eta_0)/cosh(7 eta_0); eta_0 = ln q_0",
    )

    # ── Item 3: the ONE prescribed toroidal-Legendre evaluation ──
    # nu = 5, 7 mirrors P_W/P_Z = cosh(5 eta_0)/cosh(7 eta_0):
    # Q_{5-1/2}(cosh eta_0) / Q_{7-1/2}(cosh eta_0). No variants.
    nu5 = mp.mpf("4.5")   # 5 - 1/2
    nu7 = mp.mpf("6.5")   # 7 - 1/2

    q5_legenq = q_toroidal_legenq(nu5, x0)
    q7_legenq = q_toroidal_legenq(nu7, x0)
    q5_heine = q_toroidal_heine(5, x0)
    q7_heine = q_toroidal_heine(7, x0)
    q5_laplace = q_toroidal_laplace(nu5, x0)
    q7_laplace = q_toroidal_laplace(nu7, x0)

    for nm, a, b in (
        ("Q_9/2 legenq_vs_heine", q5_legenq, q5_heine),
        ("Q_9/2 legenq_vs_laplace", q5_legenq, q5_laplace),
        ("Q_13/2 legenq_vs_heine", q7_legenq, q7_heine),
        ("Q_13/2 legenq_vs_laplace", q7_legenq, q7_laplace),
    ):
        w.add_assertion(
            f"xcheck_{nm}",
            computed=mp.nstr(a, 45), expected=mp.nstr(b, 45),
            tolerance=TOL_XCHECK,
            source="three independent representations (legenq type=3 / Heine Fourier / Laplace DLMF 14.12.4)",
        )

    q_ratio = q5_legenq / q7_legenq

    # ── Derivation anchor B: monotonicity invariant ──
    # Q_nu(x) strictly decreasing in nu for x > 1 (Laplace rep, base > 1
    # pointwise) => Q_{9/2}/Q_{13/2} > 1 for every eta_0 > 0, while both
    # targets are < 1. Witness the invariant at the substrate point.
    w.add_assertion(
        "monotonicity_invariant_Q92_gt_Q132",
        computed=str(bool(q5_legenq > q7_legenq)), expected="True",
        source="Q_nu(x) strictly decreasing in nu for x>1 (DLMF 14.12.4 integrand base > 1)",
    )
    w.add_assertion(
        "gate_exclusion_q_ratio_gt_1_targets_lt_1",
        computed=str(bool(q_ratio > 1 and cosh_ratio < 1 and sm_ratio < 1)),
        expected="True",
        source="same-index bare replacement structurally excluded: Q-ratio > 1, both targets < 1",
    )

    # ── Observation-tier numbers (item 3 deliverable) ──
    dev_vs_categorical = q_ratio / cosh_ratio - 1
    dev_vs_sm = q_ratio / sm_ratio - 1
    dev_cosh_vs_sm = cosh_ratio / sm_ratio - 1  # the +1.1% gap itself

    w.add_parameter("q0", mp.nstr(q0, 50))
    w.add_parameter("eta0 = ln q0", mp.nstr(eta0, 50))
    w.add_parameter("cosh_eta0 (argument of Q_{nu-1/2})", mp.nstr(x0, 50))
    w.add_parameter("compute_dps", mp.mp.dps)
    w.add_parameter("m_W_GeV (PDG 2022)", str(M_W_GEV))
    w.add_parameter("m_Z_GeV (PDG 2022)", str(M_Z_GEV))

    w.add_data("categorical_cosh_ratio_P_W_over_P_Z", mp.nstr(cosh_ratio, 50))
    w.add_data("sm_cos_theta_W_mW_over_mZ", mp.nstr(sm_ratio, 50))
    w.add_data("gap_cosh_vs_sm_rel", mp.nstr(dev_cosh_vs_sm, 30))
    w.add_data("Q_9_2_at_cosh_eta0", mp.nstr(q5_legenq, 50))
    w.add_data("Q_13_2_at_cosh_eta0", mp.nstr(q7_legenq, 50))
    w.add_data("toroidal_legendre_ratio_nu5_over_nu7", mp.nstr(q_ratio, 50))
    w.add_data("deviation_vs_categorical_cosh_ratio_rel", mp.nstr(dev_vs_categorical, 30))
    w.add_data("deviation_vs_sm_cos_theta_W_rel", mp.nstr(dev_vs_sm, 30))
    w.add_data("verdict", "no-reduction found (gate closed for now)")
    w.add_data(
        "verdict_scope",
        "Scope-limited stop, NOT a general refutation of toroidal-Legendre "
        "machinery. Excluded (scope (b), invariant cited): the same-index bare "
        "replacement Q_{5-1/2}/Q_{7-1/2} for cosh(5 eta_0)/cosh(7 eta_0), by "
        "degree-monotonicity of Q_nu at fixed argument > 1. Not excluded: "
        "toroidal-Legendre structures at the colored/large-N saddle level "
        "(where the Askey two-saddle table actually operates), or index "
        "assignments derived from a future colored-level analysis.",
    )
    w.add_caveat(
        "The N=2 trace ratio P_W/P_Z is exact (no asymptotic series), so no "
        "steepest-descent correction applies at this level; the 1.1% gap is "
        "not addressed by this gate."
    )

    path = w.save()
    dt = time.monotonic() - t0

    print(f"\n=== Gate 1 (bean c4uz): toroidal-Legendre Weinberg gate ===")
    print(f"  eta_0                          = {mp.nstr(eta0, 20)}")
    print(f"  categorical cosh(5e)/cosh(7e)  = {mp.nstr(cosh_ratio, 20)}")
    print(f"  SM cos theta_W = m_W/m_Z       = {mp.nstr(sm_ratio, 20)}")
    print(f"  gap (cosh vs SM)               = {mp.nstr(100*dev_cosh_vs_sm, 6)} %")
    print(f"  Q_9/2(cosh eta_0)              = {mp.nstr(q5_legenq, 20)}")
    print(f"  Q_13/2(cosh eta_0)             = {mp.nstr(q7_legenq, 20)}")
    print(f"  Q-ratio (nu=5 / nu=7)          = {mp.nstr(q_ratio, 20)}")
    print(f"  deviation vs categorical       = {mp.nstr(100*dev_vs_categorical, 6)} %")
    print(f"  deviation vs SM                = {mp.nstr(100*dev_vs_sm, 6)} %")
    print(f"  VERDICT: no-reduction found (gate closed for now)")
    print(f"  wall: {dt:.1f} s; witness: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
