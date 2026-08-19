#!/usr/bin/env python3
"""gram_mp_path_convention_d_migration_probe.py -- pyhecke.gram carried a
convention STRADDLE inside one module, and the fix is not a one-line z swap.

Bean `qou-cds2`. Owner directive this session: "d path. no float64."

WHAT WAS WRONG

`pyhecke.gram` migrated its float64 `z` to convention D on 2026-08-15 but left
the mpmath mirror on convention C:

    module float64 z   0.6126880371464652        convention D
    z_mp()             0.4993203341836944...     convention C     22.70 % apart

Both docstrings asserted they were "in lockstep". They were not, and had not
been for four days. Two further docstring claims were false in consequence:

  * `gram_matrix_mp` said it "agrees with `G` to ~1e-15". Measured gap: 0.172.
  * `z_mp` warned that splitting the mirror from the original "would be
    strictly worse than the stale convention" -- describing, in the present
    tense, the state the module was already in.

The C spelling involved is the detector-blind one catalogued in PR #5124:
`1/(sqrt(q) + 1/sqrt(q))` IS `sqrt(q)/(q+1)` exactly, so a grep for the
convention-C *form* does not find it.

WHY IT IS NOT A ONE-LINE SWAP -- the silent failure

Under D the mp Gram is EXACTLY singular (rank 5 of 6), as it is on the float64
side. `mp.lu_solve` does NOT raise on it. Swept over 20..120 dps it RETURNED at
every precision, with

    max|x| ~ 10^dps        (6.5e20 at 20 dps ... 1.5e120 at 120 dps)
    ||Gx - b|| ~ 1e-3      (visibly nonzero, but nothing raises)

i.e. the mpmath analogue of the numpy behaviour that blocked this migration
originally (`np.linalg.inv` returning 7.6e15 entries with ||G G^-1 - I|| =
1.64). One call arrangement DID raise ZeroDivisionError; that is the exception,
not the rule, and "it would raise, so we'd notice" is the wrong lesson.

WHAT THIS PROBE ESTABLISHES

1. The straddle is gone: |z - z_mp()| is now at float64 epsilon (4.1e-18), and
   `gram_matrix_mp` agrees with `G` to 2.1e-16 -- so the "~1e-15" docstring is
   TRUE again, restored rather than re-asserted.
2. `radical_mp` is the null direction and is float64-free: ||G . v|| is
   4.5e-62 at 60 dps and 1.7e-121 at 120 dps -- it tracks working precision,
   which is what an exact zero looks like in floating point.
3. `gram_quotient_solve_mp` is correct where `lu_solve` is not. On the identity
   NF it returns max|x| = 0.90 (against lu_solve's 2.9e50), solves the
   reachable part to 1.7e-51, is minimum-norm, and RETURNS the radical
   component instead of hiding it.
4. `gram_inverse_mp()` raises, mirroring `gram_inverse()`.

AND ONE FINDING THAT IS NOT A REPAIR

`qbeta_braid_nf_sdp_offset_probe` rests on "Since `G` is invertible (rank 6),
`G x = nf` fixes `x* = G^-1 nf` uniquely". Under D that premise is false, and
not marginally: BOTH anchors' NF vectors have a radical component of 47 % of
their norm (0.47268915 for each, identically). So `G x = nf` is UNSATISFIABLE
for both -- roughly half of each demand vector lies outside the range of G.

That probe's question is ill-posed under D, not merely harder to solve. This
probe therefore does NOT quietly re-solve it on the quotient and re-report an
offset angle: doing so would launder an unsatisfiable demand into a number.
Re-deriving it under D is separate work.

SCOPE -- what is deliberately NOT done here. 19 witness-emitting producers
consume the mp path (the mass chain among them: build_proton_mass_50dps_chain,
mass_formula_6term_mpfr_50dps, atomic_tr_m_*, paper_six_term_isotope_sweep,
rho_k_full_via_wenzl_lr, regenerate_y_lambda_mpfr). Their committed witnesses
are convention-C-frame and every one of them moves. That regeneration is a
bulk sweep with long-compute members and is NOT run here; it needs its own
scoped pass, as the qou-1c4y migration posture requires. Nothing downstream is
rewired, no value is wired, and no registry tier moves.

Anchor: proton (default). Every quantity is computed from the 50-dps q_0
string in mpmath; no float64 enters the mp path.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke import gram as g  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

#: The pre-migration convention-C value of `z_mp()`, for the straddle record.
Z_C_PRE_MIGRATION = mp.mpf("0.49932033418369445241344272")

DPS = 50


def _ident():
    return [mp.mpf(1)] + [mp.mpf(0)] * 5


def _braid_nf(reps):
    """NF of (sigma_1 sigma_2^-1)^reps -- the two SDP anchors."""
    nf = _ident()
    for _ in range(reps):
        nf = g.hm_mp(nf, 1, 0, 0)
        nf = g.hm_mp(nf, 1, -g.h_mp(), 1)
    return nf


def main() -> int:
    print("=" * 78)
    print(" pyhecke.gram mp path -- convention-D migration + the singular solve")
    print("=" * 78)

    zmp = g.z_mp(DPS)
    lockstep = abs(mp.mpf(g.z) - zmp)
    straddle = abs(zmp - Z_C_PRE_MIGRATION)

    print(f"\n  float64 z            {mp.nstr(mp.mpf(g.z), 20)}")
    print(f"  z_mp()  (after)      {mp.nstr(zmp, 20)}")
    print(f"  z_mp()  (before)     {mp.nstr(Z_C_PRE_MIGRATION, 20)}   <- convention C")
    print(f"  |z - z_mp|           {mp.nstr(lockstep, 6)}   <- lockstep restored")
    print(f"  pre-migration split  {float(abs(zmp - Z_C_PRE_MIGRATION) / Z_C_PRE_MIGRATION * 100):.4f} %")

    Gmp = g.gram_matrix_mp(DPS)
    # `g.G` IS float64 by design (it is the f64 path); mpmath ingests np.float64
    # directly and exactly, so no float() cast is needed to read it.
    agree = max(abs(mp.mpf(g.G[i][j]) - Gmp[i][j]) for i in range(6) for j in range(6))
    print(f"\n  max |G_f64 - gram_matrix_mp()|  {mp.nstr(agree, 6)}   (was 0.172 pre-migration)")

    print("\n  radical_mp is the null direction, and tracks precision:")
    rad_rows = {}
    for dps in (60, 120):
        G = mp.matrix(g.gram_matrix_mp(dps))
        v = mp.matrix(g.radical_mp(dps))
        nrm = max(abs(x) for x in (G * v))
        rad_rows[dps] = nrm
        print(f"    dps={dps:<5} ||G . radical_mp|| = {mp.nstr(nrm, 6)}")
    rad_types = sorted({type(x).__name__ for x in g.radical_mp(DPS)})
    print(f"    types: {rad_types}  <- no float64")

    print("\n  lu_solve vs gram_quotient_solve_mp on the identity NF:")
    G50 = mp.matrix(g.gram_matrix_mp(DPS))
    lu_rows = {}
    for dps in (20, 50, 120):
        Gd = mp.matrix(g.gram_matrix_mp(dps))
        with mp.workdps(dps):
            b = mp.matrix(_ident())
            try:
                x = mp.lu_solve(Gd, b)
                lu_rows[dps] = (mp.nstr(max(abs(t) for t in x), 6),
                                mp.nstr(max(abs(t) for t in (Gd * x - b)), 6))
            except ZeroDivisionError as exc:                       # pragma: no cover
                lu_rows[dps] = ("RAISED", str(exc))
        print(f"    lu_solve dps={dps:<5} max|x| = {lu_rows[dps][0]:<14} ||Gx-b|| = {lu_rows[dps][1]}")

    with mp.workdps(DPS):
        xq, radcomp = g.gram_quotient_solve_mp(_ident(), DPS)
        xm = mp.matrix(xq)
        v50 = mp.matrix(g.radical_mp(DPS))
        vv = mp.fsum(v50[i] * v50[i] for i in range(6))
        coeff = mp.fsum(v50[i] * _ident()[i] for i in range(6)) / vv
        bperp = mp.matrix([_ident()[i] - coeff * v50[i] for i in range(6)])
        q_maxx = max(abs(t) for t in xq)
        q_resid = max(abs(t) for t in (G50 * xm - bperp))
        q_minnorm = abs(mp.fsum(xq[i] * v50[i] for i in range(6)))
    print(f"    quotient          max|x| = {mp.nstr(q_maxx, 6):<14} "
          f"||Gx-b_perp|| = {mp.nstr(q_resid, 6)}")
    print(f"                      radical component = {mp.nstr(radcomp, 6)} "
          f"(nonzero => no exact solution exists)")

    guard_ok = False
    try:
        g.gram_inverse_mp()
    except NotImplementedError:
        guard_ok = True
    print(f"\n  gram_inverse_mp() raises NotImplementedError: {guard_ok}")

    print("\n  SDP-probe premise under D -- both anchors' NF radical components:")
    anch = {}
    with mp.workdps(DPS):
        for name, reps in (("muon_4_1", 2), ("proton_B_3", 3)):
            nf = _braid_nf(reps)
            nfm = mp.matrix(nf)
            c = mp.fsum(v50[i] * nfm[i] for i in range(6)) / vv
            rc = c * mp.sqrt(vv)
            nrm = mp.sqrt(mp.fsum(t * t for t in nf))
            anch[name] = (rc, nrm, abs(rc) / nrm)
            print(f"    {name:<12} ||nf|| = {mp.nstr(nrm, 8):<12} "
                  f"radical = {mp.nstr(rc, 8):<12} rel = {float(abs(rc)/nrm)*100:.2f} %")

    print(f"""
{'=' * 78}
 Reading
{'=' * 78}

  The module had convention C and convention D 22.70 % apart inside itself,
  with both docstrings claiming lockstep. That is now fixed, and the fix is
  checkable: the "agrees with G to ~1e-15" claim went from FALSE (0.172) to
  TRUE ({mp.nstr(agree, 3)}).

  The reason it was not a one-line swap: under D the mp Gram is singular and
  mp.lu_solve does not say so -- it returns 10^dps-sized garbage at every
  precision tested. gram_quotient_solve_mp returns the honest object plus the
  radical component the caller cannot reach.

  NOT repaired here: qbeta_braid_nf_sdp_offset_probe assumes G is invertible.
  Both its anchors are 47 % radical, so G x = nf is unsatisfiable under D and
  the question is ill-posed, not merely harder. Re-solving it on the quotient
  and reporting an angle would launder that -- so it is left for separate work.

  NOT run here: the 19 witness-emitting producers downstream of the mp path.
  Their committed values are C-frame and all move; that is a scoped bulk sweep.
