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

# The dashboard's currently-scored Q_beta prediction, read from
# computations/per-observable-100x-status.witness.json (row obs == "Q_beta").
DASHBOARD_PRED_MEV = "0.651856310060"

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
    E0 = m_e / (q * (q - 1))

    # ---- bases ------------------------------------------------------------
    base_z1 = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)   # RETIRED
    base_zD = abs(h ** 2 / 2 - h * z_d) * E0                            # RULED
    base_aug = abs(h ** 2 / 2 - h * q) * E0
    base_dash = mp.mpf(DASHBOARD_PRED_MEV)                              # RULED cell

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
        "invariant_cited": (
            "cos <= 1 (Real.cos_le_one, Mathlib; already used by "
            "QOU.QBeta.EigenphaseCarrier.replacement_excludes_some_matrix)"
        ),
        "coordinate_warning": (
            "qou-cds1's table reports relative deviation of (1 - F), not of F. "
            "Once F_required > 1 that ratio compares opposite-signed quantities "
            "and is meaningless; report F directly on a ruled base."
        ),
        "scope": (
            "(b) for the exclusion, citing a proved invariant; (a) for every "
            "number. Derives no alpha, selects no base, wires nothing."
        ),
    })
    return 0 if allp else 1


if __name__ == "__main__":
    raise SystemExit(main())
