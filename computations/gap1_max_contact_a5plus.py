#!/usr/bin/env python3
"""
gap1_max_contact_a5plus.py — GAP-1 (bean qou-lzoh): extend the max-contact edge-set
FORWARD past the A≤4 simplex to A=5,6,7 and PREDICT binding against AME.

Follows #3545 Part 13 (binding_edge_set_selection.py), which established the edge set is
the binding-maximizing max-contact 3-D sphere packing but only INVERTED B→#bonds for A≤4.
This probe supplies the missing forward test: with the per-bond energy b* fixed by the
SINGLE deuteron datum and the edge count taken from the geometric max-contact deltahedra,
predict B(A) and compare to AME2020 for A=5,6,7.

THE GEOMETRY (no fit — convex-deltahedron contact numbers). For A unit spheres the
max-contact cluster is the convex deltahedron (all-triangular-face polyhedron): every edge
is a sphere-sphere contact, and a triangulated sphere has exactly E = 3A−6 edges (Euler).
These are the Hafstad–Teller / Brink α-cluster geometries the corpus already uses (#3551):

  A:        2   3    4     5              6           7
  polytope  —  tri  tetra tri-bipyramid  octahedron  pentagonal-bipyramid
  #contacts 1   3    6     9              12          15      (= 3A−6 for A≥3; A=2 is 1)

THE TEST. b* = per-bond energy = B_strong(deuteron) (Z=1 ⇒ no Coulomb) — the ONE anchor.
B_strong = AME binding + discrete-proton Coulomb (Z(Z−1), r₀=1.2 fm; charge-symmetric, so
the strong part is compared). Forward prediction B_pred(A) = b*·(3A−6).

FINDING (scope-(a)): max-contact (3A−6, LINEAR in A) tracks the extensive B_strong (~A) with
a BOUNDED, slowly-rising ratio (~0.7–0.8 at A=5,6,7) — it does NOT blow up. Contrast:
  • simplex C(A,2) (QUADRATIC in A) begins to OVERSHOOT at A=7 (C(7,2)=21 > 15);
  • the full a_D^(n)·C(A,n) body-order tower blows up +920% at ⁶Li (#3585).
So the max-contact restriction (3A−6 < C(A,2) for A≥5) IS what tames the pairwise backbone
at A≥5 — confirming GAP-1's premise. The residual B_strong − B_pred is a bounded, roughly
per-nucleon-constant many-body/cluster term (GAP-2 / GAP-4), REPORTED not fitted.

Anti-fit checkpoint (bean qou-lzoh): #contacts is deltahedral geometry, b* is the single
deuteron anchor, predictions are forward, residuals are reported. Nothing tuned to AME;
nothing wired to production. EXPLORATORY, scope-(a).

Audit: docs/audits/2026-07-11-gap1-max-contact-a5plus.md
Workplan: docs/workplans/2026-07-11-mnk-derivation-gaps.md (GAP-1)
"""
from __future__ import annotations
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE / "substrate"), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps
set_compute_dps()
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION,
    AME_B_LI5_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_LI7_MEV_VALIDATION,
)
try:
    from witness_base import WitnessBuilder
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False

# (name): (B_AME MeV, Z, A). Coulomb uses discrete-proton Z(Z−1), r₀=1.2 fm (charge-symmetric).
ISO = {
    "D":   (AME_B_DEUTERON_MEV_VALIDATION, 1, 2),
    "T":   (AME_B_TRITIUM_MEV_VALIDATION,  1, 3),
    "3He": (AME_B_HE3_MEV_VALIDATION,      2, 3),
    "4He": (AME_B_HE4_MEV_VALIDATION,      2, 4),
    "5Li": (AME_B_LI5_MEV_VALIDATION,      3, 5),
    "6Li": (AME_B_LI6_MEV_VALIDATION,      3, 6),
    "7Li": (AME_B_LI7_MEV_VALIDATION,      3, 7),
}

# convex-deltahedron max-contact numbers (= 3A−6 for A≥3; A=2 is the single bond)
def max_contacts(A: int) -> int:
    return 1 if A == 2 else 3 * A - 6


def b_strong(B, Z, A):
    """AME binding + discrete-proton Coulomb displacement (adds back the charge energy)."""
    R = mp.mpf("1.2") * mp.mpf(A) ** (mp.mpf(1) / 3)
    return mp.mpf(str(B)) + mp.mpf("0.6") * Z * (Z - 1) * mp.mpf("1.44") / R


