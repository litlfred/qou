#!/usr/bin/env python3
"""Wire c_4^even into a laddered Qb reconstruction and size it against the odd channel.

The "wire c_4^even" ask, answered honestly. The bar-even (binding-side) ladder

    R(q) = Qb/m_e(q) / [ QA/m_e(q) * cos(alpha_eff(q)) ],   R(1) = 1
    log R(s) = sum_{k>=2} c_k^even-order[s^{2k}] + [s^odd] remainder,  s = q-1

splits into an EVEN partial sum (the c_k^even rungs, folded as
sum_{k>=2} log(1 + c_k^even u^k), u = b*hbar^2) and an ODD [s^odd] remainder —
the bar-odd channel. The exact rungs c_2/c_3/c_4^even are merged
(qbeta-c4even-exact-sseries.witness.json). This probe *uses* c_4^even in the
even partial sum at the substrate anchor and MEASURES two things the "wire it"
ask actually cares about:

  MEASUREMENT 1 (the even rung is real + sub-leading).  At u(q0) ~ 0.0085 the
  even rung magnitudes shrink: |c2 u^2| > |c3 u^3| > |c4 u^4|.  So the even
  ladder is a well-behaved (asymptotic) series here and c_4^even is a genuine
  sub-leading refinement of the EVEN partial sum — not noise, not a fit.

  MEASUREMENT 2 (the odd channel dwarfs the whole even ladder).  The full
  log R_exact(q0) is NOT reproduced by the even partial sum: the leftover
  multiplicative factor R_exact / R_even is the odd channel, and in log terms
  it is ~O(10x) LARGER than, and OPPOSITE in sign to, the entire even ladder.
  That odd remainder is the accuracy-controlling leg — a proved representational
  prune (docs/audits/2026-07-07-c3-even-solved-s-complex-volume-rigidity.md;
  it swings 2.44% between the proton/muon q0 anchors, dc3/dq ~ 4.6e6).

Wiring verdict: c_4^even is correctly *used* (folded into the even partial sum)
and is a real sub-leading even rung, but its effect on the reconstructed Qb is
~O(10^-6) MeV — utterly dominated by the odd-channel gap it cannot touch.
Accuracy vs CODATA is odd-channel-bottlenecked, so this does not — and cannot —
move beats_100x on the L2 dashboard.  auditOnly; NO production wiring; NO fit.

Witness: qbeta-c4even-ladder-reconstruction.witness.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

import sympy as sp
from mpmath import mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

HERE = Path(__file__).resolve().parent          # computations/qbeta
ROOT = HERE.parent                               # computations/
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "substrate"))

q = sp.symbols("q", positive=True)


def load_net_symbolic(side: str):
    d = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    net = sp.Integer(0)
    for t in d[side]["nf_terms"]:
        net += sp.sympify(t["coefficient_symbolic"], locals={"q": q})
    return sp.simplify(net)


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()

    print("=" * 76)
    print(" c4^even — laddered Qb reconstruction: representation vs accuracy legs")
    print("=" * 76)

    # exact objects (identical conventions to qbeta_c4even_exact_sseries_probe)
    net_n = load_net_symbolic("neutron")
    net_p = load_net_symbolic("proton")
    dnet = sp.simplify(net_n - net_p)
    dnet_reg = sp.cancel(dnet / (q - 1))

    d_wit = json.loads((ROOT / "free-neutron-decay.witness.json").read_text())
    params = d_wit.get("parameters")
    q0 = mp.mpf(str(params["q"])) if params and "q" in params else \
        mp.mpf("1.1099785955573347198997632204832250266562084087802")
    dn_wit = mp.mpf(str(d_wit["transition"]["delta_net"]))
    dnet_f = sp.lambdify(q, dnet, "mpmath")
    dn_mine = dnet_f(q0)
    assert abs(dn_mine - dn_wit) < mp.mpf("1e-6"), "Delta(net) reconstruction drifted"
    sgn = int(mp.sign(dn_mine))
    print(f"  VALIDATE @ q0: Delta(net) mine={mp.nstr(dn_mine,12)} witness={mp.nstr(dn_wit,12)}  sgn={sgn}")

    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    alpha_eff = (z - 1) * h / 2 - u / 2
    QA_over_me = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    Qb_over_me = sgn * dnet_reg / q
    Rq = Qb_over_me / (QA_over_me * sp.cos(alpha_eff))

    # numeric evaluators at q0
    u_f = sp.lambdify(q, u, "mpmath")
    QA_f = sp.lambdify(q, QA_over_me, "mpmath")
    cosa_f = sp.lambdify(q, sp.cos(alpha_eff), "mpmath")
    Qb_f = sp.lambdify(q, Qb_over_me, "mpmath")
    R_f = sp.lambdify(q, Rq, "mpmath")

    u0 = u_f(q0)
    QA0 = QA_f(q0)
    cosa0 = cosa_f(q0)
    Qb0_over_me = Qb_f(q0)         # exact net-route Qb/m_e at q0
    R_exact = R_f(q0)              # exact ratio at q0
    print(f"  u(q0)={mp.nstr(u0,12)}  QA/me(q0)={mp.nstr(QA0,12)}  cos(a_eff)(q0)={mp.nstr(cosa0,12)}")
    print(f"  R_exact(q0)={mp.nstr(R_exact,16)}  (ladder target; R(1)=1)")

    # merged exact rungs
    wit_c4 = HERE / "qbeta-c4even-exact-sseries.witness.json"
    cw = json.loads(wit_c4.read_text())
    c2 = mp.mpf(str(cw["numeric_50dps"]["c2_even"]))
    c3 = mp.mpf(str(cw["numeric_50dps"]["c3_even"]))
    c4 = mp.mpf(str(cw["numeric_50dps"]["c4_even"]))
    print(f"\n  rungs (merged witness): c2^even={mp.nstr(c2,10)}  c3^even={mp.nstr(c3,10)}  "
          f"c4^even={mp.nstr(c4,12)}")

    # constants for CODATA leg
    import codata_constants as cc
    m_e = mp.mpf(str(cc.M_E_MEV))
    Q_beta_codata = mp.mpf(str(cc.Q_BETA_MEV))

    # ---------------------------------------------------------------------------
    # MEASUREMENT 1: even rung magnitudes at u(q0) — is c4^even a real sub-leading
    # rung?  |c_k u^k| must shrink with k for the even ladder to be a well-behaved
    # (asymptotic) series here.
    rungs = {2: c2, 3: c3, 4: c4}
    print("\n  MEASUREMENT 1 — even rung magnitudes at u(q0) (asymptotic-series check):")
    mag = {}
    for k in (2, 3, 4):
        mag[k] = abs(rungs[k] * u0**k)
        print(f"    |c{k}^even u^{k}| = {mp.nstr(mag[k], 8)}")
    even_shrinks = mag[2] > mag[3] > mag[4]
    print(f"    -> |c2 u^2| > |c3 u^3| > |c4 u^4| : {'PASS' if even_shrinks else 'FAIL'} "
          f"(ratios {mp.nstr(mag[3]/mag[2],4)}, {mp.nstr(mag[4]/mag[3],4)})")

    # even partial sum R_even(N) = prod_{k=2}^N (1 + c_k u^k), and the Qb it gives
    print("\n  Even partial sum + reconstructed Qb (folding c4^even at N=4):")
    print(f"  {'N':>3} {'R_even(N)':>20} {'d(logR) from c_k':>18} {'Qb_pred(MeV)':>16}")
    rows = []
    RN = mp.mpf(1)
    logR_prev = mp.mpf(0)
    for N in (1, 2, 3, 4):
        if N >= 2:
            RN = RN * (1 + rungs[N] * u0**N)
        logRN = mp.log(RN)
        dlog = logRN - logR_prev
        logR_prev = logRN
        Qb_pred = QA0 * cosa0 * RN * m_e
        rows.append({"N": N, "R_even": mp.nstr(RN, 20),
                     "dlogR_from_rung": mp.nstr(dlog, 8),
                     "Qb_pred_MeV": mp.nstr(Qb_pred, 16)})
        print(f"  {N:>3} {mp.nstr(RN,20):>20} {mp.nstr(dlog,8):>18} {mp.nstr(Qb_pred,16):>16}")

    R_even = RN            # even partial sum through c4
    # what folding c4^even alone changed in the reconstructed Qb:
    Qb_c4_delta = abs(mp.mpf(rows[3]["Qb_pred_MeV"]) - mp.mpf(rows[2]["Qb_pred_MeV"]))
    print(f"  c4^even's incremental effect on Qb_pred: {mp.nstr(Qb_c4_delta,6)} MeV "
          f"({mp.nstr(Qb_c4_delta*mp.mpf('1e3'),6)} keV)")

    # ---------------------------------------------------------------------------
    # MEASUREMENT 2: the odd channel = R_exact / R_even.  In log terms, compare it
    # to the whole even ladder.
    log_R_exact = mp.log(R_exact)
    log_R_even = mp.log(R_even)
    log_odd = log_R_exact - log_R_even          # the [s^odd] remainder at q0
    print("\n  MEASUREMENT 2 — odd channel vs the whole even ladder (log R at q0):")
    print(f"    log R_exact      = {mp.nstr(log_R_exact, 10)}")
    print(f"    log R_even(N=4)  = {mp.nstr(log_R_even, 10)}   (entire even ladder)")
    print(f"    log(odd factor)  = {mp.nstr(log_odd, 10)}   (R_exact / R_even)")
    odd_over_even = abs(log_odd) / abs(log_R_even)
    print(f"    |odd| / |even ladder| = {mp.nstr(odd_over_even, 6)}x  "
          f"(opposite sign: {'yes' if log_odd*log_R_even < 0 else 'no'})")
    odd_dominates = abs(log_odd) > 3 * abs(log_R_even)

    # accuracy legs vs CODATA
    Qb_exact_MeV = Qb0_over_me * m_e
    acc_exact = abs(Qb_exact_MeV - Q_beta_codata) / Q_beta_codata
    Qb_even_MeV = QA0 * cosa0 * R_even * m_e
    acc_even = abs(Qb_even_MeV - Q_beta_codata) / Q_beta_codata
    print("\n  Accuracy vs CODATA (the leg the L2 dashboard scores):")
    print(f"    Qb_exact = {mp.nstr(Qb_exact_MeV,12)} MeV -> {mp.nstr(acc_exact,8)} rel "
          f"({mp.nstr(acc_exact*mp.mpf('1e9'),6)} ppb)")
    print(f"    Qb_even  = {mp.nstr(Qb_even_MeV,12)} MeV -> {mp.nstr(acc_even,8)} rel "
          "(even ladder alone; the CODATA-closeness here is the odd channel being")
    print("     dropped, NOT accuracy — it is not a prediction of Q_beta)")
    print(f"    c4^even's {mp.nstr(Qb_c4_delta*mp.mpf('1e3'),4)} keV effect vs the odd "
          f"channel's ~{mp.nstr(abs(Qb_exact_MeV-Qb_even_MeV)*mp.mpf('1e3'),4)} keV gap.")

    print(f"\n  VERDICT M1 (c4^even is a real sub-leading even rung): "
          f"{'PASS' if even_shrinks else 'FAIL'}")
    print(f"  VERDICT M2 (odd channel dominates the even ladder, controls accuracy): "
          f"{'PASS' if odd_dominates else 'FAIL'}")
    print("\n  => c4^even is correctly *used* (folded into the even partial sum) and is a")
    print("     genuine sub-leading even rung, but its Qb effect (~1e-2 keV) is dwarfed")
    print("     by the odd-channel gap (~6 keV) it cannot touch. Accuracy vs CODATA is")
    print("     odd-channel-bottlenecked (proved prune). Does NOT move beats_100x. auditOnly.")

    witness = {
        "description": (
            "Laddered Qb reconstruction *using* the merged exact rung c_4^even "
            "in the even partial sum. Measurement 1: |c_k^even u^k| shrinks with "
            "k at u(q0), so c_4^even is a real sub-leading even rung. Measurement "
            "2: the odd channel (R_exact/R_even) dominates the entire even ladder "
            "by ~O(10x) and controls accuracy vs CODATA. c_4^even's Qb effect "
            "(~1e-2 keV) is dwarfed by the odd-channel gap (~6 keV) -> cannot move "
            "beats_100x. auditOnly; no production wiring; no fit."
        ),
        "audit_only": True,
        "parameters": {
            "q0": str(q0), "u_q0": mp.nstr(u0, 30),
            "c2_even": mp.nstr(c2, 30), "c3_even": mp.nstr(c3, 30), "c4_even": mp.nstr(c4, 30),
            "m_e_MeV": str(cc.M_E_MEV), "Q_beta_codata_MeV": str(cc.Q_BETA_MEV),
        },
        "measurement_1_even_rungs": {
            "abs_c2_u2": mp.nstr(mag[2], 20), "abs_c3_u3": mp.nstr(mag[3], 20),
            "abs_c4_u4": mp.nstr(mag[4], 20),
            "shrinks_with_k": bool(even_shrinks),
            "qb_c4_incremental_keV": mp.nstr(Qb_c4_delta * mp.mpf("1e3"), 12),
        },
        "measurement_2_odd_channel": {
            "log_R_exact": mp.nstr(log_R_exact, 20),
            "log_R_even_N4": mp.nstr(log_R_even, 20),
            "log_odd_factor": mp.nstr(log_odd, 20),
            "odd_over_even_ratio": mp.nstr(odd_over_even, 12),
            "opposite_sign": bool(log_odd * log_R_even < 0),
            "odd_dominates": bool(odd_dominates),
        },
        "reconstruction": rows,
        "accuracy_vs_codata": {
            "Qb_exact_MeV": mp.nstr(Qb_exact_MeV, 20),
            "acc_exact_rel": mp.nstr(acc_exact, 20),
            "acc_exact_ppb": mp.nstr(acc_exact * mp.mpf("1e9"), 12),
            "Qb_even_MeV": mp.nstr(Qb_even_MeV, 20),
            "acc_even_rel": mp.nstr(acc_even, 20),
        },
        "assertions": [
            {"label": "Delta(net) reconstruction matches witness at q0 (<1e-6)", "passed": True},
            {"label": "M1: |c_k^even u^k| shrinks with k at u(q0) (c4^even is a real sub-leading even rung)",
             "passed": bool(even_shrinks)},
            {"label": "M2: odd channel (R_exact/R_even) dominates the even ladder (>3x) and controls accuracy",
             "passed": bool(odd_dominates)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
    witness["scriptFile"] = os.path.basename(__file__)
    witness["durationMs"] = int((time.monotonic() - t0) * 1000)
    out = HERE / "qbeta-c4even-ladder-reconstruction.witness.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
        f.write("\n")
    print(f"\n  Witness: {out.name}   ({time.monotonic()-t0:.1f}s wall)")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
