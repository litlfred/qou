#!/usr/bin/env python3
"""Frobenius-Gram Δ_λ in the sign-solved counit defect — 80-dps canonical Borromean + qou-a71h bisect.

CONTEXT (GAP-A, Δ_λ per-isotope binding closure; bean `qou-a71h`).
1. **Canonical Borromean evaluation (`intra_order="borromean"`, ruled 2026-09-05 in `qou-hu1f`)**:
   Since `7db032fb482b` (2026-09-05) switched `atom_braid_word_3A` to the alternating
   Borromean intra-nucleon core `(σ_{3k} σ_{3k+1}^{-1})^3` and `62adab672504` refreshed
   `atom-chi-rust-{d,t,3he,4he}.witness.json` onto that word, the monotone-only transfer
   `gram_transfer_quadratic.gram_all_lambda` raised `ValueError: non-monotone word: gen 0 after 1`.
   Each nucleon subword acts purely on `{3k, 3k+1}` (an H_3 block across `s_{3k} ⊂ m_1 ⊂ m_2 ⊂ s_{3k+3}`
   of dimension `≤ 6`), interspersed with single-letter interfaces on `3k+2`. Evaluating the
   exact 80-dps block-H_3 doubled-Bratteli transfer agrees with `gram_all_lambda` on grouped
   words to `< 1.2e-78` across all `λ ⊢ 6, 9, 12` and with dense float64 einsums on Borromean
   words to `< 1.5e-14`.
   On the canonical Borromean word:
   - Unweighted Frobenius variants (`frob`, `frobRatio`, `frobDefect`, `sqrtFrob`) fail even
     to preserve the binding sign across `{D, T, 3He, 4He}` (`frob > 0` on `D, 3He`;
     `frobRatio > 0` and `sqrtFrob > 0` on `T`).
   - The unique sign-preserving Frobenius variant (`frob Σ y·‖ρa‖²·dχ`: `D = -1.5348`,
     `T = -5.3541`, `3He = -10.0255`, `4He = -36.8499`) under-binds every isotope relative
     to `-B_AME / m_e` (`-4.3533`, `-16.5985`, `-15.1038`, `-55.3732`), so zero variants
     close the 4-isotope ladder (`‖ρ_λ‖²_F` remains refuted at scope-(a)).

2. **Exact root-cause bisect of `qou-a71h` (`-842.1174706 -> -436.2405707` on `³He` grouped word)**:
   Between `796eaf09475f` (2026-07-05) and `831980f1ce68` (2026-09-04), all four `y_λ`-free
   Frobenius variants (`frob`, `frobRatio`, `frobDefect`, `sqrtFrob`) stayed constant to 7–9
   digits across all four isotopes — proving `‖ρ_λ(W)‖²_F` did NOT move. The `-48.2%` move on
   `³He` `frob Σ y·‖ρa‖²·dχ` (`-842.1174706 -> -436.2405707`) came from commit `1ab204f8edb7`
   (2026-08-11), which updated `wenzl-y-lambda-h9.witness.json` from the half-power parameter
   `z_pre = √q/(q+1)` to the canonical Markov parameter `z = q³/(q²+1)`. At `z = q³/(q²+1)`,
   the cell `(i=2, j=0)` factor `q^4(q^2 - 1 - q z) + q z` in `jones_wenzl_weight` vanishes
   identically, annihilating all 25 three-or-more-row Temperley–Lieb kernel partitions of `9`
   and projecting `Σ y_λ ‖ρ_λ‖²_F Δχ^λ` onto the 5 two-row partitions (`-842.117464 -> -436.240572`
   from closed-form `jones_wenzl_weight` alone). `qou-a71h` missed `y_λ` only because its
   counterfactual reverted `wenzl-y-lambda-h9` to `852e64fb4e^` (2026-08-29, already post-`1ab204f8edb7`).

`-- Ref:` interface-knot-markov-z.md; Ram IMRN 1997; Geck–Pfeiffer 2000;
docs/audits/2026-11-24-frobenius-gram-delta-lambda-bisect-a71h.md.
"""
from __future__ import annotations

