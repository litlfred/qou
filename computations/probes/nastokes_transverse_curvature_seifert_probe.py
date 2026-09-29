#!/usr/bin/env python3
"""Transverse NA-Stokes surface-curvature — forward Seifert-Betti magnitude vs AME.

qou-prjo LEAD-2 (geometric route). Forward, geometric, ZERO-FIT test of the
surviving deuteron-binding-magnitude carrier: the transverse surface-curvature
pairing Ω₂ = ½ P ∮∮ [𝓕,𝓕] on the Seifert surface of each isotope's binding
channel. Companion to the sorry-free Lean structure
  folio/quantum-observable-universe/lean/QOU/MassTheory/TransverseSurfaceCurvature.lean
and the audit docs/audits/2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md.

CONTEXT (read first):
  * docs/audits/2026-07-24-eunit-magnus-order2.md §2 — the transverse pairing is
    the one order-2 candidate that survives on the single-generator σ₁³ deuteron
    channel (it is transverse to the strand ordering, not an inter-crossing
    commutator). WALL: "needs a canonical discretization of the Yekutieli surface
    2-form on the trefoil Seifert surface — data the corpus lacks."
  * docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md
    §4 — the missing many-body term is additive, EXTENSIVE (∝A), super-pairwise
    (≥3-body); pairwise cap ρ_A ≤ C(A,2) proved.
  * docs/audits/2026-08-02-brane-resummation-nastokes-volume-difference.md — the
    na-Stokes ℏ⁰ leg diverges, the ℏ² leg undershoots ~450×; the correct kernel
    is bracketed between. (This probe reproduces the SAME bracketing at the
    surface-Betti level.)

FORWARD DEFINITION (committed BEFORE looking at AME; no reading chosen to keep
the route alive):

  Seifert's algorithm on a connected positive-braid diagram β (s strands, c
  crossing letters) gives a surface with first Betti number
        b₁ = c − s + 1 = 2g          (g = genus).
  The transverse magnitude has two geometric envelopes:
    - DIAGONAL / additive (one κ² per independent handle):  M_diag ∝ b₁
    - OFF-DIAGONAL / full surface-ordered pairing (all handle-pair commutators,
      the upper envelope):                                    M_off  ∝ C(b₁, 2)
  The TRUE magnitude sits between, set by the transport twists U(x,O) across the
  surface — the missing surface-2-form data (the wall).

GEOMETRIC INPUTS (pure geometry — NOT fitted to T/³He/⁴He):
  * deuteron pn channel = trefoil σ₁³:  s=2, c=3  ⇒  b₁ = 2  (the anchor unit).
  * inter-nucleon links = spanning tree of A nucleons ⇒ L = A−1 links
    (the color-tube audit's "A−1 inter-nucleon Hecke generators").
  * each link carries one trefoil-genus unit b₁_link = 2 (the deuteron's own
    value) ⇒ b₁(A) = 2·(A−1).

AME is used ONLY as fixed comparison ratios (B(iso)/B(D)); never inverted,
nothing tuned, 0 free parameters. This is a derive-then-check, not a fit.
"""
from __future__ import annotations

import sys
from math import comb
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from substrate.witness_base import WitnessBuilder  # noqa: E402
from fractions import Fraction  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import set_compute_dps, str_at_true_precision  # noqa: E402

set_compute_dps(50)


def _mpf(x):
    """mpf view of an mpf or an exact Fraction.

    The combinatorial ratios are exact Fractions and the AME ratios are mpf;
    Python will not compare the two directly. Converting the Fraction (exact
    numerator and denominator) to mpf at the working precision loses nothing
    a 50-dps comparison could see, and it keeps the bracketing test off f64.
    """
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / mp.mpf(x.denominator)
    return mp.mpf(x)
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)


def betti_one(strands: int, crossings: int) -> int:
    """b₁ = c − s + 1 of the Seifert surface (mirrors Lean seifertBettiOne)."""
    return crossings - strands + 1


