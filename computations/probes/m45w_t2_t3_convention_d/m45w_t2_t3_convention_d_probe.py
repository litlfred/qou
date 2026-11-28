#!/usr/bin/env python3
"""EXPLORATORY / DIAGNOSTIC 80-dps measurement of qou-m45w remainder: what happens
to T2 and T3 in `binding_block_multiplicative.py` / `binding_via_interface_knot.py`
when evaluated on Convention-D (`z_D = q_0^3 / (q_0^2 + 1)`) interleaved block Markov
traces vs per-generator Convention-D vs `weight_scheme="normalized_plancherel"`,
including exact `Phi_q` / `Li_2^q` pole diagnostics (`qou-2tuv`) (per
.claude/skills/local/production-vs-exploratory-discipline.md).

Beans `qou-m45w` & `qou-2tuv` (under Stability Epic `qou-s028`).
Pre-registered in `PREREGISTRATION.md` (commit `9a66767a695`) BEFORE numerical
evaluation across `{D, T, 3He}` and the 16-atom sequence.

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - JSON read with `parse_float=str`, zero `float64` imports, literals, or casts,
  - ZERO parameter fitting; downstream witnesses (`binding-block-multiplicative.witness.json`,
    `binding-via-interface-knot.witness.json`) are read-only baselines and NOT mutated.
"""
from __future__ import annotations

from collections import Counter
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations"))
if str(_ROOT / "computations" / "probes" / "light_nuclei_a2_a3") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations" / "probes" / "light_nuclei_a2_a3"))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

import hecke_tl as tl  # noqa: E402
from _li_2_q_util import flavor_split_leading, li_2_q  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from pentagon_reduction_li2q import li_2_q_pentagon  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

INTERFACE_WITNESS = _ROOT / "computations" / "binding-via-interface-knot.witness.json"
BLOCK_MULT_WITNESS = _ROOT / "computations" / "binding-block-multiplicative.witness.json"
AME_JSON = _ROOT / "computations" / "data" / "ame2020.json"

ATOMS_ZN: list[tuple[str, int, int]] = [
    ("D", 1, 1),
    ("T", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("7Li", 3, 4),
    ("9Be", 4, 5),
    ("10B", 5, 5),
    ("12C", 6, 6),
    ("14N", 7, 7),
    ("16O", 8, 8),
    ("20Ne", 10, 10),
    ("24Mg", 12, 12),
    ("28Si", 14, 14),
    ("40Ca", 20, 20),
    ("56Fe", 26, 30),
]


def _load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f, parse_float=str)


def _letter_kind(c: mp.mpf, d: mp.mpf, h0: mp.mpf) -> str:
    """Classify intra-nucleon Hecke letter c*sigma + d*1 for exact Temperley-Lieb sweep."""
    tol = mp.mpf(10) ** (-40)
    if abs(c - mp.mpf(1)) > tol:
        raise ValueError(f"unexpected c={c}")
    for kind, target in (("S", mp.mpf(0)), ("I", -h0), ("A", -h0 / mp.mpf(2))):
        if abs(d - target) <= tol:
            return kind
    raise ValueError(f"unexpected d={d}")


