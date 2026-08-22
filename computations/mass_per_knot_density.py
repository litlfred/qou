#!/usr/bin/env python3
# polynomial_q_not_applicable: archimedean mass/binding assembly + hyperbolic parity.
"""Mass = Vol × Density — the proper-definition replacement for PerKnotDensity.

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

``per_knot_density_vd(vol_K, q)`` is bit-identical to the legacy
``_li_2_q_util.per_knot_density_borromean(q)`` for the Borromean nucleon — this
module is the Stage-0/1 foundation of the PerKnotDensity → Vol·Density purge
(see ``docs/workplans/2026-06-04-mass-per-knot-density-stokes-delta-formalization.md``).

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
``QOU/Mass/MassPerKnotDensity.lean`` (``mass_avg_even`` / ``mass_split_odd``).
"""
from __future__ import annotations

import functools
import json
import sys
import warnings
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _li_2_q_util import (  # noqa: E402
    borromean_markov_trace_h2,
    per_knot_density_borromean,
    per_knot_density_per_block,
)


@functools.lru_cache(maxsize=1)
def _load_tr_M_proton_at_q0() -> "mp.mpf":
    """Load the canonical H₃ proton Markov trace `tr_M(proton)` at q₀ from
    the chi-cache witness. Single source of the file/key/precision
    convention so the witness-data block and the human-readable print
    cannot drift. Cached (maxsize=1) — the cache file is fixed-precision,
    so repeated calls in one run reuse the parse. Returns an mpmath mpf."""
    d = json.loads((HERE / "chi-proton-h3-at-q0-50dps.witness.json").read_text())
    return mp.mpf(d["tr_M_at_q0"])


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
    """Per-knot Hecke density (true Markov trace) for the Borromean rings."""
    return borromean_markov_trace_h2(q, q_inv)


#: Preferred alias for the global production density scalar (``ρ_global``).
#: Non-breaking synonym for ``density_borromean`` — use whichever reads
#: clearer at the call site; the two are identical.
density_global = density_borromean


def density_per_block(tr_M_K: mp.mpf) -> mp.mpf:
    """PER-BLOCK (paper-canonical, SU(2)-selective) density
    ρ_pb(K) = tr_M(K, q) = Σ_λ y_λ χ^λ(β_K).

    The M=Vol×Density density factor in its paper-faithful, per-knot,
    per-Wedderburn-block form (`prop:hoefsmit-scattering-pipeline` Stage 4):
    the Markov trace over the partitions of the KNOT'S OWN strand count
    (H₃ for the 3-strand Borromean baryons). Pass to `per_knot_density_vd` /
    `mass_per_knot_density` as the `density` argument — i.e.
    ``per_knot_density_vd(vol_K, q, density=density_per_block(tr_M_K))`` is
    bit-identical to `_li_2_q_util.per_knot_density_per_block(vol_K, tr_M_K, q)`.

    This is the SU(2)_q density: tr_M = Σ_λ y_λ χ^λ ranges over the
    Wedderburn blocks (Young diagrams λ), so it sees the per-block
    structure that the global scalar `density_borromean` collapses.

    ⚠ The two readings are NOT interchangeable: at q₀ the per-block H₃
    trace tr_M(proton) ≈ 1.0653 differs from the global H₄ scalar
    ≈ 2.5328 by ≈2.378× (`compare_density_readings`).

    As ABSOLUTE MASS both readings are DEPRECATED (2026-06-24 ruling):
    per-block taken literally gives m_p ≈ 406 MeV (−56.7%), and the global
    scalar ≈ 966 MeV (+2.96%) — the latter only by landing near the
    CODATA-implied fit λ_A ≈ 2.46 on the (different) H₄ index set. The
    canonical absolute mass is the muon-anchored
    m_p = 2·(m_μ·F_Bor − 6·m_e) ≈ 938.27 MeV via `canonical_mass.py`.
    The per-block reading remains valid for BINDING ratios, where the
    density scale cancels. The
    reconciliation is the OPEN per-block-vs-global question, gated on the
    per-knot hyperbolic Vol (#1762/#1816) — this helper EXPOSES both
    readings, it does NOT silently swap production. See
    `docs/audits/2026-06-04-u1-su2-so3-symmetry-loss-audit.md`."""
    return tr_M_K


