#!/usr/bin/env python3
"""qou-99qc: strand order and Yukawa strengths of the right-handed singlet channels.

Pre-registered in PREREGISTRATION.md (same directory, commit 0629a1398d) before the Lean or any
number. Lean companion: folio/quantum-observable-universe/lean/QOU/QuarkState/YukawaStrandOrder.lean.

Exact sympy over Q(q, y...) for every structural check. The only numbers are the structural
factors q^2/(q^2+1), 1/(q^2+1), 1/[2], (q^2-1)/(q^2+1) at the proton q0 (mpmath, 70 dps); each
multiplies an UNDERIVED Yukawa strength, so none is a prediction. No CODATA comparison is made
(pre-registered: none is made unless order and strengths are derived). Nothing is fitted, chosen
or tuned; both orders and every strength class are enumerated, none selected.
"""
from __future__ import annotations

import itertools
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from sympy.physics.quantum import TensorProduct as TP  # noqa: E402

T0 = time.time()
ASSERTS: list = []
FAILED: list = []
q = sp.symbols("q", positive=True)
h = q - 1 / q
yu, yd, yn, ye, yq, yl, a, b = sp.symbols("y_u y_d y_nu y_e y_q y_l a b")


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def zero(M):
    return all(sp.simplify(x) == 0 for x in M)


