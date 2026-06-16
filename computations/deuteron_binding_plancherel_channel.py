"""Deuteron binding via Plancherel-channel structure — Item C of PR #1654.

Brief test: does the Plancherel-channel template at H_2 (2-strand
deuteron sub-braid) close the deuteron binding-energy ratio?

## Setup

Deuteron: B(d) = 2.22456611 MeV. The binding-fraction ratio:
  B(d) / M_d_avg = 2.22456611 / 1875.612... = 0.001186

In the framework, this corresponds to Δ_λ for partition λ at the
deuteron's Wedderburn channel.

## Plancherel-channel candidates at H_2

  - trivial V_(2): P = 1/2, σ_1(triv) = +q
  - sign V_(1,1): P = 1/2, σ_1(sign) = -1

Test various forms via the Plancherel structure.

## Cross-references

- queue: research-one-plus-q-over-two-derivation (sibling)
- queue: research-multi-nucleon-interface-operator
- prop:option-e-binding-energy (if defined)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _h4_substrate import M_E_MEV, M_P_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
import experimental_constants as _ec  # noqa: E402
from q_parameter import q_at, q_str  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402


def main() -> int:
    DPS = 80
    set_compute_dps(DPS)
    q = q_at(DPS)

    print("=" * 78)
    print("Deuteron binding via Plancherel-channel (item C)")
    print("=" * 78)
    print(f"\nq_0 = {q_str(60)} (display)\n")

    M_N_MEV = M_P_MEV + M_E_MEV + mp.mpf(repr(_ec.Q_NEUTRON_MEV))
    # Deuteron CODATA from the codata_constants registry (no inline literal).
    from codata_constants import M_D_MEV_VALIDATION
    M_D_MEV = M_D_MEV_VALIDATION
    B_d = M_P_MEV + M_N_MEV - M_D_MEV
    print(f"[CODATA]")
    print(f"  B(d) = {mp.nstr(B_d, 12)} MeV (= 2.22... )")
    print(f"  B(d) / M_d = {mp.nstr(B_d / M_D_MEV, 18)}")
    print(f"  B(d) / m_e = {mp.nstr(B_d / M_E_MEV, 18)}")
    print(f"  (m_p+m_n)/2 = {mp.nstr((M_P_MEV+M_N_MEV)/2, 12)}")

    # Substrate
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    q2 = q + 1 / q

    # H_2 Plancherel
    P_triv = mp.mpf(1) / 2
    P_sign = mp.mpf(1) / 2

    # Target: B(d) / M_d (dimensionless)
    target = B_d / M_D_MEV

    # Candidates
    candidates = [
        # (a) (1/2)·ℏ_q² · something
        ("(a) P · ℏ_q²", P_triv * hbar_q_sq),
        # (b) (1+q)/2 · ℏ_q² (Option E v9 (1+q)/2 factor)
        ("(b) (1+q)/2 · ℏ_q²", (1 + q) / 2 * hbar_q_sq),
        # (c) (q-1)² / [2]_q (Cooper-pair-like)
        ("(c) (q-1)² / [2]_q", (q - 1) ** 2 / q2),
        # (d) ℏ_q² · (1-h²)/2 (binding fraction)
        ("(d) ℏ_q² · (1-h²)/2", hbar_q_sq * (1 - h2) / 2),
        # (e) sign block: ℏ_q² · 1/2 · |σ_1(sign)|
        ("(e) ℏ_q² · |σ_1(sign)| / 2 = ℏ_q²/2",
         hbar_q_sq / 2),
        # (f) Empirical fit (control)
        ("(f) target (exact)", target),
        # (g) (1-q⁻²) · 1/8 (Bring-related)
        ("(g) (1 - q⁻²) / 8", (1 - q ** (-2)) / 8),
        # (h) ℏ_q · (q-1)² · 1/2
        ("(h) ℏ_q · (q-1)² · 1/2", hbar_q * (q - 1) ** 2 / 2),
        # (i) h⁴ / 8 ~ small h-order
        ("(i) h⁴ / 8", h ** 4 / 8),
    ]

    print(f"\n[Plancherel-channel candidates for B(d) / M_d = {mp.nstr(target, 8)}]")
    print(f"  {'name':<40}{'value':<22}{'Δ rel %'}")
    scored = []
    for name, val in candidates:
        rel = (val - target) / target * 100
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

    best = scored[0] if scored[0][0] != "(f) target (exact)" else scored[1]
    print(f"\n[Verdict]")
    if abs(best[2]) < mp.mpf("1"):
        verdict = (
            f"DEUTERON CANDIDATE: '{best[0]}' at {mp.nstr(best[2], 6)}% — "
            f"may be structurally suggestive (matches at < 1% level)."
        )
    elif abs(best[2]) < mp.mpf("10"):
        verdict = (
            f"BEST tested: '{best[0]}' at {mp.nstr(best[2], 6)}% — beats "
            f"random alignment but not at structural level."
        )
    else:
        verdict = (
            f"NULL — Plancherel-channel template at H_2 does NOT close "
            f"the deuteron binding ratio. Confirms (yet again) that the "
            f"Δ_λ binding closure requires deeper structure than H_2 "
            f"classical Plancherel — multi-session open work."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "deuteron-binding-plancherel-channel",
        engine="python",
    )
    w.set_description(
        "Item C of PR #1654: brief test of Plancherel-channel template "
        "at H_2 for the deuteron binding ratio. Complements sibling Δ_λ "
        "Option E work (multiple existing queue entries)."
    )
    w.add_parameter("q_80dps", q_str(DPS))
    w.add_parameter("mp_dps_runtime", str(mp.mp.dps))
    w.add_data("target_Bd_over_Md", mp.nstr(target, 25))
    w.add_data("best_candidate", best[0])
    w.add_data("best_rel_pct", mp.nstr(best[2], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="deuteron_scan_completed",
        computed=len(candidates),
        expected=len(candidates),
        tolerance=0,
        source=f"Scanned {len(candidates)} candidates at 80 dps.",
    )
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("deuteron (²H)"))
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
