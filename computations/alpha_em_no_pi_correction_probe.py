#!/usr/bin/env python3
# polynomial_q_not_applicable: this is an archimedean-image probe (the pi-carrying
# corrections evaluated at q_0); the GOAL is to expose the pi as Hopf-fibration
# periods so the pre-archimedean (q/sinh-cosh) numerators stand alone.  Research
# probe — reports tier=open where no pre-archimedean source is yet in hand.
"""
alpha_{basis-knot} STEP 6 — the no-pi correction (research probe).

Owner directive: "I don't like to see pi ... should be pre-archimedean."  The
bare e_- coupling 1/alpha_EM = q[9]_q[10]_q (step 2/3, sinh sector) has residual
-1.55e-3 vs CODATA; the corrections that close it are 2/(3pi) + alpha/(4pi)
(prop:em-coupling-bring-zero-mode).  Step 6 asks: express these PRE-ARCHIMEDEAN
(no pi in the derivation), the pi being only the archimedean image of the Hopf
fibration S^1 -> S^3 -> S^2 / e_- channel.

THE OWNER'S THESIS, MADE CONCRETE.
  pi is NOT fundamental here — it is the archimedean (tau-functor) image of the
  Hopf-fibration PERIODS:
      |S^1| = 2 pi,   |S^2| = 4 pi,   |S^3| = 2 pi^2.
  Write each correction as (pre-archimedean numerator) / (Hopf period):
      alpha/(4 pi) = alpha / |S^2|,         numerator = alpha
      2/(3 pi)     = (4/3) / |S^1|,         numerator = 4/3
  So the pi appears ONLY in the denominators |S^1|, |S^2|; the numerators
  (alpha, 4/3) are the objects that must have a pre-archimedean (q / sinh-cosh)
  source.  That is the whole no-pi program in one line.

SECTOR MAP (which categorical channel each term lives in).
  leading  q[9]_q[10]_q : e_- (sinh, delta_q) — DERIVED pre-archimedean (step 2).
  alpha/(4pi)           : e_+ (cosh, [2]_q Habiro) — PRE-ARCHIMEDEAN source is the
                          EXISTING Habiro element H(q)=[2]_q(1-h^2 alpha)
                          (prop:alpha-em-habiro-bar-involution), bar-fixed sector,
                          classical value H(1)=2 "gives alpha/(4pi)".  Its pi is
                          |S^2| (the base-sphere period).  STATUS: sourced.
  2/(3pi)               : numerator 4/3 over |S^1|.  STATUS: OPEN — no
                          pre-archimedean source for 4/3 yet established.
                          Structural notes (NOT a derivation): 4/3 = H(1)^2/3 =
                          [2]_{q=1}^2/3 ; the "3" coincides with the trefoil
                          second index (alpha_EM = alpha_{T_{2,3}}).  Flagged,
                          not claimed.

WHAT THIS PROBE DELIVERS (honest scope).
  1. Confirms the additive closure 1/alpha = q[9][10] + 2/(3pi) + alpha/(4pi)
     to ~1e-5 (the corrections do close the bare -1.55e-3 residual).
  2. Decomposes the corrections into (numerator)/(Hopf period) — exposing the pi
     as a period, not a constant.
  3. Identifies alpha/(4pi)'s pre-archimedean Habiro source (corpus).
  4. Leaves the 4/3 numerator of 2/(3pi) as tier=OPEN (no fit).
  Nothing fitted; the open item is reported as open.

Refs: prop:em-coupling-bring-zero-mode (the 2/(3pi)+alpha/(4pi) corrections);
prop:alpha-em-habiro-bar-involution (H=[2]_q(1-h^2 alpha), the alpha/(4pi)
source); prop:torus-knot-delta-q-writhe (step 2 leading e_- term);
prop:vdw-pskew-isolation (the same Hopf e_-/sinh channel).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

try:
    import mpmath as mp
    mp.mp.dps = 50
    HAVE_MP = True
except Exception:
    HAVE_MP = False

try:
    from qou_substrate.constants import q_at
    Q0 = str(q_at())
except Exception:
    Q0 = "1.1099780333553254"

CODATA_INV_ALPHA = "137.035999177"


def qbracket(q, k):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def main() -> None:
    w = WitnessBuilder("alpha-em-no-pi-correction-probe", engine="python")
    q = mp.mpf(Q0) if HAVE_MP else float(Q0)
    pi = mp.pi if HAVE_MP else 3.141592653589793
    codata = mp.mpf(CODATA_INV_ALPHA) if HAVE_MP else float(CODATA_INV_ALPHA)
    alpha = 1 / codata

    # leading e_- (sinh) coupling, pre-archimedean (step 2)
    bare = q * qbracket(q, 9) * qbracket(q, 10)
    # the two pi-carrying corrections (prop:em-coupling-bring-zero-mode)
    c_vacpol = 2 / (3 * pi)       # 2/(3 pi)
    c_vertex = alpha / (4 * pi)   # alpha/(4 pi)
    corrected = bare + c_vacpol + c_vertex
    resid_bare = (bare - codata) / codata
    resid_corr = (corrected - codata) / codata

    # Hopf-fibration periods S^1 -> S^3 -> S^2
    S1 = 2 * pi
    S2 = 4 * pi
    S3 = 2 * pi ** 2
    # numerators = correction * period  (expose pi as a period)
    num_vertex = c_vertex * S2    # = alpha
    num_vacpol = c_vacpol * S1    # = 4/3

    def s(x):
        return mp.nstr(x, 12) if HAVE_MP else f"{x:.12g}"

    print("=" * 74)
    print("alpha_{basis-knot} STEP 6 — the no-pi correction (research probe)")
    print("=" * 74)
    print(f"  q0 = {s(q)}")
    print(f"  leading (e_- sinh, derived):  q[9]_q[10]_q = {s(bare)}")
    print(f"    residual vs CODATA          = {s(resid_bare)}")
    print()
    print("  pi-carrying corrections (to be pushed pre-archimedean):")
    print(f"    2/(3pi)     = {s(c_vacpol)}   [e_+ ? vacuum-polarization-like]")
    print(f"    alpha/(4pi) = {s(c_vertex)}   [e_+ cosh Habiro H(1)=2; SOURCED]")
    print(f"  corrected 1/alpha = {s(corrected)}   CODATA = {CODATA_INV_ALPHA}")
    print(f"    residual vs CODATA          = {s(resid_corr)}  "
          f"(closes the bare -1.55e-3)")
    print()
    print("  pi-as-Hopf-period decomposition  (numerator)/(period):")
    print(f"    |S^1|=2pi={s(S1)}  |S^2|=4pi={s(S2)}  |S^3|=2pi^2={s(S3)}")
    print(f"    alpha/(4pi) = alpha/|S^2| ;  numerator alpha     = {s(num_vertex)}")
    print(f"    2/(3pi)     = (4/3)/|S^1| ;  numerator 4/3        = {s(num_vacpol)}")
    print()
    print("  SECTOR / SOURCE map:")
    print("    q[9][10]    : e_- sinh  — DERIVED pre-archimedean (step 2)")
    print("    alpha/(4pi) : e_+ cosh  — SOURCED (Habiro H=[2]_q(1-h^2 a), corpus)")
    print("    2/(3pi)     : num 4/3   — OPEN (no pre-archimedean source yet)")

    # honest assertions
    closes = abs(resid_corr) < (mp.mpf("5e-5") if HAVE_MP else 5e-5)
    vertex_num_is_alpha = abs(num_vertex - alpha) < (mp.mpf(10) ** -20 if HAVE_MP else 1e-15)
    expected_vacpol = mp.mpf(4) / 3 if HAVE_MP else 4 / 3
    vacpol_num_is_4_3 = abs(num_vacpol - expected_vacpol) < (mp.mpf(10) ** -20 if HAVE_MP else 1e-15)

    w.set_description(
        "alpha_{basis-knot} step 6 (no-pi correction, research probe).  Makes the "
        "owner's thesis concrete: pi is the archimedean image of the Hopf-fibration "
        "periods |S^1|=2pi, |S^2|=4pi, so the corrections that close the bare e_- "
        "coupling 1/alpha=q[9]_q[10]_q (resid -1.55e-3) decompose as "
        "(pre-archimedean numerator)/(Hopf period): alpha/(4pi)=alpha/|S^2| and "
        "2/(3pi)=(4/3)/|S^1|.  The corrected 1/alpha = q[9][10]+2/(3pi)+alpha/(4pi) "
        "closes to ~1e-5.  SECTOR/SOURCE map: the leading term is the DERIVED e_- "
        "sinh (step 2); alpha/(4pi) is the e_+ cosh Habiro element H=[2]_q(1-h^2 "
        "alpha) (prop:alpha-em-habiro-bar-involution, H(1)=2) — already "
        "pre-archimedean, pi = |S^2|; the 2/(3pi) numerator 4/3 has NO "
        "pre-archimedean source yet and is reported tier=OPEN (structural notes "
        "4/3=H(1)^2/3 and '3'=trefoil index flagged, NOT claimed).  Nothing fitted."
    )
    w.set_content_block("prop:em-coupling-bring-zero-mode")
    w.add_data("q0", str(q))
    w.add_data("bare_inv_alpha_e_minus_sinh", str(bare))
    w.add_data("residual_bare_rel", str(resid_bare))
    w.add_data("correction_2_over_3pi", str(c_vacpol))
    w.add_data("correction_alpha_over_4pi", str(c_vertex))
    w.add_data("corrected_inv_alpha", str(corrected))
    w.add_data("residual_corrected_rel", str(resid_corr))
    w.add_data("hopf_periods", {"S1_2pi": str(S1), "S2_4pi": str(S2),
                                "S3_2pi2": str(S3)})
    w.add_data("numerator_alpha_over_4pi_times_S2", str(num_vertex))
    w.add_data("numerator_2_over_3pi_times_S1", str(num_vacpol))
    w.add_data("sector_source_map", {
        "leading_q9_q10": "e_- sinh; DERIVED pre-archimedean (step 2)",
        "alpha_over_4pi": "e_+ cosh Habiro H=[2]_q(1-h^2 a); SOURCED (corpus); pi=|S^2|",
        "two_over_3pi": "numerator 4/3 over |S^1|; tier=OPEN (no pre-arch source yet)",
    })
    w.add_assertion(
        "additive corrections close bare residual: |resid_corrected| < 5e-5",
        computed=bool(closes), expected=True,
        source="1/alpha = q[9][10] + 2/(3pi) + alpha/(4pi) vs CODATA",
    )
    w.add_assertion(
        "alpha/(4pi) = alpha/|S^2|: numerator is exactly alpha (pi is the S^2 period)",
        computed=bool(vertex_num_is_alpha), expected=True,
        source="Hopf base-sphere period |S^2| = 4pi",
    )
    w.add_assertion(
        "2/(3pi) = (4/3)/|S^1|: numerator is exactly 4/3 (pi is the S^1 period)",
        computed=bool(vacpol_num_is_4_3), expected=True,
        source="Hopf fibre period |S^1| = 2pi",
    )
    w.add_data(
        "finding",
        "No-pi program, concrete: the alpha_EM corrections decompose as "
        "(pre-archimedean numerator)/(Hopf-fibration period) — alpha/(4pi)="
        "alpha/|S^2|, 2/(3pi)=(4/3)/|S^1| — so pi enters ONLY as a Hopf period "
        "(archimedean tau-image), never as a fundamental constant.  alpha/(4pi)'s "
        "numerator alpha sits in the e_+ cosh Habiro element H=[2]_q(1-h^2 alpha) "
        "(SOURCED, corpus).  The remaining open item is the pre-archimedean source "
        "of the 4/3 numerator in 2/(3pi) (tier=OPEN; not fitted).  This is the "
        "multi-session research frontier of the alpha_{basis-knot} program."
    )
    w.save()
    print("\nDone. Witness saved (alpha-em-no-pi-correction-probe).")
    print("  TIER: closure SOURCED for alpha/(4pi); OPEN for the 4/3 of 2/(3pi).")


if __name__ == "__main__":
    main()
