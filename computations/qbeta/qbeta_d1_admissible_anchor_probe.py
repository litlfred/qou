#!/usr/bin/env python3
"""(D1) is anchored at an INADMISSIBLE functional — and has an admissible form.

qou-cds1 / qou-99qc / qou-bg3w.  Three questions the corpus has been treating
separately turn out to be one:

  * "excise convention C"                     -- z_C = sqrt(q)/(q+1)
  * "net is structurally excluded under D"    -- net, and tr_M at z = 1
  * "(D1) is short-model-specific"            -- 2*alpha = net(D) - tr^z(D)

ConventionDAdmissibleRoots.lean (sorry-free) proves the (1^3)-block weight
numerator factors over any commutative ring as

    N(q,z) = (q^2+1)z^2 - (2q^3+q)z + q^4 = (z - q)*((q^2+1)z - q^3),

so a functional descends to the two-row quotient iff z is a root, i.e. iff
z = q or z = z_D = q^3/(q^2+1).  EXACTLY TWO.  This probe checks what that
criterion says about z_C and about z = 1, and what (D1) becomes when it is
re-anchored on admissible parameters only.

SCOPING CORRECTION (2026-08-29).  An earlier revision of the bullet above
read "net = tr_M at z = 1", i.e. asserted the two are the same functional.
They are NOT, in general: tr_M(z=1) weights the standard basis
[1,1,1,1,1,h+1] while `net` is the plain coordinate sum [1,1,1,1,1,1], so

    tr_M(z=1) - net = h * (e_minus coordinate).

They agree on BOTH Delta models only because both carry a zero e_minus
coordinate.  Everything this probe measures is unaffected -- it works with
those elements -- but the identity must not be quoted as general.

The corpus holds a stronger, ELEMENT-INDEPENDENT exclusion of `net` that does
not route through z at all: `net` is the functional sigma -> 1, and
sigma^2 = h*sigma + 1 then forces 1 = h + 1, i.e. h = 0, so `net` is not an
algebra map -- while the augmentation sigma -> q is one, since q^2 = hq + 1
exactly when h = q - 1/q.  That is `qbeta_epsnpq_functional_mismatch_probe`,
which could not be RUN until PR #5943 fixed its import bootstrap.

SCOPE-(a).  No c_k is proposed, no element is adjudicated, nothing is wired.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/QBeta/ConventionDAdmissibleRoots.lean
-- Ref: [manuscript] .beans/qou-99qc (the admissible set is COMPLETE, solved not sampled)
-- Ref: [manuscript] computations/qbeta/qbeta_delta_element_fork_pricing_probe.py (PR #5897, tr_M(Delta_L))
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors", Invent. Math. 92 (1988) 349-383.
"""
from __future__ import annotations
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (os.path.join(_HERE, ".."), os.path.join(_HERE, "..", "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import sympy as sp                                        # noqa: E402
import mpmath as mp                                       # noqa: E402
from q_parameter import Q_50_DIGIT_STR                    # noqa: E402

mp.mp.dps = 60

q, z = sp.symbols("q z", positive=True)
h = q - 1 / q
zD = q ** 3 / (q ** 2 + 1)
zC = sp.sqrt(q) / (q + 1)
Q0 = sp.Rational(Q_50_DIGIT_STR)

#: the (1^3)-block Ocneanu weight numerator (cited input; the Lean file proves
#: the factorisation, the sympy probe of qou-99qc established the weight).
N = (q ** 2 + 1) * z ** 2 - (2 * q ** 3 + q) * z + q ** 4

#: tr_M of the SHORT element on the standard basis, from the Markov rule
#: tr(1)=1, tr(sigma_i)=z.  Delta_S = (h^2/2, -h/2, -h/2, 0,0,0).
TR_S = h ** 2 / 2 - h * z

#: tr_M of the LONG (11-crossing) element.  CITED from PR #5897's probe, and
#: calibrated below against the corpus's committed -15.451 % at z_D.
TR_L = -(q - 1) * (q + 1) * (
    q ** 4 * z ** 2 + 2 * q ** 3 * z + 2 * q ** 2 - 2 * q * z + z ** 2
) / (4 * q ** 3)

_A: list[tuple[str, bool]] = []


def check(name: str, ok: bool, note: str = "") -> None:
    _A.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {note}")


def num(e) -> mp.mpf:
    return mp.mpf(str(sp.N(sp.simplify(e).subs(q, Q0), 55)))


def main() -> int:
    print("=" * 74)
    print(" (D1)'s anchor, and the one criterion behind three questions")
    print("=" * 74)

    # ---- 1. the criterion, and what fails it --------------------------------
    check("admissible_roots_are_exactly_q_and_zD",
          sp.simplify(N - (z - q) * ((q ** 2 + 1) * z - q ** 3)) == 0
          and sp.simplify(N.subs(z, q)) == 0
          and sp.simplify(N.subs(z, zD)) == 0,
          "N factors as (z-q)((q^2+1)z-q^3); both roots verified")

    N_at_1 = sp.factor(sp.simplify(N.subs(z, 1)))
    check("z_equals_1_is_NOT_a_root",
          sp.simplify(N.subs(z, 1)) != 0
          and sp.simplify(N_at_1 - (q - 1) * (q ** 3 - q ** 2 - 1)) == 0,
          f"N(q,1) = {N_at_1}; nonzero for 1 < q < plastic")

    check("convention_C_is_NOT_a_root_either",
          sp.simplify(N.subs(z, zC)) != 0,
          f"N(q0,z_C) = {mp.nstr(num(N.subs(z, zC)), 10)} != 0 -- C fails the "
          "SAME criterion that excludes net; they are one fact, not two")

    # ---- 2. (D1) is anchored at z = 1 by construction ------------------------
    d1_S = sp.factor(sp.simplify(TR_S.subs(z, 1) - TR_S))
    d1_L = sp.factor(sp.simplify(TR_L.subs(z, 1) - TR_L))
    check("D1_reproduces_two_alpha_on_the_short_element",
          sp.simplify(d1_S - (z - 1) * h) == 0,
          "net(D_S) - tr^z(D_S) = h(z-1) = 2*alpha exactly, alpha=(z-1)h/2")
    check("D1_is_NOT_two_alpha_on_the_long_element",
          sp.simplify(d1_L - (z - 1) * h) != 0,
          "confirms #5897 independently")
    check("D1_carries_z_minus_1_as_a_factor_on_BOTH",
          sp.simplify(sp.rem(sp.Poly(sp.expand(d1_S), z), sp.Poly(z - 1, z))) == 0
          and sp.simplify(sp.rem(sp.Poly(sp.expand(d1_L), z),
                                 sp.Poly(z - 1, z))) == 0,
          "(D1) vanishes identically at z=1 on both elements -- it is ANCHORED "
          "at the inadmissible point by construction, not incidentally")

    # ---- 3. the admissible re-anchoring -------------------------------------
    gap_S = sp.simplify(sp.factor(TR_S.subs(z, q) - TR_S.subs(z, zD)))
    gap_L = sp.simplify(sp.factor(TR_L.subs(z, q) - TR_L.subs(z, zD)))
    check("short_admissible_gap_is_h_times_root_difference",
          sp.simplify(gap_S - h * (zD - q)) == 0
          and sp.simplify(gap_S - (1 - q ** 2) / (q ** 2 + 1)) == 0,
          "tr^q - tr^{z_D} = h(z_D - q) = (1-q^2)/(q^2+1): PARAMETER-FREE")
    alpha_adm = sp.simplify(gap_S / 2)
    check("alpha_admissible_has_a_closed_form",
          sp.simplify(alpha_adm + h * q / (2 * (q ** 2 + 1))) == 0,
          f"alpha_adm = -h*q/(2(q^2+1)) = {mp.nstr(num(alpha_adm), 16)}")
    check("long_admissible_gap_is_not_the_same_closed_form",
          sp.simplify(gap_L - gap_S) != 0,
          f"gap_L = {mp.nstr(num(gap_L), 16)} vs gap_S = "
          f"{mp.nstr(num(gap_S), 16)}")

    # ---- 4. calibration against committed corpus numbers --------------------
    me = mp.mpf("0.51099895069"); Qexp = mp.mpf("0.7823334093099085")
    qn = num(q); E0 = _qbeta_e0.order_zero_scaled(me, qn)
    errs = {}
    for nm, tr in (("S", TR_S), ("L", TR_L)):
        for zl, zv in (("1", sp.Integer(1)), ("q", q), ("zD", zD)):
            Qb = abs(num(tr.subs(z, zv))) * E0
            errs[f"{nm}@{zl}"] = (Qb - Qexp) / Qexp
    check("calibrates_against_qou_99qc_three_row_table",
          abs(errs["S@1"] - mp.mpf("0.00167757")) < mp.mpf("1e-5")
          and abs(errs["S@q"] - mp.mpf("0.12470")) < mp.mpf("1e-4")
          and abs(errs["S@zD"] + mp.mpf("0.43157")) < mp.mpf("1e-4"),
          "+0.168 / +12.470 / -43.157 %, all on the NF vector")
    check("calibrates_against_committed_d_frame_baseline",
          abs(errs["L@zD"] + mp.mpf("0.15451")) < mp.mpf("1e-4"),
          "-15.451 % on the exhibited words -- so TR_L is the right object")

    print("\n  Q_beta error by (element, functional):")
    for k, v in errs.items():
        print(f"    {k:<8} {mp.nstr(v * 100, 8):>14} %")
    print(f"\n  alpha, corpus form  (z-1)h/2   -- needs a z, none admissible")
    print(f"  alpha, admissible   h(z_D-q)/2 = {mp.nstr(num(alpha_adm), 20)}")

    ok = all(v for _, v in _A)
    print("\n" + "=" * 74)
    print(f"  {sum(v for _, v in _A)}/{len(_A)} checks passed")
    print("=" * 74)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
