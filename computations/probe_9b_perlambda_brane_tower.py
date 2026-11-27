#!/usr/bin/env python3
"""
probe_9b_perlambda_brane_tower.py — PROBE 4 (bean v292 / qou-5t68): 80-dps per-lambda
(per Wedderburn block) rerun of the single-pipeline Borromean brane tower.

Carries `(weight_lambda, chi^lambda(beta_Bor))` for `lambda |- 3` through
`g(x) = -Li_2^q(-x)` per block and collapses last (Markov-weighted sum after
the tower), evaluated at `compute_dps = 95`, `output_dps = 80` (zero float64)
at the canonical proton-ratio substrate pin `q_at(95)` and tower-summed energy
scale `qbeta_e0.canonical(q, m_e)`.

Independent cross-check (`qou-5t68`):
- `borromean-binding-recompute.witness.json` evaluates `B_can0` and `B_tower`
  from the closed-form rational polynomial `tau_rat = (4+h^2-3h^4-h^6)/(h^2+4)`
  without constructing representation matrices or Wenzl hook products.
- `scalar_baseline_matches_committed_witness` here constructs `tau_rep`
  independently from direct 2x2 Young-Hoefsmit seminormal matrix multiplication
  (`(T_1 T_2^{-1})^3`) weighted by Wenzl hook-content rational functions
  (`y_lambda_wenzl_bridge_numeric`), and verifies that both `B_can0` and
  `B_tower` match the committed `borromean-binding-recompute.witness.json` to
  `< 1e-70` across all 9 isotopes (`2H .. 56Fe`).

Ref: docs/audits/2026-06-28-brane-tower-formalize-first-plan.md
Ref: docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md
"""
from __future__ import annotations

import os
import sys
from functools import lru_cache
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_OUTPUT_DPS", "80")

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "qbeta"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from _li_2_q_util import li_2_q  # noqa: E402
from closed_form_tau_M import markov_z as _markov_z  # noqa: E402
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    M_E_MEV,
)
import qbeta_e0 as _qbeta_e0  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim,
    partitions_of,
    y_lambda_wenzl_bridge_numeric,
)

set_compute_dps()

_UPSTREAM_RECORDS: list = []

ISO = [
    ("2H", 1, 1, mp.nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)),
    ("3H", 1, 2, mp.nstr(AME_B_TRITIUM_MEV_VALIDATION, 30)),
    ("3He", 2, 1, mp.nstr(AME_B_HE3_MEV_VALIDATION, 30)),
    ("4He", 2, 2, mp.nstr(AME_B_HE4_MEV_VALIDATION, 30)),
    ("6Li", 3, 3, "31.994564"),
    ("7Li", 3, 4, "39.244533"),
    ("12C", 6, 6, "92.161728"),
    ("16O", 8, 8, "127.619"),
    ("56Fe", 26, 30, "492.254"),
]

TOL_EXACT = mp.mpf("1e-75")
TOL_CROSS = mp.mpf("1e-70")


def _serialise(obj):
    """Render mpf leaves with `_precision.fmt`; leave everything else alone."""
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


@lru_cache(maxsize=None)
def mn_char(lam: tuple, mu: tuple) -> int:
    """Classical S_n character chi^lambda(mu) via Murnaghan-Nakayama (exact int)."""
    lam = tuple(p for p in lam if p > 0)
    if not mu:
        return 1 if not lam else 0
    k, rest = mu[0], mu[1:]
    n_rows = len(lam)
    if n_rows == 0:
        return 0
    beta = [lam[i] + (n_rows - 1 - i) for i in range(n_rows)]
    bset = set(beta)
    total = 0
    for b in beta:
        nb = b - k
        if nb < 0 or nb in bset:
            continue
        height = sum(1 for c in beta if nb < c < b)
        newbeta = sorted((x for x in beta if x != b), reverse=True)
        newbeta.append(nb)
        newbeta.sort(reverse=True)
        m = len(newbeta)
        newlam = tuple(
            p for p in (newbeta[j] - (m - 1 - j) for j in range(m)) if p > 0
        )
        total += (-1) ** height * mn_char(newlam, rest)
    return total


S3_CLASSES = {(1, 1, 1): 1, (2, 1): 3, (3,): 2}


