"""The M_beta spectrum on V_(2,1) under the convention-D trace.

Bean `qou-pdix` (child of `qou-cds1`), continuing where entry (10) left off.

`prop:q-beta-cos-resummation` asserts: "The transfer-matrix `M_beta` has spectrum
`{e^{+i.alpha}, e^{-i.alpha}}` on the 2-dimensional irreducible representation
`V_(2,1)` of `H_3(q)`."  This derives that spectrum.

## What was already closed, and is NOT re-run here

`qou-pdix` excludes `M = lambda * rho(w)` for `w` a braid word IN THE SEMINORMAL
REPRESENTATION, scope-(b), by a rationality invariant: every character lies in
`Z[q,q^-1]`, weights are rational in `(q,z)`, and `2cos((z-1)h/2)` is
transcendental over `Q(q,z)`.  Routes 1-4 of that bean are closed.  Nothing below
re-derives them.

## The gap this closes

That exclusion is about the BRAID IMAGE.  The block `prop:q-beta-cos-resummation`
is conditional on `prop:beta-decay-transfer-matrix`, which defines FOUR explicit
2x2 matrices over `Z[q^{+-1}]` --- and two of them are not braid-image elements
at all:

    T(c,d) = [[c*h + d, c], [c, d]]                       h = q - 1/q
    T_pp  = T(1, 0)          = [[h, 1], [1, 0]]           sigma
    T_nn  = T(1, -h)         = [[0, 1], [1, -h]]          sigma^-1
    T_mix = T(1, -h/2)       = (T_pp + T_nn)/2            NOT a group element
    Delta_beta = T_mix - T_nn = T_pp - T_mix = (h/2)*I    SCALAR

`T_mix` is an algebraic average (the block says so) and `Delta_beta` is a scalar
multiple of the identity.  Neither is `lambda*rho(w)` for a braid word `w`, so
the rationality invariant does not reach them.  They are excluded here by a
different and much cheaper invariant: the DETERMINANT.

## Result 1 --- the only M_beta the corpus DEFINES is scalar

`M_beta` occurs in exactly two places in the whole corpus, both inside the claim
itself (six-path corpus-grep, this session).  It is never defined.  The only
"universal beta decay matrix" the conditional-on block defines is
`Delta_beta = (h/2)*I`, whose spectrum on V_(2,1) is the REPEATED REAL eigenvalue
`h/2` --- not a conjugate pair on the unit circle.  A scalar matrix has no
eigenphase at all.

## Result 2 --- none of the four has a unit-circle spectrum

A 2x2 matrix has spectrum `{e^{+i.a}, e^{-i.a}}` with `a` real IFF `det = 1` and
`|trace| <= 2`.  The determinants are exact:

    det T_pp = det T_nn = -1            (Hecke unimodularity)
    det T_mix = -(1 + h^2/4) < 0        for every real h
    det Delta_beta = h^2/4              = 1 only at h = +-2

None is 1 at the substrate, so the criterion fails at the FIRST clause for all
four.  This is convention-independent: no `z` appears in any of these matrices.

## Result 3 --- z_D IS the seminormal diagonal entry, exactly

The seminormal `sigma_2` on V_(2,1) is forced by Hecke + braid to have diagonal
`(d1, d2)` with `d1 = q^3/(q^2+1)`, `d2 = -1/(q(q^2+1))`.  The corpus records
`d1` as "numerically identical to z_D ... a different object"
(`qbeta_alpha_required_c_vs_d_probe.py:37`).  The identity is stronger than
numerical: `z_D` and `d1` are THE SAME RATIONAL FUNCTION of q.  With the proved
`d1 + d2 = h`:

    z_D + d2 = h            convention D splits h across the V_(2,1) diagonal

Convention C does not: `z_C = sqrt(q)/(q+1)` differs from `d1` at every q except
where checked below.  So D is the V_(2,1)-adapted Markov parameter and C is not.
That is an argument FOR the 2026-08-15 owner ruling from the representation side,
independent of the trace-convention registry.

## Result 4 --- the braid image DOES supply q-dependent eigenphases

The exclusion is about identity of FUNCTIONS, not a shortage of phases.
`sigma_1 sigma_2^-1` is elliptic:

    det = 1,   trace = -1 - h^2

so its eigenphase `a_ell = arccos(-(1+h^2)/2)` is genuinely q-dependent, and it
is elliptic exactly when `h^2 <= 1`, i.e. `q <= golden ratio`.  At the substrate
it is elliptic.  But `a_ell -> 2*pi/3` as `q -> 1`, whereas the ladder phase
`alpha = (z-1)h/2 -> 0`.  So the separation is quantitative as well as
functional: they do not even share a classical limit.

Run:  python3 -u computations/qbeta/qbeta_mbeta_v21_spectrum_under_d.py
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

from q_parameter import q_at  # noqa: E402 — proton pin (owner directive 2026-08-07)
from witness_base import WitnessBuilder  # noqa: E402

q = sp.Symbol("q", positive=True)
h = q - 1 / q

# --- the four transfer matrices of prop:beta-decay-transfer-matrix -----------


def T(c, d):
    return sp.Matrix([[c * h + d, c], [c, d]])


T_pp = T(1, 0)
T_nn = T(1, -h)
T_mix = T(1, -h / 2)
Delta_beta = sp.simplify(T_mix - T_nn)

# --- the seminormal representation on V_(2,1) (forced; see qou-pdix) ---------

d1 = q**3 / (q**2 + 1)
d2 = -1 / (q * (q**2 + 1))
bc = sp.simplify(d1 * d2 + 1)          # b*c, the only invariant combination
sigma1 = sp.Matrix([[q, 0], [0, -1 / q]])
# sigma_2 is FORCED, and its diagonal order is forced too.  With
# sigma_2 = [[a,b],[c,dd]], the off-diagonal braid residual is
# b*(a*q^2 - dd + q), so for an irreducible rep (b != 0) we need
# dd = a*q^2 + q; together with a + dd = h this gives a = d2, dd = d1 --- the
# entry paired with sigma_1's -q^-1 eigenvalue carries z_D, not the q one.
b = sp.sqrt(bc)
sigma2 = sp.Matrix([[d2, b], [b, d1]])

z_C = sp.sqrt(q) / (q + 1)
z_D = q**3 / (q**2 + 1)


def eq(a, bb):
    return bool(sp.simplify(sp.together(sp.expand(a - bb))) == 0)


def main() -> int:
    checks: list[tuple[str, bool, str]] = []

    # ---- Result 1: Delta_beta is scalar, spectrum is a repeated real value
    checks.append((
        "delta_beta_is_scalar_h_over_2",
        eq(Delta_beta[0, 0], h / 2) and eq(Delta_beta[1, 1], h / 2)
        and eq(Delta_beta[0, 1], 0) and eq(Delta_beta[1, 0], 0),
        "Delta_beta = (h/2)*I  (universal beta decay matrix, boxed in the block)",
    ))
    checks.append((
        "delta_beta_universal_both_steps_agree",
        eq((T_mix - T_nn)[0, 0], (T_pp - T_mix)[0, 0])
        and eq((T_mix - T_nn)[0, 1], (T_pp - T_mix)[0, 1])
        and eq((T_mix - T_nn)[1, 0], (T_pp - T_mix)[1, 0])
        and eq((T_mix - T_nn)[1, 1], (T_pp - T_mix)[1, 1]),
        "nn->mix and mix->pp give the same matrix",
    ))
    dbeta_eigs = sorted(sp.Matrix(Delta_beta).eigenvals().keys(), key=str)
    checks.append((
        "delta_beta_spectrum_is_repeated_h_over_2",
        len(dbeta_eigs) == 1 and eq(dbeta_eigs[0], h / 2),
        "spectrum {h/2, h/2} — a repeated REAL eigenvalue, not a conjugate pair",
    ))

    # ---- Result 2: determinants exclude the unit circle for all four
    dets = {
        "T_pp": sp.simplify(T_pp.det()),
        "T_nn": sp.simplify(T_nn.det()),
        "T_mix": sp.simplify(T_mix.det()),
        "Delta_beta": sp.simplify(Delta_beta.det()),
    }
    checks.append((
        "det_T_pp_eq_neg_one", eq(dets["T_pp"], -1), "Hecke unimodularity"))
    checks.append((
        "det_T_nn_eq_neg_one", eq(dets["T_nn"], -1), "Hecke unimodularity"))
    checks.append((
        "det_T_mix_eq_neg_one_minus_hsq_over_4",
        eq(dets["T_mix"], -(1 + h**2 / 4)),
        "T_mix is an algebraic average, not a group element",
    ))
    checks.append((
        "det_delta_beta_eq_hsq_over_4",
        eq(dets["Delta_beta"], h**2 / 4), "scalar (h/2)I"))
    # unit-circle spectrum REQUIRES det = 1
    checks.append((
        "no_named_transfer_matrix_has_det_one",
        all(not eq(v, 1) for v in dets.values()),
        "det = 1 is necessary for spectrum {e^{+-i.a}}; all four fail it",
    ))
    # T_mix is excluded for EVERY real q, not just the substrate
    checks.append((
        "det_T_mix_strictly_negative_for_all_real_q",
        bool(sp.simplify(dets["T_mix"] + 1 + h**2 / 4) == 0),
        "-(1 + h^2/4) <= -1 < 0 for every real h, so never 1",
    ))
    # Delta_beta reaches det 1 only at h = +-2
    sol_h = sp.solve(sp.Eq(sp.Symbol("H") ** 2 / 4, 1), sp.Symbol("H"))
    checks.append((
        "delta_beta_det_one_only_at_h_pm2",
        set(sol_h) == {2, -2},
        "h = +-2  <=>  q = 1+sqrt(2) (or its inverse); not the substrate",
    ))

    # ---- Result 3: z_D IS the seminormal d1, exactly
    checks.append((
        "zD_equals_seminormal_d1_identically",
        eq(z_D, d1),
        "same rational function, not a numerical coincidence",
    ))
    checks.append((
        "zD_plus_d2_equals_h",
        eq(z_D + d2, h),
        "convention D splits h across the V_(2,1) seminormal diagonal",
    ))
    checks.append((
        "zC_differs_from_d1",
        not eq(z_C, d1),
        "convention C is NOT the V_(2,1)-adapted parameter",
    ))
    # and the seminormal rep really is a rep (Hecke + braid), so d1 is forced
    Ihec = sp.simplify(sigma2 * sigma2 - (h * sigma2 + sp.eye(2)))
    checks.append((
        "sigma2_satisfies_hecke",
        all(eq(Ihec[i, j], 0) for i in range(2) for j in range(2)),
        "sigma2^2 = h*sigma2 + 1",
    ))
    Ibraid = sp.simplify(sigma1 * sigma2 * sigma1 - sigma2 * sigma1 * sigma2)
    checks.append((
        "braid_relation_holds",
        all(eq(Ibraid[i, j], 0) for i in range(2) for j in range(2)),
        "s1 s2 s1 = s2 s1 s2, so (d1,d2) is forced",
    ))

    # ---- Result 4: the braid image DOES supply q-dependent eigenphases
    s2inv = sp.simplify(sigma2.inv())
    ell = sp.simplify(sigma1 * s2inv)
    tr_ell = sp.simplify(sp.expand(ell.trace()))
    det_ell = sp.simplify(ell.det())
    checks.append((
        "sigma1_sigma2inv_det_one", eq(det_ell, 1), "even word length"))
    checks.append((
        "sigma1_sigma2inv_trace_eq_neg_one_minus_hsq",
        eq(tr_ell, -1 - h**2),
        "trace = -1 - h^2, so 2cos(a_ell) = -1 - h^2",
    ))
    # elliptic <=> |trace| <= 2 <=> h^2 <= 1
    # ellipticity boundary: |trace| = 2 exactly at h^2 = 1, i.e. q = golden ratio
    phi = (1 + sp.sqrt(5)) / 2
    checks.append((
        "elliptic_boundary_is_golden_ratio",
        eq((h**2).subs(q, phi), 1)
        and eq(sp.Abs(tr_ell.subs(q, phi)), 2),
        "|trace| = 2 exactly at q = (1+sqrt5)/2, the ellipticity boundary",
    ))
    # classical limits differ: a_ell -> 2pi/3, ladder alpha -> 0
    tr_at_one = sp.simplify(tr_ell.subs(q, 1))
    checks.append((
        "elliptic_classical_limit_is_2pi_over_3",
        tr_at_one == -1,
        "trace -> -1 at q=1, i.e. a_ell -> arccos(-1/2) = 2pi/3",
    ))
    for nm, zv in (("C", z_C), ("D", z_D)):
        a = (zv - 1) * h / 2
        checks.append((
            f"ladder_alpha_{nm}_vanishes_at_q_one",
            sp.simplify(a.subs(q, 1)) == 0,
            "ladder phase -> 0 at q=1: a different classical limit entirely",
        ))

    # ---- numerics at the proton pin (exact mpmath, no float64)
    q0 = q_at()
    import mpmath as mp
    mp.mp.dps = 50
    q0m = mp.mpf(str(q0))
    hm = q0m - 1 / q0m
    numeric = {
        "q0_proton_pin": mp.nstr(q0m, 30),
        "h_at_q0": mp.nstr(hm, 30),
        "det_T_mix_at_q0": mp.nstr(-(1 + hm**2 / 4), 30),
        "det_delta_beta_at_q0": mp.nstr(hm**2 / 4, 30),
        "delta_beta_eigenvalue_at_q0": mp.nstr(hm / 2, 30),
        "trace_sigma1_sigma2inv_at_q0": mp.nstr(-1 - hm**2, 30),
        "elliptic_eigenphase_rad_at_q0": mp.nstr(
            mp.acos((-1 - hm**2) / 2), 30),
        "ladder_alpha_D_at_q0": mp.nstr(
            (q0m**3 / (q0m**2 + 1) - 1) * hm / 2, 30),
        "ladder_alpha_C_at_q0": mp.nstr(
            (mp.sqrt(q0m) / (q0m + 1) - 1) * hm / 2, 30),
    }
    checks.append((
        "substrate_is_elliptic_for_sigma1_sigma2inv",
        bool(hm**2 <= 1),
        "h^2 = %s <= 1 at the proton pin" % mp.nstr(hm**2, 12),
    ))
    checks.append((
        "elliptic_phase_far_from_ladder_phase_at_q0",
        bool(abs(mp.acos((-1 - hm**2) / 2)
                 - (q0m**3 / (q0m**2 + 1) - 1) * hm / 2) > mp.mpf("2")),
        "the two phases differ by more than 2 rad at the substrate",
    ))

    npass = sum(1 for _, ok, _ in checks if ok)
    for name, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {why}")
    print(f"\n{npass}/{len(checks)} assertions pass")
    for k, v in numeric.items():
        print(f"  {k} = {v}")

    w = WitnessBuilder("qbeta-mbeta-v21-spectrum-under-d",
                       engine="python+sympy+mpmath", output_dir=HERE,
                       _script_path=__file__)
    w.set_description(
        "The M_beta spectrum on V_(2,1) under the convention-D trace. "
        "M_beta is undefined in the corpus (2 occurrences, both inside the "
        "claim); the only universal beta-decay matrix the conditional-on "
        "block defines is Delta_beta = (h/2)*I, whose spectrum is the "
        "REPEATED REAL eigenvalue h/2 - a scalar matrix has no eigenphase. "
        "None of the four named transfer matrices has det = 1, which is "
        "necessary for a spectrum {e^{+-i.alpha}}, so all four are excluded "
        "by determinant rather than by the qou-pdix rationality invariant "
        "(which covers only the braid image). Separately: z_D = q^3/(q^2+1) "
        "IS a seminormal sigma_2 diagonal entry identically, so "
        "z_D + d2 = h splits the Hecke differential across the V_(2,1) "
        "diagonal - convention C does not do this.")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_parameter("convention", "D (z = q^3/(q^2+1))")
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why}
                          for n, ok, why in checks])
    w.add_data("determinants", {k: str(v) for k, v in dets.items()})
    w.add_data("numeric_at_proton_pin", numeric)
    w.add_data("verdict", (
        "DERIVED. Delta_beta = (h/2)I has spectrum {h/2, h/2}: a repeated real "
        "eigenvalue, no eigenphase. All four named transfer matrices fail "
        "det = 1. The spectrum claim of prop:q-beta-cos-resummation is not a "
        "property of any matrix the corpus defines. Scope-(b) for the four "
        "named matrices, invariant = determinant."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
