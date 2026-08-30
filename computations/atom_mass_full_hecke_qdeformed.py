#!/usr/bin/env python3
"""q-deformed three-channel Markov trace for the atom-mass-full-hecke remark.

Recomputes the ``tr_full`` column of ``rem:atom-mass-full-hecke`` with the
canonical **q-deformed Jones-Markov weights**

    ŷ_λ = y_λ(q) · d_λ          (Σ_λ ŷ_λ = 1)

(Wenzl Schur principal specialisation, ``prop:y-lambda-closed-form-wenzl-bridge``)
in place of the **classical** Wedderburn-Artin weights
d_λ²/|S₃| = {1/6, 2/3, 1/6}, which are only the q→1 limit.

    tr_full = ŷ_sym·tr_sym + ŷ_std·tr_std + ŷ_alt·tr_alt.

Scope: this script fixes the WEIGHT convention (classical → q-deformed), the
conflation flagged on PR #2481.  The per-channel traces tr_sym/tr_std/tr_alt
are the established per-atom three-channel values of the published table; they
are INHERITED here (an independent witness for the high-A χ^λ is a separate
open item — the Gröbner-Shirshov reducer is infeasible past the light nuclei,
so e.g. ²⁰Ne = H_60 cannot be recomputed canonically in-repo).  No fit, no
calibration: ŷ_λ is derived from q alone (CAL-2 substrate), the channel traces
are inherited data.

q = 111/100 — the block's convenience rational; the substrate q₀ ≈ 1.10998
gives weights identical to printed precision (Δŷ ~ 2e-5).

Usage:
    python3 computations/atom_mass_full_hecke_qdeformed.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import mpmath as mp  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

# Block convenience rational (exact); substrate q₀ ≈ 1.10998 gives the same
# weights to printed precision.
Q = mp.mpf(111) / mp.mpf(100)

# d_λ for the three S₃ irreps.
DIM = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}

# Inherited per-atom three-channel traces (tr_sym, tr_std, tr_alt) from the
# published rem:atom-mass-full-hecke table.  Weight-independent; recomputing the
# high-A χ^λ canonically is a separate open item.
CHANNELS = {
    "1H":  (1.000, 1.000, 1.000),
    "4He": (1.022, 0.122, 1.022),
    "7Li": (0.780, 0.006, -1.460),
    "9Be": (0.734, -0.00002, 1.692),
    "11B": (0.699, 0.000002, -1.984),
    "12C": (1.216, 0.000001, 1.216),
    "14N": (1.305, -4e-7, -1.305),
    "16O": (1.416, 0.101, 1.416),
    "19F": (0.638, 2e-7, -4.172),
    "20Ne": (1.722, 0.316, 1.722),
}


def q_deformed_weights():
    """Canonical ŷ_λ = y_λ(Q)·d_λ for H_3, with Σ ŷ_λ = 1."""
    y = y_lambda_at(3, Q)
    yhat = {}
    for k, v in y.items():
        kk = tuple(k) if isinstance(k, (list, tuple)) else k
        yhat[kk] = mp.mpf(str(v)) * DIM[kk]
    return yhat


def main() -> int:
    yhat = q_deformed_weights()
    ys, yd, ya = yhat[(3,)], yhat[(2, 1)], yhat[(1, 1, 1)]
    norm = ys + yd + ya

    classical = {"sym": mp.mpf(1) / 6, "std": mp.mpf(2) / 3, "alt": mp.mpf(1) / 6}

    print(f"q = 111/100   q-deformed effective weights ŷ_λ = y_λ·d_λ (Σ = {float(norm):.6f}):")
    print(f"  ŷ_sym = {float(ys):.6f}  (classical 1/6 = 0.166667)")
    print(f"  ŷ_std = {float(yd):.6f}  (classical 2/3 = 0.666667)")
    print(f"  ŷ_alt = {float(ya):.6f}  (classical 1/6 = 0.166667)")
    print()

    results = {}
    print(f"{'atom':6s} {'tr_full(classical)':>18s} {'tr_full(q-deformed)':>20s}")
    for name, (s, st, a) in CHANNELS.items():
        s_, st_, a_ = mp.mpf(str(s)), mp.mpf(str(st)), mp.mpf(str(a))
        cl = classical["sym"] * s_ + classical["std"] * st_ + classical["alt"] * a_
        qd = ys * s_ + yd * st_ + ya * a_
        # fmt, not float(): the channel traces are inherited decimal data and
        # the two tr_full columns are mpf sums. Casting either through float64
        # on the way into the witness is the raw-float64 ratchet, and it throws
        # away digits the 50-dps arithmetic above actually produced.
        results[name] = {"tr_sym": fmt(s_), "tr_std": fmt(st_), "tr_alt": fmt(a_),
                         "tr_full_classical": fmt(cl), "tr_full_qdeformed": fmt(qd)}
        print(f"{name:6s} {float(cl):>18.4f} {float(qd):>20.4f}")

    wb = WitnessBuilder("atom-mass-full-hecke", engine="mpmath")
    wb.data["q"] = "111/100"
    wb.data["weight_convention"] = "q-deformed Jones-Markov (Wenzl Schur principal specialisation)"
    wb.data["weight_source"] = "prop:y-lambda-closed-form-wenzl-bridge / y-lambda-at-q0.witness.json"
    wb.data["yhat"] = {"sym": fmt(ys), "std": fmt(yd), "alt": fmt(ya)}
    wb.data["yhat_classical_limit"] = {
        "sym": fmt(mp.mpf(1) / 6), "std": fmt(mp.mpf(2) / 3), "alt": fmt(mp.mpf(1) / 6)}
    wb.data["convention_D_cap"] = (
        "y_(1^3) = 0 EXACTLY -- the two-row cap, derived from the 2-dimensional "
        "mass fibre (FibreDimensionForcesTL.lean, bean qou-n1dj), not a small "
        "deformation of the classical 1/6. This producer was authored under "
        "convention C, where the alt weight was 0.0228 (~7.3x below classical) "
        "and its assertion divided by it; under D that division is by zero and "
        "the script crashed with ZeroDivisionError on main. The alt channel is "
        "not SUPPRESSED, it is ABSENT.")
    wb.data["channel_traces_provenance"] = (
        "inherited from published rem:atom-mass-full-hecke table; high-A χ^λ not "
        "independently witnessed (GS reducer infeasible past light nuclei)")
    wb.data["atoms"] = results
    # NOT float(norm). The residual `norm - 1` is exactly 0 at 60 dps, but a
    # float64 cast throws away the evidence for that: any mpf residual below
    # ~1e-16 rounds to exactly 1.0, so under a cast the 1e-25 tolerance does no
    # work and the assertion would pass identically on a value that missed by
    # 1e-20. Compared as mpf, the tolerance resolves what it claims to.
    wb.add_assertion("qdeformed_weights_normalised",
                     computed=norm, expected=mp.mpf(1), tolerance=mp.mpf("1e-25"),
                     source="Σ_λ y_λ d_λ = tr_M(1) = 1")
    # WAS: `alt_channel_suppressed_vs_classical`, computing (1/6)/ŷ_alt > 5.
    # Under convention D that is a division by ZERO -- ŷ_alt is identically 0,
    # not merely small -- and the producer crashed. The honest replacement
    # asserts the cap itself, which is the actual structural content: the alt
    # channel does not contribute at all, so the trace is two-row.
    wb.add_assertion("alt_channel_vanishes_two_row_cap",
                     computed=ya, expected=mp.mpf(0), tolerance=mp.mpf("1e-40"),
                     source="ŷ_(1^3) = 0 exactly under convention D (two-row cap, "
                            "derived from the 2-dim mass fibre; qou-n1dj)")
    wb.add_assertion("two_row_weights_carry_all_of_the_trace",
                     computed=ys + yd, expected=mp.mpf(1), tolerance=mp.mpf("1e-40"),
                     source="with ŷ_alt = 0, Σ_λ ŷ_λ = 1 is carried by (3) and (2,1) alone")
    wb.save()
    print("\n✓ Witness: atom-mass-full-hecke.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
