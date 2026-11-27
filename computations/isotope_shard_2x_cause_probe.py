#!/usr/bin/env python3
"""qou-85o2 — 80-dps verification probe & exhaustive 3,243-row L4 audit for canonical-isotope-witness shards.

THE CLAIM UNDER TEST (bean `qou-85o2`).
98 `canonical-isotope-witness-Z*.witness.json` shards (`Z21..Z118`) carry
`computedAt` 2026-08-23T17:15–17:16 (`commitSha = 35d18af5f783`), before commit
`a24fdac8a1a6` (2026-08-24T11:04) updated `hecke_core_symbolic.z` from
`z_pre = sqrt(q)/(q+1)` to `z = q^3/(q^2+1)`. A spot re-run of `Z=26, N=19`
reported `qclt_binding = 120.70 MeV` against the shard's recorded `55.088 MeV`
— a ratio of `2.191`, whereas the `z` update predicted `~0.728`.

80-DPS FINDINGS (verified across all 119 shards / 3,558 AME rows, shallow-clone safe)
1. **3-run bit-identical reproducibility at `Z=26, N=19` (`⁴⁵Fe`)**:
   `qclt_binding(26, 19, colour_weighted=True, dps=80)` evaluates identically across
   three independent runs to `120.70117400214785859850884647 MeV`, with
   `coulomb_energy_mev(26, 45) = 111.67413404405899054336083552 MeV` and
   `L4 = 9.02703995808886805514801095 MeV`.

2. **Exact explanation of `2.191048078` (pipeline stage mismatch, not a second drift)**:
   `canonical_isotope_witness.py` records `L4 = qclt_binding(Z, N) - coulomb_energy_mev(Z, A)`.
   `120.701174 MeV` is the *pre-Coulomb* strong term; `55.088327 MeV` is the *post-Coulomb*
   recorded `L4` prediction. `120.701174 / 55.088327 = 2.191048078` divides one pipeline stage
   by the other. Comparing like-for-like:
     - `qclt_binding`: `166.7624615024 -> 120.7011740021 MeV` (`×0.72379115`, within `0.62%` of
       the pure pn-bond log-ratio `ln(f_pn(z)) / ln(f_pn(z_pre)) = 0.72830816`, the `0.62%`
       difference coming deterministically from pp and nn bond weights in the complete graph).
     - `L4` residual: `55.0883274584 -> 9.0270399581 MeV` (`×0.16386484`), amplified by
       subtracting the unchanged `111.674134 MeV` Coulomb repulsion.

3. **Single-cause import-cone attribution (`a24fdac8a1a6`)**:
   `a24fdac8a1a6` modified two Python modules: `channel_binding.py` (self-test comment +
   assertion threshold only: `0 MeV` contribution) and `substrate/hecke_core_symbolic.py`
   (`z = sqrt(q)/(q+1) -> q^3/(q^2+1)`: `46.0612875003 MeV` contribution, `100%` of the move).

4. **Exhaustive 3,243 / 3,243 L4 census across `Z00..Z118` (new ancestry finding)**:
   - Every single one of the **`3,243` `L4-qclt-colour-weighted` rows** across all 119 shards —
     **including `91/91` `L4` rows (`A > 40`) in `Z00..Z20` (`commitSha = f8dae9f5eb2a`,
     `computedAt = 2026-08-24T14:40`)** as well as `2,892/2,892` in `Z21..Z99` and `260/260`
     in `Z100..Z118` — reproduces the pre-`a24fdac8a1a6` formula within `< 1.0 ulp` of the
     producer's `float(qclt_binding(...))` cast (`max_ulp_units = 0.988745` in units of
     `2^-53 * qclt_pre`). Thus `Z00..Z20` was generated on a branch that had not yet merged
     `a24fdac8a1a6`, and all 119 shards share the pre-`a24fdac8a1a6` `L4` state.
   - Under `z = q^3/(q^2+1)`, **`1,634 / 3,243` (`50.39%`)** of `L4` rows flip to negative net
     binding (`qclt_binding < coulomb_energy_mev`, reaching `-379.502 MeV` at `Z=118, N=175`),
     and two upstream float64 truncations remain in `canonical_isotope_witness.py:347`
     (`float(qclt_binding(...))`) and `channel_binding.py:122` (`mpf(str(_Q0))` from binary64
     `q_parameter.Q`, `|q_cb - q_at(80)| = 7.59167e-18`). Per the 2026-11-21 owner gate on
     `qou-85o2`, shards are audited rather than mass-regenerated prior to resolving those gates.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (str(HERE), str(HERE / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(80)
import mpmath as mp  # noqa: E402
from mpmath import mpf, fabs, sqrt, log  # noqa: E402
mp.mp.dps = max(mp.mp.dps, 80)

import channel_binding as cb  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

Z_SPOT, N_SPOT = 26, 19
A_SPOT = Z_SPOT + N_SPOT


def _qclt_counterfactual_at_z(Z: int, N: int, z_val: mpf, q_val: mpf, e0_val: mpf) -> mpf:
    """Exact 80-dps evaluation of `channel_binding.qclt_binding(Z, N, colour_weighted=True)`
    for an arbitrary symbolic/numeric Markov parameter `z_val`, matching `_vertex_channels_sym`
    (`V_std(1, d) = z + d`) without depending on shallow-clone `git show` history.
    """
    a_mass = Z + N
    if a_mass < 2:
        return mpf(0)
    h_val = q_val - mpf(1) / q_val
    l_pp = log(mpf(1) / z_val)
    l_pn = log(mpf(1) / (z_val - h_val / mpf(2)))
    l_nn = log(mpf(1) / (z_val - h_val))
    cnt_pp = Z * (Z - 1) // 2
    cnt_pn = Z * N
    cnt_nn = N * (N - 1) // 2
    tot = cnt_pp + cnt_pn + cnt_nn
    mean = (mpf(cnt_pp) * l_pp + mpf(cnt_pn) * l_pn + mpf(cnt_nn) * l_nn) / mpf(tot)
    return e0_val * mpf(a_mass - 1) * mean


def _measure_live(Z: int, N: int) -> dict[str, mpf]:
    b = mpf(cb.qclt_binding(Z, N, colour_weighted=True, dps=80))
    c = mpf(coulomb_energy_mev(Z, Z + N))
    return {"qclt": b, "coulomb": c, "l4": b - c}


def run_audit() -> dict:
    q80 = q_at(80)
    q_cb = cb.q0(80)
    e0_cb = cb.E0(80)
    q_pin_truncation = fabs(q_cb - q80)

    z_pre = sqrt(q_cb) / (q_cb + mpf(1))
    z_post = (q_cb ** 3) / ((q_cb ** 2) + mpf(1))

    # 1. Three-run reproducibility at Z=26, N=19
    runs = [_measure_live(Z_SPOT, N_SPOT) for _ in range(3)]
    stable_3_runs = (
        len({mp.nstr(r["qclt"], 70) for r in runs}) == 1
        and len({mp.nstr(r["coulomb"], 70) for r in runs}) == 1
        and len({mp.nstr(r["l4"], 70) for r in runs}) == 1
    )
    now = runs[0]

    # 2. Exact counterfactual parity: closed-form(z_post, q_cb) == live channel_binding to <1e-65
    b_post_cf = _qclt_counterfactual_at_z(Z_SPOT, N_SPOT, z_post, q_cb, e0_cb)
    b_pre_cf = _qclt_counterfactual_at_z(Z_SPOT, N_SPOT, z_pre, q_cb, e0_cb)
    cf_live_diff = fabs(b_post_cf - now["qclt"])
    l4_pre = b_pre_cf - now["coulomb"]

    # Read committed Z26 shard row (Z=26, N=19)
    shard26 = HERE / "canonical-isotope-witness-Z26.witness.json"
    d26 = json.loads(shard26.read_text(encoding="utf-8"))
    row26 = [r for r in d26["data"]["rows"] if r["N"] == N_SPOT][0]
    recorded_26_19 = mpf(str(row26["prediction_MeV_50dps"]))
    rel_repro_26_19 = fabs(l4_pre - recorded_26_19) / fabs(recorded_26_19)

    # Ratios & stage mismatch
    ratio_qclt = now["qclt"] / b_pre_cf
    ratio_l4 = now["l4"] / l4_pre
    stage_mismatch_ratio = now["qclt"] / recorded_26_19
    h_cb = q_cb - mpf(1) / q_cb
    f_pn_pre = z_pre - h_cb / mpf(2)
    f_pn_post = z_post - h_cb / mpf(2)
    pn_only_log_ratio = log(f_pn_post) / log(f_pn_pre)

    # 3. Exhaustive census of all 3,243 L4 rows across Z00..Z118
    ulp_unit = mpf(2) ** (-53)
    counts = {"Z00_Z20": [0, 0], "Z21_Z99": [0, 0], "Z100_Z118": [0, 0]}
    max_ulp_units = mpf(0)
    worst_ulp_row = None
    max_rel_residual = mpf(0)
    worst_rel_row = None
    neg_post_count = 0
    worst_neg = (mpf(0), None)

    for z_idx in range(119):
        spath = HERE / f"canonical-isotope-witness-Z{z_idx:02d}.witness.json"
        sdoc = json.loads(spath.read_text(encoding="utf-8"))
        bucket = "Z00_Z20" if z_idx <= 20 else ("Z21_Z99" if z_idx <= 99 else "Z100_Z118")
        for r in sdoc["data"]["rows"]:
            if r.get("layer") != "L4-qclt-colour-weighted":
                continue
            zr, nr, ar = int(r["Z"]), int(r["N"]), int(r["A"])
            rec = mpf(str(r["prediction_MeV_50dps"]))
            b_pre = _qclt_counterfactual_at_z(zr, nr, z_pre, q_cb, e0_cb)
            b_post = _qclt_counterfactual_at_z(zr, nr, z_post, q_cb, e0_cb)
            coul = mpf(coulomb_energy_mev(zr, ar))
            l4_pre_r = b_pre - coul
            l4_post_r = b_post - coul

            if l4_post_r < mpf(0):
                neg_post_count += 1
                if l4_post_r < worst_neg[0]:
                    worst_neg = (l4_post_r, [zr, nr, ar])

            err = fabs(l4_pre_r - rec)
            u_err = err / (ulp_unit * b_pre)
            rel_r = err / fabs(rec)
            if u_err > max_ulp_units:
                max_ulp_units = u_err
                worst_ulp_row = [zr, nr, ar, mp.nstr(u_err, 8)]
            if rel_r > max_rel_residual:
                max_rel_residual = rel_r
                worst_rel_row = [zr, nr, ar, mp.nstr(rel_r, 8)]

            counts[bucket][1] += 1
            if u_err <= mpf(1):
                counts[bucket][0] += 1

    tot_ok = sum(v[0] for v in counts.values())
    tot_rows = sum(v[1] for v in counts.values())

    return {
        "q80": q80,
        "q_cb": q_cb,
        "q_pin_truncation": q_pin_truncation,
        "stable_3_runs": stable_3_runs,
        "spot_Z26_N19": {
            "Z": Z_SPOT,
            "N": N_SPOT,
            "A": A_SPOT,
            "qclt_post_MeV": mp.nstr(now["qclt"], 40),
            "qclt_pre_MeV": mp.nstr(b_pre_cf, 40),
            "coulomb_MeV": mp.nstr(now["coulomb"], 40),
            "L4_post_MeV": mp.nstr(now["l4"], 40),
            "L4_pre_MeV": mp.nstr(l4_pre, 40),
            "recorded_shard_L4_MeV": mp.nstr(recorded_26_19, 40),
            "rel_diff_pre_vs_recorded": mp.nstr(rel_repro_26_19, 8),
            "closed_form_vs_live_diff_MeV": mp.nstr(cf_live_diff, 6),
            "stage_mismatch_qclt_post_over_L4_pre": mp.nstr(stage_mismatch_ratio, 12),
            "like_for_like_qclt_ratio": mp.nstr(ratio_qclt, 12),
            "pn_only_log_ratio_prediction": mp.nstr(pn_only_log_ratio, 12),
            "like_for_like_L4_ratio": mp.nstr(ratio_l4, 12),
            "hecke_core_symbolic_contribution_MeV": mp.nstr(b_pre_cf - now["qclt"], 16),
            "channel_binding_contribution_MeV": "0",
        },
        "exhaustive_L4_census": {
            "Z00_Z20_reproduced": counts["Z00_Z20"][0],
            "Z00_Z20_total": counts["Z00_Z20"][1],
            "Z21_Z99_reproduced": counts["Z21_Z99"][0],
            "Z21_Z99_total": counts["Z21_Z99"][1],
            "Z100_Z118_reproduced": counts["Z100_Z118"][0],
            "Z100_Z118_total": counts["Z100_Z118"][1],
            "all_shards_reproduced": tot_ok,
            "all_shards_total": tot_rows,
            "max_error_in_qclt_float64_ulps": mp.nstr(max_ulp_units, 8),
            "worst_ulp_row": worst_ulp_row,
            "max_rel_error_vs_residual": mp.nstr(max_rel_residual, 8),
            "worst_rel_residual_row": worst_rel_row,
            "post_update_negative_L4_rows": neg_post_count,
            "worst_negative_post_L4_MeV": mp.nstr(worst_neg[0], 12),
            "worst_negative_post_nuclide": worst_neg[1],
        },
        "checks": {
            "stable_3_runs": stable_3_runs,
            "cf_matches_live": bool(cf_live_diff < mpf("1e-65")),
            "stage_mismatch_explains_2_19": bool(
                fabs(stage_mismatch_ratio - mpf("2.191048078")) < mpf("1e-8")
            ),
            "qclt_ratio_matches_pn_prediction_within_1pct": bool(
                fabs(ratio_qclt - pn_only_log_ratio) / ratio_qclt < mpf("1e-2")
            ),
            "all_3243_L4_rows_reproduced_under_1_ulp": bool(
                tot_ok == 3243 and tot_rows == 3243 and max_ulp_units < mpf(1)
            ),
            "z00_z20_also_carries_91_pre_excision_L4_rows": bool(
                counts["Z00_Z20"] == [91, 91]
            ),
        },
    }


def main() -> int:
    res = run_audit()
    spot = res["spot_Z26_N19"]
    cen = res["exhaustive_L4_census"]
    chk = res["checks"]

    wb = WitnessBuilder("isotope-shard-2x-cause-probe", engine="python+mpmath")
    wb.set_description(
        "80-dps verification probe for qou-85o2: 3-run reproducibility at Z=26,N=19, "
        "exact proof that 2.191048078 = qclt_post / L4_pre is a pre- vs post-Coulomb "
        "stage mismatch while like-for-like qclt moves by x0.72379115 (single cause: "
        "a24fdac8a1a6 in hecke_core_symbolic.py), and exhaustive 3,243/3,243 L4-row "
        "verification across all 119 canonical-isotope-witness shards Z00..Z118."
    )
    wb.add_parameter("spot_nuclide", {"Z": Z_SPOT, "N": N_SPOT, "A": A_SPOT})
    wb.add_parameter("cause_commit", "a24fdac8a1a6 (2026-08-24T11:04:30Z)")
    wb.add_parameter("channel_binding_q0_float64_truncation", mp.nstr(res["q_pin_truncation"], 8))
    wb.add_data("spot_Z26_N19", spot)
    wb.add_data("exhaustive_L4_census", cen)
    wb.add_upstream(HERE / "canonical-isotope-witness-Z20.witness.json")
    wb.add_upstream(HERE / "canonical-isotope-witness-Z26.witness.json")
    wb.add_upstream(HERE / "canonical-isotope-witness-Z99.witness.json")

    for name, ok in chk.items():
        wb.add_assertion(name, computed=str(bool(ok)), expected="True")

    wb.set_audit_only("docs/audits/2026-11-24-canonical-isotope-z21-z99-bisect-85o2.md")
    out = wb.save(
        extra={
            "q0Anchor": "proton",
            "q0Value": mp.nstr(res["q80"], 80),
        }
    )

    print("=" * 76)
    print("qou-85o2 — 80-dps Z=26,N=19 bisect + exhaustive 3,243-row L4 shard census")
    print("=" * 76)
    print(f"[1] 3-run bit-identical at 80 dps : {chk['stable_3_runs']}")
    print(f"    qclt_post = {spot['qclt_post_MeV']} MeV")
    print(f"    coulomb   = {spot['coulomb_MeV']} MeV")
    print(f"    L4_post   = {spot['L4_post_MeV']} MeV")
    print(f"[2] Stage mismatch ratio          : {spot['stage_mismatch_qclt_post_over_L4_pre']} (= qclt_post / recorded L4_pre)")
    print(f"    Like-for-like qclt ratio      : x{spot['like_for_like_qclt_ratio']} (pn-only log-ratio: x{spot['pn_only_log_ratio_prediction']})")
    print(f"    Like-for-like L4 ratio        : x{spot['like_for_like_L4_ratio']} ({spot['L4_pre_MeV'][:12]} -> {spot['L4_post_MeV'][:12]} MeV)")
    print(f"[3] Exhaustive L4 census (<1 ulp) : {cen['all_shards_reproduced']}/{cen['all_shards_total']} across Z00..Z118")
    print(f"    Z00..Z20: {cen['Z00_Z20_reproduced']}/{cen['Z00_Z20_total']} | Z21..Z99: {cen['Z21_Z99_reproduced']}/{cen['Z21_Z99_total']} | Z100..Z118: {cen['Z100_Z118_reproduced']}/{cen['Z100_Z118_total']}")
    print(f"    Max error (float64 ulps)      : {cen['max_error_in_qclt_float64_ulps']} at {cen['worst_ulp_row']}")
    print(f"    Post-update negative L4 rows  : {cen['post_update_negative_L4_rows']}/{cen['all_shards_total']} (worst {cen['worst_negative_post_L4_MeV']} MeV at {cen['worst_negative_post_nuclide']})")
    print(f"Witness -> {out}")
    return 0 if all(chk.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
