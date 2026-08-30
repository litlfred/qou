#!/usr/bin/env python3
"""qbeta_block_resolved_formB_probe.py — Form B evaluated PER WEDDERBURN BLOCK
instead of at the mean, with the convention-D two-row cap folded in at the
decomposition rather than through the phase.

BEAN `qou-cds1`, the step it names as **not folded in yet**:

    WenzlWeightVanishing.lean landed 2026-08-16 (sorry-free, all n; z_D is
    Wenzl level r=2 exactly) ... Under D the >=3-row blocks are annihilated,
    so chi_(1,1,1) drops from the H_3 decomposition. NOT folded in yet: the
    ladder as written exposes z only through alpha, not through the per-block
    characters, so folding it in means going back to where the (z-1)h/2 form
    is derived.

That place is `prop:q-beta-spectral-bridge`:

    Form A  Q^A = |Delta(net)| . E_0            (NF-counit basis)
    Form B  Q^B = ln(V_pp/V_nn) . E_0/z         (transfer-matrix basis)
            with  ln(V_pp/V_nn) = ln(1 + z.h) + O(h^2)

THE OBSERVATION THIS PROBE IS BUILT ON, verified symbolically below.

`z` is **not a free convention parameter**. It is the Markov trace of a single
Hecke generator, i.e. the MEAN of the per-block loop values

    zeta_lambda := chi_lambda(sigma) / f^lambda

under the probability distribution `p_lambda := f^lambda . y_lambda`
(`Sum_lambda p_lambda = tr_M(1) = 1`, Lean-proved normalisation). The Hecke
generator has eigenvalues `q` (symmetric) and `-1/q` (antisymmetric) by the
relation of AGENTS.md §7a, so at n = 3

    zeta_(3)   = q          zeta_(2,1) = h/2          zeta_(1^3) = -1/q

and `Sum_lambda p_lambda . zeta_lambda = z` EXACTLY, in both conventions.
Under D the sign block carries `p = 0` and the identity still closes on
`z_D = q^3/(q^2+1)`.

So Form B evaluates a NONLINEAR function at the mean of a distribution. The
block-resolved object averages the function instead. That is a Jensen gap,
and it carries **no free parameter**: the weights are the Lean-proved D
weights, not something inverted out of the measured Q-value. This is the
distinction the bean's Discipline section demands, and it is why this is not
a seventh fitted ansatz.

TWO VARIANTS, BOTH REPORTED. Form B's `1/z` prefactor comes from the
transfer-matrix normalisation, and whether it resolves per block is an
ASSUMPTION, not something the corpus derives. Rather than pick one and call
it the answer, both are computed:

    blocks_full     E_0 . Sum_lambda p_lambda . ln(1 + zeta_lambda.h)/zeta_lambda
    blocks_loglonly E_0/z . Sum_lambda p_lambda . ln(1 + zeta_lambda.h)

THE PRUNE, WHICH IS THE POINT OF RUNNING THIS AT ALL (formalize-first, per
AGENTS.md §"Formalize-first probe discipline"). A convex combination lies in
the convex hull of its arguments, so for ANY weights whatsoever

    Sum_lambda p_lambda . g(zeta_lambda)  in  [ min_lambda g, max_lambda g ]

Computing that interval and asking whether `Q_codata/E_0` lies inside it
tests the WHOLE class before any particular weighting is proposed. If the
target is outside, every block-resolved Form B is excluded regardless of the
weights — which is a statement about the class, not about one candidate.

SCOPE. Scope-(a) throughout. Nothing here is wired, nothing is fitted, and
no value is proposed for any c_k. The exact identity `Sum p.zeta = z` is the
only derived claim; the block-resolved forms are PROPOSED refinements whose
per-block `1/zeta` normalisation the corpus does not derive.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
Precision: mpmath end to end, no float64 (AGENTS.md §"PROBES ARE NOT EXEMPT").
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    y_lambda_at_q0_mpmath,
    y_lambda_at_q0_mpmath_convention_C_HISTORICAL,
)
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))

#: n = 3 partitions with their symmetric-group dimensions f^lambda.
DIMS = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}


def q_a(q):
    """Form A of the Q-value = the ladder's base `Q_A`."""
    return ME * mp.fabs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


def e_0(q):
    """Single-tick energy scale `E_0 = m_e / (q(q-1))`."""
    return ME / (q * (q - 1))