def compute_interleaved_block_traces_80dps(q0: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Exact 80-dps Convention-D Markov trace (trP, trN) of the 11-letter interleaved
    3-strand nucleon words via `hecke_tl`."""
    h0 = q0 - mp.mpf(1) / q0
    ring = tl.Ring(q0, mp.mpf)
    res: list[mp.mpf] = []
    for z_cnt, n_cnt in ((1, 0), (0, 1)):
        letters = [
            (_letter_kind(mp.mpf(c), mp.mpf(d), h0), g)
            for (c, d, g) in atom_braid_word_3A(z_cnt, n_cnt, q=q0)
        ]
        res.append(tl.sweep_trace(tl.word_program(3, letters), ring)[0])
    return res[0], res[1]


def verify_connected_sum_trace_at_d_80dps(
    q0: mp.mpf, tr_p: mp.mpf, tr_n: mp.mpf, f_pn: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    """Verify at 80 dps on 6-strand Deuteron that:
      1. tr_D(W_free) = trP * trN
      2. tr_D(W_atom) = trP * trN * f_pn
    using linearity on the single interface letter sigma_2 + d_pn * 1."""
    h0 = q0 - mp.mpf(1) / q0
    delta = flavor_split_leading(q0)
    d_pn = -h0 * (mp.mpf(1) / mp.mpf(2) - delta / mp.mpf(4))
    ring = tl.Ring(q0, mp.mpf)

    free_letters = [
        (_letter_kind(mp.mpf(c), mp.mpf(d), h0), g)
        for (c, d, g) in atom_braid_word_3A(1, 1, q=q0, include_inter=False)
    ]
    tr_free_6 = tl.sweep_trace(tl.word_program(6, free_letters), ring)[0]

    # Insert pure sigma_2 ('S', 2) between proton (first 11 letters) and neutron (last 11 letters)
    atom_sigma_letters = free_letters[:11] + [("S", 2)] + free_letters[11:]
    tr_atom_sigma_6 = tl.sweep_trace(tl.word_program(6, atom_sigma_letters), ring)[0]
    tr_atom_6 = tr_atom_sigma_6 + d_pn * tr_free_6

    return abs(tr_free_6 - tr_p * tr_n), abs(tr_atom_6 - tr_p * tr_n * f_pn)


def per_generator_polynomials_80dps(q0: mp.mpf) -> dict[str, tuple[mp.mpf, mp.mpf]]:
    """Exact 80-dps reduction of each per-generator bucketed word W_g = alpha_g * sigma_g + beta_g * 1
    using sigma_g^2 = h_0 * sigma_g + 1."""
    one = mp.mpf(1)
    h0 = q0 - one / q0
    delta = flavor_split_leading(q0)

    def reduce_bucket(factors: list[tuple[mp.mpf, mp.mpf]]) -> tuple[mp.mpf, mp.mpf]:
        alpha = mp.mpf(0)
        beta = one
        for c_val, d_val in factors:
            # (alpha * sigma + beta) * (c * sigma + d)
            # = (alpha*c*h0 + alpha*d + beta*c) * sigma + (alpha*c + beta*d) * 1
            new_alpha = alpha * c_val * h0 + alpha * d_val + beta * c_val
            new_beta = alpha * c_val + beta * d_val
            alpha, beta = new_alpha, new_beta
        return alpha, beta

    p_word = atom_braid_word_3A(1, 0, q=q0)
    n_word = atom_braid_word_3A(0, 1, q=q0)
    p_g0 = [(mp.mpf(c), mp.mpf(d)) for (c, d, g) in p_word if g == 0]
    p_g1 = [(mp.mpf(c), mp.mpf(d)) for (c, d, g) in p_word if g == 1]
    n_g0 = [(mp.mpf(c), mp.mpf(d)) for (c, d, g) in n_word if g == 0]
    n_g1 = [(mp.mpf(c), mp.mpf(d)) for (c, d, g) in n_word if g == 1]

    return {
        "p0": reduce_bucket(p_g0),
        "p1": reduce_bucket(p_g1),
        "n0": reduce_bucket(n_g0),
        "n1": reduce_bucket(n_g1),
        "pp": (one, mp.mpf(0)),
        "nn": (one, -h0),
        "pn": (one, -h0 * (one / mp.mpf(2) - delta / mp.mpf(4))),
    }


def eval_li2q_signed(mag: mp.mpf, q0: mp.mpf, q_inv: mp.mpf, sign_mode: str) -> tuple[mp.mpf, mp.mpf, bool]:
    """Evaluate single-term dilogarithm contribution:
      - sign_mode == 'pos_arg' (`binding_block_multiplicative.py`): +Li_2^q(+|x|), pole at |x| >= q0
      - sign_mode == 'neg_arg_pentagon' (`binding_via_interface_knot.py`): -Re Li_2^q(-|x|), smooth past q0
    Returns (real_val, imag_val, hit_unrecoverable_pos_pole)."""
    crossed = bool(mag >= q0)
    if sign_mode == "pos_arg":
        if crossed:
            return mp.mpf("inf"), mp.mpf(0), True
        return li_2_q(mag, q0, q_inv), mp.mpf(0), False
    if sign_mode == "neg_arg_pentagon":
        val = -li_2_q_pentagon(-mag, q0, q_inv)
        if isinstance(val, mp.mpc):
            return val.real, val.imag, False
        return mp.mpf(val), mp.mpf(0), False
    raise ValueError(f"unknown sign_mode {sign_mode!r}")


def evaluate_factor_tower_for_zn(
    z_cnt: int,
    n_cnt: int,
    t1_free: mp.mpf,
    t1_atom: mp.mpf,
    nucleon_factors_p: list[mp.mpf],
    nucleon_factors_n: list[mp.mpf],
    inter_pp: mp.mpf,
    inter_nn: mp.mpf,
    inter_pn: mp.mpf,
    q0: mp.mpf,
    q_inv: mp.mpf,
    z_weight: mp.mpf,
    e0_mev: mp.mpf,
    sign_mode: str,
) -> dict[str, object]:
    """Evaluate T1, T2_free, T2_atom, T2_diff, T3_free, T3_atom, T3_diff (both cancelled
    and uncancelled) for a chain [p]*Z + [n]*N where each proton contributes `nucleon_factors_p`
    (length 2 for per-generator, length 1 for interleaved block) and each interface contributes
    1 in `free` and `inter_{pp,nn,pn}` in `atom`."""
    one = mp.mpf(1)
    free_list: list[tuple[str, mp.mpf]] = []
    atom_list: list[tuple[str, mp.mpf]] = []

    blocks = ["p"] * z_cnt + ["n"] * n_cnt
    for idx, b in enumerate(blocks):
        nf = nucleon_factors_p if b == "p" else nucleon_factors_n
        for k_sub, val in enumerate(nf):
            tag = f"{b}{k_sub}"
            free_list.append((tag, abs(val)))
            atom_list.append((tag, abs(val)))
        if idx + 1 < len(blocks):
            b_next = blocks[idx + 1]
            kind = "pp" if (b, b_next) == ("p", "p") else ("nn" if (b, b_next) == ("n", "n") else "pn")
            iv = abs(inter_pp if kind == "pp" else (inter_nn if kind == "nn" else inter_pn))
            free_list.append((f"I_free_{kind}", one))
            atom_list.append((f"I_atom_{kind}", iv))

    # Check uncancelled T2_free / T2_atom and cancelled T2_diff (interface slots only)
    t2_un_pole = False
    t2_diff_pole = False
    t2_diff_re = mp.mpf(0)
    t2_diff_im = mp.mpf(0)
    max_single_mag = max(max(v for _, v in free_list), max(v for _, v in atom_list))

    for (tf, vf), (ta, va) in zip(free_list, atom_list):
        if vf >= q0 or va >= q0:
            t2_un_pole = True
        if tf != ta:
            rf, imf, pf = eval_li2q_signed(vf, q0, q_inv, sign_mode)
            ra, ima, pa = eval_li2q_signed(va, q0, q_inv, sign_mode)
            if pf or pa:
                t2_diff_pole = True
            t2_diff_re += rf - ra
            t2_diff_im += imf - ima

    # Check uncancelled T3 pairs vs interface-cancelled T3_diff pairs
    n_slots = len(free_list)
    pair_counts_diff: Counter[tuple[mp.mpf, mp.mpf]] = Counter()
    max_pair_all = mp.mpf(0)
    max_pair_inter = mp.mpf(0)
    n_pairs_gt_q0_all = 0
    n_pairs_gt_q0_inter = 0

    for i in range(n_slots):
        tf_i, vf_i = free_list[i]
        ta_i, va_i = atom_list[i]
        i_is_inter = tf_i != ta_i
        for j in range(i + 1, n_slots):
            tf_j, vf_j = free_list[j]
            ta_j, va_j = atom_list[j]
            j_is_inter = tf_j != ta_j
            prod_f = vf_i * vf_j
            prod_a = va_i * va_j
            local_max = max(prod_f, prod_a)
            if local_max > max_pair_all:
                max_pair_all = local_max
            if local_max >= q0:
                n_pairs_gt_q0_all += 1
            if i_is_inter or j_is_inter:
                if local_max > max_pair_inter:
                    max_pair_inter = local_max
                if local_max >= q0:
                    n_pairs_gt_q0_inter += 1
                pair_counts_diff[(prod_f, prod_a)] += 1

    t3_diff_pole = False
    t3_diff_re = mp.mpf(0)
    t3_diff_im = mp.mpf(0)
    for (prod_f, prod_a), cnt in pair_counts_diff.items():
        rf, imf, pf = eval_li2q_signed(prod_f, q0, q_inv, sign_mode)
        ra, ima, pa = eval_li2q_signed(prod_a, q0, q_inv, sign_mode)
        if pf or pa:
            t3_diff_pole = True
        t3_diff_re += mp.mpf(cnt) * (rf - ra)
        t3_diff_im += mp.mpf(cnt) * (imf - ima)

    t3_diff_re *= z_weight * z_weight
    t3_diff_im *= z_weight * z_weight

    t1_diff = t1_free - t1_atom
    if t2_diff_pole or t3_diff_pole:
        b_dim_t1t2 = mp.mpf("inf") if t2_diff_pole else t1_diff + t2_diff_re
        b_dim_t3 = mp.mpf("inf")
        b_mev_t1t2 = mp.mpf("inf") if t2_diff_pole else e0_mev * b_dim_t1t2
        b_mev_t3 = mp.mpf("inf")
    else:
        b_dim_t1t2 = t1_diff + t2_diff_re
        b_dim_t3 = b_dim_t1t2 + t3_diff_re
        b_mev_t1t2 = e0_mev * b_dim_t1t2
        b_mev_t3 = e0_mev * b_dim_t3

    def _s(x: mp.mpf, dps: int = 25) -> str:
        return "inf" if x == mp.mpf("inf") else fmt(x, dps=dps)

    return {
        "T1_free": _s(t1_free),
        "T1_atom": _s(t1_atom),
        "T1_diff": _s(t1_diff),
        "T2_diff": _s(t2_diff_re),
        "T3_diff": _s(t3_diff_re),
        "T3_diff_imag_residue": _s(t3_diff_im),
        "B_MeV_T1T2": _s(b_mev_t1t2),
        "B_MeV_with_T3": _s(b_mev_t3),
        "max_single_abs_V": _s(max_single_mag),
        "max_pair_product_all": _s(max_pair_all),
        "max_pair_product_interface": _s(max_pair_inter),
        "n_pairs_ge_q0_all": n_pairs_gt_q0_all,
        "n_pairs_ge_q0_interface": n_pairs_gt_q0_inter,
        "uncancelled_T2_hits_q0": t2_un_pole,
        "T2_diff_hits_pos_pole": t2_diff_pole,
        "T3_diff_hits_pos_pole": t3_diff_pole,
    }


def main() -> int:
    with mp.workdps(WORK_DPS):
        one, two, four = mp.mpf(1), mp.mpf(2), mp.mpf(4)
        q0 = q_at(dps=WORK_DPS)
        q_inv = one / q0
        h0 = q0 - q_inv
        z_d = (q0 ** 3) / (q0 * q0 + one)
        delta_flav = flavor_split_leading(q0)

        # CAL-1 m_e and neutron-proton Q_beta scale used by binding_block_multiplicative.py
        m_e_mev = codata("electron mass energy equivalent in mev").value
        m_p_mev = codata("proton mass energy equivalent in mev").value
        m_n_mev = codata("neutron mass energy equivalent in mev").value
        q_beta_mev = m_n_mev - m_p_mev - m_e_mev
        e0_lattice_mev = m_e_mev / (q0 * (q0 - one))

        ame_map = {
            (int(x["Z"]), int(x["N"])): mp.mpf(x["binding_energy_total_keV"]) / mp.mpf(1000)
            for x in _load_json(AME_JSON)["entries"]
            if x.get("binding_energy_total_keV") is not None
        }
        w_inter = _load_json(INTERFACE_WITNESS)["data"]["per_atom"]
        w_bmult = _load_json(BLOCK_MULT_WITNESS)["data"]

        # 1. Exact 80-dps interleaved block traces & Deuteron connected-sum check
        tr_p, tr_n = compute_interleaved_block_traces_80dps(q0)
        f_pp = z_d
        f_nn = z_d - h0
        f_pn = z_d - h0 * (one / two - delta_flav / four)
        d_free_resid, d_atom_resid = verify_connected_sum_trace_at_d_80dps(q0, tr_p, tr_n, f_pn)

        # Cross-check against binding-block-multiplicative.witness.json trP, trN
        bmult_vp = mp.mpf(w_bmult["block_factors"]["v_p"])
        bmult_vn = mp.mpf(w_bmult["block_factors"]["v_n"])
        bmult_tr_resid = max(abs(tr_p - bmult_vp), abs(tr_n - bmult_vn))

        # 2. Exact 80-dps per-generator polynomials (alpha_g, beta_g) & Convention-D V_hat_g^D
        polys = per_generator_polynomials_80dps(q0)
        v_conv_d = {k: alpha * z_d + beta for k, (alpha, beta) in polys.items()}

        # Verify against Plancherel witness on D (n=6) and 3He (n=9):
        # For p-p interface (alpha=1, beta=0), vols_full[2] of 3He IS z_Pl(9)!
        z_pl_9 = mp.mpf(w_inter["3He"]["atom_config"]["vols_full"][2])
        he3_poly_keys = ["p0", "p1", "pp", "p0", "p1", "pn", "n0", "n1"]
        he3_witness_vols = [mp.mpf(s) for s in w_inter["3He"]["atom_config"]["vols_full"]]
        plancherel_poly_max_resid = max(
            abs((polys[k][0] * z_pl_9 + polys[k][1]) - v_w)
            for k, v_w in zip(he3_poly_keys, he3_witness_vols)
        )

        # Plancherel factors used on main in binding_block_multiplicative.py
        d_free_pl = [mp.mpf(s) for s in w_inter["D"]["free_config"]["vols_full"]]
        vp0_pl, vp1_pl = d_free_pl[0], d_free_pl[1]
        vn0_pl, vn1_pl = d_free_pl[3], d_free_pl[4]
        vpp_pl = abs(mp.mpf(w_inter["3He"]["atom_config"]["vols_full"][2]))
        vnn_pl = abs(mp.mpf(w_inter["T"]["atom_config"]["vols_full"][5]))
        vpn_pl_zero = mp.mpf(0)

        # 3. Evaluate all pre-registered arms across all 16 nuclei
        per_atom_arms: dict[str, dict[str, object]] = {}
        p0_vs_bmult_max_resid = mp.mpf(0)

        for name, z_cnt, n_cnt in ATOMS_ZN:
            n_pp = max(0, z_cnt - 1)
            n_nn = max(0, n_cnt - 1)
            n_pn = 1 if (z_cnt >= 1 and n_cnt >= 1) else 0

            t1_free_inter = (tr_p ** z_cnt) * (tr_n ** n_cnt)
            t1_atom_exact = (
                t1_free_inter
                * (f_pp ** n_pp)
                * (f_nn ** n_nn)
                * (f_pn ** n_pn)
            )
            t1_free_grouped_d = ((v_conv_d["p0"] * v_conv_d["p1"]) ** z_cnt) * (
                (v_conv_d["n0"] * v_conv_d["n1"]) ** n_cnt
            )
            t1_atom_grouped_d = (
                t1_free_grouped_d
                * (v_conv_d["pp"] ** n_pp)
                * (v_conv_d["nn"] ** n_nn)
                * (v_conv_d["pn"] ** n_pn)
            )

            # Arm P0: hybrid baseline currently on main (`binding_block_multiplicative.py`)
            arm_p0 = evaluate_factor_tower_for_zn(
                z_cnt, n_cnt,
                t1_free=t1_free_inter, t1_atom=mp.mpf(0),
                nucleon_factors_p=[vp0_pl, vp1_pl],
                nucleon_factors_n=[vn0_pl, vn1_pl],
                inter_pp=vpp_pl, inter_nn=vnn_pl, inter_pn=vpn_pl_zero,
                q0=q0, q_inv=q_inv, z_weight=z_d, e0_mev=q_beta_mev,
                sign_mode="pos_arg",
            )
            bmult_row = w_bmult["per_atom"][name]
            p0_resid = max(
                abs(mp.mpf(arm_p0["T2_diff"]) - mp.mpf(bmult_row["T2_diff"])),
                abs(mp.mpf(arm_p0["T3_diff"]) - mp.mpf(bmult_row["T3_diff"])),
            )
            if p0_resid > p0_vs_bmult_max_resid:
                p0_vs_bmult_max_resid = p0_resid

            # Arm D1a: per-generator Convention-D with positive-arg Li_2^q(+|V|)
            arm_d1a = evaluate_factor_tower_for_zn(
                z_cnt, n_cnt,
                t1_free=t1_free_grouped_d, t1_atom=t1_atom_grouped_d,
                nucleon_factors_p=[v_conv_d["p0"], v_conv_d["p1"]],
                nucleon_factors_n=[v_conv_d["n0"], v_conv_d["n1"]],
                inter_pp=v_conv_d["pp"], inter_nn=v_conv_d["nn"], inter_pn=v_conv_d["pn"],
                q0=q0, q_inv=q_inv, z_weight=z_d, e0_mev=q_beta_mev,
                sign_mode="pos_arg",
            )

            # Arm D1b: per-generator Convention-D with negative-arg pentagon -Li_2^q(-|V|)
            arm_d1b = evaluate_factor_tower_for_zn(
                z_cnt, n_cnt,
                t1_free=t1_free_grouped_d, t1_atom=t1_atom_grouped_d,
                nucleon_factors_p=[v_conv_d["p0"], v_conv_d["p1"]],
                nucleon_factors_n=[v_conv_d["n0"], v_conv_d["n1"]],
                inter_pp=v_conv_d["pp"], inter_nn=v_conv_d["nn"], inter_pn=v_conv_d["pn"],
                q0=q0, q_inv=q_inv, z_weight=z_d, e0_mev=q_beta_mev,
                sign_mode="neg_arg_pentagon",
            )

            # Arm D2a: interleaved nucleon block traces (trP, trN) + Markov interface scalars, +Li_2^q(+|V|)
            arm_d2a = evaluate_factor_tower_for_zn(
                z_cnt, n_cnt,
                t1_free=t1_free_inter, t1_atom=t1_atom_exact,
                nucleon_factors_p=[tr_p],
                nucleon_factors_n=[tr_n],
                inter_pp=f_pp, inter_nn=f_nn, inter_pn=f_pn,
                q0=q0, q_inv=q_inv, z_weight=z_d, e0_mev=q_beta_mev,
                sign_mode="pos_arg",
            )

            # Arm D2b: interleaved nucleon block traces (trP, trN) + Markov interface scalars, -Li_2^q(-|V|)
            arm_d2b = evaluate_factor_tower_for_zn(
                z_cnt, n_cnt,
                t1_free=t1_free_inter, t1_atom=t1_atom_exact,
                nucleon_factors_p=[tr_p],
                nucleon_factors_n=[tr_n],
                inter_pp=f_pp, inter_nn=f_nn, inter_pn=f_pn,
                q0=q0, q_inv=q_inv, z_weight=z_d, e0_mev=q_beta_mev,
                sign_mode="neg_arg_pentagon",
            )

            # Arm D3: single whole-word Convention-D Markov trace passed to T1+T2+T3 tower
            # plus extensive log-ratio benchmark B_log = E_0 * ln(tr_free / tr_atom)
            t1_w_diff = t1_free_inter - t1_atom_exact
            t2_w_pos = li_2_q(t1_free_inter, q0, q_inv) - li_2_q(t1_atom_exact, q0, q_inv)
            t2_w_neg = (
                -li_2_q_pentagon(-t1_free_inter, q0, q_inv)
                + li_2_q_pentagon(-t1_atom_exact, q0, q_inv)
            )
            # Single scalar trace has 0 distinct pairs (n_factors = 1 -> T3 = 0)
            b_mev_d3_pos = q_beta_mev * (t1_w_diff + t2_w_pos)
            b_mev_d3_neg = q_beta_mev * (t1_w_diff + mp.mpf(t2_w_neg.real if isinstance(t2_w_neg, mp.mpc) else t2_w_neg))
            log_ratio = mp.log(t1_free_inter / t1_atom_exact)
            b_log_qbeta_mev = q_beta_mev * log_ratio
            b_log_e0_mev = e0_lattice_mev * log_ratio

            b_ame = ame_map[(z_cnt, n_cnt)]
            per_atom_arms[name] = {
                "Z": z_cnt,
                "N": n_cnt,
                "A": z_cnt + n_cnt,
                "B_AME_MeV": fmt(b_ame, dps=20),
                "P0_hybrid_main": arm_p0,
                "D1a_per_gen_convD_pos_arg": arm_d1a,
                "D1b_per_gen_convD_neg_pentagon": arm_d1b,
                "D2a_interleaved_block_convD_pos_arg": arm_d2a,
                "D2b_interleaved_block_convD_neg_pentagon": arm_d2b,
                "D3_whole_word_trace_convD": {
                    "tr_free": fmt(t1_free_inter, dps=25),
                    "tr_atom": fmt(t1_atom_exact, dps=25),
                    "B_MeV_pos_arg_Qbeta": fmt(b_mev_d3_pos, dps=20),
                    "B_MeV_neg_arg_Qbeta": fmt(b_mev_d3_neg, dps=20),
                    "B_log_free_energy_Qbeta_MeV": fmt(b_log_qbeta_mev, dps=20),
                    "B_log_free_energy_E0_lattice_MeV": fmt(b_log_e0_mev, dps=20),
                },
            }

        print("=== qou-m45w & qou-2tuv: T2/T3 Convention-D vs Plancherel Measurement (80 dps) ===")
        print(f"  q0 (proton)        = {fmt(q0, dps=25)}")
        print(f"  z_D = q0^3/(q0^2+1)= {fmt(z_d, dps=25)}  (vs z_Pl(9) = {fmt(z_pl_9, dps=18)})")
        print(f"  Interleaved blocks : trP = {mp.nstr(tr_p, 12)}, trN = {mp.nstr(tr_n, 12)}")
        print(f"  Markov interfaces  : f_pp = {mp.nstr(f_pp, 12)}, f_nn = {mp.nstr(f_nn, 12)}, f_pn = {mp.nstr(f_pn, 12)}")
        print("  Per-generator Convention-D V_hat^D = alpha_g * z_D + beta_g:")
        for k in ("p0", "p1", "n0", "n1", "pp", "nn", "pn"):
            v_val = v_conv_d[k]
            pole_flag = "  <-- EXCEEDS q0 (Phi_q POLE!)" if abs(v_val) >= q0 else ""
            print(f"    V_D[{k:<2}] = {mp.nstr(v_val, 15)}{pole_flag}")
        print(
            f"  Grouped product V_D[p0]*V_D[p1] = {mp.nstr(v_conv_d['p0']*v_conv_d['p1'], 12)} "
            f"!= trP = {mp.nstr(tr_p, 12)}"
        )
        print(
            f"  Grouped product V_D[n0]*V_D[n1] = {mp.nstr(v_conv_d['n0']*v_conv_d['n1'], 12)} "
            f"!= trN = {mp.nstr(tr_n, 12)}"
        )
        print("\n  Sample B_MeV_with_T3 across arms (D, T, 3He, 4He, 12C, 56Fe):")
        for nm in ("D", "T", "3He", "4He", "12C", "56Fe"):
            r = per_atom_arms[nm]
            print(
                f"    {nm:<4} AME={mp.nstr(mp.mpf(r['B_AME_MeV']), 6):>8} | "
                f"P0={r['P0_hybrid_main']['B_MeV_with_T3'][:9]:>9} | "
                f"D1a(+)= {r['D1a_per_gen_convD_pos_arg']['B_MeV_with_T3'][:9]:>9} | "
                f"D1b(-)= {r['D1b_per_gen_convD_neg_pentagon']['B_MeV_with_T3'][:9]:>9} | "
                f"D2a(int+)= {r['D2a_interleaved_block_convD_pos_arg']['B_MeV_with_T3'][:9]:>9} | "
                f"D2b(int-)= {r['D2b_interleaved_block_convD_neg_pentagon']['B_MeV_with_T3'][:9]:>9} | "
                f"Log(E0)= {r['D3_whole_word_trace_convD']['B_log_free_energy_E0_lattice_MeV'][:9]:>9}"
            )

        # Structural assertions (exact invariants, pole detection, and pole-freedom of D2)
        d1a_hits_pole_on_all_atoms = int(
            all(
                bool(per_atom_arms[nm]["D1a_per_gen_convD_pos_arg"]["T3_diff_hits_pos_pole"])
                or bool(per_atom_arms[nm]["D1a_per_gen_convD_pos_arg"]["uncancelled_T2_hits_q0"])
                for nm, _, _ in ATOMS_ZN
            )
        )
        d2_globally_pole_free = int(
            all(
                per_atom_arms[nm]["D2a_interleaved_block_convD_pos_arg"]["n_pairs_ge_q0_all"] == 0
                and not per_atom_arms[nm]["D2a_interleaved_block_convD_pos_arg"]["uncancelled_T2_hits_q0"]
                for nm, _, _ in ATOMS_ZN
            )
        )
        noncommutativity_gap_confirmed = int(
            abs(v_conv_d["p0"] * v_conv_d["p1"] - tr_p) > mp.mpf("0.1")
            and abs(v_conv_d["n0"] * v_conv_d["n1"] - tr_n) > mp.mpf("0.1")
        )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "80-dps proton-pinned diagnostic measurement of the qou-m45w remainder: "
            "evaluates T2 and T3 in binding_block_multiplicative / binding_via_interface_knot "
            "under Convention-D per-generator V_hat^D (Arms D1a/D1b) and Convention-D "
            "interleaved nucleon block Markov traces trP, trN + Markov interface scalars "
            "(Arms D2a/D2b and whole-word D3) vs the hybrid normalized_plancherel baseline "
            "on main (Arm P0), isolating exact Phi_q / Li_2^q poles at z = +q0 (qou-2tuv)."
        )
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("preregistration_commit", "9a66767a695")
        wb.add_parameter("z_D", fmt(z_d, dps=OUT_DPS))
        wb.add_parameter("h0", fmt(h0, dps=OUT_DPS))
        wb.add_parameter("delta_flavor_split_leading", fmt(delta_flav, dps=OUT_DPS))
        wb.add_parameter("Q_beta_MeV", fmt(q_beta_mev, dps=OUT_DPS))
        wb.add_parameter("E0_lattice_MeV", fmt(e0_lattice_mev, dps=OUT_DPS))

        wb.add_data("factor_comparison_80dps", {
            "interleaved_block_convD": {
                "trP": fmt(tr_p, dps=OUT_DPS),
                "trN": fmt(tr_n, dps=OUT_DPS),
                "f_pp": fmt(f_pp, dps=OUT_DPS),
                "f_nn": fmt(f_nn, dps=OUT_DPS),
                "f_pn": fmt(f_pn, dps=OUT_DPS),
                "deuteron_free_connected_sum_residual": fmt(d_free_resid, dps=OUT_DPS),
                "deuteron_atom_connected_sum_residual": fmt(d_atom_resid, dps=OUT_DPS),
            },
            "per_generator_convD": {
                k: {
                    "alpha": fmt(polys[k][0], dps=OUT_DPS),
                    "beta": fmt(polys[k][1], dps=OUT_DPS),
                    "V_hat_D": fmt(v_conv_d[k], dps=OUT_DPS),
                    "exceeds_q0_pole": bool(abs(v_conv_d[k]) >= q0),
                }
                for k in ("p0", "p1", "n0", "n1", "pp", "nn", "pn")
            },
            "grouped_vs_interleaved_convD": {
                "V_p0_times_V_p1": fmt(v_conv_d["p0"] * v_conv_d["p1"], dps=OUT_DPS),
                "trP_interleaved": fmt(tr_p, dps=OUT_DPS),
                "V_n0_times_V_n1": fmt(v_conv_d["n0"] * v_conv_d["n1"], dps=OUT_DPS),
                "trN_interleaved": fmt(tr_n, dps=OUT_DPS),
            },
            "plancherel_witness_crosscheck": {
                "z_Pl_at_H9": fmt(z_pl_9, dps=30),
                "max_3He_vols_full_residual_f64_floor": fmt(plancherel_poly_max_resid, dps=20),
                "P0_vs_binding_block_multiplicative_witness_max_resid": fmt(
                    p0_vs_bmult_max_resid, dps=20
                ),
            },
        })
        wb.add_data("per_atom_arms", per_atom_arms)

        wb.add_assertion(
            "interleaved_trP_trN_match_main_witness",
            fmt(bmult_tr_resid, dps=15),
            "0",
            "1e-55",
            source="binding-block-multiplicative.witness.json trP, trN",
        )
        wb.add_assertion(
            "deuteron_6strand_connected_sum_factorization_80dps",
            fmt(max(d_free_resid, d_atom_resid), dps=15),
            "0",
            "1e-70",
            source="BraidedBlockShiftTrace + InterfaceScalar on H_6(q0)",
        )
        wb.add_assertion(
            "per_generator_polynomials_match_H9_plancherel_witness_to_f64",
            fmt(plancherel_poly_max_resid, dps=15),
            "0",
            "1e-13",
            source="binding-via-interface-knot.witness.json 3He vols_full",
        )
        wb.add_assertion(
            "arm_P0_reproduces_main_binding_block_multiplicative_T2_T3",
            fmt(p0_vs_bmult_max_resid, dps=15),
            "0",
            "1e-20",
            source="binding-block-multiplicative.witness.json T2_diff, T3_diff (50-dps vs 80-dps q0)",
        )
        wb.add_assertion(
            "per_generator_convD_hits_q0_pole_in_pos_arg_form",
            d1a_hits_pole_on_all_atoms,
            1,
            0,
            source="qou-2tuv Phi_q pole at z = +q0 when V_hat^D >= q0",
        )
        wb.add_assertion(
            "interleaved_block_convD_is_globally_pole_free",
            d2_globally_pole_free,
            1,
            0,
            source="all trP, trN, f_pp, f_nn, f_pn in (0, 1) < q0",
        )
        wb.add_assertion(
            "grouped_per_generator_product_differs_from_interleaved_trace",
            noncommutativity_gap_confirmed,
            1,
            0,
            source="qou-m45w sigma_0 sigma_1 non-commutativity under Convention D",
        )
        wb.add_caveat(
            "Diagnostic measurement only; zero fitting. Both single-crossing chain interfaces "
            "(excluded by ChainBondOrderDependence and superseded by the 2026-11-15 gamma-gamma "
            "bond ruling) and non-extensive trace/dilog differences (LogFormUniqueness) are "
            "recorded solely to answer the qou-m45w / qou-2tuv diagnostic."
        )
        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
