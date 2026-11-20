#!/usr/bin/env python3
"""qbeta_delta_tr_vs_ruled_base_probe.py — the corpus's negative against the
Habiro route is aimed at a RETIRED functional. Re-aim it at the ruled base.

Bean `qou-pdix` (the S1 blocker: derive the Q_beta ladder eigenphase alpha),
parent `qou-cds1`. Scope (a): a statement about these exact objects at the
proton pin under convention D. It asserts nothing about alpha.

## Why this exists

`qou-pdix`'s route triage lists **attack A — Habiro ring / roots of unity** as
the "best structural fit", declining it only for circularity. Two things are
true of that decline and neither is what the corpus shows.

**First, it is not circular.** `prop:habiro-precision-ladder-equivalence`, the
block that would carry attack A's bridge, has a ONE-ELEMENT `uses[]` cone
(`thm:jones-markov-trace`). It is not downstream of `qou-cds1`.

**Second, the real obstacle is a measured negative, not a loop** — and that
negative has since been aimed at a retired target. The chain:

  * `QOU.BraidKnot.QbetaHabiroTaylorBridgeClass` equates two symbols that are
    BOTH `opaque ... := fun _ => 0` and have no defining properties, so it is a
    named hole rather than a hypothesis-carrying conditional. Established by
    `qbeta_habiro_bridge_class_is_not_a_lean_target_probe.py`, which verified
    the seal does not leak (six tactics, `lean`-direct) and concluded progress
    on it is COMPUTATIONAL, not deductive. That probe is not mine and this one
    does not re-do it.
  * The corpus then ran that computation, and it came back NEGATIVE:
    `qbeta-delta-tr-vs-formA.witness.json` (computedAt 2026-08-08) finds the
    Habiro `Delta tr_M` and Form A's net-winding slot structurally distinct --
    leading Taylor `-5/4 eps` against `-2 eps` -- and the sibling probe checked
    the inference is not a mere normalisation (the term-by-term ratio changes
    sign at k=2).

**The retirement.** That witness compares against
`Abs((q^2-1)*(q*(q-2)-1))/(2*q^3*(q-1))`, which is algebraically identical to
the published `|q^2-2q-1|(q+1)/(2q^3)`: the `z = 1` cell. On **2026-09-08** the
owner ruled that `epsilon` is the Markov trace at `z_D = q^3/(q^2+1)` and
**retired the published form as the base**. The witness was last touched
2026-09-07, one day before.

So the one computational test of attack A's bridge is aimed at a functional
that is no longer the canonical base. **That does not make it wrong** -- the
inequality of those two objects is an exact algebraic fact and stands. What it
makes UNMEASURED is the question that now matters: does `Delta tr_M` match the
RULED base?

## What this probe measures

The same comparison, re-aimed. Under the ansatz `Q_beta = |epsilon(Delta)|*E_0`
with `epsilon` the Markov trace at `z_D`, the slot object is
`tr_M(Delta, z_D) = h^2/2 - h*z_D` (the corpus form, `h = q - 1/q`). This probe
Taylor-expands the exact Habiro `Delta tr_M` and each admissible slot object in
`eps = q - 1` and compares, calibrating first against the recorded Form A
figures so the harness is trusted before anything new is read off it.

Both admissible functionals are tested, not just the ruled one: the
augmentation (`z = q`) is the other admissible point, and reporting only the
ruled cell would hide whether the Habiro object matches EITHER.

## What a match would and would not mean

A match would NOT derive alpha. It would remove the corpus's one measured
obstacle to attack A, which is what `qou-pdix` needs to rank the route. A
mismatch would extend the existing negative to the ruled base, which is the
more useful outcome for the bean: it would close attack A's bridge under the
canonical convention rather than leaving it open against a retired one.

Per the anti-fit directive, the verdict here is whatever the algebra gives.
Nothing is selected against `Q_codata`, and no coefficient is tuned.

## Precision

sympy exact rationals throughout; mpmath at the proton pin for the evaluations.
No float64: `float(` appears nowhere, no `statistics`, no `math.`.
"""
from __future__ import annotations

import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import _path_bridge as _pb  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

set_compute_dps(50)

q = sp.Symbol("q", positive=True)
eps = sp.Symbol("eps")

# h and z_D exactly as the corpus defines them.
h = q - 1 / q
Z_D = q ** 3 / (q ** 2 + 1)
Z_AUG = q

RESULTS: list[dict] = []


def check(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}\n")


