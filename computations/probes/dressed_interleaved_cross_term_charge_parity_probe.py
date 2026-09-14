#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic computation in sympy over Q(q, d0, d1, d2);
# the only floating point is mpmath mpf at the proton pin for the reported magnitudes.
"""Is the Markov-trace bond-multiplicativity defect CHARGE-sensitive, and of which parity?

Bean `qou-vwu3`. Owner instruction 2026-09-14: "now go after the non-Markov-invariant
functional."

## What the object actually is -- naming it correctly first

The phrase "non-Markov-invariant functional" was my own, and it is the wrong name.
The Markov trace IS Markov-invariant. What fails is **bond-multiplicativity**: on an
interleaved word class the trace of a product of bond letters is not the product of
their traces, and the defect depends on the ORDER of the letters. That order-dependence
is the exchange-sensitivity the extensive-term arc has been asking for, and it is a
property of the existing trace rather than of some new functional.

`docs/audits/2026-09-03-markov-trace-not-bond-multiplicative-n4.md` (bean `qou-kru4`)
establishes it exactly at `n = 4`, two independent ways:

    interleaved  tr(g0 g1 g0 g2 g1) = z (z^2 + h z + h^2 z^2)
    sequential   tr(g0^2 g1^2 g2)   = z (h z + 1)^2
    difference                      = z (z^2 - h z - 1)          < 0 at convention D

It matters because `qou-brng` closes every other route from a different direction --
the Ocneanu/Markov trace FAMILY by a rank bound (`ocneanuFamily_finrank_le`), the
magnitude by `cyclic_trace_kills_iterCommTower`, mu-bar_123 as channel-blind, and the
whole linking-data class (`lk` IS `I_3`, both channels at `I_3 = 0`, achievable
asymmetry exactly 1 against 33.7 required). Its closure note leaves exactly one thing
open: *"an invariant reading the braid word beyond its linking data"*. The
multiplicativity defect is such an object, and the bond-graph exclusions provably do
not reach it because it is a word-CLASS effect, not a bond-graph count.

## THE GAP THIS FILLS

Every statement above is on **bare generators** `g_i`. The production bonds are
**charge-dressed** letters. `QOU.MathlibExt.MarkovBondRule.sigmaPlus g d` is `sigma_g +
d*I`, and the three canonical dressings are

    d_pp = 0                      f_pp = z
    d_pn = -h(1/2 - delta/4)      f_pn = z - h(1/2 - delta/4)
    d_nn = -h                     f_nn = z - h

so nobody has asked whether the DEFECT sees the charge at all. That is this probe.

## THE PARITY QUESTION, and why it is the decisive one

Charge symmetry acts on a bond by exchanging p and n, i.e. `t -> 1 - t` in
`f = z - h*t`. On the dressing that is the affine involution

    M : d  |->  -h - d                    (checked to be an involution below)

which sends `d_pp <-> d_nn` and fixes `d_pn` up to the `delta` term. So the defect
splits canonically:

    Delta = Delta_even + Delta_odd,   Delta_even(M d) = +Delta_even,  Delta_odd(M d) = -Delta_odd

and the answer PRUNES either way:

  * `Delta_odd == 0` identically -> the interleaved word class is charge-BLIND, and it
    cannot supply the electromagnetic (mirror-antisymmetric) term however it is wired.
    One more route closed, and closed structurally rather than by a miss.
  * `Delta_odd != 0` -> the class carries a mirror-antisymmetric piece whose size is
    then a DERIVED number, with no free parameter: `z`, `h` and the three `d` are all
    fixed by `q0`.

## METHOD

The 16-dimensional spin-1/2 representation on `V^{tensor 4}` with the brick-1 R-matrix
and the mu-weighted quantum trace normalised by `[2]^4` -- route (2) of the audit,
reused verbatim so that this probe's harness is the one already cross-checked against
the Ocneanu axioms. Letters are dressed as `b_i = sigma_i + d_i * I_16`. Everything is
exact sympy over `Q(q, d0, d1, d2)`; nothing is computed in float.

The CONTROL is the whole safety argument: setting `d = 0` must reproduce the recorded
closed form `-q^3(q^2-q+1)(q^2+q+1)/(q^2+1)^3` exactly. If it does not, the harness is
wrong and every other number here is about the harness.

## WHAT IS ASSERTED vs WHAT IS REPORTED

Asserted -- each can genuinely fail, and a bug in the dressing would trip at least one:

  * the control (bare limit reproduces the recorded cross term);
  * Hecke and braid relations hold in the representation;
  * `M` is an involution, and `M` exchanges the pp and nn dressings;
  * the even/odd split reconstructs `Delta` exactly and each part has its stated parity.

**The parity VERDICT is reported, not asserted** -- it is the measurement, and asserting
it either way would be asserting the answer.

## SCOPE

Scope (a). This is `n = 4` with three bonds; it is not a nucleus, and the production
atom word is sequential, so no production number moves. It asks a structural question
about the defect -- does it see charge, and with which parity -- whose answer constrains
whether the word-class route can carry the mirror splitting at all.
"""

