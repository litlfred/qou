#!/usr/bin/env python3
"""Is Q_beta the "bar-odd (sinh) partner" under q -> 1/q? Measured: NO, neither parity.

BEAN `qou-cds1`. This settles an open question raised by
`qbeta_phase_bar_parity_completeness_probe.py`: that probe showed the ladder
phase `a - u/2` is bar-odd in NEITHER convention (u scales by q^2), and left
open whether F = Q_beta/Q_A is REQUIRED to be bar-even at all. If it is, the
ladder violates the requirement by a term worth 15 % of the correction.

The corpus states the requirement explicitly and names the involution:

  three-calibration-discipline.md:18 --
    "It is the bar-odd (sinh) partner of the bar-even (cosh) meson scale m_pi
     UNDER THE BAR-INVOLUTION q -> q^{-1}"

  and similarly in epistemic-status-of-calibrations.md,
  three-calibration-discipline-proof.md, and AGENTS.md
  ("the bar-odd sinh partner of the bar-even cosh meson scale m_pi").

That is a testable claim about the exact closed form the framework computes,

    Q_A / m_e = |q^2 - 2q - 1| * (q+1) / (2 q^3)          (AGENTS.md; qbeta_utils)

MEASURED at the proton anchor, 40 dps:

    Q_A/m_e  at q    = 1.5335566273012
    Q_A/m_e  at 1/q  = 2.5868438911015
    bar(Q_A)/Q_A     = 1.686826456258

  bar-ODD would be -1. bar-EVEN would be +1. It is NEITHER.

Nor does any other natural involution rescue it (symbolic, unsigned form):

    q -> 1/q    ->  q^3 (q^2+2q-1) / (-q^2+2q+1)
    q -> -q     ->  (q^3+q^2-3q+1) / (q^3-q^2-3q-1)
    q -> -1/q   ->  q^3 (q-1) / (q+1)

none of which is the constant -1 or +1.

CONSEQUENCE FOR THE RE-DERIVATION. The bar-evenness of F cannot be derived from
"Q_beta is bar-odd", because Q_beta AS COMPUTED is neither bar-odd nor bar-even.
So the open question from the companion probe resolves in the direction of: the
requirement is NOT available from the chain as written. Anyone invoking a
bar-parity constraint on the D-frame correction must first supply the object
that actually carries the parity -- it is not this closed form.

SCOPE, stated carefully because this contradicts four corpus sites:

  * This measures the CLOSED FORM Q_A = m_e|q^2-2q-1|(q+1)/(2q^3), which is what
    AGENTS.md gives for Q_beta and what `qbeta_utils.substrate_ladder_quantities`
    computes. If the parity claim is meant for a DIFFERENT representation (an
    unevaluated sinh form, or the width D_beta before inversion), then the claim
    may hold there and the defect is that the corpus attaches it to this form.
    Either way the statement as written does not hold of the computed object.
  * This says nothing about m_pi's claimed bar-EVENness, which is not tested here.
  * Scope-(a): no invariant is proved, nothing is derived, nothing is wired.
"""
from __future__ import annotations

import sys

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

# --- muon anchor: READ, never retyped ---------------------------------------
# This file used to carry the muon q0 as a string literal. A transcribed pin
# cannot be re-pinned, cannot be flipped by QOU_Q0_ANCHOR, and reports a
# q0Anchor describing its label rather than its computation. The literal here
# was B = Vol(4_1)/206.7682830, the CODATA-2018 derivation -- superseded by the
# owner ruling of 2026-08-22 (A -> CODATA 2022, PR #5500). Reading the anchor
# is correct before and after that ruling; retyping either value is not.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[2]
                        / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import _q0_value_for_anchor as _q0_for  # noqa: E402

set_compute_dps()

ANCHORS = {
    "proton": mp.mpf("1.10997858275138080759166909561076887987449912187357873607281"),
    "muon": mp.mpf(_q0_for("muon")),
}


def qa_over_me(x: mp.mpf) -> mp.mpf:
    """Q_A/m_e — the closed form AGENTS.md gives for Q_beta."""
    return abs(x**2 - 2 * x - 1) * (x + 1) / (2 * x**3)


def main() -> int:
    ok = True
    for name, q in ANCHORS.items():
        val, bar = qa_over_me(q), qa_over_me(1 / q)
        ratio = bar / val
        print(f"=== anchor {name}")
        print(f"  Q_A/m_e at q     = {mp.nstr(val, 14)}")
        print(f"  Q_A/m_e at 1/q   = {mp.nstr(bar, 14)}")
        print(f"  bar(Q_A)/Q_A     = {mp.nstr(ratio, 14)}")
        print(f"    |ratio - (-1)| = {mp.nstr(abs(ratio + 1), 8)}   (0 iff bar-ODD)")
        print(f"    |ratio - (+1)| = {mp.nstr(abs(ratio - 1), 8)}   (0 iff bar-EVEN)")
        print()
        # Neither parity, and not marginally so.
        ok &= abs(ratio + 1) > mp.mpf("0.5")
        ok &= abs(ratio - 1) > mp.mpf("0.5")

    print("VERDICT: the computed Q_beta closed form is NEITHER bar-odd NOR")
    print("  bar-even under q -> 1/q, contradicting the 'bar-odd (sinh) partner")
    print("  under the bar-involution q -> q^-1' stated in")
    print("    content/.../observations/three-calibration-discipline.md:18")
    print("    content/.../observations/epistemic-status-of-calibrations.md:3")
    print("    content/.../observations/three-calibration-discipline-proof.md:36")
    print("    AGENTS.md (canonical-derivation cheat sheet)")
    print()
    print("  => a bar-parity constraint on the D-frame correction F CANNOT be")
    print("     derived from 'Q_beta is bar-odd'. The open question left by")
    print("     qbeta_phase_bar_parity_completeness_probe resolves: the")
    print("     requirement is not available from the chain as written.")
    print()
    print("ASSERTIONS PASS" if ok else "ASSERTIONS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
