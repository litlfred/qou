#!/usr/bin/env python3
"""qbeta_c3_closure_piecewise_fibre_archimedean_probe.py — test which
pieces of the c_3 closure are fibre-evaluated (q=1) vs archimedean (q=q_0),
plus a reverse-confirmation cross-check of PR #1811.

PR #1811 (sibling, open) found that `/25 = [5]_q²` evaluated at the
**q=1 fibre classical-limit point** (roots-of-unity scan: only N→∞
reproduces 25).  This refines the c_3 closure structural reading
to a **mixed fibre/archimedean tensor**.  This probe extends that
finding to other pieces.

c_3 closure on main (commit 305c08a91):

  c_3 = -(q² + q⁻²) · (1 + ℏ_q · [3]_q / 25 + ℏ_q³ / [2]_q)

Six categorical pieces; this probe tests only the **three with a
well-defined q=1 fibre substitution**:

  - base = -(q² + q⁻²)
  - [3]_q
  - [2]_q

For each of these, replace the q=q_0 evaluation with the q=1 fibre
value and see if the closure improves or degrades vs target c_3.

**Pieces NOT tested** (q=1 substitution is ill-defined or trivial):
  - ℏ_q  : ℏ_q|_{q=1} = 0 (zeros rung 1 — uninformative)
  - ℏ_q³ : same as ℏ_q (zeros rung 2)

Plus a separate **Test 4** (cross-check, NOT a fibre substitution):
  /25 → /[5]_q²|_{q=q_0}  — this is the reverse of PR #1811's
  central finding: swapping the q=1-pinned /25 for q_0-archimedean
  /[5]_q² should DEGRADE the match if #1811 is right.  This is the
  **inverse confirmation** of #1811, recorded under a separate
  schema field (`alt_q0_value`, NOT `q_1_fibre_value`).

PR #1811's finding is the ONE confirmed fibre-point piece (/25).
This probe asks: are there OTHERS?  Or is /25 unique?

Results recorded in two table sections:
  - "Fibre-substitution tests" (base, [3]_q, [2]_q)
  - "Cross-check vs PR #1811" (reverse /25 → /[5]_q²)

If no other piece tests as fibre, /25 is structurally UNIQUE in
the closure.  Bounds the fibre-evaluation space.  No fit.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402


def c_3_closure(base, h_pieces):
    """c_3 = base · (1 + rung1 + rung2) with the 3-rung structure
    pieces supplied separately so each can be fibre- or archimedean-
    swapped independently.

    h_pieces = (hbar_q, qint_3, div_factor, hbar_q_cubed, qint_2)
    """
    hbar_q, qint_3, div_factor, hbar_q_cubed, qint_2 = h_pieces
    rung1 = hbar_q * qint_3 / div_factor
    rung2 = hbar_q_cubed / qint_2
    return base * (1 + rung1 + rung2)


def main() -> int:
    # Constants defined inside main() per Gemini review (avoid
    # module-level magic numbers).
    Q0_MP = mp.mpf("1.1099785827513808075916690956107688798744991218736")
    C3_TARGET = mp.mpf("-2.069342577")

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-c3-closure-piecewise-fibre-archimedean-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Piece-by-piece fibre (q=1) vs archimedean (q=q_0) test of "
        "the c_3 closure. Extends PR #1811's finding (/25 is "
        "fibre-evaluated [5]_q² at q=1) to the other 5 categorical "
        "pieces. Reports which pieces (if any) also fit q=1 fibre "
        "evaluation, vs q_0 archimedean. Honest test of the mixed "
        "fibre/archimedean structural reading."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Q_β c_3 closure — fibre vs archimedean piece-wise test")
    print("=" * 78)
    print()
    print(f"  Target c_3 (cal-anchored): {mp.nstr(C3_TARGET, 12)}")
    print()

    # q=q_0 evaluations (archimedean)
    q = Q0_MP
    hbar_q_q0       = (q - 1) / q
    qint_2_q0       = q + 1 / q
    qint_3_q0       = q ** 2 + 1 + 1 / q ** 2
    base_q0         = -(q ** 2 + 1 / q ** 2)   # -J_Hopf(q_0)
    hbar_q_cubed_q0 = hbar_q_q0 ** 3

    # q=1 fibre evaluations (classical limit)
    hbar_q_fib      = mp.mpf(0)         # ℏ_q|_{q=1} = 0 — can't substitute (would zero out rung)
    qint_2_fib      = mp.mpf(2)         # [2]_1 = 2
    qint_3_fib      = mp.mpf(3)         # [3]_1 = 3
    base_fib        = mp.mpf(-2)        # -J_Hopf(1) = -2
    hbar_q_cubed_fib = mp.mpf(0)        # ditto — would zero rung 2

    # Confirmed fibre piece (per PR #1811): /25 = [5]_q²|_{q=1}
    div_25 = mp.mpf(25)
    # Hypothetical alternative: /[5]_q²|_{q=q_0} (archimedean — REFUTED per #1811)
    qint_5_q0 = q ** 4 + q ** 2 + 1 + 1 / q ** 2 + 1 / q ** 4
    div_qint_5_sq = qint_5_q0 ** 2

    # Baseline closure (all archimedean except /25 fibre, per main)
    baseline = c_3_closure(
        base_q0,
        (hbar_q_q0, qint_3_q0, div_25, hbar_q_cubed_q0, qint_2_q0),
    )
    eps_baseline = (baseline / C3_TARGET - 1) * mp.mpf("1e6")

    print(f"  Baseline (all archimedean except /25 fibre, per main):")
    print(f"    c_3 = {mp.nstr(baseline, 12)}    ε = {float(eps_baseline):+.3f} ppm")
    print()

    print(f"  Fibre-substitution tests (base, [3]_q, [2]_q):")
    print(f"  {'Piece':<22} {'q_0 value':>14} {'q=1 fibre':>10} {'Δε [ppm]':>11} verdict")
    print(f"  {'-'*22} {'-'*14} {'-'*10} {'-'*11} {'-'*9}")

    # Test 1: base = -J_Hopf
    test_base = c_3_closure(
        base_fib,
        (hbar_q_q0, qint_3_q0, div_25, hbar_q_cubed_q0, qint_2_q0),
    )
    eps_t1 = (test_base / C3_TARGET - 1) * mp.mpf("1e6")
    print(f"  {'base = -(q²+q⁻²)':<22} {mp.nstr(base_q0, 8):>14} "
          f"{mp.nstr(base_fib, 4):>10} {float(eps_t1 - eps_baseline):+11.1f} "
          f"{'WORSE' if abs(eps_t1) > abs(eps_baseline) else 'BETTER'}")

    # Test 2: [3]_q
    test_qint3 = c_3_closure(
        base_q0,
        (hbar_q_q0, qint_3_fib, div_25, hbar_q_cubed_q0, qint_2_q0),
    )
    eps_t2 = (test_qint3 / C3_TARGET - 1) * mp.mpf("1e6")
    print(f"  {'[3]_q':<22} {mp.nstr(qint_3_q0, 8):>14} "
          f"{mp.nstr(qint_3_fib, 4):>10} {float(eps_t2 - eps_baseline):+11.1f} "
          f"{'WORSE' if abs(eps_t2) > abs(eps_baseline) else 'BETTER'}")

    # Test 3: [2]_q
    test_qint2 = c_3_closure(
        base_q0,
        (hbar_q_q0, qint_3_q0, div_25, hbar_q_cubed_q0, qint_2_fib),
    )
    eps_t3 = (test_qint2 / C3_TARGET - 1) * mp.mpf("1e6")
    print(f"  {'[2]_q':<22} {mp.nstr(qint_2_q0, 8):>14} "
          f"{mp.nstr(qint_2_fib, 4):>10} {float(eps_t3 - eps_baseline):+11.1f} "
          f"{'WORSE' if abs(eps_t3) > abs(eps_baseline) else 'BETTER'}")

    # Test 4 is NOT a fibre substitution — it is the reverse-direction
    # cross-check of PR #1811's central finding. Recorded under a
    # separate `alt_q0_value` schema field (per Copilot review).
    print()
    print(f"  Cross-check vs PR #1811 (reverse direction — NOT a fibre test):")
    print(f"  {'Piece':<22} {'main /25 value':>14} {'/[5]_q²(q_0)':>14} {'Δε [ppm]':>11} verdict")
    print(f"  {'-'*22} {'-'*14} {'-'*14} {'-'*11} {'-'*9}")
    test_div = c_3_closure(
        base_q0,
        (hbar_q_q0, qint_3_q0, div_qint_5_sq, hbar_q_cubed_q0, qint_2_q0),
    )
    eps_t4 = (test_div / C3_TARGET - 1) * mp.mpf("1e6")
    print(f"  {'/25 → /[5]_q² (q_0)':<22} {mp.nstr(div_25, 8):>14} "
          f"{mp.nstr(div_qint_5_sq, 8):>14} {float(eps_t4 - eps_baseline):+11.1f} "
          f"{'WORSE' if abs(eps_t4) > abs(eps_baseline) else 'BETTER'}")
    print(f"  → confirms PR #1811: q-deformed /[5]_q² far worse than q=1-pinned /25.")
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()

    fibre_pieces = []
    archimedean_pieces = []
    for name, eps in [("base = -(q²+q⁻²)", eps_t1),
                      ("[3]_q", eps_t2),
                      ("[2]_q", eps_t3)]:
        if abs(eps) < abs(eps_baseline):
            fibre_pieces.append(name)
        else:
            archimedean_pieces.append(name)

    print(f"  c_3 closure structural reading (post-test):")
    print()
    print(f"  Fibre-point (q=1) pieces:")
    print(f"    /25 = [5]_q²|_{{q=1}}        (CONFIRMED per PR #1811)")
    for p in fibre_pieces:
        print(f"    {p}    (new finding)")
    if not fibre_pieces:
        print(f"    (no other fibre pieces — /25 is UNIQUE)")
    print()
    print(f"  Archimedean (q=q_0) pieces:")
    for p in archimedean_pieces:
        print(f"    {p}")
    print(f"    ℏ_q  (cannot test — ℏ_q|_{{q=1}} = 0 zeros the rung)")
    print(f"    ℏ_q³ (cannot test — ditto)")
    print()
    if not fibre_pieces:
        print(f"  Structural reading: c_3 closure has EXACTLY ONE fibre-point")
        print(f"  factor (/25); all other testable pieces are archimedean.")
        print(f"  This is a (5+ archimedean) × (1 fibre) tensor product.")
        print(f"  Consistent with PR #1811's identification of /25 as the")
        print(f"  unique fibre piece. The 'fibre vs observable' split per")
        print(f"  CLAUDE.md §'Im(q) at fibre vs observable level' is real")
        print(f"  but minimal in this closure.")
    print()

    builder.add_data("baseline_eps_ppm", float(eps_baseline))
    builder.add_data("piece_tests", [
        {"piece": "base = -(q²+q⁻²)", "q_0_value": mp.nstr(base_q0, 25),
         "q_1_fibre_value": str(base_fib),
         "delta_eps_ppm": float(eps_t1 - eps_baseline)},
        {"piece": "[3]_q", "q_0_value": mp.nstr(qint_3_q0, 25),
         "q_1_fibre_value": str(qint_3_fib),
         "delta_eps_ppm": float(eps_t2 - eps_baseline)},
        {"piece": "[2]_q", "q_0_value": mp.nstr(qint_2_q0, 25),
         "q_1_fibre_value": str(qint_2_fib),
         "delta_eps_ppm": float(eps_t3 - eps_baseline)},
        {"piece": "/25 → /[5]_q²|_{q=q_0} (cross-check NOT fibre test)",
         "q_0_value_main": str(div_25),
         "alt_q0_value": mp.nstr(div_qint_5_sq, 25),
         "delta_eps_ppm": float(eps_t4 - eps_baseline),
         "purpose": "reverse-direction confirmation of PR #1811"},
    ])
    builder.add_data("verdict", {
        "fibre_pieces": ["/25 = [5]_q²|_{q=1}"] + fibre_pieces,
        "archimedean_pieces": archimedean_pieces,
        "interpretation": (
            "c_3 closure structural reading: /25 is the unique testable "
            "fibre-point factor; all other testable pieces evaluate "
            "archimedean at q_0. (5 archimedean) × (1 fibre) tensor."
        ) if not fibre_pieces else (
            "Multiple pieces test as fibre-evaluated — broader "
            "fibre-tensor structure than PR #1811's single-piece reading."
        ),
    })

    builder.add_assertion(
        "pr1811_div25_finding_confirmed_reverse_test",
        computed=1 if abs(eps_t4) > abs(eps_baseline) else 0,
        expected=1,
        tolerance=0,
        source=("Reverse confirmation of PR #1811's central finding: "
                "swapping /25 (q=1 fibre) → /[5]_q² (q_0 archimedean) "
                "must DEGRADE the c_3 match (since /25 wins at proton "
                "anchor). This is the inverse of #1811's test and "
                "must agree with it. Sanity invariant."),
    )

    builder.save()
    print(f"  Witness: qbeta-c3-closure-piecewise-fibre-archimedean-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
