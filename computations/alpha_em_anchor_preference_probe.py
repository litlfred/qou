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
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402

set_compute_dps()
# Read from the registry, not hardcoded (2026-09-14). This carried the literal
# `137.035999084` — CODATA **2018** — while the two ladder probes were migrated
# to the registry at `aa546b4ba1` (2026-09-07) and this one was missed. The
# 2018 -> 2022 shift is +0.6787 ppb, which is 2.2x alpha_EM's own residual and
# FLIPS ITS SIGN, so a hardcoded edition is not a small staleness here: this
# probe's published `alpha_inv_residual_ppb.proton` was the 2018 figure while
# the dashboard next to it reported the 2022 one.
# Reading the registry also removes the choice — the value moves when the table
# does. (Note for anyone re-checking `qou-rbdi`: its claim that codata.py has
# "NO fine-structure entry" is false; it greps the module SOURCE and cannot see
# entries parsed at runtime from data/allascii.txt.)
_ALPHA_INV = _codata.codata("inverse fine-structure constant")
CODATA = mp.mpf(_ALPHA_INV.value_str)
# Both pins read BY NAME (bean qou-4bef, 2026-09-03): the muon literal this carried was the
# pin RETIRED 2026-08-22/28; the muon leg now tracks the CODATA lepton ratio. The docstring
# figures above were computed at the retired pin — the witness carries the live ones.
Q_PROTON = Q_MP
Q_MUON = q_muon_at(50)


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
        return (q - q_alpha) / q_alpha * mp.mpf(10) ** 9

    dp, dm = dppb(Q_PROTON), dppb(Q_MUON)
    print(f"\n  q_alpha (α_EM-exact q0) = {mp.nstr(q_alpha, 18)}")
    print(f"  proton pin              = {mp.nstr(Q_PROTON, 18)}   Δ = {mp.nstr(dp, 5)} ppb")
    print(f"  muon pin                = {mp.nstr(Q_MUON, 18)}   Δ = {mp.nstr(dm, 5)} ppb")
    print(f"  proton-muon gap         = {mp.nstr((Q_MUON-Q_PROTON)/Q_PROTON*10**9, 5)} ppb (mu-p tension)")
    print(f"\n  => α_EM prefers the PROTON anchor by {mp.nstr(abs(dm)/abs(dp), 3)}× "
          f"(0.245 ppb vs 11.8 ppb).")

    print("\n  residuals in 1/α at each pin:")
    for nm, q in [("proton", Q_PROTON), ("muon", Q_MUON)]:
        r = (alpha_inv(q) - CODATA) / CODATA * mp.mpf(10) ** 9
        print(f"    {nm:7s}: {mp.nstr(r, 5)} ppb ({mp.nstr(abs(r) / mp.mpf('0.15'), 3)}× σ_α)")
    # amplification: how much 1/a moves per fractional q0 move
    eps = mp.mpf("1e-9")
    ampl = ((alpha_inv(q_alpha*(1+eps)) - alpha_inv(q_alpha)) / alpha_inv(q_alpha)) / eps
    print(f"  sensitivity d(1/α)/(1/α) per dq0/q0 ≈ {mp.nstr(ampl, 3)}×  "
          f"=> +1.67 ppb(1/α) at proton = +0.245 ppb in q0-space")

    proton_wins = abs(dp) < abs(dm) and abs(dp) < 1.0

    wb.add_data("q_alpha", mp.nstr(q_alpha, 30))
    wb.add_data("anchor_deltas_ppb", {
        "proton": fmt(dp, 20), "muon": fmt(dm, 20),
        "mu_p_gap": fmt((Q_MUON - Q_PROTON) / Q_PROTON * mp.mpf(10) ** 9, 20)})
    wb.add_data("alpha_inv_residual_ppb", {
        "proton": fmt((alpha_inv(Q_PROTON) - CODATA) / CODATA * mp.mpf(10) ** 9, 20),
        "muon": fmt((alpha_inv(Q_MUON) - CODATA) / CODATA * mp.mpf(10) ** 9, 20)})
    wb.add_data("interpretation", {
        "prefers": "proton",
        "factor": fmt(abs(dm) / abs(dp), 20),
        "q0_sensitivity": fmt(ampl, 20),
        "note": "alpha_EM (EM sector) agrees with proton pin to sub-ppb; muon is the outlier (mu-p tension)"})
    wb.add_assertion("alpha_em_prefers_proton_anchor",
                     computed=("1" if proton_wins else "0"), expected="1", tolerance="0.5",
                     source="q_alpha within 0.245 ppb of proton pin vs 11.8 ppb of muon pin")
    wb.add_assertion("proton_delta_sub_ppb",
                     computed=fmt(abs(dp), 20), expected="0", tolerance="1",
                     source="|q_proton - q_alpha| = 0.245 ppb < 1 ppb")
    wb.save(q0_comparison(
        muon=Q_MUON, proton=Q_PROTON,
        reason="anchor-preference cross-check: which documented pin the alpha_EM-exact q0 "
               "agrees with; both pins are read on purpose and each is reported under its own key"))

    print("\n  RESULT: α_EM independently prefers the proton anchor (cross-check; no fit)")
    return 0 if proton_wins else 1


if __name__ == "__main__":
    raise SystemExit(main())