def main() -> None:
    # ---- forward geometry (committed before AME comparison) --------------------
    # deuteron trefoil anchor
    s_tref, c_tref = 2, 3
    b1_link = betti_one(s_tref, c_tref)          # = 2  (per-link genus unit)
    assert b1_link == 2

    # The AME constants are mpf; float()-ing them here capped the only
    # measured quantity in this probe at 17 digits before it was used.
    isotopes = {  # A, AME binding (validation MeV)
        "D":  (2, mp.mpf(AME_B_DEUTERON_MEV_VALIDATION)),
        "T":  (3, mp.mpf(AME_B_TRITIUM_MEV_VALIDATION)),
        "3He": (3, mp.mpf(AME_B_HE3_MEV_VALIDATION)),
        "4He": (4, mp.mpf(AME_B_HE4_MEV_VALIDATION)),
    }
    B_D = isotopes["D"][1]

    rows = {}
    for iso, (A, B) in isotopes.items():
        links = A - 1                            # spanning-tree inter-nucleon links
        b1 = b1_link * links                     # = 2(A−1)  (pure geometry)
        m_diag = b1                              # ∝ b₁            (additive env.)
        m_off = comb(b1, 2) if b1 >= 2 else 0    # ∝ C(b₁,2)       (upper env.)
        # diag/off are INTEGER over INTEGER — pure combinatorics, exact.
        rows[iso] = {
            "A": A, "links": links, "betti_one": b1,
            "ame_MeV": B,
            "ratio_ame_to_D": B / B_D,
            "ratio_diag_to_D": Fraction(m_diag, b1_link),   # M_diag(A)/M_diag(D)
            "ratio_off_to_D": (Fraction(m_off, comb(b1_link, 2))
                               if comb(b1_link, 2) else Fraction(0)),
        }

    # normalize both envelopes so D = 1, compare to AME ratio
    print("=" * 78)
    print("TRANSVERSE SURFACE-CURVATURE — forward Seifert-Betti magnitude vs AME")
    print("=" * 78)
    print(f"  {'iso':4s}{'A':>3s}{'links':>7s}{'b1=2g':>7s}"
          f"{'AME/D':>9s}{'diag/D':>9s}{'off/D':>9s}   verdict")
    for iso, r in rows.items():
        ame = r["ratio_ame_to_D"]
        dia = r["ratio_diag_to_D"]
        off = r["ratio_off_to_D"]
        dia_m, off_m, ame_m = _mpf(dia), _mpf(off), _mpf(ame)
        bracketed = dia_m <= ame_m <= off_m or off_m <= ame_m <= dia_m
        print(f"  {iso:4s}{r['A']:>3d}{r['links']:>7d}{r['betti_one']:>7d}"
              f"{float(ame_m):>9.3f}{float(dia_m):>9.3f}{float(off_m):>9.3f}   "
              f"{'AME bracketed [diag,off]' if bracketed else 'NOT bracketed'}")

    # ---- forward structural findings (facts, not fits) ------------------------
    # 1. additive envelope undershoots 4He; off-diagonal overshoots ⇒ AME between.
    he4 = rows["4He"]
    additive_undershoots_he4 = _mpf(he4["ratio_diag_to_D"]) < _mpf(he4["ratio_ame_to_D"])
    offdiag_overshoots_he4 = _mpf(he4["ratio_off_to_D"]) > _mpf(he4["ratio_ame_to_D"])
    ame_bracketed_he4 = additive_undershoots_he4 and offdiag_overshoots_he4

    # 2. additive envelope is EXACTLY linear in links (pairwise cap;
    #    mirrors Lean seifertBettiOne_link_additive). Check b1(A) = 2(A-1).
    additive_linear = all(
        rows[i]["betti_one"] == 2 * (rows[i]["A"] - 1) for i in rows
    )

    # 3. isospin blindness: T and 3He (both A=3) get identical geometric
    #    prediction, but AME differs (the p/n mirror split) ⇒ genus/Betti
    #    topology ALONE cannot reproduce the T vs 3He splitting.
    t_he3_same_geometry = (
        rows["T"]["betti_one"] == rows["3He"]["betti_one"]
    )
    t_he3_ame_differ = abs(
        rows["T"]["ratio_ame_to_D"] - rows["3He"]["ratio_ame_to_D"]
    ) > mp.mpf("0.05")

    print()
    print("  FINDINGS (forward, no fit):")
    print(f"   1. additive (diagonal) envelope undershoots 4He: "
          f"{float(_mpf(he4['ratio_diag_to_D'])):.2f} < "
          f"{float(_mpf(he4['ratio_ame_to_D'])):.2f}  "
          f"= {additive_undershoots_he4}")
    print(f"   2. off-diagonal envelope overshoots 4He: "
          f"{float(_mpf(he4['ratio_off_to_D'])):.2f} > "
          f"{float(_mpf(he4['ratio_ame_to_D'])):.2f}  "
          f"= {offdiag_overshoots_he4}")
    print(f"   3. AME magnitude BRACKETED between the two envelopes at 4He: "
          f"{ame_bracketed_he4}")
    print(f"   4. additive envelope exactly linear in links (pairwise cap): "
          f"{additive_linear}")
    print(f"   5. T and 3He identical geometry but AME differs (isospin-blind): "
          f"{t_he3_same_geometry and t_he3_ame_differ}")
    print()
    print("  VERDICT (scope-(a), honest): NO CLOSURE. Neither geometric envelope")
    print("  reproduces the AME ratios — the additive/diagonal reading undershoots")
    print("  (pairwise-capped, cannot be the ≥3-body term), the off-diagonal")
    print("  reading overshoots. AME sits BETWEEN them, exactly mirroring the")
    print("  na-Stokes ℏ⁰(diverge)/ℏ²(undershoot) bracketing. The true magnitude")
    print("  needs the transport weighting across the surface = the missing")
    print("  surface-2-form data (the wall, Lean-formalized).")

    # ---- witness -------------------------------------------------------------
    wb = WitnessBuilder("nastokes-transverse-curvature-seifert", engine="python")
    wb.set_description(
        "Forward Seifert-Betti magnitude of the transverse NA-Stokes surface "
        "curvature (qou-prjo geometric route), vs AME as fixed ratios. b₁ = "
        "c−s+1; deuteron trefoil anchor b₁=2; links = A−1; b₁(A)=2(A−1). "
        "Diagonal (∝b₁) undershoots 4He, off-diagonal (∝C(b₁,2)) overshoots; "
        "AME bracketed between. Additive envelope exactly linear (pairwise cap). "
        "T vs 3He splitting invisible (isospin-blind). NO CLOSURE (scope-(a)); "
        "magnitude needs the missing transport/surface-2-form data. No fit, no "
        "AME inversion, 0 free parameters."
    )
    wb.set_audit_only(
        "docs/audits/2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md"
    )
    wb.add_parameter("betti_link_unit_trefoil", b1_link)
    wb.add_parameter("link_count_model", "spanning tree, L = A-1")
    # Serialize at the sink: mpf keeps its 50 dps, the two combinatorial
    # ratios keep their exactness as "p/q". Neither was ever a float64
    # measurement, and neither is one now.
    wb.add_data("per_isotope", {
        iso: {
            "A": r["A"], "links": r["links"], "betti_one": r["betti_one"],
            "ame_MeV": str_at_true_precision(r["ame_MeV"]),
            "ratio_ame_to_D": str_at_true_precision(r["ratio_ame_to_D"]),
            "ratio_diag_to_D": f"{r['ratio_diag_to_D'].numerator}"
                               f"/{r['ratio_diag_to_D'].denominator}",
            "ratio_off_to_D": f"{r['ratio_off_to_D'].numerator}"
                              f"/{r['ratio_off_to_D'].denominator}",
        }
        for iso, r in rows.items()
    })
    wb.add_caveat(
        "AME used ONLY as comparison ratios; never inverted. The link count "
        "(A-1) and per-link b₁=2 (trefoil) are pure geometry, not fitted."
    )
    wb.add_caveat(
        "The two envelopes (diagonal ∝b₁, off-diagonal ∝C(b₁,2)) bracket the "
        "true magnitude; the interpolating weight is the transport U(x,O) across "
        "the Seifert surface — the canonical surface-2-form discretization the "
        "corpus lacks (bean qou-prjo wall)."
    )
    wb.add_assertion("deuteron_trefoil_betti_one_is_2",
                     computed=b1_link, expected=2)
    wb.add_assertion("additive_diagonal_undershoots_he4",
                     computed=str(additive_undershoots_he4), expected="True")
    wb.add_assertion("offdiagonal_overshoots_he4",
                     computed=str(offdiag_overshoots_he4), expected="True")
    wb.add_assertion("ame_bracketed_between_envelopes_he4",
                     computed=str(ame_bracketed_he4), expected="True")
    wb.add_assertion("additive_envelope_exactly_linear_pairwise_cap",
                     computed=str(additive_linear), expected="True")
    wb.add_assertion("t_vs_he3_isospin_blind",
                     computed=str(t_he3_same_geometry and t_he3_ame_differ),
                     expected="True")
    out = wb.save()
    print(f"\n  witness → {out}")


if __name__ == "__main__":
    main()
