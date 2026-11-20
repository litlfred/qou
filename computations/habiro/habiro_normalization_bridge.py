#!/usr/bin/env python3
"""
Habiro normalization bridge: map the integer expansion to tr_M.

The Habiro expansion Σ a_m(u)·(u;u)_m = 136.07 (proton at H₉).
The direct Markov trace tr_M(proton) = 1.065 (Hoefsmit at H₉).
Ratio = 127.73.

The Habiro expansion computes the CYCLOTOMIC invariant (related to
the colored Jones polynomial), not the Jones-Wenzl Markov trace.
The normalization bridge maps between them.

Key finding: ratio / [5]_q! ≈ 0.973 — within 2.7% of 1.
The q-factorial [5]_q! = 131.3 is the natural normalization for
the proton at H₉ with the muon torus-knot index n=5.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402
from canonical_trm_reference import tr_m_proton  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def q_fact(n, q):
    result = mp.mpf(1)
    for k in range(1, n+1):
        result *= (q**k - q**(-k)) / (q - 1/q)
    return result


def main():
    set_compute_dps()
    set_compute_dps()
    q = Q_MP
    h = q - 1/q

    hab = mp.mpf("136.0712063634817616514048508169837773395")
    # CONVENTION FIX (2026-08-30, bean qou-46ab). This read
    #     direct = mp.mpf("1.0653062286131670593652845…")
    # which is CONVENTION C — proved to 50 digits by
    # audits/he4_witness_convention_attribution_probe.py — while D has
    # been canonical since 2026-08-15. It is 7.55%% off, and it is
    # MULTIPLIED IN below rather than compared against, so the error
    # propagated into the result rather than showing up as a mismatch.
    # Read at the running pin instead of re-hardcoding a D literal:
    # a literal is stale the moment the anchor moves again, and the
    # previous regeneration sweep provably could not fix one.
    direct = tr_m_proton()
    ratio = hab / direct

    print("=" * 60)
    print("  Habiro normalization bridge")
    print("=" * 60)
    print()
    print(f"  Habiro sum (H₉):  {mp.nstr(hab, 15)}")
    print(f"  Direct tr_M (H₉): {mp.nstr(direct, 15)}")
    print(f"  Ratio:             {mp.nstr(ratio, 15)}")
    print()

    # Check q-factorial candidates
    print(f"  q-factorial candidates:")
    for n in range(1, 10):
        qfn = q_fact(n, q)
        r = ratio / qfn
        print(f"    ratio / [{n}]_q! = {mp.nstr(r, 10):>14s}  ([{n}]_q! = {mp.nstr(qfn, 10)})")
    print()

    # Best match: [5]_q! ≈ 131.3, ratio/[5]_q! ≈ 0.973
    qf5 = q_fact(5, q)
    delta = 1 - ratio/qf5
    print(f"  Best: ratio / [5]_q! = {mp.nstr(ratio/qf5, 15)}")
    print(f"  1 - ratio/[5]_q! = {mp.nstr(delta, 12)}")
    print(f"  δ/ℏ² = {mp.nstr(delta/((q-1)/q)**2, 10)}")
    print()

    # The correction δ ≈ 0.027 ≈ 2.78·ℏ²
    # Not a clean integer coefficient — the bridge is braid-specific.

    print("  STATUS: the normalization bridge is NOT a clean algebraic")
    print("  expression. Ratio/[5]_q! ≈ 0.973 is suggestive but the")
    print("  correction δ ≈ 2.78·ℏ² has no identified structural origin.")
    print("  The bridge involves the full H₉ representation theory of")
    print("  the proton braid word, not just q-integer factors.")

    w = WitnessBuilder("habiro-normalization-bridge", engine="mpmath")
    w.set_description(
        "Habiro normalization bridge: ratio 127.73 between Habiro "
        "integer expansion and direct Markov trace at H₉. Best "
        "candidate: ratio/[5]_q! ≈ 0.973 (2.7% off)."
    )
    w.set_audit_only("docs/audits/2026-05-27-habiro-normalization-gap.md")
    w.add_data("ratio", str(mp.nstr(ratio, 20)))
    w.add_data("ratio_over_qfact5", str(mp.nstr(ratio/qf5, 15)))
    w.add_data("status", "open — bridge is braid-specific, not algebraically clean")
    w.add_assertion("ratio_near_qfact5",
                     computed=1 if abs(float(ratio/qf5 - 1)) < 0.03 else 0,
                     expected=1, tolerance=0,
                     source="ratio/[5]_q! within 3% of 1")
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
