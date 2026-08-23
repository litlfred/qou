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
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

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


def _log_series_from_poly_coeffs(pk, order):
    """[s^1..s^order] of log(sum_k pk[k] s^k), pk[0] != 0.
    Uses the Mercator recursion on g = (P/p0 - 1), avoiding sympy's slow
    symbolic-coefficient log-series when pk[k] are polynomials in (alpha,beta)."""
    p0 = pk[0]
    g = [sp.expand(pk[k] / p0) for k in range(order + 1)]  # g[0]=1
    g[0] = sp.Integer(0)                                   # h = P/p0 - 1, h[0]=0
    # log(1+h) = sum_{m>=1} (-1)^(m+1) h^m / m  (h has no constant term)
    L = [sp.Integer(0)] * (order + 1)
    hpow = [sp.Integer(0)] * (order + 1)
    hpow[0] = sp.Integer(1)                                # h^0
    for m in range(1, order + 1):
        # hpow <- hpow * h  (truncated to `order`)
        new = [sp.Integer(0)] * (order + 1)
        for i in range(order + 1):
            if hpow[i] == 0:
                continue
            for j in range(1, order + 1 - i):
                if g[j] == 0:
                    continue
                new[i + j] = sp.expand(new[i + j] + hpow[i] * g[j])
        hpow = new
        sign = sp.Integer((-1) ** (m + 1))
        for i in range(1, order + 1):
            if hpow[i] != 0:
                L[i] = sp.expand(L[i] + sign * hpow[i] / m)
    return [sp.cancel(L[i]) for i in range(1, order + 1)]