def compare_density_readings(
    q: mp.mpf, tr_M_K: mp.mpf, q_inv: mp.mpf | None = None
) -> dict:
    """Side-by-side global vs per-block density at q (the SU(2)-loss gate).

    Returns the global scalar `density_borromean(q)`, the per-block
    `density_per_block(tr_M_K)`, their ratio (global/per-block), and the
    discipline-gate verdict (PASS iff |ratio−1| < 1e-6, i.e. the two
    readings coincide). For the proton at q₀ the gate is RED (ratio
    ≈ 2.378), which is the verified SU(2) symmetry loss: the global
    scalar replaces the per-block Markov trace.

    NO fudge is applied — the discrepancy is reported, not tuned away."""
    rho_global = density_borromean(q, q_inv)
    rho_pb = density_per_block(tr_M_K)
    if rho_pb == 0:
        # A vanishing per-block trace is not a physical density; report an
        # undefined ratio rather than dividing by zero (gate cannot pass).
        return {
            "density_global": rho_global,
            "density_per_block": rho_pb,
            "ratio_global_over_per_block": mp.inf,
            "gate_pass": False,
            "verdict": "RED — per-block density is 0 (undefined ratio)",
        }
    ratio = rho_global / rho_pb
    gate_pass = abs(ratio - 1) < mp.mpf("1e-6")
    return {
        "density_global": rho_global,
        "density_per_block": rho_pb,
        "ratio_global_over_per_block": ratio,
        "gate_pass": gate_pass,
        "verdict": "PASS" if gate_pass
        else "RED — global SU(2)-blind scalar ≠ per-block Markov trace",
    }


def per_knot_density_vd(vol_K: mp.mpf, q: mp.mpf, density: mp.mpf | None = None) -> mp.mpf:
    """PerKnotDensity as the explicit product Vol(K)·ρ(q)/ℏ_q² (the purge target).
    Defaults `density` to the Borromean ρ(q); pass a per-knot density for
    other knots. Bit-identical to `per_knot_density_borromean(q)` for K = 𝓑₃."""
    rho = density_borromean(q) if density is None else density
    return vol_K * rho / hbar_q(q) ** 2


