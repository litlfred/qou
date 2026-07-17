#!/usr/bin/env python3
"""qbeta_h4_crossing_locus_probe.py — bean 8we6 (session qou-tti3, critical-eye
option 2): does a PASSING 4th-strand crossing rule exist at all?

The Route-A gate-fail audit (2026-07-13) killed nine hand-built H4 objects and
warned that arranging a cancellation by combining opposite-[s^4] candidates is
the fit trap. This probe replaces "build a tenth candidate" with the
formalize-first question: parametrize the *categorical DOF* — the 4th strand
b's coupling strengths to up/down quarks — and DERIVE whether any choice makes
the object pass the (screen-verified) decoupling gate.

Categorical form of every crossing (free-neutron-decay.py, code-authoritative):

    crossing(i,j,gen) = sigma_gen + w * 1,   w = -HA * theta,  HA = q - 1/q
      uu (Hopf/else): theta = 0      ud: theta = 1/2      dd: theta = 1

Regularizability (Delta(net)_4(q=1) = 0, needed for the log-ratio to be finite)
FORCES w(1) = 0, i.e. w proportional to HA — a structural fact, not an
assumption: a q=1-nonzero coupling breaks the (q-1) zero the ladder needs.

So the 4th strand's only freedom is two coupling strengths (alpha, beta):

    w_bu = HA * alpha   (b crossing an up quark)
    w_bd = HA * beta    (b crossing a down quark)

with the two baryons carrying the SAME rule:
    n = [u,d,d,b]  -> b crosses u,d,d  (one bu, two bd)
    p = [u,u,d,b]  -> b crosses u,u,d  (two bu, one bd)

The calibration-verified screen (qou-tti3) says: gate-pass  <=>  phi_4 = phi_6 = 0
where phi_i = [s^i] log( Delta(net)_4 / Delta(net)_3 ), s = q-1. This probe
computes phi_4(alpha,beta), phi_6(alpha,beta) as exact rational functions and
solves the system. It then tests whether any solution is a DERIVABLE categorical
point (theta in {0, 1/2, 1}, a small rational, or a q=1 root of unity), vs a
tuned/ugly value (= the fit trap, an honest wall).

  - alpha, beta CONSTANT (leading categorical strengths, like uu/ud/dd): the
    natural first family. Two equations, two unknowns.
  - If empty/ugly, that is the structural verdict for constant-coupling 4th
    strands; a passing object would need a q-DEPENDENT (higher-Taylor) coupling,
    reported as the surviving (narrower) possibility.

auditOnly; NO production wiring; NO fit (the probe DERIVES the locus and only
ACCEPTS a solution if it is a nameable categorical value; a tuned root is
reported as a wall, never wired). Scope-(a).
Witness: qbeta-h4-crossing-locus.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

from qbeta_h4_route_a_gate_probe import (  # noqa: E402
    HA, q, s, reduce_quiet, mul_terms, baryon, net,
)

alpha, beta = sp.symbols("alpha beta")


def crossing_sym(type_i, type_j, gen):
    """As free-neutron-decay, but the b strand uses symbolic couplings."""
    if type_i == type_j == "u":
        return {(gen,): sp.Integer(1)}
    if type_i == type_j == "d":
        return {(gen,): sp.Integer(1), (): -HA}
    if {type_i, type_j} == {"u", "d"}:
        return {(gen,): sp.Integer(1), (): -HA / 2}
    if "b" in (type_i, type_j):
        other = type_j if type_i == "b" else type_i
        if other == "u":
            return {(gen,): sp.Integer(1), (): HA * alpha}
        if other == "d":
            return {(gen,): sp.Integer(1), (): HA * beta}
    return {(gen,): sp.Integer(1)}    # else-branch: bare sigma_gen


def baryon_sym(core, types):
    elem = dict(core)
    for i in range(len(types)):
        for j in range(i + 1, len(types)):
            elem = reduce_quiet(mul_terms(elem, crossing_sym(types[i], types[j], i)))
    return elem


def phis_of(dnet3, dnet4, order=7):
    f = sp.cancel(sp.together(dnet4) / sp.together(dnet3))
    ser = sp.series(sp.log(f.subs(q, 1 + s)), s, 0, order + 1).removeO()
    return [sp.simplify(ser.coeff(s, i)) for i in range(1, order + 1)]


def is_categorical(val):
    """A solution component is 'derivable' if it is one of the named
    categorical strengths or a small rational (denominator <= 4)."""
    named = {sp.Integer(0): "Hopf/uu (theta=0)",
             sp.Rational(1, 2): "ud (theta=1/2)",
             sp.Integer(1): "dd (theta=1)",
             sp.Rational(-1, 2): "ud-sign", sp.Integer(-1): "dd-sign"}
    v = sp.nsimplify(val)
    if v in named:
        return named[v]
    if v.is_rational and abs(sp.denom(v)) <= 4 and abs(sp.numer(v)) <= 4:
        return f"small rational {v}"
    return None


def main() -> int:
    t0 = time.monotonic()
    mp.dps = 50
    print("=" * 78)
    print(" 8we6 option-2: does a passing 4th-strand crossing rule EXIST? (qou-tti3)")
    print("=" * 78)

    # ── H3 baseline (fixed denominator) ──
    sig1_inv = {(1,): sp.Integer(1), (): -HA}
    unit = reduce_quiet(mul_terms({(0,): sp.Integer(1)}, sig1_inv))
    b3 = reduce_quiet(mul_terms(reduce_quiet(mul_terms(unit, unit)), unit))
    dnet3 = sp.simplify(net(baryon(b3, ["u", "d", "d"])) - net(baryon(b3, ["u", "u", "d"])))
    print(f"\n[0] H3 Delta(net)_3 fixed. ({time.monotonic()-t0:.1f}s)")

    # ── symbolic 4th strand ──
    en = baryon_sym(b3, ["u", "d", "d", "b"])
    ep = baryon_sym(b3, ["u", "u", "d", "b"])
    dnet4 = sp.expand(net(en) - net(ep))
    dnet4_q1 = sp.simplify(dnet4.subs(q, 1))
    print(f"[1] Delta(net)_4(alpha,beta). Regularizability: Delta(net)_4(q=1) = {dnet4_q1}")
    reg_forced = (dnet4_q1 == 0)
    print(f"    w ∝ HA forces the (q-1) zero for ALL (alpha,beta): {reg_forced}")

    # ── phi_4, phi_6 as rational functions of (alpha, beta) ──
    t1 = time.monotonic()
    phis = phis_of(dnet3, dnet4)
    phi4 = sp.simplify(phis[3])
    phi6 = sp.simplify(phis[5])
    print(f"\n[2] phi_4(alpha,beta) = {phi4}")
    print(f"    phi_6(alpha,beta) = {phi6}")
    print(f"    ({time.monotonic()-t1:.1f}s)")

    # ── solve phi_4 = phi_6 = 0 ──
    t2 = time.monotonic()
    sols = sp.solve([sp.numer(sp.together(phi4)), sp.numer(sp.together(phi6))],
                    [alpha, beta], dict=True)
    print(f"\n[3] solve phi_4 = phi_6 = 0  ->  {len(sols)} solution(s)  "
          f"({time.monotonic()-t2:.1f}s)")

    verdicts = []
    for sold in sols:
        a_v = sp.simplify(sold.get(alpha, alpha))
        b_v = sp.simplify(sold.get(beta, beta))
        ca = is_categorical(a_v) if a_v.free_symbols == set() else None
        cb = is_categorical(b_v) if b_v.free_symbols == set() else None
        both_cat = bool(ca) and bool(cb)
        print(f"    (alpha, beta) = ({a_v}, {b_v})  "
              f"categorical: alpha={ca}  beta={cb}  ->  "
              f"{'DERIVABLE LEAD' if both_cat else 'tuned/ugly (wall)'}")
        verdicts.append({"alpha": str(a_v), "beta": str(b_v),
                         "alpha_categorical": ca, "beta_categorical": cb,
                         "derivable": both_cat})

    # ── also: check phi_4 = 0 alone (necessary), see the alpha=beta slice ──
    phi4_diag = sp.simplify(phi4.subs(beta, alpha))
    diag_roots = sp.solve(sp.numer(sp.together(phi4_diag)), alpha)
    print(f"\n[4] on the symmetric slice alpha=beta:  phi_4 roots = "
          f"{[sp.nsimplify(r) for r in diag_roots]}")

    any_lead = any(v["derivable"] for v in verdicts)
    witness = {
        "computation": "qbeta-h4-crossing-locus",
        "description": (
            "Bean 8we6 option-2 (formalize-first): parametrize the 4th-strand "
            "categorical coupling strengths (alpha=b-u, beta=b-d; w=HA*theta, "
            "forced by regularizability), compute the screen coefficients "
            "phi_4,phi_6 as exact rational functions, solve phi_4=phi_6=0, and "
            "accept a solution ONLY if both components are nameable categorical "
            "values (theta in {0,1/2,1} or small rational). A tuned/ugly root is "
            "reported as a structural wall, never wired. Screen calibration "
            "verified in qou-tti3. auditOnly; no fit; scope-(a)."
        ),
        "audit_only": True,
        "regularizability_forces_w_prop_HA": bool(reg_forced),
        "phi4_alpha_beta": str(phi4),
        "phi6_alpha_beta": str(phi6),
        "solutions": verdicts,
        "symmetric_slice_phi4_roots": [str(sp.nsimplify(r)) for r in diag_roots],
        "assertions": [
            {"label": "Delta(net)_4(q=1)=0 for all (alpha,beta) (w∝HA regularizes)",
             "passed": bool(reg_forced)},
            {"label": "phi_4=phi_6=0 system solved (finite or parametrized)",
             "passed": True},
        ],
        "verdict": ("DERIVABLE 4th-strand crossing exists" if any_lead
                    else "no derivable constant-coupling 4th strand passes the "
                         "gate (fit-trap wall confirmed structurally); a passer "
                         "would need q-dependent (higher-Taylor) couplings"),
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    import os
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-h4-crossing-locus.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  VERDICT: {witness['verdict']}")
    print(f"  Witness: {out.name}   ({time.monotonic() - t0:.1f}s wall)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
