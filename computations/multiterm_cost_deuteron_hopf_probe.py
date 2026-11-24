"""multiterm_cost_deuteron_hopf_probe.py

Tests the multi-term additive mass formula for the deuteron under the
structural decomposition T_comp = (T_p (x) T_n) * sigma_3^2 at H_6(q_0).

Evaluated at 80-dps working precision on the canonical proton anchor q_0 with
two-row SU(2) Markov parameter z = q_0^3 / (q_0^2 + 1) (bean qou-5pgl):
  - Replaces the pre-migration literal TRM_COMPOSITE = 1.1007832370743025
    (produced under z = 1/(q_0^(1/2) + q_0^(-1/2))) with the exact two-row H_6(q_0)
    Wenzl-Schur / Markov trace (1 + h z) * (1 - h^4 + h^4 z^2 - h^5 z)^2
    = 1.12484706271117401763..., verified directly against the 80-dps H_6(q_0)
    Hoefsmit seminormal character sum sum_{lambda |- 6} y_lambda(q_0) chi^lambda(T_comp).
  - Replaces the rounded 4-digit Frobenius co-Casimir literal 1.636 with the exact
    80-dps hook-length evaluation m_e * sum_{lambda |- 6} 1/dim_q(lambda)
    = 1.63628711459308350910... MeV.
  - Confirms that the additive R-side T1 + T2 + T3 + T4 formula still fails to
    recover B_AME(2H) = 2.224566 MeV (overshooting to 3.89027 MeV, rel_resid = 0.748776, +74.88%).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, M_E_MEV  # noqa: E402
import schur_principal_mpmath as spm  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 80


def fmt60(x: mpf) -> str:
    return mp.nstr(x, 60, strip_zeros=False)


def comb_int(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    num = 1
    den = 1
    for j in range(1, k + 1):
        num *= n - k + j
        den *= j
    return num // den


def partitions_of(n: int, max_part: int | None = None) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    cap = n if max_part is None else min(n, max_part)
    out: list[tuple[int, ...]] = []
    for p in range(cap, 0, -1):
        for tail in partitions_of(n - p, p):
            out.append((p,) + tail)
    return out


def q_int(qv: mpf, k: int) -> mpf:
    return (qv ** k - qv ** (-k)) / (qv - qv ** (-1))


def sigma_inv_dim_q_hook(qv: mpf, n_val: int) -> mpf:
    qfact_n = mpf(1)
    for k in range(1, n_val + 1):
        qfact_n *= q_int(qv, k)
    tot = mpf(0)
    for lam in partitions_of(n_val):
        hook_prod = mpf(1)
        for r, row_len in enumerate(lam):
            for c in range(row_len):
                arm = row_len - c - 1
                leg = sum(1 for r2 in range(r + 1, len(lam)) if lam[r2] > c)
                hook_prod *= q_int(qv, arm + leg + 1)
        tot += hook_prod / qfact_n
    return tot


def syt_of(lam: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    n = sum(lam)
    res: list[tuple[tuple[int, int], ...]] = []
    cur = [0] * len(lam)
    placement: list[tuple[int, int]] = []

    def bt(k: int) -> None:
        if k == n:
            res.append(tuple(placement))
            return
        for r in range(len(lam)):
            if cur[r] < lam[r] and (r == 0 or cur[r] < cur[r - 1]):
                cur[r] += 1
                placement.append((r, cur[r] - 1))
                bt(k + 1)
                placement.pop()
                cur[r] -= 1

    bt(0)
    return res


def hoefsmit_seminormal_mp(lam: tuple[int, ...], qv: mpf) -> tuple[list[mp.matrix], list[mp.matrix]]:
    """Exact 80-dps Hoefsmit seminormal generators for partition `lam` at parameter `qv`."""
    tabs = syt_of(lam)
    d = len(tabs)
    idx_map = {t: i for i, t in enumerate(tabs)}
    n = sum(lam)
    hv = qv - mpf(1) / qv
    gens: list[mp.matrix] = []
    invs: list[mp.matrix] = []
    for g in range(n - 1):
        mat = mp.matrix(d, d)
        for i, tab in enumerate(tabs):
            r1, c1 = tab[g]
            r2, c2 = tab[g + 1]
            ax = (c2 - r2) - (c1 - r1)
            if r1 == r2:
                mat[i, i] = qv
            elif c1 == c2:
                mat[i, i] = -mpf(1) / qv
            else:
                qa = q_int(qv, ax)
                mat[i, i] = hv / (mpf(1) - qv ** (-2 * ax))
                swapped = tab[:g] + (tab[g + 1], tab[g]) + tab[g + 2 :]
                j = idx_map[swapped]
                if i < j:
                    off = mp.sqrt(mpf(1) - mpf(1) / (qa ** 2))
                    mat[i, j] = off
                    mat[j, i] = off
        gens.append(mat)
        invs.append(mat - hv * mp.eye(d))
    return gens, invs


def main() -> int:
    with mp.workdps(80):
        q = q_at(80)
        h = q - mpf(1) / q
        z = (q ** 3) / (q ** 2 + mpf(1))
        m_e = mpf(str(M_E_MEV))
        b_ame = mpf(str(AME_B_DEUTERON_MEV_VALIDATION))

        # 1. Exact Markov-factorized closed form for T_comp = ((s0 s1^-1)^3 (x) (s3 s4^-1)^3) * s2^2 in H_6(q_0)
        trm_bor = mpf(1) - (h ** 4) + (h ** 4) * (z ** 2) - (h ** 5) * z
        trm_composite = (mpf(1) + h * z) * (trm_bor ** 2)

        # 2. Independent verification via 80-dps H_6(q_0) Hoefsmit-Wenzl sum over two-row partitions
        y_weights = spm.y_lambda_at_q0_mpmath(6, q)
        # 1-indexed generator sequence for ((s1 s2^-1)^3 * (s4 s5^-1)^3 * s3^2) in B_6
        comp_gens_1idx = [1, -2, 1, -2, 1, -2, 4, -5, 4, -5, 4, -5, 3, 3]
        trm_wenzl_h6 = mpf(0)
        for lam, y_lam in y_weights.items():
            if y_lam == 0:
                continue
            gens, invs = hoefsmit_seminormal_mp(lam, q)
            d = gens[0].rows
            w_mat = mp.eye(d)
            for g1 in comp_gens_1idx:
                idx = abs(g1) - 1
                w_mat = w_mat * (gens[idx] if g1 > 0 else invs[idx])
            chi_val = sum(w_mat[i, i] for i in range(d))
            trm_wenzl_h6 += y_lam * chi_val

        # Historical single-row comparison value at proton q_0
        z_single_row = mp.sqrt(q) / (q + mpf(1))
        trm_bor_single = (
            mpf(1) - (h ** 4) + (h ** 4) * (z_single_row ** 2) - (h ** 5) * z_single_row
        )
        trm_composite_single_row = (mpf(1) + h * z_single_row) * (trm_bor_single ** 2)

        rho_deuteron = 1
        m_e_sigma_6 = m_e * sigma_inv_dim_q_hook(q, 6)

        # n = 6 (3A strands for A = 2)
        n = 6
        t2_hecke = mpf(n - 1) * (z ** 2)
        t3_hecke = mpf(comb_int(n - 1, 2)) * (z ** 4)
        t23_mev = m_e * (t2_hecke + t3_hecke)

        b_desc = mpf(rho_deuteron) * m_e * trm_composite
        b_pred = b_desc + m_e_sigma_6 + t23_mev
        rel_resid = abs(b_ame - b_pred) / b_ame

        print("Multi-term cost vs Deuteron Hopf-factorised probe (ALGEBRAIC FORM T2+T3)")
        print()
        print(f"  tr_M(T_comp) derived   = {mp.nstr(trm_composite, 18)}")
        print(f"  n (strands)            = {n}")
        print(f"  T2 (Hecke)             = {mp.nstr(t2_hecke, 6)}")
        print(f"  T3 (Hecke)             = {mp.nstr(t3_hecke, 6)}")
        print(f"  T2+T3 (MeV)            = {mp.nstr(t23_mev, 6)} MeV")
        print(f"  T4 (MeV)               = {mp.nstr(m_e_sigma_6, 6)} MeV")
        print(f"  Hopf-comp B_desc (T1)  = {mp.nstr(b_desc, 6)} MeV")
        print(f"  Hopf-comp B_pred       = {mp.nstr(b_pred, 6)} MeV")
        print(f"  B_AME                  = {mp.nstr(b_ame, 6)} MeV")
        print(f"  rel_resid              = {mp.nstr(rel_resid, 6)}")
        print()
        print("Conclusion: The additive multi-term formula fails to evaluate")
        print("correctly for the Hopf-decomposed deuteron at H_6(q_0), proving")
        print("that structural factorization alone cannot rescue the additive cost.")

        wb = WitnessBuilder(
            "multiterm-cost-deuteron-hopf-probe",
            _script_path=Path(__file__),
            output_dir=HERE,
            engine="mpmath",
        )
        wb.set_audit_only("docs/audits/2026-11-24-hecke-core-z-importer-audit-5pgl.md")
        wb.set_description(
            "Evaluates the additive R-side T1+T2+T3+T4 multi-term formula for the Hopf-factorised "
            "deuteron T_comp = ((sigma_1 sigma_2^-1)^3 (x) (sigma_4 sigma_5^-1)^3) * sigma_3^2 at "
            "H_6(q_0) under two-row SU(2) parameter z = q_0^3 / (q_0^2 + 1) at 80-dps precision, "
            "replacing pre-migration literal 1.1007832370743025 with the exact derived trace "
            "1.124847062711174018... and exact hook-length T4. The additive sum overshoots "
            "B_AME(2H) = 2.224566 MeV to 3.89027 MeV (+74.88%), confirming the structural refutation."
        )
        wb.add_data(
            "derived_inputs_60dps",
            {
                "q0": fmt60(q),
                "h": fmt60(h),
                "z_two_row": fmt60(z),
                "trm_composite_closed_form": fmt60(trm_composite),
                "trm_composite_wenzl_h6": fmt60(trm_wenzl_h6),
                "trm_composite_single_row_historical": fmt60(trm_composite_single_row),
                "m_e_sigma_6_MeV": fmt60(m_e_sigma_6),
                "b_ame_deuteron_MeV": fmt60(b_ame),
            },
        )
        wb.add_data(
            "predictions_60dps",
            {
                "t2_hecke": fmt60(t2_hecke),
                "t3_hecke": fmt60(t3_hecke),
                "t23_MeV": fmt60(t23_mev),
                "b_desc_MeV": fmt60(b_desc),
                "b_pred_MeV": fmt60(b_pred),
                "rel_resid": fmt60(rel_resid),
            },
        )
        wb.add_assertion(
            "h6_hopf_composite_closed_form_matches_hoefsmit_wenzl_sum",
            computed=abs(trm_composite - trm_wenzl_h6),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="(1 + h*z)*tr_M((s0 s1^-1)^3)^2 agrees with 80-dps H_6(q_0) Hoefsmit-Wenzl sum to < 1e-70",
        )
        wb.add_assertion(
            "additive_multiterm_formula_fails_on_hopf_deuteron",
            computed=bool(rel_resid > mpf("0.70")),
            expected=True,
            tolerance=0,
            source="Additive T1+T2+T3+T4 prediction (3.89027 MeV) overshoots B_AME(2H) = 2.224566 MeV by +74.88% (>70%)",
        )
        out = wb.save({"q0Anchor": "proton"})
        print(f"\n  Witness: {out.name}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
