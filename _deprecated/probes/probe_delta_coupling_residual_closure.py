"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

#!/usr/bin/env python3
# polynomial_q_not_applicable: structural-form probe at q_0
"""P3.A follow-up — residual-closure probe for Δ_coupling at (2,2).

Builds on `probe_delta_coupling_leading_form.py` (this PR), which
verified at 50 dps that

    Δ_coupling(2,2) ≈ (A − 2) · E_0 · log(1/h(q_0))     [H1]

with relative gap **+0.71 %** (~7100 ppm) at A = 4.  The residual

    R := Δ_coupling(2,2) − 2 · E_0 · log(1/h(q_0))
       ≈ +0.0936 MeV

is well above the 1 ppb floor, so the H1 ansatz is a *near*-form, not
a closure.  This probe tests three structural correction families to
see whether any closes the residual with a clean (rational / quantum-
integer) coefficient at the doubly-magic anchor:

  H6  — q-dilogarithm additive correction:
            Δ = (A−2)·E_0·log(1/h) + c · E_0 · g(q_0)
        for g ∈ {Li₂^q(−h), Li₂^q(h), Li₃^q(−h), log(1+h), h, h²,
                 (1−h)·log(1/h)}.
        Reports c = (residual / E_0) / g for each candidate.

  H7  — multiplicative q-deformation of the leading form:
        (a) [A−2]_q · E_0 · log(1/h)       with [n]_q = (q^n−q^{−n})/(q−q^{−1})
        (b) (A−2) · E_0 · log_q(1/h)       with log_q(x) := (x^{1−q}−1)/(1−q)
        Reports anchor / prediction for each.

  H8  — additive micro-corrections at the m_e or E₀·h scale:
        Δ = (A−2)·E_0·log(1/h) + c · scale,
        for scale ∈ {m_e, E_0·h, E_0·h², E_0/q_0, E_0/q_0²}.
        Reports c for each.

This is a DIAGNOSTIC PROBE, NOT a fit.  Per AGENTS.md three-cal
discipline, calibrating Δ_coupling to AME is forbidden — this script
identifies whether any of the H6/H7/H8 candidates produce a clean
(small-rational or quantum-integer) coefficient that would justify a
substrate-derivation attempt.  A numerical near-fit is NOT acceptable
as a Pattern-A/B Lean §3b-cond instance.

Witness: `delta-coupling-residual-closure-probe.witness.json`
Content block: `conj:magic-shell-stabilization`
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from mpmath import mp, mpf

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ── 50 dps for consistency with magic-shell-empirical-instantiation ──
from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV  # CODATA-2022 full precision
set_compute_dps()


def _mpf_from_str(s: str) -> "mpf":
    return mpf(s)


def li2_q_asym(z, q, terms=120):
    """Asymmetric q-dilog: Σ_{k≥1} z^k / (k · (1 − q^k)),  |z| < 1."""
    s = mpf(0)
    for k in range(1, terms + 1):
        s += z**k / (k * (1 - q**k))
    return s


def li3_q_asym(z, q, terms=120):
    """Asymmetric q-trilog: Σ_{k≥1} z^k / (k² · (1 − q^k)),  |z| < 1."""
    s = mpf(0)
    for k in range(1, terms + 1):
        s += z**k / (k * k * (1 - q**k))
    return s


def quantum_integer(n, q):
    """[n]_q = (q^n − q^{−n}) / (q − q^{−1})."""
    return (q**n - q ** (-n)) / (q - 1 / q)


def log_q(x, q):
    """q-deformed log: log_q(x) := (x^{1−q} − 1) / (1 − q)."""
    return (x ** (1 - q) - 1) / (1 - q)


def main() -> None:
    HERE = Path(__file__).parent
    builder = (
        WitnessBuilder(
            "delta-coupling-residual-closure-probe", engine="mpmath"
        )
        .set_description(
            "P3.A follow-up: 50 dps probe of three structural correction "
            "families (H6 q-dilog/q-trilog additive, H7 multiplicative "
            "q-deformation [A−2]_q or log_q, H8 m_e/E₀·h micro-correction) "
            "for the +0.71% (~7100 ppm) residual of Δ_coupling(2,2) − "
            "2·E_0·log(1/h(q_0)) at the doubly-magic anchor. Diagnostic "
            "probe — does NOT fit Δ_coupling to AME (forbidden by three-cal "
            "discipline)."
        )
        .set_content_block("conj:magic-shell-stabilization")
        .add_parameter("mp_dps", mp.dps)
    )

    # ── Inputs: Δ_cat per-atom from canonical witness ────────────────
    msei = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    pad = msei["data"]["per_atom_delta_cat"]
    dc = {
        atom: _mpf_from_str(pad[atom_key]["delta_cat_MeV_50dps"])
        for atom, atom_key in (
            ("He3", "he3"),
            ("He4", "he4"),
        )
    }
    builder.add_parameter(
        "delta_cat_source",
        "magic-shell-empirical-instantiation.witness.json#per_atom_delta_cat",
    )
    builder.add_data(
        "delta_cat_inputs_MeV_50dps",
        {atom: mp.nstr(v, 50) for atom, v in dc.items()},
    )

    # ── Substrate parameters at 50 dps ───────────────────────────────
    # Canonical 50-dps q_0 (CAL-2) from q_parameter.Q_50_DIGIT_STR.
    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = M_E_MEV  # CODATA 2022  # from codata_constants
    E0 = m_e / (q0 * (q0 - 1))
    t_h = q0 - 1 / q0  # Hecke deformation parameter

    builder.add_parameter("q_0_50dps", mp.nstr(q0, 50))
    builder.add_parameter("m_e_MeV_CODATA", mp.nstr(m_e, 12))
    builder.add_parameter("E_0_MeV_50dps", mp.nstr(E0, 50))
    builder.add_parameter("t_h_50dps", mp.nstr(t_h, 50))

    # ── Anchor (2,2) and H1 residual ─────────────────────────────────
    Z, N, A = 2, 2, 4
    anchor = dc["He4"] - 2 * dc["He3"]
    f_h = mp.log(1 / t_h)
    H1_pred = (A - 2) * E0 * f_h  # (A−2) · E_0 · log(1/h)
    R = anchor - H1_pred  # residual after H1 lead
    R_over_E0 = R / E0

    builder.add_data(
        "anchor_22_doubly_magic",
        {
            "Z": Z, "N": N, "A": A,
            "value_MeV_50dps": mp.nstr(anchor, 50),
            "H1_prediction_MeV_50dps": mp.nstr(H1_pred, 50),
            "residual_R_MeV_50dps": mp.nstr(R, 50),
            "residual_over_E0_dimensionless_50dps": mp.nstr(R_over_E0, 50),
            "relative_gap_to_anchor_pct": mp.nstr(
                100 * R / anchor, 12
            ),
        },
    )

    # ── H6 — q-dilog / q-trilog additive correction ──────────────────
    # Δ = (A−2)·E₀·log(1/h) + c · E₀ · g(q_0); c = R/(E₀·g).
    h = t_h
    g_candidates = {
        "Li2_q_minus_h":      li2_q_asym(-h, q0, terms=160),
        "Li2_q_plus_h":       li2_q_asym(h, q0, terms=160),
        "Li3_q_minus_h":      li3_q_asym(-h, q0, terms=160),
        "log_one_plus_h":     mp.log(1 + h),
        "h":                  h,
        "h_squared":          h * h,
        "one_minus_h_log":    (1 - h) * f_h,
    }
    H6 = {}
    for name, g in g_candidates.items():
        c = R_over_E0 / g if g != 0 else None
        H6[name] = {
            "g_value_50dps": mp.nstr(g, 50),
            "c_coefficient_50dps": (
                mp.nstr(c, 18) if c is not None else None
            ),
            "c_close_to_small_rational": _is_small_rational(c) if c is not None else None,
        }
    H6["verdict"] = (
        "Probe reports c = R/(E₀·g) for each candidate g. A 'clean' "
        "closure would require c rational with small denominator (≤4) "
        "or a quantum integer at q_0. Inspection of the c column "
        "decides whether any candidate is structurally plausible."
    )
    builder.add_data("H6_q_dilog_additive_correction", H6)

    # ── H7 — multiplicative q-deformation of leading form ────────────
    # H7a: [A−2]_q · E₀ · log(1/h);  H7b: (A−2) · E₀ · log_q(1/h)
    qint_2 = quantum_integer(2, q0)
    H7a_pred = qint_2 * E0 * f_h
    H7a_ratio = anchor / H7a_pred if H7a_pred != 0 else None

    log_q_inv_h = log_q(1 / t_h, q0)
    H7b_pred = (A - 2) * E0 * log_q_inv_h
    H7b_ratio = anchor / H7b_pred if H7b_pred != 0 else None

    H7 = {
        "H7a_quantum_integer_prefactor": {
            "quantum_integer_2_q0_50dps": mp.nstr(qint_2, 50),
            "prediction_MeV_50dps": mp.nstr(H7a_pred, 50),
            "anchor_over_prediction_50dps": (
                mp.nstr(H7a_ratio, 18) if H7a_ratio is not None else None
            ),
            "matches_unity_within_1pct": (
                abs(H7a_ratio - 1) < mpf("0.01")
                if H7a_ratio is not None else None
            ),
        },
        "H7b_q_deformed_log": {
            "log_q_inv_h_50dps": mp.nstr(log_q_inv_h, 50),
            "prediction_MeV_50dps": mp.nstr(H7b_pred, 50),
            "anchor_over_prediction_50dps": (
                mp.nstr(H7b_ratio, 18) if H7b_ratio is not None else None
            ),
            "matches_unity_within_1pct": (
                abs(H7b_ratio - 1) < mpf("0.01")
                if H7b_ratio is not None else None
            ),
        },
        "verdict": (
            "If either H7a or H7b matches unity within 1%, the leading "
            "form acquires a structural q-deformation. Otherwise the "
            "ordinary log + classical (A−2) prefactor remains preferred."
        ),
    }
    builder.add_data("H7_multiplicative_q_deformation", H7)

    # ── H8 — additive micro-correction at m_e / E₀·h scale ───────────
    # Δ = (A−2)·E₀·log(1/h) + c · scale;  c = R / scale.
    scales = {
        "m_e":           m_e,
        "E0_times_h":    E0 * h,
        "E0_times_h_sq": E0 * h * h,
        "E0_over_q0":    E0 / q0,
        "E0_over_q0_sq": E0 / (q0 * q0),
    }
    H8 = {}
    for name, scale in scales.items():
        c = R / scale if scale != 0 else None
        H8[name] = {
            "scale_MeV_50dps": mp.nstr(scale, 50),
            "c_coefficient_50dps": (
                mp.nstr(c, 18) if c is not None else None
            ),
            "c_close_to_small_rational": _is_small_rational(c) if c is not None else None,
        }
    H8["verdict"] = (
        "Probe reports c = R/scale for each micro-correction scale. A "
        "clean closure would require c rational with small denominator. "
        "Inspection of the c column decides plausibility."
    )
    builder.add_data("H8_additive_micro_correction", H8)

    # ── Summary verdict ──────────────────────────────────────────────
    h6_clean = [n for n, v in H6.items()
                if isinstance(v, dict) and v.get("c_close_to_small_rational")]
    h7_clean = [n for n, v in H7.items()
                if isinstance(v, dict) and v.get("matches_unity_within_1pct")]
    h8_clean = [n for n, v in H8.items()
                if isinstance(v, dict) and v.get("c_close_to_small_rational")]

    summary = {
        "anchor_relative_gap_after_H1_pct": mp.nstr(100 * R / anchor, 8),
        "candidates_with_clean_coefficient": {
            "H6_q_dilog_or_trilog": h6_clean,
            "H7_q_deformation": h7_clean,
            "H8_micro_correction": h8_clean,
        },
        "structural_finding": (
            "At the doubly-magic (2,2) anchor and 50 dps precision, none "
            "of the H6/H7/H8 candidates produce a clean rational/quantum-"
            "integer coefficient that would close the +0.71% residual to "
            "the 1 ppb floor. The H1 leading form (A−2)·E₀·log(1/h(q_0)) "
            "remains a structural near-match without an identified closure "
            "term. Recommended next steps (require post-#644 merge for "
            "(2,1) and (1,2) cross-anchor consistency): (a) re-run H6/H7/"
            "H8 with all three magic-shell anchors and check coefficient "
            "consistency across (Z,N) — a structural closure must yield "
            "the SAME coefficient at every anchor, (b) explore KLR "
            "canonical-basis dimension counts as the residual source "
            "(per the trivial-skeleton workplan Pattern-B route), (c) "
            "do not promote H1 alone to a Lean §3b-cond Pattern-A/B "
            "instance — the 7100 ppm gap is far too large for a "
            "1 ppb-target derivation."
        ) if not (h6_clean or h7_clean or h8_clean) else (
            "Some H6/H7/H8 candidates flagged as clean-coefficient — "
            "see candidates_with_clean_coefficient. These require "
            "cross-anchor consistency (post-#644 merge) before any "
            "substrate-derivation attempt."
        ),
    }
    builder.add_data("summary", summary)

    builder.add_caveat(
        "DIAGNOSTIC PROBE ONLY — does not fit Δ_coupling to AME. "
        "A numerical near-fit is NOT acceptable as a Pattern-A/B Lean "
        "§3b-cond instance per AGENTS.md §3b-cond + the trivial-skeleton "
        "workplan. Any closure candidate must be derived from substrate "
        "primitives (KLR / Markov-trace / quantum-integer structure) "
        "before promotion."
    )
    builder.add_caveat(
        "Single-anchor probe — closure candidates flagged here MUST be "
        "cross-validated against the (2,1) and (1,2) anchors after "
        "PR #644 merges (which adds proton/neutron Δ_cat to the canonical "
        "magic-shell-empirical-instantiation witness). A coefficient that "
        "varies across (Z,N) is not a structural closure."
    )
    builder.add_caveat(
        "The small-rational heuristic uses denominator ≤ 12 with "
        "tolerance 1e-3 (relative). Clean coefficients flagged here are "
        "candidates, not proofs."
    )

    out = builder.save()
    print(f"\n[ok] wrote {out}")
    print(f"\n(2,2) anchor relative gap after H1 lead: "
          f"{mp.nstr(100 * R / anchor, 6)}%")
    print("Clean-coefficient candidates:")
    print(f"  H6 q-dilog/trilog: {h6_clean or 'none'}")
    print(f"  H7 q-deformation:  {h7_clean or 'none'}")
    print(f"  H8 micro-correction: {h8_clean or 'none'}")


def _is_small_rational(x, max_denom: int = 12, tol: float = 1e-3) -> bool:
    """Heuristic: return True if x is within `tol` (relative) of p/q
    for some integer 0 < q ≤ max_denom and integer p with |p| ≤ 4·q.
    """
    if x is None:
        return False
    try:
        ax = abs(float(x))
    except (TypeError, ValueError):
        return False
    if ax < 1e-12:
        return True  # zero residual = trivially "clean"
    for q in range(1, max_denom + 1):
        for p_sign in (1, -1):
            for p in range(0, 4 * q + 1):
                if p == 0 and p_sign == -1:
                    continue
                cand = p_sign * p / q
                if cand == 0:
                    continue
                if abs(float(x) - cand) / abs(cand) < tol:
                    return True
    return False


if __name__ == "__main__":
    main()
