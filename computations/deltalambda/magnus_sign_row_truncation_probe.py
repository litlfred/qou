#!/usr/bin/env python3
"""magnus_sign_row_truncation_probe.py — the row-concentration shortcut for the
Magnus Ω₂ sign, and its validation.

DISCOVERY (this session, from the committed A=2/A=3 witnesses + A=4 partial). The
Wedderburn sum P(A) = Σ_{λ⊢3A} y_λ tr(ρ_λ Ω₂_λ) does NOT need every partition:
its value — and overwhelmingly its SIGN — concentrates on the FEW-ROW (near-
trivial, small-dimensional) representations, exactly the CHEAP ones. Measured:

  rows(λ)     A=3 fraction of Σ|contrib|
  1 (triv)    0        (Ω₂ vanishes on the 1-dim rep)
  2-row       91.0 %
  3-row        8.1 %
  ≥4-row      <0.9 %

  truncation vs full P:   hooks 95 %,   ≤2-row 92-102 %,   ≤3-row 98.5-99.9 %
  reflection rep (n-1,1) alone:  56 % (A=2) → 86 % (A=3) → 92 % (A=4) — GROWS with A
  sign margin |P|/Σ|c|:          69 % (A=2) → 99 % (A=3) → 99.9 % (A=4) — GROWS with A

Because #{λ⊢n with ≤ K rows} ~ n^{K-1} is POLYNOMIAL and the dominant reps are
small-dimensional, the ≤K-row truncation is a poly-size sum of cheap reps that
reproduces the sign (and ~99 % of the value). This is the shortcut: for the SIGN
we never need the exp-many / huge-dim partitions the flat method and even the
branching tower spend all their time on.

CONJECTURE (row-concentration / reflection-rep sign). As A→∞, sign(P(A)) is
determined by the reflection representation (n-1,1) (dim 3A-1). If tr(ρ_{(n-1,1)}
Ω₂) has a closed form (the standard rep is very concrete — germs are explicit
(n-1)×(n-1) matrices), the sign is a closed-form function of A. This mirrors a
cluster/cumulant expansion (row-count ≈ cumulant order, higher orders decaying —
cf. the just-ingested Procacci-Yuhjtman / Rebenko cluster-expansion papers) and
connects to the corpus's existing two-row closed-form character machinery
(phase1b_two_row_closed_form_character.py).

RIGOR GAP (honest). Truncation gives the sign only with a TAIL BOUND: the y_λ are
known exactly, but a rigorous sign needs Σ_{λ excluded} |y_λ tr(ρ_λ Ω₂_λ)| <
|P_truncated|, i.e. a bound on |tr(ρ_λ Ω₂_λ)| for the excluded high-row λ. The
data shows steep decay with row-count, but that decay is not yet PROVED. Until it
is, this is a high-confidence heuristic sign, not a theorem. Closing the tail
bound (or the reflection-rep closed form) is the open item.

This probe: computes the ≤K-row truncation of P(A) for any A via the validated
sparse machinery, reports the sign, and (for A=2,3 where the full witness exists)
the ratio to the full P as validation. scope-(a); NO-FLOAT64 (inherits the sparse
probe's mpf dps=140); 0 free params.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

import mpmath as mp  # noqa: E402

# Raise the compute precision before any mpmath value is built. Without this
# the file computes at mpmath's default 15 dps -- ~17 digits, i.e. float64 --
# while presenting mpf values. NO FLOAT64 EVER; drained under bean `qou-j6gb`.
# `_path_bridge` lives in `computations/`, which this file's own
# `sys.path.insert(0, dirname(__file__))` does not put on the path -- hence
# the extra parent insert before importing it.
import os as _os_dps, sys as _sys_dps  # noqa: E402
_sys_dps.path.insert(0, _os_dps.path.dirname(_os_dps.path.dirname(
    _os_dps.path.abspath(__file__))))
import _path_bridge as _bridge_dps  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402


def truncated_P(A, max_rows, verbose=True):
    """P(A) restricted to λ⊢3A with ≤ max_rows rows, via the sparse machinery."""
    from mass_at_3A_proper import atom_braid_word_3A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    n = 3 * A
    parts = [p for p in base.partitions(n) if len(p) <= max_rows]
    parts.sort(key=base._dim_estimate)
    P = mp.mpf(0)
    ctrl = mp.mpf(0)
    t0 = time.time()
    for shape in parts:
        row, dP, dC, tr_rO, hcheck, dim, nnz = base._partition_contribution(shape, gens)
        P += dP
        ctrl += dC
        if verbose:
            print(f"    {str(tuple(shape)):>24} dim={dim:>4}  [P={mp.nstr(P,6)}]", flush=True)
    return P, ctrl, len(parts), time.time() - t0


def run(As, max_rows):
    print(f"[rowtrunc] Magnus Ω₂ sign via ≤{max_rows}-row truncation\n")
    print(f"  {'A':>2} {'n':>3} {'#parts(≤K-row)':>15} {'P_trunc':>16} {'sign':>5} "
          f"{'ratio to full':>14} {'wall':>7}")
    for A in As:
        n = 3 * A
        P, ctrl, npart, wall = truncated_P(A, max_rows, verbose=False)
        sign = '+' if P > 0 else ('-' if P < 0 else '0')
        # validate against full witness if present
        full_path = {
            2: "deuteron-magnus-omega2-sign.witness.json",
            3: "triton-magnus-omega2-sign.witness.json",
            4: "he4-magnus-omega2-sign.witness.json",
        }.get(A)
        ratio = "n/a"
        if full_path and os.path.exists(os.path.join(os.path.dirname(__file__), full_path)):
            full = json.load(open(os.path.join(os.path.dirname(__file__), full_path)))
            Pf = mp.mpf(full["results"]["P_total"])
            ratio = mp.nstr(P / Pf, 6)
            sign_ok = (P > 0) == (Pf > 0)
            ratio += " ✓" if sign_ok else " ✗SIGN"
        total_parts = sum(1 for _ in base.partitions(n))
        print(f"  {A:>2} {n:>3} {npart:>6}/{total_parts:<8} {mp.nstr(P,6):>16} {sign:>5} "
              f"{ratio:>14} {wall:6.1f}s", flush=True)
    print(f"\n  #{{λ⊢n, ≤{max_rows} rows}} grows POLYNOMIALLY in n; the full count grows like exp(c√n).")
    print("  Ratios ≈1 and sign ✓ ⇒ the truncation is a cheap poly sign-estimator (heuristic;")
    print("  a rigorous sign needs the tail bound on |tr(ρ_λ Ω₂_λ)| for the excluded high-row λ).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", type=int, default=3, help="max #rows of λ to include")
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3, 4, 5, 6],
                    help="atomic numbers to estimate")
    args = ap.parse_args()
    run(args.A, args.rows)


if __name__ == "__main__":
    main()