def mass_per_knot_density(m_e: mp.mpf, vol_K: mp.mpf, q: mp.mpf,
                     density: mp.mpf | None = None) -> mp.mpf:
    """m(K) = m_e · Vol(K) · ρ(q) / ℏ_q².

    ⚠ DEPRECATED FOR ABSOLUTE NUCLEON/ATOM MASS (owner ruling 2026-06-24).
    This applies 1/ℏ_q² (= q²·c_q²) to the *Borromean* volume, which is NOT
    the canonical nucleon mass: with ρ=λ_A it gives m_p≈966 (+2.96%, a fit);
    with ρ=tr_M it gives m_p≈406 (−57%). The CANONICAL nucleon mass is the
    muon-anchored Hecke energy (substrate-identity):

        m_p = dim V_{(2,1)}·(m_μ·F_Bor − |S_3|·m_e) = 2·(m_μ·F_Bor − 6·m_e),
        m_μ = m_e·Vol(4₁)/ℏ_q²,  F_Bor = |tr_M(β_Bor)|·[3]_q!/q³   → 938.27 MeV

    Use `m_p_substrate_identity_50dps` / the `m-p-substrate-identity-50dps`
    witness. See docs/canonical-mass-formula-guardrail.md and
    docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md.
    (Still valid for non-mass diagnostics / the muon anchor where Vol=Vol(4₁).)"""
    warnings.warn(
        "mass_per_knot_density (m_e·Vol·ρ/ℏ_q²) is NOT the canonical absolute "
        "nucleon mass — use the muon-anchored F_Bor substrate-identity "
        "(m_p_substrate_identity_50dps). See "
        "docs/canonical-mass-formula-guardrail.md.",
        DeprecationWarning,
        stacklevel=2,
    )
    return m_e * per_knot_density_vd(vol_K, q, density)


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
    eq = abs(per_knot_density_borromean(q) - per_knot_density_vd(vol_borromean(), q))
    h_id = abs((q - 1 / q) - h_from_rapidity(q))
    b2_id = abs((q + 1 / q) - bracket2_from_rapidity(q))
    O0, th = mp.mpf("938.9"), mp.mpf("0.01")
    mm, pp = hyperbolic_pair(O0, th)
    avg_id = abs((mm + pp) / 2 - pair_average(O0, th))
    diff_id = abs((pp - mm) / 2 - pair_half_difference(O0, th))
    parity_even = abs(pair_average(O0, -th) - pair_average(O0, th))
    parity_odd = abs(pair_half_difference(O0, -th) + pair_half_difference(O0, th))
    tol = mp.mpf("1e-40")

    # ── SU(2) density loss: global scalar vs per-block Markov trace ────
    # Load the canonical H₃ proton Markov trace from the chi-cache; the
    # per-block density IS this trace. Compare side-by-side with the
    # global linking_weight scalar (the verified ≈2.378× SU(2) loss).
    cmp_pb = None
    skip_reason = None
    try:
        tr_M_proton = _load_tr_M_proton_at_q0()
        cmp_pb = compare_density_readings(q, tr_M_proton)
        # per_knot_density_vd with per-block density ≡ _li_2_q_util.per_knot_density_per_block.
        # Compute Vol(𝓑₃) once (precision-dependent) and reuse for both.
        vol = vol_borromean()
        vd_pb = per_knot_density_vd(vol, q, density=density_per_block(tr_M_proton))
        pb_equiv = abs(vd_pb - per_knot_density_per_block(vol, tr_M_proton, q))
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError) as e:
        # Catch only the expected chi-cache load failures; an explicit skip
        # datum is emitted below so a missing cache cannot silently pass as
        # "no SU(2) loss measured". Unexpected exceptions propagate.
        skip_reason = repr(e)
        print(f"(per-block density comparison skipped: {skip_reason})")
        pb_equiv = None

    w = WitnessBuilder("mass-per-knot-density", engine="mpmath")
    w.set_audit_only("docs/workplans/2026-06-04-mass-per-knot-density-stokes-delta-formalization.md")
    w.add_parameter("q_0", Qs)
    w.add_data("bracket_2_q_at_q0", mp.nstr(bracket2_from_rapidity(q), 16))
    if cmp_pb is not None:
        w.add_data("su2_density_loss", {
            "density_global_H4_scalar": mp.nstr(cmp_pb["density_global"], 16),
            "density_per_block_H3_trM_proton":
                mp.nstr(cmp_pb["density_per_block"], 16),
            "ratio_global_over_per_block":
                mp.nstr(cmp_pb["ratio_global_over_per_block"], 16),
            "gate_verdict": cmp_pb["verdict"],
        })
    else:
        w.add_data("su2_density_loss",
                   {"skipped": True, "reason": skip_reason or "unknown"})
    for name, val in [
        ("per_knot_density_equiv_per_knot_density", eq),
        ("h_eq_2sinh_log_q", h_id),
        ("bracket2_eq_2cosh_log_q", b2_id),
        ("pair_average_eq_cosh", avg_id),
        ("pair_half_diff_eq_sinh", diff_id),
        ("parity_average_even", parity_even),
        ("parity_difference_odd", parity_odd),
    ]:
        w.add_assertion(name, computed=1 if val < tol else 0, expected=1,
                        source=f"{name}: |Δ| = {mp.nstr(val, 4)} < {mp.nstr(tol, 1)}")
    if pb_equiv is not None:
        # per_knot_density_vd(density=per_block) reproduces per_knot_density_per_block exactly.
        w.add_assertion("per_knot_density_vd_per_block_equiv",
                        computed=1 if pb_equiv < tol else 0, expected=1,
                        source=f"per_knot_density_vd(density=tr_M) ≡ per_knot_density_per_block: "
                               f"|Δ| = {mp.nstr(pb_equiv, 4)} < {mp.nstr(tol, 1)}")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = 50
    from q_parameter import Q_50_DIGIT_STR as Qs
    q = mp.mpf(Qs)
    print("Mass = Vol × Density — wired-up compute")
    print(f"  [2]_q = 2cosh(log q₀) = {mp.nstr(bracket2_from_rapidity(q), 12)} (recurring Hecke weight)")
    print(f"  per_knot_density ≡ Vol·ρ/ℏ²: |Δ| = "
          f"{mp.nstr(abs(per_knot_density_borromean(q) - per_knot_density_vd(vol_borromean(), q)), 3)}")
    try:
        _tr = _load_tr_M_proton_at_q0()
        _c = compare_density_readings(q, _tr)
        print(f"  SU(2) density loss: global ρ={mp.nstr(_c['density_global'], 8)} "
              f"vs per-block tr_M(p)={mp.nstr(_c['density_per_block'], 8)} "
              f"→ ratio {mp.nstr(_c['ratio_global_over_per_block'], 6)} [{_c['verdict']}]")
    except Exception as e:  # noqa: BLE001
        print(f"  (SU(2) comparison skipped: {e!r})")
    _emit_witness()
