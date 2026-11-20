#!/usr/bin/env python3
"""
qbeta_ladder_convention_fee_probe.py — the Q_beta ladder's agreement rests on
THREE simultaneously non-canonical choices, each larger than the residual it
supports.

# Ref: folio/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md
# Ref: docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md
# Ref: docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md

WHY. The ladder block claims a -0.0066 ppm residual against CODATA. Asked
whether "a convention fee or non-colour-weighted [choice] is sneaking around",
this probe prices each canonical-vs-used choice against that residual.

The three, measured below, are not small corrections to a converged answer.
Each one moves Q_beta by more than the residual it is quoted alongside:

  1. CROSSING. Step 3 of the fitting-finding audit publishes the mixed u-d
     crossing as C(u,d;sigma) = sigma - h/2 -- COLOUR-BLIND. Owner ruling R3
     (2026-08-15) makes bring_color_weighted canonical, i.e.
     w = h(1/2 - delta/4) with delta = flavor_split_leading(q). Swapping to
     the canonical crossing moves Q_A by ~80 ppm.

  2. MARKOV CONVENTION -- and read the scope note, because the obvious
     reading of this row is WRONG. The ladder's first rung is
     cos(alpha - b*hbar^2/2) with alpha = (z-1)h/2, and the published
     agreement needs z_C = sqrt(q)/(q+1). Substituting z_D into that formula
     sends the ladder to 601192 ppb -- but that number is NOT "what convention
     D gives". AGENTS.md and QOU.QBeta.decayLadder_zC_threeRow_ne_zero both
     state that the ladder must be RE-DERIVED under D and that a z-swap is not
     a valid move: if the decay channel's decomposition kills the third row
     then its trace IS z_D and the existing C-frame ladder is not that trace.
     What the row measures is that the ladder is z_C-LOCKED -- evidence for
     its C-conditionality, not a measurement of D's accuracy, which is
     UNKNOWN pending the re-derivation (qou-cds1).

  3. q0 PIN. The block's -0.0066 ppm reproduces only at the MUON pin. At the
     canonical proton pin (owner directive 2026-08-07, R2 2026-08-15) the same
     five rungs land elsewhere.

NOTHING HERE IS A FIT AND NOTHING IS WIDENED. Every number is the published
formula evaluated at a stated choice. The finding is the SIZE of the choices,
not a claim that any particular one is wrong.

SCOPE, stated so it is not over-quoted. Item 1 applies the canonical
colour-weighted mixed crossing to the SAME single-wrap words. Whether that is
the right application of R3 to this word is a separate question this probe
does NOT settle -- what it settles is that the choice matters ~2000x more than
the residual, so it cannot be left implicit.
"""
from __future__ import annotations

import sys
from pathlib import Path

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported. Without
# this the module is unresolvable and the script cannot run standalone.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(M_E_MEV))
QEXP = mp.mpf(str(Q_NEUTRON_MEV))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"


def ladder(q, z, w_mixed, n_rungs=5):
    """The published five-rung ladder, at a stated (q, z, mixed-crossing)."""
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    # net(n-p) = w*h - h for a mixed-crossing subtraction w (see docstring)
    eps = w_mixed * h - h
    QA = abs(eps * ME / (q * (q - 1)))
    al = (z - 1) * h / 2
    fs = [mp.cos(al - b * hb**2 / 2),
          1 - b**2 * hb**4,
          1 - 2 * b**3 * hb**6,
          1 - 2 * b**4 * b**4 * hb**8,
          1 - (b**2 + mp.mpf(1) / 2) * b**5 * hb**10]
    out = QA
    for f in fs[:n_rungs]:
        out *= f
    return out


def ppb(v):
    return (v - QEXP) / QEXP * mp.mpf(10) ** 9


