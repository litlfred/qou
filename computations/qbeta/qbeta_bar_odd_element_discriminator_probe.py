#!/usr/bin/env python3
"""Bar-oddness discriminates the two candidate Q_beta ELEMENTS — Delta_S carries
it on the WHOLE admissible trace space, Delta_L on none of it but the zero trace.

WHY THIS IS A PHYSICS TEST AND NOT AN AESTHETIC ONE. The corpus establishes,
measured rather than posited, that the bar involution q -> 1/q IS proton<->neutron
conjugation: `L(Z,N;q) - L(N,Z;1/q) = delta(q)` with delta independent of (Z,N),
verified over 11 nuclei at five values of q, and at bond level `p <-> n` under bar
is exactly `z <-> zbar` (docs/audits/2026-08-19-bar-involution-is-isospin-
conjugation.md, bean qou-e58e).

`Q_beta` is the neutron-minus-proton decay Q-value and its element is
`Delta = B_n - B_p`, a p<->n DIFFERENCE. Under a conjugation that swaps p and n, a
difference reverses sign. So the element's trace SHOULD be bar-ODD:

    bar(N) = -N,   N(z) = tr_M(Delta)(z)

That is the criterion tested here. It is motivated by an established corpus
result, it involves NO anchor and NO experimental input, and it therefore cannot
be a fit.

WHAT IS MEASURED

Two candidate elements, from the fork the decision document leaves open
(qou-avt5, qou-99qc):

    Delta_S  the Groebner-Shirshov NORMAL FORM difference NF(n) - NF(p)
             tr_M affine in z:      N_S = h^2/2 - h z
    Delta_L  the eleven-crossing raw WORD difference beta_n - beta_p
             tr_M quadratic in z:   N_L = -(q-1)(q+1)(q^4 z^2 + 2q^3 z + 2q^2
                                          - 2q z + z^2)/(4q^3)

both taken from committed corpus artifacts, not rebuilt here.

    Delta_S:  bar(N) = -N  <=>  bar(z) = z - h        ONE branch
              satisfied by  z = q (augmentation)      ADMISSIBLE   ✓
                            z_D = q^3/(q^2+1)         ADMISSIBLE   ✓
              failed by     z = 1 (published)         inadmissible ✗
                            z_C = sqrt(q)/(q+1)       excised      ✗

    Delta_L:  bar(N) = -N  <=>  bar(z) = -z  OR  bar(z) = (q^4 z + 2q^3 - 2q + z)/(q^4+1)
              satisfied by  NONE of the four, the ADMISSIBLE PAIR INCLUDED

AND THE WHOLE SPAN, WHICH IS THE STATEMENT THAT MATTERS. Testing only the two
Markov points UNDER-CLAIMS: the decision document records (section 2, fact 3) that
the admissible TRACES form a 2-DIMENSIONAL space which those two points span. So
the real question is whether ANY combination is bar-odd. Measured:

    Delta_S   bar(A) + A = 0  AND  bar(B) + B = 0
              => EVERY admissible trace on Delta_S is bar-odd

    Delta_L   bar(A) + A = -(q-1)^2 (q+1)^2 (q^2+1)^3 / (4q^5)
              bar(B) + B = -(q-1)^2 (q+1)^2 (q^2+1)(q^4+1) / (4q^5)
              ratio = (q^2+1)^2/(q^4+1), which is q-DEPENDENT, so the two defects
              are NOT proportional over Q and a*dA + b*dB = 0 forces a = b = 0
              => ONLY THE ZERO TRACE on Delta_L is bar-odd

So under the isospin reading, `Delta_S` carries bar-oddness on the entire
admissible trace space and `Delta_L` carries it nowhere but at zero. That is a
structural preference for `Delta_S` in a question the decision document records as
open, and it is reached without touching a number.

🛑 SCOPE — what the span result does and does not settle.

  ESTABLISHED, and it is a complete statement over the admissible span with
  CONSTANT coefficients: no nonzero rational combination of the two canonical
  admissible Markov traces is bar-odd on Delta_L, while every one is on Delta_S.
  That is stronger than the four-point test and is not a sampling argument -- it
  follows from the two bar-odd defects being non-proportional over Q.

  NOT ESTABLISHED, and both matter:

  * COEFFICIENTS IN Q(q) were not tested. If the span is taken over Q(q) rather
    than Q, `bar` acts on the coefficients too and the condition becomes a
    functional equation in two unknowns, generically solvable. Note that scaling
    a trace by f(q) rescales Q_beta itself, so it is a different physical claim,
    not merely a wider search -- but it is untested either way.
  * NON-ADMISSIBLE z. Delta_L's second branch is INVOLUTION-CONSISTENT
    (`Bbar(B(z)) - z = 0` identically), so some z outside the admissible set may
    make it bar-odd. Irrelevant to the physics -- an inadmissible functional is
    excluded on other grounds -- but it means "Delta_L can never be bar-odd" is
    NOT what was shown.

  So: within the admissible span over Q this is a genuine exclusion of Delta_L;
  outside it, it is untested. The first branch `bar(z) = -z` is vacuous for a
  positive Markov parameter throughout.

CALIBRATION, AND A DEFECT FOUND BY IT. The Delta_L closed form reproduces the
committed fork-pricing witness's own Q_pred to 8.5e-51 at 60 dps — byte-exact.
It does NOT reproduce that witness's err_pct to 1e-12, and the reason is not the
algebra: `codata_constants.Q_BETA_MEV` is carried at EIGHT significant figures
(0.78233341) while the witness used 0.7823334093099085, a relative difference of
8.8e-10. A truncated reference in a corpus that computes at 60 dps. Recorded, not
fixed here.

Ref: docs/audits/2026-08-19-bar-involution-is-isospin-conjugation.md (qou-e58e)
Ref: docs/audits/2026-09-05-qbeta-functional-decision-options.md (qou-99qc)
Ref: docs/audits/2026-09-07-bar-parity-separates-the-admissible-qbeta-functionals.md
Ref: computations/qbeta/qbeta-delta-element-fork-pricing.witness.json (Delta_L tr_M)
Ref: beans qou-99qc, qou-avt5, qou-e58e, qou-37j2
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("computations", "computations/qbeta", "tools/qou-substrate/python"):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import _path_bridge  # noqa: F401, E402
from mpmath import mp, mpf  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

q = sp.symbols("q", positive=True)
z, zb = sp.symbols("z zb")
h = q - 1 / q
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(1, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

#: tr_M of each candidate element, as a function of the Markov parameter.
#: Delta_S from qbeta_published_form_is_the_inadmissible_z1_probe (affine);
#: Delta_L from qbeta-delta-element-fork-pricing.witness.json (quadratic).
N_S = h**2 / 2 - h * z
N_L = -(q - 1) * (q + 1) * (q**4 * z**2 + 2 * q**3 * z + 2 * q**2 - 2 * q * z + z**2) / (4 * q**3)

FUNCTIONALS = {
    "z=1  (published)":      (sp.Integer(1),         False),
    "z=q  (augmentation)":   (q,                     True),
    "z_D  (Markov, conv D)": (q**3 / (q**2 + 1),     True),
    "z_C  (excised conv C)": (sp.sqrt(q) / (q + 1),  False),
}


def bar_of(expr):
    """bar acting on an expression in q alone."""
    return sp.simplify(expr.subs(q, 1 / q))


def bar_odd_branches(N):
    """Solve bar(N) = -N for bar(z); returns the required bar(z) branches."""
    Nbar = sp.simplify(N.subs({q: 1 / q, z: zb}))
    return [sp.simplify(s) for s in sp.solve(sp.Eq(sp.simplify(Nbar + N), 0), zb)]


def main() -> int:
    print("=" * 78)
    print(" Bar-oddness discriminates the two Q_beta elements")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-bar-odd-element-discriminator", engine="sympy+mpmath")
    wb.set_description(
        "The corpus establishes (qou-e58e, 11 nuclei, five q) that bar: q -> 1/q IS "
        "proton<->neutron conjugation, and at bond level p<->n is exactly z<->zbar. "
        "Q_beta's element Delta = B_n - B_p is a p<->n DIFFERENCE, so under that "
        "conjugation it should be bar-ODD: bar(tr_M(Delta)) = -tr_M(Delta). Tested on "
        "the two candidate elements the fork leaves open. Delta_S (normal-form "
        "difference, tr_M AFFINE in z): bar-odd iff bar(z) = z - h, ONE branch, "
        "satisfied by EXACTLY the two admissible functionals (z=q augmentation, "
        "z_D = q^3/(q^2+1)) and by neither z=1 (published) nor z_C (excised C). "
        "Delta_L (eleven-crossing word difference, tr_M QUADRATIC in z): two branches, "
        "satisfied by NONE of the four, the admissible pair included. So under the "
        "isospin reading Delta_S + admissible functional is bar-odd and Delta_L + "
        "admissible functional is not. AND THE WHOLE SPAN, which is the statement that "
        "matters: the admissible TRACES are 2-dimensional and the two Markov points "
        "span them, so testing only those points under-claims. Measured, on Delta_S "
        "BOTH basis traces have vanishing bar-odd defect => EVERY admissible trace is "
        "bar-odd; on Delta_L neither does and the two defects are NOT proportional over "
        "Q (ratio (q^2+1)^2/(q^4+1) is q-dependent) => a*dA + b*dB = 0 forces a = b = 0, "
        "so ONLY THE ZERO TRACE is bar-odd. That is a genuine exclusion of Delta_L "
        "WITHIN the admissible span over Q, not a sampling argument. NOT established: "
        "coefficients in Q(q) (bar acts on them too; scaling by f(q) rescales Q_beta, a "
        "different physical claim) and non-admissible z (Delta_L's second branch is "
        "involution-consistent, so some inadmissible z may work). Reached with NO anchor "
        "and NO experimental input. Nothing wired, no functional adopted, no element "
        "declared canonical."
    )
    wb.set_content_block("rem:qbeta-functional-admissibility")

    results = {}

    # ── the two elements against the criterion ──────────────────────────
    for label, N, key in (("Delta_S (normal form, affine in z)", N_S, "Delta_S"),
                          ("Delta_L (11-crossing word, quadratic in z)", N_L, "Delta_L")):
        deg = sp.Poly(sp.together(N).as_numer_denom()[0], z).degree()
        branches = bar_odd_branches(N)
        print(f"\n=== {label} ===")
        print(f"  degree in z = {deg}")
        print(f"  bar(N) = -N  <=>  bar(z) in {[str(sp.factor(b)) for b in branches]}")
        rows = {}
        for name, (zv, admissible) in FUNCTIONALS.items():
            true_bar = bar_of(zv)
            odd = any(sp.simplify(sp.simplify(b.subs(z, zv)) - true_bar) == 0 for b in branches)
            print(f"    {name:24} bar(z) = {str(sp.factor(true_bar)):24} "
                  f"{'BAR-ODD' if odd else 'not bar-odd':12} admissible={admissible}")
            rows[name] = {"z": str(sp.factor(zv)), "bar_z": str(sp.factor(true_bar)),
                          "bar_odd": bool(odd), "admissible_under_D": bool(admissible)}
            if key == "Delta_S":
                wb.add_assertion(
                    f"Delta_S_bar_odd_iff_admissible__{name.split()[0].replace('=', '_')}",
                    computed=("1" if odd == admissible else "0"), expected="1",
                    tolerance="0.5",
                    source=f"{name}: bar-odd={odd}, admissible={admissible} — they agree")
            else:
                wb.add_assertion(
                    f"Delta_L_not_bar_odd__{name.split()[0].replace('=', '_')}",
                    computed=("1" if not odd else "0"), expected="1", tolerance="0.5",
                    source=f"{name}: bar-odd={odd} on Delta_L (expected False for all four)")
        results[key] = {"degree_in_z": deg,
                        "bar_odd_branches": [str(sp.factor(b)) for b in branches],
                        "functionals": rows}

    # ── the scope limit, proved rather than conceded ─────────────────────
    print("\n=== SCOPE: is Delta_L EXCLUDED? No. ===")
    branches_L = bar_odd_branches(N_L)
    consistent = []
    for i, B in enumerate(branches_L):
        Bbar = sp.simplify(B.subs(q, 1 / q))
        resid = sp.simplify(sp.factor(Bbar.subs(z, B) - z))
        consistent.append(resid == 0)
        print(f"    branch {i+1}: {sp.factor(B)}")
        print(f"        involution check Bbar(B(z)) - z = {resid}  "
              f"=> {'CONSISTENT (solutions may exist)' if resid == 0 else 'inconsistent'}")
    neg_branch = any(sp.simplify(b + z) == 0 for b in branches_L)
    print(f"    branch bar(z) = -z present? {neg_branch}  "
          f"— vacuous for a positive Markov parameter")
    wb.add_assertion("delta_L_second_branch_is_involution_consistent",
                     computed=("1" if any(consistent) else "0"), expected="1",
                     tolerance="0.5",
                     source="Bbar(B(z)) - z vanishes identically on at least one branch, so "
                            "the functional equation is not self-contradictory and Delta_L "
                            "is NOT excluded — this is scope-(a), not scope-(b)")

    # ── the WHOLE admissible trace space, not just the two points ───────
    #
    # The decision document records (section 2, fact 3) that the admissible TRACES
    # form a 2-DIMENSIONAL space which the two Markov points span. Testing only
    # those two points therefore under-claims: the honest question is whether ANY
    # combination is bar-odd. Answering it strengthens the result substantially.
    print("\n=== The whole admissible span (2-dim, spanned by the two Markov points) ===")
    span = {}
    for key, N in (("Delta_S", N_S), ("Delta_L", N_L)):
        A = sp.simplify(N.subs(z, q))                    # augmentation
        B = sp.simplify(N.subs(z, q**3 / (q**2 + 1)))    # Markov at z_D
        dA = sp.simplify(sp.factor(bar_of(A) + A))       # bar-odd defect of each
        dB = sp.simplify(sp.factor(bar_of(B) + B))
        both_odd = (dA == 0 and dB == 0)
        if both_odd:
            verdict = "EVERY combination is bar-odd"
            ratio_str, ratio_const = "0/0 (both defects vanish)", None
        else:
            ratio = sp.simplify(sp.cancel(dA / dB)) if dB != 0 else None
            ratio_const = (ratio is not None
                           and sp.simplify(sp.diff(ratio, q)) == 0)
            ratio_str = str(sp.factor(ratio)) if ratio is not None else "dB = 0"
            verdict = ("some nonzero constant combination is bar-odd" if ratio_const
                       else "ONLY the zero trace is bar-odd")
        print(f"    {key}:  bar(A)+A = {sp.factor(dA)}")
        print(f"    {' ' * len(key)}   bar(B)+B = {sp.factor(dB)}")
        print(f"    {' ' * len(key)}   defect ratio = {ratio_str}   -> {verdict}")
        span[key] = {"defect_augmentation": str(sp.factor(dA)),
                     "defect_z_D": str(sp.factor(dB)),
                     "defects_proportional_over_Q": bool(ratio_const) if ratio_const is not None else True,
                     "every_combination_bar_odd": bool(both_odd),
                     "verdict": verdict}
    wb.add_assertion("Delta_S_whole_admissible_span_is_bar_odd",
                     computed=("1" if span["Delta_S"]["every_combination_bar_odd"] else "0"),
                     expected="1", tolerance="0.5",
                     source="both basis traces have vanishing bar-odd defect, so every "
                            "admissible combination on Delta_S is bar-odd")
    wb.add_assertion("Delta_L_no_nonzero_constant_combination_is_bar_odd",
                     computed=("1" if not span["Delta_L"]["defects_proportional_over_Q"] else "0"),
                     expected="1", tolerance="0.5",
                     source="the two bar-odd defects on Delta_L are NOT proportional over Q "
                            "(ratio (q^2+1)^2/(q^4+1) is q-dependent), so a*dA + b*dB = 0 "
                            "forces a = b = 0 for constant a, b — only the zero trace")
    wb.add_data("admissible_span", span)

    # ── calibration against the committed fork-pricing witness ──────────
    print("\n=== CALIBRATION against qbeta-delta-element-fork-pricing.witness.json ===")
    wpath = _ROOT / "computations/qbeta/qbeta-delta-element-fork-pricing.witness.json"
    W = json.loads(wpath.read_text())["data"]
    Q0 = Q_MP
    f = sp.lambdify(q, sp.Abs(sp.simplify(N_L.subs(z, sp.Integer(1)) * E0)), "mpmath")
    mine = M_E_MEV * f(Q0)
    theirs = mpf(W["Qbeta_long_net"])
    rel = abs(mine - theirs) / theirs
    print(f"    Q_pred(Delta_L, z=1)  mine = {mp.nstr(mine, 30)}")
    print(f"                       witness = {mp.nstr(theirs, 30)}")
    print(f"                      rel diff = {mp.nstr(rel, 5)}   (algebra is byte-exact)")
    wb.add_assertion("delta_L_closed_form_reproduces_the_committed_witness",
                     computed=("1" if rel < mpf("1e-40") else "0"), expected="1",
                     tolerance="0.5",
                     source=f"|mine - witness|/witness = {mp.nstr(rel, 5)} at 60 dps")

    implied = theirs / (1 + mpf(W["err_long_net"]))
    ref_rel = abs(implied - Q_BETA_MEV) / Q_BETA_MEV
    print(f"\n    Q_beta reference implied by the witness = {mp.nstr(implied, 20)}")
    print(f"    codata_constants.Q_BETA_MEV today       = {mp.nstr(Q_BETA_MEV, 20)}")
    print(f"    rel diff = {mp.nstr(ref_rel, 5)}   <- an 8-significant-figure REFERENCE")
    wb.add_assertion("q_beta_reference_is_truncated_to_eight_figures",
                     computed=("1" if mpf("1e-11") < ref_rel < mpf("1e-8") else "0"),
                     expected="1", tolerance="0.5",
                     source=f"codata_constants.Q_BETA_MEV = {Q_BETA_MEV} differs from the "
                            f"witness's own reference by {mp.nstr(ref_rel, 5)} — a truncated "
                            f"reference in a corpus that computes at 60 dps. Recorded, not fixed.")

    wb.add_data("elements", results)
    wb.add_data("calibration", {
        "delta_L_Q_pred_mine": fmt(mine, 30),
        "delta_L_Q_pred_witness": W["Qbeta_long_net"],
        "rel_diff": fmt(rel, 10),
        "q_beta_reference_implied_by_witness": fmt(implied, 20),
        "q_beta_reference_in_codata_constants": fmt(Q_BETA_MEV, 20),
        "reference_rel_diff": fmt(ref_rel, 10),
    })
    wb.add_data("scope", {
        "tier": "exclusion within the admissible span over Q; scope-(a) outside it",
        "established": ("Delta_S is bar-odd under EXACTLY the two admissible functionals "
                        "and, more strongly, on the WHOLE admissible trace span; Delta_L is "
                        "bar-odd under none of the four and, on the span with constant "
                        "coefficients, ONLY at the zero trace (the two bar-odd defects are "
                        "non-proportional over Q). A genuine exclusion within the span."),
        "NOT_established": ("(i) coefficients in Q(q) — bar acts on them too, and scaling a "
                            "trace by f(q) rescales Q_beta, so it is a different physical "
                            "claim, untested either way; (ii) that Delta_L can never be "
                            "bar-odd for ANY z — its second branch is involution-consistent, "
                            "so some INADMISSIBLE z may work, which is irrelevant to the "
                            "physics but means the universal claim was not shown"),
        "premise": ("bar is p<->n conjugation, measured in qou-e58e over 11 nuclei; a p<->n "
                    "DIFFERENCE should therefore be bar-odd. If that reading is wrong, the "
                    "criterion loses its motivation and this becomes an observation about "
                    "two rational functions."),
    })
    wb.save()
    print("\n  RESULT: on the WHOLE admissible trace span, Delta_S is bar-odd everywhere "
          "and\n          Delta_L only at zero. Exclusion within the span over Q; "
          "Q(q) coefficients\n          and non-admissible z are untested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