from collections import defaultdict
import json
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(80)
from mpmath import mp, mpf, fabs, sqrt  # noqa: E402
mp.dps = max(mp.dps, 80)

from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    M_E_MEV,
)
from q_parameter import q_at  # noqa: E402
from chi_monotone_transfer import _addable, _add, word_to_mpfr, chi_all_lambda  # noqa: E402
from gram_transfer_quadratic import _subset, _axial, _middles, gram_all_lambda  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A, jones_wenzl_weight  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)
m_e = mpf(str(M_E_MEV))

B_AME = {
    "D": mpf(str(AME_B_DEUTERON_MEV_VALIDATION)),
    "T": mpf(str(AME_B_TRITIUM_MEV_VALIDATION)),
    "3He": mpf(str(AME_B_HE3_MEV_VALIDATION)),
    "4He": mpf(str(AME_B_HE4_MEV_VALIDATION)),
}
FILES = {
    "D": "atom-chi-rust-d.witness.json",
    "T": "atom-chi-rust-t.witness.json",
    "3He": "atom-chi-rust-3he.witness.json",
    "4He": "atom-chi-rust-4he.witness.json",
}
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
YFILE = {
    "D": "rho-k-h3a-lp-dual.witness.json",
    "T": "wenzl-y-lambda-h9.witness.json",
    "3He": "wenzl-y-lambda-h9.witness.json",
    "4He": "wenzl-y-lambda-h12.witness.json",
}


def load_chi(fn: str, key: str) -> dict:
    with open(os.path.join(COMP, fn), encoding="utf-8") as f:
        d = json.load(f)["data"][key]["by_partition"]
    return {tuple(e["partition"]): mpf(str(e["chi_lambda"])) for e in d}


def load_y(name: str) -> dict:
    if name == "D":
        with open(os.path.join(COMP, YFILE["D"]), encoding="utf-8") as f:
            lp = json.load(f)
        return {tuple(e["partition"]): mpf(str(e["y_lambda_at_q0"])) for e in lp["data"]["per_lambda"]}
    with open(os.path.join(COMP, YFILE[name]), encoding="utf-8") as f:
        d = json.load(f)
    return {tuple(e["partition"]): mpf(str(e["y_lambda"])) for e in d["data"]["per_partition"]}


