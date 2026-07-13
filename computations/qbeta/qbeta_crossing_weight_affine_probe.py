#!/usr/bin/env python3
"""
Q_beta crossing-weight AFFINE narrowing -- the ladder-factor bar-parity split.

Sharpens KC18 (archimedean evaluation-map bar-decomposition). KC18 decomposed
the NUMERATOR of the evaluation map E(w) = h^2/2 - h*w into a bar-even identity
term h^2/2 and a bar-odd crossing/loop term -h*w. This probe analyses the object
where the c_k actually live: the LADDER FACTOR

    L(w) = E(w) / E(w0)         (w  = effective crossing weight,
                                 w0 = reference weight; w0=1 -> counit ratio)

with h = q - 1/q the Hecke parameter (bar-ODD, q -> 1/q sends h -> -h) and the
crossing weights w, w0 bar-EVEN (z = sqrt(q)/(1+q) is bar-even, KC13).

Established facts (exact symbolic; NO anchors, NO c_k value, NO fit, NO wiring):

  (A) E(w) is AFFINE in w:  dE/dw = -h  (constant in w). The evaluation map
      introduces NO nonlinearity in the crossing weight.
  (M) L(w) is a fractional-linear (Moebius, here affine) function of w:
      L(w) = (h^2/2 - h*w)/(h^2/2 - h*w0)  -- degree (1,0) in w.
  (O) The bar-ODD (decay/swing) part of L is EXACTLY
          L_odd = 2h*(w - w0) / (4*w0^2 - h^2)
      -- LINEAR in the crossing-weight departure (w - w0), times the FIXED
      bar-odd kernel  K(q) = 2h/(4*w0^2 - h^2).
  (E) The bar-EVEN (shadow/mass) part of L is
          L_even = (4*w*w0 - h^2) / (4*w0^2 - h^2)   (bar-even).
  (K) K(q) = 2h/(4*w0^2 - h^2) is a FIXED rational function of q (anchor-free):
      no anchor enters the evaluation map, so the observed c_3 anchor-swing
      (2.375%) cannot originate in the evaluation -- it must live entirely in
      the crossing weight w(q)'s fibre structure. Trace-side corroboration of
      the c_3-not-exact verdict.
  (C2) c_2 = -1 reference identity: with w0 = 1 (counit reference),
          L(w0=1) - 1 = -2*(w - 1)/(h - 2).

Net narrowing (scope-(a), structural): the entire c_k ladder's odd channel is
the image of the SINGLE scalar bar-even departure (w - w0) under the fixed
bar-odd kernel K(q). The keystone "derive the higher-order crossing weight
whose odd part gives the c_3 -> -2 shadow" reduces to: exhibit (w - w0) as a
function of the ladder variable; the evaluation contributes only K(q). No c_k
value is produced; nothing is wired (flip-flop guard, registry section 8).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def _repo_head_sha():
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
    ).strip()
    if not sha:
        raise RuntimeError("empty commitSha -- refusing to emit witness without provenance")
    return sha


def main():
    # h is bar-ODD (q -> 1/q sends h -> -h); w, w0 are bar-EVEN abstract weights.
    # The narrowing is purely algebraic in these parity symbols; the substrate q
    # never enters (the kernel K(q) is anchor-free), so no q symbol is needed.
    h, w, w0 = sp.symbols("h w w0")
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # bar involution on the abstract parity symbols: h -> -h, w -> w, w0 -> w0.
    def bar(e):
        return e.subs(h, -h)

    def even_part(e):
        return sp.simplify((e + bar(e)) / 2)

    def odd_part(e):
        return sp.simplify((e - bar(e)) / 2)

    def parity(e):
        e = sp.simplify(e)
        if sp.simplify(e - bar(e)) == 0:
            return "even"
        if sp.simplify(e + bar(e)) == 0:
            return "odd"
        return "neither"

    E = lambda ww: h**2 / 2 - h * ww  # noqa: E731

    # (A) affine in w.
    check("A_eval_affine_dEdw_eq_neg_h", sp.simplify(sp.diff(E(w), w) + h) == 0)
    check("A_eval_diff_linear", sp.simplify((E(w) - E(w0)) - (-h * (w - w0))) == 0)

    # (M) Moebius / affine in w: numerator deg_w = 1, denom deg_w = 0.
    L = sp.cancel(E(w) / E(w0))
    num, den = sp.fraction(L)
    check("M_ladder_numer_degw_1", sp.degree(sp.Poly(num, w)) == 1)
    check("M_ladder_denom_degw_0", sp.degree(sp.Poly(den, w)) == 0)

    # (O) odd part linear in (w - w0) with the fixed kernel.
    L_odd = odd_part(L)
    K = 2 * h / (4 * w0**2 - h**2)  # fixed bar-odd kernel
    check("O_odd_part_eq_kernel_times_departure",
          sp.simplify(L_odd - K * (w - w0)) == 0)
    check("O_odd_part_is_bar_odd", parity(L_odd) == "odd")
    check("O_kernel_is_bar_odd", parity(K) == "odd")
    # linear in the departure: second derivative wrt w vanishes.
    check("O_odd_part_linear_in_w", sp.simplify(sp.diff(L_odd, w, 2)) == 0)

    # (E) even part.
    L_even = even_part(L)
    check("E_even_part_form",
          sp.simplify(L_even - (4 * w * w0 - h**2) / (4 * w0**2 - h**2)) == 0)
    check("E_even_part_is_bar_even", parity(L_even) == "even")

    # (K) the kernel denominator is bar-EVEN and anchor-free (no q0 substituted).
    check("K_denominator_bar_even", parity(4 * w0**2 - h**2) == "even")

    # (C2) c_2 = -1 reference identity with w0 = 1.
    Lc = sp.simplify(L.subs(w0, 1))
    check("C2_counit_ref_identity",
          sp.simplify((Lc - 1) - (-2 * (w - 1) / (h - 2))) == 0)

    # (D) The crossing-weight departure w-1 (counit reference w0=1), as a
    # function of the ladder variable u. Invert the ladder L = 1 + c2 u^2 + ...:
    #   w = 1 - (h-2)/2 * (L - 1),  so w - 1 = -(h-2)/2 * sum_{k>=2} c_k u^k.
    # Here h = q - 1/q is expressed in the substrate q so the Q_beta
    # decay-numerator factor (q^2-2q-1) can be exhibited (anchor-free identity;
    # q is a free symbol, NOT the substrate value -- no anchor).
    qs = sp.symbols("qs", positive=True)
    hq = qs - 1 / qs
    us, c2s, c3s = sp.symbols("u c2 c3")
    # NON-CIRCULAR (Gemini review): do NOT hand-write the inversion. SOLVE the
    # actual ladder relation L = E(w)/E(1) for the crossing weight w, then
    # substitute the ladder expansion L = 1 + c2 u^2 + c3 u^3. The departure
    # w_dep is thus derived from the Moebius relation itself, and the checks
    # below verify it independently reproduces the theoretical prefactor.
    Ls, wv = sp.symbols("L wv")
    E_wv = hq**2 / 2 - hq * wv
    E_1 = hq**2 / 2 - hq * 1
    w_solved = sp.solve(Ls - E_wv / E_1, wv)[0]
    w_dep = sp.expand(w_solved.subs(Ls, 1 + c2s * us**2 + c3s * us**3)) - 1
    # leading [u^2] coefficient (with the derived c2 = -1) is the Q_beta
    # decay-numerator prefactor (q^2-2q-1)/(2q):
    check("D_departure_leading_is_qbeta_numerator_factor",
          sp.simplify(w_dep.coeff(us, 2).subs(c2s, -1) - (qs**2 - 2 * qs - 1) / (2 * qs)) == 0)
    # the fixed prefactor (h-2)/2 = (q^2-2q-1)/(2q) -- same factor as Q_beta:
    check("D_departure_prefactor_factor_identity",
          sp.simplify((hq - 2) / 2 - (qs**2 - 2 * qs - 1) / (2 * qs)) == 0)
    # the [u^3] coefficient is -(h-2)/2 * c3 -- the sole OPEN scalar (= c3):
    check("D_departure_u3_is_open_c3_times_prefactor",
          sp.simplify(w_dep.coeff(us, 3) - (-(hq - 2) / 2 * c3s)) == 0)

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CONFIRMED (scope-(a) structural narrowing): the Q_beta evaluation map "
        "E(w) = h^2/2 - h*w is AFFINE in the crossing weight w, so the ladder factor "
        "L(w) = E(w)/E(w0) is Moebius in w and its bar-ODD (decay) part is EXACTLY "
        "2h*(w - w0)/(4*w0^2 - h^2) -- LINEAR in the crossing-weight departure (w - w0) "
        "times the FIXED bar-odd kernel K(q) = 2h/(4*w0^2 - h^2). The evaluation map "
        "introduces neither nonlinearity nor anchor-dependence into the odd channel; "
        "the whole c_k odd-channel signature (incl. the c_3 -> -2 shadow) is the image "
        "of the single scalar bar-even departure (w - w0) under K(q). Since K(q) is a "
        "fixed rational function of q, the c_3 anchor-swing must live entirely in w(q). "
        "Sharpens KC18 (numerator split) to the ladder factor where the c_k live. "
        "NO c_k value; nothing wired."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "qbeta-crossing-weight-affine",
        "description": "Q_beta ladder-factor bar-parity split: the evaluation map is affine "
                       "in the crossing weight, so the ladder factor is Moebius and its "
                       "bar-odd part is linear in the crossing-weight departure (w - w0) times "
                       "a fixed anchor-free bar-odd kernel 2h/(4w0^2 - h^2). Sharpens KC18.",
        "audit_only": True,
        "tier": "structural-exact (symbolic bar-parity; no fit, no anchors)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "sympy",
        "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "eval_map": "E(w) = h^2/2 - h*w  (affine in w; dE/dw = -h)",
            "ladder_factor": "L(w) = E(w)/E(w0)  (Moebius in w)",
            "odd_part": "2h*(w - w0)/(4*w0^2 - h^2)  (linear in w - w0; bar-odd)",
            "even_part": "(4*w*w0 - h^2)/(4*w0^2 - h^2)  (bar-even)",
            "fixed_kernel": "K(q) = 2h/(4*w0^2 - h^2)  (anchor-free bar-odd rational fn of q)",
            "c2_reference_identity": "L(w0=1) - 1 = -2*(w - 1)/(h - 2)",
            "departure": "w - 1 = -(h-2)/2 * sum_{k>=2} c_k u^k  (counit reference w0=1)",
            "departure_leading": "[u^2] coeff = (q^2-2q-1)/(2q) using derived c2=-1 "
                                 "(the Q_beta decay-numerator factor)",
            "departure_open_scalar": "[u^3] coeff = -(q^2-2q-1)/(2q) * c3 -- sole open scalar, = c3",
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: crossing-weight affine narrowing (trace side)",
            "sharpens": "registry KC18 (docs/audits/2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)",
            "eval_map_lean": "QOU.Interactions.QBetaCounitTrace (trMNP = h^2/2 - h*z)",
            "new_lean": "QOU.QBeta.CrossingWeightAffine (this branch)",
            "c3_not_exact": "docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md",
            "z_bar_even": "QOU.QBeta.z_bar_invariant (KC13)",
            "flip_flop_guard": "registry section 8 -- no c_k wired",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "qbeta-crossing-weight-affine.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("=== Q_beta crossing-weight affine narrowing ===")
    print("VERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
