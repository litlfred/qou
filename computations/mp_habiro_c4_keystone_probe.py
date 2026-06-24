#!/usr/bin/env python3
"""
m_p term-6 Habiro residue c_4 — keystone characterization (bean ovud → s5bb).

Follow-up to PR #2691 (which proved F_Bor's `/q^3` is exact and located the
production m_p fit in the multiplicative `habiro_ratio`).  This probe
CHARACTERIZES the derivation target — the term-6 Habiro residue coefficient
`c_4` — with the same rigor the Q_β programme applies to its `c_k`, so the
s5-so3 keystone (beans s5bb) has a precise mass-sector target to hit.

Formalize-first (AGENTS.md §"Formalize-first probe discipline"): characterize
the target and prune the easy classes BEFORE any wide search.  Findings:

  1. The production `habiro_ratio = (1+46u^4)(1+4u^5)(1-29u^6)` is a
     ROUNDED-INTEGER fit.  Inverting the single-term model
     `m_p_codata / m_p_{F_Bor only} = 1 + c_4 u^4` gives

         required c_4 = 46.0319   (NOT the integer 46; off by 0.032)

     and the production "46" misses the true coefficient by 0.032 = 2.8x
     the proton-pin extraction floor (sigma_c4 = 0.011).

  2. EXTRACTION FLOOR.  With m_p known to ~0.06 ppb (proton pin),
     sigma_c_k = sigma_ratio / u^k gives sigma_c4 = 0.011, sigma_c5 = 1.34,
     sigma_c6 = 157.  So ONLY c_4 is data-determined; the production
     {4, 29} at u^5/u^6 are below the floor — cosmetic integers, not
     derived.  (Same structure as the Q_β ladder, where only c_2, c_3 are
     data-determined.)

  3. CROSS-ANCHOR.  required c_4 at the proton pin (46.0319) vs the muon
     pin (46.0336) swings 3.8e-5 (rel) — small, because both mass-ratio
     anchors pin q_0 to nearly the same value (the mu-p tension is large
     in sigma but tiny in absolute q).  The target is a genuine real-q
     object ~46.03, q-dependent.

  4. EASY-CLASS PRUNE.  A small principled scan of 1-2 factor categorical
     objects ([n]_q!, [n]_q[m]_q, tr_M(beta_Bor)-dressed products) finds
     NO clean hit (best target/[7]_q = 6.037, 0.6% off >> floor).  The
     target is not a simple categorical product — consistent with the
     saturated Q_β c_3 search (28 + 1281 candidates, all NEGATIVE).

Verdict (scope-limited, AGENTS.md): the production {46,4,29} is a rounded
fit; the true c_4 = 46.03 is the term-6 Habiro residue, whose first-
principles derivation is the SAME open Habiro-element problem as the Q_β
c_k ladder (s5bb keystone).  Nothing wired; production unchanged.

Witness: mp-habiro-c4-keystone-probe.witness.json
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, findroot

sys.path.insert(0, str(Path(__file__).parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_MU_MEV_VALIDATION  # noqa: E402
from m_p_substrate_identity_50dps import F_Bor, trM_borromean, qfact_three  # noqa: E402


def _u(q):
    hbar = ((q - 1) / q) ** 2
    b = ((q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2) ** mpf("0.5")
    return b * hbar


def required_c4(q):
    """Single-term inversion: c_4 s.t. m_p_codata/m_p_{F only} = 1 + c_4 u^4."""
    m_e = mpf(M_E_MEV)
    hbar = ((q - 1) / q) ** 2
    m_mu = m_e * vol_4_1_at(50) / hbar
    m_p_F = 2 * m_mu * F_Bor(q) - 12 * m_e
    return (mpf(M_P_MEV_VALIDATION) / m_p_F - 1) / _u(q) ** 4


def main() -> int:
    set_compute_dps()
    qp = mpf(Q_50_DIGIT_STR)
    m_e = mpf(M_E_MEV)

    # muon-pinned q_0
    V = vol_4_1_at(50)
    ratio_mu = mpf(M_MU_MEV_VALIDATION) / m_e
    qm = findroot(lambda q: V / ((q - 1) / q) ** 2 - ratio_mu, mpf("1.11"))

    c4p = required_c4(qp)
    c4m = required_c4(qm)
    swing = (c4p - c4m) / c4p

    u = _u(qp)
    # extraction floor at proton pin (0.06 ppb) and formula (0.0004 ppb)
    floors = {}
    for sig, lab in ((mpf("0.06e-9"), "proton_0.06ppb"),
                     (mpf("0.0004e-9"), "formula_0.0004ppb")):
        floors[lab] = {f"sigma_c{k}": mp.nstr(sig / u ** k, 6)
                       for k in (4, 5, 6)}

    print("m_p term-6 Habiro residue c_4 — keystone characterization")
    print(f"  required c_4 (proton pin) = {mp.nstr(c4p, 15)}")
    print(f"  required c_4 (muon pin)   = {mp.nstr(c4m, 15)}")
    print(f"  cross-anchor swing (rel)  = {mp.nstr(swing, 6)}")
    print(f"  vs production integer 46  : diff = {mp.nstr(c4p - 46, 8)} "
          f"(= {mp.nstr((c4p - 46) / (mpf('0.06e-9') / u ** 4), 4)} x proton floor)")
    print(f"  extraction floors         : {floors}")

    # easy-class candidate prune (1-2 factor categorical objects)
    def qint(n):
        return (qp ** n - qp ** (-n)) / (qp - 1 / qp)
    qf3 = qfact_three(qp)
    trM = trM_borromean(qp)
    cands = {
        "[3]_q!^2": qf3 ** 2,
        "[5]_q!/[2]_q": qint(5) * qint(4) * qint(3) * qint(2) / qint(2),
        "[7]_q*[6]_q": qint(7) * qint(6),
        "2*[3]_q!*[2]_q^2": 2 * qf3 * qint(2) ** 2,
        "trM*[3]_q!^2/q^3": trM * qf3 ** 2 / qp ** 3,
        "target/[7]_q": c4p / qint(7),
    }
    best = min(
        ((k, abs((v - c4p) / c4p)) for k, v in cands.items()
         if not k.startswith("target/")),
        key=lambda kv: kv[1],
    )
    print(f"  easy-class best           : {best[0]} at {mp.nstr(best[1], 4)} rel "
          f"(>> floor ⇒ no clean hit)")

    w = WitnessBuilder("mp-habiro-c4-keystone-probe", engine="mpmath")
    w.set_description(
        "Characterizes the m_p term-6 Habiro residue coefficient c_4 "
        "(the real target behind the production habiro_ratio {46,4,29}): "
        "required c_4 = 46.03 (q-dependent, NOT integer 46); {4,29} below "
        "the extraction floor (cosmetic); cross-anchor swing 3.8e-5; no "
        "clean 1-2 factor categorical hit. Derivation gated on the s5bb "
        "keystone (same open Habiro-element as Q_beta c_k). Nothing wired."
    )
    w.set_content_block("prop:markov-trace-axiomatic-closed-form")
    w.add_parameter("q_0_proton_pin", mp.nstr(qp, 50))
    w.add_parameter("q_0_muon_pin", mp.nstr(qm, 50))
    w.add_data("required_c4", {
        "proton_pin": mp.nstr(c4p, 30),
        "muon_pin": mp.nstr(c4m, 30),
        "cross_anchor_swing_rel": mp.nstr(swing, 12),
        "production_integer": 46,
        "diff_from_46": mp.nstr(c4p - 46, 12),
    })
    w.add_data("extraction_floor", floors)
    w.add_data("easy_class_scan", {
        k: mp.nstr(v, 12) for k, v in cands.items()
    })
    w.add_data("verdict", (
        "{46,4,29} is a rounded-integer fit; only c_4 (=46.03) is data-"
        "determined and it is q-dependent, not the integer 46. {4,29} are "
        "below the extraction floor. No 1-2 factor categorical object hits "
        "46.03. Deriving it is the term-6 Habiro residue = the s5bb "
        "keystone, shared with the Q_beta c_k ladder. Nothing wired."
    ))

    w.add_assertion(
        "c4_required_not_integer_46",
        computed=bool(abs(c4p - 46) > mpf("0.06e-9") / u ** 4),
        expected=True,
    )
    w.add_assertion(
        "c5_c6_below_extraction_floor",
        computed=bool(mpf("0.06e-9") / u ** 5 > 1),  # sigma_c5 > 1 ⇒ {4} not determined
        expected=True,
    )
    w.add_assertion(
        "no_clean_easy_class_hit",
        computed=bool(best[1] > mpf("1e-3")),
        expected=True,
    )
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
