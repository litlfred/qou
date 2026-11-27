#!/usr/bin/env python3
"""80-dps algebraic & historical bisection of the derived-w witness move (qou-02g1).

Verifies to full precision (`compute_dps = 95`, `output_dps = 80`, zero float64)
that 100% of the shift between the pre-#9055 witness (`3bd2b6d93a1`, computed
`2026-09-03T04:00:37Z`) and the #9055 witness (`82c9cbc1344`, computed
`2026-11-22T16:28:43Z`) comes from the 2026-09-05 intra-nucleon ordering fix
(`intra_order="grouped"` -> `"borromean"`, bean `qou-hu1f`), with zero
contribution from `#8940` (`tr_m_word_lq` Case C), `4603bfab4aa`
(`per_generator_V_hat_3A`), or `89c454294aa`.

Also cross-checks the closed-form H_3(q_0) connected-sum factorisation against
the full 6-strand H_6(q_0) two-row Young-Hoefsmit seminormal matrix product on
deuterium (2H) to < 1e-75 under both orderings, and certifies exact ordering
invariance of the interface-product ratio `tr_M(Delta * prod sigma_{3k-1}) / tr_M(Delta)`.

Audit report: docs/audits/2026-11-24-derived-w-witness-bisect-qou-02g1.md
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_OUTPUT_DPS", "80")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "hecke"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pyhecke.atom import nucleon_word_letters  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from y_lambda_wenzl_bridge import partitions_of, y_lambda_wenzl_bridge_numeric  # noqa: E402

set_compute_dps()

# Exact historical 2026-09-03 witness values (blob 3bd2b6d93a1, 14-16 sig figs)
HIST_2026_09_03 = {
    "dtr_pred": {
        "2H": "0.55654466040444",
        "3H": "0.88853612687367",
        "3He": "0.89290857539352",
    },
    "r_sig1": "1.318452615852908",
    "r_L2": "1.275636097818101",
    "r_int_2H": "-0.9179091747058017",
}


def _eval_h3_factorisation(q: mp.mpf, q_str: str, mode: str) -> dict:
    """Closed-form H_3(q) connected-sum evaluation for 2H, 3H, 3He, 4He."""
    qi = mp.mpf(1) / q
    h = q - qi
    z = q**3 / (q**2 + 1)
    delta = flavor_split_leading(q)
    d_pp = mp.mpf(0)
    d_nn = -h
    d_pn = -h * (mp.mpf(1) / 2 - delta / 4)

    two = q + qi
    four = q**3 + q + qi + qi**3
    y3 = four / two**3
    y21 = mp.mpf(1) / two**2
    sig3 = [mp.matrix([[q]])] * 2
    sig21 = build_seminormal_matrices_mp([2, 1], q)[0]

    def h3_trace(word_triples, extra_fn=None) -> mp.mpf:
        tot = mp.mpf(0)
        for yl, sigs in ((y3, sig3), (y21, sig21)):
            dim = sigs[0].rows
            ident = mp.eye(dim)
            prod = mp.eye(dim)
            for c, d_off, g in word_triples:
                prod = prod * (c * sigs[g] + d_off * ident)
            if extra_fn is not None:
                prod = prod * extra_fn(sigs)
            tot += yl * mp.fsum(prod[i, i] for i in range(dim))
        return tot

    pw = nucleon_word_letters(["u", "u", "d"], q=q, intra_order=mode)
    nw = nucleon_word_letters(["u", "d", "d"], q=q, intra_order=mode)
    tau_p = h3_trace(pw)
    tau_n = h3_trace(nw)
    tau_p_sig1 = h3_trace(pw, lambda s: s[0])
    tau_p_l2 = h3_trace(pw, lambda s: s[0] * s[0])

    atoms = {}
    specs = [
        ("2H", 1, 1, [d_pn]),
        ("3H", 1, 2, [d_pn, d_nn]),
        ("3He", 2, 1, [d_pp, d_pn]),
        ("4He", 2, 2, [d_pp, d_pn, d_nn]),
    ]
    for name, z_cnt, n_cnt, bonds in specs:
        tf = (tau_p ** z_cnt) * (tau_n ** n_cnt)
        f_atom = mp.mpf(1)
        f_free_int = mp.mpf(1)
        f_atom_int = mp.mpf(1)
        for d_b in bonds:
            f_atom *= (z + d_b)
            f_free_int *= z
            f_atom_int *= ((h + d_b) * z + 1)
        dtr = tf * (1 - f_atom)
        dtr_int = tf * (f_free_int - f_atom_int)
        atoms[name] = {
            "dtr_pred": dtr,
            "r_int": dtr_int / dtr,
        }

    return {
        "tau_p": tau_p,
        "tau_n": tau_n,
        "r_sig1": tau_p_sig1 / tau_p,
        "r_L2": tau_p_l2 / tau_p,
        "atoms": atoms,
        "q_str": q_str,
    }


def _eval_h6_seminormal_2h(q: mp.mpf, q_str: str, mode: str) -> dict:
    """Direct 6-strand H_6(q) two-row Young-Hoefsmit cross-check on 2H."""
    w_a = atom_braid_word_3A(1, 1, include_inter=True, q=q, intra_order=mode)
    w_f = atom_braid_word_3A(1, 1, include_inter=False, q=q, intra_order=mode)
    two_row = [tuple(p) for p in partitions_of(6) if len(p) <= 2]
    tot_f = [mp.mpf(0)] * 4
    tot_a = [mp.mpf(0)] * 4
    for lam in two_row:
        yl = y_lambda_wenzl_bridge_numeric(list(lam), q_str, mp.mp.dps)
        sigmas = build_seminormal_matrices_mp(list(lam), q)[0]
        dim = sigmas[0].rows
        ident = mp.eye(dim)

        def prod_word(w):
            prod = mp.eye(dim)
            for c, d_off, g in w:
                prod = prod * (c * sigmas[g] + d_off * ident)
            return prod

        pf = prod_word(w_f)
        pa = prod_word(w_a)
        suf_mats = [ident, sigmas[0], sigmas[0] * sigmas[0], sigmas[2]]
        for j, sm in enumerate(suf_mats):
            tot_f[j] += yl * mp.fsum((pf * sm)[i, i] for i in range(dim))
            tot_a[j] += yl * mp.fsum((pa * sm)[i, i] for i in range(dim))
    dtr = tot_f[0] - tot_a[0]
    return {
        "dtr_pred": dtr,
        "r_sig1": (tot_f[1] - tot_a[1]) / dtr,
        "r_L2": (tot_f[2] - tot_a[2]) / dtr,
        "r_int": (tot_f[3] - tot_a[3]) / dtr,
    }


def main() -> int:
    set_compute_dps()
    with mp.workdps(95):
        upstream_records: list = []
        live_w = record_upstream(
            COMP / "qbeta" / "qbeta-derived-w-overdetermined-test.witness.json",
            upstream_records,
        )
        q_str = live_w["parameters"]["q0"]
        q = mp.mpf(q_str)

        grp = _eval_h3_factorisation(q, q_str, "grouped")
        bor = _eval_h3_factorisation(q, q_str, "borromean")
        h6_grp = _eval_h6_seminormal_2h(q, q_str, "grouped")
        h6_bor = _eval_h6_seminormal_2h(q, q_str, "borromean")

        # 1. Cross-check H_3 connected-sum formula vs full H_6 seminormal on 2H (< 1e-75)
        h6_cross_dev = max(
            mp.fabs(grp["atoms"]["2H"]["dtr_pred"] - h6_grp["dtr_pred"]),
            mp.fabs(grp["r_sig1"] - h6_grp["r_sig1"]),
            mp.fabs(grp["r_L2"] - h6_grp["r_L2"]),
            mp.fabs(grp["atoms"]["2H"]["r_int"] - h6_grp["r_int"]),
            mp.fabs(bor["atoms"]["2H"]["dtr_pred"] - h6_bor["dtr_pred"]),
            mp.fabs(bor["r_sig1"] - h6_bor["r_sig1"]),
            mp.fabs(bor["r_L2"] - h6_bor["r_L2"]),
            mp.fabs(bor["atoms"]["2H"]["r_int"] - h6_bor["r_int"]),
        )

        # 2. Match 2026-09-03 witness (3bd2b6d93a1, printed at 14-16 sig figs) via grouped
        hist_dtr_dev = max(
            mp.fabs(grp["atoms"][nm]["dtr_pred"] - mp.mpf(val))
            for nm, val in HIST_2026_09_03["dtr_pred"].items()
        )
        hist_ratio_dev = max(
            mp.fabs(grp["r_sig1"] - mp.mpf(HIST_2026_09_03["r_sig1"])),
            mp.fabs(grp["r_L2"] - mp.mpf(HIST_2026_09_03["r_L2"])),
            mp.fabs(grp["atoms"]["2H"]["r_int"] - mp.mpf(HIST_2026_09_03["r_int_2H"])),
        )

        # 3. Match live 2026-11-22 witness (82c9cbc1344, printed at 14-16 sig figs) via borromean
        live_rows = {r["w"]: r for r in live_w["data"]["overdetermined_test"]}
        live_dtr_dev = max(
            mp.fabs(bor["atoms"][nm]["dtr_pred"] - mp.mpf(live_w["data"]["per_atom"][nm]["dtr_pred"]))
            for nm in ("2H", "3H", "3He", "4He")
        )
        live_ratio_dev = max(
            mp.fabs(bor["r_sig1"] - mp.mpf(live_rows["sigma_1 (control)"]["ratio_to_w1"]["2H"])),
            mp.fabs(bor["r_L2"] - mp.mpf(live_rows["L_2 = T1T1"]["ratio_to_w1"]["2H"])),
            *(
                mp.fabs(
                    bor["atoms"][nm]["r_int"]
                    - mp.mpf(live_rows["interface product"]["ratio_to_w1"][nm])
                )
                for nm in ("2H", "3H", "3He", "4He")
            ),
        )

        # 4. Exact ordering invariance of interface-product ratios across all 4 atoms
        int_invariance_dev = max(
            mp.fabs(grp["atoms"][nm]["r_int"] - bor["atoms"][nm]["r_int"])
            for nm in ("2H", "3H", "3He", "4He")
        )

        wb = WitnessBuilder("qbeta-derived-w-witness-bisect", engine="mpmath")
        wb.add_upstream_records(upstream_records)
        wb.set_description(
            "Exact 80-dps bisection of the qbeta-derived-w-overdetermined-test "
            "witness shift (bean qou-02g1): proves 100% of the move between "
            "blob 3bd2b6d93a1 (computedAt 2026-09-03T04:00:37Z) and blob "
            "82c9cbc1344 (PR #9055, 2026-11-22) is explained by the 2026-09-05 "
            "intra_order='grouped' -> 'borromean' switch (qou-hu1f), with zero "
            "contribution from #8940, 4603bfab4aa, or 89c454294aa."
        )
        wb.set_audit_only("docs/audits/2026-11-24-derived-w-witness-bisect-qou-02g1.md")
        wb.add_parameter("q0", q_str)
        wb.add_data("grouped_80dps", {
            "tau_p": fmt(grp["tau_p"]),
            "tau_n": fmt(grp["tau_n"]),
            "r_sig1": fmt(grp["r_sig1"]),
            "r_L2": fmt(grp["r_L2"]),
            "atoms": {
                nm: {"dtr_pred": fmt(v["dtr_pred"]), "r_int": fmt(v["r_int"])}
                for nm, v in grp["atoms"].items()
            },
        })
        wb.add_data("borromean_80dps", {
            "tau_p": fmt(bor["tau_p"]),
            "tau_n": fmt(bor["tau_n"]),
            "r_sig1": fmt(bor["r_sig1"]),
            "r_L2": fmt(bor["r_L2"]),
            "atoms": {
                nm: {"dtr_pred": fmt(v["dtr_pred"]), "r_int": fmt(v["r_int"])}
                for nm, v in bor["atoms"].items()
            },
        })
        wb.add_data("dtr_scaling_factors_grouped_over_borromean", {
            nm: fmt(grp["atoms"][nm]["dtr_pred"] / bor["atoms"][nm]["dtr_pred"])
            for nm in ("2H", "3H", "3He", "4He")
        })

        wb.add_assertion(
            "h3_factorisation_matches_full_h6_seminormal_2h",
            computed=fmt(h6_cross_dev),
            expected="0",
            tolerance="1e-75",
            source="closed-form H_3 connected-sum formula vs full 6-strand H_6 two-row Hoefsmit product on 2H",
        )
        wb.add_assertion(
            "grouped_reproduces_2026_09_03_witness_dtr_pred",
            computed=fmt(hist_dtr_dev),
            expected="0",
            tolerance="1e-13",
            source="intra_order='grouped' reproduces all 14 printed digits of 2H/3H/3He dtr_pred in blob 3bd2b6d93a1",
        )
        wb.add_assertion(
            "grouped_reproduces_2026_09_03_witness_ratios",
            computed=fmt(hist_ratio_dev),
            expected="0",
            tolerance="1e-15",
            source="intra_order='grouped' reproduces all 16 printed digits of r_sig1, r_L2, r_int(2H) in blob 3bd2b6d93a1",
        )
        wb.add_assertion(
            "borromean_reproduces_2026_11_22_witness_dtr_pred",
            computed=fmt(live_dtr_dev),
            expected="0",
            tolerance="1e-13",
            source="intra_order='borromean' reproduces all printed digits of 2H/3H/3He/4He dtr_pred in live witness 82c9cbc1344",
        )
        wb.add_assertion(
            "borromean_reproduces_2026_11_22_witness_ratios",
            computed=fmt(live_ratio_dev),
            expected="0",
            tolerance="1e-15",
            source="intra_order='borromean' reproduces all 16 printed digits of r_sig1, r_L2, and 4-atom r_int in live witness",
        )
        wb.add_assertion(
            "interface_product_ratio_invariant_under_intra_ordering",
            computed=fmt(int_invariance_dev),
            expected="0",
            tolerance="1e-75",
            source="tau_p^Z * tau_n^N cancels identically in tr_M(Delta * prod sigma_{3k-1}) / tr_M(Delta)",
        )

        wb.save({
            "q0Anchor": "proton",
            "q0AnchorReason": "evaluates H_{3A} atomic chain traces at the proton-pinned q0 of qbeta-derived-w-overdetermined-test.witness.json",
            "q0Value": q_str,
        })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
