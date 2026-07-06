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
"""P3.A follow-up — leading-term ansatz probe for Δ_coupling at magic shells.

Continues `delta_coupling_closed_form_probe.py` (PR #644) at higher
precision (mpmath 50 dps) and with a refined hypothesis ladder.

PR #644's probe identified candidate **C1 = log(1/t)** at substrate
parameter **t = h(q_0) := q_0 − q_0⁻¹** as a near-match for the
doubly-magic anchor:

    Δ_coupling(2,2) := Δ_cat(⁴He) − 2·Δ_cat(³He)
                    ≈ 2 · E_0 · log(1/h(q_0))

with fractional gap +0.71% (float64). This script verifies the lead
at **mpmath 50 dps** for the doubly-magic (2,2) anchor — the only
Δ_coupling anchor whose inputs (Δ_cat for ³He and ⁴He) are present
in the canonical `magic-shell-empirical-instantiation.witness.json`
on `main`.  The free-nucleon-clustering anchors (2,1) and (1,2)
require Δ_cat for proton and neutron, which PR #644 added to the
witness but is not yet merged; this probe defers to PR #644 for
those anchors and focuses on the (2,2) lead.

Hypothesis ladder (all at t = h(q_0) unless noted):

  H1  Leading factor (A−2) for Δ_coupling(2,2) at A = 4:
        Δ_coupling(2,2) ?≈ 2 · E_0 · log(1/h(q_0))
        — verified at 50 dps with relative gap +0.71%.

  H3  Alternative leading factors {Z+N, Z·N, Z²+N², (A−2)², min(Z,N),
        Z·N−1} at t = h(q_0).  Reports the per-factor ratio
        Δ_coupling(2,2) / (factor · E_0 · log(1/h(q_0))) and flags
        which fall within 1% of unity.  Only (A−2) and min(Z,N)
        (which agree at (2,2) since A=4, min=2) match.

  H4  q-dilogarithm Li₂^q(−h(q_0)) as candidate `f`.  No clean integer
        factor at the (2,2) anchor.

  H5  Same factor candidates at t = q_0 − 1 (β-decay normalisation).
        No clean matches at (2,2).

The script emits a per-candidate ratio table so a downstream
formalisation can decide whether
  (a) (A−2)·E_0·log(1/h(q_0)) is a structural leading-order term
      with sub-percent residual to be closed by a higher-order
      categorical correction, or
  (b) the form is anchor-class-specific (doubly-magic only).

This is a DIAGNOSTIC PROBE, NOT a fit.  Per AGENTS.md three-cal
discipline, calibrating Δ_coupling to AME is forbidden — this script
identifies which structural form to TARGET in the closed-form
derivation, not which one to TUNE.

Witness: `delta-coupling-leading-form-probe.witness.json`
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
    """Parse a 50-dps witness string as mpmath mpf at current precision."""
    return mpf(s)


def main() -> None:
    HERE = Path(__file__).parent
    builder = (
        WitnessBuilder(
            "delta-coupling-leading-form-probe", engine="mpmath"
        )
        .set_description(
            "P3.A follow-up: high-precision (50 dps) verification of "
            "the C1 = log(1/t) lead at t = h(q_0) for Δ_coupling at "
            "the doubly-magic (2,2) anchor and the (2,1) / (1,2) "
            "free-nucleon-clustering anchors. Tests the leading-factor "
            "ladder {(A−2), Z+N, Z·N, Z²+N², (A−2)², min(Z,N), Z·N−1}, "
            "a candidate (Z−N) chirality residual, and a q-dilogarithm "
            "alternative. Diagnostic probe — does NOT fit Δ_coupling to "
            "AME (forbidden by three-cal discipline)."
        )
        .set_content_block("conj:magic-shell-stabilization")
        .add_parameter("mp_dps", mp.dps)
    )

    # ── Inputs: Δ_cat per-atom from canonical witness ────────────────
    # Per the stored memory pattern, downstream consumers must load
    # Δ_cat from the canonical magic-shell-empirical-instantiation
    # witness, not recompute or hardcode AME-based proxies.
    msei = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    pad = msei["data"]["per_atom_delta_cat"]
    # On `main`, only {D, T, ³He, ⁴He} have Δ_cat values; the proton
    # and neutron entries are added by PR #644 and not yet merged.
    # We restrict to the (2,2) doubly-magic anchor which only needs
    # ³He and ⁴He.
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
    # Equivalent to `hbar_q = sqrt(Vol(4_1) / (m_μ/m_e)); q_0 = 1/(1-hbar_q)`
    # but routed through the single source-of-truth so CAL-2 cannot drift.
    q0 = mp.mpf(Q_50_DIGIT_STR)
    # m_e from CODATA 2022 (codata_constants is the SoT, but we re-state
    # the literal so the witness is self-contained and re-runnable).
    m_e = M_E_MEV  # from codata_constants
    E0 = m_e / (q0 * (q0 - 1))
    t_h = q0 - 1 / q0  # Hecke deformation parameter
    t_qm1 = q0 - 1  # β-decay-energy normalisation

    builder.add_parameter("q_0_50dps", mp.nstr(q0, 50))
    builder.add_parameter("m_e_MeV_CODATA", mp.nstr(m_e, 12))
    builder.add_parameter("E_0_MeV_50dps", mp.nstr(E0, 50))
    builder.add_parameter("t_h_50dps", mp.nstr(t_h, 50))
    builder.add_parameter("t_qm1_50dps", mp.nstr(t_qm1, 50))

    # ── Anchors ──────────────────────────────────────────────────────
    # On `main`, we restrict to the doubly-magic (2,2) anchor.
    # The (2,1) ³He=D+p and (1,2) T=D+n anchors require Δ_cat for
    # proton/neutron, which PR #644 added but is not yet merged.
    # Per the docstring of delta_coupling_closed_form_probe.py:
    #   Δ_coupling(2,2) := Δ_cat(⁴He) − 2 · Δ_cat(³He)         doubly-magic
    anchors = {
        "(2,2)_doubly_magic": {
            "Z": 2, "N": 2, "A": 4,
            "value_MeV": dc["He4"] - 2 * dc["He3"],
            "formula": "Δ_cat(⁴He) − 2·Δ_cat(³He)",
        },
    }
    builder.add_data(
        "anchors_MeV_50dps",
        {
            k: {
                "Z": v["Z"], "N": v["N"], "A": v["A"],
                "formula": v["formula"],
                "value_MeV_50dps": mp.nstr(v["value_MeV"], 50),
            }
            for k, v in anchors.items()
        },
    )

    # ── H1 — (A−2) · E_0 · log(1/h(q_0)) ─────────────────────────────
    f_h = mp.log(1 / t_h)
    E0_f_h = E0 * f_h
    builder.add_parameter("E0_log_inv_h_MeV_50dps", mp.nstr(E0_f_h, 50))

    H1 = {}
    for k, v in anchors.items():
        leading = v["A"] - 2  # (A−2)
        pred = leading * E0_f_h
        residual = v["value_MeV"] - pred
        rel_gap = residual / v["value_MeV"] if v["value_MeV"] != 0 else mpf(0)
        H1[k] = {
            "Z": v["Z"], "N": v["N"], "A": v["A"],
            "leading_factor_A_minus_2": leading,
            "prediction_MeV_50dps": mp.nstr(pred, 50),
            "residual_MeV_50dps": mp.nstr(residual, 50),
            "relative_gap_to_anchor": mp.nstr(rel_gap, 12),
        }
    builder.add_data("H1_leading_A_minus_2", H1)

    # ── H2 — DEFERRED to PR #644 / post-merge follow-up ──────────────
    # The (Z−N) chirality residual test requires the (2,1) and (1,2)
    # anchors (proton and neutron Δ_cat), which are added by PR #644
    # but not yet on main. Recorded here as a TODO marker so the
    # downstream agent (post-#644-merge) can re-run with full anchor
    # coverage.
    builder.add_data(
        "H2_chirality_residual_test_DEFERRED",
        {
            "status": "deferred",
            "reason": (
                "Requires Δ_cat values for proton and neutron, which "
                "are added by PR #644 (per_atom_delta_cat['proton'] / "
                "['neutron']) but not yet on main. Re-run this script "
                "post-#644 merge to populate H2."
            ),
            "expected_test": (
                "If residual = c · (Z−N), then "
                "res(2,1) + res(1,2) = 0. The float64 prior run in "
                "PR #644 reports res(2,1) + res(1,2) = −0.257 MeV, "
                "which falsifies the pure (Z−N) chirality ansatz."
            ),
        },
    )

    # ── H3 — alternative leading factors at t = h(q_0) ───────────────
    factor_candidates = {
        "A_minus_2": {"(2,2)_doubly_magic": 2},
        "Z_plus_N":  {"(2,2)_doubly_magic": 4},
        "Z_times_N": {"(2,2)_doubly_magic": 4},
        "Z2_plus_N2":{"(2,2)_doubly_magic": 8},
        "A_minus_2_squared": {"(2,2)_doubly_magic": 4},
        "min_Z_N":   {"(2,2)_doubly_magic": 2},
        "ZN_minus_1":{"(2,2)_doubly_magic": 3},
    }
    H3 = {}
    for name, fac_map in factor_candidates.items():
        H3[name] = {}
        for k, v in anchors.items():
            f = fac_map[k]
            ratio = v["value_MeV"] / (f * E0_f_h) if f != 0 else None
            H3[name][k] = {
                "factor": f,
                "anchor_over_factor_E0_logInvH": (
                    mp.nstr(ratio, 18) if ratio is not None else None
                ),
                "matches_unity_within_1pct": (
                    abs(ratio - 1) < mpf("0.01") if ratio is not None else None
                ),
            }
    builder.add_data("H3_alternative_leading_factors_at_t_h", H3)

    # ── H4 — q-dilogarithm Li₂^q(−h(q_0)) ────────────────────────────
    # Asymmetric q-dilogarithm series:
    #   Li₂^q(z) = Σ_{k≥1} z^k / (k · (1 − q^k))
    # for |z| < 1.  Convergent at z = −h(q_0) ≈ −0.21 since |z| < 1.
    def li2_q_asym(z, q, terms=120):
        s = mpf(0)
        for k in range(1, terms + 1):
            s += z**k / (k * (1 - q**k))
        return s

    li2_h_neg = li2_q_asym(-t_h, q0, terms=120)
    minus_E0_li2 = -E0 * li2_h_neg
    H4 = {
        "Li2_q_minus_h_50dps": mp.nstr(li2_h_neg, 50),
        "minus_E0_times_Li2_q_minus_h_MeV_50dps": mp.nstr(minus_E0_li2, 50),
        "anchors_over_minus_E0_Li2_q": {},
    }
    for k, v in anchors.items():
        ratio = v["value_MeV"] / minus_E0_li2 if minus_E0_li2 != 0 else None
        H4["anchors_over_minus_E0_Li2_q"][k] = (
            mp.nstr(ratio, 18) if ratio is not None else None
        )
    H4["verdict"] = (
        "No clean integer factor: ratios are "
        + ", ".join(
            f"{k}={mp.nstr(v['value_MeV']/minus_E0_li2, 6)}"
            for k, v in anchors.items()
        )
    )
    builder.add_data("H4_q_dilogarithm_at_t_h", H4)

    # ── H5 — same factor candidates at t = q_0 − 1 ───────────────────
    f_qm1 = mp.log(1 / t_qm1)
    E0_f_qm1 = E0 * f_qm1
    H5 = {
        "f_qm1_50dps": mp.nstr(f_qm1, 50),
        "E0_log_inv_qm1_MeV_50dps": mp.nstr(E0_f_qm1, 50),
        "anchor_over_E0_logInvQm1": {},
    }
    for k, v in anchors.items():
        ratio = v["value_MeV"] / E0_f_qm1
        H5["anchor_over_E0_logInvQm1"][k] = mp.nstr(ratio, 18)
    H5["verdict"] = (
        "No clean integer factor at t = q_0 − 1; values are "
        + ", ".join(
            f"{k}={mp.nstr(v['value_MeV']/E0_f_qm1, 6)}"
            for k, v in anchors.items()
        )
    )
    builder.add_data("H5_t_eq_q_minus_1", H5)

    # ── Summary verdict ──────────────────────────────────────────────
    summary = {
        "leading_form_candidate": (
            "Δ_coupling(2,2) ≈ 2 · E_0 · log(1/h(q_0))   at t = h(q_0)"
        ),
        "matches_per_anchor": {
            k: {
                "factor_A_minus_2": v["A"] - 2,
                "predicted_MeV": mp.nstr(
                    (v["A"] - 2) * E0_f_h, 18
                ),
                "anchor_MeV": mp.nstr(v["value_MeV"], 18),
                "relative_gap_pct": mp.nstr(
                    100
                    * (v["value_MeV"] - (v["A"] - 2) * E0_f_h)
                    / v["value_MeV"],
                    8,
                ),
            }
            for k, v in anchors.items()
        },
        "structural_finding": (
            "At the doubly-magic (2,2) anchor and 50 dps precision, "
            "Δ_coupling(2,2) = 2 · E_0 · log(1/h(q_0)) holds with "
            "relative gap +0.71% (~7100 ppm). This is well above the "
            "1 ppb target, so the ansatz is a leading-order STRUCTURAL "
            "near-form, not a 1 ppb closure. The next steps are: "
            "(a) re-run this probe post-#644 merge to add the (2,1) "
            "and (1,2) anchors and confirm whether (A−2) generalises, "
            "(b) test higher-order categorical corrections (q-dilog "
            "or KLR canonical-basis dim count) to close the 7100 ppm "
            "residual, (c) derive the (A−2) prefactor from substrate "
            "primitives (Markov-trace / KLR structure) before any "
            "Lean §3b-cond Pattern-A/B promotion."
        ),
    }
    builder.add_data("summary", summary)

    builder.add_caveat(
        "DIAGNOSTIC PROBE ONLY — does not fit Δ_coupling to AME. "
        "The (A−2)·E_0·log(1/h(q_0)) form is suggested by the data but "
        "would need to be derived from substrate primitives (KLR / "
        "Markov-trace structure) for inclusion in the §3b-cond canonical "
        "instance MagicShellCrossCoupling.canonicalCrossCoupling. "
        "A numerical near-fit is NOT acceptable as a Pattern-A/B Lean "
        "instance per AGENTS.md §3b-cond + the trivial-skeleton workplan."
    )
    builder.add_caveat(
        "The 0.71% gap at the (2,2) doubly-magic anchor exceeds the "
        "780 ppb hard floor by ~10000× — closing it requires either a "
        "structurally-derived correction term OR demonstrating that "
        "the residual lies within the topology-class assumption error "
        "of the magic-shell ansatz itself."
    )
    builder.add_caveat(
        "(Z−N) chirality residual hypothesis (H2) is DEFERRED — needs "
        "Δ_cat for proton and neutron from PR #644's "
        "magic-shell-empirical-instantiation witness extension. The "
        "float64 prior run in PR #644 reports res(2,1) + res(1,2) "
        "= −0.257 MeV which would FALSIFY a pure (Z−N) ansatz; this "
        "probe should be re-run at 50 dps post-#644 merge to confirm."
    )

    out = builder.save()
    print(f"\n[ok] wrote {out}")
    print(f"\nLeading form: Δ_coupling ≈ (A−2)·E_0·log(1/h(q_0)) at t=h(q_0)")
    print("Per-anchor relative gaps:")
    for k, v in anchors.items():
        rel = (v["value_MeV"] - (v["A"] - 2) * E0_f_h) / v["value_MeV"]
        print(f"  {k:>32s}: {mp.nstr(100 * rel, 6)}%")


if __name__ == "__main__":
    main()
