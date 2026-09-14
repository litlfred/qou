#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic computation in sympy over Q(q, d0, d1);
# there is no floating-point arithmetic anywhere in this probe.
"""Does the MINIMAL cross term see the charge dressing on its own two letters?

Bean `qou-vwu3`.  Companion to the Lean theorem
`QOU.MathlibExt.RevisitClass.cyclicSquare_cross_term_dressed` (sorry-free), which
proves the general statement; this probe is the independent concrete confirmation in
a specific representation, and it measures the four brackets the Lean proof splits
the answer into.

## THE QUESTION

`dressed_interleaved_cross_term_charge_parity_probe` (merged, 20/20) measured the
`n = 4` dressed bond-multiplicativity defect and found

    Delta_4 = (z + d2) * (z^2 - h z - 1)

i.e. the charge dependence of the whole `n = 4` cross term is **one factor**, and that
factor carries the dressing of `d2` -- the letter that is NOT part of the interleaved
pair.  `d0` and `d1`, the dressings of the two letters that actually alternate, are
absent from the answer.

That was reported as a measurement with no mechanism.  The mechanism is the question
here, and it is not an `n = 4` fact at all: by `interleaved_eq_stab_cyclicSquare` the
`n = 4` word is the three-strand cyclic square `(g_m g_{m+1})^2` stabilised once, and
the stabilisation contributes exactly the `(z + d2)`.  So the real claim is about
`n = 3`:

    **the cyclic square's cross term is blind to the square's OWN dressings.**

## WHAT IS MEASURED

With `b0 = sigma_0 + d0*I` and `b1 = sigma_1 + d1*I` on `V^{tensor 3}` (8-dimensional,
spin-1/2 R-matrix, mu-weighted quantum trace normalised by `[2]^3`), exactly over
`Q(q, d0, d1)`:

    Delta_3(d0, d1) = tr(b0 b1 b0 b1) - tr(b0^2 b1^2)

and whether `d0`, `d1` appear in it.

## THE FOUR BRACKETS -- what the Lean proof says is happening

`dressed_difference_expand` is a pure ring identity (scalars are central):

    (a+s)(c+t)(a+s)(c+t) - (a+s)^2(c+t)^2
      = (acac - a^2c^2) + t(aca - a^2c) + s(cac - ac^2) + st(ca - ac)

-- no `s^2`, `t^2`, `s^2 t` or `s t^2` term survives, because each of those multiplies
the SAME monomial in `a, c` in both words.  And the three brackets that could carry the
dressing are exactly the three that `RevisitClassCrossTerm`'s revisit-class table
already lists as cross-term-free:

    aca - a^2c   ->  0   oneStepRevisit_eq_monotone   (cyclicity + one Markov move)
    cac - ac^2   ->  0   mirrorRevisit_eq_monotone    (braid, then one Hecke collapse
                                                       per side; NEW this session)
    ca - ac      ->  0   tr_bondCommutator            (cyclicity alone; NEW)

So the blindness is the revisit-class table read one degree down, not a coincidence of
one computation.  This probe checks the bracket identity as a matrix identity and each
bracket's trace separately, so a failure localises to a bracket rather than to "the
answer is different".

## WHY IT MATTERS -- what it prunes

Charge conjugation acts on a bond by `t -> 1 - t` in `f = z - h*t`, i.e. on the dressing
by the affine involution `M : d |-> -h - d`, which exchanges `d_pp = 0` and `d_nn = -h`.
A quantity independent of `d0, d1` is trivially `M`-even in them, so its charge-odd part
in the square's own letters is identically zero.

Consequence: a cyclically braided triple contributes the identical cross term whatever
charges sit on its two alternating letters.  This word class cannot distinguish `pp`
from `nn`, so it is **not** a candidate carrier for a charge-antisymmetric
(electromagnetic / mirror) term, however it is wired.  Scope (b) for this class --
the exclusion rests on the proved bracket identity plus three proved vanishings, not on
a numerical miss.

## WHAT IS ASSERTED vs WHAT IS REPORTED

Asserted -- each can genuinely fail:

  * Hecke and braid relations hold in the representation (if these fail, nothing else
    here is about the Hecke algebra);
  * the CONTROL: at `d0 = d1 = 0` the cross term reproduces the convention-D Markov
    defect `z^2 - h z - 1 = -(q^4+q^2+1)/(q^2+1)^2` recorded by
    `cyclicSquare_cross_term_neg_convD`;
  * the four-bracket decomposition holds as an exact matrix identity;
  * each of the three lower brackets has trace zero;
  * `M` is an involution and exchanges the pp and nn dressings;
  * the stabilisation tie-in: `Delta_4 = (z + d2) * Delta_3` at exact rational sample
    points, reproducing the merged `n = 4` closed form from this `n = 3` one.

**The dressing-dependence VERDICT is reported, not asserted.**  Asserting "d0 and d1 are
absent" would be asserting the answer; the probe prints which symbols survive.

## SCOPE

Scope (a) as a measurement, scope (b) as an exclusion of this word class.  Three strands
is not a nucleus and no production number moves.  The production atom word is sequential,
so this constrains a candidate route rather than correcting a computed observable.
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

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

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

    Verbatim from `markov_trace_n4_interleaved_cross_term_probe.route_rep` (via
    `dressed_interleaved_cross_term_charge_parity_probe`), so this probe's harness is
    the one already cross-checked against the Ocneanu axioms.
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
    I8 = sp.eye(8)

    log("building the 8-dim representation on V^{tensor 3}")
    sigma, tr = route_rep(3, q)
    a, c = sigma(0), sigma(1)

    check(
        "REP_hecke_relation_holds",
        sp.simplify(a * a - h_q * a - I8) == sp.zeros(8),
        "sigma^2 = h sigma + 1 in the representation -- if this fails the rep is not Hecke.",
    )
    check(
        "REP_braid_relation_holds",
        sp.simplify(a * c * a - c * a * c) == sp.zeros(8),
        "sigma0 sigma1 sigma0 = sigma1 sigma0 sigma1 in the representation.",
    )

    # ---- the four-bracket decomposition, as a MATRIX identity -----------------
    log("checking the four-bracket decomposition as an exact matrix identity")
    s, t = d0, d1
    A = a + s * I8
    C = c + t * I8
    lhs_mat = A * C * A * C - A * A * (C * C)
    brk4 = a * c * a * c - a * a * (c * c)
    brk_t = a * c * a - a * a * c
    brk_s = c * a * c - a * c * c
    brk_st = c * a - a * c
    rhs_mat = brk4 + t * brk_t + s * brk_s + (s * t) * brk_st
    check(
        "BRACKET_decomposition_is_exact",
        sp.simplify(sp.expand(lhs_mat - rhs_mat)) == sp.zeros(8),
        "(a+s)(c+t)(a+s)(c+t) - (a+s)^2(c+t)^2 = (acac - a^2c^2) + t(aca - a^2c) "
        "+ s(cac - ac^2) + st(ca - ac).  Lean: dressed_difference_expand.",
    )

    # ---- each lower bracket traces to zero -----------------------------------
    log("tracing the three lower brackets")
    tr_t = sp.cancel(sp.together(tr(brk_t)))
    tr_s = sp.cancel(sp.together(tr(brk_s)))
    tr_st = sp.cancel(sp.together(tr(brk_st)))
    check(
        "BRACKET_t_trace_vanishes",
        sp.simplify(tr_t) == 0,
        f"tr(aca - a^2c) = {tr_t}.  Lean: oneStepRevisit_eq_monotone.",
    )
    check(
        "BRACKET_s_trace_vanishes",
        sp.simplify(tr_s) == 0,
        f"tr(cac - ac^2) = {tr_s}.  Lean: mirrorRevisit_eq_monotone (new).",
    )
    check(
        "BRACKET_st_trace_vanishes",
        sp.simplify(tr_st) == 0,
        f"tr(ca - ac) = {tr_st}.  Lean: tr_bondCommutator (new).",
    )

    # ---- the control: bare limit ---------------------------------------------
    log("tracing the bare cyclic square and Hopf chain")
    bare = sp.cancel(sp.together(tr(a * c * a * c) - tr(a * a * (c * c))))
    defect = sp.cancel(sp.together(z_D ** 2 - h_q * z_D - 1))
    check(
        "CONTROL_bare_limit_is_the_markov_defect",
        sp.simplify(bare - defect) == 0,
        f"tr((g0 g1)^2) - tr(g0^2 g1^2) = {sp.factor(bare)}; "
        f"z^2 - h z - 1 at convention D = {sp.factor(defect)}.  "
        "If this fails the harness is wrong and nothing else here is about the Hecke algebra.",
    )

    # ---- THE MEASUREMENT -----------------------------------------------------
    log("tracing the DRESSED cyclic square and Hopf chain over Q(q, d0, d1)")
    dressed = sp.cancel(sp.together(tr(A * C * A * C) - tr(A * A * (C * C))))
    dressed_x = sp.expand(sp.cancel(dressed))
    free = sorted(str(x) for x in dressed_x.free_symbols)
    d0_present = d0 in dressed_x.free_symbols
    d1_present = d1 in dressed_x.free_symbols

    check(
        "DRESSED_equals_bare",
        sp.simplify(dressed - bare) == 0,
        f"Delta_3(d0,d1) = {sp.factor(dressed)}; bare Delta_3 = {sp.factor(bare)}.  "
        "Lean: cyclicSquare_cross_term_dressed (sorry-free).",
    )

    print()
    print("  VERDICT (reported, not asserted)")
    print(f"    Delta_3(d0, d1)      = {sp.factor(dressed)}")
    print(f"    free symbols         = {free}")
    print(f"    d0 present?          = {d0_present}")
    print(f"    d1 present?          = {d1_present}")
    print()

    # ---- charge-conjugation parity ------------------------------------------
    dd = sp.symbols("dd")
    M = -h_q - dd
    check(
        "M_is_an_involution",
        sp.simplify(M.subs(dd, M) - dd) == 0,
        "M(M(d)) = d for M : d |-> -h - d.",
    )
    d_pp = sp.Integer(0)
    d_nn = -h_q
    check(
        "M_exchanges_pp_and_nn",
        sp.simplify(M.subs(dd, d_pp) - d_nn) == 0 and sp.simplify(M.subs(dd, d_nn) - d_pp) == 0,
        f"M(d_pp = 0) = {sp.simplify(M.subs(dd, d_pp))} = d_nn, and M(d_nn) = d_pp.",
    )
    odd = sp.simplify(
        (dressed - dressed.subs({d0: -h_q - d0, d1: -h_q - d1}, simultaneous=True)) / 2
    )
    check(
        "PARITY_odd_part_vanishes",
        sp.simplify(odd) == 0,
        f"(Delta_3(d) - Delta_3(M d))/2 = {odd}.  A quantity free of d0, d1 is trivially "
        "M-even in them, so the square's own letters carry no charge-odd part.",
    )

    # ---- the stabilisation tie-in, at exact rational sample points -----------
    log("tying the n=3 result to the merged n=4 closed form (exact rationals)")
    ties = []
    tie_ok = True
    for qv, s0v, s1v, s2v in [
        (sp.Rational(5, 4), sp.Rational(0), sp.Rational(-1, 3), sp.Rational(2, 7)),
        (sp.Rational(7, 3), sp.Rational(1, 5), sp.Rational(3, 2), sp.Rational(-4, 9)),
    ]:
        sg4, t4 = route_rep(4, qv)
        I16 = sp.eye(16)
        B0 = sg4(0) + s0v * I16
        B1 = sg4(1) + s1v * I16
        B2 = sg4(2) + s2v * I16
        d4 = sp.nsimplify(sp.cancel(t4(B0 * B1 * B0 * B2 * B1) - t4(B0 * B0 * B1 * B1 * B2)))
        zv = qv ** 3 / (qv ** 2 + 1)
        hv = qv - 1 / qv
        d3 = sp.cancel(zv ** 2 - hv * zv - 1)
        pred = sp.cancel((zv + s2v) * d3)
        ok = sp.simplify(d4 - pred) == 0
        tie_ok = tie_ok and ok
        ties.append(
            {
                "q": str(qv),
                "d": [str(s0v), str(s1v), str(s2v)],
                "Delta_4": str(d4),
                "(z + d2) * Delta_3": str(pred),
                "agrees": bool(ok),
            }
        )
    check(
        "STABILISATION_Delta4_eq_z_plus_d2_times_Delta3",
        tie_ok,
        "Delta_4 = (z + d2) * (z^2 - h z - 1) at exact rational sample points, with "
        "Delta_3 the n=3 dressed cross term measured above -- reproducing the merged "
        "closed form of dressed-interleaved-cross-term-charge-parity.witness.json "
        "from this n=3 one.  The n=4 charge dependence is the STABILISER's dressing "
        "alone; the square's own two drop out.",
    )

    # ---- witness -------------------------------------------------------------
    passed = sum(1 for c in _CHECKS if c["passed"])
    total = len(_CHECKS)
    witness = {
        "$schema": "https://litlfred.github.io/qou/schemas/witness.schema.json",
        "name": "cyclic-square-cross-term-dressing-blind",
        "description": (
            "The minimal (n=3) cyclic-square cross term is independent of the dressings "
            "d0, d1 on its own two alternating letters; the charge dependence of the n=4 "
            "interleaved defect is the STABILISING letter's dressing alone."
        ),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "bean": "qou-vwu3",
        "scope": "(a) as a measurement; (b) as an exclusion of this word class",
        "convention": "D (z = q^3/(q^2+1))",
        "q0_pin": "none -- the n=3 result is exact in symbolic q; the n=4 tie-in uses "
                  "exact rational sample points, not a physical anchor",
        "representation": "spin-1/2 V^{tensor n}, mu-weighted quantum trace / [2]^n",
        "arithmetic": "exact symbolic (sympy over Q(q, d0, d1)); no floating point",
        "verdict": {
            "Delta_3_factored": str(sp.factor(dressed)),
            "free_symbols": free,
            "d0_present": bool(d0_present),
            "d1_present": bool(d1_present),
            "reading": (
                "the cyclic square's cross term is BLIND to the square's own dressings; "
                "the word class cannot distinguish pp from nn and is not a candidate "
                "carrier for a charge-antisymmetric term"
            ),
        },
        "four_brackets": {
            "identity": "(acac - a^2c^2) + t(aca - a^2c) + s(cac - ac^2) + st(ca - ac)",
            "tr_bracket_t": str(tr_t),
            "tr_bracket_s": str(tr_s),
            "tr_bracket_st": str(tr_st),
            "lean": {
                "decomposition": "QOU.MathlibExt.RevisitClass.dressed_difference_expand",
                "bracket_1": "QOU.MathlibExt.RevisitClass.cyclicSquare_cross_term",
                "bracket_t": "QOU.MathlibExt.RevisitClass.oneStepRevisit_eq_monotone",
                "bracket_s": "QOU.MathlibExt.RevisitClass.mirrorRevisit_eq_monotone",
                "bracket_st": "QOU.MathlibExt.RevisitClass.tr_bondCommutator",
                "theorem": "QOU.MathlibExt.RevisitClass.cyclicSquare_cross_term_dressed",
                "axioms": "[propext, Classical.choice, Quot.sound] -- sorry-free",
            },
        },
        "bare_limit_control": str(sp.factor(bare)),
        "markov_defect_convD": str(sp.factor(defect)),
        "stabilisation_tie_in": ties,
        "assertions": _CHECKS,
        "assertions_passed": passed,
        "assertions_total": total,
        "elapsed_seconds": round(time.monotonic() - _T0, 2),
    }
    out = _HERE / "cyclic-square-cross-term-dressing-blind.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness -> {out}")
    print(f"{passed}/{total} assertions passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
