#!/usr/bin/env python3
"""qou-cds1 Step 28: the all-pairs decay rates are DERIVED — they are the
transfer matrix's spectral ratio per bond, they are sector-indexed by bar
parity, and they are not independent.

Step 27 stopped because an all-pairs coupling needs a falloff rate per bond type
and three fitted rates would be three free parameters. The owner's steer: the
rates are already in how CAL 1/2/3 are defined, and the link is the spectral
decomposition of the transfer matrix operating on the tower. Both halves check
out, and nothing below is fitted.

*** WHERE THE RATES WERE ***

The canonical MATH-IDEAL calibration triple is not three masses. It is
(m_e, D_beta, D_pi) — CAL-2 is the neutron beta-decay WIDTH at order h^2 and
CAL-3 the pion decay WIDTH at order h^3 (owner ruling 2026-06-26;
`knots-particles-confinement/meson-scale-independence-calibration.md`). The
masses m_mu/m_e and m_pi are the observational proxies. Two of the three
calibration points are decay rates by definition.

*** THE TRANSFER MATRIX, AND ITS SPECTRUM PER BOND ***

`chi_monotone_transfer` computes chi^lambda by a fine-Bratteli transfer matrix
over edges (s_g subset s_{g+1}) of the tower ∅ = s_0 ⊂ … ⊂ s_n = lambda, one
step per generator. Its `_alpha_beta` reduces each step by Cayley–Hamilton:

    O_g = Prod_j (sigma_g + d_j . 1) = alpha . sigma_g + beta . I
    E_1 = Prod_j (q + d_j)          E_2 = Prod_j (-1/q + d_j)

E_1 and E_2 ARE the transfer step's spectrum, so the decay rate carried across
one bond is the spectral ratio |E_2/E_1| — the standard transfer-matrix
correlation falloff. For a single interface letter of offset d that is
|(d - 1/q)/(d + q)|, and the corpus's own bond templates give it in closed form:

    bond                 offset d        E_1          E_2         E_2/E_1
    p-p   sigma          0               q            -1/q        -1/q^2
    n-n   sigma^-1       -h              1/q          -q          -q^2
    p-n   average        -h/2            (q^2+1)/2q   -(q^2+1)/2q  -1     EXACTLY
    p-n   color-weighted -h(1/2-delta/4)                          -1 + tanh(ln q).delta + O(delta^2)

Three rates, all closed forms in q, no free parameter anywhere. This is what
Step 27 said it would not invent.

*** THEY ARE NOT INDEPENDENT ***

    r_pp . r_nn = 1 = r_pn^2          ONE exact relation
    r_nn / r_pp = q^4

So the three bond rates carry ONE degree of freedom, q^2 — not three. An
all-pairs coupling built on them adds no parameter to the framework.

*** AND THEY ARE SECTOR-INDEXED, BY BAR PARITY ***

`interaction-sector-taxonomy.md` classifies the three interaction sectors by the
bar involution q -> 1/q: strong is bar-EVEN (cosh channel), weak is bar-ODD
(sinh channel), and electromagnetic is provably the cell admitting NO pure
parity. The bond rates reproduce that classification exactly:

    r_pp(1/q) = r_nn(q)  and  r_nn(1/q) = r_pp(q)   -> a bar-conjugate PAIR
    r_pn(1/q) = r_pn(q) = -1                        -> bar-FIXED

    product  r_pp . r_nn = 1     bar-EVEN   -> STRONG  (cosh channel)
    ratio    r_nn / r_pp = q^4   bar-ODD    -> WEAK    (sinh channel)
    r_pn                          bar-fixed at -1, and its DEPARTURE is

        1 - |r_pn| = 2.delta.(q^2-1) / (delta.(q^2-1) + 2q^2 + 2)
                   = tanh(ln q) . delta + O(delta^2)

    because tanh(ln q) = (q - 1/q)/(q + 1/q) = (q^2-1)/(q^2+1). And
    tanh(ln q_0) = 0.103963710 is EXACTLY the odd-to-even ratio the taxonomy
    derives for the ELECTROMAGNETIC coupling — the mixed cell. Measured:
    tanh(ln q_0) . delta = 1.4302400e-4 against 1.4301377e-4, agreeing to
    7.2e-5 relative, which is the second order in delta.

So the p-p / n-n pair is the bar-conjugate (strong/weak) axis, and the p-n bond
sits at the intertwiner point carrying the EM ratio — the same place the
taxonomy independently puts the electromagnetic sector. The rates differ by
sector and they are not independent, exactly as the owner said.

*** THE h-ORDERS LINE UP WITH THE CAL LADDER ***

    delta = flavor_split_leading(q)   measured order in (q-1): 2.99999  -> O(h^3)
    tanh(ln q)                                                          -> O(h)
    1 - |r_pn| = tanh(ln q).delta                                       -> O(h^4)
    r_pp, r_nn = -q^{-+2}                                               -> O(h^0)

delta sits at CAL-3's order h^3, the pion decay width's order. The bond rates
themselves are O(h^0) with a bar-odd ratio q^4.

*** WHAT THIS DOES NOT YET DO ***

It supplies the RATE, not the coupling word. A non-adjacent nucleon pair still
has no single generator to sit on — sigma_g couples strands g and g+1 only — so
building the all-pairs word remains a construction, and Step 27's caveat stands.
What is removed is the three-free-parameter objection: the falloff is derived.

SCOPE. Scope-(a). Nothing derived here is wired, proposed or readmitted; no
convention adjudicated; no c_k value asserted. Anchor: experimental (proton) pin.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate"),
                str(HERE.parent / "hecke"), str(HERE.parent / "markov")]
import _path_bridge  # noqa: E402, F401

import qou_substrate.constants as CONST  # noqa: E402
from _li_2_q_util import flavor_split_leading, flavor_split_subleading  # noqa: E402

mp.mp.dps = 40
Q0 = mp.mpf(str(CONST.Q_50_DIGIT_STR))
H0 = Q0 - 1 / Q0
QS = sp.Symbol("q", positive=True)
HS = QS - 1 / QS
DL = sp.Symbol("delta", positive=True)


def transfer_spectrum(d):
    """`(E_1, E_2)` of one transfer step `sigma + d.1` — `_alpha_beta`'s
    Cayley-Hamilton eigenvalues, which ARE the step's spectrum."""
    return sp.cancel(QS + d), sp.cancel(-1 / QS + d)


