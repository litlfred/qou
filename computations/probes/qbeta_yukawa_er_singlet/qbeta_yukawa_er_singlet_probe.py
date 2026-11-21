#!/usr/bin/env python3
"""qou-99qc route Y step 2: is there a right-handed singlet e_R in the corpus?

Pre-registered in PREREGISTRATION.md (same directory, commit ba04169b03), before the Lean or any
number. Lean companion:
folio/quantum-observable-universe/lean/QOU/QuarkState/RightHandedSingletChannel.lean.

Exact sympy over Q(q, y...) for every structural check. The only numeric evaluation is the two
vev-compression entries q^2/(q^2+1), 1/(q^2+1) at the proton q0 (mpmath, 70 dps); each multiplies
a FREE Yukawa strength, so they are not predictions. CODATA Q_beta/m_e is printed for comparison
only. Nothing is fitted, chosen or tuned; the strand order is enumerated, not selected.
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


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


def zero(M):
    return all(sp.simplify(x) == 0 for x in M)


# basis of V⊗V: uu, ud, du, dd
RC = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
SING = sp.Matrix([0, q, -1, 0])
COSING = sp.Matrix([[0, 1, -1 / q, 0]])
I4 = sp.eye(4)
PR = sp.simplify((q * I4 - RC) / (q + 1 / q))
K1 = sp.diag(q, 1 / q)
E1 = sp.Matrix([[0, 1], [0, 0]])
F1 = sp.Matrix([[0, 0], [1, 0]])
I2 = sp.eye(2)


def main() -> int:
    log("1. The right line of the crossing")
    ev = {sp.simplify(k): m for k, m, _ in [(k, m, v) for k, m, v in RC.eigenvects()]}
    check("right_line_dim_1", ev.get(sp.simplify(-1 / q)) == 1, "the −q⁻¹ eigenspace of Ř is one line")
    check("left_line_dim_3", ev.get(q) == 3, "the q eigenspace (left line, q>1) is the triplet")
    check("sing_is_right_eigenvector", zero(RC * SING + SING / q), "Ř s = −q⁻¹ s, s = q·ud − du")
    check("cosing_is_left_eigenvector", zero(COSING * RC + COSING / q), "s* Ř = −q⁻¹ s*")
    check("PR_idempotent", zero(PR * PR - PR), "P_R = [2]⁻¹(q − Ř) is idempotent")
    check("PR_rank_one_form", zero(PR - SING * COSING / (q + 1 / q)), "P_R = s s*/[2]")

    log("2. U_q(sl2) singlet (stronger than the Lean T³ = 0 grading check)")
    conv = {}
    for name, dE, dF in [
        ("E⊗K+1⊗E, F⊗1+K⁻¹⊗F", TP(E1, K1) + TP(I2, E1), TP(F1, I2) + TP(K1.inv(), F1)),
        ("E⊗1+K⊗E, F⊗K⁻¹+1⊗F", TP(E1, I2) + TP(K1, E1), TP(F1, K1.inv()) + TP(I2, F1)),
    ]:
        commutes = zero(RC * dE - dE * RC) and zero(RC * dF - dF * RC)
        kills = zero(dE * SING) and zero(dF * SING)
        conv[name] = {"Rc_commutes": commutes, "kills_singlet": kills}
        log(f"  coproduct {name}: Ř commutes {commutes}, kills s {kills}")
    good = [n for n, v in conv.items() if v["Rc_commutes"]]
    check("singlet_is_Uq_invariant", len(good) >= 1 and all(conv[n]["kills_singlet"] for n in good),
          f"for the coproduct Ř intertwines ({good}), ΔE s = ΔF s = 0: s is a U_q(sl2) singlet")
    KK = TP(K1, K1)
    check("T3_zero", zero(KK * SING - SING), "(K⊗K) s = s: T³ = 0")
    check("qdim_right_line", sp.simplify((KK * PR).trace()) == 1, "Tr((K⊗K)P_R) = 1")
    check("qdim_left_line", sp.simplify((KK * (I4 - PR)).trace() - (q**2 + 1 + q**-2)) == 0,
          "Tr((K⊗K)P_L) = q² + 1 + q⁻² = [3]")
    check("weak_insertion_blind", zero(-h * (I4 - PR) * SING),
          "−h·P_L annihilates the singlet (WeakVertexLeftProjector form)")
    a1, b1, a2, b2 = sp.symbols("a1 b1 a2 b2", nonzero=True)
    x1, x2, r = sp.symbols("x1 x2 r", nonzero=True)
    Kg = sp.diag(x1 * r * x2 * r, x1 * r * x2 / r, x1 / r * x2 * r, x1 / r * x2 / r)
    check("hypercharge_adds", zero(Kg * SING - x1 * x2 * SING),
          "strand gradings x·diag(r, r⁻¹): singlet weight x₁x₂ (T³ factor cancels)")

    log("3. Functional supported on the right line: forced up to one scalar")
    phi = sp.Matrix([sp.symbols("p0:4")]).reshape(1, 4)
    sol = sp.solve(list(phi * RC + phi / q), list(phi), dict=True)
    check("vertex_forced_up_to_scalar", len(sol) == 1 and len(sol[0]) == 3,
          f"φ Ř = −q⁻¹ φ leaves one free component: {sol}")

    log("4. Charges (6Q) of the four channels; matter-up + Higgs-down")
    lep, qrk, phi_h, phit = (0, -6), (4, -2), (6, 0), (0, -6)
    chans = {"e_R (lepton⊗Φ̃)": (lep, phit), "d_R (quark⊗Φ̃)": (qrk, phit),
             "u_R (quark⊗Φ)": (qrk, phi_h), "nu_R (lepton⊗Φ)": (lep, phi_h)}
    target = {"e_R (lepton⊗Φ̃)": -6, "d_R (quark⊗Φ̃)": -2, "u_R (quark⊗Φ)": 4, "nu_R (lepton⊗Φ)": 0}
    charges = {}
    for k, (m, hh) in chans.items():
        c1, c2 = m[0] + hh[1], m[1] + hh[0]
        charges[k] = {"sixQ": c1, "sixY": 2 * c1, "components_agree": c1 == c2}
        check(f"charge_{k.split()[0]}", c1 == c2 == target[k],
              f"6Q = {c1} (both components), 6Y = {2 * c1}")
    check("B2_rh_row", sorted(v["sixY"] for v in charges.values()) == sorted([8, -4, -12, 0]),
          "6Y ∈ {8, −4, −12, 0} = B2 right-handed {4/3, −2/3, −2, 0} (entailed by Q at T³=0)")

    log("5. vev compression: (order) × (Higgs slot) enumerated")
    diag = [sp.simplify(PR[i, i]) for i in range(4)]
    idx = {"uu": 0, "ud": 1, "du": 2, "dd": 3}
    cases = {}
    for order, slot in itertools.product(("matter_left", "higgs_left"), ("u", "d")):
        f = "d" if slot == "u" else "u"   # charge selection: the matter slot paired by the singlet
        state = f + slot if order == "matter_left" else slot + f
        cases[f"{order}/vev_{slot}"] = {"matter_slot": f, "state": state,
                                        "energy": str(diag[idx[state]])}
    for k, v in cases.items():
        log(f"  {k}: picks matter {v['matter_slot']}, entry {v['energy']}")
    c_hi, c_lo = q**2 / (q**2 + 1), 1 / (q**2 + 1)
    check("diag_entries", sp.simplify(diag[1] - c_hi) == 0 and sp.simplify(diag[2] - c_lo) == 0
          and diag[0] == 0 and diag[3] == 0, "diag P_R = (0, q²/(q²+1), 1/(q²+1), 0)")
    check("entries_sum_one", sp.simplify(c_hi + c_lo - 1) == 0, "the two entries sum to 1")
    check("entries_half_at_q1", c_hi.subs(q, 1) == sp.Rational(1, 2) and c_lo.subs(q, 1) == sp.Rational(1, 2),
          "both are 1/2 at q = 1")
    ser_hi = sp.series(c_hi.subs(q, 1 + sp.Symbol("t")), sp.Symbol("t"), 0, 3).removeO()

    log("6. Split on the four-strand states, both trace forms")
    yu, yd, yn, ye = sp.symbols("y_u y_d y_nu y_e")
    results = {}
    for order in ("matter_left", "higgs_left"):
        cPhi = c_hi if order == "matter_left" else c_lo     # vev in d slot (Φ) picks u
        cConj = c_lo if order == "matter_left" else c_hi    # vev in u slot (Φ̃) picks d
        Et = {"q": sp.diag(yu**2 * cPhi, yd**2 * cConj), "l": sp.diag(yn**2 * cPhi, ye**2 * cConj)}
        types = ["q", "q", "q", "l"]
        H = sp.zeros(16, 16)
        for i, t in enumerate(types):
            ops = [I2] * 4
            ops[i] = Et[t]
            H += TP(*ops)
        K4 = TP(K1, K1, K1, K1)

        def sector_qtrace(quark_content, lep_flav):
            idxs = []
            for bits in itertools.product((0, 1), repeat=4):   # 0 = u, 1 = d
                if sorted(bits[:3]) == sorted(quark_content) and bits[3] == lep_flav:
                    idxs.append(int("".join(map(str, bits)), 2))
            num = sum(K4[i, i] * H[i, i] for i in idxs)
            den = sum(K4[i, i] for i in idxs)
            return sp.simplify(num / den)

        e_nnu = sector_qtrace([0, 1, 1], 0)
        e_pe = sector_qtrace([0, 0, 1], 1)
        one_term = sp.simplify(e_nnu - e_pe)
        formula = sp.simplify((yd**2 - ye**2) * cConj + (yn**2 - yu**2) * cPhi)
        check(f"split_formula_{order}", sp.simplify(one_term - formula) == 0,
              f"one-term qtrace split = (y_d²−y_e²)c̃ + (y_ν²−y_u²)c = {formula}")
        check(f"equal_yukawa_zero_{order}", sp.simplify(one_term.subs({yu: 1, yd: 1, yn: 1, ye: 1})) == 0,
              "equal strengths give split 0")
        results[order] = {"cPhi": str(cPhi), "cConj": str(cConj), "split_one_term_qtrace": str(one_term),
                          "split_two_term_covariant_all_pairs": str(one_term) + "  (argued: no pair term from a one-strand energy)",
                          "split_noncovariant_adjacent_comparison": str(one_term) + "  (argued; labelled comparison)",
                          "SM_no_nuR": str(sp.simplify(one_term.subs(yn, 0)))}
    # Argued, not computed (not an assertion): the Yukawa energy is a sum of one-strand
    # operators and carries no pair term; the scored two-term covariant all-pairs form and the
    # non-covariant adjacent comparison differ from the one-term trace only by PAIR insertions
    # (connected part 0 on V^3, deltaT_allPairs_connected_eq_zero). So the Yukawa contribution to
    # the split is the same in all three forms. The QED pair term itself is a sibling's subject.

    log("7. Numbers at the proton q0 (70 dps) — comparison only")
    from qou_substrate.constants import q_at, M_E_MEV_STR, Q_NEUTRON_MEV_STR  # noqa: PLC0415
    mp.mp.dps = 70
    q0 = mp.mpf(q_at(70))
    me = mp.mpf(M_E_MEV_STR)
    qbeta = mp.mpf(Q_NEUTRON_MEV_STR)
    nums = {
        "q0": mp.nstr(q0, 70),
        "c_hi_q2_over_q2p1": mp.nstr(q0**2 / (q0**2 + 1), 50),
        "c_lo_1_over_q2p1": mp.nstr(1 / (q0**2 + 1), 50),
        "c_hi_q_to_1_series_in_t": str(ser_hi),
        "codata_Qbeta_over_me_comparison_only": mp.nstr(qbeta / me, 30),
    }
    for k, v in nums.items():
        log(f"  {k} = {v}")
    check("q0_is_proton_pin", abs(q0 - mp.mpf("1.10997858275")) < mp.mpf("1e-10"), "q_at(70) proton pin")

    candidates = {
        "C1_rightLine_of_matter_x_Higgs_crossing": "QUALIFIES on T³=0, charge, distinct-from-e_L "
            "(Lean RightHandedSingletChannel); identification as e_R is scope (a), owner call",
        "C2_weak_insertion_P_R": "same object as C1 on two strands (insertion = −h·P_triplet)",
        "C3_rightLine_sigma1_in_H4_(3,1)": "fails: Hecke-side multiplicity line, commutes with U_q, "
            "carries no T³ (FlavourDoubletFourStrands scoping note)",
        "C4_mirror_bar_image_of_doublet": "fails: maps a doublet to a doublet (leftLine_mirror)",
        "C5_photon_chiral_term_s0_s1inv": "fails: a Hecke operator, not a state; no T³ "
            "(sibling #8696 owns mirror vertices)",
        "C6_sign_block_(1^3)": "fails: Λ³V = 0 for sl2; convention D weight 0",
        "C7_Gen1Quark_u_R_labels_and_B2": "labels only, no object; B2 gives the target charges",
        "C8_Furey_minimal_right_ideal (library/arxiv-1611.09182v1)": "literature, not a corpus "
            "object; supports the idempotent mechanism",
    }
    out = {
        "question": "owner 2026-11-21: find e_R in corpus",
        "candidates": candidates,
        "coproduct_check": conv,
        "channel_charges": charges,
        "vev_compression_cases": cases,
        "split": results,
        "forced": ["right line is one line (s = q·ud − du)", "T³ = 0, qdim 1", "vertex shape up to "
                   "one scalar per channel", "which Higgs slot (Φ vs Φ̃) by target charge"],
        "free": ["y_u, y_d, y_nu, y_e (one per channel)", "strand order (matter left / Higgs left): "
                 "a selection, enumerated", "energy scale"],
        "q_to_1_order": "c, c̃ → 1/2 (order q⁰); split is order q⁰ in the strengths",
        "numbers": nums,
        "qbeta_number": "not produced: no magnitude forced (pre-registered)",
        "scope": "(b) for equal strengths ⇒ 0 and for the forced shape; magnitudes free",
        "selected": "none",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-yukawa-er-singlet", engine="python", start_time=T0, output_dir=_HERE)
    wb.set_description("qou-99qc route Y step 2: the right line of the matter⊗Higgs crossing as the "
                       "e_R channel; forced vs free; both trace forms. Exact sympy; q0 comparison only.")
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
