#!/usr/bin/env python3
"""
Molecular boiling points from the antisymmetric-channel cohesion (scope-(a) negative).

Companion to `phase_transition_q_ideal_gas.py`. That script feeds the bare
h²-suppressed H-bond cohesion into the q-ideal gas law

    P_q V_q = n_q R T   =>   T_boil = S_q^(∂) / ([2]_q R)

and over-predicts by 6-10x. This one replaces the h² factor with the
antisymmetric (directional H-bond) channel weight y0*, and finds the
over-prediction gets an order of magnitude WORSE, not better: ~10^4 K.

FINDING (scope-(a), per AGENTS.md §"Before declaring 'refuted'"): a purely
structural map from P_q V_q = n_q R T requires a much larger entropic /
topological denominator ΔS_vap than the bare [2]_q. This constrains the
magnitude of ΔS_vap; it does NOT exclude the antisymmetric channel, the
q-ideal gas law, or any ingredient of either -- neither term was tested in
combination with anything else.

WHAT THIS RECONSTRUCTION DOES NOT DO (read before citing it as an SDP result)
----------------------------------------------------------------------------
The witness this file regenerates was originally described as an SDP: "the
canonical LP-dual shadow price of the H_2(q) Wedderburn idempotents. The SDP
selects the antisymmetric e_- (directional H-bond) channel." That SDP
formulation is NOT recoverable and is NOT reconstructed here -- no constraint
matrix, objective, or Gram input survives anywhere in the repository, and the
original witness never carried the LP/SDP dual fields that AGENTS.md
§"LP / SDP duals" makes mandatory (`y_star`, `active_set`, `primal_obj`,
`dual_obj`, `duality_gap`); it recorded `y0_star` alone.

What IS established is that the recorded `y0_star` coincides, to every one of
the 16 digits it was serialized at, with the closed-form antisymmetric
linked-channel weight

    W_(1,1)(q) = (q³ + q² - q^{3/2}) / (q³ + q² + q + 1)

documented in `docs/audits/2026-06-01-inter-nucleon-linked-channel.md` (which
gives W_(1,1)(q₀) = 0.303675…). This file therefore computes y0* from that
closed form and says so. A coinciding value is not a re-derivation: if the
SDP route is ever wanted, it has to be built, and it must emit the full dual.

NOTE — W_(1,1) is NOT y_λ. The three partition-weight families y_λ / w_λ /
w̃_λ are distinct at q ≠ 1 (notation register). `y_lambda_at_q0_mpmath(2, q)`
returns y_(1,1) = 0.2473…, a different number; do not substitute it.

Reconstruction note (2026-08-16, bean qou-zdz5)
-----------------------------------------------
The original producer named in the witness was never committed -- not in any
of the 26276 commits, on any branch. The witness landed under
`folio-assistant/computations/` in 5cd90f065f and moved to `computations/` in
d27b002745, always without a script. At 58f27639, the commit the witness
stamps as its own, the tree's only phase-transition compute was
`phase_transition_q_ideal_gas.py`. So the producer lived in a working tree and
was never saved.

It was nonetheless fully reconstructible, because the equation is the sibling
script's with h² -> y0*: that reproduces all six recorded values
(three T_boil_pred, three ratios) bit-for-bit — but ONLY when q₀ is the stale
hardcoded 1.1099780333553254. That is the sibling's `except` fallback constant,
which means the original run could not import `qou_substrate.constants` and
silently used a q₀ five significant figures stale.

This file uses the live `q_at()` (the proton pin, per the standing
experimental-anchor directive). The recorded numbers therefore shift by
8.07e-07 relative (8.59e-07 on y0* itself) -- far below anything the finding
depends on, since the assertion is "> 10000 K" against ~1.7e4. The stale
constant is
deliberately not preserved: reproducing a bug byte-for-byte to make a diff
look clean is not reproduction.

Usage:
    python3 computations/phase_transition_sdp_derivation.py

Output:
    computations/phase-transition-sdp-derivation.witness.json
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

try:
    from qou_substrate.constants import q_at
except Exception:  # pragma: no cover - the substrate package is the norm
    raise SystemExit(
        "qou_substrate.constants is not importable. Refusing to fall back to a "
        "hardcoded q0: that silent fallback is exactly what staled the original "
        "run of this computation by five significant figures."
    )

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:  # pragma: no cover
    from witness_base import WitnessBuilder

# Raise precision at module scope, ABOVE the mpf constants below: an mpf built
# at import time is fixed at whatever dps was current then, so calling this
# inside main() would leave every constant at the default. `set_compute_dps` is
# idempotent. (import-time dps ratchet)
set_compute_dps()

R_GAS = mp.mpf("8.314462618")  # J / (mol K) — CODATA 2018 exact

# (E_cov kJ/mol, n_HB, T_boil_obs K) — same table as the q-ideal-gas sibling.
MOLECULES = {
    "H2O": (mp.mpf("460.0"), 2, mp.mpf("373.15")),
    "HF": (mp.mpf("565.0"), 1, mp.mpf("293.15")),
    "NH3": (mp.mpf("391.0"), 1, mp.mpf("239.81")),
}

T_BOIL_FLOOR = mp.mpf("10000")  # K — the threshold the finding asserts


def antisymmetric_channel_weight(q: mp.mpf) -> mp.mpf:
    """W_(1,1)(q) — the antisymmetric linked-channel weight, closed form.

    docs/audits/2026-06-01-inter-nucleon-linked-channel.md. NOT y_(1,1).
    """
    q = mp.mpf(q)
    return (q**3 + q**2 - q ** mp.mpf("1.5")) / (q**3 + q**2 + q + 1)


def main() -> int:
    t0 = time.monotonic()
    q0 = mp.mpf(q_at())
    dim_q = q0 + 1 / q0  # [2]_q
    y0_star = antisymmetric_channel_weight(q0)

    # `start_time` makes durationMs measure from the top of main() rather than
    # from the builder's construction. It does not change much here -- the
    # arithmetic above is genuinely sub-millisecond, and the ~1.2 s of wall this
    # script spends is inside `save()` (hashing, environment capture, the
    # float64 pre-check), which is after the clock stops either way.
    w = WitnessBuilder("phase-transition-sdp-derivation", engine="python",
                       start_time=t0)
    w.add_data("q0", fmt(q0))
    w.add_data("y0_star", fmt(y0_star))
    w.add_data("dim_q_bracket_2", fmt(dim_q))

    # The assertion is scoped to H2O, per its own `source` string. NH3 lands at
    # ~7.1e3 K, below the floor -- applying the floor to all three would make
    # the recorded assertion fail on a molecule it was never about.
    above_floor = False
    print("=" * 78)
    print("Boiling points from the antisymmetric-channel cohesion (NO FIT)")
    print(f"q0 = {mp.nstr(q0, 20)}   y0* = W_(1,1)(q0) = {mp.nstr(y0_star, 20)}")
    print("=" * 78)

    for name, (e_cov, n_hb, t_boil_obs) in MOLECULES.items():
        # Cohesion energy with the antisymmetric channel weight in place of h².
        s_q_boundary = n_hb * y0_star * e_cov * 1000
        t_boil_pred = s_q_boundary / (dim_q * R_GAS)
        boil_ratio = t_boil_pred / t_boil_obs

        if name == "H2O":
            above_floor = bool(t_boil_pred > T_BOIL_FLOOR)

        w.add_data(f"{name}_T_boil_pred", fmt(t_boil_pred))
        w.add_data(f"{name}_boil_ratio", fmt(boil_ratio))
        print(f"  {name:4s} T_boil(pred) = {mp.nstr(t_boil_pred, 12)} K"
              f" | obs = {mp.nstr(t_boil_obs, 8)} K"
              f" | {mp.nstr(boil_ratio, 8)}x")

    w.add_assertion(
        "SDP shadow price predicts temperatures far above empirical",
        computed=above_floor, expected=True,
        source="T_boil_pred > 10000 K for H2O",
    )

    w.set_description(
        "Boiling points from the q-ideal gas law with the antisymmetric "
        "(directional H-bond) channel weight y0* = W_(1,1)(q0) in place of the "
        "h2-suppressed cohesion of the sibling scan. Yields temperatures of order "
        "10^4 K, showing that a purely structural map from P_q V_q = n_q R T "
        "requires a much larger entropic/topological denominator dS_vap than the "
        "bare [2]_q. Scope-(a): this constrains the magnitude of dS_vap; it "
        "excludes neither the antisymmetric channel nor the q-ideal gas law. "
        "NOTE: the original witness framed y0* as an SDP LP-dual shadow price; "
        "that SDP is not recoverable and is NOT reconstructed here (see the module "
        "docstring). y0* is computed from the documented closed form, which matches "
        "the recorded value to all 16 serialized digits."
    )
    w.add_data("tier", "open")
    w.add_data(
        "y0_star_provenance",
        "closed form W_(1,1)(q) = (q^3+q^2-q^{3/2})/(q^3+q^2+q+1); "
        "docs/audits/2026-06-01-inter-nucleon-linked-channel.md. NOT an SDP solve, "
        "and NOT y_(1,1) (= 0.2473 at q0, a different weight family).",
    )
    w.add_data(
        "finding",
        "Substituting the antisymmetric channel weight for h2 makes the "
        "over-prediction worse, not better: ~30-45x observed rather than 6-10x. "
        "A derived topological factor for dS_vap is required. No fit applied. "
        "Status remains OPEN.",
    )

    out = w.save()
    print(f"\nWitness: {out}")
    print(f"allPassed: {above_floor}  ({int((time.monotonic() - t0) * 1000)} ms)")
    return 0 if above_floor else 1


if __name__ == "__main__":
    sys.exit(main())