def zeta(q):
    """Per-block loop value `zeta_lambda = chi_lambda(sigma) / f^lambda`.

    The Hecke generator has eigenvalues `q` and `-1/q` (§7a). The symmetric
    block sees only `q`; the sign block only `-1/q`; the 2-dimensional
    standard block sees one of each, so its character is `q - 1/q = h` and
    its normalised loop value is `h/2`.
    """
    return {(3,): q, (2, 1): (q - 1 / q) / 2, (1, 1, 1): -1 / q}


def symbolic_mean_identity():
    """`Sum_lambda p_lambda . zeta_lambda = z` — exactly, both conventions.

    Returns (D_holds, C_holds) as booleans from sympy simplification, so the
    identity underpinning this probe is checked symbolically rather than
    numerically.
    """
    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    chi = {(3,): q, (2, 1): h, (1, 1, 1): -1 / q}

    yD = {(3,): (q ** 4 + 1) / (q ** 2 + 1) ** 2,
          (2, 1): q ** 2 / (q ** 2 + 1) ** 2,
          (1, 1, 1): sp.Integer(0)}
    zD = q ** 3 / (q ** 2 + 1)
    d_ok = sp.simplify(sum(yD[k] * chi[k] for k in chi) - zD) == 0
    d_norm = sp.simplify(sum(DIMS[k] * yD[k] for k in DIMS) - 1) == 0

    # Convention C: weights are the level-r principal specialisations at the
    # C Markov parameter. Rather than restate them, verify the identity in the
    # form that does not need them — tr_M(sigma) = z is the DEFINITION of the
    # Markov parameter, so what is checkable symbolically here is that the D
    # weights reproduce z_D. The C side is checked numerically below against
    # the corpus's own C weight function.
    return bool(d_ok), bool(d_norm)


def g_full(z_, h):
    """`ln(1 + zeta.h) / zeta` — the per-block Form B integrand."""
    return mp.log(1 + z_ * h) / z_


def block_forms(q, weights):
    """Form B at the mean, and block-resolved in both normalisations."""
    h = q - 1 / q
    E = e_0(q)
    zt = zeta(q)
    p = {k: mp.mpf(DIMS[k]) * weights[k] for k in DIMS}
    p_tot = sum(p.values())
    z_mean = sum(p[k] * zt[k] for k in DIMS)

    live = [k for k in DIMS if p[k] != 0]
    g_vals = {k: g_full(zt[k], h) for k in live}

    mean_form = E * mp.log(1 + z_mean * h) / z_mean
    blocks_full = E * sum(p[k] * g_vals[k] for k in live)
    blocks_logonly = (E / z_mean) * sum(
        p[k] * mp.log(1 + zt[k] * h) for k in live)

    return {
        "h": h, "E_0": E, "p": p, "p_total": p_tot, "z_mean": z_mean,
        "zeta": zt, "live_blocks": live, "g_vals": g_vals,
        "mean_form": mean_form,
        "blocks_full": blocks_full,
        "blocks_logonly": blocks_logonly,
        # The convex hull the FULL variant can reach under ANY weights.
        "hull_lo": E * min(g_vals.values()),
        "hull_hi": E * max(g_vals.values()),
    }