from __future__ import annotations

import datetime
import json
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

try:
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402
except Exception:  # pragma: no cover
    Q_50_DIGIT_STR = None

_T0 = time.monotonic()
_CHECKS: list[dict] = []


def log(msg: str) -> None:
    print(f"[{time.monotonic() - _T0:7.1f}s] {msg}", flush=True)


def check(name: str, ok: bool, detail: str) -> bool:
    _CHECKS.append({"name": name, "passed": bool(ok), "detail": detail})
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    return bool(ok)


def route_rep(n: int, q):
    """Spin-1/2 V^{tensor n} rep, mu-weighted quantum trace / [2]^n.

    Verbatim from markov_trace_n4_interleaved_cross_term_probe.route_rep, so the
    control below is a genuine cross-check against an already-verified harness.
    """
    R = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
    I2 = sp.eye(2)

    def kron(*ms):
        out = ms[0]
        for m in ms[1:]:
            out = sp.kronecker_product(out, m)
        return out

    def sigma(i):
        return kron(*([I2] * i + [R] + [I2] * (n - i - 2)))

    W = kron(*([sp.diag(q, 1 / q)] * n))
    br2 = q + 1 / q

    def tr(X):
        return sp.cancel(sp.together((W * X).trace() / br2 ** n))

    return sigma, tr


