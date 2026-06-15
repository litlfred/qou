"""m_n standard-channel correction probe — followup to PR #1654 Item A.

Item A finding: X(q) = ℏ_q²·h·[2]_q IS algebraically the (P_trivial +
P_sign) 1-dim-block Plancherel sum at H_3. The 0.10% residual is the
missing STANDARD channel (P_(2,1) = 4/6) piece.

This probe tests candidate forms for the standard-channel addition.

## Setup

  Δ_extra = target - X(q)  [the unexplained piece]
  Hypothesis: Δ_extra = P_(2,1) · (categorical piece)
              = (4/6) · (??)

## Cross-references

- PR #1654 Item A (mn_flavor_split_h3_plancherel.py)
- prop:flavor-split-substrate
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import ALPHA_EM, M_E_MEV, M_P_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
import experimental_constants as _ec  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("m_n flavor-split STANDARD channel correction probe")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    M_N_MEV = M_P_MEV + M_E_MEV + mp.mpf(repr(_ec.Q_NEUTRON_MEV))
    M_N_avg = (M_P_MEV + M_N_MEV) / 2
    target = (M_N_MEV - M_P_MEV) / M_N_avg

    # Baseline
    X_baseline = (q - 1) ** 2 * (1 - q ** (-4)) / 3

    # Extra needed
    delta_extra = target - X_baseline
    print(f"[Setup]")
    print(f"  target              = {mp.nstr(target, 18)}")
    print(f"  X(q) baseline       = {mp.nstr(X_baseline, 18)}")
    print(f"  Δ_extra = target - X = {mp.nstr(delta_extra, 18)}")

    # Standard-channel Plancherel weight
    P_standard = mp.mpf(4) / 6
    standard_piece = delta_extra / P_standard
    print(f"  P_(2,1) (standard)  = 4/6")
    print(f"  Δ_extra / P_standard = (categorical piece needed) = {mp.nstr(standard_piece, 18)}")

    # Substrate
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    q2 = q + 1 / q
    G = mp.catalan

    # Candidates for the categorical piece needed
    candidates = [
        # EM-correction-related
        ("(a) (α_em/π) · h⁴", ALPHA_EM / mp.pi * h ** 4),
        ("(b) (α_em/π) · h⁴ / 2", ALPHA_EM / mp.pi * h ** 4 / 2),
        ("(c) (α_em/π) · ℏ_q⁴", ALPHA_EM / mp.pi * hbar_q ** 4),
        ("(d) (α_em/π) · ℏ_q² · h²", ALPHA_EM / mp.pi * hbar_q_sq * h2),
        ("(e) (α_em/π) · ℏ_q · h³", ALPHA_EM / mp.pi * hbar_q * h ** 3),
        # Pure substrate (no α_em)
        ("(f) h⁴ / dim H_3", h ** 4 / 6),
        ("(g) h⁴ · G / (8π)", h ** 4 * G / (8 * mp.pi)),
        ("(h) h⁴ / (4·[2]_q)", h ** 4 / (4 * q2)),
        ("(i) ℏ_q⁴", hbar_q ** 4),
        ("(j) ℏ_q²·h²/4", hbar_q_sq * h2 / 4),
        # Bare h-power for reference
        ("(k) h⁴", h ** 4),
        ("(l) h⁶", h ** 6),
        # Standard-rep specific
        ("(m) [2]_q²/dim_q V_(2,1) · h⁴",
         q2 ** 2 / q2 * h ** 4),  # = q2 · h⁴
    ]

    print(f"\n[Candidates for standard-channel categorical piece]")
    print(f"  target = {mp.nstr(standard_piece, 12)}")
    print(f"  {'name':<40}{'value':<22}{'Δ rel %'}")
    scored = []
    for name, val in candidates:
        rel = (val - standard_piece) / standard_piece * 100 if abs(standard_piece) > mp.mpf("1e-30") else mp.inf
        scored.append((name, val, rel))

    scored.sort(key=lambda r: abs(r[2]))
    for name, val, rel in scored:
        marker = ""
        if abs(rel) < mp.mpf("0.1"):
            marker = " ⭐⭐ < 0.1%"
        elif abs(rel) < mp.mpf("1"):
            marker = " ⭐ < 1%"
        elif abs(rel) < mp.mpf("10"):
            marker = " *"
        print(f"  {name:<40}{mp.nstr(val, 12):<22}{mp.nstr(rel, 6)}{marker}")

    # ── PSLQ on standard_piece ──
    print(f"\n[PSLQ: standard_piece vs natural basis at maxcoeff 10⁵]")
    basis = {
        "h⁴": h ** 4,
        "h⁶": h ** 6,
        "ℏ_q⁴": hbar_q ** 4,
        "ℏ_q² · h²": hbar_q_sq * h2,
        "(α_em/π) · h⁴": ALPHA_EM / mp.pi * h ** 4,
        "(α_em/π) · ℏ_q²": ALPHA_EM / mp.pi * hbar_q_sq,
        "G · h⁴": G * h ** 4,
        "h⁴ / [2]_q²": h ** 4 / q2 ** 2,
    }
    matches = []
    for name, val in basis.items():
        try:
            rel = mp.pslq([standard_piece, val], tol=mp.mpf("1e-15"), maxcoeff=100000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = standard_piece - ratio * val
                if abs(check) < mp.mpf("1e-12"):
                    matches.append((name, rel, ratio))
                    print(f"  ⭐ standard_piece ≈ ({rel[1]}/{rel[0]}) · {name} = {mp.nstr(ratio*val, 15)}")
        except Exception:
            pass
    if not matches:
        print(f"  No tight pairwise integer relations.")

    # Verdict
    best = scored[0]
    print(f"\n[Verdict]")
    if matches:
        verdict = (
            f"PSLQ HIT: {matches[0][0]} with ratio {matches[0][2]}. "
            f"Structural candidate for the standard-channel piece."
        )
    elif abs(best[2]) < mp.mpf("1"):
        verdict = (
            f"CANDIDATE: '{best[0]}' at {mp.nstr(best[2], 6)}% — within 1% "
            f"of standard-channel piece. Worth structural investigation."
        )
    elif abs(best[2]) < mp.mpf("10"):
        verdict = (
            f"WEAK: '{best[0]}' at {mp.nstr(best[2], 6)}% — within 10% but "
            f"not at structural-identity level."
        )
    else:
        verdict = (
            f"NULL — no natural categorical candidate matches the standard-"
            f"channel piece needed ({mp.nstr(standard_piece, 6)}). May need "
            f"q-deformed Plancherel or non-Hecke operator."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "mn-standard-channel-correction",
        engine="python",
    )
    w.set_description(
        "Follow-up to PR #1654 Item A insight: tests candidate forms for "
        "the standard-channel (P_(2,1) = 4/6) correction needed to close "
        "m_n flavor-split 0.10% residual."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("delta_extra", mp.nstr(delta_extra, 25))
    w.add_data("standard_piece_target", mp.nstr(standard_piece, 25))
    w.add_data("best_candidate", best[0])
    w.add_data("best_rel_pct", mp.nstr(best[2], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="standard_channel_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} candidates at 80 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