@lru_cache(maxsize=None)
def lr_coeff(nu: tuple, lam: tuple, muu: tuple) -> int:
    """Littlewood-Richardson c^nu_{lambda,mu} for lambda, mu |- 3, nu |- 6."""
    acc = 0
    for a, sa in S3_CLASSES.items():
        for b, sb in S3_CLASSES.items():
            joint = tuple(sorted(a + b, reverse=True))
            acc += sa * sb * mn_char(nu, joint) * mn_char(lam, a) * mn_char(muu, b)
    if acc % 36 != 0:
        raise RuntimeError(f"non-integral LR coefficient for {nu},{lam},{muu}")
    return acc // 36


def chi21_seminormal_direct(q: mp.mpf, qi: mp.mpf) -> mp.mpf:
    """Direct 95-dps Young-Hoefsmit 2x2 matrix trace of chi^{(2,1)}((sigma_1 sigma_2^{-1})^3)."""
    h = q - qi
    a = h / (mp.mpf(1) - q**4)
    ap = h / (mp.mpf(1) - q**-4)
    b = mp.sqrt(a * ap + mp.mpf(1))
    t1 = mp.matrix([[q, mp.mpf(0)], [mp.mpf(0), -qi]])
    t2 = mp.matrix([[a, b], [b, ap]])
    m_mat = (t1 * t2**-1) ** 3
    return m_mat[0, 0] + m_mat[1, 1]


def block_data(q: mp.mpf, qi: mp.mpf):
    """Per-block (lambda |- 3) closed-form characters, direct seminormal characters, and weights."""
    h = q - qi
    two = q + qi
    four = q**3 + q + qi + qi**3
    chi_closed = {
        (3,): mp.mpf(1),
        (2, 1): mp.mpf(2) - mp.mpf(3) * h**4 - h**6,
        (1, 1, 1): mp.mpf(1),
    }
    chi_seminormal = {
        (3,): (q * qi) ** 3,
        (2, 1): chi21_seminormal_direct(q, qi),
        (1, 1, 1): ((-qi) * (-q)) ** 3,
    }
    d = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    y_jones = {(3,): four / two**3, (2, 1): mp.mpf(1) / two**2, (1, 1, 1): mp.mpf(0)}
    q_str_full = mp.nstr(q, mp.mp.dps)
    y_wenzl = {
        tuple(l): y_lambda_wenzl_bridge_numeric(l, q_str_full, mp.mp.dps)
        for l in partitions_of(3)
    }
    return chi_closed, chi_seminormal, d, y_jones, y_wenzl