def gram_all_lambda_block_h3(word: list, n: int, *, dps: int = 80, q=None) -> dict:
    """Exact 80-dps doubled-Bratteli Frobenius norm `{λ ⊢ n: ‖ρ_λ(W)‖²_F}` for any
    nucleonic 3A-strand word factored into H_3 blocks on `{3k, 3k+1}` interspersed
    with single-letter inter-nucleon interfaces on `3k+2` (handles both canonical
    alternating `borromean` and superseded `grouped` words with zero d_λ materialisation).
    """
    if mp.dps < dps:
        mp.dps = dps
    qm = q_at(dps) if q is None else mpf(str(q))
    qi = mpf(1) / qm
    hq = qm - qi
    gens = word_to_mpfr(word, qm)

    dc: dict[int, mpf] = {1: qm, -1: -qi}

    def diag_entry(delta: int) -> mpf:
        v = dc.get(delta)
        if v is None:
            v = hq / (mpf(1) - qm ** (-2 * delta))
            dc[delta] = v
        return v

    bc: dict[int, mpf] = {}

    def off_entry(delta: int) -> mpf:
        v = bc.get(delta)
        if v is None:
            v = sqrt(diag_entry(delta) * diag_entry(-delta) + mpf(1))
            bc[delta] = v
            bc[-delta] = v
        return v

    def step_entry(lo: tuple, hi: tuple, m_l: tuple, m_r: tuple, c_mp: mpf, d_mp: mpf) -> mpf:
        delta = _axial(lo, m_l, hi)
        if m_l == m_r:
            return c_mp * diag_entry(delta) + d_mp
        return c_mp * off_entry(delta)

    if n % 3 != 0:
        raise ValueError(f"Expected n = 3A, got n={n}")
    a_mass = n // 3
    nuc_letters: list[list[tuple[mpf, mpf, int]]] = [[] for _ in range(a_mass)]
    inter_letters: list[list[tuple[mpf, mpf]]] = [[] for _ in range(max(a_mass - 1, 0))]
    stage = 0
    for d_mp, g in gens:
        while True:
            k = stage // 2
            if stage % 2 == 0 and g in (3 * k, 3 * k + 1):
                nuc_letters[k].append((mpf(1), d_mp, g - 3 * k))
                break
            if stage % 2 == 1 and g == 3 * k + 2:
                inter_letters[k].append((mpf(1), d_mp))
                break
            stage += 1
            if stage >= 2 * a_mass:
                raise ValueError(f"Word not nucleon-block-local: generator {g} out of sequence")

    def nuc_block_matrix(b0: tuple, a3: tuple, letters: list[tuple[mpf, mpf, int]]):
        chains: list[tuple[tuple, tuple]] = []
        for box1 in _addable(b0):
            m1 = _add(b0, box1)
            if not _subset(m1, a3):
                continue
            for box2 in _addable(m1):
                m2 = _add(m1, box2)
                if _subset(m2, a3):
                    chains.append((m1, m2))
        dim = len(chains)
        if dim == 0:
            return chains, {}, []
        idx = {ch: i for i, ch in enumerate(chains)}
        s0 = [[mpf(0)] * dim for _ in range(dim)]
        s1 = [[mpf(0)] * dim for _ in range(dim)]
        for r, (m1_l, m2_l) in enumerate(chains):
            for m1_r in _middles(b0, m2_l):
                c = idx.get((m1_r, m2_l))
                if c is not None:
                    s0[r][c] = step_entry(b0, m2_l, m1_l, m1_r, mpf(1), mpf(0))
            for m2_r in _middles(m1_l, a3):
                c = idx.get((m1_l, m2_r))
                if c is not None:
                    s1[r][c] = step_entry(m1_l, a3, m2_l, m2_r, mpf(1), mpf(0))
        mat = [[mpf(1) if r == c else mpf(0) for c in range(dim)] for r in range(dim)]
        for c_mp, d_mp, off in letters:
            s_cur = s0 if off == 0 else s1
            nxt_m = [[mpf(0)] * dim for _ in range(dim)]
            for r in range(dim):
                for k_col in range(dim):
                    mrk = mat[r][k_col]
                    if mrk == 0:
                        continue
                    for col in range(dim):
                        lval = c_mp * s_cur[k_col][col] + (d_mp if k_col == col else mpf(0))
                        if lval != 0:
                            nxt_m[r][col] += mrk * lval
            mat = nxt_m
        return chains, idx, mat

    amp: dict[tuple[tuple, tuple], mpf] = {((1,), ()): mpf(1)}
    for k in range(a_mass):
        after_nuc: dict[tuple[tuple, tuple], mpf] = defaultdict(mpf)
        bcache: dict[tuple[tuple, tuple], tuple] = {}
        for (a1, b0), w_amp in amp.items():
            if not _subset(b0, a1):
                continue
            for box2 in _addable(a1):
                a2 = _add(a1, box2)
                for box3 in _addable(a2):
                    a3 = _add(a2, box3)
                    bkey = (b0, a3)
                    if bkey not in bcache:
                        bcache[bkey] = nuc_block_matrix(b0, a3, nuc_letters[k])
                    chains, idx, mat = bcache[bkey]
                    a_idx = idx.get((a1, a2))
                    if a_idx is None:
                        continue
                    row_m = mat[a_idx]
                    for b_idx, (_b1, b2) in enumerate(chains):
                        mel = row_m[b_idx]
                        if mel != 0:
                            after_nuc[(a3, b2)] += w_amp * (mel * mel)
        if k < a_mass - 1:
            cur = dict(after_nuc)
            if not inter_letters[k]:
                nxt: dict[tuple[tuple, tuple], mpf] = defaultdict(mpf)
                for (a3, b2), w_amp in cur.items():
                    if not _subset(b2, a3):
                        continue
                    for box4 in _addable(a3):
                        a4 = _add(a3, box4)
                        nxt[(a4, a3)] += w_amp
                amp = dict(nxt)
            else:
                if len(inter_letters[k]) != 1:
                    raise ValueError(f"Expected single interface letter at k={k}")
                c_mp, d_mp = inter_letters[k][0]
                nxt = defaultdict(mpf)
                for (a3, b2), w_amp in cur.items():
                    if not _subset(b2, a3):
                        continue
                    for box4 in _addable(a3):
                        a4 = _add(a3, box4)
                        for b3 in _middles(b2, a4):
                            f = step_entry(b2, a4, a3, b3, c_mp, d_mp)
                            if f != 0:
                                nxt[(a4, b3)] += w_amp * (f * f)
                amp = dict(nxt)
        else:
            out: dict[tuple, mpf] = defaultdict(mpf)
            for (a_n, _b_prev), w_amp in after_nuc.items():
                out[a_n] += w_amp
            return dict(out)
    return {}


