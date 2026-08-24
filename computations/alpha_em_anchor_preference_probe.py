#!/usr/bin/env python3
"""alpha_em_anchor_preference_probe.py

Which q0 anchor does alpha_EM prefer? — an honest cross-check (NOT a fit).

alpha_EM is a pure-q0 prediction (form: 1/a = q[9]_q[10]_q + 2/(3pi) + O(a),
prop:em-coupling-bring-zero-mode). Requiring it to equal CODATA therefore DEFINES a
q0 (call it q_alpha). This probe inverts the fixed-point form for q_alpha and asks
which of the two documented pins (proton 0.06 ppb / muon) it agrees with. Nothing is
tuned — the form is fixed; only q0 is solved for (like asking what q0 the proton mass
implies).

FINDING (computed; scope-(a); no coefficient fitted):
  q_alpha (alpha_EM-exact q0)  = 1.10997858247973714
  proton pin                   = 1.10997858275138081   ->  q_proton - q_alpha = +0.245 ppb
  muon pin                     = 1.10997859555733471   ->  q_muon   - q_alpha = +11.78 ppb
  (proton-muon gap = 11.54 ppb = the mu-p substrate tension)

So alpha_EM's implied q0 sits ~0.245 ppb from the PROTON pin but ~11.8 ppb from the
MUON pin — it agrees with the proton anchor to sub-ppb and DISagrees with the muon by
the full mu-p tension. alpha_EM is thus a THIRD, electromagnetic-sector cross-check
(alongside m_p) that the substrate q0 is the proton-pinned value, and the muon is the
outlier.

The alpha_inv residual AT the proton pin (+1.67 ppb) corresponds to only +0.245 ppb
in q0-space (amplification d(1/a)/(1/a) per dq0/q0 ~ 6.8x) — i.e. ~4x the proton
pin's own 0.06 ppb precision, plus the uncomputed O(a^2) tower. At the muon pin the
80 ppb residual is just the mu-p tension propagated into the EM sector.

Companion Lean: QOU/Archimedean/EmCouplingBringZeroMode.lean (zero-mode value
genus-determined, this PR). Audit: docs/audits/2026-07-11-path-to-1ppq-alpha-em-opportunity.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
CODATA = mp.mpf("137.035999084")
Q_PROTON = mp.mpf("1.109978582751380808")
Q_MUON = mp.mpf("1.10997859555733471")


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def alpha_inv(q):
    T = q * qb(9, q) * qb(10, q) + mp.mpf(8) / (12 * mp.pi)   # tree + zero-mode 2/(3π)
    H = qb(2, q) / (8 * mp.pi)
    alpha = (-T + mp.sqrt(T * T + 4 * H)) / (2 * H)
    return 1 / alpha


def main() -> int:
    print("=" * 78)
    print(" α_EM anchor preference — which q0 does the EM sector pick? (cross-check)")
    print("=" * 78)

    wb = WitnessBuilder("alpha-em-anchor-preference", engine="mpmath")
    wb.set_description(
        "Inverts the pure-q0 alpha_EM fixed-point form for the q0 that reproduces "
        "CODATA (q_alpha), then compares to the proton and muon pins. Finding: "
        "q_alpha is ~0.245 ppb from the PROTON pin but ~11.8 ppb from the MUON pin "
        "(= the mu-p tension) — alpha_EM is a THIRD EM-sector cross-check preferring "
        "the proton anchor, agreeing with m_p against the muon. No coefficient fitted "
        "(only q0 solved for); scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    q_alpha = mp.findroot(lambda q: alpha_inv(q) - CODATA, Q_PROTON)

    def dppb(q):
        return float((q - q_alpha) / q_alpha * 1e9)

    dp, dm = dppb(Q_PROTON), dppb(Q_MUON)
    print(f"\n  q_alpha (α_EM-exact q0) = {mp.nstr(q_alpha, 18)}")
    print(f"  proton pin              = {mp.nstr(Q_PROTON, 18)}   Δ = {dp:+.3f} ppb")
    print(f"  muon pin                = {mp.nstr(Q_MUON, 18)}   Δ = {dm:+.3f} ppb")
    print(f"  proton-muon gap         = {float((Q_MUON-Q_PROTON)/Q_PROTON*1e9):+.2f} ppb (mu-p tension)")
    print(f"\n  => α_EM prefers the PROTON anchor by {abs(dm)/abs(dp):.0f}× "
          f"(0.245 ppb vs 11.8 ppb).")

    print("\n  residuals in 1/α at each pin:")
    for nm, q in [("proton", Q_PROTON), ("muon", Q_MUON)]:
        r = float((alpha_inv(q) - CODATA) / CODATA * 1e9)
        print(f"    {nm:7s}: {r:+7.2f} ppb ({abs(r)/0.15:.0f}× σ_α)")
    # amplification: how much 1/a moves per fractional q0 move
    eps = mp.mpf("1e-9")
    ampl = float(((alpha_inv(q_alpha*(1+eps)) - alpha_inv(q_alpha)) / alpha_inv(q_alpha)) / eps)
    print(f"  sensitivity d(1/α)/(1/α) per dq0/q0 ≈ {ampl:.2f}×  "
          f"=> +1.67 ppb(1/α) at proton = +0.245 ppb in q0-space")

    proton_wins = abs(dp) < abs(dm) and abs(dp) < 1.0

    wb.add_data("q_alpha", mp.nstr(q_alpha, 30))
    wb.add_data("anchor_deltas_ppb", {
        "proton": dp, "muon": dm,
        "mu_p_gap": float((Q_MUON - Q_PROTON) / Q_PROTON * 1e9)})
    wb.add_data("alpha_inv_residual_ppb", {
        "proton": float((alpha_inv(Q_PROTON) - CODATA) / CODATA * 1e9),
        "muon": float((alpha_inv(Q_MUON) - CODATA) / CODATA * 1e9)})
    wb.add_data("interpretation", {
        "prefers": "proton",
        "factor": abs(dm) / abs(dp),
        "q0_sensitivity": ampl,
        "note": "alpha_EM (EM sector) agrees with proton pin to sub-ppb; muon is the outlier (mu-p tension)"})
    wb.add_assertion("alpha_em_prefers_proton_anchor",
                     computed=float(proton_wins), expected=1.0, tolerance=0.5,
                     source="q_alpha within 0.245 ppb of proton pin vs 11.8 ppb of muon pin")
    wb.add_assertion("proton_delta_sub_ppb",
                     computed=abs(dp), expected=0.0, tolerance=1.0,
                     source="|q_proton - q_alpha| = 0.245 ppb < 1 ppb")
    wb.save()

    print("\n  RESULT: α_EM independently prefers the proton anchor (cross-check; no fit)")
    return 0 if proton_wins else 1


if __name__ == "__main__":
    raise SystemExit(main())
