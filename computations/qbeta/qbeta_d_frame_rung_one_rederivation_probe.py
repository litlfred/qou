#!/usr/bin/env python3
"""
qbeta_d_frame_rung_one_rederivation_probe.py — qou-cds1: ALL of the Q_beta
ladder's convention-dependence is one additive phase in rung 1, and that phase
is exactly the gap between the inadmissible baseline and the admissible one.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: folio/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/MarkovZFullBarCondition.lean
# Ref: docs/audits/2026-08-26-qbeta-epsilon-is-inadmissible-under-convention-d.md

WHY THIS IS A RE-DERIVATION AND NOT A z-SWAP. qou-cds1 and
QOU.QBeta.decayLadder_zC_threeRow_ne_zero both forbid substituting z_D into the
C-frame ladder. This probe does not substitute anything. It asks where the
Markov parameter ENTERS the five-rung product at all, finds that it enters in
exactly one place, and identifies what that place is computing.

WHAT IS DERIVED (exact, symbolic, in q and z; no anchor, no fit).

  (D1)  2*alpha = net(Delta) - tr_M^z(Delta)          identically in q and z

        *** THE IDENTIFICATION IS NOT MINE. CORRECTED 2026-08-27. *** A sibling
        stated it on PR #5337 at 2026-08-26T06:59Z (comment 5421747260, from
        #5815 / bean qou-avt5), ~15 h before this probe existed, in these words:
        "Q_A = -E_0*eps(Delta), and the ladder's phase IS eps - tr_M". I called
        (D1) new in the first version of this file, in its commit, in the bean
        and on #5337 itself -- where that sibling comment sits in the same
        thread. Credit for the identification is theirs.

        What this probe adds is the DERIVATION rather than the assertion, and
        the difference is not cosmetic:

          - the FACTOR. Their sentence reads "the phase IS eps - tr_M"; the
            phase is alpha and the identity carries a 2. Stated loosely it is
            off by that factor.
          - "IDENTICALLY IN z", which is the whole load-bearing part. An
            unquantified assertion at one z says nothing about localisation;
            the joint statement with (D2) needs the relation to hold for EVERY
            z, and that is what is proved here.
          - Delta is REBUILT from the corpus's typed-crossing words and
            asserted against its stated coordinates, so the identity is about
            the corpus's object rather than about a transcription of it.

        So: identification theirs, proof and exact form here. Not new; not
        redundant either.

        where alpha = (z-1)h/2 is the ladder's rung-1 phase, `net` is the
        coordinate sum (the step-8 "counit"), and tr_M^z is the Ocneanu trace.
        Both sides are computed here from Delta REBUILT out of the corpus's
        typed-crossing words, not from its stated coordinates.

        So alpha is not a free parameter and not a fitted phase: it IS the
        discrepancy between the baseline the ladder starts from and the
        admissible functional. It is determined by the two functionals.

  (D2)  rungs 2..5 are free of z. Every appearance of the Markov convention in
        the whole five-rung product is the single alpha inside rung 1.

        *** (D2) IS NOT NEW. CORRECTED 2026-08-26, same session. *** It was
        already proved in Lean, sorry-free, before this probe existed:
        `QOU.BraidKnot.Q_beta_categorical_ofPhase_tail_common`
        (LadderConventionLocalisation.lean:69), reached from the D-weight side
        by a sibling working the same bean. My first commit of this probe
        presented (D2) as a finding of its own; it is an independent
        re-derivation and is kept as corroboration, not as a discovery. Two
        routes to the same localisation is worth something -- claiming it
        twice is not.

  (D3)  the Hoefsmit V_(2,1) diagonal entry IS the convention-D Markov
        parameter:  d_1 = q^3/(q^2+1) = z_D  (exact).

        Hence, with the Hoefsmit coupling defined as b^2 = d_1*d_2 + 1
        (chi-v21-hoefsmit-matrix-derivation.lean:58) and d_2 = -q^-1/(q^2+1):

            y_(2,1)^D = -d_1 * d_2                                    [exact]

        which makes the sibling's `hoefsmitB_sq_eq_one_sub_stdWeightD`
        (b^2 = 1 - y_(2,1)^D) the Hoefsmit coupling definition re-read, rather
        than a separate coincidence between the weights and the matrix. This
        is an explanation of an already-proved theorem, not a new theorem --
        one line once both objects are written down, and stated at that
        weight.

WHAT IS *NOT* DERIVED, and is flagged as a reading rather than a result.

  (I1)  "with an admissible baseline, alpha has no referent and is dropped."

        (D1) says the same quantity plays two roles -- ADDITIVELY in the
        baseline, and as a PHASE inside a cosine. Those are two different
        edits, and (D1) does not license treating one as the other. So the
        D-frame rung 1 is a PROPOSAL here, and this probe measures three
        readings of it side by side rather than choosing one.

NO SELECTION ON AGREEMENT. The three D-frame candidates are reported in a fixed
order decided before any of them was evaluated, and this probe deliberately
does NOT pick the closest to CODATA, does not form a convex combination, and
does not tune anything. Per the owner ruling of 2026-08-26, the re-derivation
is worth doing whether or not it closes the gap: a structurally-correct rung is
a permanent contribution, and the remaining terms of the gap are a separate
question (the trace-invisible sl_2 part, qou-xzrj).

SCOPE -- (a), not (b). Nothing here excludes any ingredient. It locates the
convention-dependence and prices three readings of the D-frame rung 1.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(M_E_MEV))
QEXP = mp.mpf(str(Q_NEUTRON_MEV))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"

# ---------------------------------------------------------------- H_3 regular
E = (0, 1, 2)
S0 = (1, 0, 2)
S1 = (0, 2, 1)


def compose(p, r):
    return tuple(p[r[i]] for i in range(3))


def length(w):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if w[i] > w[j])


BASIS = [E, S0, S1, compose(S0, S1), compose(S1, S0), compose(compose(S0, S1), S0)]
IDX = {w: i for i, w in enumerate(BASIS)}
NDIM = 6


def main() -> int:
    import json

    q, z = sp.symbols("q z", positive=True)
    h = q - 1 / q

    def left_gen(s):
        M = sp.zeros(NDIM, NDIM)
        for j, w in enumerate(BASIS):
            sw = compose(s, w)
            if length(sw) > length(w):
                M[IDX[sw], j] += 1
            else:
                M[IDX[w], j] += h
                M[IDX[sw], j] += 1
        return M

    L = [left_gen(S0), left_gen(S1)]
    ONE = sp.eye(NDIM)

    def bv(i):
        v = sp.zeros(NDIM, 1)
        v[i] = 1
        return v

    # Delta, rebuilt from the corpus's typed-crossing words (NOT hardcoded)
    proton = sp.expand(L[0] * (L[1] - (h / 2) * ONE) * bv(0))
    neutron = sp.expand((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * bv(0))
    delta = sp.expand(neutron - proton)

    # the two functionals, on a general element of H_3
    def net(v):
        return sp.simplify(sum(v[i] for i in range(NDIM)))

    # Ocneanu trace: tr(1)=1, tr(sigma_i)=z, tr(sigma_i sigma_j)=z^2,
    # tr(longest)=z(hz+1).  Values by reduced length / shape.
    TRV = [sp.Integer(1), z, z, z**2, z**2, z * (h * z + 1)]

    def tr_M(v):
        return sp.simplify(sum(v[i] * TRV[i] for i in range(NDIM)))

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {note}")

    print("=" * 78)
    print(" qou-cds1 — where the ladder's convention-dependence actually lives")
    print("=" * 78)

    stated = sp.Matrix([h**2 / 2, -h / 2, -h / 2, 0, 0, 0])
    check("delta_rebuilt_from_words_matches_the_corpus_NF_vector",
          all(sp.simplify(sp.expand(e)) == 0 for e in (delta - stated)),
          "typed-crossing words -> [h^2/2, -h/2, -h/2, 0, 0, 0]")

    net_d = net(delta)
    tr_d = tr_M(delta)
    alpha = (z - 1) * h / 2

    check("net_of_delta_is_the_step_8_epsNPq",
          sp.simplify(net_d - (h**2 / 2 - h)) == 0,
          f"net(Delta) = {sp.simplify(net_d)}")
    check("markov_trace_of_delta_is_h2_over_2_minus_h_z",
          sp.simplify(tr_d - (h**2 / 2 - h * z)) == 0,
          f"tr_M^z(Delta) = {sp.simplify(tr_d)}")

    # ------------------------------------------------------------------ (D1)
    check("D1_two_alpha_IS_the_net_minus_trace_gap",
          sp.simplify(2 * alpha - (net_d - tr_d)) == 0,
          "2*alpha = net(Delta) - tr_M^z(Delta), identically in q AND z -- so "
          "the rung-1 phase is a DETERMINED quantity, not a free parameter")

    # ------------------------------------------------------------------ (D2)
    hb = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    rungs_hi = [1 - b**2 * hb**4,
                1 - 2 * b**3 * hb**6,
                1 - 2 * b**4 * b**4 * hb**8,
                1 - (b**2 + sp.Rational(1, 2)) * b**5 * hb**10]
    z_free = all(sp.simplify(sp.diff(r, z)) == 0 for r in rungs_hi)
    check("D2_rungs_2_to_5_carry_no_Markov_parameter_CORROBORATION", z_free,
          "d/dz = 0 for all four. NOT a discovery -- already Lean-proved as "
          "Q_beta_categorical_ofPhase_tail_common; this is a second, "
          "independent route to the same localisation")

    # ------------------------------------------------------------------ (D3)
    # Hoefsmit V_(2,1) data, from chi-v21-hoefsmit-matrix-derivation.lean:51-58
    d1 = q**3 / (q**2 + 1)
    d2 = -q**-1 / (q**2 + 1)
    zD_sym = q**3 / (q**2 + 1)
    y21_D = q**2 / (q**2 + 1) ** 2          # the sibling's D weight
    check("D3_hoefsmit_diagonal_d1_IS_the_convention_D_markov_parameter",
          sp.simplify(d1 - zD_sym) == 0,
          "d_1 = q^3/(q^2+1) = z_D -- convention D's Markov parameter is the "
          "(2,1) Hoefsmit diagonal entry, not an independent choice")
    check("D3_D_weight_of_the_2dim_block_is_minus_the_hoefsmit_determinant",
          sp.simplify(y21_D - (-d1 * d2)) == 0,
          "y_(2,1)^D = -d_1*d_2, so `b^2 = 1 - y_(2,1)^D` (Lean, sibling) is "
          "b^2 = d_1*d_2 + 1 re-read -- an explanation of a proved theorem, "
          "not a new one")
    check("D3_consistency_b_squared_from_both_routes_agrees",
          sp.simplify((d1 * d2 + 1) - b**2) == 0,
          "the ladder's b and the Hoefsmit coupling are the same object")

    # ------------------------------------------------- numeric, at both pins
    qP = Q_MP
    qM = mp.mpf(str(json.loads(MUON_WITNESS.read_text())["derived_50_digit"]["q"]))

    def hi_rungs(qv):
        hbv = (qv - 1) / qv
        bv_ = mp.sqrt(qv**4 + qv**2 + 1) / (qv**2 + 1)
        return (bv_, [1 - bv_**2 * hbv**4,
                      1 - 2 * bv_**3 * hbv**6,
                      1 - 2 * bv_**4 * bv_**4 * hbv**8,
                      1 - (bv_**2 + mp.mpf(1) / 2) * bv_**5 * hbv**10])

    def assemble(qv, baseline, phase):
        """baseline: the functional's value on Delta.  phase: rung-1 phase."""
        bv_, hi = hi_rungs(qv)
        hbv = (qv - 1) / qv
        out = abs(_qbeta_e0.order_zero_scaled(baseline * ME, qv)) * mp.cos(phase - bv_ * hbv**2 / 2)
        for f in hi:
            out *= f
        return out

    def ppb(v):
        return (v - QEXP) / QEXP * mp.mpf(10) ** 9

    def netv(qv):
        hv = qv - 1 / qv
        return hv**2 / 2 - hv

    def trv(qv, zv):
        hv = qv - 1 / qv
        return hv**2 / 2 - hv * zv

    def alphav(qv, zv):
        return (zv - 1) * (qv - 1 / qv) / 2

    zC = lambda qv: mp.sqrt(qv) / (qv + 1)     # noqa: E731
    zD = lambda qv: qv**3 / (qv**2 + 1)        # noqa: E731

    # calibration: the published C-frame ladder, reproduced from this
    # decomposition (net baseline + alpha phase) at the block's own muon pin
    pub_mu = assemble(qM, netv(qM), alphav(qM, zC(qM)))
    pub_pr = assemble(qP, netv(qP), alphav(qP, zC(qP)))
    print(f"\n  CALIBRATION — published C-frame, rebuilt from (D1)'s pieces:")
    print(f"    muon pin (the block's own frame): {mp.nstr(ppb(pub_mu), 7)} ppb")
    print(f"    proton pin (canonical)          : {mp.nstr(ppb(pub_pr), 7)} ppb")
    check("calibration_reproduces_the_blocks_sub_ppb_muon_frame_number",
          abs(ppb(pub_mu)) < 100,
          f"{mp.nstr(ppb(pub_mu), 6)} ppb -- the decomposition is faithful to "
          f"the published ladder, so (D1) is about THIS ladder")

    # the three D-frame readings, ORDER FIXED BEFORE EVALUATION
    print(f"\n  THREE READINGS OF THE D-FRAME RUNG 1 (order fixed in advance;")
    print(f"  this probe does NOT select among them on agreement):\n")
    print(f"    {'reading':58s} {'err (ppb)':>16s}")
    readings = [
        ("R-i   baseline=tr_M^{z_D},  alpha DROPPED  (the (I1) reading)",
         assemble(qP, trv(qP, zD(qP)), mp.mpf(0))),
        ("R-ii  baseline=tr_M^{z_D},  alpha KEPT at z_D",
         assemble(qP, trv(qP, zD(qP)), alphav(qP, zD(qP)))),
        ("R-iii baseline=net,         alpha at z_D   (the INVALID z-swap)",
         assemble(qP, netv(qP), alphav(qP, zD(qP)))),
    ]
    for lbl, v in readings:
        print(f"    {lbl:58s} {mp.nstr(ppb(v), 7):>16s}")

    # the augmentation is the OTHER admissible functional (trace at z = q)
    aug = assemble(qP, trv(qP, qP), mp.mpf(0))
    print(f"\n    {'R-iv  baseline=augmentation (tr at z=q), alpha DROPPED':58s} "
          f"{mp.nstr(ppb(aug), 7):>16s}")

    # PREDICTION RETRACTED, kept rather than deleted. I asserted "all four
    # exceed 1e6 ppb" before checking, and it FAILED: R-iii, the reading the
    # corpus FORBIDS, comes in at 6.0e5 ppb -- under the threshold, and two
    # orders of magnitude closer to CODATA than any admissible reading. The
    # honest repair is to state what is true and to name what the failure
    # showed, not to widen the bound until the claim passes.
    admissible = [readings[0][1], readings[1][1], aug]
    check("all_three_ADMISSIBLE_baseline_readings_exceed_1e8_ppb",
          all(abs(ppb(v)) > mp.mpf(10) ** 8 for v in admissible),
          f"{', '.join(mp.nstr(ppb(v), 4) for v in admissible)} ppb -- and per "
          f"the owner ruling this is NOT a reason to leave the re-derivation "
          f"undone; a structurally-correct rung is a permanent contribution")
    closest = min(abs(ppb(v)) for v in admissible) / abs(ppb(readings[2][1]))
    check("the_INVALID_z_swap_is_the_CLOSEST_reading_adverse_evidence",
          all(abs(ppb(readings[2][1])) < abs(ppb(v)) for v in admissible),
          f"the forbidden z-swap is {mp.nstr(closest, 5)}x closer to CODATA "
          f"than the nearest admissible reading. Third construction in this "
          f"channel where proximity tracks INADMISSIBILITY (step-8's `net` "
          f"was the first). Adverse to the ansatz, reported not buried")
    check("the_two_admissible_baselines_BRACKET_CODATA",
          (ppb(readings[0][1]) < 0) != (ppb(aug) < 0),
          f"tr at z_D gives {mp.nstr(ppb(readings[0][1]), 5)} ppb, "
          f"augmentation gives {mp.nstr(ppb(aug), 5)} ppb -- opposite signs. "
          f"NOT combined here: one parameter against one anchor is a fit")

    wb = WitnessBuilder("qbeta-d-frame-rung-one-rederivation", engine="mpmath+sympy")
    wb.set_description(
        "qou-cds1: locates ALL of the Q_beta ladder's convention-dependence in "
        "one additive phase inside rung 1, and proves that phase is exactly "
        "net(Delta) - tr_M^z(Delta) -- the gap between the inadmissible "
        "step-8 baseline and the admissible Ocneanu trace, identically in q "
        "and z. Rungs 2-5 carry no Markov parameter. Measures three readings "
        "of the D-frame rung 1 plus the augmentation baseline, in an order "
        "fixed before evaluation, and selects none of them.")
    wb.add_data("net_delta_symbolic", str(sp.simplify(net_d)))
    wb.add_data("trM_delta_symbolic", str(sp.simplify(tr_d)))
    wb.add_data("alpha_symbolic", str(sp.simplify(alpha)))
    wb.add_data("published_C_muon_pin_ppb", fmt(ppb(pub_mu)))
    wb.add_data("published_C_proton_pin_ppb", fmt(ppb(pub_pr)))
    for lbl, v in readings:
        wb.add_data(lbl.split()[0] + "_ppb", fmt(ppb(v)))
    wb.add_data("R-iv_augmentation_ppb", fmt(ppb(aug)))
    wb.add_data("z_D_at_proton_pin", fmt(zD(qP)))
    wb.add_data("z_C_at_proton_pin", fmt(zC(qP)))
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
