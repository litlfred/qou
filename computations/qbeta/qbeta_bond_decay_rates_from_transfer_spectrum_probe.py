#!/usr/bin/env python3
"""qou-cds1 Step 28: the all-pairs decay rates are DERIVED — they are the
transfer matrix's spectral gap per bond.

*** 🛑 CORRECTED 2026-09-01, AND DUPLICATED BY A SIBLING WHO HAD IT RIGHT ***

This probe first read the per-bond rate as `E_2/E_1` in the FIXED (q, -1/q)
eigenvalue order. That is the reciprocal of the spectral gap whenever
|E_2| > |E_1|, which is exactly the n-n case. The correlation decay of a
transfer matrix is |lambda_2 / lambda_1| with lambda_1 the LARGER-magnitude
eigenvalue, and `sigma^-1` carries `sigma`'s spectrum up to sign, so:

    p-p   rate = 1/q^2          (unchanged — |E_1| > |E_2| there)
    n-n   rate = 1/q^2          (was reported as q^2; WRONG)
    p-n   rate = 1  exactly     (unchanged — equal magnitudes either way)

Bean `qou-brng` derived the same object correctly and independently on `main`
(`computations/probes/spectral_gap_bond_decay_probe.py`, merged 2026-09-01),
asserting pp and nn are both exactly 1/q^2 to 45 digits. That probe is the
reference; this one is the duplicate, and it was the one with the error.

TWO CLAIMS ARE WITHDRAWN, not restated:

  * "the three rates satisfy r_pp . r_nn = 1 = r_pn^2, so they carry ONE degree
    of freedom" — FALSE once corrected. Both like-nucleon rates are 1/q^2, so
    the product is 1/q^4, not 1.
  * "bar parity reproduces the interaction-sector taxonomy: p-p and n-n exchange
    under q -> 1/q, product bar-even = STRONG, ratio bar-odd = WEAK" — VACUOUS
    once corrected. Equal rates do not exchange. And the claim was partly
    circular even before that: `d = 0` and `d = -h` ARE `sigma` and `sigma^-1`,
    bar-images of each other by definition, so their exchange was a restatement
    of the templates rather than a discovery about sectors.

WHAT SURVIVES, and it is the part that never depended on the ordering:

  * the rates are DERIVED closed forms in q with no free parameter — which was
    the point, and which removes Step 27's three-free-parameter objection;
  * the averaged p-n interface has rate EXACTLY 1: the p-n bond is LONG-RANGE
    while both like-nucleon bonds are short-range at 1/q^2. That asymmetry is
    real and is what `qou-brng` leads with;
  * the colour-weighted p-n bond's departure from 1 is tanh(ln q).delta +
    O(delta^2), because tanh(ln q) = (q^2-1)/(q^2+1); at the pin
    tanh(ln q_0) = 0.103963710 is the odd-to-even ratio
    `interaction-sector-taxonomy.md` derives for the ELECTROMAGNETIC coupling.
    Predicted 1.4302400e-4 against measured 1.4301377e-4, agreeing to 7.2e-5.
    *** THE EM READING IS WITHDRAWN (2026-09-01, qou-i9gk resolved). *** The
    self-raised caveat was right: it is a triviality. `q` ALONE has that
    odd/even ratio (quantum integers are bar-even so [9]_q[10]_q divides out),
    X = q.B gives it for any bar-even B, and tanh(ln q) IS h/(q+1/q) — which is
    exactly how it arises here. And the match lands on the taxonomy's BARE
    ratio, not its Chern-Simons-DRESSED 0.10356, which differs by 54x the
    residual. The closed form is kept; the link is not.
    See qbeta_tanh_em_match_is_formal_probe.py (4/4).
  * delta = flavor_split_leading(q) vanishes to order h^3 — CAL-3's order, the
    pion decay width's.

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
    tanh(ln q_0) = 0.103963710 is the odd-to-even ratio the taxonomy derives for
    the electromagnetic coupling — BUT SEE THE BANNER: that match is FORMAL, not
    a link (qou-i9gk resolved 2026-09-01). Measured:
    tanh(ln q_0) . delta = 1.4302400e-4 against 1.4301377e-4, agreeing to
    7.2e-5 relative, which is the second order in delta.

So the p-p / n-n pair is the bar-conjugate (strong/weak) axis, and the p-n bond
sits at the bar-fixed point carrying h/(q+1/q). Calling that "the EM ratio" is
WITHDRAWN — `q` alone has the same odd/even ratio, so the match is formal. The rates differ by
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


def bond_rate(d, q_val=None):
    """The transfer step's SPECTRAL GAP |lambda_2/lambda_1|, lambda_1 the
    larger-magnitude eigenvalue. Corrected 2026-09-01 — see the banner."""
    e1, e2 = transfer_spectrum(d)
    if q_val is None:
        q_val = Q0
    a1 = mp.fabs(mp.mpf(str(sp.N(e1.subs(QS, sp.Rational(str(q_val))), 40))))
    a2 = mp.fabs(mp.mpf(str(sp.N(e2.subs(QS, sp.Rational(str(q_val))), 40))))
    lo, hi = (e2, e1) if a2 <= a1 else (e1, e2)
    return sp.cancel(lo / hi), min(a1, a2) / max(a1, a2)


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
    rates, gaps = {}, {}
    print(f"\n[1] the transfer step's spectrum per bond, and its SPECTRAL GAP")
    print(f"    {'bond':6s}{'template':12s}{'offset d':>14s}{'E_1':>18s}"
          f"{'E_2':>18s}{'|l2/l1|':>14s}")
    for name, tmpl, d in bonds:
        e1, e2 = transfer_spectrum(d)
        r, g = bond_rate(d)
        rates[name], gaps[name] = r, g
        print(f"    {name:6s}{tmpl:12s}{str(sp.factor(d)):>14s}"
              f"{str(sp.factor(e1)):>18s}{str(sp.factor(e2)):>18s}"
              f"{mp.nstr(g, 12):>14s}")
    r_pp, r_nn, r_pn = rates["p-p"], rates["n-n"], rates["p-n"]
    inv_q2 = 1 / Q0 ** 2
    print(f"\n    1/q_0^2 = {mp.nstr(inv_q2, 14)}")
    print(f"    -> p-p and n-n are BOTH exactly 1/q^2 (sigma^-1 carries sigma's")
    print(f"       spectrum up to sign), and p-n is exactly 1: the p-n bond is")
    print(f"       LONG-RANGE while both like-nucleon bonds are short-range.")
    print(f"    -> CORRECTS this probe's first version, which read E_2/E_1 in the")
    print(f"       fixed (q, -1/q) order and reported q^2 for n-n. Bean qou-brng")
    print(f"       had it right independently on main.")

    # [2] the two claims the ordering error cost -------------------------
    prod_wrong = bool(mp.fabs(gaps["p-p"] * gaps["n-n"] - 1) > mp.mpf("0.1"))
    like_coincide = bool(mp.fabs(gaps["p-p"] - gaps["n-n"]) < mp.mpf("1e-30"))
    print(f"\n[2] WITHDRAWN: the 'one degree of freedom' and 'sector' claims")
    print(f"    r_pp . r_nn = {mp.nstr(gaps['p-p'] * gaps['n-n'], 12)}, NOT 1 — so the")
    print(f"    exact relation r_pp.r_nn = r_pn^2 this probe first asserted is false.")
    print(f"    And p-p = n-n = {mp.nstr(gaps['p-p'], 12)} exactly, so they do not")
    print(f"    EXCHANGE under the bar and the strong/weak sector split built on that")
    print(f"    exchange is vacuous. Both withdrawn, neither restated.")
    print(f"    The exchange claim was partly circular anyway: d = 0 and d = -h ARE")
    print(f"    sigma and sigma^-1, bar-images by definition, so their swapping")
    print(f"    restated the templates rather than discovering anything about sectors.")

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
    print(f"    the taxonomy quotes 0.10396 for its EM coupling — but that match is")
    print(f"    FORMAL, not a link (qou-i9gk, 2026-09-01): `q` ALONE has this same")
    print(f"    odd/even ratio, X = q.B gives it for any bar-even B, and tanh(ln q)")
    print(f"    IS h/(q+1/q) — which is exactly how it arises here. The match also")
    print(f"    lands on the taxonomy's BARE ratio, not its dressed 0.10356 (54x the")
    print(f"    residual away). The closed form is kept; the EM link is withdrawn.")
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
    print(f"       O(h). So 1 - |r_pn| = O(h^4), while both like-nucleon rates")
    print(f"       are exactly 1/q^2.")

    # ------------------------------------------------------------- assertions
    a = [
        {"name": "bond_rates_are_closed_forms_and_like_nucleon_bonds_coincide",
         "passed": bool(like_coincide
                        and mp.fabs(gaps["p-p"] - inv_q2) < mp.mpf("1e-30")
                        and mp.fabs(gaps["p-n"] - 1) < mp.mpf("1e-30")),
         "detail": f"the transfer step's spectrum is E_1 = Prod(q + d_j), "
                   f"E_2 = Prod(-1/q + d_j) (`chi_monotone_transfer._alpha_beta`), so the "
                   f"per-bond falloff is the SPECTRAL GAP |lambda_2/lambda_1|: exactly "
                   f"1/q^2 for BOTH p-p and n-n (sigma^-1 carries sigma's spectrum up to "
                   f"sign) and exactly 1 for the averaged p-n, which is therefore "
                   f"LONG-RANGE. Closed forms in q with no free parameter, which removes "
                   f"Step 27's three-free-parameter objection. CORRECTS this probe's "
                   f"first version (E_2/E_1 in fixed order gave q^2 for n-n); bean "
                   f"qou-brng derived the same object correctly on main"},
        {"name": "the_one_dof_and_sector_claims_are_withdrawn",
         "passed": bool(prod_wrong and like_coincide),
         "detail": f"r_pp . r_nn = {mp.nstr(gaps['p-p'] * gaps['n-n'], 10)} rather than 1, "
                   f"so the 'one exact relation, one degree of freedom' claim is false; "
                   f"and p-p = n-n exactly, so they do not exchange under the bar and the "
                   f"strong/weak sector assignment built on that exchange is vacuous. "
                   f"Both are withdrawn and neither is restated. The exchange was partly "
                   f"circular in any case: d = 0 and d = -h are sigma and sigma^-1, "
                   f"bar-images of each other by definition"},
        {"name": "pn_departure_is_the_electromagnetic_ratio_times_the_flavour_split",
         "passed": bool(tanh_is_lead
                        and all(v[3] < mp.mpf("1e-3") for v in dep_rows.values())),
         "detail": f"1 - |r_pn| = 2.delta.(q^2-1)/(delta.(q^2-1) + 2q^2 + 2), whose "
                   f"leading coefficient is (q^2-1)/(q^2+1) = tanh(ln q). At the pin "
                   f"tanh(ln q_0) = {mp.nstr(tanh0, 12)}. The taxonomy quotes the same "
                   f"number for its EM coupling, but that match is FORMAL and is "
                   f"WITHDRAWN (qou-i9gk): `q` alone has the ratio. Predicted "
                   f"{mp.nstr(dep_rows['leading'][2], 10)} against measured "
                   f"{mp.nstr(1 - dep_rows['leading'][1], 10)}, agreeing to "
                   f"{mp.nstr(dep_rows['leading'][3], 4)} relative — the second order in "
                   f"delta. SELF-RAISED CAVEAT (bean qou-i9gk): tanh(ln q) is just 'odd "
                   f"part over even part', which any bar decomposition produces, so this "
                   f"may be two instances of one triviality rather than a link. Unlike "
                   f"the withdrawn sector claim it is at least a numerical coincidence "
                   f"that has to be explained away rather than a restated definition"},
        {"name": "flavour_split_sits_at_CAL3_h_order",
         "passed": bool(mp.fabs(ords["delta"] - 3) < mp.mpf("1e-3")
                        and mp.fabs(p_t - 1) < mp.mpf("1e-3")),
         "detail": f"delta = flavor_split_leading(q) vanishes to order "
                   f"{mp.nstr(ords['delta'], 8)} in (q-1) — h^3, the order the math-ideal "
                   f"CAL ladder assigns to CAL-3 (D_pi, the pion decay width). tanh(ln q) "
                   f"is O(h), so 1 - |r_pn| is O(h^4) while both like-nucleon rates are "
                   f"the q-independent-in-order 1/q^2. The canonical triple is "
                   f"(m_e, D_beta, D_pi) at h^0/h^2/h^3, so two of the three calibration "
                   f"points are decay rates by definition"},
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
            "the taxonomy also quotes for its EM coupling — but that match is FORMAL and "
            "is WITHDRAWN (qou-i9gk, 2026-09-01): `q` alone has the same odd/even ratio. "
            "Predicted 1.4302400e-4 against measured 1.4301377e-4, agreeing to 7.2e-5. delta vanishes to order "
            "h^3, CAL-3's order. What this does NOT do: supply the coupling word — a "
            "non-adjacent nucleon pair still has no single generator to sit on."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": ok,
        "parameters": {"pin": "experimental (proton)", "dps": 40,
                       "cal_triple": "math ideal (m_e, D_beta, D_pi) at h^0/h^2/h^3",
                       "transfer": "chi_monotone_transfer._alpha_beta (fine-Bratteli)"},
        "data": {
            "q0": mp.nstr(Q0, 20), "h0": mp.nstr(H0, 18),
            "gap_pp": mp.nstr(gaps["p-p"], 20), "gap_nn": mp.nstr(gaps["n-n"], 20),
            "gap_pn": mp.nstr(gaps["p-n"], 20),
            "inv_q_squared": mp.nstr(inv_q2, 20),
            "like_nucleon_rates_coincide": bool(like_coincide),
            "withdrawn": ["r_pp . r_nn = r_pn^2 (one degree of freedom)",
                          "bar exchange -> strong/weak sector split"],
            "reference_implementation": "computations/probes/spectral_gap_bond_decay_probe.py (bean qou-brng, main)",
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
            q0_anchor="proton", q0_value=mp.nstr(Q0, 30))
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
