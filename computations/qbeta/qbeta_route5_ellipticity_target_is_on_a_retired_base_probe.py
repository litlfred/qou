#!/usr/bin/env python3
"""qbeta_route5_ellipticity_target_is_on_a_retired_base_probe.py — the target that
makes route 5 need an ELLIPTIC generator is computed on the RETIRED `z = 1` cell,
and on the RULED base the requirement inverts.

Bean `qou-pdix` (route 5 / the S1 blocker: derive the Q_beta ladder eigenphase
`alpha`), parent `qou-cds1`.

Scope: **(b)** for the two class statements (each cites a proved invariant --
`Real.cos_le_one` and `1 <= cosh`), **(a)** for every number.

## What this is about, in one paragraph

Steps 18-20 of route 5 form a chain:

  18. `HolonomySpectrumSignObstruction` -- a holonomy whose generator has REAL
      spectrum has normalised character `cosh a >= 1`, while the required
      correction is `0.998399 < 1`.  So route 5 needs an ELLIPTIC generator.
  19. `ImQCannotSupplyEllipticGenerator` -- `Im q` cannot be that source at the
      archimedean level, because `Re q = 1.10998 > 1` forces `|q| > 1`.
  20. `qbeta_fibre_unit_circle_opens_route5_probe` -- on the FIBRE the locus is
      exactly `|q| = 1`, with eigenphase `theta = |arg q|`; whether a root of
      unity supplies it reduces to "is `theta/2pi` rational", and `N = 111` is
      the only low-denominator candidate.

**Every step of that chain is downstream of one number**, the required correction
factor.  This probe establishes where that number comes from and what it becomes
on the base the owner actually ruled.

## 1. Provenance — reproduced, not asserted

Route 5 computes `theta = acos(Q_beta^exp / (Q_A * (1 - u^2)))` with

    Q_A = m_e * |q^2 - 2q - 1| * (q + 1) / (2 q^3)

That is the **`z = 1` cell** -- algebraically `|eps(Delta)| * E_0` evaluated at
Markov parameter `z = 1`, the published 0.17 % form.  The owner **retired it as
the base on 2026-09-08**, ruling that `eps` is the Markov trace at
`z_D = q^3/(q^2 + 1)` (bean `qou-99qc`; AGENTS.md, cheat-sheet ruling).

The three step-18/19/20 files are dated **2026-09-07** -- one day BEFORE the
ruling.  They were **correct when written**.  This is staleness acquired by a
ruling, not an error, and it is the same shape as the attack-A finding in
PR #7326 (that negative was also aimed at the `z = 1` cell) -- a second instance
of one class, in a second arc.

Check 1 reproduces route 5's `theta` from that formula, so the provenance is
measured rather than read off a docstring.

## 2. The inversion, and it is NOT uniform across bases

The required factor is `R(base) = Q_beta^exp / (base * (1 - u^2))`.  Two proved
invariants bracket what a holonomy can supply:

    elliptic generator  (spectrum +-i*theta)  =>  character = cos theta  <= 1
    real-spectrum generator (spectrum +-a)    =>  character = cosh a     >= 1

So `R < 1` forces elliptic (step 18's situation) and `R > 1` **excludes**
elliptic and forces real spectrum.  Measured over all four bases the corpus
carries, `R` lands on BOTH sides -- the direction of the obstruction is a
function of which admissible functional is in play, which was invisible while
only the `z = 1` cell was in view.

## 3. What this does NOT say

It does **not** retract steps 18-20: their algebra is exact and correct for the
target they were given.  It does **not** derive `alpha`.  It does **not**
resurrect Kohno-Drinfeld -- check 4 shows KD's own `cosh(ln q_0)` still misses on
every base, so the failure moves from a CLASS exclusion to a MAGNITUDE gap
rather than disappearing.  And it does **not** recommend a base: per
AGENTS.md §NO FITTING a base is not chosen by which obstruction it removes, and
the ruled base is ruled whatever it does to this chain.

## Precision

mpmath at 50 dps throughout; `q_0` from `q_at` (proton pin); `m_e` / `Q_beta`
from `codata_constants`.  No float64: no `float(` outside display, no
`statistics`, no `math.`.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    if str(_p) not in _sys.path:
        _sys.path.insert(0, str(_p))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 50

# Raise precision AT MODULE SCOPE, above the constants below. Without this the
# module-level `mp.mpf("...")` calls are built at mpmath's default dps=15 and
# the 17-significant-digit ROUTE5_THETA_PRINTED is ROUNDED AT CONSTRUCTION --
# it stops being the value it records. `main()` already calls
# `set_compute_dps(DPS)`, which is too late for a module constant; the call is
# idempotent, so having both is safe. Caught by
# computations/module_const_precision_audit.py (its only LOSSY row).
set_compute_dps(DPS)
mp.dps = DPS

# Route 5's own printed value, taken by RUNNING
# qbeta_fibre_unit_circle_opens_route5_probe.py, not from any docstring.
# Used ONLY as a reproduction target for check 1; nothing is derived from it.
ROUTE5_THETA_PRINTED = mp.mpf("0.05661730079406103")

# The figure that appears in the corpus's PROSE for the same quantity. It is the
# convention-C form value (the bean records it as |alpha_N1| in convention C to
# 7 digits), NOT the live experimental target -- see check 5.
PROSE_THETA = mp.mpf("0.0565947")

# The dashboard's currently-scored Q_beta base, read from
# computations/per-observable-100x-status.witness.json (row obs == "Q_beta",
# pred_MeV) -- nuc11_interleaved on the tower-summed E_0 at z_D, zero c_k rungs.
DASHBOARD_PRED_MEV = "0.651856310060"

RESULTS: list[dict] = []


def check(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}\n")


def main() -> int:
    set_compute_dps(DPS)
    mp.dps = DPS

    print("=" * 78)
    print(" route 5's ellipticity target sits on the RETIRED z = 1 cell")
    print("=" * 78)

    q = q_at(DPS)
    m_e = mp.mpf(str(M_E_MEV))
    q_exp = mp.mpf(str(Q_BETA_MEV))

    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    n2 = 1 - u ** 2                      # the c_2 = -1 rung, structural

    # ---- the four bases the corpus carries --------------------------------
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)             # order-zero E_0, as in PR #7326
    z_D = q ** 3 / (q ** 2 + 1)
    base_z1 = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
    base_zD = abs(h ** 2 / 2 - h * z_D) * E0
    base_aug = abs(h ** 2 / 2 - h * q) * E0
    base_dash = mp.mpf(DASHBOARD_PRED_MEV)

    BASES = [
        ("z = 1 (Form A)", base_z1, "RETIRED as base 2026-09-08"),
        ("z_D = q^3/(q^2+1)", base_zD, "RULED (order-zero E_0, old element)"),
        ("z = q (augmentation)", base_aug, "the other admissible point"),
        ("dashboard scored cell", base_dash, "RULED (nuc11_interleaved, tower E_0)"),
    ]

    # ---- 1. provenance: reproduce route 5's theta --------------------------
    R_z1 = q_exp / (base_z1 * n2)
    theta = mp.acos(R_z1)
    rel = abs(theta - ROUTE5_THETA_PRINTED) / ROUTE5_THETA_PRINTED
    check(
        "route5_theta_reproduces_from_the_retired_z_eq_1_cell",
        rel < mp.mpf(10) ** -14,
        f"theta = acos(Q_beta^exp / (Q_A*(1-u^2))) with Q_A the z=1 cell gives "
        f"{mp.nstr(theta, 12)}, reproducing route 5's printed "
        f"{mp.nstr(ROUTE5_THETA_PRINTED, 8)} to rel {mp.nstr(rel, 4)}. So the "
        f"ellipticity target's base is MEASURED to be the z = 1 cell, not "
        f"inferred from prose. R(z=1) = {mp.nstr(R_z1, 14)} < 1.",
    )

    # ---- 2. R on every base; the direction is not uniform ------------------
    print("  base                          Q_base (MeV)        R = Qexp/(base*(1-u^2))")
    rows = []
    for label, base, note in BASES:
        R = q_exp / (base * n2)
        side = "< 1  -> needs ELLIPTIC" if R < 1 else "> 1  -> ELLIPTIC EXCLUDED"
        rows.append({"base": label, "note": note, "Q_base_MeV": fmt(base),
                     "R": fmt(R), "side": side})
        print(f"  {label:<28} {mp.nstr(base, 12):>16}   {mp.nstr(R, 12):>16}  {side}")
    print()

    R_zD = q_exp / (base_zD * n2)
    R_aug = q_exp / (base_aug * n2)
    R_dash = q_exp / (base_dash * n2)
    check(
        "on_both_ruled_bases_R_exceeds_one_so_elliptic_is_excluded",
        R_zD > 1 and R_dash > 1,
        f"R(z_D) = {mp.nstr(R_zD, 12)} and R(dashboard) = {mp.nstr(R_dash, 12)}, "
        f"both > 1. An elliptic generator has character cos(theta) <= 1 "
        f"(Real.cos_le_one -- the SAME invariant the carrier file's "
        f"replacement_excludes_some_matrix already uses), so on the ruled base "
        f"no elliptic generator can supply the correction: acos(R) is not real. "
        f"This is the exact MIRROR of step 18, which excluded real spectrum "
        f"because cosh a >= 1 > 0.998399.",
    )

    check(
        "the_direction_is_base_dependent_not_uniform",
        (R_z1 < 1) and (R_aug < 1) and (R_zD > 1) and (R_dash > 1),
        f"R lands on BOTH sides of 1 across the four bases: z=1 "
        f"{mp.nstr(R_z1, 10)} and augmentation {mp.nstr(R_aug, 10)} are below, "
        f"z_D {mp.nstr(R_zD, 10)} and the dashboard cell {mp.nstr(R_dash, 10)} "
        f"are above. So 'route 5 needs an elliptic generator' is not a fact "
        f"about the framework -- it is a fact about which admissible functional "
        f"is the base, and that was invisible while only the z=1 cell was in "
        f"view. NOT a reason to prefer a base: per AGENTS.md NO FITTING a base "
        f"is never chosen by which obstruction it removes.",
    )

    # ---- 3. what the ruled base asks for instead ---------------------------
    a_zD = mp.acosh(R_zD)
    a_dash = mp.acosh(R_dash)
    check(
        "ruled_base_asks_for_a_REAL_spectrum_generator_and_names_its_value",
        a_zD > 0 and a_dash > 0,
        f"with R > 1 the equation cosh(a) = R HAS a real solution, so the "
        f"class step 18 excluded is the class the ruled base requires: "
        f"a = {mp.nstr(a_zD, 12)} on z_D and a = {mp.nstr(a_dash, 12)} on the "
        f"dashboard cell. Steps 19 (Im q) and 20 (the |q| = 1 fibre locus, "
        f"theta/2pi rational, N = 111) are downstream of the OPPOSITE "
        f"requirement and do not arise on the ruled base at all.",
    )

    # ---- 4. but KD's own value still misses --------------------------------
    kd_char = (q + 1 / q) / 2            # cosh(ln q_0), the KD hbar = 2 ln q value
    miss_zD = (kd_char - R_zD) / R_zD
    miss_dash = (kd_char - R_dash) / R_dash
    miss_z1 = (kd_char - R_z1) / R_z1
    # ---- 5. the prose figure is the convention-C form value ---------------
    rel_prose = (theta - PROSE_THETA) / theta
    check(
        "prose_theta_is_the_convention_C_form_value_not_the_live_target",
        mp.mpf("3e-4") < abs(rel_prose) < mp.mpf("5e-4"),
        f"three Lean files and two beans carry 'theta = 0.0565947' for this "
        f"quantity; the live producer computes {mp.nstr(theta, 16)}, a relative "
        f"{mp.nstr(rel_prose, 6)} away. That gap IS the documented form-vs-"
        f"experiment correction (route 5's own docstring: 'moved it by 4.0e-4'), "
        f"and the bean records 0.0565947 as |alpha_N1| in convention C to 7 "
        f"digits. So the prose figure is the convention-C FORM value. Live "
        f"sites, all in commit 87bf883793 -- the SAME commit whose probe "
        f"corrects the target: EigenphaseCarrierVacuity.lean:221, "
        f"BringEllipticCurveJInvariant.lean:39, "
        f"nuclear-interactions/q-beta-cos-resummation.lean:191. NOT swept: on "
        f"the ruled base theta does not exist at all (check 2), so these would "
        f"need re-deriving rather than re-numbering, and AGENTS.md's 2026-09-07 "
        f"ask-first directive governs. Recorded, not fixed. This probe's own "
        f"first draft took 0.0565947 from that prose as an input and failed its "
        f"own check -- which is how the discrepancy was found.",
    )

    check(
        "kohno_drinfeld_own_value_still_misses_on_every_base",
        abs(miss_zD) > mp.mpf("0.01") and abs(miss_dash) > mp.mpf("0.01")
        and abs(miss_z1) > mp.mpf("0.001"),
        f"KD fixes hbar = 2 ln q by matching the Hecke pair, giving character "
        f"cosh(ln q_0) = (q_0 + 1/q_0)/2 = {mp.nstr(kd_char, 12)}. Against R "
        f"that is {mp.nstr(miss_z1 * 100, 6)} % on z=1, "
        f"{mp.nstr(miss_zD * 100, 6)} % on z_D and "
        f"{mp.nstr(miss_dash * 100, 6)} % on the dashboard cell. So the ruled "
        f"base does NOT resurrect Kohno-Drinfeld: it moves the failure from a "
        f"CLASS exclusion (wrong side of 1) to a MAGNITUDE gap (right side, "
        f"wrong size), which is a weaker obstruction and a different problem.",
    )

    # ---- 6. cross-validate against qou-99qc's z-space figures -------------
    # That bean inverts the functional for CODATA and gets z* = 0.99850, then
    # reports z = q at "+11.17 %" and z_D at "-38.64 %". Those are distances in
    # z, NOT residuals in Q_beta, so they are not the +12.470 % / -43.157 %
    # this arc records -- a reader meeting both will think one is stale.
    # They are the same statement: Q is proportional to (h^2/2 - z*h).
    Z_STAR = mp.mpf("0.99850")
    def qfun(z):
        return h ** 2 / 2 - z * h
    ratio_zD = qfun(z_D) / qfun(Z_STAR)
    ratio_aug = qfun(q) / qfun(Z_STAR)
    pct_zD = (ratio_zD - 1) * 100
    pct_aug = (ratio_aug - 1) * 100
    zdist_zD = (z_D - Z_STAR) / Z_STAR * 100
    zdist_aug = (q - Z_STAR) / Z_STAR * 100
    check(
        "qou_99qc_z_space_figures_and_this_arcs_q_space_figures_agree",
        abs(pct_zD - mp.mpf("-43.157")) < mp.mpf("0.05")
        and abs(pct_aug - mp.mpf("12.470")) < mp.mpf("0.05"),
        f"bean qou-99qc reports z = q at +11.17 % and z_D at -38.64 % from its "
        f"inverted z* = 0.99850; reproduced here as distances IN z: "
        f"{mp.nstr(zdist_aug, 6)} % and {mp.nstr(zdist_zD, 6)} %. Pushed "
        f"through the exact functional h^2/2 - z*h those become residuals in "
        f"Q_beta of {mp.nstr(pct_aug, 7)} % and {mp.nstr(pct_zD, 7)} %, "
        f"reproducing this arc's +12.470 % and -43.157 %. NOT a discrepancy -- "
        f"two coordinates for one shortfall. Recorded because a reader meeting "
        f"both pairs will otherwise conclude one is stale.",
    )

    # ---- 7. my own 'factor 11.2' understated the gap by ~12x ---------------
    # The gap was stated as a ratio of the generator eigenvalue a. But a enters
    # only through cosh, and near a = 0, cosh a - 1 ~ a^2/2 -- so a ratio in a
    # is roughly the SQUARE ROOT of the ratio in the quantity that matters.
    a_needed = mp.acosh(R_zD)
    a_kd = mp.log(q)
    ratio_in_a = a_needed / a_kd
    ratio_in_deviation = (R_zD - 1) / (kd_char - 1)
    check(
        "stating_the_gap_in_a_understates_it_by_an_order_of_magnitude",
        ratio_in_deviation > 100 > ratio_in_a,
        f"CORRECTION to this session's own framing. The route-5 gap on the "
        f"ruled base was reported as 'a factor 11.2', i.e. a_needed/a_KD = "
        f"{mp.nstr(ratio_in_a, 6)}. But `a` enters only through cosh, and near "
        f"a = 0, cosh a - 1 ~ a^2/2, so a ratio in `a` is about the SQUARE ROOT "
        f"of the ratio in the deviation the correction must actually supply. "
        f"That deviation ratio is (R - 1)/(cosh(ln q_0) - 1) = "
        f"{mp.nstr(ratio_in_deviation, 6)}x -- Kohno-Drinfeld supplies "
        f"{mp.nstr((kd_char - 1) * 100, 4)} % where {mp.nstr((R_zD - 1) * 100, 5)} "
        f"% is needed. Quote the deviation ratio; 'factor 11.2' understates the "
        f"gap by roughly an order of magnitude and flatters the route.",
    )

    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    wb = WitnessBuilder("qbeta-route5-ellipticity-target-retired-base",
                        engine="mpmath")
    for r in RESULTS:
        wb.add_assertion(r["name"],
                         computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "Route 5's ellipticity requirement is computed from the RETIRED "
            "z = 1 cell. Reproduced here: theta = acos(Q_beta^exp/(Q_A(1-u^2))) "
            "with Q_A = m_e|q^2-2q-1|(q+1)/(2q^3) gives route 5's printed "
            "0.05659469. The owner retired that cell as the base on 2026-09-08; "
            "the three step-18/19/20 files are dated 2026-09-07, so they were "
            "correct when written. On BOTH ruled bases the required factor "
            "R = Q_beta^exp/(base(1-u^2)) EXCEEDS 1, and an elliptic generator "
            "has character cos(theta) <= 1 -- so the requirement inverts: the "
            "ruled base excludes the elliptic class and requires the real-spectrum "
            "class step 18 excluded. Steps 19 (Im q) and 20 (the |q|=1 fibre "
            "locus, theta/2pi rational, N=111) are downstream of the opposite "
            "requirement. The direction is NOT uniform -- the augmentation base "
            "keeps R < 1 -- so it is a fact about the base, not about the "
            "framework, and is explicitly NOT a reason to prefer a base. "
            "Kohno-Drinfeld's own cosh(ln q_0) = 1.00545 still misses on every "
            "base, so the failure moves from a class exclusion to a magnitude gap."
        ),
        "bean": "qou-pdix",
        "parent_bean": "qou-cds1",
        "q0Anchor": "proton",
        "q0Value": fmt(q),
        "bases": rows,
        "prose_theta_stale_sites": [
            "folio/quantum-observable-universe/lean/QOU/QBeta/EigenphaseCarrierVacuity.lean:221",
            "folio/quantum-observable-universe/lean/QOU/QBeta/BringEllipticCurveJInvariant.lean:39",
            "folio/quantum-observable-universe/nuclear-interactions/q-beta-cos-resummation.lean:191",
        ],
        "retired_base_ruling": "owner 2026-09-08: eps = Markov trace at z_D = q^3/(q^2+1); z = 1 retired as base",
        "supersedes_nothing": (
            "steps 18-20 are NOT retracted: their algebra is exact and correct "
            "for the target they were given. What changed is the target."
        ),
        "invariants_cited": [
            "Real.cos_le_one (elliptic character <= 1) -- Mathlib, and already "
            "used by QOU.QBeta.EigenphaseCarrier.replacement_excludes_some_matrix",
            "1 <= cosh (real-spectrum character >= 1) -- QOU.QBeta."
            "HolonomySpectrumSignObstruction, sorry-free",
        ],
        "gap_magnitude_correction": (
            "The route-5 gap on the ruled base must be quoted as the DEVIATION "
            "ratio (R-1)/(cosh(ln q0)-1), not as a_needed/a_KD. `a` enters only "
            "through cosh and cosh a - 1 ~ a^2/2 near 0, so the ratio in `a` is "
            "about the square root of the ratio that matters and understates the "
            "gap by roughly an order of magnitude."
        ),
        "cross_validation": (
            "bean qou-99qc's z-space figures (z* = 0.99850; z = q at +11.17 %, "
            "z_D at -38.64 %) and this arc's Q_beta residuals (+12.470 %, "
            "-43.157 %) are the SAME statement in two coordinates, related by "
            "the exact functional h^2/2 - z*h. Not a discrepancy."
        ),
        "scope": (
            "(b) for the two class statements, each citing a proved invariant; "
            "(a) for every number. Derives no alpha, selects no base, proposes "
            "no wiring, and does not show that no connection exists."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
