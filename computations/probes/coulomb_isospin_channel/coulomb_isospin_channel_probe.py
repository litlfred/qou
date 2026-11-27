#!/usr/bin/env python3
"""Probe: the EM channel of binding, ranks 0/1/2 on the nucleus block (gap G3, bean qou-tcl3).

Pre-registered content (fixed before any comparison was looked at):
  * charge structure a = A(A−2)/8, b = (A−1)/2, c = 1/2 (Lean `chargePairs_imme`);
  * pair weight ε = 2 f αħc / r_rms with f = q-Hankel 0.520011 (PR #9665) — no alternate f
    is selected; the uniform ball is printed for comparison only;
  * r_rms is OPEN. The only available length, CAL-3 λ̄_π A^{1/3} (coefficient selected,
    A^{1/3} assumed), is used to print numbers and every such number is CONDITIONAL.

Checks (exact, Fraction):
  1. Z(Z−1)/2 = a + b T_z + c T_z² for every 0 ≤ Z ≤ A ≤ 300.
  2. Quark level: Σ_{i<j} q_i q_j over 3A strands (charges 2/3, −1/3)
     = Z(Z−1)/2 + Σ_nucleons internal, internal p = 0, n = −1/3.
  3. Rank split: rank1 and rank2 average to 0 over each multiplet T ≤ 10.
  4. With f = uniform ball and the CAL-3 length, E_EM reproduces `coulomb_energy_mev`
     (the existing module is the f = (3/5)^{3/2} special case of this one).

Comparison boundary (AME2020 enters only here, never as an input):
  mirror pairs: model split ε (A−1)/2 vs ΔB_AME; also the length r_rms that AME would
  require, printed as a diagnostic about the open length, not used anywhere.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import coulomb_isospin_channel as em  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402

MIRROR_PAIRS = [  # (lo, Z_lo, hi, Z_hi, A): lo = more bound (T_z = −1/2)
    ("3H", 1, "3He", 2, 3), ("7Li", 3, "7Be", 4, 7), ("11B", 5, "11C", 6, 11),
    ("13C", 6, "13N", 7, 13), ("15N", 7, "15O", 8, 15), ("17O", 8, "17F", 9, 17),
    ("39K", 19, "39Ca", 20, 39), ("41Ca", 20, "41Sc", 21, 41),
]


def check_imme(max_a: int = 300) -> int:
    bad = 0
    for A in range(1, max_a + 1):
        a, b, c = em.em_coefficients(A)
        for Z in range(0, A + 1):
            Tz = em.t_z(Z, A)
            if em.charge_pairs(Z) != a + b * Tz + c * Tz * Tz:
                bad += 1
    return bad


def quark_pairs(Z: int, N: int) -> Fraction:
    qs = [Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)] * Z + \
         [Fraction(2, 3), Fraction(-1, 3), Fraction(-1, 3)] * N
    s = sum(qs)
    return (s * s - sum(x * x for x in qs)) / 2


def check_quark(max_a: int = 40) -> int:
    bad = 0
    for A in range(1, max_a + 1):
        for Z in range(0, A + 1):
            N = A - Z
            if quark_pairs(Z, N) != em.charge_pairs(Z) + Fraction(-1, 3) * N:
                bad += 1
    return bad


def check_rank_average(max_twoT: int = 20) -> int:
    bad = 0
    for d in range(0, max_twoT + 1):
        T = Fraction(d, 2)
        for A in (d, d + 2, d + 10):
            if A < 1:
                continue
            r1 = sum(em.em_rank_split(A, T, Fraction(k) - T)["rank1"] for k in range(d + 1))
            r2 = sum(em.em_rank_split(A, T, Fraction(k) - T)["rank2"] for k in range(d + 1))
            if r1 != 0 or r2 != 0:
                bad += 1
    return bad


def check_ball_reduces(max_a: int = 60) -> "mp.mpf":
    worst = mp.mpf(0)
    for A in range(2, max_a + 1):
        for Z in range(2, A + 1):
            mine = em.em_energy_mev(Z, A, em.r_rms_cal3_conditional(A), f=em.F_UNIFORM_BALL)
            old = coulomb_energy_mev(Z, A)
            worst = max(worst, abs(mine - old) / old)
    return worst


def mirror_rows():
    import mass_binding_dashboard as mbd
    ame = mbd._ame_table()
    ahc = em.alpha_hbar_c()
    rows = []
    for lo, zlo, hi, zhi, A in MIRROR_PAIRS:
        r = em.r_rms_cal3_conditional(A)
        eps = em.pair_weight_mev(r)
        eps_ball = em.pair_weight_mev(r, f=em.F_UNIFORM_BALL)
        model = eps * (A - 1) / 2
        model_ball = eps_ball * (A - 1) / 2
        # identity check: E(hi) − E(lo) = ε (A−1)/2
        diff = em.em_energy_mev(zhi, A, r) - em.em_energy_mev(zlo, A, r)
        assert abs(diff - model) < mp.mpf(10) ** (-(mp.mp.dps - 10))
        t_lo, t_hi = ame.get((zlo, A)), ame.get((zhi, A))
        dB = (t_lo[0] - t_hi[0]) if (t_lo and t_hi) else None
        row = {
            "pair": f"{lo}/{hi}", "A": A,
            "eps_times_r_MeV_fm": mp.nstr(2 * em.F_QHANKEL * ahc, 15),
            "r_rms_cal3_conditional_fm": mp.nstr(r, 15),
            "split_model_qhankel_MeV": mp.nstr(model, 15),
            "split_model_ball_MeV": mp.nstr(model_ball, 15),
        }
        if dB is not None:
            # comparison only: what length would AME need at this f (diagnostic of the open scale)
            r_req = 2 * em.F_QHANKEL * ahc * (A - 1) / 2 / dB
            row.update({
                "split_AME_MeV": mp.nstr(dB, 15),
                "rel_err_qhankel": mp.nstr(model / dB - 1, 10),
                "rel_err_ball": mp.nstr(model_ball / dB - 1, 10),
                "r_rms_AME_would_need_fm (comparison only)": mp.nstr(r_req, 10),
                "r_cal3_over_r_needed": mp.nstr(r / r_req, 10),
            })
        rows.append(row)
    return rows


def main() -> int:
    n_imme = check_imme()
    n_quark = check_quark()
    n_rank = check_rank_average()
    worst_ball = check_ball_reduces()
    rows = mirror_rows()

    print("EM channel, charge structure (exact):")
    for A in (3, 4, 7, 12, 40, 208):
        a, b, c = em.em_coefficients(A)
        print(f"  A={A:4d}  a={a}  b={b}  c={c}   b/c={b / c}  a/c={a / c}")
    print(f"IMME identity failures (A ≤ 300): {n_imme}")
    print(f"quark-level split failures (A ≤ 40): {n_quark}")
    print(f"rank-1/2 multiplet-average failures (2T ≤ 20): {n_rank}")
    print(f"uniform-ball special case vs coulomb_energy_mev, worst rel diff: {mp.nstr(worst_ball, 5)}")
    print(f"f(q-Hankel)/f(ball) = {mp.nstr(em.F_QHANKEL / em.F_UNIFORM_BALL, 12)}")
    print("\nMirror splits, CONDITIONAL on the CAL-3 length (AME = comparison only):")
    print("| pair | A | r_rms (fm, cond.) | ε(A−1)/2 q-Hankel | ball | ΔB_AME | err qH | err ball | r needed |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['pair']} | {r['A']} | {r['r_rms_cal3_conditional_fm'][:7]} | "
              f"{r['split_model_qhankel_MeV'][:7]} | {r['split_model_ball_MeV'][:7]} | "
              f"{r.get('split_AME_MeV', 'n/a')[:7]} | {r.get('rel_err_qhankel', 'n/a')[:7]} | "
              f"{r.get('rel_err_ball', 'n/a')[:7]} | "
              f"{r.get('r_rms_AME_would_need_fm (comparison only)', 'n/a')[:6]} |")

    w = WitnessBuilder("coulomb-isospin-channel-probe", engine="mpmath")
    w.set_description(
        "Gap G3 (bean qou-tcl3): the EM channel of binding on the nucleus block. Exact charge "
        "structure Z(Z-1)/2 = a + b T_z + c T_z^2 with a = A(A-2)/8, b = (A-1)/2, c = 1/2 "
        "(Lean CoulombIsospinChannel.chargePairs_imme), one EM pair weight eps = 2 f alpha hbar_c "
        "/ r_rms with f = q-Hankel 0.520011 (PR #9665). r_rms is OPEN; numbers use the CAL-3 "
        "length (coefficient selected, A^{1/3} assumed) and are CONDITIONAL. AME mirror splits "
        "are comparison only. Scope (a)."
    )
    w.add_data("f_qhankel", mp.nstr(em.F_QHANKEL, 40))
    w.add_data("f_qhankel_provenance", em.F_QHANKEL_PROVENANCE)
    w.add_data("f_uniform_ball", mp.nstr(em.F_UNIFORM_BALL, 40))
    w.add_data("alpha_hbar_c_MeV_fm", mp.nstr(em.alpha_hbar_c(), 30))
    w.add_data("mirror_rows", rows)
    w.add_assertion("imme_identity_exact_A_le_300", computed=n_imme, expected=0, tolerance=0,
                    source="Z(Z-1)/2 = A(A-2)/8 + (A-1)/2 T_z + T_z^2/2, exact Fractions")
    w.add_assertion("quark_level_split_exact_A_le_40", computed=n_quark, expected=0, tolerance=0,
                    source="3A-strand quark pair sum = Z(Z-1)/2 - N/3 (p internal 0, n internal -1/3)")
    w.add_assertion("rank12_multiplet_average_zero", computed=n_rank, expected=0, tolerance=0,
                    source="Lean rank_one_multiplet_sum / rank_two_multiplet_sum, 2T <= 20")
    w.add_assertion("uniform_ball_special_case_matches_coulomb_energy",
                    computed=mp.nstr(worst_ball, 5), expected="0", tolerance="1e-40",
                    source="em_energy_mev(f=(3/5)^{3/2}, r_rms=sqrt(3/5) R) == coulomb_energy_mev")
    out = w.save()
    print(f"\nwitness → {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