def lead_coeffs(expr, n: int = 6) -> dict:
    """Leading Taylor coefficients in eps = q - 1 (the 2026-08-08 basis)."""
    e = sp.series(sp.expand(sp.together(expr).subs(q, 1 + eps)), eps, 0, n).removeO()
    e = sp.expand(e)
    return {k: sp.nsimplify(e.coeff(eps, k)) for k in range(n)}


def first_nonzero(c: dict):
    for k in sorted(c):
        if c[k] != 0:
            return k, c[k]
    return None, sp.Integer(0)


def main() -> int:
    print("=" * 78)
    print(" Habiro Delta tr_M against the RULED base (z_D), not the retired z=1 cell")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-delta-tr-vs-ruled-base", engine="sympy+mpmath")

    # ---- the exact Habiro Delta tr_M, from the same upstream as 2026-08-08 --
    hab = wb.add_upstream(
        _pb.witness_path("habiro-coefficients-atomic.witness.json", _HERE)
    )
    tr_p = sp.sympify(hab["results"]["p (proton, A=1)"]["tr_M_in_q"], locals={"q": q})
    tr_n = sp.sympify(hab["results"]["n (neutron, A=1)"]["tr_M_in_q"], locals={"q": q})
    delta_tr = sp.simplify(tr_n - tr_p)

    # ---- the three slot objects -------------------------------------------
    # RETIRED (z = 1 cell): Form A's net-winding slot, verbatim from the
    # 2026-08-08 witness, kept ONLY to calibrate this harness against it.
    delta_net_A = (q ** 2 - 1) * (q * (q - 2) - 1) / (2 * q ** 2)
    # RULED (owner, 2026-09-08): the Markov trace at z_D on the NF vector.
    tr_at_zD = sp.simplify(h ** 2 / 2 - h * Z_D)
    # The OTHER admissible point: the augmentation, z = q.
    tr_at_aug = sp.simplify(h ** 2 / 2 - h * Z_AUG)

    cT = lead_coeffs(delta_tr)
    cA = lead_coeffs(delta_net_A)
    cD = lead_coeffs(tr_at_zD)
    cG = lead_coeffs(tr_at_aug)

    print("\n  Leading Taylor coefficients, basis eps = q - 1:\n")
    print(f"     {'order':>5} | {'Delta tr_M':>14} | {'Delta(net)_A':>14} "
          f"| {'tr_M at z_D':>14} | {'tr_M at z=q':>14}")
    print("     " + "-" * 74)
    for k in range(6):
        print(f"     {k:>5} | {str(cT[k]):>14} | {str(cA[k]):>14} "
              f"| {str(cD[k]):>14} | {str(cG[k]):>14}")

    # ---- calibration: reproduce the RECORDED 2026-08-08 figures -------------
    kT, vT = first_nonzero(cT)
    kA, vA = first_nonzero(cA)
    check(
        "harness_reproduces_the_recorded_form_A_negative",
        kA == 1 and vA == -2 and kT == 1 and vT == sp.Rational(-5, 4),
        f"leading orders Delta(net)_A = {vA}*eps^{kA} and Delta tr_M = "
        f"{vT}*eps^{kT}, matching qbeta-delta-tr-vs-formA.witness.json's "
        f"recorded '-2 eps' and '-5/4 eps'. The harness is trusted against the "
        f"existing record BEFORE anything new is read from it.",
    )

    # ---- the re-aimed test: RULED base --------------------------------------
    kD, vD = first_nonzero(cD)
    matches_zD = sp.simplify(delta_tr - tr_at_zD) == 0
    check(
        "delta_tr_is_NOT_the_ruled_z_D_slot_object",
        not matches_zD,
        f"Delta tr_M - tr_M(Delta, z_D) does not vanish identically. Leading "
        f"orders: Delta tr_M = {vT}*eps^{kT}, tr_M at z_D = {vD}*eps^{kD}. So "
        f"the 2026-08-08 negative EXTENDS to the ruled base -- re-aiming it at "
        f"the canonical convention does not rescue the identification."
        if not matches_zD else
        "they are identically equal -- the Habiro object IS the ruled slot "
        "object, and the 2026-08-08 negative was an artifact of the retired "
        "z = 1 cell.",
    )

    # ---- and the other admissible point ------------------------------------
    kG, vG = first_nonzero(cG)
    matches_aug = sp.simplify(delta_tr - tr_at_aug) == 0
    check(
        "delta_tr_is_NOT_the_augmentation_slot_object_either",
        not matches_aug,
        f"Delta tr_M - tr_M(Delta, z=q) does not vanish identically either "
        f"(leading {vG}*eps^{kG}). Both admissible functionals are tested, so "
        f"this is not a statement about the ruled cell alone.",
    )

    # ---- proportionality: is the mismatch structural or a normalisation? ----
    # The sibling probe's finding 5: leading-order difference is weak evidence
    # if the two series are merely PROPORTIONAL. Term-by-term ratio settles it.
    ratios = {}
    for k in range(1, 6):
        if cD[k] != 0:
            ratios[k] = sp.nsimplify(sp.Rational(0) + cT[k] / cD[k])
    vals = list(ratios.values())
    non_constant = len(set(map(str, vals))) > 1
    signs = {sp.sign(v) for v in vals if v != 0}
    print("  Term-by-term ratio Delta tr_M / tr_M(z_D):")
    for k, v in ratios.items():
        print(f"     k={k}  {v}   = {sp.nsimplify(v).evalf(8)}")
    check(
        "the_z_D_mismatch_is_structural_not_a_normalisation",
        non_constant,
        f"the term-by-term ratio is NOT constant across k "
        f"({len(set(map(str, vals)))} distinct values over "
        f"{len(ratios)} orders; sign set {sorted(map(str, signs))}). A constant "
        f"ratio would mean the two series differ only by normalisation, which "
        f"would make the mismatch uninteresting. It is not constant, so the "
        f"objects are structurally distinct -- the same discipline the sibling "
        f"probe applied to the Form A negative.",
    )

    # ---- numbers at the proton pin, for the record --------------------------
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
    Qexp = mp.mpf(str(Q_NEUTRON_MEV))
    rows = []
    for label, expr, status in (
        ("Delta tr_M (Habiro)", delta_tr, "the object under test"),
        ("Delta(net)_A (z = 1)", delta_net_A, "RETIRED as base 2026-09-08"),
        ("tr_M at z_D", tr_at_zD, "RULED base 2026-09-08"),
        ("tr_M at z = q (augmentation)", tr_at_aug, "the other admissible point"),
    ):
        v = ev(sp.simplify(expr))
        Q = abs(v) * E0
        rows.append({
            "slot_object": label,
            "status": status,
            "value_at_q0": fmt(v),
            "Q_MeV": fmt(Q),
            "err_pct_vs_codata": fmt((Q / Qexp - 1) * 100),
        })
        print(f"    {label:<30} {fmt(Q)[:12]:>14} MeV   "
              f"err {fmt((Q / Qexp - 1) * 100)[:9]:>10} %")

    allp = all(r["passed"] for r in RESULTS)
    print(f"\n  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    for r in RESULTS:
        wb.add_assertion(
            r["name"],
            computed="PASS" if r["passed"] else "FAIL",
            expected="PASS",
            tolerance="exact",
            source=r["detail"],
        )
    wb.save({
        "description": (
            "Re-aims the corpus's 2026-08-08 negative against the Habiro route "
            "at the RULED base. qbeta-delta-tr-vs-formA compares Delta tr_M "
            "against Form A's net-winding slot -- the z = 1 cell, which the "
            "owner retired as the base on 2026-09-08, one day after that "
            "witness was last touched. This re-runs the same comparison "
            "against the Markov trace at z_D = q^3/(q^2+1) (the ruled epsilon) "
            "and against the augmentation z = q (the other admissible point), "
            "calibrating first against the recorded Form A figures. Scope (a), "
            "proton pin, convention D. Asserts nothing about alpha."
        ),
        "bean": "qou-pdix",
        "q0Anchor": "proton",
        "taylor_basis": "eps = q - 1",
        "leading_taylor_coefficients": {
            "delta_tr_M": {f"eps^{k}": str(cT[k]) for k in range(6)},
            "delta_net_A_RETIRED": {f"eps^{k}": str(cA[k]) for k in range(6)},
            "tr_M_at_z_D_RULED": {f"eps^{k}": str(cD[k]) for k in range(6)},
            "tr_M_at_z_q_augmentation": {f"eps^{k}": str(cG[k]) for k in range(6)},
        },
        "ratio_delta_tr_over_tr_zD": {f"k={k}": str(v) for k, v in ratios.items()},
        "numerical_at_q0": rows,
        "scope": (
            "(a) scope-limited: these exact objects at the proton pin under "
            "convention D. It does NOT derive alpha, does not exclude the "
            "Habiro ring from an alpha closure by another route, and does not "
            "retract the 2026-08-08 Form A negative -- that inequality is an "
            "exact algebraic fact and stands on its own terms. What it settles "
            "is only whether re-aiming that negative at the ruled base changes "
            "its verdict."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