def make_tower(q: mp.mpf, qi: mp.mpf, me: mp.mpf):
    h = q - qi
    z = _markov_z(q)
    z2 = z * z
    f_pp = z
    f_pn = z
    f_nn = z - h
    e0 = _qbeta_e0.canonical(q=q, m_e=me)

    def g(x: mp.mpf) -> mp.mpf:
        return -li_2_q(-x, q, qi)

    def binding(z_cnt: int, n_cnt: int, tau_scalar: mp.mpf, pair_term):
        a_num = z_cnt + n_cnt
        ratio = (
            (f_pp ** max(z_cnt - 1, 0))
            * (f_pn if z_cnt and n_cnt else mp.mpf(1))
            * (f_nn ** max(n_cnt - 1, 0))
        )
        trf = tau_scalar ** a_num
        dtr = trf - trf * ratio
        pair = mp.mpf(0)
        for cnt, fb in (((z_cnt * (z_cnt - 1)) // 2, f_pp), (z_cnt * n_cnt, f_pn), ((n_cnt * (n_cnt - 1)) // 2, f_nn)):
            if cnt:
                pair += cnt * pair_term(fb)
        return e0 * dtr, e0 * (dtr + z2 * pair)

    return g, binding, (z, z2, f_pp, f_pn, f_nn, e0, h)


def main() -> int:
    set_compute_dps()
    with mp.workdps(95):
        _UPSTREAM_RECORDS.clear()
        me = mp.mpf(str(M_E_MEV))
        q = q_at(95)
        qi = mp.mpf(1) / q
        h = q - qi
        q_str_full = mp.nstr(q, 95)

        # Closed-form rational Borromean trace vs independent seminormal+Wenzl trace
        tau_rat = (mp.mpf(4) + h**2 - mp.mpf(3) * h**4 - h**6) / (h**2 + mp.mpf(4))
        chi, chi_semi, d, y_j, y_w = block_data(q, qi)
        tau_w_closed = mp.fsum(y_w[l] * chi[l] for l in chi)
        tau_rep_independent = mp.fsum(y_w[l] * chi_semi[l] for l in chi_semi)

        dev_jones = mp.fabs(mp.fsum(y_j[l] * chi[l] for l in chi) - tau_rat)
        dev_chi21 = mp.fabs(chi[(2, 1)] - chi_semi[(2, 1)])
        dev_m3_j = mp.fabs(mp.fsum(y_j[l] * d[l] for l in chi) - mp.mpf(1))
        dev_m3_w = mp.fabs(mp.fsum(y_w[l] * d[l] for l in chi) - mp.mpf(1))
        convention_gap = mp.fabs(tau_rat - tau_w_closed)

        print("=" * 76)
        print("PROBE 4 (9b, bean v292 / qou-5t68) — 80-dps per-lambda Borromean brane tower")
        print("=" * 76)
        print(f"  tau (rational closed form)      = {mp.nstr(tau_rat, 25)}")
        print(f"  tau (independent Hoefsmit+Wenzl)= {mp.nstr(tau_rep_independent, 25)}")
        print(f"  Jones/TL decomposition dev      = {mp.nstr(dev_jones, 5)}")
        print(f"  chi^(2,1) closed vs seminormal  = {mp.nstr(dev_chi21, 5)}")
        print(f"  trace-convention gap |tau-tau_W|= {mp.nstr(convention_gap, 5)}")

        g, binding, (_z, _z2, _f_pp, _f_pn, _f_nn, e0, _h) = make_tower(q, qi, me)

        raw_max_arg = max(mp.fabs(chi[a] * chi[b]) for a in chi for b in chi)
        raw_diverges = raw_max_arg >= q

        def norm_blocks(y_map):
            w_map = {l: y_map[l] * d[l] for l in y_map}
            r_map = {l: chi[l] / d[l] for l in chi}
            return w_map, r_map

        w_j, r_j = norm_blocks(y_j)
        w_w, r_w = norm_blocks(y_w)

        def pair_term_scalar(tau_s: mp.mpf):
            def pt(fb: mp.mpf) -> mp.mpf:
                return g(tau_s * tau_s) - g(tau_s * tau_s * fb)
            return pt

        def pair_term_perblock(w_map, r_map):
            def pt(fb: mp.mpf) -> mp.mpf:
                acc = mp.mpf(0)
                for a in w_map:
                    if w_map[a] == 0:
                        continue
                    for b in w_map:
                        if w_map[b] == 0:
                            continue
                        x = r_map[a] * r_map[b]
                        acc += w_map[a] * w_map[b] * (g(x) - g(x * fb))
                return acc
            return pt

        def max_arg(w_map, r_map) -> mp.mpf:
            return max(
                mp.fabs(r_map[a] * r_map[b])
                for a in w_map
                for b in w_map
                if w_map[a] != 0 and w_map[b] != 0
            )

        conv_j = max_arg(w_j, r_j) < q
        conv_w = max_arg(w_w, r_w) < q

        parts3 = [tuple(l) for l in partitions_of(3)]
        parts6 = [tuple(l) for l in partitions_of(6)]
        mn_dims_ok = all(
            mn_char(nu, (1, 1, 1, 1, 1, 1)) == classical_dim(list(nu))
            for nu in parts6
        )
        lr_dims_ok = all(
            sum(lr_coeff(nu, a, b) * classical_dim(list(nu)) for nu in parts6)
            == 20 * classical_dim(list(a)) * classical_dim(list(b))
            for a in parts3
            for b in parts3
        )
        chi_pair = {
            nu: mp.fsum(lr_coeff(nu, a, b) * chi[a] * chi[b] for a in parts3 for b in parts3)
            for nu in parts6
        }
        y6 = {
            nu: y_lambda_wenzl_bridge_numeric(list(nu), q_str_full, mp.mp.dps)
            for nu in parts6
        }
        dev_mult = mp.fabs(mp.fsum(y6[nu] * chi_pair[nu] for nu in parts6) - tau_w_closed**2)
        w6 = {nu: y6[nu] * classical_dim(list(nu)) for nu in parts6}
        r6 = {nu: chi_pair[nu] / classical_dim(list(nu)) for nu in parts6}
        conv_6 = max_arg(w6, r6) < q

        def pair_term_ambient(fb: mp.mpf) -> mp.mpf:
            acc = mp.mpf(0)
            for nu in parts6:
                if w6[nu] == 0:
                    continue
                x = r6[nu]
                acc += w6[nu] * (g(x) - g(x * fb))
            return acc

        variants = {
            # Independent representation-theoretic scalar baseline (Hoefsmit 2x2 + Wenzl hooks)
            "scalar_jones": (tau_rep_independent, pair_term_scalar(tau_rep_independent)),
            "perl_jones": (tau_rat, pair_term_perblock(w_j, r_j)),
            "scalar_wenzl": (tau_w_closed, pair_term_scalar(tau_w_closed)),
            "perl_wenzl": (tau_w_closed, pair_term_perblock(w_w, r_w)),
            "ambient_h6": (tau_w_closed, pair_term_ambient),
        }

        rows = {}
        print(f"\n{'iso':5s}{'B_AME':>9s} | " + " | ".join(f"{v:>13s} err" for v in variants))
        for nm, z_cnt, n_cnt, b_ame_str in ISO:
            b_ame = mp.mpf(b_ame_str)
            rows[nm] = {"Z": z_cnt, "N": n_cnt, "B_AME": b_ame_str}
            line = f"{nm:5s}{mp.nstr(b_ame, 6):>9s} | "
            for vn, (tau_s, pt) in variants.items():
                b0, bt = binding(z_cnt, n_cnt, tau_s, pt)
                rows[nm][vn] = {
                    "B_can0": b0,
                    "B_tower": bt,
                    "errT_AME_over_B": b_ame / bt,
                }
                line += f"{mp.nstr(bt, 6):>13s} {mp.nstr(b_ame / bt, 3):>4s} | "
            print(line)

        # Genuine independent cross-check: Hoefsmit+Wenzl scalar tower vs committed
        # rational-polynomial witness (both B_can0 and B_tower across all 9 isotopes)
        committed = record_upstream(
            HERE / "borromean-binding-recompute.witness.json",
            _UPSTREAM_RECORDS,
        )
        max_base_dev = mp.mpf(0)
        for row in committed["isotopes"]:
            iso_nm = row["iso"]
            mine_b0 = rows[iso_nm]["scalar_jones"]["B_can0"]
            mine_bt = rows[iso_nm]["scalar_jones"]["B_tower"]
            ref_b0 = mp.mpf(str(row["B_can0"]))
            ref_bt = mp.mpf(str(row["B_tower"]))
            dev_b0 = mp.fabs(mine_b0 / ref_b0 - mp.mpf(1))
            dev_bt = mp.fabs(mine_bt / ref_bt - mp.mpf(1))
            max_base_dev = max(max_base_dev, dev_b0, dev_bt)
        print(
            f"\n  independent Hoefsmit+Wenzl scalar tower vs committed witness: "
            f"max rel dev = {mp.nstr(max_base_dev, 6)}"
        )

        max_shift = max(
            mp.fabs(rows[nm]["perl_jones"]["B_tower"] / rows[nm]["scalar_jones"]["B_tower"] - mp.mpf(1))
            for nm, *_ in ISO
        )
        max_shift_w = max(
            mp.fabs(rows[nm]["perl_wenzl"]["B_tower"] / rows[nm]["scalar_wenzl"]["B_tower"] - mp.mpf(1))
            for nm, *_ in ISO
        )
        max_shift_6 = max(
            mp.fabs(rows[nm]["ambient_h6"]["B_tower"] / rows[nm]["scalar_wenzl"]["B_tower"] - mp.mpf(1))
            for nm, *_ in ISO
        )

        wb = WitnessBuilder("probe-9b-perlambda-brane-tower", engine="mpmath")
        wb.add_upstream_records(_UPSTREAM_RECORDS)
        wb.set_description(
            "PROBE 4 (bean v292 / qou-5t68): 80-dps per-lambda collapse-last rerun "
            "of the single-pipeline Borromean brane tower at q_at(95) and canonical "
            "tower-summed E_0. Verifies exact coincidence of SU(2)/TL Jones and Wenzl "
            "r=2 traces on H_3, divergence of the raw-chi per-block tower, universal "
            "convergence of normalized collapse-last variants (Jones, Wenzl, ambient H_6), "
            "and < 1e-70 agreement between the independent 2x2 Young-Hoefsmit+Wenzl "
            "scalar tower and the committed rational-polynomial witness."
        )
        wb.set_audit_only("docs/audits/2026-07-02-9b-probes-alphak-perlambda-tower.md")
        wb.add_parameter("compute_dps", mp.mp.dps)
        wb.add_parameter("q0_source", "qou_substrate.constants.q_at(95) (proton pin)")
        wb.add_parameter("E0_MeV", fmt(e0))
        wb.add_data("tau_pipeline", fmt(tau_rat))
        wb.add_data("tau_hoefsmit_wenzl_independent", fmt(tau_rep_independent))
        wb.add_data("tau_wenzl_convention", fmt(tau_w_closed))
        wb.add_data("trace_convention_gap", fmt(convention_gap))
        wb.add_data("block_data", {
            "chi": {str(l): fmt(chi[l]) for l in chi},
            "dims": {str(l): d[l] for l in d},
            "y_jones": {str(l): fmt(y_j[l]) for l in y_j},
            "y_wenzl": {str(l): fmt(y_w[l]) for l in y_w},
        })
        wb.add_data("raw_perblock", {
            "max_abs_chi_pair_arg": fmt(raw_max_arg),
            "q0": fmt(q),
            "diverges": bool(raw_diverges),
            "invariant": "Li_2^q radius |z| < q + exact chi^{(2,1)}^2 > q_0",
        })
        wb.add_data("ambient_h6", {
            "wenzl_multiplicativity_dev": fmt(dev_mult),
            "chi_pair_by_nu": {str(nu): fmt(chi_pair[nu]) for nu in parts6},
            "converges": bool(conv_6),
        })
        wb.add_data("per_isotope", _serialise(rows))
        wb.add_data("max_tower_shift_vs_scalar", {
            "perl_jones": fmt(max_shift),
            "perl_wenzl": fmt(max_shift_w),
            "ambient_h6": fmt(max_shift_6),
        })

        wb.add_assertion(
            "pipeline_tau_is_jones_tl_decomposition",
            computed=fmt(dev_jones),
            expected="0",
            tolerance="1e-75",
            source="tau closed form = [4]/[2]^3*1 + 1/[2]^2*(2-3h^4-h^6) at 95 working dps",
        )
        wb.add_assertion(
            "chi21_closed_form_vs_seminormal",
            computed=fmt(dev_chi21),
            expected="0",
            tolerance="1e-75",
            source="chi^{(2,1)}((sigma_1 sigma_2^{-1})^3) = 2-3h^4-h^6 vs direct 2x2 Hoefsmit matrix product at 95 dps",
        )
        wb.add_assertion(
            "markov_m3_both_conventions",
            computed=fmt(dev_m3_j + dev_m3_w),
            expected="0",
            tolerance="1e-75",
            source="sum y_lambda d_lambda = 1 under both SU(2)/TL Jones and Wenzl hook-content weights",
        )
        wb.add_assertion(
            "trace_convention_gap_recorded",
            computed=fmt(convention_gap),
            expected="0",
            tolerance="1e-75",
            source="|tau_pipeline - tau_Wenzl| == 0 at z = q^3/(q^2+1) (Wenzl level r=2)",
        )
        wb.add_assertion(
            "raw_perblock_diverges",
            computed=int(raw_diverges),
            expected=1,
            tolerance=0,
            source="chi^{(2,1)}^2 approx 3.98 > q_0 exceeds the proved Li_2^q convergence radius",
        )
        wb.add_assertion(
            "normalized_variants_converge_all_Z",
            computed=int(conv_j and conv_w and conv_6),
            expected=1,
            tolerance=0,
            source="all normalized per-block pair arguments < q_0 (r_lambda = chi^lambda / d_lambda)",
        )
        wb.add_assertion(
            "lr_mn_machinery_validated",
            computed=int(mn_dims_ok and lr_dims_ok and dev_mult < TOL_CROSS),
            expected=1,
            tolerance=0,
            source="MN dims + LR dim-sums exact; sum_nu y_nu^(6) chi^nu(beta otimes beta) = tau_W^2 to < 1e-70",
        )
        wb.add_assertion(
            "scalar_baseline_matches_committed_witness",
            computed=fmt(max_base_dev),
            expected="0",
            tolerance="1e-70",
            source="independent 2x2 Young-Hoefsmit + Wenzl hook-content scalar tower vs committed borromean-binding-recompute.witness.json (both B_can0 and B_tower across all 9 isotopes)",
        )
        wb.add_assertion(
            "perlambda_does_not_close_16O",
            computed=fmt(max(max_shift, max_shift_w, max_shift_6)),
            expected="0",
            tolerance="0.01",
            source="max per-lambda tower shift vs scalar < 1% across all isotopes and all three collapse-last variants",
        )
        wb.save({
            "q0Anchor": "proton",
            "q0AnchorReason": "proton-ratio substrate pin q_at(95) matching borromean-binding-recompute.witness.json",
            "q0Value": fmt(q),
        })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