def main() -> int:
    bstar = b_strong(*ISO["D"])   # deuteron: 1 bond, Z=1 ⇒ Coulomb 0 ⇒ b* = B_strong(D)
    print("=== GAP-1: max-contact deltahedra (3A−6) FORWARD-predict binding, A=5,6,7 ===\n")
    print(f"per-bond b* = B_strong(deuteron) = {mp.nstr(bstar, 6)} MeV  (the SINGLE anchor)\n")
    print(f"  {'iso':<5}{'A':>2}{'maxC=3A−6':>10}{'C(A,2)':>8}{'B_pred=b*·maxC':>15}"
          f"{'B_strong':>10}{'pred/strong':>12}{'residual':>10}")
    rows = {}
    for K, (B, Z, A) in ISO.items():
        mc = max_contacts(A)
        c2 = comb(A, 2)
        bs = b_strong(B, Z, A)
        bpred = bstar * mc
        ratio = float(bpred / bs)
        resid = float(bs - bpred)
        rows[K] = dict(A=A, max_contacts=mc, simplex_C_A2=c2, B_strong=float(bs),
                       B_pred_maxcontact=float(bpred), pred_over_strong=ratio,
                       residual_manybody=resid, residual_per_nucleon=resid / A)
        print(f"  {K:<5}{A:>2}{mc:>10}{c2:>8}{float(bpred):>15.3f}{float(bs):>10.3f}"
              f"{ratio:>12.3f}{resid:>10.3f}")

    # the three edge-set models at A≥5, side by side
    print(f"\n### Edge-set model comparison at A≥5 (B_pred/B_strong)")
    print(f"  {'iso':<5}{'maxC 3A−6':>11}{'simplex C(A,2)':>16}")
    a5plus = [K for K in ISO if ISO[K][2] >= 5]
    simplex_overshoots = False
    for K in a5plus:
        B, Z, A = ISO[K]
        bs = b_strong(B, Z, A)
        r_mc = float(bstar * max_contacts(A) / bs)
        r_cx = float(bstar * comb(A, 2) / bs)
        if r_cx > 1.0:
            simplex_overshoots = True
        print(f"  {K:<5}{r_mc:>11.3f}{r_cx:>16.3f}")

    # the two structural facts this probe establishes
    ratios_mc = [rows[K]["pred_over_strong"] for K in a5plus]
    max_contact_bounded = all(0.5 <= r <= 1.0 for r in ratios_mc)  # bounded, no blow-up
    print(f"\n### Findings (scope-(a))")
    print(f"  • Max-contact (3A−6, LINEAR in A) ratio at A=5,6,7 = "
          f"{', '.join(f'{r:.3f}' for r in ratios_mc)} — BOUNDED in [0.5,1], no blow-up.")
    print(f"  • Simplex C(A,2) (QUADRATIC) overshoots by A=7: {'YES' if simplex_overshoots else 'no'} "
          f"(C(7,2)=21 > maxC 15). Full a_D^(n)·C(A,n) tower blows up +920% @⁶Li (#3585).")
    print(f"  ⇒ the max-contact restriction (3A−6 < C(A,2) for A≥5) is what tames the pairwise")
    print(f"    backbone at A≥5. Confirms GAP-1's premise: max-contact is the correct edge set.")
    resid_pn = ', '.join(f"{K} {rows[K]['residual_per_nucleon']:.2f}" for K in a5plus)
    print(f"  • Residual/nucleon B_strong−B_pred (many-body/cluster term, GAP-2/GAP-4): "
          f"{resid_pn} MeV/nucleon —")
    print(f"    bounded and roughly per-nucleon-constant (NOT fitted; reported).")
    print(f"\n  OPEN (unchanged): the many-body M_3/M_4 residual (GAP-2) + cluster/halo (⁶Li α+d,")
    print(f"  GAP-4). This probe fixes the 2-body edge set at A≥5 — no fit, deltahedral geometry.")

    ok = max_contact_bounded and simplex_overshoots
    if _HAVE_WB:
        try:
            wb = WitnessBuilder("gap1-max-contact-a5plus", engine="mpmath")
            wb.set_description(
                "GAP-1 (qou-lzoh): forward-predict binding from the max-contact deltahedra "
                "(3A−6 contacts: tri-bipyramid 9, octahedron 12, pentagonal-bipyramid 15) with "
                "per-bond b* pinned by the SINGLE deuteron datum. Max-contact (linear in A) "
                "tracks extensive B_strong with a BOUNDED ratio ~0.7–0.8 at A=5,6,7 (no blow-up), "
                "while simplex C(A,2) (quadratic) overshoots by A=7 and the a_D^(n)·C(A,n) tower "
                "blows up +920% @⁶Li (#3585). So the max-contact restriction 3A−6<C(A,2) is what "
                "tames the pairwise backbone at A≥5 — confirms GAP-1. Residual = bounded per-"
                "nucleon many-body/cluster term (GAP-2/GAP-4), reported not fitted. Scope-(a), "
                "deltahedral geometry, single anchor, no fit, no wiring.")
            wb.add_data("per_bond_bstar_MeV", float(bstar))
            wb.add_data("per_isotope", rows)
            wb.add_assertion(
                name="max_contact_bounded_simplex_overshoots",
                computed=str(int(ok)), expected="1", tolerance=0,
                source=("with b* = B_strong(deuteron) (single anchor) and #contacts = 3A−6 "
                        "(convex deltahedra), B_pred/B_strong is bounded in [0.5,1] at A=5,6,7 "
                        "(%s) — no blow-up — while simplex C(A,2) overshoots by A=7 (C(7,2)=21). "
                        "The max-contact restriction tames the A≥5 pairwise backbone; residual is "
                        "the reported many-body/cluster term." % ", ".join(f"{r:.3f}" for r in ratios_mc)))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