""")

    wb = WitnessBuilder("gram-mp-path-convention-d-migration", engine="mpmath")
    wb.set_description(
        "pyhecke.gram carried a convention straddle inside one module: the "
        "float64 z moved to convention D on 2026-08-15 while the mpmath mirror "
        "(z_mp, tr_m_mp, gram_matrix_mp) stayed on C, 22.70 % apart, with both "
        "docstrings asserting lockstep and gram_matrix_mp claiming a ~1e-15 "
        "agreement with G whose true gap was 0.172. The C spelling was the "
        "detector-blind 1/(sqrt(q)+1/sqrt(q)) = sqrt(q)/(q+1) catalogued in PR "
        "#5124. Migrated to D, float64-free. It is NOT a one-line swap: under D "
        "the mp Gram is exactly singular and mp.lu_solve does not raise -- swept "
        "20..120 dps it returned max|x| ~ 10^dps with residual ~1e-3 at every "
        "precision, the mpmath analogue of the numpy behaviour that blocked this "
        "migration originally. Adds the float64-free quotient API mirroring the "
        "f64 side: radical_mp (the proved q-antisymmetriser), "
        "gram_quotient_solve_mp (minimum-norm solve on H_3(q)/rad, returning the "
        "unreachable radical component rather than hiding it), and "
        "gram_inverse_mp (raises, like gram_inverse). SEPARATE FINDING, not "
        "repaired: qbeta_braid_nf_sdp_offset_probe assumes G is invertible "
        "(rank 6); under D both its anchors carry a 47 % radical component, so "
        "G x = nf is UNSATISFIABLE and its question is ill-posed -- re-solving on "
        "the quotient and reporting an angle would launder that. NOT RUN: the 19 "
        "witness-emitting downstream producers whose committed values are C-frame "
        "and all move; that is a scoped bulk sweep. No value wired, no tier moved."
    )
    wb.add_data("convention", "D (z = q^3/(q^2+1))")
    wb.add_data("z", {
        "float64_module_z": repr(g.z),
        "z_mp_after": fmt(zmp),
        "z_mp_before_convention_C": fmt(Z_C_PRE_MIGRATION),
        "lockstep_abs_gap": fmt(lockstep),
        "pre_migration_split_pct": fmt(abs(zmp - Z_C_PRE_MIGRATION) / Z_C_PRE_MIGRATION * 100),
    })
    wb.add_data("gram_f64_vs_mp_max_abs_diff", fmt(agree))
    wb.add_data("gram_f64_vs_mp_max_abs_diff_pre_migration", "0.17218519")
    wb.add_data("radical_mp_residual", {str(k): fmt(v) for k, v in rad_rows.items()})
    wb.add_data("radical_mp_types", rad_types)
    wb.add_data("lu_solve_sweep", {str(k): {"max_abs_x": v[0], "residual": v[1]}
                                   for k, v in lu_rows.items()})
    wb.add_data("quotient_solve", {
        "max_abs_x": fmt(q_maxx),
        "residual_vs_b_perp": fmt(q_resid),
        "min_norm_dot_radical": fmt(q_minnorm),
        "radical_component": fmt(radcomp),
    })
    wb.add_data("sdp_probe_anchors_radical_fraction", {
        k: {"radical_component": fmt(v[0]), "nf_norm": fmt(v[1]),
            "relative": fmt(v[2])} for k, v in anch.items()
    })
    wb.add_data("downstream_witness_producers_not_regenerated", 19)
    wb.add_data("closes_cds2", False)

    tol = mp.mpf(10) ** -15
    wb.add_assertion(
        name="mp_path_and_f64_path_are_now_the_same_convention",
        computed=str(int(lockstep < tol and straddle > mp.mpf("0.1"))),
        expected="1", tolerance=0,
        source=f"|z - z_mp()| = {mp.nstr(lockstep, 6)} (float64 epsilon scale) "
               f"while the pre-migration mp value differed from the f64 one by "
               f"{float(abs(zmp - Z_C_PRE_MIGRATION) / Z_C_PRE_MIGRATION * 100):.4f} %. "
               "Both halves are asserted: the gap is closed now, AND it was "
               "genuinely open before -- so this cannot pass by the two paths "
               "having always agreed.",
    )
    wb.add_assertion(
        name="gram_matrix_mp_agrees_with_G_as_its_docstring_claims",
        computed=str(int(agree < mp.mpf(10) ** -14)),
        expected="1", tolerance=0,
        source=f"max |G_f64 - gram_matrix_mp()| = {mp.nstr(agree, 6)}, against the "
               "docstring's '~1e-15'. Pre-migration this was 0.172 -- the claim "
               "was false while the module straddled conventions, and is restored "
               "by the migration rather than merely re-asserted.",
    )
    wb.add_assertion(
        name="lu_solve_fails_SILENTLY_on_the_singular_D_gram_at_every_precision",
        computed=str(int(all(v[0] != "RAISED" and mp.mpf(v[0]) > mp.mpf(10) ** 15
                             for v in lu_rows.values()))),
        expected="1", tolerance=0,
        source="swept 20/50/120 dps: lu_solve RETURNED at every precision with "
               f"max|x| = {', '.join(v[0] for v in lu_rows.values())} and a "
               "visibly nonzero residual (~1e-3), never raising. This is why the "
               "convention swap could not be one line -- and why 'it would raise, "
               "so we would notice' is the wrong lesson.",
    )
    wb.add_assertion(
        name="quotient_solve_is_sane_where_lu_solve_is_not",
        computed=str(int(q_maxx < mp.mpf(10) and q_resid < mp.mpf(10) ** -40
                         and q_minnorm < mp.mpf(10) ** -40 and guard_ok)),
        expected="1", tolerance=0,
        source=f"gram_quotient_solve_mp on the identity NF: max|x| = "
               f"{mp.nstr(q_maxx, 6)} (lu_solve gave {lu_rows[50][0]}), residual "
               f"against the reachable part {mp.nstr(q_resid, 6)}, minimum-norm "
               f"(x . radical = {mp.nstr(q_minnorm, 6)}), and it returns the "
               f"radical component {mp.nstr(radcomp, 6)} rather than hiding it. "
               f"gram_inverse_mp() raises: {guard_ok}.",
    )
    wb.add_assertion(
        name="sdp_probe_premise_G_invertible_is_FALSE_under_D_for_both_anchors",
        computed=str(int(all(v[2] > mp.mpf("0.4") for v in anch.values()))),
        expected="1", tolerance=0,
        source="qbeta_braid_nf_sdp_offset_probe states 'Since G is invertible "
               "(rank 6), G x = nf fixes x* uniquely'. Under D both anchors carry "
               f"a radical component of {float(anch['muon_4_1'][2])*100:.2f} % "
               f"(muon) and {float(anch['proton_B_3'][2])*100:.2f} % (proton) of "
               "their NF norm, so G x = nf is UNSATISFIABLE for both. The question "
               "is ill-posed under D, not merely harder; this probe deliberately "
               "does not re-solve it on the quotient and report an angle.",
    )
    out = wb.save({"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR})
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