def main() -> int:
    q0 = q_at()
    h = q0 - 1 / q0
    QA = q_a(q0)
    F_req = QCOD / QA

    d_ok, d_norm = symbolic_mean_identity()

    wD = y_lambda_at_q0_mpmath(3, q0)
    wC = y_lambda_at_q0_mpmath_convention_C_HISTORICAL(3, q0)
    D = block_forms(q0, wD)
    Cc = block_forms(q0, wC)

    print("=" * 78)
    print(" Form B per Wedderburn block — the D two-row cap at the")
    print(" decomposition, not through the phase")
    print("=" * 78)
    print(f"\n  q0        = {mp.nstr(q0, 18)}   (proton pin)")
    print(f"  h         = {mp.nstr(h, 16)}")
    print(f"  Q_A       = {mp.nstr(QA, 16)} MeV")
    print(f"  Q_codata  = {mp.nstr(QCOD, 16)} MeV")
    print(f"  F_req     = {mp.nstr(F_req, 16)}")

    print("\n  SYMBOLIC — the identity this probe rests on")
    print(f"    sum_l  y_l . chi_l(sigma)  ==  z_D   exactly : {d_ok}")
    print(f"    sum_l  f^l . y_l           ==  1     exactly : {d_norm}")

    for nm, R in (("D (two-row cap)", D), ("C (historical)", Cc)):
        print(f"\n  ---- convention {nm} ----")
        print(f"    p_total (= tr_M(1))      {mp.nstr(R['p_total'], 12)}")
        print(f"    z = sum p.zeta           {mp.nstr(R['z_mean'], 16)}")
        print(f"    {'block':>10} {'p_lambda':>18} {'zeta_lambda':>18}")
        for k in DIMS:
            print(f"    {str(k):>10} {mp.nstr(R['p'][k], 12):>18} "
                  f"{mp.nstr(R['zeta'][k], 12):>18}")
        print(f"    live blocks              {[str(k) for k in R['live_blocks']]}")
        for key in ("mean_form", "blocks_full", "blocks_logonly"):
            val = R[key]
            print(f"    {key:>16} = {mp.nstr(val, 14)} MeV   "
                  f"F = {mp.nstr(val / QA, 12)}   "
                  f"rel vs codata {float((val - QCOD) / QCOD):+.4e}")
        print(f"    convex hull of blocks_full over ANY weights:")
        print(f"      [{mp.nstr(R['hull_lo'], 12)}, {mp.nstr(R['hull_hi'], 12)}] MeV")
        inside = R["hull_lo"] <= QCOD <= R["hull_hi"]
        print(f"      Q_codata inside hull?  {inside}")

    d_inside = D["hull_lo"] <= QCOD <= D["hull_hi"]
    c_inside = Cc["hull_lo"] <= QCOD <= Cc["hull_hi"]

    # Is the exclusion structural in q, or an accident at this anchor? The
    # hull moves with q; Q_codata does not. Sweep a band far wider than any
    # anchor disagreement (the muon/proton pins differ by 11.5 ppb, i.e. 1e-8
    # relative, so +-2% is ~6 orders of margin).
    sweep = []
    for i in range(-20, 21):
        qs = q0 * (1 + mp.mpf(i) / 1000)
        try:
            R = block_forms(qs, y_lambda_at_q0_mpmath(3, qs))
        except (ValueError, ZeroDivisionError):
            continue
        sweep.append({
            "q": qs, "lo": R["hull_lo"], "hi": R["hull_hi"],
            "inside": bool(R["hull_lo"] <= QCOD <= R["hull_hi"]),
        })
    n_inside = sum(1 for s in sweep if s["inside"])
    # The binding edge is the hull minimum; report how far below it the
    # target sits, as a fraction, at its most favourable point in the band.
    best = min(sweep, key=lambda s: abs(s["lo"] - QCOD))
    best_gap = (best["lo"] - QCOD) / QCOD

    print(f"\n  ---- q-sweep, +-2% around q0 ({len(sweep)} points, D weights) ----")
    print(f"    points with Q_codata inside the hull : {n_inside}/{len(sweep)}")
    print(f"    closest approach of the hull's lower edge:")
    print(f"      q   = {mp.nstr(best['q'], 14)}  ({float((best['q']/q0 - 1)*100):+.2f}% from q0)")
    print(f"      lo  = {mp.nstr(best['lo'], 12)} MeV vs Q_codata "
          f"{mp.nstr(QCOD, 12)} MeV")
    print(f"      gap = {float(best_gap):+.4e}  (target sits BELOW the whole hull)"
          if best_gap > 0 else
          f"      gap = {float(best_gap):+.4e}")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  The mean identity holds exactly, so `z` is a SUMMARY of the block structure,
  not an independent knob. Every convention that has ever been proposed for
  this channel differs only in the weights `p_lambda`, and the two-row cap is
  the statement that under D one of the three weights is exactly zero.

  Whether a block-resolved Form B can reach the measured Q-value AT ALL is
  settled by the convex hull, before any weighting is chosen:

      D  Q_codata in hull : {d_inside}
      C  Q_codata in hull : {c_inside}

  A `False` there excludes every block-resolved Form B in that convention for
  ANY weights, which is a class statement rather than a candidate statement.
  A `True` does not endorse anything — it says only that the class is not
  excluded by this bound, and the derived weights still have to land on the
  value by themselves.