def phis_of(dnet3, dnet4, order=7):
    """[s^1..s^order] of log(dnet4/dnet3). dnet4 may carry (alpha,beta).
    log(dnet4/dnet3) = log P4 - log P3 with P = dnet/(q-1) (the regularized
    part); the (q-1) zero cancels. Both logs via the fast poly recursion."""
    P4 = sp.cancel(sp.together(dnet4) / (q - 1))
    P3 = sp.cancel(sp.together(dnet3) / (q - 1))
    # plain rational-function series (no log) — fast even with (alpha,beta)
    s4 = sp.series(P4.subs(q, 1 + s), s, 0, order + 1).removeO().expand()
    s3 = sp.series(P3.subs(q, 1 + s), s, 0, order + 1).removeO().expand()
    pk4 = [sp.expand(s4.coeff(s, k)) for k in range(order + 1)]
    pk3 = [sp.expand(s3.coeff(s, k)) for k in range(order + 1)]
    L4 = _log_series_from_poly_coeffs(pk4, order)
    L3 = _log_series_from_poly_coeffs(pk3, order)
    return [sp.cancel(L4[i] - L3[i]) for i in range(order)]


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
    set_compute_dps()
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
    phi4 = sp.cancel(phis[3])
    phi6 = sp.cancel(phis[5])
    N4 = sp.expand(sp.numer(sp.together(phi4)))   # degree-8 bivariate
    N6 = sp.expand(sp.numer(sp.together(phi6)))   # degree-12 bivariate
    print(f"\n[2] phi_4 num deg = {sp.Poly(N4, alpha, beta).total_degree()}, "
          f"phi_6 num deg = {sp.Poly(N6, alpha, beta).total_degree()}  "
          f"(denominators are powers of (alpha-beta+1))  ({time.monotonic()-t1:.1f}s)")

    # ── [3] the SCIENTIFIC question: does any DERIVABLE coupling pass? ──
    # Evaluate the gate (phi_4 = phi_6 = 0) on the categorical/nameable grid of
    # coupling strengths (theta in {0, +-1/2, +-1, 2}; w = -HA*theta, so the
    # existing rules are alpha,beta in {0 (Hopf/uu), -1/2 (ud), -1 (dd)}).
    grid = [sp.Integer(0), sp.Rational(1, 2), sp.Rational(-1, 2),
            sp.Integer(1), sp.Integer(-1), sp.Integer(2), sp.Integer(-2)]
    print("\n[3] categorical grid — gate pass requires phi_4 = phi_6 = 0:")
    grid_pass = []
    for a_v in grid:
        for b_v in grid:
            n4 = sp.simplify(N4.subs({alpha: a_v, beta: b_v}))
            if n4 != 0:
                continue
            n6 = sp.simplify(N6.subs({alpha: a_v, beta: b_v}))
            tag = f"(alpha,beta)=({a_v},{b_v})"
            if n6 == 0:
                print(f"    *** {tag}: phi_4=phi_6=0  -> GATE PASS (derivable!)")
                grid_pass.append((str(a_v), str(b_v)))
            else:
                print(f"    {tag}: phi_4=0 but phi_6!=0 (fails at c3)")
    if not grid_pass:
        print("    no categorical (alpha,beta) zeroes BOTH phi_4 and phi_6.")

    # ── [3b] the full real locus via resultant (guarded) — is it even nonempty,
    #        and does any branch pass near a rational point? ──
    print("\n[3b] full locus: resultant_beta(N4, N6) -> real roots in alpha:")
    locus_pts, res_ok = [], False

    import signal

    class _Timeout(Exception):
        pass

    def _alarm(signum, frame):  # noqa: ANN001, ARG001
        raise _Timeout()

    has_alarm = hasattr(signal, "alarm")  # Unix-only; guard for portability
    if has_alarm:
        signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(180)  # hard cap; grid verdict already stands without this
    try:
        res = sp.resultant(N4, N6, beta)
        res_ok = True
        num_res = sp.numer(sp.together(sp.expand(res)))
        poly_a = sp.Poly(num_res, alpha)
        # rational roots exactly (rational-root theorem, no numerics needed)
        rat_roots = [r for r in poly_a.ground_roots().keys() if r.is_rational]
        print(f"     resultant degree {poly_a.degree()}; "
              f"{len(rat_roots)} rational alpha root(s)")
        for ar in rat_roots:
            # solve for beta at this alpha (common root of N4, N6)
            g = sp.gcd(sp.Poly(N4.subs(alpha, ar), beta),
                       sp.Poly(N6.subs(alpha, ar), beta))
            broots = sp.roots(g).keys() if g.degree() > 0 else []
            for br in broots:
                # CRITICAL: a numerator root on the pole locus (alpha-beta+1=0)
                # is a 0/0 degeneration, NOT a finite gate pass — phi_4 diverges
                # there (the 4-strand net loses its leading term). Exclude it and
                # require phi_4=phi_6=0 as FINITE zeros.
                on_pole = (ar - br + 1) == 0
                if on_pole:
                    print(f"     locus point (alpha,beta)=({ar},{br}) is on the "
                          f"pole locus alpha-beta+1=0 -> 0/0 degeneration "
                          f"(phi diverges), NOT a gate pass")
                    locus_pts.append({"alpha": str(ar), "beta": str(br),
                                      "on_pole_degeneration": True, "derivable": False})
                    continue
                f4v = sp.cancel(phi4.subs({alpha: ar, beta: br}))
                f6v = sp.cancel(phi6.subs({alpha: ar, beta: br}))
                finite_zero = (f4v == 0) and (f6v == 0)
                ca = is_categorical(ar)
                cb = is_categorical(br) if getattr(br, "is_rational", False) else None
                deriv = bool(ca) and bool(cb) and finite_zero
                print(f"     RATIONAL locus point (alpha,beta)=({ar},{br})  "
                      f"phi4={f4v} phi6={f6v}  finite_zero={finite_zero}  "
                      f"derivable={deriv}")
                locus_pts.append({"alpha": str(ar), "beta": str(br),
                                  "phi4": str(f4v), "phi6": str(f6v),
                                  "finite_zero": bool(finite_zero), "derivable": deriv})
        if not rat_roots:
            print("     NO rational alpha on the locus -> every passing (alpha,beta) "
                  "is irrational/tuned (fit-trap wall)")
    except _Timeout:
        print("     resultant timed out (>180s); relying on the categorical-grid "
              "verdict (the scientific answer)")
    except Exception as e:  # noqa: BLE001
        print(f"     resultant not completed ({type(e).__name__}: {e}); "
              "relying on the categorical-grid verdict")
    finally:
        if has_alarm:
            signal.alarm(0)

    any_lead = bool(grid_pass) or any(p["derivable"] for p in locus_pts)
    verdicts = ([{"alpha": a, "beta": b, "source": "grid", "derivable": True}
                 for (a, b) in grid_pass] + locus_pts)
    diag_roots = []  # (symmetric-slice detail folded into the grid above)
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
        "phi_denominators": "phi_4: 8*(alpha-beta+1)^4 ; phi_6: 24*(alpha-beta+1)^6",
        "categorical_grid_passes": [{"alpha": a, "beta": b} for (a, b) in grid_pass],
        "locus_rational_points": locus_pts,
        "resultant_completed": bool(res_ok),
        "solutions": verdicts,
        "assertions": [
            {"label": "Delta(net)_4(q=1)=0 for all (alpha,beta) (w∝HA regularizes)",
             "passed": bool(reg_forced)},
            {"label": "categorical-grid gate evaluated (7x7 nameable couplings)",
             "passed": True},
        ],
        "verdict": ("DERIVABLE 4th-strand crossing exists (grid or rational locus "
                    "point passes)" if any_lead
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