def main() -> int:
    import json

    q_pr = Q_MP
    q_mu = mp.mpf(str(json.loads(MUON_WITNESS.read_text())
                      ["derived_50_digit"]["q"]))

    wb = WitnessBuilder("qbeta-ladder-convention-fee", engine="mpmath")
    wb.set_description(
        "Prices the three non-canonical choices the Q_beta ladder's published "
        "agreement rests on -- colour-blind mixed crossing, convention C, and "
        "the muon pin -- against the residual they are quoted alongside. Each "
        "is larger than that residual. No fit, nothing widened; every number "
        "is the published formula at a stated choice.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 76)
    print(" Q_beta ladder — pricing the convention choices")
    print("=" * 76)

    def w_blind(q):
        return (q - 1 / q) / 2

    def w_colour(q):
        return (q - 1 / q) * (mp.mpf(1) / 2 - flavor_split_leading(q) / 4)

    zC = lambda q: mp.sqrt(q) / (q + 1)          # noqa: E731
    zD = lambda q: q**3 / (q**2 + 1)             # noqa: E731

    base = ladder(q_pr, zC(q_pr), w_blind(q_pr))
    print(f"\n  AS PUBLISHED (proton pin, conv C, colour-blind):"
          f"  {mp.nstr(ppb(base), 7)} ppb")

    rows = [
        ("canonical COLOUR-WEIGHTED crossing (R3)",
         ladder(q_pr, zC(q_pr), w_colour(q_pr))),
        ("z_D SUBSTITUTED into the C-frame ladder (INVALID move; "
         "not a measurement of convention D)",
         ladder(q_pr, zD(q_pr), w_blind(q_pr))),
        ("MUON pin (the block's own -0.0066 ppm frame)",
         ladder(q_mu, zC(q_mu), w_blind(q_mu))),
        ("colour-weighted AND z_D-substituted (same caveat on z_D)",
         ladder(q_pr, zD(q_pr), w_colour(q_pr))),
    ]
    print(f"\n  {'one choice changed':50s} {'err (ppb)':>16s} {'x the base':>12s}")
    for lbl, v in rows:
        e = ppb(v)
        print(f"  {lbl:50s} {mp.nstr(e, 7):>16s} "
              f"{mp.nstr(abs(e / ppb(base)), 5):>12s}")
        wb.add_data(lbl.replace(" ", "_")[:60], fmt(e))

    # Two canonical swaps DEGRADE the agreement; the pin runs the other way,
    # which is the stronger signature and was mis-stated on the first pass.
    check("canonical_colour_weighting_degrades",
          abs(ppb(rows[0][1])) > abs(ppb(base)),
          f"|{mp.nstr(ppb(rows[0][1]), 6)}| > |{mp.nstr(ppb(base), 6)}| ppb")
    check("ladder_is_z_C_locked_substitution_is_not_a_D_measurement",
          abs(ppb(rows[1][1])) > abs(ppb(base)),
          f"z_D substituted gives {mp.nstr(ppb(rows[1][1]), 6)} ppb vs "
          f"{mp.nstr(ppb(base), 6)} -- this shows the ladder is z_C-LOCKED. "
          f"It is NOT what convention D gives; a z-swap is invalid per "
          f"decayLadder_zC_threeRow_ne_zero. D's value is UNKNOWN (qou-cds1)")
    check("published_residual_is_quoted_at_the_NON_canonical_muon_pin",
          abs(ppb(rows[2][1])) < abs(ppb(base)),
          f"muon {mp.nstr(ppb(rows[2][1]), 6)} ppb BEATS canonical proton "
          f"{mp.nstr(ppb(base), 6)} ppb -- the block\'s -0.0066 ppm is a "
          f"muon-frame number, and the canonical pin is "
          f"{mp.nstr(abs(ppb(base) / ppb(rows[2][1])), 4)}x worse")

    check("colour_shift_dwarfs_the_residual",
          abs(ppb(rows[0][1]) - ppb(base)) > 100 * abs(ppb(base)),
          "the colour-weighting swap alone moves Q_beta by >100x the residual")

    wb.add_data("published_frame_err_ppb", fmt(ppb(base)))
    wb.add_data("delta_flavor_split", fmt(flavor_split_leading(q_pr)))
    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    # q0 STAMP (bean qou-zk51, draining the q0-dataflow ratchet). This producer
    # reads BOTH pins -- the proton pin via Q_50_DIGIT_STR (line ~108) and the
    # muon pin straight out of q-pinning-50-digit.witness.json (line ~109) --
    # so the honest declaration is "comparison", the E1 exception in AGENTS.md
    # §"q0 anchor convention", not a single pin and not independence.
    #
    # Until this stamp it carried NO q0Anchor, NO q0Value and no q0 literal
    # anywhere, so neither q0 gate could see it: the anchor-flip gate reads the
    # stamp pair and the value-drift gate reads q0 literals. That is exactly the
    # blind spot measured on this very witness -- the 2026-08-22 muon re-pin
    # moved its muon row 7.336484242 -> 7.133936641 ppb (-2.7608 %), amplified
    # 3.588e8x off a 0.0769423 ppb shift, and nothing flagged it.
    #
    # q0Values is what makes the "comparison" claim CHECKABLE rather than taken
    # on trust: q0_anchor_consistency_audit verifies each named leg against its
    # canonical pin, and a comparison stamped WITHOUT it counts as
    # Q0_COMPARISON_NO_VALUES ("the claim is unchecked"). Measured on
    # fvk_selection_probe: the stamp alone traded Q0_ANCHOR_MISSING for that
    # counter, i.e. one gate red for another.
    out = wb.save({
        "q0Anchor": "comparison",
        "q0AnchorReason": (
            "deliberate two-pin comparison: the ladder is evaluated at the "
            "canonical proton pin (the AS PUBLISHED row and the two convention "
            "rows) and at the muon pin read from q-pinning-50-digit.witness.json "
            "(the MUON pin row), to price the pin choice against the residual. "
            "Stamped 2026-09-04 draining the q0-dataflow ratchet -- bean qou-zk51"),
        "q0Values": {"proton": Q_50_DIGIT_STR, "muon": mp.nstr(q_mu, 50)},
    })
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
