"""chi_(1^3) of the nucleon words, and their Markov traces under N = 2 (convention D)
and N = 3 (the SU(3) member of the Ocneanu family, y_lambda_su_n).

Issue #7895 follow-up.  Measuring only: convention D is unchanged.  Under N = 2
the (1^3) block has y = 0 (RowCapObstruction.lean); under N = 3 it is the
1-dimensional Lambda^3(C^3) (epsilon_ijk) channel.  Proton pin, mpmath 60 dps.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python", "computations/substrate",
           "computations/hecke", "computations", "computations/probes"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402
from gamma_gamma_h3_psd_selector_probe import nucleon_block, vertex_pow, word_image, trace  # noqa: E402

DPS = 60
set_compute_dps(DPS)


def main() -> int:
    t0 = time.time()
    mp.mp.dps = DPS
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    cache = BlockCacheMP(q, h)
    parts = [tuple(p) for p in partitions_of(3)]
    reps = {lam: seminormal_matrices_mp(lam, cache=cache) for lam in parts}
    yN = {N: {tuple(k): mp.mpf(v) for k, v in y_lambda_su_n(3, q, N).items()} for N in (2, 3)}
    sig111 = reps[(1, 1, 1)][0][0][0, 0]
    words = {"proton block": nucleon_block("p", h), "neutron block": nucleon_block("n", h),
             "B_3 = V^3": vertex_pow(0, 3, h), "V": vertex_pow(0, 1, h)}
    print(f"sign block: sigma acts by {mp.nstr(sig111, 15)}  (-1/q = {mp.nstr(-1/q, 15)})")
    for N in (2, 3):
        print(f"y_lambda N={N}: " + ", ".join(f"{lam}: {mp.nstr(yN[N][lam], 12)}" for lam in parts))
    rows = []
    for name, w in words.items():
        ch = {}
        for lam in parts:
            s, dim, _ = reps[lam]
            ch[lam] = trace(word_image(s, dim, w), dim)
        tr = {N: mp.fsum(yN[N][lam] * ch[lam] for lam in parts) for N in (2, 3)}
        share3 = yN[3][(1, 1, 1)] * ch[(1, 1, 1)] / tr[3]
        crossings = len(w)
        rows.append({"word": name, "crossings": crossings,
                     "chi": {str(l): fmt(ch[l]) for l in parts},
                     "trM_N2": fmt(tr[2]), "trM_N3": fmt(tr[3]), "sign_share_N3": fmt(share3)})
        print(f"\n{name} ({crossings} letters)")
        print("  chi: " + ", ".join(f"{lam}: {mp.nstr(ch[lam], 12)}" for lam in parts))
        print(f"  tr_M N=2: {mp.nstr(tr[2], 15)}   N=3: {mp.nstr(tr[3], 15)}   (1^3) share of N=3 trace: {mp.nstr(share3, 6)}")
    print(f"\n  wall {time.time() - t0:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    wb = WitnessBuilder("nucleon-sign-block-n3-probe", engine="python", start_time=t0)
    wb.set_description("chi_(1^3) of nucleon words and their Markov traces under N=2 (convention D) "
                       "and N=3 (y_lambda_su_n). Measurement only; convention D unchanged.")
    wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_parameter("dps", DPS)
    wb.add_data("y_lambda_N2", {str(l): fmt(yN[2][l]) for l in parts})
    wb.add_data("y_lambda_N3", {str(l): fmt(yN[3][l]) for l in parts})
    wb.add_data("rows", rows)
    wb.add_assertion(name="N2_sign_weight_zero", computed=fmt(yN[2][(1, 1, 1)]), expected="0",
                     tolerance="1e-50", source="RowCapObstruction.lean")
    wb.add_assertion(name="sign_block_generator_is_minus_inverse_q", computed=fmt(sig111 + 1 / q),
                     expected="0", tolerance="1e-50", source="Hoefsmit seminormal form, one-row column")
    out = wb.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