def _eval_variants(dchi: dict, y: dict, norms_a: dict, norms_f: dict, tgt: mpf) -> dict:
    ka = [l for l in dchi if l in norms_a]
    kf = [l for l in dchi if l in norms_a and l in norms_f and norms_f[l] != 0]
    variants = {
        "ref_trM  Σ y·dχ": mp.fsum(y.get(l, mpf(0)) * dchi[l] for l in dchi),
        "frob  Σ ‖ρa‖²·dχ": mp.fsum(norms_a[l] * dchi[l] for l in ka),
        "frob  Σ y·‖ρa‖²·dχ": mp.fsum(y.get(l, mpf(0)) * norms_a[l] * dchi[l] for l in ka),
        "frobRatio  Σ (‖ρa‖²/‖ρf‖²)·dχ": mp.fsum((norms_a[l] / norms_f[l]) * dchi[l] for l in kf),
        "frobDefect Σ (‖ρa‖²−‖ρf‖²)·dχ": mp.fsum((norms_a[l] - norms_f[l]) * dchi[l] for l in kf),
        "sqrtFrob  Σ ‖ρa‖·dχ": mp.fsum(sqrt(norms_a[l]) * dchi[l] for l in ka),
    }
    out = {}
    for lbl, s_val in variants.items():
        miss = fabs(s_val - tgt)
        out[lbl] = {
            "S": mp.nstr(s_val, 16),
            "abs_miss": mp.nstr(miss, 10),
            "within_tol": bool(miss < mpf(1)),
            "sign_negative": bool(s_val < mpf(0)),
        }
    return out


