#!/usr/bin/env python3
"""
qou-ales step 11 — the gamma-gamma bond's trace response is ONE-BODY, and its SIGN is an
artifact of an underived placement choice.

Step 10 derived the pp response r = (mu - 1)/h^2 in closed form and described it as "the
trace-weighted response over the two free 11-letter nucleon words". This probe extends the
same exact computation in two directions and finds the description too generous twice over.

SETUP. H_6, convention D, exact over Q(q). Nucleons on generators (0,1) and (3,4) -- strands
1-3 and 4-6 -- so the interface is generator 2 (strands 3-4). A gamma-gamma vertex needs TWO
ADJACENT generators, and there is no adjacent pair consisting of the interface alone: every
placement of a vertex at the interface must BORROW one generator from one of the two
nucleons. That is the root of everything below.

    V1 = sigma_2 sigma_3^-1    interface positive, borrows sigma_3 from the RIGHT nucleon
    V4 = sigma_2 sigma_1^-1    interface positive, borrows sigma_1 from the LEFT  nucleon
    V2 = sigma_3 sigma_2^-1    interface inverted, borrows sigma_3 from the RIGHT nucleon
    V3 = sigma_1 sigma_2^-1    interface inverted, borrows sigma_1 from the LEFT  nucleon

V1 is the canonical one -- step 6's `interfaceBond m = shift 2 (vertexPow m)` -- and steps
6-10 all work with V1^3 exclusively. Nothing in the arc derives the choice.

FINDING 1 (arity). At V1^3 the response is blind to the LEFT nucleon: r_pp = r_np exactly
and r_nn = r_pn exactly, while r_pp != r_nn. Four ordered channels, two values. The response
sees only the nucleon it borrows from. The free traces do differ (tr_M(pp) = 0.39605,
tr_M(nn) = 0.22575, tr_M(pn) = tr_M(np) = 0.29902) -- the two words are genuinely different
elements -- so it is the RESPONSE that collapses, not the state.

A pair interaction that cannot distinguish pp from np is not a pair interaction. The
sign-mixed two-body pattern bean qou-q8vl requires (g_pn opposite to both like-pair bonds,
i.e. deuteron bound while diproton and dineutron are not) therefore cannot be supplied by
this bond -- not because its sign is wrong but because it is not a function of the pair at
all. An ARITY obstruction, which is stronger than a sign one.

FINDING 2 (the sign is a placement artifact). Moving the borrowed generator to the other
nucleon REVERSES the sign of the binding. On the pn channel:

    V1^3  (borrow right)  ratio 1.00105775 > 1  ->  B = -4.469 keV   UNBOUND
    V3^3  (borrow left)   ratio 0.98669973 < 1  ->  B = +56.6  keV   BOUND

and the magnitude grows by a factor of ~13. So "the gamma-gamma-selected diproton is
unbound" -- the reading steps 8, 9 and 10 carry -- is scope-(a): true of V1, and reversed by
the equally-underived V3. V2 and V4 are computed here to separate the two candidate causes:
whether the sign tracks WHICH SIDE the bond borrows from, or WHICH generator carries the
inverse.

FINDING 3 (the dineutron order). c_N carries one more factor of (q^2 - 1) than c_P, so at V1
the nn/pn ratio deviates at h^5 against the diproton's h^4 -- one power weaker. Both are
unbound at V1, the diproton more so.

WHAT IS NOT AFFECTED. Step 10's closed form, its Lean file and its Theta(h^4) bracket are
correct for the word they are about. What this probe narrows is the INTERPRETATION: r is a
one-body quantity, and its sign is placement-dependent.

BY-PRODUCT, a fourth independent confirmation of bean qou-sikd: the single-nucleon H_3
convention-D Markov traces are tr_M(p) = 0.629328402... and tr_M(n) = 0.475133517...,
matching what assembly_chain_11_letter_recompute_probe recomputes and NOT the 1.145759692 /
0.987743688 literals it still compares against.

## Precision
Exact sympy over Q(q) for every derivation; mpmath at 60 dps for the numerical evaluations.
No float64 anywhere. Nothing here reads AME2020, a CODATA binding value, or a census.

## Cost
~25 min wall (56 symbolic H_6 characters). Progress is logged per block; run with
`python3 -u ... 2>&1 | tee /tmp/step11.log`.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/hecke", "computations/markov",
           "computations/substrate", "tools/pyhecke/python", "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402
from markov_weights_symbolic import solve_y_lambda, tr_M_canonical  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)

T = sp.symbols("t", positive=True)
P_P = (Q**18 - 3*Q**16 + 7*Q**14 - 8*Q**12 + 10*Q**10 - 9*Q**8 + 10*Q**6
       - 6*Q**4 + 3*Q**2 - 1)
P_N = Q**14 - 3*Q**12 + 4*Q**10 - 4*Q**8 + 5*Q**6 - 4*Q**4 + 3*Q**2 - 1
TR_P = (Q**4 + 1) * P_P / (4 * Q**9 * (Q**2 + 1)**2)
TR_N = (Q**4 + 1) * P_N / (4 * Q**9)

# The four vertices at the interface. (positive generator, inverted generator, borrowed side)
VERTICES = {
    "V1": (2, 3, "right"),   # canonical: step 6's shift 2 (vertexPow m)
    "V2": (3, 2, "right"),
    "V3": (1, 2, "left"),
    "V4": (2, 1, "left"),
}


def nucleon(kind: str, g0: int) -> list[tuple[int, str]]:
    """The canonical 11-letter nucleon element on generators (g0, g0+1), as ctypes.

    Same construction as step 3's `nucleon_block`: beta_Bor = (sigma_0 sigma_1^-1)^3, then
    the three quark letters (colour-blind -h/2 averages), then two gluon sigma_0 crossings.
    """
    g1 = g0 + 1
    w: list[tuple[int, str]] = []
    for _ in range(3):
        w += [(g0, "sigma"), (g1, "sigma_inv")]
    if kind == "p":
        w += [(g0, "sigma"), (g0, "averaged"), (g1, "averaged")]
    else:
        w += [(g0, "averaged"), (g0, "averaged"), (g1, "sigma_inv")]
    w += [(g0, "sigma"), (g0, "sigma")]
    return w


def vertex_pow(name: str, m: int = 3) -> list[tuple[int, str]]:
    pos, inv, _side = VERTICES[name]
    return [(pos, "sigma"), (inv, "sigma_inv")] * m


def vanishing_order(poly: sp.Expr) -> tuple[int, list]:
    co = sp.Poly(sp.expand(sp.cancel(poly).subs(Q, 1 + T)), T).all_coeffs()[::-1]
    k = 0
    while k < len(co) and co[k] == 0:
        k += 1
    return k, co


def main() -> int:
    t0 = time.time()
    q = Q_MP
    h2 = (q - 1 / q) ** 2
    qv = sp.Rational(Q_50_DIGIT_STR)
    h2_sym = sp.cancel((Q - 1 / Q) ** 2)

    print(f"qou-ales step 11 — bond response arity + placement (proton pin, {DPS} dps)")
    print(f"  q_0 = {mp.nstr(q, 20)}   h^2 = {mp.nstr(h2, 20)}   h^4 = {mp.nstr(h2**2, 20)}")

    y6 = solve_y_lambda(6)
    support = sorted((lam for lam in y6 if sp.cancel(y6[lam]) != 0), key=len)
    print(f"  convention-D weight support at H_6: {support} "
          f"({len(support)} of {len(y6)} blocks)")

    dev_trp = sp.simplify(sp.cancel(tr_M_canonical(nucleon("p", 0), 3)[0]) - TR_P)
    dev_trn = sp.simplify(sp.cancel(tr_M_canonical(nucleon("n", 0), 3)[0]) - TR_N)
    print(f"\n  tr_M,H3(p) = {sp.N(TR_P.subs(Q, qv), 22)}  (closed-form dev {dev_trp})")
    print(f"  tr_M,H3(n) = {sp.N(TR_N.subs(Q, qv), 22)}  (closed-form dev {dev_trn})")
    print("  qou-sikd cross-check: assembly_chain_11_letter_recompute_probe still compares"
          " against 1.145759692 / 0.987743688, which these are not.")

    def trM(word, tag):
        tot = sp.Integer(0)
        for lam in support:
            t1 = time.time()
            tot += sp.cancel(y6[lam] * sp.cancel(chi_lambda_symbolic(lam, word)))
            print(f"      [{tag}] chi^{str(lam):<8} {time.time() - t1:6.1f}s", flush=True)
        return sp.cancel(sp.together(tot))

    from qou_substrate.constants import M_E_MEV  # noqa: PLC0415
    me = mp.mpf(str(M_E_MEV))
    alpha = me * (1 / (q - 1)) ** 2 * (1 - 1 / q) / (1 - (1 - 1 / q) ** 2)

    CH = [("pp", "p", "p"), ("nn", "n", "n"), ("pn", "p", "n"), ("np", "n", "p")]
    free_tr: dict[str, sp.Expr] = {}
    mult_dev: dict[str, sp.Expr] = {}
    rows: dict[tuple[str, str], dict] = {}

    # Grid A: all four ordered channels at the canonical vertex V1.
    # Grid B: the two unlike channels at V2, V3, V4 (the placement experiment).
    # The FULL grid: every vertex against every ordered channel. The like-pair rows are
    # what decide each vertex's arity -- r_pp vs r_np (both right = p) and r_nn vs r_pn
    # (both right = n) test right-dependence; r_pp vs r_pn and r_nn vs r_np test left.
    # An earlier version computed only pn and np off V2/V3/V4, which cannot decide either:
    # pn != np is CONSISTENT with right-dependence (the right nucleon differs).
    plan = [(lbl, v) for v in ("V1", "V2", "V3", "V4") for lbl, _, _ in CH]

    for label, left, right in CH:
        free = nucleon(left, 0) + nucleon(right, 3)
        print(f"\n  --- channel {label} free trace ---", flush=True)
        tf = trM(free, f"{label}/free")
        free_tr[label] = tf
        expect = sp.cancel((TR_P if left == "p" else TR_N) * (TR_P if right == "p" else TR_N))
        mult_dev[label] = sp.simplify(tf - expect)
        print(f"    tr_M(free) @q0 = {sp.N(tf.subs(Q, qv), 22)}   "
              f"(multiplicativity dev {mult_dev[label]})", flush=True)

    for label, vname in plan:
        left, right = next((l, r) for lb, l, r in CH if lb == label)
        free = nucleon(left, 0) + nucleon(right, 3)
        print(f"\n  --- channel {label} with {vname}^3 "
              f"(borrows from the {VERTICES[vname][2]}) ---", flush=True)
        ta = trM(free + vertex_pow(vname), f"{label}/{vname}")
        ratio = sp.cancel(ta / free_tr[label])
        r = sp.cancel((ratio - 1) / h2_sym)
        c = sp.cancel(r / h2_sym)
        ratio_v = mp.mpf(str(sp.N(ratio.subs(Q, qv), DPS + 10)))
        B = -alpha * mp.log(ratio_v)
        rows[(label, vname)] = {
            "left": left, "right": right, "borrows": VERTICES[vname][2],
            "ratio": ratio, "r": r, "c": c, "ratio_v": ratio_v, "B": B,
        }
        print(f"    ratio @q0 = {mp.nstr(ratio_v, 20)}   r = "
              f"{sp.N(r.subs(Q, qv), 20)}   c = {sp.N(c.subs(Q, qv), 20)}", flush=True)
        print(f"    B = {mp.nstr(B * 1000, 12)} keV   "
              f"{'BOUND' if B > 0 else 'unbound'}", flush=True)

    # ---------------- FINDING 1: arity, per vertex ----------------
    print("\n  FINDING 1 — every vertex's response is ONE-BODY, in the slot it borrows from:")
    print(f"    {'vertex':>7} {'borrows':>8} {'right-dependent':>16} {'left-dependent':>15}"
          f" {'two-body?':>10}")
    arity: dict[str, dict] = {}
    for vname in ("V1", "V2", "V3", "V4"):
        dr1 = sp.simplify(rows[("pp", vname)]["r"] - rows[("np", vname)]["r"])
        dr2 = sp.simplify(rows[("nn", vname)]["r"] - rows[("pn", vname)]["r"])
        dl1 = sp.simplify(rows[("pp", vname)]["r"] - rows[("pn", vname)]["r"])
        dl2 = sp.simplify(rows[("nn", vname)]["r"] - rows[("np", vname)]["r"])
        right = bool(dr1 == 0 and dr2 == 0)
        left = bool(dl1 == 0 and dl2 == 0)
        arity[vname] = {"right_dependent": right, "left_dependent": left,
                        "borrows": VERTICES[vname][2],
                        "dev_pp_np": sp.sstr(dr1), "dev_nn_pn": sp.sstr(dr2),
                        "dev_pp_pn": sp.sstr(dl1), "dev_nn_np": sp.sstr(dl2)}
        print(f"    {vname:>7} {VERTICES[vname][2]:>8} {str(right):>16} {str(left):>15}"
              f" {str(not (right or left)):>10}")
    all_one_body = all(arity[v]["right_dependent"] or arity[v]["left_dependent"]
                       for v in ("V1", "V2", "V3", "V4"))
    borrowed_slot_matches = all(
        (arity[v]["right_dependent"] if VERTICES[v][2] == "right"
         else arity[v]["left_dependent"]) for v in ("V1", "V2", "V3", "V4"))
    d_p_n = sp.simplify(rows[("pp", "V1")]["r"] - rows[("nn", "V1")]["r"])
    print(f"    every vertex one-body            : {all_one_body}")
    print(f"    and in the slot it BORROWS from  : {borrowed_slot_matches}")
    print(f"    not zero-body (r_pp != r_nn at V1): {d_p_n != 0}")
    d_pp_np = arity["V1"]["dev_pp_np"]
    d_nn_pn = arity["V1"]["dev_nn_pn"]

    # ---------------- FINDING 2: placement flips the sign ----------------
    print("\n  FINDING 2 — the sign tracks the placement, not the species:")
    print(f"    {'channel':>8} {'vertex':>7} {'borrows':>8} {'ratio':>24} {'B [keV]':>14}  verdict")
    for label, vname in plan:
        d = rows[(label, vname)]
        print(f"    {label:>8} {vname:>7} {d['borrows']:>8} {mp.nstr(d['ratio_v'], 18):>24} "
              f"{mp.nstr(d['B'] * 1000, 10):>14}  {'BOUND' if d['B'] > 0 else 'unbound'}")
    sign_by_side = (rows[("pn", "V1")]["B"] < 0 and rows[("pn", "V2")]["B"] < 0
                    and rows[("pn", "V3")]["B"] > 0 and rows[("pn", "V4")]["B"] > 0)
    sign_by_inverse = (rows[("pn", "V1")]["B"] < 0 and rows[("pn", "V4")]["B"] < 0
                       and rows[("pn", "V2")]["B"] > 0 and rows[("pn", "V3")]["B"] > 0)
    print(f"    sign tracks the BORROWED SIDE      : {sign_by_side}")
    print(f"    sign tracks WHICH GEN IS INVERTED  : {sign_by_inverse}")
    v1_v3_flip = bool(rows[("pn", "V1")]["B"] * rows[("pn", "V3")]["B"] < 0)
    print("    NOTE: r_pn != r_np does NOT discriminate arity -- it is consistent with"
          " right-dependence, since the right nucleon differs. Only the LIKE-pair"
          " comparisons in finding 1 decide it.")

    # ---------------- FINDING 3: the dineutron order ----------------
    print("\n  FINDING 3 — order in (q^2 - 1) of c = r/h^2 at V1:")
    orders = {}
    for label, _, _ in CH:
        k, co = vanishing_order(sp.fraction(sp.cancel(rows[(label, "V1")]["c"]))[0])
        orders[label] = k
        print(f"    {label}: numerator vanishes to order {k} at q = 1; t^0..t^3 = {co[:4]}")
    all_unbound_v1 = all(rows[(lbl, "V1")]["B"] < 0 for lbl, _, _ in CH)

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("two-nucleon-bond-response-arity-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 11: extends step 10's exact H_6 convention-D response computation to all "
        "four ORDERED two-nucleon channels and to all four gamma-gamma vertices at the "
        "interface. FINDING 1 (arity): at the canonical vertex V1 = sigma_2 sigma_3^-1 the "
        "response r is a function of the RIGHT nucleon ALONE -- r_pp = r_np and r_nn = r_pn "
        "exactly, r_pp != r_nn -- because a gamma-gamma vertex needs two adjacent generators and "
        "so must BORROW one from a nucleon; it sees only the one it borrows from. So it cannot "
        "distinguish a like pair from an unlike one, which is an ARITY obstruction to the "
        "sign-mixed two-body pattern qou-q8vl requires, stronger than a sign objection. "
        "FINDING 2: moving the borrowed generator to the other nucleon REVERSES the binding sign "
        "(V1 unbinds the deuteron by 4.469 keV; V3 = sigma_1 sigma_2^-1 BINDS it by ~57 keV, 13x "
        "larger), so the 'unbound' reading carried by steps 8-10 is scope-(a) -- true of V1 and "
        "reversed by the equally underived V3. FINDING 3: c_N carries one more factor (q^2-1) "
        "than c_P, so at V1 the dineutron deviates at h^5 against the diproton's h^4. Step 10's "
        "closed form and Lean are unaffected; what narrows is the interpretation. By-product: a "
        "fourth confirmation of qou-sikd. No AME/CODATA binding value or census read.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (z = q^3/(q^2+1); two-row weight support at H_6)")
    w.add_parameter("dps", DPS)
    w.add_parameter("nucleon_generators", "left (0,1); right (3,4); interface generator 2")
    w.add_parameter("interface_letters", "colour-blind -h/2 (NOT the colour-weighted variant)")
    w.add_parameter("vertices", {k: {"positive_gen": v[0], "inverted_gen": v[1],
                                     "borrows_from": v[2]} for k, v in VERTICES.items()})
    w.add_parameter("canonical_vertex", "V1 = sigma_2 sigma_3^-1 (step 6 shift 2 vertexPow)")
    w.add_data("weight_support", [list(lam) for lam in support])
    w.add_data("tr_M_H3_proton_symbolic", sp.sstr(sp.factor(sp.cancel(TR_P))))
    w.add_data("tr_M_H3_neutron_symbolic", sp.sstr(sp.factor(sp.cancel(TR_N))))
    w.add_data("tr_M_H3_proton_at_q0", fmt(mp.mpf(str(sp.N(TR_P.subs(Q, qv), DPS + 10)))))
    w.add_data("tr_M_H3_neutron_at_q0", fmt(mp.mpf(str(sp.N(TR_N.subs(Q, qv), DPS + 10)))))
    for label, _, _ in CH:
        w.add_data(f"free_trace_{label}", {
            "symbolic": sp.sstr(sp.factor(free_tr[label])),
            "at_q0": fmt(mp.mpf(str(sp.N(free_tr[label].subs(Q, qv), DPS + 10)))),
        })
    for (label, vname), d in rows.items():
        w.add_data(f"response_{label}_{vname}", {
            "left": d["left"], "right": d["right"], "borrows_from": d["borrows"],
            "ratio_at_q0": fmt(d["ratio_v"]),
            "r_symbolic": sp.sstr(sp.factor(d["r"])),
            "c_symbolic": sp.sstr(sp.factor(d["c"])),
            "r_at_q0": fmt(mp.mpf(str(sp.N(d["r"].subs(Q, qv), DPS + 10)))),
            "c_at_q0": fmt(mp.mpf(str(sp.N(d["c"].subs(Q, qv), DPS + 10)))),
            "B_keV": fmt(d["B"] * 1000),
            "bound": bool(d["B"] > 0),
        })
    w.add_data("c_numer_vanishing_order_at_V1", orders)
    w.add_data("alpha_E0_full_MeV", fmt(alpha))
    w.add_assertion(name="tr_H3_proton_matches_closed_form", computed=sp.sstr(dev_trp),
                    expected="0", tolerance="0",
                    source="tr_M_canonical(11-letter p, 3) vs (q^4+1)P_P/(4q^9(q^2+1)^2)")
    w.add_assertion(name="tr_H3_neutron_matches_closed_form", computed=sp.sstr(dev_trn),
                    expected="0", tolerance="0",
                    source="tr_M_canonical(11-letter n, 3) vs (q^4+1)P_N/(4q^9)")
    for label, _, _ in CH:
        w.add_assertion(name=f"free_trace_multiplicative_{label}",
                        computed=sp.sstr(mult_dev[label]), expected="0", tolerance="0",
                        source="disjoint-union multiplicativity tr_M(W_l W_r) = tr_M(l) tr_M(r)")
    w.add_assertion(name="V1_response_blind_to_left_when_right_is_p",
                    computed=d_pp_np, expected="0", tolerance="0",
                    source="r_pp(V1) - r_np(V1): V1 borrows right, so the left cancels")
    w.add_assertion(name="V1_response_blind_to_left_when_right_is_n",
                    computed=d_nn_pn, expected="0", tolerance="0",
                    source="r_nn(V1) - r_pn(V1)")
    w.add_assertion(name="V1_response_does_depend_on_the_borrowed_nucleon",
                    computed=str(int(d_p_n != 0)), expected="1", tolerance="0",
                    source="r_pp(V1) != r_nn(V1) -- one-body, not zero-body")
    w.add_data("arity_by_vertex", arity)
    w.add_assertion(name="every_vertex_response_is_one_body",
                    computed=str(int(all_one_body)), expected="1", tolerance="0",
                    source="per vertex: the two LIKE-pair deviations vanish in one slot")
    w.add_assertion(name="one_body_slot_is_the_borrowed_slot",
                    computed=str(int(borrowed_slot_matches)), expected="1", tolerance="0",
                    source="right-borrowing vertices are right-dependent; left ones left")
    w.add_assertion(name="placement_reverses_the_binding_sign",
                    computed=str(int(v1_v3_flip)), expected="1", tolerance="0",
                    source="B_pn(V1) < 0 < B_pn(V3): the sign is a placement artifact")
    w.add_assertion(name="proton_response_coeff_order_zero_at_V1",
                    computed=str(orders["pp"]), expected="0", tolerance="0",
                    source="c_P does not vanish at q = 1, so mu - 1 ~ h^4 (step 10)")
    w.add_assertion(name="neutron_response_coeff_order_one_at_V1",
                    computed=str(orders["nn"]), expected="1", tolerance="0",
                    source="c_N vanishes to first order at q = 1, so mu - 1 ~ h^5")
    w.add_assertion(name="all_four_channels_unbound_at_V1",
                    computed=str(int(all_unbound_v1)), expected="1", tolerance="0",
                    source="every V1 ratio > 1, so B < 0 in all four channels")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
