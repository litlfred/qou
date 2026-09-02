"""What replaces the cosine under convention D: the bar action on the traced
volume is MULTIPLICATIVE, not an affine reflection — so the resummation cannot
be additive.

Bean `qou-cds1`, Step 7. Step 4 established that the cos-resummation's stated
justification ("the resummation must be EVEN in alpha", from `alpha -> -alpha`)
fails under D. Step 6 established that the phase formula itself is generic in z.
This derives WHY the evenness fails, from the group action rather than from the
symptom — and therefore what class the D replacement must lie in.

## The phase is a re-centred traced volume

With the Markov trace `Vhat = z*h + 1` on the pp transfer matrix
(beta-decay-transfer-matrix-proof.md), verified for BOTH conventions:

    alpha = (z - 1)h/2 = (Vhat - 1 - h)/2                    EXACT identity

So the phase is the traced volume, re-centred on 1 and shifted by h.

## The bar involution acts COMPLETELY DIFFERENTLY in the two conventions

Measured, exact:

    C:  bar(Vhat) = 2 - Vhat        an AFFINE REFLECTION, fixed point 1
    D:  bar(Vhat) = Vhat / q^2      a MULTIPLICATIVE EIGENVECTOR, weight -2

These are different group actions, not different values of one action. That is
the root of everything Step 4 observed as a symptom.

Under C, bar fixes the centre 1 and negates h, so `Vhat - 1 - h` is bar-ODD and
alpha inherits `alpha -> -alpha`. Under D, bar does not fix 1 at all — it
scales — so nothing about the centring survives:

    C:  bar(alpha) + alpha = 0
    D:  bar(alpha) + alpha = (q-1)^2 (q+1)^2 / (2 q^2)   != 0

## No constant re-centring can repair it

Solving for the offset `c` that would make `Vhat - c - h` bar-odd under D:

    c = (q^4 + 1) / (2 q^2)   =   (Vhat + bar(Vhat)) / 2

i.e. the bar-MIDPOINT of Vhat — which depends on q. A q-dependent `c` is not a
re-centring of the phase; it is a different object. So the affine route is
closed, independently confirming the bar-weight argument of Step 2 (which
reached the same conclusion from weights rather than from the action).

## THE RESULT — why `cos` is C-specific, and what the D form must respect

`cos(alpha) = (e^{i alpha} + e^{-i alpha})/2` is precisely the ADDITIVE
symmetrisation. Measured on the traced volume:

    C:  bar(Vhat) + Vhat = 2                       CONSTANT in q
    D:  bar(Vhat) + Vhat = (q^4 + 1)/q^2           NOT constant
        bar(Vhat) * Vhat = (q^4+1)^2/(q^2 (q^2+1)^2)   NOT constant

Under C the ADDITIVE bar-symmetrisation of the traced volume is a constant.
That is the precise sense in which the additive/cosine structure is
convention-C's: the bar action is affine, so additive symmetrisation is the
invariant, and the cosine is its trigonometric realisation.

Under D the bar action is multiplicative (scaling by q^-2), so an additive
symmetrisation is not what bar preserves. **The D resummation must respect a
MULTIPLICATIVE bar action, and no additive form — cosine included — can be the
minimal invariant.**

## What this does NOT establish

It does not hand over the replacement form. It establishes the CLASS the
replacement must lie in (multiplicative in the bar action) and closes the
additive route, from the group action rather than by search. Naming the
specific form still requires the D-frame M_beta spectrum on V_(2,1), which is
not derived here.

No c_k is proposed, extracted, or wired; c_3 ~ -974 remains a sensitivity
measurement per qou-cds1.

Run:  python3 -u computations/qbeta/qbeta_d_frame_bar_action_on_traced_volume.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
COMP = REPO / "computations"
for _p in (str(COMP), str(COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from q_parameter import q_at  # noqa: E402 — proton pin
from witness_base import WitnessBuilder  # noqa: E402

q = sp.Symbol("q", positive=True)
h = q - 1 / q


def bar(e):
    return sp.simplify(sp.together(sp.expand(e).subs(q, 1 / q)))


def main() -> int:
    z_C = sp.sqrt(q) / (q + 1)
    z_D = q**3 / (q**2 + 1)
    out_rows = {}

    for nm, zv in (("C", z_C), ("D", z_D)):
        V = sp.simplify(zv * h + 1)
        bV = bar(V)
        a = (zv - 1) * h / 2
        out_rows[nm] = {
            "Vhat": str(V),
            "bar_Vhat": str(bV),
            "alpha_equals_recentred_Vhat": bool(
                sp.simplify(a - (V - 1 - h) / 2) == 0),
            "bar_is_affine_reflection_2_minus_V": bool(
                sp.simplify(bV - (2 - V)) == 0),
            "bar_is_multiplicative_weight_minus2": bool(
                sp.simplify(bV - V / q**2) == 0),
            "bar_alpha_plus_alpha": str(sp.factor(sp.simplify(bar(a) + a))),
            "alpha_is_bar_odd": bool(sp.simplify(bar(a) + a) == 0),
            "additive_symmetrisation": str(sp.factor(sp.simplify(bV + V))),
            "additive_is_constant": bool(
                sp.simplify(sp.diff(sp.simplify(bV + V), q)) == 0),
            "multiplicative_symmetrisation": str(sp.factor(sp.simplify(bV * V))),
            "multiplicative_is_constant": bool(
                sp.simplify(sp.diff(sp.simplify(bV * V), q)) == 0),
        }

    # Which q-power makes Vhat bar-INVARIANT? An affine reflection has a fixed
    # POINT; a multiplicative action has a WEIGHT, so the two answer differently.
    inv = {}
    for nm, zv in (("C", z_C), ("D", z_D)):
        V = zv * h + 1
        powers = [k for k in (-2, -1, sp.Rational(-1, 2), 0,
                              sp.Rational(1, 2), 1, 2)
                  if sp.simplify(bar(V * q**k) - V * q**k) == 0]
        inv[nm] = {"q_powers_giving_invariance": [str(k) for k in powers]}
    Y = sp.simplify((z_D * h + 1) / q)          # the D invariant
    two_q = q + 1 / q                            # [2]_q
    closed = sp.simplify(Y - (two_q + h**2 * z_D / q**2) / 2)
    inv["D"]["invariant"] = str(sp.factor(Y))
    inv["D"]["invariant_is_constant"] = bool(sp.simplify(sp.diff(Y, q)) == 0)
    inv["D"]["closed_form"] = "Vhat_D/q = ([2]_q + h^2 z_D/q^2)/2,  [2]_q = q + 1/q"
    inv["D"]["closed_form_verified"] = bool(closed == 0)
    VC = z_C * h + 1
    inv["C"]["invariant"] = str(sp.simplify((VC + bar(VC)) / 2))
    inv["C"]["invariant_is_constant"] = bool(
        sp.simplify(sp.diff(sp.simplify((VC + bar(VC)) / 2), q)) == 0)
    inv["C"]["note"] = ("an affine reflection has a FIXED POINT, not a weight, "
                        "so no q-power works; the invariant is the centre 1")

    # the offset that WOULD restore bar-oddness under D
    c = sp.Symbol("c")
    V_D = z_D * h + 1
    c_sol = sp.solve(sp.simplify(bar(V_D - c - h) + (V_D - c - h)), c)
    midpoint = sp.simplify((V_D + bar(V_D)) / 2)
    c_is_midpoint = bool(c_sol and sp.simplify(c_sol[0] - midpoint) == 0)

    q0 = q_at(40)
    payload = {
        "description": (
            "The bar involution acts on the Q_beta traced volume as an AFFINE "
            "REFLECTION under convention C (fixed point 1) and as a "
            "MULTIPLICATIVE eigenvector of weight -2 under D. That is the root "
            "cause of the cos-resummation's failure under D, and it says the D "
            "replacement must respect a multiplicative action."
        ),
        "phase_is_recentred_traced_volume": "alpha = (z-1)h/2 = (Vhat - 1 - h)/2",
        "by_convention": out_rows,
        "no_constant_recentring_repairs_D": {
            "offset_c_solving_bar_oddness": [str(s) for s in c_sol],
            "equals_bar_midpoint_of_Vhat": c_is_midpoint,
            "why_this_is_not_a_repair": (
                "c depends on q, so it is not a re-centring of the phase but a "
                "different object. Independently confirms Step 2's bar-weight "
                "argument, reached there from weights rather than the action."
            ),
        },
        "result": (
            "cos(alpha) = (e^{i alpha} + e^{-i alpha})/2 is the ADDITIVE "
            "symmetrisation. Under C the additive bar-symmetrisation of the "
            "traced volume is CONSTANT (= 2) — the bar action is affine, so "
            "additive symmetrisation is the invariant and the cosine is its "
            "trigonometric realisation. Under D the action is multiplicative, "
            "so no additive form, cosine included, can be the minimal invariant."
        ),
        "does_not_establish": (
            "the replacement FORM. This fixes the CLASS it must lie in "
            "(multiplicative in the bar action) and closes the additive route, "
            "from the group action rather than by search. Naming the form "
            "still needs the D-frame M_beta spectrum on V_(2,1)."
        ),
        "bar_invariant_of_the_traced_volume": inv,
        "the_sharpest_statement": (
            "cos works under C because bar has a FIXED CENTRE (the constant 1) "
            "to resum around. Under D the bar-invariant is Vhat/q, which is NOT "
            "constant — there is no fixed centre, so no additive resummation "
            "has anything to be centred on."
        ),
        "no_ck_wired": True,
        "context": {"beans": ["qou-cds1"],
                    "prior": ["Step 4 (cos justification fails)",
                              "Step 6 (phase formula is generic in z)"]},
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = WitnessBuilder.wrap_legacy(
        "qbeta-d-frame-bar-action-on-traced-volume", payload,
        script_path=__file__, engine="python+sympy (exact in q)",
    ).save()

    print("=== How bar acts on the traced volume Vhat = z*h + 1 ===")
    for nm in ("C", "D"):
        r = out_rows[nm]
        kind = ("AFFINE REFLECTION 2-V (fixed point 1)"
                if r["bar_is_affine_reflection_2_minus_V"]
                else "MULTIPLICATIVE V/q^2 (weight -2)")
        print(f"  {nm}: bar(Vhat) is an {kind}")
        print(f"      alpha = (Vhat-1-h)/2 : {r['alpha_equals_recentred_Vhat']}"
              f"    alpha bar-odd: {r['alpha_is_bar_odd']}")
        print(f"      bar(V)+V = {r['additive_symmetrisation']:28s} "
              f"constant: {r['additive_is_constant']}")
        print(f"      bar(V)*V = {r['multiplicative_symmetrisation']:28s} "
              f"constant: {r['multiplicative_is_constant']}")
    print()
    print(f"  D repair attempt: offset c = {[str(s) for s in c_sol]}")
    print(f"    equals the bar-MIDPOINT of Vhat : {c_is_midpoint}")
    print(f"    q-dependent => not a re-centring; the affine route is CLOSED")
    print()
    print("  RESULT: cos is the ADDITIVE symmetrisation. Under C the additive")
    print("  bar-symmetrisation of Vhat is CONSTANT (=2) — bar acts affinely.")
    print("  Under D bar acts MULTIPLICATIVELY, so no additive form (cosine")
    print("  included) can be the minimal invariant.")
    print()
    print("  === which q-power makes Vhat bar-INVARIANT? ===")
    print(f"    C: {inv['C']['q_powers_giving_invariance'] or 'NONE'}"
          f"   (affine reflection -> fixed point, not weight)")
    print(f"       invariant = {inv['C']['invariant']}   "
          f"constant: {inv['C']['invariant_is_constant']}")
    print(f"    D: {inv['D']['q_powers_giving_invariance']}"
          f"   -> invariant = {inv['D']['invariant']}")
    print(f"       constant: {inv['D']['invariant_is_constant']}")
    print(f"       closed form {inv['D']['closed_form']}")
    print(f"       verified: {inv['D']['closed_form_verified']}")
    print()
    print("  SHARPEST STATEMENT: cos works under C because bar has a FIXED")
    print("  CENTRE (the constant 1) to resum around. Under D the invariant is")
    print("  Vhat/q, NOT constant — no fixed centre, so no additive resummation")
    print("  has anything to be centred on.")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
