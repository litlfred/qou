#!/usr/bin/env python3
"""Class B of the #7181 escape enumeration: what happens when the bond energies
are allowed to be negative.

Numerical companion to `QOU/Hecke/BondCutSymmetryNoSignDefinite.lean` (generic)
and `QOU/Hecke/BondCutSymmetryNoSignDefiniteLogBound.lean` (the `-ln b` letters),
bean `qou-brng`. #7165 excludes **positive** pair-additive bond counts from
supplying the SEMF symmetry energy; class B drops `bondSum_nonneg`'s
`0 <= e_pp, e_pn, e_nn`, i.e. admits a bond factor `b_t > 1` -- a *repulsive*
bond, which is what unbinds neutron matter.

*** NO FITTING ***

Dropping a sign restriction hands you three free reals `(e_pp, e_pn, e_nn)`;
choosing them so the symmetry coefficient reaches `a_A ~ 23.7 MeV` is a
three-parameter fit and is forbidden (AGENTS.md 'NO FITTING, EXCEPT CAL-1/2/3').
So the energies here are **derived**, never chosen: every bond factor is the
two-strand convention-D Markov trace `tr(a.sigma + b) = a.z_D + b` of the
canonical interface letter, `z_D = q^3/(q^2+1)`, with the letters exactly as
`atom_braid_word_3A` emits them (`pp = sigma`, `nn = sigma - h`,
`pn = sigma - h(1/2 - delta_f/4)`, `h = q - 1/q`, `delta_f =
(q-1)^2 (1 - q^-4)/3` = `_li_2_q_util.flavor_split_leading`). Every SEMF number
is a TARGET, checked against, never searched on. The multiplicity scan R9 reports
the WHOLE table and selects no `m`; selecting one for its residual would be the
'sweeping a discrete parameter' fit the directive names.

*** WHAT IS MEASURED ***

R1  The canonical bond factors ARE convention D: `b_pp = z_D` exactly, and all
    three carry `(q^2+1)` in the denominator -- the AGENTS.md convention test
    that keys on the ANSWER rather than on how `z` was spelled. Checked exactly
    over `Fraction` at a rational sample `q`, not numerically.
R2  The three closed forms agree with the corpus's recorded `b_pp = q^2/[2]_q`,
    `b_nn = q^-2/[2]_q` and the `b_pn` polynomial of
    `qbeta_bond_cut_symmetry_shape_probe`.
R3  **At the canonical multiplicity `m = 1` all three derived energies are
    POSITIVE** (`b < 1`): the corpus's own law is NOT in class B. Class B is a
    hypothesis about a construction the corpus does not have.
R4  `delta = e_pn - (e_pp+e_nn)/2` with its sign and magnitude, against the
    shape probe's recorded value.
R5  `delta <= 2 ln q_0` -- invariant (1) of #7165, which needs `0 < b_nn <= b_pp`
    and NEVER `b <= 1`. Positivity was not the binding constraint.
R6  The class-B rescaling: `c = 1/b_pp + 1/b_pn + 1/b_nn` drives ALL THREE
    energies negative, and `delta` is unchanged to the full working precision.
    Numerical companion to `exists_bondRescale_all_energies_neg`.
R7  The price of the escape (`enn_neg_of_semf_neutronMatter`): reproducing the
    SEMF at pure neutron matter FORCES `b_nn > 1`. Measured against the derived
    `b_nn`.
R8  The interface a law would need to beat the cap, and how far below the convex
    hull of `b_pp`, `b_nn` it sits (`interface_below_of_gt_two_log`).
R9  The multiplicity family `m = 1..12` -- the only mechanism in the corpus that
    produces `b > 1` (bean `qou-ib3g`, and REFUTED there on independent grounds).
    Reproduces that bean's `m = 3` figures and its `m = 2` class-B claim, and
    reports whether ANY `m` supplies the SEMF magnitude. NOTE the bean's
    "factors 0.335 / 0.984 / 1.709" are ENERGY RATIOS `L(m)/L(1)`, not bond
    factors: as bond factors `b(3) = 0.8485 / 0.5139 / 0.2122`. Its `m = 2`
    `b > 1` claim IS about `b`. Both are reproduced, each against the quantity
    it actually names.

Precision: mpmath at 50 dps end to end plus exact `Fraction` for R1; `q_0` from
the substrate's 50-digit string (PROTON pin, owner directive 2026-08-07), `m_e`
from the NIST table string. No float64 arithmetic anywhere.
`E_0 = m_e/(q(q-1))/(1 - hbar_q^2)` per `2026-09-05-binding-law-arc-synthesis`,
matching `qbeta_bond_cut_symmetry_shape_probe`; the sibling multiplicity probe
omits the `1/(1 - hbar_q^2)`, a 0.99 % difference that changes no verdict here
and is reported as `E0_convention_spread_pct`.

Run:  PYTHONPATH=computations python3 -u \\
        computations/qbeta/qbeta_class_b_nonsigndefinite_bond_probe.py \\
        2>&1 | tee /tmp/classb-bond.log
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
from qou_substrate import constants as _c  # noqa: E402

DPS = 50
mp.mp.dps = DPS

Q0 = mp.mpf(_c.Q_50_DIGIT_STR)
M_E = mp.mpf(str(_c._E_MEV.value))
TWO_Q = Q0 + 1/Q0
HBAR = (Q0 - 1)/Q0
H = Q0 - 1/Q0
E0 = M_E/(Q0*(Q0 - 1))/(1 - HBAR**2)
Z_D = Q0**3/(Q0**2 + 1)                       # convention D Markov parameter
DELTA_F = (Q0 - 1)**2 * (1 - Q0**-4)/3        # _li_2_q_util.flavor_split_leading

#: the three canonical interface letters `(c, d)` meaning `c.sigma + d`,
#: exactly as `atom_braid_word_3A` emits them.
LETTERS = {
    "pp": (mp.mpf(1), mp.mpf(0)),
    "pn": (mp.mpf(1), -H*(mp.mpf(1)/2 - DELTA_F/4)),
    "nn": (mp.mpf(1), -H),
}

#: SEMF targets (Rohlf 1994 / Krane 1988). TARGETS ONLY -- never searched on.
A_V_TARGET = mp.mpf("15.75")
A_A_TARGET = mp.mpf("23.7")

#: the recorded `b_pn` closed form of `qbeta_bond_cut_symmetry_shape_probe`.
B_PN_RECORDED = ((Q0**10 - 2*Q0**9 + 7*Q0**8 - 2*Q0**6 + 4*Q0**5 + 4*Q0**4
                  + Q0**2 - 2*Q0 + 1)/(12*Q0**5*(Q0**2 + 1)))

TOL = mp.mpf(10)**(-40)
MAX_M = 12
K_DEGREES = (2, 12)                           # chain and close-packed


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return "unknown"


def letter_pow_trace(c, d, m: int, h, z):
    """`tr_2((c.sigma + d)^m)` reduced by `sigma^2 = h.sigma + 1`.

    The two-strand trace is affine in the offset, `tr(a.sigma + b) = a.z + b`.
    Works over `mpf` and over `Fraction` alike -- arithmetic only, no floats.
    """
    a, b = 0*h, 1 + 0*h                       # identity = 0.sigma + 1
    for _ in range(m):
        a, b = a*c*h + a*d + b*c, a*c + b*d
    return a*z + b


def bond_factors(m: int = 1):
    return {k: letter_pow_trace(c, d, m, H, Z_D) for k, (c, d) in LETTERS.items()}


def energy_slope(bpp, bpn, bnn):
    """`delta = e_pn - (e_pp + e_nn)/2` with `e = -ln b`."""
    return -mp.log(bpn) + (mp.log(bpp) + mp.log(bnn))/2


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    print("=" * 78)
    print("CLASS B -- non-sign-definite bond energies (bean qou-brng, PR #7181 row B)")
    print("=" * 78)
    print(f"q_0 = {mp.nstr(Q0, 25)}  (PROTON pin)   E_0 = {mp.nstr(E0, 12)} MeV")
    print(f"z_D = q^3/(q^2+1) = {mp.nstr(Z_D, 18)}   h = {mp.nstr(H, 12)}")

    b = bond_factors(1)
    e = {k: -mp.log(v) for k, v in b.items()}
    delta = energy_slope(b["pp"], b["pn"], b["nn"])
    cap = 2*mp.log(Q0)

    # ---------------------------------------------------------------- R1
    print("\n-- R1  the canonical letters ARE convention D ------------------")
    print(f"   b_pp  = {mp.nstr(b['pp'], 18)}")
    print(f"   b_pn  = {mp.nstr(b['pn'], 18)}")
    print(f"   b_nn  = {mp.nstr(b['nn'], 18)}")
    ok &= chk("R1a_b_pp_is_the_convention_D_markov_parameter",
              abs(b["pp"] - Z_D) < TOL, True,
              "tr(sigma) = z_D = q^3/(q^2+1); convention C would give "
              "sqrt(q)/(q+1) = 0.4993")

    # The convention test that keys on the ANSWER, not on how `z` was spelled
    # (AGENTS.md): `(q^2+1)` must divide each denominator. Exact, over Fraction,
    # at a rational sample q -- 13 = numerator of (q^2+1) at q = 3/2.
    qf = F(3, 2)
    hf = qf - 1/qf
    zf = qf**3/(qf**2 + 1)
    df = (qf - 1)**2 * (1 - qf**-4)/3
    lf = {"pp": (F(1), F(0)), "pn": (F(1), -hf*(F(1, 2) - df/4)), "nn": (F(1), -hf)}
    marker = (qf**2 + 1).numerator                      # 13
    divides = {k: letter_pow_trace(c, d, 1, hf, zf).denominator % marker == 0
               for k, (c, d) in lf.items()}
    ok &= chk("R1b_q2_plus_1_divides_every_denominator",
              all(divides.values()), True,
              f"exact over Fraction at q = {qf}; marker {marker}; {divides}")

    # ---------------------------------------------------------------- R2
    print("\n-- R2  agreement with the recorded corpus closed forms ---------")
    ok &= chk("R2a_b_pp_eq_q2_over_two_q",
              abs(b["pp"] - Q0**2/TWO_Q) < TOL, True)
    ok &= chk("R2b_b_nn_eq_q_minus2_over_two_q",
              abs(b["nn"] - Q0**-2/TWO_Q) < TOL, True)
    ok &= chk("R2c_b_pn_eq_shape_probe_polynomial",
              abs(b["pn"] - B_PN_RECORDED) < TOL, True,
              "the recorded degree-10 closed form of "
              "qbeta_bond_cut_symmetry_shape_probe")

    # ---------------------------------------------------------------- R3
    print("\n-- R3  the DERIVED signs at the canonical m = 1 ----------------")
    for k in ("pp", "pn", "nn"):
        print(f"   e_{k} = -ln b_{k} = {mp.nstr(e[k], 15)}"
              f"   ({'REPULSIVE, class B' if e[k] < 0 else 'attractive'})")
    ok &= chk("R3a_all_three_derived_energies_are_positive",
              all(e[k] > 0 for k in e), True,
              "every b < 1, so the corpus's own construction is NOT in class B; "
              "class B is a hypothesis about a law the corpus does not have")
    ok &= chk("R3b_no_derived_bond_factor_exceeds_one",
              max(b.values()) < 1, True,
              f"max b = {mp.nstr(max(b.values()), 15)}")

    # ---------------------------------------------------------------- R4
    print("\n-- R4  the p-n slope ------------------------------------------")
    print(f"   delta = {mp.nstr(delta, 15)}")
    ok &= chk("R4a_delta_is_negative_wrong_SEMF_sign", delta < 0, True,
              "symmetryCoeff_pos_iff: the SEMF sign needs delta > 0")
    ok &= chk("R4b_delta_matches_shape_probe_record",
              abs(delta - mp.mpf("-0.02176")) < mp.mpf("5e-5"), True,
              f"recorded -0.0218; measured {mp.nstr(delta, 12)}")

    # ---------------------------------------------------------------- R5
    print("\n-- R5  invariant (1) does not use positivity -------------------")
    print(f"   cap 2 ln q_0 = {mp.nstr(cap, 15)}")
    ok &= chk("R5a_delta_within_two_log_q_cap", delta <= cap, True)
    aA_cap = {k: E0*cap*mp.mpf(k)/4 for k in K_DEGREES}
    for k in K_DEGREES:
        print(f"   a_A^eff cap at k = {k:2d}: {mp.nstr(aA_cap[k], 10)} MeV"
              f"   ({mp.nstr(A_A_TARGET/aA_cap[k], 8)}x short of {A_A_TARGET})")
    ok &= chk("R5b_cap_is_short_of_the_SEMF_target_at_every_degree",
              all(aA_cap[k] < A_A_TARGET for k in K_DEGREES), True,
              "E_0.delta.k/4 with delta at its convex maximum 2 ln q")
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    e0_alt = _qbeta_e0.order_zero_scaled(M_E, Q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    spread = 100*(E0 - e0_alt)/E0

    # ---------------------------------------------------------------- R6
    print("\n-- R6  class B by uniform rescaling: delta is INVARIANT --------")
    c_scale = 1/b["pp"] + 1/b["pn"] + 1/b["nn"]
    br = {k: c_scale*v for k, v in b.items()}
    er = {k: -mp.log(v) for k, v in br.items()}
    delta_r = energy_slope(br["pp"], br["pn"], br["nn"])
    print(f"   c = {mp.nstr(c_scale, 12)}   ->  "
          f"b' = ({mp.nstr(br['pp'], 8)}, {mp.nstr(br['pn'], 8)}, "
          f"{mp.nstr(br['nn'], 8)})")
    ok &= chk("R6a_rescaling_reaches_class_B_all_three_energies_negative",
              all(er[k] < 0 for k in er), True,
              "every rescaled b > 1; bondSum_nonneg fully escaped")
    ok &= chk("R6b_delta_unchanged_by_the_rescaling",
              abs(delta_r - delta) < TOL, True,
              f"|delta' - delta| = {mp.nstr(abs(delta_r - delta), 6)}; "
              "energySlope_bondRescale, an identity not an estimate")

    # ---------------------------------------------------------------- R7
    print("\n-- R7  the price of the escape: neutron matter needs b_nn > 1 --")
    print(f"   required: b_nn > 1        derived: b_nn = {mp.nstr(b['nn'], 15)}")
    ok &= chk("R7a_derived_b_nn_fails_the_neutron_matter_condition",
              b["nn"] < 1, True,
              f"short by a factor {mp.nstr(1/b['nn'], 10)}; "
              "enn_neg_of_semf_neutronMatter forces e_nn < 0 i.e. b_nn > 1")
    ok &= chk("R7b_SEMF_unbinds_neutron_matter", A_V_TARGET < A_A_TARGET, True,
              "the hypothesis a_V < a_A of semf_neutronMatter_neg, AME2020")

    # ---------------------------------------------------------------- R8
    print("\n-- R8  the interface a law would need, vs the convex hull ------")
    k_max = max(K_DEGREES)
    delta_req = 4*A_A_TARGET/(E0*mp.mpf(k_max))
    b_pn_req = mp.e**(-(delta_req - (mp.log(b["pp"]) + mp.log(b["nn"]))/2))
    print(f"   delta required at k = {k_max}: {mp.nstr(delta_req, 12)}"
          f"   (cap {mp.nstr(cap, 12)})")
    print(f"   b_pn required: {mp.nstr(b_pn_req, 12)}"
          f"   vs b_nn = {mp.nstr(b['nn'], 12)}")
    ok &= chk("R8a_required_slope_exceeds_the_convex_cap", delta_req > cap, True)
    ok &= chk("R8b_required_interface_is_below_the_convex_hull",
              b_pn_req < b["nn"], True,
              f"{mp.nstr(b['nn']/b_pn_req, 10)}x below the smaller like-species "
              "bond; interface_below_of_gt_two_log")

    # ---------------------------------------------------------------- R9
    print("\n-- R9  the multiplicity family (the ONLY class-B mechanism here)")
    print("    m |     b_pp      b_pn      b_nn |    delta   a_A^eff(k=12) | classB")
    rows = []
    for m in range(1, MAX_M + 1):
        bm = bond_factors(m)
        if min(bm.values()) <= 0:
            rows.append({"m": m, "defined": False})
            print(f"   {m:2d} | a bond factor is non-positive -- log undefined")
            continue
        dm = energy_slope(bm["pp"], bm["pn"], bm["nn"])
        aA = E0*dm*mp.mpf(k_max)/4
        cb = [k for k in bm if bm[k] > 1]
        rows.append({"m": m, "defined": True,
                     "b": {k: mp.nstr(v, 12) for k, v in bm.items()},
                     "delta": mp.nstr(dm, 12), "aA_eff_k12_MeV": mp.nstr(aA, 10),
                     "class_b_letters": cb})
        print(f"   {m:2d} | {mp.nstr(bm['pp'], 6):>9} {mp.nstr(bm['pn'], 6):>9} "
              f"{mp.nstr(bm['nn'], 6):>9} | {mp.nstr(dm, 6):>9} "
              f"{mp.nstr(aA, 6):>13} | {','.join(cb) if cb else '-'}")
    live = [r for r in rows if r["defined"]]
    best = max(mp.mpf(r["aA_eff_k12_MeV"]) for r in live)
    ok &= chk("R9a_no_multiplicity_supplies_the_SEMF_magnitude",
              best < A_A_TARGET, True,
              f"best over m = 1..{MAX_M} at k = {k_max} is "
              f"{mp.nstr(best, 10)} MeV against the {A_A_TARGET} target; "
              "the WHOLE table is reported and no m is selected -- selecting "
              "one for its residual would be a fit")
    # qou-ib3g's "factors at m = 3: 0.335 / 0.984 / 1.709" are ENERGY RATIOS
    # `L(m)/L(1)` with `L = -ln b`, NOT bond factors -- the bean's question was
    # whether the multiplicity supplies the missing factor of 3 on the bond
    # ENERGY. Read as bond factors they are 0.8485 / 0.5139 / 0.2122 and the
    # comparison fails by 8x on the nn leg. Recording the distinction because
    # a quantity differing only by normalisation, mistaken for a discrepancy,
    # is the exact error class AGENTS.md flags on the c_3 3.47 %/3.35 % pair.
    b3 = bond_factors(3)
    l3 = {k: -mp.log(v)/e[k] for k, v in b3.items()}
    print(f"   m = 3 energy ratios L(3)/L(1): pp {mp.nstr(l3['pp'], 6)}  "
          f"pn {mp.nstr(l3['pn'], 6)}  nn {mp.nstr(l3['nn'], 6)}")
    ok &= chk("R9b_reproduces_qou_ib3g_m3_energy_ratios",
              all(abs(l3[k] - mp.mpf(v)) < mp.mpf("5e-4")
                  for k, v in (("pp", "0.335"), ("pn", "0.984"), ("nn", "1.709"))),
              True,
              f"bean qou-ib3g records 0.335 / 0.984 / 1.709 as L(3)/L(1), not "
              f"as b(3); measured {mp.nstr(l3['pp'], 6)} / "
              f"{mp.nstr(l3['pn'], 6)} / {mp.nstr(l3['nn'], 6)}. The bond "
              f"factors b(3) are {mp.nstr(b3['pp'], 6)} / "
              f"{mp.nstr(b3['pn'], 6)} / {mp.nstr(b3['nn'], 6)}.")
    b2 = bond_factors(2)
    ok &= chk("R9c_reproduces_qou_ib3g_m2_class_B_claim",
              b2["pp"] > 1 and b2["pn"] > 1, True,
              f"bean qou-ib3g: at m = 2 both pp and pn give b > 1; measured "
              f"{mp.nstr(b2['pp'], 8)} / {mp.nstr(b2['pn'], 8)} "
              f"(nn = {mp.nstr(b2['nn'], 8)}, still < 1)")

    elapsed = time.monotonic() - t0
    print("\n" + "=" * 78)
    n_pass = sum(1 for x in a if x["passed"])
    print(f"{n_pass}/{len(a)} assertions passed   ({elapsed:.2f} s)")
    print("VERDICT: the derived law is NOT in class B (R3); the uniform route "
          "into class B\n         changes delta by zero (R6); the convex cap "
          "holds without positivity (R5);\n         and the only mechanism that "
          "does produce b > 1 supplies no magnitude (R9).")

    out = {
        "probe": "qbeta_class_b_nonsigndefinite_bond_probe",
        "bean": "qou-brng",
        "lean": ["QOU.Hecke.BondCutSymmetryNoSignDefinite",
                 "QOU.Hecke.BondCutSymmetryNoSignDefiniteLogBound"],
        "q0_anchor": "physical_proton",
        "q0": mp.nstr(Q0, 30),
        "convention": "D (z = q^3/(q^2+1))",
        "dps": DPS,
        "commitSha": _head_sha(),
        "E0_MeV": mp.nstr(E0, 15),
        "E0_convention_spread_pct": mp.nstr(spread, 6),
        "bond_factors_m1": {k: mp.nstr(v, 20) for k, v in b.items()},
        "bond_energies_m1": {k: mp.nstr(v, 20) for k, v in e.items()},
        "delta": mp.nstr(delta, 20),
        "two_log_q_cap": mp.nstr(cap, 20),
        "aA_eff_cap_MeV": {str(k): mp.nstr(v, 12) for k, v in aA_cap.items()},
        "rescale_c": mp.nstr(c_scale, 20),
        "delta_after_rescale": mp.nstr(delta_r, 20),
        "b_pn_required_at_k12": mp.nstr(b_pn_req, 20),
        "multiplicity_scan": rows,
        "assertions": a,
        "passed": n_pass,
        "total": len(a),
        "elapsed_seconds": round(elapsed, 3),
    }
    print(json.dumps({"summary": {k: out[k] for k in
                                  ("passed", "total", "delta", "two_log_q_cap")}}))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