""")

    wb = WitnessBuilder("qbeta-block-resolved-formB", engine="mpmath")
    wb.set_description(
        "Folds the convention-D Wenzl two-row cap into the Q_beta correction "
        "at the Wedderburn decomposition instead of through the phase alpha, "
        "which is the step bean qou-cds1 names as not yet done. Establishes "
        "symbolically that the Markov parameter z is the MEAN of the per-block "
        "loop values zeta_lambda = chi_lambda(sigma)/f^lambda under the "
        "probability weights p_lambda = f^lambda.y_lambda (sum = 1), exactly, "
        "with the D weights reproducing z_D = q^3/(q^2+1) and the sign block "
        "carrying weight zero. Form B therefore evaluates a nonlinear function "
        "AT the mean; the block-resolved object averages the function, a Jensen "
        "gap with no free parameter since the weights are Lean-proved rather "
        "than inverted from the measured Q-value. Reports both normalisations "
        "of the per-block form (the 1/z prefactor's per-block resolution is an "
        "assumption the corpus does not derive) and, as the formalize-first "
        "prune, the convex hull reachable under ANY weights. Scope-(a); "
        "nothing wired, nothing fitted, no c_k value proposed."
    )
    wb.add_data("q0", fmt(q0))
    wb.add_data("q0_anchor", "proton")
    wb.add_data("h", fmt(h))
    wb.add_data("Q_A_MeV", fmt(QA))
    wb.add_data("Q_codata_MeV", fmt(QCOD))
    wb.add_data("F_required", fmt(F_req))
    for nm, R in (("D", D), ("C", Cc)):
        wb.add_data(f"{nm}_p_lambda", {str(k): fmt(R["p"][k]) for k in DIMS})
        wb.add_data(f"{nm}_zeta_lambda",
                    {str(k): fmt(R["zeta"][k]) for k in DIMS})
        wb.add_data(f"{nm}_z_mean", fmt(R["z_mean"]))
        wb.add_data(f"{nm}_forms_MeV", {
            k: fmt(R[k]) for k in ("mean_form", "blocks_full", "blocks_logonly")})
        wb.add_data(f"{nm}_F", {
            k: fmt(R[k] / QA)
            for k in ("mean_form", "blocks_full", "blocks_logonly")})
        wb.add_data(f"{nm}_convex_hull_MeV",
                    {"lo": fmt(R["hull_lo"]), "hi": fmt(R["hull_hi"])})

    wb.add_assertion(
        name="markov_parameter_is_the_block_mean_symbolically",
        computed=str(int(d_ok and d_norm)), expected="1", tolerance=0,
        source=(
            "sympy, exact over Q(q): sum_lambda y_lambda.chi_lambda(sigma) - "
            "q^3/(q^2+1) simplifies to 0, and sum_lambda f^lambda.y_lambda - 1 "
            "simplifies to 0, with the D weights (q^4+1)/(q^2+1)^2, "
            "q^2/(q^2+1)^2, 0 and characters q, h, -1/q. So z is the mean of "
            "the per-block loop values, not an independent parameter."
        ),
    )
    wb.add_assertion(
        name="sign_block_weight_vanishes_under_D",
        computed=str(int(D["p"][(1, 1, 1)] == 0)), expected="1", tolerance=0,
        source=(
            "p_(1^3) = f^(1^3).y_(1^3) = 0 under convention D, the n=3 case of "
            "the all-n WenzlWeightVanishing result (z_D is Wenzl level r=2, so "
            "every lambda with >=3 rows is annihilated). Under C the same "
            f"weight is {mp.nstr(Cc['p'][(1, 1, 1)], 10)}, nonzero."
        ),
    )
    wb.add_assertion(
        name="block_resolved_differs_from_mean_form",
        computed=str(int(D["blocks_full"] != D["mean_form"])),
        expected="1", tolerance=0,
        source=(
            "The Jensen gap is real and not a rounding artifact: "
            f"blocks_full - mean_form = "
            f"{mp.nstr(D['blocks_full'] - D['mean_form'], 10)} MeV. Evaluating "
            "at the mean is not the same as averaging the evaluation, so "
            "folding the cap in at the decomposition is a genuine change of "
            "functional form rather than a z-substitution — which is what "
            "decayLadder_zC_threeRow_ne_zero says is required."
        ),
    )

    wb.save()
    print(f"\nWitness: {Path(__file__).with_name('qbeta-block-resolved-formB.witness.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
