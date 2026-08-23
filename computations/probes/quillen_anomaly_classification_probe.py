#!/usr/bin/env python3
"""quillen_anomaly_classification_probe.py — Quillen holomorphic anomaly as the
organizing principle for the corpus's exact-gate vs magnitude-leg split.

Bean qou-2nm8. Scope-(a), audit-only, NO FIT, nothing wired. The owner asked
"are we seeing Quillen's holomorphic anomaly?" against the uploaded
Alvarez-Gaumé–Moore–Vafa 1986 paper (AGMV: "Theta Functions, Modular
Invariance, and Strings", Commun. Math. Phys. 106, 1–40 (1986);
library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf). This probe grounds the answer rigorously.

TASK A — THE EXACT CURVATURE (formalize-first anchor, symbolic + numeric).
The corpus's verified genus-1 identity det'Δ(E_τ) = (Im τ)²·|η(τ)|⁴
(bring_polarized_epstein_determinant_probe.py, genus-1 EXACT validation) is
precisely a Quillen-norm object: |η(τ)|⁴ = |η(τ)²|² is ∂τ∂τ̄-flat (modulus
squared of a holomorphic function; η ≠ 0 on ℍ), so the full mixed Wirtinger
derivative is carried by the metric factor alone:

    ∂τ∂τ̄ log[(Im τ)²|η(τ)|⁴] = ∂τ∂τ̄ (2·log Im τ) = −1/(2·(Im τ)²)   (exact).

This is nonzero at every τ ∈ ℍ, hence det'Δ(E_τ) is NOT |f(τ)|² for any
holomorphic f — the theorem-level statement of Quillen's holomorphic anomaly
(AGMV Sect. 4, Eqs. (4.1)–(4.2); curvature form of the determinant line
bundle, Eqs. (4.17)–(4.18)) made quantitative with the exact coefficient
−1/2 against the hyperbolic form 1/(Im τ)². Verified: (i) symbolically in
sympy (Wirtinger operators ∂τ∂τ̄ = ¼(∂ₓ² + ∂ᵧ²) on 2·log y; independent-
variable flatness of log f(u) + log g(v)); (ii) numerically in mpmath by
finite-difference quarter-Laplacian of F(x,y) = log(y²|η(x+iy)|⁴) at the
Bring τ₀ = −0.5 + 0.186676i and at a generic τ, to ≥ 10 digits; anchored by
the closed form |η(i)| = Γ(1/4)/(2π^{3/4}).

TASK B — THE ANOMALY-CANCELLATION IDENTITY FOR t₅ (exact bookkeeping).
Write |η| in Petersson-invariant form: N(τ) := (Im τ)^{1/4}·|η(τ)| is
SL(2,ℤ)-invariant (η has weight 1/2; the anomaly factor is (Im τ)^{w/2} with
w = 1/2). Then, using Im(5τ) = 5·Im τ EXACTLY,

    |t₅(τ)| = |η(τ)/η(5τ)|⁶ = 5^{3/2} · (N(τ)/N(5τ))⁶.

The per-factor anomaly weights (Im τ)^{1/4} cancel in the ratio up to the
exact constant 5^{6/4} = 5^{3/2} = 5√5 — t₅ is a weight-0 holomorphic
modular function (anomaly-free), which is WHY it can take the exact rational
distinguished value t₅(τ₀) = −10 on the Bring class. Relation to the Fricke
125 = 5³ made precise: under W₅: τ ↦ −1/(5τ) the invariant norm satisfies
N(5·W₅τ) = N(τ) and N(W₅τ) = N(5τ) (S-invariance), so the norm-ratio
R := (N(τ)/N(5τ))⁶ obeys R(W₅τ) = 1/R(τ) and

    |t₅(τ)·t₅(W₅τ)| = (5^{3/2})² = 5³ = 125,

i.e. the Fricke constant 125 is exactly the SQUARE of the anomaly-
cancellation constant 5^{3/2}; on the W₅-fixed circle R = 1/R ⇒ R = 1 and
|t₅| ≡ 5^{3/2} = 5√5 — re-deriving the 2026-07-24 Fricke-circle invariant
from the anomaly bookkeeping alone.

TASK C — CLASSIFICATION TABLE (data). Each session/corpus object classified
as (a) weight-0 holomorphic sector (anomaly-free ⇒ exact distinguished
values possible), (b) Quillen norm / metric quantity (anomaly-carrying ⇒
point values are frame data, no distinguished holomorphic constant), or (c)
mixed. Cross-checks: the retracted 8.226 = m(5τ₀)³·m(τ₀) and the naive
2.922 = m(5τ₀)·m(τ₀) per-factor products are reproduced from
m(τ) = 1/(√(Im τ)·|η(τ)|²) — confirming those numbers are genus-1 Quillen
norms (class (b)).

Retroactive-explanation framing (audit doc): this classification ORGANIZES
the existing scope-(a) negatives (endpoint/polarization blindness; every
det'Δ magnitude probe's "no distinguished constant" outcome); it is NOT a
new no-go claim. The existing negatives stand on their own.

Exit 0 ⟺ all assertions pass. Witness:
quillen-anomaly-classification-probe.witness.json (audit-only).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sympy as sp  # noqa: E402
from mpmath import mp, mpc, mpf, pi, sqrt, gamma  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Reuse the committed validator's η and t₅ (consistency with the gate).
from tau_dictionary_hauptmodul_validator import dedekind_eta, t5  # noqa: E402


# ── Task A1: symbolic curvature (sympy, exact) ─────────────────────────────

def symbolic_curvature() -> dict:
    """∂τ∂τ̄ log[(Im τ)²|η|⁴] = −1/(2 y²), y = Im τ, exactly.

    (i) Metric part: with τ = x + iy the Wirtinger operators satisfy
        ∂τ∂τ̄ = ¼(∂ₓ² + ∂ᵧ²), and Im τ = y depends on y only, so
        ∂τ∂τ̄ (2 log Im τ) = ¼·∂ᵧ²(2 log y) = −1/(2y²).
    (ii) Holomorphic part: in the (τ, τ̄)-independent-variable formalism,
        log|η|⁴ = 2 log η(τ) + 2 log η̄(τ̄) and the mixed derivative of
        f(u) + g(v) in independent u, v vanishes identically (η ≠ 0 on ℍ,
        so the logarithm is locally well defined).
    """
    x, y = sp.symbols("x y", real=True, positive=True)

    # (i) quarter-Laplacian of the metric term 2·log(Im τ) = 2·log y.
    metric = 2 * sp.log(y)
    quarter_lap = sp.Rational(1, 4) * (sp.diff(metric, x, 2) + sp.diff(metric, y, 2))
    target = -1 / (2 * y**2)
    diff_metric = sp.simplify(quarter_lap - target)
    assert diff_metric == 0, f"metric curvature mismatch: {quarter_lap} vs {target}"

    # (ii) ∂∂̄-flatness of |holomorphic|² in independent variables (u, v):
    u, v = sp.symbols("u v")
    f = sp.Function("f")
    g = sp.Function("g")
    hol = 2 * sp.log(f(u)) + 2 * sp.log(g(v))
    mixed = sp.diff(hol, u, v)
    assert sp.simplify(mixed) == 0, f"|hol|^2 not del-delbar flat: {mixed}"

    # (iii) Wirtinger identity ∂τ∂τ̄ = ¼(∂ₓ²+∂ᵧ²) on a generic C² function:
    F = sp.Function("F")(x, y)
    # ∂τ = ½(∂ₓ − i∂ᵧ), ∂τ̄ = ½(∂ₓ + i∂ᵧ) acting on F(x, y):
    d_tau = sp.Rational(1, 2) * (sp.diff(F, x) - sp.I * sp.diff(F, y))
    d_tau_taubar = sp.Rational(1, 2) * (sp.diff(d_tau, x) + sp.I * sp.diff(d_tau, y))
    quarter_lap_F = sp.Rational(1, 4) * (sp.diff(F, x, 2) + sp.diff(F, y, 2))
    assert sp.simplify(d_tau_taubar - quarter_lap_F) == 0, "Wirtinger identity failed"

    return {
        "statement": "d_tau d_taubar log[(Im tau)^2 |eta(tau)|^4] = "
                     "d_tau d_taubar (2 log Im tau) = -1/(2 (Im tau)^2)  (exact)",
        "metric_part": "quarter-Laplacian of 2 log y = -1/(2 y^2), verified exact",
        "holomorphic_part": "mixed derivative of 2 log f(u) + 2 log g(v) in "
                            "independent (u, v) is identically 0 (|hol|^2 flat; "
                            "eta nonvanishing on H)",
        "wirtinger_identity": "d_tau d_taubar = (1/4)(d_xx + d_yy), verified on "
                              "generic F(x, y)",
        "consequence": "the curvature is nonzero at every tau in H, hence "
                       "det'Delta(E_tau) = (Im tau)^2 |eta|^4 is NOT |f(tau)|^2 "
                       "for any holomorphic f (Quillen holomorphic anomaly, AGMV "
                       "Sect. 4) — coefficient exactly -1/2 against 1/(Im tau)^2",
    }


# ── Task A2: numeric curvature (mpmath finite differences) ─────────────────

def _log_detprime(x: mpf, y: mpf) -> mpf:
    """F(x, y) = log[(Im τ)²|η(τ)|⁴] = 2 log y + 4 log|η(x+iy)|."""
    tau = mpc(x, y)
    return 2 * mp.log(y) + 4 * mp.log(abs(dedekind_eta(tau)))


def numeric_curvature(x0: mpf, y0: mpf) -> dict:
    """Quarter-Laplacian of F by mpmath finite differences vs −1/(2y²)."""
    with mp.workdps(mp.dps + 40):
        fxx = mp.diff(lambda x: _log_detprime(x, y0), x0, 2)
        fyy = mp.diff(lambda y: _log_detprime(x0, y), y0, 2)
        computed = (fxx + fyy) / 4
        expected = -1 / (2 * y0**2)
        rel = abs(computed - expected) / abs(expected)
    return {
        "tau": mp.nstr(mpc(x0, y0), 12),
        "quarter_laplacian": mp.nstr(computed, 20),
        "expected_-1/(2y^2)": mp.nstr(expected, 20),
        "rel_dev": mp.nstr(rel, 5),
        "_rel": rel,
    }


# ── Task B: the anomaly-cancellation identity for t₅ ───────────────────────

def petersson_norm(tau) -> mpf:
    """N(τ) = (Im τ)^{1/4}·|η(τ)| — the SL(2,ℤ)-invariant Petersson norm of
    the weight-1/2 form η."""
    return mp.im(tau) ** mpf("0.25") * abs(dedekind_eta(tau))


def symbolic_cancellation() -> None:
    """Exact bookkeeping: (y^{1/4} a / ((5y)^{1/4} b))⁶ · 5^{3/2} = (a/b)⁶,
    i.e. |t₅| = (a/b)⁶ = 5^{3/2}·(N(τ)/N(5τ))⁶ given Im(5τ) = 5·Im τ; and
    125 = (5^{3/2})² exactly."""
    y, a, b = sp.symbols("y a b", positive=True)
    lhs = 5 ** sp.Rational(3, 2) * ((y ** sp.Rational(1, 4) * a)
                                    / ((5 * y) ** sp.Rational(1, 4) * b)) ** 6
    rhs = (a / b) ** 6
    assert sp.simplify(lhs - rhs) == 0, "anomaly-cancellation bookkeeping failed"
    assert (5 ** sp.Rational(3, 2)) ** 2 == 125, "5^{3/2} squared is not 125"


def numeric_cancellation(tau) -> dict:
    """|t₅(τ)| = 5^{3/2}(N(τ)/N(5τ))⁶; Fricke |t₅(τ)t₅(W₅τ)| = 125;
    R(W₅τ)·R(τ) = 1; SL(2,ℤ)-invariance of N."""
    five32 = 5 * sqrt(5)
    N_tau, N_5tau = petersson_norm(tau), petersson_norm(5 * tau)
    R = (N_tau / N_5tau) ** 6
    t5_tau = t5(tau)
    dev_id = abs(abs(t5_tau) - five32 * R) / abs(t5_tau)

    w5 = -1 / (5 * tau)
    R_w5 = (petersson_norm(w5) / petersson_norm(5 * w5)) ** 6
    dev_recip = abs(R * R_w5 - 1)
    dev_fricke = abs(abs(t5_tau * t5(w5)) - 125)

    # SL(2,Z)-invariance of the Petersson norm (T and S):
    dev_T = abs(petersson_norm(tau + 1) - N_tau) / N_tau
    dev_S = abs(petersson_norm(-1 / tau) - N_tau) / N_tau
    return {
        "tau": mp.nstr(tau, 12),
        "abs_t5": mp.nstr(abs(t5_tau), 20),
        "5^{3/2}*R": mp.nstr(five32 * R, 20),
        "dev_identity": mp.nstr(dev_id, 5),
        "dev_R_reciprocal_under_W5": mp.nstr(dev_recip, 5),
        "dev_fricke_125": mp.nstr(dev_fricke, 5),
        "dev_petersson_T_invariance": mp.nstr(dev_T, 5),
        "dev_petersson_S_invariance": mp.nstr(dev_S, 5),
        "_devs": (dev_id, dev_recip, dev_fricke, dev_T, dev_S),
    }


# ── Task C: classification table (data; corpus cross-refs) ─────────────────

CLASSIFICATION = [
    {
        "object": "t5(tau) = (eta(tau)/eta(5 tau))^6",
        "class": "(a) weight-0 holomorphic modular function on X_0(5)",
        "why": "eta(tau)^6 and eta(5 tau)^6 are both weight-3 on Gamma_0(5); "
               "the quotient is weight 0 and holomorphic (eta nonvanishing); "
               "the (Im tau)^{1/4} anomaly factors cancel up to the exact "
               "constant 5^{3/2} (Task B). Anomaly-free => exact distinguished "
               "values possible: t5(tau_0) = -10 exactly on the Bring class.",
        "refs": ["content/quantum-observable-universe/lean/QOU/Archimedean/BringHauptmodulGate.lean",
                 "docs/audits/2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md"],
    },
    {
        "object": "j(tau)",
        "class": "(a) weight-0 holomorphic modular function on X(1)",
        "why": "hauptmodul of SL(2,Z); exact algebraic/rational values at "
               "distinguished (e.g. CM) points are the expected behavior of the "
               "anomaly-free sector.",
        "refs": ["docs/audits/2026-07-24-tau-dictionary-hauptmodul-gate-wiring.md"],
    },
    {
        "object": "Fricke pair (t5(tau_0), t5(W5 tau_0)) = (-10, -25/2), "
                  "product 125",
        "class": "(a) exact rational values of a weight-0 function",
        "why": "the Fricke relation t5(tau) * t5(-1/(5 tau)) = 125 is an "
               "identity of weight-0 holomorphic functions; 125 = (5^{3/2})^2 "
               "is exactly the square of the anomaly-cancellation constant "
               "(Task B).",
        "refs": ["docs/audits/2026-07-24-tau-dictionary-fricke-cusp-spin.md"],
    },
    {
        "object": "a_p integers (X_0(50)/50a newform Hecke data)",
        "class": "(a) holomorphic-sector arithmetic data",
        "why": "Fourier coefficients of a weight-2 HOLOMORPHIC newform: "
               "frame-independent integers, no metric/norm dependence anywhere "
               "in their definition.",
        "refs": ["docs/audits/2026-07-25-x050-50a-hecke-gate.md"],
    },
    {
        "object": "det'Delta(E_tau) = (Im tau)^2 |eta(tau)|^4",
        "class": "(b) Quillen norm (anomaly-carrying)",
        "why": "d_tau d_taubar log = -1/(2 (Im tau)^2) != 0 (Task A, exact): "
               "not |f|^2 for holomorphic f; point values are frame data of "
               "the Quillen metric on the determinant line, not distinguished "
               "holomorphic constants. AGMV Sect. 4 (Quillen theorem 4.1-4.2, "
               "curvature 4.17-4.18); the torus special case is AGMV Sect. 2 "
               "(the 'quadratic term in the exponent' obstruction below "
               "Eq. 2.3).",
        "refs": ["computations/alpha_em/bring_polarized_epstein_determinant_probe.py",
                 "docs/audits/2026-07-18-bring-polarized-epstein-determinant.md"],
    },
    {
        "object": "polarized Bring det'Delta measure sqrt(Vol)/sqrt(det'Delta) "
                  "= 1.38757991 (period tau_0 * M)",
        "class": "(b) Quillen-norm-type quantity (genus 4)",
        "why": "same object class as det'Delta(E_tau) one genus up: a "
               "zeta-regularized determinant norm on the determinant line over "
               "the Siegel family. Anomaly-carrying => no distinguished "
               "holomorphic constant expected at any single period point.",
        "refs": ["docs/audits/2026-07-19-bring-genus4-polarized-epstein-detprime.md"],
    },
    {
        "object": "product-period (unpolarized) genus-4 measure ~ 1.4724e12 "
                  "(#3934-lineage blow-up)",
        "class": "(b) Quillen-norm-type quantity (product frame)",
        "why": "the same determinant norm evaluated in the product-period "
               "frame; the ~12-orders separation from the polarized value "
               "lives in the genus-4 theta-factor — i.e. in the norm sector, "
               "not the holomorphic sector.",
        "refs": ["docs/audits/2026-07-19-bring-genus4-polarized-epstein-detprime.md"],
    },
    {
        "object": "per-factor measures m(tau_0), m(5 tau_0), "
                  "m(tau) = 1/(sqrt(Im tau) |eta(tau)|^2)",
        "class": "(b) genus-1 Quillen norms",
        "why": "m(tau) = det'Delta(E_tau)^{-1/2} * Vol^{1/2}: a norm of the "
               "genus-1 determinant line (reproduced numerically in this "
               "probe).",
        "refs": ["docs/audits/2026-07-18-bring-polarized-epstein-determinant.md"],
    },
    {
        "object": "8.226 = m(5 tau_0)^3 * m(tau_0) (retracted product)",
        "class": "(b) product of Quillen norms",
        "why": "product of per-factor norm data (and already retracted as the "
               "wrong object for the polarized determinant, 2026-07-18); "
               "doubly not a candidate distinguished constant.",
        "refs": ["docs/audits/2026-07-18-bring-polarized-epstein-determinant.md"],
    },
    {
        "object": "alpha_EM 1/(8 pi) loop weight (target)",
        "class": "(c) unresolved: proposed as a CURVATURE COEFFICIENT of the "
                 "determinant line (R2, owner-gated, propose-only)",
        "why": "anomaly/curvature coefficients in AGMV are rational multiples "
               "of 1/pi (counterterm (1/2 pi) int A_z A_zbar, Eq. 4.4/4.6; "
               "gravitational 1/(192 pi), Eq. 4.26-4.27) — a DERIVABLE object "
               "class (index density), unlike point values of norms. Proposal "
               "only; tautology risk stated in the audit doc; NOT computed "
               "here.",
        "refs": ["docs/audits/2026-07-25-quillen-anomaly-classification.md"],
    },
]


def main() -> None:
    set_compute_dps()
    wb = WitnessBuilder("quillen-anomaly-classification-probe",
                        engine="mpmath+sympy")

    tau0 = mpc(mpf("-0.5"), mpf("0.186676"))   # BDH22 Sect. 2.2 Bring modulus
    tau_gen = mpc(mpf("0.31"), mpf("1.17"))    # generic interior point

    # ── Task A1: symbolic ──────────────────────────────────────────────────
    sym = symbolic_curvature()
    print("Task A1 (symbolic):", sym["statement"])
    wb.add_assertion(
        "curvature_symbolic_exact_residual",
        computed="0",
        expected="0",
        source="sympy exact residuals: quarter-Laplacian(2 log y) - "
               "(-1/(2y^2)) = 0; mixed d_u d_v [2 log f(u) + 2 log g(v)] = 0; "
               "Wirtinger d_tau d_taubar = (1/4)(d_xx + d_yy) verified. "
               "Statement: d_tau d_taubar log[(Im tau)^2 |eta|^4] = "
               "-1/(2 (Im tau)^2) exactly",
    )

    # ── Task A2: numeric (both points, >= 10 digits) ───────────────────────
    num_results = []
    for tau in (tau0, tau_gen):
        r = numeric_curvature(mp.re(tau), mp.im(tau))
        rel = r.pop("_rel")
        num_results.append(r)
        print(f"Task A2 at tau = {r['tau']}: quarter-Laplacian = "
              f"{r['quarter_laplacian']}, rel dev = {r['rel_dev']}")
        assert rel < mpf("1e-10"), f"numeric curvature at {r['tau']}: rel {rel}"
        wb.add_assertion(
            f"curvature_numeric_{r['tau']}",
            computed=r["quarter_laplacian"],
            expected=r["expected_-1/(2y^2)"],
            tolerance=1e-10,
            source="mpmath finite-difference quarter-Laplacian of "
                   "log[(Im tau)^2 |eta|^4]",
        )

    # η(i) closed-form anchor: |η(i)| = Γ(1/4)/(2 π^{3/4}).
    eta_i = abs(dedekind_eta(mpc(0, 1)))
    eta_i_exact = gamma(mpf(1) / 4) / (2 * pi ** mpf("0.75"))
    dev_eta_i = abs(eta_i - eta_i_exact) / eta_i_exact
    assert dev_eta_i < mpf("1e-40"), f"eta(i) anchor off: {dev_eta_i}"
    wb.add_assertion("eta_i_closed_form", computed=mp.nstr(eta_i, 30),
                     expected=mp.nstr(eta_i_exact, 30), tolerance=1e-40,
                     source="|eta(i)| = Gamma(1/4)/(2 pi^{3/4})")

    # ── Task B: cancellation identity ──────────────────────────────────────
    symbolic_cancellation()
    canc_results = []
    all_devs: list = []
    for tau in (tau0, tau_gen):
        r = numeric_cancellation(tau)
        devs = r.pop("_devs")
        canc_results.append(r)
        print(f"Task B at tau = {r['tau']}: |t5| = {r['abs_t5']}, "
              f"5^(3/2)*R = {r['5^{3/2}*R']}, dev = {r['dev_identity']}")
        for name, d in zip(("identity", "R-reciprocal", "fricke-125",
                            "petersson-T", "petersson-S"), devs):
            assert d < mpf("1e-40"), f"{name} at {r['tau']}: dev {d}"
        all_devs.append(devs)
    wb.add_assertion(
        "anomaly_cancellation_t5_max_dev",
        computed=float(max(d[0] for d in all_devs)),
        expected=0.0,
        tolerance=1e-40,
        source="|t5(tau)| = 5^(3/2) * (N(tau)/N(5 tau))^6, N = (Im tau)^(1/4) "
               "|eta| SL(2,Z)-invariant (T/S invariance asserted < 1e-40): "
               "the (Im tau)^{1/4} anomaly factors cancel exactly up to "
               "5^{3/2}; sympy bookkeeping identity asserted exact",
    )
    wb.add_assertion(
        "fricke_125_is_square_of_cancellation_constant_max_dev",
        computed=float(max(max(d[1], d[2]) for d in all_devs)),
        expected=0.0,
        tolerance=1e-40,
        source="R(W5 tau) = 1/R(tau) and |t5(tau) * t5(W5 tau)| = 125 = "
               "(5^(3/2))^2 via S-invariance of N: the Fricke constant is "
               "exactly the square of the anomaly-cancellation constant",
    )

    # W5 fixed point: |t5(i/sqrt5)| = 5^{3/2} (R = 1 there).
    fp = mpc(0, 1 / sqrt(5))
    dev_fp = abs(t5(fp) - 5 * sqrt(5))
    assert dev_fp < mpf("1e-40"), f"fixed-point value off: {dev_fp}"
    wb.add_assertion("w5_fixed_point_value_dev", computed=float(dev_fp),
                     expected=0.0, tolerance=1e-40,
                     source="t5(i/sqrt5) = 5 sqrt(5); R = 1 at the W5 fixed "
                            "point => |t5| = 5^(3/2): the 2026-07-24 "
                            "Fricke-circle invariant re-derived from anomaly "
                            "bookkeeping")

    # ── Task C: per-factor Quillen norms reproduce the retracted products ──
    def m_measure(tau):
        return 1 / (sqrt(mp.im(tau)) * abs(dedekind_eta(tau)) ** 2)

    m_t0, m_5t0 = m_measure(tau0), m_measure(5 * tau0)
    prod_naive = m_5t0 * m_t0
    prod_8226 = m_5t0 ** 3 * m_t0
    print(f"Task C: m(tau_0) = {mp.nstr(m_t0, 10)}, m(5 tau_0) = "
          f"{mp.nstr(m_5t0, 10)}, m*m = {mp.nstr(prod_naive, 8)}, "
          f"m^3*m = {mp.nstr(prod_8226, 8)}")
    assert abs(prod_naive - mpf("2.922")) < mpf("5e-3"), \
        f"naive product drifted from corpus print 2.922: {prod_naive}"
    assert abs(prod_8226 - mpf("8.226")) < mpf("5e-3"), \
        f"8.226 product drifted from corpus print: {prod_8226}"
    wb.add_assertion("naive_product_m5t0_mt0", computed=float(prod_naive),
                     expected=2.922, tolerance=5e-3,
                     source="m(5 tau_0)*m(tau_0), m(tau) = 1/(sqrt(Im tau) "
                            "|eta|^2): corpus print 2.922 (2026-07-18 "
                            "retraction audit) — product of genus-1 Quillen "
                            "norms, class (b)")
    wb.add_assertion("retracted_8226_product", computed=float(prod_8226),
                     expected=8.226, tolerance=5e-3,
                     source="m(5 tau_0)^3*m(tau_0): the retracted 8.226 is a "
                            "product of genus-1 Quillen norms — class (b), "
                            "frame data, not a candidate distinguished "
                            "constant")

    # ── witness ────────────────────────────────────────────────────────────
    wb.set_description(
        "Quillen holomorphic anomaly classification (bean qou-2nm8). TASK A: "
        "the corpus's verified genus-1 identity det'Delta(E_tau) = "
        "(Im tau)^2 |eta|^4 has Quillen curvature d_tau d_taubar log = "
        "-1/(2 (Im tau)^2) EXACTLY (sympy symbolic: metric part carries all "
        "of it, |eta|^4 is del-delbar flat as |holomorphic|^2; mpmath "
        "finite-difference quarter-Laplacian confirms to >= 10 digits at the "
        "Bring tau_0 and a generic tau) — det'Delta is NOT |f|^2 for "
        "holomorphic f, the quantitative form of AGMV Sect. 4 (Quillen "
        "theorem Eqs. 4.1-4.2, curvature 4.17-4.18; torus obstruction AGMV "
        "Sect. 2 below Eq. 2.3). TASK B: in t5 = (eta/eta(5.))^6 the "
        "weight-1/2 anomaly factors (Im tau)^{1/4} cancel EXACTLY up to "
        "5^{3/2} = 5 sqrt(5): |t5| = 5^{3/2} (N(tau)/N(5 tau))^6 with "
        "N = (Im tau)^{1/4}|eta| the SL(2,Z)-invariant Petersson norm; the "
        "Fricke 125 = 5^3 is exactly the SQUARE of the cancellation "
        "constant, and on the W5-fixed circle the norm-ratio is 1 => "
        "|t5| = 5 sqrt(5), re-deriving the 2026-07-24 circle invariant. "
        "TASK C: classification table — exact gates (t5 = -10, Fricke "
        "-25/2, j, a_p) are weight-0 holomorphic-sector (anomaly-free, "
        "class a); every stuck magnitude leg (det'Delta(E_tau), polarized "
        "Bring 1.38758, product-period 1.4724e12, per-factor m's, the "
        "retracted 8.226 — reproduced here from genus-1 Quillen norms) is "
        "an anomaly-carrying norm (class b). Organizing principle for the "
        "existing scope-(a) negatives; NOT a new no-go. NO FIT; nothing "
        "wired; audit-only."
    )
    wb.set_audit_only("docs/audits/2026-07-25-quillen-anomaly-classification.md")
    wb.add_data("task_a_symbolic", sym)
    wb.add_data("task_a_numeric", num_results)
    wb.add_data("task_b_cancellation", {
        "identity": "|t5(tau)| = 5^(3/2) * (N(tau)/N(5 tau))^6, "
                    "N(tau) = (Im tau)^(1/4) |eta(tau)| SL(2,Z)-invariant",
        "constant": "5^(3/2) = 5 sqrt(5) = sqrt(125); Fricke 125 = 5^3 = "
                    "(5^(3/2))^2; Im(5 tau) = 5 Im tau is the entire "
                    "bookkeeping",
        "per_point": canc_results,
    })
    wb.add_data("task_c_classification_table", CLASSIFICATION)
    wb.add_data("agmv_reference", {
        "citation": "L. Alvarez-Gaume, G. Moore, C. Vafa, 'Theta Functions, "
                    "Modular Invariance, and Strings', Commun. Math. Phys. "
                    "106, 1-40 (1986)",
        "upload": "library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf",
        "key_locations": {
            "Sect. 2": "torus spin structures; Det(theta,phi) = "
                       "theta[](0|tau)/eta(tau) (Eq. 2.3); the holomorphic "
                       "anomaly first exhibited (quadratic exponent term)",
            "Sect. 4": "Holomorphic Factorization: Quillen theorem "
                       "(4.1)-(4.2); counterterm (1/2 pi) int A_z A_zbar "
                       "(4.4)/(4.6); determinant-line curvature "
                       "(4.17)-(4.18) with Bismut-Freed; Belavin-Knizhnik "
                       "1/(192 pi) (4.26)-(4.27); Weil-Petersson form "
                       "(4.30)-(4.32)",
            "Sect. 5": "chiral Dirac determinant detD+D(u) = "
                       "e^{...}|g(u)|^2, g = const * theta[a,b](u|Omega) "
                       "(5.1)-(5.4)",
        },
    })
    wb.save()
    print("\nwitness saved; all assertions passed.")


if __name__ == "__main__":
    main()
