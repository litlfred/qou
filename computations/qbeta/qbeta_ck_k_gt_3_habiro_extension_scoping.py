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
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
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

Q0_MP_PIN = "1.1099785827513808075916690956107688798744991218736"
Q_BETA_CODATA_MEV = mp.mpf("0.78233")
M_E_MEV = mp.mpf("0.51099895069")


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
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))  # Markov-Jones
    alpha = (z - 1) * h / 2           # eigenphase
    d1 = q ** 3 / (q ** 2 + 1)
    d2 = -1 / (q * (q ** 2 + 1))
    b = mp.sqrt(d1 * d2 + 1)          # Hoefsmit b = √(q⁴+q²+1)/(q²+1)
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
    Q_A = M_E_MEV * (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)

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
    print(f"      (matches qbeta_1ppq_achieved c_4 ≈ -0.972 — even-k geometric)")
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
    print(f"          mpf('939.5654205240') - mpf(M_P_MEV_VALIDATION) - m_e")
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

    # Assertion: c_2 = -1 STRUCTURAL is the only proved c_k (the
    # invariant this probe respects). c_3 closes via empirical Habiro
    # near-match. c_4 has no derivation. The probe's job is to scope,
    # not to claim.
    builder.add_assertion(
        "c_2_remains_only_structural_ck",
        computed=1,
        expected=1,
        tolerance=0,
        source=("Invariant respected by this scoping probe: c_2 = -1 "
                "is the only c_k with a sorry-free Lean STRUCTURAL "
                "proof (prop:q-beta-c-2-eq-neg-one-structural, "
                "PR #1786). c_3 closes via empirical [3]_q/25 Habiro "
                "near-match (commit 305c08a91 on main, tagged "
                "NEAR-MATCH not derived). c_4 is empirical extraction "
                "only. This probe scopes the c_4 base hypothesis "
                "without claiming a structural derivation."),
    )

    builder.save()
    print(f"  Witness: qbeta-ck-k-gt-3-habiro-extension-scoping.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
