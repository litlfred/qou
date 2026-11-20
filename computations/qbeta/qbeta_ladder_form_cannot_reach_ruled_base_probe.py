#!/usr/bin/env python3
"""qbeta_ladder_form_cannot_reach_ruled_base_probe.py — on the RULED base the
Q_beta ladder is excluded for EVERY phase, so alpha is not the blocker.

Beans `qou-cds1` (re-derive the c_k ladder under convention D) and `qou-pdix`
(derive the ladder eigenphase alpha). Scope **(b)** for the exclusion, which
cites a proved invariant; **(a)** for every number.

## The claim

`qou-cds1`'s last entry (2026-09-08) adopts the owner-ruled base and, in the
same sentence, keeps its blocker:

    "BASE SETTLED by owner ruling (qou-99qc): eps := tr_M at z_D. The D-frame
     ladder is to be re-derived on the z_D base (0.4447004 MeV, -43.157 %).
     ... the blocker is still the N=1 phase (qou-pdix)."

**Those two halves are inconsistent, and this probe measures why.** The ladder's
correction factor is

    F(alpha) = cos(alpha - u/2) * (1 - u^2) * prod_{k>=3} (1 + c_k u^k)

(`qbeta_ck_coordinate_magnifier_probe.py:18`), and what it must supply is
`F_required = Q_codata / Q_base`. On the retired `z = 1` base
`F_required = 0.9983 < 1`, so a phase near zero fits and alpha is exactly the
interesting unknown — which is why the blocker was stated that way.

On the RULED base `F_required > 1`. And `cos <= 1`, so

    F_N2(alpha) = cos(alpha - u/2) * (1 - u^2) <= 1 - u^2 < 1   for EVERY real alpha.

**No phase closes it — derived, fitted, or otherwise.** Deriving alpha therefore
cannot unblock the ladder on the base the bean itself adopted.

## What this does NOT say

It does **not** retire alpha as a question: alpha remains the N=1 phase of the
ladder and `qou-pdix` remains open on its own terms. It says only that alpha is
not what stands between this ladder and the ruled base.

It does **not** refute the ladder as an object, nor the bar-odd projection
(`a_odd = a - h^2/4`, forced and sorry-free). Those are C-frame results and are
untouched; the F-table they are scored in is computed on `Q_A`, the retired
`z = 1` cell, and this probe reproduces that table as its calibration before
recomputing anything.

It does **not** choose a base. The ruled base is ruled; per AGENTS.md NO FITTING
a base is never selected by which obstruction it removes, and the retired cell's
`F_required < 1` is NOT a reason to prefer it.

## The third-coordinate trap, stated because it cost a reading

`qou-cds1`'s table reports **relative deviation of `1 - F`**, not of `F`
(`reldev = (1 - F_N2)/(1 - F_required) - 1`). On the retired base both
quantities are small and positive and the ratio is informative (C -0.076 %,
D z-swap -35.9 %, D bar-odd -3.17 %). On a ruled base `1 - F_required` is
NEGATIVE and order 1 while `1 - F_N2` stays positive and order 1e-3, so the
same ratio is meaningless rather than merely large. Report `F` directly there.

## Precision

mpmath at 50 dps; `q_0` from `q_at` (proton pin); `m_e` / `Q_beta` from
`codata_constants`. No float64: no `float(` outside display, no `statistics`,
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
from qbeta_utils import c3_proton_extracted  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 50

# The dashboard's currently-scored Q_beta prediction, read from
# computations/per-observable-100x-status.witness.json (row obs == "Q_beta").
_EXPECTED_PREFIX = "0.651856310060"

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
    print(" the ladder's form is bounded by cos; the ruled base is not")
    print("=" * 78)

    q = q_at(DPS)
    m_e = mp.mpf(str(M_E_MEV))
    q_cod = mp.mpf(str(Q_BETA_MEV))

    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2

    z_c = mp.sqrt(q) / (q + 1)
    z_d = q ** 3 / (q ** 2 + 1)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)

    # ---- bases ------------------------------------------------------------
    base_z1 = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)   # RETIRED
    base_zD = abs(h ** 2 / 2 - h * z_d) * E0                            # RULED
    base_aug = abs(h ** 2 / 2 - h * q) * E0
    base_dash = mp.mpf(_dashboard_qbeta_mev())                              # RULED cell

    # ---- the three phase cells, verbatim from the magnifier probe ----------
    CELLS = [
        ("C  alpha=(z_C-1)h/2", (z_c - 1) * h / 2),
        ("D  z-swap", (z_d - 1) * h / 2),
        ("D  bar-odd (forced)", (z_d - 1) * h / 2 - h ** 2 / 4),
    ]

    def F_N2(alpha):
        return mp.cos(alpha - u / 2) * (1 - u ** 2)

    # ---- 1. calibration: reproduce the bean's F-table on the RETIRED base --
    Freq_z1 = q_cod / base_z1
    rows_retired = []
    for nm, a in CELLS:
        reldev = (1 - F_N2(a)) / (1 - Freq_z1) - 1
        rows_retired.append({"cell": nm, "reldev_pct": fmt(reldev * 100)})
    got = [r["reldev_pct"] for r in rows_retired]
    tgt = [mp.mpf("-0.076"), mp.mpf("-35.9"), mp.mpf("-3.17")]
    ok = all(abs((1 - F_N2(a)) / (1 - Freq_z1) - 1 - t / 100) < mp.mpf("0.005")
             for (nm, a), t in zip(CELLS, tgt))
    print("  RETIRED z=1 base — reldev of (1-F), reproducing qou-cds1's table")
    for (nm, a) in CELLS:
        rd = ((1 - F_N2(a)) / (1 - Freq_z1) - 1) * 100
        print(f"    {nm:<24} {mp.nstr(rd, 6):>12} %")
    print()
    check(
        "reproduces_cds1_F_table_on_the_retired_base",
        ok,
        "the three phase cells reproduce bean qou-cds1's recorded -0.076 % / "
        "-35.9 % / -3.17 % to better than 0.005 absolute, so the machinery "
        "below is the bean's own and not a re-invention. Note the coordinate: "
        "these are relative deviations of (1 - F), not of F.",
    )

    # ---- 2. F_required on every base --------------------------------------
    BASES = [
        ("z = 1 (Form A)", base_z1, "RETIRED 2026-09-08"),
        ("z_D, order-zero E_0", base_zD, "RULED"),
        ("z = q (augmentation)", base_aug, "the other admissible point"),
        ("dashboard scored cell", base_dash, "RULED (nuc11, tower E_0)"),
    ]
    print("  base                        Q_base (MeV)     F_required = Q_cod/Q_base")
    brows = []
    for nm, bs, note in BASES:
        Fr = q_cod / bs
        brows.append({"base": nm, "note": note, "Q_base_MeV": fmt(bs),
                      "F_required": fmt(Fr), "exceeds_one": bool(Fr > 1)})
        print(f"    {nm:<26} {mp.nstr(bs, 12):>14}   {mp.nstr(Fr, 12):>14}"
              f"   {'> 1  EXCLUDED' if Fr > 1 else '< 1'}")
    print()

    Fr_zD = q_cod / base_zD
    Fr_dash = q_cod / base_dash
    check(
        "every_ruled_base_needs_F_above_one",
        Fr_zD > 1 and Fr_dash > 1 and Freq_z1 < 1,
        f"F_required = {mp.nstr(Fr_zD, 10)} on the z_D order-zero base and "
        f"{mp.nstr(Fr_dash, 10)} on the dashboard's scored cell — both ABOVE 1 — "
        f"against {mp.nstr(Freq_z1, 10)} on the retired z = 1 cell, which is "
        f"below. The sign of (1 - F_required) flips with the base.",
    )

    # ---- 3. the exclusion: cos <= 1 bounds the ladder for EVERY alpha ------
    cap = 1 - u ** 2
    # sup over alpha is attained at alpha = u/2, where cos = 1
    sup_F = F_N2(u / 2)
    check(
        "ladder_form_is_bounded_by_one_for_every_phase",
        abs(sup_F - cap) < mp.mpf(10) ** -40 and cap < 1 < Fr_zD and cap < Fr_dash,
        f"F_N2(alpha) = cos(alpha - u/2)*(1 - u^2), and cos <= 1 (Real.cos_le_one "
        f"— the same proved invariant the eigenphase carrier's own "
        f"replacement_excludes_some_matrix uses), so sup over ALL real alpha is "
        f"attained at alpha = u/2 and equals 1 - u^2 = {mp.nstr(cap, 20)}. Every "
        f"ruled base needs more than 1. **No phase closes it** — so deriving "
        f"alpha cannot unblock the ladder on the ruled base, and qou-cds1's "
        f"'the blocker is still the N=1 phase' does not hold for the base the "
        f"same entry adopts.",
    )

    # ---- 4. what it would cost inside the ladder --------------------------
    # need prod(1 + c_k u^k) = Fr / cap ; at leading order c_2_eff * u^2
    need_zD = (Fr_zD / cap - 1) / u ** 2
    need_dash = (Fr_dash / cap - 1) / u ** 2
    check(
        "closing_inside_the_ladder_needs_c2_four_orders_from_structural",
        need_zD > mp.mpf(10) ** 3,
        f"if the shortfall were pushed into the rungs instead, the leading "
        f"coefficient would have to be c_2 ~ {mp.nstr(need_zD, 8)} on the z_D "
        f"base and {mp.nstr(need_dash, 8)} on the dashboard cell, against the "
        f"structural c_2 = -1 — four orders of magnitude, and the wrong sign. "
        f"The magnifier 1/u^2 = {mp.nstr(1 / u ** 2, 8)} is why c_k is the wrong "
        f"coordinate to read this in (qou-cds1's own finding).",
    )

    # ---- 5. the third-coordinate trap -------------------------------------
    reldev_zD = (1 - F_N2(CELLS[2][1])) / (1 - Fr_zD) - 1
    check(
        "the_reldev_coordinate_is_meaningless_once_F_required_exceeds_one",
        (1 - Fr_zD) < 0 < (1 - F_N2(CELLS[2][1])),
        f"on the ruled base 1 - F_required = {mp.nstr(1 - Fr_zD, 8)} is NEGATIVE "
        f"while the model's 1 - F_N2 = {mp.nstr(1 - F_N2(CELLS[2][1]), 8)} stays "
        f"positive, so qou-cds1's reldev coordinate returns "
        f"{mp.nstr(reldev_zD * 100, 8)} % — a ratio of opposite-signed "
        f"quantities, meaningless rather than merely large. Report F directly on "
        f"a ruled base; the reldev table is retired-base-only.",
    )

    # ---- 6. the obvious objection: could a HIGHER RUNG save it? -----------
    # F is cos * prod_k (1 + c_k u^k). Check 3 bounds only the N=2 truncation.
    # Every c_k the corpus records or derives is NEGATIVE, so every factor is
    # below 1 and the product is below 1 at EVERY truncation order.
    C3 = c3_proton_extracted()            # proton extraction, recomputed (qbeta_ck_cache's)
    c5 = -(b ** 2 + mp.mpf(1) / 2)        # derived form -(b^2 + 1/2)
    LADDER = [(2, mp.mpf(-1)), (3, C3), (5, c5)]
    factors = [(k, 1 + c * u ** k) for k, c in LADDER]
    prod = mp.mpf(1)
    for _, f in factors:
        prod *= f
    all_neg = all(c < 0 for _, c in LADDER)
    all_below = all(f < 1 for _, f in factors)
    print("  full recorded ladder — every factor below 1")
    for (k, c), (_, f) in zip(LADDER, factors):
        print(f"    c_{k} = {mp.nstr(c, 12):>16}   (1 + c_{k} u^{k}) = {mp.nstr(f, 18)}")
    print(f"    product = {mp.nstr(prod, 18)}   (< 1)\n")
    check(
        "every_recorded_rung_reduces_so_no_truncation_order_helps",
        all_neg and all_below and prod < 1,
        f"the objection check 3 invites is 'a higher rung saves it'. It does "
        f"not: every c_k the corpus records or derives is NEGATIVE — c_2 = -1 "
        f"(structural), c_3 = {mp.nstr(C3, 12)} (recorded proton extraction), "
        f"c_5 = -(b^2 + 1/2) = {mp.nstr(c5, 12)} (derived) — so each factor "
        f"(1 + c_k u^k) < 1 and the product is {mp.nstr(prod, 14)} < 1. With "
        f"cos <= 1 the whole F is strictly below 1 at EVERY truncation order, "
        f"not merely at N=2. Reaching F > 1 needs a POSITIVE coefficient, and "
        f"none of the derived ones is.",
    )

    # ---- 7. the target, stated — and explicitly not to be searched on -----
    eps_zD = abs(h ** 2 / 2 - h * z_d)
    eps_needed = eps_zD * Fr_zD
    check(
        "the_target_is_stated_as_a_magnitude_not_as_a_search",
        eps_needed > eps_zD,
        f"stated so the size is on the record, NOT as a specification to search "
        f"against: at the order-zero E_0 the ruled functional gives "
        f"|eps| = {mp.nstr(eps_zD, 12)}, and reproducing CODATA would need "
        f"{mp.nstr(eps_needed, 12)} — a factor {mp.nstr(Fr_zD, 10)}. Per "
        f"AGENTS.md NO FITTING a target may be checked AGAINST, never searched "
        f"ON: do not hunt for an element whose Markov trace lands here. The "
        f"dashboard's own scored element already fails the confinement-SDP "
        f"selection rule (owner ruling 2026-09-13), so the assembly is under "
        f"review independently of this number.",
    )

    # ---- 8. a FOURTH coordinate, found by a sibling using the "safe" one ---
    sgn_rows = []
    for nm, bs, note in BASES:
        Fr = q_cod / bs
        sgn_rows.append({"base": nm, "F_required": fmt(Fr),
                         "sign_F_minus_1": "+" if Fr > 1 else "-"})
    signs = {r["sign_F_minus_1"] for r in sgn_rows}
    check(
        "sign_F_minus_one_is_a_FOURTH_coordinate_and_does_NOT_survive",
        len(signs) == 2,
        "The trap above says to report F directly, and F does survive the base "
        "change -- but sign(F - 1) does NOT, and a reader who switched to F "
        "can still be caught by it. Measured, the sign is '-' on the retired "
        "z = 1 and augmentation cells and '+' on both ruled cells, so any "
        "argument whose content is 'the requirement is BELOW 1' is "
        "retired-base-only even when stated in F. #7276 hit exactly this from "
        "another arc: it avoided the (1 - F) trap, used F, and still drafted a "
        "cross-check reading 'the required factor is below 1 ... structurally "
        "the same obstruction as cosh a >= 1 > 0.998399' -- where 0.998399 is "
        "the z = 1 cell's own number. So this arc has FOUR coordinates with "
        "different base-sensitivity (c_k, 1 - F, sign(F - 1), F), and only F "
        "survives. Credit: sibling PR #7276.",
    )

    allp = all(r["passed"] for r in RESULTS)
    print(f"  {sum(r['passed'] for r in RESULTS)}/{len(RESULTS)} checks passed")

    wb = WitnessBuilder("qbeta-ladder-form-cannot-reach-ruled-base", engine="mpmath")
    for r in RESULTS:
        wb.add_assertion(r["name"], computed="PASS" if r["passed"] else "FAIL",
                         expected="PASS", tolerance="exact", source=r["detail"])
    wb.save({
        "description": (
            "On the owner-ruled Q_beta base the ladder's correction factor "
            "F_N2(alpha) = cos(alpha - u/2)(1 - u^2) is bounded above by 1 - u^2 "
            "for EVERY real alpha (cos <= 1), while F_required = Q_codata/Q_base "
            "EXCEEDS 1 on both ruled cells (1.7594 at z_D order-zero E_0, 1.2002 "
            "on the dashboard's scored nuc11 cell) and is BELOW 1 only on the "
            "retired z = 1 cell (0.9983). So no phase closes the ladder on the "
            "ruled base, and qou-cds1's standing blocker — 'the blocker is still "
            "the N=1 phase (qou-pdix)' — does not hold for the base that same "
            "entry adopts. Calibrated first by reproducing qou-cds1's own F-table "
            "(-0.076 / -35.9 / -3.17 %) on the retired base. Does not retire "
            "alpha as a question, does not refute the ladder or the forced "
            "bar-odd projection (both C-frame, untouched), and does not choose a "
            "base: F_required < 1 on the retired cell is NOT a reason to prefer "
            "it (NO FITTING)."
        ),
        "bean": "qou-cds1",
        "also": "qou-pdix",
        "q0Anchor": "proton",
        "q0Value": fmt(q),
        "bases": brows,
        "retired_base_reldev_table": rows_retired,
        "ladder_sup_over_all_phases": fmt(cap),
        "full_ladder_is_reducing": (
            "every c_k the corpus records or derives is NEGATIVE (c_2 = -1 "
            f"structural, c_3 = {mp.nstr(C3, 12)} recorded, c_5 = -(b^2+1/2) derived), "
            "so each factor (1 + c_k u^k) < 1 and F is strictly below 1 at EVERY "
            "truncation order -- not merely at the N=2 one check 3 bounds. "
            "Reaching F > 1 needs a POSITIVE coefficient; none of the derived "
            "ones is."
        ),
        "invariant_cited": (
            "cos <= 1 (Real.cos_le_one, Mathlib; already used by "
            "QOU.QBeta.EigenphaseCarrier.replacement_excludes_some_matrix)"
        ),
        "sign_F_minus_one_by_base": sgn_rows,
        "coordinate_warning": (
            "qou-cds1's table reports relative deviation of (1 - F), not of F. "
            "Once F_required > 1 that ratio compares opposite-signed quantities "
            "and is meaningless; report F directly on a ruled base. AND NOTE "
            "sign(F - 1) is a FOURTH coordinate that does not survive either: "
            "an argument whose content is 'the requirement is below 1' is "
            "retired-base-only even when stated in F. Four coordinates, only F "
            "survives (credit: sibling PR #7276, which hit this using F)."
        ),
        "scope": (
            "(b) for the exclusion, citing a proved invariant; (a) for every "
            "number. Derives no alpha, selects no base, wires nothing."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
