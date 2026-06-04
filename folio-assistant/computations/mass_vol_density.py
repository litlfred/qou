#!/usr/bin/env python3
# polynomial_q_not_applicable: archimedean mass/binding assembly + hyperbolic parity.
"""Mass = Vol × Density — the proper-definition replacement for Geom_full.

Exposes the canonical mass formula as the explicit product of its two proper
factors, plus the hyperbolic (sinh/cosh) structure that makes the
proton/neutron (and mirror-binding) even/odd parity a *structural identity*
rather than an order-by-order check.

## M = Vol × Density

    m(K) = m_e · Vol(K) · ρ(q) / ℏ_q²

- ``Vol(K)`` — hyperbolic volume of the complement, an INPUT constant
  (Vol(𝓑₃) = 8·G, Adams 1985 / SnapPy). NOT derived from the trace — the
  Kashaev volume conjecture is deliberately out of scope.
- ``ρ(q)`` — the algebraic Hecke linking-weight density
  ``(3q²+4+3q⁻²)/4 = 5/2 + 3h²/4`` (= ``_li_2_q_util.linking_weight_family_a``).
- ``ℏ_q = (q−1)/q`` — substrate Planck quantum.

``geom_full_vd(vol_K, q)`` is bit-identical to the legacy
``_li_2_q_util.geom_full_borromean(q)`` for the Borromean nucleon — this
module is the Stage-0/1 foundation of the Geom_full → Vol·Density purge
(see ``docs/workplans/2026-06-04-mass-vol-density-stokes-delta-formalization.md``).

## Hyperbolic parity (q = e^η, η = log q)

    h     = q − q⁻¹ = 2 sinh η   (ODD)
    [2]_q = q + q⁻¹ = 2 cosh η   (EVEN, = 2.0108969 at q₀ — the recurring Hecke weight)

A mirror pair written as a hyperbolic rotation by a rapidity θ,
``O_± = O₀·e^{∓θ}``, splits cleanly:

    O_avg  = O₀ cosh θ   (EVEN — all δ²,δ⁴ … corrections; needs the absolute scale)
    ΔO/2   = O₀ sinh θ   (ODD  — all δ¹,δ³ … corrections; the antisymmetric channel)

- **Mass:** the production ``m_{p,n} = m_avg·(1∓δ/2)`` is the O(δ) truncation
  of ``e^{∓δ/2}`` (θ = δ/2 at leading order).
- **Binding:** the SAME structure applies to a mirror binding pair (³H, ³He):
  ``ΔB/2 = B₀ sinh θ_B`` is the ODD channel — the mirror **difference**,
  computable **prior to** the even/cosh absolute normalization. This is the
  M_λ-gate sidestep: the difference (sinh) is the non-circular channel
  (cf. the eigenphase-difference closing the ³H−³He mirror to ~2% with 0
  free params), while the absolute average (cosh) carries the gated scale.

A δ² (even) correction is parity-ALLOWED on the average, parity-FORBIDDEN on
the difference — the formal statement is in
``QOU/Mass/MassVolDensity.lean`` (``mass_avg_even`` / ``mass_split_odd``).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _li_2_q_util import linking_weight_family_a, geom_full_borromean  # noqa: E402


def vol_borromean() -> mp.mpf:
    """Adams-1985 hyperbolic volume of 𝓑₃ = 8·G (INPUT, not Kashaev).
    Computed lazily at the *current* mpmath precision (a module-level
    constant would capture the import-time dps and silently lose precision)."""
    return 8 * mp.catalan


# ── M = Vol × Density ────────────────────────────────────────────────
def hbar_q(q: mp.mpf) -> mp.mpf:
    """Substrate Planck quantum ℏ_q = (q−1)/q."""
    return (q - 1) / q


def density_borromean(q: mp.mpf, q_inv: mp.mpf | None = None) -> mp.mpf:
    """Algebraic Hecke linking-weight density ρ(q) = (3q²+4+3q⁻²)/4
    = 5/2 + 3h²/4. Re-exports the canonical `linking_weight_family_a`."""
    return linking_weight_family_a(q, q_inv)


def geom_full_vd(vol_K: mp.mpf, q: mp.mpf, density: mp.mpf | None = None) -> mp.mpf:
    """Geom_full as the explicit product Vol(K)·ρ(q)/ℏ_q² (the purge target).
    Defaults `density` to the Borromean ρ(q); pass a per-knot density for
    other knots. Bit-identical to `geom_full_borromean(q)` for K = 𝓑₃."""
    rho = density_borromean(q) if density is None else density
    return vol_K * rho / hbar_q(q) ** 2


def mass_vol_density(m_e: mp.mpf, vol_K: mp.mpf, q: mp.mpf,
                     density: mp.mpf | None = None) -> mp.mpf:
    """m(K) = m_e · Vol(K) · ρ(q) / ℏ_q² — the canonical mass, proper form."""
    return m_e * geom_full_vd(vol_K, q, density)


# ── Hyperbolic structure (q = e^η) ───────────────────────────────────
def eta(q: mp.mpf) -> mp.mpf:
    """Rapidity η = log q."""
    return mp.log(q)


def h_from_rapidity(q: mp.mpf) -> mp.mpf:
    """h = q − q⁻¹ = 2 sinh(log q) (ODD in η)."""
    return 2 * mp.sinh(eta(q))


def bracket2_from_rapidity(q: mp.mpf) -> mp.mpf:
    """[2]_q = q + q⁻¹ = 2 cosh(log q) (EVEN in η). = 2.0108969 at q₀."""
    return 2 * mp.cosh(eta(q))


# ── Hyperbolic pair O_± = O₀·e^{∓θ} (mass OR binding) ─────────────────
def hyperbolic_pair(O0: mp.mpf, theta: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """(O_minus, O_plus) = (O₀·e^{−θ}, O₀·e^{+θ})."""
    return O0 * mp.e ** (-theta), O0 * mp.e ** theta


def pair_average(O0: mp.mpf, theta: mp.mpf) -> mp.mpf:
    """O_avg = O₀ cosh θ — the EVEN channel (absolute scale, M_λ-gated)."""
    return O0 * mp.cosh(theta)


def pair_half_difference(O0: mp.mpf, theta: mp.mpf) -> mp.mpf:
    """ΔO/2 = O₀ sinh θ — the ODD channel (the antisymmetric difference,
    computable prior to the absolute normalization)."""
    return O0 * mp.sinh(theta)


def mirror_binding_difference(B0: mp.mpf, theta_B: mp.mpf) -> mp.mpf:
    """Mirror-pair binding difference ΔB = 2·B₀·sinh θ_B — the ODD/sinh
    channel. This is the M_λ-gate sidestep: the *difference* of a mirror
    pair (e.g. ³H/³He) lives in the odd channel and does not require the
    even/cosh absolute mass scale that the per-block M_λ gate blocks."""
    return 2 * pair_half_difference(B0, theta_B)


def _emit_witness() -> None:
    """Emit the cross-check witness asserting the equivalence + parity."""
    try:
        from witness_base import WitnessBuilder
    except Exception as e:  # noqa: BLE001
        print(f"(witness skipped: {e!r})")
        return
    from q_parameter import Q_50_DIGIT_STR as Qs
    q = mp.mpf(Qs)
    eq = abs(geom_full_borromean(q) - geom_full_vd(vol_borromean(), q))
    h_id = abs((q - 1 / q) - h_from_rapidity(q))
    b2_id = abs((q + 1 / q) - bracket2_from_rapidity(q))
    O0, th = mp.mpf("938.9"), mp.mpf("0.01")
    mm, pp = hyperbolic_pair(O0, th)
    avg_id = abs((mm + pp) / 2 - pair_average(O0, th))
    diff_id = abs((pp - mm) / 2 - pair_half_difference(O0, th))
    parity_even = abs(pair_average(O0, -th) - pair_average(O0, th))
    parity_odd = abs(pair_half_difference(O0, -th) + pair_half_difference(O0, th))
    tol = mp.mpf("1e-40")
    w = WitnessBuilder("mass-vol-density", engine="mpmath")
    w.set_audit_only("docs/workplans/2026-06-04-mass-vol-density-stokes-delta-formalization.md")
    w.add_parameter("q_0", Qs)
    w.add_data("bracket_2_q_at_q0", mp.nstr(bracket2_from_rapidity(q), 16))
    for name, val in [
        ("geom_full_equiv_vol_density", eq),
        ("h_eq_2sinh_log_q", h_id),
        ("bracket2_eq_2cosh_log_q", b2_id),
        ("pair_average_eq_cosh", avg_id),
        ("pair_half_diff_eq_sinh", diff_id),
        ("parity_average_even", parity_even),
        ("parity_difference_odd", parity_odd),
    ]:
        w.add_assertion(name, computed=1 if val < tol else 0, expected=1,
                        source=f"{name}: |Δ| = {mp.nstr(val, 4)} < {mp.nstr(tol, 1)}")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = 50
    from q_parameter import Q_50_DIGIT_STR as Qs
    q = mp.mpf(Qs)
    print("Mass = Vol × Density — wired-up compute")
    print(f"  [2]_q = 2cosh(log q₀) = {mp.nstr(bracket2_from_rapidity(q), 12)} (recurring Hecke weight)")
    print(f"  geom_full ≡ Vol·ρ/ℏ²: |Δ| = "
          f"{mp.nstr(abs(geom_full_borromean(q) - geom_full_vd(vol_borromean(), q)), 3)}")
    _emit_witness()
