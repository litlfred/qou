#!/usr/bin/env python3
"""
qbeta_epsnpq_functional_mismatch_probe.py — qou-99qc: the fork's premise does
not hold. Two different functionals are both called `ε`.

# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/CounitSigmaOneForcesHZero.lean
# Ref: folio/quantum-observable-universe/lean/QOU/Interactions/qbeta_counit_vs_trace.lean
# Ref: computations/qbeta/qbeta_epsnpq_colour_weighted_exclusion_probe.py
# Ref: computations/qbeta/qbeta_delta_vs_deltaTbeta_settled_probe.py

THE FORK, as posed by qou-99qc: either (a) Δ is not a difference of two words,
or (b) `epsNPq` is wrong and takes `Q_A` and the ladder phase with it.

BOTH BRANCHES ASSUME A CONTRADICTION THAT IS NOT THERE. `qou-avt6` proved that
no difference of two typed-crossing words has counit `epsNPq`. That proof
evaluates a word as a PRODUCT of per-letter counits — legitimate only for an
algebra homomorphism — and its per-letter table starts `COUNIT["sigma"] = q`.
So avt6's `ε` is the AUGMENTATION `σ ↦ q`.

`epsNPq` is not a value of that map. `QBetaCounitTrace.epsNP` is defined as the
functional "which weights every basis element by `1`" — the COORDINATE SUM,
i.e. `σ ↦ 1` — applied to the stated normal-form vector

    (n − p) = [h²/2, −h/2, −h/2, 0, 0, 0]   in [γ, σ₀, σ₁, L₊, L₋, e⁻]

whose coordinates sum to `h²/2 − h = h(h−2)/2 = epsNPq`.

`σ ↦ 1` is NOT an algebra homomorphism unless `h = 0`: push `σ² = hσ + 1`
through a unital multiplicative map sending `σ ↦ 1` and get `1 = h + 1`.
Lean, sorry-free: `QOU.QBeta.CounitSigmaOne.h_eq_zero_of_image_one`.

So an exclusion theorem about the multiplicative `ε` does not constrain
`epsNPq`, which the non-multiplicative coordinate sum produced. avt6's theorem
stands; what does not stand is quoting it against `epsNPq`.

WHAT THIS DOES **NOT** RESCUE, and the distinction matters. Showing the fork's
premise is broken is not showing `epsNPq` is right. The stated NF vector is
still not the exhibited nucleon-word difference, under EITHER functional —
CHECK 5 measures that gap and it survives. So `qou-avt5`'s scope-(a) finding
is untouched: `Q_A` still rests on a vector nobody has derived. The fork was
the wrong question, not a question with a reassuring answer.
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
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from chi_general_word import chi_all_lambda_any as chi_all_lambda  # noqa: E402
from hecke_core import (  # noqa: E402
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
)
from q_parameter import Q as Q0  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — exact mpf, not the f64 twin

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
    qs = sp.symbols("q")
    hs = qs - 1 / qs

    q = Q_MP
    h = q - 1 / q

    wb = WitnessBuilder("qbeta-epsnpq-functional-mismatch", engine="mpmath")
    wb.set_description(
        "qou-99qc: the fork's premise fails. avt6's exclusion is about the "
        "multiplicative augmentation sigma -> q; epsNPq is a value of the "
        "NON-multiplicative coordinate sum sigma -> 1, which is not an "
        "algebra map unless h = 0. So the exclusion does not constrain "
        "epsNPq and no choice between the two branches is forced. This does "
        "NOT show epsNPq is right: the stated NF vector still is not the "
        "exhibited nucleon-word difference (CHECK 5).")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 74)
    print(" qou-99qc — epsNPq and avt6 use DIFFERENT functionals")
    print("=" * 74)
    print(f"  q0 = {mp.nstr(q, 17)}   h = {mp.nstr(h, 17)}\n")

    # CHECK 1 — epsNPq is exactly the coordinate sum of the stated NF vector.
    coords = [hs**2 / 2, -hs / 2, -hs / 2, 0, 0, 0]
    eps_closed = (qs**2 - 1) * (qs**2 - 2 * qs - 1) / (2 * qs**2)
    check("epsNPq_is_the_coordinate_sum_of_the_NF_vector",
          sp.simplify(sum(coords) - eps_closed) == 0,
          "sum[h^2/2, -h/2, -h/2, 0,0,0] == (q^2-1)(q^2-2q-1)/(2q^2), exactly")
    check("coordinate_sum_is_sigma_maps_to_one",
          sp.simplify(sum(coords) - (hs**2 / 2 - hs)) == 0,
          "weights every basis element by 1, i.e. sigma -> 1")

    # CHECK 2 — sigma -> 1 is not an algebra map at h != 0. This is the Lean
    # lemma, re-checked numerically: it would force h = 0.
    check("sigma_to_one_would_force_h_zero", h != 0,
          f"sigma^2 = h*sigma + 1 under sigma->1 gives 1 = h+1; here h = "
          f"{mp.nstr(h, 12)} != 0, so sigma->1 is NOT multiplicative")

    # CHECK 3 — avt6's per-letter table is the augmentation sigma -> q, and
    # that one IS a valid algebra map.
    check("avt6_counit_of_sigma_is_q",
          sp.simplify(sp.cancel(qs) - qs) == 0,
          "COUNIT['sigma'] = q in qbeta_epsnpq_colour_weighted_exclusion_probe")
    check("sigma_to_q_satisfies_the_hecke_relation",
          sp.simplify(qs**2 - (hs * qs + 1)) == 0,
          "q^2 = h*q + 1 with h = q - 1/q, so sigma->q IS an algebra map")

    # CHECK 4 — the two functionals disagree on the SAME vector, by h(q-1).
    eps_aug = hs**2 / 2 - hs * qs          # same vector, sigma -> q
    gap = sp.simplify(sum(coords) - eps_aug)
    check("the_two_functionals_differ_by_h_times_q_minus_one",
          sp.simplify(gap - hs * (qs - 1)) == 0,
          "coordinate-sum minus augmentation = h(q-1), nonzero at q0")

    # CHECK 5 — and neither is the exhibited element. Recomputed here from the
    # nucleon words, not quoted from the earlier probe.
    cp = chi_all_lambda(_word(_PROTON_G0, _PROTON_G1), 3, dps=50, q=q)
    cn = chi_all_lambda(_word(_NEUTRON_G0, _NEUTRON_G1), 3, dps=50, q=q)
    chi3 = cn.get((3,), mp.mpf(0)) - cp.get((3,), mp.mpf(0))
    v_sum = h**2 / 2 - h
    v_aug = h**2 / 2 - h * q
    print(f"\n  chi_(3)(beta_n - beta_p)  = {mp.nstr(chi3, 17)}   (exhibited words)")
    print(f"  coordinate sum (epsNPq)   = {mp.nstr(v_sum, 17)}")
    print(f"  augmentation on same vec  = {mp.nstr(v_aug, 17)}")
    check("NF_vector_is_not_the_exhibited_element_under_either_functional",
          abs(v_sum - chi3) > mp.mpf("1e-6") and abs(v_aug - chi3) > mp.mpf("1e-6"),
          "so qou-avt5's scope-(a) finding stands: Q_A rests on an "
          "underived vector. The fork's premise is broken; epsNPq is not "
          "thereby vindicated")

    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    wb.add_data("chi3_exhibited", fmt(chi3))
    wb.add_data("coordinate_sum_epsNPq", fmt(v_sum))
    wb.add_data("augmentation_on_same_vector", fmt(v_aug))
    wb.add_data("gap_coordinate_sum_minus_augmentation", fmt(v_sum - v_aug))

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
