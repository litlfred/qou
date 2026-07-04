#!/usr/bin/env python3
"""qbeta_zeta4_faithful_odd_probe.py — bean 0zr0: the ζ₄-faithfulness
constraint on the bar-odd (Q_β) sector, tested exactly at ORD = 17.

Post h·D(ũ) + h³·F(ũ) refutation (bean 08ds, `qbeta_bar_split_ord17_probe`):
the (ũ, h²) family is asymptotically unconstraining, so the next odd
candidate must carry STRUCTURE, not freedom. The ζ₄-residue route
(`docs/audits/2026-06-28-frakV-descent-zeta4-partner.md`) supplies it:

  ζ₄ acts on the fibre by q ↦ ζ₄·q (λ ↦ λ + iπ/2). The faithful isotypes
  are the ±i eigencomponents = the ODD-q-degree support classes
  (q^k with k ≡ 1, 3 mod 4); non-faithful (eigenvalue ±1) = even degrees.
  The descent audit's constraint: the odd/Q_β kernel must be ζ₄-FAITHFUL —
  supported entirely on the ±i isotypes.

Formalize-first reduction (this is the pruning step, done BEFORE the
solve): a Laurent series that is (i) bar-odd (antisymmetric under
q ↔ q⁻¹) and (ii) odd-degree supported is exactly a ℤ-combination of
{q^(2j+1) − q^−(2j+1)}, and sinh((2j+1)λ) is an odd Chebyshev polynomial
in sinh λ = h/2 — so the ζ₄-faithful bar-odd one-variable family is

    O  =  Σ_j c_j · h^(2j+1)          (h = q − q⁻¹, NO ladder variable)

ũ is EXCLUDED by faithfulness (ũ = q·b·ℏ_q² has mixed even/odd degree
support — the refuted 08ds form violated the ζ₄ constraint through ũ).

DOF accounting (honest): at ORD = 17 the family has 9 unknowns
(c_0…c_8, read off triangularly at the odd s-orders 1,3,…,17) against 17
constraint orders — the 8 even orders are pure over-determination:
**margin 8**, a strong test in the same class as the E(ũ) margin-9 result,
NOT consistency-at-margin.

All exact (ℚ(√3) scalars); scope (a) on any failure; audit-only; no
wiring; the c_k owner-gates and the Δ_λ no-seventh-ansatz rule are not
touched (nothing here is fitted to experiment — the target is the exact
net-route bar-odd series itself).

Emits `qbeta-zeta4-faithful-odd.witness.json`.

Usage:
    python3 -u qbeta/qbeta_zeta4_faithful_odd_probe.py 2>&1 | tee /tmp/zeta4_odd.log
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

import qbeta_ck_sseries_exact_rational as core  # noqa: E402
core.ORD = 17
ORD = core.ORD
from qbeta_ck_sseries_exact_rational import (  # noqa: E402
    q, simp, ser_add, ser_mul, ser_scale, ser_inv, ser_sqrt,
    ser_log1, ser_cos0, rat_series, load_net_symbolic,
)

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def ser_compose(a, phi):
    assert phi[0] == 0
    out = [sp.Integer(0)] * (ORD + 1)
    out[0] = a[ORD]
    for n in range(ORD - 1, -1, -1):
        out = ser_mul(out, phi)
        out[0] = simp(out[0] + a[n])
    return out


def odd_h_match(f, h_ser, jmax):
    """Triangular read-off of f ≈ Σ_{j≤jmax} c_j·h^(2j+1) + full residuals.

    h = O(s) with unit (nonzero) leading coefficient, so c_j is determined
    at s-order 2j+1 after subtracting lower rungs; every other order is a
    pure constraint. Returns (c, resid, model)."""
    c = {}
    model = [sp.Integer(0)] * (ORD + 1)
    hpow = {1: list(h_ser)}
    h2 = ser_mul(h_ser, h_ser)
    for j in range(1, jmax + 1):
        hpow[2 * j + 1] = ser_mul(hpow[2 * j - 1], h2)
    lead = {k: hpow[k][k] for k in hpow}          # leading s^k coefficient
    for j in range(0, jmax + 1):
        k = 2 * j + 1
        cj = simp((f[k] - model[k]) / lead[k])
        c[j] = cj
        model = ser_add(model, ser_scale(cj, hpow[k]))
    resid = {n: simp(f[n] - model[n]) for n in range(1, ORD + 1)}
    return c, resid, model


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(f" 0zr0 — ORD={ORD} ζ₄-faithful odd sector: O ∈ h·ℚ(√3)[[h²]] ?")
    print("=" * 78)

    # ---- identical net-route construction to the 08ds probe ---------------
    dnet = sp.simplify(load_net_symbolic("neutron") - load_net_symbolic("proton"))
    dnet_reg = sp.cancel(dnet / (q - 1))
    q0 = mp.mpf(json.load(open(_pb.witness_path(
        "q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"])
    sgn = int(mp.sign(sp.lambdify(q, dnet, "mpmath")(q0)))
    Qb = rat_series(sp.Integer(sgn) * dnet_reg / q)
    QA = rat_series((2 * q + 1 - q**2) * (q + 1) / (2 * q**3))
    hbar2 = rat_series(((q - 1) / q) ** 2)
    b_ser = ser_mul(ser_sqrt(rat_series(q**4 + q**2 + 1)),
                    ser_inv(rat_series(q**2 + 1)))
    u_ser = ser_mul(rat_series(q), ser_mul(b_ser, hbar2))
    sqrt_q = ser_sqrt(rat_series(q))
    z_ser = ser_mul(sqrt_q, ser_inv(rat_series(q + 1)))
    h_ser = rat_series(q - 1 / q)
    zm1 = list(z_ser); zm1[0] = simp(zm1[0] - 1)
    alpha = ser_add(ser_scale(sp.Rational(1, 2), ser_mul(zm1, h_ser)),
                    ser_scale(sp.Rational(-1, 2), u_ser))
    R = ser_mul(Qb, ser_inv(ser_mul(QA, ser_cos0(alpha))))
    logR = ser_log1(R)
    print(f"  series built ({time.monotonic()-t0:.0f}s)")

    phi = [sp.Integer(0)] + [sp.Integer(-1) ** n for n in range(1, ORD + 1)]
    logR_bar = ser_compose(logR, phi)
    O = [simp((x - y) / 2) for x, y in zip(logR, logR_bar)]

    # ---- the ζ₄-faithful one-variable solve --------------------------------
    JMAX = (ORD - 1) // 2                        # h^(2j+1) ≤ s^17 → j ≤ 8
    c, resid, _ = odd_h_match(O, h_ser, JMAX)
    nonzero = {n: r for n, r in resid.items() if sp.simplify(r) != 0}
    first_bad = min(nonzero) if nonzero else None
    n_unknowns = JMAX + 1
    margin = ORD - n_unknowns
    print(f"  rungs c_0..c_{JMAX}: " +
          ", ".join(f"c_{j}={sp.nsimplify(v)}" for j, v in list(c.items())[:4])
          + " …")
    print(f"  unknowns={n_unknowns}  constraint orders={ORD}  margin={margin}")
    if first_bad is None:
        print(f"  ζ₄-FAITHFUL FORM HOLDS through s^{ORD} "
              f"(all {margin} over-determining orders exactly zero)")
    else:
        print(f"  FAILS at s^{first_bad}: residual = "
              f"{sp.nsimplify(nonzero[first_bad])} "
              f"({len(nonzero)} nonzero residual orders)")
        print("  verdict: the pure ζ₄-faithful one-variable form h·D(h²), "
              "alone, does not absorb the odd sector — scope (a).")

    w = WitnessBuilder("qbeta-zeta4-faithful-odd", engine="sympy")
    w.set_description(
        "Bean 0zr0: exact ORD-17 test of the ζ₄-faithfulness constraint on "
        "the bar-odd (Q_beta) net-route sector — O in h·Q(sqrt3)[[h^2]] "
        "(odd-q-degree support, the ±i isotypes; no ladder variable).")
    w.add_parameter("ORD", ORD)
    w.add_parameter("family", "O = sum_j c_j h^(2j+1), h = q - 1/q")
    w.add_parameter("n_unknowns", n_unknowns)
    w.add_parameter("margin", margin)
    w.add_parameter("derivation",
                    "zeta4-faithful = odd-q-degree support; bar-odd + "
                    "odd-degree = odd Chebyshev in h (formalize-first "
                    "reduction, audit 2026-06-28-frakV-descent-zeta4-partner)")
    w.add_data("rungs", {f"c_{j}": str(sp.nsimplify(v)) for j, v in c.items()})
    w.add_data("residuals_nonzero",
               {str(n): str(sp.nsimplify(r)) for n, r in nonzero.items()})
    w.add_data("first_nonzero_order", first_bad)
    w.add_data("verdict",
               ("HOLDS: odd sector IS the zeta4-faithful h-ladder through "
                f"s^{ORD} (margin {margin})") if first_bad is None else
               ("REFUTED at s^%d — scope (a): the pure one-variable "
                "zeta4-faithful form h·D(h^2), alone as-is, does not absorb "
                "the odd sector; faithfulness of multi-variable faithful "
                "combinations is NOT excluded (no invariant against them)"
                % first_bad))
    w.add_assertion(
        name="triangular_readoff_consistent",
        computed=float(len(c)), expected=float(n_unknowns), tolerance=0.0,
        unit="rungs read off at odd orders (compute validity)",
        source="exact Q(sqrt3)[[s]] triangular solve.")
    w.set_audit_only("docs/audits/2026-07-03-qbar-norm-repitch-assessment.md")
    out = w.save()
    print(f"\nWitness: {out}  ({time.monotonic()-t0:.0f}s total)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
