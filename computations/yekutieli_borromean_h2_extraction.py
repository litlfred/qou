#!/usr/bin/env python3
"""EXPLORATORY (canonical infrastructure, unproved numerical claim).

Yekutieli finite-slice multiplicative integral for the Borromean braid.

Implements the non-abelian Stokes curvature extraction directly from
the Hecke algebra, following `atom-knot-mass-derivation.md`:

  "The Hecke quadratic relation σ_i² = (q − q⁻¹)σ_i + 1 IS the
   curvature 2-form of non-abelian Stokes at adjacent slices."

The curvature at each crossing is the DEVIATION of the Hecke relation
from the symmetric-group relation (σ_i² = 1):

  F_i := σ_i² − 1 = (q − q⁻¹)σ_i = h · σ_i

At h² order, the total integrated curvature over the Borromean
surface is Σ_crossings (curvature contribution), where each crossing
contributes an h-dependent factor.

For the canonical Borromean braid (σ₁σ₂⁻¹)³ on 3 strands, the 6
crossings yield a specific h² coefficient from the Markov trace of
the curvature-accumulated product.

This script computes that coefficient and compares to −G (Catalan).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

G = mp.catalan


def borromean_markov_trace_at_q(q: mp.mpf) -> mp.mpf:
    """Markov trace of the canonical Borromean braid (σ₁σ₂⁻¹)³ on H_3(q).

    The Borromean braid β = (σ₁σ₂⁻¹)³ in B_3.

    In H_3(q) with Hecke relation σᵢ² = (q−q⁻¹)σᵢ + 1:
      σᵢ⁻¹ = σᵢ − (q − q⁻¹)  (from the Hecke relation)

    The Markov trace tr_M on H_n(q) satisfies:
      tr_M(1) = 1
      tr_M(a · σ_{n-1}^{±1}) = z · tr_M(a)  where z = 1/(q^{1/2} + q^{-1/2})
      tr_M(ab) = tr_M(ba)  (trace property)

    We compute tr_M((σ₁σ₂⁻¹)³) by reducing in H_3(q) using braid
    and Hecke relations, then applying the Markov trace.
    """
    qi = mp.mpf(1) / q
    h = q - qi  # h = q − q⁻¹
    sq = mp.sqrt(q)
    sqi = mp.mpf(1) / sq
    z = mp.mpf(1) / (sq + sqi)  # Markov parameter

    # In H_3(q), work with the basis {1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁}
    # using σᵢ² = h·σᵢ + 1 and σ₁σ₂σ₁ = σ₂σ₁σ₂ (braid relation).

    # σ₂⁻¹ = σ₂ − h (Hecke inverse)
    # σ₁σ₂⁻¹ = σ₁(σ₂ − h) = σ₁σ₂ − h·σ₁

    # (σ₁σ₂⁻¹)² = (σ₁σ₂ − h·σ₁)²
    # Let A = σ₁σ₂, B = σ₁.
    # (A − hB)² = A² − h(AB + BA) + h²B²

    # A² = (σ₁σ₂)² = σ₁(σ₂σ₁)σ₂ = σ₁(σ₁σ₂σ₁ · σ₁⁻¹ · σ₁)σ₂
    #     ... this gets complex. Let me use the direct Hecke algebra multiplication.

    # Actually, let me just use markov_peel's existing infrastructure for a simpler approach:
    # evaluate the SYMBOLIC Markov trace at specific q values.

    # The expression from markov_peel for the proton (Z=1, N=0) braid:
    # tr_M = q⁹/4 + q/4 + (terms with z = 1/(√q + 1/√q)) − 1/(4q) − 1/(4q⁹)
    #
    # But that's the PROTON braid, not the simple Borromean (σ₁σ₂⁻¹)³.
    # The proton's canonical braid is more complex (11 crossings).
    #
    # For the pure Borromean braid (σ₁σ₂⁻¹)³, I need to compute from scratch.
    # Let me use the Burau matrix representation instead.

    # Jones polynomial of the Borromean rings via Burau:
    # The reduced Burau representation of B_3 is 2×2 over ℤ[t^±1] with t = −q.
    # σ₁ → [[1-t, 1], [0, 1]] (but this is for the UNREDUCED Burau...)

    # Simpler: use the Kauffman bracket / Jones polynomial directly.
    # Jones polynomial of Borromean rings (3-component link):
    # V(B_3; t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³
    # where t = q² (standard Jones variable).

    # The Jones polynomial IS the Markov trace (up to normalization):
    # J_L(q) = (−1)^{n−1} · (q^{1/2} + q^{-1/2})^{n−1} · tr_M(β_L)
    # where n = number of strands and β_L is the braid whose closure is L.

    # For B_3 as closure of (σ₁σ₂⁻¹)³ on n=3 strands:
    # J_{B_3}(q) = (−1)² · (q^{1/2} + q^{-1/2})² · tr_M((σ₁σ₂⁻¹)³)
    # = (q + 2 + q⁻¹) · tr_M(β_{B_3})

    # So tr_M(β_{B_3}) = J_{B_3}(q) / (q + 2 + q⁻¹)

    # Jones polynomial of Borromean rings at variable q (standard: t = q²):
    # V(t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³
    # With t = q²:
    t = q ** 2
    ti = qi ** 2
    jones = -ti**3 + 3*ti**2 - 2*ti + 4 - 2*t + 3*t**2 - t**3

    # Normalization: tr_M = J / (q^{1/2} + q^{-1/2})^{n-1} · (−1)^{n-1}
    # For n=3: (−1)² = 1, (q^{1/2} + q^{-1/2})² = q + 2 + q⁻¹
    norm = (sq + sqi) ** 2  # = q + 2 + q⁻¹
    return jones / norm


def main() -> int:
    t_start = time.monotonic()

    print("=" * 90)
    print("Yekutieli finite-slice: Borromean braid Markov trace h² extraction")
    print("=" * 90)
    print()

    # Compute at q near 1 and at substrate q_0
    import json
    # q₀ from q_parameter (proton pin, AGENTS.md 2026-08-07 directive).
    # Was a direct read of q-pinning-50-digit.witness.json, which is the
    # MUON anchor’s definition and bypasses the manifest entirely.
    q0 = Q_MP
    tr_q0 = borromean_markov_trace_at_q(q0)
    print(f"  tr_M(β_Borromean, q_0) = {mp.nstr(tr_q0, 20)}")
    print(f"  |tr_M| at q_0          = {mp.nstr(abs(tr_q0), 15)}")
    print()

    # h² coefficient extraction via mpmath.diff
    def tr_as_fn_of_h(h_val):
        h = mp.mpf(h_val)
        q = (h + mp.sqrt(h ** 2 + 4)) / 2
        return borromean_markov_trace_at_q(q)

    tr_at_0 = tr_as_fn_of_h(0)
    d2 = mp.diff(tr_as_fn_of_h, 0, 2)
    kappa = d2 / 2

    print(f"  tr_M(β_Borromean, q=1)  = {mp.nstr(tr_at_0, 15)}")
    print(f"  d²(tr_M)/dh² at h=0    = {mp.nstr(d2, 15)}")
    print(f"  κ = d²/2               = {mp.nstr(kappa, 15)}")
    print()
    print(f"  Comparison targets:")
    print(f"    −G (Catalan)          = {mp.nstr(-G, 15)}")
    print(f"    +3/4 (Family A)       = {mp.nstr(mp.mpf(3)/4, 15)}")
    print(f"    +87/64 (proton braid) = {mp.nstr(mp.mpf(87)/64, 15)}")
    print()

    diff_vs_G = kappa + G
    ratio_vs_G = kappa / (-G)
    print(f"  κ − (−G) = {mp.nstr(diff_vs_G, 12)}")
    print(f"  κ / (−G) = {mp.nstr(ratio_vs_G, 12)}")
    print()

    # Check if κ is a clean rational
    # Try to identify as p/q with small denominators
    frac = mp.identify(kappa, tol=1e-25)
    print(f"  mpmath.identify(κ) = {frac}")

    # Also sweep q to see the full shape
    print()
    print("  q sweep:")
    print(f"  {'q':<14}{'h':<14}{'tr_M':>16}{'Δ from tr(1)':>16}{'Δ/h²':>16}")
    print("  " + "-" * 76)
    for q_str in ["1.001", "1.005", "1.01", "1.02", "1.05", "1.10"]:
        q = mp.mpf(q_str)
        h = q - 1/q
        tr = borromean_markov_trace_at_q(q)
        delta = tr - tr_at_0
        ratio = delta / h**2 if h > 0 else mp.mpf(0)
        print(f"  {mp.nstr(q, 6):<14}{mp.nstr(h, 8):<14}"
              f"{mp.nstr(tr, 12):>16}{mp.nstr(delta, 10):>16}{mp.nstr(ratio, 10):>16}")

    # Witness
    w = WitnessBuilder(
        "yekutieli-borromean-h2-extraction",
        engine="mpmath",
        start_time=t_start,
    )
    w.set_description(
        "Computes the h² Taylor coefficient of the Borromean braid "
        "Markov trace tr_M((σ₁σ₂⁻¹)³, q) via the Jones polynomial "
        "of the Borromean rings, V(t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 "
        "− 2t + 3t² − t³ at t = q². The h² coefficient κ is compared "
        "against the Yekutieli conjecture's claimed −G (Catalan "
        "constant = Vol(𝓑₃)/8)."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("braid", "(σ₁σ₂⁻¹)³ = canonical Borromean braid on B_3")
    w.add_parameter("jones_polynomial",
                    "V(t) = −t⁻³ + 3t⁻² − 2t⁻¹ + 4 − 2t + 3t² − t³")
    w.add_parameter("tr_M_at_q_1", mp.nstr(tr_at_0, 20))
    w.add_parameter("kappa_h2", mp.nstr(kappa, 20))
    w.add_parameter("minus_G", mp.nstr(-G, 20))
    w.add_parameter("kappa_minus_G_diff", mp.nstr(diff_vs_G, 15))
    w.add_parameter("kappa_over_minus_G", mp.nstr(ratio_vs_G, 15))

    # The assertion this replaces was `computed=kappa, expected=-G,
    # tolerance=max(|kappa|,|G|)*2`. That bound is a THEOREM, not a threshold:
    # |c - e| <= |c| + |e| <= 2*max(|c|,|e|) for all real values, so it passed
    # for every possible kappa and reported `allPassed: true` while kappa
    # (0.1875) and its expected value (-0.9159...) did not even share a sign.
    # It was also this witness's ONLY raw-float64 field, because
    # max(abs(float(...)), ...) computes in float64 — one expression carrying
    # both defects. Bean `qou-t0wm`; audit
    # docs/audits/2026-09-05-tolerance-that-bounds-its-own-residual.md.
    #
    # Strings in, per the drained convention (qou-t0rf): `passed` coerces with
    # float() either way, but the witness then records the mpmath value rather
    # than a float64 shadow of it.
    kappa_exact = mp.mpf(3) / 16

    # What the run actually establishes. `mpmath.identify(kappa) = (3/16)` was
    # already being PRINTED by this producer and asserted nowhere; verified
    # here as exact rather than as a PSLQ guess — kappa - 3/16 is 0.0 at
    # dps = 30, 50 and 80 alike. Falsifiable: a change to the Jones polynomial
    # or to the Markov trace breaks it.
    w.add_assertion(
        "kappa_is_three_sixteenths",
        computed=fmt(kappa),
        expected=fmt(kappa_exact),
        tolerance="1e-40",
        unit="h² coefficient",
        source="d²(tr_M(Borromean))/dh² / 2; exact at dps 30/50/80",
    )

    # The Yekutieli claim itself, stated so it CAN fail — and it does, by 121 %.
    # AGENTS.md asks for the honest negative explicitly; a red assertion here is
    # the correct state, not something to tune away. SCOPE (a): this braid's h²
    # coefficient, computed this way, is not -G. Nothing here excludes the
    # Catalan constant from some other route into the framework.
    w.add_assertion(
        "yekutieli_kappa_equals_minus_G",
        computed=fmt(kappa),
        expected=fmt(-G),
        tolerance="1e-40",
        unit="h² coefficient",
        source="Yekutieli conjecture: κ = −G (Catalan) = −Vol(𝓑₃)/8",
    )

    out = w.save()
    print()
    print(f"Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
