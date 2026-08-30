#!/usr/bin/env python3
"""The Q_beta bridge phase alpha = (z-1)h/2 is GENERIC in z — so the D-frame
re-derivation is narrower than the ladder guard's wording suggests.

Bean `qou-cds1`, continuing Steps 2-5 (PRs #6110, #6149). Step 4 established
that under convention D the COS-RESUMMATION loses its stated justification
(alpha is not bar-odd, so the "must be even in alpha" argument fails). Step 5
established that the carrier block V_(2,1) survives D, so the re-derivation is
worth doing. This asks the next question: how much of the construction is
actually convention-dependent?

## Where z enters — measured, not assumed

`beta-decay-transfer-matrix-proof.md` gives the transfer matrices explicitly:

    T_pp = [[h, 1], [1,  0]]      T_nn = [[0, 1], [1, -h]]
    T_mix = [[h/2, 1], [1, -h/2]]     Delta_beta = (h/2) . I

**All four are z-FREE** — built from `h = q - 1/q` alone. So M_beta as an
OPERATOR is convention-independent. `z` enters in exactly two downstream
places, both in the trace/normalisation rather than the operator:

    Vhat_i = z . M_11 + M_21          the Markov trace on a 2x2 (z-linear)
    Q^B    = ln(Vhat_dau/Vhat_par) . E_0 / z

## The result

Re-deriving the bridge from those matrices with `z` carried as a FREE symbol:

    Vhat_pp = z.h + 1        Vhat_nn = 1
    Q^B/E_0 = ln(1 + z.h)/z
    Q^A/E_0 = |q^2 - 2q - 1| (q^2 - 1) / (2 q^2)      (prop:neutron-qvalue-symbolic
                                                       over E_0 = m_e/(q(q-1)))

expanded about the classical point q = 1 + w:

    w^0 : 1
    w^1 : z - 1          <- matches the corpus's (z-1)h/2 EXACTLY
    w^2 : -z^2/3 - 3z/2 + 1/2        } NEW — the corpus records only
    w^3 : z^3/3 + 2z^2/3 + 3z/2 - 1/2}      first order plus O(h^2)

**So alpha = (z-1)h/2 is the GENERIC-z result, not a convention-C
specialisation.** Nothing in the bridge derivation privileges z_C. Substituting
z_D into the BRIDGE is therefore legitimate and gives the correct D-frame
first-order term.

## What this does and does not license — the scope that matters

`qbeta_utils.py`'s guard says, in its KeyError:

    "Under D the c_k ladder is NOT derived (bean qou-cds1): substituting z_D
     into alpha = (z-1)h/2 is proved invalid by
     QOU.QBeta.decayLadder_zC_threeRow_ne_zero and
     QOU.QBeta.eigenphase_bar_defect_of_fullBar."

That is CORRECT FOR THE LADDER and this probe does not contradict it. The two
Lean results it cites are about the ladder's three-row forcing and the bar
defect — not about whether the bridge's first-order coefficient is generic.
The distinction this probe adds:

  - the BRIDGE term (z-1)h/2            generic in z    -> D substitution OK
  - the COS RESUMMATION cos(alpha)      justified by alpha bar-odd (Step 4)
                                        -> FAILS under D
  - the c_k LADDER built on it          C-frame          -> FAILS under D

So what must be re-derived under D is the RESUMMATION FORM and the ladder, not
the phase formula. That is a strictly narrower target than "re-derive the
ladder from scratch", and it is narrower than the guard's sentence reads if
that sentence is taken as a claim about the phase formula alone.

The guard should stay exactly as it is: it withholds `z`/`alpha` unless the
caller NAMES a convention, which is a visibility mechanism, and it serves
`convention='D'` already. Nothing here asks for it to be loosened.

## Values at the proton pin

    alpha_C = -0.052336120268228835      cos = 0.998630777833329740
    alpha_D = -0.040485777340642763      cos = 0.999180562853895945

alpha_D is recorded as the generic-formula value, NOT as a wired ladder input.
No c_k is proposed, extracted, or wired; c_3 ~ -974 remains a sensitivity
measurement per qou-cds1.

Run:  python3 -u computations/qbeta/qbeta_d_frame_bridge_generic_z.py
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

q, z, w = sp.symbols("q z w", positive=True)
h = q - 1 / q


def bar(e):
    return sp.simplify(sp.together(e.subs(q, 1 / q)))


def main() -> int:
    # transfer matrices, verbatim from beta-decay-transfer-matrix-proof.md
    T_pp = sp.Matrix([[h, 1], [1, 0]])
    T_nn = sp.Matrix([[0, 1], [1, -h]])
    T_mix = sp.Matrix([[h / 2, 1], [1, -h / 2]])
    delta = sp.simplify(T_mix - T_nn)
    z_free_ops = all(sp.simplify(sp.diff(M, z)) == sp.zeros(*M.shape)
                     for M in (T_pp, T_nn, T_mix))

    # Markov trace on a 2x2:  Vhat = z*M_11 + M_21
    Vhat = lambda M: sp.simplify(z * M[0, 0] + M[1, 0])  # noqa: E731
    Vpp, Vnn = Vhat(T_pp), Vhat(T_nn)

    QB = sp.log(Vpp / Vnn) / z                      # in units of E_0
    QA = (1 + 2 * q - q**2) * (q**2 - 1) / (2 * q**2)   # q>1 near 1: sign resolved
    ratio = sp.simplify(QA / QB)
    ser = sp.expand(sp.series(ratio.subs(q, 1 + w), w, 0, 4).removeO())
    coeffs = {f"w^{k}": str(sp.simplify(ser.coeff(w, k))) for k in range(4)}

    corpus = 1 + (z - 1) * h / 2
    corpus_ser = sp.expand(sp.series(corpus.subs(q, 1 + w), w, 0, 4).removeO())
    first_order_matches = bool(
        sp.simplify(ser.coeff(w, 1) - corpus_ser.coeff(w, 1)) == 0)

    z_C = sp.sqrt(q) / (q + 1)
    z_D = q**3 / (q**2 + 1)
    q0 = q_at(40)
    q0s = sp.Float(str(q0), 40)
    phases = {}
    for nm, zv in (("C", z_C), ("D", z_D)):
        a = (zv - 1) * h / 2
        phases[nm] = {
            "alpha_at_q0": str(sp.N(a.subs(q, q0s), 18)),
            "cos_alpha_at_q0": str(sp.N(sp.cos(a.subs(q, q0s)), 18)),
            "bar_ratio": str(sp.factor(sp.simplify(bar(a) / a))),
        }

    payload = {
        "description": (
            "The Q_beta bridge phase alpha = (z-1)h/2 is GENERIC in z, not a "
            "convention-C specialisation. z enters only via the Markov trace "
            "functional and the E_0/z normalisation; the transfer matrices are "
            "z-free. So the D re-derivation target is the RESUMMATION FORM and "
            "the ladder, not the phase formula."
        ),
        "where_z_enters": {
            "transfer_matrices_are_z_free": bool(z_free_ops),
            "T_pp": str(T_pp.tolist()), "T_nn": str(T_nn.tolist()),
            "T_mix": str(T_mix.tolist()),
            "Delta_beta": str(sp.simplify(delta).tolist()),
            "trace_functional": "Vhat = z*M_11 + M_21   (z-linear)",
            "normalisation": "Q^B = ln(Vhat_dau/Vhat_par) * E_0/z",
        },
        "generic_z_bridge": {
            "Vhat_pp": str(Vpp), "Vhat_nn": str(Vnn),
            "QB_over_E0": str(QB), "QA_over_E0": str(sp.simplify(QA)),
            "expansion_about_q_eq_1": coeffs,
            "first_order_matches_corpus_(z-1)": first_order_matches,
            "second_and_third_order_are_new": (
                "the corpus records 1 + (z-1)h/2 + O(h^2) only; w^2 and w^3 "
                "above are the exact generic-z continuation"
            ),
        },
        "phases_at_proton_pin": phases,
        "scope": {
            "bridge_term": "generic in z -> z_D substitution legitimate",
            "cos_resummation": ("justified by alpha bar-odd (qou-cds1 Step 4); "
                                "bar(alpha)/alpha = -1 under C, non-constant "
                                "under D -> FAILS"),
            "ck_ladder": "C-frame -> FAILS under D",
            "guard_is_correct_for_the_ladder": (
                "qbeta_utils.py's KeyError cites decayLadder_zC_threeRow_ne_zero "
                "and eigenphase_bar_defect_of_fullBar, which are about the "
                "ladder and the bar defect, not about the bridge coefficient. "
                "Nothing here asks for the guard to be loosened; it withholds "
                "z/alpha unless a convention is NAMED, and already serves D."
            ),
            "no_ck_wired": True,
        },
        "context": {"beans": ["qou-cds1"],
                    "prior": ["qbeta_d_frame_ladder_bar_weight_prune.py",
                              "qbeta_trm_identity_normalisation_under_d.py"]},
        "q0Anchor": "proton",
        "q0Value": str(q0),
    }

    out = WitnessBuilder.wrap_legacy(
        "qbeta-d-frame-bridge-generic-z", payload,
        script_path=__file__, engine="python+sympy (exact in q, z free)",
    ).save()

    print("=== Is alpha = (z-1)h/2 generic in z, or convention-C? ===")
    print(f"  transfer matrices are z-free        : {z_free_ops}")
    print(f"  z enters only via  Vhat = z*M_11 + M_21  and  E_0/z")
    print()
    print("  Q^A/Q^B about q = 1+w, with z FREE:")
    for k, v in coeffs.items():
        print(f"     {k} : {v}")
    print(f"  first order matches corpus (z-1)    : {first_order_matches}")
    print(f"  => the bridge phase is GENERIC in z; w^2, w^3 are NEW")
    print()
    for nm in ("C", "D"):
        p = phases[nm]
        print(f"  {nm}: alpha(q0) = {p['alpha_at_q0']}   "
              f"bar(alpha)/alpha = {p['bar_ratio']}")
    print()
    print("  SCOPE: the D target is the RESUMMATION FORM + the ladder,")
    print("         NOT the phase formula. The qbeta_utils guard is correct")
    print("         for the ladder and should stay as it is.")
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
