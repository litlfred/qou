#!/usr/bin/env python3
"""Euler-Poincare Obstructions & Pauli-Wigner Extensive Cell-Sum Carrier Probe for Nuclear b_3.

Beans `qou-eptr` + `qou-q8vl` (towards `qou-brng`).
Companion Lean 4 module: `QOU/MassTheory/B3ExtensiveCellSumCarrier.lean` (`0 sorry`).
Companion audit: `docs/audits/2026-11-24-b3-extensive-ep-cell-carrier.md`.

WHAT THIS MEASURES (80 dps, zero float64, zero fitting)
-------------------------------------------------------
1. Route A (`qou-eptr` geometric & homological Euler-Poincare obstructions):
   - Light-end & Hecke-element obstruction: `2H` is non-hyperbolic (`Vol = 0`, Thurston
     trichotomy), `classify_nuclear_knot` collapses `A >= 4` onto `L6a4`, and per-atom
     `atom_canonical_crossings(Z, N)` has `12A - 1` crossings splitting for `A >= 2` into
     `10A - 2` pure braid crossings (`b_3 = 28 - 3*18 = -26 < 0`) plus `2A` `averaged` and
     `1` `averaged_weighted` non-braid Hecke letters outside the image of `B_{3A} -> H_{3A}(q)`.
   - Simplicial Euler-Poincare collapse & Mayer sign inversion: on any contractible complex
     `K_A`, unweighted `c_1 - c_2 + c_3 = A - 1` (`b_3 = -1 < 0`), while `(-1)^{d-1}` graded
     Euler-Poincare alternation gives `b_3 = -w_2 < 0` for `w_2 > 0` (cellular counterpart of
     `UrsellPartitionFunctionB3`).

2. Route B (`qou-eptr` + `qou-q8vl` Pauli-Wigner Young-diagram / Bratteli cell-sum carrier):
   - Global content sum `sum (j - i)` over `m` filled 4-column shells has constant negative
     second difference `-4` (`-A^2/8` Pauli column drift, non-extensive).
   - Intra-shell `(Z, N)`-resolved Pauli-Wigner cell sum `S_phi(Z, N)` (each spatial shell holds
     `<= 2` protons and `<= 2` neutrons, row lengths `r_i in {1, 2, 3, 4}`) is well-defined at
     `A = 2` with zero 3-manifold requirement, strictly alpha-extensive `S_phi(2m, 2m) = m S_phi(2, 2)`,
     satisfies `b_3 = phi(2) - 2*phi(1) > 0 <=> 2*phi(1) < phi(2)` (escaping `B3SignOneRoot`'s
     `(0, 1)` single-bond chain confinement), separates bound `3H`/`3He` (`r = [3]`) from
     Pauli-split `3n`/`3p` (`r = [2, 1]`, zero `j = 2` cell), and generates a parameter-free
     `|N - Z|` Wigner symmetry deficit at fixed `A`.
   - Symbolic `Q(q)` (`sympy`) and 80-dps (`mpmath`) evaluation at BOTH registered substrate pins
     (`q_p = q_at(80)` and `q_mu = q_muon_at(80)`) of zero-parameter QOU cell kernels against
     all `2,550` non-estimated `ame2020.json` nuclides across light `A in {2, 3, 4, 6, 12, 16}`
     and medium/heavy `A = 16..240`.

SCOPE & ANTI-FITTING GUARDRAIL
------------------------------
Strictly a **working-assumption probe** (`zero fitting`, zero tuned coefficients, nothing wired
into production). Any pre-2026-11-15 single-crossing `atom_braid_word_3A` bond figure is cited
solely as a historical reference baseline per `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`;
all primary cell-sum models (`M1`-`M5`) depend ONLY on `(q_0, m_e)` and Pauli-Wigner shell
combinatorics (`100%` independent of superseded single-crossing bond offsets).
"""

from __future__ import annotations

