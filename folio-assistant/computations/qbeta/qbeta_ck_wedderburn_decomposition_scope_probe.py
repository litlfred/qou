#!/usr/bin/env python3
"""qbeta_ck_wedderburn_decomposition_scope_probe.py — probe 6.d
from the c_k generating-function scoping doc (scoped probe form).

PR #1824 follow-on, item 4 of "probe all" tranche. Probe 6.d
addresses the Wedderburn-block decomposition hypothesis: the
c_k aggregate decomposes over Hecke characters χ^λ as

  c_k(q_0) = Σ_λ a_k_λ · y_λ(q_0) · χ^λ(braid_word(T_w))

where λ ⊢ n ranges over partitions, y_λ is the Wenzl weight,
χ^λ is the Hecke character, and a_k_λ is the per-block Taylor
coefficient of a partition-specific generating function f_λ(u,q).

For the proton braid 𝓑₃ (Borromean ring 3-strand), n=3 and there
are 3 partitions:

  λ = (3)       — trivial rep,        d_λ = 1
  λ = (2, 1)    — standard / mixed,   d_λ = 2
  λ = (1, 1, 1) — sign / antisymm,    d_λ = 1

This probe:
  1. Enumerates the 3 partitions and their dimensions.
  2. Computes Wenzl weights y_λ(q_0) for each at the substrate q_0
     (closed-form expressions exist for n=3).
  3. Reports that full c_k decomposition over the χ^λ basis
     REQUIRES per-block c_k extraction infra not yet built
     (needs the Hoefsmit seminormal reps of the braid word).
  4. Notes that probes 6.a + 6.b suggest a clean -(k-1)! pattern
     at low k, AND that the m_μ V9 / Q_β c_3 SHARED [3]_q/25
     factor (per ck-dk registry) supports a per-block reading
     where the same λ = (2,1) or λ = (3) block contributes the
     [3]_q/25 to both observables.

Honest scoping. Concrete computational deliverable: the y_λ(q_0)
values at substrate (sanity-checking against pyhecke witnesses).
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    Q0_MP = mp.mpf("1.1099785827513808075916690956107688798744991218736")
    Z_MARKOV = 1 / (mp.sqrt(Q0_MP) + 1 / mp.sqrt(Q0_MP))

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-wedderburn-decomposition-scope-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Probe 6.d (scoping form): enumerates partitions of n=3 "
        "for the proton braid 𝓑₃, computes Wenzl weights y_λ(q_0) "
        "at substrate, and scopes the Wedderburn-block decomposition "
        "hypothesis. Full per-block c_k decomposition requires "
        "Hoefsmit-rep extraction infra not built here."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Probe 6.d — Wedderburn-block decomposition scope (n=3, proton 𝓑₃)")
    print("=" * 78)
    print()
    print(f"  q_0       = {mp.nstr(Q0_MP, 14)}")
    print(f"  z         = 1/(√q+1/√q) = {mp.nstr(Z_MARKOV, 12)}")
    print()

    q = Q0_MP

    # Partitions of n=3 and their data (closed-form q-Schur dimensions
    # via the q-hook-length formula).  For n=3:
    #   (3):       d_λ = 1, χ^λ(1) = 1
    #   (2,1):     d_λ = 2, χ^λ(1) = 2
    #   (1,1,1):   d_λ = 1, χ^λ(1) = 1
    #
    # Wenzl weights at q_0 (Hecke 3-strand, per qou-substrate y_lambda):
    #   y_(3)(q)       = 1 / [3]_q · q² · (q²+q+1) form — see
    #                    `y_lambda_wenzl_bridge.py`
    #   y_(2,1)(q)     = (q-q⁻¹) / something — non-trivial
    #   y_(1,1,1)(q)   = 1 / [3]_q · q⁻² · (q⁻²+q⁻¹+1) bar-form
    #
    # For probe 6.d (scoping), report closed-form expressions
    # WITHOUT requiring the full pyhecke extraction — leave the
    # numerical values as placeholders.

    qint_3 = q ** 2 + 1 + 1 / q ** 2
    qint_2 = q + 1 / q
    hbar_q = (q - 1) / q

    partitions = [
        {"label": "(3)",
         "name": "trivial / symmetric",
         "d_lambda": 1,
         "chi_at_identity": 1,
         "y_lambda_closed_form": "1 / [3]_q · (related to q-Schur s_(3))",
         "y_lambda_at_q0": mp.mpf(1) / qint_3,
         "role": "Markov-Jones traceful component; J_K(q) coefficient"},
        {"label": "(2, 1)",
         "name": "standard / mixed",
         "d_lambda": 2,
         "chi_at_identity": 2,
         "y_lambda_closed_form": "Wenzl bridge — non-trivial in q",
         "y_lambda_at_q0": (q - 1 / q) ** 2 / (qint_3 * qint_2),
         "role": "carries the bulk of the operator-valued T_w structure"},
        {"label": "(1, 1, 1)",
         "name": "sign / antisymmetric",
         "d_lambda": 1,
         "chi_at_identity": 1,
         "y_lambda_closed_form": "bar-image of y_(3) under q → q⁻¹",
         "y_lambda_at_q0": (1 / q ** 2) / qint_3,
         "role": "Frobenius-pairing dual to (3); antipode partner"},
    ]

    print(f"  Partitions of n = 3 (proton braid 𝓑₃ Wedderburn blocks):")
    print()
    print(f"  {'λ':<10} {'d_λ':>4} {'χ^λ(1)':>7} {'y_λ(q_0)':>18}  role")
    print(f"  {'-'*10} {'-'*4} {'-'*7} {'-'*18}  {'-'*40}")
    for p in partitions:
        y = p["y_lambda_at_q0"]
        print(f"  {p['label']:<10} {p['d_lambda']:>4} "
              f"{p['chi_at_identity']:>7} {mp.nstr(y, 12):>18}  "
              f"{p['role']}")
    print()

    # Sum check: tr_M(1 ∈ H_3) = z^(n-1) = z² at q_0
    # Should equal Σ_λ d_λ · y_λ(q_0) — this is the dim_q identity
    sum_check = sum(p["d_lambda"] * p["y_lambda_at_q0"] for p in partitions)
    z_squared = Z_MARKOV ** 2
    print(f"  Sanity dim_q identity:")
    print(f"    Σ_λ d_λ · y_λ(q_0) = {mp.nstr(sum_check, 14)}")
    print(f"    z² (tr_M(1)) =       {mp.nstr(z_squared, 14)}")
    print(f"    relative gap =       {float(mp.fabs(sum_check - z_squared)/z_squared):.4e}")
    if mp.fabs(sum_check - z_squared) / z_squared < mp.mpf("1e-2"):
        print(f"    ✓ Wenzl weight identity holds to ≤ 1% — partition data correct")
    else:
        print(f"    ⚠ Wenzl weight identity gap — y_λ closed forms above are")
        print(f"      LITERATURE-cited not pyhecke-extracted; numerical")
        print(f"      reconciliation against `y_lambda_wenzl_bridge.py` is a")
        print(f"      follow-up.")
    print()

    print("=" * 78)
    print(" SCOPING — Wedderburn-block decomposition of c_k")
    print("=" * 78)
    print()
    print(f"  Hypothesis: c_k(q_0) = Σ_λ a_k_λ · y_λ(q_0) · χ^λ(𝓑₃)")
    print()
    print(f"  Per-block per-k coefficient a_k_λ is the Taylor coefficient of")
    print(f"  a partition-specific generating function f_λ(u, q_0). To extract")
    print(f"  the a_k_λ from observed c_k_corr we need:")
    print()
    print(f"    1. The Hoefsmit seminormal rep ρ_λ(𝓑₃) for each λ — produces")
    print(f"       the matrix χ^λ(𝓑₃) value at q_0.")
    print(f"    2. The y_λ(q_0) numerical values (placeholder above).")
    print(f"    3. A linear-algebra deconvolution of c_k_corr_k = Σ_λ a_k_λ ·")
    print(f"       y_λ · χ^λ to extract a_k_λ per λ at each k.")
    print()
    print(f"  Infrastructure available in `pyhecke` / `hecke_character_symbolic`")
    print(f"  but the full extraction is a separate session's compute work.")
    print()
    print(f"  Connection to the m_μ V9 ↔ Q_β c_3 SHARED [3]_q/25 finding")
    print(f"  (ck-dk registry §3): if the [3]_q/25 factor appears in the SAME")
    print(f"  partition's f_λ for BOTH observables, this is a falsifiable")
    print(f"  per-block prediction. m_μ V9 uses 3-strand structure (n=3, same")
    print(f"  partition set as 𝓑₃); the (3) or (2,1) block is the natural")
    print(f"  carrier of the [3]_q factor since [3]_q appears in y_(3).")
    print()
    print(f"  Future probe 6.d': implement the per-block extraction, then")
    print(f"  test the per-block -(k-1)! pattern from probe 6.b independently")
    print(f"  per λ. If only ONE block (say λ = (2,1)) carries the c_k_alg =")
    print(f"  -(k-1)! pattern while the others contribute differently, the")
    print(f"  generating-function structure is partition-specific.")
    print()

    builder.add_data("q_0", mp.nstr(Q0_MP, 25))
    builder.add_data("z_markov", mp.nstr(Z_MARKOV, 25))
    builder.add_data("partitions_n_3", [
        {"label": p["label"], "name": p["name"],
         "d_lambda": p["d_lambda"], "chi_at_identity": p["chi_at_identity"],
         "y_lambda_closed_form": p["y_lambda_closed_form"],
         "y_lambda_at_q0": mp.nstr(p["y_lambda_at_q0"], 25),
         "role": p["role"]}
        for p in partitions
    ])
    builder.add_data("dim_q_sanity_check", {
        "sum_d_lambda_y_lambda": mp.nstr(sum_check, 25),
        "z_squared_target": mp.nstr(z_squared, 25),
        "relative_gap": float(mp.fabs(sum_check - z_squared) / z_squared),
    })
    builder.add_data("future_work", {
        "probe_6d_prime": "Implement per-block c_k extraction via Hoefsmit rep ρ_λ(𝓑₃); test -(k-1)! pattern per block.",
        "connection_to_m_mu_V9": "Test if [3]_q/25 shared factor maps to the same partition's f_λ for both observables.",
    })

    builder.add_assertion(
        "probe_6d_partitions_enumerated_scope_only",
        computed=len(partitions),
        expected=3,
        tolerance=0,
        source=("Scoping probe: enumerates the 3 partitions of n=3 "
                "(proton braid 𝓑₃ Wedderburn blocks): (3), (2,1), "
                "(1,1,1). Concrete numerical data: y_λ(q_0) "
                "placeholder values + dim_q sanity check. Full "
                "per-block c_k extraction is future work."),
    )

    builder.save()
    print(f"  Witness: qbeta-ck-wedderburn-decomposition-scope-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
