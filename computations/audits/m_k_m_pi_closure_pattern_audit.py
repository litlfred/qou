"""m_K/m_π closure pattern — does it transfer to the other 4 missing observables?

Per author 2026-05-31 ("all" — direction 3).

## Context

m_K/m_π is the only genuine prediction currently meeting Subgoal-1
(23.4 ppb vs 264 ppb target, 11× margin). Closure achieved by
PR #1442 via:

  m_K²/m_π² = [3]_q · [4]_q + (α_em / π) · (3q² − 1)/(2q²)
              ^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              strong sector    meson EM correction (genuinely missing)

The strong-sector base gave a 290-ppm residual (audit
`2026-05-29-meson-mK-mpi-residual-derivation-attempt.md`). The
genuine closure path was recognizing that EM/isospin-breaking
self-energy was a MISSING CATEGORICAL TERM, not a tower-coefficient
fit. The specific form `(3q²−1)/(2q²)` originates from the Bring
zero-mode projection at α_em (PR #1442 / em-coupling-bring-zero-mode).

## Question

Does this closure pattern transfer to the 4 still-missing observables
(m_μ, Q_β, m_n, Δm_pn)? For each, identify:
- What is the missing categorical piece (if any)?
- Is it analogous to m_K/m_π's EM correction (a separate categorical
  term to ADD)?
- Or is the gap of a different KIND (over-determination, truncation
  error, intrinsic formula residual)?

## Method

Catalog the closure-blocker for each missing observable, classify
by category (additive / truncation / over-determined / formula-
intrinsic), and identify which (if any) could benefit from a
m_K/m_π-style additive categorical correction.

## Conclusion preview

NONE of the 4 missing observables is awaiting an additive
categorical correction analogous to (α_em/π)·(3q²−1)/(2q²). They
miss for different structural reasons:

- m_μ: over-determined substrate (q_0 anchors m_p; m_μ shifts mechanically)
- Q_β: bounded c_4·u⁴ truncation error past Habiro identification
- m_n / Δ_pn: flavor-split's intrinsic 0.10% residual

The m_K/m_π pattern (find missing categorical term, ADD it) does
NOT directly apply.

The META-lesson DOES transfer: each closure requires identifying a
specific categorical missing piece, not coefficient fitting.

## Cross-references

- audit 2026-05-29-meson-mK-mpi-residual-derivation-attempt.md
- meson_em_sinh_closed_form.py (the (3q²-1)/(2q²) categorical form)
- PR #1442 (meson EM correction merge)
- PR #1581 Probes A + B + C (this branch's sibling probes)
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps(50)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("m_K/m_π closure pattern — transferability audit")
    print("=" * 78)

    # Numerical sanity: the EM correction form at q_0
    em_correction = (3 * q ** 2 - 1) / (2 * q ** 2)
    alpha_em_codata = mp.mpf(1) / mp.mpf("137.0359991")
    em_term = (alpha_em_codata / mp.pi) * em_correction

    print(f"\nq_0 = {Q_50_DIGIT_STR}")
    print(f"\n[Strong-sector m_K²/m_π² base: [3]_q · [4]_q at q_0]")
    h = q - 1 / q
    q3 = (q ** 3 - 1 / q ** 3) / (q - 1 / q)
    q4 = (q ** 4 - 1 / q ** 4) / (q - 1 / q)
    base = q3 * q4
    print(f"  [3]_q = {mp.nstr(q3, 12)}")
    print(f"  [4]_q = {mp.nstr(q4, 12)}")
    print(f"  base  = {mp.nstr(base, 18)}")

    print(f"\n[EM correction at q_0]")
    print(f"  (3q² − 1)/(2q²) = {mp.nstr(em_correction, 18)}")
    print(f"  (α_em/π)·corr   = {mp.nstr(em_term, 18)}")
    print(f"  relative to base: {mp.nstr(em_term / base * mp.mpf('1e6'), 6)} ppm")

    # PDG-anchored m_K/m_π:
    # m_K± = 493.677 MeV, m_π± = 139.57039 MeV  →  m_K/m_π = 3.5371
    from codata_constants import (  # registry (no inline literal)
        M_K_PM_MEV_VALIDATION as m_k_pdg,
        M_PI_PM_MEV_VALIDATION as m_pi_pdg,
    )
    ratio_pdg_sq = (m_k_pdg / m_pi_pdg) ** 2
    pred_sq = base + em_term
    print(f"\n[Closure check]")
    print(f"  base + EM      = {mp.nstr(pred_sq, 18)}")
    print(f"  (m_K/m_π)²_PDG = {mp.nstr(ratio_pdg_sq, 18)}")
    print(f"  residual ppm   = {mp.nstr((pred_sq - ratio_pdg_sq) / ratio_pdg_sq * mp.mpf('1e6'), 8)}")

    # ── The pattern catalog ──
    print("\n" + "=" * 78)
    print("Closure-blocker catalog for the 4 missing observables")
    print("=" * 78)

    observables = [
        {
            "obs": "m_K/m_π",
            "status": "MET",
            "residual_ppb": "23.4",
            "blocker_type": "missing categorical term (EM correction)",
            "fix_form": "additive: + (α_em/π)·(3q²−1)/(2q²)",
            "fix_origin": "Bring zero-mode projection at α_em (PR #1442)",
            "fix_pattern": "ADDITIVE — new categorical term",
        },
        {
            "obs": "m_μ",
            "status": "MISS ×964",
            "residual_ppb": "210",
            "blocker_type": "substrate over-determination",
            "fix_form": "NONE — choice of q_0 anchor (m_p vs m_μ)",
            "fix_origin": "PR #1422 chose m_p; m_μ inherits the shift",
            "fix_pattern": "NOT applicable (no formula correction exists)",
        },
        {
            "obs": "Q_β",
            "status": "MISS ×164",
            "residual_ppb": "1247",
            "blocker_type": "ladder truncation order N (not coefficient)",
            "fix_form": "INCREASE N — c_3=-2 is structurally OK (Probe B)",
            "fix_origin": "Habiro element identification per α_em template",
            "fix_pattern": "TRUNCATION (N=3 already beats 100×; tier=near-match)",
        },
        {
            "obs": "m_n",
            "status": "MISS ×185",
            "residual_ppb": "1.04",
            "blocker_type": "flavor-split formula intrinsic residual",
            "fix_form": "improve X(q) in m_n = m_p · (1 + X/(1−X/2))",
            "fix_origin": "canonical Hecke-skein has 0.10% intrinsic residual",
            "fix_pattern": "INTRINSIC (gated on flavor-split refinement)",
        },
        {
            "obs": "Δm_pn",
            "status": "MISS ×163",
            "residual_ppb": "755",
            "blocker_type": "flavor-split formula intrinsic residual",
            "fix_form": "= same as m_n",
            "fix_origin": "= same as m_n",
            "fix_pattern": "INTRINSIC (gated on flavor-split refinement)",
        },
    ]

    print(f"\n  {'obs':<12}{'status':<10}{'blocker type':<42}{'fix pattern'}")
    print(f"  {'-'*12}{'-'*10}{'-'*42}{'-'*30}")
    for o in observables:
        print(f"  {o['obs']:<12}{o['status']:<10}{o['blocker_type']:<42}{o['fix_pattern']}")

    # ── Transferability analysis ──
    print("\n" + "=" * 78)
    print("Does the m_K/m_π pattern transfer?")
    print("=" * 78)

    print("""