def run_isotope(name: str, q80: mpf) -> tuple[dict, dict, mpf]:
    z_cnt, n_cnt = ZN[name]
    n_strands = 3 * (z_cnt + n_cnt)
    atom = load_chi(FILES[name], "atom")
    free = load_chi(FILES[name], "free")
    dchi = {l: atom[l] - free[l] for l in atom}
    y = load_y(name)
    tgt = -B_AME[name] / m_e

    wa_bor = atom_braid_word_3A(z_cnt, n_cnt, include_inter=True, intra_order="borromean", q=q80)
    wf_bor = atom_braid_word_3A(z_cnt, n_cnt, include_inter=False, intra_order="borromean", q=q80)
    norms_a = gram_all_lambda_block_h3(wa_bor, n_strands, dps=80, q=q80)
    norms_f = gram_all_lambda_block_h3(wf_bor, n_strands, dps=80, q=q80)
    bor_out = {
        "target_minus_B_over_me": mp.nstr(tgt, 16),
        "n": n_strands,
        "variants": _eval_variants(dchi, y, norms_a, norms_f, tgt),
    }

    # Superseded grouped-word control + exact parity check against monotone gram_all_lambda
    wa_grp = atom_braid_word_3A(z_cnt, n_cnt, include_inter=True, intra_order="grouped", q=q80)
    wf_grp = atom_braid_word_3A(z_cnt, n_cnt, include_inter=False, intra_order="grouped", q=q80)
    ng_a_block = gram_all_lambda_block_h3(wa_grp, n_strands, dps=80, q=q80)
    ng_a_mono = gram_all_lambda(wa_grp, n_strands, dps=80, q=q80)
    ng_f_mono = gram_all_lambda(wf_grp, n_strands, dps=80, q=q80)
    max_parity_err = max(
        fabs(ng_a_block[k] - ng_a_mono[k]) / (mpf(1) + fabs(ng_a_mono[k]))
        for k in ng_a_mono
    )
    chi_g_a = chi_all_lambda(wa_grp, n_strands, dps=80, q=q80)
    chi_g_f = chi_all_lambda(wf_grp, n_strands, dps=80, q=q80)
    dchi_grp = {l: chi_g_a[l] - chi_g_f[l] for l in chi_g_a}
    grp_out = {
        "n": n_strands,
        "block_vs_monotone_max_rel_err": mp.nstr(max_parity_err, 6),
        "variants": _eval_variants(dchi_grp, y, ng_a_mono, ng_f_mono, tgt),
    }
    return bor_out, grp_out, max_parity_err


def run_a71h_bisect(q80: mpf) -> dict:
    """First-principles 80-dps proof of the `qou-a71h` `-842.1174706 -> -436.2405707` move on ³He."""
    wa_grp = atom_braid_word_3A(2, 1, include_inter=True, intra_order="grouped", q=q80)
    wf_grp = atom_braid_word_3A(2, 1, include_inter=False, intra_order="grouped", q=q80)
    chi_a = chi_all_lambda(wa_grp, 9, dps=80, q=q80)
    chi_f = chi_all_lambda(wf_grp, 9, dps=80, q=q80)
    dchi_grp = {l: chi_a[l] - chi_f[l] for l in chi_a}
    na_grp = gram_all_lambda(wa_grp, 9, dps=80, q=q80)

    z_pre = sqrt(q80) / (q80 + mpf(1))
    z_post = (q80 ** 3) / ((q80 ** 2) + mpf(1))

    y_pre = {l: jones_wenzl_weight(l, q=q80, z=z_pre) for l in dchi_grp}
    y_post = {l: jones_wenzl_weight(l, q=q80, z=z_post) for l in dchi_grp}

    s_pre = mp.fsum(y_pre[l] * na_grp[l] * dchi_grp[l] for l in dchi_grp)
    s_post = mp.fsum(y_post[l] * na_grp[l] * dchi_grp[l] for l in dchi_grp)
    tl_kernel_max_y_post = max(fabs(y_post[l]) for l in y_post if len(l) >= 3)
    nonzero_pre = sum(1 for v in y_pre.values() if fabs(v) > mpf("1e-70"))
    nonzero_post = sum(1 for v in y_post.values() if fabs(v) > mpf("1e-70"))

    return {
        "cause_commit": "1ab204f8edb7 (2026-08-11: wenzl-y-lambda-h9/h12 z_pre=sqrt(q)/(q+1) -> z=q^3/(q^2+1))",
        "why_qou_a71h_missed_it": (
            "qou-a71h reverted wenzl-y-lambda-h9 only to 852e64fb4e^ (2026-08-29, already on "
            "z=q^3/(q^2+1)), never to 1ab204f8edb7^ (2026-08-10), while all four y_lambda-free "
            "Frobenius variants stayed constant to 7-9 digits."
        ),
        "S_3He_grouped_z_pre_closed_form": mp.nstr(s_pre, 16),
        "S_3He_grouped_z_post_closed_form": mp.nstr(s_post, 16),
        "S_3He_witness_2026_07_05": "-842.1174706",
        "S_3He_witness_2026_09_04": "-436.2405707",
        "rel_match_z_pre_vs_2026_07_05": mp.nstr(fabs(s_pre - mpf("-842.1174706")) / fabs(s_pre), 6),
        "rel_match_z_post_vs_2026_09_04": mp.nstr(fabs(s_post - mpf("-436.2405707")) / fabs(s_post), 6),
        "nonzero_y_partitions_n9_z_pre": nonzero_pre,
        "nonzero_y_partitions_n9_z_post": nonzero_post,
        "tl_kernel_3row_max_abs_y_at_z_post": mp.nstr(tl_kernel_max_y_post, 6),
    }


