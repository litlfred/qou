#!/usr/bin/env python3
"""body_number_expansion_classical_floor_probe.py — the body-number expansion is NOT ordered in ε = q − 1.

Bean `qou-olxi`, attack option 1 (owner: "do as suggested", 2026-09-15). The question: does the
many-body (body-number) expansion of the binding carry a power counting in the deformation
parameter `ε = q − 1` — the ingredient a Weinberg-style effective-field-theory ordering over
body number would need, and the theorem "tower-level `m` contributions have `ε`-valuation ≥ `m`"
that the chat assessment proposed to prove?

Answer: **no, and the obstruction is an identity, not a measurement.** Every interface (bond)
factor of the multiplicative assembly is `z_D + d_kind` (`bond_factors_are_z_plus_d_probe`),
and at the classical point `z_D(1) = 1³/(1² + 1) = 1/2` while `d_kind(0) = 0` for all three
kinds. So every bond factor is `1/2` at `q = 1`, its Mayer variable `g = f − 1` is `−1/2`, and
the connected three-body cumulant of the assembly, `b₃ = −φᵀ₃(g, g, g)`
(`QOU.MassTheory.b3corpus_eq_neg_phi3`), is `−5/8 ≠ 0` at the classical point. Its
`ε`-valuation is `0`. Same for `b₄`. There is no power counting in `ε` over body number.

What IS ordered in the corpus is the jet tower: `T(ρ) = Σ_{n ≥ 1} ℏ_q^{2n} Δ^{(n)}(ρ)` with
geometric remainder ratio `q⁻²` (`rem:brane-tower-q-laplacian-decay-interpretation`). The
framework's expansion parameter counts jet level, not body number. And the corpus already knew
the body-number floor in another guise: the `c₀` "classical floor" of the Hecke trace
difference `Δ = tr(free) − tr(atom)` is `2^{−A} − 2^{1−2A} ≠ 0` at `ε = 0`
(`c2-diagonal-insertion-expansion-probe`, assertion 0).

Everything exact is in `Fraction`; the two `q₀`-dependent contrasts (the jet remainder ratio
and the bond factors at the physical point) are `mpmath` at the PROTON pin. Lean twin:
`QOU/MassTheory/BondFactorClassicalFloor.lean` (`b3corpus_classical`, sorry-free).

Scope: this is a scope-(b) exclusion of the ORDERING IN ε — the invariant is `z_D(1) = 1/2`.
It does not exclude an ordering in some other parameter.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

import mpmath as mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.mp.dps = 70


# ---------------------------------------------------------------- exact part
def zD_series(order: int = 2) -> list[Fr]:
    """ε-series of z_D(1+ε) = (1+ε)³ / ((1+ε)² + 1), by exact long division."""
    num = [Fr(1), Fr(3), Fr(3), Fr(1)]          # (1+ε)^3
    den = [Fr(2), Fr(2), Fr(1)]                 # (1+ε)^2 + 1
    out: list[Fr] = []
    rem = num[:] + [Fr(0)] * (order + 1)
    for k in range(order + 1):
        c = rem[k] / den[0]
        out.append(c)
        for j, dj in enumerate(den):
            rem[k + j] -= c * dj
    return out


def zD_exact(q: Fr) -> Fr:
    return q**3 / (q**2 + 1)


# d_kind series, as recorded by bond_factors_are_z_plus_d_probe (z + d columns minus z):
D_KIND = {
    "pp (sigma)": [Fr(0), Fr(0), Fr(0)],
    "pn (averaged_weighted)": [Fr(0), Fr(-1), Fr(1, 2)],
    "nn (sigma_inv)": [Fr(0), Fr(-2), Fr(1)],
}
Z_PLUS_D_RECORDED = {
    "pp (sigma)": [Fr(1, 2), Fr(1), Fr(1, 4)],
    "pn (averaged_weighted)": [Fr(1, 2), Fr(0), Fr(3, 4)],
    "nn (sigma_inv)": [Fr(1, 2), Fr(-1), Fr(5, 4)],
}


def mayer(f: Fr) -> Fr:
    return f - 1


def phi3(g12: Fr, g13: Fr, g23: Fr) -> Fr:
    return g12 * g13 * g23 + g12 * g13 + g12 * g23 + g13 * g23


def b3corpus(f12: Fr, f13: Fr, f23: Fr) -> Fr:
    Z3 = f12 * f13 * f23
    W = lambda z: 1 - z  # noqa: E731
    return W(Z3) - W(f12) - W(f13) - W(f23)


def phi4_uniform(g: Fr) -> Fr:
    """Fourth Ursell function on uniform bonds: sum over the 38 connected spanning
    subgraphs of K₄, counted by edge number: 16 trees·g³ + 15·g⁴ + 6·g⁵ + 1·g⁶."""
    return 16 * g**3 + 15 * g**4 + 6 * g**5 + g**6


def valuation(series: list[Fr]) -> int | None:
    for k, c in enumerate(series):
        if c != 0:
            return k
    return None


def main() -> None:
    zs = zD_series(2)
    assert zs == [Fr(1, 2), Fr(1), Fr(1, 4)], zs
    checks = []

    # 1. z_D(1) = 1/2, and the recorded z+d columns are z_D + d exactly
    checks.append(("zD_classical_is_one_half", zD_exact(Fr(1)) == Fr(1, 2), "z_D(1) = 1/2"))
    for kind, zd in Z_PLUS_D_RECORDED.items():
        recon = [zs[i] + D_KIND[kind][i] for i in range(3)]
        checks.append((f"z_plus_d_reconstructs_{kind.split()[0]}", recon == zd,
                       f"{kind}: z+d = {[str(x) for x in recon]}"))

    # 2. every bond factor is 1/2 at ε = 0
    for kind in D_KIND:
        f0 = zs[0] + D_KIND[kind][0]
        checks.append((f"bond_factor_classical_{kind.split()[0]}", f0 == Fr(1, 2), f"{kind}: f(ε=0) = {f0}"))

    # 3. the cumulants at the classical point
    g0 = mayer(Fr(1, 2))
    b3 = b3corpus(Fr(1, 2), Fr(1, 2), Fr(1, 2))
    checks.append(("b3_classical_is_minus_five_eighths", b3 == Fr(-5, 8), f"b3(1/2,1/2,1/2) = {b3}"))
    checks.append(("b3_equals_minus_phi3", b3 == -phi3(g0, g0, g0), f"-phi3 = {-phi3(g0, g0, g0)}"))
    b4 = -phi4_uniform(g0)
    checks.append(("b4_classical_nonzero", b4 != 0, f"-phi4(-1/2) = {b4}"))

    # 4. ε-valuation of b3 along the mixed pp/pn/nn chain (the A = 3 words use two interfaces;
    #    a triangle needs three — take the three kinds once each, series to order 2)
    def series_mul(a, b):
        out = [Fr(0)] * 3
        for i in range(3):
            for j in range(3 - i):
                out[i + j] += a[i] * b[j]
        return out
    def series_add(*ss):
        return [sum(s[i] for s in ss) for i in range(3)]
    gs = {k: [zs[i] + D_KIND[k][i] - (1 if i == 0 else 0) for i in range(3)] for k in D_KIND}
    g12, g13, g23 = gs["pp (sigma)"], gs["pn (averaged_weighted)"], gs["nn (sigma_inv)"]
    phi3_series = series_add(series_mul(series_mul(g12, g13), g23), series_mul(g12, g13),
                             series_mul(g12, g23), series_mul(g13, g23))
    b3_series = [-c for c in phi3_series]
    v = valuation(b3_series)
    checks.append(("b3_epsilon_valuation_is_zero", v == 0,
                   f"b3(ε) = {[str(c) for c in b3_series]} + O(ε³); valuation {v}"))

    # 5. the classical floor the corpus already carries: c0 = 2^-A - 2^(1-2A) ≠ 0
    floors = {A: Fr(1, 2**A) - Fr(2, 4**A) for A in (2, 3, 4)}
    checks.append(("c0_classical_floor_nonzero_A234", all(x != 0 for x in floors.values()),
                   f"c0(A) = {dict((A, str(x)) for A, x in floors.items())}"))
    checks.append(("c0_A2_matches_c2_witness_a0", floors[2] == Fr(1, 8), "c2 witness rows a0 = 1/8 at A = 2"))

    # ------------------------------------------------------------ q0 contrasts (proton pin)
    q0 = Q_MP
    jet_ratio = q0 ** -2
    checks.append(("jet_tower_remainder_ratio_below_one", jet_ratio < 1,
                   f"q0^-2 = {mp.nstr(jet_ratio, 20)} (the jet tower IS geometrically ordered)"))
    eps0 = q0 - 1
    zD0 = q0**3 / (q0**2 + 1)
    bond_at_q0 = {k: zD0 + D_KIND[k][1] * eps0 + D_KIND[k][2] * eps0**2 for k in D_KIND}
    # the Lean twin's statement at the physical point: no bond factor is near 1, all are near 1/2
    checks.append(("bond_factors_at_q0_near_one_half", all(abs(f - mp.mpf(1) / 2) < mp.mpf("0.2") for f in bond_at_q0.values()),
                   "; ".join(f"{k.split()[0]}: {mp.nstr(f, 12)}" for k, f in bond_at_q0.items())))

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, src in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}")
    print(f"{passed}/{len(checks)} passed")

    w = WitnessBuilder("body-number-expansion-classical-floor", engine="mpmath")
    for name, ok, src in checks:
        w.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = w.save(
        {
            "q0Anchor": "proton",
            "q0_anchor_reason": (
                "The exact part is anchor-free (Fractions at q = 1). The two q0 contrasts "
                "(jet remainder ratio, bond factors at the physical point) use the proton pin, "
                "the 2026-08-07 default."
            ),
            "description": (
                "The body-number (cluster) expansion of the multiplicative binding assembly has a "
                "classical floor: every bond factor is z_D(1) = 1/2 at q = 1, so the connected "
                "three-body cumulant b3 = -phi3 is -5/8 at epsilon = 0 and has epsilon-valuation 0. "
                "No power counting in epsilon = q - 1 orders the body-number expansion; the ordered "
                "expansion of the framework is the jet tower (ratio q^-2). Scope (b) for the ordering "
                "in epsilon; invariant z_D(1) = 1/2."
            ),
            "data": {
                "zD_series_eps": [str(c) for c in zs],
                "d_kind_series_eps": {k: [str(c) for c in v] for k, v in D_KIND.items()},
                "mayer_classical": str(g0),
                "b3_classical": str(b3),
                "b4_classical_uniform": str(b4),
                "b3_series_eps_mixed_chain": [str(c) for c in b3_series],
                "b3_epsilon_valuation": v,
                "c0_classical_floor": {str(A): str(x) for A, x in floors.items()},
                "q0_proton": mp.nstr(q0, 60),
                "jet_remainder_ratio_q0_inv_sq": mp.nstr(jet_ratio, 60),
                "bond_factors_at_q0": {k: mp.nstr(f, 60) for k, f in bond_at_q0.items()},
            },
            "lean_twin": "QOU.MassTheory.b3corpus_classical (BondFactorClassicalFloor.lean)",
            "bean": "qou-olxi",
        }
    )
    print("witness:", out)
    if not all(ok for _, ok, _ in checks):
        sys.exit(1)


if __name__ == "__main__":
    main()
