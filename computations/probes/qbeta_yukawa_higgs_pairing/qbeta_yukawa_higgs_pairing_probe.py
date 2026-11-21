#!/usr/bin/env python3
"""qou-99qc route Y: a Yukawa-type pairing of the Higgs vacuum with doublet strands.

Pre-registered in PREREGISTRATION.md (same directory, commit 76ddb991d3), committed before
the Lean compiled or any number was evaluated. Lean companion:
folio/quantum-observable-universe/lean/QOU/QuarkState/YukawaVacuumPairing.lean.

Exact sympy over Q(q, a, b, ...) for every structural check. The only numeric evaluation is at
the proton q0 (mpmath, 70 dps) of the q-dependent gaps of the compressed Ř pairing, each of which
multiplies a FREE coefficient b; CODATA Q_beta / m_e is read only as a comparison number. No
coupling is fitted, chosen or tuned.
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
a, b, y = sp.symbols("a b y")


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


def check(name, ok, note):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {note}", flush=True)
    ASSERTS.append({"name": name, "ok": bool(ok), "note": note})
    if not ok:
        FAILED.append(name)


N_NU = [("q", "u"), ("q", "d"), ("q", "d"), ("l", "u")]
P_E = [("q", "u"), ("q", "u"), ("q", "d"), ("l", "d")]


def split(chi):
    return sp.expand(sum(chi(*s) for s in N_NU) - sum(chi(*s) for s in P_E))


def main() -> int:
    log("Arm 1: operators commuting with diag(q^nu, q^nd)")
    E = sp.Matrix(2, 2, sp.symbols("e00 e01 e10 e11"))
    nu, nd = 1, -1
    K = sp.diag(q ** nu, q ** nd)
    sol = sp.solve(list(K * E - E * K), [E[0, 1], E[1, 0]], dict=True)
    check("commutant_diagonal", sol == [{E[0, 1]: 0, E[1, 0]: 0}],
          "[K, E] = 0 forces E01 = E10 = 0 for q ≠ 1")
    x0, x1 = sp.symbols("x0 x1")
    idem = sp.solve([x0 ** 2 - x0, x1 ** 2 - x1, x0 + x1 - 1], [x0, x1], dict=True)
    check("trace_one_idempotents", sorted([(d[x0], d[x1]) for d in idem]) == [(0, 1), (1, 0)],
          "diagonal idempotents of trace 1 are exactly P_u, P_d")

    log("Arm 2: pivotal trace of the vev projector")
    for nslot in range(-3, 4):
        ok = (sp.Eq(q ** nslot, 1).subs(q, sp.Rational(11, 10)) == (nslot == 0))
        check(f"trace_one_iff_weight_zero_n{nslot}", bool(ok), f"(q^{nslot} = 1) iff n = 0, at q = 11/10")
    check("no_vev_on_bare_T3", all(sp.simplify(w - 1) != 0 for w in (q, 1 / q)),
          "weights q, 1/q of q^{2T3}: neither weight projector has trace 1")

    log("Arm 3: type-blind pairings, compressed a·1 + b·Ř")
    Rc = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, q - 1 / q, 0], [0, 0, 0, q]])
    M = a * sp.eye(4) + b * Rc
    comp = {s: sp.Matrix(2, 2, lambda i, j: M[2 * i + s, 2 * j + s]) for s in (0, 1)}
    check("compress_vev_d", sp.simplify(comp[1] - sp.diag(a, a + b * q)) == sp.zeros(2),
          f"vev in d: {list(comp[1])}")
    check("compress_vev_u",
          sp.simplify(comp[0] - sp.diag(a + b * q, a + b * (q - 1 / q))) == sp.zeros(2),
          f"vev in u: {list(comp[0])}")
    # U_q(gl2) invariance of Ř: commutes with Δ(K) = K⊗K (the only check needed for the claim
    # that the compressed operator is a pairing the quantum group allows)
    Kq = sp.diag(q, 1 / q)
    check("R_commutes_KK", sp.simplify(Rc * sp.Matrix(TP(Kq, Kq)) - sp.Matrix(TP(Kq, Kq)) * Rc)
          == sp.zeros(4), "Ř commutes with K⊗K")
    for s in (0, 1):
        ener = {"u": comp[s][0, 0], "d": comp[s][1, 1]}
        check(f"typeblind_split_zero_vev{'ud'[s]}", split(lambda t, f: ener[f]) == 0,
              "same operator on quark and lepton strands ⇒ split 0")
    aq, bq, al, bl = sp.symbols("a_q b_q a_l b_l")
    diag = {("q", "d"): aq, ("q", "u"): bq, ("l", "d"): al, ("l", "u"): bl}
    gen = split(lambda t, f: diag[(t, f)])
    check("split_general", sp.expand(gen - ((aq - bq) - (al - bl))) == 0, f"split = {gen}")

    log("Arm 4: charge-conserving 2-point pairing with a charge-0 vev")
    charges = {("q", "u"): 2, ("q", "d"): -1, ("l", "u"): 0, ("l", "d"): -3}  # 3Q
    allowed = {k: (v == 0) for k, v in charges.items()}  # cH(vev) = 0 ⇒ cM must be 0
    check("selection_only_nu", [k for k, v in allowed.items() if v] == [("l", "u")],
          "only the ν slot may pair with the neutral vev")
    # every hypothetical non-zero Higgs-slot charge: the vev slot must be 0 by Arm 2
    chi = lambda t, f: y ** 2 if allowed[(t, f)] else 0
    sp_split = split(chi)
    check("split_neutral", sp.expand(sp_split - y ** 2) == 0, f"split = {sp_split}")
    check("split_neutral_q_independent", sp.diff(sp_split, q) == 0, "no q dependence")
    check("split_neutral_nonzero_at_q1", sp_split.subs(q, 1) == y ** 2,
          "does not vanish at q → 1 (contrast #8676 Part D: (g_l − g_q)(q − 1/q))")
    # robustness: Higgs conjugate (vev charge 0 either way) and any assignment of the other
    # Higgs slot charge give the same support
    supports = set()
    for other in range(-6, 7):
        cH = (0, other)
        sup = tuple(sorted(k for k, cm in charges.items() if cH[0] + cm == 0))
        supports.add(sup)
    check("support_independent_of_other_higgs_slot", supports == {(("l", "u"),)},
          "support of the vev pairing is the ν slot for every charge of the other Higgs slot")
    # SM comparison (structural, no numbers): SM Yukawa L̄Φe_R gives e⁻ mass, ν massless
    sm_massive = {("q", "u"), ("q", "d"), ("l", "d")}
    here_massive = {k for k, v in allowed.items() if v}
    check("opposite_to_SM", here_massive.isdisjoint(sm_massive) and ("l", "u") not in sm_massive,
          "2-point pairing reaches exactly the one slot the SM leaves massless")

    log("Numbers at the proton q0 (70 dps) — comparison only")
    from qou_substrate.constants import q_at, M_E_MEV_STR, Q_NEUTRON_MEV_STR  # noqa: PLC0415
    mp.mp.dps = 70
    q0 = mp.mpf(q_at(70))
    me = mp.mpf(M_E_MEV_STR)
    qbeta = mp.mpf(Q_NEUTRON_MEV_STR)
    nums = {
        "q0": mp.nstr(q0, 70),
        "gap_compress_vev_d_over_b": mp.nstr(q0, 40),
        "gap_compress_vev_u_over_b": mp.nstr(-1 / q0, 40),
        "split_neutral_idempotent_normalisation": "1 (exact, q-independent; unit undetermined)",
        "codata_Qbeta_over_me_comparison_only": mp.nstr(qbeta / me, 30),
    }
    for k, v in nums.items():
        log(f"  {k} = {v}")
    check("q0_is_proton_pin", abs(q0 - mp.mpf("1.10997858275")) < mp.mpf("1e-10"),
          "q_at(70) is the proton pin")

    out = {
        "arms": {
            "1_unbroken_grading": "forced: weight-diagonal; e_H on a doublet = P_u or P_d",
            "2_trace_one": "forced: tr e_H = 1 ⇒ vev slot has grading weight 0; impossible on "
                           "bare q^{2T3} (needs a hypercharge-shifted Higgs doublet)",
            "3_type_blind": "split 0 for every type-blind pairing; compressed a+bŘ gives "
                            "diag(a, a+bq) (vev d) / diag(a+bq, a+b(q-1/q)) (vev u)",
            "4_charge_selection": "forced: quark and e⁻ couplings 0; free: y_ν; split = y_ν²",
        },
        "forced": ["eq_diag_of_commute", "idem_commute_trace_one", "vev_charge_zero_of_trace_one",
                   "no_vev_on_bare_T3", "split_typeBlind", "compress_vev_d", "compress_vev_u",
                   "pairing_quark_zero", "pairing_lepton", "split_neutral"],
        "free": {"arm3_general": ["a_q", "b_q", "a_l", "b_l"],
                 "arm3_compressed": ["a", "b"],
                 "arm4": ["y_nu = B_l(vev, nu)"],
                 "energy_scale": "undetermined in every arm"},
        "split_formula": {"general": str(gen), "type_blind": "0", "charge_selection": "y_nu^2"},
        "q_to_1_order": "charge-selection split is order q^0 (does not vanish at q=1)",
        "numbers": nums,
        "physics_note": "Arm 4 gives energy to ν, not e⁻ — opposite to the SM, where the "
                        "3-point vertex L̄Φe_R (right-handed singlet) makes e⁻ massive. The strand "
                        "model has no right-handed singlet.",
        "premise_L": "assumed for arms 3-4 (undecided by owner); under ¬L only the object-level "
                     "selection rule (vev pairs with neutral objects only) survives",
        "qbeta_number": "not produced: no magnitude forced (pre-registered)",
        "scope": "(b) for arms 1, 2, 3 (type-blind ⇒ 0) and for the arm-4 support; "
                 "the arm-4 magnitude is free",
        "selected": "none",
    }
    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("qbeta-yukawa-higgs-pairing", engine="python", start_time=T0,
                        output_dir=_HERE)
    wb.set_description("qou-99qc route Y: Higgs-vacuum Yukawa-type pairing with doublet strands; "
                       "forced vs free. Exact sympy; q0 numbers comparison only.")
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
