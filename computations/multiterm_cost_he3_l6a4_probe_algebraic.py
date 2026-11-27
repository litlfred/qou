"""multiterm_cost_he3_l6a4_probe_algebraic.py

Tests the hypothesis: "using the R-side algebraic form (symbolic form) for T2 and T3
rescues the multi-term mass formula for He3 and allows L6a4 to win."

For the algebraic form:
  T2 = (n - 1) * z^2
  T3 = C(n - 1, 2) * z^4
where n is the strand count (n = 9 for He3 full atom, or n = 3 for interface),
evaluated at 80-dps working precision on the canonical proton anchor q_0 with
two-row SU(2) Markov parameter z = q_0^3 / (q_0^2 + 1).

Both the interleaved Borromean trace |tr_M((sigma_0 sigma_1^-1)^3)| = 1 - h^4 + h^4 z^2 - h^5 z
and the Frobenius co-Casimir sum m_e * sum_{lambda |- 9} 1 / dim_q(lambda) are derived
directly at 80 dps rather than hardcoded from pre-migration literals (bean qou-5pgl).
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
from codata_constants import AME_B_HE3_MEV_VALIDATION, M_E_MEV  # noqa: E402
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
    """Exact hook-length evaluation of sum_{lambda |- n_val} 1 / dim_q(lambda)."""
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


def h3_step(vec: list[mpf], c: mpf, d: mpf, gen: int, hv: mpf) -> list[mpf]:
    """Multiply 6-basis normal form [1, T0, T1, T0 T1, T1 T0, T0 T1 T0] in H_3(q) on the right by (c*T_gen + d)."""
    out = [mpf(0)] * 6
    if gen == 0:
        rules = [
            (0, [(1, c), (0, d)]),
            (1, [(1, c * hv), (0, c), (1, d)]),
            (2, [(3, c), (2, d)]),
            (3, [(3, c * hv), (2, c), (3, d)]),
            (4, [(5, c), (4, d)]),
            (5, [(5, c * hv), (4, c), (5, d)]),
        ]
    else:
        rules = [
            (0, [(2, c), (0, d)]),
            (1, [(4, c), (1, d)]),
            (2, [(2, c * hv), (0, c), (2, d)]),
            (3, [(5, c), (3, d)]),
            (4, [(4, c * hv), (1, c), (4, d)]),
            (5, [(5, c * hv), (3, c), (5, d)]),
        ]
    for src, targets in rules:
        v_src = vec[src]
        for dst, coeff in targets:
            out[dst] += v_src * coeff
    return out


def main() -> int:
    with mp.workdps(80):
        q = q_at(80)
        qi = mpf(1) / q
        h = q - qi
        z = (q ** 3) / (q ** 2 + mpf(1))
        m_e = mpf(str(M_E_MEV))
        b_ame = mpf(str(AME_B_HE3_MEV_VALIDATION))

        # Derive L6a4 = (sigma_0 sigma_1^-1)^3 Markov trace in H_3(q_0) two independent ways:
        # (a) closed-form polynomial 1 - h^4 + h^4 z^2 - h^5 z
        trm_l6a4 = mpf(1) - (h ** 4) + (h ** 4) * (z ** 2) - (h ** 5) * z
        # (b) explicit 6-basis Hecke normal-form reduction
        vec_bor = [mpf(1)] + [mpf(0)] * 5
        for _ in range(3):
            vec_bor = h3_step(vec_bor, mpf(1), mpf(0), 0, h)
            vec_bor = h3_step(vec_bor, mpf(1), -h, 1, h)
        basis_weights = [mpf(1), z, z, z ** 2, z ** 2, h * (z ** 2) + z]
        trm_l6a4_basis = sum(vec_bor[i] * basis_weights[i] for i in range(6))

        # Historical single-row z = sqrt(q)/(q + 1) comparison figure (audit telemetry only)
        z_single_row = mp.sqrt(q) / (q + mpf(1))
        trm_l6a4_single_row = (
            mpf(1) - (h ** 4) + (h ** 4) * (z_single_row ** 2) - (h ** 5) * z_single_row
        )

        rho_l6a4 = 3
        m_e_sigma_9 = m_e * sigma_inv_dim_q_hook(q, 9)

        # n = 9 (3A strands for A = 3)
        n = 9
        t2_hecke = mpf(n - 1) * (z ** 2)
        t3_hecke = mpf(comb_int(n - 1, 2)) * (z ** 4)
        t23_mev = m_e * (t2_hecke + t3_hecke)

        b_desc = mpf(rho_l6a4) * m_e * trm_l6a4
        b_pred_n9 = b_desc + m_e_sigma_9 + t23_mev
        rel_resid_n9 = abs(b_ame - b_pred_n9) / b_ame

        # Interface n = 3
        n3 = 3
        t2_3 = mpf(n3 - 1) * (z ** 2)
        t3_3 = mpf(comb_int(n3 - 1, 2)) * (z ** 4)
        t23_3_mev = m_e * (t2_3 + t3_3)
        b_pred_n3 = b_desc + m_e_sigma_9 + t23_3_mev
        rel_resid_n3 = abs(b_ame - b_pred_n3) / b_ame

        print("Multi-term cost vs He3 L6a4 probe (ALGEBRAIC FORM T2+T3)")
        print()
        print(f"  tr_M(L6a4) derived     = {mp.nstr(trm_l6a4, 18)}")
        print(f"  n (strands)            = {n}")
        print(f"  T2 (Hecke)             = {mp.nstr(t2_hecke, 6)}")
        print(f"  T3 (Hecke)             = {mp.nstr(t3_hecke, 6)}")
        print(f"  T2+T3 (MeV)            = {mp.nstr(t23_mev, 6)} MeV")
        print(f"  T4 (MeV)               = {mp.nstr(m_e_sigma_9, 6)} MeV")
        print(f"  L6a4 B_desc (T1)       = {mp.nstr(b_desc, 6)} MeV")
        print(f"  L6a4 B_pred (T1+T23+T4)= {mp.nstr(b_pred_n9, 6)} MeV")
        print(f"  B_AME                  = {mp.nstr(b_ame, 6)} MeV")
        print(f"  rel_resid (n=9)        = {mp.nstr(rel_resid_n9, 6)}")
        print()
        print("  If n=3 (interface):")
        print(f"  T2+T3 (MeV)            = {mp.nstr(t23_3_mev, 6)} MeV")
        print(f"  L6a4 B_pred            = {mp.nstr(b_pred_n3, 6)} MeV")
        print(f"  rel_resid (n=3)        = {mp.nstr(rel_resid_n3, 6)}")

        wb = WitnessBuilder(
            "multiterm-cost-he3-l6a4-probe-algebraic",
            _script_path=Path(__file__),
            output_dir=HERE,
            engine="mpmath",
        )
        wb.set_audit_only("docs/audits/2026-11-24-hecke-core-z-importer-audit-5pgl.md")
        wb.set_description(
            "Evaluates the R-side algebraic T2 + T3 multi-term formula for 3He (L6a4) at 80-dps "
            "precision under the two-row SU(2) Markov parameter z = q_0^3 / (q_0^2 + 1), replacing "
            "the stale pre-migration literal 0.998367 with the derived H_3(q_0) trace "
            "1 - h^4 + h^4 z^2 - h^5 z = 0.998562163836787266... and exact hook-length T4. "
            "Both strand choices fail to recover B_AME(3He) = 7.71804 MeV (n=9 leaves a >15% "
            "deficit; n=3 leaves a >57% deficit)."
        )
        wb.add_data(
            "derived_inputs_60dps",
            {
                "q0": fmt60(q),
                "h": fmt60(h),
                "z_two_row": fmt60(z),
                "trm_l6a4_derived": fmt60(trm_l6a4),
                "trm_l6a4_single_row_historical": fmt60(trm_l6a4_single_row),
                "m_e_sigma_9_MeV": fmt60(m_e_sigma_9),
                "b_ame_he3_MeV": fmt60(b_ame),
            },
        )
        wb.add_data(
            "predictions_60dps",
            {
                "b_desc_MeV": fmt60(b_desc),
                "n9_t2_hecke": fmt60(t2_hecke),
                "n9_t3_hecke": fmt60(t3_hecke),
                "n9_t23_MeV": fmt60(t23_mev),
                "n9_b_pred_MeV": fmt60(b_pred_n9),
                "n9_rel_resid": fmt60(rel_resid_n9),
                "n3_t23_MeV": fmt60(t23_3_mev),
                "n3_b_pred_MeV": fmt60(b_pred_n3),
                "n3_rel_resid": fmt60(rel_resid_n3),
            },
        )
        wb.add_assertion(
            "l6a4_closed_form_matches_h3_normal_form_basis_trace",
            computed=abs(trm_l6a4 - trm_l6a4_basis),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="H_3(q_0) 6-basis reduction of (sigma_0 sigma_1^-1)^3 equals 1 - h^4 + h^4 z^2 - h^5 z",
        )
        wb.add_assertion(
            "algebraic_t23_fails_to_recover_he3_binding_for_n9_and_n3",
            computed=bool(rel_resid_n9 > mpf("0.15") and rel_resid_n3 > mpf("0.55")),
            expected=True,
            tolerance=0,
            source="Both n=9 (rel_resid > 15%) and n=3 (rel_resid > 55%) miss B_AME(3He) = 7.71804 MeV",
        )
        out = wb.save({"q0Anchor": "proton"})
        print(f"\n  Witness: {out.name}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
