#!/usr/bin/env python3
"""The three inter-nucleon bond factors are a BAR-CONJUGATE PAIR and their
(colour-corrected) MIDPOINT.

`qbeta_bond_factors_derived_probe.py` derives five closed forms and records
three identities, of which two concern the bonds:

    identity 1:  b_pp - z = 0            z = q^3/(q^2+1), the convention-D
                                         Ocneanu / Markov parameter
    identity 2:  b_pp/b_nn - q^4 = 0     "the two same-species bond factors
                                         differ by exactly q^4"

Both are correct and neither is restated here.  What this probe adds is that
the `q^4` of identity 2 is not a scale factor that happens to be a fourth
power — it is the **bar involution** `q -> q^-1`, which the corpus already uses
as its parity apparatus everywhere (bar-even / bar-odd c_k, the `S_leak`
decomposition, `MarkovZFullBarCondition`).  Written that way the three bonds
stop being three constants and become one object:

    b_pp = z                             the bar-EVEN+ODD endpoint
    b_nn = zbar := z|_{q -> 1/q}         the other endpoint
    b_pn = (z + zbar)/2 + (delta/4)*h    their midpoint, colour-displaced

with `h = q - q^-1` the Hecke deformation parameter and
`delta = (q-1)^2 (1 - q^-4)/3` the colour weighting that
`qbeta_bond_factors_derived_probe` already names.

*** THE FIVE IDENTITIES, EACH SIMPLIFYING TO EXACTLY ZERO ***

  1. `b_nn - zbar = 0`.  The neutron-neutron bond IS the bar conjugate of the
     proton-proton bond.  (Equivalent to identity 2 of the sibling probe;
     stated in the vocabulary that makes it a symmetry rather than a scale.)

  2. `z - zbar - h = 0`.  The bar-ODD part of the Ocneanu parameter is exactly
     `h/2`.  This is why the like-pair bonds are separated by `h` and not by
     some other quantity: `z - zbar` is forced.

  3. `b_pn - (z + zbar)/2 - h*delta/4 = 0`.  The unlike-pair bond sits at the
     bar-EVEN part of `z` (= the midpoint of the two like-pair bonds),
     displaced by the colour weighting alone.  Set `delta = 0` — the
     colour-BLIND crossing — and `b_pn` is exactly the midpoint.

  4. `z*zbar - 1/(q + q^-1)^2 = 0`.  So `sqrt(b_pp * b_nn) = 1/(q + q^-1)`,
     manifestly bar-invariant: the geometric mean of the two like-pair bonds
     is a bar-fixed point.

  5. The bar-ODD part of `b_pn` factors as
     `-(q-1)^5 (q+1)^3 (q^2+1) / (24 q^5)` — a FIFTH-order zero at `q = 1`.
     So the p-n bond is the one bond that breaks the bar symmetry, it breaks
     it only through the colour weighting, and it breaks it at fifth order:
     `1.64e-05` relative at the proton pin — MEASURED, and reported in the
     witness.  (This docstring read `4.6e-07` before the probe was first run;
     that figure was estimated from the order of the zero rather than
     evaluated, and was wrong by 35x.)

*** WHAT THIS IS NOT ***

- **Not a claim about the categorical bar involution.**  The involution here is
  `q -> q^-1` applied to a rational function.  Whether it is the Hecke-algebra
  bar involution acting on the Markov trace — which would make identity 1 a
  statement about the *words* rather than about their traces — is NOT
  established here and would need the trace's own bar-equivariance.  Read
  these as identities between closed forms.

- **Not independent of the sibling's frame caveat.**  These are identities
  satisfied by the closed forms exactly as written in
  `qbeta_bond_factors_derived_probe.py`, whose own header flags that its
  `t_p`/`t_n` are GROUPED-era while its atom witnesses are canonical
  (bean `qou-4383`).  The bond factors are *inter*-nucleon and the intra-order
  ruling (`qou-hu1f`) changes the *intra*-nucleon word, so they are plausibly
  frame-independent — but that is a plausibility argument, not a measurement,
  and it is not made here.

*** INDEPENDENT CORROBORATION (bean qou-5c64) ***

The same three interface shifts `d = b - z` were isolated by a completely
different route that never touches the Laurent expansion: differencing the
June-era `binding-single-pipeline-comparison` witness against a live run and
solving the four atoms' bond residuals for three unknowns.  That route
returned `d_pp = 0`, `d_pn = -0.10445825933572413`, `d_nn = -0.20906032198987946`
at the MUON pin, against `0`, `-h(1/2 - delta/4)`, `-h` here.  Both are
reported below, each against its own anchor — the ~8th-digit separation
between them is the mu-p substrate tension, not a discrepancy.

Emits `qbeta-bond-bar-parity.witness.json`.
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

_q = sp.Symbol("q", positive=True)

# The five closed forms, verbatim from `qbeta_bond_factors_derived_probe.py`.
# Only the three bonds are used; `t_p`/`t_n` are the per-nucleon free traces
# and carry the frame caveat quoted in the docstring.
Z = _q**3 / (_q**2 + 1)
B_PP = _q**3 / (_q**2 + 1)
B_PN = ((_q**10 - 2*_q**9 + 7*_q**8 - 2*_q**6 + 4*_q**5 + 4*_q**4
         + _q**2 - 2*_q + 1) / (12*_q**5*(_q**2 + 1)))
B_NN = 1 / (_q**3 + _q)

H = _q - 1/_q                                   # Hecke deformation parameter
DELTA = (_q - 1)**2 * (1 - _q**-4) / 3          # colour weighting

# The independently-isolated shifts of bean qou-5c64, at the MUON pin.
# Labelled with their anchor: they are NOT to be compared against a
# proton-pin evaluation (layer straddle).
QOU_5C64_MUON = {"d_pp": "0", "d_pn": "-0.10445825933572413",
                 "d_nn": "-0.20906032198987946"}


def _bar(expr):
    """The involution q -> 1/q."""
    return sp.simplify(expr.subs(_q, 1/_q))


def _ev(expr, q0):
    """Evaluate a rational function of q at `q0`, exactly then to mpf.

    `sp.Rational`-exact substitution, so the only rounding is the final
    `mpf` render at the live compute precision — no float64 anywhere.
    """
    exact = sp.nsimplify(expr.subs(_q, sp.Rational(q0)))
    return mp.mpf(sp.N(exact, mp.dps + 5).__str__())


def main() -> int:
    builder = WitnessBuilder("qbeta-bond-bar-parity", engine="sympy+mpmath")
    set_compute_dps()

    import qou_substrate.constants as _c
    Q0S = _c.Q_50_DIGIT_STR          # experimental (proton) pin — the default
    q0 = mp.mpf(Q0S)

    zbar = _bar(Z)

    # ── the five symbolic identities ────────────────────────────────────
    identities = [
        ("bnn_is_zbar",
         "b_nn - z|_{q->1/q}",
         sp.simplify(B_NN - zbar)),
        ("z_minus_zbar_is_h",
         "z - z|_{q->1/q} - (q - q^-1)",
         sp.simplify(Z - zbar - H)),
        ("bpn_is_bar_even_plus_colour",
         "b_pn - (z + zbar)/2 - h*delta/4",
         sp.simplify(B_PN - (Z + zbar)/2 - H*DELTA/4)),
        ("geometric_mean_is_bar_fixed",
         "z*zbar - 1/(q + q^-1)^2",
         sp.simplify(Z*zbar - 1/(_q + 1/_q)**2)),
        ("bpn_bar_odd_factorisation",
         "[b_pn - bar(b_pn)]/2 + (q-1)^5 (q+1)^3 (q^2+1)/(24 q^5)",
         sp.simplify((B_PN - _bar(B_PN))/2
                     + (_q-1)**5*(_q+1)**3*(_q**2+1)/(24*_q**5))),
    ]

    print("=" * 74)
    print("1. FIVE SYMBOLIC IDENTITIES — each must simplify to exactly zero")
    print("=" * 74)
    id_rows, all_zero = [], True
    for name, expr_str, residual in identities:
        is_zero = residual == 0
        all_zero &= is_zero
        id_rows.append({"name": name, "expression": expr_str,
                        "simplifies_to": str(residual),
                        "exactly_zero": bool(is_zero)})
        print(f"  {'OK ' if is_zero else 'FAIL'}  {expr_str:<54} -> "
              f"{residual}")

    # ── numeric, at the proton pin only (no cross-anchor arithmetic) ────
    print()
    print("=" * 74)
    print("2. AT THE EXPERIMENTAL (PROTON) PIN")
    print("=" * 74)
    v_z, v_zbar = _ev(Z, Q0S), _ev(zbar, Q0S)
    v_h, v_delta = _ev(H, Q0S), _ev(DELTA, Q0S)
    v_pn = _ev(B_PN, Q0S)
    v_gm = mp.sqrt(v_z * v_zbar)
    v_mid = (v_z + v_zbar) / 2
    numerics = {
        "z_eq_b_pp": v_z,
        "zbar_eq_b_nn": v_zbar,
        "b_pn": v_pn,
        "h_eq_z_minus_zbar": v_h,
        "delta_colour_weighting": v_delta,
        "geometric_mean_sqrt_z_zbar": v_gm,
        "one_over_q_plus_qinv": 1/(q0 + 1/q0),
        "bar_even_midpoint": v_mid,
        "b_pn_minus_midpoint": v_pn - v_mid,
        "h_delta_over_4": v_h*v_delta/4,
    }
    for k, v in numerics.items():
        print(f"  {k:<30} {mp.nstr(v, 25):>30}")

    # bar-odd relative size of b_pn
    v_odd = _ev(sp.simplify((B_PN - _bar(B_PN))/2), Q0S)
    rel_odd = abs(v_odd) / abs(v_pn)
    print(f"  {'b_pn bar-odd / b_pn':<30} {mp.nstr(rel_odd, 12):>30}")

    # ── the sibling probe's own measured literals ───────────────────────
    print()
    print("=" * 74)
    print("3. AGAINST qbeta_bond_factors_derived_probe.MEASURED (proton pin)")
    print("=" * 74)
    measured = {"b_pp": "0.6126880371464652516",
                "b_pn": "0.50822978937673896258",
                "b_nn": "0.40362773835082593617"}
    derived = {"b_pp": v_z, "b_pn": v_pn, "b_nn": v_zbar}
    worst = mp.mpf(0)
    meas_rows = []
    for k, s in measured.items():
        m = mp.mpf(s)
        rel = abs(derived[k] - m)/abs(m)
        worst = max(worst, rel)
        meas_rows.append({"name": k, "measured": s,
                          "from_bar_form": fmt(derived[k]),
                          "rel_err": fmt(rel)})
        print(f"  {k:<6} measured {s:>24}   rel {mp.nstr(rel, 4)}")
    print(f"  worst relative disagreement: {mp.nstr(worst, 4)}")

    # ── the qou-5c64 isolation, at ITS OWN (muon) anchor ────────────────
    print()
    print("=" * 74)
    print("4. INDEPENDENT ISOLATION (bean qou-5c64) — AT THE MUON PIN")
    print("=" * 74)
    QM = _c.Q_MUON_50_DIGIT_STR if hasattr(_c, "Q_MUON_50_DIGIT_STR") else None
    x_rows = []
    if QM is None:
        print("  muon 50-digit string not exported by qou_substrate.constants;")
        print("  recording the isolated values without a same-anchor compare.")
        for k, s in QOU_5C64_MUON.items():
            x_rows.append({"name": k, "isolated_at_muon_pin": s,
                           "same_anchor_prediction": None})
    else:
        pred = {"d_pp": _ev(B_PP - Z, QM), "d_pn": _ev(B_PN - Z, QM),
                "d_nn": _ev(B_NN - Z, QM)}
        for k, s in QOU_5C64_MUON.items():
            iso = mp.mpf(s)
            denom = abs(iso) if iso != 0 else mp.mpf(1)
            rel = abs(pred[k] - iso)/denom
            x_rows.append({"name": k, "isolated_at_muon_pin": s,
                           "same_anchor_prediction": fmt(pred[k]),
                           "rel_err": fmt(rel)})
            print(f"  {k:<6} isolated {s:>24}   predicted "
                  f"{mp.nstr(pred[k], 20):>24}   rel {mp.nstr(rel, 4)}")

    (
        builder
        .set_description(
            "The three inter-nucleon bond factors of "
            "qbeta_bond_factors_derived_probe are a BAR-CONJUGATE PAIR and "
            "their colour-displaced midpoint: b_pp = z, b_nn = z|_{q->1/q}, "
            "b_pn = (z + zbar)/2 + (delta/4)h.  Five symbolic identities, "
            "each simplifying to exactly zero.  This RESTATES that probe's "
            "identity 2 (b_pp/b_nn = q^4) in the vocabulary of the bar "
            "involution rather than of a scale factor, and adds that the "
            "separation z - zbar is exactly the Hecke parameter h = q - q^-1, "
            "that the geometric mean sqrt(b_pp b_nn) = 1/(q + q^-1) is "
            "bar-fixed, and that b_pn's bar-odd part carries a FIFTH-order "
            "zero at q = 1 (1.6415e-05 relative at the proton pin), so the "
            "unlike-pair bond is the only one that breaks the symmetry and "
            "breaks it only through the colour weighting.  Identities "
            "between closed forms; NOT a claim that q -> q^-1 here is the "
            "Hecke-algebra bar involution acting on the Markov trace, and "
            "NOT independent of that probe's own GROUPED-frame caveat "
            "(bean qou-4383)."
        )
        .set_content_block("rem:jones-markov-trace-stabilisation")
        .add_parameter("q0", Q0S)
        .add_parameter("q0_pin", "experimental (proton) — qou_substrate.constants.Q_50_DIGIT_STR")
        .add_parameter("markov_convention", "D (z = q^3/(q^2+1))")
        .add_parameter("bar_involution", "q -> q^-1")
        .add_data("symbolic_identities", id_rows)
        .add_data("at_proton_pin",
                  {k: fmt(v) for k, v in numerics.items()}
                  | {"b_pn_bar_odd_over_b_pn": fmt(rel_odd)})
        .add_data("against_sibling_measured", meas_rows)
        .add_data("qou_5c64_independent_isolation_muon_pin", x_rows)
        .add_assertion(
            name="five_bar_parity_identities_exactly_zero",
            computed="0" if all_zero else "nonzero",
            expected="0",
            tolerance="exact",
            unit="sympy.simplify of each of the five residuals",
            source=(
                "Closed forms as written in "
                "computations/qbeta/qbeta_bond_factors_derived_probe.py; "
                "bar involution q -> q^-1."
            ),
        )
        .add_assertion(
            name="bar_form_reproduces_sibling_measured_bonds",
            computed=fmt(worst),
            expected="0",
            tolerance="1e-18",
            unit=(
                "max over {b_pp, b_pn, b_nn} of |bar-form value - MEASURED| "
                "/ |MEASURED|, both at the proton pin"
            ),
            source=(
                "qbeta_bond_factors_derived_probe.MEASURED, which carries "
                "19-20 significant digits."
            ),
        )
    )

    out = builder.save()
    print()
    print(f"Witness: {out}")
    return 0 if all_zero and worst < mp.mpf("1e-18") else 1


if __name__ == "__main__":
    raise SystemExit(main())
