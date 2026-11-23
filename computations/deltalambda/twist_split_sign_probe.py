#!/usr/bin/env python3
"""Sign of the spin-only twist split: deuteron vs singlet, cell by cell.

Companion to ``QOU/Hecke/TwistSplitSignDictionary.lean``.  ``framing_twist_channel_split_probe``
established ``D - S = (theta(4,2)^k - theta(3,3)^k) w42 w33`` and ``D/S = q^(2k)`` for a twist
acting on the spin factor only (k = 1 ribbon, k = 2 full twist), and verified exactly that the
POSITIVE full twist acts on the (4,2), (3,3) seminormal blocks by ``q^(2c)``.

Two inputs that decide whether the deuteron binds more are NOT fixed by the corpus:

  orientation  +1 : theta^k        (positive twist; Delta^2 for k = 2)
               -1 : theta^(-k)     (negative twist; Delta^-2)
  energy map   antitone : larger channel trace binds LESS   (direction of every working form:
                          B = -alpha ln mu, B_sym = alpha ln(tr_free/tr_atom) [POSITED],
                          mass facade m ~ |tr_M|)
               monotone : larger channel trace binds MORE

This probe evaluates all four cells, exactly.  Nothing is selected.  The comparison with
nature (deuteron bound, singlet unbound) is printed, LABELLED, and used for nothing.

Arithmetic: ``fractions.Fraction`` for the sign table at rational q; ``mpmath`` at
``mp.dps = 60`` at the proton-pinned ``q0`` (``q_parameter.Q_MP``).  No float in any
computation.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent.parent),
                str(Path(__file__).resolve().parent.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
C42, C33 = 5, 3          # content sums, contentSum_four_two / contentSum_three_three


def ocneanu(lam, qv, zv):
    """Frame-general Ocneanu weight (prop:markov-z-reconciliation), h = q - 1/q."""
    h = qv - 1 / qv
    num = den = mp.mpf(1)
    for i, r in enumerate(lam):
        for j in range(r):
            c = j - i
            arm = r - j - 1
            leg = sum(1 for rr in lam[i + 1:] if rr > j)
            hk = arm + leg + 1
            num *= zv * qv ** c - (zv - h) * qv ** (-c)
            den *= qv ** hk - qv ** (-hk)
    return num / den


def sign(x):
    return (x > 0) - (x < 0)


def cell_verdict(orient, energy):
    """+1: deuteron binds more; -1: binds less.  sign(D - S) = orient (q > 1, traces > 0)."""
    trace_sign = orient
    return trace_sign if energy == "monotone" else -trace_sign


def main() -> int:
    print("=" * 76)
    print("  SPIN-ONLY TWIST SPLIT -- WHICH CHANNEL BINDS MORE, PER CONVENTION CELL")
    print("=" * 76)

    # 1. exact sign of D - S at rational q > 1, with positive block traces (Fraction)
    table_ok = True
    for qv in (Fraction(11, 10), Fraction(3, 2)):
        for orient in (+1, -1):
            for k in (1, 2):
                s, s_ = qv ** (orient * k * C42), qv ** (orient * k * C33)
                w42, w33 = Fraction(2, 7), Fraction(5, 9)   # any positive pair
                D, S = s * w42 * w33, s_ * w33 * w42
                table_ok &= sign(D - S) == orient and D / S == qv ** (2 * orient * k)
    print(f"  exact (Fraction, q in {{11/10, 3/2}}): sign(D - S) = orientation, "
          f"D/S = q^(2*orient*k): {table_ok}")

    # 2. numbers at q0
    from q_parameter import Q_MP
    from codata_constants import M_E_MEV
    q0 = mp.mpf(Q_MP)
    h = q0 - 1 / q0
    zD = q0 ** 3 / (q0 ** 2 + 1)
    w42, w33 = ocneanu((4, 2), q0, zD), ocneanu((3, 3), q0, zD)
    traces_pos = w42 > 0 and w33 > 0
    print(f"\n  block traces at z_D: w(4,2) = {mp.nstr(w42, 20)}, w(3,3) = {mp.nstr(w33, 20)}"
          f"  (both > 0: {traces_pos})")
    me = mp.mpf(str(M_E_MEV))            # CODATA decimal, round-trips exactly
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(me, q0)         # E0, the alpha of the working log forms
    lnq = mp.log(q0)
    tol = mp.mpf(10) ** -50

    cells = []
    log_ok = True
    for orient in (+1, -1):
        for k, kname in ((1, "ribbon theta^(+-1)"), (2, "full twist Delta^(+-2)")):
            s, s_ = q0 ** (orient * k * C42), q0 ** (orient * k * C33)
            D, S = s * w42 * w33, s_ * w33 * w42
            # log working form B = -alpha ln(trace): Delta B = B_D - B_S = -alpha ln(D/S)
            dB_log = -alpha * mp.log(D / S)
            closed = -2 * orient * k * alpha * lnq
            log_ok &= abs(dB_log - closed) < tol
            for energy in ("antitone", "monotone"):
                v = cell_verdict(orient, energy)
                row = {
                    "orientation": "+" if orient > 0 else "-",
                    "twist": kname, "k": k, "energy_map": energy,
                    "D_over_S": mp.nstr(D / S, 30),
                    "sign_D_minus_S": sign(D - S),
                    "deuteron_binds": "more" if v > 0 else "less",
                }
                if energy == "antitone":
                    row["deltaB_log_form_over_alpha"] = mp.nstr(dB_log / alpha, 30)
                    row["deltaB_log_form_MeV"] = mp.nstr(dB_log, 30)
                cells.append(row)
                extra = (f"  Delta B(log) = {mp.nstr(dB_log, 12)} MeV = "
                         f"{mp.nstr(dB_log / alpha, 12)} alpha" if energy == "antitone" else "")
                print(f"  orient {row['orientation']} {kname:24s} {energy:8s}: D/S = "
                      f"{mp.nstr(D / S, 12)} -> deuteron binds {row['deuteron_binds']}{extra}")

    print(f"\n  log-form split = -2*orient*k*alpha*ln q0 to 1e-50: {log_ok}")
    print(f"  alpha = E0 = {mp.nstr(alpha, 20)} MeV; ln q0 = {mp.nstr(lnq, 20)}")
    print("\n  VERDICT: the sign is orientation x (energy-map direction). Neither factor is")
    print("  fixed by a corpus artifact, so the combined sign is NOT fixed.")
    print("\n  COMPARISON (labelled, selects nothing): AME2020 deuteron (S=1,T=0) bound,")
    print("  B = 2.224566 MeV; singlet (S=0,T=1) unbound. Matching cells: (-, antitone) and")
    print("  (+, monotone). Choosing a cell BECAUSE it matches would be selection against the")
    print("  target (AGENTS.md, NO FITTING).")

    w = WitnessBuilder("twist-split-sign", engine="mpmath+fraction",
                       output_dir=Path(__file__).resolve().parent)
    w.add_assertion("sign_table_exact_fraction", 1 if table_ok else 0, 1)
    w.add_assertion("block_traces_positive_at_zD", 1 if traces_pos else 0, 1)
    w.add_assertion("log_form_split_closed_form_1e-50", 1 if log_ok else 0, 1)
    w.add_parameter("q0", mp.nstr(q0, 50))
    w.add_parameter("q0_anchor", "proton (q_parameter.Q_MP)")
    w.add_parameter("mp_dps", str(mp.mp.dps))
    w.add_parameter("alpha_E0_MeV", mp.nstr(alpha, 40))
    w.add_parameter("w42_zD", mp.nstr(w42, 40))
    w.add_parameter("w33_zD", mp.nstr(w33, 40))
    w.add_parameter("verdict", "combined sign NOT fixed: orientation and trace->energy map "
                    "both unfixed by corpus artifacts")
    w.add_data("cells", cells)
    w.save()
    return 0 if (table_ok and traces_pos and log_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