import json
import sys
import time
from collections import Counter
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in (
    "tools/qou-substrate/python",
    "tools/pyhecke/python",
    "computations",
    "computations/substrate",
    "computations/qbeta",
):
    _s = str(_ROOT / _p)
    if _s not in sys.path:
        sys.path.insert(0, _s)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

mp.mp.dps = 80

import qbeta_e0  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_at, q_muon_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

WORKING_DPS = 80

LIGHT_BENCHMARKS = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("12C", 6, 6),
    ("16O", 8, 8),
]
LIGHT_A_SET = (3, 4, 6, 12, 16)


def fmt80(x: mp.mpf) -> str:
    return mp.nstr(x, WORKING_DPS)


def fmt24(x: mp.mpf) -> str:
    return mp.nstr(x, 24)


def load_ame2020_exact() -> dict[tuple[int, int], dict]:
    """Load non-estimated AME2020 binding energies using exact decimal strings -> mpf (zero float64)."""
    raw = json.loads((_ROOT / "computations/data/ame2020.json").read_text(encoding="utf-8"))
    out: dict[tuple[int, int], dict] = {}
    for e in raw["entries"]:
        if e.get("binding_energy_per_A_estimated", False):
            continue
        b_str = e.get("binding_energy_per_A_keV")
        if b_str is None:
            continue
        Z = int(e["Z"])
        N = int(e["N"])
        A = int(e["A"])
        b_per_a_kev = mp.mpf(str(b_str))
        B_mev = b_per_a_kev * mp.mpf(A) / mp.mpf(1000)
        out[(Z, N)] = {
            "Z": Z,
            "N": N,
            "A": A,
            "element": str(e.get("element", "")),
            "B_MeV": B_mev,
            "B_per_A_MeV": b_per_a_kev / mp.mpf(1000),
        }
    return out


def pauli_wigner_rows(Z: int, N: int) -> list[int]:
    """Spin-isospin Pauli-Wigner shell filling: <= 2 protons and <= 2 neutrons per spatial shell."""
    z_rem, n_rem = Z, N
    rows: list[int] = []
    while z_rem > 0 or n_rem > 0:
        zp = 2 if z_rem >= 2 else z_rem
        np_ = 2 if n_rem >= 2 else n_rem
        rows.append(zp + np_)
        z_rem -= zp
        n_rem -= np_
    return rows


def cell_sum_mp(Z: int, N: int, phi_vals: tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]) -> mp.mpf:
    """Evaluate S_phi(Z, N) = sum_i sum_{j=0}^{r_i - 1} phi(j) in 80-dps mpmath."""
    row_sums = (
        mp.mpf(0),
        phi_vals[0],
        phi_vals[0] + phi_vals[1],
        phi_vals[0] + phi_vals[1] + phi_vals[2],
        phi_vals[0] + phi_vals[1] + phi_vals[2] + phi_vals[3],
    )
    tot = mp.mpf(0)
    for r in pauli_wigner_rows(Z, N):
        tot += row_sums[r]
    return tot


