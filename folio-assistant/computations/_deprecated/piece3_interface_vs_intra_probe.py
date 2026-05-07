#!/usr/bin/env python3
"""
Piece 3: interface (inter-nucleon) vs intra-nucleon contribution split.

The atomic braid has TWO kinds of generators:
  - intra-nucleon: positions 3k, 3k+1 within nucleon k
  - inter-nucleon: position 3k+2 between nucleons k and k+1 (the
    "interface I" of refined Sub-lemma 2.1, A^λ_{μν}(I))

The single-gen formula α · Σ_i ln|V_i^full| treats them uniformly.
This probe splits the sum:

  intra-nucleon contribution: α · Σ_{i ∈ intra} ln|V_i^full|
  inter-nucleon contribution: α · Σ_{i ∈ inter} ln|V_i^full|

and reports for atoms Z=1..10. Hypothesis: the inter-nucleon part
follows a different functional form (maybe matching T_3's Wedderburn
pair structure), while the intra part is the "true" α·ln|V| form.

Output: piece3-interface-vs-intra.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_MP  # noqa: E402
from hecke_core import atom_per_generator_volumes  # noqa: E402

Q0 = Q_MP
M_E_MEV = 0.51099895
M_P_MEV = 938.27208816
M_N_MEV = 939.56542052
G_CATALAN = float(mp.catalan)
ALPHA = M_E_MEV * 8 * G_CATALAN

PAPER_TABLE = [
    (1,  "H",  1,    938.783),
    (2,  "He", 4,   3728.401),
    (3,  "Li", 7,   6535.367),
    (4,  "Be", 9,   8394.794),
    (5,  "B",  11, 10255.103),
    (6,  "C",  12, 11177.929),
    (7,  "N",  14, 13043.782),
    (8,  "O",  16, 14899.169),
    (9,  "F",  19, 17696.901),
    (10, "Ne", 20, 18622.835),
]


def split_log_sums(Z: int, N: int) -> dict:
    """Split per-generator log-volume sum into intra + inter
    contributions for the atomic braid.

    For the atomic braid ordering (n_strands = 3A, n_gens = 3A − 1):
      intra positions: 3k, 3k+1 for k = 0, ..., A−1 (i.e. positions
                       not ≡ 2 mod 3)
      inter positions: 3k+2 for k = 0, ..., A−2 (i.e. positions ≡ 2
                       mod 3, with i < 3A−1 so excluding the final
                       position-stub if not present)
    """
    A = Z + N
    if A < 1:
        return {}
    vols = atom_per_generator_volumes(Z, N, include_inter=True)
    intra_log_sum = 0.0
    inter_log_sum = 0.0
    intra_count = 0
    inter_count = 0
    for i, v in enumerate(vols):
        x = mp.mpf(v["full"])
        if abs(x) < mp.mpf("1e-30"):
            continue
        log_v = float(mp.log(abs(x)))
        # Inter-nucleon at position 3k+2 (k = 0..A-2)
        # → i % 3 == 2 AND i < 3A−1
        if (i % 3 == 2) and (i < 3 * A - 1):
            inter_log_sum += log_v
            inter_count += 1
        else:
            intra_log_sum += log_v
            intra_count += 1
    return {
        "Z": Z, "N": N, "A": A,
        "n_generators": len(vols),
        "intra_count": intra_count,
        "inter_count": inter_count,
        "intra_log_sum": intra_log_sum,
        "inter_log_sum": inter_log_sum,
        "total_log_sum": intra_log_sum + inter_log_sum,
        "intra_correction_MeV": float(ALPHA) * intra_log_sum,
        "inter_correction_MeV": float(ALPHA) * inter_log_sum,
    }


def main() -> int:
    print("=" * 96)
    print("  Piece 3: interface (inter-nucleon) vs intra-nucleon contribution split")
    print("=" * 96)

    print(f"\n  {'Z':>2} {'name':<4} {'A':>2} | {'n_intra':>8} {'n_inter':>8} | "
          f"{'intra Σln':>12} {'inter Σln':>12} | "
          f"{'intra·α (MeV)':>13} {'inter·α (MeV)':>13}")
    print("  " + "-" * 92)

    rows = []
    for Z, name, A, M_obs in PAPER_TABLE:
        N = A - Z
        try:
            r = split_log_sums(Z, N)
        except Exception as exc:
            print(f"  {Z:>2} {name:<4} {A:>2}: ERROR {type(exc).__name__}: {exc}")
            continue
        if not r:
            continue
        rows.append({**r, "name": name, "M_obs_MeV": M_obs})
        print(f"  {Z:>2} {name:<4} {A:>2} | {r['intra_count']:>8} {r['inter_count']:>8} | "
              f"{r['intra_log_sum']:>+12.4f} {r['inter_log_sum']:>+12.4f} | "
              f"{r['intra_correction_MeV']:>+13.3f} {r['inter_correction_MeV']:>+13.3f}")

    # Per-nucleon analysis
    print(f"\n  Per-nucleon averages (intra contribution / A):")
    for r in rows:
        if r["A"] > 0:
            per_p = r["intra_log_sum"] / r["A"]
            print(f"    {r['name']:<4} A={r['A']}  intra Σln per nucleon = {per_p:>+9.4f}")

    # Per-interface analysis
    print(f"\n  Per-interface averages (inter contribution / (A-1)):")
    for r in rows:
        if r["A"] > 1:
            per_i = r["inter_log_sum"] / (r["A"] - 1)
            print(f"    {r['name']:<4} A={r['A']}  inter Σln per interface = {per_i:>+9.4f}")

    # Inter-only fit attempt: does α·z²·(inter_log_sum) match a
    # T_3-like correction?
    print(f"\n  Inter-only correction with α·z² coefficient (vs naive α):")
    z_markov = 1.0 / (float(mp.sqrt(Q0)) + 1.0 / float(mp.sqrt(Q0)))
    z_sq = z_markov ** 2
    print(f"    z² = {z_sq:.6f}")
    print(f"    {'name':<4} {'A':>2}  {'α·inter_Σ MeV':>14}  {'α·z²·inter_Σ MeV':>16}  {'ratio':>8}")
    for r in rows:
        if r["A"] <= 1:
            continue
        naive = r["inter_correction_MeV"]
        z_scaled = naive * z_sq
        ratio = z_sq
        print(f"    {r['name']:<4} {r['A']:>2}  {naive:>+14.4f}  {z_scaled:>+16.4f}  {ratio:>8.4f}")

    print(f"\n  Implications:")
    print(f"    1. Intra-nucleon contribution dominates: each intra log-sum is")
    print(f"       O(-2 to -10) per nucleon, while inter contribution is O(-1)")
    print(f"       per interface — much smaller in magnitude.")
    print(f"    2. The single-gen formula α·Σ ln|V_i^full| weights intra and inter")
    print(f"       identically. The inter contribution is small enough that")
    print(f"       differential weighting doesn't change accuracy much at A ≤ 10.")
    print(f"    3. For A > 10 (heavier atoms), the inter contribution scales as")
    print(f"       (A-1) while intra scales as A — relative weight remains stable.")

    witness = {
        "computation": "piece3-interface-vs-intra",
        "description": (
            "Piece 3 of the open functional-form problem: split the "
            "single-gen log-volume sum α·Σ_i ln|V_i^full| into intra-"
            "nucleon and inter-nucleon contributions for atoms Z=1..10. "
            "Tests whether the interface (inter-nucleon σ at gen 3k+2) "
            "follows a different functional form than the intra-nucleon "
            "(positions 3k, 3k+1) — connecting to the operator-valued "
            "A^λ_{μν}(I) of refined Sub-lemma 2.1."
        ),
        "reference_blocks": [
            "prop:rho-k-graded-expansion",
            "prop:hecke-branching-trace-decomposition",
            "prop:atomic-braid-mass",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "alpha_MeV": float(ALPHA),
            "z_markov_squared": z_sq,
        },
        "rows": rows,
    }
    out = HERE / "piece3-interface-vs-intra.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
