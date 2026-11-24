#!/usr/bin/env python3
"""80-dps diagnostic probe for Q-Drain-9 beans `qou-zrx2` and `qou-cds5` (parent `qou-v2om`).

Formal Lean 4 backing (`0 sorry`, `0 axiom`, zero empirical literals, §7c generic):
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/ClassicalTraceFloorParity.lean`
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/DeltaLambdaRStarOrderBounds.lean`

Scope & anti-fit discipline:
  - `mpmath` at `WORK_DPS = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - exact integer / `Fraction` arithmetic for all `q = 1` cycle-count and interface-parity laws,
  - pure `mpmath` Hoefsmit seminormal character evaluation (zero `float64`, zero `pyhecke_native`
    f64 calls, `probe-float64-guard.py --diff` clean),
  - zero fitting (CAL-1 `m_e` and CAL-2 `q_0` only; `mu_3 = 0.4708` enters solely as the historical
    read-only comparison target from `#4320`/`#4364` to verify `qou-cds5`).
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
    _ROOT / "computations" / "substrate",
    _ROOT / "computations" / "hecke",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import value_str  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

from hecke_characters import standard_young_tableaux  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, chi_lambda_of_word_mp, seminormal_matrices_mp  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from y_lambda_wenzl_bridge import classical_dim, partitions_of, schur_principal  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)


# ---------------------------------------------------------------------------
# Pure-mpmath Hoefsmit 1x1 / 2x2 block-pair trace evaluator (zero float64)
# ---------------------------------------------------------------------------
def build_hoefsmit_blocks_mp(shape: tuple[int, ...], cache: BlockCacheMP):
    """Build per-generator `(ones, pairs)` lists of Hoefsmit 1x1 and 2x2 blocks in `mpf`."""
    syts, _cells, contents = standard_young_tableaux(list(shape))
    dim = len(syts)
    if dim == 0:
        return [], 0
    n = sum(shape)
    syt_keys = [tuple(sorted(t.items())) for t in syts]
    syt_to_idx = {k: i for i, k in enumerate(syt_keys)}

    gens = []
    for k in range(1, n):
        ones: list[tuple[int, mp.mpf]] = []
        pairs: list[tuple[int, int, mp.mpf, mp.mpf, mp.mpf]] = []
        seen = [False] * dim
        for i in range(dim):
            if seen[i]:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            a, a_prime, b = cache.get(contents[ci_k1] - contents[ci_k])
            swapped = dict(syts[i])
            swapped[k] = ci_k1
            swapped[k + 1] = ci_k
            j = syt_to_idx.get(tuple(sorted(swapped.items())))
            if j is None or j == i:
                ones.append((i, a))
                seen[i] = True
            else:
                ones_pair = (i, j, a, a_prime, b)
                pairs.append(ones_pair)
                seen[i] = True
                seen[j] = True
        gens.append((ones, pairs))
    return gens, dim


def trace_word_blocks_mp(gens, dim: int, word) -> mp.mpf:
    """Exact `tr prod_k (c_k * sigma_{g_k} + d_k * I)` in `mpf` via 1x1/2x2 column updates."""
    if dim == 0:
        return mp.mpf(0)
    zero = mp.mpf(0)
    one = mp.mpf(1)
    mat = [[one if r == c else zero for c in range(dim)] for r in range(dim)]
    coerced = [(mp.mpf(c), mp.mpf(d), int(g)) for (c, d, g) in word]
    for c_val, d_val, g_idx in coerced:
        ones, pairs = gens[g_idx]
        for i, a in ones:
            s = c_val * a + d_val
            for row in mat:
                row[i] = row[i] * s
        for i, j, a, a_prime, b in pairs:
            sa = c_val * a + d_val
            sap = c_val * a_prime + d_val
            sb = c_val * b
            for row in mat:
                u = row[i]
                v = row[j]
                row[i] = u * sa + v * sb
                row[j] = u * sb + v * sap
    return mp.fsum(mat[i][i] for i in range(dim))


# ---------------------------------------------------------------------------
# Wenzl-Ocneanu & Beasley-Witten block weights in pure mpmath
# ---------------------------------------------------------------------------
def q_int_bal(q: mp.mpf, m: int) -> mp.mpf:
    return (q ** m - q ** (-m)) / (q - 1 / q)


def z_convention_c(q: mp.mpf) -> mp.mpf:
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def z_convention_d(q: mp.mpf) -> mp.mpf:
    return q ** 3 / (q ** 2 + 1)


def wenzl_weights_at_z(n: int, q: mp.mpf, z: mp.mpf) -> dict[tuple[int, ...], mp.mpf]:
    q_sq = q ** 2
    x_param = q * z / (1 - q_sq + q * z)
    parts = [tuple(p) for p in partitions_of(n)]
    raw = {lam: schur_principal(list(lam), x_param, q_sq) for lam in parts}
    norm = mp.fsum(classical_dim(list(lam)) * raw[lam] for lam in parts)
    return {lam: raw[lam] / norm for lam in parts}


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    if not lam:
        return []
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    out: list[int] = []
    for i, r in enumerate(lam):
        for j in range(r):
            out.append((r - 1 - j) + (conj[j] - 1 - i) + 1)
    return out


def dq_balanced(lam: tuple[int, ...], q: mp.mpf) -> mp.mpf:
    n = sum(lam)
    num = mp.mpf(1)
    for m in range(1, n + 1):
        num *= q_int_bal(q, m)
    den = mp.mpf(1)
    for h_len in hook_lengths(lam):
        den *= q_int_bal(q, h_len)
    return num / den


# ---------------------------------------------------------------------------
# Part A: qou-zrx2 exact q=1 interface-parity & 80-dps classical floor shares
# ---------------------------------------------------------------------------
def perm_of_word_q1(word, n: int) -> list[int]:
    p = list(range(n))
    for _c, _d, g in word:
        gi = int(g)
        p[gi], p[gi + 1] = p[gi + 1], p[gi]
    return p


def num_cycles(perm: list[int]) -> int:
    n = len(perm)
    seen = [False] * n
    c = 0
    for i in range(n):
        if not seen[i]:
            c += 1
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cur = perm[cur]
    return c


def odd_interfaces_count(z_cnt: int, n_cnt: int, m_pp: int = 1, m_pn: int = 1, m_nn: int = 1) -> int:
    total = 0
    if z_cnt >= 1:
        total += (z_cnt - 1) * (m_pp % 2)
    if n_cnt >= 1:
        total += (n_cnt - 1) * (m_nn % 2)
    if z_cnt >= 1 and n_cnt >= 1:
        total += m_pn % 2
    return total


def floor_parity_fraction(a_mass: int, odd_cnt: int) -> Fraction:
    half = Fraction(1, 2)
    return (half ** a_mass) * (1 - (half ** odd_cnt))


def run_part_a_zrx2(q0: mp.mpf, cache: BlockCacheMP) -> dict:
    # 1. Exact q=1 permutation cycle & interface-parity sweep across A=1..12
    isotopes = [
        ("p", 1, 0), ("n", 0, 1),
        ("2H", 1, 1), ("pp", 2, 0), ("nn", 0, 2),
        ("3H", 1, 2), ("3He", 2, 1),
        ("4He", 2, 2), ("5Li", 3, 2), ("6Li", 3, 3),
        ("7Li", 3, 4), ("8Be", 4, 4), ("10B", 5, 5), ("12C", 6, 6),
    ]
    mult_cases = [
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 3),
        (1, 2, 1),
        (2, 1, 2),
    ]
    parity_checks = 0
    parity_mismatches = 0
    invariance_checks = 0
    invariance_mismatches = 0

    for _label, z_cnt, n_cnt in isotopes:
        a_mass = z_cnt + n_cnt
        n_strands = 3 * a_mass
        for m_pp, m_pn, m_nn in mult_cases:
            odd_cnt = odd_interfaces_count(z_cnt, n_cnt, m_pp, m_pn, m_nn)
            pred = floor_parity_fraction(a_mass, odd_cnt)
            seen_floors = set()
            for intra in ("borromean", "grouped"):
                for pn_conv in ("bring_color_weighted", "strict_averaged"):
                    wf = atom_braid_word_3A(
                        z_cnt, n_cnt, include_inter=False,
                        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                        intra_order=intra, pn_convention=pn_conv, q=q0,
                    )
                    wa = atom_braid_word_3A(
                        z_cnt, n_cnt, include_inter=True,
                        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                        intra_order=intra, pn_convention=pn_conv, q=q0,
                    )
                    cf = num_cycles(perm_of_word_q1(wf, n_strands))
                    ca = num_cycles(perm_of_word_q1(wa, n_strands))
                    meas = Fraction(1, 2) ** (n_strands - cf) - Fraction(1, 2) ** (n_strands - ca)
                    parity_checks += 1
                    if cf != 2 * a_mass or ca != 2 * a_mass - odd_cnt or meas != pred:
                        parity_mismatches += 1
                    seen_floors.add(meas)
            invariance_checks += 1
            if len(seen_floors) != 1:
                invariance_mismatches += 1

    # 2. 80-dps Convention-D exact trace difference & classical floor shares for 2H, 3H, 3He
    # Under Convention D, only <=2-row shapes have nonzero weight (exact, 0 truncation).
    zd = z_convention_d(q0)
    y6_d = wenzl_weights_at_z(6, q0, zd)
    y9_d = wenzl_weights_at_z(9, q0, zd)
    two_row_6 = [lam for lam in y6_d if len(lam) <= 2]
    two_row_9 = [lam for lam in y9_d if len(lam) <= 2]

    gens6 = {lam: build_hoefsmit_blocks_mp(lam, cache) for lam in two_row_6}
    gens9 = {lam: build_hoefsmit_blocks_mp(lam, cache) for lam in two_row_9}

    # Self-test our block-pair trace evaluator against hoefsmit_mpmath.chi_lambda_of_word_mp on H_6
    selftest_max_err = mp.mpf(0)
    wf_d_bor = atom_braid_word_3A(1, 1, include_inter=False, intra_order="borromean", q=q0)
    for lam in two_row_6:
        sigs, dim_dense, _ = seminormal_matrices_mp(list(lam), cache=cache)
        chi_dense = chi_lambda_of_word_mp(sigs, dim_dense, wf_d_bor, 5)
        g_blocks, dim_b = gens6[lam]
        chi_fast = trace_word_blocks_mp(g_blocks, dim_b, wf_d_bor)
        selftest_max_err = max(selftest_max_err, abs(chi_dense - chi_fast))

    def tr_d_exact(z_cnt: int, n_cnt: int, intra: str):
        a_mass = z_cnt + n_cnt
        y_map = y6_d if a_mass == 2 else y9_d
        g_map = gens6 if a_mass == 2 else gens9
        shapes = two_row_6 if a_mass == 2 else two_row_9
        wf = atom_braid_word_3A(z_cnt, n_cnt, include_inter=False, intra_order=intra, q=q0)
        wa = atom_braid_word_3A(z_cnt, n_cnt, include_inter=True, intra_order=intra, q=q0)
        tr_f = mp.fsum(y_map[lam] * trace_word_blocks_mp(*g_map[lam], wf) for lam in shapes)
        tr_a = mp.fsum(y_map[lam] * trace_word_blocks_mp(*g_map[lam], wa) for lam in shapes)
        return tr_f, tr_a, tr_f - tr_a

    shares = {}
    for iso_name, z_cnt, n_cnt, c0_frac in (
        ("2H", 1, 1, Fraction(1, 8)),
        ("3H", 1, 2, Fraction(3, 32)),
        ("3He", 2, 1, Fraction(3, 32)),
    ):
        c0_mp = mp.mpf(c0_frac.numerator) / mp.mpf(c0_frac.denominator)
        row = {"c0_exact": f"{c0_frac.numerator}/{c0_frac.denominator}", "c0_decimal": fmt(c0_mp, dps=OUT_DPS)}
        for intra in ("borromean", "grouped"):
            tr_f, tr_a, dtr = tr_d_exact(z_cnt, n_cnt, intra)
            share_pct = mp.mpf(100) * c0_mp / dtr
            row[intra] = {
                "tr_free": fmt(tr_f, dps=OUT_DPS),
                "tr_atom": fmt(tr_a, dps=OUT_DPS),
                "delta_tr": fmt(dtr, dps=OUT_DPS),
                "floor_share_pct": fmt(share_pct, dps=20),
            }
        shares[iso_name] = row

    d_bor_pct = mp.mpf(shares["2H"]["borromean"]["floor_share_pct"])
    d_grp_pct = mp.mpf(shares["2H"]["grouped"]["floor_share_pct"])

    return {
        "parity_checks": parity_checks,
        "parity_mismatches": parity_mismatches,
        "invariance_checks": invariance_checks,
        "invariance_mismatches": invariance_mismatches,
        "hoefsmit_block_selftest_max_err": selftest_max_err,
        "floor_shares_convention_D_80dps": shares,
        "deuteron_borromean_pct": d_bor_pct,
        "deuteron_grouped_pct": d_grp_pct,
    }


# ---------------------------------------------------------------------------
# Part B: qou-cds5 80-dps Convention-D r* verification vs PR #4766 [2.04, 2.16]
# ---------------------------------------------------------------------------
def block_transposition_gens(a: int, width: int = 3) -> list[int]:
    gens: list[int] = []
    for r in range(width):
        for g in range(a + width - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def cabled_borromean_inter_word(h_val: mp.mpf) -> list[tuple[mp.mpf, mp.mpf, int]]:
    da = block_transposition_gens(0, 3)
    db_inv = list(reversed(block_transposition_gens(3, 3)))
    one = mp.mpf(1)
    zero = mp.mpf(0)
    neg_h = -h_val
    word: list[tuple[mp.mpf, mp.mpf, int]] = []
    for _ in range(3):
        word.extend((one, zero, g) for g in da)
        word.extend((one, neg_h, g) for g in db_inv)
    return word


def run_part_b_cds5(q0: mp.mpf, e0_mev: mp.mpf, cache: BlockCacheMP) -> dict:
    h_val = q0 - 1 / q0
    zc = z_convention_c(q0)
    zd = z_convention_d(q0)
    mu3_target = mp.mpf("0.4708")  # read-only historical residual target (#4320/#4364)

    parts9 = [tuple(p) for p in partitions_of(9)]
    two_row9 = [lam for lam in parts9 if len(lam) <= 2]

    y9_c = wenzl_weights_at_z(9, q0, zc)
    y9_d = wenzl_weights_at_z(9, q0, zd)

    qfact9 = mp.mpf(1)
    for m in range(1, 10):
        qfact9 *= q_int_bal(q0, m)
    dq_sq9 = {lam: dq_balanced(lam, q0) ** 2 for lam in parts9}
    d2_norm = mp.fsum(dq_sq9[lam] for lam in parts9)
    w_raw9 = {lam: dq_sq9[lam] / qfact9 for lam in parts9}
    w_geom9 = {lam: dq_sq9[lam] / d2_norm for lam in parts9}

    sum_y_c = mp.fsum(y9_c[lam] for lam in parts9)
    sum_y_d = mp.fsum(y9_d[lam] for lam in two_row9)
    sum_w_geom = mp.fsum(w_geom9[lam] for lam in parts9)

    gens9_all = {lam: build_hoefsmit_blocks_mp(lam, cache) for lam in parts9}

    def all_chis9(word, shapes=parts9) -> dict[tuple[int, ...], mp.mpf]:
        return {lam: trace_word_blocks_mp(*gens9_all[lam], word) for lam in shapes}

    # 1. PR #4766 uncabled pairwise supermodularity door c3^door (grouped word, C vs D)
    door_data = {}
    door_ratios = {}
    for iso_name, (z_cnt, n_cnt) in (("3H", (1, 2)), ("3He", (2, 1))):
        full_grp = atom_braid_word_3A(z_cnt, n_cnt, include_inter=True, intra_order="grouped", q=q0)
        ga, gb = sorted({int(x[2]) for x in full_grp if int(x[2]) % 3 == 2})
        w_empty = [x for x in full_grp if int(x[2]) % 3 != 2]
        w_a = [x for x in full_grp if int(x[2]) % 3 != 2 or int(x[2]) == ga]
        w_b = [x for x in full_grp if int(x[2]) % 3 != 2 or int(x[2]) == gb]
        w_ab = full_grp

        c_e = all_chis9(w_empty)
        c_a = all_chis9(w_a)
        c_b = all_chis9(w_b)
        c_ab = all_chis9(w_ab)

        d2_c_abs = mp.fsum(
            y9_c[lam] * (abs(c_ab[lam]) - abs(c_a[lam]) - abs(c_b[lam]) + abs(c_e[lam]))
            for lam in parts9
        )
        d2_d_abs = mp.fsum(
            y9_d[lam] * (abs(c_ab[lam]) - abs(c_a[lam]) - abs(c_b[lam]) + abs(c_e[lam]))
            for lam in two_row9
        )
        d2_d_raw = mp.fsum(
            y9_d[lam] * (c_ab[lam] - c_a[lam] - c_b[lam] + c_e[lam])
            for lam in two_row9
        )
        c3_door_c = -e0_mev * d2_c_abs
        c3_door_d = -e0_mev * d2_d_abs
        ratio_c_over_d = abs(c3_door_c) / abs(c3_door_d)
        door_ratios[iso_name] = ratio_c_over_d
        door_data[iso_name] = {
            "c3_door_C_MeV": fmt(c3_door_c, dps=OUT_DPS),
            "c3_door_D_MeV": fmt(c3_door_d, dps=OUT_DPS),
            "abs_vs_raw_diff_under_D": fmt(abs(d2_d_abs - d2_d_raw), dps=15),
            "door_C_to_D_ratio": fmt(ratio_c_over_d, dps=OUT_DPS),
            "saved_intra_chis": c_e,
        }

    # 2. #4364 width-3 cabled Borromean cluster on grouped word (C, D, W_raw, W_geom)
    inter_bor = cabled_borromean_inter_word(h_val)
    cabled_grp_per_iso = {}
    for iso_name, (z_cnt, n_cnt) in (("3H", (1, 2)), ("3He", (2, 1))):
        full_grp = atom_braid_word_3A(z_cnt, n_cnt, include_inter=True, intra_order="grouped", q=q0)
        intra_grp = [x for x in full_grp if int(x[2]) % 3 != 2]
        chis_g0 = door_data[iso_name].pop("saved_intra_chis")
        chis_gb = all_chis9(intra_grp + inter_bor)

        def eval_c3(w_map, shapes):
            g0 = mp.fsum(w_map[lam] * abs(chis_g0[lam]) for lam in shapes)
            gb = mp.fsum(w_map[lam] * abs(chis_gb[lam]) for lam in shapes)
            return e0_mev * (g0 - gb)

        cabled_grp_per_iso[iso_name] = {
            "y_C": eval_c3(y9_c, parts9),
            "y_D": eval_c3(y9_d, two_row9),
            "W_raw": eval_c3(w_raw9, parts9),
            "W_geom": eval_c3(w_geom9, parts9),
        }

    c3_cabled_c_grp = (cabled_grp_per_iso["3H"]["y_C"] + cabled_grp_per_iso["3He"]["y_C"]) / 2
    c3_cabled_d_grp = (cabled_grp_per_iso["3H"]["y_D"] + cabled_grp_per_iso["3He"]["y_D"]) / 2
    c3_cabled_raw_grp = (cabled_grp_per_iso["3H"]["W_raw"] + cabled_grp_per_iso["3He"]["W_raw"]) / 2
    c3_cabled_geom_grp = (cabled_grp_per_iso["3H"]["W_geom"] + cabled_grp_per_iso["3He"]["W_geom"]) / 2

    r_star_c_grp = mu3_target / c3_cabled_c_grp
    r_star_d_grp = mu3_target / c3_cabled_d_grp
    band_lo = r_star_c_grp * min(door_ratios["3H"], door_ratios["3He"])
    band_hi = r_star_c_grp * max(door_ratios["3H"], door_ratios["3He"])

    r_geom_c = c3_cabled_geom_grp / c3_cabled_c_grp
    r_geom_d = c3_cabled_geom_grp / c3_cabled_d_grp
    r_both_c = r_geom_c * sum_y_c
    r_both_d = r_geom_d * sum_y_d

    # 3. Canonical `borromean` intra-nucleon word under Convention D (5 two-row shapes, exact)
    cabled_bor_per_iso_d = {}
    for iso_name, (z_cnt, n_cnt) in (("3H", (1, 2)), ("3He", (2, 1))):
        full_bor = atom_braid_word_3A(z_cnt, n_cnt, include_inter=True, intra_order="borromean", q=q0)
        intra_bor = [x for x in full_bor if int(x[2]) % 3 != 2]
        chis_g0_bor = all_chis9(intra_bor, shapes=two_row9)
        chis_gb_bor = all_chis9(intra_bor + inter_bor, shapes=two_row9)
        g0_d = mp.fsum(y9_d[lam] * abs(chis_g0_bor[lam]) for lam in two_row9)
        gb_d = mp.fsum(y9_d[lam] * abs(chis_gb_bor[lam]) for lam in two_row9)
        cabled_bor_per_iso_d[iso_name] = e0_mev * (g0_d - gb_d)

    c3_cabled_d_bor = (cabled_bor_per_iso_d["3H"] + cabled_bor_per_iso_d["3He"]) / 2
    r_star_d_bor = mu3_target / c3_cabled_d_bor

    return {
        "door_band_provenance_pr4766": {
            "per_isotope": door_data,
            "r_star_C_grouped": fmt(r_star_c_grp, dps=OUT_DPS),
            "door_extrapolated_band_lo": fmt(band_lo, dps=OUT_DPS),
            "door_extrapolated_band_hi": fmt(band_hi, dps=OUT_DPS),
        },
        "cabled_cluster_grouped_80dps": {
            "c3_y_C_MeV": fmt(c3_cabled_c_grp, dps=OUT_DPS),
            "c3_y_D_MeV": fmt(c3_cabled_d_grp, dps=OUT_DPS),
            "c3_W_raw_MeV": fmt(c3_cabled_raw_grp, dps=OUT_DPS),
            "c3_W_geom_MeV": fmt(c3_cabled_geom_grp, dps=OUT_DPS),
            "r_star_C": fmt(r_star_c_grp, dps=OUT_DPS),
            "r_star_D": fmt(r_star_d_grp, dps=OUT_DPS),
            "r_geom_C": fmt(r_geom_c, dps=OUT_DPS),
            "r_geom_D": fmt(r_geom_d, dps=OUT_DPS),
            "sum_y_C": fmt(sum_y_c, dps=OUT_DPS),
            "sum_y_D": fmt(sum_y_d, dps=OUT_DPS),
            "sum_W_geom": fmt(sum_w_geom, dps=OUT_DPS),
            "r_both_C": fmt(r_both_c, dps=OUT_DPS),
            "r_both_D": fmt(r_both_d, dps=OUT_DPS),
        },
        "cabled_cluster_borromean_D_80dps": {
            "c3_y_D_3H_MeV": fmt(cabled_bor_per_iso_d["3H"], dps=OUT_DPS),
            "c3_y_D_3He_MeV": fmt(cabled_bor_per_iso_d["3He"], dps=OUT_DPS),
            "c3_y_D_mean_MeV": fmt(c3_cabled_d_bor, dps=OUT_DPS),
            "r_star_D_borromean": fmt(r_star_d_bor, dps=OUT_DPS),
        },
        "raw_mp": {
            "c3_c": c3_cabled_c_grp,
            "c3_d_grp": c3_cabled_d_grp,
            "c3_d_bor": c3_cabled_d_bor,
            "r_star_c": r_star_c_grp,
            "r_star_d_grp": r_star_d_grp,
            "r_star_d_bor": r_star_d_bor,
            "band_lo": band_lo,
            "band_hi": band_hi,
            "r_both_c": r_both_c,
            "r_both_d": r_both_d,
            "sum_w_geom_err": abs(sum_w_geom - mp.mpf(1)),
        },
    }


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        me_mev = mp.mpf(value_str("electron mass energy equivalent in MeV"))
        e0_mev = me_mev / (q0 * (q0 - 1))
        cache = BlockCacheMP(q0)

        part_a = run_part_a_zrx2(q0, cache)
        part_b = run_part_b_cds5(q0, e0_mev, cache)
        rmp = part_b["raw_mp"]

        print("=" * 84)
        print("Q-Drain-9 80-dps Diagnostic: qou-zrx2 Classical Floor & qou-cds5 Convention-D r*")
        print("=" * 84)
        print(
            f"Part A (qou-zrx2): {part_a['parity_checks']} parity checks ({part_a['parity_mismatches']} mismatches), "
            f"2H floor share borromean={fmt(part_a['deuteron_borromean_pct'], dps=8)}% vs grouped={fmt(part_a['deuteron_grouped_pct'], dps=8)}%"
        )
        print(
            f"Part B (qou-cds5): PR #4766 door band=[{fmt(rmp['band_lo'], dps=8)}, {fmt(rmp['band_hi'], dps=8)}]"
        )
        print(
            f"  Actual r*_D(grouped)={fmt(rmp['r_star_d_grp'], dps=8)} (< band_lo), "
            f"r*_D(borromean)={fmt(rmp['r_star_d_bor'], dps=8)} (> band_hi), "
            f"r_both^D={fmt(rmp['r_both_d'], dps=8)}"
        )

        wb = WitnessBuilder(
            "classical-floor-and-rstar-d-band-80dps",
            engine="mpmath",
            output_dir=Path(__file__).resolve().parent,
        )
        wb.set_description(
            "80-dps (50-dps serialized) Q-Drain-9 verification for beans qou-zrx2 and qou-cds5: "
            "(A) exact q=1 cycle-merge & interface-multiplicity parity law floor(A,O) = 2^(-A)*(1 - 2^(-O)) "
            "across A=1..12 plus 80-dps Convention-D canonical Borromean vs grouped classical floor shares "
            "(2H: 85.007% Borromean vs 22.460% grouped), and (B) pure-mpmath 80-dps Convention-D verification "
            "of the PR #4766 [2.04, 2.16] uncabled-door band provenance ([2.043411, 2.155251]) against the "
            "actual #4364 cabled-Borromean r*_D(grouped)=1.549361, r*_D(borromean)=2.458116, and r_both^D=2.871237."
        )
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("m_e_MeV", fmt(me_mev, dps=OUT_DPS))
        wb.add_parameter("E0_unit_cell_MeV", fmt(e0_mev, dps=OUT_DPS))
        wb.add_parameter("free_parameters", 0)

        wb.add_data(
            "lean_modules",
            [
                "folio/quantum-observable-universe/lean/QOU/MassTheory/ClassicalTraceFloorParity.lean",
                "folio/quantum-observable-universe/lean/QOU/MassTheory/DeltaLambdaRStarOrderBounds.lean",
            ],
        )
        wb.add_data(
            "part_a_qou_zrx2_interface_parity_and_floor_shares",
            {
                "parity_checks": part_a["parity_checks"],
                "parity_mismatches": part_a["parity_mismatches"],
                "invariance_checks": part_a["invariance_checks"],
                "invariance_mismatches": part_a["invariance_mismatches"],
                "hoefsmit_block_selftest_max_err": fmt(part_a["hoefsmit_block_selftest_max_err"], dps=15),
                "floor_shares_convention_D_80dps": part_a["floor_shares_convention_D_80dps"],
            },
        )
        wb.add_data(
            "part_b_qou_cds5_convention_d_rstar_band",
            {
                "door_band_provenance_pr4766": part_b["door_band_provenance_pr4766"],
                "cabled_cluster_grouped_80dps": part_b["cabled_cluster_grouped_80dps"],
                "cabled_cluster_borromean_D_80dps": part_b["cabled_cluster_borromean_D_80dps"],
            },
        )

        wb.add_assertion(
            "zrx2_interface_parity_and_convention_invariance_exact",
            1
            if (
                part_a["parity_mismatches"] == 0
                and part_a["invariance_mismatches"] == 0
                and part_a["parity_checks"] == 280
            )
            else 0,
            1,
            "0",
            source="ClassicalTraceFloorParity.numCycles_applyInterfaceChain_add_odd & classicalTraceFloor_eq_parity",
        )
        wb.add_assertion(
            "hoefsmit_1x1_2x2_block_evaluator_matches_dense_80dps",
            fmt(part_a["hoefsmit_block_selftest_max_err"], dps=15),
            "0",
            "1e-72",
            source="80-dps self-test of trace_word_blocks_mp against hoefsmit_mpmath.chi_lambda_of_word_mp on H_6",
        )
        wb.add_assertion(
            "zrx2_deuteron_borromean_floor_share_85pct_vs_grouped_22pct",
            1
            if (
                mp.mpf("85") < part_a["deuteron_borromean_pct"] < mp.mpf("85.02")
                and mp.mpf("22.45") < part_a["deuteron_grouped_pct"] < mp.mpf("22.47")
            )
            else 0,
            1,
            "0",
            source="80-dps Convention-D deuteron c_0=1/8 share on canonical borromean (85.007%) vs grouped (22.460%)",
        )
        wb.add_assertion(
            "cds5_pr4766_door_band_provenance_2_04_to_2_16_reproduced",
            1
            if (
                mp.mpf("2.043") < rmp["band_lo"] < mp.mpf("2.044")
                and mp.mpf("2.155") < rmp["band_hi"] < mp.mpf("2.156")
                and rmp["sum_w_geom_err"] < mp.mpf("1e-72")
            )
            else 0,
            1,
            "0",
            source="80-dps reproduction of PR #4766 uncabled door ratio * r*_C = [2.043411, 2.155251]",
        )
        wb.add_assertion(
            "cds5_cabled_rstar_D_strictly_outside_door_band_both_orderings",
            1
            if (
                rmp["c3_c"] < rmp["c3_d_grp"]
                and rmp["r_star_d_grp"] < rmp["r_star_c"] < rmp["band_lo"]
                and rmp["band_hi"] < rmp["r_star_d_bor"]
            )
            else 0,
            1,
            "0",
            source="DeltaLambdaRStarOrderBounds.rStarD_lt_doorScaled_band & doorScaled_lt_rStarD_of_cluster_drop",
        )
        wb.add_assertion(
            "cds5_rboth_D_diverges_opposite_to_rstar_D_refuting_near_miss",
            1
            if (
                rmp["r_both_c"] < rmp["r_both_d"]
                and rmp["r_star_d_grp"] < rmp["r_both_d"]
                and rmp["r_star_d_bor"] < rmp["r_both_d"]
            )
            else 0,
            1,
            "0",
            source="DeltaLambdaRStarOrderBounds.rBoth_increases_while_rStar_decreases (r_both^D = 2.871237)",
        )

        wb.add_caveat(
            "1. Bean qou-zrx2: c_0(A,O) = 2^(-A)*(1 - 2^(-O)) is an exact q=1 cycle-count property "
            "invariant under intra_order and pn_convention; zeroing it via even interface multiplicity "
            "would be selection against the target (forbidden by NO FITTING), and the E_0 scale-index "
            "pairing between the hbar_q^0 floor and hbar_q^1 deformation remains recorded without "
            "changing production constants. "
            "2. Bean qou-cds5: [2.04, 2.16] in PR #4766 is the C-frame cabled ratio r*_C=1.585412 "
            "multiplied by the uncabled pairwise door ratios (1.288883, 1.359427); direct 80-dps "
            "Convention-D evaluation of the #4364 cabled-Borromean cluster gives r*_D(grouped)=1.549361 "
            "and r*_D(borromean)=2.458116, while r_both^D=2.871237 overshoots both, confirming none "
            "of the six pruned Delta_lambda ansaetze is rescued."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"witness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
