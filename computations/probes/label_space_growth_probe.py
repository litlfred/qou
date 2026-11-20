"""Growth dimension of the U_q(sl2) label space at the proton pin (issue #7895).

V(n) = sum_{m=1}^{n} [m]_q^2 (Plancherel volume of the label ball).  At q = 1,
V = n(n+1)(2n+1)/6 (growth dimension 3, Kirillov).  For q > 1 Lean
QOU.Optimization.QIntGrowth proves n <= [n]_q <= n q^(n-1) and V >= q^(2(n-1)).
This probe reports the local growth exponent d log V / d log n and the scale
1/log q where it leaves the cubic regime.  Also the rank and radical of the
H_3 trace form under convention D (the Gram nearness of GramNearness.lean).
Label space only; no physical-space claim.  mpmath 60 dps.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
           "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n, f_lambda  # noqa: E402

DPS = 60
set_compute_dps(DPS)


def qint(n, q):
    return mp.fsum(q ** (n - 1 - 2 * k) for k in range(n))


def main() -> int:
    t0 = time.time()
    mp.mp.dps = DPS
    q = Q_MP
    scale = 1 / mp.log(q)
    rows = []
    V = {0: mp.mpf(0)}
    for n in range(1, 61):
        V[n] = V[n - 1] + qint(n, q) ** 2
    print(f"q0 = {Q_50_DIGIT_STR[:20]}...   curvature length 1/log q0 = {mp.nstr(scale, 10)} labels")
    print(f"{'n':>3} {'[n]_q/n':>12} {'V(n)':>16} {'local exponent':>15}")
    for n in range(2, 61):
        expo = (mp.log(V[n]) - mp.log(V[n - 1])) / (mp.log(n) - mp.log(n - 1))
        r = {"n": n, "qint_over_n": fmt(qint(n, q) / n), "V": fmt(V[n]), "local_exponent": fmt(expo)}
        rows.append(r)
        if n in (2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 40, 60):
            print(f"{n:3d} {mp.nstr(qint(n, q) / n, 8):>12} {mp.nstr(V[n], 10):>16} {mp.nstr(expo, 6):>15}")
    # checks of the Lean bounds
    ok = all(n <= qint(n, q) <= n * q ** (n - 1) for n in range(1, 61))
    okV = all(V[n] >= mp.fsum((m) ** 2 for m in range(1, n + 1)) and V[n] >= q ** (2 * (n - 1)) for n in range(1, 61))
    # H_3 trace form rank under D: Gram on the Wedderburn basis has rank sum f^2 over y>0
    y = y_lambda_su_n(3, q, 2)
    rank = sum(f_lambda(tuple(lam)) ** 2 for lam, v in y.items() if mp.mpf(v) > mp.mpf("1e-40"))
    radical = 6 - rank
    print(f"\nH_3 trace form under D: rank {rank}, radical dimension {radical}")
    print(f"Lean bounds hold for n <= 60: qint {ok}, volume {okV}")
    print(f"  wall {time.time() - t0:.2f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("label-space-growth-probe", engine="python", start_time=t0)
    wb.set_description("Plancherel volume growth of the U_q(sl2) label ball at the proton pin: cubic "
                       "(growth dimension 3) below 1/log q, exponential above; checks Lean QIntGrowth "
                       "bounds; H_3 trace-form rank/radical under D. Label space only.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_data("curvature_length_labels", fmt(scale))
    wb.add_data("rows", rows)
    wb.add_data("h3_trace_form_rank_D", rank)
    wb.add_data("h3_radical_dim_D", radical)
    wb.add_assertion(name="qint_bounds_hold", computed=str(int(ok)), expected="1", tolerance="0",
                     source="Lean QIntGrowth.qint_ge_n, qint_le")
    wb.add_assertion(name="volume_floors_hold", computed=str(int(okV)), expected="1", tolerance="0",
                     source="Lean QIntGrowth.vol_ge_classical, vol_ge_exp")
    wb.add_assertion(name="h3_radical_is_sign_block", computed=str(radical), expected="1", tolerance="0",
                     source="RowCapObstruction: y_(1^3) = 0 at N = 2")
    out = wb.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
