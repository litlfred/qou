#!/usr/bin/env python3
"""chi_atom_fmatrix_recoupling — design + validation harness for the
scalable ATOM-config χ^λ via F-matrix recoupling (the step-[3] core).

CONTEXT (PRs #2080 §scaling, #2092 foundation; audit
docs/audits/2026-06-09-large-A-chi-bottleneck-scaling-plan.md §8a/§8b):

  * The FREE-config χ already scales (chi_free_via_lr, validated 50-dps ε,
    ⁶Li 3.8 s) — parabolic character formula, nucleon-cache + active-set LR.
  * The ATOM config adds the inter-nucleon junction σ at each block
    boundary, which couples adjacent (H_3)-blocks. The current per-λ paths
    (chi_q_atomic / chi_lambda_*_mpfr) are per-basis-vector traces,
    O(L·d_λ²) ⇒ L·n!/atom — the 3.6-year wall at ⁶Li (d_max=16,336,320).

WHY EXTRACTION IS A DEAD END (confirmed this session):
  Re-extracting the junction A^λ_{ξν} at each level needs a test-word
  basis large enough to span End(V_ξ), i.e. the SAME basis-size bottleneck
  that makes the per-basis-vector path infeasible at large A. Extraction —
  at f64 OR MPFR — does not scale.

THE SCALABLE PATH — F-matrix recoupling:
  The junction operator is LOCAL (a single σ at the boundary). Build the
  atom χ as a transfer matrix that chains the SINGLE validated H_6 junction
  via the Hecke recoupling (F-matrix / 6j) — never re-extracting and never
  materialising d_λ. Per-λ cost → the running Bratteli multiplicity
  (Σ_ξ m_k[ξ] = 90M at ⁶Li; minutes at MPFR), per audit §8b.

  χ^λ(β_atom) = transfer-contract over the GZ flag ξ_1⊂ξ_2⊂…⊂ξ_A=λ of
    [ nucleon op on block k  (diagonal → χ^{μ_k} on the interior) ]
    [ junction σ_{3k}        (the H_6 junction, recoupled to the running ξ) ]
  with the recoupling F^λ relating the fusion trees ((…)μ_k)μ_{k+1} vs
  (…)(μ_k μ_{k+1}). The F-matrices are determined by the seminormal rep of
  the SMALL fusions (H_6, H_9), computable from char_fast at MPFR.

CONFIRMED PRIMITIVES (this session):
  * MPFR seminormal: char_fast `_compiled_sigmas(shape,"mpmath50")` +
    `chi_lambda_fast_mp` — verified ≡ pyhecke_native to 1e-15 (see
    `validate_toolchain` below). This is the building block for the
    F-matrices (small shapes only — never the full d_λ).
  * Oracles for A ≤ 4: the cached chi-{atom}-h{n} MPFR witnesses
    (validate the recoupling output at each A before applying to ⁶Li/⁷Li).

IMPLEMENTATION ORDER (each validated against the oracle before the next):
  (a) H_6 single junction in the (μ,ν) GZ basis from char_fast MPFR
      seminormal (NOT extraction) — the local tensor. Validate: reproduces
      the deuteron atom χ.
  (b) H_9 F-matrix recoupling: derive the H_9 junction from the H_6 local
      tensor + recoupling; validate vs the existing H_9 nn/pn extracts AND
      the tritium/³He χ oracles (no H_9 extraction used).
  (c) transfer contraction over A blocks with the running multiplicity;
      validate ⁴He vs oracle.
  (d) apply to ⁶Li/⁷Li (no oracle; validated method) at canonical MPFR.

NO float64 on the canonical path (owner ruling 2026-06-09); the f64
seminormal is admissible only as a small-shape structural cross-check.

This module currently provides the DESIGN + the VALIDATION HARNESS the
implementation is built against. The F-matrix construction (steps a–d) is
the focused continuation.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

ATOM_ORACLE = {
    "D": "chi-deuteron-h6-at-q0-50dps.witness.json",
    "T": "chi-tritium-h9-at-q0-50dps.witness.json",
    "3He": "chi-helium-3-h9-at-q0-50dps.witness.json",
    "4He": "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def load_atom_oracle(atom: str, dps: int = 50) -> dict[tuple, "mp.mpf"]:
    """Cached MPFR atom χ^λ — the per-A validation target for recoupling."""
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    f = HERE / ATOM_ORACLE[atom]
    d = json.loads(f.read_text())
    bp = d.get("by_partition") or d["data"]["by_partition"]
    return {tuple(p["partition"]): mp.mpf(str(p["chi_lambda"])) for p in bp}


def validate_toolchain(dps: int = 50) -> bool:
    """Confirm the MPFR-seminormal primitive: char_fast `chi_lambda_fast_mp`
    ≡ pyhecke_native (chi_cd_mpfr) for the deuteron word, to ~1e-(dps-2).
    This is the building block the F-matrix construction relies on.
    """
    from char_fast import chi_lambda_fast_mp
    from chi_cd_mpfr import chi_all_partitions_cd_mpfr
    from mass_at_3A_proper import atom_braid_word_3A
    from q_parameter import Q_50_DIGIT_STR
    from lr_coefficients import partitions_of
    mp.mp.dps = max(mp.mp.dps, dps)
    q = mp.mpf(Q_50_DIGIT_STR)
    word = atom_braid_word_3A(1, 1)
    native = chi_all_partitions_cd_mpfr(6, word, dps=dps)
    max_rel = mp.mpf(0)
    for lam in partitions_of(6):
        lam = tuple(lam)
        cf = chi_lambda_fast_mp(lam, word, q).real
        nv = native[lam]
        if nv != 0:
            max_rel = max(max_rel, abs(cf - nv) / abs(nv))
    ok = max_rel < mp.mpf(10) ** -12
    print(f"  char_fast(mpmath) ≡ pyhecke_native on deuteron word: "
          f"max_rel={mp.nstr(max_rel, 4)}  {'OK' if ok else 'MISMATCH'}")
    return ok


if __name__ == "__main__":
    set_compute_dps()
    print("F-matrix recoupling — validation harness (design in module docstring)")
    ok = validate_toolchain()
    for atom in ("D", "T", "3He", "4He"):
        o = load_atom_oracle(atom)
        print(f"  oracle {atom:<4}: {len(o)} λ loaded "
              f"(χ^(n)={mp.nstr(next(iter(o.values())), 8)})")
    print("  harness ready; F-matrix construction (steps a–d) is the continuation.")
    sys.exit(0 if ok else 1)