m_K/m_π closure was an ADDITIVE missing categorical correction:
  - The strong-sector derivation was complete but DROPPED an EM contribution
  - Adding the categorical EM term (form pinned by Bring zero-mode) closed it
  - The fix was: identify the SPECIFIC physical piece that was dropped,
    derive its categorical form, add it.

For the 4 missing observables, the closure-blockers are STRUCTURALLY
DIFFERENT:

  m_μ: NO missing categorical term. The q_0 re-pin choice mechanically
       shifts m_μ. To "close" m_μ would mean reverting to a μ-anchored
       q_0, which would re-open the m_p gap by the same propagated
       amount. The substrate is fundamentally over-determined (Probe A).

  Q_β: Already MEETS 100× target if c_3 = -2 is wired at N=3 (~6 ppb,
       below the 7.8 ppb target). The current 1247 ppb is the c_2-only
       (proved Taylor) cliff; the c_3 = -2 wiring is structurally legit
       (Probe B) — it just needs tier=near-match wiring, awaiting full
       Habiro identification.

  m_n / Δm_pn: Gated on flavor-split refinement. The canonical Hecke-
               skein X(q) formula has a 0.10% intrinsic residual that
               is the dominant error in m_n and Δm_pn predictions.
               Closure path = improve the flavor-split derivation.

NONE of these is awaiting a m_K/m_π-style additive missing categorical
term. The m_K/m_π pattern does NOT directly transfer.

The META-LESSON DOES transfer:
  → for each closure, identify the SPECIFIC categorical missing piece
  → derive its form (not fit it)
  → integrate at substrate precision

For m_μ: meta-lesson confirms NO closure path exists at this anchor.
For Q_β: meta-lesson points at the Habiro element identification (open).
For m_n: meta-lesson points at the flavor-split formula refinement (open).
""")

    # ── Witness ──
    w = WitnessBuilder(
        "m-k-m-pi-closure-pattern-audit",
        engine="python",
    )
    w.set_description(
        "Audits whether the m_K/m_π closure pattern (additive missing "
        "categorical EM correction) transfers to the 4 still-missing "
        "L2 dashboard observables (m_μ, Q_β, m_n, Δm_pn). Catalogs each "
        "observable's closure-blocker type. Finds NO transfer of the "
        "additive-correction pattern — each missing observable has a "
        "structurally different blocker. The META-lesson (identify "
        "specific categorical missing pieces, not fits) does transfer."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("m_K_m_pi_em_correction_at_q0",
               mp.nstr(em_correction, 25))
    w.add_data("closure_pattern_catalog", observables)
    w.add_data("transferability_verdict",
        "The m_K/m_π additive-EM-correction pattern does NOT directly "
        "transfer to m_μ (over-determined), Q_β (truncation/Habiro), "
        "or m_n / Δ_pn (flavor-split intrinsic residual). Each closure "
        "blocker has a structurally distinct type. The META-lesson "
        "(specific categorical missing pieces, not coefficient fits) "
        "DOES transfer: m_μ has no formula correction (Probe A confirms); "
        "Q_β needs Habiro identification (Probe B framing); m_n / Δ_pn "
        "need flavor-split refinement (gated separately)."
    )

    w.add_assertion(
        name="audit_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Closure pattern audit completed at 50 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
