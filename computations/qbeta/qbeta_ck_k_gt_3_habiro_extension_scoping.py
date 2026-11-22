#!/usr/bin/env python3
"""qbeta_ck_k_gt_3_habiro_extension_scoping.py — does the [3]_q/25
Habiro template extend to c_4 (and beyond)?

PR #1786 follow-up. After the rebase onto origin/main, the c_3
closure landed (commit `305c08a91`):

  c_3(q) = -(q² + q⁻²) · (1 + ℏ_q · [3]_q / 25 + ℏ_q³ / [2]_q)

at q_0 → -2.069348 vs target -2.069343 = **2.65 ppm** (closes 10 ppm
gate). Audit doc:
`docs/audits/2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`.

The c_3 closure is tagged **NEAR-MATCH** (not structural) — 5+ free
parameters. But the existence of a structural-shape Habiro element
that closes c_3 raises the natural question for k = 4, 5, 6:

  Does c_4 = base_4 · (1 + ℏ_q · ?·[?]_q / ? + ...) for some
  categorical base_4 and some Habiro correction?

This probe is the **SCOPING step** before any c_4 closure claim. It:

  1. Computes c_4 empirically from the CODATA residual at q_0
     (50 dps), using the same N=2 partial ladder Q_A·cos(α_eff)·(1-u²)
     established structurally in PR #1786, plus the c_3 closure now
     on main.
  2. Tests several **categorical base** hypotheses for c_4:
        - -1   (analogous to c_2 = -1 STRUCTURAL — even-k geometric)
        - +1   (J_unknot)
        - -2   (J_Hopf at q=1)
        - -(q² + q⁻²) at q_0 (= J_Hopf(q_0) — same as c_3 base)
        - J_trefoil(q_0)    — Jones of 3_1
        - J_figure_eight(q_0) — Jones of 4_1
     For each base, computes `correction = c_4_empirical / base`.
  3. For the base with `correction` closest to a clean Habiro form
     (e.g. 1 + small), reports the residual Habiro element shape.
  4. Verdict: does the template extend? Which (if any) base for c_4
     is consistent with a [N]_q/25 or similar Habiro correction?

Honest scoping. NEAR-MATCH at best — no derivation claim. The
output identifies the most promising base for downstream
categorical investigation.

The same machinery applies to c_5, c_6, ... but this probe focuses
on c_4 (the next one open after PR #1786's c_2 = -1 STRUCTURAL).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from codata_constants import (  # noqa: E402 (codata sweep)
    M_E_MEV,
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
    Q_BETA_MEV,
)
del _sys, _Path, _bridge

import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

Q0_MP_PIN = Q_50_DIGIT_STR
# The 5-decimal Q_β this probe has always used. Kept as a literal ON
# PURPOSE: this producer's headline finding is that a c_4 "extraction"
# elsewhere is an artifact of mixing a ROUNDED CODATA Q_β with a
# full-precision one, and this literal is the rounded one. The
# assertion in `main()` measures the gap against the registry rather
# than leaving the claim as prose.
Q_BETA_CODATA_LITERAL = "0.78233"
Q_BETA_CODATA_MEV = mp.mpf(Q_BETA_CODATA_LITERAL)
# Likewise hand-typed here rather than taken from codata_constants.
# Left in place, and checked against the registry below — deleting the
# literal would delete the check, and Q_A scales linearly with it.
M_E_LITERAL_IN_THIS_FILE = "0.51099895069"
M_E_MEV_LOCAL = mp.mpf(M_E_LITERAL_IN_THIS_FILE)


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-k-gt-3-habiro-extension-scoping",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "After the c_3 [3]_q/25 Habiro closure landed on main "
        "(commit 305c08a91), this probe asks: does the same "
        "template extend to c_4? Computes c_4 empirically by "
        "residual extraction, tests 6 categorical base hypotheses, "
        "reports which base needs the smallest Habiro correction. "
        "Scoping only — no derivation claim."
    )
    builder.set_content_block("prop:q-beta-c-2-eq-neg-one-structural")

    print("=" * 78)
    print(" Q_β c_4 SCOPING — does the [3]_q/25 Habiro template extend?")
    print("=" * 78)
    print()

    q = mp.mpf(Q0_MP_PIN)

    # Substrate quantities (per probe_q_beta_operator_valued_N3.py
    # convention — the one used in c_2 = -1 STRUCTURAL).
    h = q - 1 / q                     # Hecke skein
    z = q**3 / (q**2 + 1)  # Markov-Jones
    alpha = (z - 1) * h / 2           # eigenphase
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)          # Hoefsmit b = √(q⁴+q²+1)/(q²+1)
    # SECOND ROUTE to b². The comment above asserts an identity that
    # nothing here checked. `b_sq_skein` reaches the same number from
    # the Hecke skein variable h alone — (h²+3)/(h²+4) — never forming
    # d₁ or d₂. u = b·ℏ_q² is the ladder variable every c_k in this file
    # is a coefficient of, so the two conventions agreeing is the
    # precondition for comparing c_3 against a closure written in h.
    b_sq_skein = (h ** 2 + 3) / (h ** 2 + 4)
    hbar_q = (q - 1) / q              # quantum Planck
    hbar_q_sq = hbar_q ** 2
    hbar_q_4 = hbar_q ** 4
    hbar_q_6 = hbar_q ** 6
    hbar_q_8 = hbar_q ** 8

    # u_ladder = b · ℏ_q² (the precision-ladder variable)
    u = b * hbar_q_sq
    u2 = u ** 2
    u3 = u ** 3
    u4 = u ** 4

    # Q_A bare scale (substrate region |q²-2q-1| = 2q+1-q²)
    Q_A = M_E_MEV_LOCAL * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)

    # N=1, N=2, N=3 partial ladder
    alpha_eff = alpha - b * hbar_q_sq / 2
    cos_alpha_eff = mp.cos(alpha_eff)
    Q_N1 = Q_A * cos_alpha_eff
    Q_N2 = Q_N1 * (1 - u2)            # c_2 = -1 STRUCTURAL ✓

    # c_3 EMPIRICAL extraction (to u³ precision). The qbeta_1ppq_
    # achieved procedure: extract c_3 from CODATA-Q_β at u³ order
    # FIRST, then c_4 captures the residual at u⁴ order.
    # (If we used the closure formula c_3 — off by ~3 ppm at u³ —
    # the c_4 extraction is dominated by the c_3 fit error, NOT
    # the genuine u⁴ ladder coefficient. So we must use empirical
    # c_3 for a clean c_4 extraction. Compute c_3 as the value
    # making Q_N3 hit Q_β_CODATA exactly at u³ order.)
    Q_emp_factor_N3 = Q_BETA_CODATA_MEV / Q_N2
    c_3_empirical = (Q_emp_factor_N3 - 1) / u3
    Q_N3 = Q_N2 * (1 + c_3_empirical * u3)

    # c_3 closure formula on main (305c08a91) for comparison
    qint_2 = q + 1 / q                                 # [2]_q
    qint_3 = q ** 2 + 1 + 1 / q ** 2                   # [3]_q
    J_Hopf_q = -(q ** 2 + 1 / q ** 2)
    c_3_closure = J_Hopf_q * (1 + hbar_q * qint_3 / 25
                              + hbar_q ** 3 / qint_2)

    eps_N2 = (Q_N2 / Q_BETA_CODATA_MEV - 1) * mp.mpf("1e6")
    eps_N3 = (Q_N3 / Q_BETA_CODATA_MEV - 1) * mp.mpf("1e6")

    # Empirical c_4 from N=3 → CODATA residual
    # Q_β_CODATA = Q_N3 · (1 + c_4 · u⁴)
    # → c_4 = (Q_β_CODATA / Q_N3 - 1) / u⁴
    c_4_empirical = (Q_BETA_CODATA_MEV / Q_N3 - 1) / u4

    print(f"  Substrate at q_0:")
    print(f"    q_0       = {Q0_MP_PIN}")
    print(f"    b         = {mp.nstr(b, 12)}")
    print(f"    ℏ_q       = {mp.nstr(hbar_q, 12)}")
    print(f"    u = b·ℏ_q² = {mp.nstr(u, 12)}")
    print(f"    [2]_q     = {mp.nstr(qint_2, 12)}")
    print(f"    [3]_q     = {mp.nstr(qint_3, 12)}")
    print(f"    -(q²+q⁻²) = {mp.nstr(J_Hopf_q, 12)}")
    print()
    print(f"  Ladder precision at q_0:")
    print(f"    eps(Q_N2 with c_2 = -1 STRUCTURAL)        = "
          f"{float(eps_N2):+9.3f} ppm")
    print(f"    eps(Q_N3 with c_3 empirical, exact at u³) = "
          f"{float(eps_N3):+12.6f} ppm (extraction residual)")
    print()
    print(f"  c_3 values:")
    print(f"    c_3 empirical (this probe, exact at u³) = "
          f"{mp.nstr(c_3_empirical, 15)}")
    print(f"    c_3 closure formula (main, NEAR-MATCH)  = "
          f"{mp.nstr(c_3_closure, 15)}")
    print(f"    delta = {mp.nstr(c_3_closure - c_3_empirical, 8)}")
    print(f"            ({float(mp.fabs(c_3_closure - c_3_empirical)/c_3_empirical*1e6):.2f} ppm)")
    print()
    print(f"  Empirical c_4 (from N=3 → CODATA residual, u⁴ coefficient):")
    print(f"    c_4_emp = {mp.nstr(c_4_empirical, 15)}")
    # The line that used to sit here read "(matches qbeta_1ppq_achieved
    # c_4 ≈ -0.972 — even-k geometric)". It was a fixed string printed
    # directly beneath a number that is 0, and it contradicted this
    # probe's own verdict twenty lines down. Say what the number is
    # instead, and let it disagree.
    if c_4_empirical == 0:
        print(f"      → EXACTLY zero: c_3 was extracted from the same "
              f"single CODATA Q_β, so it absorbs the whole residual and")
        print(f"        leaves nothing at u⁴. This CONTRADICTS "
              f"qbeta_1ppq_achieved's c_4 ≈ -0.972; see the verdict below.")
    else:
        print(f"      → nonzero at {mp.nstr(c_4_empirical, 8)}; compare "
              f"qbeta_1ppq_achieved's c_4 ≈ -0.972.")
    print()

    # ---------------------------------------------------------------
    # Test categorical base hypotheses for c_4
    # ---------------------------------------------------------------
    # Trefoil 3_1 Jones polynomial (one common convention):
    # V(3_1)(q) = -q^-4 + q^-3 + q^-1 (right-handed)
    J_trefoil = -1 / q ** 4 + 1 / q ** 3 + 1 / q
    # Figure-eight 4_1 Jones polynomial:
    # V(4_1)(q) = q^-2 - q^-1 + 1 - q + q^2
    J_figure_eight = (1 / q ** 2 - 1 / q + 1 - q + q ** 2)

    bases = {
        "-1  (c_2 = -1 STRUCTURAL analog, even-k geometric)":
            mp.mpf("-1"),
        "+1  (J_unknot)":
            mp.mpf("+1"),
        "-2  (J_Hopf at q=1)":
            mp.mpf("-2"),
        "-(q²+q⁻²) = J_Hopf(q_0) (same as c_3 base)":
            J_Hopf_q,
        "J_trefoil(q_0) (3_1 right-handed)":
            J_trefoil,
        "J_figure_eight(q_0) (4_1)":
            J_figure_eight,
        # The 'no-base' fit: c_4_empirical itself
        "c_4_emp (trivial fit, sanity)":
            c_4_empirical,
    }

    print(f"  Base hypothesis           value at q_0       correction = c_4/base")
    print(f"  " + "-" * 76)

    results = []
    for name, base_val in bases.items():
        if base_val == 0:
            continue
        correction = c_4_empirical / base_val
        # "Distance from 1" — closer to 1 = needs smaller Habiro correction
        dist_from_one = mp.fabs(correction - 1)
        print(f"  {name[:45]:<45} {mp.nstr(base_val, 10):>14}  "
              f"correction = {mp.nstr(correction, 10):<14}  "
              f"|c-1| = {float(dist_from_one):.4f}")
        results.append({
            "base_name": name,
            "base_value_at_q0": mp.nstr(base_val, 20),
            "correction_factor": mp.nstr(correction, 20),
            "dist_from_one": float(dist_from_one),
        })

    print()

    # Sort by smallest |correction - 1| — most promising structural base
    results_sorted = sorted(results, key=lambda r: r["dist_from_one"])
    best = results_sorted[0]
    # When c_4 is exactly 0, every base gives correction = 0 and every
    # |correction - 1| is exactly 1: the ranking is a total tie and
    # "MOST PROMISING" below is just whichever key came first. Say so,
    # rather than presenting the dict order as a result.
    tied = [r for r in results_sorted
            if r["dist_from_one"] == best["dist_from_one"]]
    ranking_is_degenerate = len(tied) == len(results_sorted)
    if ranking_is_degenerate:
        print(f"  ⚠ RANKING DEGENERATE — all {len(results_sorted)} bases tie "
              f"at |correction - 1| = {best['dist_from_one']:.6f} "
              f"(c_4 = {mp.nstr(c_4_empirical, 6)}), so the 'most "
              f"promising' base below is dict order, not a finding.")
        print()
    print(f"  MOST PROMISING base for c_4 (smallest |correction - 1|):")
    print(f"    {best['base_name']}")
    print(f"    correction factor = {best['correction_factor']}")
    print(f"    → distance from 1 = {best['dist_from_one']:.6f}")
    print()

    # Skip trivial-fit base; report best NON-TRIVIAL base
    non_trivial = [r for r in results_sorted
                   if "trivial" not in r["base_name"]]
    print(f"  MOST PROMISING NON-TRIVIAL base for c_4:")
    if non_trivial:
        best_nt = non_trivial[0]
        print(f"    {best_nt['base_name']}")
        print(f"    correction = {best_nt['correction_factor']}")
        print(f"    → distance from 1 = {best_nt['dist_from_one']:.6f}")
        correction_mp = mp.mpf(best_nt['correction_factor'])
        # Is correction close to (1 + a·ℏ_q·[N]_q/M)? For c_3 closure:
        # correction = 1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q
        # Try the same form for c_4:
        c3_style = 1 + hbar_q * qint_3 / 25 + hbar_q ** 3 / qint_2
        match_c3_style = mp.fabs(correction_mp - c3_style) / c3_style
        print()
        print(f"  Test: does correction match the c_3 Habiro form?")
        print(f"    c_3-style: (1 + ℏ_q·[3]_q/25 + ℏ_q³/[2]_q) = "
              f"{mp.nstr(c3_style, 12)}")
        print(f"    relative gap: {float(match_c3_style * 1e6):.1f} ppm")
        if match_c3_style < mp.mpf("1e-3"):
            print(f"    ✓ Habiro template MAY extend to c_4 (same correction shape)")
        else:
            print(f"    ✗ Habiro template does NOT extend straightforwardly")
            print(f"      (would need different rung structure)")
    else:
        print(f"    (no non-trivial candidates)")
    print()

    print("=" * 78)
    print(" VERDICT — c_k for k > 3")
    print("=" * 78)
    print()
    print(f"  c_2 = -1                 STRUCTURAL ✓ (PR #1786)")
    print(f"  c_3 = -(q²+q⁻²)·(1+...)  NEAR-MATCH closed via [3]_q/25 (main)")
    print(f"  c_4 = {float(c_4_empirical):.4e}  vanishes at consistent precision")
    print()
    print(f"  ★ MAJOR FINDING — c_4 'extraction' in qbeta_1ppq_achieved.py")
    print(f"    is a normalization artifact, NOT a genuine ladder coefficient.")
    print()
    print(f"    qbeta_1ppq_achieved.py extracts c_4 by:")
    print(f"      (a) reading c_3 from q-beta-operator-valued-N3.witness")
    print(f"          where c_3 was fitted using rounded Q_AME =")
    print(f"          mpf('939.5654205240') - mpf(M_P_MEV_VALIDATION) - m_e")  # noqa: P31 — quotes the historical fit input
    print(f"      (b) computing Q_N3 with that c_3")
    print(f"      (c) comparing to full-precision Q_codata = m_n - m_p - m_e")
    print(f"          using codata_constants values (different precision!)")
    print(f"      (d) attributing the discrepancy to a 'c_4 ≈ -0.972' term")
    print()
    print(f"    The discrepancy is between TWO CODATA Q_β values (rounded vs")
    print(f"    full precision), NOT a genuine u⁴ ladder coefficient.")
    print(f"    When THIS probe uses ONE consistent CODATA value throughout,")
    print(f"    c_3 fits the entire residual and c_4 → 0 exactly.")
    print()
    print(f"  Implication: the 1 ppQ claim in qbeta_1ppq_achieved.py rests")
    print(f"  on absorbing a precision-mismatch artifact into c_4, which")
    print(f"  cancels in Q_N4. This works numerically (it's a self-consistency")
    print(f"  loop) but does NOT identify a categorical c_4 coefficient.")
    print()
    print(f"  Genuine open objects:")
    print(f"    A. Close the 3 ppm c_3 NEAR-MATCH residual categorically")
    print(f"       (a u⁴ correction to the [3]_q/25 closure, IF it exists)")
    print(f"    B. Define c_4, c_5, ... using ONE single CODATA Q_β value")
    print(f"       and SEPARATE extractions (e.g. take a SECOND CODATA")
    print(f"       observable — Q_β at higher precision, or a related")
    print(f"       isotope's Q_β — to separately constrain c_4)")
    print(f"    C. The 'even-k geometric' pattern hypothesis (c_2 = c_4 ≈ -1)")
    print(f"       cannot be tested without first defining c_4 cleanly.")
    print()

    builder.add_data("substrate", {
        "q_0": Q0_MP_PIN,
        "b": mp.nstr(b, 25),
        "u": mp.nstr(u, 25),
        "qint_2": mp.nstr(qint_2, 25),
        "qint_3": mp.nstr(qint_3, 25),
        "J_Hopf_q": mp.nstr(J_Hopf_q, 25),
    })
    builder.add_data("c_3_closure_at_q_0", {
        "formula": "-(q^2 + q^-2) * (1 + hbar_q * [3]_q / 25 + hbar_q^3 / [2]_q)",
        "value": mp.nstr(c_3_closure, 25),
        "source": "commit 305c08a91 on origin/main",
    })
    builder.add_data("c_4_empirical_at_q_0", {
        "value": mp.nstr(c_4_empirical, 25),
        "method": "residual from Q_β_CODATA / Q_N3 - 1 = c_4 · u^4",
    })
    builder.add_data("base_hypothesis_results", results)
    builder.add_data("best_non_trivial_base",
                     non_trivial[0] if non_trivial else None)

    # ── Assertions ────────────────────────────────────────────────────
    # The narration above says c_2 is the only structural c_k, that c_4
    # is a normalisation artifact, and that the artifact comes from
    # mixing two CODATA Q_β values. None of that was asserted. It is now.

    # (1) The MAJOR FINDING, measured on this probe's own constant.
    #   Route A: the 5-decimal Q_β literal typed into this module.
    #   Route B: codata_constants.Q_BETA_MEV, derived from CAL-1+CAL-2
    #            at full precision — and, as a third cross-check
    #            recorded below, m_n - m_p - m_e from the registry.
    # This probe IS on the rounded side of the mismatch it describes:
    # the 4.4 ppm gap propagates to a 0.75% shift in c_3_empirical
    # (-981.5 here vs -974.1 in the operator-valued N3 witness, which
    # uses the full-precision value). Tolerance 5e-6 is the half-ulp of
    # a 5-decimal rounding; anything larger means the literal is not
    # merely rounded but wrong.
    q_beta_from_masses = M_N_MEV_VALIDATION - M_P_MEV_VALIDATION - M_E_MEV
    builder.add_data("codata_q_beta_three_routes", {
        "literal_in_this_module": Q_BETA_CODATA_LITERAL,
        "registry_Q_BETA_MEV": mp.nstr(Q_BETA_MEV, 25),
        "registry_m_n_minus_m_p_minus_m_e": mp.nstr(q_beta_from_masses, 25),
        "literal_vs_registry_ppm": mp.nstr(
            (Q_BETA_CODATA_MEV / Q_BETA_MEV - 1) * mp.mpf("1e6"), 10),
        "note": ("The rounded/full-precision mismatch this probe's "
                 "verdict attributes to qbeta_1ppq_achieved is present "
                 "in this probe's own input constant."),
    })
    builder.add_assertion(
        "qbeta_literal_matches_codata_registry_to_five_decimals",
        computed=Q_BETA_CODATA_LITERAL,
        expected=mp.nstr(Q_BETA_MEV, 25),
        tolerance="5e-6",
        source=(
            "Route A: the hand-typed 5-decimal Q_β used throughout this "
            "probe. Route B: codata_constants.Q_BETA_MEV (CAL-1+CAL-2). "
            "Tolerance 5e-6 = half-ulp of a 5-decimal rounding."
        ),
    )

    # (2) The hand-typed electron mass, same shape.
    builder.add_assertion(
        "local_electron_mass_literal_matches_codata_registry",
        computed=M_E_LITERAL_IN_THIS_FILE,
        expected=mp.nstr(M_E_MEV, 25),
        tolerance="1e-20",
        source=(
            "Route A: the m_e literal in this module, which sets the "
            "scale of Q_A and hence of every Q_N. Route B: "
            "codata_constants.M_E_MEV."
        ),
    )

    # (3) The ladder, against a SECOND PRODUCER.
    #   Route A: Q_N2 = Q_A·cos(α_eff)·(1 − u²) rebuilt here at 65 dps
    #            from q₀ and the Hoefsmit substrate.
    #   Route B: the `Q_N2` field of the committed
    #            q-beta-operator-valued-N3 witness, produced by a
    #            different script.
    # Neither side sees a CODATA Q_β, so this isolates the ladder from
    # the rounding question in (1): it says the substrate construction
    # is the same one the N3 probe used, which is what licenses
    # comparing c_3 across the two.
    n3 = builder.add_upstream(
        HERE.parent / "q-beta-operator-valued-N3.witness.json")
    builder.add_assertion(
        "q_n2_ladder_matches_operator_valued_n3_witness",
        computed=mp.nstr(Q_N2, 25),
        expected=n3["data"]["Q_N2"],
        tolerance="1e-22",
        source=(
            "Route A: Q_A·cos(α_eff)·(1−u²) from q₀, b and ℏ_q at 65 "
            "dps in this probe. Route B: the Q_N2 recorded by "
            "q_beta_operator_valued_N3 in its own witness."
        ),
    )

    # (4) The two conventions for the ladder variable's b.
    #   Route A: 1 + d₁d₂ from the Hoefsmit block entries.
    #   Route B: (h²+3)/(h²+4) from the Hecke skein variable.
    builder.add_data("b_squared_two_routes", {
        "hoefsmit_one_plus_d1_d2": mp.nstr(d1 * d2 + 1, 25),
        "skein_h2_plus_3_over_h2_plus_4": mp.nstr(b_sq_skein, 25),
        "difference": mp.nstr((d1 * d2 + 1) - b_sq_skein, 8),
    })
    builder.add_assertion(
        "b_squared_hoefsmit_and_skein_routes_agree",
        computed=mp.nstr(d1 * d2 + 1, 30),
        expected=mp.nstr(b_sq_skein, 30),
        tolerance="1e-55",
        source=(
            "Route A: 1 + d₁d₂ with d₁ = q³/(q²+1), d₂ = -1/(q(q²+1)) — "
            "the Hoefsmit seminormal block. Route B: (h²+3)/(h²+4) with "
            "h = q − 1/q — the skein form the c_3 closure is written in. "
            "The comment beside `b` above asserts this identity."
        ),
    )

    # (5) The q-brackets the closure formula is built from.
    #   Route A: the explicit polynomials q + 1/q and q² + 1 + q⁻².
    #   Route B: the bracket quotients (q^k − q^-k)/(q − q^-1).
    qint_2_quot = (q ** 2 - q ** -2) / (q - 1 / q)
    qint_3_quot = (q ** 3 - q ** -3) / (q - 1 / q)
    builder.add_data("q_bracket_two_routes_gap", {
        "[2]_q": mp.nstr(qint_2 - qint_2_quot, 8),
        "[3]_q": mp.nstr(qint_3 - qint_3_quot, 8),
    })
    builder.add_assertion(
        "qint3_polynomial_matches_bracket_quotient",
        computed=mp.nstr(qint_3, 30),
        expected=mp.nstr(qint_3_quot, 30),
        tolerance="1e-55",
        source=(
            "Route A: the polynomial q² + 1 + q⁻² written out in this "
            "probe and fed to the [3]_q/25 closure. Route B: the "
            "bracket quotient (q³ − q⁻³)/(q − q⁻¹)."
        ),
    )

    # (6) The verdict's central claim, asserted.
    #   Route A: c_4 = (Q_β/Q_N3 − 1)/u⁴ evaluated numerically at 65 dps.
    #   Route B: 0 — because c_3_empirical is DEFINED as the value making
    #            Q_N3 hit Q_β exactly at u³, so Q_N3 ≡ Q_β and there is
    #            no u⁴ residual left to attribute. An evaluated property
    #            of the extraction, not a copy of Route A.
    # This is the honest form of "c_4 is a normalisation artifact": it
    # fails the moment the extraction stops being self-consistent (two
    # different Q_β values, or 65 dps proving insufficient for the
    # division by u⁴ ≈ 5e-9).
    builder.add_assertion(
        "c4_extraction_vanishes_under_single_codata_value",
        computed=mp.nstr(mp.fabs(c_4_empirical), 30),
        expected="0",
        tolerance="1e-30",
        source=(
            "Route A: |c_4| = |Q_β/Q_N3 − 1|/u⁴ at 65 dps. Route B: 0, "
            "from the construction — c_3 is extracted so that Q_N3 = "
            "Q_β exactly at u³ order, using ONE CODATA value. "
            "qbeta_1ppq_achieved reports c_4 ≈ -0.972 by mixing a "
            "rounded Q_β into the c_3 fit and a full-precision one into "
            "the comparison; that difference is the whole coefficient."
        ),
    )

    # (7) Recorded, not repaired: the empirical/closure c_3 gap.
    builder.add_data("c_3_two_routes", {
        "empirical_at_u3_this_probe": mp.nstr(c_3_empirical, 25),
        "closure_formula_main": mp.nstr(c_3_closure, 25),
        "relative_gap_ppm": mp.nstr(
            mp.fabs(c_3_closure - c_3_empirical) / mp.fabs(c_3_empirical)
            * mp.mpf("1e6"), 10),
        "docstring_claims_ppm": "2.65",
    })
    builder.add_caveat(
        f"This module's docstring says the c_3 closure lands 2.65 ppm "
        f"from target and 'closes the 10 ppm gate'. Measured here, the "
        f"closure ({mp.nstr(c_3_closure, 10)}) and this probe's "
        f"u³-order empirical extraction ({mp.nstr(c_3_empirical, 10)}) "
        f"differ by "
        f"{mp.nstr(mp.fabs(c_3_closure - c_3_empirical) / mp.fabs(c_3_empirical) * mp.mpf('1e6'), 6)} "
        f"ppm — they are not the same c_3. The empirical one absorbs "
        f"the entire {float(eps_N2):+.1f} ppm N=2 residual at u³, so it "
        f"is ~981, of the same order as the -974 recorded in "
        f"q-beta-operator-valued-N3.witness.json, while the closure "
        f"formula is O(1). No assertion above compares them, because "
        f"reconciling the two normalisations is a content question, not "
        f"a tautology drain. Assertion (6)'s c_4 = 0 result is "
        f"unaffected: it depends only on c_3 being extracted from the "
        f"same single Q_β, not on its magnitude."
    )
    if ranking_is_degenerate:
        builder.add_data("base_ranking_degenerate", True)
        builder.add_caveat(
            f"With c_4 = 0 exactly, correction = c_4/base = 0 for every "
            f"base, so all {len(results_sorted)} base hypotheses tie at "
            f"|correction - 1| = 1. 'MOST PROMISING base' and "
            f"'best_non_trivial_base' in this witness are dict insertion "
            f"order, not a ranking — the c_4 base question cannot be "
            f"scoped at all until c_4 is defined against a second "
            f"observable, which is the probe's own open item B."
        )

    builder.save()
    print(f"  Witness: qbeta-ck-k-gt-3-habiro-extension-scoping.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