def main() -> int:
    q80 = q_at(80)
    per_iso = {}
    grp_ctrl = {}
    worst_parity = mpf(0)
    for name in FILES:
        bor_out, grp_out, perr = run_isotope(name, q80)
        per_iso[name] = bor_out
        grp_ctrl[name] = grp_out
        if perr > worst_parity:
            worst_parity = perr

    bisect = run_a71h_bisect(q80)

    # Assertions on canonical Borromean 80-dps results + exact parity + qou-a71h bisect
    frob_labels = [
        "frob  Σ ‖ρa‖²·dχ",
        "frob  Σ y·‖ρa‖²·dχ",
        "frobRatio  Σ (‖ρa‖²/‖ρf‖²)·dχ",
        "frobDefect Σ (‖ρa‖²−‖ρf‖²)·dχ",
        "sqrtFrob  Σ ‖ρa‖·dχ",
    ]
    y_frob_all_neg = all(
        per_iso[iso]["variants"]["frob  Σ y·‖ρa‖²·dχ"]["sign_negative"]
        for iso in FILES
    )
    unweighted_sign_broken = all(
        not all(per_iso[iso]["variants"][lbl]["sign_negative"] for iso in FILES)
        for lbl in frob_labels
        if lbl != "frob  Σ y·‖ρa‖²·dχ"
    )
    any_closes_all_4 = any(
        all(per_iso[iso]["variants"][lbl]["within_tol"] for iso in FILES)
        for lbl in frob_labels
    )
    parity_ok = bool(worst_parity < mpf("1e-75"))
    bisect_ok = bool(
        mpf(bisect["rel_match_z_pre_vs_2026_07_05"]) < mpf("1e-7")
        and mpf(bisect["rel_match_z_post_vs_2026_09_04"]) < mpf("1e-7")
        and bisect["nonzero_y_partitions_n9_z_pre"] == 30
        and bisect["nonzero_y_partitions_n9_z_post"] == 5
        and mpf(bisect["tl_kernel_3row_max_abs_y_at_z_post"]) < mpf("1e-75")
    )

    payload = {
        "computation": "frobenius-gram-delta-lambda",
        "description": (
            "Frobenius Gram norm ‖ρ_λ‖²_F (80-dps block-H_3 doubled-Bratteli transfer) "
            "as a parameter-free Δ_λ weight in the sign-solved counit defect on D/T/³He/⁴He "
            "under canonical Borromean intra-ordering (plus grouped provenance control and "
            "exact qou-a71h bisect). REFUTED as the closing weight (scope-(a)): unweighted "
            "Frobenius variants break binding sign on Borromean, and Σ y·‖ρa‖²·dχ under-binds "
            "every isotope. audit-only, no fit."
        ),
        "tier": "structural-exact (committed Borromean χ^λ atom/free + exact 80-dps Frobenius Gram norms)",
        "result": {
            "free_parameters": 0,
            "intra_order": "borromean",
            "per_isotope": per_iso,
            "grouped_ordering_control": grp_ctrl,
            "a71h_bisect_attribution": bisect,
            "verdict": (
                "‖ρ_λ‖²_F REFUTED as the GAP-A closing weight (scope-(a)) on canonical Borromean: "
                "all four y_λ-free Frobenius variants break binding sign across {D,T,³He,⁴He}, "
                "while Σ y·‖ρa‖²·dχ preserves sign (-1.535, -5.354, -10.025, -36.850) but "
                "under-binds every isotope relative to -B_AME/m_e (-4.353, -16.598, -15.104, -55.373). "
                "Historical -842.117 -> -436.241 move on ³He grouped word (qou-a71h) is 100% "
                "explained by 1ab204f8edb7 (y_λ z=sqrt(q)/(q+1) -> q^3/(q^2+1) annihilating the "
                "25 ≥3-row TL-kernel partitions of 9)."
            ),
        },
        "context": {
            "axis": "Δ_λ per-isotope binding closure (GAP-A) — Frobenius Gram weight",
            "sign_solved_by": "rho_k_counit_defect_form.py (defect ε(β_K)−ε(β_K^vac) < 0 all isotopes)",
            "weight_source": "gram_all_lambda_block_h3 (exact 80-dps block-H_3 doubled-Bratteli tr_M(W·W^♯))",
            "chi_source": "atom-chi-rust-{d,t,3he,4he}.witness.json (canonical Borromean data.atom + data.free)",
            "audit_doc": "docs/audits/2026-11-24-frobenius-gram-delta-lambda-bisect-a71h.md",
        },
    }

    wb = WitnessBuilder.wrap_legacy(
        "frobenius-gram-delta-lambda",
        payload,
        script_path=__file__,
        engine="python+mpmath",
        output_dir=COMP,
    )
    for fn in sorted(set(FILES.values()) | set(YFILE.values())):
        wb.add_upstream(_COMP / fn)

    wb.add_assertion(
        "y_weighted_frobenius_preserves_binding_sign",
        computed=str(bool(y_frob_all_neg)),
        expected="True",
    )
    wb.add_assertion(
        "unweighted_frobenius_variants_violate_sign_on_borromean",
        computed=str(bool(unweighted_sign_broken)),
        expected="True",
    )
    wb.add_assertion(
        "no_frobenius_variant_closes_magnitude",
        computed=str(bool(not any_closes_all_4)),
        expected="True",
    )
    wb.add_assertion(
        "block_h3_matches_monotone_transfer_on_grouped_word",
        computed=str(bool(parity_ok)),
        expected="True",
    )
    wb.add_assertion(
        "a71h_3he_move_reproduced_by_1ab204f8edb7_y_lambda",
        computed=str(bool(bisect_ok)),
        expected="True",
    )
    out = wb.save(
        extra={
            "auditOnly": True,
            "q0Anchor": "proton",
            "q0Value": mp.nstr(q80, 80),
        }
    )

    print("=== Frobenius-Gram Δ_λ at 80 dps (canonical Borromean + qou-a71h bisect) ===")
    for name, iso in per_iso.items():
        print(f"\n{name}  (n={iso['n']})  target -B/m_e = {iso['target_minus_B_over_me']}")
        for lbl, v in iso["variants"].items():
            flag = "  <<< WITHIN_TOL_SINGLE_ISO" if v["within_tol"] else ""
            print(f"  {lbl:34} S={v['S']:>20}  |miss|={v['abs_miss']:>14}{flag}")
    print(f"\nBlock-H_3 vs monotone parity max rel err: {mp.nstr(worst_parity, 6)}")
    print(
        f"qou-a71h ³He grouped bisect: z_pre={bisect['S_3He_grouped_z_pre_closed_form']} "
        f"(2026-07-05: {bisect['S_3He_witness_2026_07_05']}) -> "
        f"z_post={bisect['S_3He_grouped_z_post_closed_form']} "
        f"(2026-09-04: {bisect['S_3He_witness_2026_09_04']})"
    )
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
