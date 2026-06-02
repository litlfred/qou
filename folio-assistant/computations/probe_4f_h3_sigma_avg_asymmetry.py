#!/usr/bin/env python3
"""
Probe (4f): test hypothesis H3 (σ_avg drives the transpose-pair
asymmetry).

For the transpose pair (3,3,3,3,2,2,2) ↔ (7,7,4) at A=6, the
observed asymmetry is Δ = +20.72. Hypothesis H3 says this is driven
by the 13/71 σ_avg crossings in T_w_⁶Li carrying bar-anti-symmetric
content, which favours tall-narrow shapes.

This probe constructs MODIFIED braid words from the canonical
T_w_⁶Li by replacing each σ_avg = σ − h/2·I by either:
  (a) σ (positive only — drops anti-symmetric content)
  (b) σ⁻¹ = σ − h·I (negative only)
  (c) Identity (σ - σ + 1 = 1 — drops the crossing entirely)
And measures the transpose-pair asymmetry in each variant.

If Δ collapses toward zero under variants (a)/(b)/(c), H3 is
strongly supported: σ_avg carries the asymmetry.
If Δ stays large, H3 is falsified; H1 or H2 is the carrier.

Audit-only.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as q0
from probe_4_li6_rectangular_python import build_seminormal_fast, apply_T_w, apply_T_w_T


def modify_word_replace_avg(word, mode: str, h: float):
    """Replace σ_avg crossings (c, d=−h/2) by:
       mode='pos' → (c=1, d=0)   = σ
       mode='neg' → (c=1, d=−h)  = σ⁻¹
       mode='id'  → (c=0, d=1)   = I  (skips the crossing)
    Returns modified word.
    """
    new_word = []
    n_replaced = 0
    for (c, d, g) in word:
        # Is this a σ_avg? c=1, d ≈ -h/2
        if abs(c - 1.0) < 1e-9 and abs(d - (-h / 2)) < 1e-6:
            n_replaced += 1
            if mode == "pos":
                new_word.append((1.0, 0.0, g))
            elif mode == "neg":
                new_word.append((1.0, -h, g))
            elif mode == "id":
                new_word.append((0.0, 1.0, g))
            else:
                raise ValueError(mode)
        else:
            new_word.append((c, d, g))
    return new_word, n_replaced


def compute_min_eig(shape, word, q: float):
    sigmas, dim = build_seminormal_fast(shape, q)
    sigmas_T = [sg.T.tocsr() for sg in sigmas]

    def matvec(v):
        return 0.5 * (apply_T_w(v, sigmas, word, 0.0)
                      + apply_T_w_T(v, sigmas_T, word, 0.0))

    L = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)
    w_min = eigsh(L, k=1, which="SA", maxiter=2000, tol=1e-6, return_eigenvectors=False)
    return float(w_min[0])


def main():
    h = float(q0) - 1.0 / float(q0)
    canonical_word = atom_braid_word_3A(3, 3)
    print(f"⁶Li canonical T_w: {len(canonical_word)} crossings, h={h:.6f}")

    # Transpose-pair test
    pairs = [
        ((3, 3, 3, 3, 2, 2, 2), (7, 7, 4)),
    ]

    variants = ["canonical", "pos", "neg", "id"]

    print(f"\n{'pair':>40s}  {'variant':>10s}  {'tall min_eig':>12s}  {'wide min_eig':>12s}  Δ_asymm")

    results = {}
    for (tall, wide) in pairs:
        for v in variants:
            if v == "canonical":
                word_v = canonical_word
                n_repl = 0
            else:
                word_v, n_repl = modify_word_replace_avg(canonical_word, v, h)

            t0 = time.time()
            me_tall = compute_min_eig(tall, word_v, float(q0))
            me_wide = compute_min_eig(wide, word_v, float(q0))
            dt = time.time() - t0
            asymm = abs(me_tall) - abs(me_wide)
            results[(tall, wide, v)] = (me_tall, me_wide, asymm, n_repl, dt)
            pair_str = f"{list(tall)}↔{list(wide)}"
            print(f"{pair_str:>40s}  {v:>10s}  {me_tall:>+12.4f}  {me_wide:>+12.4f}  {asymm:+8.4f}  (replaced {n_repl}; {dt:.1f}s)")

    # Verdict
    print(f"\n=== Verdict ===")
    canon_asymm = results[(tall, wide, "canonical")][2]
    for v in ["pos", "neg", "id"]:
        var_asymm = results[(tall, wide, v)][2]
        reduction = (canon_asymm - var_asymm) / canon_asymm if canon_asymm != 0 else 0
        print(f"  variant {v:>10s}: Δ = {var_asymm:+.4f}  ({reduction * 100:+.1f}% change from canonical {canon_asymm:+.4f})")

    out = WitnessBuilder("probe-4f-h3-sigma-avg-asymmetry", engine="python")
    out.set_description(
        "Tests Hypothesis H3 (σ_avg carries the transpose-pair "
        "asymmetry) at the critical pair (3,3,3,3,2,2,2) ↔ (7,7,4) "
        "by replacing σ_avg crossings with σ, σ⁻¹, or identity, and "
        "measuring how the asymmetry changes."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-transpose-pair-asymmetry-categorical.md"
    )
    out.set_content_block("conj:psd-trace-orthogonality")

    out.add_data("variant_min_eigs", {
        f"{list(tall)}_{v}": {
            "tall_shape": list(tall),
            "wide_shape": list(wide),
            "variant": v,
            "tall_min_eig": results[(tall, wide, v)][0],
            "wide_min_eig": results[(tall, wide, v)][1],
            "asymmetry": results[(tall, wide, v)][2],
            "n_avg_replaced": results[(tall, wide, v)][3],
        }
        for v in variants
    })

    abs_canon = abs(canon_asymm)
    max_reduction = max(
        abs(canon_asymm - results[(tall, wide, v)][2]) / abs_canon
        if abs_canon > 0 else 0
        for v in ["pos", "neg", "id"]
    )

    out.add_assertion(
        name="sigma_avg_partially_drives_asymmetry",
        computed=str(int(max_reduction > 0.3)),
        expected="1",
        tolerance=0,
        source=f"max |Δ_canonical − Δ_variant| / |Δ_canonical| across variants = {max_reduction:.4f}; threshold 0.3",
    )

    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
