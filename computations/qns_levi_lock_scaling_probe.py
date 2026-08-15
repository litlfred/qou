#!/usr/bin/env python3
"""qns_levi_lock_scaling_probe — ladder scaling of the hyperbolic-overlap Levi lock.

EXPLORATORY PROBE (not production).

Corpus mechanism (`rem:hyperbolic-overlap-saturation`): when two anti-parallel
vortex cores overlap, the flow becomes a hyperbolic stagnation-point flow and
the squared Levi condition number LOCKS at kappa^2 = pi*nu/Gamma > 0 — contact
non-degeneracy survives at every fixed q (authored as the branch-A candidate).

This probe records what that lock formula implies ON THE LADDER q -> 1: with
nu = nu_q = (q-1)/(2q) -> 0 and Gamma fixed (data-dependent circulation),
C_L(eps) = 1/kappa^2_lock = Gamma/(pi*nu_q) ~ (2*Gamma/pi)*eps^{-1}, so the
growth exponent beta = dlog C_L/dlog(1/eps) -> 1: BRANCH B of
conj:levi-degeneracy (regular classical limit) — IF the lock formula is the
correct asymptotic uniformly along the ladder.

Honest scope: this is the corpus's own formula evaluated on the ladder — an
in-model tension flag (the block was authored pro-A; its nu-scaling points to
B in the limit), NOT a resolution of conj:levi-degeneracy. Consistent with the
merged results: the obstruction is nonzero at every fixed q != 1; only the
q -> 1 limit flattens. Precision tier: float64 (exact rational formula).

Run: python3 -u computations/qns_levi_lock_scaling_probe.py 2>&1 | tee /tmp/qns_levi_lock.log
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:
    from witness_base import WitnessBuilder

try:
    from _precision import fmt  # noqa: E402
except Exception:  # pragma: no cover - fallback keeps the probe runnable
    def fmt(value, dps=None, strip_zeros=False):  # type: ignore[misc]
        return str(value)


def _f(x):
    """Serialize float64-tier values as strings.

    Witnesses must not carry raw float64 (AGENTS.md §"QA is agent-owned";
    `computations/witness_raw_float64_audit.py`). This probe's declared tier is
    *"float64 (exact rational formula)"* — there is no integrator, so the
    `float64-integrator` carve-out (`qou-7kq3`) does **not** apply and
    serialization is the right treatment: `_precision.fmt` renders a float via
    `str()`, which round-trips exactly. Non-floats pass through untouched so
    counts and flags keep their JSON types.
    """
    return fmt(x) if isinstance(x, float) else x


GAMMA = 1.0  # circulation (fixed data-dependent constant; scaling is Gamma-independent)
EPS_LADDER = [10.0 ** (-e) for e in range(1, 9)]


def main() -> None:
    w = WitnessBuilder("qns-levi-lock-scaling-probe", engine="python")
    print("=" * 76)
    print("Levi-lock ladder scaling: C_L = Gamma/(pi*nu_q) on eps = q-1 -> 0 (EXPLORATORY)")
    print("=" * 76)
    xs, ys = [], []
    for eps in EPS_LADDER:
        q = 1.0 + eps
        nu_q = (q - 1.0) / (2.0 * q)
        kappa2_lock = math.pi * nu_q / GAMMA
        C_L = 1.0 / kappa2_lock
        xs.append(-math.log(eps))
        ys.append(math.log(C_L))
        w.add_data(f"eps_{eps:.0e}_kappa2_lock", _f(kappa2_lock))
        w.add_data(f"eps_{eps:.0e}_C_L", _f(C_L))
        print(f"  eps={eps:.0e}  nu_q={nu_q:.3e}  kappa2_lock={kappa2_lock:.3e}  C_L={C_L:.6e}")
    n = len(xs)
    xb, yb = sum(xs) / n, sum(ys) / n
    beta = sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum((x - xb) ** 2 for x in xs)
    w.add_data("beta_fit", _f(beta))
    print(f"  -> fitted beta = {beta:.5f}  (branch A: 0; branch B: 1; marginal: (0,1))")

    w.add_assertion(
        "Lock formula implies beta = 1 on the ladder (branch B) to within 0.01",
        computed=(abs(beta - 1.0) < 0.01), expected=True,
        source="C_L = Gamma/(pi*nu_q) with nu_q=(q-1)/(2q); kappa2_lock -> 0 linearly in eps",
    )
    w.add_assertion(
        "Lock stays strictly positive at every fixed eps > 0 (non-degenerate at fixed q)",
        computed=all((math.pi * ((1 + e - 1) / (2 * (1 + e))) / GAMMA) > 0 for e in EPS_LADDER),
        expected=True,
        source="kappa2 = pi*nu/Gamma > 0 for nu > 0 — consistent with obstruction != 0 at fixed q",
    )
    w.set_description(
        "Ladder scaling of the hyperbolic-overlap Levi lock (rem:hyperbolic-overlap-"
        "saturation): kappa^2_lock = pi*nu_q/Gamma with nu_q=(q-1)/(2q). At every fixed "
        "q>1 the lock is strictly positive (contact non-degeneracy survives — the "
        "block's pro-branch-A reading). But on the ladder eps->0 the lock vanishes "
        "linearly, so C_L = 1/kappa^2 ~ (2Gamma/pi) eps^{-1}, i.e. growth exponent "
        "beta = 1 — BRANCH B (regular classical limit) of conj:levi-degeneracy — IF "
        "the lock formula is the correct uniform asymptotic. Recorded as an in-model "
        "TENSION FLAG (the corpus argues branch A; its own formula's nu-scaling points "
        "to B in the limit), not a resolution. Exploratory tier; float64 exact formula."
    )
    w.add_data("tier", "exploratory")
    w.add_data("finding",
               f"beta_fit={beta:.5f}: the corpus lock formula implies branch B on the "
               "ladder; positive lock at fixed q is consistent with branch-A reading "
               "at fixed q. Tension flagged, conj:levi-degeneracy NOT resolved.")
    w.save()
    print("Saved witness: qns-levi-lock-scaling-probe.witness.json")


if __name__ == "__main__":
    main()