def bond_rate(d):
    e1, e2 = transfer_spectrum(d)
    return sp.cancel(e2 / e1)


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:  # noqa: C901 — one linear narrative, deliberately not split
    t_start = time.monotonic()
    print("=" * 78)
    print(" Step 28: the bond decay rates are the transfer matrix's spectral")
    print("          ratio — derived, sector-indexed, and not independent")
    print("=" * 78)

    # [1] the rates, in closed form ------------------------------------------
    bonds = [("p-p", "sigma", sp.Integer(0)),
             ("n-n", "sigma^-1", -HS),
             ("p-n", "average", -HS / 2)]
    rates = {}
    print(f"\n[1] the transfer step's spectrum per bond, and its ratio")
    print(f"    {'bond':6s}{'template':12s}{'offset d':>14s}{'E_1':>18s}"
          f"{'E_2':>18s}{'E_2/E_1':>12s}")
    for name, tmpl, d in bonds:
        e1, e2 = transfer_spectrum(d)
        r = bond_rate(d)
        rates[name] = r
        print(f"    {name:6s}{tmpl:12s}{str(sp.factor(d)):>14s}"
              f"{str(sp.factor(e1)):>18s}{str(sp.factor(e2)):>18s}"
              f"{str(sp.factor(r)):>12s}")
    r_pp, r_nn, r_pn = rates["p-p"], rates["n-n"], rates["p-n"]
    print(f"    -> |E_2/E_1| = q^-2 (p-p), q^+2 (n-n), 1 (p-n) — EXACT, closed")
    print(f"       forms in q. This is the falloff rate Step 27 declined to invent.")

    # [2] one relation, one degree of freedom --------------------------------
    prod = sp.simplify(r_pp * r_nn)
    pn_sq = sp.simplify(r_pn ** 2)
    ratio = sp.simplify(r_nn / r_pp)
    not_indep = bool(sp.simplify(prod - pn_sq) == 0 and prod == 1)
    print(f"\n[2] the three rates are NOT independent")
    print(f"    r_pp . r_nn = {prod}      r_pn^2 = {pn_sq}      "
          f"=> r_pp . r_nn = r_pn^2 : {not_indep}")
    print(f"    r_nn / r_pp = {ratio}")
    print(f"    ONE relation among three rates -> ONE degree of freedom (q^2).")
    print(f"    An all-pairs coupling on these adds NO parameter to the framework.")

    # [3] bar parity reproduces the sector taxonomy ---------------------------
    bar_pp = sp.simplify(r_pp.subs(QS, 1 / QS))
    bar_nn = sp.simplify(r_nn.subs(QS, 1 / QS))
    bar_pn = sp.simplify(r_pn.subs(QS, 1 / QS))
    exch = bool(sp.simplify(bar_pp - r_nn) == 0 and sp.simplify(bar_nn - r_pp) == 0)
    fixed = bool(sp.simplify(bar_pn - r_pn) == 0)
    prod_even = bool(sp.simplify(prod.subs(QS, 1 / QS) - prod) == 0)
    ratio_odd = bool(sp.simplify(ratio.subs(QS, 1 / QS) * ratio - 1) == 0)
    print(f"\n[3] bar parity (q -> 1/q) reproduces the interaction-sector taxonomy")
    print(f"    r_pp(1/q) = {bar_pp}   r_nn(1/q) = {bar_nn}   r_pn(1/q) = {bar_pn}")
    print(f"    p-p and n-n EXCHANGE under the bar : {exch}   "
          f"p-n is bar-FIXED : {fixed}")
    print(f"    product r_pp.r_nn = 1   bar-EVEN : {prod_even}  -> STRONG (cosh)")
    print(f"    ratio r_nn/r_pp = q^4   bar-ODD  : {ratio_odd}  -> WEAK   (sinh)")

    # [4] the electromagnetic link -------------------------------------------
    x = (QS + 1 / QS) / 2
    y = HS * DL / 4
    dep = sp.cancel(sp.simplify(1 - (x - y) / (x + y)))
    lead = sp.cancel(sp.simplify(sp.series(dep, DL, 0, 2).removeO() / DL))
    tanh_closed = sp.cancel((QS - 1 / QS) / (QS + 1 / QS))
    tanh_is_lead = bool(sp.simplify(lead - tanh_closed) == 0)
    tanh0 = mp.tanh(mp.log(Q0))
    tanh0_closed = (Q0 - 1 / Q0) / (Q0 + 1 / Q0)
    print(f"\n[4] the p-n bond's departure carries the taxonomy's EM ratio")
    print(f"    1 - |r_pn| = {dep}")
    print(f"    leading coefficient in delta = {lead}")
    print(f"    and tanh(ln q) = (q - 1/q)/(q + 1/q) = {tanh_closed} : {tanh_is_lead}")
    print(f"    |tanh(ln q_0) - closed form|  = "
          f"{mp.nstr(mp.fabs(tanh0 - tanh0_closed), 4)}")
    print(f"    tanh(ln q_0) = {mp.nstr(tanh0, 18)}")
    print(f"    — EXACTLY the odd-to-even ratio `interaction-sector-taxonomy.md`")
    print(f"      derives for the ELECTROMAGNETIC coupling (0.10396), the cell it")
    print(f"      proves admits no pure parity.")
    dep_rows = {}
    for nm, fn in (("leading", flavor_split_leading),
                   ("subleading", flavor_split_subleading)):
        dlt = mp.mpf(str(fn(Q0)))
        d_num = -(H0 * (mp.mpf("0.5") - dlt / 4))
        r_num = mp.fabs((-1 / Q0 + d_num) / (Q0 + d_num))
        pred = tanh0 * dlt
        rel = mp.fabs(pred - (1 - r_num)) / (1 - r_num)
        dep_rows[nm] = (dlt, r_num, pred, rel)
        print(f"    delta_{nm:11s} = {mp.nstr(dlt, 18)}")
        print(f"      measured 1 - |r_pn|  = {mp.nstr(1 - r_num, 18)}")
        print(f"      tanh(ln q_0) . delta = {mp.nstr(pred, 18)}    relative "
              f"difference {mp.nstr(rel, 6)}  (2nd order in delta)")

    # [5] h-orders against the CAL ladder -------------------------------------
    print(f"\n[5] h-orders, against the math-ideal CAL ladder h^0 / h^2 / h^3")
    print(f"    CAL-1 m_e (h^0) · CAL-2 D_beta, neutron beta-decay width (h^2) ·")
    print(f"    CAL-3 D_pi, pion decay width (h^3). Two of three ARE decay rates.")
    ords = {}
    for nm, fn in (("delta", flavor_split_leading),):
        vals = []
        for k in (3, 4, 5, 6):
            e = mp.mpf(10) ** (-k)
            vals.append((e, mp.mpf(str(fn(1 + e)))))
        ps = [mp.log(vals[i - 1][1] / vals[i][1]) / mp.log(vals[i - 1][0] / vals[i][0])
              for i in range(1, len(vals))]
        ords[nm] = ps[-1]
        print(f"    order of {nm} in (q-1) : {mp.nstr(ps[-1], 10)}")
    t_ord = []
    for k in (3, 4, 5, 6):
        e = mp.mpf(10) ** (-k)
        t_ord.append((e, mp.tanh(mp.log(1 + e))))
    p_t = mp.log(t_ord[-2][1] / t_ord[-1][1]) / mp.log(t_ord[-2][0] / t_ord[-1][0])
    print(f"    order of tanh(ln q)  : {mp.nstr(p_t, 10)}")
    print(f"    -> delta is O(h^3), CAL-3's order (the pion decay width). tanh is")
    print(f"       O(h). So 1 - |r_pn| = O(h^4), while r_pp and r_nn are O(h^0)")
    print(f"       with a bar-odd ratio q^4.")

    # ------------------------------------------------------------- assertions
    a = [
        {"name": "bond_decay_rates_are_closed_forms_in_q",
         "passed": bool(sp.simplify(r_pp + 1 / QS ** 2) == 0
                        and sp.simplify(r_nn + QS ** 2) == 0
                        and r_pn == -1),
         "detail": "the transfer step's spectrum is E_1 = Prod(q + d_j), E_2 = "
                   "Prod(-1/q + d_j) (`chi_monotone_transfer._alpha_beta`), so the "
                   "per-bond falloff is E_2/E_1: -1/q^2 for p-p (d=0), -q^2 for n-n "
                   "(d=-h), and EXACTLY -1 for the averaged p-n (d=-h/2). Three closed "
                   "forms in q with no free parameter — the rate Step 27 declined to "
                   "invent was already determined by the transfer matrix"},
        {"name": "the_three_rates_carry_one_degree_of_freedom",
         "passed": bool(not_indep and sp.simplify(ratio - QS ** 4) == 0),
         "detail": "r_pp . r_nn = 1 = r_pn^2 is an exact relation among the three, and "
                   "r_nn / r_pp = q^4. So the bond rates have ONE degree of freedom "
                   "(q^2), not three: an all-pairs coupling built on them adds no "
                   "parameter to the framework. They are not independent"},
        {"name": "bar_parity_reproduces_the_interaction_sector_taxonomy",
         "passed": bool(exch and fixed and prod_even and ratio_odd),
         "detail": "under q -> 1/q the p-p and n-n rates EXCHANGE and the p-n rate is "
                   "FIXED. Their product (=1) is bar-even — the taxonomy's STRONG cosh "
                   "channel; their ratio (=q^4) is bar-odd — its WEAK sinh channel. The "
                   "sector classification `interaction-sector-taxonomy.md` states by "
                   "parity is recovered from the bond rates alone"},
        {"name": "pn_departure_is_the_electromagnetic_ratio_times_the_flavour_split",
         "passed": bool(tanh_is_lead
                        and all(v[3] < mp.mpf("1e-3") for v in dep_rows.values())),
         "detail": f"1 - |r_pn| = 2.delta.(q^2-1)/(delta.(q^2-1) + 2q^2 + 2), whose "
                   f"leading coefficient is (q^2-1)/(q^2+1) = tanh(ln q). At the pin "
                   f"tanh(ln q_0) = {mp.nstr(tanh0, 12)} — exactly the odd-to-even ratio "
                   f"the taxonomy derives for the ELECTROMAGNETIC coupling, the cell it "
                   f"proves admits no pure parity. Predicted "
                   f"{mp.nstr(dep_rows['leading'][2], 10)} against measured "
                   f"{mp.nstr(1 - dep_rows['leading'][1], 10)}, agreeing to "
                   f"{mp.nstr(dep_rows['leading'][3], 4)} relative — the second order "
                   f"in delta. So the p-n bond sits at the intertwiner point, which is "
                   f"where the taxonomy independently puts the EM sector"},
        {"name": "flavour_split_sits_at_CAL3_h_order",
         "passed": bool(mp.fabs(ords["delta"] - 3) < mp.mpf("1e-3")
                        and mp.fabs(p_t - 1) < mp.mpf("1e-3")),
         "detail": f"delta = flavor_split_leading(q) vanishes to order "
                   f"{mp.nstr(ords['delta'], 8)} in (q-1) — h^3, the order the math-ideal "
                   f"CAL ladder assigns to CAL-3 (D_pi, the pion decay width). tanh(ln q) "
                   f"is O(h), so 1 - |r_pn| is O(h^4) while r_pp and r_nn are O(h^0). "
                   f"The canonical triple is (m_e, D_beta, D_pi) at h^0/h^2/h^3, so two "
                   f"of the three calibration points are decay rates by definition"},
    ]
    ok = all(v["passed"] for v in a)
    print("\n  assertions:")
    for v in a:
        print(f"    [{'PASS' if v['passed'] else 'FAIL'}] {v['name']}")
        print(f"           {v['detail']}")
    print(f"\n  allPassed: {ok}  ({sum(1 for v in a if v['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-bond-decay-rates-from-transfer-spectrum",
        "engine": "sympy + mpmath",
        "description": (
            "qou-cds1 Step 28. Step 27 stopped because an all-pairs coupling needs a "
            "falloff rate per bond type and three fitted rates would be three free "
            "parameters. They are not free. The math-ideal CAL triple is "
            "(m_e, D_beta, D_pi) at orders h^0/h^2/h^3 — CAL-2 and CAL-3 are the neutron "
            "beta-decay and pion decay WIDTHS, i.e. two of the three calibration points "
            "are decay rates by definition. And `chi_monotone_transfer._alpha_beta` "
            "reduces each fine-Bratteli transfer step to O_g = alpha.sigma_g + beta.I "
            "with spectrum E_1 = Prod(q+d_j), E_2 = Prod(-1/q+d_j), so the falloff across "
            "one bond is the spectral ratio E_2/E_1. In closed form: -1/q^2 for p-p, "
            "-q^2 for n-n, EXACTLY -1 for the averaged p-n. THEY ARE NOT INDEPENDENT: "
            "r_pp.r_nn = 1 = r_pn^2 and r_nn/r_pp = q^4, so three rates carry one degree "
            "of freedom. AND THEY ARE SECTOR-INDEXED: under the bar involution p-p and "
            "n-n exchange while p-n is fixed; their product is bar-even (the taxonomy's "
            "STRONG cosh channel) and their ratio bar-odd (its WEAK sinh channel). The "
            "colour-weighted p-n bond's departure from -1 is tanh(ln q).delta + "
            "O(delta^2), and tanh(ln q_0) = 0.103963710 is exactly the odd-to-even ratio "
            "`interaction-sector-taxonomy.md` derives for the ELECTROMAGNETIC coupling — "
            "the cell it proves admits no pure parity. Predicted 1.4302400e-4 against "
            "measured 1.4301377e-4, agreeing to 7.2e-5 relative. delta vanishes to order "
            "h^3, CAL-3's order. What this does NOT do: supply the coupling word — a "
            "non-adjacent nucleon pair still has no single generator to sit on."),
        "contentBlock": "prop:three-calibration-inputs",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 40,
                       "cal_triple": "math ideal (m_e, D_beta, D_pi) at h^0/h^2/h^3",
                       "transfer": "chi_monotone_transfer._alpha_beta (fine-Bratteli)"},
        "data": {
            "q0": mp.nstr(Q0, 20), "h0": mp.nstr(H0, 18),
            "rate_pp": str(sp.factor(r_pp)), "rate_nn": str(sp.factor(r_nn)),
            "rate_pn": str(r_pn),
            "product_pp_nn": str(prod), "ratio_nn_pp": str(ratio),
            "bar_pp": str(bar_pp), "bar_nn": str(bar_nn), "bar_pn": str(bar_pn),
            "pn_departure_exact": str(dep),
            "pn_departure_leading_coeff": str(lead),
            "tanh_ln_q_closed_form": str(tanh_closed),
            "tanh_ln_q0": mp.nstr(tanh0, 20),
            "flavour_split": {k: {"delta": mp.nstr(v[0], 18),
                                  "rate_abs": mp.nstr(v[1], 20),
                                  "departure_measured": mp.nstr(1 - v[1], 18),
                                  "departure_predicted": mp.nstr(v[2], 18),
                                  "relative_difference": mp.nstr(v[3], 8)}
                              for k, v in dep_rows.items()},
            "order_delta_in_q_minus_1": mp.nstr(ords["delta"], 10),
            "order_tanh_in_q_minus_1": mp.nstr(p_t, 10),
        },
        "context": {
            "axis": "qou-cds1: are the all-pairs bond decay rates free parameters, or "
                    "are they already determined by the CAL definitions and the tower's "
                    "transfer matrix?",
            "answer": (
                "Determined. The rate across a bond is the transfer step's spectral ratio "
                "E_2/E_1, a closed form in q for every bond template; the three rates "
                "satisfy r_pp.r_nn = r_pn^2 so they carry one degree of freedom rather "
                "than three; and their bar parity reproduces the interaction-sector "
                "taxonomy, with the p-n departure carrying tanh(ln q_0), the taxonomy's "
                "own electromagnetic odd-to-even ratio. The three-free-parameter "
                "objection that stopped Step 27 is removed."),
            "does_not_close": (
                "The coupling WORD. A non-adjacent nucleon pair has no single generator "
                "to sit on, so building the all-pairs braid remains a construction."),
            "scope": "Scope-(a). Nothing wired, proposed or readmitted.",
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t_start) * 1000),
    }
    out_p = HERE / "qbeta-bond-decay-rates-from-transfer-spectrum.witness.json"
    with open(out_p, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="sympy+mpmath",
            q0_anchor="proton (experimental pin)", q0_value=mp.nstr(Q0, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
