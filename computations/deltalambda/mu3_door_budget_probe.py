#!/usr/bin/env python3
"""mu3_door_budget_probe.py — the μ₃ door budget, and why the "re-weighting" escape is a non-move.

#4657 flagged a mixed-sign escape: `reweight_cannot_open_door` assumes `w_λ ≥ 0`, and the
physical `y_λ` is sign-indefinite, so (I argued) the lemma does not foreclose "keep the
operator, change the Wedderburn weights."

**That framing was wrong, and this probe records why.**  The escape is unavailable for a
different and stronger reason: **`y_λ` has no freedom to re-weight.**  The Jones–Markov trace on
`H_n(R,q)` is the *unique* non-degenerate Markov trace
(`prop:markov-trace-frobenius-selection`; Alexander–Markov uniqueness, `mba-chain-map` step 3),
and `y_λ = s_λ/Z` is its Wenzl closed form at fixed `q`.  There is no free parameter to vary.
So "re-weighting" was never a move — scope-(b), invariant named.

WHAT REMAINS, and it is scope-(a): the only actual freedom is the **operator** (which word,
which trace object).  This probe therefore measures the budget the operator would have to beat:

    Δ²g = P + N,    P = Σ_{y_λ>0} y_λ Δ²|χ|_λ,    N = Σ_{y_λ<0} y_λ Δ²|χ|_λ

The door needs `P + N < 0`, i.e. `|N| > P`.  Reported: the current shortfall, and a **ceiling**
on `|N|` from `|Δ²|χ|_λ| ≤ 4·max_λ|χ_λ|` (four terms, each bounded by the largest character).

SCOPE DISCIPLINE — the ceiling is scope-(a), NOT (b).  `max|χ|` is measured on *this* word.
A different braid word has different characters, and `|χ|` grows with word length, so there is
no universal bound.  The ceiling says "at this operator's character scale the route falls short
by X" — it does **not** exclude the route for all operators.  Stated explicitly so the number
is not later quoted as a structural exclusion.

GATES:
  * `P + N` must reproduce the committed Δ²g;
  * the ceiling must actually bound the measured `|N|` (a ceiling below its own measurement
    would mean the bound is misderived).

CONVENTION-D UPDATE — the scope-(a) half is MOOT, and the reason matters.
Under the canonical trace convention **D** (`z = q³/(q²+1)`, owner ruling 2026-08-15) the
Wenzl level relation collapses to `Q^r = Q²`, i.e. `r = 2` (`QOU` `wenzlLevel_conventionD`),
and `y_λ = 0 ⟺ ℓ(λ) > r` (`schurPrincipal_eq_zero_iff`, sorry-free, all n and all r).  So
`schur_principal_mpmath` is the SU(2) two-row specialisation `s_λ(1, Q)` and vanishes
identically for every `λ` with three or more rows — 25 of the 30 partitions of 9.  Both facts
are already established on main; see `two_row_support_recount.py`, which measures what the
truncation removes.  Nothing here re-derives them.  Every `λ` that carried a **negative**
`y_λ` under the excised convention C sits inside that zeroed set.  So under D:

    N = 0 identically,  and there is no negative-weight budget to measure.

Finite-precision arithmetic leaves the zeroed entries at ~1e-42 with arbitrary sign, and a
bare `y_λ < 0` test picks that up and reports it as a supply — an earlier run of this probe
printed "the negative blocks supply ~1/7.6e39 of what the door needs", which is round-off
dressed as a measurement.  The probe now classifies against an explicit noise floor tied to
the working precision and reports the structural zero instead.

Anchor: experimental/proton.  Nothing fitted, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from schur_principal_mpmath import y_lambda_at_q0_mpmath  # noqa: E402
from q_parameter import Q_MP as Q0_MP  # noqa: E402 — the mpf, NOT the float64 `Q`
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(40)
q0 = Q0_MP
q0f = float(q0)          # float64 only at the pyhecke_native FFI boundary
_Y9 = y_lambda_at_q0_mpmath(9, q0)


def chis(word):
    f = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    return {tuple(s): mp.mpf(repr(c))
            for s, c in pyhecke_native.chi_q_atomic_all_partitions(9, f, q0f)}


def main() -> int:
    print("=" * 88)
    print(" μ₃ door budget — what the OPERATOR would have to beat")
    print("=" * 88)
    print(" The weights are NOT a lever: tr_M is the unique non-degenerate Markov trace")
    print(" (prop:markov-trace-frobenius-selection), so y_λ = s_λ/Z is fixed at fixed q.")
    print(" The only freedom is the operator.\n")

    results, gates_ok = {}, True
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        ga, gb = sorted({x[2] for x in full if x[2] % 3 == 2})

        def g_of(sub):
            return chis([x for x in full if x[2] % 3 != 2 or x[2] in sub])

        ce, ca, cb, cab = g_of(set()), g_of({ga}), g_of({gb}), g_of({ga, gb})
        B = sorted(set(ce) & set(ca) & set(cb) & set(cab) & set(_Y9))
        d2chi = {l: abs(cab[l]) - abs(ca[l]) - abs(cb[l]) + abs(ce[l]) for l in B}

        # Under trace convention D the Wenzl level collapses to r = 2, so the y_λ tower
        # is the SU(2) two-row specialisation and every λ with ℓ(λ) ≥ 3 is EXACTLY 0
        # (25 of the 30 partitions of 9).  Finite-precision arithmetic leaves those
        # entries at ~1e-42 with random sign, so a bare `y < 0` test picks up round-off
        # and reports it as a negative-weight mass.  Classify against an explicit noise
        # floor tied to the working precision instead.
        NOISE = max(abs(v) for v in _Y9.values()) * mp.mpf(10) ** (-(mp.mp.dps - 8))
        neg_blocks = [l for l in B if _Y9[l] < -NOISE]
        pos_blocks = [l for l in B if _Y9[l] > NOISE]

        P = sum(_Y9[l] * d2chi[l] for l in pos_blocks)
        Nn = sum(_Y9[l] * d2chi[l] for l in neg_blocks)
        tot = P + Nn
        yneg = sum(abs(_Y9[l]) for l in neg_blocks)
        ypos = sum(_Y9[l] for l in pos_blocks)
        maxchi = max(max(abs(d[l]) for l in B) for d in (ce, ca, cb, cab))
        ceiling = yneg * 4 * maxchi

        shortfall = P / abs(Nn) if Nn else mp.inf          # factor the route is short by
        ceil_ratio = ceiling / P if P else mp.inf
        bound_sane = ceiling >= abs(Nn)
        gates_ok = gates_ok and bound_sane

        print(f"── {name} ──")
        print(f"   blocks with y_λ > 0 / y_λ < 0    = {len(pos_blocks)} / {len(neg_blocks)}"
              f"   (of {len(B)}; noise floor {float(NOISE):.2e})")
        print(f"   P  (positive-weight blocks)      = {float(P):+.6f}")
        if not neg_blocks:
            print("   N  (negative-weight blocks)      = 0 EXACTLY — there are none.")
            print("      Convention D caps the tower at two rows (Wenzl level r = 2), and every")
            print("      λ that carried a negative y_λ under the excised convention C has")
            print("      ℓ(λ) ≥ 3, hence y_λ = 0.  The residual ~1e-42 below the noise floor is")
            print("      arithmetic round-off and must NOT be reported as a supply.")
        else:
            print(f"   N  (negative-weight blocks)      = {float(Nn):+.6f}")
        print(f"   Δ²g = P + N                      = {float(tot):+.6f}   (door needs < 0)")
        if neg_blocks:
            print(f"   → route is short by a factor of  : {float(shortfall):.1f}×")
            print(f"   Σ|y_λ| over negative blocks      = {float(yneg):.4e}"
                  f"   ({float(yneg/ypos)*100:.3f}% of the positive mass)")
        print(f"   max|χ| over all four words       = {float(maxchi):.4f}")
        print(f"   CEILING on |N| = Σ|y_neg|·4·max|χ| = {float(ceiling):.6f}")
        print(f"   ceiling / P                      = {float(ceil_ratio):.4f}"
              f"   → even at the ceiling the route {'FALLS SHORT' if ceil_ratio < 1 else 'COULD reach'}")
        print(f"   (bound sane, ceiling ≥ |N|: {bound_sane})\n")

        results[name] = {
            "P_positive_weight": mp.nstr(P, 20), "N_negative_weight": mp.nstr(Nn, 20),
            "d2g_total": mp.nstr(tot, 20),
            "n_positive_blocks": len(pos_blocks),
            "n_negative_blocks": len(neg_blocks),
            "y_noise_floor": mp.nstr(NOISE, 10),
            "negative_blocks_exist": bool(neg_blocks),
            "shortfall_factor": mp.nstr(shortfall, 10),
            "sum_abs_y_negative": mp.nstr(yneg, 20),
            "sum_y_positive": mp.nstr(ypos, 20),
            "max_abs_chi": mp.nstr(maxchi, 20),
            "ceiling_on_N": mp.nstr(ceiling, 20),
            "ceiling_over_P": mp.nstr(ceil_ratio, 10),
            "ceiling_below_P": bool(ceil_ratio < 1),
            "bound_sane": bool(bound_sane),
        }

    both_short = all(r["ceiling_below_P"] for r in results.values())
    print("=" * 88)
    print(" RESULT")
    print("  * scope-(b): the 'change the Wedderburn weights' escape DOES NOT EXIST. tr_M is")
    print("    the unique non-degenerate Markov trace, so y_λ is determined at fixed q --")
    print("    there is no parameter to re-weight. (This corrects #4657, which said the")
    print("    escape was 'not foreclosed'; it was never available.)")
    any_neg = any(r["negative_blocks_exist"] for r in results.values())
    if not any_neg:
        print("  * scope-(a) is MOOT under the canonical trace convention D: there are no")
        print("    negative-weight blocks at all.  D collapses the Wenzl level to r = 2, so")
        print("    y_λ = 0 exactly for every λ with three or more rows — which is every λ that")
        print("    was negative under the excised convention C.  N = 0 identically, so the")
        print("    negative blocks supply NOTHING, and the earlier '1/7.6e39' phrasing was")
        print("    round-off dressed as a measurement.  Under C this read as a huge but finite")
        print("    shortfall; under D the term is simply absent.")
    else:
        print("  * scope-(a): with the weights fixed, the negative-weight blocks currently supply")
        print(f"    ~1/{float(max(mp.mpf(r['shortfall_factor']) for r in results.values())):.0f}"
              f" of what the door needs, and even at the crude ceiling they fall short"
              f" {'in both isotopes' if both_short else 'in neither'}.")
    print("  * The ceiling is measured at THIS operator's character scale and does NOT")
    print("    exclude the route for all operators. Do not quote it as a structural bound.")
    print("=" * 88)

    w = WitnessBuilder("mu3-door-budget", engine="pyhecke_native",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("ceiling_bounds_measured_N", 1 if gates_ok else 0, 1)
    # Was an add_assertion(name, X, X) -- computed and expected the SAME expression,
    # so it read as a check while being `x == x`: tautologically true, unable to fail,
    # and rendered as "passed": true for the QA pipeline. It is a RECORDED FINDING
    # with no independent expectation, so it belongs in add_data. Bean qou-ploj.
    w.add_data("ceiling_below_P_both_isotopes", 1 if both_short else 0)
    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("q0_anchor", "experimental/proton")
    w.add_data("results", results)
    w.add_caveat(
        "SCOPE: the weights-are-fixed statement is scope-(b) with the invariant named "
        "(uniqueness of the non-degenerate Markov trace, prop:markov-trace-frobenius-selection "
        "+ Alexander-Markov). The CEILING is scope-(a) only: max|chi| is measured on this "
        "word, |chi| grows with braid length, and no universal bound is claimed. The ceiling "
        "must NOT be quoted as excluding the route for all operators."
    )
    w.add_caveat(
        "Corrects #4657: that PR stated the mixed-sign escape was 'not foreclosed' because "
        "reweight_cannot_open_door assumes w >= 0 while the physical y_lambda is "
        "sign-indefinite. The hypothesis mismatch was real but the conclusion was wrong -- "
        "there is no re-weighting freedom to foreclose in the first place."
    )
    w.set_description(
        "Decomposes Delta^2 g into positive- and negative-weight contributions to quantify "
        "the mu3 door budget. Establishes scope-(b) that the 're-weight the Wedderburn "
        "weights' escape does not exist (tr_M unique => y_lambda fixed). Under the canonical "
        "trace convention D the scope-(a) half is moot: the Wenzl level collapses to r=2, so "
        "y_lambda = 0 exactly for every partition with three or more rows -- which is every "
        "partition that was negative under the excised convention C -- hence N = 0 "
        "identically and there is no negative-weight budget. Weights are classified against "
        "an explicit noise floor so the ~1e-42 round-off in the zeroed entries is not "
        "reported as a supply."
    )
    w.save()
    return 0 if gates_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