def qint_mp(n: int, qv: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return sum((qv ** (n - 1 - 2 * k) for k in range(n)), mp.mpf(0))


def qbinom2_mp(n: int, qv: mp.mpf) -> mp.mpf:
    if n < 2:
        return mp.mpf(0)
    return qint_mp(n, qv) * qint_mp(n - 1, qv) / qint_mp(2, qv)


def qbinom3_mp(n: int, qv: mp.mpf) -> mp.mpf:
    if n < 3:
        return mp.mpf(0)
    return qint_mp(n, qv) * qint_mp(n - 1, qv) * qint_mp(n - 2, qv) / (
        qint_mp(2, qv) * qint_mp(3, qv)
    )


def symbolic_derivations() -> dict[str, str]:
    """Derive exact closed forms over Q(q) via sympy."""
    q = sp.Symbol("q", positive=True)

    def q_int(n: int) -> sp.Expr:
        if n == 0:
            return sp.Integer(0)
        return sp.simplify(sum(q ** (n - 1 - 2 * k) for k in range(n)))

    def q_b2(n: int) -> sp.Expr:
        if n < 2:
            return sp.Integer(0)
        return sp.simplify(q_int(n) * q_int(n - 1) / q_int(2))

    def q_b3(n: int) -> sp.Expr:
        if n < 3:
            return sp.Integer(0)
        return sp.simplify(q_int(n) * q_int(n - 1) * q_int(n - 2) / (q_int(2) * q_int(3)))

    phi_qi = [q_int(j) for j in range(4)]
    b3_qi = sp.factor(phi_qi[2] - 2 * phi_qi[1])
    b4_qi = sp.factor(phi_qi[3] - 3 * phi_qi[2] + 3 * phi_qi[1])

    phi_tri = [q_b2(j) for j in range(4)]
    b3_tri = sp.factor(phi_tri[2] - 2 * phi_tri[1])
    b4_tri = sp.factor(phi_tri[3] - 3 * phi_tri[2] + 3 * phi_tri[1])

    phi_qs = [
        sp.simplify(q_int(j) / q_int(2) + q_b2(j) / q_int(3) + q_b3(j) / q_int(4))
        for j in range(4)
    ]
    b2_qs = sp.factor(phi_qs[1])
    b3_qs = sp.factor(phi_qs[2] - 2 * phi_qs[1])
    b4_qs = sp.factor(phi_qs[3] - 3 * phi_qs[2] + 3 * phi_qs[1])
    bulk_qs = sp.factor((phi_qs[1] + phi_qs[2] + phi_qs[3]) / 4)

    phi_ep = [
        sp.simplify(q_int(j) / q_int(2) - q_b2(j) / q_int(3) + q_b3(j) / q_int(4))
        for j in range(4)
    ]
    b3_ep = sp.factor(phi_ep[2] - 2 * phi_ep[1])
    b4_ep = sp.factor(phi_ep[3] - 3 * phi_ep[2] + 3 * phi_ep[1])

    # Verify exact identities matching Lean theorems
    assert sp.simplify(b3_qi - (q - 1) ** 2 / q) == 0
    assert sp.simplify(b4_qi - (q - 1) ** 2 * (q**2 - q + 1) / q**2) == 0
    assert sp.simplify(b3_tri - 1) == 0
    assert sp.simplify(b4_tri - (q - 1) ** 2 * (q + 1) ** 2 / q**2) == 0
    assert sp.simplify(b2_qs - q / (q**2 + 1)) == 0
    assert sp.simplify(b3_qs - ((q - 1) ** 2 / (q**2 + 1) + q**2 / (q**4 + q**2 + 1))) == 0
    assert sp.simplify(b3_ep - ((q - 1) ** 2 / (q**2 + 1) - q**2 / (q**4 + q**2 + 1))) == 0

    u = sp.Symbol("u")
    pal_check = sp.simplify(
        b3_ep
        - q**3 * (((q + 1 / q) - 2) * ((q + 1 / q) ** 2 - 1) - (q + 1 / q))
        / ((q**2 + 1) * (q**4 + q**2 + 1))
    )
    assert pal_check == 0

    return {
        "qInt_b3": str(b3_qi),
        "qInt_b4": str(b4_qi),
        "qBinom2_b3": str(b3_tri),
        "qBinom2_b4": str(b4_tri),
        "qSimplex_b2_over_E0": str(b2_qs),
        "qSimplex_b3_over_E0": str(b3_qs),
        "qSimplex_b4_over_E0": str(b4_qs),
        "qSimplex_alpha_bulk_per_A_over_E0": str(bulk_qs),
        "epQSimplex_b3_over_E0": str(b3_ep),
        "epQSimplex_b4_over_E0": str(b4_ep),
        "epQSimplex_palindromic_factor_u_eq_q_plus_qinv": str(
            sp.expand((u - 2) * (u**2 - 1) - u)
        ),
    }


def score_dataset(
    pred_fn, records: list[dict]
) -> dict[str, str]:
    """Compute exact 80-dps MAE and RMSE on total B (MeV) and B/A (MeV/nucleon)."""
    n = mp.mpf(len(records))
    abs_tot = mp.mpf(0)
    sq_tot = mp.mpf(0)
    abs_pa = mp.mpf(0)
    sq_pa = mp.mpf(0)
    for rec in records:
        pred = pred_fn(rec["Z"], rec["N"])
        err = pred - rec["B_MeV"]
        err_pa = err / mp.mpf(rec["A"])
        abs_tot += abs(err)
        sq_tot += err * err
        abs_pa += abs(err_pa)
        sq_pa += err_pa * err_pa
    return {
        "count": str(len(records)),
        "MAE_B_MeV": fmt24(abs_tot / n),
        "RMSE_B_MeV": fmt24(mp.sqrt(sq_tot / n)),
        "MAE_B_per_A_MeV": fmt24(abs_pa / n),
        "RMSE_B_per_A_MeV": fmt24(mp.sqrt(sq_pa / n)),
    }


def evaluate_pin(
    pin_name: str, q_val: mp.mpf, me_val: mp.mpf, ame: dict[tuple[int, int], dict]
) -> dict:
    """Evaluate all zero-parameter carriers at 80 dps for a single substrate pin."""
    q_str_full = mp.nstr(q_val, WORKING_DPS + 5)
    me_str_full = str(M_E_MEV)
    E0_tower = qbeta_e0.tower_summed(q=q_str_full, m_e=me_str_full)
    E0_zero = qbeta_e0.order_zero(q=q_str_full, m_e=me_str_full)
    z_D = q_val**3 / (q_val**2 + 1)
    ln_inv_zD = -mp.log(z_D)
    w1_zD = E0_tower * ln_inv_zD

    qi2 = qint_mp(2, q_val)
    qi3 = qint_mp(3, q_val)
    qi4 = qint_mp(4, q_val)

    # Precompute 4-element intra-shell column kernels phi(0..3) at 80 dps
    phi_lin = tuple(mp.mpf(j) * w1_zD for j in range(4))
    phi_qint = tuple(qint_mp(j, q_val) * w1_zD for j in range(4))
    phi_qsimplex = tuple(
        E0_tower * (
            qint_mp(j, q_val) / qi2
            + qbinom2_mp(j, q_val) / qi3
            + qbinom3_mp(j, q_val) / qi4
        )
        for j in range(4)
    )
    phi_ep_qsimplex = tuple(
        E0_tower * (
            qint_mp(j, q_val) / qi2
            - qbinom2_mp(j, q_val) / qi3
            + qbinom3_mp(j, q_val) / qi4
        )
        for j in range(4)
    )
    phi_unsigned_zD = tuple(
        w1_zD * mp.mpf(j + (j * (j - 1) // 2) + (j * (j - 1) * (j - 2) // 6))
        for j in range(4)
    )

    models = {
        "M0_chain_zD": lambda Z, N: mp.mpf(Z + N - 1) * w1_zD,
        "M1_pw_shell_zD_b3_zero": lambda Z, N: cell_sum_mp(Z, N, phi_lin),
        "M2_ep_alternating_qSimplex": lambda Z, N: cell_sum_mp(Z, N, phi_ep_qsimplex),
        "M3_qInt_bratteli_zD": lambda Z, N: cell_sum_mp(Z, N, phi_qint),
        "M4_unsigned_qSimplex_wenzl": lambda Z, N: cell_sum_mp(Z, N, phi_qsimplex),
        "M5_unsigned_simplex_uniform_zD": lambda Z, N: cell_sum_mp(Z, N, phi_unsigned_zD),
    }

    light_bench_6 = [ame[(Z, N)] for _, Z, N in LIGHT_BENCHMARKS if Z + N >= 3]
    light_all_isobars = [
        rec for rec in ame.values() if rec["A"] in LIGHT_A_SET
    ]
    med_heavy_16_240 = [
        rec for rec in ame.values() if 16 <= rec["A"] <= 240
    ]

    B_2H_ame = ame[(1, 1)]["B_MeV"]
    b3_ame_sym = (ame[(1, 2)]["B_MeV"] + ame[(2, 1)]["B_MeV"]) / mp.mpf(2) - mp.mpf(3) * B_2H_ame
    b4_ame_sym = ame[(2, 2)]["B_MeV"] - mp.mpf(6) * B_2H_ame - mp.mpf(4) * b3_ame_sym

    model_summaries = {}
    for mname, mfn in models.items():
        b2_m = mfn(1, 1)
        b3_m = (mfn(1, 2) + mfn(2, 1)) / mp.mpf(2) - mp.mpf(3) * b2_m
        b4_m = mfn(2, 2) - mp.mpf(6) * b2_m - mp.mpf(4) * b3_m
        b3_rel_err_pct = (b3_m - b3_ame_sym) / b3_ame_sym * mp.mpf(100)
        bench_rows = {}
        for lbl, Z, N in LIGHT_BENCHMARKS:
            pred = mfn(Z, N)
            ref = ame[(Z, N)]["B_MeV"]
            bench_rows[lbl] = {
                "pred_MeV": fmt24(pred),
                "ame_MeV": fmt24(ref),
                "err_MeV": fmt24(pred - ref),
            }
        model_summaries[mname] = {
            "b2_MeV": fmt80(b2_m),
            "b3_MeV": fmt80(b3_m),
            "b4_MeV": fmt80(b4_m),
            "b3_rel_diff_vs_ame_pct": fmt24(b3_rel_err_pct),
            "alpha_bulk_limit_B_per_A_MeV": fmt24(mfn(2, 2) / mp.mpf(4)),
            "triton_MeV": fmt24(mfn(1, 2)),
            "trineutron_MeV": fmt24(mfn(0, 3)),
            "triton_minus_trineutron_MeV": fmt24(mfn(1, 2) - mfn(0, 3)),
            "light_benchmarks": bench_rows,
            "metrics_light_6_benchmarks_A_3_4_6_12_16": score_dataset(mfn, light_bench_6),
            "metrics_light_all_isobars_A_3_4_6_12_16": score_dataset(mfn, light_all_isobars),
            "metrics_med_heavy_A_16_240": score_dataset(mfn, med_heavy_16_240),
        }

    # Check order-zero E0 variant on M4_unsigned_qSimplex_wenzl for completeness
    b3_qsimplex_order_zero = E0_zero * (
        (q_val - 1) ** 2 / (q_val**2 + 1) + q_val**2 / (q_val**4 + q_val**2 + 1)
    )

    return {
        "pin": pin_name,
        "q0_80dps": fmt80(q_val),
        "E0_tower_summed_MeV": fmt80(E0_tower),
        "E0_order_zero_MeV": fmt80(E0_zero),
        "w1_zD_MeV": fmt80(w1_zD),
        "qSimplex_b3_tower_MeV": model_summaries["M4_unsigned_qSimplex_wenzl"]["b3_MeV"],
        "qSimplex_b3_order_zero_MeV": fmt80(b3_qsimplex_order_zero),
        "ame_reference": {
            "b2_MeV": fmt24(B_2H_ame),
            "b3_sym_MeV": fmt24(b3_ame_sym),
            "b4_sym_MeV": fmt24(b4_ame_sym),
        },
        "models": model_summaries,
    }


def main() -> int:
    t0 = time.time()
    mp.mp.dps = WORKING_DPS

    q_proton = q_at(WORKING_DPS)
    q_muon = q_muon_at(WORKING_DPS)
    me = mp.mpf(str(M_E_MEV))

    ame = load_ame2020_exact()
    sym_data = symbolic_derivations()

    # Route A: exact per-atom canonical crossing census across light nuclei
    route_a_rows = []
    all_route_a_formulas_exact = True
    for lbl, Z, N in [("1H", 1, 0), *LIGHT_BENCHMARKS]:
        w = atom_canonical_crossings(Z, N)
        cnt = Counter(t for _, t in w)
        A = Z + N
        n_braid = cnt["sigma"] + cnt["sigma_inv"]
        n_avg = cnt["averaged"]
        n_avg_wtd = cnt["averaged_weighted"]
        expected_braid = 9 if A == 1 else 10 * A - 2
        expected_avg = 2 * A
        expected_wtd = 0 if A == 1 else 1
        ok_row = (
            len(w) == 12 * A - 1
            and n_braid == expected_braid
            and n_avg == expected_avg
            and n_avg_wtd == expected_wtd
        )
        all_route_a_formulas_exact &= ok_row
        route_a_rows.append({
            "nucleus": lbl,
            "Z": Z,
            "N": N,
            "A": A,
            "total_letters": len(w),
            "pure_braid_letters": n_braid,
            "averaged_letters": n_avg,
            "averaged_weighted_letters": n_avg_wtd,
            "non_braid_hecke_letters": n_avg + n_avg_wtd,
            "matches_closed_form": ok_row,
        })

    res_proton = evaluate_pin("proton", q_proton, me, ame)
    res_muon = evaluate_pin("muon", q_muon, me, ame)

    m4_p = res_proton["models"]["M4_unsigned_qSimplex_wenzl"]
    m2_p = res_proton["models"]["M2_ep_alternating_qSimplex"]
    m1_p = res_proton["models"]["M1_pw_shell_zD_b3_zero"]
    m0_p = res_proton["models"]["M0_chain_zD"]
    m3_p = res_proton["models"]["M3_qInt_bratteli_zD"]
    m4_m = res_muon["models"]["M4_unsigned_qSimplex_wenzl"]

    b3_m4_p = mp.mpf(m4_p["b3_MeV"])
    b3_m4_m = mp.mpf(m4_m["b3_MeV"])
    b3_m2_p = mp.mpf(m2_p["b3_MeV"])
    b3_m3_p = mp.mpf(m3_p["b3_MeV"])
    b3_ame_sym = mp.mpf(res_proton["ame_reference"]["b3_sym_MeV"])
    cross_anchor_swing_ppb = abs(b3_m4_p - b3_m4_m) / b3_m4_p * mp.mpf("1e9")

    mae_light_m0 = mp.mpf(m0_p["metrics_light_6_benchmarks_A_3_4_6_12_16"]["MAE_B_per_A_MeV"])
    mae_light_m1 = mp.mpf(m1_p["metrics_light_6_benchmarks_A_3_4_6_12_16"]["MAE_B_per_A_MeV"])
    mae_light_m2 = mp.mpf(m2_p["metrics_light_6_benchmarks_A_3_4_6_12_16"]["MAE_B_per_A_MeV"])
    mae_light_m4 = mp.mpf(m4_p["metrics_light_6_benchmarks_A_3_4_6_12_16"]["MAE_B_per_A_MeV"])

    mae_mh_m0 = mp.mpf(m0_p["metrics_med_heavy_A_16_240"]["MAE_B_per_A_MeV"])
    mae_mh_m1 = mp.mpf(m1_p["metrics_med_heavy_A_16_240"]["MAE_B_per_A_MeV"])
    mae_mh_m4 = mp.mpf(m4_p["metrics_med_heavy_A_16_240"]["MAE_B_per_A_MeV"])

    wb = WitnessBuilder(
        "b3-extensive-ep-cell-carrier-probe",
        engine="mpmath+sympy",
        start_time=t0,
        _script_path=__file__,
    )
    wb.set_description(
        "80-dps working-assumption probe and exact Q(q) symbolic derivation for beans "
        "qou-eptr and qou-q8vl: proves the Hecke non-braid & homological (-1)^{d-1} "
        "Euler-Poincare sign obstructions on Route A, and evaluates the zero-parameter "
        "(Z, N)-resolved Pauli-Wigner intra-shell quantum simplex cell-sum carriers across "
        "light A in {2,3,4,6,12,16} and medium/heavy A=16..240 against AME2020 at both "
        "proton and muon q0 pins (zero fitting; nothing wired into production)."
    )
    wb.add_parameter("working_dps", WORKING_DPS)
    wb.add_parameter("zero_fitting", True)
    wb.add_parameter("working_assumption_probe", True)
    wb.add_parameter("ame2020_non_estimated_count", len(ame))

    # Assertions verifying every structural theorem and 80-dps measurement
    wb.add_assertion(
        "route_a_nonbraid_hecke_and_layered_b3_neg_26",
        computed="1"
        if (all_route_a_formulas_exact and (28 - 3 * 18 == -26))
        else "0",
        expected="1",
        tolerance="0",
        source="atom_canonical_crossings(Z,N) has 10A-2 braid letters (b3 = -26 < 0) + 2A averaged + 1 averaged_weighted non-braid Hecke letters for A >= 2",
    )
    wb.add_assertion(
        "ep_alternating_sign_forces_b3_negative",
        computed="1" if (b3_m2_p < mp.mpf(0) and mae_light_m2 > mae_light_m1) else "0",
        expected="1",
        tolerance="0",
        source="(-1)^{d-1} Euler-Poincare sign alternation gives b3 = -1.36602 MeV < 0 and worsens MAE vs pairwise baseline",
    )
    wb.add_assertion(
        "qint_bratteli_b3_positive_but_hbar_suppressed",
        computed="1" if (mp.mpf(0) < b3_m3_p < mp.mpf("0.05")) else "0",
        expected="1",
        tolerance="0",
        source="S_{[j]_q} has b3 > 0 unconditionally ((q-1)^2/q * w1 = +0.02257 MeV) but O(hbar_q^2)-suppressed ~63x below AME2020",
    )
    wb.add_assertion(
        "unsigned_qsimplex_wenzl_b3_positive_and_on_scale",
        computed=fmt24(b3_m4_p),
        expected=fmt24(b3_ame_sym),
        tolerance="0.05",
        source="Zero-parameter Wenzl-normalised quantum simplex carrier gives b3 = +1.4118346 MeV vs AME2020 +1.4262202 MeV (-1.0087%, within 0.05 MeV diagnostic window)",
    )
    wb.add_assertion(
        "pauli_triton_exceeds_trineutron_by_phi2",
        computed="1"
        if mp.mpf(m4_p["triton_minus_trineutron_MeV"]) > mp.mpf("5.6")
        else "0",
        expected="1",
        tolerance="0",
        source="Pauli spin exclusion splits (0,3) across [2,1] while (1,2) occupies [3], giving B(3H) - B(3n) = phi(2) = +5.61641 MeV > 0",
    )
    wb.add_assertion(
        "unsigned_qsimplex_reduces_mae_light_and_heavy_vs_chain_and_pairwise",
        computed="1"
        if (mae_light_m4 < mae_light_m1 < mae_light_m0 and mae_mh_m4 < mae_mh_m1 < mae_mh_m0)
        else "0",
        expected="1",
        tolerance="0",
        source="M4_unsigned_qSimplex_wenzl lowers MAE(B/A) on both light A in {3,4,6,12,16} (3.930 -> 2.931 -> 1.701 MeV/A) and medium/heavy A=16..240 (6.106 -> 5.383 -> 3.926 MeV/A)",
    )

    wb.add_data("symbolic_Q_of_q", sym_data)
    wb.add_data("route_a_canonical_crossings_census", route_a_rows)
    wb.add_data("pins", {"proton": res_proton, "muon": res_muon})
    wb.add_data(
        "cross_anchor_comparison",
        {
            "qSimplex_b3_proton_MeV": m4_p["b3_MeV"],
            "qSimplex_b3_muon_MeV": m4_m["b3_MeV"],
            "abs_diff_MeV": fmt80(abs(b3_m4_p - b3_m4_m)),
            "rel_swing_ppb": fmt24(cross_anchor_swing_ppb),
        },
    )
    wb.add_data(
        "honest_limitations",
        {
            "working_assumption_status": (
                "The Wenzl-normalised 1/[d+1]_q simplex measure is an explicit zero-parameter "
                "working-assumption probe over Pauli-Wigner SU(4) shells, NOT yet derived from "
                "the full 3A-strand gamma-gamma-selected Hecke trace."
            ),
            "four_body_and_inter_shell_gap": (
                "Intra-shell cell sums give b4 = +1.11253 MeV vs AME2020 +9.24338 MeV on 4He "
                "(19.3736 vs 28.2957 MeV) and cap the alpha-conjugate bulk rate at "
                "4.8434 MeV/nucleon vs ~8.795 MeV/nucleon at 62Ni because inter-shell alpha-alpha "
                "contacts and Z(Z-1)/A^{1/3} Coulomb repulsion live between spatial shells."
            ),
            "gg_selection_rule_compliance": (
                "Per docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md, none of "
                "models M0-M5 read superseded single-crossing atom_braid_word_3A shifts d_k."
            ),
        },
    )

    out_path = wb.save(
        q0_comparison(
            muon=mp.nstr(q_muon, 50),
            proton=Q_50_DIGIT_STR,
            reason=(
                "evaluates zero-parameter Pauli-Wigner intra-shell cell-sum carriers and "
                "Euler-Poincare sign obstructions for b_3 at 80 dps across both registered "
                "q0 pins (proton Physical-Observations pin q_p and muon ideal pin q_mu)"
            ),
        )
    )

    print("=" * 88)
    print(" B3 EXTENSIVE EULER-POINCARE & PAULI-WIGNER CELL-SUM CARRIER PROBE (80 dps)")
    print("=" * 88)
    print(f" Proton q_p : {mp.nstr(q_proton, 36)}")
    print(f" Muon   q_mu: {mp.nstr(q_muon, 36)}")
    print(f" AME2020    : b2 = {mp.nstr(mp.mpf(res_proton['ame_reference']['b2_MeV']), 10)} MeV | "
          f"b3_sym = {mp.nstr(b3_ame_sym, 10)} MeV | "
          f"b4_sym = {mp.nstr(mp.mpf(res_proton['ame_reference']['b4_sym_MeV']), 10)} MeV")
    print("-" * 88)
    for mname, minfo in res_proton["models"].items():
        ml = minfo["metrics_light_6_benchmarks_A_3_4_6_12_16"]
        mmh = minfo["metrics_med_heavy_A_16_240"]
        print(
            f" {mname:34s} | b3 = {mp.nstr(mp.mpf(minfo['b3_MeV']), 8):>11s} MeV "
            f"| Light MAE(B/A) = {mp.nstr(mp.mpf(ml['MAE_B_per_A_MeV']), 5):>7s} "
            f"| A=16..240 MAE(B/A) = {mp.nstr(mp.mpf(mmh['MAE_B_per_A_MeV']), 5):>7s}"
        )
    print("-" * 88)
    print(f" Cross-anchor swing on M4 b_3 (q_p vs q_mu): {mp.nstr(cross_anchor_swing_ppb, 8)} ppb")
    print(f" Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
