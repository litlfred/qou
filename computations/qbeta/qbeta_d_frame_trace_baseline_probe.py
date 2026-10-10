#!/usr/bin/env python3
"""
qbeta_d_frame_trace_baseline_probe.py — qou-cds1: the D-frame trace baseline,
computed rather than substituted, and what it prices.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean
# Ref: docs/audits/2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md

WHY THIS IS NOT A z-SWAP. qou-cds1 and
QOU.QBeta.decayLadder_zC_threeRow_ne_zero both state that the ladder must be
RE-DERIVED under convention D, not re-evaluated at z_D. So this probe does not
touch the ladder's formula. It builds the D-frame object from its defining
structural property instead:

    under D the decay trace kills the third row (y_(1^3) = 0) and factors
    through Temperley-Lieb

and `y_lambda_su_n(3, q, N=2)` IS that structure -- a three-row partition has
vanishing Schur function at N = 2, so y_(1^3) = 0 falls out rather than being
imposed. The trace is then computed on the EXHIBITED nucleon words, per block.

WHAT IT FINDS. The D-frame (two-row) Markov trace of Delta gives Q_beta about
15.5 % low, against the coordinate-sum counit's +0.17 %. The three-row trace is
27.3 % low. Neither is close.

WHY THAT MATTERS FOR THE RE-DERIVATION. Every rung of the published ladder is a
sub-percent correction -- the whole five-rung product moves Q_A by 0.168 %. A
15.5 % baseline gap is ~92x the entire existing ladder. So rungs of that size,
applied to this baseline, do not by themselves land on CODATA.

WHAT THAT IS NOT A REASON TO DO -- corrected 2026-08-26 on owner instruction.
An earlier reading of this measurement (and the chat summary of it, which was
worse than this file) treated the 92x as a reason to leave the D-frame ladder
re-derivation undone. That inverts the standing rule: a structurally-exact
piece is a PERMANENT, CORRECT contribution even while the current total is
inaccurate, and "inaccurate alone" is not "excluded" (AGENTS.md, the two
permanence principles under "Before declaring refuted"). The ladder is
convention-C-frame throughout and un-re-derived under the canonical convention
(bean qou-cds1); if re-deriving it is the right thing to do, it is right
independently of whether it closes this gap, because once the other terms of
the gap are supplied the correct rungs are what improves the accuracy. Do the
re-derivation. What this measurement changes is the EXPECTATION set on it --
it will not, on its own, land on CODATA -- not whether to do it.

🛑 THE COUNIT AND THE TRACE BELOW ARE ON DIFFERENT ELEMENTS -- read this
before quoting the 92.1058x (added 2026-09-03, bean qou-bg3w).  The trace is
computed on `hecke_core`'s ELEVEN-crossing gen-grouped nucleon words
(Delta_L); the counit closed form `h**2 / 2 - h` hardcoded below is the
ONE-/TWO-crossing short model's (Delta_S).  Those are different elements of
H_3(q), so the ratio compares a property of one against a property of the
other.  Both measurements are correct on the element they are taken on; the
RATIO is the straddle.

Priced consistently the figure is not one number but two, and they BRACKET
the published one -- 0.6237x on Delta_L, 92.1058x as published, 257.26x on
Delta_S.  So it is not an approximation to either, and the recorded reading
"understates by 2.793x" is itself Delta_S-conditional: against Delta_L the
same figure OVERSTATES by 148x.  Measured in
`qbeta_d_frame_baseline_element_consistency_probe.py` (5/5), which also
verifies that the Frobenius pairing used here IS the Markov trace at z_D.
Nothing below is changed by this: the 92.1058x is left intact because it is
what downstream calibrates against, and the fix is to say which element each
half is on, not to silently move a number consumers key on.

SCOPE -- (a), NOT (b), per AGENTS.md. This is "this construction, alone, does
not reproduce the numbers as-is". It does NOT exclude the trace as an
ingredient, does NOT prove Q_beta is not a trace observable, and does NOT
foreclose the D-frame re-derivation. It prices one baseline.
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
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from chi_general_word import chi_all_lambda_any as chi_all_lambda  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

set_compute_dps()


def _word(g0, g1):
    """The nucleon word. GROUPED -- a CHOICE, no longer forced: since 2026-10-10 the kernel is
    `chi_general_word.chi_all_lambda_any` (byte-identical output on this word),
    and the canonical word MOVES these numbers -- which frame to use is an owner
    call recorded in bean `qou-11l4`. The paragraph below is the history.

    `chi_monotone_transfer.chi_all_lambda`, which this probe uses, accepts only
    a monotone generator sequence. The canonical borromean word is non-monotone
    by construction -- its core is `(sigma_0 sigma_1^-1)^3` -- so feeding it
    here raises `ValueError: non-monotone word: gen 0 after 1`. Measured, not
    inferred. The frame therefore cannot be changed by editing this helper; it
    changes when the kernel does (`chi_general_word.chi_all_lambda_any`, the
    remedy `closed_form_tau_M` already took).

    Named via `grouped_word_from_chains` so the constraint is visible at the
    call site instead of one import line away. Beans `qou-11l4` (this probe is
    missing from `qou-y2o7`'s blast radius, which is marked completed) and
    `qou-t29k`. Output unchanged: the helper IS this concatenation, with the
    mpf conversion preserved per chain.
    """
    from pyhecke.atom import grouped_word_from_chains
    return grouped_word_from_chains(
        [(mp.mpf(str(c)), mp.mpf(str(d))) for c, d in g0],
        [(mp.mpf(str(c)), mp.mpf(str(d))) for c, d in g1],
    )


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    me = mp.mpf(str(M_E_MEV))
    Qexp = mp.mpf(str(Q_NEUTRON_MEV))
    E0 = me / (q * (q - 1))

    wb = WitnessBuilder("qbeta-d-frame-trace-baseline", engine="mpmath")
    wb.set_description(
        "qou-cds1: the convention-D trace baseline for Q_beta, built from the "
        "two-row (Temperley-Lieb) structure rather than by substituting z_D "
        "into the C-frame ladder. Finds the D-frame trace 15.5 % low against "
        "the counit's +0.17 %, and prices that gap at ~92x the entire "
        "five-rung ladder -- so a D-frame re-derivation of the existing rung "
        "structure cannot close it. Scope-(a), not an exclusion of the trace.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    cp = chi_all_lambda(_word(_PROTON_G0, _PROTON_G1), 3, dps=50, q=q)
    cn = chi_all_lambda(_word(_NEUTRON_G0, _NEUTRON_G1), 3, dps=50, q=q)
    chi = {k: cn.get(k, mp.mpf(0)) - cp.get(k, mp.mpf(0))
           for k in set(cn) | set(cp)}

    print("=" * 74)
    print(" qou-cds1 — the D-frame trace baseline, computed not substituted")
    print("=" * 74)

    res = {}
    for N, lbl in ((2, "two-row / TL / convention-D"), (3, "three-row")):
        y = y_lambda_su_n(3, q, N)
        tot = mp.mpf(0)
        for sh, v in y.items():
            tot += v * chi.get(tuple(sh), mp.mpf(0))
        Qb = abs(tot * E0)
        res[N] = (y, tot, Qb, (Qb - Qexp) / Qexp)
        print(f"\n  {lbl}:  tr_M(Delta) = {mp.nstr(tot, 14)}   "
              f"Q_beta = {mp.nstr(Qb, 12)}   err = {mp.nstr(res[N][3] * 100, 6)} %")

    y2 = res[2][0]
    check("third_row_vanishes_at_N_equals_2",
          y2.get((1, 1, 1), mp.mpf(0)) == 0,
          "y_(1^3) = 0 falls out of the N=2 Schur specialisation, not imposed")

    # the counit baseline, for contrast
    eps = h**2 / 2 - h
    QA = abs(eps * E0)
    errA = (QA - Qexp) / Qexp
    print(f"\n  counit (coordinate sum) baseline: Q_A = {mp.nstr(QA, 12)}   "
          f"err = {mp.nstr(errA * 100, 6)} %")

    gap = abs(res[2][3]) - abs(errA)
    check("D_frame_trace_baseline_is_far_from_CODATA",
          abs(res[2][3]) > mp.mpf("0.10"),
          f"two-row trace is {mp.nstr(res[2][3] * 100, 5)} % off")

    # every rung is sub-percent; the whole ladder moves Q_A by |errA|
    ratio = abs(res[2][3]) / abs(errA)
    check("gap_exceeds_the_entire_existing_ladder",
          ratio > 50,
          f"baseline gap is {mp.nstr(ratio, 5)}x the whole five-rung ladder "
          f"({mp.nstr(abs(errA) * 100, 4)} %), so rungs that size cannot close it")

    check("three_row_trace_is_further_still",
          abs(res[3][3]) > abs(res[2][3]),
          f"{mp.nstr(res[3][3] * 100, 5)} % vs {mp.nstr(res[2][3] * 100, 5)} %")

    for k, (_, tot, Qb, e) in res.items():
        wb.add_data(f"trM_Delta_N{k}", fmt(tot))
        wb.add_data(f"Qbeta_N{k}", fmt(Qb))
        wb.add_data(f"err_N{k}", fmt(e))
    wb.add_data("counit_baseline_Qbeta", fmt(QA))
    wb.add_data("counit_baseline_err", fmt(errA))
    wb.add_data("gap_over_ladder_ratio", fmt(ratio))
    for sh, v in sorted(chi.items()):
        wb.add_data(f"chi_{'_'.join(map(str, sh))}", fmt(v))
    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
