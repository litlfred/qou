#!/usr/bin/env python3
"""qbeta_ruled_base_inverts_the_route5_obstruction_probe.py -- the step-18
obstruction's HYPOTHESIS is false on the ruled base, so route 5's narrowing to an
elliptic generator is void, and the requirement now points at the HYPERBOLIC
generator the substrate already has.

Beans `qou-pdix` / `qou-cds1`, route 5.  Scope-(b) for the exclusion it reverses
-- two proved invariants, both already sorry-free in this corpus -- and (a) for
every number.

## What was established, and on which base

`qbeta_holonomy_spectrum_sign_obstruction_probe` (step 18) reads the ladder's
correction as the normalised character of a holonomy and argues:

    a generator with REAL spectrum +-a has character cosh(a) >= 1 for every real
    a; the required correction is BELOW 1; therefore the generator cannot have
    real spectrum.

Its own words: *"1.005448 against a required 0.998399: wrong SIDE of 1."*  Step
19 then refuted Im(q) as the source of the needed ellipticity at the archimedean
level, and `qbeta_fibre_unit_circle_opens_route5_probe` carried the surviving
question to the fibre, where `det A > 0 <=> |q| = 1` selects the Kashaev locus
and reduces to whether `theta/2pi` is rational (the N = 111 question).

**That whole chain rests on `required < 1`.**  This probe measures the premise.

## What this measures

`0.998399` is the requirement on the **retired** `z = 1` cell.  Reproduced here
to 7 digits as a calibration, so what follows is about the same object.

On the base the owner ruled on 2026-09-08 (`eps := tr_M` at `z_D`, bean
`qou-99qc`) the requirement is **above** 1 -- 1.7594 at the order-zero `E_0`,
1.2002 on the dashboard's scored `nuc11` cell.  So

    correction_below_one_excludes_real_spectrum  (hκ : κ < 1)

does not apply.  The Lean is untouched and correct: it is a conditional, and it
was always stated as one.  What changed is its **premise** -- the
"conditional-proved != premise-established" pattern AGENTS.md names, here in the
direction where the corpus stated the conditional properly and the surrounding
prose then treated the hypothesis as settled.

## And the requirement now points the other way

Two proved inequalities, taken together on the ruled base:

  * `real_spectrum_character_ge_one` (step 18, sorry-free): hyperbolic => >= 1.
  * `ladderN2_lt_of_one_le` (`QOU/QBeta/LadderFactorBound.lean`, sorry-free, this
    PR): the elliptic/cos form is `< F` whenever `1 <= F`.

On a base needing more than 1 it is the **elliptic** generator that is excluded
and the **hyperbolic** one that is not -- the exact reverse of route 5's current
narrowing.  The substrate's own Kohno-Drinfeld generator is already hyperbolic at
real `q_0` (`hbar = 2 ln q`, `det A = -(ln q)^2 < 0`), which step 18 recorded as
the defect.  It is no longer a defect.

**This does NOT say the KD holonomy supplies the correction.**  Its character at
`q_0` is 1.00544843 against 1.75936460 required -- right side, wrong size.  That
is a scope-(a) quantitative gap and stays open.

## A coordinate note, and it resolves a live disagreement

The residual gap has at least three spellings and they differ by an order of
magnitude:

    generator eigenvalue   a_req / a_KD        = 11.168
    character excess       (kappa-1)/(KD-1)    = 139.373
    character ratio        kappa / KD          =  1.7498

A sibling branch reported "the route-5 gap is 139x, not the factor 11.2 I
reported an hour ago".  **Both numbers are right and they are the same gap**;
the second is not a correction of the first, it is a change of coordinate.  With
`c_k` (magnifier `1/u^2 = 13784.87`) and `1 - F` this arc now has five
coordinates for one deviation, and every confusion in it so far has been about
which one is in use.

## Discipline

The required character and generator eigenvalue are recorded as quantities to
check AGAINST.  No search was run for a construction producing them, and none
should be until something independent selects one.  This probe derives no alpha,
adjudicates no convention, chooses no base -- per NO FITTING, that the ruled base
makes the step-18 exclusion lapse is not a reason to prefer or disprefer it -- and
wires nothing.

## Precision

mpmath at 50 dps; `q_0` from `q_at` (proton pin); `m_e` / `Q_beta` from
`codata_constants`.  No float64: no `float(` outside display, no `statistics`,
no `math.`.
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

# Dashboard's currently-scored Q_beta prediction (per-observable-100x-status,
# row obs == "Q_beta"); and step 18's own quoted figures, for calibration.
_EXPECTED_PREFIX = "0.651856310060"
STEP18_QUOTED_REQUIRED = "0.998399"
STEP18_QUOTED_KD = "1.005448"

def _dashboard_qbeta_mev():
    """Read the scored Q_beta cell from the dashboard witness, at FULL precision.

    Hardcoding the 12-digit truncation silently loses ~5e-13 and, worse, goes
    stale without saying so -- the exact defect this arc keeps documenting. The
    witness carries 60 digits; reading it turns a staleness hazard into a
    failing assertion. `_EXPECTED_PREFIX` is the value this probe's prose was
    written against, so a dashboard move is LOUD rather than invisible.
    """
    import json
    w = _COMP / "per-observable-100x-status.witness.json"
    if not w.exists():
        raise SystemExit(f"dashboard witness missing: {w}")
    d = json.loads(w.read_text())
    v = d.get("data", {}).get("qbeta_ruled_base", {}).get("Q_beta_MeV")
    if v is None:
        for r in d.get("data", {}).get("rows", []) or d.get("rows", []):
            if r.get("obs") == "Q_beta":
                v = r.get("pred_MeV")
                break
    if v is None:
        raise SystemExit("dashboard witness carries no Q_beta cell")
    if not str(v).startswith(_EXPECTED_PREFIX):
        raise SystemExit(
            f"DASHBOARD MOVED: witness Q_beta = {v}, this probe's prose was "
            f"written against {_EXPECTED_PREFIX}. Re-read the prose before "
            f"re-running -- do not just update the literal."
        )
    return str(v)

RESULTS: list[dict] = []


def check(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n         {detail}\n")


def main() -> int:
    set_compute_dps(DPS)
    mp.dps = DPS

    print("=" * 78)
    print(" the ruled base inverts the route-5 spectrum obstruction")
    print("=" * 78)

    q = q_at(DPS)
    m_e = mp.mpf(str(M_E_MEV))
    q_cod = mp.mpf(str(Q_BETA_MEV))

    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    z_d = q ** 3 / (q ** 2 + 1)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)

    base_z1 = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)   # RETIRED
    base_zD = abs(h ** 2 / 2 - h * z_d) * E0                            # RULED
    base_aug = abs(h ** 2 / 2 - h * q) * E0
    base_dash = mp.mpf(_dashboard_qbeta_mev())                              # RULED

    # kappa: the normalised character the ladder's N=1 factor must supply, i.e.
    # F_required with the N=2 factor (1 - u^2) divided out.
    def kappa(base):
        return (q_cod / base) / (1 - u ** 2)

    # Kohno-Drinfeld: hbar = 2 ln q, generator eigenvalues +- ln q, character
    # cosh(ln q) = (q + 1/q)/2.
    a_kd = mp.log(q)
    kd = (q + 1 / q) / 2

    # ---- 1. calibration against step 18's own two quoted numbers ----------
    k_z1 = kappa(base_z1)
    d_req = abs(k_z1 - mp.mpf(STEP18_QUOTED_REQUIRED))
    d_kd = abs(kd - mp.mpf(STEP18_QUOTED_KD))
    print(f"  step-18 quoted required {STEP18_QUOTED_REQUIRED}  -> here "
          f"{mp.nstr(k_z1, 12)}")
    print(f"  step-18 quoted KD char  {STEP18_QUOTED_KD}  -> here "
          f"{mp.nstr(kd, 12)}\n")
    check(
        "reproduces_step18_quoted_required_and_kd_character",
        d_req < mp.mpf("2e-6") and d_kd < mp.mpf("2e-6"),
        f"kappa on the RETIRED z=1 cell is {mp.nstr(k_z1, 12)} against step 18's "
        f"quoted {STEP18_QUOTED_REQUIRED} (|d| = {mp.nstr(d_req, 4)}), and the "
        f"Kohno-Drinfeld character (q + 1/q)/2 = {mp.nstr(kd, 12)} against its "
        f"quoted {STEP18_QUOTED_KD} (|d| = {mp.nstr(d_kd, 4)}). Same object, so "
        f"what follows is about step 18's own quantity and not a near-relative.",
    )

    # ---- 2. the hypothesis kappa < 1, per base ----------------------------
    BASES = [
        ("z = 1 (Form A)", base_z1, "RETIRED 2026-09-08"),
        ("z_D, order-zero E_0", base_zD, "RULED"),
        ("z = q (augmentation)", base_aug, "the other admissible point"),
        ("dashboard scored cell", base_dash, "RULED (nuc11, tower E_0)"),
    ]
    print("  base                        kappa = F_req/(1-u^2)   hypothesis "
          "kappa < 1")
    krows = []
    for nm, bs, note in BASES:
        k = kappa(bs)
        krows.append({"base": nm, "note": note, "Q_base_MeV": fmt(bs),
                      "kappa": fmt(k), "kappa_below_one": bool(k < 1),
                      "step18_exclusion": "FIRES" if k < 1 else "DOES NOT FIRE"})
        print(f"    {nm:<26} {mp.nstr(k, 15):>18}   "
              f"{'TRUE  -> FIRES' if k < 1 else 'FALSE -> DOES NOT FIRE'}")
    print()

    k_zD, k_dash = kappa(base_zD), kappa(base_dash)
    check(
        "step18_hypothesis_is_false_on_both_ruled_cells",
        k_z1 < 1 and k_zD > 1 and k_dash > 1,
        f"correction_below_one_excludes_real_spectrum carries the hypothesis "
        f"(hk : k < 1). It holds on the retired cell (k = {mp.nstr(k_z1, 10)}) "
        f"and FAILS on both ruled ones (k = {mp.nstr(k_zD, 10)} at z_D "
        f"order-zero, {mp.nstr(k_dash, 10)} on the dashboard cell). The Lean "
        f"theorem is correct and untouched -- it is a conditional and was always "
        f"stated as one; its PREMISE is what the base change falsified.",
    )

    # ---- 3. the invariant that replaces it, on the ruled base --------------
    # hyperbolic: cosh(a) >= 1 for all real a  (real_spectrum_character_ge_one)
    # elliptic:   |cos| <= 1                    (ladderN2_lt_of_one_le)
    worst_cosh = min(mp.cosh(mp.mpf(t) / 10) for t in range(-40, 41))
    check(
        "on_a_ruled_base_the_elliptic_branch_is_excluded_not_the_hyperbolic",
        worst_cosh >= 1 and k_zD > 1 and k_dash > 1,
        f"cosh(a) >= 1 for every real a (sampled min over a in [-4, 4] is "
        f"{mp.nstr(worst_cosh, 12)}; proved in general by "
        f"real_spectrum_character_ge_one) while |cos| <= 1 (Real.cos_le_one, via "
        f"ladderN2_lt_of_one_le). On a base needing kappa > 1 the ELLIPTIC "
        f"generator is the excluded one and the HYPERBOLIC one is not -- the "
        f"reverse of route 5's current narrowing to det A > 0 / |q| = 1 / the "
        f"Kashaev locus, which was derived from the retired premise.",
    )

    # ---- 4. the substrate's own generator is already hyperbolic -----------
    det_A = -(mp.log(q)) ** 2
    check(
        "the_substrate_kd_generator_is_hyperbolic_and_on_the_right_side_now",
        det_A < 0 and kd > 1,
        f"Kohno-Drinfeld scale-fixing gives hbar = 2 ln q, so det A = "
        f"-(ln q)^2 = {mp.nstr(det_A, 10)} < 0 -- hyperbolic at the real q_0, "
        f"which step 18 recorded as the defect. With kappa > 1 it is no longer a "
        f"defect: the character {mp.nstr(kd, 12)} is on the SAME side of 1 as "
        f"the requirement. Right side, wrong size -- see the next check.",
    )

    # ---- 5. the residual gap, and it stays open ---------------------------
    print("  residual gap in three coordinates (a CHECK-AGAINST, not a target "
          "to search on)")
    grows = []
    for nm, bs in (("z_D order-zero", base_zD), ("dashboard cell", base_dash)):
        k = kappa(bs)
        a_req = mp.acosh(k)
        grows.append({
            "base": nm, "kappa_required": fmt(k),
            "generator_a_required": fmt(a_req),
            "ratio_a_req_over_a_kd": fmt(a_req / a_kd),
            "ratio_character_excess": fmt((k - 1) / (kd - 1)),
            "ratio_character": fmt(k / kd),
        })
        print(f"    {nm:<16} a_req/a_KD = {mp.nstr(a_req / a_kd, 8):>10}   "
              f"(k-1)/(KD-1) = {mp.nstr((k - 1) / (kd - 1), 8):>10}   "
              f"k/KD = {mp.nstr(k / kd, 8):>10}")
    print()
    check(
        "the_kd_character_is_on_the_right_side_but_the_wrong_size",
        kd < k_zD and kd < k_dash,
        f"cosh(ln q_0) = {mp.nstr(kd, 12)} against {mp.nstr(k_zD, 12)} required "
        f"at z_D order-zero. Non-exclusion is not a derivation: route 5 goes "
        f"from a STRUCTURAL obstruction back to a QUANTITATIVE gap, which stays "
        f"open. Recorded as a quantity to check against; no search was run for a "
        f"construction that produces it.",
    )

    # ---- 6. the two figures a sibling reported as a correction -------------
    r_a = mp.acosh(k_zD) / a_kd
    r_x = (k_zD - 1) / (kd - 1)
    check(
        "the_11x_and_139x_figures_are_one_gap_in_two_coordinates",
        abs(r_a - mp.mpf("11.168")) < mp.mpf("0.01")
        and abs(r_x - mp.mpf("139.373")) < mp.mpf("0.01"),
        f"a_req/a_KD = {mp.nstr(r_a, 10)} and (kappa-1)/(KD-1) = "
        f"{mp.nstr(r_x, 10)} are the SAME gap at the same base, in the generator "
        f"eigenvalue and in the character excess. A sibling branch recorded 139x "
        f"as a correction of 11.2x; it is a change of coordinate, not a "
        f"correction, and neither figure is wrong. With c_k (magnifier 1/u^2 = "
        f"{mp.nstr(1 / u ** 2, 9)}) and (1 - F) this arc has five coordinates "
        f"for one deviation.",
    )

    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    wb = WitnessBuilder("qbeta-ruled-base-inverts-route5-obstruction",
                        engine="mpmath")
    for r in RESULTS:
        wb.add_assertion(r["name"], computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "Route 5's step-18 obstruction (a real-spectrum holonomy has "
            "character cosh(a) >= 1, so it cannot supply a correction below 1) "
            "carries the explicit hypothesis kappa < 1. That hypothesis holds on "
            "the RETIRED z = 1 cell (kappa = 0.9983977, reproducing step 18's "
            "quoted 0.998399) and is FALSE on both cells of the base the owner "
            "ruled on 2026-09-08: kappa = 1.7593646 at the z_D order-zero E_0 "
            "and 1.2002494 on the dashboard's scored nuc11 cell. The Lean "
            "theorem correction_below_one_excludes_real_spectrum is correct and "
            "untouched -- it is a conditional; its PREMISE is what changed. "
            "Consequence: on a ruled base the two proved inequalities point the "
            "other way -- cosh >= 1 (real_spectrum_character_ge_one) and "
            "|cos| <= 1 (Real.cos_le_one, via ladderN2_lt_of_one_le) together "
            "exclude the ELLIPTIC generator and leave the HYPERBOLIC one, which "
            "is what the substrate's Kohno-Drinfeld generator already is at real "
            "q_0 (det A = -(ln q)^2 < 0). So the narrowing to det A > 0 / |q| = 1 "
            "/ the Kashaev locus / the N = 111 question rests on a retired "
            "premise. This does NOT derive the correction: the KD character "
            "1.0054484 is on the right side of 1 and the wrong size against "
            "1.7593646, a scope-(a) gap that stays open."
        ),
        "bean": "qou-pdix",
        "also": "qou-cds1",
        "q0Anchor": "proton",
        "q0Value": fmt(q),
        "kappa_by_base": krows,
        "residual_gap_coordinates": grows,
        "kd_character": fmt(kd),
        "kd_generator_eigenvalue": fmt(a_kd),
        "kd_det_A": fmt(-(mp.log(q)) ** 2),
        "invariants_cited": (
            "real_spectrum_character_ge_one (QOU/QBeta/"
            "HolonomySpectrumSignObstruction.lean, sorry-free) and "
            "Real.cos_le_one via ladderN2_lt_of_one_le (QOU/QBeta/"
            "LadderFactorBound.lean, sorry-free)"
        ),
        "coordinate_warning": (
            "the residual gap is 11.168 in the generator eigenvalue, 139.373 in "
            "the character excess (kappa-1)/(KD-1), and 1.7498 in the character "
            "ratio -- one gap, three spellings. A sibling recorded 139x as a "
            "correction of 11.2x; it is a change of coordinate. Say which "
            "coordinate before quoting a factor in this arc."
        ),
        "scope": (
            "(b) for the reversal, citing two proved invariants; (a) for every "
            "number. Derives no alpha, selects no base -- that the ruled base "
            "makes the step-18 exclusion lapse is NOT a reason to prefer it "
            "(NO FITTING) -- and wires nothing."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