RC = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
CC = sp.Matrix([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
I4 = sp.eye(4)
br2 = q + 1 / q
PR = sp.simplify((q * I4 - RC) / br2)
PRF = sp.simplify((q * I4 - SWAP * RC * SWAP) / br2)
K1 = sp.diag(q, 1 / q)
E1 = sp.Matrix([[0, 1], [0, 0]])


def ptrR(M, wa, wb):
    return sp.Matrix(2, 2, lambda i, j: sp.simplify(wa * M[2 * i, 2 * j] + wb * M[2 * i + 1, 2 * j + 1]))


def ptrL(M, wa, wb):
    return sp.Matrix(2, 2, lambda i, j: sp.simplify(wa * M[i, j] + wb * M[2 + i, 2 + j]))


def split(cPhi, cConj, Yu, Yd, Yn, Ye):
    return sp.simplify((Yd**2 - Ye**2) * cConj + (Yn**2 - Yu**2) * cPhi)


def main() -> int:
    log("1. Charge conjugation relates the two orders")
    check("C_R_C_eq_P_R_P", zero(CC * RC * CC - SWAP * RC * SWAP), "C·Ř·C = P·Ř·P")
    check("PRflip_eq_C_PR_C", zero(PRF - CC * PR * CC), "flipped singlet projector = C·P_R·C")
    check("PRflip_idempotent", zero(PRF * PRF - PRF), "P_R(flip) idempotent")
    diag_ml = (sp.simplify(PR[1, 1]), sp.simplify(PR[2, 2]))
    diag_hl = (sp.simplify(PRF[1, 1]), sp.simplify(PRF[2, 2]))
    check("entries_swap", sp.simplify(diag_ml[0] - diag_hl[1]) == 0 and sp.simplify(diag_ml[1] - diag_hl[0]) == 0,
          f"ud/du entries {diag_ml} vs flipped {diag_hl}")
    check("swap_is_bar", sp.simplify(diag_ml[0].subs(q, 1 / q) - diag_ml[1]) == 0, "q²/(q²+1) at q⁻¹ = 1/(q²+1)")

    log("   Coproduct check: which tensor order a fixed coproduct makes the singlet invariant in")
    # Δ(E) = E⊗K + 1⊗E kills s = q·ud − du in the corpus basis (as #8694 conv check)
    dE = TP(E1, K1) + TP(sp.eye(2), E1)
    s = sp.Matrix([0, q, -1, 0])
    sflip = sp.Matrix([0, -1, q, 0])
    check("DeltaE_kills_corpus_singlet", zero(dE * s), "Δ(E)·(q·ud − du) = 0 (coproduct E⊗K + 1⊗E)")
    check("DeltaE_on_flipped_singlet_nonzero", not zero(dE * sflip),
          "the flipped singlet is NOT invariant under the same Δ: it is the invariant of the opposite"
          " coproduct, i.e. of W⊗V in the other order — the order is a choice of tensor product, not of"
          " basis")

    log("2. The left-handed vertex does not select an order")
    check("weak_kills_both",
          zero((-h) * (I4 - PR) * s) and zero((-h) * (I4 - PRF) * sflip),
          "−h·(1 − P_R) kills the singlet in both orders")

    log("3. Pivotal partial traces")
    red = ptrR(PR, a, b)
    check("ptrR_form", zero(red - sp.diag(b * q**2 / (q**2 + 1), a / (q**2 + 1))),
          "(id⊗tr)((1⊗diag(a,b))P_R) = diag(b q²/(q²+1), a/(q²+1))")
    check("ptrR_scalar_iff_a_eq_q2b", sp.solve(sp.Eq(red[0, 0], red[1, 1]), a) == [b * q**2],
          "scalar iff a = q²·b")
    check("ptrR_K", zero(ptrR(PR, q, 1 / q) - sp.eye(2) / br2), "bare K: [2]⁻¹·1")
    check("ptrL_Kinv", zero(ptrL(PR, 1 / q, q) - sp.eye(2) / br2), "Higgs-left, left trace K⁻¹: [2]⁻¹·1")
    check("ptrL_K_not_scalar", not zero(ptrL(PR, q, 1 / q) - sp.eye(2) * ptrL(PR, q, 1 / q)[0, 0]),
          "Higgs-left with K (wrong side) is not a module map")
    check("vev_restricted", sp.simplify(ptrR(PR, 0, 1)[0, 0] - q**2 / (q**2 + 1)) == 0
          and sp.simplify(ptrR(PR, 1, 0)[1, 1] - 1 / (q**2 + 1)) == 0,
          "with the vacuum (one Higgs slot, weight 1 per tr e_H = 1): plain, order-dependent entries")

    log("4. Split under each strength class, both orders, plus one-term K^{⊗4} sector trace")
    cML = (q**2 / (q**2 + 1), 1 / (q**2 + 1))   # (c_Phi, c_Conj) matter-left
    cHL = (1 / (q**2 + 1), q**2 / (q**2 + 1))   # Higgs-left
    kap = 1 / br2
    classes = {
        "general": (yu, yd, yn, ye),
        "flavour_blind_equal": (yq, yq, yq, yq),
        "slot_only_(generation_label/qdim/tr_eH)": (a, b, a, b),
        "type_only": (yq, yq, yl, yl),
        "SM_like_no_nuR": (yu, yd, 0, ye),
    }
    table = {}
    for name, ys in classes.items():
        ml = split(*cML, *ys)
        hl = split(*cHL, *ys)
        bal = split(kap, kap, *ys)
        table[name] = {"matter_left": str(sp.factor(ml)), "higgs_left": str(sp.factor(hl)),
                       "balanced_pivotal_1_over_[2]": str(sp.factor(bal))}
        log(f"  {name}: ML {sp.factor(ml)} | HL {sp.factor(hl)} | bal {sp.factor(bal)}")
    check("slot_only_zero", table["slot_only_(generation_label/qdim/tr_eH)"]["matter_left"] == "0"
          and table["slot_only_(generation_label/qdim/tr_eH)"]["higgs_left"] == "0", "flavour-slot-only strengths: 0")
    tml = split(*cML, yq, yq, yl, yl)
    check("type_only_ML", sp.simplify(tml + (yq**2 - yl**2) * (q**2 - 1) / (q**2 + 1)) == 0,
          "type-only matter-left = −(y_q² − y_ℓ²)(q²−1)/(q²+1)")
    check("type_only_odd", sp.simplify(tml + split(*cHL, yq, yq, yl, yl)) == 0, "Higgs-left = − matter-left")
    check("type_only_balanced_zero", sp.simplify(split(kap, kap, yq, yq, yl, yl)) == 0, "balanced: 0")

    # One-term K^{⊗4} sector quantum trace of a one-strand energy reproduces the strand-sum split
    def chi(t, f, c):  # t: 0 quark 1 lepton ; f: 0 u 1 d
        y = {(0, 0): yu, (0, 1): yd, (1, 0): yn, (1, 1): ye}[(t, f)]
        cc = c[0] if f == 0 else c[1]   # u slot picked by Φ (c_Phi), d slot by Φ̃ (c_Conj)
        return y**2 * cc
    K4 = TP(K1, K1, K1, K1)
    for oname, c in (("matter_left", cML), ("higgs_left", cHL)):
        def sector(qc, lf):
            num = den = 0
            for bits in itertools.product((0, 1), repeat=4):
                if sorted(bits[:3]) == sorted(qc) and bits[3] == lf:
                    i = int("".join(map(str, bits)), 2)
                    e = sum(chi(0, bt, c) for bt in bits[:3]) + chi(1, bits[3], c)
                    num += K4[i, i] * e
                    den += K4[i, i]
            return sp.simplify(num / den)
        one_term = sp.simplify(sector([0, 1, 1], 0) - sector([0, 0, 1], 1))
        check(f"one_term_eq_formula_{oname}", sp.simplify(one_term - split(*c, yu, yd, yn, ye)) == 0,
              "one-term K⊗4 sector trace = strand-sum split")
    # Argued, not computed: a one-strand energy has no pair term, so the scored two-term covariant
    # all-pairs trace (connected term 0, twoTerm_allPairs_formula / deltaT_allPairs_connected_eq_zero)
    # adds nothing to the Yukawa contribution: both trace forms give the same split.

    log("5. q → 1 order and structural factors at the proton q0 (70 dps)")
    t = sp.symbols("t")
    ser = sp.series(((q**2 - 1) / (q**2 + 1)).subs(q, 1 + t), t, 0, 3).removeO()
    from qou_substrate.constants import q_at  # noqa: PLC0415
    mp.mp.dps = 70
    q0 = mp.mpf(q_at(70))
    nums = {
        "q0": mp.nstr(q0, 70),
        "c_hi_q2_over_q2p1": mp.nstr(q0**2 / (q0**2 + 1), 50),
        "c_lo_1_over_q2p1": mp.nstr(1 / (q0**2 + 1), 50),
        "balanced_1_over_bracket2": mp.nstr(1 / (q0 + 1 / q0), 50),
        "type_only_factor_(q2-1)/(q2+1)": mp.nstr((q0**2 - 1) / (q0**2 + 1), 50),
        "type_only_factor_series_q=1+t": str(ser),
    }
    for k, v in nums.items():
        log(f"  {k} = {v}")
    check("q0_is_proton_pin", abs(q0 - mp.mpf("1.10997858275")) < mp.mpf("1e-10"), "q_at(70) proton pin")

    strengths = {
        "generation_label_(lepton_partner_crossing_count)": "all four first-generation fields carry 3 "
            "(#8698): any rule through the label alone is slot-blind ⇒ split 0. Rule itself is NEW.",
        "channel_quantum_dimension": "every singlet channel has qdim 1 (qtrace_PR) ⇒ equal ⇒ 0. Rule NEW.",
        "tr_eH_eq_1": "one normalisation shared by all four channels ⇒ type-blind ⇒ 0. Owner-ruled "
            "normalisation; as a STRENGTH rule it is NEW.",
        "partner_knot_volume_Vol·rho": "unknot (quark strand) and Hopf link / trefoil (electron, owner "
            "ruling 2026-11-21 + backup) all have Vol 0 ⇒ no strength. Not usable.",
        "Vol(4_1)/hbar_q^2_(cal2-higgs-knot-coupling)": "interpretive (block says so); a μ/e generation "
            "ratio only, CAL-2; does not reach the first-generation four.",
        "Jones/Markov_trace_of_partner": "would distinguish quark (unknot) from lepton (Hopf link) ⇒ "
            "type-only class; no corpus artifact makes it a Yukawa strength. NEW, not adopted.",
        "CategoricalHiggsIdempotent": "fields v, g, g', λ; no Yukawa field; no instance.",
    }
    out = {
        "question": "owner 2026-11-21: derive strand order and Yukawa strengths of the e_R singlet channels",
        "strand_order": {
            "verdict": "NOT forced by the corpus",
            "reasons": [
                "C·Ř·C = P·Ř·P: the orders are charge-conjugate; swap = q↦q⁻¹ on the vev entries",
                "a fixed coproduct makes the singlet invariant in each tensor product; which product "
                "(matter⊗Higgs or Higgs⊗matter) is the choice — no corpus object places the Higgs strand",
                "the weak insertion −h·P_L kills the singlet in both orders; leftLine/rightLine are letter-level",
                "the only order-free reduction (pivotal partial trace over the Higgs strand, [2]⁻¹·1) sums both "
                "Higgs slots: it does not use the vacuum and is flavour-blind",
                "with the vacuum and tr e_H = 1 (vev weight 1) the reduction is the order-dependent compression",
                "#8638 puts quark left / lepton right in the β vertex: a quark–lepton convention, no Higgs",
            ],
        },
        "strengths": {"verdict": "NOT derived", "candidates": strengths},
        "split_by_class": table,
        "numbers": nums,
        "qbeta_number": "not produced (pre-registered: order and strengths not derived)",
        "scope": "(b) for: slot-only strengths ⇒ 0 in both orders; type-only ⇒ order-odd; pivotal "
                 "partial trace ⇒ [2]⁻¹·1. (a) everywhere else; no magnitude forced",
        "selected": "none",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-yukawa-strand-order", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc: strand order and Yukawa strengths of the e_R singlet channels; "
                       "exact sympy; structural factors at proton q0, no comparison.")
    wb.add_parameter("q0", nums["q0"])
    for key, val in out.items():
        wb.add_data(key, val)
    for a_ in ASSERTS:
        wb.add_assertion(a_["name"], computed=str(int(a_["ok"])), expected="1", tolerance="0",
                         source=a_["note"])
    path = wb.save({"q0Anchor": "proton"})
    log(f"witness -> {path.relative_to(_ROOT)}; {len(ASSERTS) - len(FAILED)}/{len(ASSERTS)} pass")
    return 0 if not FAILED else 1


if __name__ == "__main__":
    sys.exit(main())
