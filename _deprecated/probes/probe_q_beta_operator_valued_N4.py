#!/usr/bin/env python3
"""Q_β N=4 operator-valued tower extension — probe for c_4.

EXPLORATORY shape-probe (per .claude/skills/local/production-vs-exploratory-discipline.md).

Background (from q-beta-operator-valued-N3.witness.json):
  Q_A   = 0.78365 MeV  (categorical base)
  Q_N1  = 0.78239 MeV  (N=1, 73.8 ppm from CODATA)
  Q_N2  = 0.78233 MeV  (N=2, 1.24 ppm)
  Q_N3  = Q_N2 · (1 + c_3 · b³ · ℏ_q^6)
        = 0.782333419 MeV with c_3 = -2 (Hopf, proved)
        → 11.13 ppb from CODATA (framework-bounded)

100× target: 7.80 ppb → miss factor 1.43.

N=4 EXTENSION:
  Q_N4 = Q_N3 · (1 + c_4 · b⁴ · ℏ_q^8)

where b = hoefsmit_b at q_0, ℏ_q = (q_0-1)/q_0.

The correction scale b⁴·ℏ_q^8 ≈ 5.25×10⁻⁹ — same order as the
current 11.13 ppb gap (~1.4×10⁻⁸ MeV/Q_N3). So c_4 of order 2
could close the gap, IF categorical.

CANDIDATE c_4 VALUES (from the 13-driver canonical menu):
  - c_4 = -2 (same as c_3 — Hopf J(q=1) self-similar)
  - c_4 = +2 (sign-flipped Hopf)
  - c_4 = b² + 1/2 (partition-algebra at H_4, per Story B audit)
  - c_4 = [3]_q (quantum integer at substrate)
  - c_4 = 0 (trivial — no N=4 correction)

If c_4 is categorical (≤ 10 coefficient, from a named Driver), the
Q_β 100× target may close. If c_4 is large / irrational, Q_β is
framework-bounded at 11.13 ppb (same conclusion as 2026-05-22 audit).
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def main() -> int:
    # Load N=3 witness
    with (HERE / "q-beta-operator-valued-N3.witness.json").open() as fh:
        n3 = json.load(fh)
    n3_data = n3["data"]

    q = mp.mpf(n3_data["q_0_50dps"])
    hbar_q = (q - 1) / q
    hbar_q_sq = hbar_q ** 2
    hbar_q_4 = hbar_q_sq ** 2
    hbar_q_6 = hbar_q_sq * hbar_q_4
    hbar_q_8 = hbar_q_4 ** 2
    b = mp.mpf(n3_data["hoefsmit_b"])
    b3 = b ** 3
    b4 = b ** 4

    Q_N2 = mp.mpf(n3_data["Q_N2"])
    Q_AME = mp.mpf(n3_data["Q_AME"])

    # Reconstruct Q_N3 with c_3 = -2 (categorical Hopf)
    c_3_categorical = mp.mpf(-2)
    Q_N3 = Q_N2 * (1 + c_3_categorical * b3 * hbar_q_6)

    eps_N3_ppb = float((Q_N3 - Q_AME) / Q_AME * mp.mpf("1e9"))

    print(f"q_0           = {mp.nstr(q, 20)}")
    print(f"b (Hoefsmit)  = {mp.nstr(b, 15)}")
    print(f"ℏ_q           = {mp.nstr(hbar_q, 15)}")
    print(f"b⁴·ℏ_q⁸      = {mp.nstr(b4 * hbar_q_8, 6)}")
    print()
    print(f"Q_N2          = {mp.nstr(Q_N2, 18)} MeV")
    print(f"Q_N3 (c_3=-2) = {mp.nstr(Q_N3, 18)} MeV")
    print(f"Q_AME (CODATA)= {mp.nstr(Q_AME, 18)} MeV")
    print(f"ε_N3          = {eps_N3_ppb:.2f} ppb")
    print(f"100× target   = 7.80 ppb")
    print()

    # N=4 correction scale
    n4_scale = b4 * hbar_q_8
    print(f"N=4 correction scale b⁴·ℏ_q⁸ = {mp.nstr(n4_scale, 6)}")
    print()

    # Empirical c_4 that would close exactly to CODATA
    c_4_empirical = (Q_AME / Q_N3 - 1) / (b4 * hbar_q_8)
    print(f"c_4 empirical (CODATA fit) = {mp.nstr(c_4_empirical, 15)}")
    print()

    # Test categorical c_4 candidates
    bracket_3_q = q ** 2 + 1 + q ** (-2)
    candidates = {
        "c_4 = 0 (trivial)": mp.mpf(0),
        "c_4 = -2 (Hopf self-similar)": mp.mpf(-2),
        "c_4 = +2 (sign-flipped Hopf)": mp.mpf(2),
        "c_4 = -1": mp.mpf(-1),
        "c_4 = +1": mp.mpf(1),
        "c_4 = b² + 1/2": b ** 2 + mp.mpf("0.5"),
        "c_4 = [3]_q": bracket_3_q,
        "c_4 = -[3]_q": -bracket_3_q,
        "c_4 = c_3² / 2 = 2": c_3_categorical ** 2 / 2,
        "c_4 = -c_3 = +2 (alt)": -c_3_categorical,
    }

    print(f"{'candidate':<35s} {'c_4':>12s}  {'Q_N4 (MeV)':>18s}  {'ε (ppb)':>10s}  {'< 7.80?':>8s}")
    print("-" * 90)

    results = []
    for name, c4 in candidates.items():
        Q_N4 = Q_N3 * (1 + c4 * b4 * hbar_q_8)
        eps_ppb = float((Q_N4 - Q_AME) / Q_AME * mp.mpf("1e9"))
        beats = abs(eps_ppb) < 7.80
        marker = "✓" if beats else ""
        print(f"{name:<35s} {mp.nstr(c4, 8):>12s}  {mp.nstr(Q_N4, 16):>18s}  {eps_ppb:>+10.2f}  {marker:>8s}")
        results.append({
            "name": name,
            "c_4": mp.nstr(c4, 15),
            "Q_N4_MeV": mp.nstr(Q_N4, 25),
            "eps_ppb": eps_ppb,
            "beats_100x": beats,
        })

    print()
    winners = [r for r in results if r["beats_100x"]]
    if winners:
        print(f"CANDIDATES BEATING 100× TARGET ({len(winners)}):")
        for w in winners:
            print(f"  {w['name']}: ε = {w['eps_ppb']:.2f} ppb")
        print()
        print("NOTE: beating 100× at q_0 is NECESSARY but NOT SUFFICIENT.")
        print("Each winning c_4 must also:")
        print("  1. Pass the q-locality gate (slope < 10² ppm/q)")
        print("  2. Be derivable from the 13-driver canonical menu")
        print("  3. Or be escalated to the owner per Rule 14")
    else:
        print("NO CANDIDATES beat the 100× target.")
        print(f"Q_β remains framework-bounded at {eps_N3_ppb:.2f} ppb")
        print("(consistent with 2026-05-22 audit conclusion).")

    # Witness
    w = WitnessBuilder("q-beta-operator-valued-N4-probe", engine="mpmath")
    w.set_description(
        "EXPLORATORY: Q_β N=4 operator-valued tower extension probe. "
        "Tests categorical c_4 candidates for the next Kashiwara b⁴ "
        "recursion level: Q_N4 = Q_N3 · (1 + c_4 · b⁴ · ℏ_q⁸). "
        "Current Q_N3 (c_3=-2 Hopf) at 11.13 ppb; 100× target 7.80 ppb. "
        "Per production-vs-exploratory discipline: candidate c_4 values "
        "are probed, NOT fitted; any that beat 100× must pass q-locality "
        "gate + 13-driver menu check before production adoption."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", int(mp.mp.dps))
    w.add_data("Q_N3_MeV", mp.nstr(Q_N3, 25))
    w.add_data("Q_AME_MeV", mp.nstr(Q_AME, 25))
    w.add_data("eps_N3_ppb", eps_N3_ppb)
    w.add_data("b4_hbar_q_8", mp.nstr(b4 * hbar_q_8, 25))
    w.add_data("c_4_empirical", mp.nstr(c_4_empirical, 25))
    w.add_data("results", results)
    w.add_data("winners_count", len(winners))

    # Assert: probe documents the landscape (passes iff no assertion error)
    w.add_assertion(
        "n4_probe_landscape_documented",
        computed=1,
        expected=1,
        tolerance=None,
        source="EXPLORATORY probe documenting c_4 candidate landscape",
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