def main() -> int:
    q = sp.symbols("q", positive=True)
    d0, d1, d2 = sp.symbols("d0 d1 d2")
    h_q = q - 1 / q
    z_D = q ** 3 / (q ** 2 + 1)
    I16 = sp.eye(16)

    log("building the 16-dim representation")
    sigma, tr = route_rep(4, q)
    s0, s1, s2 = sigma(0), sigma(1), sigma(2)

    check(
        "REP_hecke_relation_holds",
        sp.simplify(s0 * s0 - h_q * s0 - I16) == sp.zeros(16),
        "sigma^2 = h sigma + 1 in the representation -- if this fails the rep is not Hecke.",
    )
    check(
        "REP_braid_relation_holds",
        sp.simplify(s0 * s1 * s0 - s1 * s0 * s1) == sp.zeros(16),
        "sigma0 sigma1 sigma0 = sigma1 sigma0 sigma1 in the representation.",
    )

    # ---- dressed letters ---------------------------------------------------
    b0, b1, b2 = s0 + d0 * I16, s1 + d1 * I16, s2 + d2 * I16

    log("tracing the interleaved dressed word b0 b1 b0 b2 b1")
    inter = tr(b0 * b1 * b0 * b2 * b1)
    log("tracing the sequential dressed word b0 b0 b1 b1 b2")
    seq = tr(b0 * b0 * b1 * b1 * b2)
    log("forming the difference")
    Delta = sp.cancel(sp.together(inter - seq))

    # ---- CONTROL: the bare limit must reproduce the recorded closed form ----
    recorded = -q ** 3 * (q ** 2 - q + 1) * (q ** 2 + q + 1) / (q ** 2 + 1) ** 3
    bare = sp.cancel(Delta.subs({d0: 0, d1: 0, d2: 0}))
    check(
        "CONTROL_bare_limit_reproduces_the_recorded_cross_term",
        sp.simplify(bare - recorded) == 0,
        f"Delta|_(d=0) = {sp.factor(bare)}; recorded (qou-kru4 audit) "
        f"= -q^3(q^2-q+1)(q^2+q+1)/(q^2+1)^3.  If this fails, the dressing is wrong "
        f"and nothing else in this probe means anything.",
    )

    # ---- the mirror involution on dressings --------------------------------
    def M(expr):
        """Charge conjugation p <-> n on every bond: d |-> -h - d."""
        return expr.subs({d0: -h_q - d0, d1: -h_q - d1, d2: -h_q - d2}, simultaneous=True)

    check(
        "MIRROR_is_an_involution",
        sp.simplify(M(M(d0)) - d0) == 0,
        "M(M(d)) = d, so the even/odd split below is well defined.",
    )
    d_pp, d_nn = sp.Integer(0), -h_q
    check(
        "MIRROR_exchanges_the_pp_and_nn_dressings",
        sp.simplify((-h_q - d_pp) - d_nn) == 0 and sp.simplify((-h_q - d_nn) - d_pp) == 0,
        f"M(d_pp = 0) = -h = d_nn and M(d_nn) = d_pp.  This is what makes M the "
        f"charge conjugation rather than an arbitrary affine map.",
    )

    log("applying the mirror and splitting into even/odd parts")
    Delta_M = sp.cancel(sp.together(M(Delta)))
    even = sp.cancel(sp.together((Delta + Delta_M) / 2))
    odd = sp.cancel(sp.together((Delta - Delta_M) / 2))

    check(
        "SPLIT_reconstructs_Delta",
        sp.simplify(even + odd - Delta) == 0,
        "Delta = even + odd exactly.",
    )
    check(
        "SPLIT_even_part_is_mirror_even",
        sp.simplify(M(even) - even) == 0,
        "even(M d) = +even(d).",
    )
    check(
        "SPLIT_odd_part_is_mirror_odd",
        sp.simplify(M(odd) + odd) == 0,
        "odd(M d) = -odd(d).",
    )

    # ---- THE MEASUREMENT (reported, not asserted) --------------------------
    odd_is_zero = sp.simplify(odd) == 0
    log("verdict computed")

    # ---- what the answer COLLAPSES TO, found by inspecting the odd part ----
    # The odd part came out depending on d2 alone, with numerator q(2*d2 + h)
    # (using q^2 - 1 = q*h), which vanishes at the charge-symmetric midpoint
    # d2 = -h/2.  That shape says the whole defect should factor through the
    # LAST bond's factor.  It does, exactly:
    f2 = z_D + d2
    markov_defect = z_D ** 2 - h_q * z_D - 1
    log("testing the factorisation Delta = f2 * (z^2 - h z - 1)")
    check(
        "FACTORISATION_Delta_eq_lastBondFactor_times_MarkovDefect",
        sp.simplify(Delta - sp.cancel(sp.together(f2 * markov_defect))) == 0,
        f"Delta = (z + d2)(z^2 - hz - 1) EXACTLY.  The convention-D Markov defect "
        f"z^2-hz-1 = {sp.factor(sp.cancel(sp.together(markov_defect)))} is charge-BLIND, "
        f"so the entire charge dependence of the cross term is the single factor f2.",
    )
    check(
        "CHARGE_DEPENDENCE_IS_ONLY_THROUGH_THE_PEELED_BOND",
        (not Delta.has(d0)) and (not Delta.has(d1)),
        f"d0 present in Delta: {Delta.has(d0)};  d1 present: {Delta.has(d1)}.  The two "
        f"INTERLEAVED bonds drop out entirely; only d2 -- the bond on the generator that "
        f"is Markov-peeled -- survives.  So the object that reads the word beyond its "
        f"linking data does not read the CHARGES of the letters it interleaves.",
    )
    f2_even = sp.cancel((f2 + f2.subs(d2, -h_q - d2)) / 2)
    f2_odd = sp.cancel((f2 - f2.subs(d2, -h_q - d2)) / 2)
    check(
        "PARITY_RATIO_IS_IDENTICAL_TO_THE_BOND_FACTOR_ITSELF",
        sp.simplify(sp.cancel(odd / even) - sp.cancel(f2_odd / f2_even)) == 0,
        f"Delta_odd/Delta_even == f2_odd/f2_even identically.  Multiplying by a "
        f"charge-blind scalar cannot move an odd/even ratio, so the cross term inherits "
        f"the bond channel's isospin parity structure VERBATIM -- the same structure "
        f"QOU.MassTheory.BondChannelTzParity proves cannot be even at any q > 1.",
    )

    print()
    print("=" * 72)
    print("THE VERDICT (reported, NOT asserted -- this is the measurement)")
    print("=" * 72)
    print(f"  mirror-ODD part identically zero?   {odd_is_zero}")
    print()
    if odd_is_zero:
        print("  => The interleaved cross term is CHARGE-BLIND.  The word-class route")
        print("     cannot supply a mirror-antisymmetric (electromagnetic) term at all,")
        print("     for any wiring and any q.  Scope (b) for this class.")
    else:
        print("  => The interleaved cross term CARRIES a mirror-antisymmetric piece.")
        print("     Its size is then derived, not chosen: z, h and every d are fixed by q0.")
        print(f"     odd part = {sp.factor(sp.simplify(odd))}")
    print()
    print(f"  mirror-EVEN part = {sp.factor(sp.simplify(even))}")

    # ---- the 3H / 3He mirror pattern, at the live dressings ----------------
    from _li_2_q_util import flavor_split_leading  # noqa: E402

    payload_pin = {}
    if Q_50_DIGIT_STR is not None:
        q0 = mp.mpf(Q_50_DIGIT_STR)
        hh = q0 - 1 / q0
        delta = mp.mpf(str(flavor_split_leading(q0)))
        t_pn = mp.mpf(1) / 2 - delta / 4
        dpp_n, dpn_n, dnn_n = mp.mpf(0), -hh * t_pn, -hh

        def ev(expr, vals):
            f = sp.lambdify((q, d0, d1, d2), expr, modules="mpmath")
            return f(q0, *vals)

        # A 3-bond chain whose mirror partner swaps the like-pair bond:
        #   3H-like  (pn, pn, nn)   <->   3He-like  (pn, pn, pp)
        trit = (dpn_n, dpn_n, dnn_n)
        heli = (dpn_n, dpn_n, dpp_n)
        D_t, D_h = ev(Delta, trit), ev(Delta, heli)
        print()
        print("AT THE PROTON PIN, on the 3H/3He mirror bond pattern (scope (a): n=4, not a nucleus)")
        print(f"  Delta(pn,pn,nn)  = {mp.nstr(D_t, 20)}")
        print(f"  Delta(pn,pn,pp)  = {mp.nstr(D_h, 20)}")
        print(f"  difference       = {mp.nstr(D_t - D_h, 20)}")
        print(f"  bare  Delta(0,0,0-generators) = {mp.nstr(ev(bare, (0, 0, 0)), 20)}")
        payload_pin = {
            "q0": mp.nstr(q0, 30),
            "d_pp": mp.nstr(dpp_n, 30),
            "d_pn": mp.nstr(dpn_n, 30),
            "d_nn": mp.nstr(dnn_n, 30),
            "Delta_3H_pattern": mp.nstr(D_t, 30),
            "Delta_3He_pattern": mp.nstr(D_h, 30),
            "mirror_difference": mp.nstr(D_t - D_h, 30),
            "bare_cross_term": mp.nstr(ev(bare, (0, 0, 0)), 30),
        }

    payload = {
        "description": (
            "Charge parity of the Markov-trace bond-multiplicativity defect at n=4. "
            "The recorded cross term z(z^2-hz-1) is on BARE generators; this dresses the "
            "letters as sigma_i + d_i*I with the canonical bond dressings and splits the "
            "defect under the charge conjugation d -> -h-d. The verdict is REPORTED, not "
            "asserted. Scope (a): n=4 with three bonds, not a nucleus; the production atom "
            "word is sequential so no production number moves."
        ),
        "bean": "qou-vwu3",
        "builds_on": {
            "audit": "docs/audits/2026-09-03-markov-trace-not-bond-multiplicative-n4.md",
            "bean": "qou-kru4",
            "harness": "computations/probes/markov_trace_n4_interleaved_cross_term_probe.py route_rep",
            "why": (
                "qou-brng closes the Ocneanu trace family (rank bound), the magnitude "
                "(cyclic_trace_kills_iterCommTower), mu-bar_123 (channel-blind) and the whole "
                "linking-data class (lk IS I_3, both channels at I_3 = 0). Its closure note "
                "leaves open 'an invariant reading the braid word beyond its linking data', "
                "and the multiplicativity defect is such an object."
            ),
        },
        "q0Anchor": "physical_proton",
        "convention": "D (z = q^3/(q^2+1))",
        "mirror_map": "d -> -h - d  (p<->n on each bond; exchanges d_pp=0 and d_nn=-h)",
        "verdict": {
            "odd_part_identically_zero": bool(odd_is_zero),
            "odd_part": sp.srepr(sp.simplify(odd)) if not odd_is_zero else "0",
            "odd_part_factored": str(sp.factor(sp.simplify(odd))),
            "even_part_factored": str(sp.factor(sp.simplify(even))),
        },
        "bare_limit_control": str(sp.factor(bare)),
        "factorisation": {
            "identity": "Delta(d0,d1,d2) = (z + d2) * (z^2 - h*z - 1)",
            "markov_defect_convD": str(sp.factor(sp.cancel(sp.together(z_D ** 2 - h_q * z_D - 1)))),
            "d0_present": bool(Delta.has(d0)),
            "d1_present": bool(Delta.has(d1)),
            "consequence": (
                "The cross term's entire charge dependence is one bond factor times a "
                "charge-blind scalar, so its mirror odd/even RATIO equals the bond "
                "factor's own. The interleaved word class changes the MAGNITUDE of the "
                "bond channel (extra binding, which is what qou-kru4 wants it for) and "
                "provably cannot change its CHARGE PARITY."
            ),
        },
        "at_proton_pin": payload_pin,
        "scope": (
            "(a) scope-limited: n=4, three bonds, exact and symbolic. Not a nucleus. "
            "Does NOT claim the production word is interleaved -- it is sequential "
            "(qou-5vhf is which word class a nucleus is)."
        ),
        "assertions": _CHECKS,
        "free_parameters": 0,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    out = _HERE / "dressed-interleaved-cross-term-charge-parity.witness.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"\nwrote {out}")

    npass = sum(1 for c in _CHECKS if c["passed"])
    print(f"\n{npass}/{len(_CHECKS)} assertions passed")
    return 0 if npass == len(_CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
