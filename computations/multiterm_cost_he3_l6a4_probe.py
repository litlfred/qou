"""multiterm_cost_he3_l6a4_probe.py — Subgoal-1 He3 canonical knot probe.

Tests the hypothesis: "wiring the multi-term mass formula (T4 Frobenius offset)
into the cost function makes He3's historical canonical knot L6a4 the SDP winner".

## Result: the hypothesis is STRUCTURALLY REFUTED.

At 80-dps precision on the canonical proton anchor q_0 with two-row SU(2) Markov
parameter z = q_0^3 / (q_0^2 + 1) (bean qou-5pgl):
  - L6a4 = (sigma_0 sigma_1^-1)^3 has rho = 3 and derived |tr_M| = 1 - h^4 + h^4 z^2 - h^5 z
    = 0.998562163836787266... (replacing pre-migration literal 0.998367), giving
    B_desc = 3 * m_e * |tr_M| = 1.53079 MeV.
  - Exact hook-length Frobenius co-Casimir T4 = m_e * sum_{lambda |- 9} 1/dim_q(lambda)
    = 1.299921976484767797... MeV.
  - Predicted T1 + T4 binding for L6a4 is B_pred = 2.83071 MeV vs B_AME = 7.71804 MeV
    (rel_resid = 0.633234, cost = 0.158309).
  - Higher-trace candidate sigma_0^6 sigma_1^2 in H_3(q_0) with rho = 4 has derived
    |tr_M| = (1 + h z) * tr_M(sigma_0^6) = 1.737180929838697567... (replacing pre-migration
    literal 1.617533), giving B_pred = 4.85071 MeV (rel_resid = 0.371510, cost = 0.092878),
    so L6a4 loses by an even wider margin (0.06543 vs pre-migration 0.05752).
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


def h3_step(vec: list[mpf], c: mpf, d: mpf, gen: int, hv: mpf) -> list[mpf]:
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

        alpha_gap_l6a4 = mpf(0)
        rho_l6a4 = 3
        rho_alt = 4
        w_alpha = mpf(1)
        w_resid = mpf(1) / mpf(4)

        basis_weights = [mpf(1), z, z, z ** 2, z ** 2, h * (z ** 2) + z]

        # Derived L6a4 = (sigma_0 sigma_1^-1)^3 Markov trace in H_3(q_0)
        trm_l6a4 = mpf(1) - (h ** 4) + (h ** 4) * (z ** 2) - (h ** 5) * z
        vec_bor = [mpf(1)] + [mpf(0)] * 5
        for _ in range(3):
            vec_bor = h3_step(vec_bor, mpf(1), mpf(0), 0, h)
            vec_bor = h3_step(vec_bor, mpf(1), -h, 1, h)
        trm_l6a4_basis = sum(vec_bor[i] * basis_weights[i] for i in range(6))

        # Derived alternate candidate [1, 1, 1, 1, 1, 1, 2, 2] = sigma_0^6 sigma_1^2 in H_3(q_0)
        vec_alt = [mpf(1)] + [mpf(0)] * 5
        for g_idx in (0, 0, 0, 0, 0, 0, 1, 1):
            vec_alt = h3_step(vec_alt, mpf(1), mpf(0), g_idx, h)
        trm_alt = sum(vec_alt[i] * basis_weights[i] for i in range(6))
        # Closed-form check via Hecke power T_0^6 = a_6 T_0 + b_6 and Markov peel on T_1^2 = h T_1 + 1:
        a_pow, b_pow = mpf(0), mpf(1)
        for _ in range(6):
            a_pow, b_pow = a_pow * h + b_pow, a_pow
        trm_alt_cf = (mpf(1) + h * z) * (a_pow * z + b_pow)

        m_e_sigma_9 = m_e * sigma_inv_dim_q_hook(q, 9)

        b_desc = mpf(rho_l6a4) * m_e * trm_l6a4
        b_pred = b_desc + m_e_sigma_9
        rel_resid = abs(b_ame - b_pred) / b_ame
        cost_l6a4 = w_alpha * alpha_gap_l6a4 + w_resid * rel_resid

        b_desc_alt = mpf(rho_alt) * m_e * trm_alt
        b_pred_alt = b_desc_alt + m_e_sigma_9
        rel_resid_alt = abs(b_ame - b_pred_alt) / b_ame
        cost_alt = w_resid * rel_resid_alt

        print("Multi-term cost vs He3 L6a4 probe")
        print(f"  cost = {mp.nstr(w_alpha, 4)}*alpha_gap + {mp.nstr(w_resid, 4)}*rel_resid")
        print()
        print(f"  L6a4 |tr_M| derived    = {mp.nstr(trm_l6a4, 16)}")
        print(f"  L6a4 B_desc (T1)       = {mp.nstr(b_desc, 6)} MeV")
        print(f"  L6a4 B_pred (T1+T4)    = {mp.nstr(b_pred, 6)} MeV")
        print(f"  B_AME                  = {mp.nstr(b_ame, 6)} MeV")
        print(f"  rel_resid              = {mp.nstr(rel_resid, 6)}")
        print(f"  L6a4 cost              = {mp.nstr(cost_l6a4, 6)}")
        print()
        print(f"  Alt |tr_M| derived     = {mp.nstr(trm_alt, 16)}")
        print(f"  Alt winner B_pred      = {mp.nstr(b_pred_alt, 6)} MeV")
        print(f"  Alt rel_resid          = {mp.nstr(rel_resid_alt, 6)}")
        print(f"  Alt cost               = {mp.nstr(cost_alt, 6)}")
        print(f"  Alt wins?              = {bool(cost_alt < cost_l6a4)}")

        wb = WitnessBuilder(
            "multiterm-cost-he3-l6a4-probe",
            _script_path=Path(__file__),
            output_dir=HERE,
            engine="mpmath",
        )
        wb.set_audit_only("docs/audits/2026-11-24-hecke-core-z-importer-audit-5pgl.md")
        wb.set_description(
            "Refutes the hypothesis that wiring the T4 Frobenius offset into the SDP "
            "cost makes He3's historical L6a4 the winner, evaluated at 80-dps precision "
            "under z = q_0^3 / (q_0^2 + 1). L6a4's derived T1+T4 binding prediction is "
            "2.8307 MeV vs 7.7180 MeV B_AME, while sigma_0^6 sigma_1^2 reaches 4.8507 MeV "
            "and wins on relative residual."
        )
        wb.add_data("b_pred_l6a4", fmt60(b_pred))
        wb.add_data("cost_l6a4", fmt60(cost_l6a4))
        wb.add_data("cost_alt_winner", fmt60(cost_alt))
        wb.add_data(
            "derived_traces_60dps",
            {
                "trm_l6a4": fmt60(trm_l6a4),
                "trm_alt_s0_6_s1_2": fmt60(trm_alt),
                "m_e_sigma_9_MeV": fmt60(m_e_sigma_9),
                "b_pred_alt_MeV": fmt60(b_pred_alt),
            },
        )
        wb.add_assertion(
            name="multiterm_t4_cannot_rescue_l6a4",
            computed=bool(cost_alt < cost_l6a4),
            expected=True,
            tolerance=0,
            source="T1+T4 offset leaves a 4.89 MeV gap on L6a4, so L6a4 loses to higher-|tr_M| braids.",
        )
        wb.add_assertion(
            name="l6a4_and_alt_h3_trace_identities_at_80dps",
            computed=abs(trm_l6a4 - trm_l6a4_basis) + abs(trm_alt - trm_alt_cf),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="Closed-form H_3(q_0) traces agree with 6-basis normal-form reduction to < 1e-75.",
        )
        out = wb.save({"q0Anchor": "proton"})
        print(f"\n  Witness: {out.name}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
