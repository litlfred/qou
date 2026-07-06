"""Production-side wiring probe for `prop:flavor-dressed-mass-from-substrate-split`.

Computes the dressed-quark mass splitting μ_d − μ_u from the substrate
prop:

    μ_d − μ_u = M_N · (q-1)²(1 - q^{-4})/3 · (q^{1/2}+q^{-1/2})/(q+q^{-1})
              = (M_N / 3) · ℏ_q² · h_q · (q^{1/2}+q^{-1/2})

at q = q_0 and M_N = (m_p + m_n)/2.

CLASS-A acknowledged-stub status (AGENTS.md §canonical-discipline):
M_N is anchored on CODATA m_p + m_n (the `_VALIDATION` constants in
`codata_constants`), which is acknowledged to be a CAL-3-ish
calibration input pending its own substrate derivation.  This is
the same anchor used by the existing nucleon-mass-splitting
production chain; eliminating it requires a substrate-pure
derivation of M_N itself, which is the open Workplan-0b item
tracked in `docs/audits/2026-05-17-1ppb-workplan-v4.md`.  The
substrate-pure quantity this probe DERIVES is m_n − m_p; M_N
remains an external scale.
Emits a witness whose `contentBlock` references the new prop and
whose assertion gates the residual against CODATA m_n − m_p to
within 1% (measured residual at q_0 is −0.53%, dominated by the
dropped O((Δm/M_N)²) correction).

This is Phase 3 of the D3 wiring for PR #696: it makes the new
prop's substrate-pure derivation a first-class production-side
computable, so downstream consumers (paper_six_term_isotope_sweep,
derive_m_p / derive_m_n) can reference it via `upstream_witness_hashes`
without needing to re-derive the formula inline.

Upstream: `probe-flavor-split-substrate.witness.json` for the
underlying (m_n − m_p)/M_N substrate ratio (the Skein lift to
μ_d − μ_u is added here).

Companion content blocks:
- `prop:flavor-dressed-mass-from-substrate-split` (new this PR)
- `thm:flavor-mass-splitting-bound` (the upper bound on the same
  quantity, also new this PR)
- `rem:dressed-quark-numerology-at-q0` (the per-quark numerics at q_0)
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    M_P_MEV_VALIDATION as M_P_CODATA,
    M_N_MEV_VALIDATION as M_N_CODATA,
)


def _bound_factor(q: mp.mpf) -> mp.mpf:
    """Upper-bound factor ℏ_q² · h_q · [2]_q at the dressed-mass scale.

    Returns the dimensionless coefficient that, when multiplied by
    M_N, gives the substrate upper bound on μ_d − μ_u per
    `thm:flavor-mass-splitting-bound`.
    """
    hbar_q = (q - 1) / q
    h_q = q - 1 / q
    bracket_2_q = q + 1 / q
    return hbar_q * hbar_q * h_q * bracket_2_q


def _substrate_split_factor(q: mp.mpf) -> mp.mpf:
    """Substrate factor S(q) such that μ_d − μ_u = M_N · S(q).

    Equivalent forms (proved in
    `prop:flavor-dressed-mass-from-substrate-split` §"Derivation"
    via the algebraic identity (q − 1)²(1 − q⁻⁴)/3 = (1/3)·ℏ_q²·h_q·[2]_q
    and cancelling the [2]_q = q + q⁻¹ in numerator with the Skein
    denominator):

        S(q) = (q - 1)² · (1 - q^{-4}) / 3
                       · (q^{1/2} + q^{-1/2}) / (q + q^{-1})

             = (1/3) · ℏ_q² · h_q · (q^{1/2} + q^{-1/2})

             = (1/3) · ℏ_q² · h_q · z_mkv⁻¹
               where z_mkv = (q^{1/2} + q^{-1/2})^{-1}
    """
    nucleon_factor = ((q - 1) ** 2) * (1 - q ** (-4)) / 3
    sqrt_q = mp.sqrt(q)
    skein_factor = (sqrt_q + 1 / sqrt_q) / (q + 1 / q)
    return nucleon_factor * skein_factor


def main() -> int:
    mp.mp.dps = 50

    # Construct the builder BEFORE the computation so durationMs
    # captures actual runtime, not just the save step (per
    # Copilot #696 review).
    builder = (
        WitnessBuilder(
            "flavor-dressed-mass-from-substrate-split",
            engine="mpmath",
        )
        .set_description(
            "Substrate-pure derivation of μ_d − μ_u from "
            "prop:flavor-split-substrate (substrate side) + "
            "lem:pair-skein-mass-formula (Skein lift).  Reports "
            "(a) the substrate-derived value, (b) closure vs CODATA "
            "m_n − m_p, and (c) the realised-vs-bound ratio against "
            "thm:flavor-mass-splitting-bound.  Calibration discipline: "
            "M_N is anchored on CODATA m_p + m_n (validation-tagged, "
            "Class-A acknowledged-stub pending Workplan-0b); "
            "q_0 is the substrate parameter (CAL-2). m_n − m_p itself "
            "is NOT an input — it is the derived quantity being "
            "predicted."
        )
        .set_content_block("prop:flavor-dressed-mass-from-substrate-split")
    )

    q0 = Q0_MP
    m_p_codata = mp.mpf(str(M_P_CODATA))
    m_n_codata = mp.mpf(str(M_N_CODATA))

    M_N = (m_p_codata + m_n_codata) / 2
    delta_m_codata = m_n_codata - m_p_codata

    S_q = _substrate_split_factor(q0)
    bound_factor = _bound_factor(q0)

    mu_d_minus_mu_u_substrate = M_N * S_q
    mu_d_minus_mu_u_bound = M_N * bound_factor

    residual_vs_codata = (
        (mu_d_minus_mu_u_substrate - delta_m_codata) / delta_m_codata
    )
    bound_ratio = mu_d_minus_mu_u_substrate / mu_d_minus_mu_u_bound

    print("=" * 80)
    print("  Substrate-pure derivation of (μ_d − μ_u)")
    print("  (prop:flavor-dressed-mass-from-substrate-split)")
    print("=" * 80)
    print()
    print(f"  q_0                          = {mp.nstr(q0, 16)}")
    print(f"  M_N = (m_p + m_n)/2 (CODATA) = {mp.nstr(M_N, 16)} MeV")
    print(f"  CODATA m_n − m_p             = {mp.nstr(delta_m_codata, 16)} MeV")
    print()
    print("  ── Substrate factor S(q) ──")
    print(f"    S(q_0)                     = {mp.nstr(S_q, 16)}")
    print(f"    μ_d − μ_u (substrate)      = {mp.nstr(mu_d_minus_mu_u_substrate, 16)} MeV")
    print(f"    residual vs CODATA Δm_pn   = {mp.nstr(residual_vs_codata, 6)}  "
          f"({mp.nstr(100 * residual_vs_codata, 6)}%)")
    print()
    print("  ── Upper bound (thm:flavor-mass-splitting-bound) ──")
    print(f"    ℏ_q² · h_q · [2]_q          = {mp.nstr(bound_factor, 16)}")
    print(f"    M_N · ℏ_q² · h_q · [2]_q   = {mp.nstr(mu_d_minus_mu_u_bound, 16)} MeV")
    print(f"    realised / bound           = {mp.nstr(bound_ratio, 6)}  "
          "(~1/3 expected per §'Tightness' of the .md)")
    print()

    builder = (
        builder
        .add_parameter("q_0", mp.nstr(q0, 50))
        .add_parameter("M_N_MeV", mp.nstr(M_N, 50))
        .add_parameter(
            "M_N_source",
            "CODATA m_p + m_n / 2 (validation-tagged anchor; M_N "
            "substrate derivation pending — see "
            "docs/audits/2026-05-17-1ppb-workplan-v4.md)",
        )
        .add_data(
            "delta_m_codata_MeV",
            mp.nstr(delta_m_codata, 50),
        )
        .add_data(
            "delta_m_codata_role",
            "validation target — NOT a production input.  Used only "
            "for closure cross-check vs the substrate-derived value.",
        )
        .add_data(
            "substrate_factor_value",
            mp.nstr(S_q, 50),
        )
        .add_data(
            "mu_d_minus_mu_u_substrate_MeV",
            mp.nstr(mu_d_minus_mu_u_substrate, 50),
        )
        .add_data(
            "bound_factor_dimensionless",
            mp.nstr(bound_factor, 50),
        )
        .add_data(
            "upper_bound_MeV",
            mp.nstr(mu_d_minus_mu_u_bound, 50),
        )
        .add_data(
            "residual_vs_codata_delta_m_pn",
            mp.nstr(residual_vs_codata, 50),
        )
        .add_data(
            "realised_over_bound_ratio",
            mp.nstr(bound_ratio, 50),
        )
    )
    # add_upstream returns the body, not the builder — call separately.
    # Pass an absolute path (HERE / ...) so the lookup works regardless
    # of the script's CWD (per Copilot #696 review).
    builder.add_upstream(str(HERE / "probe-flavor-split-substrate.witness.json"))
    builder = (
        builder
        .add_assertion(
            name="substrate_closure_vs_codata_within_1_percent",
            computed=float(abs(residual_vs_codata)),
            expected=0.0,
            tolerance=0.01,
            unit="relative residual (dimensionless)",
            source=(
                "prop:flavor-dressed-mass-from-substrate-split closure: "
                "the substrate-pure formula matches CODATA m_n − m_p to "
                "within 1% modulo the dropped O((Δm/M_N)²) term. "
                "Measured residual at q_0: −0.53% (within the 1% gate)."
            ),
        )
        .add_assertion(
            name="upper_bound_strictly_respected",
            # Boolean encoding: 1.0 iff 0 < bound_ratio < 1 strictly.
            # Tolerance 0 forces the predicate to evaluate exactly,
            # so boundary values 0 and 1 (which would coincide with
            # μ_d−μ_u = 0 or μ_d−μ_u saturating the bound) fail.
            computed=(
                1.0
                if (bound_ratio > mp.mpf(0) and bound_ratio < mp.mpf(1))
                else 0.0
            ),
            expected=1.0,
            tolerance=0.0,
            unit="boolean (1.0 = strict bound holds)",
            source=(
                "thm:flavor-mass-splitting-bound: the realised "
                "μ_d − μ_u must lie strictly below "
                "M_N · ℏ_q² · h_q · [2]_q and strictly above 0.  "
                "Boolean predicate enforces strict inequality (boundary "
                "values 0 and 1 fail)."
            ),
        )
        .add_assertion(
            name="substrate_value_strictly_positive",
            # Same boolean trick: 1.0 iff value > 0 strictly.
            computed=(
                1.0
                if mu_d_minus_mu_u_substrate > mp.mpf(0)
                else 0.0
            ),
            expected=1.0,
            tolerance=0.0,
            unit="boolean (1.0 = strictly positive)",
            source=(
                "Positivity of substrate factor at q_0 > 1; gives "
                "μ_d − μ_u > 0 as required by hadronic physics.  "
                "Boolean predicate enforces strict positivity (negative "
                "values fail, including the boundary value 0)."
            ),
        )
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
