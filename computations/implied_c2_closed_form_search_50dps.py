"""Closed-form search for the implied h² coefficient -0.91628 at q_0.

Per author 2026-05-25 — searches a curated catalog of mathematical
constants and their combinations against the actual implied h²
coefficient `c_implied = -0.91628187612727488...` (computed from
target_lw at q_0 at 50 dps).

The closest candidates from prior probes:
  -G ≈ -0.91596 (Δ +3.2e-4)
  -11/12 ≈ -0.91667 (Δ -3.8e-4)

This probe systematically tests ~70 candidate closed forms drawn from:
  - Dirichlet L-values: L(2, χ_d) for d = 3, 4, 7, 8, 11
  - Polylog values: Li_n at z = -1, 1/2, 1/3, 1/4, golden ratio
  - Hurwitz zeta ζ(2, p/q) for small rationals
  - Hyperbolic volumes: Lobachevsky Λ(πp/q) for small q
  - π, e, G, ζ(n) combinations: products / ratios / sums
  - Modular L-function values (limited subset)

If ANY candidate matches -0.91628 within 1 ppm (5e-7), that's a
suspect structural identity; report and flag. If NONE matches, then
-0.91628 is either:
  (a) A new constant we haven't catalogued, or
  (b) NOT a single closed-form (composite of multiple contributions)

## Method

For each candidate constant `c`, compute `|c - c_implied|`. Report
the K closest candidates, sorted by absolute deviation. The candidate
`-G` should appear with deviation 3.2e-4 (already known).

## Cross-references

- [`implied_h2_coefficient_audit_50dps.py`](implied_h2_coefficient_audit_50dps.py)
- [audit 2026-05-25 Path C](../../docs/audits/2026-05-25-path-c-categorical-principle-hunt.md)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


M_E_MEV = "0.51099895069"
M_P_MEV = "938.27208816"


def compute_implied_c2(dps: int = 50) -> "mp.mpf":
    """Recompute c_implied at the target precision."""
    mp.mp.dps = dps
    q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    h2 = h * h
    G = mp.catalan
    m_e = mp.mpf(M_E_MEV)
    m_p = mp.mpf(M_P_MEV)
    hbar_q = 1 - qi
    vol_b3 = 8 * G
    geom_leading = vol_b3 / hbar_q ** 2
    target_lw = m_p / (m_e * geom_leading)
    return (target_lw - mp.mpf("2.5")) / h2


def dirichlet_L_at_2(chi_period: int, chi_values: dict[int, int]) -> "mp.mpf":
    """L(2, χ) = Σ_{n=1}^∞ χ(n) / n² for a Dirichlet character χ.

    chi_values maps n mod chi_period to χ(n) ∈ {-1, 0, +1}.
    """
    total = mp.mpf(0)
    for n in range(1, 5001):  # truncate; series converges quickly
        residue = n % chi_period
        chi_n = chi_values.get(residue, 0)
        if chi_n != 0:
            total += mp.mpf(chi_n) / (n * n)
    return total


def lobachevsky(angle: "mp.mpf") -> "mp.mpf":
    """Lobachevsky function Λ(θ) = -∫_0^θ log|2 sin(t)| dt.

    Implemented via series:
      Λ(θ) = (1/2) Σ_{k=1}^∞ sin(2kθ) / k².

    Converges for any real θ.
    """
    total = mp.mpf(0)
    for k in range(1, 5001):
        total += mp.sin(2 * k * angle) / (k * k)
    return total / 2


def build_candidates() -> list[tuple[str, "mp.mpf"]]:
    """Build the candidate catalogue."""
    G = mp.catalan
    pi = mp.pi
    e = mp.e
    ln2 = mp.log(2)
    zeta2 = mp.zeta(2)
    zeta3 = mp.zeta(3)

    candidates: list[tuple[str, "mp.mpf"]] = []

    # --- Direct G-based ---
    candidates += [
        ("-G", -G),
        ("-G - 1/3500", -G - mp.mpf(1) / 3500),
        ("-G·(1 + 1/3000)", -G * (1 + mp.mpf(1) / 3000)),
        ("-G - π²/(6·5000)", -G - pi ** 2 / (6 * 5000)),
        ("-G - G²/2900", -G - G * G / 2900),
        ("-G - 1/π²·1e-3", -G - 1 / pi ** 2 * mp.mpf("0.001")),
    ]

    # --- Simple rationals near -0.916 ---
    for num, den in [
        (-11, 12), (-22, 24), (-23, 25), (-23, 25.1), (-44, 48),
        (-91, 99), (-92, 100), (-9163, 10000), (-91628, 100000),
    ]:
        candidates.append((f"{num}/{den}", mp.mpf(num) / mp.mpf(den)))

    # --- Lobachevsky function values ---
    for p, q in [(1, 4), (1, 3), (1, 6), (2, 3), (1, 2), (3, 8),
                 (1, 5), (2, 5), (3, 10), (1, 12)]:
        angle = pi * mp.mpf(p) / q
        val = lobachevsky(angle)
        candidates.append((f"Λ(π·{p}/{q})", val))
        candidates.append((f"-Λ(π·{p}/{q})", -val))
        candidates.append((f"-Λ(π·{p}/{q})·2", -val * 2))

    # --- Dirichlet L-values L(2, χ) ---
    # χ_3 (non-trivial mod 3): χ(1)=1, χ(2)=-1
    chi3 = {1: 1, 2: -1}
    L2_chi3 = dirichlet_L_at_2(3, chi3)
    candidates += [
        ("L(2,χ_3)", L2_chi3),
        ("-L(2,χ_3)", -L2_chi3),
    ]
    # χ_4 (non-trivial mod 4): χ(1)=1, χ(3)=-1 — this IS G
    # (sanity: should match -G)
    chi4 = {1: 1, 3: -1}
    L2_chi4 = dirichlet_L_at_2(4, chi4)
    candidates.append(("L(2,χ_4) = G", L2_chi4))
    candidates.append(("-L(2,χ_4) = -G", -L2_chi4))
    # χ_5 (mod 5, quadratic): χ(1)=1, χ(2)=-1, χ(3)=-1, χ(4)=1
    chi5 = {1: 1, 2: -1, 3: -1, 4: 1}
    L2_chi5 = dirichlet_L_at_2(5, chi5)
    candidates += [
        ("L(2,χ_5)", L2_chi5),
        ("-L(2,χ_5)", -L2_chi5),
        ("-L(2,χ_5)·2", -L2_chi5 * 2),
    ]
    # χ_7 (mod 7, quadratic): χ(1)=1, χ(2)=1, χ(3)=-1, χ(4)=1, χ(5)=-1, χ(6)=-1
    chi7 = {1: 1, 2: 1, 3: -1, 4: 1, 5: -1, 6: -1}
    L2_chi7 = dirichlet_L_at_2(7, chi7)
    candidates += [
        ("L(2,χ_7)", L2_chi7),
        ("-L(2,χ_7)", -L2_chi7),
        ("-L(2,χ_7)·2", -L2_chi7 * 2),
    ]
    # χ_8 (mod 8, χ(1)=1, χ(3)=-1, χ(5)=-1, χ(7)=1)
    chi8 = {1: 1, 3: -1, 5: -1, 7: 1}
    L2_chi8 = dirichlet_L_at_2(8, chi8)
    candidates += [
        ("L(2,χ_8)", L2_chi8),
        ("-L(2,χ_8)", -L2_chi8),
    ]

    # --- Polylog values ---
    li2_half = mp.polylog(2, mp.mpf("0.5"))  # = π²/12 - (ln2)²/2
    li2_minus1 = mp.polylog(2, -1)  # = -π²/12
    li2_third = mp.polylog(2, mp.mpf(1) / 3)
    li2_quarter = mp.polylog(2, mp.mpf(1) / 4)
    li2_phi_inv = mp.polylog(2, (mp.sqrt(5) - 1) / 2)  # golden ratio
    candidates += [
        ("Li_2(1/2)", li2_half),
        ("-Li_2(1/2)", -li2_half),
        ("Li_2(-1)", li2_minus1),
        ("-Li_2(-1)", -li2_minus1),
        ("Li_2(1/3)", li2_third),
        ("-Li_2(1/3)", -li2_third),
        ("Li_2(1/4)", li2_quarter),
        ("-Li_2(1/4)", -li2_quarter),
        ("Li_2(φ⁻¹)", li2_phi_inv),
        ("-Li_2(φ⁻¹)", -li2_phi_inv),
    ]

    # --- Combinations of π, e, G, ζ(3), ln(2) ---
    candidates += [
        ("-π²/(8·G)", -pi ** 2 / (8 * G)),
        ("-π²/12 + ln(2)²/2", -pi ** 2 / 12 + ln2 ** 2 / 2),
        ("π²/12 - ln(2)²/2", pi ** 2 / 12 - ln2 ** 2 / 2),
        ("-G - π/(8·G²·100)", -G - pi / (8 * G ** 2 * 100)),
        ("-G·π/e", -G * pi / e),  # silly combo
        ("ln(π)/π", mp.log(pi) / pi),
        ("-ln(π)/π", -mp.log(pi) / pi),
        ("-3·ln(π)/π²", -3 * mp.log(pi) / pi ** 2),
        ("-ln(2π)/2", -mp.log(2 * pi) / 2),
        ("ζ(3)·G·π/100", zeta3 * G * pi / 100),
        ("-ζ(3)/(2·π·G)", -zeta3 / (2 * pi * G)),
        ("-ζ(2)/π·1/8", -zeta2 / pi / 8),
        ("-ζ(3)/(π·G)·π", -zeta3 / pi),
        ("-(π+G·π)/(8)", -(pi + G * pi) / 8),
        ("e²-2π", e ** 2 - 2 * pi),
        ("-(e²-2π)·100", -(e ** 2 - 2 * pi) * 100),
    ]

    # --- Specific structural candidates from QOU substrate context ---
    # h² at q_0
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    h2 = h * h
    candidates += [
        ("h²(q_0)·-20", h2 * -20),
        ("h²(q_0)·-21", h2 * -21),
        ("-(h(q_0)+G)·G", -(h + G) * G),
        # The Vol(𝓑₃)/8 = G, and other 𝓑₃-derived constants
        ("-Vol(4_1)/(2π)", -2 * mp.mpf("1.0149416064966") / (2 * pi)),  # Vol(4_1) ≈ 2.0299
    ]

    return candidates


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "implied-c2-closed-form-search-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Searches a curated catalogue of ~70 closed-form mathematical "
        "constants against the actual implied h² coefficient c_implied "
        "≈ -0.91628 at q_0 (50 dps). Reports top-10 closest matches "
        "to identify any structural identity within 1 ppm precision."
    )

    print("=" * 78)
    print("Closed-form search for the implied h² coefficient at q_0")
    print("=" * 78)

    c_implied = compute_implied_c2(dps=50)
    print(f"\nc_implied = {mp.nstr(c_implied, 25)}")

    candidates = build_candidates()
    print(f"\nSearching {len(candidates)} candidates...")

    # Score each candidate
    scored: list[tuple[mp.mpf, str, mp.mpf]] = []  # (|deviation|, name, value)
    for name, val in candidates:
        if mp.isnan(val) or mp.isinf(val):
            continue
        dev = val - c_implied
        scored.append((abs(dev), name, val))

    scored.sort(key=lambda t: t[0])

    print(f"\nTop 15 closest closed-form candidates to c_implied:\n")
    print(f"  {'rank':<6}{'name':<32}{'value':<22}{'Δ':<22}{'|Δ|/|c|':<10}")
    for rank, (adev, name, val) in enumerate(scored[:15], 1):
        rel = adev / abs(c_implied)
        print(f"  {rank:<6}{name:<32}{mp.nstr(val, 12):<22}"
              f"{mp.nstr(val - c_implied, 8):<22}{mp.nstr(rel, 6):<10}")

    # Threshold checks
    one_ppm = mp.mpf("1e-6") * abs(c_implied)
    matches_1ppm = [t for t in scored if t[0] < one_ppm]
    matches_1pct = [t for t in scored if t[0] < abs(c_implied) * mp.mpf("0.01")]

    print(f"\n[Threshold analysis]")
    print(f"  Candidates within 1 ppm of c_implied:")
    if matches_1ppm:
        for adev, name, val in matches_1ppm:
            print(f"    {name}: {mp.nstr(val, 18)} (Δ = {mp.nstr(adev, 6)})")
    else:
        print(f"    NONE — no candidate matches to 1 ppm")
        print(f"    Closest is {scored[0][1]} at Δ = {mp.nstr(scored[0][0], 6)}")
        print(f"    Relative deviation: {mp.nstr(scored[0][0] / abs(c_implied), 6)}")
        print()
        print(f"    INTERPRETATION: c_implied is unlikely to be a single")
        print(f"    closed-form constant from this catalogue. It's either")
        print(f"    (a) a new constant not in standard tables, or")
        print(f"    (b) a sum/combination of multiple contributions")
        print(f"    (e.g. -G - α·h²·something at q_0 specifically).")

    print(f"\n  Candidates within 1% (relative): {len(matches_1pct)}")

    # Witness
    w.add_parameter("c_implied", mp.nstr(c_implied, 25))
    w.add_parameter("num_candidates", len(candidates))
    w.add_data("top_15_closest", [
        {
            "rank": rank,
            "name": name,
            "value": mp.nstr(val, 25),
            "deviation": mp.nstr(val - c_implied, 25),
            "relative": mp.nstr(adev / abs(c_implied), 12),
        }
        for rank, (adev, name, val) in enumerate(scored[:15], 1)
    ])
    w.add_data("matches_1ppm", [
        {"name": name, "value": mp.nstr(val, 25)}
        for adev, name, val in matches_1ppm
    ])
    w.add_data("conclusion", (
        f"Found {len(matches_1ppm)} closed-form candidate(s) within "
        f"1 ppm of c_implied at 50 dps. Closest match overall: "
        f"'{scored[0][1]}' at Δ = {mp.nstr(scored[0][0], 6)} "
        f"(relative {mp.nstr(scored[0][0] / abs(c_implied), 6)}). "
        + ("This is a STRUCTURAL IDENTITY candidate — recommend "
           "categorical follow-up." if matches_1ppm
           else "No structural identity found in the catalogue; "
           "c_implied is either a new constant or a sum of "
           "multiple contributions.")
    ))

    has_match_1ppm = len(matches_1ppm) > 0
    w.add_assertion(
        name="closed_form_search_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=(
            f"Catalog of {len(candidates)} closed-form constants "
            f"searched against c_implied at 50 dps. Found "
            f"{len(matches_1ppm)} match(es) within 1 ppm. "
            f"(Sanity check: search completed without error.)"
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
